#!/usr/bin/env python3
"""Wystawia ogłoszenia AGRII na OLX przez Partner API + pilnuje auto_extend.

To pisze na koncie klienta. Domyślnie NIC nie wysyła — trzeba świadomie podać tryb.

    post_adverts.py --dry-run              podgląd, zero ruchu do OLX
    post_adverts.py --pilot 1              wystaw N pierwszych (pilot przed masówką)
    post_adverts.py --all                  wystaw resztę z ładunku
    post_adverts.py --ids plik.txt         wystaw tylko wskazane external_id (po jednym w linii)
    post_adverts.py --check                rozkład statusów ogłoszeń z rejestru wg API
    post_adverts.py --update [--limit N]    wgraj aktualną treść na już wystawione ogłoszenia
    post_adverts.py --auto-extend          włącz auto_extend na WSZYSTKICH ogłoszeniach konta
    post_adverts.py --status               co już wystawione wg lokalnego rejestru

Rejestr wystawionych: data/olx/posted.json (external_id → advert_id). Skrypt nigdy nie
wystawia drugi raz tego samego external_id — można go bezpiecznie uruchomić ponownie.

Bezpiecznik moderacyjny: przy --all/--ids co N ogłoszeń (--guard N, domyślnie 20) skrypt czyta
GET /partner/adverts i przerywa serię, gdy którekolwiek ogłoszenie z rejestru ma status
moderated/blocked — a `disabled` dopiero, gdy utrzyma się ponad 5 minut, bo tuż po POST jest
stanem przejściowym (moderacja przepuszcza ogłoszenie na `active` po ~2-3 min).
POST zwraca sukces niezależnie od werdyktu, który przychodzi po fakcie i po cichu — bez
bezpiecznika można wypchnąć całość, zanim zobaczy się pierwszy odrzut.

Uwaga o auto_extend: to on zdecydował, że konto zgasło 18.07 — był włączony na 1 z 20 ogłoszeń.
"""
import json
import os
import subprocess
import sys
import time

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


def body_of(item):
    return {k: v for k, v in item.items() if not k.startswith("_")}


def post_one(item):
    body = body_of(item)
    code, resp = call("POST", "/partner/adverts", body)
    if code not in (200, 201):
        return None, f"HTTP {code}: {json.dumps(resp, ensure_ascii=False)[:400]}"
    advert_id = (resp.get("data") or {}).get("id")
    if not advert_id:
        return None, f"brak id w odpowiedzi: {json.dumps(resp, ensure_ascii=False)[:300]}"
    # auto_extend od razu — inaczej ogłoszenie cicho wygaśnie po 30 dniach.
    # PUT w tym API to podmiana całego zasobu, nie łatka: wysłanie samego
    # {"auto_extend_enabled": true} kończy się błędem walidacji na wszystkich
    # brakujących polach, a flaga zostaje na false. Stąd pełny ładunek.
    code, resp = call("PUT", f"/partner/adverts/{advert_id}",
                      dict(body, auto_extend_enabled=True))
    if code not in (200, 201):
        return advert_id, f"utworzone, ale auto_extend NIE wszedł: HTTP {code}"
    return advert_id, None


# Twardy odrzut moderacji — zatrzymuje serię natychmiast.
BAD = ("moderated", "blocked")
# Stan, który tuż po POST jest przejściowy: pomiar 20.08 na 42 ogłoszeniach — aktywacja
# przychodzi 2 min 14 s – 2 min 58 s po wystawieniu, a do tego czasu ogłoszenie potrafi
# stać w `disabled`. Alarmujemy dopiero, gdy utrzyma się dłużej niż KARENCJA.
PODEJRZANE = ("disabled", "unconfirmed", "unpaid")
KARENCJA = 300


