#!/usr/bin/env python3
"""Co mają strony z top N wyników organicznych — pod research treści kart (T-136).

Czyta zapisane wyniki `dfs_serp.py` (nic nie kupuje w DataForSEO), pobiera curl-em
strony z top N i szuka elementów: cena, producent/zakład, dokumenty, frakcje, dawka,
FAQ, schemat Product/FAQPage. Wynik to sygnał obecności, nie ocena jakości.

Użycie:
    python3 scripts/serp_elementy.py --top 5 --out data/produkty/pilot/serp-elementy.json \
        --serp data/produkty/dfs/serp-kredy-dolomit-2026-09-10.json "kreda pastewna" "kreda pastewna dla kur"
"""
import argparse, html, json, re, subprocess

UA = "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/128.0 Mobile Safari/537.36"
WZORCE = {
    "cena": r"\d[\d  ]*(?:,\d{2})?\s?zł",
    "producent": r"lhoist|nordkalk|celiny|hochel|trzuskawic|holcim|industria|siarkopol|grankal|kornica|polcalc|morawic|zalesiak",
    "zakład/kopalnia": r"kopalni|zakład\w* (?:produkc|wapien)|złoż",
    "dokumenty": r"atest|karta charakterystyki|karta produktu|certyfikat|deklaracj|świadectw|GMP\+|nr weterynaryjn|numer weterynaryjn",
    "frakcja": r"\d(?:,\d)?\s?[–-]\s?\d(?:,\d)?\s?mm|frakcj",
    "dawka": r"kg\s?/\s?100\s?kg|kg na 100|t\s?/\s?ha|ton\w* na hektar|dawk",
    "gatunki": r"\bkur\b|kury|niosek|nioski|drobi|bydł|krów|krowy|świń|trzod",
    "FAQ (nagłówek)": r"(?:FAQ|najczęściej zadawane|pytania i odpowiedzi|często zadawane)",
    "transport": r"transport|dostaw[ay] |dowóz|dowozi",
}


def pobierz(url):
    r = subprocess.run(["curl", "-sSL", "-A", UA, "--max-time", "25", url], capture_output=True, text=True, errors="replace")
    return r.stdout


def analiza(h):
    schema = set(re.findall(r'"@type"\s*:\s*"(Product|FAQPage|Offer|AggregateOffer|HowTo|Article|BlogPosting)"', h))
    body = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).replace("\xa0", " ")
    wynik = {k: bool(re.search(v, t, re.I)) for k, v in WZORCE.items()}
    wynik["schema"] = sorted(schema)
    wynik["pdf_linki"] = len(set(re.findall(r'href="[^"]+\.pdf', h, re.I)))
    wynik["słowa"] = len(t.split())
    return wynik


ap = argparse.ArgumentParser()
ap.add_argument("frazy", nargs="+")
ap.add_argument("--serp", action="append", required=True, help="plik JSON z dfs_serp.py (można kilka)")
ap.add_argument("--top", type=int, default=5)
ap.add_argument("--out")
a = ap.parse_args()

serpy = {}
for f in a.serp:
    serpy.update(json.load(open(f)))

wyniki = {}
for kw in a.frazy:
    r = serpy.get(kw)
    if not r:
        print(f"### {kw} — brak w podanych plikach SERP"); continue
    org = [it for it in r.get("items") or [] if it["type"] == "organic"][: a.top]
    wyniki[kw] = []
    print("=" * 78, f"\n### {kw}")
    for it in org:
        url = it["url"]
        e = analiza(pobierz(url)) if not url.lower().endswith(".pdf") else {"pdf": True}
        e.update({"abs": it["rank_absolute"], "domena": it.get("domain"), "tytuł": it.get("title"), "url": url})
        wyniki[kw].append(e)
        flagi = ", ".join(k for k in WZORCE if e.get(k)) if "pdf" not in e else "PDF"
        print(f"  abs {e['abs']:2d} {e['domena'][:26]:26s} {e.get('słowa', '-'):>5} sł. | {flagi} | schema {e.get('schema', '-')}")

if a.out:
    json.dump(wyniki, open(a.out, "w"), ensure_ascii=False, indent=1)
    print("zapisane:", a.out)
