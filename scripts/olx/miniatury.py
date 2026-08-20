#!/usr/bin/env python3
"""Generuje pierwsze zdjęcia (miniatury) do ogłoszeń OLX — po dwa warianty na siatkę.

Po co to istnieje
-----------------
Miniatura na liście wyników OLX to slot `image;s=516x361` — POZIOMY, proporcja 1,43:1,
a CDN nie kadruje, tylko wpisuje zdjęcie w prostokąt. Nasze pionowe plansze 435×700 zajmowały
w nim 43 % szerokości niezależnie od rozdzielczości. Stąd stały format 1500×1050.

Co pokazujemy: dwa najczęstsze archetypy kategorii (zmierzone na 214 pierwszych zdjęciach
konkurencji 20.08) — pryzma towaru z odniesieniem skali (~38 %) i transport/rozładunek (~8 %,
ale najsilniejszy komunikat: „dowieziemy") — połączone z KONTEKSTEM ZASTOSOWANIA, którego
w kategorii nie ma nikt. Siatka 200 ogłoszeń jest zbudowana wokół 12 intencji; miniatura
domyka to, co w tytułach i opisach już stoi.

Granica materiału generowanego
------------------------------
Kadr pokazuje, DO CZEGO towar służy — nie udaje konkretnej dostawy AGRII. Dlatego prompt
wyklucza ludzi, czytelne znaki firmowe, tablice rejestracyjne i jakikolwiek tekst na obrazie.
Napis nakładamy sami, z tabeli w tym pliku, krojem marki — dzięki temu nie ma zmyślonej
liczby ani podrobionej etykiety, a dwanaście par wygląda jak jedna seria.
Zero kodów QR, adresów WWW i numerów telefonu — regulamin OLX traktuje zdjęcia jako treść
ogłoszenia, a dane kontaktowe mają być w polach formularza.

Wymaga: klucza Gemini w ~/secrets/google/gemini-api-key.txt, ImageMagicka, kroju i logo
w assets/brand/. Pillow NIE jest potrzebny.

Użycie:
    miniatury.py <katalog wyjściowy> [siatka ...]     # bez nazw = wszystkie 24
"""
import base64
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FONT_B = os.path.join(ROOT, "assets", "brand", "fonts", "PlusJakartaSans-ExtraBold.ttf")
FONT_M = os.path.join(ROOT, "assets", "brand", "fonts", "PlusJakartaSans-Medium.ttf")
LOGO = os.path.join(ROOT, "assets", "brand", "agria-logo-poziom-biale.png")
KLUCZ = os.path.expanduser("~/secrets/google/gemini-api-key.txt")

MODEL = "gemini-3-pro-image"
W, H = 1500, 1050          # dokładnie kształt slotu miniatury OLX
MARGINES = 46              # wspólny margines: od lewej, od dołu, od prawej
WYS = 96                   # wysokość paska z korzyścią — ta sama co logo
SCRIM = 0.42               # jaka część kadru od góry jest przyciemniona pod napis
SZER_HASLA = 1180          # docelowa szerokość hasła; stopień pisma dobiera się sam
CIEMNA = "#0A4030"         # zieleń marki, ta sama co stopka katalogu
AKCENT = "#94C14D"         # jasna zieleń z podpisów plansz
JASNY = "#EAF0E7"

# Szablon kadru — wzorzec Janka z 20.08. Próbka towaru leży na kontrolowanym zielonym
# gradiencie, nie na ziemi obok łopaty czy palety. To jest różnica, która rozwiązuje problem
# uziarnienia: przy obiekcie wielkości metra w kadrze generator MUSI narysować ziarno widoczne,
# więc z 3–8 mm robił bryły wielkości pięści. Na gradiencie nie ma z czym porównywać, więc
# proszek zostaje proszkiem, a granulat granulatem.
SZABLON = (
    "Create a photo that is to be a presentation product. The clear background of the photo "
    "should be {tlo}. At the bottom left there should be a dark green blend background and "
    "on this gradient there should be {material}. "
    "No text, no logos, no people, no tools, no machinery in the foreground."
)

