#!/usr/bin/env python3
"""Wystawia ogłoszenia AGRII na OLX przez Partner API + pilnuje auto_extend.

To pisze na koncie klienta. Domyślnie NIC nie wysyła — trzeba świadomie podać tryb.

    post_adverts.py --dry-run              podgląd, zero ruchu do OLX
    post_adverts.py --pilot 1              wystaw N pierwszych (pilot przed masówką)
    post_adverts.py --all                  wystaw resztę z ładunku
    post_adverts.py --auto-extend          włącz auto_extend na WSZYSTKICH ogłoszeniach konta
    post_adverts.py --status               co już wystawione wg lokalnego rejestru

Rejestr wystawionych: data/olx/posted.json (external_id → advert_id). Skrypt nigdy nie
wystawia drugi raz tego samego external_id — można go bezpiecznie uruchomić ponownie.

Uwaga o auto_extend: to on zdecydował, że konto zgasło 18.07 — był włączony na 1 z 20 ogłoszeń.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")
PAYLOAD = os.path.join(D, "adverts-payload.json")
POSTED = os.path.join(D, "posted.json")
HELPER = os.path.expanduser("~/bin/olx-agria")
API = "https://www.olx.pl/api"


def token():
    tk = os.path.expanduser("~/domains/auratest.pl/olx-private/agria-tokens.json")
    return json.load(open(tk))["access_token"]


def call(method, path, body=None):
    cmd = ["curl", "-sS", "-X", method, API + path,
           "-H", f"Authorization: Bearer {token()}",
           "-H", "Version: 2.0", "-H", "Content-Type: application/json",
           "-w", "\n%{http_code}"]
    if body is not None:
        cmd += ["-d", json.dumps(body, ensure_ascii=False)]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    raw, _, code = out.rpartition("\n")
    try:
        return int(code), json.loads(raw)
    except json.JSONDecodeError:
        return int(code), {"raw": raw}


def load_posted():
    return json.load(open(POSTED, encoding="utf-8")) if os.path.exists(POSTED) else {}


def save_posted(reg):
    json.dump(reg, open(POSTED, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def post_one(item):
    body = {k: v for k, v in item.items() if not k.startswith("_")}
    code, resp = call("POST", "/partner/adverts", body)
    if code not in (200, 201):
        return None, f"HTTP {code}: {json.dumps(resp, ensure_ascii=False)[:400]}"
    advert_id = (resp.get("data") or {}).get("id")
    if not advert_id:
        return None, f"brak id w odpowiedzi: {json.dumps(resp, ensure_ascii=False)[:300]}"
    # auto_extend od razu — inaczej ogłoszenie cicho wygaśnie po 30 dniach
    call("PUT", f"/partner/adverts/{advert_id}", {"auto_extend_enabled": True})
    return advert_id, None


def cmd_dry(items, reg):
    for i, it in enumerate(items, 1):
        mark = "JUŻ WYSTAWIONE" if it["external_id"] in reg else "do wystawienia"
        print(f"{i:>4}. [{mark}] {it['_meta']['city']:<22} {it['title'][:58]}")
        print(f"      cena {it['price']['value']} zł · zdjęć {len(it['images'])} · "
              f"opis {len(it['description'])} zn. · kat {it['category_id']} · {it['external_id']}")
    nowe = sum(1 for it in items if it["external_id"] not in reg)
    print(f"\nrazem w ładunku: {len(items)} | do wystawienia: {nowe} | już na koncie: {len(items)-nowe}")
    print("nic nie zostało wysłane do OLX (--dry-run)")


def cmd_post(items, reg, limit):
    todo = [it for it in items if it["external_id"] not in reg][:limit]
    if not todo:
        return print("nic do wystawienia — wszystko z ładunku jest już w rejestrze")
    print(f"wystawiam {len(todo)} ogłoszeń…")
    ok = 0
    for it in todo:
        advert_id, err = post_one(it)
        if err:
            print(f"  BŁĄD  {it['_meta']['city']:<20} {it['title'][:44]}\n        {err}")
            if ok == 0:
                sys.exit("pierwsze ogłoszenie nie przeszło — przerywam, żeby nie mnożyć błędów")
            continue
        reg[it["external_id"]] = {"advert_id": advert_id, "title": it["title"],
                                  "city": it["_meta"]["city"], "sku": it["_meta"]["sku"]}
        save_posted(reg)
        ok += 1
        print(f"  OK    {advert_id}  {it['_meta']['city']:<20} {it['title'][:44]}")
    print(f"\nwystawione: {ok}/{len(todo)}. Rejestr: {os.path.relpath(POSTED)}")


def cmd_auto_extend():
    code, resp = call("GET", "/partner/adverts?limit=100")
    if code != 200:
        sys.exit(f"nie mogę pobrać listy ogłoszeń: HTTP {code}")
    adverts = resp["data"]
    off = [a for a in adverts if not a.get("auto_extend_enabled") and a["category_id"] != 15]
    print(f"ogłoszeń na koncie: {len(adverts)} | bez auto_extend: {len(off)}")
    for a in off:
        c, r = call("PUT", f"/partner/adverts/{a['id']}", {"auto_extend_enabled": True})
        stan = "OK" if c in (200, 201) else f"BŁĄD HTTP {c}"
        print(f"  {stan:<12} {a['id']}  {a['title'][:52]}")


if __name__ == "__main__":
    args = sys.argv[1:]
    items = json.load(open(PAYLOAD, encoding="utf-8"))
    reg = load_posted()

    if "--status" in args:
        print(f"w rejestrze: {len(reg)} ogłoszeń")
        for eid, v in reg.items():
            print(f"  {v['advert_id']:>12}  {v['city']:<22} {v['title'][:52]}")
    elif "--auto-extend" in args:
        cmd_auto_extend()
    elif "--pilot" in args:
        n = int(args[args.index("--pilot") + 1])
        cmd_post(items, reg, n)
    elif "--all" in args:
        cmd_post(items, reg, len(items))
    elif "--dry-run" in args:
        cmd_dry(items, reg)
    else:
        sys.exit(__doc__)
