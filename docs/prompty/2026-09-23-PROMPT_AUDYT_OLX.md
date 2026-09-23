# Prompt wątku: audyt kanału OLX po pięciu tygodniach — co działa, co przełożyć, co z drugim pakietem

> **Jak używać:** nowa sesja `cd ~/projekty/agria && claude`, wklej:
> `Przeczytaj docs/prompty/2026-09-23-PROMPT_AUDYT_OLX.md i zrób audyt OLX.`
>
> Wątek **analityczny**. Na koncie OLX niczego nie zmieniasz. Wynik to raport z liczbami
> i lista propozycji, każda z liczbą i numerem `T-NNN`. Wykonanie idzie osobnym wątkiem, po „ok” Janka.
> Poprzedni wątek tego typu: `docs/prompty/archiwum/2026-08-28-PROMPT_OLX_WYNIKI.md` → raport
> `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md`. **Nie powtarzaj go** — zacznij od jego rekomendacji
> i sprawdź, co z nich wyszło.

---

## 0. Zasada nadrzędna

Liczby poniżej wskazują, gdzie patrzeć. Nie zwalniają z patrzenia. Każdą przelicz świeżym odczytem
z API, zanim na niej coś oprzesz. Sprzeczność z tym promptem zapisz wprost, jako korektę.

## 1. Stan na 23.09 — punkt startu

- **200 ogłoszeń `active`** od 20.08, 53 miasta, wszystkie z `auto_extend`
  (monitor 23.09 07:25: 0 poza `active`, 0 bez `auto_extend`, 0 poza kontem).
- **Pakiet Premium 200 przedłużył Paweł 16/17.09.** 23.09 zostały **23 dni**, więc **wygasa około 16.10**.
  Decyzja o trzecim cyklu jest po stronie AGRII, tak jak ostatnio. Audyt ma dać Jankowi liczby do tej rozmowy
  **przed 10.10**.
- **Pomiary kumulatywne** (`data/olx/statystyki.json`):

  | Pomiar | Odsłony | Odsłony numeru | Obserwujący |
  |---|---|---|---|
  | 07.09 07:35 | 1 023 | 34 | 29 |
  | 11.09 12:08 | 1 137 | 36 | 31 |
  | 14.09 07:35 | 1 314 | 39 | 36 |
  | 21.09 07:35 | 1 860 | 47 | 43 |

  Wniosek wstępny do sprawdzenia: po zmianach z 11.09 odsłony przyspieszyły mocno (27 → 63 → ok. 78 na dobę),
  **odsłony numeru dużo słabiej** (0,5 → ok. 1,1 na dobę). Ruch rośnie szybciej niż kontakty.
- **Zmiany na koncie po cyklu 1**, każdą trzeba rozliczyć osobno (dziennik M3/M4 w rejestrze):
  - **T-106 (28.08)**: 68 ogłoszeń przełożonych bliżej magazynów (`data/olx/przelozenie-2026-08-28.json`);
  - **T-137 (11.09)**: zdjęcia „z placu”, marka AGRIA w tytułach, 9 martwych ogłoszeń przełożonych;
  - **T-138 (11.09)**: 12 różnych zdjęć głównych zamiast 3, w tym 4 prawdziwe zdjęcia Janka z placu;
  - **T-139 (11.09)**: 56 ogłoszeń do miast konkurencji (`data/olx/przelozenie-2026-09-11.json`);
  - **T-140 (11.09)**: wycofana scena z wywrotką wysypującą w złą stronę.
  Stan przed zmianami z 11.09: `docs/raporty/2026-09-11-OLX_STAN_PRZED_WYMIANA_ZDJEC.md`.
- **Ekonomia z cyklu 1:** koszt kontaktu **12–15 zł netto** wobec kilkuset zł z Google Ads.
  **Wieś bije aglomerację 2,2 razy.** AGRIA jest drugim sprzedawcą kategorii.

## 2. Co ma rozstrzygnąć audyt — osiem pytań

