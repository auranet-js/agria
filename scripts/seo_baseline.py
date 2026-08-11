#!/usr/bin/env python3
"""Snapshot widoczności SEO agria.pl + konkurenci — pomiar powtarzalny.

Po co: ADR 2026-08-11 (podział ról Ads vs SEO) opiera się na konkretnych liczbach.
Ten skrypt odtwarza ten sam pomiar w dowolnym momencie i pokazuje deltę wobec
poprzedniego snapshotu — żeby decyzję dało się zweryfikować, a nie tylko pamiętać.

Mierzy cztery rzeczy:
  A. Widoczność organiczna (DataForSEO Labs, frazy w TOP30) — agria vs 3 konkurentów,
     z rozbiciem na typ strony (blog/poradnik vs produkt/kategoria). To jest metryka,
     która rozstrzygnęła spór "landingi czy treść".
  B. SERP head (6 fraz komercyjnych) — pozycja agria.pl, kto trzyma TOP5,
     obecność local_pack / AI Overview.
  C. GSC — kluczowe URL-e i frazy projektu (ostatnie 28 dni).
  D. Indeksacja landingów Ads (URL Inspection) — mają zostać POZA indeksem do końca sezonu.

Użycie:
    python3 scripts/seo_baseline.py              # nowy snapshot + delta vs poprzedni
    python3 scripts/seo_baseline.py --dry-run    # tylko odczyt GSC, bez kosztów DataForSEO
    python3 scripts/seo_baseline.py --compare    # sama delta z dwóch ostatnich, zero zapytań

Snapshoty: docs/seo/baselines/YYYY-MM-DD.json (commitowane — to jest dowód w czasie).
Koszt DataForSEO: ~0,05 USD za pełny przebieg.
"""
import json, os, sys, urllib.request, urllib.parse, time
from datetime import date, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(REPO, "docs", "seo", "baselines")
SEC = os.path.expanduser("~/secrets")
SITE = "https://agria.pl/"

DOMENY = ["agria.pl", "polcalc.pl", "biovita.com.pl", "orcal.pl"]
FRAZY_HEAD = ["wapno nawozowe", "wapno granulowane", "wapno palone",
              "wapno magnezowe", "kreda nawozowa", "wapno hydratyzowane"]
# URL-e, których losy rozstrzygają o słuszności ADR
URLE_KLUCZOWE = ["/wapnowanie-gleby/", "/kalkulator-wapnowania/",
                 "/wapno-nawozowe-rolnictwo/", "/wapno-granulowane/",
                 "/wapno-do-stabilizacji-gruntow/", "/"]
FRAZY_GSC = ["wapno nawozowe", "wapno granulowane", "ile wapna na hektar",
             "ile wapna granulowanego na hektar", "wapno bielik", "wapnowanie gleby"]
# landingi reklamowe — wg ADR mają być poza indeksem do końca października
LANDINGI_ADS = ["https://agria.pl/wapno-granulowane/", "https://agria.pl/wapno-nawozowe/"]


def bucket(url):
    """Typ strony — rozróżnienie, na którym stoi cała teza ADR."""
    u = (url or "").lower()
    if any(s in u for s in ("/blog", "/porad", "/wiedza", "/artyk", "/jak-", "/ile-")):
        return "blog/poradnik"
    if u.rstrip("/") in ("", "/"):
        return "home"
    return "produkt/kategoria"


# ---------------------------------------------------------------- DataForSEO
def dfs(endpoint, payload):
    auth = open(f"{SEC}/dataforseo/basic-auth-b64.txt").read().strip()
    req = urllib.request.Request(
        f"https://api.dataforseo.com/v3/{endpoint}", data=json.dumps(payload).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))


def zbierz_widocznosc():
    out, koszt = {}, 0.0
    for d in DOMENY:
        r = dfs("dataforseo_labs/google/ranked_keywords/live", [{
            "target": d, "location_code": 2616, "language_code": "pl", "limit": 700,
            "order_by": ["keyword_data.keyword_info.search_volume,desc"],
            "filters": [["ranked_serp_element.serp_item.rank_group", "<=", 30]]}])
        koszt += r.get("cost") or 0
        res = (r["tasks"][0].get("result") or [{}])[0]
        items = res.get("items") or []
        typy = {}
        top10 = []
        for i in items:
            se = i["ranked_serp_element"]["serp_item"]
            if se["rank_group"] > 10:
                continue
            v = i["keyword_data"]["keyword_info"].get("search_volume") or 0
            b = bucket(se.get("relative_url"))
            t = typy.setdefault(b, {"fraz": 0, "wolumen": 0})
            t["fraz"] += 1
            t["wolumen"] += v
            top10.append({"kw": i["keyword_data"]["keyword"], "poz": se["rank_group"],
                          "vol": v, "url": se.get("relative_url", "")})
        out[d] = {
            "fraz_top30": len(items),
            "fraz_top10": len(top10),
            "fraz_top3": sum(1 for i in items
                             if i["ranked_serp_element"]["serp_item"]["rank_group"] <= 3),
            "wolumen_top10": sum(t["wolumen"] for t in typy.values()),
            "wg_typu": typy,
            "top10": sorted(top10, key=lambda x: -x["vol"])[:60],
        }
        time.sleep(1)
    return out, koszt


