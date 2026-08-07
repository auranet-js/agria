#!/usr/bin/env python3
"""Wyciąga tabelę „Specyfikacja techniczna" z wyrenderowanych kart produktowych agria.pl.

Czytamy RENDER, nie bazę — parametry żyją w 4 warstwach (atrybuty pa_*, post_content,
Elementor, meta SEO) i tylko render pokazuje to, co widzi klient.
Wynik: data/olx/product-specs.json — źródło opisów ogłoszeń OLX.
"""
import html
import json
import os
import re
import subprocess

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "olx", "product-specs.json")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"


def fetch(url):
    return subprocess.run(["curl", "-sS", "-A", UA, url], capture_output=True, text=True, check=True).stdout


def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def parse(url):
    h = fetch(url)
    out = {"url": url}

    m = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    out["title"] = strip_tags(m.group(1)) if m else None

    spec = {}
    m = re.search(r"Specyfikacja techniczna(.*?)</table>", h, re.S)
    if m:
        for row in re.findall(r"<tr>(.*?)</tr>", m.group(1), re.S):
            cells = [strip_tags(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
            if len(cells) == 2 and cells[0] != "Parametr":
                spec[cells[0]] = cells[1]
    out["spec"] = spec

    # akapit wprowadzający pod pierwszym H2 — baza pod lead opisu ogłoszenia
    m = re.search(r"<h2[^>]*>.*?</h2>\s*<p>(.*?)</p>", h, re.S)
    out["lead"] = strip_tags(m.group(1)) if m else None

    # obrazy z galerii produktu (publiczne URL-e, nadają się do POST /partner/adverts)
    imgs = re.findall(r"https://agria\.pl/wp-content/uploads/[^\"'\s]+?\.(?:jpg|jpeg|png|webp)", h)
    CHROME = ("agria-full-on-white", "agria-logo-poziom", "-logo-", "placeholder")
    seen, uniq = set(), []
    for i in imgs:
        base = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", i)  # odrzuć warianty rozmiarowe WP
        if any(c in base for c in CHROME):
            continue
        if base not in seen:
            seen.add(base)
            uniq.append(base)
    out["images"] = uniq[:12]
    return out


if __name__ == "__main__":
    sm = fetch("https://agria.pl/product-sitemap.xml")
    # Permalink Manager daje karcie adres /<kategoria>/<slug>/, nie /produkt/<slug>/
    urls = [u for u in re.findall(r"<loc>(https://agria\.pl/[^<]+)</loc>", sm) if u.count("/") == 5]
    print(f"kart produktowych w sitemapie: {len(urls)}")
    data = []
    for u in urls:
        row = parse(u)
        data.append(row)
        print(f"  {row['title'][:55]:<55} parametrów: {len(row['spec']):>2}  zdjęć: {len(row['images'])}")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    print(f"→ {os.path.relpath(OUT)}")