# tło · materiał · hasło (do czego) · korzyść (co z tego masz)
# Materiał opisany UZIARNIENIEM Z KARTY PRODUKTOWEJ, nie porównaniem do grochu czy orzecha —
# tak powstały kadry, w których „3–8 mm" wyglądało jak tłuczeń.
# Hasło i korzyść wyprowadzone z pól `intencja` i `lead` w planie oraz z „Efektu zastosowania".
SIATKI = {
"agrobielik-70-staw": (
    "Wapno nawozowe tlenkowe Agrobielik 70 · 0–2 mm",
    "a carp fish pond with reeds along the bank and calm water, early spring",
    "a small pile of white powder with small lumps",
    "Wapno do stawu", "Odkaża dno stawu"),
"agrobielik-70-gleba": (
    "Wapno nawozowe tlenkowe Agrobielik 70 · 0–2 mm",
    "a field of dark heavy clay soil freshly ploughed, autumn, wide horizon",
    "a small pile of white powder with small lumps",
    "Wapno na gleby ciężkie", "Efekt w 2–4 tygodnie"),
"agrobielik-90": (
    "Wapno nawozowe tlenkowe Agrobielik 90 · 0–3 mm",
    "a field divided vertically in half, one half ripe cereal grain, the other half "
    "flowering rapeseed",
    "a small pile of white powder with fine lumps",
    "Wapno pod zboża i rzepak", "Mniejsza dawka na hektar"),
"oxyfertil-90": (
    "Wapno nawozowe tlenkowe Oxyfertil 90 · 3–8 mm",
    "a field divided vertically in half, one half is grain, half is rapeseed",
    "a small pile of white crushed limestone chips",
    "Wapno na mniejsze pole", "Już od 1 tony"),
"weglanowe-granulowane": (
    "Wapno nawozowe węglanowe Granulowane · 3–6 mm",
    "a field of flowering rapeseed in full bloom under a cloudy sky",
    "a small pile of small round cream-coloured granules",
    "Wapno do rozsiewacza", "Bez pylenia"),
"weglanowe-magnez-granulowane": (
    "Wapno węglanowe z magnezem Granulowane · 3–6 mm",
    "a light sandy field in early spring with a young green crop emerging in rows",
    "a small pile of small round beige granules",
    "Wapno na gleby lekkie", "Odkwasza i daje magnez"),
"weglanowe-odmiana-04": (
    "Wapno nawozowe węglanowe Odmiana 04 · 0–2 mm",
    "a field after harvest, wheat stubble on the left and freshly ploughed dark soil on the right",
    "a small pile of off-white loose limestone powder with small lumps",
    "Wapno na duże areały", "Najniższy koszt hektara"),
"weglanowe-magnez-odmiana-04": (
    "Wapno węglanowe z magnezem Odmiana 04",
    "a very wide field after harvest stretching to the horizon, cloudy autumn sky",
    "a small pile of greyish-beige loose limestone powder",
    "Wapno i magnez w jednym", "Odkwasza i daje magnez"),
"weglanowe-magnez-odmiana-05": (
    "Wapno węglanowe z magnezem Odmiana 05",
    "a field just after spring ploughing with clear furrows of moist soil",
    "a small pile of greyish-beige loose limestone powder",
    "Wapno na niedobór magnezu", "Magnez w najniższej cenie tony"),
"kreda-nawozowa-sypka": (
    "Kreda nawozowa Sypka",
    "a wide field of ripe cereal grain under a slightly cloudy sky",
    "a small pile of soft cream-coloured loose chalk",
    "Kreda do wapnowania pola", "Bez ryzyka poparzenia"),
"kreda-nawozowa-granulowana": (
    "Kreda nawozowa Granulowana · 3–6 mm",
    "a small family farm field with farm buildings in the distance, spring",
    "a small pile of small round snow-white granules",
    "Kreda do rozsiewacza", "Big-bag już od 1 tony"),
"kreda-pastewna": (
    "Kreda Pastewna",
    "the inside of a bright dairy cattle barn with a feeding table and dairy cows out of focus",
    "a small pile of very fine snow-white chalk powder",
    "Kreda pastewna do paszy", "Bezpieczne źródło wapnia"),
}


def prompt_dla(siatka):
    _, tlo, material, _, _ = SIATKI[siatka]
    return SZABLON.format(tlo=tlo, material=material)


