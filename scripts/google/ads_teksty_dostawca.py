#!/usr/bin/env python3
"""Przepisanie reklam AGRIA pod pozycjonowanie 'dostawca całosamochodowy, nie sklep'.

Decyzja Janka 13.08: AGRIA ma być czytana jako dostawca surowca z dostawami
w całej Polsce, a nie sklep online z workami wapna.

Co robi:
  1. tworzy nowe reklamy RSA z przepisanymi tekstami
  2. usuwa stare reklamy (RSA są w większości pól niezmienialne — trzeba wymienić)
  3. dokłada wykluczenia odsiewające detal
  4. podmienia objaśnienie "Luz, big-bag, worki" na komunikat o skali dostaw

Użycie: python3 ads_teksty_dostawca.py [--dry-run]
"""
import json, subprocess, sys, os, pathlib

HERE = pathlib.Path(__file__).parent
CALL = HERE / "ads_call.sh"
DRY = "--dry-run" in sys.argv
CID = "6742071446"

# ── Nowe teksty ───────────────────────────────────────────────────────────────
GRUPY = {
    "Wapno granulowane": {
        "url": "https://agria.pl/wapno-granulowane/",
        "sciezka": ["wapno", "granulowane"],
        "naglowki": [
            "Wapno granulowane luzem", "Dostawy całosamochodowe",
            "Wapno granulowane – producent", "Dostawca wapna od 1989 r.",
            "Wapno nawozowe granulowane", "Dostawy w całej Polsce",
            "Granulat wapniowy dla rolnika", "Własna flota – cała Polska",
            "Wapno granulowane big-bag", "Zapytaj o ofertę – podaj tonaż",
            "Atesty i karty produktowe", "Wapnowanie pożniwne – termin",
            "Wapno pod orkę – dobierzemy", "Prosto od producenta wapna",
            "37 lat na rynku wapna",
        ],
        "opisy": [
            "Dostawca wapna nawozowego od 1989 r. Dostawy całosamochodowe w całej Polsce.",
            "Własna flota i magazyny w całym kraju. Dowozimy na termin, także większe tonaże.",
            "Karty produktowe, atesty OSChR, klasy normowe. Wiesz dokładnie, co wjeżdża na pole.",
            "Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą. Gospodarstwa i hurtownie.",
        ],
    },
    "Wapno nawozowe": {
        "url": "https://agria.pl/wapno-nawozowe/",
        "sciezka": ["wapno", "nawozowe"],
        "naglowki": [
            "Wapno nawozowe – producent", "Wapno nawozowe luzem 24 t",
            "Dostawy całosamochodowe", "Wapno węglanowe i tlenkowe",
            "Dostawca wapna od 1989 r.", "Odkwaszanie gleby – wapno",
            "Zapytaj o ofertę – podaj tonaż", "Dostawy w całej Polsce",
            "Atesty OSChR, karty techniczne", "Własna flota – cała Polska",
            "Agrobielik i Oxyfertil", "Wapno pod rzepak i zboża",
            "Wapno nawozowe dla rolnictwa", "Prosto od producenta wapna",
            "Trzy pokolenia w branży",
        ],
        "opisy": [
            "Dostawca wapna nawozowego od 1989 r. Dostawy całosamochodowe w całej Polsce.",
            "Dobierzemy typ wapna do Twojej gleby i terminu zabiegu. Doradztwo w cenie dostawy.",
            "Własna flota i magazyny w całym kraju. Terminy dopasowane do prac polowych.",
            "Karty produktowe i atesty dostępne na stronie. Parametry zgodne z rozporządzeniem.",
        ],
    },
    "Wapno magnezowe i kreda": {
        "url": "https://agria.pl/wapno-nawozowe/",
        "sciezka": ["wapno", "magnezowe"],
        "naglowki": [
            "Wapno magnezowe granulowane", "Wapno z magnezem – producent",
            "Dostawy całosamochodowe", "Kreda nawozowa luzem",
            "Dolomit i wapno magnezowe", "Dostawca wapna od 1989 r.",
            "Magnez i wapń jednym zabiegiem", "Zapytaj o ofertę – podaj tonaż",
            "Dostawy w całej Polsce", "Kreda nawozowa i pastewna",
            "Własna flota – cała Polska", "Atesty i karty produktowe",
            "Niedobór magnezu – uzupełnij", "Prosto od producenta wapna",
            "37 lat na rynku wapna",
        ],
        "opisy": [
            "Wapno magnezowe i kreda od producenta. Wapń i magnez w jednym zabiegu.",
            "Dostawy całosamochodowe w całej Polsce. Własna flota i magazyny w kraju.",
            "Karty produktowe z zawartością CaO i MgO. Atesty OSChR dla każdej partii.",
            "Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą własną flotą.",
        ],
    },
    "Brand": {
        "url": "https://agria.pl/",
        "sciezka": ["oferta"],
        "naglowki": [
            "AGRIA – dostawca wapna", "AGRIA Sp. z o.o. Tarnów",
            "Agrobielik – wapno tlenkowe", "Bielik – wapno hydratyzowane",
            "Oxyfertil w ofercie AGRIA", "Producent od 1989 roku",
            "Wapno i surowce wapniowe", "Dostawy w całej Polsce",
            "Oficjalna strona AGRIA", "EkoGranCali – granulat",
            "Trzy pokolenia, 37 lat", "Zapytaj o ofertę – podaj tonaż",
        ],
        "opisy": [
            "Oficjalna strona AGRIA Sp. z o.o. Dostawca wapna nawozowego i budowlanego od 1989 r.",
            "Agrobielik, Bielik, Oxyfertil, EkoGranCali – pełna oferta prosto od producenta.",
            "Rodzinna firma z Tarnowa, trzy pokolenia w branży wapna. Dostawy w całej Polsce.",
            "Karty produktowe, atesty i kalkulator wapnowania dostępne na stronie.",
        ],
    },
}

