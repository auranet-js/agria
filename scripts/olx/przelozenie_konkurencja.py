#!/usr/bin/env python3
"""Projekt przełożenia ogłoszeń OLX do miast, w których wystawia konkurencja (11.09.2026).

Polecenie Janka 11.09: w małopolskim, świętokrzyskim, podkarpackim i mazowieckim obsadzić
miasta, w których mają oferty Wapna Świętokrzyskie (plusplon), Robert, WAP POL, WAPNO-PRODUCENT.

Powód (statystyki 11.09 12:08, 158 ogłoszeń AGRII w tych 4 województwach):
    w miastach, gdzie wystawia ktoś z czwórki   0,247 odsłony numeru na ogłoszenie (89 ogł.)
    w miastach bez konkurencji                  0,087                            (69 ogł.)
Tam, gdzie konkurencja wystawia, rolnicy szukają wapna.

Źródła (co przenosimy): ogłoszenia AGRII w 4 województwach stojące w miastach bez żadnego z czwórki,
POZA: ogłoszeniami z choć jedną odsłoną numeru (działają), 9 przełożonymi 11.09 w serii C
(bez pomiaru w nowym miejscu) i jednym ogłoszeniem przy każdym magazynie (Radgoszcz, Żabno).
Cele: miasta czwórki w tych województwach, bez AGRII, do 200 km od magazynów (pomiar 28.08:
dalej praktycznie zero kontaktów). Jedno ogłoszenie na miasto; kolejność: liczba sprzedawców,
liczba ich ogłoszeń, pierścień 60–200 km przed 0–60 km. Produkt zostaje ten sam — dobieramy go tak,
żeby w promieniu 50 km nie stał drugi nasz egzemplarz tego samego produktu.

    przelozenie_konkurencja.py                   projekt na ekran
    przelozenie_konkurencja.py --zapisz          data/olx/przelozenie-2026-09-11.json (format przeloz.py)
    przelozenie_konkurencja.py --html plik.html  plan do akceptu
Wykonanie: przeloz.py --projekt data/olx/przelozenie-2026-09-11.json ...
"""
import json, math, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")
KONK = os.path.join(D, "market", "konkurencja-4-sprzedawcow-2026-09-11.json")
SPRZEDAWCY = {"594644825": "Wapna Świętokrzyskie", "18710719": "Robert",
              "1020485928": "WAP POL", "2017493038": "WAPNO-PRODUCENT"}
