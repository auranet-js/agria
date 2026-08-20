#!/usr/bin/env python3
"""Robi z kart katalogowych (PDF druk 2026) obrazy zdatne do wystawienia na OLX.

Po co: karta katalogowa jest najlepszym materiałem parametrowym, jaki mamy — logo, zdjęcie
produktu, korzyści, pełna tabela z kartami producentów. Ale w postaci drukowej ma trzy rzeczy,
których na zdjęciu ogłoszenia być NIE MOŻE:

  1. plakietka z kodem QR („KALKULATOR WAPNOWANIA") — regulamin OLX traktuje zdjęcia jako treść
     ogłoszenia, więc kod prowadzący na zewnątrz jest tam odnośnikiem. Z plansz produktowych
     usuwaliśmy go już w `zdjecia.py`, tu obowiązuje ta sama zasada;
  2. stopka z `www.agria.pl` i numerem telefonu — adres WWW i dane kontaktowe w treści ogłoszenia;
Skrypt NIE rusza tabeli parametrów. Dwa wiersze warte świadomej decyzji przed emisją:
„Magazyn" wypisuje zakłady dostawców (Sitkówka, Bukowa, Celiny) — to samo pole `build_adverts.py`
wycina z opisu ogłoszenia; „Forma dostawy" wymienia worki i big-bagi, a T-002 zdjął formy dostawy
z kart na stronie na polecenie Pawła. Jedno i drugie zostaje na karcie, dopóki Janek nie powie inaczej.

Geometria jest stała, bo wszystkie 17 kart siedzi na jednym szablonie InDesign — podana jako
ułamki wymiaru strony, więc działa niezależnie od DPI renderu (tak samo jak PLAKIETKA w zdjecia.py).

Wymaga ghostscriptu (`gs`) i ImageMagicka. Pillow NIE jest potrzebny.

Użycie: karty_katalogowe.py <katalog wyjściowy> [dpi]
"""
import os
import subprocess
import sys

PDF = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "assets", "print", "catalog", "Agria-katalog-2026-05-04-web.pdf")

# strona w PDF → nazwa karty w GALERIE/FOTO (build_adverts.py). Strony 1–3 i 21–23 to okładka,
# spis branż i kontakt — nie są kartami produktu.
STRONY = {
    4:  "agrobielik-70",
    5:  "agrobielik-90-0-3",
    6:  "agrobielik-90-2-8",
    7:  "oxyfertil-90",
    8:  "tlenkowe-z-magnezem",
    9:  "mieszanka-tlenkowo-weglanowa",
    10: "weglanowe-granulowane",
    11: "weglanowe-odmiana-04",
    12: "weglanowe-magnez-granulowane",
    13: "weglanowe-magnez-odmiana-04",
    14: "weglanowe-magnez-odmiana-05",
    15: "kreda-nawozowa-granulowana",
    16: "kreda-nawozowa-sypka",
    17: "kreda-pastewna",
    18: "dolomit",
    19: "wapno-hydratyzowane-bielik",
    20: "wapno-palone-mielone",
}

# ułamki wymiaru strony (x0, y0, x1, y1)
PLAKIETKA_QR = (0.784, 0.340, 0.968, 0.483)   # kod QR + podpis „KALKULATOR WAPNOWANIA" + cień
STOPKA       = (0.000, 0.958, 1.000, 1.000)   # ciemnozielony pas z www i telefonem
STOPKA_KOLOR = "srgb(10,64,48)"


def render(dpi, tmp):
    os.makedirs(tmp, exist_ok=True)
    # -dTextAlphaBits/-dGraphicsAlphaBits są tu obowiązkowe, nie kosmetyczne: bez nich
    # ghostscript renderuje bez antyaliasingu i cienkie kroje rozpadają się na kreski —
    # akapit opisu produktu jest wtedy nieczytelny, a półpauzy i część diakrytyków znikają.
    subprocess.run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=jpeg", "-dJPEGQ=94",
                    "-dTextAlphaBits=4", "-dGraphicsAlphaBits=4",
                    "-r" + str(dpi), "-sOutputFile=" + os.path.join(tmp, "str-%02d.jpg"), PDF],
                   check=True)


def wymiary(f):
    o = subprocess.run(["magick", "identify", "-format", "%w %h", f],
                       capture_output=True, text=True, check=True).stdout
    return tuple(int(v) for v in o.split())


def prostokat(w, h, ramka):
    x0, y0, x1, y1 = ramka
    return round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)


def wyczysc(src, dst):
    """Zamalowuje plakietkę QR na biało (tło jest tam czyste) i zalewa stopkę kolorem pasa."""
    w, h = wymiary(src)
    qx0, qy0, qx1, qy1 = prostokat(w, h, PLAKIETKA_QR)
    sx0, sy0, sx1, sy1 = prostokat(w, h, STOPKA)
    subprocess.run([
        "magick", src,
        "-fill", "white", "-draw", f"rectangle {qx0},{qy0} {qx1},{qy1}",
        "-fill", STOPKA_KOLOR, "-draw", f"rectangle {sx0},{sy0} {sx1},{sy1}",
        "-quality", "92", dst], check=True)
    return wymiary(dst)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    dpi = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    os.makedirs(out, exist_ok=True)
    tmp = os.path.join(out, ".render")
    render(dpi, tmp)
    for nr, nazwa in sorted(STRONY.items()):
        src = os.path.join(tmp, f"str-{nr:02d}.jpg")
        dst = os.path.join(out, f"agria-karta-{nazwa}.jpg")
        w, h = wyczysc(src, dst)
        kb = os.path.getsize(dst) // 1024
        print(f"  agria-karta-{nazwa}.jpg  ({w}x{h}, {kb} kB)  ← str. {nr}")
    print(f"→ {out}")