def notify(text):
    """Telegram do Janka. Powiadomienie nigdy nie może wywrócić publikacji — stąd try."""
    try:
        d = os.path.expanduser("~/secrets/telegram")
        tok = open(os.path.join(d, "bot-token.txt")).read().strip()
        chat = open(os.path.join(d, "chat-id.txt")).read().strip()
        subprocess.run(["curl", "-sS", "-o", "/dev/null",
                        f"https://api.telegram.org/bot{tok}/sendMessage",
                        "--data-urlencode", f"chat_id={chat}",
                        "--data-urlencode", f"text={text}"], check=False, timeout=30)
    except Exception as e:
        print(f"  (Telegram nie poszedł: {e})")


def account_statuses():
    """{advert_id: (status, wiek w sekundach)} dla całego konta — API paginuje po 100."""
    out, offset = {}, 0
    teraz = time.time()
    while True:
        code, resp = call("GET", f"/partner/adverts?limit=100&offset={offset}")
        if code != 200:
            print(f"  UWAGA: nie mogę odczytać statusów, HTTP {code}")
            return out
        page = resp.get("data") or []
        for a in page:
            try:
                wiek = teraz - time.mktime(time.strptime(a["created_at"], "%Y-%m-%d %H:%M:%S"))
            except (KeyError, ValueError):
                wiek = KARENCJA + 1
            out[a["id"]] = (a["status"], wiek)
        if len(page) < 100:
            return out
        offset += 100


def moderation_check(reg, recheck=150):
    """Zwraca listę (advert_id, status, opis) dla ogłoszeń z rejestru w złym statusie.

    Pomiar 20.08: świeżo wystawione ogłoszenie potrafi przez ~3 minuty siedzieć w `disabled`,
    zanim moderacja przepuści je na `active` (8/8 tak przeszło). Dlatego zły status
    potwierdzamy drugim odczytem po pauzie — inaczej bezpiecznik zatrzymuje serię na
    stanie przejściowym.
    """
    def zle():
        st = account_statuses()
        ours = {v["advert_id"]: v for v in reg.values()}
        out = []
        for aid, v in ours.items():
            status, wiek = st.get(aid, (None, 0))
            if status in BAD or (status in PODEJRZANE and wiek > KARENCJA):
                out.append((aid, status, f"{v['city']} {v['title'][:44]}"))
        return out

    pierwsze = zle()
    if not pierwsze or not recheck:
        return pierwsze
    print(f"  … {len(pierwsze)} ogłoszeń w złym statusie — sprawdzam ponownie za {recheck} s")
    time.sleep(recheck)
    return zle()


def cmd_check(reg):
    st = account_statuses()
    ours = {v["advert_id"]: v for v in reg.values()}
    licz = {}
    for aid in ours:
        k = st.get(aid, ("BRAK W API", 0))[0]
        licz[k] = licz.get(k, 0) + 1
    print(f"ogłoszeń w rejestrze: {len(ours)} | na koncie widocznych: {len(st)}")
    for k, v in sorted(licz.items(), key=lambda x: -x[1]):
        print(f"  {k:<16} {v}")
    for aid, v in ours.items():
        status = st.get(aid, ("BRAK W API", 0))[0]
        if status in BAD or status in PODEJRZANE or aid not in st:
            print(f"  !! {aid} {status:<12} {v['city']:<20} {v['title'][:44]}")


def cmd_dry(items, reg):
    for i, it in enumerate(items, 1):
        mark = "JUŻ WYSTAWIONE" if it["external_id"] in reg else "do wystawienia"
        print(f"{i:>4}. [{mark}] {it['_meta']['city']:<22} {it['title'][:58]}")
        print(f"      cena {it['price']['value']} zł · zdjęć {len(it['images'])} · "
              f"opis {len(it['description'])} zn. · kat {it['category_id']} · {it['external_id']}")
    nowe = sum(1 for it in items if it["external_id"] not in reg)
    print(f"\nrazem w ładunku: {len(items)} | do wystawienia: {nowe} | już na koncie: {len(items)-nowe}")
    print("nic nie zostało wysłane do OLX (--dry-run)")


