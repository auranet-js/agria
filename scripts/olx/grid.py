#!/usr/bin/env python3
"""Dobór miejscowości pod ogłoszenia OLX — z ekonomiki transportu i popytu, nie z wyczucia.

Dwa wejścia, oba twarde:

1. POPYT — wolumen wyszukiwań per województwo (DataForSEO, Google Ads, PL, pull 2026-08-07),
   `data/olx/popyt-woj.json`. Uwaga metodologiczna: lokalizacji ogłoszeń konkurencji NIE da się
   użyć jako sygnału popytu — 88 ze 124 ogłoszeń stawowych na OLX to jeden sprzedawca powielający
   ofertę po całej Polsce, więc jego rozkład mierzy jego strategię, nie rynek.

2. TRANSPORT — sprzedajemy na tony loco magazyn, więc o zasięgu decyduje stosunek kosztu
   przewozu do ceny produktu. Zakłady wysyłkowe są RÓŻNE dla różnych produktów (z kart
   produktowych agria.pl): kreda granulowana jedzie z Kornicy pod Siedlcami, węglanowe odm. 04
   z Góraźdżec i Tarnowa Opolskiego, kreda sypka z Pierzchnicy — nie wszystko z Niedomic.

Wniosek, który z tego wychodzi: wapno węglanowe po 36–57 zł/t nie ma sensu wozić dalej niż
~150 km, bo transport przebija cenę towaru. Agrobielik 90 po 750 zł/t można wozić przez
całą Polskę. Dlatego siatka miast jest inna dla każdego produktu.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")

# Stawka przewozu dla zestawu 24 t. ZAŁOŻENIE do potwierdzenia u Pawła — on kwotuje transport
# indywidualnie, więc zna realną stawkę. 6 zł/km przy 24 t daje 0,25 zł za tonę na kilometr.
ZL_ZA_KM = 6.0
TONY = 24.0
ZL_T_KM = ZL_ZA_KM / TONY

# Zakłady wysyłkowe (kod pocztowy → współrzędne). Źródło nazw: pole „Magazyn" na kartach produktowych.
ZAKLADY = {
    "Niedomice": (50.150, 20.900), "Sitkówka": (50.820, 20.550),
    "Bukowa": (50.750, 19.950), "Celiny": (50.720, 20.600),
    "Góraźdżce": (50.550, 18.100), "Tarnów Opolski": (50.580, 18.030),
    "Draby": (51.100, 18.850), "Kornica": (52.170, 22.850),
    "Pierzchnica": (50.700, 20.700), "Chęciny": (50.800, 20.470),
    "Kostomłoty Drugie": (50.900, 20.500), "Łagów": (50.780, 21.060),
    "Tarnobrzeg": (50.570, 21.680), "Częstochowa": (50.810, 19.120),
}

REGION_NAZWA = {3: "Dolnośląskie", 15: "Kujawsko-pom", 8: "Lubelskie", 9: "Lubuskie",
                7: "Łódzkie", 4: "Małopolskie", 2: "Mazowieckie", 12: "Opolskie",
                17: "Podkarpackie", 18: "Podlaskie", 5: "Pomorskie", 6: "Śląskie",
                13: "Świętokrzyskie", 14: "Warm-mazurskie", 1: "Wielkopolskie",
                11: "Zachodniopom"}

# Frazy, po których liczymy popyt danego produktu — każdy produkt ma inny koszyk.
KOSZYKI = {
    "tlenkowe": ["wapno tlenkowe", "wapno palone", "wapno nawozowe"],
    "stawy": ["wapno do stawu", "wapno tlenkowe", "wapno palone"],
    "granulowane": ["wapno granulowane", "wapno nawozowe"],
    "granulowane_mg": ["wapno granulowane", "wapno magnezowe"],
    "kreda": ["kreda nawozowa", "wapno nawozowe"],
    "weglanowe": ["wapno węglanowe", "wapno nawozowe", "odkwaszanie gleby"],
    "pastewna": ["kreda pastewna"],
}


def km(a, b):
    """Odległość po ortodromie, wystarczająco dokładna dla decyzji o zasięgu dostawy."""
    lat1, lon1, lat2, lon2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(h))


def transport_udzial(dystans_km, cena_t):
    """Jaką część ceny towaru zjada przewóz na dany dystans."""
    return (dystans_km * ZL_T_KM) / cena_t


def zasieg(cena_t, prog=0.5):
    """Do ilu kilometrów transport mieści się w progu (domyślnie: połowa ceny towaru)."""
    return (cena_t * prog) / ZL_T_KM


def popyt_regionu(popyt, region, frazy):
    d = popyt.get(region, {})
    return sum(d.get(f, 0) for f in frazy)


def ocena(miasto, zaklady, cena_t, frazy, popyt, rynek, wlasne=None):
    """Wynik = popyt w województwie × zasięg miejscowości × ile z ceny zostaje po przewozie.

    „Zasięg miejscowości" mierzymy liczbą ogłoszeń wapniarskich, jakie rynek tam wystawia.
    To proxy z ograniczeniem — konkurenci mogli wybrać źle — ale lepsze niż intuicja i lepsze
    niż sama liczba mieszkańców, bo obejmuje też małe miasta w rejonach rolniczych.
    Bez tego czynnika model wybiera wsie najbliżej zakładu, gdzie w wyszukiwaniu lokalnym
    nie ma kogo dosięgnąć.
    """
    zaklad, dyst = min(
        ((z, km((float(miasto["latitude"]), float(miasto["longitude"])), ZAKLADY[z]))
         for z in zaklady), key=lambda x: x[1])
    udzial = transport_udzial(dyst, cena_t)
    if udzial > 0.5:
        return None
    region = REGION_NAZWA.get(miasto["region_id"])
    p = popyt_regionu(popyt, region, frazy)
    klucz = f"{miasto['name']}|{region}"
    ogl = rynek.get(klucz, 0)

    # Dane własne biją proxy z rynku. Kohorta z lipca 2025 to szesnaście ogłoszeń o tej samej
    # treści, tym samym wieku i tej samej historii pakietów, różniących się WYŁĄCZNIE miastem —
    # czyli jedyny czysty eksperyment, jaki mamy. Zator zebrał 213 wyświetleń przy medianie 102
    # i wypadał z siatki, bo mało kto się tam wystawia. Rynek nie wie tego, co my wiemy.
    w = (wlasne or {}).get(klucz)
    if ogl < 2 and not w:
        return None
    zasieg_miasta = math.log(1 + max(ogl, 2))
    if w:
        zasieg_miasta *= min(max(w["wskaznik"], 0.5), 2.0)

    return {"zaklad": zaklad, "km": round(dyst), "udzial": round(udzial, 3), "popyt": p, "ogl_rynku": ogl,
            "wlasny_wskaznik": (w or {}).get("wskaznik"),
            "wynik": round(p * zasieg_miasta * (1 - udzial), 1), "region": region}


def siatka(produkt, kandydaci, popyt, rynek, wlasne=None, zajete=None, maks_na_miasto=6,
           maks_na_wojewodztwo=None):
    """Zwraca listę miejscowości pod jeden produkt, posortowaną wynikiem, z limitem na region.

    Limit na województwo jest adaptacyjny. Produkty drogie (od 350 zł/t) uniosą transport
    przez pół Polski, więc rozsypujemy je szerzej — geografia nic tam nie kosztuje.
    Produkty tanie i tak są zamknięte w promieniu kilkudziesięciu kilometrów od zakładu,
    więc zagęszczenie w jednym województwie jest u nich naturalne, nie jest błędem.
    """
    if maks_na_wojewodztwo is None:
        maks_na_wojewodztwo = 4 if produkt["cena_t"] >= 350 else 6
    zajete = zajete if zajete is not None else {}
    oceny = []
    for miasto in kandydaci:
        o = ocena(miasto, produkt["zaklady"], produkt["cena_t"],
                  KOSZYKI[produkt["koszyk"]], popyt, rynek, wlasne)
        if o and o["popyt"] > 0:
            oceny.append(dict(o, name=miasto["name"], city_id=miasto["id"],
                              region_id=miasto["region_id"]))
    oceny.sort(key=lambda x: -x["wynik"])
    out, na_region = [], {}
    for o in oceny:
        if len(out) >= produkt["ile"]:
            break
        if na_region.get(o["region_id"], 0) >= maks_na_wojewodztwo:
            continue
        # Globalny limit na miejscowość: dziesięć naszych ogłoszeń w jednym mieście
        # konkurowałoby ze sobą w tym samym wyszukiwaniu lokalnym i wyglądałoby na spam.
        if zajete.get(o["city_id"], 0) >= maks_na_miasto:
            continue
        na_region[o["region_id"]] = na_region.get(o["region_id"], 0) + 1
        zajete[o["city_id"]] = zajete.get(o["city_id"], 0) + 1
        out.append(o)
    return out


# Produkty z zakładami wysyłkowymi wprost z kart produktowych agria.pl (pole „Magazyn").
PRODUKTY = [
    {"klucz": "agrobielik-70-staw", "cena_t": 220, "koszyk": "stawy", "ile": 22,
     "zaklady": ["Niedomice", "Sitkówka"]},
    {"klucz": "agrobielik-70-gleba", "cena_t": 220, "koszyk": "tlenkowe", "ile": 20,
     "zaklady": ["Niedomice", "Sitkówka"]},
    {"klucz": "agrobielik-90", "cena_t": 750, "koszyk": "tlenkowe", "ile": 18,
     "zaklady": ["Niedomice", "Sitkówka"]},
    {"klucz": "oxyfertil-90", "cena_t": 790, "koszyk": "tlenkowe", "ile": 14,
     "zaklady": ["Góraźdżce", "Tarnów Opolski", "Niedomice"]},
    {"klucz": "weglanowe-granulowane", "cena_t": 350, "koszyk": "granulowane", "ile": 20,
     "zaklady": ["Draby", "Niedomice", "Tarnów Opolski"]},
    {"klucz": "weglanowe-magnez-granulowane", "cena_t": 370, "koszyk": "granulowane_mg", "ile": 18,
     "zaklady": ["Draby", "Niedomice"]},
    {"klucz": "kreda-nawozowa-sypka", "cena_t": 125, "koszyk": "kreda", "ile": 16,
     "zaklady": ["Pierzchnica"]},
    {"klucz": "kreda-nawozowa-granulowana", "cena_t": 410, "koszyk": "kreda", "ile": 14,
     "zaklady": ["Kornica", "Niedomice"]},
    {"klucz": "weglanowe-odmiana-04", "cena_t": 57, "koszyk": "weglanowe", "ile": 16,
     "zaklady": ["Bukowa", "Celiny", "Góraźdżce", "Tarnów Opolski"]},
    {"klucz": "kreda-pastewna", "cena_t": 190, "koszyk": "pastewna", "ile": 12,
     "zaklady": ["Bukowa", "Celiny"]},
    {"klucz": "weglanowe-magnez-odmiana-04", "cena_t": 50, "koszyk": "weglanowe", "ile": 12,
     "zaklady": ["Chęciny"]},
    {"klucz": "weglanowe-magnez-odmiana-05", "cena_t": 36, "koszyk": "weglanowe", "ile": 8,
     "zaklady": ["Kostomłoty Drugie", "Łagów"]},
    {"klucz": "mieszanka-tlenkowo-weglanowa", "cena_t": 120, "koszyk": "tlenkowe", "ile": 10,
     "zaklady": ["Sitkówka"]},
]

if __name__ == "__main__":
    popyt = json.load(open(os.path.join(D, "popyt-woj.json"), encoding="utf-8"))

    if "--zasieg" in sys.argv:
        print(f"Założenie transportowe: {ZL_ZA_KM:.0f} zł/km przy {TONY:.0f} t "
              f"= {ZL_T_KM:.2f} zł za tonę na kilometr (DO POTWIERDZENIA U PAWŁA)\n")
        print(f"{'produkt':<40}{'zł/t':>7}{'zasięg przy 50% ceny':>24}")
        for nazwa, cena in [("Węglanowe z Mg odm. 05", 36), ("Węglanowe odm. 04", 57),
                            ("Mieszanka tlenkowo-węglanowa", 120), ("Kreda nawozowa sypka", 125),
                            ("Kreda pastewna", 190), ("Agrobielik 70 luz", 220),
                            ("Węglanowe granulowane", 350), ("Kreda granulowana", 410),
                            ("Agrobielik 90 luz 0–3", 750), ("Oxyfertil 90 big-bag", 790),
                            ("Wapno palone mielone", 950)]:
            print(f"{nazwa:<40}{cena:>7}{zasieg(cena):>21.0f} km")
        print("\nDla porównania: Niedomice → Gdańsk to ~500 km w linii prostej.")
        sys.exit()

    kandydaci = json.load(open(os.path.join(D, "miasta-kandydaci.json"), encoding="utf-8"))
    rynek = json.load(open(os.path.join(D, "miasta-rynek.json"), encoding="utf-8"))
    wlasne = json.load(open(os.path.join(D, "wyniki-wlasne.json"), encoding="utf-8"))["miasta"]
    out, zajete = {}, {}
    for p in PRODUKTY:
        s = siatka(p, kandydaci, popyt, rynek, wlasne, zajete)
        out[p["klucz"]] = s
        naj, dal = s[0], max(s, key=lambda x: x["km"])
        print(f"{p['klucz']:<30}{p['cena_t']:>5} zł/t  {len(s):>3} miast  "
              f"najdalsze {dal['km']:>3} km ({dal['udzial']*100:>2.0f}% ceny)  "
              f"czoło: {naj['name']}")
    json.dump(out, open(os.path.join(D, "siatka-miast.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    wszystkie = [m["name"] for s in out.values() for m in s]
    print(f"\nrazem ogłoszeń: {len(wszystkie)} | unikalnych miejscowości: {len(set(wszystkie))}")