WOJ = {4: "małopolskie", 13: "świętokrzyskie", 17: "podkarpackie", 2: "mazowieckie"}
NIEDOMICE, RADGOSZCZ = (50.150, 20.900), (50.235, 21.030)
PRZY_MAGAZYNIE = {"Radgoszcz", "Żabno"}
WYKLUCZONE = {"Zakopane", "Rabka-Zdrój"}   # kurorty, nie rynek rolny — decyzja 11.09
MAKS_KM = 200
DZIS = "2026-09-11"


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def projekt():
    reg = json.load(open(os.path.join(D, "posted.json"), encoding="utf-8"))
    miasta = {c["id"]: c for c in json.load(open(os.path.join(D, "cities-all.json"), encoding="utf-8"))}
    st = json.load(open(os.path.join(D, "statystyki.json"), encoding="utf-8"))[-1]["per_ogloszenie"]
    konk = json.load(open(KONK, encoding="utf-8"))
    geo = lambda cid: (miasta[cid]["latitude"], miasta[cid]["longitude"])
    mag = lambda cid: min(km(geo(cid), NIEDOMICE), km(geo(cid), RADGOSZCZ))
    stat = lambda v: st.get(str(v["advert_id"]), [0, 0])

    kc = defaultdict(lambda: defaultdict(int))
    nazwa = {}
    for uid, rows in konk.items():
        for r in rows:
            cid = r["location"]["city"]["id"]
            kc[cid][uid] += 1
            nazwa[cid] = r["location"]["city"]["name"]
    nasze_miasta = {v["city_id"] for v in reg.values()}

    zostaja, zrodla = [], []
    for klucz, v in reg.items():
        w = miasta[v["city_id"]]["region_id"]
        if w not in WOJ or v["city_id"] in kc:
            continue
        o, t = stat(v)
        rec = dict(klucz=klucz, advert_id=v["advert_id"], siatka=v["wariant"], sku=v["sku"],
                   miasto=v["city"], woj=WOJ[w], km=round(mag(v["city_id"])), odslony=o, telefony=t,
                   stary_wariant=v["wariant"], geo=geo(v["city_id"]))
        if t > 0:
            zostaja.append(dict(rec, powod=f"{t} odsł. numeru — działa"))
        elif v.get("przelozone") == DZIS:
            zostaja.append(dict(rec, powod="przełożone dziś (seria C) — bez pomiaru"))
        else:
            zrodla.append(rec)
    for m in PRZY_MAGAZYNIE:  # jedno ogłoszenie przy magazynie zostaje — najwięcej odsłon
        tu = sorted((r for r in zrodla if r["miasto"] == m), key=lambda r: -r["odslony"])
        if tu:
            zrodla.remove(tu[0])
            zostaja.append(dict(tu[0], powod="przy magazynie AGRII"))

    cele = []
    for cid, u in kc.items():
        if cid not in miasta or miasta[cid]["region_id"] not in WOJ or cid in nasze_miasta \
                or nazwa[cid] in WYKLUCZONE:
            continue
        d = mag(cid)
        if d <= MAKS_KM:
            cele.append(dict(city_id=cid, miasto=nazwa[cid], woj=WOJ[miasta[cid]["region_id"]], km=round(d),
                             geo=geo(cid), sprzedawcy={SPRZEDAWCY[k]: n for k, n in u.items()}))
    cele.sort(key=lambda c: (-len(c["sprzedawcy"]), -sum(c["sprzedawcy"].values()), c["km"] < 60, c["km"]))

    # rozmieszczenie produktu: dla kolejnego celu bierzemy źródło, którego produkt ma najdalej
    # do najbliższego naszego egzemplarza (po dotychczasowych i nowych pozycjach)
    pozycje = defaultdict(list)
    for v in reg.values():
        if not any(v["advert_id"] == r["advert_id"] for r in zrodla):
            pozycje[v["wariant"]].append(geo(v["city_id"]))
    plan, wolne = [], list(zrodla)
    for c in cele:
        if not wolne:
            break
        odl = lambda r: min((km(c["geo"], p) for p in pozycje[r["siatka"]]), default=999)
        r = max(wolne, key=lambda r: (min(odl(r), 50), -r["odslony"], r["advert_id"]))
        wolne.remove(r)
        pozycje[r["siatka"]].append(c["geo"])
        plan.append(dict({k: x for k, x in r.items() if k != "geo"}, nowe_miasto=c["miasto"],
                         nowy_city_id=c["city_id"], nowy_woj=c["woj"], nowy_km=c["km"],
                         sprzedawcy=c["sprzedawcy"], nowy_wariant=None))
    nieobsadzone = cele[len(plan):]
    return plan, zostaja, nieobsadzone, cele, wolne


