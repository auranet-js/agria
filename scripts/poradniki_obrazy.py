#!/usr/bin/env python3
"""Ilustracje do poradników (Gemini `gemini-2.5-flash-image`, ~$0,04/szt., PNG 16:9).

23.09.2026 — pierwsza partia: poradnik 2837 „Wapno pod ziemniaki” (zdjęcie wyróżniające + ujęcie
do sekcji o przedplonie) i terminarz 2743 „Kiedy wapnować pole?”. Po 3 warianty, wybór Janka.
Zasada: ilustracja zjawiska rolniczego, nigdy „zdjęcie AGRII” (magazyn, towar, auta firmy) —
te muszą być prawdziwe. Rozsiewacz tylko jako wariant: AGRIA nie świadczy rozsiewu (decyzja 11.09 przy OLX).

    poradniki_obrazy.py <katalog-wyjściowy> [nazwa ...]     bez nazw = wszystkie
Wołać sekwencyjnie — LVE (limit procesów).
"""
import base64, json, os, subprocess, sys

KEY = open(os.path.expanduser("~/secrets/google/gemini-api-key.txt")).read().strip()
MODEL = "gemini-2.5-flash-image"
STYLE = (" Natural documentary photograph for an agricultural advice article, not an advertisement: "
         "realistic colours, soft natural daylight, no HDR, no dramatic lighting, no people in close-up. "
         "Rural southern Poland (Małopolska), gentle hills, small fields separated by tree lines. "
         "No text, no logos, no brand names, no watermarks, machines plain without lettering. "
         "Horizontal composition.")

SCENY = {
    # 2837 — zdjęcie wyróżniające
    "ziemniaki-a": "A potato field in late summer: long straight earthed-up ridges with green, slightly yellowing potato plants, seen at a low angle along the rows towards a tree line.",
    "ziemniaki-b": "Close-up of a single earthed-up potato ridge in brown loamy soil, lush potato plants with a few white-purple flowers, the next ridges blurred in the background.",
    "ziemniaki-c": "Freshly dug potatoes lying on the surface of a brown ridge in a potato field during harvest, soil still on the tubers, the rest of the field in soft focus.",
    # 2837 — sekcja „Kiedy wapnować pole pod ziemniaki” (pod przedplon, po żniwach)
    "przedplon-a": "A harvested cereal stubble field in late August with a thin, even white dusting of agricultural lime spread over the whole surface, the stubble visible through it, a field edge with trees.",
    "przedplon-b": "A heap of white powdery agricultural lime dumped at the edge of a harvested wheat stubble field, tyre tracks in the soil, rolling fields in the background.",
    "przedplon-c": "Close-up of cereal stubble and dry soil lightly covered with white powdery agricultural lime after spreading, shallow depth of field.",
    # 2743 — zdjęcie wyróżniające terminarza
    "terminarz-a": "A farm tractor with a rear-mounted twin-disc fertiliser spreader driving forward across a harvested stubble field, spreading white agricultural lime behind it in a wide, even fan.",
    "terminarz-b": "A tractor with a mouldboard plough ploughing a stubble field that is lightly covered with white agricultural lime, the freshly turned brown furrows next to the white stubble, early autumn.",
    "terminarz-c": "A wide view of a harvested stubble field in early September with a large heap of white agricultural lime at the field edge, waiting to be spread, clear sky, hills in the background.",
}


def generuj(nazwa, opis, out):
    body = {"contents": [{"parts": [{"text": opis + STYLE}]}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "16:9"}}}
    for _ in range(3):
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
    return None


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for n in (sys.argv[2:] or SCENY):
        print(n, generuj(n, SCENY[n], out), flush=True)
