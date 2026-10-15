# -*- coding: utf-8 -*-
"""Kampania „AGRIA - Wapno tlenkowe” — przebudowa Ads od zera po dwóch cyklach bez wyniku (15.10.2026).

Decyzje Janka 15.10: jedna intencja (wapno tlenkowe luzem — na tlenek idzie najwięcej telefonów u Pawła),
jedna fraza „wapno tlenkowe”, pierwsza pozycja, promień 80 km od Niedomic. Rolnictwo i Paszarstwo
zostają wstrzymane, Marka wraca na 5 zł/dz bez zmian.
Popyt i stawki: Planer słów kluczowych 15.10 — tlenek hurtowy ok. 66 wyszukiwań/dz w kraju,
górny zakres stawki na górę strony 1,4–2,0 zł.

Domyślnie PODGLĄD (odczyty tak, zapisy nie). Zapis: `--go`, wyłącznie po „ok” Janka.
Kampania powstaje jako PAUSED — włączenie razem ze wznowieniem konta (faktura albo promocja).
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SH = os.path.normpath(os.path.join(HERE, "..", "..", "google", "ads_call.sh"))
TMP = os.path.normpath(os.path.join(HERE, "..", "..", "..", "tmp", "ads-tlenek"))
DRY = "--go" not in sys.argv
os.makedirs(TMP, exist_ok=True)

NIEDOMICE = (50133000, 20850000)        # ten sam punkt co w promieniu kampanii Rolnictwo
PROMIEN_KM = 80
BUDZET_ZL = 15                          # sufit; przy ok. 8–10 wyszukiwaniach/dz realnie zejdzie mniej
STAWKA_ZL = 2.50

KARTA_70 = "https://agria.pl/wapno-nawozowe-rolnictwo/agrobielik-70/"

# Jedna fraza (decyzja Janka 15.10). Dopasowanie do wyrażenia łapie też „wapno tlenkowe luzem / cena /
# big bag / granulowane”; worki i budownictwo odcinają wykluczenia niżej.
GRUPY = {
    "Wapno tlenkowe": {
        "url": KARTA_70,
        "frazy": [("wapno tlenkowe", "PHRASE")],
        "naglowki": [
            "Wapno tlenkowe luzem", "Agrobielik 70 od 220 zł/t", "Wapno tlenkowe na pole",
            "Cały samochód 24 t", "Wysyłka z Niedomic", "AGRIA – dostawca od 1989 r.",
            "Wapno tlenkowe granulowane", "Wapno palone nawozowe", "Dostawa w 2–5 dni",
            "Szybko odkwasza glebę", "Atesty i karty produktu", "Wapno tlenkowe Małopolska",
            "Agrobielik 70 i 90", "Wycena z transportem", "Zamów cały samochód"],
        "opisy": [
            "Agrobielik 70 od 220 zł/t netto przy dostawie całosamochodowej 24 t. Cena bez transportu.",
            "Wysyłka z Niedomic i Radgoszczy. Podaj miejscowość i tonaż – policzymy transport.",
            "Wapno tlenkowe działa szybko i odkwasza glebę w kilka tygodni. Atesty na stronie.",
            "Dostawca od 1989 r. Wapno tlenkowe luzem i w big-bagach, prosto na pole."],
    },
}

# Budowlane, worki, chemia, staw, sklepy — tlenek luzem na pole to nie te zapytania.
NEGATYWY = ["gaszone", "gaszonego", "gaszenie", "budowlane", "budowlanego", "tynk", "zaprawa",
            "bielenie", "do bielenia", "ściany", "drzew", "staw", "stawu", "kurnik", "dezynfekcja",
            "wzór", "reakcja", "chemiczny", "co to", "wikipedia", "jak zrobić", "5 kg", "10 kg",
            "20 kg", "25 kg", "40 kg", "worek", "worki", "castorama", "leroy", "obi", "allegro",
            "olx", "bryłach"]

for nazwa, g in GRUPY.items():
    for h in g["naglowki"]:
        assert len(h) <= 30, (nazwa, len(h), h)
    for o in g["opisy"]:
        assert len(o) <= 90, (nazwa, len(o), o)
    assert 3 <= len(g["naglowki"]) <= 15 and 2 <= len(g["opisy"]) <= 4, nazwa
print("limity OK:", {n: (max(map(len, g["naglowki"])), max(map(len, g["opisy"]))) for n, g in GRUPY.items()})


def call(path, body, opis):
    if DRY:
        print(f"[PODGLĄD] {path:26s} {len(body['operations']):3d} op.  {opis}")
        return {"results": [{"resourceName": f"DRY/{opis}"}]}
    f = os.path.join(TMP, "op.json")
    open(f, "w").write(json.dumps(body, ensure_ascii=False))
    r = subprocess.run(["bash", SH, path, "POST", f], capture_output=True, text=True, timeout=120)
    try:
        d = json.loads(r.stdout)
    except Exception:
        print("ODPOWIEDŹ:", r.stdout[:800], r.stderr[:400]); raise
    if isinstance(d, dict) and "error" in d:
        print("BŁĄD:", json.dumps(d["error"], ensure_ascii=False)[:900]); raise SystemExit(1)
    print(f"[ZAPIS] {path:26s} {opis}")
    return d


def odczyt(query):
    f = os.path.join(TMP, "q.json")
    open(f, "w").write(json.dumps({"query": query}))
    r = subprocess.run(["bash", SH, "/googleAds:searchStream", "POST", f], capture_output=True, text=True, timeout=120)
    return [x for ch in json.loads(r.stdout) for x in ch.get("results", [])]


# Odczyt (także w podglądzie): rozszerzenia połączeń.
telefony = odczyt("SELECT asset.resource_name, asset.call_asset.phone_number FROM asset WHERE asset.type = CALL")
# Tylko numer Pawła (decyzja Janka 15.10): to on odbiera telefony o tlenek i może zapytać, skąd klient przyszedł.
telefony = [a for a in telefony if a["asset"]["callAsset"]["phoneNumber"] == "+48664393062"]
print("rozszerzenia połączeń:", [(a["asset"]["resourceName"].split("/")[-1], a["asset"]["callAsset"]["phoneNumber"]) for a in telefony])

# 1. budżet
b = call("/campaignBudgets:mutate", {"operations": [{"create": {
    "name": f"AGRIA - Wapno tlenkowe ({BUDZET_ZL} zl/dz)", "amountMicros": str(BUDZET_ZL * 1_000_000),
    "deliveryMethod": "STANDARD", "explicitlyShared": False}}]}, f"budżet {BUDZET_ZL} zł/dz")
bud = b["results"][0]["resourceName"]

# 2. kampania — PAUSED do wznowienia konta
c = call("/campaigns:mutate", {"operations": [{"create": {
    "name": "AGRIA - Wapno tlenkowe", "status": "PAUSED", "advertisingChannelType": "SEARCH",
    "containsEuPoliticalAdvertising": "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    "campaignBudget": bud, "manualCpc": {"enhancedCpcEnabled": False},
    "networkSettings": {"targetGoogleSearch": True, "targetSearchNetwork": False,
                        "targetContentNetwork": False, "targetPartnerSearchNetwork": False},
    "geoTargetTypeSetting": {"positiveGeoTargetType": "PRESENCE", "negativeGeoTargetType": "PRESENCE"}}}]},
    "kampania (PAUSED)")
camp = c["results"][0]["resourceName"]

# 3. kryteria kampanii: promień 80 km, język, harmonogram 7 dni 6–22 (niedziela najmocniejsza), wykluczenia
DNI = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
krit = [{"create": {"campaign": camp, "proximity": {
            "geoPoint": {"latitudeInMicroDegrees": NIEDOMICE[0], "longitudeInMicroDegrees": NIEDOMICE[1]},
            "radius": PROMIEN_KM, "radiusUnits": "KILOMETERS"}}},
        {"create": {"campaign": camp, "language": {"languageConstant": "languageConstants/1030"}}}]
krit += [{"create": {"campaign": camp, "adSchedule": {"dayOfWeek": d, "startHour": 6, "startMinute": "ZERO",
          "endHour": 22, "endMinute": "ZERO"}}} for d in DNI]
krit += [{"create": {"campaign": camp, "negative": True, "keyword": {"text": t, "matchType": "PHRASE"}}}
         for t in NEGATYWY]
call("/campaignCriteria:mutate", {"operations": krit},
     f"promień {PROMIEN_KM} km od Niedomic, harmonogram 7×6–22, {len(NEGATYWY)} wykluczeń")

# 4. rozszerzenia połączeń — te same numery co w dotychczasowych kampaniach
if telefony:
    call("/campaignAssets:mutate", {"operations": [{"create": {"campaign": camp, "asset": a["asset"]["resourceName"],
         "fieldType": "CALL"}} for a in telefony]}, f"{len(telefony)} rozszerzeń połączeń")

# 5. grupy, frazy, reklamy
for nazwa, g in GRUPY.items():
    a = call("/adGroups:mutate", {"operations": [{"create": {
        "name": nazwa, "campaign": camp, "status": "ENABLED", "type": "SEARCH_STANDARD",
        "cpcBidMicros": str(int(STAWKA_ZL * 1_000_000))}}]}, f"grupa „{nazwa}”, stawka {STAWKA_ZL:.2f} zł")
    ag = a["results"][0]["resourceName"]
    call("/adGroupCriteria:mutate", {"operations": [{"create": {"adGroup": ag, "status": "ENABLED",
         "keyword": {"text": t, "matchType": m}}} for t, m in g["frazy"]]}, f"  {len(g['frazy'])} fraz")
    call("/adGroupAds:mutate", {"operations": [{"create": {"adGroup": ag, "status": "ENABLED", "ad": {
        "finalUrls": [g["url"]], "responsiveSearchAd": {
            "headlines": [{"text": h} for h in g["naglowki"]],
            "descriptions": [{"text": o} for o in g["opisy"]]}}}}]}, f"  reklama → {g['url']}")

print("\nPODGLĄD — nic nie wysłano. Zapis: --go (po „ok” Janka)." if DRY else "\nZapisane. Sprawdź odczytem zwrotnym.")
