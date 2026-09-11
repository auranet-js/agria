#!/usr/bin/env python3
"""Pierwsze zdjęcie ogłoszenia OLX w wersji v4: zdjęcie „z placu” + białe pole z rodzajem wapna.

Wzór zaakceptowany przez Janka 11.09.2026: białe pole u góry, marginesy 7% z boków i od góry,
wysokość 20% zdjęcia, napis Plus Jakarta Sans ExtraBold w kolorze #07571e, wyśrodkowany,
dopasowany do 92% szerokości i 62% wysokości pola. Zdjęcia źródłowe 4:5 (896×1152) — kadr
miniatury na liście mobilnej OLX (0,82) przycina je minimalnie, więc marginesy zostają.

Napis = rodzaj wapna, którego rolnik szuka; nazwa handlowa i przeznaczenie są w tytule.
Wariant A / B różni się zdjęciem (rotacja w obrębie produktu, jak przy miniaturach v3).
Granulowane i Oxyfertil mają na razie tylko A — B czeka na zdjęcia big bagów z placu.

Użycie: miniatury_v4.py   (wymaga ImageMagick `magick`)
"""
import os, subprocess

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONT = os.path.join(REPO, "assets/brand/fonts/PlusJakartaSans-ExtraBold.ttf")
V4 = os.path.expanduser("~/domains/auratest.pl/public_html/agria-olx/v4")
KOLOR = "#07571e"

# wariant: (napis, zdjęcie A, zdjęcie B albo None)
PLAN = {
    "agrobielik-70-staw":           ("WAPNO DO STAWU",    "wywrotka-zsyp", "halda-pole"),
    "agrobielik-70-gleba":          ("WAPNO NAWOZOWE",    "wywrotka-zsyp", "halda-pole"),
    "agrobielik-90":                ("WAPNO NAWOZOWE",    "wywrotka-zsyp", "halda-pole"),
    "oxyfertil-90":                 ("WAPNO NAWOZOWE",    "hds-bigbagi",   None),
    "weglanowe-granulowane":        ("WAPNO GRANULOWANE", "hds-bigbagi",   None),
    "weglanowe-magnez-granulowane": ("WAPNO MAGNEZOWE",   "hds-bigbagi",   None),
    "weglanowe-magnez-odmiana-04":  ("WAPNO MAGNEZOWE",   "wywrotka-zsyp", "halda-pole"),
    "weglanowe-magnez-odmiana-05":  ("WAPNO MAGNEZOWE",   "wywrotka-zsyp", "halda-pole"),
    "weglanowe-odmiana-04":         ("WAPNO WĘGLANOWE",   "wywrotka-zsyp", "halda-pole"),
    "kreda-nawozowa-sypka":         ("KREDA NAWOZOWA",    "wywrotka-zsyp", "halda-pole"),
    "kreda-nawozowa-granulowana":   ("KREDA GRANULOWANA", "hds-bigbagi",   None),
    "kreda-pastewna":               ("KREDA PASTEWNA",    "zaladunek",     "wywrotka-zsyp"),
}


def slug(napis):
    tr = str.maketrans("ĄĆĘŁŃÓŚŹŻ", "ACELNOSZZ")
    return napis.translate(tr).lower().replace(" ", "-")


def nazwa(napis, zdjecie):
    return f"agria-mini4-{slug(napis)}-{zdjecie}.jpg"


def render(napis, zdjecie):
    src = os.path.join(V4, f"agria-foto-{zdjecie}.jpg")
    out = os.path.join(V4, nazwa(napis, zdjecie))
    w, h = map(int, subprocess.check_output(
        ["magick", "identify", "-format", "%w %h", src], text=True).split())
    bx, by = w * 7 // 100, h * 7 // 100
    bw, bh = w - 2 * bx, h * 20 // 100
    tw, th = bw * 92 // 100, bh * 62 // 100
    subprocess.run([
        "magick", src,
        "(", "-size", f"{bw}x{bh}", "xc:white", ")",
        "-gravity", "northwest", "-geometry", f"+{bx}+{by}", "-composite",
        "(", "-background", "none", "-fill", KOLOR, "-font", FONT,
        "-size", f"{tw}x{th}", "-gravity", "center", f"label:{napis}", ")",
        "-gravity", "northwest", "-geometry", f"+{bx + (bw - tw) // 2}+{by + (bh - th) // 2}",
        "-composite", "-quality", "88", out], check=True)
    return out


if __name__ == "__main__":
    zrobione = set()
    for napis, a, b in PLAN.values():
        for z in (a, b):
            if z and (napis, z) not in zrobione:
                zrobione.add((napis, z))
                print(os.path.basename(render(napis, z)))
    print(f"plików: {len(zrobione)}")
