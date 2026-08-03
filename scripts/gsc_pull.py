#!/usr/bin/env python3
"""GSC Search Analytics pull dla AGRIA — raport miesięczny.

Property: URL-prefix https://agria.pl/ (NIE sc-domain).
Pobiera pełne miesiące kalendarzowe w jednym przebiegu (porównywalność —
GSC dojrzewa dane ~30 dni, więc liczby z poprzednich raportów będą inne).

Użycie: python3 gsc_pull.py            # maj/czerwiec/lipiec 2026
"""
import json, urllib.request, urllib.parse, sys
from collections import defaultdict

SEC = "/home/host476470/secrets/google"
SITE = "https://agria.pl/"

MONTHS = [
    ("maj",      "2026-05-01", "2026-05-31"),
    ("czerwiec", "2026-06-01", "2026-06-30"),
    ("lipiec",   "2026-07-01", "2026-07-31"),
]

# frazy-cele projektu (docs/seo/ROZPISKA_INTENCJA_WOLUMENOWA + POMIAR_POD_WYNIK)
FRAZY = [
    "ile wapna na hektar", "ile wapna na ha",
    "ile wapna granulowanego na ha", "ile wapna granulowanego na hektar",
    "wapń skorygowany kalkulator", "kalkulator wapnowania",
    "wapno bielik", "agrobielik",
    "wapno nawozowe", "wapno rolnicze", "wapno granulowane",
    "wapno hydratyzowane", "wapno tlenkowe", "wapno węglanowe",
    "stabilizacja gruntu", "stabilizacja gruntów wapnem",
    "wapno do stabilizacji gruntów",
    "kreda pastewna", "kreda nawozowa", "kreda granulowana",
    "wapno do stawów", "wapnowanie stawów",
    "higienizacja osadów", "wapno do oczyszczalni",
    "oxyfertil", "ekograncali",
]


def load(p):
    with open(p) as f:
        return json.load(f)


tok = load(f"{SEC}/tokens.json")
cli = load(f"{SEC}/oauth-desktop-client.json")["installed"]
data = urllib.parse.urlencode({
    "client_id": cli["client_id"],
    "client_secret": cli["client_secret"],
    "refresh_token": tok["refresh_token"],
    "grant_type": "refresh_token",
}).encode()
AT = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", data=data))["access_token"]


def gsc(body):
    url = ("https://searchconsole.googleapis.com/webmasters/v3/sites/"
           f"{urllib.parse.quote(SITE, safe='')}/searchAnalytics/query")
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {AT}",
                                          "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))


def p(s=""):
    print(s)


p(f"# GSC AGRIA — pull {SITE}")
p()

# ---------- 1. Agregaty miesięczne ----------
p("## 1. Agregaty miesięczne (pełne miesiące kalendarzowe)")
p()
p("| Miesiąc | Klik | Wyświetlenia | CTR | Śr. pozycja |")
p("|---|---|---|---|---|")
for name, sd, ed in MONTHS:
    r = gsc({"startDate": sd, "endDate": ed, "dimensions": []})
    row = r.get("rows", [{}])[0] if r.get("rows") else {}
    p(f"| {name} ({sd}..{ed}) | {row.get('clicks',0)} | {row.get('impressions',0)} | "
      f"{round(row.get('ctr',0)*100,2)}% | {round(row.get('position',0),1)} |")
p()

# ---------- 2. Frazy z widocznością / TOP3 / TOP10 / TOP20 ----------
p("## 2. Zasięg fraz (dimensions=query, rowLimit 25000)")
p()
p("| Miesiąc | Fraz z widocznością | TOP3 | TOP10 | TOP20 | Fraz z klikami |")
p("|---|---|---|---|---|---|")
month_queries = {}
for name, sd, ed in MONTHS:
    r = gsc({"startDate": sd, "endDate": ed, "dimensions": ["query"], "rowLimit": 25000})
    rows = r.get("rows", [])
    month_queries[name] = rows
    t3 = sum(1 for x in rows if x["position"] <= 3.5)
    t10 = sum(1 for x in rows if x["position"] <= 10.5)
    t20 = sum(1 for x in rows if x["position"] <= 20.5)
    kl = sum(1 for x in rows if x["clicks"] > 0)
    p(f"| {name} | {len(rows)} | {t3} | {t10} | {t20} | {kl} |")
p()

# ---------- 3. TOP strony ----------
p("## 3. TOP strony (lipiec vs czerwiec)")
p()
page_data = {}
for name, sd, ed in MONTHS:
    r = gsc({"startDate": sd, "endDate": ed, "dimensions": ["page"], "rowLimit": 500})
    page_data[name] = {x["keys"][0]: x for x in r.get("rows", [])}