def cmd_post(items, reg, limit, guard=20):
    todo = [it for it in items if it["external_id"] not in reg][:limit]
    if not todo:
        return print("nic do wystawienia — wszystko z ładunku jest już w rejestrze")
    print(f"wystawiam {len(todo)} ogłoszeń… (bezpiecznik moderacyjny co {guard})")
    ok = 0
    for i, it in enumerate(todo):
        if i:
            time.sleep(2)   # limitów API nikt nie udokumentował — nie strzelamy serią bez przerw
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
        if guard and ok % guard == 0:
            zle = moderation_check(reg)
            if zle:
                opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
                print(f"\nSTOP — moderacja odrzuciła {len(zle)} ogłoszeń:\n{opis}")
                notify(f"OLX AGRIA — STOP po {ok} ogłoszeniach.\n"
                       f"Moderacja wstrzymała {len(zle)}:\n{opis}\n"
                       f"Seria przerwana, reszta niewystawiona.")
                sys.exit(1)
            print(f"  … bezpiecznik: {ok} wystawionych, zero odrzutów")
    print(f"\nwystawione: {ok}/{len(todo)}. Rejestr: {os.path.relpath(POSTED)}")
    # Kontrola końcowa: seria krótsza od --guard nie trafiłaby w sprawdzenie w pętli,
    # a partia po produkcie zwykle ma mniej niż N ogłoszeń.
    if ok:
        zle = moderation_check(reg)
        if zle:
            opis = "\n".join(f"{a} {st} — {t}" for a, st, t in zle)
            print(f"STOP — moderacja odrzuciła {len(zle)} ogłoszeń:\n{opis}")
            notify(f"OLX AGRIA — STOP na koniec partii ({ok} wystawionych).\n"
                   f"Moderacja wstrzymała {len(zle)}:\n{opis}")
            sys.exit(1)
        print("kontrola końcowa: zero odrzutów")


PUT_FIELDS = ("title", "description", "category_id", "advertiser_type", "external_id",
              "external_url", "contact", "location", "images", "price", "attributes", "courier")


def putable(advert):
    """Przerabia odpowiedź GET na ładunek akceptowany przez PUT (PUT podmienia cały zasób)."""
    body = {}
    for f in PUT_FIELDS:
        if advert.get(f) is None:
            continue
        v = advert[f]
        if f == "location":
            v = {k: v[k] for k in ("city_id", "district_id") if v.get(k) is not None}
        elif f == "images":
            v = [{"url": i["url"]} for i in v]
        elif f == "attributes":
            v = [{"code": a["code"], "value": a.get("value")} for a in v if a.get("value")]
        elif f == "price":
            v = {k: v[k] for k in ("value", "currency", "negotiable") if k in v}
        body[f] = v
    return body


def cmd_auto_extend():
    code, resp = call("GET", "/partner/adverts?limit=100")
    if code != 200:
        sys.exit(f"nie mogę pobrać listy ogłoszeń: HTTP {code}")
    adverts = resp["data"]
    # kategoria 15 to prywatne ogłoszenie Pawła (mieszkanie) — nie dotykamy go
    off = [a for a in adverts if not a.get("auto_extend_enabled") and a["category_id"] != 15]
    print(f"ogłoszeń na koncie: {len(adverts)} | bez auto_extend: {len(off)}")
    for a in off:
        c, r = call("PUT", f"/partner/adverts/{a['id']}", dict(putable(a), auto_extend_enabled=True))
        stan = "OK" if c in (200, 201) else f"BŁĄD HTTP {c}"
        print(f"  {stan:<12} {a['id']}  {a['title'][:52]}")
        if c not in (200, 201):
            print(f"               {json.dumps(r, ensure_ascii=False)[:300]}")


