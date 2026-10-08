#!/usr/bin/env python3
"""Cykl 3 (08.10.2026): T-150 tytuły i opisy zgodne z kartami + T-152 test „kreda do stawu”.

Reguły per ogłoszenie z data/olx/plan-cykl-3/tytuly-dry-run.json (stary → nowy tytuł, frazy opisu),
wysyłka tym samym mechanizmem co tresc.py: GET → putable() → podmiana dokładnych fraz → PUT → GET
(telefon, tytuł, opis, miasto). Fraza, która nie trafia, zatrzymuje to ogłoszenie.

    tresc_cykl3.py [--wsad plik.json] --dry-run | --pilot N | --all

Każda seria (pole `seria` we wsadzie) ma własny znacznik w posted.json — T-163 (opis „skąd wysyłamy”,
wsad data/olx/plan-cykl-3/t163-opis-wysylka.json) nie pomija ogłoszeń zmienionych wcześniej tego dnia.
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import call, putable, load_posted, save_posted, moderation_check, D  # noqa: E402
from tresc import zastosuj, put_i_sprawdz, sprawdz_ladunek, PAYLOAD, PAUZA, GUARD  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
WSAD = os.path.join(REPO, "data", "olx", "plan-cykl-3", "tytuly-dry-run.json")
BACKUP = os.path.join(REPO, "data", "backups", "olx-tresc-przed-2026-10-08.json")
DATA = "2026-10-08"


def main():
    a = sys.argv[1:]
    dry = "--dry-run" in a
    lim = int(a[a.index("--pilot") + 1]) if "--pilot" in a else None
    if not (dry or lim or "--all" in a):
        sys.exit(__doc__)
    wsad = json.load(open(a[a.index("--wsad") + 1] if "--wsad" in a else WSAD, encoding="utf-8"))
    reg = load_posted()
    payload = json.load(open(PAYLOAD, encoding="utf-8"))
    pidx = {p["external_id"]: p for p in payload}
    backup = json.load(open(BACKUP, encoding="utf-8")) if os.path.exists(BACKUP) else {}
    by_aid = {v["advert_id"]: k for k, v in reg.items()}
    todo = [w for w in wsad if reg[by_aid[w["advert_id"]]].get(w["seria"]) != DATA][:lim]
    print(f"do poprawy: {len(todo)} ogłoszeń{' (dry-run)' if dry else ''}\n")
    ok = 0
    for i, w in enumerate(todo):
        aid, klucz = w["advert_id"], by_aid[w["advert_id"]]
        if i and not dry:
            time.sleep(PAUZA)
        code, resp = call("GET", f"/partner/adverts/{aid}")
        if code != 200:
            print(f"  BŁĄD {aid} GET HTTP {code}")
            continue
        stan = resp["data"]
        body = putable(stan)
        reguly = [("title", w["stary_tytul"], w["nowy_tytul"])] + [("description", s, n) for s, n in w["opis"]]
        blad = zastosuj(body, reguly)
        if not blad and len(body["title"]) > 150:
            blad = f"tytuł {len(body['title'])} > 150 znaków"
        braki = None if blad else sprawdz_ladunek(body, aid)
        if blad or braki:
            print(f"  POMIJAM {aid} {w['seria']} {w['miasto']}: {blad or '; '.join(braki)}")
            continue
        if dry:
            ok += 1
            continue
        backup.setdefault(str(aid), stan)
        json.dump(backup, open(BACKUP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        po, bledy = put_i_sprawdz(aid, body, {"title": body["title"], "description": body["description"]})
        print(f"  {'OK  ' if not bledy else 'UWAGA'} {aid} {w['seria']} {w['wariant']:<28} {w['miasto']:<20}"
              f" {po.get('status') if po else ''} {bledy}")
        if po is None or "TELEFONU" in bledy:
            save_posted(reg)
            sys.exit("STOP — ogłoszenie bez PUT albo bez telefonu")
        reg[klucz].update({"title": body["title"], "tresc": DATA, w["seria"]: DATA})
        if klucz in pidx:
            pidx[klucz].update(title=body["title"], description=body["description"])
        save_posted(reg)
        json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        ok += 1
        if ok % GUARD == 0:
            zle = moderation_check(reg)
            if zle:
                sys.exit(f"STOP — moderacja wstrzymała {len(zle)}: {zle}")
            print(f"  … bezpiecznik: {ok}, zero odrzutów")
    print(f"\n{'do wysłania' if dry else 'poprawione'}: {ok}/{len(todo)}")


if __name__ == "__main__":
    main()
