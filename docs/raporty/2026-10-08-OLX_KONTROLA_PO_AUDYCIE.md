# OLX — kontrola 15 dni po audycie (T-142…T-146)

**Pomiar:** 08.10.2026 12:51, `statystyki.py --zapisz` (nr 15 w `data/olx/statystyki.json`), 200/200.
**Punkt odniesienia:** 23.09 10:49 (nr 12) — pomiar sprzed zmian z audytu `docs/raporty/2026-09-OLX_AUDYT.md`.
**Okno:** 23.09 10:49 → 08.10 12:51 = **15,08 doby**. Wskaźniki „na 100 ogł./dobę” = przyrost ÷ liczba ogłoszeń ÷ doby × 100.

## Wynik w jednym akapicie

Po audycie kanał daje **2,52 odsłony numeru na dobę** wobec 1,60 średnio przez pierwsze 34 dni . Wejść
przybyło mniej (70,9 odsłony/dobę wobec 75,9 tuż po podbiciu 19.09; średnia pierwszych 34 dni 60,0), więc
przyrost kontaktów idzie z konwersji, nie z ruchu.
Konwersja odsłona → numer **3,55%** wobec 2,67%. Koszt odsłony numeru przy tym tempie **ok. 17 zł netto**
(audyt: 27 zł). Rekomendacja: **odnowić Premium 200**.

## Liczby

| | 23.09 10:49 | 08.10 12:51 | przyrost | na dobę |
|---|---|---|---|---|
| Odsłony | 2 022 | 3 091 | +1 069 | 70,9 |
| Odsłony numeru | 54 | 92 | **+38** | **2,52** |
| Obserwujący | 45 | 64 | +19 | 1,26 |

Ogłoszeń z choć jedną odsłoną numeru: **67** (23.09: 43). Pomiary cronu w oknie: 28.09 (62 numery) i 05.10 (82) —
najszybszy odcinek to 28.09 → 05.10: **+20 numerów w 7 dób**.

### Grupy (odsłony / odsłony numeru na 100 ogł./dobę)

| Grupa | n | przed: 14.09 → 23.09 | po: 23.09 → 08.10 | werdykt |
|---|---|---|---|---|
| **T-144** przełożone martwe | 29 | 14,3 / **0,00** | 34,1 / **1,14** | zadziałało — z zera do poziomu reszty (1,28); 5 numerów |
| reszta (bez T-144) | 171 | 42,9 / 0,96 | 35,7 / 1,28 | tło |
| **T-146** Mg gran. → węgl. gran. | 8 | 35,6 / 0,00 | 26,5 / **1,66** | kontakty są (2 — Żabno, Wieliczka), ale wejść mniej niż 20 starych węglanowych (40,8 / 1,99) |
| węglanowe gran. dotychczasowe | 20 | 44,3 / 2,74 | 40,8 / 1,99 | najmocniejszy produkt nadal |
| **„do stawu”** po zmianie tytułu | 17 | 17,4 / 0,64 | 15,2 / **1,56** | tytuł nie obciął ruchu (−13% wejść przy −13% całości), numery ×2,4; 4 numery |
| pozostałe (nie staw) | 183 | 40,7 / 0,84 | 37,3 / 1,23 | tło |
| wszystkie | 200 | 38,8 / 0,82 | 35,4 / 1,26 | |

Zastrzeżenia: grupy są małe (T-146 = 8 ogłoszeń, 2 numery) — kierunek, nie dowód. Okno „przed” T-144
to te same ogłoszenia jeszcze w starych miastach. T-144: rozkład odsłon w oknie 0–18, mediana 5;
jedno ogłoszenie z 29 nadal bez ani jednej odsłony.

## Koszt odsłony numeru

1 275,60 zł netto na cykl (pakiet 975,60 + obsługa 300) ÷ odsłony numeru w przeliczeniu na 30 dni:

| Tempo z okna | numery / 30 dni | koszt |
|---|---|---|
| po audycie (23.09 → 08.10) | 75,6 | **16,9 zł** |
| drugi cykl (14.09 → 08.10) | 65,6 | 19,4 zł |
| całość kanału (20.08 → 08.10) | 56,6 | 22,5 zł |

Wszystkie trzy w obiecanym przedziale 6,50–30 zł. To koszt **odsłony numeru**, nie zapytania — bez liczby
telefonów od Pawła nie wiemy, ile z nich zadzwoniło.

## Pakiet i rynek

- `monitor.py` 08.10: 200 `active`, 200 `auto_extend`, **7 dni pakietu** — wygasa **16.10 11:19**,
  bez odnowienia wszystkie 200 gasną jednego dnia (ogłoszenia ważne do 19.10).
- Spis rynku `market_snapshot.py --spis` (`data/olx/market/spis-2026-10-08.json`) vs 23.09:
  rynek **6 748 → 5 676 ogłoszeń** (−16%), sprzedawców 451 → 448 (70 weszło, 73 wyszło).
  AGRIA 200 = **3,5% rynku** (23.09: 3,0%), **6.** miejsce ex aequo (23.09: 8.).
  Wyszło kilku stuprocentowych graczy (WAP POL 200 → 0, Agrokorkus, WAP-TRANS, agrogran1980, Groch-Tra 100 → 0);
  urośli Wapna Świętokrzyskie (269 → 311) i Produkcja Nawozów Mineralnych (101 → 200).

## Do rozmowy z AGRIĄ (przez Janka, przed 10.10)

1. **Odnowić Premium 200** — kontakty przyspieszyły (2,52/dobę), koszt odsłony numeru spadł z 27 do ok. 17 zł,
   a rynek się przerzedza, więc nasze 200 ogłoszeń waży więcej.
2. Pytanie do Pawła: **ile telefonów „z OLX” i ile zamówień** od 20.08 — bez tego nie przeliczymy kosztu zapytania.

## Otwarte z audytu (bez zmian, nie ruszane)

Tytuły „big bag 1 t” przy granulowanych (karty: 500/600 kg) · „kreda nawozowa” w tytule węglanowego odm. 04 ·
`wysyp-podworze` · rewizja sezonowa składu (listopad).
