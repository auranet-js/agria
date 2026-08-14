# ADR 2026-08-11 — podział ról między Google Ads a SEO organiczne

**Status:** przyjęta 2026-08-11 · obowiązuje do 31.10.2026 (rewizja po sezonie)
**Kontekst:** wątek Google Ads (konto 674-207-1446, start kampanii 14.08). Przy przygotowaniu kampanii wyszły ustalenia dotyczące SEO, które zmieniają wcześniejszy plan contentowy.
**Baseline danych:** `docs/seo/baselines/2026-08-11.json` · odtworzenie pomiaru: `python3 scripts/seo_baseline.py`
**Analiza źródłowa:** `docs/seo/ROZSTRZYGNIECIE_ARCHITEKTURY_2026-08-11.md`

---

## Problem

Rekomendacje rozjeżdżały się między lipcem a sierpniem: najpierw sześć landingów komercyjnych exact-match (`ROZPISKA_INTENCJA_WOLUMENOWA` 14.07), potem rozdzielenie ról landing/kategoria (`REWIZJA_STANU` 06.08), potem wstrzymanie publikacji. Uruchamiamy kampanie Google Ads i trzeba rozstrzygnąć, gdzie kierować reklamy — a odpowiedź zależy od tego, co robimy organicznie. **Ryzyko: optymalizacja pod jeden kanał psuje drugi.**

## Decyzja

**Ads i SEO dostają rozłączne cele i rozłączne strony docelowe.** Landing jest narzędziem konwersji ruchu płatnego, nie narzędziem rankingu organicznego.

| Kanał | Frazy | Strony docelowe | Status stron |
|---|---|---|---|
| **Google Ads** | head komercyjne (wapno granulowane, nawozowe, magnezowe, kreda nawozowa…) | `/wapno-granulowane/`, `/wapno-nawozowe/` | **poza indeksem** — bez sitemapy, bez linkowania wewnętrznego |
| **OLX** | te same frazy head | ogłoszenia + link na stronę | osobny projekt |
| **SEO organiczne** | poradnikowe i decyzyjne wokół gleby | `/wapnowanie-gleby/`, `/kalkulator-wapnowania/`, poradniki | rozwijane |
| **SEO — jedna fraza head** | „wapno nawozowe" | `/wapno-nawozowe-rolnictwo/` (kategoria) | jedyna strona organiczna na tę frazę |
| **Wizytówka Google** | local_pack na „wapno nawozowe" | GBP Tarnów | do uruchomienia |

Cztery pozostałe landingi z Bloku 1 (`/wapno-palone/`, `/wapno-hydratyzowane/`, `/wapno-magnezowe/`, `/kreda-nawozowa/`) **nie powstają.** Zwolniony zasób idzie w treść poradniczą.

## Uzasadnienie — dane z 11.08.2026

**1. Wzorzec, na którym oparto strategię landingów, był błędny.**
`ROZPISKA` z 14.07 wywiodła architekturę z tezy „Biovita jest #1 na «wapno nawozowe» landingiem produktowym". Pełny portfel Biovity: ziemia uniwersalna (5 400), włókno kokosowe (2 900), torf odkwaszony (2 400), ziemia do pomidorów, do palm, do sukulentów, do pelargonii. To hurtownia ogrodnicza detaliczna; „wapno nawozowe" (1 300) jest u niej jedną frazą w portfelu ziemi doniczkowej. Reguła architektoniczna dla producenta surowców została wyciągnięta z jednego punktu danych.

**2. Właściwy odpowiednik AGRII wygrywa treścią, nie landingami.**

| Domena | Fraz ≤30 | TOP10 | TOP3 | Wolumen TOP10 | Udział treści w TOP10 |
|---|---|---|---|---|---|
| polcalc.pl (producent wapna) | 172 | 122 | 52 | 71 010 | **95% blog** |
| biovita.com.pl (hurt. ogrodnicza) | 64 | 31 | 20 | 32 830 | 0% blog |
| orcal.pl | 20 | 12 | 3 | 9 330 | 15% blog |
| **agria.pl** | **6** | **0** | **0** | **0** | — |

