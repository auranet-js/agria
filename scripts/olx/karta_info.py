#!/usr/bin/env python3
"""Robi kartę informacyjną do galerii ogłoszenia: kod QR do kalkulatora + zakres oferty.

Dlaczego kod QR wraca
---------------------
`OLX_BASELINE_2026-08-07.md` §„QR na zdjęciach to jedyna działająca droga OLX → strona":
w całej kategorii tylko 5 ogłoszeń na 1 204 ma adres WWW w opisie, a numery telefonu sprzedawcy
rozbijają gwiazdkami — czyli tekstowa droga na stronę praktycznie nie istnieje. Decyzja z tamtego
dokumentu brzmi: **zostawiamy kod, dokładając UTM**, i nie budujemy na nim jedynej ścieżki pomiaru.
`2026-08-PLAN_OLX.md` §247 dopisuje, że UTM wchodzi „przy najbliższej rewizji grafik, razem
z ujęciami pod zastosowanie" — czyli teraz.

Kod nie wraca na plansze produktowe, tylko na OSOBNĄ kartę. Powód jest ten sam, dla którego
`zdjecia.py` go stamtąd usuwa: plansza to zdjęcie towaru i ma pokazywać towar. Kod na własnej
karcie jest czytelny (490 px zamiast plakietki wielkości znaczka), skanuje się z miniatury
i nie zaśmieca kadru produktu.

Ryzyko regulaminowe jest znane i świadomie przyjęte: regulamin OLX mówi, że „Treść Ogłoszenia
stanowią również dodane w ramach niego zdjęcia", więc kod prowadzący na zewnątrz jest tam
odnośnikiem. Chodził na koncie AGRII rok bez interwencji — to tolerancja, nie zgoda.

UTM niesie też `utm_content` z nazwą karty produktowej, więc w GA4 widać, KTÓRY produkt
przyprowadza ruch do kalkulatora. Dziś `/kalkulator-wapnowania/` ma 5 odsłon w 90 dni,
a sesji ze źródłem „olx" zero w dwunastu miesiącach — bo nie ma czego mierzyć, nie dlatego
że ruchu nie ma.

Wymaga: `segno` (pip install --user segno), ImageMagick, kroju i logo w assets/brand/.

Użycie: karta_info.py <katalog wyjściowy> [karta ...]
"""
import os
import subprocess
import sys

import segno

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FONT_B = os.path.join(ROOT, "assets", "brand", "fonts", "PlusJakartaSans-ExtraBold.ttf")
FONT_M = os.path.join(ROOT, "assets", "brand", "fonts", "PlusJakartaSans-Medium.ttf")
LOGO = os.path.join(ROOT, "assets", "brand", "agria-logo-poziom-biale.png")

W, H = 1500, 1050
CIEMNA, AKCENT, JASNY = "#0A4030", "#94C14D", "#EAF0E7"
CEL = "https://agria.pl/kalkulator-wapnowania/"
KAMPANIA = "ogloszenia-2026-08"

# karty produktowe z build_adverts.py — utm_content, żeby widzieć, co przyprowadza ruch
KARTY = ["agrobielik-70", "agrobielik-90", "oxyfertil-90", "weglanowe-granulowane",
         "weglanowe-magnez-granulowane", "weglanowe-odmiana-04", "weglanowe-magnez-odmiana-04",
         "weglanowe-magnez-odmiana-05", "kreda-nawozowa-sypka", "kreda-nawozowa-granulowana",
         "kreda-pastewna"]

NAGLOWEK = ["Policzymy za darmo,", "ile wapna kupić"]
TRESC = [
    "Zeskanuj kod telefonem. Podajesz pH gleby,",
    "jej kategorię i areał — kalkulator wylicza",
    "dawkę na hektar i liczbę ton do zamówienia.",
]
DOPISEK = "Za darmo, bez rejestracji — wynik od ręki."
OFERTA = ["Pełna oferta AGRII:",
          "wapno tlenkowe · węglanowe · granulowane · kreda nawozowa i pastewna"]


def adres(karta):
    return (f"{CEL}?utm_source=olx&utm_medium=qr&utm_campaign={KAMPANIA}"
            f"&utm_content={karta}")


def zbuduj(karta, dst):
    qr_png = dst + ".qr.png"
    # wysoka korekcja błędów — kod bywa skanowany z ekranu pod kątem i z odbiciem
    segno.make(adres(karta), error="h").save(qr_png, scale=20, border=2,
                                             dark=CIEMNA, light="white")
    pas_y = H - 168
    subprocess.run([
        "magick", "-size", f"{W}x{H}", f"xc:{CIEMNA}", "-gravity", "NorthWest",
        # nadtytuł
        "-font", FONT_M, "-pointsize", "30", "-fill", AKCENT,
        "-annotate", "+90+128", "KALKULATOR WAPNOWANIA",
        # nagłówek w dwóch wierszach — jednowierszowy wchodził pod płytkę z kodem
        "-font", FONT_B, "-pointsize", "70", "-fill", "white",
        "-annotate", "+90+240", NAGLOWEK[0],
        "-annotate", "+90+322", NAGLOWEK[1],
        "-font", FONT_M, "-pointsize", "32", "-interline-spacing", "12", "-fill", JASNY,
        "-annotate", "+90+430", "\n".join(TRESC),
        "-font", FONT_B, "-pointsize", "30", "-fill", AKCENT,
        "-annotate", "+90+640", DOPISEK,
        # biała płytka pod kodem — kontrast dla skanera
        "-fill", "white", "-draw", f"roundrectangle {W-540},178 {W-90},628 18,18",
        "(", qr_png, "-resize", "410x410", ")", "-geometry", f"+{W-520}+198", "-composite",
        # pas dolny: zakres oferty po lewej, logo po prawej — rozdzielone, żeby nie nachodziły
        "-fill", AKCENT, "-draw", f"rectangle 0,{pas_y - 4} {W},{pas_y}",
        "-font", FONT_M, "-pointsize", "27", "-fill", AKCENT,
        "-annotate", f"+90+{pas_y + 60}", OFERTA[0],
        "-fill", JASNY,
        "-annotate", f"+90+{pas_y + 106}", OFERTA[1],
        LOGO, "-gravity", "NorthWest",
        "-geometry", f"190x53+{W - 190 - 90}+{pas_y + 58}", "-composite",
        "-quality", "92", dst], check=True)
    os.remove(qr_png)
    return subprocess.run(["magick", "identify", "-format", "%wx%h %b", dst],
                          capture_output=True, text=True).stdout


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for karta in (sys.argv[2:] or KARTY):
        dst = os.path.join(out, f"agria-info-{karta}.jpg")
        print(f"  agria-info-{karta}.jpg  {zbuduj(karta, dst)}")
        print(f"      → {adres(karta)}")
    print(f"→ {out}")
