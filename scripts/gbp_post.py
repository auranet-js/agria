#!/usr/bin/env python3
"""Publikuje wpis na wizytówce Google Business Profile (localPosts).

Rytm wizytówki AGRIA: **jedna publikacja tygodniowo, we wtorek** — kampania emituje nd/pn/wt,
więc post wchodzi w ten sam rytm, w którym kupujemy uwagę. Gotowe teksty i uzasadnienia:
`docs/gbp/2026-09-08-blok0-publikacje-i-opinie.md`.

⚠️ **Publikacji NIE da się datować wstecz** — `createTime` jest polem tylko do odczytu, post
dostaje znacznik czasu w chwili utworzenia. Nie ma sensu wrzucać kilku naraz „na zapas":
Google eksponuje wpis przez mniej więcej tydzień, więc cztery jednego dnia to zmarnowanie trzech.

⚠️ Zdjęcie podajemy przez `sourceUrl` i **musi to być JPG albo PNG** — uploady agria.pl są
serwowane jako `.jpg.webp`, których GBP nie przyjmie. Sprawdź `content-type`, zanim użyjesz.

Usunięcie wpisu jest możliwe (DELETE na jego `name`), ale wpis zdążył już być publiczny.

Użycie:
    gbp_post.py <plik.json>              # pokazuje, co poleci — nic nie wysyła
    gbp_post.py <plik.json> --wyslij

Plik wejściowy: {"summary": "Nagłówek\\n\\nTreść", "url": "https://…", "zdjecie": "https://….jpg"}
`zdjecie` jest opcjonalne, ale wszystkie dotychczasowe wpisy je mają — bez niego post odstaje.
"""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

SEKRETY = Path.home() / "secrets" / "google"
KONTO = "accounts/111497772731899556217"
LOKALIZACJA = "locations/11686460679773422640"
BAZA = f"https://mybusiness.googleapis.com/v4/{KONTO}/{LOKALIZACJA}/localPosts"
LIMIT_SUMMARY = 1500


def token():
    import urllib.parse
    o = json.loads((SEKRETY / "oauth-desktop-client.json").read_text())["installed"]
    t = json.loads((SEKRETY / "tokens.json").read_text())
    d = urllib.parse.urlencode({
        "client_id": o["client_id"], "client_secret": o["client_secret"],
        "refresh_token": t["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(
        urllib.request.Request("https://oauth2.googleapis.com/token", data=d)))["access_token"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    wpis = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    if len(wpis["summary"]) > LIMIT_SUMMARY:
        sys.exit(f"BŁĄD: treść ma {len(wpis['summary'])} znaków, limit GBP to {LIMIT_SUMMARY}")

    cialo = {
        "languageCode": "pl",
        "summary": wpis["summary"],
        "topicType": "STANDARD",
        "callToAction": {"actionType": "LEARN_MORE", "url": wpis["url"]},
    }
    if wpis.get("zdjecie"):
        cialo["media"] = [{"mediaFormat": "PHOTO", "sourceUrl": wpis["zdjecie"]}]

    print(f"CEL:     {wpis['url']}")
    print(f"ZDJĘCIE: {wpis.get('zdjecie') or '(brak — post będzie odstawał od pozostałych)'}")
    print(f"ZNAKÓW:  {len(wpis['summary'])} z {LIMIT_SUMMARY}")
    print("TREŚĆ:")
    for linia in wpis["summary"].split("\n"):
        print(f"  {linia}")
    if "--wyslij" not in sys.argv:
        sys.exit("\nnic nie wysłano — dopisz --wyslij")

    req = urllib.request.Request(BAZA, method="POST",
                                 headers={"Authorization": f"Bearer {token()}",
                                          "Content-Type": "application/json"},
                                 data=json.dumps(cialo).encode())
    try:
        r = json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        sys.exit(f"BŁĄD {e.code}: {e.read().decode()[:600]}")

    print(f"\nstan:      {r.get('state')}")
    print(f"utworzony: {r.get('createTime')}")
    print(f"nazwa:     {r.get('name')}")
    print(f"podgląd:   {r.get('searchUrl', '(brak — pojawi się po chwili)')}")
