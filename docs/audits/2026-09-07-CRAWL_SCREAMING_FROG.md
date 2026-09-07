# Crawl Screaming Frog — 07.09.2026

**Źródło:** eksporty SF z 07.09 (Janek), crawl 228 adresów / 55 stron HTML, z podpiętym GSC i GA4.
Pliki robocze: `tmp/sf/` (poza gitem). Analiza: `tmp/sf/analiza.py`, `analiza2.py`, `serp_hub.py`.
Zestawione z pomiarami z tego samego dnia: `data/kontrole/2026-09-07-odczyt-ads-7-dni.md`.

---

## 1. Jedna strona odpowiada za 90% straty w całym serwisie

| adres | wyświetlenia | kliknięcia | CTR | pozycja | brak kliknięć |
|---|---|---|---|---|---|
| **`/wapnowanie-gleby/`** | **20 106** | **120** | **0,60%** | **5,8** | **~483** |
| `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/` | 1 115 | 10 | 0,90% | 7,6 | ~23 |
| `/wapno-nawozowe-rolnictwo/` | 1 011 | 6 | 0,60% | 8,9 | ~14 |
| pozostałe 8 stron razem | — | — | — | — | ~20 |
| **RAZEM brakujących kliknięć / mies.** | | | | | **~540** |

Hub zbiera **63% wszystkich wyświetleń serwisu** (20 106 z 32 047) i oddaje 120 kliknięć.
Cały serwis robi dziś ~410 kliknięć miesięcznie — **sama ta strona przy normalnym CTR dla pozycji 5,8
dałaby ich ponad 600**. Wszystkie karty produktowe razem to ~57 brakujących kliknięć, czyli
jedna dziesiąta tego.

## 2. Dlaczego hub nie klika — sprawdzone w SERP-ie, nie zgadnięte

SERP mobilny dla `ile wapna granulowanego na hektar` (nasza największa fraza, 1 560 wyświetleń),
pomiar DataForSEO 07.09:

| pozycja bezwzgl. | element |
|---|---|
| **1** | **AI OVERVIEW** — źródła: `polcalc.pl`, `distripark.com`, `wapno-piotrex.pl`, **`agria.pl`** |
| 2 | VIDEO |
| 3 | PEOPLE ALSO ASK |
| dalej | wyniki organiczne: 1. polcalc.pl · 2. distripark.com · **3. agria.pl** · 4. wapno-piotrex.pl |

**Jesteśmy trzecim wynikiem organicznym i jesteśmy cytowani w AI Overview — a mimo to nie mamy
kliknięć, bo nad wynikami stoją trzy bloki, które odpowiadają na pytanie za nas.** To jest strukturalna
przyczyna CTR 0,60% przy „pozycji 5,8": pozycja GSC liczy miejsce wśród wyników, nie ilość ekranu
nad nimi.

⚠️ **To wyjaśnia, dlaczego T-053 nie dało efektu.** Zmiana meta huba z 21.08 nie mogła zadziałać,
bo problem nie leży w snippecie, tylko w tym, co jest **nad** snippetem. Kontrola 04.09 („efektu nie ma")
była poprawna w pomiarze i myląca we wniosku.

**Konsekwencja kierunkowa:** dla osi „ile wapna na hektar" gra idzie o obecność w AI Overview i o PAA,
nie o pozycję organiczną — i tę pierwszą już mamy. Wnioski dla treści: zapytania z tej osi obsługują
odpowiedź na miejscu, więc ruch trzeba budować na zapytaniach **zakupowych**, gdzie AI Overview
nie rozstrzyga (cena, dostawa, forma, ilość na konkretne pole).

## 3. Schema — pełne potwierdzenie T-097

**19 adresów z błędem walidacji, wszystkie ten sam:**
`Either 'schema.org/review', 'schema.org/aggregateRating' or 'schema.org/offers' is required`

To jest dokładnie 19 kart produktowych. Google Product Snippet nie ma z czego zbudować wyniku
z ceną — w SERP-ie pełnym sklepów nasze wyniki są wizualnie ubogie. Zgodne z ADR
`2026-08-19-dwie-warstwy-cen.md`: `offers` budujemy **ręcznie z treści**, nigdy z `_price`.

## 4. Znalezione przy okazji — rzeczy, o których nie wiedzieliśmy

| co | stan | waga |
|---|---|---|
| **`/polityka-prywatnosci/`** | **404** | strona wymagana prawnie, linkowana z serwisu |
| **`/rolnictwo`** | **404** | adres bez slasha, linkowany, brak reguły 301 |
| **`/kontakt/pawel.bigos@agria.pl`** | **404** | adres e-mail wstawiony jako link **względny** zamiast `mailto:` — na stronie kontaktu |
| 5 obrazów bez ani jednego użycia | **1,70 MB** martwego balastu | kreda pastewna ×3 (479, 427, 402 KB), Agrobielik ×2 |
| duplikat tytułu | 2 × „Wapno nawozowe węglanowe zawierające magnez \| AGRIA" | dwie karty konkurują tym samym tytułem |
| brak meta description | `/rodo/`, `/kreda-malarska/`, `/category/poradniki/` | `/kreda-malarska/` to potwierdzenie T-096 |
| tytuły ucinane w SERP | 8 stron powyżej 561 px | |

`/oferta` i `/kontakt` bez slasha oddają **301** — to jest w porządku, nie duplikat.

## 5. Korekta własnej hipotezy z T-116

Po odczycie GSC z 03.09 postawiłem tezę, że karty z nazwą własną w tytule (Oxyfertil 6,05%,
Agrobielik 5,56%) klikają się lepiej niż generyczne, i że robi to **długość tytułu**. Crawl to
**odrzuca**: dla stron z ≥100 wyświetleń tytuły krótsze niż 45 znaków dają CTR **1,01%**, tytuły
45 znaków i dłuższe — **1,16%**. Różnica mieści się w szumie, a i tak jest zaburzona przez hub
(54 znaki, 20 tys. wyświetleń, 0,60%).

**Co zostaje z T-116:** różnicę robi prawdopodobnie sama nazwa własna produktu i typ zapytania
(brandowe kontra generyczne), nie liczba znaków. Zadanie zostaje, ale bez tezy o długości tytułu —
przed przepisaniem 10 kart trzeba sprawdzić SERP-y dla ich fraz, tak jak zrobiliśmy to dla huba.
