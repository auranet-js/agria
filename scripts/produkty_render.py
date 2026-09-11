#!/usr/bin/env python3
"""Stan karty produktu z RENDERU — pod §6 szablonu bazy wiedzy (docs/produkty/).

Czytamy render, nie bazę: parametry żyją w 4 warstwach i tylko render pokazuje to,
co widzi klient. Bez `?cb=` (WP Rocket traktuje to jako osobny wpis cache) —
rozgrzewka jednym żądaniem, potem odczyt.

Użycie:
    python3 scripts/produkty_render.py agrobielik-70 /wapno-nawozowe-rolnictwo/agrobielik-70/
Wynik: data/produkty/render/<slug>.html + <slug>.json, skrót na stdout.
"""
import html, json, os, re, subprocess, sys, datetime as dt

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "produkty", "render")


def fetch(url):
    return subprocess.run(["curl", "-sS", "-A", UA, "--max-time", "60", url],
                          capture_output=True, text=True, check=True).stdout


def txt(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


slug, path = sys.argv[1], sys.argv[2]
url = path if path.startswith("http") else "https://agria.pl" + path
fetch(url)  # rozgrzewka
h = fetch(url)
os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/{slug}.html", "w").write(h)

body = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", h, flags=re.S)
main = re.search(r"<main[^>]*>(.*?)</main>", body, re.S)
main = main.group(1) if main else body

spec = {}
m = re.search(r"Specyfikacja techniczna(.*?)</table>", h, re.S)
if m:
    for row in re.findall(r"<tr>(.*?)</tr>", m.group(1), re.S):
        c = [txt(x) for x in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
        if len(c) == 2 and c[0] != "Parametr":
            spec[c[0]] = c[1]

schema = []
for blok in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, re.S):
    try:
        d = json.loads(blok)
    except ValueError:
        continue
    for n in (d.get("@graph", [d]) if isinstance(d, dict) else d):
        if isinstance(n, dict):
            schema.append({"@type": n.get("@type"), "offers": "offers" in n,
                           "faq": n.get("@type") == "FAQPage"})

tekst = txt(main)
r = {
    "url": url,
    "pobrano": dt.datetime.now().isoformat(timespec="seconds"),
    "bajty_html": len(h),
    "title": txt(re.search(r"<title>(.*?)</title>", h, re.S).group(1)),
    "meta_description": (lambda m: html.unescape(m.group(1)) if m else None)(
        re.search(r'<meta name="description" content="([^"]*)"', h)),
    "robots": (lambda m: m.group(1) if m else None)(re.search(r'<meta name="robots" content="([^"]*)"', h)),
    "canonical": (lambda m: m.group(1) if m else None)(re.search(r'<link rel="canonical" href="([^"]*)"', h)),
    "h1": [txt(x) for x in re.findall(r"<h1[^>]*>(.*?)</h1>", main, re.S)],
    "h2": [txt(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", main, re.S)],
    "h3": [txt(x) for x in re.findall(r"<h3[^>]*>(.*?)</h3>", main, re.S)],
    "znaki_main": len(tekst),
    "ceny_w_tresci": sorted(set(re.findall(r"[^.]{0,60}\d[\d\s]*\s*zł[^.]{0,40}", tekst)))[:10],
    "schema": schema,
    "spec": spec,
    "obrazy": sorted(set(re.sub(r"-\d+x\d+(\.\w+)$", r"\1", i) for i in re.findall(
        r"https://agria\.pl/wp-content/uploads/[^\"'\s]+?\.(?:jpg|jpeg|png|webp)", main))),
    "pdf": sorted(set(re.findall(r"https://agria\.pl/wp-content/uploads/[^\"'\s]+?\.pdf", h))),
    "tekst": tekst,
}
json.dump(r, open(f"{OUT}/{slug}.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in r.items() if k != "tekst"}, ensure_ascii=False, indent=1))
