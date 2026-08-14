#!/usr/bin/env python3
"""Builder kampanii Google Ads dla AGRIA (CID 6742071446).

Buduje całą strukturę z docs/ads/SETUP_KAMPANII_2026-08.md w jednym przebiegu:
budżety -> kampanie -> kryteria (geo/język/wykluczenia) -> grupy -> słowa -> reklamy -> zasoby.

Użycie:
    python3 ads_build_campaigns.py --dry-run     # tylko waliduje i wypisuje ładunki
    python3 ads_build_campaigns.py               # wykonuje mutacje

Idempotencja: skrypt NIE sprawdza, czy zasoby już istnieją. Uruchomiony dwa razy
utworzy duplikaty. Przed drugim uruchomieniem skasuj to, co powstało za pierwszym.

Wersja API czytana z ~/secrets/google/ads-config.json (pole api_version) — nie hardkodować.
"""
import json, subprocess, sys, os, pathlib

HERE = pathlib.Path(__file__).parent
CALL = HERE / "ads_call.sh"
DRY = "--dry-run" in sys.argv

# ── Parametry kampanii ────────────────────────────────────────────────────────
# UWAGA: pole campaign.start_date NIE ISTNIEJE w API v25 (usunięte przez Google).
# Kampania startuje w momencie utworzenia. Datę startu kontrolujemy statusem.
GEO_PL     = "geoTargetConstants/2616"
LANG_PL    = "languageConstants/1030"
CPC_CEIL   = 2_000_000           # 2,00 zł — limit CPC przy Maksymalizacji kliknięć

# Landing /wapno-nawozowe/ NIE ISTNIEJE (301 -> /wapno-nawozowe-na-trawnik/).
# Grupy, które na niego kierują, powstają WSTRZYMANE. Po publikacji landingu:
#   przełączyć status na ENABLED (patrz --enable-pending na końcu pliku).
LP_NAWOZOWE_GOTOWY = True   # opublikowany 13.08, post ID 2757, noindex+follow

URL_GRANULOWANE = "https://agria.pl/wapno-granulowane/"
URL_NAWOZOWE    = "https://agria.pl/wapno-nawozowe/"
URL_HOME        = "https://agria.pl/"

# ── Wykluczenia ───────────────────────────────────────────────────────────────
# Poziom konta (lista współdzielona podpięta pod obie kampanie): uniwersalne śmieci.
NEG_GLOBALNE = """
praca oferty pracy zarobki sprzedam kupię używane
olx allegro ceneo leroy castorama obi bricomarche amazon
wikipedia definicja prezentacja referat
""".split()

# Poziom kampanii Rolnictwo: odsiew hobbysty i budowlanki detalicznej.
NEG_ROLNICTWO = """
trawnik ogród ogrodowy działka doniczka kwiaty
basen akwarium bielenie
budowlane malarska gaszone tynk zaprawa
kury drób pastewna
""".split() + ["rośliny doniczkowe", "5 kg", "10 kg", "do ścian", "bielenie drzew"]

# Wykluczenia brandowe w kampanii Rolnictwo — żeby ruch brandowy nie był
# przechwytywany po CPC rolniczym i nie fałszował oceny obu kampanii.
NEG_BRAND = ["agria", "agrobielik", "bielik", "oxyfertil", "ekograncali"]

