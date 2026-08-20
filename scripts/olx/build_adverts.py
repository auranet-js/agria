#!/usr/bin/env python3
"""Buduje gotowe ładunki POST /partner/adverts z planu + parametrów z kart produktowych.

Wejście:  data/olx/plan-ogloszen.json, data/olx/product-specs.json
Wyjście:  data/olx/adverts-payload.json

Reguły treści wymuszone tu kodem, nie dobrą wolą:
- ŻADNEGO numeru telefonu w opisie (regulamin OLX pkt 4: dane kontaktowe wyłącznie
  w polach formularza). Stare ogłoszenia AGRII kończyły się `6*6*4*3*9*3*0*6*2`.
- Jedno ogłoszenie = jeden produkt. Bez wyliczania innych pozycji z oferty i bez wymieniania
  kilku form sprzedaży naraz — pkt 4.4.h Regulaminu OLX, zacytowany przy wstrzymaniu ogłoszenia
  1089946612 dnia 20.08.
- Cena KOŃCOWA, ze wskazaniem, czego dotyczy — pkt 4.4.c i 4.4.i. Żadnego „od", żadnej klauzuli
  o cenach orientacyjnych. Bez określenia netto/brutto (decyzja Janka 20.08): regulamin wymaga
  „Ceny końcowej w złotych polskich", słowo „brutto" pochodzi z artykułu pomocy, nie z 4.4.c.
- Parametry wyłącznie z kart produktowych agria.pl, zero wymyślania — pkt 13.1.d zabrania
  podawania nieprawdziwych informacji o Przedmiocie i zatajania istotnych.
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

V2 = "https://auratest.pl/agria-olx/v2/agria-{}.jpg"

# GALERIA — osiem slotów, czyli limit kategorii 4368. Kolejność ustalona 20.08 po obejrzeniu
# 214 pierwszych zdjęć konkurencji i po zmierzeniu, że miniatura na liście OLX to slot
# `image;s=516x361`, POZIOMY, a CDN nie kadruje, tylko wpisuje zdjęcie w prostokąt.
# Pionowa plansza 435x700 zajmowała w nim 43 % szerokości niezależnie od rozdzielczości —
# dlatego pierwszy kadr jest poziomy 1500x1050, dokładnie w kształcie slotu.
#
#   1. miniatura zastosowaniowa (per SIATKA — inna dla stawu, inna dla gleby ciężkiej):
#      próbka towaru na zielonym gradiencie marki, tło pod zastosowanie, u góry nazwa produktu
#      i ZASTOSOWANIE, w lewym dolnym rogu pasek z KORZYŚCIĄ
#   2. zdjęcie studyjne produktu (kółko z karty produktowej, WEBP → JPG)
#   3. karta katalogowa z parametrami (bez kodu QR i bez stopki z adresem i telefonem)
#   4. big-bag — archetyp nr 2 kategorii, 25 % pierwszych zdjęć konkurencji
#   5. plansza produktowa 750x1205 (makro materiału z podpisem)
#   6. kadr otwierający „WAPNA NAWOZOWE"
#   7. karta z kodem QR do kalkulatora (UTM z nazwą karty w utm_content)
#
# Drugi kadr generowany („pryzma ze skalą") wypadł 20.08: przy łopacie albo palecie w kadrze
# generator musiał narysować ziarno widoczne i z uziarnienia 3–8 mm robił bryły wielkości
# pięści. Uziarnienie pokazują teraz zdjęcia realne — studyjne kółko i plansza.
#
# Sloty 1 i 4 zależą od SIATKI, nie od karty: Agrobielik 70 idzie jako dwa różne ogłoszenia
# (do stawu / na odkwaszanie) i każde ma własny kontekst zastosowania.

# karta produktowa → plansza z zdjecia.py. Kreda pastewna nie ma własnej planszy (plansze są
# cięte po dwie z pięciu kadrów kitu), więc dostaje własne zdjęcie frakcji z karty produktowej.
PLANSZA = {
    "agrobielik-70": "agrobielik-70",
    "agrobielik-90": "agrobielik-90-0-3",
    "oxyfertil-90": "oxyfertil-90",
    "weglanowe-granulowane": "granulowane-bez-magnezu",
    "weglanowe-magnez-granulowane": "granulowane-z-magnezem",
    "weglanowe-odmiana-04": "weglanowe-bez-magnezu",
    "weglanowe-magnez-odmiana-04": "weglanowe-z-magnezem",
    "weglanowe-magnez-odmiana-05": "weglanowe-z-magnezem",
    "kreda-nawozowa-sypka": "kreda-sypka",
    "kreda-nawozowa-granulowana": "kreda-granulowana",
    "kreda-pastewna": "kreda-pastewna-frakcja",
}

# karta produktowa → strona katalogu druku 2026 (karty_katalogowe.py)
KARTA_KATALOGOWA = {
    "agrobielik-70": "karta-agrobielik-70",
    "agrobielik-90": "karta-agrobielik-90-0-3",
    "oxyfertil-90": "karta-oxyfertil-90",
    "weglanowe-granulowane": "karta-weglanowe-granulowane",
    "weglanowe-magnez-granulowane": "karta-weglanowe-magnez-granulowane",
    "weglanowe-odmiana-04": "karta-weglanowe-odmiana-04",
    "weglanowe-magnez-odmiana-04": "karta-weglanowe-magnez-odmiana-04",
    "weglanowe-magnez-odmiana-05": "karta-weglanowe-magnez-odmiana-05",
    "kreda-nawozowa-sypka": "karta-kreda-nawozowa-sypka",
    "kreda-nawozowa-granulowana": "karta-kreda-nawozowa-granulowana",
    "kreda-pastewna": "karta-kreda-pastewna",
}

# Zdjęcia studyjne — kółka z kart produktowych agria.pl, robione w studio.
# `kreda-nawozowa-granulowana` NIE MA tu wpisu świadomie: na produkcji karta ID 305 ma podpięte
# `wapno-weglanowe-bez-magnezu-grankal-agria.webp`, czyli to samo zdjęcie co ID 314 (wapno
# węglanowe granulowane). Pokazałaby więc inny produkt. Wróci, gdy karta dostanie własne zdjęcie.
STUDIO = {k: f"studio-{k}" for k in (
    "agrobielik-70", "agrobielik-90", "oxyfertil-90", "weglanowe-granulowane",
    "weglanowe-magnez-granulowane", "weglanowe-odmiana-04", "weglanowe-magnez-odmiana-04",
    "weglanowe-magnez-odmiana-05", "kreda-nawozowa-sypka", "kreda-pastewna")}


def galeria(row, bledy):
    """Składa listę zdjęć dla jednego ogłoszenia. Puste sloty wypadają, kolejność zostaje."""
    karta, siatka = row["karta"], row["siatka"]
    sloty = [
        f"mini-{siatka}",
        STUDIO.get(karta),
        KARTA_KATALOGOWA.get(karta),
        "bigbag",
        PLANSZA.get(karta),
        "hero",
        f"info-{karta}",
    ]
    for nazwa, mapa in (("karta katalogowa", KARTA_KATALOGOWA), ("plansza", PLANSZA)):
        if karta not in mapa:
            bledy.append(f"brak wpisu {nazwa} dla {karta}")
    return [{"url": V2.format(s)} for s in sloty if s][:8]

# Które parametry z karty produktowej wchodzą do opisu i w jakiej kolejności.
PARAMETRY = ["Zawartość CaO", "Zawartość CaO+MgO", "Zawartość MgO", "Reaktywność",
             "Typ reakcji", "Forma fizyczna", "Frakcja", "Norma", "Producent"]
STOSOWANIE = ["Zastosowanie funkcjonalne", "Dawkowanie", "Szybkość działania",
              "Efekt zastosowania", "Dodatkowe zastosowanie"]

# Kalkulator: kod QR prowadzi do niego z ostatniego zdjęcia w galerii (scripts/olx/karta_info.py).
# W opisie NIE podajemy adresu WWW — w całej kategorii ma go 5 ogłoszeń na 1 204 i wygląda to
# na obchodzenie filtra, nie na dozwoloną praktykę (OLX_BASELINE_2026-08-07.md).
KALKULATOR = (
    "POLICZYMY ZA DARMO, ILE WAPNA POTRZEBUJESZ\n"
    "Podajesz pH gleby, jej kategorię i areał — kalkulator wapnowania wylicza dawkę na hektar "
    "i liczbę ton do zamówienia. Za darmo, bez rejestracji, wynik od ręki. "
    "Kod QR do kalkulatora jest na ostatnim zdjęciu w galerii.\n"
    "Wolisz, żeby ktoś to policzył za Ciebie? Napisz, jaki masz areał i wynik badania gleby — "
    "odeślemy wyliczenie. Doradzimy też, jak rozsiać: jaka dawka na przejazd, jaki termin "
    "i na co uważać przy Twoim sprzęcie."
)

# WYŁĄCZONE 20.08 po werdykcie moderacji. Pkt 4.4.h Regulaminu: „jedno Ogłoszenie może dotyczyć
# jednego Przedmiotu" — a to jest wyliczenie jedenastu innych. Sekcja weszła rano decyzją Janka
# i wypadła tego samego dnia, gdy OLX zacytował ten punkt przy wstrzymaniu ogłoszenia 1089946612.
# Zostaje w kodzie, bo 27,9 % żywych ogłoszeń kategorii ma podobne listy — jeśli okaże się,
# że powodem było co innego, wraca jedną linią.
# Wyliczenie z katalogu druku 2026 (17 kart produktowych) — nie z pamięci i nie z rozumowania.
POZOSTALA_OFERTA = (
    "POZOSTAŁA OFERTA\n"
    "• Wapno tlenkowe: Agrobielik 70, Agrobielik 90 (0–3 i 2–8 mm), Oxyfertil 90, "
    "tlenkowe z magnezem\n"
    "• Wapno węglanowe sypkie i granulowane, także z magnezem — odmiany 04 i 05\n"
    "• Kreda nawozowa sypka i granulowana, kreda pastewna\n"
    "• Dolomit, mieszanka tlenkowo-węglanowa\n"
    "• Wapno hydratyzowane Bielik, wapno palone mielone wysokoreaktywne\n"
    "Pytaj o dostępność i wycenę pod numerem z ogłoszenia."
)

# Transport. „Własny transport" deklaruje 4 % kategorii, wywrotkę 6 %, HDS 1 % (pomiar 20.08
# na 1 105 opisach) — czyli kategoria mówi „z transportem", nie mówiąc czyim i czym. To jest
# wolne miejsce i AGRIA ma czym je zająć. Decyzja Janka 20.08: NIE nazywamy magazynów,
# NIE piszemy, czego kupujący potrzebuje do rozładunku, NIE podajemy stawek transportu.
TRANSPORT = (
    "TRANSPORT\n"
    "• Wozimy własną flotą z własnych magazynów — termin ustalamy z Tobą, nie z przewoźnikiem "
    "z rynku.\n"
    "• Towar luzem przyjeżdża naczepą samowyładowczą, ładunek całosamochodowy 24 tony.\n"
    "• Big-bagi i worki na paletach — dostawa również na mniejsze zamówienia.\n"
    "• Koszt dostawy liczymy pod konkretny adres. Napisz, dokąd ma jechać, a policzymy."
)

# Rozsiew: doradztwo, nie usługa (decyzja Janka 20.08). Sekcja jest twierdząca — mówi, co dajemy,
# a nie czego nie robimy. Zdanie „usługi wysiewu nie wykonujemy" wypadło na jego polecenie:
# ogłoszenie sprzedażowe nie jest miejscem na wyliczanie, czego nie ma w ofercie.
ROZSIEW = (
    "ROZSIEW I DOBÓR DAWKI\n"
    "Doradzimy, jaką dawkę wysiać, w jakim terminie i jakim sprzętem, żeby zabieg miał sens "
    "przy Twoim odczynie i rodzaju gleby."
)

# Dofinansowanie: kategoria gra tym hasłem w 423 ogłoszeniach na 1 105, ale prawie zawsze
# ogólnikowo — „spełniamy wymagania dofinansowania" (115×), „zgodne z dofinansowaniem" (46×).
# Konkretów nie podaje nikt: zero wystąpień NFOŚiGW, zero słowa „wniosek", 27 % wspomina fakturę.
# Dlatego my mówimy DOKŁADNIE, co jest po naszej, a co po stronie kupującego — to jest realna
# przewaga, a nie kolejne „spełniamy wymagania".

# Nabór dotyczy WYŁĄCZNIE województwa łódzkiego, a siatka obejmuje dziewięć województw, więc
# ten akapit wchodzi tylko na 12 ogłoszeń z region_id 7 (Łódź, Piotrków, Tomaszów, Łowicz).
# Fakty zweryfikowane 20.08 na stronie NFOŚiGW, nie przepisane z drugiej ręki.
REGION_LODZKIE = 7
DOFINANSOWANIE_LODZKIE = (
    "NABÓR W WOJEWÓDZTWIE ŁÓDZKIM\n"
    "Na terenie województwa łódzkiego trwa nabór wniosków o dotację na wapnowanie gleb dla osób "
    "fizycznych prowadzących działalność rolniczą, prowadzony przez Narodowy Fundusz Ochrony "
    "Środowiska i Gospodarki Wodnej. Dotacja do 150 zł za tonę czystego składnika CaO lub "
    "CaO+MgO, od 1 000 do 20 000 zł na wniosek, dla użytków rolnych o odczynie pH 5,5 lub "
    "niższym. Jedna działka ewidencyjna nie częściej niż raz na cztery lata. Nabór do "
    "31 sierpnia 2027 r. Szczegółowe warunki określa regulamin naboru."
)

# Dowód społeczny wyłącznie z faktów, które da się obronić: rok założenia, atest do każdej
# partii, dwa magazyny, dostawy własną flotą (karta katalogowa 2026). Żadnych „setek zadowolonych
# klientów" ani „numeru 1 w Polsce" — kategoria jest tym zapchana i to nic nie znaczy.
DLACZEGO = (
    "DLACZEGO AGRIA\n"
    "• Firma rodzinna od 1989 roku — 37 lat na rynku surowców wapniowych.\n"
    "• Atest OSChR do każdej partii. Parametry zgodne z kartami producentów, bez niespodzianek "
    "przy rozładunku.\n"
    "• Własne magazyny i dostawy własną flotą — nie pośredniczymy w cudzym towarze.\n"
    "• Ta sama jakość przy każdym kolejnym zamówieniu, nie partia w partię inna."
)

# CTA na końcu, przed stopką. Bez numeru telefonu i bez adresu — regulamin OLX dopuszcza dane
# kontaktowe wyłącznie w polach formularza, a walidacja API odrzuca je w opisie.
KONTAKT = (
    "MASZ PYTANIE? DZWOŃ ALBO NAPISZ\n"
    "Nie wiesz, które wapno wybrać i ile go potrzeba? Zadzwoń albo napisz wiadomość przez OLX — "
    "chętnie doradzimy, jaki rodzaj i jaka dawka będą właściwe dla Twojej gleby, policzymy "
    "potrzebną ilość i koszt dostawy pod Twój adres."
)

# Dofinansowanie. 37 % opisów w kategorii obiecuje dotacje, ale to jest obietnica pusta w naszej
# siatce: sprawdzone 20.08 — Mazowieckie (55 ogłoszeń) ma stronę programu z 2020 i nabór
# 01.01.2020–31.12.2021, Małopolskie (33) pisze wprost „NABÓR ZAKOŃCZONY, wyczerpanie alokacji",
# Wielkopolskie (21) zamknęło nabór 15.12.2023, a 02.08.2024 wyczerpał się krajowy limit
# de minimis w rolnictwie. Otwarte jest Łódzkie (12 ogłoszeń) — ale to osobny program wojewódzki
# na 2026, wyłącznie dla osób fizycznych. Dlatego NIE obiecujemy pieniędzy. Mówimy o dokumentach,
# które AGRIA realnie wystawia, i odsyłamy po stan naboru do właściwego funduszu.
DOFINANSOWANIE = (
    "DOKUMENTY POD DOFINANSOWANIE\n"
    "Do każdej dostawy wystawiamy fakturę VAT z określeniem typu i parametrów wapna oraz atest "
    "partii — czyli komplet, którego fundusz wymaga od SPRZEDAWCY. Opinię o odczynie Twojej gleby "
    "wydaje właściwa miejscowo Okręgowa Stacja Chemiczno-Rolnicza, o nią występujesz sam.\n"
    "Nabory prowadzą fundusze ochrony środowiska i w każdym województwie wyglądają "
    "inaczej — część jest zamknięta z powodu wyczerpania środków, część trwa. Sprawdź stan "
    "w swoim funduszu przed zakupem. Dokumenty przygotujemy niezależnie od tego, kiedy złożysz "
    "wniosek."
)

STOPKA = (
    "DOKUMENTY\n"
    "Atest OSChR do każdej partii. Karty produktowe i świadectwa jakości dostępne "
    "do pobrania oraz dostarczane przy dostawie.\n\n"
    "AGRIA Sp. z o.o. — surowce wapniowe od 1989 r.\n"
    "Stabilne parametry. Pewne dostawy."
)

TELEFON = re.compile(r"(?:\d[\s\-\*\.]{0,2}){9,}")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
# Reguły walidacji z OpenAPI Partner API (sekcja „Validation rules"), nie z domysłów:
# opis 80–9000 znaków, tytuł 16–150, wielkie litery ≤50 % tekstu, żaden z tych znaków
# nie może wystąpić trzy razy pod rząd, e-maile i telefony zabronione w tytule i opisie.
TROJKA = re.compile(r"([!?.,\-=+#%&@*_><:()|])\1\1")


def sprawdz_regulyOLX(tytul_txt, opis_txt, etykieta, bledy):
    if not 16 <= len(tytul_txt) <= 150:
        bledy.append(f"TYTUŁ poza 16–150 znaków ({len(tytul_txt)}): {etykieta}")
    if not 80 <= len(opis_txt) <= 9000:
        bledy.append(f"OPIS poza 80–9000 znaków ({len(opis_txt)}): {etykieta}")
    for nazwa, tekst in (("tytule", tytul_txt), ("opisie", opis_txt)):
        m = TROJKA.search(tekst)
        if m:
            bledy.append(f"TRZY ZNAKI POD RZĄD w {nazwa} {etykieta}: {m.group(0)!r}")
        litery = [c for c in tekst if c.isalpha()]
        if litery and sum(c.isupper() for c in litery) / len(litery) > 0.5:
            bledy.append(f"PONAD 50% WIELKICH LITER w {nazwa} {etykieta}")
        if EMAIL.search(tekst):
            bledy.append(f"E-MAIL w {nazwa} {etykieta}")


def sekcja(naglowek, spec, klucze):
    linie = [f"• {k}: {spec[k]}" for k in klucze if spec.get(k)]
    return f"{naglowek}\n" + "\n".join(linie) if linie else ""


def tytul(t, bledy):
    """OLX tnie tytuł na 150 znakach. Wcześniej ucinaliśmy po cichu i „…od 350 zł/t" wychodziło
    jako „…od 350 zł/" na dwudziestu ogłoszeniach. Teraz to błąd, nie milczące obcięcie."""
    if len(t) > 150:
        bledy.append(f"TYTUŁ za długi ({len(t)} zn.): {t}")
    return t[:150]


