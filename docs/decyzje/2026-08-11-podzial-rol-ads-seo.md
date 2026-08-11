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
