#!/usr/bin/env python3
"""Zmienia pojedyncze pole wizytówki Google Business Profile.

Domyślnie NIC nie wysyła — trzeba podać `--wyslij`. GBP nie wersjonuje profilu, więc jedynym
rollbackiem jest zrzut z `gbp_dump.py`.

Uwaga operacyjna z 20.08: po zapisie API przez kilkadziesiąt sekund oddaje jeszcze STARĄ wartość.
Skrypt czyta zwrotnie w pętli, zamiast raportować wynik po pierwszym odczycie.

Wartość zaczynająca się od `{` albo `[` idzie jako JSON (np. `categories`).

Użycie: gbp_patch.py <pole> <wartość> [--lok tarnow|niedomice|radgoszcz] [--wyslij]
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from gbp_dump import wybierz_lokalizacje

SECRETS = Path.home() / "secrets" / "google"
BAZA = "https://mybusinessbusinessinformation.googleapis.com/v1/" + wybierz_lokalizacje(sys.argv)


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


def zgodne(ma, chce):
    """Czy odczyt zawiera wysłaną wartość — Google dokleja do struktur własne pola (np. displayName)."""
    if isinstance(chce, dict):
        return isinstance(ma, dict) and all(zgodne(ma.get(k), v) for k, v in chce.items())
    if isinstance(chce, list):
        return isinstance(ma, list) and len(ma) == len(chce) and all(map(zgodne, ma, chce))
    return ma == chce


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    pole, wartosc = sys.argv[1], sys.argv[2]
    if wartosc[:1] in "{[":
        wartosc = json.loads(wartosc)
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
        if zgodne(ma, wartosc):
            sys.exit(0)
    print("UWAGA: po sześciu odczytach pole nadal ma starą wartość — sprawdź moderację")