# Siedem miast, w których OLX odrzuca POST z pustym district_id („niepoprawna wartość").
# Wartości to dzielnice centralne, odczytane z GET /partner/cities/{id}/districts 20.08.
DISTRICTS = {17871: 351,   # Warszawa — Śródmieście
             4765: 83,     # Częstochowa — Śródmieście
             8959: 273,    # Kraków — Stare Miasto
             7691: 211,    # Katowice — Śródmieście
             19701: 387,   # Wrocław — Śródmieście
             13983: 327,   # Poznań — Stare Miasto
             10609: 299}   # Łódź — Śródmieście


def lokalizacja(city_id):
    loc = {"city_id": city_id}
    if city_id in DISTRICTS:
        loc["district_id"] = DISTRICTS[city_id]
    return loc


def opis(row, spec):
    czesci = [row["lead"]]

    p = sekcja("PARAMETRY", spec, PARAMETRY)
    if p:
        czesci.append(p)

    s = sekcja("ZASTOSOWANIE", spec, STOSOWANIE)
    if s:
        czesci.append(s)

    # Z linii cenowej wypadły dwie rzeczy i tylko dwie: słowo „netto" oraz klauzula
    # „Ceny orientacyjne, nie stanowią oferty handlowej w rozumieniu Kodeksu cywilnego"
    # (pkt 4.4.c Regulaminu OLX — cena ma być końcowa). Worki wypadły, big-bagi zostają.
    czesci.append(
        "FORMY DOSTAWY I CENA\n"
        f"• {row['cena_opis']}\n"
        "• Ceny za sam towar — bez transportu. Transport wyceniamy indywidualnie "
        "w zależności od miejsca dostawy.\n"
        "• Możliwy odbiór własny."
    )
    czesci.append(TRANSPORT)
    czesci.append(ROZSIEW)
    # Pole „Magazyn" z karty produktowej wypisuje zakłady DOSTAWCÓW (Sitkówka, Bukowa, Celiny,
    # Góraźdżce…). W ogłoszeniu wystawionym w Płocku to tylko myli czytelnika, a przy okazji
    # eksponuje strukturę zaopatrzenia. Lokalizacji własnych magazynów też nie podajemy —
    # decyzja Janka 20.08.
    if spec.get("Dostępność"):
        czesci.append(f"DOSTĘPNOŚĆ\n• {spec['Dostępność']}")
    czesci.append(KALKULATOR)
    czesci.append(DOFINANSOWANIE)
    # Nabór łódzki obowiązuje tylko w jednym z dziewięciu województw siatki — 12 ogłoszeń.
    if row.get("region_id") == REGION_LODZKIE:
        czesci.append(DOFINANSOWANIE_LODZKIE)
    czesci.append(POZOSTALA_OFERTA)
    czesci.append(DLACZEGO)
    czesci.append(KONTAKT)
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
        sprawdz_regulyOLX(row["title"], tresc, row["karta"], bledy)

        zdjecia = galeria(row, bledy)

        out.append({
            "title": tytul(row["title"], bledy),
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
            "location": lokalizacja(row["city_id"]),
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
