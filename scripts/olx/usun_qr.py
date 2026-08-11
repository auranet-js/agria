#!/usr/bin/env python3
"""Usuwa plakietkę z kodem QR z plansz produktowych używanych w ogłoszeniach OLX.

Po co: regulamin OLX mówi wprost, że „Treść Ogłoszenia stanowią również dodane w ramach niego
zdjęcia oraz tytuł". Kod QR prowadzący na zewnętrzną stronę jest więc formalnie odnośnikiem
w treści ogłoszenia. Chodził tam rok bez interwencji, ale przy dwustu ogłoszeniach ryzyko
blokady całego konta przestaje być akceptowalne — a same plansze są zbyt dobre, żeby je wyrzucić.

Metoda: plakietka siedzi na styku dwóch tekstur (plansze są dzielone na pół, dwie frakcje obok
siebie), więc każdą połowę łatamy próbką z JEJ strony, pobraną z tego samego pasa wysokości —
inaczej widać jaśniejszy prostokąt albo przeciągniętą stopkę.

Użycie: usun_qr.py <katalog wyjściowy>
"""
import os
import subprocess
import sys

CDN = "https://ireland.apollo.olxcdn.com/v1/files/{}-PL/image;s=1000x700"

# Plansze z plakietką QR. Bez niej są: hero, worki i big-bagi.
Z_KODEM = {
    "tlenkowe_drobne": "ehrko21q6pcg",
    "tlenkowe_grube": "c7x3u8i4d8672",
    "weglanowe_sypkie": "mfbvu7uouj6o",
    "weglanowe_granul": "eq6zi11x7gdq",
    "kreda": "6mrdec42b9il",
}


def pobierz(fid, cel):
    subprocess.run(["curl", "-sS", CDN.format(fid), "-o", cel], check=True)


def wymiary(f):
    o = subprocess.run(["magick", "identify", "-format", "%w %h", f],
                       capture_output=True, text=True, check=True).stdout
    return tuple(int(x) for x in o.split())


def pixel(f, x, y):
    o = subprocess.run(["magick", f, "-format", f"%[pixel:p{{{x},{y}}}]", "info:"],
                       capture_output=True, text=True, check=True).stdout
    v = o[o.find("(") + 1:o.find(")")].split(",")
    return tuple(int(t) for t in v[:3])


# Plakietka siedzi w tym samym miejscu na każdej planszy, bo wszystkie są z jednego szablonu.
# Automatyczne wykrywanie ciemnego prostokąta zawiodło — łapało pojedyncze moduły kodu zamiast
# całego kafla, więc zostaje geometria stała, podana jako ułamki wymiaru kadru.
PLAKIETKA = (0.385, 0.300, 0.637, 0.679)  # x0, y0, x1, y1


def bbox_plakietki(f, w, h):
    x0, y0, x1, y1 = PLAKIETKA
    return round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)


def zamaluj(src, dst):
    w, h = wymiary(src)
    box = bbox_plakietki(src, w, h)
    if not box:
        print(f"  {os.path.basename(src)}: nie znalazłem plakietki — kopiuję bez zmian")
        subprocess.run(["cp", src, dst], check=True)
        return False
    x0, y0, x1, y1 = box
    srodek = w // 2
    bw, bh = x1 - x0, y1 - y0
    lewa = max(0, min(x0, srodek) - bw - 40)
    prawa = min(w - bw - 1, max(x1, srodek) + 40)
    lw = max(1, srodek - x0)
    pw = max(1, x1 - srodek)
    subprocess.run([
        "magick", src,
        "(", "+clone", "-crop", f"{lw}x{bh}+{lewa}+{y0}", "+repage", ")",
        "-geometry", f"+{x0}+{y0}", "-composite",
        "(", "+clone", "-crop", f"{pw}x{bh}+{prawa}+{y0}", "+repage", "-flop", ")",
        "-geometry", f"+{srodek}+{y0}", "-composite",
        "-quality", "92", dst], check=True)
    print(f"  {os.path.basename(dst)}: plakietka {bw}x{bh} px w ({x0},{y0}) — zamalowana")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    tmp = os.path.join(out, ".src")
    os.makedirs(tmp, exist_ok=True)
    for nazwa, fid in Z_KODEM.items():
        src = os.path.join(tmp, nazwa + ".jpg")
        pobierz(fid, src)
        zamaluj(src, os.path.join(out, f"agria-{nazwa}.jpg"))
    print(f"→ {out}")
