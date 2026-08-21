#!/usr/bin/env python3
"""Miniatury OLX v3 — pierwsze zdjęcie ogłoszenia, czytelne w kadrze telefonu.

Po co v3 (pomiar 21.08.2026 na realnym OLX, emulacja iPhone)
------------------------------------------------------------
Miniatura na liście wyników na telefonie to kadr **150 × 183 px, proporcja 0,82**,
przy `object-fit: cover`. Z pliku 1500 × 1050 widać więc **środkowe 861 px szerokości** —
wersja z 20.08 miała hasło rozciągnięte na 1180 px, pasek korzyści przy lewej krawędzi
i logo przy prawej, czyli wszystkie trzy elementy poza kadrem. Na liście czytało się
„apno na gleby ciężk", „2–4 TYGODNIE" i „Ag".

Zasady tego układu:
  • **Treść mieści się w kwadracie ze środka** (1050 px) z zapasem — blok liczymy na 820 px.
    Kwadrat to prosta reguła robocza Janka: cokolwiek OLX zrobi z kadrem, środek zostaje.
  • **Hasło mówi TYLKO, do czego** — bez słowa „Wapno”, bo tytuł ogłoszenia stoi tuż obok
    miniatury i zaczyna się właśnie od nazwy produktu. Powtarzanie jej marnuje kadr.
  • Nagłówek produktu u góry, hasło pod nim, pasek z korzyścią pod hasłem, wszystko
    wyśrodkowane; małe logo na dole pośrodku. Nic nie dotyka krawędzi.
  • Tła jasne i nasycone: błękitne niebo, złote zboża, lazurowa woda, soczysta zieleń.
    Wersja z 20.08 była brązowo-szara i na liście ginęła między cudzymi ogłoszeniami.

Wymaga: klucza Gemini w ~/secrets/google/gemini-api-key.txt, ImageMagicka, kroju i logo
w assets/brand/.

Użycie:
    miniatury_v3.py <katalog wyjściowy> [siatka ...]     # bez nazw = wszystkie 12
"""
import base64
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FONT_B = os.path.join(ROOT, "assets", "brand", "fonts", "PlusJakartaSans-ExtraBold.ttf")
LOGO = os.path.join(ROOT, "assets", "brand", "agria-logo-poziom-biale.png")
KLUCZ = os.path.expanduser("~/secrets/google/gemini-api-key.txt")

MODEL = "gemini-3-pro-image"
W, H = 1500, 1050
BLOK = 820                 # szerokość każdego elementu — mieści się i w kwadracie, i w kadrze telefonu
LOGO_H = 56
AKCENT = "#D3FF23"         # jaskrawa limonka, wybór Janka 21.08

WSPOLNE = ("Bright sunny day, vivid saturated colours, deep blue sky with white clouds, "
           "warm golden light, high contrast, sharp, professional agricultural photography. "
           "No text, no logos, no people, no tools, no machinery in the foreground.")