# ── Struktura: kampanie i grupy ───────────────────────────────────────────────
STRUKTURA = [
    {
        "kampania": "AGRIA - Rolnictwo",
        "budzet_zl": 34,
        "negatywy": NEG_ROLNICTWO + NEG_BRAND,
        "grupy": [
            {
                "nazwa": "Wapno granulowane",
                "url": URL_GRANULOWANE,
                "sciezka": ["wapno", "granulowane"],
                "wstrzymana": False,
                "frazy": [
                    ("wapno granulowane", "PHRASE"), ("wapno granulowane", "EXACT"),
                    ("wapno nawozowe granulowane", "PHRASE"),
                    ("wapno granulowane luzem", "PHRASE"),
                    ("wapno granulowane big bag", "PHRASE"),
                    ("granulat wapniowy", "PHRASE"),
                    ("wapno węglanowe granulowane", "PHRASE"),
                    ("wapno tlenkowe granulowane", "PHRASE"),
                    ("kreda granulowana", "PHRASE"),
                ],
                "naglowki": [
                    "Wapno granulowane luzem", "Wapno granulowane – producent",
                    "Wapno nawozowe granulowane", "Granulat wapniowy dla rolnika",
                    "Wapno granulowane od 1989 r.", "Dostawa własną flotą 3–24 t",
                    "Luz, big-bag, worek 25 kg", "Zapytaj o ofertę – podaj tonaż",
                    "Atesty i karty produktowe", "Wapno granulowane Małopolska",
                    "Dwa magazyny, szybki załadunek", "Wapnowanie pożniwne – termin",
                    "Wapno pod orkę – dobierzemy", "Wycena dla gospodarstw",
                    "Wapno granulowane hurt",
                ],
                "opisy": [
                    "Producent wapna od 1989 r. Granulat luzem, w big-bagach i workach. Zapytaj o ofertę.",
                    "Własna flota 3–24 t i dwa magazyny – dowozimy na termin, także przy większych tonażach.",
                    "Karty produktowe, atesty OSChR, klasy normowe. Wiesz dokładnie, co wjeżdża na pole.",
                    "Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą. Gospodarstwa i hurtownie.",
                ],
            },
            {
                "nazwa": "Wapno nawozowe",
                "url": URL_NAWOZOWE,
                "sciezka": ["wapno", "nawozowe"],
                "wstrzymana": not LP_NAWOZOWE_GOTOWY,
                "frazy": [
                    ("wapno nawozowe", "PHRASE"), ("wapno nawozowe", "EXACT"),
                    ("wapno rolnicze", "PHRASE"), ("wapno do gleby", "PHRASE"),
                    ("wapno węglanowe", "PHRASE"), ("wapno tlenkowe", "PHRASE"),
                    ("wapno nawozowe luzem", "PHRASE"), ("wapno pod orkę", "PHRASE"),
                    ("wapno na pole", "PHRASE"), ("wapno do odkwaszania gleby", "PHRASE"),
                ],
                "naglowki": [
                    "Wapno nawozowe – producent", "Wapno nawozowe luzem 24 t",
                    "Wapno węglanowe i tlenkowe", "Wapno nawozowe dla rolnictwa",
                    "Odkwaszanie gleby – wapno", "Zapytaj o ofertę – podaj tonaż",
                    "Wapno nawozowe od 1989 r.", "Dostawa własną flotą",
                    "Atesty OSChR, karty techniczne", "Big-bag 1000 kg lub luzem",
                    "Wapno nawozowe Małopolska", "Agrobielik i Oxyfertil",
                    "Wapno pod rzepak i zboża", "Wycena dla gospodarstw",
                    "Wapno nawozowe hurt",
                ],
                "opisy": [
                    "Wapno tlenkowe i węglanowe prosto od producenta. Luz, big-bag, worek. Zapytaj o ofertę.",
                    "Dobierzemy typ wapna do Twojej gleby i terminu zabiegu. Doradztwo w cenie dostawy.",
                    "Własna flota 3–24 t, dwa magazyny, terminy dopasowane do prac polowych.",
                    "Karty produktowe i atesty dostępne na stronie. Parametry zgodne z rozporządzeniem.",
                ],
            },
            {
                "nazwa": "Wapno magnezowe i kreda",
                "url": URL_NAWOZOWE,
                "sciezka": ["wapno", "magnezowe"],
                "wstrzymana": not LP_NAWOZOWE_GOTOWY,
                "frazy": [
                    ("wapno magnezowe", "PHRASE"), ("wapno magnezowe", "EXACT"),
                    ("wapno z magnezem", "PHRASE"), ("wapno węglanowo-magnezowe", "PHRASE"),
                    ("wapno magnezowe granulowane", "PHRASE"),
                    ("dolomit nawozowy", "PHRASE"), ("kreda nawozowa", "PHRASE"),
                ],
                "naglowki": [
                    "Wapno magnezowe granulowane", "Wapno z magnezem – producent",
                    "Kreda nawozowa luzem", "Dolomit i wapno magnezowe",
                    "Magnez i wapń w jednym zabiegu", "Zapytaj o ofertę – podaj tonaż",
                    "Kreda nawozowa i pastewna", "Dostawa własną flotą 3–24 t",
                    "Wapno magnezowe od 1989 r.", "Atesty i karty produktowe",
                    "Big-bag 1000 kg lub luzem", "Wapno magnezowe Małopolska",
                    "Niedobór magnezu – uzupełnij", "Wycena dla gospodarstw",
                    "Kreda nawozowa hurt",
                ],
                "opisy": [
                    "Wapno magnezowe i kreda od producenta. Wapń i magnez w jednym zabiegu.",
                    "Luz 24 t, big-bag 1000 kg, worki. Dobór formy dostawy do wielkości gospodarstwa.",
                    "Karty produktowe z zawartością CaO i MgO. Atesty OSChR dla każdej partii.",
                    "Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą własną flotą.",
                ],
            },
        ],
    },
    {
        "kampania": "AGRIA - Marka",
        "budzet_zl": 6,
        "negatywy": [],
        "grupy": [
            {
                "nazwa": "Brand",
                "url": URL_HOME,
                "sciezka": ["oferta"],
                "wstrzymana": False,
                "frazy": [
                    ("agria", "EXACT"), ("agria wapno", "PHRASE"), ("agria tarnów", "PHRASE"),
                    ("agrobielik", "EXACT"), ("agrobielik", "PHRASE"),
                    ("bielik wapno", "PHRASE"), ("oxyfertil", "PHRASE"),
                    ("ekograncali", "PHRASE"),
                ],
                "naglowki": [
                    "AGRIA – wapno nawozowe", "AGRIA Sp. z o.o. Tarnów",
                    "Agrobielik – wapno tlenkowe", "Bielik – wapno hydratyzowane",
                    "Oxyfertil w ofercie AGRIA", "Producent od 1989 roku",
                    "Wapno i surowce wapniowe", "Zapytaj o ofertę",
                    "Oficjalna strona AGRIA", "EkoGranCali – granulat",
                    "Trzy pokolenia, 37 lat", "Dwa magazyny w Małopolsce",
                ],
                "opisy": [
                    "Oficjalna strona AGRIA Sp. z o.o. Wapno nawozowe, budowlane i surowce od 1989 r.",
                    "Agrobielik, Bielik, Oxyfertil, EkoGranCali – pełna oferta prosto od producenta.",
                    "Rodzinna firma z Tarnowa, trzy pokolenia w branży wapna. Własna flota i magazyny.",
                    "Karty produktowe, atesty i kalkulator wapnowania dostępne na stronie.",
                ],
            },
        ],
    },
]

