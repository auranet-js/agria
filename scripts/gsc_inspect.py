#!/usr/bin/env python3
"""URL Inspection API — stan indeksacji kluczowych URL agria.pl.

Główny dowód postępu M1/M2 (ważniejszy niż pozycje).
Property: https://agria.pl/ (URL-prefix).
"""
import json, urllib.request, urllib.parse, sys, time

SEC = "/home/host476470/secrets/google"
SITE = "https://agria.pl/"

URLS = [
    # nowe treści lipcowe (klaster wapnowanie + landingi)
    "https://agria.pl/wapnowanie-gleby/",
    "https://agria.pl/ile-wapna-granulowanego-na-ha/",
    "https://agria.pl/jak-stosowac-wapno-nawozowe/",
    "https://agria.pl/wapno-nawozowe-na-trawnik/",
    "https://agria.pl/higienizacja-osadow-sciekowych-wapnem/",
    "https://agria.pl/wapno-do-stabilizacji-gruntow/",
    # kategorie po migracji URL
    "https://agria.pl/wapno-nawozowe-rolnictwo/",
    "https://agria.pl/wapno-do-oczyszczalni/",
    "https://agria.pl/wapno-hydratyzowane/",
    "https://agria.pl/kreda-pastewna/",
    "https://agria.pl/kreda-malarska/",
    # strony statyczne / komercyjne
    "https://agria.pl/",
    "https://agria.pl/oferta/",
    "https://agria.pl/kalkulator-wapnowania/",
    "https://agria.pl/do-pobrania/",
    "https://agria.pl/kontakt/",
    # przykładowe karty produktów na nowych URL
    "https://agria.pl/wapno-nawozowe-rolnictwo/oxyfertil-90/",
    "https://agria.pl/wapno-nawozowe-rolnictwo/agrobielik-70/",
    "https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/",
    "https://agria.pl/wapno-hydratyzowane/bielik/",
]


def load(p):
    with open(p) as f:
        return json.load(f)


tok = load(f"{SEC}/tokens.json")
cli = load(f"{SEC}/oauth-desktop-client.json")["installed"]
data = urllib.parse.urlencode({
    "client_id": cli["client_id"], "client_secret": cli["client_secret"],
    "refresh_token": tok["refresh_token"], "grant_type": "refresh_token",
}).encode()
AT = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", data=data))["access_token"]

print("| URL | Werdykt | Stan w indeksie | Ostatni crawl | Canonical Google | Robots |")
print("|---|---|---|---|---|---|")

for u in URLS:
    body = {"inspectionUrl": u, "siteUrl": SITE, "languageCode": "pl"}
    req = urllib.request.Request(
        "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {AT}", "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req))
    except Exception as e:
        print(f"| {u} | ERROR | {e} | | | |")
        continue
    idx = r.get("inspectionResult", {}).get("indexStatusResult", {})
    path = u.replace("https://agria.pl", "") or "/"
    crawl = (idx.get("lastCrawlTime") or "—")[:10]
    gc = (idx.get("googleCanonical") or "—").replace("https://agria.pl", "")
    print(f"| `{path}` | {idx.get('verdict','—')} | {idx.get('coverageState','—')} | "
          f"{crawl} | `{gc}` | {idx.get('robotsTxtState','—')} / {idx.get('indexingState','—')} |")
    time.sleep(0.4)
