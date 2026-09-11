#!/usr/bin/env python3
"""Sceny „z placu” do ogłoszeń OLX — generowanie przez Gemini (`gemini-2.5-flash-image`, ~$0,04/szt.).

11.09.2026: pierwsza partia (6 scen), Janek wybrał 4 — leżą jako JPG w
`~/domains/auratest.pl/public_html/agria-olx/v4/agria-foto-<scena>.jpg`:
wywrotka-zsyp, halda-pole, zaladunek, hds-bigbagi. Odrzucone: auto-rozsiew, ciagnik-rozsiew
(AGRIA nie świadczy rozsiewu — zdjęcie sugerowałoby usługę).

NOWE = propozycje drugiej partii (T-138, fronty ≥10) — NIE wygenerowane, do akceptu Janka.

    sceny_gemini.py <katalog-wyjściowy> [nazwa ...]     bez nazw = wszystkie z NOWE
Wynik: PNG 896×1152 (4:5 — kadr miniatury OLX 0,82 przycina minimalnie). Napis nakłada
`miniatury_v4.py` (po dopisaniu sceny do jego PLAN). Wołać sekwencyjnie — LVE (limit procesów).
"""
import base64, json, os, subprocess, sys, time

KEY = open(os.path.expanduser("~/secrets/google/gemini-api-key.txt")).read().strip()
MODEL = "gemini-2.5-flash-image"
STYLE = (" Raw, candid smartphone photo taken by a farmer or driver, not a stock or advertising photo: "
         "natural daylight, slightly overcast Polish autumn sky, ordinary everyday look, a bit of mud, "
         "realistic colours, no HDR, no dramatic lighting. Rural southern Poland (Małopolska). "
         "No text, no logos, no brand names, no watermarks anywhere, trucks plain white or grey without "
         "lettering. Vertical composition.")

PIERWSZA_PARTIA = {
    "wywrotka-zsyp": "A tipper semi-trailer truck (steel tipping trailer raised) unloading white powdery agricultural lime onto the edge of a harvested stubble field next to a farm; a large white heap forming behind the trailer, fine white dust in the air.",
    "halda-pole": "A large heap of white powdery agricultural lime (about 24 tonnes) dumped at the edge of a stubble field after delivery, tyre tracks in the soil, a farm building and trees in the background, the empty tipper truck driving away on a field road.",
    "zaladunek": "A yellow wheel loader loading white agricultural lime from a big pile into a tipper semi-trailer in an industrial yard of a lime warehouse, white dust, concrete yard, steel hall in the background.",
    "hds-bigbagi": "A truck with a loader crane (HDS) unloading white big bags of agricultural lime onto a farmyard, several big bags already standing on the ground on pallets, farm buildings around.",
}

NOWE = {
    "wywrotka-podworze": "A tipper semi-trailer seen from the side, unloading white agricultural lime next to an old barn on a Polish farmyard, the heap growing on packed earth.",
    "halda-ladowacz": "A heap of white agricultural lime at the edge of a field with a farm tractor with a front loader parked next to it, bucket half full of lime.",
    "bigbagi-wiata": "A row of white big bags of agricultural lime standing on wooden pallets under a simple steel farm shed roof, gravel yard.",
    "hala-pryzma": "Inside a large steel warehouse: a big pile of loose white agricultural lime with a wheel loader beside it, daylight from the open gate.",
    "dlon-granulat": "Close-up of a hand in a work glove holding white lime granules 3-6 mm above an open big bag, shallow depth of field.",
    "naczepa-droga": "A tipper semi-trailer truck driving on a narrow rural road between autumn fields, seen from the roadside.",
    "halda-mgla": "A large heap of white agricultural lime on a freshly ploughed brown field on a misty autumn morning, a line of trees in the background.",
    "bigbagi-przyczepa": "White big bags of agricultural lime loaded on a farm trailer hitched to a tractor in a farmyard.",
}


def generuj(nazwa, opis, out):
    body = {"contents": [{"parts": [{"text": opis + STYLE}]}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "4:5"}}}
    for proba in range(3):
        r = subprocess.run(["curl", "-sS", "--max-time", "120", "-H", "Content-Type: application/json",
                            "-d", json.dumps(body),
                            f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}"],
                           capture_output=True, text=True)
        try:
            parts = json.loads(r.stdout)["candidates"][0]["content"]["parts"]
            im = next(p["inlineData"] for p in parts if "inlineData" in p)
            ext = "png" if "png" in im["mimeType"] else "jpg"
            plik = os.path.join(out, f"{nazwa}.{ext}")
            open(plik, "wb").write(base64.b64decode(im["data"]))
            return plik
        except Exception:
            print(f"  ponawiam {nazwa}: {r.stdout[:200]}", file=sys.stderr)
            time.sleep(3)
    return None


if __name__ == "__main__":
    out = sys.argv[1]
    nazwy = sys.argv[2:] or list(NOWE)
    wszystkie = {**PIERWSZA_PARTIA, **NOWE}
    for n in nazwy:
        print(n, generuj(n, wszystkie[n], out))
