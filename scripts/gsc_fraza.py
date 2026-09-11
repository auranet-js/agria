#!/usr/bin/env python3
"""GSC w cały serwis dla zapytań zawierających podany ciąg — zapytanie × strona.

Odwrotność gsc_baseline.py: tam strona → zapytania, tu fragment frazy → które
nasze adresy się na nią pokazują. Do bazy wiedzy produktowej (docs/produkty/).

Użycie:
    python3 scripts/gsc_fraza.py --dni 90 --out data/produkty/gsc/agrobielik-70-frazy.json agrobielik bielik
"""
import argparse, datetime as dt, json, os, urllib.parse, urllib.request

SEC = "/home/host476470/secrets/google"
SITE = "https://agria.pl/"

ap = argparse.ArgumentParser()
ap.add_argument("ciagi", nargs="+")
ap.add_argument("--dni", type=int, default=90)
ap.add_argument("--out")
a = ap.parse_args()

koniec = str(dt.date.today() - dt.timedelta(days=4))
start = str(dt.date.fromisoformat(koniec) - dt.timedelta(days=a.dni - 1))

tok = json.load(open(f"{SEC}/tokens.json"))
cli = json.load(open(f"{SEC}/oauth-desktop-client.json"))["installed"]
AT = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", data=urllib.parse.urlencode({
    "client_id": cli["client_id"], "client_secret": cli["client_secret"],
    "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"}).encode()))["access_token"]


def gsc(body):
    url = ("https://searchconsole.googleapis.com/webmasters/v3/sites/"
           f"{urllib.parse.quote(SITE, safe='')}/searchAnalytics/query")
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {AT}", "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req)).get("rows", [])


wynik = {"okno": {"startDate": start, "endDate": koniec},
         "pobrano": dt.datetime.now().isoformat(timespec="seconds"), "ciagi": {}}
print(f"# GSC zapytania × strony {start} … {koniec}\n")
for c in a.ciagi:
    rows = gsc({"startDate": start, "endDate": koniec, "dimensions": ["query", "page"], "rowLimit": 1000,
                "dimensionFilterGroups": [{"filters": [
                    {"dimension": "query", "operator": "contains", "expression": c}]}]})
    wynik["ciagi"][c] = rows
    print(f"## „{c}” — {len(rows)} wierszy\n")
    print("| zapytanie | strona | klik | wyśw | poz |")
    print("|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: -r["impressions"]):
        print(f"| {r['keys'][0]} | `{r['keys'][1].replace('https://agria.pl', '')}` | "
              f"{r['clicks']} | {r['impressions']} | {round(r['position'], 1)} |")
    print()

if a.out:
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(wynik, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"Zapisane: {a.out}")
