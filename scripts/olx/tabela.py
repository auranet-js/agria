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
            "woj": REG.get(r["region_id"], "?"), "zaklad": r["zaklad"], "km": r["km_z_zakladu"],
            "transport": r["transport_udzial"],
        }


def markdown():
    rows = list(wiersze())
    out = ["| # | SKU | Ogłoszenie | Cena w polu | Miejscowość | Województwo | Zakład wysyłkowy | km z zakładu | Transport jako % ceny |",
           "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['lp']} | {r['sku']} | {r['tytul']} | {r['cena']} zł | {r['miasto']} | "
                   f"{r['woj']} | {r['zaklad']} | {r['km']} | {r['transport']*100:.0f}% |")
    return "\n".join(out)


def wzorzec():
    """Pierwsze ogłoszenie z gotowego ładunku — dokładnie to, co pójdzie do OLX."""
    pay = json.load(open(os.path.join(D, "adverts-payload.json"), encoding="utf-8"))
    a = pay[0]
    opis = a["description"].replace("&", "&amp;").replace("<", "&lt;")
    return f"""<section>
<h2>Wzór treści — tak wygląda jedno ogłoszenie</h2>
<p class="meta">Poniżej treść gotowa do publikacji, bez skrótów. Pozostałe 199 ogłoszeń mają tę samą
budowę: zdanie wprowadzające pod konkretne zastosowanie · parametry z karty produktowej ·
zastosowanie i dawkowanie · formy dostawy i cena · dostępność · dokumenty · stopka firmowa.
Zmienia się produkt, miejscowość i to pierwsze zdanie.</p>
<div class="karta">
<p class="etyk">Tytuł ogłoszenia</p>
<p class="tyt">{a['title']}</p>
<p class="etyk">Cena w polu ogłoszenia</p>
<p class="tyt">{a['price']['value']} zł <span class="slabe">(do negocjacji)</span></p>
<p class="etyk">Treść</p>
<pre>{opis}</pre>
<p class="etyk">Zdjęcia · kontakt · kategoria</p>
<p>{len(a['images'])} zdjęć · telefon <strong>{a['contact']['phone']}</strong> w polu kontaktowym
formularza · konto firmowe · kategoria Rolnictwo &gt; Nawozy</p>
</div>
<p class="meta">Numer telefonu jest wyłącznie w polu kontaktowym — regulamin OLX zabrania numerów
w treści opisu. To ważne, bo odsłona numeru jest u Was źródłem praktycznie wszystkich kontaktów.</p>
</section>"""