Polcalc buduje widoczność treścią o glebie („rodzaje gleb w Polsce", „badanie gleby", „pH gleby", „wapnowanie trawnika", „niedobór wapnia objawy"). Landingi produktowe dają mu 4% widoczności.

**3. Frazy head są zajęte przez marketplace'y — landing ich nie przeskoczy w trzy miesiące.**
SERP PL desktop, 11.08: AGRIA **poza TOP20 na wszystkich sześciu** frazach. OLX trzyma #1 na „wapno nawozowe", „wapno granulowane", „wapno magnezowe"; Allegro i Leroy Merlin na „wapno palone". AI Overview na trzech frazach. Na „wapno nawozowe" dodatkowo **local_pack z 12 pozycjami** — wizytówki mniejszych konkurentów (Wap-Rol, Dolpol, Agrokan, GEKOFARM, AgroCalc), AGRIA nieobecna.

**4. AGRIA ma realną trakcję wyłącznie na treści.**
GSC, okno 12.07–08.08: `/wapnowanie-gleby/` — **9 867 wyświetleń, 59 kliknięć, poz. 6,8** (motor całej witryny przy 14 413 wyświetleniach ogółem). `/kalkulator-wapnowania/` — poz. 6,2. Wszystkie 6 fraz AGRII w TOP30 wg DataForSEO to poradniki.

**5. Kategoria na „wapno nawozowe" rośnie i nie wolno jej w tym przeszkadzać.**
`/wapno-nawozowe-rolnictwo/`: czerwiec 7 wyświetleń / poz. 12,7 → lipiec 146 / 11,0 → okno 28-dniowe 221 / **10,9** z pierwszym kliknięciem. Wprowadzenie drugiej własnej strony na tę frazę w szczycie sezonu (sierpień = 9 900 wyszukań „wapno granulowane", najwyżej w roku) oznaczałoby kilkutygodniowe rozstrzyganie przez Google w najgorszym możliwym momencie.

**6. Ads nie wymaga indeksacji strony docelowej.** To jest fakt techniczny, który usuwa konflikt: landing może obsługiwać reklamy, mieć własne CTA „zapytaj o ofertę — podaj tonaż", tabelę parametrów i formy dostawy, i jednocześnie nie istnieć w indeksie organicznym.

## Przyczyna pierwotna — zmierzona kanibalizacja (uzupełnienie 13.08)

> Dopisane, bo w kolejnych sesjach wracało pytanie „dlaczego landingi są poza indeksem" i odpowiedź brzmiała „bo tak ustaliliśmy". Ustaliliśmy tak z powodu, który da się pokazać liczbami — i ten powód jest ważniejszy od samej reguły, bo obowiązuje także dla stron, o których jeszcze nie rozmawialiśmy.

**Reguła nie wzięła się z ostrożności, tylko z cofnięcia własnego planu po pomiarze.** Kolejność zdarzeń: `ROZPISKA` 14.07 planuje sześć landingów **do indeksu** → raport M2 z 03.08 (§4.2) po raz pierwszy mierzy kanibalizację na własnych danych → `REWIZJA` z 06.08 stwierdza, że kategoria weszła na poz. 11,0, więc landing byłby **drugą własną stroną na tę samą frazę** → ten ADR.

### Dowód A — im więcej własnych URL na frazę, tym niżej wszystkie

GSC, query × page (lipiec; kolumna „naszych URL" to liczba adresów agria.pl notowanych na frazę):

| Fraza | Naszych URL | Najlepsza pozycja | Wyświetlenia |
|---|---|---|---|
| ile wapna granulowanego na hektar | 1 | **7,9** | 791 |
| ile wapna na hektar | 1 | **9,0** | 899 |
| wapno nawozowe | 1 (patrz korekta 13.08) | **10,9** — trend 12,7 → 11,0 → 10,9 | 221 |
| wapno węglanowe | 2 | 10,0 / 36,4 | 74 / 38 |
| **wapno bielik** | **6** | **15,3**, jeden klik | 18 |

**Weryfikacja na żywo 13.08** (okno 14.07–10.08, 285 klik / 15 666 wyśw.) — zależność potwierdzona w drugim, niezależnym oknie:

| Fraza | Naszych URL | Najlepsza pozycja |
|---|---|---|
| ile wapna granulowanego na hektar | 1 | **7,8** (892 wyśw.) |
| ile wapna na hektar | 1 | **8,8** (1 005 wyśw.) |
| wapno granulowane | 1 | **2,1** |
| wapno węglanowe | 2 | 9,6 / 35,6 |
| wapno tlenkowe | 3 | 2,8 (hub) / 23,4 (karta) / 44 (stary URL) |
| **wapno bielik** | **5** | **15,7**, jeden klik |

**Korekta jednego twierdzenia:** „wapno nawozowe" nie ma już jednego URL-a, tylko dwa — `/wapno-nawozowe-rolnictwo/` poz. 10,7 (225 wyśw.) i `/wapnowanie-gleby/` poz. 2 przy **jednym** wyświetleniu. Hub nie zabiera kategorii ruchu (wycinek lokalny/mobilny), więc decyzja stoi, ale teza „jedyna strona organiczna na tę frazę" opisuje zamiar, nie stan faktyczny w GSC.

„wapno bielik" zeszło z 6 na 5 URL-i — stare adresy 301 wygasają z indeksu zgodnie z przewidywaniem `REWIZJA` §5. Kanibalizacja rezydualna (karta + kategoria + strona główna + kategoria hydratyzowanych) pozostaje.

Rozbicie frazy markowej „wapno bielik" (210 wyszukań/mies.): `/wapno-hydratyzowane/…bielik-luz/` 15,3 · `/wapno-hydratyzowane/bielik/` 16 · `/` 28,2 · `/wapno-hydratyzowane/` 55 · `/wapno-nawozowe-hurt/…agrobielik-70-big-bag/` 58 · `/wapno-nawozowe-rolnictwo/agrobielik-70/` 62.

**Sześć własnych stron na własną markę, najlepsza na piętnastej pozycji.** Każda fraza z jednym adresem jest w TOP10. To jest cena rozbicia sygnału i to jest powód, dla którego nie dokładamy stron na frazy, na których już coś mamy.

### Dowód B — nasza treść wypiera nasz produkt

Fraza „wapno tlenkowe": poradnik `/wapnowanie-gleby/` stoi na **2,8**, karta produktu na **41**. Google wybiera naszą treść poradniczą, nie naszą kartę — nawet na frazie produktowej.

### Dowód C — strony produktowe nie rankują ani u nas, ani u lidera kategorii

DataForSEO, TOP30 PL, baseline 11.08: AGRIA ma 6 fraz w TOP30 i **wszystkie sześć to poradniki i kalkulator — ani jedna strona produktowa**. Polcalc, jedyny właściwy komparator (producent wapna nawozowego, 122 frazy w TOP10, wolumen 71 010): **95% widoczności z bloga, 4% z produktów i kategorii**.

Dokładanie landingów produktowych to więc dokładanie stron w klasie, która nie rankuje nigdzie — przy jednoczesnym rozbijaniu sygnału tam, gdzie coś już mamy.

### Dowód D — timing

Sierpień to **9 900 wyszukań „wapno granulowane"**, najwyżej w roku, a `/wapno-nawozowe-rolnictwo/` właśnie wchodzi do TOP10. Druga własna strona na tę frazę oznaczałaby kilkutygodniowe rozstrzyganie przez Google w najlepszym miesiącu sezonu.

### Dlaczego Ads są wyjątkiem

**Reklamy nie wymagają indeksacji.** Landing poza indeksem daje pełną korzyść płatną (dopasowana strona docelowa → wyższa ocena jakości → niższy CPC) przy zerowym koszcie organicznym. To jedyna rola, w której dodatkowa strona na frazę head nie szkodzi.

### Stan izolacji — sprawdzony 13.08

| Kontrola | Wynik |
|---|---|
| URL Inspection obu landingów (13.08, live) | **„Adres URL jest Google nieznany"**, brak crawlu — `/wapno-granulowane/` jest nieznany tydzień po publikacji. Kontrolnie `/wapno-nawozowe-rolnictwo/`: PASS, zaindeksowana, crawl 10.08 |
| Linki wewnętrzne z `/`, `/wapnowanie-gleby/`, `/poradniki/`, `/wapno-nawozowe-rolnictwo/`, `/oferta/` | **0** z każdej |
| Obecność w `page-sitemap.xml` | brak |
| Meta robots landingu | `index, follow` — **izolacja stoi na braku odkrycia, nie na dyrektywie** |

Ostatni wiersz to jedyna luka techniczna: `noindex` domknąłby izolację twardo i jest zgodny z tą decyzją, ale nie został wdrożony — do rozstrzygnięcia przy najbliższej pracy na landingach.

## Konsekwencje

- `/wapno-granulowane/` (opublikowany 06.08) **zostaje poza sitemapą i bez linkowania** — dotychczasowy stan przestaje być zaniedbaniem, staje się decyzją.
- `/wapno-nawozowe/` powstaje przed 14.08 na tych samych zasadach. Publikacja wyłącza przy okazji zgadywanie WP, które dziś kieruje ten adres na poradnik o trawniku.
- Treść z `LP_WAPNO_NAWOZOWE_2026-08-06.md` zostaje wykorzystana **dwa razy**: jako landing reklamowy i jako opis kategorii (wersja skrócona, bez powielania całości).
- Backlog contentowy wrzesień–październik: **39 fraz o wolumenie ≥500, łącznie 47 210 wyszukań/mies.**, gdzie Polcalc jest w TOP10, a AGRIA poza TOP30. Lista w analizie źródłowej §5.
- Wizytówka Tarnów wchodzi jako osobne zadanie (local_pack na głównej frazie).
- Plan Ads wysłany klientowi 06.08 pozostaje bez zmian — decyzja nie dotyka niczego, co obiecaliśmy.

## Co ta decyzja unieważnia

| Ustalenie | Data | Nowy status |
|---|---|---|
| „Biovita jako wzorzec architektury" | 14.07 | **obalone** — zły komparator |
| Blok 1: sześć landingów exact-match do indeksu | 14.07 | **zredukowane do dwóch, poza indeksem** |
| „Rozdzielenie ról landing/kategoria przez title i H1" | 06.08 | **zastąpione** — rozdział przez kanał, nie przez meta |
| „Nie mamy ani jednej strony komercyjnej" jako diagnoza | 14.07 | **nieaktualne** — kategoria rankuje i rośnie |

## Jak to zweryfikować (i co by ją obaliło)

Pomiar odtwarzalny: `python3 scripts/seo_baseline.py` — zapisuje snapshot do `docs/seo/baselines/` i pokazuje deltę wobec poprzedniego. Skrypt mierzy również konkurentów, więc weryfikuje **samą przesłankę decyzji**, nie tylko jej skutek.

**Kontrole:** 01.09 · 01.10 · 01.11 (rewizja całości po sezonie).

| # | Hipoteza | Miernik | Baseline 11.08 | Próg potwierdzenia | Co ją obala |
|---|---|---|---|---|---|
| 1 | Landing nie szkodzi kategorii, bo jest poza indeksem | poz. `/wapno-nawozowe-rolnictwo/` na „wapno nawozowe" | 10,9 · 221 wyśw. | ≤10 przy ≥200 wyśw. do 30.09 | spadek poniżej 13 przy utrzymanym wolumenie |
| 2 | Treść jest właściwą drogą dla producenta wapna | udział blog/poradnik w wolumenie TOP10 Polcalc | 95% | utrzymanie ≥80% | spadek <50% przy wzroście produktowych = teza wymaga rewizji |
| 3 | AGRIA rośnie tam, gdzie inwestujemy w treść | wyświetlenia `/wapnowanie-gleby/` (28 dni) | 9 867 · poz. 6,8 | wzrost m/m | spadek dwa okresy z rzędu |
| 4 | Landingi pozostają poza indeksem | URL Inspection obu landingów | „URL unknown" | bez zmian do 31.10 | wejście do indeksu = alarm w skrypcie, sprawdzić przyczynę |
| 5 | Landing konwertuje ruch płatny lepiej niż kategoria | koszt konwersji z Ads per strona docelowa | brak (start 14.08) | landing ≤ kategoria | jeśli kategoria konwertuje taniej — kierować Ads na kategorię i wycofać landingi |

**Warunek rewizji przed terminem:** jeśli którakolwiek z hipotez 1–4 zostanie obalona przed 01.10, ADR wraca na stół bez czekania na koniec sezonu.

**Argument, który po sezonie może wpuścić landingi do indeksu:** dane konwersji z Ads (hipoteza 5). Jeśli landing okaże się wyraźnie skuteczniejszy sprzedażowo od kategorii, to jest przesłanka, żeby dać mu również rolę organiczną — ale wtedy poza szczytem sezonu i z przemyślanym przekierowaniem ról.

## Otwarte, do decyzji Janka

1. Czy backlog 39 fraz wchodzi do planu wrześniowego w miejsce czterech skasowanych landingów.
2. Czy wizytówka Tarnów rusza w sierpniu (local_pack na głównej frazie), czy zostaje we wrześniu zgodnie z planem M3.
