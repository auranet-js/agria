# -*- coding: utf-8 -*-
import json, subprocess, sys, os
SH = "/home/host476470/projekty/agria/scripts/google/ads_call.sh"
TMP = "/tmp/claude-1584/-home-host476470-projekty-agria/6771d600-cdc7-4400-bd3c-8888646d6e0e/scratchpad"
CID = "customers/6742071446"
DRY = "--go" not in sys.argv

def call(path, body):
    f = os.path.join(TMP, "op.json")
    open(f, "w").write(json.dumps(body, ensure_ascii=False))
    if DRY:
        print(f"[DRY] {path}  ({len(body.get('operations',[]))} op.)"); return {"results":[{"resourceName":"DRY"}]}
    r = subprocess.run(["bash", SH, path, "POST", f], capture_output=True, text=True, timeout=120)
    try: d = json.loads(r.stdout)
    except Exception: print("ODPOWIEDŹ:", r.stdout[:800], r.stderr[:400]); raise
    if isinstance(d, dict) and "error" in d:
        print("BŁĄD:", json.dumps(d["error"], ensure_ascii=False)[:900]); raise SystemExit(1)
    return d

NAGLOWKI = ["Kreda pastewna luzem","Kreda pastewna 30 kg","Kreda pastewna dla niosek",
 "Kreda pastewna dla bydła","Wapń dla drobiu i trzody","Dostawa własną flotą 3–24 t",
 "Zapytaj o ofertę – podaj tonaż","Atesty i karty produktowe","Kreda pastewna Małopolska",
 "AGRIA – dostawca od 1989 r.","Frakcja dobrana do gatunku","Kreda pastewna hurt",
 "Wycena dla ferm i hodowli","Kreda pastewna big-bag","Kreda paszowa – węglan wapnia"]
OPISY = ["Kreda pastewna dla drobiu, trzody i bydła. Luz, big-bag, worek 30 kg. Zapytaj o ofertę.",
 "Dostawa własną flotą 3–24 t. Dwa magazyny w Małopolsce, terminy pod cykl produkcyjny.",
 "Karty produktowe i atesty na stronie. Znasz zawartość wapnia i frakcję przed zakupem.",
 "Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą. Obsługa ferm i hodowli."]
FRAZY = [("kreda pastewna","PHRASE"),("kreda pastewna","EXACT"),("kreda pastewna dla kur","PHRASE"),
 ("kreda pastewna dla kur niosek","PHRASE"),("kreda pastewna dla bydła","PHRASE"),
 ("kreda pastewna dawkowanie","PHRASE"),("kreda pastewna gruboziarnista","PHRASE"),
 ("kreda pastewna cena","PHRASE"),("wapno dla kur niosek","PHRASE"),("kreda dla kur niosek","PHRASE"),
 ("kreda paszowa","PHRASE"),("wapno pastewne","PHRASE"),("węglan wapnia dla drobiu","PHRASE")]
NEGATYWY = ["jadalna","do jedzenia","dla ludzi","do picia","ślimak","ślimaki","akwarium","chomik",
 "papug","kreda szkolna","kreda do tablicy","kreda malarska","kreda krawiecka","allegro","olx",
 "ceneo","empik","sklep internetowy","1 kg","2 kg","5 kg","przepis","recenzje"]

for h in NAGLOWKI:
    assert len(h) <= 30, (len(h), h)
for o in OPISY:
    assert len(o) <= 90, (len(o), o)
print(f"limity OK: nagłówki max {max(len(h) for h in NAGLOWKI)}, opisy max {max(len(o) for o in OPISY)}")

# 1. budżet
b = call("/campaignBudgets:mutate", {"operations":[{"create":{
    "name":"AGRIA - Paszarstwo (9 zl/dz)","amountMicros":"9000000","deliveryMethod":"STANDARD",
    "explicitlyShared":False}}]})
bud = b["results"][0]["resourceName"]; print("budżet:", bud)

# 2. kampania
c = call("/campaigns:mutate", {"operations":[{"create":{
    "name":"AGRIA - Paszarstwo","status":"ENABLED","advertisingChannelType":"SEARCH",
    "containsEuPoliticalAdvertising":"DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    "campaignBudget":bud,"manualCpc":{"enhancedCpcEnabled":False},
    "networkSettings":{"targetGoogleSearch":True,"targetSearchNetwork":False,
        "targetContentNetwork":False,"targetPartnerSearchNetwork":False},
    "geoTargetTypeSetting":{"positiveGeoTargetType":"PRESENCE","negativeGeoTargetType":"PRESENCE"}}}]})
camp = c["results"][0]["resourceName"]; print("kampania:", camp)

# 3. kryteria: geo, język, harmonogram 6-22 x7, wykluczenia
DNI = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
krit = [{"create":{"campaign":camp,"location":{"geoTargetConstant":"geoTargetConstants/2616"}}},
        {"create":{"campaign":camp,"language":{"languageConstant":"languageConstants/1030"}}}]
krit += [{"create":{"campaign":camp,"adSchedule":{"dayOfWeek":d,"startHour":6,"startMinute":"ZERO",
          "endHour":22,"endMinute":"ZERO"}}} for d in DNI]
krit += [{"create":{"campaign":camp,"negative":True,"keyword":{"text":t,"matchType":"PHRASE"}}}
         for t in NEGATYWY]
call("/campaignCriteria:mutate", {"operations":krit}); print(f"kryteria: {len(krit)} op.")

# 4. grupa reklam
a = call("/adGroups:mutate", {"operations":[{"create":{
    "name":"Kreda pastewna","campaign":camp,"status":"ENABLED","type":"SEARCH_STANDARD",
    "cpcBidMicros":"1200000"}}]})
ag = a["results"][0]["resourceName"]; print("grupa:", ag)

# 5. frazy
call("/adGroupCriteria:mutate", {"operations":[{"create":{"adGroup":ag,"status":"ENABLED",
     "keyword":{"text":t,"matchType":m}}} for t,m in FRAZY]}); print(f"frazy: {len(FRAZY)}")

# 6. reklama
call("/adGroupAds:mutate", {"operations":[{"create":{"adGroup":ag,"status":"ENABLED","ad":{
    "finalUrls":["https://agria.pl/paszarstwo/kreda-pastewna/"],
    "responsiveSearchAd":{"headlines":[{"text":h} for h in NAGLOWKI],
        "descriptions":[{"text":o} for o in OPISY],
        "path1":"kreda","path2":"pastewna"}}}}]}); print("reklama: 1 RSA")
print("\nGOTOWE" if not DRY else "\n(dry-run — dodaj --go)")
