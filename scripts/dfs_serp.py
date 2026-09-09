#!/usr/bin/env python3
"""SERP Google (DataForSEO live/advanced) dla listy fraz — PL, mobile domyślnie.

⚠️ Endpoint `live` przyjmuje JEDNO zadanie na wywołanie ("You can set only one
task at a time") — dlatego pętla, nie tablica w jednym POST.

Użycie:
    python3 scripts/dfs_serp.py --out data/seo/serp-2026-09-09.json "wapno węglanowe" "wapno granulowane"
    python3 scripts/dfs_serp.py --desktop --top 5 --plik frazy.txt
"""
import argparse, base64, json, os, sys, urllib.request

AUTH = open("/home/host476470/secrets/dataforseo/basic-auth-b64.txt").read().strip()
URL = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"

ap = argparse.ArgumentParser()
ap.add_argument("frazy", nargs="*")
ap.add_argument("--plik")
ap.add_argument("--desktop", action="store_true")
ap.add_argument("--depth", type=int, default=20)
ap.add_argument("--top", type=int, default=10)
ap.add_argument("--out")
a = ap.parse_args()

frazy = list(a.frazy) + ([l.strip() for l in open(a.plik) if l.strip()] if a.plik else [])
if not frazy:
    sys.exit("brak fraz")

zebrane, koszt = {}, 0.0
for kw in frazy:
    body = [{"keyword": kw, "location_code": 2616, "language_code": "pl",
             "device": "desktop" if a.desktop else "mobile", "depth": a.depth,
             "people_also_ask_click_depth": 1}]
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Basic {AUTH}", "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req))
    koszt += d.get("cost", 0)
    t = d["tasks"][0]
    if not t.get("result"):
        print(f"### {kw} — BRAK WYNIKU: {t.get('status_message')}\n"); continue
    r = t["result"][0]
    zebrane[kw] = r
    items = r.get("items") or []
    typy = {}
    for it in items:
        typy[it["type"]] = typy.get(it["type"], 0) + 1
    print("=" * 78)
    print(f"### {kw}   [{'desktop' if a.desktop else 'mobile'}]")
    print("bloki:", ", ".join(f"{k}×{v}" for k, v in typy.items()))
    n = 0
    for it in items:
        if it["type"] == "organic":
            n += 1
            if n <= a.top:
                mark = " ← AGRIA" if "agria.pl" in (it.get("domain") or "") else ""
                print(f"  org{n:2d} (abs {it['rank_absolute']:2d}) {it.get('domain',''):26s} {(it.get('title') or '')[:66]}{mark}")
        elif it["type"] == "people_also_ask":
            print("  PAA:", " | ".join(x.get("title", "") for x in (it.get("items") or [])[:6]))
        elif it["type"] in ("ai_overview", "featured_snippet", "shopping", "popular_products", "commercial_units"):
            print(f"  >>> {it['type']} na pozycji abs {it.get('rank_absolute')}")
    # gdzie stoimy, jeśli poza TOP
    nasze = [f"abs {it['rank_absolute']}" for it in items
             if it["type"] == "organic" and "agria.pl" in (it.get("domain") or "")]
    print("  AGRIA:", ", ".join(nasze) if nasze else f"poza depth={a.depth}")
    print()

print(f"koszt: ${koszt:.5f}")
if a.out:
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(zebrane, open(a.out, "w"), ensure_ascii=False, indent=1)
    print("zapisane:", a.out)
