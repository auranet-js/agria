#!/usr/bin/env python3
"""Zrzut pełnego stanu wizytówki Google Business Profile — jedyny rollback, jaki mamy.

GBP nie wersjonuje profilu i nie ma cofnięcia zmiany: `patch` nadpisuje pole i tyle.
Dlatego przed KAŻDĄ zmianą robimy zrzut do `tmp/` — lokalizacja, media, opinie i publikacje
w jednym pliku, z datą w nazwie.

Wymaga scope `business.manage` w ~/secrets/google/tokens.json.

Użycie: gbp_dump.py <plik-wyjściowy.json>
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SECRETS = Path.home() / "secrets" / "google"
KONTO = "accounts/111497772731899556217"
LOKALIZACJA = "locations/11686460679773422640"

POLA = ("name,title,storefrontAddress,websiteUri,phoneNumbers,categories,regularHours,"
        "specialHours,profile,labels,latlng,metadata,openInfo,serviceArea,moreHours")


def token():
    oauth = json.loads((SECRETS / "oauth-desktop-client.json").read_text())["installed"]
    tok = json.loads((SECRETS / "tokens.json").read_text())
    dane = urllib.parse.urlencode({
        "client_id": oauth["client_id"], "client_secret": oauth["client_secret"],
        "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(
        urllib.request.Request("https://oauth2.googleapis.com/token", data=dane)))["access_token"]


def get(t, url):
    try:
        return json.load(urllib.request.urlopen(
            urllib.request.Request(url, headers={"Authorization": f"Bearer {t}"})))
    except urllib.error.HTTPError as e:
        return {"_błąd": e.code, "_treść": e.read().decode()[:600]}


if __name__ == "__main__":
    t = token()
    B1 = "https://mybusinessbusinessinformation.googleapis.com/v1"
    B2 = f"https://mybusiness.googleapis.com/v4/{KONTO}/{LOKALIZACJA}"
    zrzut = {
        "lokalizacja": get(t, f"{B1}/{LOKALIZACJA}?readMask={POLA}"),
        "media": get(t, f"{B2}/media"),
        "opinie": get(t, f"{B2}/reviews"),
        "publikacje": get(t, f"{B2}/localPosts"),
    }
    cel = sys.argv[1] if len(sys.argv) > 1 else "tmp/gbp-tarnow.json"
    json.dump(zrzut, open(cel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in zrzut.items():
        blad = v.get("_błąd") if isinstance(v, dict) else None
        ile = len(v.get("mediaItems") or v.get("reviews") or v.get("localPosts") or []) if not blad else "—"
        print(f"  {k:12} {'BŁĄD ' + str(blad) if blad else 'ok'}   pozycji: {ile}")
    print(f"→ {cel}")