lip = page_data["lipiec"]
cze = page_data["czerwiec"]
p("| Strona | Klik VII | Wyśw VII | Poz VII | Klik VI | Wyśw VI | Poz VI |")
p("|---|---|---|---|---|---|---|")
for url, x in sorted(lip.items(), key=lambda kv: kv[1]["impressions"], reverse=True)[:30]:
    c = cze.get(url)
    path = url.replace("https://agria.pl", "") or "/"
    cc = f"{c['clicks']} | {c['impressions']} | {round(c['position'],1)}" if c else "0 | 0 | —"
    p(f"| {path} | {x['clicks']} | {x['impressions']} | {round(x['position'],1)} | {cc} |")
p()

# ---------- 4. Wszystkie zapytania z klikami — lipiec ----------
p("## 4. Zapytania z klikami — lipiec")
p()
p("| Zapytanie | Klik | Wyśw | CTR | Poz |")
p("|---|---|---|---|---|")
for x in sorted([q for q in month_queries["lipiec"] if q["clicks"] > 0],
                key=lambda x: x["clicks"], reverse=True):
    p(f"| {x['keys'][0]} | {x['clicks']} | {x['impressions']} | "
      f"{round(x['ctr']*100,1)}% | {round(x['position'],1)} |")
p()

# ---------- 5. TOP zapytania wg wyświetleń — lipiec ----------
p("## 5. TOP 40 zapytań wg wyświetleń — lipiec")
p()
p("| Zapytanie | Wyśw | Klik | Poz VII | Poz VI | Poz V |")
p("|---|---|---|---|---|---|")
q_by_month = {m: {x["keys"][0]: x for x in rows} for m, rows in month_queries.items()}
for x in sorted(month_queries["lipiec"], key=lambda x: x["impressions"], reverse=True)[:40]:
    q = x["keys"][0]
    pv = q_by_month["czerwiec"].get(q)
    pm = q_by_month["maj"].get(q)
    p(f"| {q} | {x['impressions']} | {x['clicks']} | {round(x['position'],1)} | "
      f"{round(pv['position'],1) if pv else '—'} | {round(pm['position'],1) if pm else '—'} |")
p()

# ---------- 6. Frazy-cele: query x page (kanibalizacja) ----------
p("## 6. Frazy-cele — query × page, lipiec (kanibalizacja + pozycje)")
p()
for kw in FRAZY:
    r = gsc({"startDate": "2026-07-01", "endDate": "2026-07-31",
             "dimensions": ["page"],
             "dimensionFilterGroups": [{"filters": [
                 {"dimension": "query", "operator": "equals", "expression": kw}]}],
             "rowLimit": 10})
    rows = r.get("rows", [])
    # porównanie: czerwiec
    r6 = gsc({"startDate": "2026-06-01", "endDate": "2026-06-30",
              "dimensions": [],
              "dimensionFilterGroups": [{"filters": [
                  {"dimension": "query", "operator": "equals", "expression": kw}]}]})
    r6rows = r6.get("rows", [])
    prev = f"czerwiec: poz {round(r6rows[0]['position'],1)} / {r6rows[0]['impressions']} wyśw" if r6rows else "czerwiec: brak"
    if not rows:
        p(f"**[{kw}]** — lipiec: brak impresji ({prev})")
        p()
        continue
    tag = "  ⚠️ KANIBALIZACJA" if len(rows) > 1 else ""
    p(f"**[{kw}]**{tag} — {prev}")
    for row in sorted(rows, key=lambda x: x["impressions"], reverse=True):
        path = row["keys"][0].replace("https://agria.pl", "") or "/"
        p(f"- poz **{round(row['position'],1)}** · klik {row['clicks']} · wyśw {row['impressions']} · `{path}`")
    p()

# ---------- 7. Kraje ----------
p("## 7. Kraje — lipiec")
p()
r = gsc({"startDate": "2026-07-01", "endDate": "2026-07-31",
         "dimensions": ["country"], "rowLimit": 20})
p("| Kraj | Klik | Wyśw | Poz |")
p("|---|---|---|---|")
for x in r.get("rows", []):
    p(f"| {x['keys'][0]} | {x['clicks']} | {x['impressions']} | {round(x['position'],1)} |")
p()

# ---------- 8. Urządzenia ----------
p("## 8. Urządzenia — lipiec")
p()
r = gsc({"startDate": "2026-07-01", "endDate": "2026-07-31", "dimensions": ["device"]})
p("| Urządzenie | Klik | Wyśw | CTR | Poz |")
p("|---|---|---|---|---|")
for x in r.get("rows", []):
    p(f"| {x['keys'][0]} | {x['clicks']} | {x['impressions']} | "
      f"{round(x['ctr']*100,1)}% | {round(x['position'],1)} |")
p()