# siatka: (tło · nagłówek produktu · hasło „do czego” („|” łamie linię) · korzyść)
# Każda siatka ma DWA warianty do rotacji: A i B. Hasło zostaje to samo — zastosowanie się
# nie zmienia — różni się tło i korzyść, obie wzięte z `lead` w planie ogłoszeń, nie wymyślone.
# Wariant B zapisuje się jako `agria-mini-<siatka>-b.jpg`.
SIATKI = {
"agrobielik-70-staw": (
    "A clear azure fishing pond with turquoise water reflecting the blue sky, green reeds "
    "along the bank, fresh spring greenery around. " + WSPOLNE,
    "Agrobielik 70 · tlenkowe · 0–2 mm", "Do stawu", "Odkaża dno"),
"agrobielik-70-gleba": (
    "A freshly ploughed field with rich brown furrows in bright sunshine, green grass margin "
    "in front, deep blue sky with white clouds. " + WSPOLNE,
    "Agrobielik 70 · tlenkowe · 0–2 mm", "Na gleby|średnie i ciężkie", "Szybkie odkwaszanie"),
"agrobielik-90": (
    "A field of ripe golden wheat under a deep blue summer sky, ears glowing in the sun, "
    "a strip of bright yellow flowering rapeseed on the horizon. " + WSPOLNE,
    "Agrobielik 90 · tlenkowe · 0–3 mm", "Pod zboża|i rzepak", "Szybkie odkwaszanie"),
"oxyfertil-90": (
    "A small sunny farm field with ripe cereal on one side and green crop on the other, "
    "farm buildings with red roofs in the distance, blue sky. " + WSPOLNE,
    "Oxyfertil 90 · tlenkowe · 3–8 mm", "Na mniejsze|pole", "Bardzo szybkie działanie"),
"weglanowe-granulowane": (
    "A field of rapeseed in full yellow bloom under a bright blue sky, vivid yellow flowers "
    "to the horizon. " + WSPOLNE,
    "Węglanowe granulowane · 3–6 mm", "Do rozsiewacza", "Stabilne i bezpieczne"),
"weglanowe-magnez-granulowane": (
    "A bright green field of young cereal shoots in neat rows in spring, fresh vivid green, "
    "blue sky with white clouds. " + WSPOLNE,
    "Węglanowe z magnezem · 3–6 mm", "Na gleby|lekkie", "Stabilne i bezpieczne"),
"weglanowe-odmiana-04": (
    "A very wide golden stubble field stretching to the horizon after harvest, sunny day, "
    "deep blue sky with white clouds. " + WSPOLNE,
    "Węglanowe · odmiana 04 · 0–2 mm", "Na duże|areały", "Najniższy koszt hektara"),
"weglanowe-magnez-odmiana-04": (
    "A wide green field of vigorous cereal crop in early summer under a blue sky, rolling "
    "farmland to the horizon. " + WSPOLNE,
    "Węglanowo-magnezowe · odmiana 04", "Z magnezem", "Dwa składniki naraz"),
"weglanowe-magnez-odmiana-05": (
    "A sunny field of maize with strong green leaves under a deep blue sky with white clouds. "
    + WSPOLNE,
    "Węglanowo-magnezowe · odmiana 05", "Na niedobór|magnezu", "Magnez w cenie tony"),
"kreda-nawozowa-sypka": (
    "A wide field of ripe golden cereal grain under a bright blue sky with white clouds, "
    "sunlit ears. " + WSPOLNE,
    "Kreda nawozowa sypka", "Na pole|pod zboża", "Lepsze plony"),
"kreda-nawozowa-granulowana": (
    "A tidy small family farm field in spring, fresh green crop, white farm buildings in the "
    "distance, blue sky with white clouds. " + WSPOLNE,
    "Kreda nawozowa granulowana · 3–6 mm", "Do rozsiewacza", "Lepsze plony"),
"kreda-pastewna": (
    "Interior of a bright modern dairy barn: black and white Holstein cows standing in a row "
    "at a concrete feed table, eating a fresh mixed ration of silage. Indoor scene, barn roof "
    "structure visible above, green fields and blue sky far away through the open side wall. "
    "NOT a pasture, no grazing. " + WSPOLNE,
    "Kreda pastewna · węglan wapnia", "Dla bydła|i drobiu", "Bezpieczny wapń"),
}