# ── Rozszerzenia ──────────────────────────────────────────────────────────────
SITELINKI = [
    ("Kalkulator wapnowania", "Policz dawkę na hektar", "Bezpłatne narzędzie online",
     "https://agria.pl/kalkulator-wapnowania/"),
    ("Karty produktowe", "Parametry i atesty PDF", "Wszystko do pobrania",
     "https://agria.pl/do-pobrania/"),
    ("Wapnowanie gleby", "Poradnik: kiedy i ile", "Terminy i dawki wapna",
     "https://agria.pl/wapnowanie-gleby/"),
    ("Kontakt", "Zapytaj o ofertę", "Telefon i formularz",
     "https://agria.pl/kontakt/"),
]

OBJASNIENIA = ["Producent od 1989 roku", "Własna flota 3–24 t", "Dwa magazyny w Małopolsce",
               "Atesty OSChR", "Luz, big-bag, worki", "Doradztwo w doborze wapna"]

# Rozszerzenie połączeń z harmonogramem — telefon dzwoni tylko w godzinach pracy.
# UWAGA: godziny na stronie to 8:00-16:00, Janek pamięta 7-15. DO POTWIERDZENIA
# z Pawłem przed uruchomieniem; poniżej wersja ze strony.
TELEFON = "+48604428782"
GODZINY = [("MONDAY", 8, 16), ("TUESDAY", 8, 16), ("WEDNESDAY", 8, 16),
           ("THURSDAY", 8, 16), ("FRIDAY", 8, 16)]