def podsumowanie(rows):
    grup = len({r["tytul"] for r in rows})
    miast = len({r["miasto"] for r in rows})
    pozycje = []
    for tytul in dict.fromkeys(r["tytul"] for r in rows):
        g = [r for r in rows if r["tytul"] == tytul]
        pozycje.append(f"<tr><td>{tytul}</td><td class='num'>{g[0]['cena']} zł</td>"
                       f"<td>{g[0]['cena_opis']}</td><td class='num'>{len(g)}</td></tr>")
    return f"""<section>
<h2>Co uruchamiamy</h2>
<p><strong>{len(rows)} ogłoszeń</strong> w kategorii Rolnictwo &gt; Nawozy: {grup} pozycji
asortymentowych rozłożonych na <strong>{miast} miejscowości</strong> w 8 województwach.
Każde ogłoszenie ma własny tytuł pod zastosowanie, własną miejscowość i pełne parametry z karty
produktowej. Wystawiamy je my, przez oficjalne API OLX, z Waszego konta.</p>
<h2>Kwoty</h2>
<table><thead><tr><th>Pozycja</th><th class="num">Kwota</th><th>Kto płaci</th></tr></thead><tbody>
<tr><td>Pakiet OLX <strong>Premium 200</strong>, kategoria Nawozy — ważny 30 dni</td>
<td class="num"><strong>1 199,99 zł brutto</strong></td><td>AGRIA, ze swojego konta OLX</td></tr>
<tr><td>To samo w przeliczeniu na jedno ogłoszenie</td><td class="num">6,00 zł</td>
<td class="slabe">najniższa stawka jednostkowa w całym cenniku OLX</td></tr>
<tr><td>Przygotowanie kanału — treści, siatka miejscowości, spięcie z API</td>
<td class="num">1 800 zł netto jednorazowo</td><td>Auranet</td></tr>
<tr><td>Prowadzenie — odczyt wyników, korekty, wymiana ogłoszeń</td>
<td class="num">300 zł netto / mies.</td><td>Auranet</td></tr>
</tbody></table>
<p class="meta">Koszt kanału po pierwszym miesiącu: około <strong>1 500 zł miesięcznie</strong>.
Przy wskaźnikach zmierzonych na Waszych własnych ogłoszeniach daje to ostrożnie ~50, realnie ~150,
a przy dobrym zadziałaniu tytułów ~230 odsłon numeru telefonu miesięcznie — czyli od 6,50 do 30 zł
za jeden kontakt od zainteresowanego.</p>
<p class="meta"><strong>Uwaga przy zakupie:</strong> na ekranie pakietów OLX podpowiada u góry
„Kup ponownie" i Megapakiet — to inny, droższy wariant (2 199,99 zł za te same 200 ogłoszeń).
Właściwa ścieżka: Twoje ogłoszenia → Kup pakiet ogłoszeń → Rolnictwo → Nawozy → 200 → <strong>Premium</strong>.</p>
<h2>Ceny w ogłoszeniach</h2>
<p class="meta">Ceny netto za sam towar, bez transportu — dokładnie w takiej formie, w jakiej pójdą
do treści. Jeśli któraś ma być inna, poprawiamy przed publikacją.</p>
<table><thead><tr><th>Pozycja</th><th class="num">Cena w polu</th><th>Zapis w treści</th>
<th class="num">Ogłoszeń</th></tr></thead><tbody>{''.join(pozycje)}</tbody></table>
</section>"""


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
            f"<td class='zak'>{r['zaklad']}</td><td class='num'>{r['km']}</td>"
            f"<td class='num {'hot' if r['transport'] > 0.4 else ''}'>{r['transport']*100:.0f}%</td></tr>"
            for r in g)
        czesci.append(f"""<section>
<h2>{tytul}</h2>
<p class="meta"><strong>{r0['sku']}</strong> · cena w polu ogłoszenia: <strong>{r0['cena']} zł</strong>
· {r0['cena_opis']} · <strong>{len(g)}</strong> ogłoszeń · wysyłka z: {', '.join(sorted({x['zaklad'] for x in g}))}</p>
<table><thead><tr><th>#</th><th>Miejscowość</th><th>Województwo</th>
<th>Zakład wysyłkowy</th><th>km z zakładu</th><th>Transport / cena</th></tr></thead>
<tbody>{wiersze_html}</tbody></table>
</section>""")

    miast = len({r["miasto"] for r in rows})
    woj = len({r["woj"] for r in rows})
    return f"""<title>AGRIA — ogłoszenia OLX</title>
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
.zak {{ color:var(--slabe); }}
.slabe {{ color:var(--slabe); font-weight:400; }}
.karta {{ border:1px solid var(--linia); border-radius:.4rem; padding:1rem 1.2rem; margin:.8rem 0 .6rem; }}
.etyk {{ color:var(--slabe); font-size:.72rem; text-transform:uppercase; letter-spacing:.05em; margin:1rem 0 .15rem; }}
.karta .etyk:first-child {{ margin-top:0; }}
.tyt {{ font-size:1.05rem; font-weight:600; margin:0; }}
pre {{ white-space:pre-wrap; font:inherit; margin:0; background:var(--pas); padding:.9rem 1rem; border-radius:.3rem; }}
h3 {{ font-size:.95rem; margin:2.4rem 0 .8rem; color:var(--akcent); }}
</style>
<h1>AGRIA — ogłoszenia OLX, wersja do publikacji</h1>
<p class="lead">Stan na 17 sierpnia 2026. <strong>{len(rows)} ogłoszeń</strong>, {len(grupy)} pozycji asortymentowych,
<strong>{miast} miejscowości</strong>, {woj} województw. Wszystko poniżej jest gotowe — czeka wyłącznie na
opłacony pakiet. Jeśli coś ma wyglądać inaczej, teraz jest właściwy moment.</p>
{podsumowanie(rows)}
{wzorzec()}
<h3>Gdzie będzie wystawione — pełna lista</h3>
<p class="meta">Miejscowości nie są dobierane na oko. Dla każdej liczymy, jaką część ceny tony zjada przewóz
z zakładu, z którego dany produkt faktycznie jedzie — <span class="hot">czerwone</span> to pozycje powyżej 40%,
które przejrzymy przy pierwszej korekcie. Dlatego np. kreda granulowana sięga dalej na Mazowsze:
wysyłana jest z Kornicy, nie z Niedomic.</p>
<div class="scroll">{''.join(czesci)}</div>
"""


if __name__ == "__main__":
    md = os.path.join(HERE, "..", "..", "docs", "offers", "OLX_TABELA_OGLOSZEN.md")
    naglowek = ("# OLX — pełna rozpiska ogłoszeń\n\n"
                "> Generowane z `data/olx/plan-ogloszen.json` przez `scripts/olx/tabela.py`.\n"
                "> Nie edytować ręcznie — zmiany wprowadzać w `grid.py` / `plan.py` i przegenerować.\n\n")
    open(md, "w", encoding="utf-8").write(naglowek + markdown() + "\n")
    print(f"→ {os.path.relpath(md)}")
    if len(sys.argv) > 1:
        open(sys.argv[1], "w", encoding="utf-8").write(html())
        print(f"→ {sys.argv[1]}")
