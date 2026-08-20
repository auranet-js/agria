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
PAS = 196                  # wysokość pasa z podpisem
CIEMNA = "#0A4030"         # zieleń marki, ta sama co stopka katalogu
AKCENT = "#94C14D"         # jasna zieleń z podpisów plansz
JASNY = "#EAF0E7"

WSPOLNE = (
    "Fotografia dokumentalna, poziomy kadr, obiektyw 35 mm, naturalne światło dzienne, "
    "lekkie zachmurzenie, realistyczne proporcje i kolory, widoczny kurz i zabrudzenia sprzętu, "
    "polski krajobraz rolniczy. Bez HDR, bez wyglądu zdjęcia stockowego. "
    "BEZ ludzi i twarzy, BEZ czytelnych znaków firmowych i logotypów, BEZ tablic rejestracyjnych, "
    "BEZ jakiegokolwiek tekstu, napisów, znaków wodnych i ramek. "
    "Nie dodawaj podpisu do obrazu."
)

# siatka → (linia nadrzędna, nazwa produktu, dopisek frakcji, opis materiału,
#           kontekst wariantu A „pryzma", kontekst wariantu B „transport lub zastosowanie")
SIATKI = {
"agrobielik-70-gleba": (
    "Wapno nawozowe tlenkowe", "Agrobielik 70", "0–2 mm",
    "biały, bardzo drobny sypki materiał wapienny o konsystencji mąki, lekko zbrylony",
    "duża pryzma usypana na ściernisku po zbiorach zbóż, wbita w nią zwykła szpadel-łopata "
    "jako odniesienie skali, w drugim planie ciemna, ciężka gleba świeżo zaorana i pas drzew",
    "trzyosiowa wywrotka z podniesioną skrzynią zsypuje ładunek na skraju zaoranego pola, "
    "biały strumień materiału, ciężka gleba, jesienne popołudnie"),
"agrobielik-70-staw": (
    "Wapno nawozowe tlenkowe", "Agrobielik 70", "0–2 mm",
    "biały, bardzo drobny sypki materiał wapienny o konsystencji mąki",
    "pryzma usypana na grobli stawu hodowlanego, obok wiadro i łopata jako skala, "
    "w tle spokojna tafla wody, trzciny i groble stawów karpiowych",
    "brzeg dużego stawu hodowlanego wczesną wiosną, biały pas materiału rozsypany wzdłuż grobli, "
    "trzciny, spokojna woda, mostek i mnich spustowy w oddali"),
"agrobielik-90": (
    "Wapno nawozowe tlenkowe", "Agrobielik 90", "0–3 mm",
    "biały materiał wapienny, drobne nieregularne grudki wielkości ziarna grochu",
    "pryzma na skraju dużego pola, obok wbita łopata jako skala, szerokie otwarte pole, "
    "jesienne pochmurne światło",
    "ciągnik z rozsiewaczem tarczowym rozsiewa biały materiał na dużym polu, widoczny wachlarz "
    "wysiewu i smuga kurzu, ujęcie z boku z poziomu ziemi"),
"oxyfertil-90": (
    "Wapno nawozowe tlenkowe", "Oxyfertil 90", "3–8 mm",
    "białe kruszywo wapienne o ostrych krawędziach, wielkości od ziarna grochu do orzecha",
    "niewielka pryzma kruszywa na betonowym placu gospodarstwa, obok drewniana paleta "
    "jako odniesienie skali, w tle blaszana wiata",
    "biały big-bag stojący na przyczepie rolniczej na podwórzu gospodarstwa, "
    "ciągnik częściowo w kadrze, big-bag bez żadnych napisów ani nadruków"),
"weglanowe-granulowane": (
    "Wapno nawozowe węglanowe", "Granulowane", "",
    "kremowobiały granulat nawozowy — regularne kuleczki o średnicy 2–5 mm, pojedyncze ziarna "
    "wyraźnie widoczne, jak granulat nawozu wysypany z worka; NIE piasek, NIE ziemia, NIE zboże",
    "kopczyk granulatu na betonowym placu pod wiatą, sfotografowany z bliska pod kątem, "
    "obok drewniana paleta jako skala, widoczna struktura pojedynczych kulek",
    "rozsiewacz zawieszany za ciągnikiem, wypełniony kremowym granulatem, "
    "pracuje na zielonym oziminie, ujęcie zza maszyny"),
"weglanowe-magnez-granulowane": (
    "Wapno węglanowe z magnezem", "Granulowane", "",
    "jasnobeżowy granulat nawozowy — regularne kuleczki o średnicy 2–5 mm, pojedyncze ziarna "
    "wyraźnie widoczne; NIE ziemniaki, NIE fasola, NIE kamienie, NIE bryły ziemi",
    "kopczyk jasnobeżowego granulatu wysypany na skraju lekkiej piaszczystej gleby, ujęcie "
    "z bliska pod kątem, obok wbita łopata jako skala, młody zasiew nieostro w tle",
    "zbliżenie na lej rozsiewacza wypełniony jasnobeżowym granulatem o kuleczkach 2–5 mm, "
    "w tle lekka piaszczysta gleba z młodym zasiewem, ciągnik częściowo w kadrze"),
"weglanowe-odmiana-04": (
    "Wapno nawozowe węglanowe", "Odmiana 04", "",
    "szarobiały, wilgotny sypki materiał wapienny z drobnymi bryłkami",
    "bardzo duża pryzma usypana na skraju rozległego pola, dla skali obok stoi "
    "drewniana paleta, szeroki kadr pokazujący wielkość hałdy",
    "naczepa samowyładowcza wysypuje materiał na dużym ściernisku, biała smuga na ziemi, "
    "rozległe pole ciągnące się po horyzont"),
"weglanowe-magnez-odmiana-04": (
    "Wapno węglanowe z magnezem", "Odmiana 04", "",
    "szarobeżowy wilgotny sypki materiał wapienny",
    "pryzma na dużym ściernisku, obok wbita łopata jako skala, jesienne pochmurne niebo, "
    "rozległe pole",
    "ciężarówka z przyczepą stoi na polnej drodze przy dużym polu, przy niej rozładowany "
    "materiał w pryzmie, jesienny krajobraz"),
"weglanowe-magnez-odmiana-05": (
    "Wapno węglanowe z magnezem", "Odmiana 05", "",
    "szarobeżowy sypki materiał wapienny z widocznymi drobnymi bryłkami",
    "pryzma na polu tuż po orce, wyraźne skiby ziemi, obok łopata jako skala",
    "świeżo zaorane pole z wyraźnymi skibami, na pierwszym planie rozsypany szarobeżowy "
    "materiał wapienny, w tle ciągnik z pługiem"),
"kreda-nawozowa-sypka": (
    "Kreda nawozowa", "Sypka", "",
    "jasnobeżowa, miękka sypka kreda o drobnej strukturze",
    "bardzo duża pryzma kredy na skraju rozległego pola, dla skali drewniana paleta obok, "
    "szeroki kadr",
    "naczepa samowyładowcza z podniesioną skrzynią wysypuje jasnobeżową kredę "
    "na dużym areale, widoczny strumień materiału i chmura pyłu"),
"kreda-nawozowa-granulowana": (
    "Kreda nawozowa", "Granulowana", "",
    "śnieżnobiały granulat kredowy — regularne kuleczki o średnicy 2–5 mm, pojedyncze ziarna "
    "wyraźnie widoczne; NIE proszek, NIE ciemny materiał, NIE obornik",
    "niewielki kopczyk śnieżnobiałego granulatu na betonowym placu gospodarstwa, "
    "obok metalowe wiadro jako skala, w tle stodoła",
    "rozsiewacz zawieszany za małym ciągnikiem wysypuje ŚNIEŻNOBIAŁY granulat na niewielkim "
    "polu, widoczna biała smuga materiału na ziemi, zabudowania gospodarstwa w tle"),
"kreda-pastewna": (
    "Kreda", "Pastewna", "",
    "bardzo drobny, śnieżnobiały proszek kredowy o konsystencji mąki",
    "biały drobny proszek nasypany na stole paszowym obok paszy objętościowej, "
    "obok metalowa miarka jako skala, wnętrze obory",
    "wnętrze jasnej obory dla bydła mlecznego, stół paszowy z paszą, "
    "na pierwszym planie biały proszek kredowy wymieszany z paszą, krowy nieostro w tle"),
}

