#!/usr/bin/env python3
"""Monitoring konkurencji na OLX — snapshot kategorii + różnica między snapshotami.

OLX nie udostępnia statystyk cudzych ogłoszeń, ale publiczne API wyszukiwania oddaje
`created_time` i `last_refresh_time` dla każdego ogłoszenia. To wystarczy, żeby zmierzyć
to, czego nie widać gołym okiem: jak często konkurenci odświeżają oferty, czy podmieniają
tytuły, czy przestawiają miejscowości i jak duża jest rotacja asortymentu.

    market_snapshot.py                       snapshot kat. 4368 (Nawozy) + 765 (Pozostałe)
    market_snapshot.py --diff A.json B.json  co się zmieniło między snapshotami
    market_snapshot.py --diff-last           dwa ostatnie snapshoty
    market_snapshot.py --profile             profile sprzedawców z ostatniego snapshotu
    market_snapshot.py --spis                SPIS rynku wapna: kat. 4368, „wapno”, per województwo
    market_snapshot.py --spis-diff A B       kto wszedł / wyszedł / urósł — po user_id, tylko spisy

⚠️ Snapshot domyślny to PRÓBKA, nie spis (T-145, 23.09.2026). OLX ucina paginację na offsecie
~1000, a crawl idzie od najnowszych — widać ~1200 najnowszych ogłoszeń na kategorię z ~17 000
(Nawozy) i ~35 000 (Pozostałe). Ogłoszenia AGRII z 20.08 wypadły z próbki do 23.09. Liczebność
sprzedawców i udziały licz WYŁĄCZNIE ze spisu (`--spis`): zapytanie „wapno” w kat. 4368 dzielone
na województwa mieści się pod limitem wszędzie poza mazowieckim (~1050 z ~1220 w 09.2026).
Z próbki wolno czytać tylko napływ nowych ogłoszeń. Tezy z cyklu 1 („AGRIA 2. sprzedawcą”,
„lider spadł 510 → 122”, „rynek −3,8%”) były artefaktem próbki — spis 23.09: AGRIA 8., lider 496.
"""
import collections
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import olx_market as m

HERE = os.path.dirname(os.path.abspath(__file__))
SNAPDIR = os.path.join(HERE, "..", "..", "data", "olx", "market")
KATEGORIE = {4368: "Nawozy", 765: "Pozostałe rolnicze"}


def zbierz():
    rows = []
    for cid, nazwa in KATEGORIE.items():
        print(f"kategoria {cid} ({nazwa})…", file=sys.stderr)
        for o in m.crawl(cid, max_pages=40, limit=50):
            u = o.get("user") or {}
            loc = o.get("location") or {}
            promo = o.get("promotion") or {}
            rows.append({
                "id": o["id"], "category_id": cid,
                "title": o.get("title"),
                "price": m.price_of(o)[0],
                "user_id": u.get("id"),
                "user": u.get("company_name") or u.get("name"),
                "city": (loc.get("city") or {}).get("name"),
                "region": (loc.get("region") or {}).get("name"),
                "created": o.get("created_time"),
                "refreshed": o.get("last_refresh_time"),
                "promoted": bool(promo.get("highlighted") or promo.get("top_ad")),
                "url": o.get("url"),
                "desc": (o.get("description") or "")[:800],
            })
    return rows


