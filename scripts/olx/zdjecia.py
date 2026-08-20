#!/usr/bin/env python3
"""Przygotowuje zdjęcia produktowe pod ogłoszenia OLX — jedna plansza na jeden produkt.

Kontekst: plansze porównawcze Auranetu powstały pod INNĄ koncepcję — jedno zbiorcze ogłoszenie
prezentujące całą ofertę, po dwa produkty na kadr, rozdzielone pionowo, z kodem QR do kalkulatora
na styku. Przy rozbiciu oferty na osobne ogłoszenia ta formuła się nie broni: w ogłoszeniu
Agrobielika 70 klient widziałby kadr, na którym jest też Agrobielik 90.

Rozwiązanie ma dwa kroki. Najpierw **zamalowujemy plakietkę z kodem** — każdą jej połowę próbką
tekstury z tej samej strony i tego samego pasa wysokości, bo plansza ma po obu stronach inny
materiał i inne oświetlenie. Potem **tniemy planszę dokładnie po środku**, więc każda połowa ma
własny podpis produktu i element brandingu (logo po lewej, hasło po prawej).

Kolejność jest istotna: samo cięcie z marginesem też usuwa kod, ale margines musi być na tyle
szeroki, że obcina podpisy produktów po prawej stronie. Stąd najpierw łatka, potem cięcie na styk.

Ryzyko regulaminowe, które to załatwia: regulamin OLX mówi, że „Treść Ogłoszenia stanowią również
dodane w ramach niego zdjęcia", więc kod prowadzący na zewnętrzną stronę jest tam odnośnikiem.

Użycie: zdjecia.py <katalog wyjściowy>
"""
import os
import subprocess
import sys

# CDN trzyma oryginały w 1500x1205 — przy s=1000x700 dostawaliśmy 871x700, czyli połówki
# 435x700. Żądanie większego kadru daje połówki 750x1205, trzy razy więcej pikseli.
CDN = "https://ireland.apollo.olxcdn.com/v1/files/{}-PL/image;s=2000x1400"

PLANSZE = {
    "tlenkowe_drobne": "ehrko21q6pcg",   # Agrobielik 70 0–2 mm | Agrobielik 90 0–3 mm
    "tlenkowe_grube": "c7x3u8i4d8672",   # Agrobielik 90 2–8 mm | Oxyfertil 90 3–8 mm
    "weglanowe_sypkie": "mfbvu7uouj6o",  # sypkie z magnezem | sypkie bez magnezu
    "weglanowe_granul": "eq6zi11x7gdq",  # granulowane z magnezem | granulowane bez magnezu
    "kreda": "6mrdec42b9il",             # kreda sypka | kreda granulowana
}

# nazwa wyniku → (plansza, która połowa)
POLOWKI = {
    "agrobielik-70": ("tlenkowe_drobne", "L"),
    "agrobielik-90-0-3": ("tlenkowe_drobne", "P"),
    "agrobielik-90-2-8": ("tlenkowe_grube", "L"),
    "oxyfertil-90": ("tlenkowe_grube", "P"),
    "weglanowe-z-magnezem": ("weglanowe_sypkie", "L"),
    "weglanowe-bez-magnezu": ("weglanowe_sypkie", "P"),
    "granulowane-z-magnezem": ("weglanowe_granul", "L"),
    "granulowane-bez-magnezu": ("weglanowe_granul", "P"),
    "kreda-sypka": ("kreda", "L"),
    "kreda-granulowana": ("kreda", "P"),
}


def pobierz(fid, cel):
    subprocess.run(["curl", "-sS", CDN.format(fid), "-o", cel], check=True)


def wymiary(f):
    o = subprocess.run(["magick", "identify", "-format", "%w %h", f],
                       capture_output=True, text=True, check=True).stdout
    return tuple(int(x) for x in o.split())


# Plakietka z kodem, jako ułamki wymiaru kadru. Wszystkie plansze są z jednego szablonu.
PLAKIETKA = (0.385, 0.300, 0.637, 0.679)


