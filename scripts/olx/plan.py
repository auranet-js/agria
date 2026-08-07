#!/usr/bin/env python3
"""Plan 100 ogłoszeń OLX dla AGRII — produkty, tytuły pod intencję, siatka miast.

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
- Miasta dobrane pod segment: stawy do rejonów karpiowych, paszarstwo do rejonów
  drobiarskich, odkwaszanie do rejonów o intensywnej produkcji roślinnej.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = os.path.join(HERE, "..", "..", "data", "olx", "product-specs.json")
OUT = os.path.join(HERE, "..", "..", "data", "olx", "plan-ogloszen.json")
CITIES = os.path.join(HERE, "..", "..", "data", "olx", "cities-all.json")

CAT_NAWOZY = 4368

# Pule miast per segment: (nazwa, region_id). Województwo jest częścią klucza, bo w bazie OLX
# siedzi 53 tys. miejscowości i sama nazwa trafia w wieś-homonim (Konin jest też na Śląsku,
# Zamość w Kujawsko-pomorskiem). Bez tego 11 z 56 miast lądowało w złym regionie.
#
# Rejony karpiowe, drobiarskie i intensywnej produkcji roślinnej — lokalizacja ogłoszenia steruje
# widocznością w wyszukiwaniu lokalnym, nie zasięgiem dostawy (w tej kategorii wszyscy
# kwotują loco + transport osobno).
REGIONY = {"dolnoslaskie": 3, "kujawsko": 15, "lubelskie": 8, "lubuskie": 9, "lodzkie": 7,
           "malopolskie": 4, "mazowieckie": 2, "opolskie": 12, "podkarpackie": 17, "podlaskie": 18,
           "pomorskie": 5, "slaskie": 6, "swietokrzyskie": 13, "warminsko": 14,
           "wielkopolskie": 1, "zachodniopomorskie": 11}
R = REGIONY

POOLS = {
    "stawy": [("Zator", R["malopolskie"]), ("Oświęcim", R["malopolskie"]), ("Milicz", R["dolnoslaskie"]),
              ("Krotoszyn", R["wielkopolskie"]), ("Rawicz", R["wielkopolskie"]),
              ("Piotrków Trybunalski", R["lodzkie"]), ("Sieradz", R["lodzkie"]),
              ("Lubartów", R["lubelskie"]), ("Chełm", R["lubelskie"]), ("Przemyśl", R["podkarpackie"]),
              ("Rzeszów", R["podkarpackie"]), ("Olsztyn", R["warminsko"]), ("Ostróda", R["warminsko"]),
              ("Gostynin", R["mazowieckie"])],
    "gleby_ciezkie": [("Tarnów", R["malopolskie"]), ("Kielce", R["swietokrzyskie"]),
                      ("Sandomierz", R["swietokrzyskie"]), ("Nowy Sącz", R["malopolskie"]),
                      ("Krosno", R["podkarpackie"]), ("Jarosław", R["podkarpackie"]),
                      ("Zamość", R["lubelskie"]), ("Lublin", R["lubelskie"]), ("Puławy", R["lubelskie"]),
                      ("Radom", R["mazowieckie"]), ("Bochnia", R["malopolskie"]),
                      ("Dębica", R["podkarpackie"])],
    "wielkopolska": [("Gniezno", R["wielkopolskie"]), ("Września", R["wielkopolskie"]),
                     ("Inowrocław", R["kujawsko"]), ("Włocławek", R["kujawsko"]),
                     ("Konin", R["wielkopolskie"]), ("Kalisz", R["wielkopolskie"]),
                     ("Leszno", R["wielkopolskie"]), ("Piła", R["wielkopolskie"]),
                     ("Środa Wielkopolska", R["wielkopolskie"]), ("Koło", R["wielkopolskie"]),
                     ("Turek", R["wielkopolskie"]), ("Żnin", R["kujawsko"])],
    "mazowsze": [("Płock", R["mazowieckie"]), ("Siedlce", R["mazowieckie"]),
                 ("Ostrołęka", R["mazowieckie"]), ("Łomża", R["podlaskie"]),
                 ("Białystok", R["podlaskie"]), ("Mińsk Mazowiecki", R["mazowieckie"]),
                 ("Sokołów Podlaski", R["mazowieckie"]), ("Węgrów", R["mazowieckie"]),
                 ("Ciechanów", R["mazowieckie"]), ("Grajewo", R["podlaskie"])],
    "poludnie_zachod": [("Opole", R["opolskie"]), ("Kędzierzyn-Koźle", R["opolskie"]),
                        ("Nysa", R["opolskie"]), ("Legnica", R["dolnoslaskie"]),
                        ("Częstochowa", R["slaskie"]), ("Racibórz", R["slaskie"]),
                        ("Głubczyce", R["opolskie"]), ("Strzelin", R["dolnoslaskie"]),
                        ("Oleśnica", R["dolnoslaskie"]), ("Brzeg", R["opolskie"])],
    "paszarstwo": [("Białystok", R["podlaskie"]), ("Łomża", R["podlaskie"]),
                   ("Grajewo", R["podlaskie"]), ("Ostrołęka", R["mazowieckie"]),
                   ("Kalisz", R["wielkopolskie"]), ("Rawicz", R["wielkopolskie"])],
}

# 10 pozycji × przypisana liczba miast = 100 ogłoszeń.
# Ceny: netto, loco magazyn (CENNIK_PAWEL_2026-08-07.md). W tytule podajemy jednostkę.
PRODUKTY = [
    {
        "wc_id": 310, "sku": "AGR-001", "karta": "agrobielik-70",
        "tytul": "Wapno do stawu — tlenkowe palone 70% CaO, atest, od 220 zł/t",
        "intencja": "rybactwo — pH wody, mineralizacja mułu",
        "cena_pole": 220, "cena_opis": "od 220 zł/t netto luzem (całopojazdowo), 400 zł/t w big-bag",
        "pule": ["stawy"], "ile": 14,
        "uwaga": "wzorzec potwierdzony danymi konta: 94 odsłony telefonu = 45% kontaktów",
    },
    {
        "wc_id": 310, "sku": "AGR-001", "karta": "agrobielik-70",
        "tytul": "Odkwaszanie gleb ciężkich — wapno tlenkowe 70% CaO, od 220 zł/t",
        "intencja": "rolnictwo — szybkie podniesienie pH gleb średnich i ciężkich",
        "cena_pole": 220, "cena_opis": "od 220 zł/t netto luzem (całopojazdowo), 400 zł/t w big-bag",
        "pule": ["gleby_ciezkie"], "ile": 12,
    },
    {
        "wc_id": 311, "sku": "AGR-002", "karta": "agrobielik-90",
        "tytul": "Wapno tlenkowe 90% CaO — frakcja 0–3 i 2–8 mm, od 750 zł/t",
        "intencja": "rolnictwo — najwyższa koncentracja CaO, mniejsza dawka na hektar",
        "cena_pole": 750, "cena_opis": "0–3 mm: 750 zł/t luz, 850 zł/t big-bag · 2–8 mm: 850 / 940 zł/t",
        "pule": ["gleby_ciezkie", "wielkopolska"], "ile": 10,
        "uwaga": "w tej frakcji na OLX brak porównywalnej oferty",
    },
    {
        "wc_id": 312, "sku": "AGR-003", "karta": "oxyfertil-90",
        "tytul": "Oxyfertil 90 — wapno tlenkowe 90% CaO w big-bag, od 790 zł/t",
        "intencja": "rolnictwo — dostawa od 1 tony, bez całopojazdowego minimum",
        "cena_pole": 790, "cena_opis": "790 zł/t netto, big-bag od 1 tony",
        "pule": ["wielkopolska", "mazowsze"], "ile": 8,
    },
    {
        "wc_id": 314, "sku": "AGR-008", "karta": "weglanowe-granulowane",
        "tytul": "Wapno granulowane pod rzepak i zboża — wysiew rozsiewaczem, od 350 zł/t",
        "intencja": "rolnictwo — wysiew własnym rozsiewaczem, bez usługi wapnowania",
        "cena_pole": 350, "cena_opis": "350 zł/t big-bag od 1 t · 380 zł/t w workach 25 kg",
        "pule": ["wielkopolska", "mazowsze"], "ile": 12,
    },
    {
        "wc_id": 317, "sku": "AGR-011", "karta": "weglanowe-magnez-granulowane",
        "tytul": "Wapno granulowane z magnezem — uzupełnienie MgO, od 370 zł/t",
        "intencja": "rolnictwo — niedobory magnezu, gleby lekkie",
        "cena_pole": 370, "cena_opis": "370 zł/t big-bag od 1 t · 410 zł/t w workach 25 kg",
        "pule": ["wielkopolska", "poludnie_zachod"], "ile": 10,
    },
    {
        "wc_id": 306, "sku": "AGR-014", "karta": "kreda-nawozowa-sypka",
        "tytul": "Kreda nawozowa luzem — odkwaszanie całopojazdowe, od 125 zł/t",
        "intencja": "rolnictwo — duże areały, dostawa 24 t",
        "cena_pole": 125, "cena_opis": "125 zł/t netto luzem, dostawa całopojazdowa 24 t",
        "pule": ["gleby_ciezkie", "mazowsze"], "ile": 10,
    },
    {
        "wc_id": 305, "sku": "AGR-013", "karta": "kreda-nawozowa-granulowana",
        "tytul": "Kreda nawozowa granulowana — big-bag od 1 t, od 410 zł/t",
        "intencja": "rolnictwo — mniejsze gospodarstwa, wysiew rozsiewaczem",
        "cena_pole": 410, "cena_opis": "410 zł/t big-bag od 1 t · 490 zł/t w workach 25 kg",
        "pule": ["poludnie_zachod", "wielkopolska"], "ile": 8,
    },
    {
        "wc_id": 315, "sku": "AGR-006", "karta": "weglanowe-odmiana-04",
        "tytul": "Wapno węglanowe odm. 04 luzem — 57 zł/t netto loco, dostawa 24 t",
        "intencja": "rolnictwo — najniższy koszt odkwaszania na hektar",
        "cena_pole": 57, "cena_opis": "57 zł/t netto loco magazyn, dostawa całopojazdowa 24 t",
        "pule": ["mazowsze", "poludnie_zachod"], "ile": 10,
        "uwaga": "cena w parytecie z kopalnią Morawica (57,40 zł/t netto loco)",
    },
    {
        "wc_id": 307, "sku": "AGR-015", "karta": "kreda-pastewna",
        "tytul": "Kreda pastewna dla bydła i drobiu — wapń w paszy, od 190 zł/t",
        "intencja": "paszarstwo — suplementacja wapnia",
        "cena_pole": 190, "cena_opis": "190 zł/t netto luzem · 610 zł/t w workach 30 kg",
        "pule": ["paszarstwo"], "ile": 6,
    },
]


def fetch_cities():
    """Ściąga pełną listę miast z Partner API. 53 tys. rekordów / 7,8 MB — poza repo."""
    import subprocess
    helper = os.path.expanduser("~/bin/olx-agria")
    out, offset = [], 0
    while True:
        page = json.loads(subprocess.run(
            [helper, "api", f"/partner/cities?limit=1000&offset={offset}"],
            capture_output=True, text=True, check=True).stdout)["data"]
        out += page
        if len(page) < 1000:
            break
        offset += 1000
    os.makedirs(os.path.dirname(CITIES), exist_ok=True)
    json.dump(out, open(CITIES, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"pobrano {len(out)} miast → {os.path.relpath(CITIES)}")


def load_cities():
    if not os.path.exists(CITIES):
        print("brak lokalnej listy miast — pobieram z /partner/cities…")
        fetch_cities()
    idx = {}
    for c in json.load(open(CITIES, encoding="utf-8")):
        idx.setdefault(c["name"], []).append(c)
    return idx


def resolve(name, region_id, city_idx):
    """Wybiera właściwy wpis miasta: musi być we wskazanym województwie, a wśród kandydatów
    wygrywa siedziba gminy o tej samej nazwie (odsiewa wsie-homonimy w tym samym regionie)."""
    cand = [c for c in city_idx.get(name, []) if c["region_id"] == region_id]
    if not cand:
        return None
    cand.sort(key=lambda c: (c.get("municipality") != name, c.get("county") != name, c["id"]))
    return cand[0]


def pick_cities(pools, ile, city_idx, used):
    """Bierze miasta z pul po kolei, bez powtórzeń w obrębie jednego produktu."""
    out, seen = [], set()
    entries = []
    for p in pools:
        for e in POOLS[p]:
            if e not in entries:
                entries.append(e)
    for name, region_id in entries:
        if len(out) >= ile:
            break
        if name in seen:
            continue
        c = resolve(name, region_id, city_idx)
        if not c:
            print(f"    UWAGA: brak '{name}' w województwie {region_id} — pomijam")
            continue
        seen.add(name)
        out.append({"name": name, "city_id": c["id"], "region_id": c["region_id"]})
        used[name] = used.get(name, 0) + 1
    if len(out) < ile:
        print(f"    UWAGA: zebrano {len(out)} z {ile} miast — pule za małe")
    return out


if __name__ == "__main__":
    specs = {}
    for row in json.load(open(SPECS, encoding="utf-8")):
        specs[row["url"].rstrip("/").split("/")[-1]] = row

    city_idx = load_cities()
    used, plan = {}, []
    for p in PRODUKTY:
        spec = specs.get(p["karta"])
        if not spec:
            print(f"  UWAGA: brak specyfikacji dla '{p['karta']}' — sprawdź extract_specs.py")
        print(f"{p['tytul'][:62]:<64} {p['ile']:>3} miast")
        for c in pick_cities(p["pule"], p["ile"], city_idx, used):
            plan.append({
                "wc_id": p["wc_id"], "sku": p["sku"], "karta": p["karta"],
                "title": p["tytul"], "intencja": p["intencja"],
                "category_id": CAT_NAWOZY,
                "price": p["cena_pole"], "cena_opis": p["cena_opis"],
                "city": c["name"], "city_id": c["city_id"], "region_id": c["region_id"],
                "spec": (spec or {}).get("spec", {}),
                "uwaga": p.get("uwaga"),
            })

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(plan, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nrazem ogłoszeń: {len(plan)}")
    print(f"miast objętych: {len(used)}")
    top = sorted(used.items(), key=lambda x: -x[1])[:6]
    print(f"najwięcej ogłoszeń w jednym mieście: {top}")
    print(f"→ {os.path.relpath(OUT)}")