def cmd_update(items, reg, guard=25, limit=None):
    """Wgrywa aktualną treść z ładunku na ogłoszenia, które już są na koncie.

    Edycja przechodzi moderację tak samo jak nowe ogłoszenie, więc obowiązuje tu ten sam
    bezpiecznik co przy wystawianiu: co `guard` sztuk i na koniec serii czytamy statusy
    i przerywamy przy pierwszym twardym odrzucie.
    """
    by_eid = {it["external_id"]: it for it in items}
    todo = [(eid, v) for eid, v in reg.items() if eid in by_eid][:limit]
    print(f"aktualizuję {len(todo)} ogłoszeń z rejestru… (bezpiecznik co {guard})")
    ok = 0
    for i, (eid, v) in enumerate(todo):
        if i:
            time.sleep(2)
        it = by_eid[eid]
        c, r = call("PUT", f"/partner/adverts/{v['advert_id']}",
                    dict(body_of(it), auto_extend_enabled=True))
        stan = "OK" if c in (200, 201) else f"BŁĄD HTTP {c}"
        print(f"  {stan:<12} {v['advert_id']}  {v['city']:<20} {it['title'][:44]}")
        if c not in (200, 201):
            print(f"               {json.dumps(r, ensure_ascii=False)[:400]}")
            continue
        ok += 1
        if guard and ok % guard == 0:
            zle = moderation_check(reg)
            if zle:
                opis = "\n".join(f"{a} {st} — {t}" for a, st, t in zle)
                print(f"STOP — moderacja wstrzymała {len(zle)}:\n{opis}")
                notify(f"OLX AGRIA — STOP przy podmianie zdjęć po {ok} sztukach:\n{opis}")
                sys.exit(1)
            print(f"  … bezpiecznik: {ok} zaktualizowanych, zero odrzutów")
    if ok:
        zle = moderation_check(reg)
        if zle:
            opis = "\n".join(f"{a} {st} — {t}" for a, st, t in zle)
            print(f"STOP — moderacja wstrzymała {len(zle)}:\n{opis}")
            notify(f"OLX AGRIA — STOP po podmianie {ok} sztuk:\n{opis}")
            sys.exit(1)
    print(f"zaktualizowane: {ok}/{len(todo)}, zero odrzutów")


if __name__ == "__main__":
    args = sys.argv[1:]
    items = json.load(open(PAYLOAD, encoding="utf-8"))
    reg = load_posted()

    guard = int(args[args.index("--guard") + 1]) if "--guard" in args else 20

    if "--check" in args:
        cmd_check(reg)
    elif "--status" in args:
        print(f"w rejestrze: {len(reg)} ogłoszeń")
        for eid, v in reg.items():
            print(f"  {v['advert_id']:>12}  {v['city']:<22} {v['title'][:52]}")
    elif "--auto-extend" in args:
        cmd_auto_extend()
    elif "--update" in args:
        lim = int(args[args.index("--limit") + 1]) if "--limit" in args else None
        wybrane = items
        if "--ids" in args:
            # bez tego filtru --update ignoruje listę i przechodzi po CAŁYM rejestrze:
            # 21.08 pętla po partiach zrobiła dwa pełne przebiegi po 200 ogłoszeń zamiast
            # dwóch partii po 25.
            chce = {l.strip() for l in open(args[args.index("--ids") + 1], encoding="utf-8")
                    if l.strip() and not l.startswith("#")}
            wybrane = [it for it in items if it["external_id"] in chce]
            if not wybrane:
                sys.exit("żaden external_id z pliku nie pasuje do ładunku")
        cmd_update(wybrane, reg, guard, lim)
    elif "--ids" in args:
        wanted = [l.strip() for l in open(args[args.index("--ids") + 1], encoding="utf-8")
                  if l.strip() and not l.startswith("#")]
        wybrane = [it for it in items if it["external_id"] in set(wanted)]
        brak = set(wanted) - {it["external_id"] for it in wybrane}
        if brak:
            sys.exit(f"external_id spoza ładunku: {sorted(brak)}")
        cmd_post(wybrane, reg, len(wybrane), guard)
    elif "--pilot" in args:
        n = int(args[args.index("--pilot") + 1])
        cmd_post(items, reg, n, guard)
    elif "--all" in args:
        cmd_post(items, reg, len(items), guard)
    elif "--dry-run" in args:
        cmd_dry(items, reg)
    else:
        sys.exit(__doc__)
