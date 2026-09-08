#!/usr/bin/env python3
"""Ustawia obszar obsługi (`serviceArea`) wizytówki Google Business Profile.

Po co osobny skrypt: `gbp_patch.py` wysyła wartość jako zwykły string, a `serviceArea` jest
strukturą (typ działalności + lista miejsc z `placeId`). Tego drugiego tamten nie potrafi.

⚠️ GBP nie wersjonuje profilu — jedynym rollbackiem jest zrzut z `gbp_dump.py`. Zrób go przed.

⚠️ Domyślnie `businessType` to `CUSTOMER_AND_BUSINESS_LOCATION`, czyli obszar obsługi **obok**
adresu. AGRIA ma realną siedzibę pod Warsztatową 5 i ta pinezka daje prośby o trasę — nie zamieniaj
wizytówki na firmę bez adresu (`CUSTOMER_LOCATION_ONLY`), bo pinezka wtedy znika.

`placeId` bierzemy z Geocoding API (klucz `~/secrets/google/psi-crux-key.txt`), bo GBP przyjmuje
wyłącznie miejsca — promieni, jakich używamy w Google Ads, to pole nie zna. Limit: 20 miejsc.

Użycie:
    gbp_service_area.py <plik.json>            # pokazuje stan przed i planowany, nic nie wysyła
    gbp_service_area.py <plik.json> --wyslij

Plik wejściowy: {"places": [{"placeName": "...", "placeId": "..."}, ...]}
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SEKRETY = Path.home() / "secrets" / "google"
LOKALIZACJA = "locations/11686460679773422640"
BAZA = f"https://mybusinessbusinessinformation.googleapis.com/v1/{LOKALIZACJA}"


def token():
    o = json.loads((SEKRETY / "oauth-desktop-client.json").read_text())["installed"]
    t = json.loads((SEKRETY / "tokens.json").read_text())
    d = urllib.parse.urlencode({
        "client_id": o["client_id"], "client_secret": o["client_secret"],
        "refresh_token": t["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(
        urllib.request.Request("https://oauth2.googleapis.com/token", data=d)))["access_token"]


def czytaj(t):
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        f"{BAZA}?readMask=serviceArea", headers={"Authorization": f"Bearer {t}"})))
    return r.get("serviceArea")


def miejsca_z_profilu(obszar):
    """Zwraca (placeId, placeName). Porównujemy po ID, bo Google normalizuje nazwy —
    „Województwo śląskie" wraca jako „Województwo śląskie, Polska"."""
    if not obszar:
        return []
    return [(p.get("placeId"), p.get("placeName"))
            for p in (obszar.get("places") or {}).get("placeInfos", [])]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    miejsca = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))["places"]
    if len(miejsca) > 20:
        sys.exit(f"BŁĄD: {len(miejsca)} miejsc, limit GBP to 20")

    t = token()
    print(f"PRZED: {[n for _, n in miejsca_z_profilu(czytaj(t))] or None}")
    print(f"NOWY:  {[m['placeName'] for m in miejsca]}")
    if "--wyslij" not in sys.argv:
        sys.exit("\nnic nie wysłano — dopisz --wyslij")

    cialo = {"serviceArea": {"businessType": "CUSTOMER_AND_BUSINESS_LOCATION",
                             "places": {"placeInfos": miejsca}}}
    req = urllib.request.Request(f"{BAZA}?updateMask=serviceArea", method="PATCH",
                                 headers={"Authorization": f"Bearer {t}",
                                          "Content-Type": "application/json"},
                                 data=json.dumps(cialo).encode())
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        sys.exit(f"BŁĄD {e.code}: {e.read().decode()[:600]}")

    # API po zapisie potrafi jeszcze chwilę oddawać stary stan — czytamy w pętli, jak gbp_patch.py
    oczekiwane = sorted(m["placeId"] for m in miejsca)
    for proba in range(1, 7):
        time.sleep(10)
        ma = miejsca_z_profilu(czytaj(t))
        print(f"  odczyt {proba}: {[n for _, n in ma]}")
        if ma and sorted(i for i, _ in ma) == oczekiwane:
            sys.exit(0)
    print("UWAGA: po sześciu odczytach obszar nadal się nie zgadza — sprawdź moderację profilu")
