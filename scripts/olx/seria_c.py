#!/usr/bin/env python3
"""Seria C (11.09.2026): marka AGRIA w tytułach + przełożenie 9 martwych ogłoszeń na najtańsze produkty.

1. --agria     : 191 ogłoszeń — do tytułu dopisane „, AGRIA" (decyzja Janka 11.09: budowa marki,
                 skojarzenie AGRIA–wapno w indeksowanych, długo żyjących ogłoszeniach). Dwa tytuły
                 przekraczały 150 znaków, więc skrócone: „2-4 tygodnie" → „2-4 tyg.", „na hektar" → „na ha".
                 GET → putable() → podmiana samego `title` → PUT. Reszta ogłoszenia bez zmian.
2. --przeloz   : 9 ogłoszeń z zerem odsłon (pomiar 11.09 12:08) → węglanowo-magnezowe odm. 05
                 i węglanowe odm. 04, miejscowości w świętokrzyskim blisko kopalni (Łagów, Celiny),
                 bez innych ogłoszeń AGRII. Treść, zdjęcia, cena i atrybuty z istniejącego ogłoszenia
                 docelowego wariantu, nowy tytuł, nowy `external_id` (jak seria B z 28.08).
                 Cena NIE w tytule — decyzja 20.08 po wstrzymaniu pilota przez moderację.

    seria_c.py --dry-run
    seria_c.py --przeloz [--limit N]
    seria_c.py --agria [--limit N]
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import call, putable, load_posted, save_posted, moderation_check, notify, PAYLOAD  # noqa: E402

DZIS = "2026-09-11"
SKROTY = [("efekt w 2-4 tygodnie", "efekt w 2-4 tyg."), ("mniejsza dawka na hektar", "mniejsza dawka na ha")]
TYTUL = {
    "weglanowe-magnez-odmiana-05": "Wapno nawozowe magnezowe w niskiej cenie, odmiana 05, luzem 24 t, "
                                   "odkwaszanie gleby i magnez w jednym zabiegu, atest OSChR, AGRIA",
    "weglanowe-odmiana-04": "Wapno nawozowe węglanowe w niskiej cenie, kreda do odkwaszania gleby, "
                            "odmiana 04, luzem 24 t, atest OSChR, AGRIA",
}
# advert_id: (nowy wariant, city_id, miasto)
PRZELOZ = {
    1092691910: ("weglanowe-magnez-odmiana-05", 64115, "Iwaniska"),
    1092691718: ("weglanowe-magnez-odmiana-05", 4837, "Daleszyce"),
    1092698451: ("weglanowe-magnez-odmiana-05", 42421, "Bodzentyn"),
    1092696837: ("weglanowe-magnez-odmiana-05", 144407, "Szydłów"),
    1092698639: ("weglanowe-magnez-odmiana-05", 55391, "Staszów"),
    1092691851: ("weglanowe-odmiana-04", 65413, "Kije"),
    1092691659: ("weglanowe-odmiana-04", 3997, "Busko-Zdrój"),
    1092691599: ("weglanowe-odmiana-04", 52521, "Pińczów"),
    1092696537: ("weglanowe-odmiana-04", 76513, "Wiślica"),
}


def tytul_agria(t):
    if t.endswith(", AGRIA"):
        return t
    for a, b in SKROTY:
        t = t.replace(a, b)
    t = t + ", AGRIA"
    assert len(t) <= 150, (len(t), t)
    return t


def wzorce(payload, reg):
    """Po jednym ogłoszeniu wariantu A i B dla każdego docelowego produktu."""
    out = {}
    for it in payload:
        w = reg[it["external_id"]]["wariant"]
        if w in TYTUL:
            ab = "B" if it["images"][1]["url"].endswith("-b.jpg") else "A"
            out.setdefault((w, ab), it)
    return out


def zapisz(reg, payload):
    save_posted(reg)
    json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def kontrola(reg, ok):
    if not ok:
        return
    zle = moderation_check(reg)
    if zle:
        opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
        notify(f"OLX AGRIA — STOP w serii C po {ok}:\n{opis}")
        sys.exit(f"STOP — moderacja:\n{opis}")
    print("kontrola moderacji: zero odrzutów")


def cmd_przeloz(limit, dry):
    reg, payload = load_posted(), json.load(open(PAYLOAD, encoding="utf-8"))
    wz = wzorce(payload, reg)
    by_aid = {v["advert_id"]: k for k, v in reg.items()}
    ok, licznik = 0, {}
    for aid, (w, cid, miasto) in list(PRZELOZ.items())[:limit]:
        stary = by_aid.get(aid)
        if not stary or (reg[stary]["wariant"] == w and reg[stary]["city_id"] == cid):
            # 11.09: bez drugiego warunku ponowne uruchomienie przepuściło już przełożone
            # ogłoszenie i nadpisało mu `poprzedni_external_id` nowym kluczem
            print(f"  POMIJAM {aid} — już przełożone")
            continue
        ab = "AB"[licznik.get(w, 0) % 2]
        licznik[w] = licznik.get(w, 0) + 1
        t = wz[(w, ab)]
        nowy = f"agria-{w}-{cid}"
        print(f"  {aid} {reg[stary]['wariant']:<22} {reg[stary]['city']:<18} → {w:<28} {miasto:<12} {ab}")
        if dry:
            continue
        c, r = call("GET", f"/partner/adverts/{aid}")
        if c != 200:
            sys.exit(f"GET {aid} HTTP {c}")
        body = dict(putable(r["data"]), title=TYTUL[w], description=t["description"],
                    images=t["images"], price=t["price"], attributes=t["attributes"],
                    external_id=nowy, location={"city_id": cid})
        c, r = call("PUT", f"/partner/adverts/{aid}", dict(body, auto_extend_enabled=True))
        if c not in (200, 201):
            print(f"  BŁĄD PUT {aid} HTTP {c}: {json.dumps(r, ensure_ascii=False)[:300]}")
            break
        c, r = call("GET", f"/partner/adverts/{aid}")
        po = r.get("data", {}) if c == 200 else {}
        uw = []
        if po.get("external_id") != nowy: uw.append(f"external_id {po.get('external_id')!r}")
        if po.get("location", {}).get("city_id") != cid: uw.append("city_id")
        if not (po.get("contact") or {}).get("phone"): uw.append("BRAK TELEFONU — WYCOFAĆ")
        if po.get("title") != TYTUL[w]: uw.append("tytuł")
        print(f"     {'OK' if not uw else 'UWAGA ' + '; '.join(uw)} · {po.get('status')}")
        if "BRAK TELEFONU" in " ".join(uw):
            break
        wpis = dict(reg.pop(stary), city=miasto, city_id=cid, wariant=w, title=TYTUL[w],
                    sku=t["_meta"]["sku"], poprzedni_external_id=stary, przelozone=DZIS)
        reg[nowy] = wpis
        payload = [p for p in payload if p["external_id"] != stary]
        payload.append({k: v for k, v in body.items()} | {"_meta": dict(t["_meta"], city=miasto)})
        zapisz(reg, payload)
        ok += 1
        time.sleep(2)
    print(f"przełożone: {ok}")
    kontrola(reg, ok)


def cmd_agria(limit, dry):
    reg, payload = load_posted(), json.load(open(PAYLOAD, encoding="utf-8"))
    todo = [it for it in payload if not it["title"].endswith(", AGRIA")][:limit]
    print(f"AGRIA w tytule: {len(todo)} ogłoszeń")
    ok = 0
    for i, it in enumerate(todo):
        v = reg[it["external_id"]]
        nowy = tytul_agria(it["title"])
        if dry:
            continue
        if i:
            time.sleep(2)
        c, r = call("GET", f"/partner/adverts/{v['advert_id']}")
        if c != 200:
            print(f"  BŁĄD GET {v['advert_id']} HTTP {c}")
            continue
        if r["data"]["location"].get("city_id") != v["city_id"]:
            print(f"  POMIJAM {v['advert_id']} — miasto na koncie ≠ rejestr")
            continue
        c, r = call("PUT", f"/partner/adverts/{v['advert_id']}",
                    dict(putable(r["data"]), title=nowy, auto_extend_enabled=True))
        if c not in (200, 201):
            print(f"  BŁĄD PUT {v['advert_id']} HTTP {c}: {json.dumps(r, ensure_ascii=False)[:300]}")
            if ok == 0:
                sys.exit("pierwsza zmiana nie przeszła — przerywam")
            continue
        it["title"] = nowy
        v["title"] = nowy
        zapisz(reg, payload)
        ok += 1
        print(f"  OK {v['advert_id']} {v['city']:<20} {len(nowy)} zn.", flush=True)
        if ok % 25 == 0:
            kontrola(reg, ok)
    if dry:
        dl = sorted({len(tytul_agria(it["title"])) for it in todo})
        return print(f"długości po zmianie: {dl[0]}–{dl[-1]} zn. — nic nie wysłane")
    print(f"AGRIA dopisana: {ok}/{len(todo)}")
    kontrola(reg, ok)


if __name__ == "__main__":
    a = sys.argv[1:]
    lim = int(a[a.index("--limit") + 1]) if "--limit" in a else None
    dry = "--dry-run" in a
    if "--przeloz" in a or dry:
        cmd_przeloz(lim, dry)
    if "--agria" in a or dry:
        cmd_agria(lim, dry)
