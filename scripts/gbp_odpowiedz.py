#!/usr/bin/env python3
"""Podmienia odpowiedź na opinię w Google Business Profile.

Domyślnie NIC nie wysyła — trzeba świadomie podać `--wyslij`. Odpowiedzi są publiczne
i sygnowane firmą, a GBP nie ma historii zmian: nowy tekst nadpisuje poprzedni bez śladu.

Użycie:
    gbp_odpowiedz.py <reviewId> <plik-z-treścią.txt> [--wyslij]
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
BAZA = f"https://mybusiness.googleapis.com/v4/{KONTO}/{LOKALIZACJA}/reviews"


def token():
    oauth = json.loads((SECRETS / "oauth-desktop-client.json").read_text())["installed"]
    tok = json.loads((SECRETS / "tokens.json").read_text())
    dane = urllib.parse.urlencode({
        "client_id": oauth["client_id"], "client_secret": oauth["client_secret"],
        "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(
        urllib.request.Request("https://oauth2.googleapis.com/token", data=dane)))["access_token"]


def wolaj(t, metoda, url, body=None):
    req = urllib.request.Request(url, method=metoda,
                                 headers={"Authorization": f"Bearer {t}",
                                          "Content-Type": "application/json"},
                                 data=json.dumps(body, ensure_ascii=False).encode() if body else None)
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        return {"_błąd": e.code, "_treść": e.read().decode()[:600]}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    rid, plik = sys.argv[1], sys.argv[2]
    tresc = Path(plik).read_text(encoding="utf-8").strip()
    t = token()

    stan = wolaj(t, "GET", f"{BAZA}/{rid}")
    print("PRZED:")
    print("  ocena:  ", stan.get("starRating"))
    print("  opinia: ", (stan.get("comment") or "(bez treści)").split("(Translated")[0].strip()[:120])
    print("  odpowiedź:", (stan.get("reviewReply") or {}).get("comment", "(brak)")[:200])
    print("\nNOWA ODPOWIEDŹ:")
    print(" ", tresc)

    if "--wyslij" not in sys.argv:
        print("\nnic nie wysłano — dopisz --wyslij")
        sys.exit()

    wynik = wolaj(t, "PUT", f"{BAZA}/{rid}/reply", {"comment": tresc})
    if wynik.get("_błąd"):
        sys.exit(f"BŁĄD {wynik['_błąd']}: {wynik['_treść']}")
    po = wolaj(t, "GET", f"{BAZA}/{rid}")
    print("\nPO (odczyt zwrotny z API):")
    print(" ", (po.get("reviewReply") or {}).get("comment", "(brak)"))
