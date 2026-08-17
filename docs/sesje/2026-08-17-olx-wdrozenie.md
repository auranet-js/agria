# OLX — prompt wdrożeniowy (publikacja 200 ogłoszeń)

> Stan na 17.08.2026. Wszystko po stronie Auranet gotowe; czeka wyłącznie na opłacony pakiet.
> Ten plik jest promptem startowym dla sesji, w której faktycznie wystawiamy ogłoszenia.

## Warunek startu

Na koncie AGRII (`pawelxpb@gmail.com`) opłacony **Pakiet Premium 200 w kategorii Nawozy**
— 1 199,99 zł brutto, ważny 30 dni od zakupu. Bez tego ogłoszenia wychodzą ze statusem
`limited`, czyli praktycznie niewidoczne.

Weryfikacja przed startem: panel OLX → Pakiety, albo status wiszącego pilota
`1089946612` — po opłaceniu pakietu powinien przejść z `limited` na `active`.

## Stan przygotowania (zweryfikowany 17.08)

- **200 ładunków** w `data/olx/adverts-payload.json` — 13 pozycji × 52 miejscowości,
  8 województw, kategoria 4368.
- **Tytuły przepisane 17.08** na konwencję kategorii: przecinki, 4–6 członów, 108–123 znaki
  (limit OLX to 150, nie 70 — zweryfikowane na 2 486 ogłoszeniach ze snapshotu rynku).
  Towar i przeznaczenie z przodu, żadnych czasowników usługowych („wapnowanie", „odkwaszanie"
  jako czynność = usługa rozsiewu, której AGRIA nie świadczy), transport poza tytułem.
- **Żargon wyczyszczony** — 228 wystąpień „loco magazyn" zamienione na „cena za towar,
  bez transportu".
- **Pilot 1089946612** („Wapno do stawu", Zator) wisi na koncie ze **starą treścią** —
  wymaga `--update` przed resztą.
- Rejestr wystawionych: `data/olx/posted.json` (1 pozycja). Skrypt nie wystawia dwa razy
  tego samego `external_id`.

## Kolejność

```bash
cd ~/projekty/agria

# 0. Token (żyje 24 h; refresh_token bezterminowo)
~/bin/olx-agria status          # jeśli WYGASŁ:
~/bin/olx-agria refresh

# 1. Pilot dostaje aktualną treść (stary tytuł + „loco")
python3 scripts/olx/post_adverts.py --update

#    sprawdź render na żywo: https://www.olx.pl/d/oferta/…-ID1bLiU4.html
#    tytuł, cena 220 zł, 6 zdjęć, telefon w polu kontaktowym, status już nie `limited`

# 2. Jedno nowe ogłoszenie na próbę — potwierdza, że pakiet konsumuje jednostki
python3 scripts/olx/post_adverts.py --pilot 2

# 3. STOP — pokaż Jankowi wynik, czekaj na „ok"

# 4. Reszta
python3 scripts/olx/post_adverts.py --all

# 5. auto_extend na wszystkim (to on zgasił konto 18.07 — był na 1 z 20 ogłoszeń)
python3 scripts/olx/post_adverts.py --auto-extend

# 6. Baseline pomiarowy w dniu startu, potem co tydzień
~/projekty/agria/scripts/olx/olx-snapshot
```

## Gotchas (wszystkie zapłacone własną krwią)

- **`PUT /partner/adverts/{id}` podmienia cały zasób**, nie łata pola. Wysłanie samego
  `{"auto_extend_enabled":true}` zwraca 400 i flaga zostaje na `false` — dokładnie ten
  mechanizm zgasił konto 18.07. Obsłużone w `putable()`, nie obchodzić go ręcznie.
- **`contact.phone` musi być jawnie w ładunku** — inaczej ogłoszenie wychodzi bez numeru,
  czyli bez kanału, który daje praktycznie wszystkie kontakty.
- **Numer telefonu w treści opisu łamie regulamin** (dane kontaktowe tylko w polach
  formularza). `build_adverts.py` przerywa generowanie, jeśli go wykryje.
- **Pakiet i każde ogłoszenie żyją 30 dni.** `auto_extend` odnawia ogłoszenie tylko dopóki
  żyje pakiet — pilnować daty odnowienia pakietu, bo wygaśnięcie gasi wszystko naraz.
- **Pierwsze ogłoszenie, które nie przejdzie, przerywa masówkę** (celowo). Kolejne błędy
  są tylko logowane.
- **API nie ma endpointów pakietów ani limitów** — stan pakietu wyłącznie z panelu.

## Po wystawieniu

- Snapshot w dniu startu + co tydzień (`olx-snapshot`), różnica między snapshotami = realny
  przyrost, panel pokazuje sumy narastająco od założenia ogłoszenia.
- Prognoza do weryfikacji: ostrożnie ~50, realnie ~150, optymistycznie ~230 odsłon numeru
  miesięcznie przy 200 ogłoszeniach.
- Wspólna ocena kanału z Google Ads — **koniec października**.
- Rewizja sezonowa poza wyceną: listopad (wapno palone w szczycie, zimą paszarstwo
  i hydratyzowane pod budownictwo).

## Otwarte, do rozstrzygnięcia przez Janka

- Czy „Oxyfertil" zostaje w tytule (nazwy handlowej nikt nie szuka, ale w środku nie szkodzi).
- Czy przy węglanowym i magnezowym zostaje „odm. 04 / 05" — nomenklatura z rozporządzenia,
  rolnicy piszą częściej po prostu „wapno węglanowe".
- Zmiana hasła do konta OLX (przyszło plaintextem mailem 07.08) + włączenie 2FA.

Kontekst handlowy i pełna rozpiska: `docs/offers/2026-08-PLAN_OLX.md`,
`docs/offers/OLX_TABELA_OGLOSZEN.md`, `docs/operations/OLX_BASELINE_2026-08-07.md`.
Wersja klient-facing wysłana Pawłowi 17.08:
`https://auratest.pl/fe4f58fec53ctmp/agria-olx-ogloszenia-final-2026-08-17.html`
