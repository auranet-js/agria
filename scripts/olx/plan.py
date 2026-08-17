#!/usr/bin/env python3
"""Plan 200 ogłoszeń OLX dla AGRII — produkty, tytuły pod intencję, siatka miast.

Wejście: data/olx/product-specs.json (parametry z renderu kart agria.pl) + cennik
z docs/operations/CENNIK_PAWEL_2026-08-07.md (przepisany tutaj jako ceny „od").
Wyjście: data/olx/plan-ogloszen.json — gotowe do POST /partner/adverts.

Zasady, z których wynika ten plan:
- Regulamin OLX dopuszcza to samo ogłoszenie w wielu lokalizacjach w kategoriach płatnych,
  pod warunkiem różnych lokalizacji i jednego konta — na tym stoi model liderów kategorii.
- Jedno ogłoszenie = jeden przedmiot (regulamin), więc rozbijamy na produkty,
  zamiast powielać jedną ofertę zbiorczą.
- Tytuł prowadzi intencją, nie ceną — ale cena z JEDNOSTKĄ zostaje, bo to odróżnia
  ofertę od wabików bez jednostki, którymi kategoria jest zapchana.
- Miasta wyliczone w `grid.py` z popytu i kosztu transportu, per produkt — nie dobrane
  z wyczucia. Wapno po 57 zł/t nie jedzie 400 km, bo przewóz przebiłby cenę towaru.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = os.path.join(HERE, "..", "..", "data", "olx", "product-specs.json")
OUT = os.path.join(HERE, "..", "..", "data", "olx", "plan-ogloszen.json")
CITIES = os.path.join(HERE, "..", "..", "data", "olx", "cities-all.json")

CAT_NAWOZY = 4368

# Siatka miast NIE jest tu wpisywana ręcznie — pochodzi z `grid.py`, który wylicza ją
# z popytu per województwo (DataForSEO) i z ekonomiki transportu per produkt (zakłady
# wysyłkowe z kart produktowych, cena za tonę, koszt przewozu). Wcześniejsza wersja miała
# tu listy miast dobrane „pod stawy" i „pod rolnictwo" z głowy — to było zgadywanie.
# Wejście: data/olx/siatka-miast.json (uruchom najpierw `python3 scripts/olx/grid.py`).

# 13 pozycji × przypisana liczba miast = 200 ogłoszeń.
# Ceny: netto, loco magazyn (CENNIK_PAWEL_2026-08-07.md). W tytule podajemy jednostkę.
PRODUKTY = [
    {
        "siatka": "agrobielik-70-staw",
        "wc_id": 310, "sku": "AGR-001", "karta": "agrobielik-70",
        "tytul": "Wapno do stawu, tlenkowe palone 70% CaO, odkażanie dna i podniesienie pH wody, atest OSChR, luzem i big bag, od 220 zł/t",
        "lead": "Wapno tlenkowe palone do przygotowania stawu przed zalaniem i do zabiegów w sezonie. Podnosi pH wody, odkaża dno i przyspiesza mineralizację mułu, zwiększając pojemność użytkową stawu. Reakcja egzotermiczna — działanie widoczne w 2–3 tygodnie.",
        "intencja": "rybactwo — pH wody, mineralizacja mułu",
        "cena_pole": 220, "cena_opis": "od 220 zł/t netto luzem — cena za towar, bez transportu · dostępne również w big-bagach i workach",
        "pule": ["stawy"], "ile": 14,
        "uwaga": "wzorzec potwierdzony danymi konta: 94 odsłony telefonu = 45% kontaktów",
    },
    {
        "siatka": "agrobielik-70-gleba",
        "wc_id": 310, "sku": "AGR-001", "karta": "agrobielik-70",
        "tytul": "Wapno do odkwaszania gleb ciężkich, tlenkowe palone 70% CaO, szybkie działanie, atest OSChR, luzem i big bag, od 220 zł/t",
        "lead": "Wapno tlenkowe palone do szybkiego odkwaszania gleb średnich i ciężkich. Reaktywność bliska 100% oznacza, że efekt widać w 2–4 tygodnie, a nie w kolejnym sezonie. Uregulowany odczyn odblokowuje składniki pokarmowe już zalegające w glebie.",
        "intencja": "rolnictwo — szybkie podniesienie pH gleb średnich i ciężkich",
        "cena_pole": 220, "cena_opis": "od 220 zł/t netto luzem — cena za towar, bez transportu · dostępne również w big-bagach i workach",
        "pule": ["gleby_ciezkie"], "ile": 12,
    },
    {
        "siatka": "agrobielik-90",
        "wc_id": 311, "sku": "AGR-002", "karta": "agrobielik-90",
        "tytul": "Wapno tlenkowe 90% CaO pod zboża i rzepak, frakcja 0-3 i 2-8 mm, mniejsza dawka na hektar, atest OSChR, od 750 zł/t",
        "lead": "Najwyższa koncentracja tlenku wapnia w ofercie — 90% CaO. Wyższa koncentracja to mniejsza dawka na hektar i mniej ton do przewiezienia i rozsiania. Dostępne w dwóch frakcjach: 0–3 mm do szybkiego działania i 2–8 mm do wysiewu rozsiewaczem.",
        "intencja": "rolnictwo — najwyższa koncentracja CaO, mniejsza dawka na hektar",
        "cena_pole": 750, "cena_opis": "od 750 zł/t netto luzem — cena za towar, bez transportu · frakcje 0–3 mm i 2–8 mm",
        "pule": ["gleby_ciezkie", "wielkopolska"], "ile": 10,
        "uwaga": "w tej frakcji na OLX brak porównywalnej oferty",
    },
    {
        "siatka": "oxyfertil-90",
        "wc_id": 312, "sku": "AGR-003", "karta": "oxyfertil-90",
        "tytul": "Wapno tlenkowe 90% CaO w big bag, Oxyfertil, dostawa od 1 tony, do gleb średnich i ciężkich, atest OSChR, od 790 zł/t",
        "lead": "Wapno tlenkowe 90% CaO w big-bagach, sprzedawane od jednej tony — bez minimum całopojazdowego. Rozwiązanie dla gospodarstw, które potrzebują wysokiej koncentracji CaO, ale nie zamawiają 24 ton naraz.",
        "intencja": "rolnictwo — dostawa od 1 tony, bez całopojazdowego minimum",
        "cena_pole": 790, "cena_opis": "od 790 zł/t netto — cena za towar, bez transportu · dostawa od 1 tony",
        "pule": ["wielkopolska", "mazowsze"], "ile": 8,
    },
    {
        "siatka": "weglanowe-granulowane",
        "wc_id": 314, "sku": "AGR-008", "karta": "weglanowe-granulowane",
        "tytul": "Wapno granulowane pod rzepak i zboża, węglanowe do rozsiewacza, big bag 1 t i worki 25 kg, bez pylenia, od 350 zł/t",
        "lead": "Wapno węglanowe w granulacie — do wysiewu własnym rozsiewaczem nawozów, bez usługi wapnowania i bez pylenia. Pozwala wapnować w terminie, który pasuje do zabiegu, a nie do dostępności usługodawcy.",
        "intencja": "rolnictwo — wysiew własnym rozsiewaczem, bez usługi wapnowania",
        "cena_pole": 350, "cena_opis": "od 350 zł/t netto — cena za towar, bez transportu · dostawa od 1 tony, dostępne też w workach 25 kg",
        "pule": ["wielkopolska", "mazowsze"], "ile": 12,
    },
    {
        "siatka": "weglanowe-magnez-granulowane",
        "wc_id": 317, "sku": "AGR-011", "karta": "weglanowe-magnez-granulowane",
        "tytul": "Wapno granulowane z magnezem, węglanowo-magnezowe MgO, do gleb lekkich, do rozsiewacza, big bag i worki 25 kg, od 370 zł/t",
        "lead": "Wapno węglanowo-magnezowe w granulacie — odkwasza i jednocześnie uzupełnia magnez. Do gleb lekkich i stanowisk z rozpoznanym niedoborem MgO. Wysiew własnym rozsiewaczem.",
        "intencja": "rolnictwo — niedobory magnezu, gleby lekkie",
        "cena_pole": 370, "cena_opis": "od 370 zł/t netto — cena za towar, bez transportu · dostawa od 1 tony, dostępne też w workach 25 kg",
        "pule": ["wielkopolska", "poludnie_zachod"], "ile": 10,
    },
    {
        "siatka": "kreda-nawozowa-sypka",
        "wc_id": 306, "sku": "AGR-014", "karta": "kreda-nawozowa-sypka",
        "tytul": "Kreda nawozowa luzem pod zboża, wapno węglanowe sypkie, łagodne odkwaszanie, dostawa 24 t, atest OSChR, od 125 zł/t",
        "lead": "Kreda nawozowa luzem do odkwaszania większych areałów. Węglanowa forma działa łagodnie i długo, bez ryzyka poparzenia roślin. Dostawa całopojazdowa 24 t.",
        "intencja": "rolnictwo — duże areały, dostawa 24 t",
        "cena_pole": 125, "cena_opis": "125 zł/t netto za towar, bez transportu · dostawa całopojazdowa 24 t",
        "pule": ["gleby_ciezkie", "mazowsze"], "ile": 10,
    },
    {
        "siatka": "kreda-nawozowa-granulowana",
        "wc_id": 305, "sku": "AGR-013", "karta": "kreda-nawozowa-granulowana",
        "tytul": "Kreda nawozowa granulowana, big bag od 1 t i worki 25 kg, do rozsiewacza, łagodne odkwaszanie, atest OSChR, od 410 zł/t",
        "lead": "Kreda nawozowa w granulacie, big-bag od jednej tony. Łagodne, rozłożone w czasie odkwaszanie przy wysiewie własnym rozsiewaczem — dla gospodarstw, które nie zamawiają dostaw całopojazdowych.",
        "intencja": "rolnictwo — mniejsze gospodarstwa, wysiew rozsiewaczem",
        "cena_pole": 410, "cena_opis": "od 410 zł/t netto — cena za towar, bez transportu · dostawa od 1 tony, dostępne też w workach 25 kg",
        "pule": ["poludnie_zachod", "wielkopolska"], "ile": 8,
    },
    {
        "siatka": "weglanowe-odmiana-04",
        "wc_id": 315, "sku": "AGR-006", "karta": "weglanowe-odmiana-04",
        "tytul": "Wapno węglanowe odm. 04 luzem, kreda nawozowa do odkwaszania gleby, dostawa 24 t, atest OSChR, 57 zł/t netto",
        "lead": "Wapno węglanowe odmiany 04 luzem — najniższy koszt odkwaszania w przeliczeniu na hektar. Do planowego wapnowania większych powierzchni, gdzie liczy się cena tony, a nie szybkość reakcji.",
        "intencja": "rolnictwo — najniższy koszt odkwaszania na hektar",
        "cena_pole": 57, "cena_opis": "57 zł/t netto za towar, bez transportu · dostawa całopojazdowa 24 t",
        "pule": ["mazowsze", "poludnie_zachod"], "ile": 10,
        "uwaga": "cena w parytecie z kopalnią Morawica (57,40 zł/t netto loco)",
    },
    {
        "siatka": "kreda-pastewna",
        "wc_id": 307, "sku": "AGR-015", "karta": "kreda-pastewna",
        "tytul": "Kreda pastewna dla bydła i drobiu, wapń w paszy, węglan wapnia paszowy, luzem i w workach 30 kg, od 190 zł/t",
        "lead": "Kreda pastewna jako źródło wapnia w żywieniu bydła, drobiu i trzody. Dostępna w kilku frakcjach dobieranych do rodzaju paszy i systemu zadawania.",
        "intencja": "paszarstwo — suplementacja wapnia",
        "cena_pole": 190, "cena_opis": "od 190 zł/t netto luzem — cena za towar, bez transportu · dostępna również w workach 30 kg",
        "pule": ["paszarstwo"], "ile": 6,
    },
    {
        "siatka": "weglanowe-magnez-odmiana-04",
        "wc_id": 318, "sku": "AGR-009", "karta": "weglanowe-magnez-odmiana-04",
        "tytul": "Wapno węglanowo-magnezowe odm. 04 luzem, magnez i odkwaszanie, gleby lekkie, dostawa 24 t, atest OSChR, 50 zł/t netto",
        "lead": "Wapno węglanowo-magnezowe odmiany 04 luzem. Odkwasza i jednocześnie uzupełnia magnez, którego brakuje na glebach lekkich i przy intensywnym nawożeniu potasem. Działa łagodnie i długo, bez ryzyka poparzenia roślin.",
        "intencja": "rolnictwo — odkwaszanie z uzupełnieniem magnezu, duże areały",
        "cena_pole": 50, "cena_opis": "50 zł/t netto za towar, bez transportu · dostawa całopojazdowa 24 t",
        "ile": 12,
    },
    {
        "siatka": "weglanowe-magnez-odmiana-05",
        "wc_id": 319, "sku": "AGR-010", "karta": "weglanowe-magnez-odmiana-05",
        "tytul": "Wapno magnezowe odm. 05 luzem, węglanowo-magnezowe, magnez do gleby, dostawa całopojazdowa 24 t, atest OSChR, 36 zł/t netto",
        "lead": "Wapno węglanowo-magnezowe odmiany 05 — najniższy koszt odkwaszania z magnezem w przeliczeniu na hektar. Do planowego wapnowania większych powierzchni, gdzie liczy się cena tony, a nie szybkość reakcji.",
        "intencja": "rolnictwo — najniższy koszt tony przy uzupełnieniu magnezu",
        "cena_pole": 36, "cena_opis": "36 zł/t netto za towar, bez transportu · dostawa całopojazdowa 24 t",
        "ile": 8,
    },
    {
        "siatka": "mieszanka-tlenkowo-weglanowa",
        "wc_id": 308, "sku": "AGR-005", "karta": "mieszanka-tlenkowo-weglanowa",
        "tytul": "Wapno tlenkowo-węglanowe do gleb kwaśnych, szybkie i długie działanie, luzem, dostawa 24 t, atest OSChR, od 120 zł/t",
        "lead": "Połączenie wapna tlenkowego i węglanowego w jednym produkcie. Część tlenkowa podnosi pH szybko, część węglanowa utrzymuje efekt przez kolejne miesiące. Rozwiązanie dla stanowisk, gdzie potrzebna jest i szybka reakcja, i trwałość.",
        "intencja": "rolnictwo — szybki start odkwaszania z długim podtrzymaniem",
        "cena_pole": 120, "cena_opis": "120 zł/t netto za towar, bez transportu · dostawa całopojazdowa 24 t",
        "ile": 10,
    },
]

def wczytaj_siatke():
    path = os.path.join(HERE, "..", "..", "data", "olx", "siatka-miast.json")
    if not os.path.exists(path):
        sys.exit("brak siatki miast — uruchom najpierw: python3 scripts/olx/grid.py")
    return json.load(open(path, encoding="utf-8"))


if __name__ == "__main__":
    specs = {}
    for row in json.load(open(SPECS, encoding="utf-8")):
        specs[row["url"].rstrip("/").split("/")[-1]] = row

    siatki = wczytaj_siatke()
    plan = []
    for p in PRODUKTY:
        spec = specs.get(p["karta"])
        if not spec:
            print(f"  UWAGA: brak specyfikacji dla '{p['karta']}' — sprawdź extract_specs.py")
        miasta = siatki.get(p["siatka"], [])
        if len(miasta) != p["ile"]:
            print(f"  UWAGA: siatka '{p['siatka']}' ma {len(miasta)} miast, plan zakłada {p['ile']}")
        naj = max(miasta, key=lambda m: m["udzial"]) if miasta else None
        print(f"{p['tytul'][:56]:<58}{len(miasta):>3} miast  "
              f"najdalsze {naj['km'] if naj else 0:>3} km "
              f"({(naj['udzial'] if naj else 0)*100:>2.0f}% ceny)")
        for c in miasta:
            plan.append({
                "wc_id": p["wc_id"], "sku": p["sku"], "karta": p["karta"], "siatka": p["siatka"],
                "title": p["tytul"], "lead": p["lead"], "intencja": p["intencja"],
                "category_id": CAT_NAWOZY,
                "price": p["cena_pole"], "cena_opis": p["cena_opis"],
                "city": c["name"], "city_id": c["city_id"], "region_id": c["region_id"],
                "zaklad": c["zaklad"], "km_z_zakladu": c["km"], "transport_udzial": c["udzial"],
                "spec": (spec or {}).get("spec", {}),
                "uwaga": p.get("uwaga"),
            })

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(plan, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nrazem ogłoszeń: {len(plan)}")
    import collections
    licznik = collections.Counter(r["city"] for r in plan)
    print(f"miast objętych: {len(licznik)} | województw: {len({r['region_id'] for r in plan})}")
    print(f"najwięcej ogłoszeń w jednym mieście: {licznik.most_common(4)}")
    daleko = [r for r in plan if r["transport_udzial"] > 0.4]
    if daleko:
        print(f"UWAGA: {len(daleko)} ogłoszeń, gdzie transport zjada >40% ceny towaru — "
              f"do przejrzenia: {sorted({r['city'] for r in daleko})}")
    print(f"→ {os.path.relpath(OUT)}")
