#!/usr/bin/env python3
"""Projekt przełożenia ogłoszeń OLX na teren wokół magazynów AGRII (Niedomice + Radgoszcz).

Powód (pomiar 28.08.2026, 200 ogłoszeń, 8 dni emisji):
    0–60 km od magazynów   0,065 odsłony numeru na ogłoszenie
    60–120 km              0,270      <- najlepszy pierścień
    120–200 km             0,141
    200–300 km             0,017
    >300 km                0,000
21 z 22 kontaktów przyszło z promienia do 200 km. Dalej stoi 68 ogłoszeń, które dały razem JEDEN.

Przyczyna rozlania siatki: `grid.py` liczy dystans od magazynu wpisanego w kartę produktu,
a karty wskazują magazyny PRODUCENTÓW (Kornica pod Siedlcami, Pierzchnica, Chęciny). Ten skrypt
liczy od magazynów AGRII i obsadza teren wokół nich — powiat dąbrowski i tarnowski w pierwszej
kolejności, potem sąsiednie w promieniu 110 km.

    przelozenie.py            projekt przydziału na ekran
    przelozenie.py --zapisz   zapis do data/olx/przelozenie-YYYY-MM-DD.json
"""
import json, math, os, sys, time
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")

NIEDOMICE = (50.150, 20.900)
RADGOSZCZ = (50.235, 21.030)
PROG_DO_PRZELOZENIA = 200      # km — powyżej tego ogłoszenie idzie do przełożenia
PROG_DOCELOWY = 110            # km — w tym promieniu szukamy miejsc docelowych
MAKS_NA_MIEJSCOWOSC = 4        # więcej naszych ogłoszeń w jednym miejscu konkurowałoby ze sobą

# Ile ogłoszeń wolno postawić w powiecie. Dąbrowski to powiat magazynu w Radgoszczy,
# tarnowski — magazynu w Niedomicach. Teren własny obsadzamy gęsto, dalej rozsypujemy.
LIMIT_POWIATU = {"dąbrowski": 12, "tarnowski": 10}
# Siedziby magazynów AGRII wchodzą do siatki NIEZALEŻNIE od rynku lokalnego — ogłoszenie
# z tą lokalizacją mówi kupującemu, że towar leży na miejscu. Radgoszcz ma zerowy rynek
# na OLX i bez tego wyjątku wypadłaby z rankingu.
WYMAGANE = {"Radgoszcz": 2, "Żabno": 4}
LIMIT_BLISKI = 4               # powiaty do 45 km
LIMIT_DALSZY = 2               # reszta promienia

REGION_NAZWA = {3: "Dolnośląskie", 15: "Kujawsko-pom", 8: "Lubelskie", 9: "Lubuskie",
                7: "Łódzkie", 4: "Małopolskie", 2: "Mazowieckie", 12: "Opolskie",
                17: "Podkarpackie", 18: "Podlaskie", 5: "Pomorskie", 6: "Śląskie",
                13: "Świętokrzyskie", 14: "Warm-mazurskie", 1: "Wielkopolskie",
                11: "Zachodniopom"}

# Oba to wapno tlenkowe 90% CaO — w jednej miejscowości biłyby się w tym samym wyszukiwaniu.
ROZDZIEL = ({"agrobielik-90", "oxyfertil-90"},)

# Kreda pastewna stoi w kategorii 4368 (Nawozy), a rynek paszowy siedzi w 765 i 761.
# Pakiet obejmuje WYŁĄCZNIE 4368, więc przeniesienie kategorii jest niewykonalne — te sloty
# zmieniają produkt. Zamienniki wg zmierzonego zwrotu na ogłoszenie (28.08).
ZAMIANA_PRODUKTU = {"kreda-pastewna": ["weglanowe-odmiana-04", "kreda-nawozowa-granulowana",
                                       "agrobielik-70-gleba"]}

# Korekta regionalna (28.08, decyzja Janka). Rotacja wyżej dobiera zamiennik wg zwrotu na CAŁEJ
# siatce, a ten rozkłada się inaczej niż zwrot w promieniu magazynów. Dwa niezależne pomiary
# w naszych trzech województwach mówią zgodnie:
#   • zwrot własny w pierścieniu ≤200 km: oxyfertil-90 0,50 · weglanowe-odmiana-04 0,36 ·
#     kreda-nawozowa-granulowana 0,22 · agrobielik-70-gleba 0,15 · kreda-pastewna 0,00
#   • podaż konkurencji (snapshot 28.08, kat. 4368, MŁP+PDK+ŚWK): granulowane 94 oferty,
#     z magnezem 64, kreda i węglanowe sypkie 28, tlenkowe 27, pastewna 1
# Tam, gdzie oba sygnały idą w tę samą stronę, korygujemy. Bochnia zostaje przy kredzie
# granulowanej ŚWIADOMIE: tam sygnały są sprzeczne (nasz zwrot mówi „nieźle", gęstość rynku
# „tłok"), a własny pomiar jest mocniejszym dowodem niż cudza podaż — nie uśredniamy.
# Oxyfertil wchodzi tylko do Sandomierza, bo to jedyne z ośmiu miast bez Agrobielika 90 obok,
# a ROZDZIEL trzyma oba tlenkowe 90% z dala od siebie.
KOREKTA_REGIONALNA = {("Sandomierz", "kreda-nawozowa-granulowana"): "oxyfertil-90",
                      ("Dąbrowa Tarnowska", "kreda-nawozowa-granulowana"): "weglanowe-odmiana-04"}


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(h))


