#!/usr/bin/env python3
"""Audyt kanału OLX — tabela per ogłoszenie z historią przełożeń i przyrostami między pomiarami.

    audyt.py [--out katalog]     zapisuje ogloszenia-analiza.json + okna.json, drukuje przekroje

Wejście (wyłącznie lokalne, nic nie woła OLX):
  data/olx/statystyki.json          pomiary kumulatywne per ogłoszenie
  data/olx/posted.json              rejestr (advert_id, wariant, city_id)
  data/olx/adverts-payload.json     galeria (pierwsze zdjęcie → scena frontu)
  data/backups/T-106-olx-przed-2026-08-28.json, olx-seria-c-przed-2026-09-11-1240.json,
  olx-przelozenie-przed-2026-09-11.json   miasta przed przełożeniami

Statystyki są kumulatywne i przełożenie nie zeruje licznika — przyrost po przełożeniu liczymy
od pomiaru bezpośrednio przed nim (28.08 15:01 dla T-106, 11.09 12:08 dla T-137/T-139).
"""
import json, math, os, sys
from collections import defaultdict
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(REPO, "data", "olx")
B = os.path.join(REPO, "data", "backups")
sys.path.insert(0, HERE)
from grid import ZAKLADY, PRODUKTY  # noqa: E402
from fronty_v5 import scena  # noqa: E402

MAGAZYNY = {"Niedomice": (50.150, 20.900), "Radgoszcz": (50.235, 21.030)}
ZAKLADY_W = {p["klucz"]: p["zaklady"] for p in PRODUKTY}
PLAC = {"plac-budynek", "plac-bigbagi-budynek", "plac-bigbagi-hala", "plac-bigbagi-wieza"}


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def load(p):
    return json.load(open(p, encoding="utf-8"))


def main():
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(D, "audyt-2026-09")
    hist = [h for h in load(os.path.join(D, "statystyki.json")) if h["ogloszen"] == 200]
    reg = load(os.path.join(D, "posted.json"))
    pay = {p["external_id"]: p for p in load(os.path.join(D, "adverts-payload.json"))}
    miasta = {c["id"]: c for c in load(os.path.join(D, "cities-all.json"))}
    t106 = {int(k): v for k, v in load(os.path.join(B, "T-106-olx-przed-2026-08-28.json")).items()}
    przed_c = {int(k): v for k, v in load(os.path.join(B, "olx-seria-c-przed-2026-09-11-1240.json")).items()}
    t139 = {int(k): v for k, v in load(os.path.join(B, "olx-przelozenie-przed-2026-09-11.json")).items()}
    kiedy = [h["kiedy"] for h in hist]

    rows = []
    for eid, v in reg.items():
        aid = v["advert_id"]
        c = miasta[v["city_id"]]
        geo = (c["latitude"], c["longitude"])
        grupy = []
        if aid in t106:
            grupy.append("T-106")
        if aid in t139:
            grupy.append("T-139")
        elif aid in przed_c and przed_c[aid]["location"]["city_id"] != v["city_id"]:
            grupy.append("seria-C")
        ost = "2026-09-11 12:08" if {"T-139", "seria-C"} & set(grupy) else (
            "2026-08-28 15:01" if "T-106" in grupy else None)
        cum = [h["per_ogloszenie"].get(str(aid), [None, None]) for h in hist]
        s = scena(pay[eid]["images"][0]["url"]) if eid in pay else None
        zak = ZAKLADY_W.get(v["wariant"], [])
        dz = min(((z, km(geo, ZAKLADY[z])) for z in zak), key=lambda x: x[1]) if zak else (None, None)
        dm = min(km(geo, g) for g in MAGAZYNY.values())
        rows.append(dict(
            advert_id=aid, external_id=eid, wariant=v["wariant"], sku=v["sku"], miasto=c["name"],
            powiat=c.get("county"), region_id=c["region_id"], city_id=v["city_id"],
            km_magazyn=round(dm), zaklad=dz[0], km_zaklad=round(dz[1]) if dz[1] is not None else None,
            front=s, front_typ=("plac" if s in PLAC else "scena") if s else None,
            grupy=grupy, ostatnie_przelozenie=ost,
            odslony=cum[-1][0], telefony=cum[-1][1], historia=dict(zip(kiedy, cum))))
    os.makedirs(out, exist_ok=True)
    json.dump(rows, open(os.path.join(out, "ogloszenia-analiza.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{len(rows)} ogłoszeń, {len(kiedy)} pomiarów: {kiedy[0]} … {kiedy[-1]}")
    return rows, kiedy


def przyrost(r, a, b):
    ha, hb = r["historia"].get(a), r["historia"].get(b)
    if not ha or not hb or ha[0] is None or hb[0] is None:
        return None
    return hb[0] - ha[0], hb[1] - ha[1]


def dni(a, b):
    f = "%Y-%m-%d %H:%M"
    return (datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds() / 86400


if __name__ == "__main__":
    main()