def generuj(prompt, out_png):
    klucz = open(KLUCZ).read().strip()
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"],
                                 "imageConfig": {"aspectRatio": "4:3", "imageSize": "2K"}}}
    r = subprocess.run(["curl", "-sS", "--max-time", "240",
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


def _etykieta(tekst, font, rozmiar, kolor, plik):
    """Renderuje napis i PRZYCINA go do samego tuszu, więc znamy jego realne wymiary."""
    subprocess.run(["magick", "-background", "none", "-fill", kolor, "-font", font,
                    "-pointsize", str(rozmiar), f"label:{tekst}", "-trim", "+repage", plik],
                   check=True)
    w, h = subprocess.run(["magick", "identify", "-format", "%w %h", plik],
                          capture_output=True, text=True, check=True).stdout.split()
    return int(w), int(h)


def _dopasuj(tekst, font, kolor, plik, cel, wg_szerokosci, start=100, lo=34, hi=136):
    """Dobiera stopień pisma tak, żeby napis miał zadaną szerokość albo wysokość tuszu.

    Bez tego długość hasła decydowałaby o wielkości liter — „Wapno do stawu" byłoby dwa razy
    większe niż „Wapno na niedobór magnezu" i dwanaście kadrów nie trzymałoby się jako seria.
    """
    r = start
    for _ in range(8):
        w, h = _etykieta(tekst, font, r, kolor, plik)
        masz = w if wg_szerokosci else h
        if abs(masz - cel) <= max(3, cel // 100) or r >= hi or r <= lo:
            break
        r = max(lo, min(hi, round(r * cel / masz)))
    return _etykieta(tekst, font, r, kolor, plik)


def podpisz(src, dst, siatka):
    """Kadruje do 1500×1050 i nakłada trzy warstwy komunikatu.

    Układ zatwierdzony przez Janka 20.08, po trzech podejściach:
      • u GÓRY, na miękkim przyciemnieniu — nazwa produktu z frakcją, pod nią wielkim krojem
        ZASTOSOWANIE. Pas na dole odpadł, bo zasłaniał próbkę towaru leżącą w lewym dolnym rogu.
      • w LEWYM DOLNYM rogu, na próbce — prosty pasek w jaskrawej zieleni marki z czarnymi
        wersalikami: KORZYŚĆ.
      • w PRAWYM DOLNYM rogu logo. Pasek i logo mają tę samą wysokość i wspólną linię dołu.

    Przyciemnienie u góry nie jest ozdobą: bez niego napis ginie na jasnym łanie zbóż
    i na piaszczystej glebie — sprawdzone na obu.
    """
    produkt, _, _, haslo, korzysc = SIATKI[siatka]
    t = dst + ".t"
    l1, l2, sc, lg, pk, pt_ = (t + x for x in ("1.png", "2.png", "s.png", "l.png", "k.png", "kt.png"))

    w1, h1 = _etykieta(produkt, FONT_B, 44, "#CFE0C6", l1)
    w2, h2 = _dopasuj(haslo, FONT_B, "white", l2, SZER_HASLA, True)

    hs = round(H * SCRIM)
    subprocess.run(["magick", "-size", f"{W}x{hs}", "gradient:black-none", "-alpha", "set",
                    "-channel", "A", "-evaluate", "multiply", "0.62", "+channel", sc], check=True)
    subprocess.run(["magick", LOGO, "-resize", f"x{WYS}",
                    "(", "+clone", "-background", "black", "-shadow", "75x14+0+4", ")",
                    "+swap", "-background", "none", "-layers", "merge", "+repage", lg], check=True)
    lw, lh = (int(v) for v in subprocess.run(["magick", "identify", "-format", "%w %h", lg],
                                             capture_output=True, text=True, check=True).stdout.split())
    tw, th = _dopasuj(korzysc.upper(), FONT_B, "black", pt_, round(WYS * 0.40), False, 52, 34, 72)
    bw = tw + 60
    subprocess.run(["magick", "-size", f"{bw}x{WYS}", f"xc:{AKCENT}",
                    pt_, "-gravity", "center", "-composite", pk], check=True)

    y1 = MARGINES + 8
    y2 = y1 + h1 + 22
    subprocess.run([
        "magick", src, "-resize", f"{W}x^", "-gravity", "center", "-extent", f"{W}x{H}",
        "-gravity", "NorthWest",
        sc, "-geometry", "+0+0", "-composite",
        l1, "-geometry", f"+{(W - w1) // 2}+{y1}", "-composite",
        l2, "-geometry", f"+{(W - w2) // 2}+{y2}", "-composite",
        pk, "-geometry", f"+{MARGINES}+{H - MARGINES - WYS}", "-composite",
        lg, "-geometry", f"+{W - MARGINES - lw}+{H - MARGINES - lh}", "-composite",
        "-quality", "90", dst], check=True)
    for f in (l1, l2, sc, lg, pk, pt_):
        if os.path.exists(f):
            os.remove(f)
    return subprocess.run(["magick", "identify", "-format", "%wx%h %b", dst],
                          capture_output=True, text=True).stdout


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    wybor = sys.argv[2:] or list(SIATKI)
    os.makedirs(out, exist_ok=True)
    surowe = os.path.join(out, ".surowe")
    os.makedirs(surowe, exist_ok=True)
    for siatka in wybor:
        if siatka not in SIATKI:
            print(f"  nieznana siatka: {siatka}"); continue
        png = os.path.join(surowe, f"{siatka}.png")
        jpg = os.path.join(out, f"agria-mini-{siatka}.jpg")
        if not os.path.exists(png):
            blad = generuj(prompt_dla(siatka), png)
            if blad:
                print(f"  BŁĄD {siatka}: {blad}"); continue
        print(f"  agria-mini-{siatka}.jpg  {podpisz(png, jpg, siatka)}")
    print(f"→ {out}")
