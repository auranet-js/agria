#!/usr/bin/env python3
"""Buduje gotowe ładunki POST /partner/adverts z planu + parametrów z kart produktowych.

Wejście:  data/olx/plan-ogloszen.json, data/olx/product-specs.json
Wyjście:  data/olx/adverts-payload.json

Reguły treści wymuszone tu kodem, nie dobrą wolą:
- ŻADNEGO numeru telefonu w opisie (regulamin OLX pkt 4: dane kontaktowe wyłącznie
  w polach formularza). Stare ogłoszenia AGRII kończyły się `6*6*4*3*9*3*0*6*2`.
- Jedno ogłoszenie = jeden produkt. Bez list „w ofercie także…", bez „nawozów sztucznych"
  (te są poza zakresem produktowym AGRII — docs/MASTER_PROMPT.md).
- Parametry wyłącznie z kart produktowych agria.pl, zero wymyślania.
- Cena zawsze z jednostką i z informacją netto/loco — to jest właśnie ta różnica
  wobec wabików bez jednostki, którymi kategoria jest zapchana.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")
PLAN = os.path.join(D, "plan-ogloszen.json")
SPECS = os.path.join(D, "product-specs.json")
OUT = os.path.join(D, "adverts-payload.json")

CDN = "https://ireland.apollo.olxcdn.com/v1/files/{}-PL/image;s=1000x700"

# Kit grafik brandowych Auranetu, już na CDN OLX (8 zdjęć z ogłoszenia 930166743).
# Kolejność zgodna z tym, co widać na każdej: to są plansze porównawcze frakcji.
FOTO = {
    "hero":            "bszde7mjrgep2",  # „WAPNA NAWOZOWE" — ciągnik na polu
    "tlenkowe_drobne": "ehrko21q6pcg",   # Agrobielik 70 0–2 mm | Agrobielik 90 0–3 mm
    "tlenkowe_grube":  "c7x3u8i4d8672",  # Agrobielik 90 2–8 mm | Oxyfertil 90 3–8 mm
    "weglanowe_sypkie": "mfbvu7uouj6o",  # węglanowe sypkie z magnezem | bez magnezu
    "weglanowe_granul": "eq6zi11x7gdq",  # węglanowe granulowane z magnezem | bez magnezu
    "kreda":           "6mrdec42b9il",   # kreda sypka | kreda granulowana
    "worki":           "df737gqzimu12",  # palety z workami wapna tlenkowego
    "bigbagi":         "03yl2d0fc5313",  # big-bagi Agrobielik w magazynie
}

# Zdjęcie wiodące dobrane do produktu — pierwsze zdjęcie decyduje o kliknięciu z listy.
GALERIE = {
    "agrobielik-70":              ["tlenkowe_drobne", "bigbagi", "worki", "hero"],
    "agrobielik-90":              ["tlenkowe_drobne", "tlenkowe_grube", "bigbagi", "hero"],
    "oxyfertil-90":               ["tlenkowe_grube", "bigbagi", "hero"],
    "weglanowe-granulowane":      ["weglanowe_granul", "bigbagi", "hero"],
    "weglanowe-magnez-granulowane": ["weglanowe_granul", "bigbagi", "hero"],
    "kreda-nawozowa-sypka":       ["kreda", "hero", "bigbagi"],
    "kreda-nawozowa-granulowana": ["kreda", "bigbagi", "hero"],
    "weglanowe-odmiana-04":       ["weglanowe_sypkie", "hero", "bigbagi"],
    "kreda-pastewna":             ["kreda", "worki", "hero"],
    "weglanowe-magnez-odmiana-04": ["weglanowe_sypkie", "hero", "bigbagi"],
    "weglanowe-magnez-odmiana-05": ["weglanowe_sypkie", "hero", "bigbagi"],
    "mieszanka-tlenkowo-weglanowa": ["tlenkowe_drobne", "weglanowe_sypkie", "hero"],
}

# Które parametry z karty produktowej wchodzą do opisu i w jakiej kolejności.
PARAMETRY = ["Zawartość CaO", "Zawartość CaO+MgO", "Zawartość MgO", "Reaktywność",
             "Typ reakcji", "Forma fizyczna", "Frakcja", "Norma", "Producent"]
STOSOWANIE = ["Zastosowanie funkcjonalne", "Dawkowanie", "Szybkość działania",
              "Efekt zastosowania", "Dodatkowe zastosowanie"]

STOPKA = (
    "DOKUMENTY\n"
    "Atest OSChR do każdej partii. Karty produktowe i świadectwa jakości dostępne "
    "do pobrania oraz dostarczane przy dostawie.\n\n"
    "AGRIA Sp. z o.o. — surowce wapniowe od 1989 r. Magazyny: Niedomice i Radgoszcz.\n"
    "Stabilne parametry. Pewne dostawy."
)

TELEFON = re.compile(r"(?:\d[\s\-\*\.]{0,2}){9,}")


def sekcja(naglowek, spec, klucze):
    linie = [f"• {k}: {spec[k]}" for k in klucze if spec.get(k)]
    return f"{naglowek}\n" + "\n".join(linie) if linie else ""


def opis(row, spec):
    czesci = [row["lead"]]

    p = sekcja("PARAMETRY", spec, PARAMETRY)
    if p:
        czesci.append(p)

    s = sekcja("ZASTOSOWANIE", spec, STOSOWANIE)
    if s:
        czesci.append(s)

    czesci.append(
        "FORMY DOSTAWY I CENA\n"
        f"• {row['cena_opis']}\n"
        "• Ceny netto, loco magazyn — bez transportu. Transport wyceniamy indywidualnie "
        "w zależności od miejsca dostawy.\n"
        "• Możliwy odbiór własny.\n"
        "Ceny orientacyjne, nie stanowią oferty handlowej w rozumieniu Kodeksu cywilnego."
    )
    # Pole „Magazyn" z karty produktowej wypisuje zakłady DOSTAWCÓW (Sitkówka, Bukowa, Celiny,
    # Góraźdżce…). W ogłoszeniu wystawionym w Płocku to tylko myli czytelnika, a przy okazji
    # eksponuje strukturę zaopatrzenia. Magazyny AGRII są w stopce.
    if spec.get("Dostępność"):
        czesci.append(f"DOSTĘPNOŚĆ\n• {spec['Dostępność']}")
    czesci.append(STOPKA)
    return "\n\n".join(c for c in czesci if c)


if __name__ == "__main__":
    plan = json.load(open(PLAN, encoding="utf-8"))
    specs = {r["url"].rstrip("/").split("/")[-1]: r for r in json.load(open(SPECS, encoding="utf-8"))}

    out, bledy = [], []
    for row in plan:
        spec = specs.get(row["karta"], {}).get("spec", {})
        if not spec:
            bledy.append(f"brak parametrów dla {row['karta']}")
        tresc = opis(row, spec)

        m = TELEFON.search(tresc)
        if m:
            bledy.append(f"NUMER TELEFONU w opisie {row['karta']}: {m.group(0)!r}")

        klucze = GALERIE.get(row["karta"])
        if not klucze:
            bledy.append(f"brak galerii dla {row['karta']}")
            klucze = ["hero"]
        zdjecia = [{"url": CDN.format(FOTO[k])} for k in klucze]
        # domknięcie galerii zdjęciem produktowym z karty na agria.pl (8 to limit OLX)
        for u in specs.get(row["karta"], {}).get("images", [])[:2]:
            if len(zdjecia) < 8:
                zdjecia.append({"url": u})

        out.append({
            "title": row["title"][:70],
            "description": tresc,
            "category_id": row["category_id"],
            "advertiser_type": "business",
            # Klucz musi zawierać wariant, nie sam SKU: Agrobielik 70 idzie jako dwa różne
            # ogłoszenia (do stawu / na odkwaszanie) i w 17 miastach oba wypadają w siatce.
            "external_id": f"agria-{row['siatka']}-{row['city_id']}",
            # Telefon MUSI tu być: pominięty w pilocie dał ogłoszenie bez numeru, czyli bez
            # kanału, który odpowiada za wszystkie 209 kontaktów na tym koncie. To jest
            # jednocześnie właściwe miejsce na dane kontaktowe wg regulaminu — pole formularza,
            # nie treść opisu.
            "contact": {"name": "AGRIA Sp. z o.o.", "phone": "664 393 062"},
            "location": {"city_id": row["city_id"]},
            "images": zdjecia,
            "price": {"value": row["price"], "currency": "PLN", "negotiable": True},
            "attributes": [{"code": "state", "value": "new"}],
            "_meta": {"karta": row["karta"], "sku": row["sku"], "siatka": row["siatka"],
                      "city": row["city"],
                      "intencja": row["intencja"]},
        })

    if bledy:
        print("PROBLEMY:")
        for b in sorted(set(bledy)):
            print("  -", b)
        if any("TELEFON" in b for b in bledy):
            sys.exit("STOP: numer telefonu w opisie łamie regulamin OLX")

    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    dl = [len(o["description"]) for o in out]
    print(f"ogłoszeń: {len(out)}  |  opis: {min(dl)}–{max(dl)} znaków  |  zdjęć: "
          f"{min(len(o['images']) for o in out)}–{max(len(o['images']) for o in out)}")
    print(f"→ {os.path.relpath(OUT)}")
