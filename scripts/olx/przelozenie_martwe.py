#!/usr/bin/env python3
"""T-144 (audyt 23.09.2026): projekt przełożenia martwych ogłoszeń OLX.

Martwe = zero odsłon numeru od wystawienia i najwyżej 5 odsłon przez ≥25 dni w jednym miejscu
(data/olx/audyt-2026-09/martwe-2026-09-23.json). Poza serią: „do stawu” (sezon X–XI), kreda pastewna
(rewizja listopadowa) i ogłoszenia przy magazynach (Żabno, Radgoszcz).

Cele łączą dwie reguły, które się sprawdziły: odległość ≤120 km od Niedomic/Radgoszczy (T-106 dało
kontakty) i realny rynek wapna w mieście (T-139 dało ruch). Rynek = spis 23.09 (kat. 4368, „wapno”,
bez AGRII). Jedno ogłoszenie na miasto, miasto bez AGRII; w promieniu 50 km nie stoi drugi nasz
egzemplarz tego samego produktu. Kolejność: liczba sprzedawców, liczba ich ogłoszeń, bliżej magazynu.

    przelozenie_martwe.py            projekt na ekran
    przelozenie_martwe.py --zapisz   data/olx/przelozenie-2026-09-23.json (format przeloz.py)
Wykonanie: przeloz.py --projekt data/olx/przelozenie-2026-09-23.json --pilot 3 / --all
"""
import json, math, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")
MAG = [(50.150, 20.900), (50.235, 21.030)]
AGRIA_UID = 43762401
POZA = {"agrobielik-70-staw", "kreda-pastewna"}
PRZY_MAGAZYNIE = {"Żabno", "Radgoszcz"}
# Zasięg opłacalnej dostawy od zakładu (transport ≤ 50% ceny towaru przy 0,25 zł/t/km — memory
# project_agria_olx_kanal). Tanie sypkie jadą blisko kopalni; reszta ma zasięg ponad promień siatki.
ZASIEG = {"weglanowe-magnez-odmiana-05": 72, "weglanowe-magnez-odmiana-04": 100, "weglanowe-odmiana-04": 114}
sys.path.insert(0, HERE)
from grid import ZAKLADY, PRODUKTY  # noqa: E402
ZAKLADY_W = {p["klucz"]: p["zaklady"] for p in PRODUKTY}


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def main():
    L = lambda p: json.load(open(os.path.join(D, p), encoding="utf-8"))
    miasta = {c["id"]: c for c in L("cities-all.json")}
    geo = lambda cid: (miasta[cid]["latitude"], miasta[cid]["longitude"])
    dm = lambda cid: min(km(geo(cid), m) for m in MAG)
    po_nazwie = defaultdict(list)
    for c in miasta.values():
        po_nazwie[(c["name"], c["region_id"])].append(c["id"])
    reg = L("posted.json")
    martwe = [x for x in L("audyt-2026-09/martwe-2026-09-23.json")
              if x["tel_calosc"] == 0 and x["ods_od_przel"] <= 5 and x["dni_od_przel"] >= 25
              and x["wariant"] not in POZA and x["miasto"] not in PRZY_MAGAZYNIE]
    by_aid = {v["advert_id"]: (k, v) for k, v in reg.items()}
    martwe = [x for x in martwe if x["advert_id"] in by_aid
              and by_aid[x["advert_id"]][1]["wariant"] == x["wariant"]]  # T-146 zmienił produkt → poza

    rynek, sprz = Counter(), defaultdict(set)
    for o in L("audyt-2026-09/rynek-wapno-spis-2026-09-23.json")["offers"]:
        if o["user_id"] == AGRIA_UID:
            continue
        ids = po_nazwie.get((o["city"], o["region"]))
        if ids and len(ids) == 1:  # nazwa niejednoznaczna w województwie (5× Białobrzegi) — pomijamy
            cid = ids[0]
            rynek[cid] += 1
            sprz[cid].add(o["user_id"])
    zajete = {v["city_id"] for v in reg.values()}
    stoi = [(v["wariant"], v["city_id"]) for v in reg.values()
            if v["advert_id"] not in {x["advert_id"] for x in martwe}]
    cele = sorted((c for c in rynek if c not in zajete and dm(c) <= 120 and len(sprz[c]) >= 2),
                  key=lambda c: (-len(sprz[c]), -rynek[c], dm(c)))

    def pasuje(c, w, promien):
        if w in ZASIEG and min(km(geo(c), ZAKLADY[z]) for z in ZAKLADY_W[w]) > ZASIEG[w]:
            return False
        return all(not (ww == w and km(geo(c), geo(cc)) < promien) for ww, cc in stoi)

    projekt = []
    for x in sorted(martwe, key=lambda x: -x["km_magazyn"]):
        k, v = by_aid[x["advert_id"]]
        cel = next((c for c in cele if pasuje(c, x["wariant"], 50)), None) \
            or next((c for c in cele if pasuje(c, x["wariant"], 30)), None)
        if cel is None:
            print(f"  brak celu dla {x['advert_id']} {x['wariant']} — zostaje")
            continue
        cele.remove(cel)
        stoi.append((x["wariant"], cel))
        projekt.append(dict(klucz=k, advert_id=x["advert_id"], siatka=x["wariant"], sku=v["sku"],
                            miasto=x["miasto"], km=x["km_magazyn"], odslony=x["ods_od_przel"], telefony=0,
                            stary_wariant=x["wariant"], nowe_miasto=miasta[cel]["name"],
                            nowy_city_id=cel, nowy_powiat=miasta[cel].get("county"),
                            nowy_km=round(dm(cel)), sprzedawcy=len(sprz[cel]), ogl_rynku=rynek[cel],
                            nowy_wariant=None))
    for p in projekt:
        print(f"  {p['advert_id']} {p['siatka']:<28} {p['miasto']:<22}{p['km']:>4} km → "
              f"{p['nowe_miasto']:<20}{p['nowy_km']:>4} km  sprzedawców {p['sprzedawcy']}, ogł. {p['ogl_rynku']}")
    print(f"\nprojekt: {len(projekt)} z {len(martwe)} martwych")
    if "--zapisz" in sys.argv:
        json.dump(projekt, open(os.path.join(D, "przelozenie-2026-09-23.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("→ data/olx/przelozenie-2026-09-23.json")


if __name__ == "__main__":
    main()
