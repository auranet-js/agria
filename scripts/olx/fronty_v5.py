#!/usr/bin/env python3
"""T-138: pierwsze zdjęcie ogłoszeń OLX z 12 frontów zamiast 3 scen — rozkład po mapie.

Wybór Janka 11.09.2026 (plansza auratest.pl/fe4f58fec53ctmp/agria-olx-t138/):
  luz      : halda-pole, zaladunek (v4) + hala-pryzma (Gemini)
             + od 11.09 wieczór wysyp-bok, wysyp-tyl, wysyp-podworze zamiast wycofanej wywrotka-zsyp
             (wysyp z górnego końca skrzyni — fizycznie błędny, zgłosił Janek; poprawka tylko na
             ogłoszeniach z tą sceną, pozostałe fronty z T-138 zostają — `rozklad(stale=...)`)
  big bagi : hds-bigbagi (v4) + 4 zdjęcia Janka z placu AGRII 10.09 (plac-*)
             + bigbagi-wiata, bigbagi-przyczepa, dlon-granulat (Gemini)
Odrzucone: worki Bielik i worki tlenkowe 25 kg (pozycjonowanie „nie sklep z workami”),
halda-ladowacz (pseudonapis na ciągniku), pozostałe sceny luzem.

Pula per forma dostawy — zdjęcie nie może obiecywać innej formy niż tytuł:
  tylko big bag (granulowane, Oxyfertil) : sceny big bagowe; dłoń z granulatem tylko przy granulowanych
  luz + big bag (Agrobieliki)            : sceny luzem + prawdziwe zdjęcia big bagów z placu
  tylko luz (kreda, węglanowe, pastewna) : sceny luzem
Przydział zachłanny z poprawkami: w jednym mieście każde ogłoszenie AGRII ma inną scenę,
identyczny obraz (ten sam napis + ta sama scena) nie powtarza się w promieniu ~100 km.

Galeria bez zmian składu — podmieniony front; jeśli scena frontu albo scena wycofana siedzi dalej
w galerii, w to miejsce wchodzi scena luzem, której ogłoszenie jeszcze nie ma, najrzadziej używana
(zero duplikatów, QR zostaje ostatni).
Napisy: miniatury_v4.render() (wzór 11.09). Wysyłka: zdjecia_v4.cli() — GET → putable() → PUT.

    fronty_v5.py --render            miniatury z napisami do agria-olx/v4/ (nic do OLX)
    fronty_v5.py --mockup plik.html  przed/po + metryki
    fronty_v5.py --zmienione plik    advert_id ogłoszeń, których galeria różni się od ładunku
    fronty_v5.py --sprawdz           odczyt per ogłoszenie z konta (status, zdjęcia, miasto, telefon)
    fronty_v5.py --dry-run | --backup | --ids plik.txt | --all   jak zdjecia_v4.py
"""
import json, math, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from miniatury_v4 import PLAN, nazwa, render  # noqa: E402
import zdjecia_v4 as z4  # noqa: E402

V4 = z4.V4
V4DIR = os.path.expanduser("~/domains/auratest.pl/public_html/agria-olx/v4")
LUZ_SC = ["wysyp-bok", "wysyp-tyl", "wysyp-podworze", "halda-pole", "zaladunek", "hala-pryzma"]
# 11.09 wieczór: wywrotka-zsyp wycofana — wapno sypało się z górnego końca skrzyni (zgłosił Janek,
# zdjęcie 4/8). Zastąpiona trzema wysypami z poprawną fizyką (przód skrzyni w górze, wysyp tylną klapą).
WYCOFANE = ["wywrotka-zsyp"]
PLAC = ["plac-budynek", "plac-bigbagi-budynek", "plac-bigbagi-hala", "plac-bigbagi-wieza"]
BB_SC = ["hds-bigbagi"] + PLAC + ["bigbagi-wiata", "bigbagi-przyczepa", "dlon-granulat"]
SCENY = LUZ_SC + BB_SC
GRANULAT = {"weglanowe-granulowane", "weglanowe-magnez-granulowane", "kreda-nawozowa-granulowana"}
REPO = os.path.dirname(os.path.dirname(HERE))


def pula(wariant):
    if wariant in z4.LUZ_BB:
        return LUZ_SC + PLAC
    if wariant in z4.LUZ or wariant == "kreda-pastewna":
        return LUZ_SC
    return [s for s in BB_SC if s != "dlon-granulat" or wariant in GRANULAT]


