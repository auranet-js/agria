# Odczyt Google Ads — 18.09.2026, materiał pod decyzję T-109

**Metoda:** Google Ads API v25, `scripts/google/ads_call.sh`, konto 674-207-1446.
**Okres:** 01–17.09 (17 dni z danymi) · **Zero zmian na koncie — wyłącznie odczyt.**

## 1. Sprostowanie: kampanie nie są i nie były wstrzymane

| kampania | status | serving | budżet | 01–17.09 |
|---|---|---|---|---|
| AGRIA - Rolnictwo | `ENABLED` | `SERVING` | 60 zł/dz | 1 090 wyśw. · 170 klik. · **329,36 zł** (07–17.09) |
| AGRIA - Paszarstwo | `ENABLED` | `SERVING` | 9 zł/dz | 1 059 · 82 · **97,00 zł** (07–17.09) |
| AGRIA - Marka | `ENABLED` | `SERVING` | 5 zł/dz | 264 · 20 · **24,59 zł** (07–17.09) |

**Cały wrzesień 01–17.09: 749,17 zł · 453 kliknięcia · 4 377 wyświetleń · 2 konwersje.**
Sierpień dla porównania (14–31.08): 809,58 zł · 453 kliknięcia · 3 946 wyświetleń · 3 konwersje.

⚠️ **Zapis w rejestrze o „pauzie przedłużonej poza 14.09" jest nieprawdziwy.** Emisja szła nieprzerwanie.

⚠️ **Prognoza „~1 800 zł we wrześniu" też się nie sprawdza.** Rytm dzienny: nd/pn/wt po 68–72 zł,
pozostałe dni 2–17 zł (harmonogram tnie emisję skuteczniej niż limit dzienny).
Projekcja do 30.09: **ok. 1 240 zł** wobec 1 200 zatwierdzonych.

## 2. T-113 — jakość strony docelowej. **Dźwignia NIE jest odblokowana**

Stan 18.09, 65 aktywnych fraz (50 z oceną, 15 bez danych):

| wymiar | poniżej średniej | średnia | powyżej średniej |
|---|---|---|---|
| **jakość strony docelowej** | **40** | 7 | 3 |
| jakość reklamy | 11 | 17 | 22 |
| przewidywany CTR | 15 | 24 | 11 |

Proporcja bez zmian wobec 07.09 (wtedy 34 z 37). **Powód jest teraz znany i nie jest nim treść kart:**

| kampania | grupa | strona docelowa | koszt 01–17.09 |
|---|---|---|---|
| Rolnictwo | Wapno granulowane | `/wapno-granulowane/` | 225,92 zł |
| Rolnictwo | Wapno nawozowe | `/wapno-nawozowe/` | 161,19 zł |
| Rolnictwo | Wapno magnezowe i kreda | `/wapno-nawozowe/` | 156,50 zł |
| Paszarstwo | Kreda pastewna | `/paszarstwo/kreda-pastewna/` | 162,12 zł |
| Marka | Brand | `/` | 43,44 zł |

**Reklamy prowadzą na dwa landingi Ads (`noindex`), nie na karty produktów.** T-136 przepisał
19 kart — ale **543 zł z 749 zł (72%) idzie na strony, których T-136 w ogóle nie dotknął**.
Jedyna kampania kierująca na kartę v2 to Paszarstwo (#307, treść od 14.09) — i to jedyne miejsce,
gdzie ocena strony docelowej może się ruszyć samoistnie, z opóźnieniem właściwym Google.

Landingi **nie są puste** (sprawdzone 18.09: `/wapno-granulowane/` 9 779 znaków tekstu,
`/wapno-nawozowe/` 10 628) — to nie jest powtórka incydentu z sierpnia.

Frazy o największym wolumenie, wszystkie z `BELOW_AVERAGE` na stronie docelowej:
`kreda pastewna` (789 wyśw., QS 3), `kreda pastewna dla kur` (748, QS 4), `kreda nawozowa` (300, QS 3),
`wapno magnezowe` (185, QS 4), `bielik wapno` (139, QS 3). Wyjątki na plus: `wapno granulowane` (QS 7,
strona docelowa `AVERAGE`) i `agria` (QS 8, `ABOVE_AVERAGE`).

## 3. T-110 — co w ogóle liczymy jako konwersję

**Dwie konwersje w 17 dni, obie `phone_click`** (1 × Rolnictwo, 1 × Paszarstwo). Zero `generate_lead`,
zero `form_submit` w Ads. **Koszt konwersji: 374,59 zł.**
Dla porównania wizytówka Google Tarnów dała w tym samym rzędzie czasu 31 kliknięć „zadzwoń" za 0 zł.

## 4. T-111 — rozkład godzinowy. **Zapis wymaga odwrócenia**

| | koszt | udział |
|---|---|---|
| godziny pracy biura 8–16 | **495,13 zł** | **66,1%** |
| poza godzinami pracy | 254,04 zł | 33,9% |

Rejestr mówi „58,6% budżetu wychodzi przy zamkniętym biurze" — dziś jest odwrotnie: **dwie trzecie
budżetu schodzi, gdy telefon jest odbierany.** Szczyt kosztowy: 10:00 (107 zł), 12:00 (74 zł), 15:00 (68 zł).
Emisja zaczyna się o 6:00 i kończy o 21:00. Pozycja T-111 do przeliczenia albo zamknięcia.

## 5. Tabela decyzyjna

| opcja | co daje | co kosztuje | czego nie wiemy |
|---|---|---|---|
| **A. Zostawiamy bez zmian do 30.09** (rekomendacja) | pełny wrzesień na jednej konfiguracji = porównywalny materiał do T-107; sezon rdzenia trwa | ~1 240 zł, czyli 3% nad planem | czy październik powtórzy rytm, czy szczyt podniesie koszt |
| B. Obniżka budżetu Rolnictwa 60 → 45 zł/dz | zejście pod 1 200 zł | utrata udziału w wyświetleniach w szczycie sezonu | o ile spadnie wolumen — przy MANUAL_CPC nieliniowo |
| C. Przepięcie grup Rolnictwa na karty v2 | test, czy nowa treść rusza ocenę strony docelowej | reset historii jakości na tych grupach, utrata optymalizacji landingów pod kontakt | czy karta konwertuje lepiej niż landing — nigdy tego nie mierzyliśmy |
| D. Wstrzymanie do poprawy landingów | zero wydatku | kanał milczy w szczycie rdzenia (X) | czy wrócimy przed listopadem |

**Rekomendacja: A, z jednym zastrzeżeniem.** Materiał do T-107 (31.10, na jego podstawie klient
decyduje o kontynuacji) będzie wiarygodny tylko wtedy, gdy wrzesień i październik pójdą na jednej
konfiguracji. Opcja C jest kusząca, ale **to test, nie poprawka** — i jeśli go robić, to na jednej
grupie („Wapno magnezowe i kreda", 156 zł), nie na całej kampanii.

**Odrzucone:** B — oszczędza 40 zł kosztem widoczności w miesiącu, który ma dowieźć argument handlowy.
D — kanał milczy dokładnie wtedy, kiedy szczyt `wapno magnezowe` (X 3 600) i `wapno tlenkowe` (X 1 000).

**Wykonanie po stronie Janka** — konta nie dotykamy.
