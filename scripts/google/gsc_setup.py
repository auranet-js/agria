#!/usr/bin/env python3
"""GSC config dla AGRIA: sitemap submit + URL inspection test.

GA4 ↔ GSC link NIE jest dostepny przez API Google (tylko UI). To zostaje
do manualnego kliknięcia w GA4 admin → Product Links → Search Console.

Run: python3 ~/projekty/agria/scripts/google/gsc_setup.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import api

SITE = "https://agria.pl/"
SITE_ENC = "https%3A%2F%2Fagria.pl%2F"
SITEMAP_URLS = [
    "https://agria.pl/sitemap_index.xml",  # RankMath default
]
BASE = "https://www.googleapis.com"


def step(t):
    print(f"\n=== {t} ===")


# 1. Listę istniejących sitemap
step("Existing sitemaps in GSC")
r = api("GET", BASE, f"/webmasters/v3/sites/{SITE_ENC}/sitemaps")
print(json.dumps(r, indent=2, ensure_ascii=False))
existing_urls = {s.get("path") for s in r.get("sitemap", [])}

# 2. Submit sitemap (RankMath powinien serwować /sitemap_index.xml)
step("Submit sitemap(s)")
for sm in SITEMAP_URLS:
    if sm in existing_urls:
        print(f"SKIP {sm} (already submitted)")
        continue
    sm_enc = sm.replace(":", "%3A").replace("/", "%2F")
    r = api("PUT", BASE, f"/webmasters/v3/sites/{SITE_ENC}/sitemaps/{sm_enc}")
    if "error" in r:
        print(f"ERR {sm}: HTTP {r.get('code')}")
        print(r.get("error")[:300])
    else:
        print(f"OK submitted: {sm}")

# 3. URL inspection — strona główna agria.pl
step("URL inspection: https://agria.pl/")
r = api("POST", BASE, "/v1/urlInspection/index:inspect", {
    "inspectionUrl": "https://agria.pl/",
    "siteUrl": SITE,
    "languageCode": "pl-PL",
})
if "error" in r:
    print(f"ERR: HTTP {r.get('code')}: {r.get('error')[:300]}")
else:
    ir = r.get("inspectionResult", {})
    idx = ir.get("indexStatusResult", {})
    print(f"Verdict: {idx.get('verdict')}")
    print(f"Coverage state: {idx.get('coverageState')}")
    print(f"Robots.txt state: {idx.get('robotsTxtState')}")
    print(f"Indexing state: {idx.get('indexingState')}")
    print(f"Page fetch state: {idx.get('pageFetchState')}")
    print(f"Crawled as: {idx.get('crawledAs')}")
    print(f"Last crawl: {idx.get('lastCrawlTime')}")
    print(f"Sitemap referencing: {idx.get('sitemap', [])}")
    print(f"Referring URLs: {idx.get('referringUrls', [])[:5]}")

# Wrong endpoint — URL Inspection is on searchconsole.googleapis.com
print("\n(jesli 404 wyzej — endpoint jest na searchconsole.googleapis.com)")
