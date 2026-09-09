#!/usr/bin/env python3
"""Baseline GSC per adres — metryki strony + zapytania, do JSON i tabelki.

Użycie:
    python3 scripts/gsc_baseline.py --dni 28 --out data/T-117/baseline.json /a/ /b/
    python3 scripts/gsc_baseline.py --od 2026-08-08 --do 2026-09-05 --plik lista.txt

Zapytania per strona bierzemy filtrem `page` — dimension `query` bez filtra
miesza cały serwis. Okno domyślne kończy się 4 dni wstecz (GSC dojrzewa dane).
"""
import argparse, datetime as dt, json, os, sys, urllib.parse, urllib.request

SEC = "/home/host476470/secrets/google"
SITE = "https://agria.pl/"

ap = argparse.ArgumentParser()
ap.add_argument("sciezki", nargs="*")
ap.add_argument("--plik")
ap.add_argument("--dni", type=int, default=28)
ap.add_argument("--od")
ap.add_argument("--do", dest="do_")
ap.add_argument("--out")
ap.add_argument("--limit", type=int, default=200, help="ile zapytań na stronę")
a = ap.parse_args()

paths = list(a.sciezki)
if a.plik:
    paths += [l.strip() for l in open(a.plik) if l.strip()]
if not paths:
    sys.exit("brak adresów")
URLS = [p if p.startswith("http") else "https://agria.pl" + p for p in paths]

koniec = a.do_ or str(dt.date.today() - dt.timedelta(days=4))
start = a.od or str(dt.date.fromisoformat(koniec) - dt.timedelta(days=a.dni - 1))

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


okno = {"startDate": start, "endDate": koniec}
wynik = {"okno": okno, "pobrano": dt.datetime.now().isoformat(timespec="seconds"), "strony": {}}

print(f"# GSC baseline {start} … {koniec}\n")
print("| Strona | Klik | Wyśw | CTR | Poz | Zapytań |")
print("|---|---|---|---|---|---|")
for u in URLS:
    flt = {"dimensionFilterGroups": [{"filters": [
        {"dimension": "page", "operator": "equals", "expression": u}]}]}
    agg = gsc({**okno, "dimensions": [], **flt})
    q = gsc({**okno, "dimensions": ["query"], "rowLimit": a.limit, **flt})
    r = agg[0] if agg else {"clicks": 0, "impressions": 0, "ctr": 0, "position": 0}
    wynik["strony"][u] = {"agregat": r, "zapytania": q}
    print(f"| `{u.replace('https://agria.pl','')}` | {r['clicks']} | {r['impressions']} | "
          f"{round(r['ctr']*100,2)}% | {round(r['position'],1)} | {len(q)} |")

if a.out:
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(wynik, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"\nZapisane: {a.out}")