def zbierz_serp():
    out, koszt = {}, 0.0
    for kw in FRAZY_HEAD:
        r = dfs("serp/google/organic/live/advanced", [{
            "keyword": kw, "location_code": 2616, "language_code": "pl",
            "device": "desktop", "depth": 20}])
        koszt += r.get("cost") or 0
        res = (r["tasks"][0].get("result") or [{}])[0]
        items = res.get("items") or []
        org = [i for i in items if i.get("type") == "organic"]
        ag = [i for i in org if "agria.pl" in (i.get("domain") or "")]
        out[kw] = {
            "agria_poz": ag[0]["rank_group"] if ag else None,
            "agria_url": ag[0].get("url") if ag else None,
            "top5": [{"poz": i["rank_group"], "domena": i.get("domain"), "url": i.get("url")}
                     for i in org[:5]],
            "bloki": {t: sum(1 for i in items if i.get("type") == t)
                      for t in {i.get("type") for i in items}},
        }
        time.sleep(1)
    return out, koszt


# ---------------------------------------------------------------- Google
def google_token():
    tok = json.load(open(f"{SEC}/google/tokens.json"))
    cli = json.load(open(f"{SEC}/google/oauth-desktop-client.json"))["installed"]
    data = urllib.parse.urlencode({
        "client_id": cli["client_id"], "client_secret": cli["client_secret"],
        "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", data=data))["access_token"]