def zapisz(rows):
    now = datetime.now(timezone.utc).astimezone()
    os.makedirs(SNAPDIR, exist_ok=True)
    path = os.path.join(SNAPDIR, now.strftime("%Y-%m-%d") + ".json")
    json.dump({"taken_at": now.isoformat(timespec="seconds"), "offers": rows},
              open(path, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"snapshot: {os.path.relpath(path)} — {len(rows)} ogłoszeń, "
          f"{len({r['user_id'] for r in rows})} sprzedawców")
    return path


def wiek_odswiezenia(rows, teraz):
    """Ile dni temu ogłoszenie było ostatnio odświeżone — miara aktywności sprzedawcy."""
    out = []
    for r in rows:
        if not r.get("refreshed"):
            continue
        try:
            t = datetime.fromisoformat(r["refreshed"].replace("Z", "+00:00"))
        except ValueError:
            continue
        out.append((teraz - t).total_seconds() / 86400)
    return out


def profile(path=None):
    path = path or sorted(os.path.join(SNAPDIR, f) for f in os.listdir(SNAPDIR))[-1]
    snap = json.load(open(path, encoding="utf-8"))
    rows = snap["offers"]
    teraz = datetime.fromisoformat(snap["taken_at"])
    print(f"snapshot {snap['taken_at']}, {len(rows)} ogłoszeń\n")
    print(f"{'sprzedawca':<26}{'ogł':>5}{'tyt':>5}{'miast':>7}{'promo':>7}"
          f"{'mediana dni od odświeżenia':>28}")
    by = collections.Counter(r["user_id"] for r in rows)
    for uid, n in by.most_common(12):
        mine = [r for r in rows if r["user_id"] == uid]
        wieki = sorted(wiek_odswiezenia(mine, teraz))
        med = wieki[len(wieki) // 2] if wieki else float("nan")
        print(f"{(mine[0]['user'] or '?')[:25]:<26}{n:>5}"
              f"{len({r['title'] for r in mine}):>5}{len({r['city'] for r in mine}):>7}"
              f"{sum(1 for r in mine if r['promoted']):>7}{med:>28.1f}")


def diff(pa, pb):
    a = json.load(open(pa, encoding="utf-8"))
    b = json.load(open(pb, encoding="utf-8"))
    ta, tb = datetime.fromisoformat(a["taken_at"]), datetime.fromisoformat(b["taken_at"])
    dni = (tb - ta).total_seconds() / 86400 or 1e-9
    ai = {r["id"]: r for r in a["offers"]}
    bi = {r["id"]: r for r in b["offers"]}
    print(f"Okres: {a['taken_at']} → {b['taken_at']} ({dni:.1f} dnia)\n")

    nowe, znikle = set(bi) - set(ai), set(ai) - set(bi)
    print(f"nowych ogłoszeń: {len(nowe)} | zniknęło: {len(znikle)} | "
          f"stan: {len(ai)} → {len(bi)}")

    def per_user(ids, idx):
        return collections.Counter(idx[i]["user"] for i in ids)

    print(f"\n{'sprzedawca':<26}{'nowe':>6}{'zniknęło':>10}{'zmiana tytułu':>15}"
          f"{'zmiana miasta':>15}{'odświeżeń':>11}")
    users = set(per_user(nowe, bi)) | set(per_user(znikle, ai))
    tyt = collections.Counter()
    mia = collections.Counter()
    odsw = collections.Counter()
    for i in set(ai) & set(bi):
        if ai[i]["title"] != bi[i]["title"]:
            tyt[bi[i]["user"]] += 1
        if ai[i]["city"] != bi[i]["city"]:
            mia[bi[i]["user"]] += 1
        if ai[i].get("refreshed") != bi[i].get("refreshed"):
            odsw[bi[i]["user"]] += 1
    users |= set(tyt) | set(mia) | set(odsw)
    wg = sorted(users, key=lambda u: -(per_user(nowe, bi)[u] + per_user(znikle, ai)[u]
                                       + tyt[u] + mia[u] + odsw[u]))
    for u in wg[:15]:
        print(f"{(u or '?')[:25]:<26}{per_user(nowe, bi)[u]:>6}{per_user(znikle, ai)[u]:>10}"
              f"{tyt[u]:>15}{mia[u]:>15}{odsw[u]:>11}")


WOJEWODZTWA = {1: "wielkopolskie", 2: "mazowieckie", 3: "dolnośląskie", 4: "małopolskie",
               5: "pomorskie", 6: "śląskie", 7: "łódzkie", 8: "lubelskie", 9: "lubuskie",
               11: "zachodniopomorskie", 12: "opolskie", 13: "świętokrzyskie",
               14: "warmińsko-mazurskie", 15: "kujawsko-pomorskie", 17: "podkarpackie",
               18: "podlaskie"}


def spis():
    """Wszystkie ogłoszenia z „wapno” w kat. 4368, województwo po województwie (limit 1000 na zapytanie)."""
    rows, widoczne = {}, {}
    for rid, woj in WOJEWODZTWA.items():
        for page in range(25):
            try:
                d = m.fetch({"category_id": 4368, "query": "wapno", "region_id": rid,
                             "limit": 50, "offset": page * 50, "sort_by": "created_at:desc"})
            except Exception as exc:  # OLX odcina paginację ~offsetu 1000
                print(f"  {woj}: stop na offsecie {page * 50} ({exc})", file=sys.stderr)
                break
            if page == 0:
                widoczne[woj] = d.get("metadata", {}).get("visible_total_count")
            items = d.get("data", [])
            for o in items:
                u, loc, promo = o.get("user") or {}, o.get("location") or {}, o.get("promotion") or {}
                rows[o["id"]] = {"id": o["id"], "title": o.get("title"), "price": m.price_of(o)[0],
                                 "user_id": u.get("id"), "user": u.get("company_name") or u.get("name"),
                                 "city": (loc.get("city") or {}).get("name"), "region": woj,
                                 "created": o.get("created_time"), "refreshed": o.get("last_refresh_time"),
                                 "promoted": bool(promo.get("highlighted") or promo.get("top_ad"))}
            if len(items) < 50:
                break
            m.time.sleep(0.3)
        print(f"  {woj}: widocznych {widoczne.get(woj)}, zebrane łącznie {len(rows)}", file=sys.stderr)
    now = datetime.now(timezone.utc).astimezone()
    path = os.path.join(SNAPDIR, "spis-" + now.strftime("%Y-%m-%d") + ".json")
    json.dump({"taken_at": now.isoformat(timespec="seconds"), "zakres": "kat. 4368, query=wapno",
               "widoczne": widoczne, "offers": list(rows.values())},
              open(path, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"spis: {os.path.relpath(path)} — {len(rows)} ogłoszeń z {sum(v or 0 for v in widoczne.values())} "
          f"widocznych, {len({r['user_id'] for r in rows.values()})} sprzedawców")


def spis_diff(pa, pb):
    a, b = (json.load(open(p, encoding="utf-8"))["offers"] for p in (pa, pb))
    ca, cb = (collections.Counter(r["user_id"] for r in x) for x in (a, b))
    nazwy = {r["user_id"]: r["user"] for r in a + b}
    print(f"sprzedawców {len(ca)} → {len(cb)} | wspólnych {len(set(ca) & set(cb))} | "
          f"weszło {len(set(cb) - set(ca))} | wyszło {len(set(ca) - set(cb))}")
    print("\nnajwięksi dziś:")
    for i, (u, n) in enumerate(cb.most_common(12), 1):
        print(f"  {i:>2}. {(nazwy[u] or '?')[:28]:<30}{ca.get(u, 0):>5} → {n}")
    zm = sorted(set(ca) | set(cb), key=lambda u: -abs(cb.get(u, 0) - ca.get(u, 0)))[:10]
    print("\nnajwiększe zmiany:")
    for u in zm:
        print(f"  {(nazwy[u] or '?')[:28]:<30}{ca.get(u, 0):>5} → {cb.get(u, 0)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--spis" in args:
        spis()
    elif "--spis-diff" in args:
        i = args.index("--spis-diff")
        spis_diff(args[i + 1], args[i + 2])
    elif "--profile" in args:
        profile()
    elif "--diff-last" in args:
        f = sorted(os.path.join(SNAPDIR, x) for x in os.listdir(SNAPDIR) if x.endswith(".json"))
        if len(f) < 2:
            sys.exit("potrzebne co najmniej 2 snapshoty")
        diff(f[-2], f[-1])
    elif "--diff" in args:
        i = args.index("--diff")
        diff(args[i + 1], args[i + 2])
    else:
        zapisz(zbierz())