# ── Wykluczenia odsiewające detal ─────────────────────────────────────────────
NEG_DETAL = ["worek", "worki", "w workach", "25 kg", "20 kg", "10 kg",
             "sklep", "sklep internetowy", "kup online", "wysyłka kurierem",
             "paczka", "gdzie kupić", "cena za worek"]


def call(path, body):
    js = json.dumps(body, ensure_ascii=False, indent=1)
    if DRY:
        print(f"\n--- POST {path} ---\n{js[:1200]}")
        return {"results": [{"resourceName": f"DRY/{i}"} for i in range(len(body.get("operations", [{}])))]}
    tmp = f"/tmp/ads_t_{abs(hash(js))}.json"
    open(tmp, "w").write(js)
    out = subprocess.run(["bash", str(CALL), path, "POST", tmp],
                         capture_output=True, text=True).stdout
    os.unlink(tmp)
    d = json.loads(out)
    if "error" in d:
        e = d["error"]["details"][0]["errors"][0]
        sys.exit(f"BŁĄD {path}: {e.get('message','')[:300]}\n{e.get('location',{})}")
    return d


def gaql(query):
    tmp = f"/tmp/ads_q_{abs(hash(query))}.json"
    json.dump({"query": query}, open(tmp, "w"))
    out = subprocess.run(["bash", str(CALL), "/googleAds:searchStream", "POST", tmp],
                         capture_output=True, text=True).stdout
    os.unlink(tmp)
    d = json.loads(out)
    if isinstance(d, dict) and "error" in d:
        return []
    return [r for c in d for r in c.get("results", [])]


# walidacja limitów
bledy = []
for n, g in GRUPY.items():
    for h in g["naglowki"]:
        if len(h) > 30: bledy.append(f"[{n}] nagłówek {len(h)}: {h}")
    for d in g["opisy"]:
        if len(d) > 90: bledy.append(f"[{n}] opis {len(d)}: {d}")