def zamaluj_kod(src, dst):
    """Zakrywa plakietkę z kodem QR teksturą z tej samej planszy — lustrzanym odbiciem sąsiedztwa.

    Pierwsze podejście kopiowało próbkę z pasa oddalonego o ćwierć szerokości kadru i wklejało ją
    na styk. Przy połówkach 435x700 nie było tego widać, przy 750x1205 łatka rzucała się w oczy:
    twarda pionowa krawędź plus tekstura będąca dokładnym powtórzeniem tej obok. Samo rozmycie
    krawędzi nie wystarczyło — plansza ma poziomy gradient oświetlenia, więc próbka z odległego
    miejsca wnosiła skok jasności widoczny nawet przez piórko.

    Rozwiązanie: łatkę robimy z pasa PRZYLEGŁEGO do plakietki i odbijamy go w poziomie. Odbicie
    względem krawędzi plakietki sprawia, że tekstura przechodzi przez tę krawędź bez szwu, a że
    próbka jest tuż obok — jasność zgadza się sama. Lewą połowę odbijamy względem lewej krawędzi,
    prawą względem prawej; obie łatki spotykają się dokładnie na środku kadru, czyli w linii,
    w której i tak tniemy planszę na dwa ogłoszenia.
    """
    w, h = wymiary(src)
    fx0, fy0, fx1, fy1 = PLAKIETKA
    x0, y0, x1, y1 = round(fx0 * w), round(fy0 * h), round(fx1 * w), round(fy1 * h)
    srodek, bh = w // 2, y1 - y0
    lw, pw = srodek - x0, x1 - srodek

    # Samo odbicie daje ciągłość, ale zostawia widoczną symetrię wokół osi. Dlatego każdą łatkę
    # składamy z DWÓCH odbitych pasów pobranych z różnej wysokości i mieszamy je gradientem:
    # przy osi odbicia liczy się pas przylegający (ciągłość), dalej przechodzimy w drugi
    # (symetria się rozmywa). Gradient jest poziomy, czarny przy osi, biały przy końcu łatki.
    dy = round(h * 0.14)
    tmp, maska = dst + ".tmp.png", dst + ".mask.png"
    lat_l, lat_p = dst + ".l.png", dst + ".p.png"

    def lataj(szer, zx, os_przy_lewej, cel):
        """Składa jedną łatkę: dwa odbite pasy zmieszane gradientem od osi odbicia."""
        y_alt = max(0, min(h - bh, y0 - dy))
        kierunek = ["-rotate", "270"] if os_przy_lewej else ["-rotate", "90"]
        subprocess.run(["magick",
            "(", src, "-crop", f"{szer}x{bh}+{zx}+{y0}", "+repage", "-flop", ")",
            "(", src, "-crop", f"{szer}x{bh}+{zx}+{y_alt}", "+repage", "-flop", ")",
            "(", "-size", f"{bh}x{szer}", "gradient:black-white", *kierunek, ")",
            "-composite", cel], check=True)

    lataj(lw, x0 - lw, True, lat_l)     # oś przy lewej krawędzi łatki (x0)
    lataj(pw, x1, False, lat_p)         # oś przy prawej krawędzi łatki (x1)
    subprocess.run([
        "magick", src,
        lat_l, "-geometry", f"+{x0}+{y0}", "-composite",
        lat_p, "-geometry", f"+{srodek}+{y0}", "-composite", tmp], check=True)
    # piórko wygładza tylko górną i dolną krawędź łatki; boczne są ciągłe z definicji
    piorko = max(10, round(h * 0.012))
    subprocess.run([
        "magick", "-size", f"{w}x{h}", "xc:black", "-fill", "white",
        "-draw", f"rectangle {x0},{y0 + piorko} {x1},{y1 - piorko}",
        "-blur", f"0x{piorko}", maska], check=True)
    subprocess.run(["magick", src, tmp, maska, "-composite", "-quality", "94", dst], check=True)
    for f in (tmp, maska, lat_l, lat_p):
        os.remove(f)


def polowa(src, strona, dst):
    """Tnie wyczyszczoną planszę dokładnie po środku — bez marginesu, żeby nie ciąć podpisów."""
    w, h = wymiary(src)
    szer = w // 2
    x = 0 if strona == "L" else szer
    subprocess.run(["magick", src, "-crop", f"{szer}x{h}+{x}+0", "+repage",
                    "-quality", "92", dst], check=True)
    return szer, h


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    src_dir = os.path.join(out, ".plansze")
    os.makedirs(src_dir, exist_ok=True)
    for nazwa, fid in PLANSZE.items():
        surowa = os.path.join(src_dir, nazwa + "-surowa.jpg")
        pobierz(fid, surowa)
        zamaluj_kod(surowa, os.path.join(src_dir, nazwa + ".jpg"))
    for nazwa, (plansza, strona) in POLOWKI.items():
        dst = os.path.join(out, f"agria-{nazwa}.jpg")
        w, h = polowa(os.path.join(src_dir, plansza + ".jpg"), strona, dst)
        print(f"  agria-{nazwa}.jpg  ({w}x{h})  ← {plansza} {'lewa' if strona=='L' else 'prawa'}")
    print(f"→ {out}")
