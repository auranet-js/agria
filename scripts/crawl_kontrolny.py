#!/usr/bin/env python3
"""Crawl kontrolny agria.pl — powtarzalny zamiennik Screaming Froga dla 62 adresów.

Po co: serwis ma kilkadziesiąt stron, a jedyne, czego potrzebujemy po wdrożeniu, to sprawdzić,
czy nie przybyło 404, czy tytuły i opisy są na miejscu, czy schema kart ma `offers` i czy nic
się nie zdublowało. Odpalenie SF wymaga maszyny Janka i eksportu; to robi się z Elary w minutę.

⚠️ **WP Rocket:** `?cb=` po włączeniu cache omija go i pokazuje wersję, której użytkownik nie
dostaje. Dlatego każdy adres pobieramy DWA razy — pierwsze żądanie rozgrzewa cache, mierzymy
drugie. Wynik to stan, który realnie widzi odwiedzający.

Użycie:
    crawl_kontrolny.py [plik-z-adresami] [--json plik.json]

Domyślne źródło adresów: `data/seo/audyt-2026-08-24/urls.txt` (format: `TYP /sciezka/`),
plus adresy kontrolne z crawlu 07.09, które wtedy oddawały 404.
"""
import json
import re
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

BAZA = "https://agria.pl"
UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")

# Adresy, które crawl 07.09 pokazał jako 404 — sprawdzamy je osobno, bo nie ma ich w urls.txt
KONTROLNE = [
    "/polityka-prywatnosci/",
    "/rolnictwo",
    "/kontakt/pawel.bigos@agria.pl",
    "/oferta",
    "/kontakt",
]

# Przybliżona szerokość znaku w pikselach dla kroju SERP-owego (~Arial 20px).
# SF tnie tytuł powyżej 561 px; to oszacowanie, nie pomiar — służy do wskazania kandydatów.
WASKIE = set("iljItf.,;:'!|[]()")
SZEROKIE = set("mMWw@")


def px(tekst):
    return sum(4.5 if z in WASKIE else 13.5 if z in SZEROKIE else 9.2 for z in tekst)


def pobierz(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.geturl(), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:                                    # noqa: BLE001
        return 0, url, f"__blad__ {e}"


def wytnij(wzor, html, grupa=1):
    m = re.search(wzor, html, re.S | re.I)
    return m.group(grupa).strip() if m else None


def zbadaj(sciezka):
    url = BAZA + sciezka
    pobierz(url)                                              # rozgrzewka cache Rocketa
    status, koncowy, html = pobierz(url)
    # Porównanie MUSI być dokładne. Zrównywanie adresu ze slashem i bez maskuje 301
    # z `/oferta` na `/oferta/` i pokazuje je potem jako duplikat tytułu (błąd z 08.09).
    w = {"sciezka": sciezka, "status": status,
         "przekierowanie": None if koncowy == url else koncowy}
    if status != 200 or not html or html.startswith("__blad__"):
        return w
    w["title"] = wytnij(r"<title>(.*?)</title>", html)
    w["meta_desc"] = wytnij(r'<meta name="description" content="([^"]*)"', html)
    w["canonical"] = wytnij(r'<link rel="canonical" href="([^"]*)"', html)
    w["h1"] = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x)).strip()
               for x in re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)]
    w["noindex"] = bool(re.search(r'<meta name="robots"[^>]*noindex', html, re.I))
    w["bajty"] = len(html.encode())
    w["z_cache"] = "WP Rocket" in html[-400:]
    typy = re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"', html)
    w["schema"] = sorted(set(typy))
    w["ma_offers"] = '"offers"' in html
    w["produkt"] = "Product" in typy
    return w


def main():
    argv = sys.argv[1:]
    cel_json = None
    if "--json" in argv:
        i = argv.index("--json")
        cel_json = argv[i + 1] if i + 1 < len(argv) else None
        del argv[i:i + 2]
    pozycyjne = [a for a in argv if not a.startswith("--")]
    zrodlo = Path(pozycyjne[0]) if pozycyjne else Path("data/seo/audyt-2026-08-24/urls.txt")
    sciezki = []
    for linia in zrodlo.read_text(encoding="utf-8").splitlines():
        czesci = linia.split()
        if len(czesci) >= 2:
            sciezki.append(czesci[1])
    sciezki += [s for s in KONTROLNE if s not in sciezki]

    wyniki = [zbadaj(s) for s in sciezki]

    ok = [w for w in wyniki if w["status"] == 200]
    print(f"Zbadano {len(wyniki)} adresów · 200: {len(ok)} · "
          f"przekierowania: {sum(1 for w in wyniki if 300 <= w['status'] < 400)} · "
          f"z cache Rocketa: {sum(1 for w in ok if w.get('z_cache'))}/{len(ok)}")

    czterysta = [w for w in wyniki if w["status"] in (0, 404) or w["status"] >= 400]
    print(f"\n404 i błędy: {len(czterysta)}")
    for w in czterysta:
        print(f"   {w['status']}  {w['sciezka']}")
    if not czterysta:
        print("   (brak)")

    print("\nDuplikaty tytułów:")
    wlasne = [w for w in ok if not w["przekierowanie"] and w.get("title")]
    licz = Counter(w["title"] for w in wlasne)
    dupli = {t: n for t, n in licz.items() if n > 1}
    for t, n in dupli.items():
        print(f"   ×{n}  {t}")
        for w in wlasne:
            if w["title"] == t:
                print(f"        {w['sciezka']}")
    if not dupli:
        print("   (brak)")

    braki = [w for w in ok if not w.get("meta_desc")]
    print(f"\nBrak meta description: {len(braki)}")
    for w in braki:
        print(f"   {w['sciezka']}")
    if not braki:
        print("   (brak)")

    puste_h1 = [w for w in ok if not w.get("h1") or not any(w["h1"])]
    print(f"\nPusty lub brakujący H1: {len(puste_h1)}")
    for w in puste_h1:
        print(f"   {w['sciezka']}")
    if not puste_h1:
        print("   (brak)")

    produkty = [w for w in ok if w.get("produkt")]
    bez_offers = [w for w in produkty if not w.get("ma_offers")]
    print(f"\nKarty produktów: {len(produkty)} · bez `offers` w schemacie: {len(bez_offers)}")
    for w in bez_offers:
        print(f"   {w['sciezka']}")

    dlugie = sorted(((px(w["title"]), w) for w in ok if w.get("title") and px(w["title"]) > 561),
                    key=lambda x: -x[0])
    print(f"\nTytuły prawdopodobnie ucinane w SERP (>561 px, oszacowanie): {len(dlugie)}")
    for szer, w in dlugie:
        print(f"   ~{szer:.0f} px  {len(w['title'])} zn.  {w['sciezka']}")

    noindex = [w for w in ok if w.get("noindex")]
    if noindex:
        print(f"\nnoindex: {len(noindex)}")
        for w in noindex:
            print(f"   {w['sciezka']}")

    if cel_json:
        json.dump(wyniki, open(cel_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"\n→ {cel_json}")


if __name__ == "__main__":
    main()
