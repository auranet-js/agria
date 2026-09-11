#!/usr/bin/env python3
"""Scala data/produkty/macierz/*.csv w docs/produkty/_macierz-fraz.csv z jednolitymi kolumnami GSC.

Kolumny z plików produktów (produkt, wc_id, fraza, typ, wolumen, cpc_zl) zostają. Kolumny GSC liczone
od nowa z jednego zrzutu całego serwisu (zapytanie × strona, to samo okno dla wszystkich fraz):
  nasz_url_gsc      — nasz adres z największą liczbą wyświetleń na tę frazę (remis: lepsza pozycja)
  pozycja_gsc       — pozycja tego adresu
  wyswietlenia_gsc  — suma wyświetleń wszystkich naszych adresów na tę frazę
  klikniecia_gsc    — suma kliknięć jw.
  adresow_gsc       — ile naszych adresów pokazuje się na tę frazę
Fraza bez wierszy w GSC = puste pola (próg prywatności albo brak wyświetleń — NIE zero).

Użycie:
    python3 scripts/produkty_macierz.py --od 2026-06-09 --do 2026-09-06
"""
import argparse, collections, csv, datetime as dt, glob, json, os, urllib.parse, urllib.request

SEC = "/home/host476470/secrets/google"
SITE = "https://agria.pl/"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

ap = argparse.ArgumentParser()
ap.add_argument("--od", required=True)
ap.add_argument("--do", dest="do_", required=True)
a = ap.parse_args()

tok = json.load(open(f"{SEC}/tokens.json"))
cli = json.load(open(f"{SEC}/oauth-desktop-client.json"))["installed"]
AT = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", data=urllib.parse.urlencode({
    "client_id": cli["client_id"], "client_secret": cli["client_secret"],
    "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"}).encode()))["access_token"]
URL = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(SITE, safe='')}/searchAnalytics/query"

rows, start = [], 0
while True:
    body = {"startDate": a.od, "endDate": a.do_, "dimensions": ["query", "page"], "rowLimit": 25000, "startRow": start}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {AT}", "Content-Type": "application/json"})
    part = json.load(urllib.request.urlopen(req)).get("rows", [])
    rows += part
    if len(part) < 25000:
        break
    start += 25000
os.makedirs(f"{ROOT}/data/produkty/gsc", exist_ok=True)
json.dump({"okno": [a.od, a.do_], "pobrano": dt.datetime.now().isoformat(timespec="seconds"), "rows": rows},
          open(f"{ROOT}/data/produkty/gsc/_serwis-zapytania-strony.json", "w"), ensure_ascii=False)

po_frazie = collections.defaultdict(list)
for r in rows:
    po_frazie[r["keys"][0].strip().lower()].append(r)

POLA = ["produkt", "wc_id", "fraza", "typ", "wolumen", "cpc_zl"]
wyj, bez = [], 0
for plik in sorted(glob.glob(f"{ROOT}/data/produkty/macierz/*.csv")):
    for w in csv.DictReader(open(plik, encoding="utf-8")):
        rs = po_frazie.get(w["fraza"].strip().lower(), [])
        rec = {k: (w.get(k) or "").strip() for k in POLA}
        if rs:
            best = sorted(rs, key=lambda r: (-r["impressions"], r["position"]))[0]
            rec.update(nasz_url_gsc=best["keys"][1].replace("https://agria.pl", ""),
                       pozycja_gsc=round(best["position"], 1),
                       wyswietlenia_gsc=sum(r["impressions"] for r in rs),
                       klikniecia_gsc=sum(r["clicks"] for r in rs), adresow_gsc=len(rs))
        else:
            bez += 1
            rec.update(nasz_url_gsc="", pozycja_gsc="", wyswietlenia_gsc="", klikniecia_gsc="", adresow_gsc="")
        wyj.append(rec)

out = f"{ROOT}/docs/produkty/_macierz-fraz.csv"
with open(out, "w", newline="", encoding="utf-8") as fh:
    wr = csv.DictWriter(fh, fieldnames=POLA + ["nasz_url_gsc", "pozycja_gsc", "wyswietlenia_gsc", "klikniecia_gsc", "adresow_gsc"],
                        quoting=csv.QUOTE_ALL)
    wr.writeheader()
    wr.writerows(wyj)
print(f"zrzut GSC: {len(rows)} wierszy zapytanie×strona, {len(po_frazie)} zapytań")
print(f"macierz: {len(wyj)} wierszy z {len(glob.glob(ROOT + '/data/produkty/macierz/*.csv'))} plików; bez wierszy w GSC: {bez}")
print(f"zapisane: {out}")
