#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator strony „Postęp prac i plan" dla AGRII.

Układ wzorowany na victorini/docs/postep/build_postep.py, który z kolei wziął go
z primaauto/docs/kosztorys/build_postep.py: dwie kolumny — lewa „Zrealizowane"
chronologicznie z podziałem na miesiące i sumą godzin pod każdym, prawa „W kolejce"
z widełkami godzin i pytaniami do rozstrzygnięcia.

Dwie różnice wobec Victorini:

1. Victorini ma retainer 20 h/mc, więc rozbija miesiąc na pakiet i ponad pakiet.
   AGRIA jest na ryczałcie 2 000 netto, więc miesiąc pokazuje sumę godzin i wyliczoną
   z niej stawkę godzinową — po to, żeby było widać, czy ryczałt się spina.
2. Godziny mają dwa rodzaje: mierzone i znacznikowe („5 h*"). Rejestr zaczął zapisywać
   realne dopiero 19.08.2026, wcześniejsze pozycje dostały znacznik, żeby nie udawać
   pomiaru. Sumy liczone są osobno i osobno pokazywane.

Doszła też trzecia sekcja „Czekamy na AGRIĘ" — pozycje, których nie ruszymy bez klienta.

Dokument jest **wewnętrzny** (dla Janka), nie klient-facing: pokazuje godziny, numery
zadań i stawkę. Wersja dla AGRII, gdyby powstała, musi mieć kolumnę godzin zdjętą.

Źródło merytoryczne: docs/REJESTR_ZOBOWIAZAN.md. Dane strony: dane/postep.json.

Użycie:
    python3 build_postep.py            # generuje postep.html obok skryptu
    python3 build_postep.py --deploy   # + kopiuje na zahaszowany URL auratest.pl
"""
import json, os, shutil, sys, datetime, html

BASE = os.path.dirname(os.path.abspath(__file__))
DANE = os.path.join(BASE, 'dane')
OUT = os.path.join(BASE, 'postep.html')
DEPLOY_DIR = os.path.expanduser('~/domains/auratest.pl/public_html/ag-postep-7f3c9d21e8b4a6f5')
RYCZALT = 2000


def esc(s):
    return html.escape(str(s), quote=False)


def fmt_h(v):
    if isinstance(v, float) and v == int(v):
        v = int(v)
    return str(v).replace('.', ',')


with open(os.path.join(DANE, 'postep.json'), encoding='utf-8') as f:
    d = json.load(f)

meta = d['meta']
today = datetime.date.today().strftime('%d.%m.%Y')


def klucz_daty(p):
    """Sortowanie malejąco po dacie DD.MM; pozycje bez daty („—") lądują na końcu."""
    try:
        dd, mm = p['data'].split('.')
        return (1, int(mm), int(dd))
    except ValueError:
        return (0, 0, 0)


def blok_miesiaca(m):
    wiersze = []
    for p in sorted(m['pozycje'], key=klucz_daty, reverse=True):
        if p.get('godz'):
            godz = fmt_h(p['godz']) + ('&nbsp;*' if p.get('znacznik') else '')
        else:
            godz = '—'
        ident = f'<span class="tid">{esc(p["id"])}</span>' if p.get('id') and p['id'] != '—' else ''
        wiersze.append(
            f'<tr><td class="data-col">{esc(p["data"])}</td>'
            f'<td>{ident}<strong>{esc(p["tytul"])}</strong>'
            f'<div class="opis">{esc(p["opis"])}</div></td>'
            f'<td class="num">{godz}</td></tr>'
        )

    mierzone = sum(p.get('godz', 0) for p in m['pozycje'] if not p.get('znacznik'))
    znacznik = sum(p.get('godz', 0) for p in m['pozycje'] if p.get('znacznik'))
    razem = mierzone + znacznik

    czesci = []
    if mierzone:
        czesci.append(f'mierzone {fmt_h(round(mierzone, 1))} h')
    if znacznik:
        czesci.append(f'znaczniki {fmt_h(round(znacznik, 1))} h*')
    if m.get('ryczalt', True) and razem:
        # stawka policzona ze znaczników nie jest pomiarem — oznaczamy ją jako orientacyjną
        znak = '' if not znacznik else '≈'
        czesci.append(f'ryczałt {RYCZALT} zł → {znak}{round(RYCZALT / razem)} zł/h')
    rozliczenie = ' · '.join(czesci) if czesci else 'godziny nieodtworzone'

    uwaga = f'<p class="uwaga">{esc(m["uwaga"])}</p>' if m.get('uwaga') else ''

    return f"""<h3>{esc(m['nazwa'])}</h3>
{uwaga}
<table>
<thead><tr><th>Data</th><th>Praca</th><th class="num">h</th></tr></thead>
<tbody>
{chr(10).join(wiersze)}
</tbody>
<tfoot><tr><td colspan="2">Razem — {rozliczenie}</td>
<td class="num">{fmt_h(round(razem, 1)) if razem else '—'}</td></tr></tfoot>
</table>"""


def wiersz_kolejki(t, nr):
    pytania = ''
    if t.get('pytania'):
        li = ''.join(f'<li>{esc(q)}</li>' for q in t['pytania'])
        pytania = f'<div class="pytania"><strong>Do rozstrzygnięcia:</strong><ul>{li}</ul></div>'
    return f"""<tr>
<td><span class="nr">{nr}</span><strong>{esc(t['tytul'])}</strong>
<div class="opis">{esc(t['opis'])}</div>{pytania}
<div class="skala">{esc(t.get('kiedy', ''))}</div></td>
<td class="num">{esc(t.get('godz', '—'))}</td></tr>"""


def wiersz_czekamy(t):
    return f"""<tr>
<td><strong>{esc(t['tytul'])}</strong>
<div class="opis">{esc(t['opis'])}</div></td>
<td class="num czeka">od {esc(t['od'])}</td></tr>"""


# najnowszy miesiąc u góry — dane w JSON trzymamy chronologicznie
miesiace_html = '\n'.join(blok_miesiaca(m) for m in reversed(d['miesiace']))
kolejka_html = '\n'.join(wiersz_kolejki(t, i) for i, t in enumerate(d['kolejka'], 1))
czekamy_html = '\n'.join(wiersz_czekamy(t) for t in d.get('czekamy', []))

suma_mierzone = sum(p.get('godz', 0) for m in d['miesiace'] for p in m['pozycje'] if not p.get('znacznik'))
suma_znacznik = sum(p.get('godz', 0) for m in d['miesiace'] for p in m['pozycje'] if p.get('znacznik'))
ile_poz = sum(len(m['pozycje']) for m in d['miesiace'])

html_doc = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{esc(meta['tytul'])}</title>
<style>
:root {{
  --ink: #1a2332; --ink-2: #4a5568; --ink-3: #8b95a5;
  --accent: #1f5c2e; --accent-soft: #eaf3ea;
  --surface: #ffffff; --bg: #f4f6f9; --line: #e2e7ee;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font: 15px/1.55 -apple-system, "Segoe UI", Roboto, Arial, sans-serif; color: var(--ink); background: var(--bg); }}
.wrap {{ max-width: none; margin: 0; padding: 32px 40px 80px; }}
.cols {{ display: grid; grid-template-columns: minmax(0,1fr) minmax(0,1fr); gap: 40px; align-items: start; }}
.cols > section {{ min-width: 0; }}
.cols h2 {{ margin-top: 0; }}
header.top {{ border-bottom: 3px solid var(--accent); padding-bottom: 20px; margin-bottom: 28px; }}
header.top h1 {{ font-size: 26px; line-height: 1.25; }}
header.top .sub {{ color: var(--ink-2); margin-top: 6px; }}
header.top .stamp {{ color: var(--ink-3); font-size: 13px; margin-top: 10px; }}
h2 {{ font-size: 20px; margin: 0 0 6px; }}
h3 {{ font-size: 16px; margin: 30px 0 4px; color: var(--accent); }}
h3:first-of-type {{ margin-top: 18px; }}
.lead {{ color: var(--ink-2); margin-bottom: 16px; }}
.uwaga {{ color: var(--ink-2); font-size: 13.5px; margin: 4px 0 0; font-style: italic; }}
table {{ width: 100%; border-collapse: collapse; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; margin: 12px 0; }}
th {{ text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.4px; color: var(--ink-2); background: var(--accent-soft); padding: 10px 14px; border-bottom: 1px solid var(--line); }}
th.num, td.num {{ text-align: right; }}
td {{ padding: 12px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }}
tr:last-child td {{ border-bottom: none; }}
td.num {{ font-variant-numeric: tabular-nums; font-weight: 600; white-space: nowrap; }}
td.num.czeka {{ font-weight: 500; color: var(--ink-3); font-size: 13px; }}
td.data-col {{ white-space: nowrap; color: var(--ink-2); font-size: 13px; font-variant-numeric: tabular-nums; }}
tfoot td {{ background: var(--accent-soft); font-weight: 700; font-size: 13.5px; }}
.opis {{ color: var(--ink-2); font-weight: 400; margin-top: 4px; font-size: 14px; }}
.nr {{ display: inline-block; min-width: 20px; font-size: 11px; font-weight: 700; color: #fff; background: var(--accent); border-radius: 4px; padding: 1px 5px; margin-right: 7px; text-align: center; vertical-align: 1px; }}
.tid {{ display: inline-block; font-size: 11px; font-weight: 700; color: var(--accent); background: var(--accent-soft); border-radius: 4px; padding: 1px 6px; margin-right: 6px; vertical-align: 1px; font-variant-numeric: tabular-nums; }}
.skala {{ color: var(--ink-3); font-size: 12.5px; margin-top: 6px; }}
.pytania {{ margin-top: 8px; padding: 8px 12px; background: var(--accent-soft); border-radius: 6px; font-size: 13.5px; color: var(--ink-2); }}
.pytania strong {{ font-size: 12.5px; }}
.pytania ul {{ margin: 4px 0 0; padding-left: 18px; }}
.pytania li {{ margin: 2px 0; }}
.bilans {{ background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 8px; padding: 12px 16px; margin-bottom: 18px; font-size: 14px; color: var(--ink-2); }}
.bilans strong {{ color: var(--ink); }}
footer {{ margin-top: 60px; padding-top: 16px; border-top: 1px solid var(--line); color: var(--ink-3); font-size: 12.5px; }}
@media (max-width: 1100px) {{
  .cols {{ grid-template-columns: 1fr; gap: 8px; }}
  .cols > section + section h2 {{ margin-top: 36px; }}
}}
@media (max-width: 720px) {{
  .wrap {{ padding: 24px 16px 60px; }}
  td.data-col {{ font-size: 11px; }}
}}
@media print {{ body {{ background: #fff; }} .wrap {{ padding: 0; }} }}
</style>
</head>
<body>
<div class="wrap">

<header class="top">
<h1>{esc(meta['tytul'])}</h1>
<div class="sub">{esc(meta['podtytul'])}</div>
<div class="stamp">Stan na {today} · dokument wewnętrzny Auranet, aktualizowany na bieżąco</div>
</header>

<div class="cols">
<section>
<h2>Zrealizowane</h2>
<div class="bilans"><strong>{ile_poz} pozycji</strong> · {fmt_h(round(suma_mierzone, 1))} h mierzonych
· {fmt_h(round(suma_znacznik, 1))} h w znacznikach<br>{esc(meta['lead'])}</div>
{miesiace_html}
</section>

<section>
<h2>W kolejce</h2>
{f'<p class="lead">{esc(d["kolejka_lead"])}</p>' if d.get('kolejka_lead') else ''}
<table>
<thead><tr><th>Zadanie — od najpilniejszego</th><th class="num">h</th></tr></thead>
<tbody>
{kolejka_html}
</tbody>
</table>

<h2 style="margin-top:36px">Czekamy na AGRIĘ</h2>
{f'<p class="lead">{esc(d["czekamy_lead"])}</p>' if d.get('czekamy_lead') else ''}
<table>
<thead><tr><th>Na co czekamy</th><th class="num">od</th></tr></thead>
<tbody>
{czekamy_html}
</tbody>
</table>
</section>
</div>

<footer>Auranet · Jan Schenk · js@auranet.com.pl · dokument niepubliczny, wygenerowany {today}
· źródło: docs/REJESTR_ZOBOWIAZAN.md</footer>

</div>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html_doc)
print(f'OK: {OUT}')
print(f'   {ile_poz} pozycji · {fmt_h(round(suma_mierzone,1))} h mierzonych · {fmt_h(round(suma_znacznik,1))} h*')

if '--deploy' in sys.argv:
    os.makedirs(DEPLOY_DIR, exist_ok=True)
    shutil.copy(OUT, os.path.join(DEPLOY_DIR, 'index.html'))
    print(f'Deploy: {DEPLOY_DIR}/index.html')
    print('URL: https://auratest.pl/' + os.path.basename(DEPLOY_DIR) + '/')