def scena(url):
    f = url.rsplit("/", 1)[-1].removesuffix(".jpg")
    return next((s for s in sorted(SCENY + WYCOFANE, key=len, reverse=True) if f.endswith(s)), None)


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def ogloszenia():
    payload = json.load(open(z4.PAYLOAD, encoding="utf-8"))
    reg = json.load(open(z4.POSTED, encoding="utf-8"))
    miasta = {c["id"]: (c["latitude"], c["longitude"])
              for c in json.load(open(os.path.join(REPO, "data/olx/cities-all.json"), encoding="utf-8"))}
    ads = []
    for it in payload:
        v = reg[it["external_id"]]
        imgs = [i["url"] for i in it["images"]]
        ads.append(dict(eid=it["external_id"], v=v, w=v["wariant"], napis=PLAN[v["wariant"]][0],
                        city=v["city_id"], geo=miasta[v["city_id"]], imgs=imgs, stara=scena(imgs[0])))
    return payload, reg, ads


def koszt(a, s, ads, przydzial, licznik):
    k = 0.4 * licznik[s]
    for b in ads:
        if b is a or przydzial.get(b["eid"]) != s:
            continue
        if b["city"] == a["city"]:
            k += 100
            continue
        d = km(a["geo"], b["geo"])
        if b["napis"] == a["napis"]:
            k += 40 * max(0.0, 1 - d / 100)
        else:
            k += 8 * max(0.0, 1 - d / 60)
    return k


def rozklad(ads, stale=None):
    """stale = fronty, których nie ruszamy (eid → scena); optymalizowane są tylko pozostałe."""
    stale = stale or {}
    na_miasto = Counter(a["city"] for a in ads)
    kolej = [a for a in sorted(ads, key=lambda a: (-na_miasto[a["city"]], a["city"], a["w"], a["eid"]))
             if a["eid"] not in stale]
    przydzial, licznik = dict(stale), Counter(stale.values())
    for a in kolej:
        s = min(pula(a["w"]), key=lambda s: (koszt(a, s, ads, przydzial, licznik), SCENY.index(s)))
        przydzial[a["eid"]] = s
        licznik[s] += 1
    for _ in range(4):  # poprawki: każde ogłoszenie na najlepszą scenę przy ustalonych pozostałych
        zmiany = 0
        for a in kolej:
            stara = przydzial.pop(a["eid"])
            licznik[stara] -= 1
            s = min(pula(a["w"]), key=lambda s: (koszt(a, s, ads, przydzial, licznik), SCENY.index(s)))
            przydzial[a["eid"]] = s
            licznik[s] += 1
            zmiany += s != stara
        if not zmiany:
            break
    return przydzial


def galeria(a, s, uzycie):
    """Nowy front; zdjęcie sceny frontu albo sceny wycofanej dalej w galerii → scena luzem, której
    w tym ogłoszeniu jeszcze nie ma, najrzadziej używana w środku galerii (uzycie = licznik)."""
    g = [V4 + nazwa(a["napis"], s)] + a["imgs"][1:]
    zajete = {s} | {scena(u) for u in g[1:] if "/agria-foto-" in u}
    for i, u in enumerate(g[1:], 1):
        if "/agria-foto-" in u and (scena(u) == s or scena(u) in WYCOFANE):
            zast = min((x for x in LUZ_SC if x not in zajete), key=lambda x: (uzycie[x], LUZ_SC.index(x)))
            g[i] = V4 + f"agria-foto-{zast}.jpg"
            zajete.add(zast)
            uzycie[zast] += 1
    assert len(g) == len(a["imgs"]) <= 8 and g[-1] == a["imgs"][-1], a["eid"]
    assert len(set(g)) == len(g), (a["eid"], g)
    return g


def metryki(ads, przydzial):
    obraz = {a["eid"]: (a["napis"], przydzial[a["eid"]]) for a in ads}
    miasto = defaultdict(list)
    for a in ads:
        miasto[a["city"]].append(przydzial[a["eid"]])
    dubl_miasto = sum(len(v) - len(set(v)) for v in miasto.values())
    pary = sum(1 for i, a in enumerate(ads) for b in ads[i + 1:]
               if obraz[a["eid"]] == obraz[b["eid"]] and km(a["geo"], b["geo"]) < 50)
    return dict(fronty=len(set(przydzial.values())), obrazy=len(set(obraz.values())),
                dubl_miasto=dubl_miasto, pary50=pary, licznik=Counter(przydzial.values()))