# ── Walidacja limitów Google ──────────────────────────────────────────────────
def waliduj():
    bledy = []
    for k in STRUKTURA:
        for g in k["grupy"]:
            for h in g["naglowki"]:
                if len(h) > 30:
                    bledy.append(f"[{g['nazwa']}] nagłówek {len(h)} zn.: {h}")
            for d in g["opisy"]:
                if len(d) > 90:
                    bledy.append(f"[{g['nazwa']}] opis {len(d)} zn.: {d}")
            if len(g["naglowki"]) > 15:
                bledy.append(f"[{g['nazwa']}] {len(g['naglowki'])} nagłówków (max 15)")
            if not 2 <= len(g["opisy"]) <= 4:
                bledy.append(f"[{g['nazwa']}] {len(g['opisy'])} opisów (wymagane 2–4)")
            for p in g["sciezka"]:
                if len(p) > 15:
                    bledy.append(f"[{g['nazwa']}] ścieżka >15 zn.: {p}")
    for t, d1, d2, _ in SITELINKI:
        if len(t) > 25: bledy.append(f"sitelink tytuł >25: {t}")
        if len(d1) > 35 or len(d2) > 35: bledy.append(f"sitelink opis >35: {t}")
    for o in OBJASNIENIA:
        if len(o) > 25: bledy.append(f"objaśnienie >25 zn.: {o}")
    return bledy


def call(path, body):
    """Wywołuje ads_call.sh; w trybie dry-run tylko wypisuje ładunek."""
    js = json.dumps(body, ensure_ascii=False, indent=1)
    if DRY:
        print(f"\n--- POST {path} ---\n{js}")
        typ = path.strip("/").split(":")[0]
        return {"results": [{"resourceName": f"DRY/{typ}/{i}"}
                            for i in range(len(body.get("operations", [{}])))]}
    tmp = f"/tmp/ads_payload_{abs(hash(js))}.json"
    with open(tmp, "w") as f:
        f.write(js)
    out = subprocess.run(["bash", str(CALL), path, "POST", tmp],
                         capture_output=True, text=True).stdout
    os.unlink(tmp)
    try:
        r = json.loads(out)
    except json.JSONDecodeError:
        sys.exit(f"BŁĄD odpowiedzi API dla {path}:\n{out}")
    if "error" in r:
        sys.exit(f"BŁĄD API {path}:\n{json.dumps(r['error'], ensure_ascii=False, indent=2)}")
    return r


def rn(resp, i=0):
    return resp["results"][i]["resourceName"]


def gaql(query):
    """Odczyt przez GoogleAdsService — do sprawdzania, co już istnieje."""
    if DRY:
        return []
    tmp = f"/tmp/ads_q_{abs(hash(query))}.json"
    with open(tmp, "w") as f:
        json.dump({"query": query}, f)
    out = subprocess.run(["bash", str(CALL), "/googleAds:searchStream", "POST", tmp],
                         capture_output=True, text=True).stdout
    os.unlink(tmp)
    try:
        d = json.loads(out)
    except json.JSONDecodeError:
        return []
    if isinstance(d, dict) and "error" in d:
        return []
    return [r for chunk in d for r in chunk.get("results", [])]


