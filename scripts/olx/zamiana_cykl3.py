#!/usr/bin/env python3
"""T-151 + T-155 (08.10.2026): 15 ogłoszeń bez odsłon numeru → Agrobielik 70 gleba, zmiana produktu w miejscu.

Decyzja z rozmowy z Pawłem (ADR docs/decyzje/2026-10-08-olx-tlenek-wysylka-z-magazynow.md): połowa kredy
i 4 × węglanowe z Mg odm. 04 idą na tlenek. Uogólnienie tresc.py --t146. Treść, cena, atrybuty i galeria
z żywego ogłoszenia Agrobielika 70 (wszystkie 32 mają ten sam tytuł i opis); front ze sceny Agrobielika 70,
której nie ma inne takie ogłoszenie w promieniu 100 km (bez `wysyp-podworze` — audyt 23.09). Gdy w szkicu
miasto docelowe jest inne niż obecne, zmienia się też `location.city_id`. Reszta ładunku z GET (putable).
Lista: data/olx/plan-cykl-3/seria-45-szkic.json, seria „zamiana→A70”.

    zamiana_cykl3.py --dry-run | --pilot N | --all
"""
import json, os, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import call, putable, load_posted, save_posted, moderation_check, D  # noqa: E402
from tresc import put_i_sprawdz, sprawdz_ladunek, PAYLOAD, PAUZA  # noqa: E402
from fronty_v5 import km  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
WSAD = os.path.join(REPO, "data", "olx", "plan-cykl-3", "seria-45-szkic.json")
BACKUP = os.path.join(REPO, "data", "backups", "olx-zamiana-przed-2026-10-08.json")
DATA = "2026-10-08"
NOWY = "agrobielik-70-gleba"


def main():
    a = sys.argv[1:]
    dry = "--dry-run" in a
    lim = int(a[a.index("--pilot") + 1]) if "--pilot" in a else None
    if not (dry or lim or "--all" in a):
        sys.exit(__doc__)
    reg = load_posted()
    payload = json.load(open(PAYLOAD, encoding="utf-8"))
    pidx = {p["external_id"]: p for p in payload}
    backup = json.load(open(BACKUP, encoding="utf-8")) if os.path.exists(BACKUP) else {}
    miasta = {c["id"]: c for c in json.load(open(os.path.join(D, "cities-all.json"), encoding="utf-8"))}
    geo = lambda i: (miasta[i]["latitude"], miasta[i]["longitude"])
    by_aid = {v["advert_id"]: k for k, v in reg.items()}

    a70 = [k for k, v in reg.items() if v["wariant"] == NOWY and k in pidx]
    wz = a70[0]
    code, resp = call("GET", f"/partner/adverts/{reg[wz]['advert_id']}")
    wzor = putable(resp["data"])
    galeria = Counter(tuple(i["url"] for i in pidx[k]["images"][1:]) for k in a70).most_common(1)[0][0]
    sceny = sorted({pidx[k]["images"][0]["url"] for k in a70} - {u for u in (pidx[k]["images"][0]["url"] for k in a70)
                                                                  if "wysyp-podworze" in u})
    sku = reg[wz]["sku"]

    def front(city_id):
        zajete = [(pidx[k]["images"][0]["url"], pidx[k]["location"]["city_id"]) for k in a70]
        def kara(u):
            return sum(max(0.0, 1 - km(geo(city_id), geo(c)) / 100) for f, c in zajete if f == u)
        return min(sceny, key=lambda u: (kara(u), sceny.index(u)))

    todo = [w for w in json.load(open(WSAD, encoding="utf-8"))
            if w["seria"] == "zamiana→A70" and w["advert_id"] in by_aid
            and reg[by_aid[w["advert_id"]]]["wariant"] != NOWY][:lim]
    print(f"zamiana → {NOWY}: {len(todo)} ogłoszeń, wzorzec {reg[wz]['advert_id']} ({reg[wz]['city']}), sku {sku}"
          f"{' (dry-run)' if dry else ''}\n")
    for i, w in enumerate(todo):
        aid = w["advert_id"]
        stary = by_aid[aid]
        if i and not dry:
            time.sleep(PAUZA)
        code, resp = call("GET", f"/partner/adverts/{aid}")
        stan = resp["data"]
        body = putable(stan)
        for pole in ("title", "description", "price", "attributes", "category_id"):
            if pole in wzor:
                body[pole] = wzor[pole]
        if w["city_id"] != body["location"]["city_id"]:
            body["location"] = {"city_id": w["city_id"]}
        cid = body["location"]["city_id"]
        body["images"] = [{"url": front(cid)}] + [{"url": u} for u in galeria]
        nowy = f"agria-{NOWY}-{cid}"
        while nowy in reg:
            nowy += "-b"
        body["external_id"] = nowy
        braki = sprawdz_ladunek(body, aid)
        if braki:
            print(f"  POMIJAM {aid}: {'; '.join(braki)}")
            continue
        print(f"  {'PLAN' if dry else '...'} {aid} {reg[stary]['wariant'][:26]:<26} {reg[stary]['city']:<20} → "
              f"{miasta[cid]['name']:<20} front {body['images'][0]['url'].rsplit('/', 1)[-1]}")
        if dry:
            continue
        backup.setdefault(str(aid), stan)
        json.dump(backup, open(BACKUP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        po, bledy = put_i_sprawdz(aid, body, {"title": body["title"], "external_id": nowy})
        print(f"  {'OK  ' if not bledy else 'UWAGA'} {aid} {po.get('status') if po else ''} {bledy}")
        if po is None or "TELEFONU" in bledy:
            sys.exit("STOP")
        reg[nowy] = dict(reg.pop(stary), wariant=NOWY, sku=sku, title=body["title"], city=miasta[cid]["name"],
                         city_id=cid, poprzedni_external_id=stary, zmiana_produktu=DATA, tresc=DATA)
        meta = dict(pidx.get(stary, {}).get("_meta", {}), karta=NOWY, sku=sku, siatka=NOWY, city=miasta[cid]["name"])
        payload[:] = [p for p in payload if p["external_id"] != stary]
        payload.append(dict(body, _meta=meta))
        pidx = {p["external_id"]: p for p in payload}
        a70.append(nowy)
        save_posted(reg)
        json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not dry:
        zle = moderation_check(reg)
        print("kontrola moderacji:", "zero odrzutów" if not zle else zle)


if __name__ == "__main__":
    main()