WARIANT_B = {
"agrobielik-70-staw": (
    "A calm azure fish pond in spring seen from a low grassy bank, wooden footbridge over "
    "turquoise water, green reeds, blue sky reflected in the surface. " + WSPOLNE,
    "Podnosi pH wody"),
"agrobielik-70-gleba": (
    "Close view of freshly ploughed heavy soil furrows glistening in the sun, green field "
    "margin and deep blue sky with clouds behind. " + WSPOLNE,
    "Wzrost plonów"),
"agrobielik-90": (
    "A dense field of ripe barley with heavy golden ears bending in the sun, deep blue sky. "
    + WSPOLNE,
    "Wzrost plonów"),
"oxyfertil-90": (
    "Two white big bags of fertiliser standing at the edge of a sunny green field, farm "
    "buildings far in the background, blue sky with white clouds. " + WSPOLNE,
    "Wysoka reaktywność"),
"weglanowe-granulowane": (
    "A field of young winter cereal in even green rows stretching to the horizon in spring "
    "sunshine, blue sky. " + WSPOLNE,
    "Własnym rozsiewaczem"),
"weglanowe-magnez-granulowane": (
    "A light sandy field with a young green crop and visible pale sandy soil between rows, "
    "sunny day, blue sky. " + WSPOLNE,
    "Na braki magnezu"),
"weglanowe-odmiana-04": (
    "A huge ploughed field in autumn sunshine with long straight furrows running to the "
    "horizon, dramatic blue sky with white clouds. " + WSPOLNE,
    "Do planowego wapnowania"),
"weglanowe-magnez-odmiana-04": (
    "A wide sunny field of tall green maize under a deep blue sky with white clouds. "
    + WSPOLNE,
    "Bez ryzyka poparzenia"),
"weglanowe-magnez-odmiana-05": (
    "A vast green field of winter wheat in spring under a bright blue sky, gentle hills on "
    "the horizon. " + WSPOLNE,
    "Do dużych powierzchni"),
"kreda-nawozowa-sypka": (
    "Close view of ripe golden wheat ears in bright sunlight with a blue sky behind. "
    + WSPOLNE,
    "Bezpieczne odkwaszanie"),
"kreda-nawozowa-granulowana": (
    "A small tidy farm field bordered by fruit trees in blossom, white farmhouse in the "
    "background, sunny spring day, blue sky. " + WSPOLNE,
    "Bezpieczne odkwaszanie"),
"kreda-pastewna": (
    "White laying hens inside a bright clean poultry house with fresh feed in a long feeder, "
    "daylight coming through the windows, green fields visible outside. " + WSPOLNE,
    "Kilka frakcji do wyboru"),
}


def wariant(siatka, b=False):
    """Zwraca (tło, nagłówek, hasło, korzyść) dla wariantu A albo B."""
    tlo, produkt, haslo, korzysc = SIATKI[siatka]
    if b:
        tlo, korzysc = WARIANT_B[siatka]
    return tlo, produkt, haslo, korzysc


