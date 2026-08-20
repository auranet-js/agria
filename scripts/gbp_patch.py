#!/usr/bin/env python3
"""Zmienia pojedyncze pole wizytówki Google Business Profile.

Domyślnie NIC nie wysyła — trzeba podać `--wyslij`. GBP nie wersjonuje profilu, więc jedynym
rollbackiem jest zrzut z `gbp_dump.py`.

Uwaga operacyjna z 20.08: po zapisie API przez kilkadziesiąt sekund oddaje jeszcze STARĄ wartość.
Skrypt czyta zwrotnie w pętli, zamiast raportować wynik po pierwszym odczycie.

Użycie: gbp_patch.py <pole> <wartość> [--wyslij]
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SECRETS = Path.home() / "secrets" / "google"
LOKALIZACJA = "locations/11686460679773422640"
BAZA = f"https://mybusinessbusinessinformation.googleapis.com/v1/{LOKALIZACJA}"


def token():
    o = json.loads((SECRETS / "oauth-desktop-client.json").read_text())["installed"]
    t = json.loads((SECRETS / "tokens.json").read_text())
    d = urllib.parse.urlencode({"client_id": o["client_id"], "client_secret": o["client_secret"],
                                "refresh_token": t["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(
        urllib.request.Request("https://oauth2.googleapis.com/token", data=d)))["access_token"]


def czytaj(t, pole):
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        f"{BAZA}?readMask={pole}", headers={"Authorization": f"Bearer {t}"})))
    return r.get(pole)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    pole, wartosc = sys.argv[1], sys.argv[2]
    t = token()
    print(f"PRZED: {pole} = {czytaj(t, pole)!r}")
    print(f"NOWA:  {pole} = {wartosc!r}")
    if "--wyslij" not in sys.argv:
        sys.exit("\nnic nie wysłano — dopisz --wyslij")

    req = urllib.request.Request(f"{BAZA}?updateMask={pole}", method="PATCH",
                                 headers={"Authorization": f"Bearer {t}",
                                          "Content-Type": "application/json"},
                                 data=json.dumps({pole: wartosc}).encode())
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        sys.exit(f"BŁĄD {e.code}: {e.read().decode()[:500]}")

    for próba in range(1, 7):
        time.sleep(12)
        ma = czytaj(t, pole)
        print(f"  odczyt {próba}: {ma!r}")
        if ma == wartosc:
            sys.exit(0)
    print("UWAGA: po sześciu odczytach pole nadal ma starą wartość — sprawdź moderację")
