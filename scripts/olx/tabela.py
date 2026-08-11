#!/usr/bin/env python3
"""Wypisuje pełną tabelę zaplanowanych ogłoszeń — markdown do repo + HTML do przeglądania."""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")
REG = {3: "dolnośląskie", 15: "kujawsko-pom.", 8: "lubelskie", 9: "lubuskie", 7: "łódzkie",
       4: "małopolskie", 2: "mazowieckie", 12: "opolskie", 17: "podkarpackie", 18: "podlaskie",
       5: "pomorskie", 6: "śląskie", 13: "świętokrzyskie", 14: "warm.-maz.",
       1: "wielkopolskie", 11: "zachodniopom."}


def wiersze():
    plan = json.load(open(os.path.join(D, "plan-ogloszen.json"), encoding="utf-8"))
    for i, r in enumerate(plan, 1):
        yield {
            "lp": i, "sku": r["sku"], "tytul": r["title"], "cena": r["price"],
            "cena_opis": r["cena_opis"], "miasto": r["city"],
            "woj": REG.get(r["region_id"], "?"), "km": r["km_z_zakladu"],
            "transport": r["transport_udzial"],
        }


def markdown():
    rows = list(wiersze())
    out = ["| # | SKU | Ogłoszenie | Cena w polu | Miejscowość | Województwo | km z zakładu | Transport jako % ceny |",
           "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['lp']} | {r['sku']} | {r['tytul']} | {r['cena']} zł | {r['miasto']} | "
                   f"{r['woj']} | {r['km']} | {r['transport']*100:.0f}% |")
    return "\n".join(out)


def html():
    rows = list(wiersze())
    grupy = collections.OrderedDict()
    for r in rows:
        grupy.setdefault(r["tytul"], []).append(r)

    czesci = []
    for tytul, g in grupy.items():
        r0 = g[0]
        wiersze_html = "\n".join(
            f"<tr><td>{r['lp']}</td><td>{r['miasto']}</td><td>{r['woj']}</td>"
            f"<td class='num'>{r['km']}</td>"
            f"<td class='num {'hot' if r['transport'] > 0.4 else ''}'>{r['transport']*100:.0f}%</td></tr>"
            for r in g)
        czesci.append(f"""<section>
<h2>{tytul}</h2>
<p class="meta"><strong>{r0['sku']}</strong> · cena w polu ogłoszenia: <strong>{r0['cena']} zł</strong>
· {r0['cena_opis']} · <strong>{len(g)}</strong> ogłoszeń</p>
<table><thead><tr><th>#</th><th>Miejscowość</th><th>Województwo</th>
<th>km z zakładu</th><th>Transport / cena</th></tr></thead>
<tbody>{wiersze_html}</tbody></table>
</section>""")

    miast = len({r["miasto"] for r in rows})
    woj = len({r["woj"] for r in rows})
    return f"""<title>AGRIA — 100 ogłoszeń OLX, pełna rozpiska</title>
<style>
:root {{ --tlo:#fff; --tekst:#1b1b1b; --slabe:#666; --linia:#e2e2e2; --akcent:#354E33; --hot:#a33; --pas:#fafafa; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --tlo:#151715; --tekst:#e8e8e6; --slabe:#9a9a95; --linia:#2c2f2c; --akcent:#8fbf87; --hot:#e08d8d; --pas:#1b1e1b; }} }}
:root[data-theme="dark"] {{ --tlo:#151715; --tekst:#e8e8e6; --slabe:#9a9a95; --linia:#2c2f2c; --akcent:#8fbf87; --hot:#e08d8d; --pas:#1b1e1b; }}
body {{ background:var(--tlo); color:var(--tekst); font:16px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;
  max-width:60rem; margin:0 auto; padding:2rem 1.2rem 4rem; }}
h1 {{ font-size:1.6rem; margin:0 0 .3rem; }}
h2 {{ font-size:1.05rem; margin:0 0 .2rem; color:var(--akcent); }}
.lead {{ color:var(--slabe); margin:0 0 2rem; }}
.meta {{ color:var(--slabe); font-size:.88rem; margin:0 0 .6rem; }}
section {{ margin:0 0 2.2rem; }}
.scroll {{ overflow-x:auto; }}
table {{ border-collapse:collapse; width:100%; font-size:.9rem; }}
th, td {{ text-align:left; padding:.35rem .6rem; border-bottom:1px solid var(--linia); }}
th {{ font-weight:600; color:var(--slabe); font-size:.8rem; text-transform:uppercase; letter-spacing:.03em; }}
tbody tr:nth-child(even) {{ background:var(--pas); }}
.num {{ text-align:right; font-variant-numeric:tabular-nums; }}
.hot {{ color:var(--hot); font-weight:600; }}
</style>
<h1>AGRIA — 100 ogłoszeń OLX, pełna rozpiska</h1>
<p class="lead">Stan na 7 sierpnia 2026. Dziesięć produktów, <strong>{miast} miejscowości</strong>,
{woj} województw. Kolumna „transport / cena" pokazuje, jaką część ceny tony zjada przewóz
z najbliższego zakładu wysyłkowego — <span class="hot">czerwone</span> to pozycje powyżej 40%,
do przejrzenia przy pierwszej korekcie.</p>
<div class="scroll">{''.join(czesci)}</div>
"""


if __name__ == "__main__":
    md = os.path.join(HERE, "..", "..", "docs", "offers", "OLX_TABELA_OGLOSZEN.md")
    naglowek = ("# OLX — pełna rozpiska 100 ogłoszeń\n\n"
                "> Generowane z `data/olx/plan-ogloszen.json` przez `scripts/olx/tabela.py`.\n"
                "> Nie edytować ręcznie — zmiany wprowadzać w `grid.py` / `plan.py` i przegenerować.\n\n")
    open(md, "w", encoding="utf-8").write(naglowek + markdown() + "\n")
    print(f"→ {os.path.relpath(md)}")
    if len(sys.argv) > 1:
        open(sys.argv[1], "w", encoding="utf-8").write(html())
        print(f"→ {sys.argv[1]}")
