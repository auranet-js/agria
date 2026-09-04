#!/usr/bin/env python3
"""T-067 — weryfikacja tablic kalkulatora wobec źródła IUNG-PIB.

Porównuje tablice zaszyte w `class-iung-data.php` z tekstem wyciągniętym
z publikacji IUNG-PIB 2022 „Zasady ustalania dawek wapna w doradztwie nawozowym"
(`data/zrodla/`). Wynik: lista rozjazdów albo cisza.

Użycie: python3 scripts/weryfikacja_tablic_iung.py
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF_TXT = ROOT / "data/zrodla/IUNG-PIB-2022-zasady-ustalania-dawek-wapna.txt"
PHP = ROOT / "src/plugins/agria-by-auranet/modules/liming-calculator/includes/class-iung-data.php"

def licz(t):
    """'2,8' -> 2.8 ; '-' -> None"""
    t = t.strip()
    if t in ("-", "–", "—", ""):
        return None
    return float(t.replace(",", "."))

# ---------- źródło: PDF ----------
def z_pdf():
    txt = PDF_TXT.read_text(encoding="utf-8")
    orne, kat = {}, None
    nazwy = {"Gleby bardzo lekkie": "bardzo_lekka", "Gleby lekkie": "lekka",
             "Gleby średnie": "srednia", "Gleby ciężkie": "ciezka"}
    # grunty orne: sekcja od "DAWKI CaO NA GRUNTACH ORNYCH" do użytków zielonych
    sek = txt.split("DAWKI CaO NA GRUNTACH ORNYCH")[1].split("DAWKI CaO NA UŻYTKACH ZIELONYCH")[0]
    for lin in sek.splitlines():
        s = lin.strip()
        for n, k in nazwy.items():
            if s == n:
                kat = k
        m = re.match(r"^(\d,\d)\s+(\d+,\d)\s+(\d+,\d)\s+([\d,]+|-|–|—)$", s)
        if m and kat:
            orne.setdefault(kat, {})[m.group(1).replace(",", ".")] = (
                licz(m.group(2)), licz(m.group(3)), licz(m.group(4)))
    # użytki zielone
    uz = {}
    sek2 = txt.split("DAWKI CaO NA UŻYTKACH ZIELONYCH")[1]
    for lin in sek2.splitlines():
        m = re.match(r"^(\d,\d)\s+(\d,\d)\s+(\d,\d)\s+(\d,\d)\s+(\d,\d)$", lin.strip())
        if m:
            uz[m.group(1).replace(",", ".")] = [licz(m.group(i)) for i in range(2, 6)]
    return orne, uz

# ---------- kod: PHP ----------
def z_php():
    src = PHP.read_text(encoding="utf-8")
    orne, kat = {}, None
    blok = src.split("get_arable_doses")[1].split("get_grassland_doses")[0]
    for lin in blok.splitlines():
        m = re.search(r"'(bardzo_lekka|lekka|srednia|ciezka)'\s*=>", lin)
        if m:
            kat = m.group(1)
        m = re.search(r"'(\d\.\d)'\s*=>\s*\[([\d.]+),\s*([\d.]+),\s*([\d.]+)\]", lin)
        if m and kat:
            orne.setdefault(kat, {})[m.group(1)] = (
                float(m.group(2)), float(m.group(3)), float(m.group(4)))
    uz = {}
    blok2 = src.split("get_grassland_doses")[1].split("get_carbon_index")[0]
    for lin in blok2.splitlines():
        m = re.search(r"'(\d\.\d)'\s*=>\s*\[([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\]", lin)
        if m:
            uz[m.group(1)] = [float(m.group(i)) for i in range(2, 6)]
    return orne, uz

po, pu = z_pdf()
ko, ku = z_php()
bledy, n = [], 0

for kat in ("bardzo_lekka", "lekka", "srednia", "ciezka"):
    zr, kd = po.get(kat, {}), ko.get(kat, {})
    if set(zr) != set(kd):
        bledy.append(f"[{kat}] różne zestawy pH — źródło {sorted(set(zr)-set(kd))}, kod {sorted(set(kd)-set(zr))}")
    for ph in sorted(set(zr) & set(kd)):
        n += 1
        z, k = zr[ph], kd[ph]
        # w źródle „-" w części II oznacza brak podziału; w kodzie to 0
        z_norm = (z[0], z[1], 0.0 if z[2] is None else z[2])
        if z_norm != k:
            bledy.append(f"[{kat}] pH {ph}: źródło {z_norm} ≠ kod {k}")

if set(pu) != set(ku):
    bledy.append(f"[użytki zielone] różne zestawy pH: {sorted(set(pu)^set(ku))}")
for ph in sorted(set(pu) & set(ku)):
    n += 1
    if pu[ph] != ku[ph]:
        bledy.append(f"[użytki zielone] pH {ph}: źródło {pu[ph]} ≠ kod {ku[ph]}")

print(f"Porównanych wierszy: {n} "
      f"(grunty orne {sum(len(v) for v in po.values())}, użytki zielone {len(pu)})")
if bledy:
    print(f"\nROZJAZDY ({len(bledy)}):")
    for b in bledy:
        print("  ⚠️ " + b)
    sys.exit(1)
print("\nZgodność pełna — każdy wiersz kodu ma pokrycie w publikacji.")
