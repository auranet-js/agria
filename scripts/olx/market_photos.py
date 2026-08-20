#!/usr/bin/env python3
"""Zbiera próbkę ogłoszeń konkurencji z publicznego API OLX — RAZEM ZE ZDJĘCIAMI.

Po co osobny skrypt obok market_snapshot.py: tamten ciągnie listing kategorii 4368 i pola
photo/image wracają z niego PUSTE (sprawdzone na `data/olx/market/2026-08-07.json` — zero
wystąpień). Publiczne API wyszukiwania zwraca komplet: `photos[].link` (wzorzec CDN
`image;s={width}x{height}`) plus width/height każdego kadru, więc dopiero stąd da się policzyć,
ile zdjęć i jakiej wielkości wystawia kategoria.

Zapytania idą po frazach, nie po samej kategorii, bo kategoria „Nawozy" zawiera też saletrę,
obornik i nawozy sztuczne — a punktem odniesienia dla AGRII jest wapno i kreda.

Użycie: market_photos.py <plik-wyjściowy.json>
"""
import json, subprocess, sys, time

BASE = "https://www.olx.pl/api/v1/offers/?offset={off}&limit=50&category_id=4368&query={q}"
QUERIES = ["wapno", "kreda", "wapno nawozowe", "wapno granulowane", "wapno palone",
           "kreda nawozowa", "wapno rolnicze", "wapno tlenkowe", "wapno weglanowe"]

def fetch(url):
    r = subprocess.run(["curl", "-sS", "--max-time", "30",
                        "-H", "User-Agent: Mozilla/5.0", url], capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except Exception:
        return None

wszystkie = {}
for q in QUERIES:
    for off in (0, 50, 100, 150):
        d = fetch(BASE.format(off=off, q=q.replace(" ", "%20")))
        if not d or not d.get("data"):
            break
        for o in d["data"]:
            wszystkie[o["id"]] = o
        time.sleep(0.4)
    print(f"{q}: łącznie {len(wszystkie)}", file=sys.stderr)

json.dump(list(wszystkie.values()), open(sys.argv[1], "w", encoding="utf-8"),
          ensure_ascii=False)
print(f"zebrane: {len(wszystkie)} ogłoszeń → {sys.argv[1]}", file=sys.stderr)