1. **Wynik drugiego cyklu i trend.** Przyrost odsłon i odsłon numeru na dobę w oknach: 20.08–28.08 · 28.08–11.09
   · 11.09–17.09 · 17.09–dziś. Świeży pomiar `statystyki.py --zapisz` na start.
2. **Co dały zmiany.** Dla T-106, T-137/T-138 i T-139 porównaj ogłoszenia zmienione z niezmienionymi w tym samym oknie
   (grupa kontrolna), nie „przed/po” na całym koncie, bo w tle rośnie sezon.
   Osobno: czy prawdziwe zdjęcia z placu biją wygenerowane sceny.
3. **Dlaczego ruch rośnie szybciej niż kontakty.** Konwersja odsłona → numer per ogłoszenie, produkt, miasto,
   zdjęcie główne. Czy nowe odsłony idą z miast konkurencji (T-139), gdzie nie jesteśmy tańsi?
4. **Martwe ogłoszenia.** Lista ogłoszeń z zerem odsłon numeru od wystawienia i od ostatniego przełożenia,
   z odległością do zakładu wysyłkowego produktu. Kandydaci do przełożenia z liczbą, nie z przeczucia.
5. **Zgodność treści ze stroną po T-136.** Wszystkie 19 kart przepisano 14.09. Sprawdź, czy ogłoszenia mówią
   to samo co karty: **ceny** (np. Dolomit od 260 zł/t, węglanowe z Mg odm. 05 36 zł/t), nazwy produktów,
   parametry wyłącznie z kart producentów, opakowania. Zero żargonu (`loco`, MOQ, franco, EXW, HDS).
   Każda rozbieżność = propozycja poprawki z listą ID ogłoszeń.
6. **Zdjęcia — kontrola poprawności.** Przejrzyj wszystkie użyte zdjęcia główne i sceny (lekcja T-140):
   sprzęt, kierunek pracy, towar, brak napisów i logotypów. Odczyt obrazów, nie nazw plików.
7. **Rynek.** Świeży `scripts/olx/market_snapshot.py` i diff z 07.08 (`data/olx/snapshots/2026-08-07-1752.json`)
   oraz 28.08 (`data/olx/market/2026-08-28.json`). **Diff po `user_id`, nie po nazwie sprzedawcy.**
   Kto wszedł, kto wyszedł, ile ogłoszeń mają liderzy, czy ktoś skopiował nasze tytuły lub zdjęcia.
8. **Co dalej przed sezonem zimowym.** Rolnictwo słabnie od października, wapno palone szczytuje w X–XI,
   zimą paszarstwo i hydratyzowane. Zaproponuj skład ogłoszeń na trzeci cykl na liczbach z cyklu 1 i 2.
   **Bez cen usług Auranet**: rewizja sezonowa jest poza wyceną, ale kwotę ustala Janek.

**Czego nie wiemy z danych:** ile odsłon numeru zamieniło się w telefon, a ile w sprzedaż. To wie Paweł.
Zanim zaproponujesz pytanie do Pawła, zrób **quiz do Janka** (`AskUserQuestion`, 2–4 warianty,
twoja rekomendacja pierwsza, opcja „nie wiem, pytamy Pawła”). Na listę do klienta idzie tylko reszta.

## 3. Pułapki pomiarowe — ktoś już na nie wszedł

- **Statystyki są kumulatywne od wystawienia.** Przyrost = różnica pomiarów. Historii w `statystyki.json`
  nie nadpisujesz, dopisujesz z datą.
- **Przełożenie zmienia miasto, nie zeruje licznika.** Przy ogłoszeniach z T-106 i T-139 licz przyrost
  od dnia przełożenia, nie od wystawienia.
- **API gubi zapytania przy równoległości** (przy 8 wątkach ginęła co trzecia). Odczyt mniejszy niż 200 to
  najpewniej zgubione zapytania, nie zgaszone ogłoszenia. Potwierdź w `monitor-log.json`.
- **Lista zbiorcza `GET /partner/adverts` oddaje statusy z opóźnieniem.** Wiarygodny jest odczyt per ID.
  `new` i `disabled` tuż po zmianie są przejściowe (2–3 min moderacji).