def istnieje(typ, nazwa):
    """Zwraca resourceName istniejącego zasobu o tej nazwie albo None.
    Skrypt jest przez to idempotentny — po błędzie w połowie można go odpalić ponownie."""
    pola = {"campaign_budget": "campaign_budget", "shared_set": "shared_set",
            "campaign": "campaign", "ad_group": "ad_group"}[typ]
    esc = nazwa.replace("'", "\\'")
    rows = gaql(f"SELECT {pola}.resource_name, {pola}.name FROM {typ} "
                f"WHERE {pola}.name = '{esc}'")
    key = "".join(w.capitalize() if i else w for i, w in enumerate(pola.split("_")))
    for r in rows:
        if key in r:
            return r[key]["resourceName"]
    return None


def main():
    bledy = waliduj()
    if bledy:
        print("WALIDACJA NIE PRZESZŁA:")
        for b in bledy:
            print("  -", b)
        sys.exit(1)
    print(f"Walidacja limitów Google: OK ({sum(len(g['naglowki']) for k in STRUKTURA for g in k['grupy'])} nagłówków, "
          f"{sum(len(g['frazy']) for k in STRUKTURA for g in k['grupy'])} słów kluczowych)")
    if DRY:
        print("TRYB DRY-RUN — nic nie zostanie wysłane.\n")

    # 1. Lista wykluczeń współdzielona (poziom konta)
    shared_rn = istnieje("shared_set", "AGRIA - wykluczenia globalne")
    if shared_rn:
        print(f"  = lista wykluczeń już istnieje, używam: {shared_rn}")
    else:
        shared_rn = rn(call("/sharedSets:mutate", {"operations": [{"create": {
            "name": "AGRIA - wykluczenia globalne", "type": "NEGATIVE_KEYWORDS"}}]}))
        call("/sharedCriteria:mutate", {"operations": [
            {"create": {"sharedSet": shared_rn,
                        "keyword": {"text": t, "matchType": "PHRASE"}}}
            for t in NEG_GLOBALNE]})

    # 2. Budżety
    bud_rns, do_utworzenia = [], []
    for k in STRUKTURA:
        nazwa = f"{k['kampania']} (dzienny)"
        r = istnieje("campaign_budget", nazwa)
        if r:
            print(f"  = budżet już istnieje, używam: {nazwa}")
        else:
            do_utworzenia.append(k)
        bud_rns.append(r)
    if do_utworzenia:
        nowe = call("/campaignBudgets:mutate", {"operations": [
            {"create": {"name": f"{k['kampania']} (dzienny)",
                        "amountMicros": str(k["budzet_zl"] * 1_000_000),
                        "deliveryMethod": "STANDARD", "explicitlyShared": False}}
            for k in do_utworzenia]})
        it = iter(range(len(do_utworzenia)))
        for i, r in enumerate(bud_rns):
            if r is None:
                bud_rns[i] = rn(nowe, next(it))

    class _Bud:
        def __init__(self, lst): self.lst = lst
    bud = _Bud(bud_rns)

    for idx, k in enumerate(STRUKTURA):
        # 3. Kampania
        camp = call("/campaigns:mutate", {"operations": [{"create": {
            "name": k["kampania"],
            "status": "ENABLED",
            "advertisingChannelType": "SEARCH",
            # Wymagane od 2025 (unijne rozporządzenie o przejrzystości reklamy politycznej).
            # AGRIA sprzedaje wapno, nie prowadzi reklamy politycznej.
            "containsEuPoliticalAdvertising": "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
            "campaignBudget": bud.lst[idx] if not DRY else f"DRY/budget/{idx}",
            "targetSpend": {"cpcBidCeilingMicros": str(CPC_CEIL)},
            "networkSettings": {
                "targetGoogleSearch": True,
                "targetSearchNetwork": False,
                "targetContentNetwork": False,
                "targetPartnerSearchNetwork": False},
            "geoTargetTypeSetting": {
                "positiveGeoTargetType": "PRESENCE",
                "negativeGeoTargetType": "PRESENCE"},
        }}]})
        camp_rn = rn(camp)

        # 4. Kryteria kampanii: geo, język, lista wykluczeń, wykluczenia własne
        krit = [
            {"create": {"campaign": camp_rn, "location": {"geoTargetConstant": GEO_PL}}},
            {"create": {"campaign": camp_rn, "language": {"languageConstant": LANG_PL}}},
        ] + [
            {"create": {"campaign": camp_rn, "negative": True,
                        "keyword": {"text": t, "matchType": "PHRASE"}}}
            for t in k["negatywy"]
        ]
        call("/campaignCriteria:mutate", {"operations": krit})
        call("/campaignSharedSets:mutate", {"operations": [{"create": {
            "campaign": camp_rn, "sharedSet": shared_rn}}]})

        # 5. Grupy reklam
        ag = call("/adGroups:mutate", {"operations": [
            {"create": {"name": g["nazwa"], "campaign": camp_rn,
                        "status": "PAUSED" if g["wstrzymana"] else "ENABLED",
                        "type": "SEARCH_STANDARD"}}
            for g in k["grupy"]]})

        for gi, g in enumerate(k["grupy"]):
            ag_rn = rn(ag, gi)
            # 6. Słowa kluczowe
            call("/adGroupCriteria:mutate", {"operations": [
                {"create": {"adGroup": ag_rn, "status": "ENABLED",
                            "keyword": {"text": t, "matchType": m}}}
                for t, m in g["frazy"]]})
            # 7. Reklama elastyczna
            rsa = {"headlines": [{"text": h} for h in g["naglowki"]],
                   "descriptions": [{"text": d} for d in g["opisy"]],
                   "path1": g["sciezka"][0]}
            if len(g["sciezka"]) > 1:
                rsa["path2"] = g["sciezka"][1]
            call("/adGroupAds:mutate", {"operations": [{"create": {
                "adGroup": ag_rn, "status": "ENABLED",
                "ad": {"finalUrls": [g["url"]], "responsiveSearchAd": rsa}}}]})

    # 8. Zasoby na poziomie konta: sitelinki, objaśnienia, połączenia
    # UWAGA: samo utworzenie zasobu NIE wystarcza — bez wpisu w customerAssets
    # zasób istnieje, ale nie wyświetla się w żadnej reklamie. Błąd z 13.08.
    zasoby = call("/assets:mutate", {"operations":
        [{"create": {"sitelinkAsset": {"linkText": t, "description1": d1, "description2": d2},
                     "finalUrls": [u]}} for t, d1, d2, u in SITELINKI] +
        [{"create": {"calloutAsset": {"calloutText": o}}} for o in OBJASNIENIA] +
        [{"create": {"callAsset": {
            "countryCode": "PL", "phoneNumber": TELEFON,
            "callConversionReportingState": "USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION",
            "adScheduleTargets": [
                {"dayOfWeek": d, "startHour": s, "startMinute": "ZERO",
                 "endHour": e, "endMinute": "ZERO"} for d, s, e in GODZINY]}}}]
    })

    # 8b. Powiązanie zasobów z kontem — bez tego nie działają
    typy = ["SITELINK"] * len(SITELINKI) + ["CALLOUT"] * len(OBJASNIENIA) + ["CALL"]
    call("/customerAssets:mutate", {"operations": [
        {"create": {"asset": rn(zasoby, i), "fieldType": t, "status": "ENABLED"}}
        for i, t in enumerate(typy)]})

    print("\nGOTOWE." if not DRY else "\nDRY-RUN zakończony — nic nie wysłano.")
    print("Po publikacji /wapno-nawozowe/ przełącz grupy 'Wapno nawozowe' i "
          "'Wapno magnezowe i kreda' na ENABLED (LP_NAWOZOWE_GOTOWY = True).")


if __name__ == "__main__":
    main()