if bledy:
    print("WALIDACJA NIE PRZESZŁA:")
    [print("  -", b) for b in bledy]
    sys.exit(1)
print(f"Walidacja OK ({sum(len(g['naglowki']) for g in GRUPY.values())} nagłówków)")

# mapa grup i istniejących reklam
grupy = {r["adGroup"]["name"]: r["adGroup"]["id"]
         for r in gaql("SELECT ad_group.id, ad_group.name FROM ad_group "
                       "WHERE ad_group.status != 'REMOVED'")}
stare = [(r["adGroup"]["name"], r["adGroupAd"]["resourceName"])
         for r in gaql("SELECT ad_group.name, ad_group_ad.resource_name FROM ad_group_ad "
                       "WHERE ad_group_ad.status != 'REMOVED'")]

# 1. nowe reklamy
ops = []
for n, g in GRUPY.items():
    if n not in grupy:
        print(f"  ! brak grupy {n}, pomijam"); continue
    rsa = {"headlines": [{"text": h} for h in g["naglowki"]],
           "descriptions": [{"text": d} for d in g["opisy"]],
           "path1": g["sciezka"][0]}
    if len(g["sciezka"]) > 1:
        rsa["path2"] = g["sciezka"][1]
    ops.append({"create": {"adGroup": f"customers/{CID}/adGroups/{grupy[n]}",
                           "status": "ENABLED",
                           "ad": {"finalUrls": [g["url"]], "responsiveSearchAd": rsa}}})
call("/adGroupAds:mutate", {"operations": ops})
print(f"  utworzono {len(ops)} nowych reklam")

# 2. usunięcie starych
if stare:
    call("/adGroupAds:mutate", {"operations": [{"remove": rn} for _, rn in stare]})
    print(f"  usunięto {len(stare)} starych reklam")

# 3. wykluczenia detalu na kampanii rolniczej
kamp = {r["campaign"]["name"]: r["campaign"]["resourceName"]
        for r in gaql("SELECT campaign.resource_name, campaign.name FROM campaign "
                      "WHERE campaign.status = 'ENABLED'")}
rol = kamp.get("AGRIA - Rolnictwo")
if rol:
    call("/campaignCriteria:mutate", {"operations": [
        {"create": {"campaign": rol, "negative": True,
                    "keyword": {"text": t, "matchType": "PHRASE"}}}
        for t in NEG_DETAL]})
    print(f"  dodano {len(NEG_DETAL)} wykluczeń detalu")

# 4. objaśnienie "Luz, big-bag, worki" -> komunikat o skali
stary_cal = [r for r in gaql("SELECT asset.id, asset.callout_asset.callout_text FROM asset "
                             "WHERE asset.type = 'CALLOUT'")
             if "worki" in r["asset"]["calloutAsset"]["calloutText"].lower()]
if stary_cal:
    aid = stary_cal[0]["asset"]["id"]
    ca = gaql(f"SELECT customer_asset.resource_name FROM customer_asset "
              f"WHERE customer_asset.asset = 'customers/{CID}/assets/{aid}'")
    if ca:
        call("/customerAssets:mutate",
             {"operations": [{"remove": ca[0]["customerAsset"]["resourceName"]}]})
    nowy = call("/assets:mutate", {"operations": [
        {"create": {"calloutAsset": {"calloutText": "Dostawy całosamochodowe"}}}]})
    call("/customerAssets:mutate", {"operations": [
        {"create": {"asset": nowy["results"][0]["resourceName"],
                    "fieldType": "CALLOUT", "status": "ENABLED"}}]})
    print("  objaśnienie 'Luz, big-bag, worki' -> 'Dostawy całosamochodowe'")

print("\nGOTOWE." if not DRY else "\nDRY-RUN.")