def zbierz_gsc(at):
    def q(body):
        url = ("https://searchconsole.googleapis.com/webmasters/v3/sites/"
               f"{urllib.parse.quote(SITE, safe='')}/searchAnalytics/query")
        req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                     headers={"Authorization": f"Bearer {at}",
                                              "Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(req))

    # GSC dojrzewa dane ~3 dni — okno 28 dni kończy się 3 dni wstecz
    end = date.today() - timedelta(days=3)
    start = end - timedelta(days=27)
    okno = {"startDate": start.isoformat(), "endDate": end.isoformat()}

    calosc = (q({**okno, "dimensions": []}).get("rows") or [{}])[0]
    strony = {r["keys"][0].replace("https://agria.pl", "") or "/": r
              for r in q({**okno, "dimensions": ["page"], "rowLimit": 500}).get("rows", [])}
    frazy = {}
    for f in FRAZY_GSC:
        rows = q({**okno, "dimensions": ["page"], "rowLimit": 20,
                  "dimensionFilterGroups": [{"filters": [
                      {"dimension": "query", "operator": "equals", "expression": f}]}]}).get("rows", [])
        frazy[f] = [{"url": r["keys"][0].replace("https://agria.pl", ""), "klik": r["clicks"],
                     "wysw": r["impressions"], "poz": round(r["position"], 1)} for r in rows]
    return {
        "okno": okno,
        "calosc": {"klik": calosc.get("clicks", 0), "wysw": calosc.get("impressions", 0),
                   "poz": round(calosc.get("position", 0), 1)},
        "urle": {u: ({"klik": strony[u]["clicks"], "wysw": strony[u]["impressions"],
                      "poz": round(strony[u]["position"], 1)} if u in strony else None)
                 for u in URLE_KLUCZOWE},
        "frazy": frazy,
    }


def zbierz_indeksacje(at):
    out = {}
    for u in LANDINGI_ADS:
        req = urllib.request.Request(
            "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect",
            data=json.dumps({"inspectionUrl": u, "siteUrl": SITE}).encode(),
            headers={"Authorization": f"Bearer {at}", "Content-Type": "application/json"})
        try:
            r = json.load(urllib.request.urlopen(req))
            s = r.get("inspectionResult", {}).get("indexStatusResult", {})
            out[u] = {"verdict": s.get("verdict"), "coverage": s.get("coverageState"),
                      "lastCrawl": s.get("lastCrawlTime")}
        except Exception as e:
            out[u] = {"blad": str(e)}
    return out


# ---------------------------------------------------------------- raport
def wypisz(s, prev=None):
    def d(now, was, odwrotnie=False):
        if was is None or now is None:
            return ""
        r = now - was
        if r == 0:
            return "  (bez zmian)"
        znak = "+" if r > 0 else ""
        dobrze = (r < 0) if odwrotnie else (r > 0)
        return f"  ({znak}{r}{' ▲' if dobrze else ' ▼'})"

    print(f"\n{'='*78}\nSNAPSHOT SEO agria.pl — {s['data']}")
    if prev:
        print(f"porównanie z: {prev['data']}")
    print("=" * 78)

    print("\n## A. Widoczność organiczna (frazy w TOP30, PL)\n")
    print(f"{'domena':<18} {'≤30':>5} {'TOP10':>6} {'TOP3':>5} {'wolumen TOP10':>14}   udział treści")
    for dom, v in s["widocznosc"].items():
        p = (prev or {}).get("widocznosc", {}).get(dom, {})
        blog = v["wg_typu"].get("blog/poradnik", {}).get("wolumen", 0)
        tot = v["wolumen_top10"] or 1
        print(f"{dom:<18} {v['fraz_top30']:>5} {v['fraz_top10']:>6}{d(v['fraz_top10'], p.get('fraz_top10'))} "
              f"{v['fraz_top3']:>5} {v['wolumen_top10']:>14,}   {round(blog/tot*100):>3}% blog")

    print("\n## B. SERP head — pozycja agria.pl\n")
    for kw, v in s["serp"].items():
        p = (prev or {}).get("serp", {}).get(kw, {})
        poz = v["agria_poz"]
        txt = f"poz. {poz}" if poz else "poza TOP20"
        delta = d(poz, p.get("agria_poz"), odwrotnie=True) if poz and p.get("agria_poz") else ""
        gora = ", ".join(x["domena"] for x in v["top5"][:3])
        extra = []
        if v["bloki"].get("local_pack"):
            extra.append(f"local_pack×{v['bloki']['local_pack']}")
        if v["bloki"].get("ai_overview"):
            extra.append("AI Overview")
        print(f"  {kw:<24} {txt:<12}{delta:<16} góra: {gora}   {' '.join(extra)}")

    print(f"\n## C. GSC — okno {s['gsc']['okno']['startDate']}..{s['gsc']['okno']['endDate']}\n")
    c, pc = s["gsc"]["calosc"], (prev or {}).get("gsc", {}).get("calosc", {})
    print(f"  witryna: {c['klik']} klik{d(c['klik'], pc.get('klik'))}, "
          f"{c['wysw']} wyśw{d(c['wysw'], pc.get('wysw'))}, śr. poz. {c['poz']}")
    print(f"\n  {'URL':<36} {'klik':>6} {'wyśw':>7} {'poz':>6}")
    for u, v in s["gsc"]["urle"].items():
        if not v:
            print(f"  {u:<36} {'—':>6} {'—':>7} {'—':>6}")
            continue
        pu = ((prev or {}).get("gsc", {}).get("urle", {}) or {}).get(u) or {}
        print(f"  {u:<36} {v['klik']:>6} {v['wysw']:>7}{d(v['wysw'], pu.get('wysw'))} {v['poz']:>6}")

    print("\n  frazy kluczowe (strona docelowa wg Google):")
    for f, rows in s["gsc"]["frazy"].items():
        if not rows:
            print(f"    {f:<34} — brak")
        for r in rows[:2]:
            print(f"    {f:<34} {r['url']:<34} {r['klik']:>3} klik {r['wysw']:>5} wyśw  poz {r['poz']}")

    print("\n## D. Landingi reklamowe — wg ADR mają być POZA indeksem do 31.10\n")
    for u, v in s["indeksacja"].items():
        cov = v.get("coverage", v.get("blad", "?"))
        alarm = "  ⚠ WESZŁO DO INDEKSU — sprawdź ADR" if v.get("verdict") == "PASS" else ""
        print(f"  {u:<45} {cov}{alarm}")
    print()


def main():
    tryb_dry = "--dry-run" in sys.argv
    tylko_porownanie = "--compare" in sys.argv
    os.makedirs(OUTDIR, exist_ok=True)
    stare = sorted(f for f in os.listdir(OUTDIR) if f.endswith(".json"))

    if tylko_porownanie:
        if len(stare) < 2:
            sys.exit("Potrzeba dwóch snapshotów do porównania.")
        wypisz(json.load(open(os.path.join(OUTDIR, stare[-1]))),
               json.load(open(os.path.join(OUTDIR, stare[-2]))))
        return

    at = google_token()
    s = {"data": date.today().isoformat(), "gsc": zbierz_gsc(at), "indeksacja": zbierz_indeksacje(at)}
    if tryb_dry:
        s["widocznosc"], s["serp"], s["koszt_usd"] = {}, {}, 0
    else:
        s["widocznosc"], k1 = zbierz_widocznosc()
        s["serp"], k2 = zbierz_serp()
        s["koszt_usd"] = round(k1 + k2, 4)

    prev = json.load(open(os.path.join(OUTDIR, stare[-1]))) if stare else None
    wypisz(s, prev)

    if not tryb_dry:
        sciezka = os.path.join(OUTDIR, f"{s['data']}.json")
        json.dump(s, open(sciezka, "w"), ensure_ascii=False, indent=1)
        print(f"Zapisano: {sciezka}   (koszt DataForSEO: {s['koszt_usd']} USD)\n")


if __name__ == "__main__":
    main()
