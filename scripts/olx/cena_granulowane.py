#!/usr/bin/env python3
"""Obniżka ceny granulatów węglanowych na OLX (13.10.2026, prośba Pawła): 350 → 250 i 370 → 260 zł/t.

Tylko OLX — karty agria.pl, Ads, worki 25 kg i ofertownik bez zmian (decyzja Janka 13.10).
Mechanizm jak tresc_cykl3.py: GET → putable() → pole ceny + linia opisu → PUT → GET.
Fraza opisu, która nie trafia, zatrzymuje to ogłoszenie.

    cena_granulowane.py --dry-run | --pilot N | --all
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import call, putable, load_posted, save_posted, moderation_check  # noqa: E402
from tresc import zastosuj, put_i_sprawdz, sprawdz_ladunek, PAYLOAD, PAUZA, GUARD  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
BACKUP = os.path.join(REPO, "data", "backups", "olx-cena-granulowane-przed-2026-10-13.json")
DATA = "2026-10-13"
SERIA = "cena"
CENY = {  # wariant (z posted.json) → (stara, nowa)
    "weglanowe-granulowane": (350, 250),
    "weglanowe-magnez-granulowane": (370, 260),
}


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
    todo = [(k, v) for k, v in reg.items() if v.get("wariant") in CENY and v.get(SERIA) != DATA][:lim]
    print(f"do zmiany: {len(todo)} ogłoszeń{' (dry-run)' if dry else ''}\n")
    ok = 0
    for i, (klucz, w) in enumerate(todo):
        aid = w["advert_id"]
        stara, nowa = CENY[w["wariant"]]
        if i and not dry:
            time.sleep(PAUZA)
        code, resp = call("GET", f"/partner/adverts/{aid}")
        if code != 200:
            print(f"  BŁĄD {aid} GET HTTP {code}")
            continue
        stan = resp["data"]
        body = putable(stan)
        blad = None
        if str(body.get("price", {}).get("value")) != str(stara):
            blad = f"cena na koncie {body.get('price', {}).get('value')}, oczekiwana {stara}"
        else:
            body["price"]["value"] = nowa
            blad = zastosuj(body, [("description", f"od {stara} zł/t — cena za towar", f"od {nowa} zł/t — cena za towar")])
        braki = None if blad else sprawdz_ladunek(body, aid)
        if blad or braki:
            print(f"  POMIJAM {aid} {w['wariant']} {w['city']}: {blad or '; '.join(braki)}")
            continue
        if dry:
            ok += 1
            continue
        backup.setdefault(str(aid), stan)
        os.makedirs(os.path.dirname(BACKUP), exist_ok=True)
        json.dump(backup, open(BACKUP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        po, bledy = put_i_sprawdz(aid, body, {"description": body["description"]})
        if po and str((po.get("price") or {}).get("value")) != str(nowa):
            bledy = "; ".join(filter(None, [bledy, "cena na koncie inna niż wysłana"]))
        print(f"  {'OK  ' if not bledy else 'UWAGA'} {aid} {w['wariant']:<30} {w['city']:<20}"
              f" {po.get('status') if po else ''} {bledy}")
        if po is None or "TELEFONU" in bledy:
            save_posted(reg)
            sys.exit("STOP — ogłoszenie bez PUT albo bez telefonu")
        reg[klucz][SERIA] = DATA
        if klucz in pidx:
            pidx[klucz]["price"]["value"] = nowa
            pidx[klucz]["description"] = body["description"]
        save_posted(reg)
        json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        ok += 1
        if ok % GUARD == 0:
            zle = moderation_check(reg)
            if zle:
                sys.exit(f"STOP — moderacja wstrzymała {len(zle)}: {zle}")
            print(f"  … bezpiecznik: {ok}, zero odrzutów")
    print(f"\n{'do wysłania' if dry else 'zmienione'}: {ok}/{len(todo)}")


if __name__ == "__main__":
    main()