def generuj(prompt, out_png):
    klucz = open(KLUCZ).read().strip()
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"],
                                 "imageConfig": {"aspectRatio": "4:3", "imageSize": "2K"}}}
    r = subprocess.run(["curl", "-sS", "--max-time", "300",
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={klucz}",
        "-H", "Content-Type: application/json", "-d", json.dumps(body)],
        capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        return f"odpowiedź nie-JSON: {r.stdout[:200]}"
    if "candidates" not in d:
        return f"API: {json.dumps(d, ensure_ascii=False)[:300]}"
    for p in d["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            open(out_png, "wb").write(base64.b64decode(p["inlineData"]["data"]))
            return None
    return "odpowiedź bez obrazu"


def _etykieta(tekst, rozmiar, kolor, plik):
    subprocess.run(["magick", "-background", "none", "-fill", kolor, "-font", FONT_B,
                    "-pointsize", str(rozmiar), f"label:{tekst}", "-trim", "+repage", plik],
                   check=True)
    w, h = subprocess.run(["magick", "identify", "-format", "%w %h", plik],
                          capture_output=True, text=True, check=True).stdout.split()
    return int(w), int(h)


def _dopasuj(tekst, kolor, plik, cel, wg_szerokosci=True, start=110, lo=28, hi=170):
    """Dobiera stopień pisma do zadanej szerokości (albo wysokości) tuszu.

    Dzięki temu o wielkości liter decyduje kadr, nie długość hasła — inaczej „Do stawu”
    byłoby dwa razy większe niż „Na gleby średnie i ciężkie” i dwanaście kadrów nie
    trzymałoby się jako jedna seria.
    """
    r = start
    for _ in range(9):
        w, h = _etykieta(tekst, r, kolor, plik)
        masz = w if wg_szerokosci else h
        if abs(masz - cel) <= max(3, cel // 100) or r >= hi or r <= lo:
            break
        r = max(lo, min(hi, round(r * cel / masz)))
    return _etykieta(tekst, r, kolor, plik)


def podpisz(tlo_png, dst, siatka, b=False):
    _, produkt, haslo, korzysc = wariant(siatka, b)
    t = dst + ".t"
    sc, pk, pt_, lg, pp = (t + x for x in ("s.png", "k.png", "kt.png", "l.png", "p.png"))
    linie = haslo.split("|")
    pliki = []
    for i, l in enumerate(linie):
        p = t + f"h{i}.png"
        pliki.append((p, *_dopasuj(l, "white", p, BLOK if len(linie) == 1 else round(BLOK * 0.94))))
    wp, hp = _dopasuj(produkt, "#E8F2DF", pp, round(BLOK * 0.82), start=44, lo=24, hi=50)
    tw, th = _dopasuj(korzysc.upper(), "black", pt_, 38, False, 50, 28, 66)
    bw, bh = tw + 56, 88
    subprocess.run(["magick", "-size", f"{bw}x{bh}", f"xc:{AKCENT}", pt_, "-gravity", "center",
                    "-composite", pk], check=True)
    subprocess.run(["magick", LOGO, "-resize", f"x{LOGO_H}",
                    "(", "+clone", "-background", "black", "-shadow", "70x12+0+3", ")",
                    "+swap", "-background", "none", "-layers", "merge", "+repage", lg], check=True)
    lw, lh = (int(v) for v in subprocess.run(["magick", "identify", "-format", "%w %h", lg],
              capture_output=True, text=True, check=True).stdout.split())

    blok = hp + 20 + sum(h + 14 for _, _, h in pliki) + 18 + bh
    y0 = (H - blok) // 2
    # przyciemnienie wygaszane w obie strony — bez niego napis ginie na jasnym łanie
    hs = blok + 260
    subprocess.run(["magick", "-size", f"{W}x{hs // 2}", "gradient:none-black",
                    "(", "-size", f"{W}x{hs // 2}", "gradient:black-none", ")", "-append",
                    "-alpha", "set", "-channel", "A", "-evaluate", "multiply", "0.5", "+channel",
                    sc], check=True)
    cmd = ["magick", tlo_png, "-resize", f"{W}x{H}^", "-gravity", "center", "-extent", f"{W}x{H}",
           "-modulate", "104,118,100",
           "-gravity", "NorthWest",
           sc, "-geometry", f"+0+{max(0, y0 - (hs - blok) // 2)}", "-composite",
           pp, "-geometry", f"+{(W - wp) // 2}+{y0}", "-composite"]
    y = y0 + hp + 20
    for p, w, h in pliki:
        cmd += [p, "-geometry", f"+{(W - w) // 2}+{y}", "-composite"]
        y += h + 14
    y += 18
    cmd += [pk, "-geometry", f"+{(W - bw) // 2}+{y}", "-composite",
            lg, "-geometry", f"+{(W - lw) // 2}+{H - 46 - lh}", "-composite",
            "-quality", "92", dst]
    subprocess.run(cmd, check=True)
    for f in [sc, pk, pt_, lg, pp] + [p for p, _, _ in pliki]:
        if os.path.exists(f):
            os.remove(f)
    return subprocess.run(["magick", "identify", "-format", "%wx%h %b", dst],
                          capture_output=True, text=True).stdout


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    wybor = [s for s in (sys.argv[2:] or list(SIATKI))]
    tla = os.path.join(out, ".tla")
    os.makedirs(tla, exist_ok=True)

    zadania = [(s, b) for s in wybor if s in SIATKI for b in (False, True)]
    brak = [(s, b) for s, b in zadania if not os.path.exists(f"{tla}/{s}{'-b' if b else ''}.png")]
    if brak:
        print(f"generuję {len(brak)} teł…")
        with ThreadPoolExecutor(max_workers=6) as ex:
            for (s, b), blad in zip(brak, ex.map(
                    lambda sb: generuj(wariant(*sb)[0], f"{tla}/{sb[0]}{'-b' if sb[1] else ''}.png"),
                    brak)):
                print(f"  {'BŁĄD ' + blad if blad else 'OK'}  {s}{'-b' if b else ''}")
    for s, b in zadania:
        suf = "-b" if b else ""
        png = f"{tla}/{s}{suf}.png"
        if not os.path.exists(png):
            print(f"  pomijam {s}{suf} — brak tła"); continue
        print(f"  agria-mini-{s}{suf}.jpg  {podpisz(png, f'{out}/agria-mini-{s}{suf}.jpg', s, b)}")
    print(f"→ {out}")