- **Stan pakietu:** `GET /partner/users/me/packets` działa. Płatności są tylko w panelu.
- **Odświeżenie z Premium dzieje się samo w 7. dniu.** Nie ma czego klikać, nie proponuj tego jako działania.
- **Nie wnioskuj z `last_refresh_time` konkurencji.** Rozstrzyga diff między snapshotami.
- **Ceny konkurencji:** pole ceny na OLX nie ma jednostki. Porównuj wyłącznie ogłoszenia z ceną za tonę,
  bez kopii. Tania konkurencja to często wapno bez atestu, czyli inny produkt. Do tezy „AGRIA za droga” nie wracamy
  bez tego filtra.
- **Warianty zastosowania tego samego towaru (staw / gleba) celowo dzielą 22 miasta.** To nie duplikat.

## 4. Czego nie robić

- **Nie zmieniaj niczego na koncie OLX.** `PUT /partner/adverts/{id}` podmienia **cały** zasób.
  Jedno niedomknięte pole kasuje numer telefonu, czyli źródło wszystkich kontaktów.
- **Nie pisz do klienta.** Wszystko idzie do Janka na `js@auranet.com.pl` przez `~/bin/send-to-jan`.
- **Nie ruszaj crontaba** inaczej niż przez `~/bin/cron-install`.
- **Nie krytykuj kanału ani własnej roboty w tekstach dla klienta.** Słabe liczby opisujesz i mówisz,
  co z nimi zrobić.
- **Nie generuj nowych zdjęć w tym wątku.** Propozycje nowych scen wypisz z opisem, do akceptu.

## 5. Czym się kończy wątek

1. **Raport** `docs/raporty/2026-09-OLX_AUDYT.md`: odpowiedź na osiem pytań, każda z liczbą i źródłem
   (plik w `data/olx/`, data odczytu). Na końcu sekcja „Czego nie zmierzono”.
2. **Surowe odczyty** w `data/olx/audyt-2026-09/`.
3. **Propozycje** jako nowe wiersze w `docs/REJESTR_ZOBOWIAZAN.md` od **T-142** w górę, zakres **P**
   (obsługa OLX), każda z liczbą ogłoszeń, oczekiwanym efektem i ryzykiem. Nic nie wykonane.
4. **Dla Janka:** wersja HTML raportu na `https://auratest.pl/fe4f58fec53ctmp/agria-olx-audyt-<data>.html`,
   link w czacie. Na górze pięć zdań: co działa, co nie, ile kosztuje kontakt, co proponujemy,
   co z pakietem po 16.10.
5. Wiersz „Audyt OLX” w dzienniku M4 z godzinami, **commit + push**.

## 6. Skąd czytać

| Co | Gdzie |
|---|---|
| Memory | `project_agria_olx_kanal`, `reference_agria_olx_api` (sekrety `~/secrets/olx/`, `~/secrets/agria/olx.txt`) |
| Pomiary | `data/olx/statystyki.json` · `data/olx/monitor-log.json` · `data/olx/wyniki-wlasne.json` |
| Rejestr ogłoszeń | `data/olx/posted.json` (ID, SKU, miasto, tytuł) · `data/olx/adverts-payload.json` |
| Przełożenia | `data/olx/przelozenie-2026-08-28.json` · `data/olx/przelozenie-2026-09-11.json` · `pozycje-*.json` |
| Siatka i popyt | `data/olx/plan-ogloszen.json` · `siatka-miast.json` · `popyt-woj.json` · `miasta-rynek.json` |
| Rynek | `data/olx/snapshots/` · `data/olx/market/` · `scripts/olx/market_snapshot.py` · `olx_market.py` |
| Skrypty | `scripts/olx/` — `statystyki.py`, `monitor.py`, `pozycje.py`, `przelozenie_konkurencja.py`, `fronty_v5.py` |
| Poprzednie raporty | `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md` · `2026-09-11-OLX_STAN_PRZED_WYMIANA_ZDJEC.md` |
| Karty produktów (ceny, parametry) | `docs/produkty/` + produkcja przez `ssh agria-prod` (render, nie baza) |