def dystans(miasto):
    p = (float(miasto["latitude"]), float(miasto["longitude"]))
    return min(km(p, NIEDOMICE), km(p, RADGOSZCZ))


def wczytaj():
    posted = json.load(open(os.path.join(D, "posted.json"), encoding="utf-8"))
    plan = {(r["siatka"], r["city"]): r
            for r in json.load(open(os.path.join(D, "plan-ogloszen.json"), encoding="utf-8"))}
    kand = json.load(open(os.path.join(D, "miasta-kandydaci.json"), encoding="utf-8"))
    rynek = json.load(open(os.path.join(D, "miasta-rynek.json"), encoding="utf-8"))
    hist = json.load(open(os.path.join(D, "statystyki.json"), encoding="utf-8"))
    return posted, plan, kand, rynek, hist[-1]["per_ogloszenie"]


def main():
    posted, plan, kand, rynek, stat = wczytaj()

    # Przydział jest ZACHŁANNY i liczony od stanu rejestru, więc przeliczenie w trakcie serii
    # daje inny wynik niż na starcie: ogłoszenia już przełożone zajmują sloty i zwalniają
    # swoje stare miasta. Zmierzone 28.08 — przeliczenie po pilocie na 3 sztukach przetasowało
    # 56 z 65 pozycji i zgubiło 3. Plan raz zatwierdzony poprawiamy punktowo w pliku projektu,
    # nie regeneracją.
    w_locie = sum(1 for v in posted.values() if v.get("przelozone"))
    if w_locie and "--mimo-serii" not in sys.argv:
        sys.exit(f"STOP: {w_locie} ogłoszeń jest już przełożonych — przeliczenie da inny przydział "
                 f"niż zatwierdzony projekt.\nPoprawki nanoś punktowo na "
                 f"data/olx/przelozenie-*.json. Świadome przeliczenie od zera: --mimo-serii")
    po_nazwie = {c["name"]: c for c in kand}
    zajete_miasta = {v["city"] for v in posted.values()}

    # 1. Co idzie do przełożenia
    do_przelozenia, zostaje = [], defaultdict(int)
    for klucz, v in posted.items():
        siatka = klucz[len("agria-"):].rsplit("-", 1)[0]
        m = po_nazwie.get(v["city"])
        if not m:
            continue
        d = dystans(m)
        od, tel = stat.get(str(v["advert_id"]), [0, 0])
        rec = dict(klucz=klucz, advert_id=v["advert_id"], siatka=siatka, sku=v["sku"],
                   miasto=v["city"], km=round(d), odslony=od, telefony=tel)
        if d > PROG_DO_PRZELOZENIA:
            do_przelozenia.append(rec)
        else:
            zajete_miasta.add(v["city"])
            zostaje[v["city"]] += 1

    # 2. Miejsca docelowe: powiaty w promieniu, najbliżej magazynów najpierw.
    #    Powiat dąbrowski i tarnowski to teren własny — idą przed wszystkim innym.
    #    W obrębie powiatu wybieramy nie najbliższą wieś, tylko miejscowość z realnym rynkiem:
    #    liczba ogłoszeń wapniarskich, jakie rynek tam wystawia, jest jedynym proxy popytu,
    #    jakie mamy. Gmina z zerowym rynkiem daje zerowy ruch — zmierzone na Gorzycach,
    #    Goździe i Przysusze (razem 7 ogłoszeń, 23 odsłony, 0 kontaktów).
    cele = []
    for c in kand:
        if c["name"] in zajete_miasta:
            continue
        d = dystans(c)
        if d > PROG_DOCELOWY:
            continue
        wlasny = c["county"] in LIMIT_POWIATU
        r = rynek.get(f"{c['name']}|{REGION_NAZWA.get(c['region_id'])}", 0)
        siedziba = c["name"] == c.get("municipality")
        cele.append(dict(c, km=round(d), wlasny=wlasny, rynek=r,
                         wymagane=WYMAGANE.get(c["name"], 0),
                         ranga=r * 10 + (3 if siedziba else 0) - d / 40))
    cele.sort(key=lambda c: (-c["wymagane"], not c["wlasny"], -c["ranga"]))

    # 3. Przydział zachłanny. Kolejność ogłoszeń: najsłabsze i najdalsze idą pierwsze,
    #    bo dostają najbliższe wolne miejsca.
    do_przelozenia.sort(key=lambda r: (r["telefony"], -r["km"]))
    w_miescie = defaultdict(list)
    na_powiat = defaultdict(int)
    przydzial = []
    for r in do_przelozenia:
        wariant = r["siatka"]
        nowy_produkt = None
        if wariant in ZAMIANA_PRODUKTU:
            # rotujemy zamienniki, żeby nie postawić ośmiu takich samych
            i = sum(1 for p in przydzial if p["stary_wariant"] == wariant)
            nowy_produkt = ZAMIANA_PRODUKTU[wariant][i % len(ZAMIANA_PRODUKTU[wariant])]
            wariant = nowy_produkt
        cel = None
        for c in cele:
            n = c["name"]
            if len(w_miescie[n]) >= max(MAKS_NA_MIEJSCOWOSC, c["wymagane"]):
                continue
            if wariant in w_miescie[n]:          # ten sam wariant dwa razy w mieście = kanibalizacja
                continue
            if any(wariant in para and (para - {wariant}).pop() in w_miescie[n]
                   for para in ROZDZIEL):
                continue
            # rozsyp po powiatach: najpierw jedno na powiat, dokładamy dopiero w drugim przebiegu
            limit = LIMIT_POWIATU.get(c["county"], LIMIT_BLISKI if c["km"] <= 45 else LIMIT_DALSZY)
            if na_powiat[c["county"]] >= limit:
                continue
            cel = c
            break
        if not cel:
            przydzial.append(dict(r, nowe_miasto=None, nowy_wariant=None,
                                  stary_wariant=r["siatka"], uwaga="brak wolnego miejsca"))
            continue
        w_miescie[cel["name"]].append(wariant)
        na_powiat[cel["county"]] += 1
        przydzial.append(dict(r, stary_wariant=r["siatka"], nowe_miasto=cel["name"],
                              nowy_city_id=cel["id"], nowy_powiat=cel["county"],
                              nowy_km=cel["km"], nowy_wariant=nowy_produkt))

    # 3b. Korekta regionalna — punktowa podmiana zamiennika, z tymi samymi regułami co przydział.
    #     Świadomie NIE przez zmianę rotacji: tamta przetasowałaby cały przydział serii B,
    #     a zmiana ma dotknąć dokładnie dwóch slotów.
    for p in przydzial:
        nowy = KOREKTA_REGIONALNA.get((p.get("nowe_miasto"), p.get("nowy_wariant")))
        if not nowy:
            continue
        stoi = w_miescie[p["nowe_miasto"]]
        kolizja = nowy in stoi or any(nowy in para and (para - {nowy}).pop() in stoi
                                      for para in ROZDZIEL)
        if kolizja:
            print(f"UWAGA: korekta {p['nowe_miasto']} → {nowy} pominięta, koliduje z {stoi}")
            continue
        stoi[stoi.index(p["nowy_wariant"])] = nowy
        p["nowy_wariant"] = nowy
        p["korekta"] = "regionalna 28.08"

    # 4. Raport
    print(f"do przełożenia (dalej niż {PROG_DO_PRZELOZENIA} km od magazynów): {len(do_przelozenia)} ogłoszeń")
    print(f"miejsc docelowych w promieniu {PROG_DOCELOWY} km: {len(cele)} miejscowości\n")
    print(f"{'stare miejsce':<22}{'km':>4}  →  {'nowe miejsce':<22}{'km':>4} {'powiat':<20}{'produkt'}")
    for p in sorted(przydzial, key=lambda x: (x["nowe_miasto"] is None, x.get("nowy_km", 999))):
        if not p["nowe_miasto"]:
            print(f"{p['miasto']:<22}{p['km']:>4}  →  {'— BRAK MIEJSCA —':<48}{p['stary_wariant']}")
            continue
        prod = p["stary_wariant"] if not p["nowy_wariant"] else f"{p['stary_wariant']} → {p['nowy_wariant']}"
        print(f"{p['miasto']:<22}{p['km']:>4}  →  {p['nowe_miasto']:<22}{p['nowy_km']:>4} "
              f"{p['nowy_powiat']:<20}{prod}")

    print(f"\n=== obsadzenie powiatów po zmianie ===")
    for pow_, n in sorted(na_powiat.items(), key=lambda kv: -kv[1]):
        print(f"   {pow_:<24}{n:>3} nowych ogłoszeń")
    zmiana_produktu = [p for p in przydzial if p["nowy_wariant"]]
    print(f"\nsama zmiana miejscowości: {len(przydzial)-len(zmiana_produktu)} ogłoszeń "
          f"(PUT, payload istnieje)")
    print(f"zmiana miejscowości I produktu: {len(zmiana_produktu)} ogłoszeń "
          f"(wymaga regeneracji payloadu przez build_adverts.py)")

    if "--zapisz" in sys.argv:
        sciezka = os.path.join(D, f"przelozenie-{time.strftime('%Y-%m-%d')}.json")
        json.dump(przydzial, open(sciezka, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"\n→ {os.path.relpath(sciezka)}")


if __name__ == "__main__":
    main()
