#!/usr/bin/env python3
"""Planer słów kluczowych Google Ads — wolumen i CPC dla listy fraz (koszt zerowy).

`:generateKeywordHistoricalMetrics` na koncie AGRII (CID w ads_call.sh), PL / polski / wyszukiwarka.
Fraza bez `keywordMetrics` w odpowiedzi = poniżej progu planera, NIE zero — w tabeli jako „<10".
Google skleja warianty bliskie (liczba pojedyncza/mnoga, szyk) — nie mieszaj ich w jednej liście,
bo dostaniesz tę samą liczbę dwa razy.

Użycie:
    python3 scripts/ads_planer.py --out data/produkty/ads/agrobielik-70-planer.json --plik frazy.txt
    python3 scripts/ads_planer.py "wapno tlenkowe" "agrobielik"
"""
import argparse, datetime as dt, json, os, subprocess, tempfile

ADS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "google", "ads_call.sh")
MIES = {m: i for i, m in enumerate(["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
                                    "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"], 1)}

ap = argparse.ArgumentParser()
ap.add_argument("frazy", nargs="*")
ap.add_argument("--plik")
ap.add_argument("--out")
a = ap.parse_args()
frazy = list(a.frazy) + ([l.strip() for l in open(a.plik) if l.strip() and not l.startswith("#")] if a.plik else [])
frazy = list(dict.fromkeys(frazy))

wyniki = []
for i in range(0, len(frazy), 20):
    body = {"keywords": frazy[i:i + 20], "language": "languageConstants/1030",
            "geoTargetConstants": ["geoTargetConstants/2616"], "keywordPlanNetwork": "GOOGLE_SEARCH",
            "historicalMetricsOptions": {"includeAverageCpc": True}}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(body, f)
    out = subprocess.run(["bash", ADS, ":generateKeywordHistoricalMetrics", "POST", f.name],
                         capture_output=True, text=True, timeout=90).stdout
    os.unlink(f.name)
    wyniki += json.loads(out).get("results", [])

zwrocone = {r["text"] for r in wyniki} | {v for r in wyniki for v in r.get("closeVariants", [])}
print("| fraza | wyszukań/mies. | CPC śr. zł | stawka top min–max zł | konkurencja | szczyt (rok-mies.) | warianty sklejone |")
print("|---|---|---|---|---|---|---|")
tab = []
for r in wyniki:
    m = r.get("keywordMetrics", {})
    serie = [(f"{s['year']}-{MIES[s['month']]:02d}", int(s.get("monthlySearches", 0)))
             for s in m.get("monthlySearchVolumes", [])]
    szczyt = max(serie, key=lambda x: x[1]) if serie else None
    zl = lambda k: round(int(m[k]) / 1e6, 2) if k in m else None
    w = {"fraza": r["text"], "wolumen": int(m["avgMonthlySearches"]) if "avgMonthlySearches" in m else None,
         "cpc": zl("averageCpcMicros"), "top_min": zl("lowTopOfPageBidMicros"), "top_max": zl("highTopOfPageBidMicros"),
         "konkurencja": m.get("competition"), "serie": serie, "warianty": r.get("closeVariants", [])}
    tab.append(w)
    print(f"| {w['fraza']} | {w['wolumen'] if w['wolumen'] is not None else '<10 (brak metryk)'} | "
          f"{w['cpc'] or '—'} | {w['top_min'] or '—'}–{w['top_max'] or '—'} | {w['konkurencja'] or '—'} | "
          f"{f'{szczyt[0]}: {szczyt[1]}' if szczyt else '—'} | {', '.join(w['warianty'])} |")
brak = [f for f in frazy if f not in zwrocone]
if brak:
    print(f"\nNie zwrócone przez API: {brak}")

if a.out:
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump({"pobrano": dt.datetime.now().isoformat(timespec="seconds"), "zrodlo": "Google Ads API generateKeywordHistoricalMetrics, PL/pl",
               "frazy": tab, "nie_zwrocone": brak}, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"\nZapisane: {a.out}")