WARIANTY = ("pryzma", "kontekst")


def prompt_dla(siatka, wariant):
    _, _, _, materiał, ka, kb = SIATKI[siatka]
    scena = ka if wariant == "pryzma" else kb
    return (f"{scena}. Materiał: {materiał}. {WSPOLNE}")


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


def podpisz(src, dst, siatka):
    """Kadruje do 1500×1050 i kładzie pas z nazwą produktu oraz logo."""
    nad, nazwa, frakcja, *_ = SIATKI[siatka]
    y_pasa = H - PAS
    cmd = [
        "magick", src,
        "-resize", f"{W}x^", "-gravity", "center", "-extent", f"{W}x{H}",
        # od tego miejsca współrzędne liczymy od lewego górnego rogu, nie od środka
        "-gravity", "NorthWest",
        # pas
        "-fill", CIEMNA, "-draw", f"rectangle 0,{y_pasa} {W},{H}",
        # cienka linia akcentu nad pasem
        "-fill", AKCENT, "-draw", f"rectangle 0,{y_pasa - 6} {W},{y_pasa}",
        # linia nadrzędna
        "-font", FONT_M, "-pointsize", "34", "-fill", JASNY,
        "-annotate", f"+56+{y_pasa + 62}", nad,
        # nazwa produktu
        "-font", FONT_B, "-pointsize", "64", "-fill", AKCENT,
        "-annotate", f"+56+{y_pasa + 132}", nazwa,
    ]
    if frakcja:
        szer = subprocess.run(["magick", "-font", FONT_B, "-pointsize", "64",
                               f"label:{nazwa}", "-format", "%w", "info:"],
                              capture_output=True, text=True).stdout
        x = 56 + int(szer) + 22
        cmd += ["-font", FONT_M, "-pointsize", "40", "-fill", JASNY,
                "-annotate", f"+{x}+{y_pasa + 130}", frakcja]
    cmd += [LOGO, "-gravity", "NorthWest",
            "-geometry", f"260x73+{W - 260 - 56}+{y_pasa + 62}", "-composite",
            "-quality", "90", dst]
    subprocess.run(cmd, check=True)
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
        for w in WARIANTY:
            png = os.path.join(surowe, f"{siatka}-{w}.png")
            jpg = os.path.join(out, f"agria-mini-{siatka}-{w}.jpg")
            if not os.path.exists(png):
                blad = generuj(prompt_dla(siatka, w), png)
                if blad:
                    print(f"  BŁĄD {siatka}-{w}: {blad}"); continue
            print(f"  agria-mini-{siatka}-{w}.jpg  {podpisz(png, jpg, siatka)}")
    print(f"→ {out}")
