# Kontrola indeksacji — 19 kart v2 i Faza 0

**Data pomiaru:** 2026-09-18 · **Metoda:** GSC URL Inspection API (`scripts/gsc_inspect.py`), 24 adresy
**Kontrola przesunięta z 15.09** (pytanie z ADR 24.08, przedefiniowane 09.09)

## Wynik jednym zdaniem

**24 na 24 adresy mają werdykt `PASS` i stan „Strona przesłana i zindeksowana".** Ręczne zgłoszenie
z 09.09 zadziałało i **utrzymało się przez dziewięć dni** — warunek wejścia w Fazę 2 jest spełniony.

## Faza 0 — pięć adresów zgłoszonych ręcznie 09.09

| adres | werdykt | stan | ostatni crawl |
|---|---|---|---|
| `/wapno-do-stawu/` | PASS | zindeksowana | 2026-09-09 |
| `/wapno-do-stabilizacji-gruntow/` | PASS | zindeksowana | 2026-09-09 |
| `/jak-stosowac-wapno-nawozowe/` | PASS | zindeksowana | 2026-09-09 |
| `/wapno-nawozowe-na-trawnik/` | PASS | zindeksowana | 2026-09-09 |
| `/higienizacja-osadow-sciekowych-wapnem/` | PASS | zindeksowana | 2026-09-09 |

Wszystkie pięć miało przed 09.09 werdykt „URL nieznany Google" albo „Discovered — not indexed",
a linkowanie przez 16 dni nie ruszyło żadnego z nich. **Crawl w dniu zgłoszenia, indeks utrzymany
do dziś** — to domyka pytanie postawione 24.08 i potwierdza ustalenie z 09.09: do indeksu wchodzi się
ręcznym zgłoszeniem w panelu, nie linkowaniem i nie Indexing API.

## 19 kart produktów — czy Google pobrał treść v2 (wdrożenia 11–14.09)

| ID | adres | ostatni crawl | treść v2 w indeksie |
|---|---|---|---|
| #310 | `/wapno-nawozowe-rolnictwo/agrobielik-70/` | 2026-09-17 | tak |
| #314 | `/wapno-nawozowe-rolnictwo/weglanowe-granulowane/` | 2026-09-16 | tak |
| #309 | `/wapno-hydratyzowane/bielik/` | 2026-09-16 | tak |
| #319 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-05/` | 2026-09-15 | tak |
| #308 | `/wapno-nawozowe-rolnictwo/mieszanka-tlenkowo-weglanowa/` | 2026-09-15 | tak |
| #306 | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-sypka/` | 2026-09-15 | tak |
| #304 | `/kreda-malarska/kreda-malarska/` | 2026-09-15 | tak |
| #317 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/` | 2026-09-14 | tak |
| #313 | `/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/` | 2026-09-14 | tak |
| #307 | `/paszarstwo/kreda-pastewna/` | 2026-09-14 | tak (dzień wdrożenia — do potwierdzenia przy następnym crawlu) |
| #305 | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-granulowana/` | 2026-09-14 | tak |
| #312 | `/wapno-nawozowe-rolnictwo/oxyfertil-90/` | 2026-09-13 | tak |
| #315 | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/` | 2026-09-12 | tak |
| **#311** | `/wapno-nawozowe-rolnictwo/agrobielik-90/` | **2026-09-09** | **NIE — crawl sprzed wdrożenia** |
| **#318** | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-04/` | **2026-09-09** | **NIE** |
| **#302** | `/wapno-nawozowe-rolnictwo/dolomit/` | **2026-09-09** | **NIE** |
| **#320** | `/wapno-do-oczyszczalni/wapno-palone-mielone/` | **2026-09-09** | **NIE** |
| #316 | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` | 2026-09-09 | bez zmian w T-136 |
| #303 | `/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/` | 2026-09-04 | bez zmian w T-136 |

## Korekta obrazu sytuacji

⚠️ **Cztery karty niezgłoszone 15.09 nie są „poza indeksem" — są w indeksie ze starą treścią.**
Ich ostatni crawl to 09.09, wdrożenie v2 nastąpiło 14.09. Google zna te adresy, ale nie zna nowych
tekstów. To zmienia pilność: zgłoszenie **przyspiesza odświeżenie**, nie warunkuje obecności w indeksie.
Karty crawlowane bez zgłoszeń (#310 — 17.09, #314 — 16.09) pokazują, że serwis jest odwiedzany
na bieżąco, więc te cztery zostaną pobrane same — tylko później i w nieznanym terminie.

⚠️ **T-094 „osiem kart poza indeksem" (pomiar 24.08) jest nieaktualne.** Wszystkie osiem
(#302, #303, #306, #308, #311, #316, #318, #320) ma dziś werdykt `PASS`. Pozycja do zamknięcia w rejestrze
z tym dowodem.

## Próba zgłoszenia 18.09 — odbita

`#311` zgłoszona przez panel GSC o 09:5x: **„Przekroczono limit — nie udało nam się przetworzyć tego
żądania, ponieważ został przekroczony Twój dzienny limit. Spróbuj ponownie jutro."**
Pozostałych trzech nie próbowano — limit jest wspólny dla właściwości.
⚠️ Limit padł **przy pierwszej dzisiejszej próbie**, choć dziś nic wcześniej nie zgłaszaliśmy —
czyli okno limitu nie resetuje się o północy czasu lokalnego albo liczy dłuższy okres niż doba.
Warto to zmierzyć przed planowaniem serii zgłoszeń.

**Do powtórzenia 19.09:** #311, #318, #302, #320.
