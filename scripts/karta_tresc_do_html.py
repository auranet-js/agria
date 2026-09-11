#!/usr/bin/env python3
"""Plik treści karty (docs/produkty/pilot/<slug>-tresc.md) → HTML do wdrożenia (T-136).

Z pliku bierze: §2 Meta (title, meta description, focus keyword — kolumna „nowe"),
§3 Lead (→ post_excerpt) i §4 Treść do sekcji „Zapytaj o ofertę" (→ post_content).
Końcówkę karty od <h2 id="zapytajoofertzamwprbk"> przenosi 1:1 z backupu stanu przed zmianą.
Kotwice nawigacji „Na skróty" zostają: #specyfikacja-techniczna, #lokalizacje (sekcja ceny i dostawy),
#najczciejzadawanepytania, #zapytajoofertzamwprbk.

Użycie:
    python3 scripts/karta_tresc_do_html.py 312 docs/produkty/pilot/oxyfertil-90-tresc.md \
        data/produkty/pilot/backup/przed-wdrozeniem-2026-09-11.json data/produkty/pilot/wdrozenie/
"""
import json, os, re, sys, unicodedata
import markdown

post_id, plik, backup, out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
md = open(plik).read()
przed = json.load(open(backup))[post_id]


def sekcja(nr):
    m = re.search(rf"^## {nr}\..*?$(.*?)(?=^## \d+\.|\Z)", md, re.S | re.M)
    return m.group(1)


def slug(t):
    t = re.sub(r"<[^>]+>", "", t).lower()
    return re.sub(r"[^a-z0-9]", "", t)  # jak dotychczasowe id: polskie litery wypadają


# --- meta
meta = {}
for wiersz in sekcja(2).splitlines():
    kom = [k.strip() for k in re.split(r"(?<!\\)\|", wiersz)[1:-1]]
    if len(kom) == 3 and kom[0] not in ("pole", "---"):
        klucz = kom[0].split(" (")[0]
        nowe = kom[2].replace("\\|", "|")
        if "*bez zmian*" in nowe:
            continue
        meta[klucz] = re.sub(r"^\*\*|\*\*$", "", nowe)

# --- lead
lead_md = "\n".join(l[2:] if l.startswith("> ") else "" for l in sekcja(3).splitlines() if l.startswith(">"))
excerpt = markdown.markdown(lead_md.strip()).replace("<p>", "").replace("</p>", "\n\n").strip()

# --- treść
tresc = sekcja(4)
tresc = tresc.split("### H2 Zapytaj o ofertę")[0]
linie = []
for l in tresc.splitlines():
    if l.startswith("Tabela 1:1 z karty PDF"):
        continue
    l = re.sub(r"^### H2 (.*)$", r"## \1", l)
    l = re.sub(r"^\*\*H3 (.*)\*\*$", r"### \1", l)
    l = re.sub(r"^Pod tabelą: ", "", l)
    l = re.sub(r"^\| \*\*Forma dostawy\*\* \| \*\*(.*?)\*\* \|$", r"| Forma dostawy | \1 |", l)
    linie.append(l)
html = markdown.markdown("\n".join(linie), extensions=["tables"])


def h2(m):
    tekst = m.group(1)
    if tekst == "Specyfikacja techniczna":
        return '<h2 id="specyfikacja-techniczna">Specyfikacja techniczna</h2>'
    if tekst == "Najczęściej zadawane pytania":
        return '<h2 id="najczciejzadawanepytania">Najczęściej zadawane pytania</h2>'
    kotwica = '<a name="lokalizacje"></a>\n' if "cena" in tekst.lower() else ""
    return f'{kotwica}<h2 id="{slug(tekst)}">{tekst}</h2>'


html = re.sub(r"<h2>(.*?)</h2>", h2, html)
html = re.sub(r"<h3>(.*?)</h3>", lambda m: f'<h3 id="{slug(m.group(1))}">{m.group(1)}</h3>', html)
# tabele porównawcze (więcej niż 2 kolumny) przewijane w poziomie na telefonie
html = re.sub(r"(<table>(?:(?!</table>).)*?<th>.*?</th>\s*<th>.*?</th>\s*<th>.*?</table>)",
              r'<div style="overflow-x:auto">\1</div>', html, flags=re.S)

# wpautop zamienia pojedynczy \n na <br> — łamania z pliku .md zdejmujemy wewnątrz akapitów i punktów
def jedna_linia(t):
    return re.sub(r"<(p|li|td|th)>(.*?)</\1>", lambda m: f"<{m.group(1)}>" + re.sub(r"\s*\n\s*", " ", m.group(2)) + f"</{m.group(1)}>", t, flags=re.S)


def cudzyslowy(t):  # „X" → „X”
    return re.sub(r'„([^"”<>]*)"', r"„\1”", t)


html = cudzyslowy(jedna_linia(html))
excerpt = cudzyslowy("\n\n".join(re.sub(r"\s*\n\s*", " ", a).strip() for a in excerpt.split("\n\n")))
meta = {k: cudzyslowy(v) for k, v in meta.items()}

ogon = przed["post_content"]
i = ogon.find('<h2 id="zapytajoofertzamwprbk">')
assert i > 0, "brak sekcji Zapytaj o ofertę w stanie przed"
post_content = html + "\n" + ogon[i:]

os.makedirs(out, exist_ok=True)
base = os.path.join(out, os.path.basename(plik).replace("-tresc.md", ""))
open(base + "-post_content.html", "w").write(post_content)
open(base + "-post_excerpt.html", "w").write(excerpt)
json.dump(meta, open(base + "-meta.json", "w"), ensure_ascii=False, indent=1)
print(base, len(post_content.encode()), "B treści,", len(excerpt.encode()), "B leadu")
print(json.dumps(meta, ensure_ascii=False, indent=1))