def html(plik, plan, zostaja, nieobsadzone, cele):
    from html import escape as e
    sp = lambda d: ", ".join(f"{k} {n}" for k, n in d.items())
    css = ('<style>:root{--bg:#f2f4f5;--fg:#002f34;--mut:#406367;--card:#fff;--line:#d8dfe0}'
           '@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10181a;--fg:#e8f0f0;--mut:#9db3b5;--card:#1b2629;--line:#2c3b3e}}'
           ':root[data-theme="dark"]{--bg:#10181a;--fg:#e8f0f0;--mut:#9db3b5;--card:#1b2629;--line:#2c3b3e}'
           'body{background:var(--bg);color:var(--fg);font:14px/1.4 system-ui,sans-serif;padding-inline:16px;padding-block:24px;max-width:1150px;margin:0 auto}'
           'h1{font-size:22px}h2{font-size:18px;margin:26px 0 6px}.mut{color:var(--mut)}'
           '.tw{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:8px}'
           'table{border-collapse:collapse;width:100%}th,td{padding:5px 10px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}'
           'th{font-size:12px}td.n{text-align:right}</style>')
    t = lambda head, rows: (f'<div class="tw"><table><thead><tr>{"".join(f"<th>{h}</th>" for h in head)}</tr></thead>'
                            f'<tbody>{"".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)}</tbody></table></div>')
    h = [f'<title>OLX AGRIA — przełożenie do miast konkurencji</title>{css}',
         '<h1>OLX AGRIA — przełożenie do miast konkurencji (projekt 11.09.2026)</h1>',
         '<p class="mut">Województwa: małopolskie, świętokrzyskie, podkarpackie, mazowieckie. Zmienia się tylko miejscowość ogłoszenia — '
         'produkt, tytuł, treść, zdjęcia i telefon bez zmian; OLX nie liczy tego jako nowej publikacji (zmierzone 28.08).</p>',
         '<p><b>Dlaczego:</b> nasze ogłoszenia w miastach, gdzie wystawia ktoś z czwórki, dają <b>0,25</b> odsłony numeru na ogłoszenie; '
         'w miastach bez konkurencji <b>0,09</b> (statystyki 11.09 12:08).</p>',
         f'<p><b>Przenosimy {len(plan)}</b> · zostaje {len(zostaja)} · miast konkurencji do 200 km bez AGRII: {len(cele)}, '
         f'z tego nieobsadzonych po przełożeniu: {len(nieobsadzone)}.</p>',
         f'<h2>1. Przeniesienia ({len(plan)})</h2>',
         t(["#", "Produkt", "Z miasta", "odsłony / numer", "→ Do miasta", "Województwo", "km od magazynu", "Konkurencja tam (liczba ogł.)"],
           [(i, e(r["siatka"]), e(r["miasto"]), f'{r["odslony"]} / {r["telefony"]}', f'<b>{e(r["nowe_miasto"])}</b>',
             r["nowy_woj"], r["nowy_km"], e(sp(r["sprzedawcy"]))) for i, r in enumerate(plan, 1)]),
         f'<h2>2. Zostają w miastach bez konkurencji ({len(zostaja)})</h2>',
         t(["Produkt", "Miasto", "Województwo", "odsłony / numer", "Dlaczego zostaje"],
           [(e(r["siatka"]), e(r["miasto"]), r["woj"], f'{r["odslony"]} / {r["telefony"]}', e(r["powod"])) for r in zostaja]),
         f'<h2>3. Miasta konkurencji do 200 km, których nie obsadzamy — zabrakło ogłoszeń ({len(nieobsadzone)})</h2>',
         t(["Miasto", "Województwo", "km od magazynu", "Konkurencja (liczba ogł.)"],
           [(e(c["miasto"]), c["woj"], c["km"], e(sp(c["sprzedawcy"]))) for c in nieobsadzone])]
    open(plik, "w", encoding="utf-8").write("\n".join(h))
    print(f"html → {plik}")


def main():
    plan, zostaja, nieobsadzone, cele, wolne = projekt()
    for r in plan:
        print(f"{r['advert_id']} {r['siatka']:<28} {r['miasto']:<16} → {r['nowe_miasto']:<18} {r['nowy_km']:>4} km  {r['sprzedawcy']}")
    print(f"\nprzenosimy {len(plan)}, zostaje {len(zostaja)}, niewykorzystane źródła {len(wolne)}, "
          f"cele {len(cele)}, nieobsadzone {len(nieobsadzone)}")
    if "--zapisz" in sys.argv:
        plik = os.path.join(D, f"przelozenie-{DZIS}.json")
        json.dump(plan, open(plik, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"zapisane → {os.path.relpath(plik)}")
    if "--html" in sys.argv:
        html(sys.argv[sys.argv.index("--html") + 1], plan, zostaja, nieobsadzone, cele)


if __name__ == "__main__":
    main()
