#!/usr/bin/env python3
"""Podmiana galerii OLX na wersję v4 (zdjęcia „z placu”) — tylko zdjęcia, reszta ogłoszenia bez zmian.

Mockup zaakceptowany przez Janka 11.09.2026:
auratest.pl/fe4f58fec53ctmp/agria-olx-mockup-wymiana-zdjec-v2-2026-09-11.html

Mechanika jak przy T-106: GET ogłoszenia → putable() → podmiana samego `images` → PUT.
NIE przez `post_adverts.py --update`, bo ten wysyła całą treść z adverts-payload.json
i przy każdym rozjeździe ładunku z kontem cofnąłby żywy stan. Po udanym PUT ta sama lista
zdjęć trafia do adverts-payload.json — żeby późniejsze `--update` nie cofnęło zdjęć.

Galeria (limit kategorii 4368: 8 zdjęć):
  luz + big bag (Agrobieliki) : napis+foto1 · grafika · studio · foto2 · karta · big bag Agrobielik · załadunek · QR
  luz (kreda, węglanowe)      : napis+foto1 · grafika · studio · foto2 · karta · frakcja · załadunek · QR
  big bag (granulowane, Oxyf.): napis+HDS · grafika · studio · karta · frakcja · QR
  kreda pastewna              : napis+załadunek/wywrotka · grafika · studio · karta · foto2 · frakcja · QR
Wariant A/B = ten sam, co dotychczasowa miniatura (-b.jpg → B). Zdjęcie z ciągnikiem (hero) wypada,
big bag z napisem Agrobielik zostaje tylko przy Agrobielikach (etykieta innego towaru).

    zdjecia_v4.py --dry-run          plan per ogłoszenie, zero ruchu do OLX
    zdjecia_v4.py --backup           zrzut GET wszystkich 200 do data/backups/ (przed podmianą)
    zdjecia_v4.py --ids plik.txt     podmiana tylko wskazanych advert_id (pilot)
    zdjecia_v4.py --all              podmiana wszystkich, bezpiecznik moderacyjny co 25
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import call, putable, moderation_check, notify, PAYLOAD, POSTED  # noqa: E402
from miniatury_v4 import PLAN, nazwa  # noqa: E402

D = os.path.join(HERE, "..", "..", "data")
V3DIR = os.path.expanduser("~/domains/auratest.pl/public_html/agria-olx/v3")
V4 = "https://auratest.pl/agria-olx/v4/"
FOTO = {k: V4 + f"agria-foto-{k}.jpg" for k in ("wywrotka-zsyp", "halda-pole", "zaladunek", "hds-bigbagi")}
LUZ_BB = {"agrobielik-70-staw", "agrobielik-70-gleba", "agrobielik-90"}
LUZ = {"kreda-nawozowa-sypka", "weglanowe-odmiana-04", "weglanowe-magnez-odmiana-04",
       "weglanowe-magnez-odmiana-05"}


def rozloz(images):
    """Dzieli dotychczasową galerię (adresy auratest) na role."""
    r = {"mini": images[0]}
    for u in images[1:]:
        f = u.rsplit("/", 1)[-1]
        klucz = next((k for k in ("studio", "karta", "bigbag", "hero", "info") if k in f), "frakcja")
        r[klucz] = u
    # 8 ogłoszeń z T-106 (seria B) poszło z miniaturą v2 — ucinała hasło na telefonie
    if "/v2/agria-mini-" in r["mini"]:
        f = r["mini"].rsplit("/", 1)[-1]
        if os.path.exists(os.path.join(V3DIR, f)):
            r["mini"] = r["mini"].replace("/v2/", "/v3/")
    return r


def galeria(wariant, images):
    r = rozloz(images)
    b = r["mini"].endswith("-b.jpg")
    napis, fa, fb = PLAN[wariant]
    if wariant == "kreda-pastewna":
        f1, f2 = (fb, fa) if b else (fa, fb)
        g = [V4 + nazwa(napis, f1), r["mini"], r.get("studio"), r.get("karta"), FOTO[f2],
             r.get("frakcja"), r.get("info")]
    elif wariant in LUZ_BB or wariant in LUZ:
        f1, f2 = (fb, fa) if b else (fa, fb)
        srodek = r.get("bigbag") if wariant in LUZ_BB else r.get("frakcja")
        g = [V4 + nazwa(napis, f1), r["mini"], r.get("studio"), FOTO[f2], r.get("karta"),
             srodek, FOTO["zaladunek"], r.get("info")]
    else:  # big bag: wariant B czeka na zdjęcia big bagów z placu — do tego czasu HDS dla wszystkich
        g = [V4 + nazwa(napis, fa), r["mini"], r.get("studio"), r.get("karta"), r.get("frakcja"),
             r.get("info")]
    g = [u for u in g if u]
    assert len(g) <= 8 and g[-1] == r.get("info", g[-1]), wariant
    return g


def plan():
    payload = json.load(open(PAYLOAD, encoding="utf-8"))
    reg = json.load(open(POSTED, encoding="utf-8"))
    out = []
    for it in payload:
        v = reg[it["external_id"]]
        out.append((it["external_id"], v, galeria(v["wariant"], [i["url"] for i in it["images"]])))
    return payload, reg, out


def main():
    args = sys.argv[1:]
    payload, reg, zadania = plan()
    if "--dry-run" in args:
        for eid, v, g in zadania:
            print(f"{v['advert_id']} {v['wariant']:<30} {v['city']:<20} " +
                  " · ".join(u.rsplit('/', 1)[-1].replace('.jpg', '') for u in g))
        return print(f"ogłoszeń: {len(zadania)} — nic nie wysłane (--dry-run)")

    if "--backup" in args:
        stan = {}
        for eid, v, _ in zadania:
            c, r = call("GET", f"/partner/adverts/{v['advert_id']}")
            if c != 200:
                sys.exit(f"GET {v['advert_id']} HTTP {c} — backup niepełny, przerywam")
            stan[str(v["advert_id"])] = r["data"]
        plik = os.path.join(D, "backups", f"olx-zdjecia-v4-przed-{time.strftime('%Y-%m-%d-%H%M')}.json")
        json.dump(stan, open(plik, "w", encoding="utf-8"), ensure_ascii=False)
        return print(f"backup: {len(stan)} ogłoszeń → {os.path.relpath(plik)}")

    if "--ids" in args:
        chce = {l.strip() for l in open(args[args.index("--ids") + 1]) if l.strip()}
        zadania = [z for z in zadania if str(z[1]["advert_id"]) in chce]
    elif "--all" not in args:
        sys.exit(__doc__)

    by_eid = {it["external_id"]: it for it in payload}
    ok = 0
    print(f"podmieniam zdjęcia w {len(zadania)} ogłoszeniach… (bezpiecznik co 25)")
    for i, (eid, v, g) in enumerate(zadania):
        if i:
            time.sleep(2)
        c, r = call("GET", f"/partner/adverts/{v['advert_id']}")
        if c != 200:
            print(f"  BŁĄD GET {v['advert_id']} HTTP {c}")
            continue
        zywe = r["data"]
        if zywe["location"].get("city_id") != v["city_id"]:
            print(f"  POMIJAM {v['advert_id']} — miasto na koncie ≠ rejestr")
            continue
        body = dict(putable(zywe), images=[{"url": u} for u in g], auto_extend_enabled=True)
        c, r = call("PUT", f"/partner/adverts/{v['advert_id']}", body)
        if c not in (200, 201):
            print(f"  BŁĄD PUT {v['advert_id']} HTTP {c}: {json.dumps(r, ensure_ascii=False)[:300]}")
            if ok == 0:
                sys.exit("pierwsza podmiana nie przeszła — przerywam")
            continue
        by_eid[eid]["images"] = [{"url": u} for u in g]
        json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        ok += 1
        print(f"  OK {v['advert_id']} {v['wariant']:<30} {v['city']:<20} {len(g)} zdj.")
        if ok % 25 == 0:
            zle = moderation_check(reg)
            if zle:
                opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
                notify(f"OLX AGRIA — STOP przy podmianie zdjęć v4 po {ok}:\n{opis}")
                sys.exit(f"STOP — moderacja:\n{opis}")
            print(f"  … bezpiecznik: {ok} podmienionych, zero odrzutów")
    zle = moderation_check(reg) if ok else []
    if zle:
        opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
        notify(f"OLX AGRIA — STOP na koniec podmiany zdjęć v4 ({ok}):\n{opis}")
        sys.exit(f"STOP — moderacja:\n{opis}")
    print(f"podmienione: {ok}/{len(zadania)}, zero odrzutów")


if __name__ == "__main__":
    main()