def mockup(plik, ads, przydzial, zadania, m_przed, m_po):
    """Przed/po do akceptu Janka: metryki, fronty, listy wyników w miastach, przykładowe galerie."""
    from html import escape as e
    gal = {eid: g for eid, _, g in zadania}
    nazwy = {a["city"]: a["v"]["city"] for a in ads}
    im = lambda u, w=120: f'<img src="{u}" width="{w}" loading="lazy" alt="">'
    grupa = lambda a: ("Agrobieliki (luz + big bag)" if a["w"] in z4.LUZ_BB else
                       "tylko luz" if a["w"] in z4.LUZ or a["w"] == "kreda-pastewna" else "tylko big bag")
    wiersz = lambda k, a, b: f"<tr><td>{k}</td><td>{a}</td><td><b>{b}</b></td></tr>"
    h = ['<title>AGRIA OLX — fronty v5 (T-138)</title><style>'
         ':root{--bg:#f2f4f5;--fg:#002f34;--mut:#406367;--card:#fff;--line:#d8dfe0}'
         '@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10181a;--fg:#e8f0f0;--mut:#9db3b5;--card:#1b2629;--line:#2c3b3e}}'
         ':root[data-theme="dark"]{--bg:#10181a;--fg:#e8f0f0;--mut:#9db3b5;--card:#1b2629;--line:#2c3b3e}'
         'body{background:var(--bg);color:var(--fg);font:14px/1.4 system-ui,sans-serif;padding-inline:16px;padding-block:24px;max-width:1240px;margin:0 auto}'
         'section{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin:18px 0}'
         'h1{font-size:22px}h2{font-size:18px;margin:0 0 8px}.mut{color:var(--mut)}table{border-collapse:collapse}'
         'td,th{border-bottom:1px solid var(--line);padding:4px 12px 4px 0;text-align:left}'
         '.row{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px}figure{margin:0;flex:0 0 auto}'
         'figcaption{font-size:11px;color:var(--mut);max-width:120px}img{border-radius:4px;display:block}'
         '.lbl{font-size:12px;font-weight:600;margin:10px 0 4px}</style>',
         '<h1>OLX AGRIA — 12 frontów zamiast 3 scen (T-138)</h1>',
         '<p class="mut">Zmienia się pierwsze zdjęcie (miniatura na liście wyników). Skład galerii bez zmian, '
         'QR z kalkulatorem zostaje ostatni. Jeśli nowy front był też dalej w galerii, w to miejsce wchodzi '
         'dotychczasowy front, więc duplikatów nie ma.</p>',
         '<section><h2>Metryki</h2><table><tr><th></th><th>teraz</th><th>po</th></tr>',
         wiersz("różne sceny na froncie", m_przed["fronty"], m_po["fronty"]),
         wiersz("różne obrazy (napis × scena)", m_przed["obrazy"], m_po["obrazy"]),
         wiersz("ta sama scena drugi raz w tym samym mieście", m_przed["dubl_miasto"], m_po["dubl_miasto"]),
         wiersz("pary identycznych obrazów bliżej niż 50 km", m_przed["pary50"], m_po["pary50"]),
         '</table></section>',
         '<section><h2>Fronty i liczba ogłoszeń</h2><p class="mut">Pula według formy dostawy: tylko luz → 4 sceny luzem; '
         'tylko big bag → 8 scen big bagowych (dłoń z granulatem tylko przy granulowanych, bez Oxyfertilu); '
         'Agrobieliki (luz i big bag) → 4 sceny luzem + 4 Twoje zdjęcia z placu.</p><div class="row">']
    for s in SCENY:
        h.append(f'<figure>{im(V4 + f"agria-foto-{s}.jpg")}<figcaption><b>{s}</b><br>'
                 f'{m_po["licznik"][s]} ogł. (było {m_przed["licznik"][s]})</figcaption></figure>')
    h.append('</div></section>')
    na_miasto = defaultdict(list)
    for a in ads:
        na_miasto[a["city"]].append(a)
    h.append('<section><h2>Co widzi rolnik w swoim mieście</h2><p class="mut">Miasta z największą liczbą '
             'ogłoszeń AGRII — lista wyników teraz i po zmianie.</p>')
    for c in sorted(na_miasto, key=lambda c: -len(na_miasto[c]))[:10]:
        lst = sorted(na_miasto[c], key=lambda a: a["w"])
        h.append(f'<div class="lbl">{e(nazwy[c])} — {len(lst)} ogł.</div><div class="row">')
        h += [f'<figure>{im(a["imgs"][0], 100)}<figcaption>teraz · {e(a["w"])}</figcaption></figure>' for a in lst]
        h.append('</div><div class="row">')
        h += [f'<figure>{im(gal[a["eid"]][0], 100)}<figcaption><b>po</b> · {e(a["w"])}</figcaption></figure>' for a in lst]
        h.append('</div>')
    h.append('</section>')
    h.append('<section><h2>Przykładowe pełne galerie po zmianie</h2>')
    wzory = [next(a for a in ads if a["w"] in z4.LUZ_BB and przydzial[a["eid"]] in PLAC),
             next(a for a in ads if a["w"] in z4.LUZ and przydzial[a["eid"]] == "zaladunek"),
             next(a for a in ads if a["w"] in GRANULAT and przydzial[a["eid"]] == "dlon-granulat")]
    for a in wzory:
        h.append(f'<div class="lbl">{e(a["w"])} · {e(a["v"]["city"])} · {grupa(a)}</div><div class="row">')
        h += [f'<figure>{im(u, 100)}<figcaption>{i}</figcaption></figure>' for i, u in enumerate(gal[a["eid"]], 1)]
        h.append('</div>')
    h.append('</section>')
    for g_ in ("Agrobieliki (luz + big bag)", "tylko luz", "tylko big bag"):
        lst = sorted((a for a in ads if grupa(a) == g_), key=lambda a: (a["w"], a["v"]["city"]))
        h.append(f'<section><h2>{g_} — wszystkie {len(lst)} ogłoszeń po zmianie</h2><div class="row" style="flex-wrap:wrap">')
        h += [f'<figure>{im(gal[a["eid"]][0], 100)}<figcaption>{e(a["v"]["city"])}<br>{e(a["w"])}</figcaption></figure>'
              for a in lst]
        h.append('</div></section>')
    open(plik, "w", encoding="utf-8").write("\n".join(h))
    print(f"mockup → {plik}")


def plan():
    payload, reg, ads = ogloszenia()
    stale = {a["eid"]: a["stara"] for a in ads if a["stara"] not in WYCOFANE}  # fronty z T-138 zostają
    przydzial = rozklad(ads, stale)
    uzycie = Counter(scena(u) for a in ads for u in a["imgs"][1:]
                     if "/agria-foto-" in u and scena(u) not in WYCOFANE)
    zadania = [(a["eid"], a["v"], galeria(a, przydzial[a["eid"]], uzycie)) for a in ads]
    return payload, reg, ads, przydzial, zadania


def main():
    args = sys.argv[1:]
    payload, reg, ads, przydzial, zadania = plan()
    if "--render" in args:
        pary = sorted({(a["napis"], przydzial[a["eid"]]) for a in ads})
        nowe = [(n, s) for n, s in pary if not os.path.exists(os.path.join(V4DIR, nazwa(n, s)))]
        for napis, s in nowe:  # istniejących nie nadpisujemy — wiszą pod żywymi ogłoszeniami
            print(os.path.basename(render(napis, s)))
        return print(f"miniatur: {len(pary)}, nowych: {len(nowe)}")
    if "--mockup" in args:
        przed = {a["eid"]: a["stara"] for a in ads}
        return mockup(args[args.index("--mockup") + 1], ads, przydzial, zadania,
                      metryki(ads, przed), metryki(ads, przydzial))
    if "--sprawdz" in args:  # odczyt per ogłoszenie — lista zbiorcza oddaje stan z opóźnieniem
        by_eid = {it["external_id"]: it for it in payload}
        zle = []
        for eid, v in reg.items():
            c, r = z4.call("GET", f"/partner/adverts/{v['advert_id']}")
            d = r.get("data", {}) if c == 200 else {}
            braki = [f"HTTP {c}"] if c != 200 else []
            if d and d.get("status") != "active": braki.append(f"status {d.get('status')}")
            if d and not d.get("auto_extend_enabled"): braki.append("auto_extend wyłączone")
            if d and len(d.get("images", [])) != len(by_eid[eid]["images"]): braki.append(f"zdjęć {len(d['images'])}")
            if d and d.get("location", {}).get("city_id") != v["city_id"]: braki.append("miasto ≠ rejestr")
            if d and d.get("external_id") != eid: braki.append(f"external_id {d.get('external_id')}")
            if d and not (d.get("contact") or {}).get("phone"): braki.append("BRAK TELEFONU")
            if braki:
                zle.append((v["advert_id"], v["city"], braki))
        for z in zle:
            print("  !!", *z)
        return print(f"zgodnych: {len(reg) - len(zle)}/{len(reg)}")
    if "--zmienione" in args:  # advert_id ogłoszeń, których galeria różni się od ładunku
        by_eid = {it["external_id"]: [i["url"] for i in it["images"]] for it in payload}
        ids = [str(v["advert_id"]) for eid, v, g in zadania if g != by_eid[eid]]
        open(args[args.index("--zmienione") + 1], "w").write("\n".join(ids) + "\n")
        return print(f"do zmiany: {len(ids)}")
    if "--metryki" in args:
        przed = {a["eid"]: a["stara"] for a in ads}
        for nazwa_, p in (("przed", przed), ("po", przydzial)):
            print(nazwa_, metryki(ads, p))
        return
    z4.cli(args, payload, reg, zadania, "v5", __doc__)


if __name__ == "__main__":
    main()
