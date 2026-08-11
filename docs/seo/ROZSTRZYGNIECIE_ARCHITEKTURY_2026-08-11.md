# Rozstrzygnięcie architektury: landingi, kategorie, poradniki, Ads

> Data: 2026-08-11. Powód: rekomendacje rozjeżdżały się między lipcem a sierpniem (landingi → rozdzielenie fraz → „może poczekajmy"). Ten dokument zamyka temat jednym ustaleniem opartym na danych, nie na wzorcu z jednego konkurenta.
> Źródła: DataForSEO SERP live (6 fraz, PL desktop, 11.08), DataForSEO Labs ranked_keywords (4 domeny), GSC API (maj–10.08), sezonowość DataForSEO (pull 06.08), baza produkcyjna przez MCP.

---

## 1. Skąd wziął się rozjazd — nazwane wprost

`ROZPISKA_INTENCJA_WOLUMENOWA` z 14.07 postawiła całą strategię landingów komercyjnych na jednym wzorcu: **Biovita jest #1 na „wapno nawozowe" landingiem produktowym bez cen, więc budujemy sześć takich landingów.**

Sprawdzenie pełnego portfela Biovity (11.08) obala ten wzorzec:

| Pozycja | Wolumen | Fraza | URL |
|---|---|---|---|
| 3 | 5 400 | ziemia uniwersalna | `/pl/29-ziemia-uniwersalna.html` |
| 4 | 2 900 | włókno kokosowe | `/pl/316-wlokno-kokosowe…` |
| 3 | 2 400 | kreda | `/pl/314-kreda-do-warzyw-i-ogrodu…` |
| 2 | 2 400 | torf odkwaszony | `/pl/204-torf-odkwaszony.html` |
| 1 | 1 900 | wapno do bielenia drzew | `/pl/155-wapno-do-bielenia-drzew.html` |
| **1** | **1 300** | **wapno nawozowe** | `/pl/16-wapno-nawozowe.html` |
| 3 | 1 600 | ziemia do pomidorów | … |

Biovita to **hurtownia ogrodnicza detaliczna** — ziemia do palm, sukulentów, pelargonii, torf, podłoża. „Wapno nawozowe" to jedna fraza w portfelu ogrodniczym, nie dowód na model biznesowy AGRII. Wyciągnięcie z tego reguły architektonicznej dla producenta surowców było błędem analitycznym.

---

## 2. Właściwy wzorzec: Polcalc — i on robi coś odwrotnego

Polcalc to producent wapna nawozowego, czyli realny odpowiednik AGRII. Porównanie widoczności organicznej (frazy w TOP30, PL):

| Domena | Fraz ≤30 | TOP10 | TOP3 | Wolumen z TOP10 |
|---|---|---|---|---|
| **polcalc.pl** | 172 | **122** | **52** | **71 010** |
| biovita.com.pl | 64 | 31 | 20 | 32 830 |
| orcal.pl | 20 | 12 | 3 | 9 330 |
| **agria.pl** | **6** | **0** | **0** | **0** |

**Skąd Polcalc bierze widoczność:**

| Typ strony | Fraz w TOP10 | Wolumen | Udział |
|---|---|---|---|
| **blog / poradnik** | **116** | **67 460** | **95%** |
| produkt / kategoria | 5 | 3 160 | 4% |
| strona główna | 1 | 390 | 1% |

Producent wapna, który wygrywa rynek organiczny, robi to **treścią poradniczą o glebie** — „rodzaje gleb w Polsce", „badanie gleby", „pH gleby", „wapnowanie trawnika", „niedobór wapnia objawy", nawet „uprawa pomidorów w gruncie" (poz. 1, 1 600/mies.). Landingi produktowe dają mu 4% widoczności.

Dla porównania — struktura Biovity jest dokładnie odwrotna (92% z kart/kategorii), bo Biovita sprzedaje detalicznie i konkuruje ceną w porównywarkach. AGRIA nie robi ani jednego, ani drugiego.

---

## 3. Frazy head komercyjne: kto tam realnie stoi

SERP live, PL desktop, 11.08. **AGRIA jest poza TOP20 na wszystkich sześciu.**

| Fraza | Kto trzyma górę | Bloki SERP |
|---|---|---|
| wapno nawozowe | **OLX #1**, Holcim #2, poradniki, sklepy, Biovita #10 | **local_pack 9 poz.**, PAA, images |
| wapno granulowane | **OLX #1**, sklepy z kartami (Rolmat, Sklepogrodniczy), poradniki | PAA, images |
| wapno palone | **Allegro #1**, iFarmer, Leroy Merlin, OLX #4, Wikipedia | **AI Overview**, knowledge graph |
| wapno magnezowe | **OLX #1**, PH70, Rolmat, Polcalc #5, Allegro | **AI Overview** |
| kreda nawozowa | Nawozy24, **OLX #2**, sklepy, Ceneo | **AI Overview** |
| wapno hydratyzowane | Unibuild, Ramex, Allegro, Leroy Merlin, Castorama | featured snippet |

Trzy fakty operacyjne:

1. **Marketplace'y trzymają pozycję #1 na czterech z sześciu fraz.** OLX jest na szczycie „wapno nawozowe", „wapno granulowane", „wapno magnezowe". To bezpośrednio uzasadnia projekt OLX — wchodzimy tam, gdzie Google już wysyła ruch.
2. **Na „wapno nawozowe" jest local_pack z dziewięcioma wizytówkami** — Wap-Rol, Agro Wap-Trans, Agrokan, Dolpol, GEKOFARM, AgroCalc. Wszystkie mają frazę w nazwie profilu („Nawozy Wapniowe", „Wapno nawozowe"). AGRIA nie istnieje w tym bloku, a wizytówka Tarnów jest dostępna do optymalizacji.
3. **AI Overview na trzech frazach** — to zmienia zwrot z pozycji organicznej i przesuwa wartość w stronę treści cytowalnej, czyli znów poradników.

---

## 4. Co AGRIA ma dzisiaj

**DataForSEO (TOP30, PL):** 6 fraz, zero w TOP10 — wszystkie poradnikowe:

| Poz. | Wolumen | Fraza | URL |
|---|---|---|---|
| 14 | 720 | ile wapna na hektar | `/wapnowanie-gleby/` |
| 17 | 720 | ile wapna na ha | `/wapnowanie-gleby/` |
| 24 | 480 | ile wapna granulowanego na ha | `/wapnowanie-gleby/` |
| 24 | 480 | ile wapna granulowanego na hektar | `/wapnowanie-gleby/` |
| 20 | 390 | wapń skorygowany kalkulator | `/kalkulator-wapnowania/` |
| 28 | 210 | wapno bielik | `/` |

**GSC (dane własne, szersze niż DFS bo obejmują lokalne i mobile):**

- `/wapno-nawozowe-rolnictwo/` na exact „wapno nawozowe": czerwiec 7 wyśw./poz. 12,7 → lipiec 146/11,0 → 1–10.08 **84 wyśw./poz. 10,5, pierwszy klik**. Zaindeksowana, ostatni crawl 10.08.
- `/wapnowanie-gleby/` na „ile wapna granulowanego na hektar": **468 wyśw., poz. 7,7** (1–10.08). Plus wąskie wejścia na frazy komercyjne (poz. 2 na „wapno granulowane", ale tylko 13 wyświetleń — to lokalny/mobilny wycinek, nie pozycja na pełnym wolumenie).
- `/wapno-granulowane/` (opublikowany 06.08): **„URL unknown to Google"** — brak w sitemapie, brak linkowania. Google go nie zna.

**Rozbieżność DFS vs GSC jest sygnałem, nie błędem:** DataForSEO mierzy SERP krajowy, GSC uśrednia po lokalizacjach i urządzeniach. AGRIA rankuje **lokalnie i mobilnie**, nie krajowo. To wzmacnia wniosek o wizytówce.

**GA4 celowo pominięty** — Consent Mode odmawia zgody bez CMP, lipiec pokazał 5 sesji organicznych przy 221 kliknięciach w GSC. Dane nie nadają się do wnioskowania i nie były do niego użyte.

---

## 5. Rozstrzygnięcie — podział ról, obowiązuje do końca sezonu

Konflikt „landing czy kategoria" był źle postawiony. **Landing i organik to dwa różne zadania i nie konkurują ze sobą, jeśli świadomie rozdzielimy kanały.**

| Kanał | Cel | Strony docelowe | Uzasadnienie |
|---|---|---|---|
| **Google Ads** | frazy head komercyjne — natychmiastowy ruch w szczycie sezonu | **landingi** `/wapno-granulowane/`, `/wapno-nawozowe/` | Ads nie wymaga indeksacji. Landing z tabelą parametrów, formami dostawy i CTA „podaj tonaż" daje wyższą ocenę jakości i niższy CPC niż kategoria sklepowa |
| **OLX** | te same frazy head, gdzie marketplace trzyma #1 | ogłoszenia + link na stronę | OLX jest #1 na 3 z 6 fraz — nie walczymy z nim, wchodzimy do środka |
| **SEO organiczne** | frazy poradnikowe i decyzyjne wokół gleby | `/wapnowanie-gleby/`, `/kalkulator-wapnowania/`, poradniki | Droga, którą Polcalc zbudował 95% widoczności. AGRIA już ma tam trakcję i jedyne realne pozycje |
| **Wizytówka Google** | local_pack na „wapno nawozowe" i pochodne | GBP Tarnów | Dziewięć wizytówek w bloku, wszystkie mniejsze od AGRII. Najtańsza niewykorzystana pozycja |

### Konsekwencje operacyjne

**Landingi nie idą do indeksu w sierpniu.** `/wapno-granulowane/` zostaje stroną docelową reklam, poza sitemapą i bez linkowania wewnętrznego. `/wapno-nawozowe/` publikujemy na tych samych zasadach przed startem kampanii. Powód: nie wprowadzamy drugiej własnej strony na frazę, na której kategoria właśnie wchodzi w TOP10, i nie robimy tego w miesiącu o najwyższym wolumenie w roku. Decyzja o wpuszczeniu ich do indeksu zapada **po sezonie, na wyniku** — będziemy mieli dane z Ads o tym, która treść konwertuje.

**Kategoria `/wapno-nawozowe-rolnictwo/` zostaje jedyną stroną organiczną na tę frazę.** Dopracowanie on-page (opis pod listą produktów: tlenkowe vs węglanowe, parametry, FAQ, schema) — treść jest już napisana w `LP_WAPNO_NAWOZOWE_2026-08-06.md` i można ją wykorzystać tutaj zamiast tworzyć konkurenta.

**Blok 1 z ROZPISKI (sześć landingów exact-match) zostaje zawieszony w części organicznej.** Powstają tylko te dwa, które są potrzebne jako cele reklam. Pozostałe cztery (`/wapno-palone/`, `/wapno-hydratyzowane/`, `/wapno-magnezowe/`, `/kreda-nawozowa/`) nie mają uzasadnienia w danych — SERP na tych frazach należy do marketplace'ów i sklepów detalicznych, a nasza droga do widoczności prowadzi przez treść.

**Content organiczny idzie w kierunku Polcalc.** Luka policzona wprost: **39 fraz o wolumenie ≥500 (łącznie 47 210 wyszukań/mies.), gdzie Polcalc jest w TOP10, a AGRIA poza TOP30.** Prawie wszystkie obsługiwane przez treść poradniczą: rodzaje gleb, badanie gleby, pH gleby, niedobór wapnia, rekultywacja, kreda pastewna dla kur, nawozy azotowe. To jest backlog contentowy na wrzesień–październik, oparty na dowodzie, że ta droga działa u bezpośredniego konkurenta.

---

## 6. Czego ten dokument nie zmienia

- Plan Ads wysłany klientowi 06.08 (dwie kampanie, 1 200 zł budżetu, start 14.08) — bez zmian.
- Projekt OLX — bez zmian, dane SERP go wzmacniają.
- Praca lipcowa (4 poradniki, hub, migracja URL) — potwierdzona jako właściwy kierunek, nie zmarnowana.

## 7. Co wymaga decyzji Janka

1. Zatwierdzenie podziału ról z §5 jako obowiązującego do końca października.
2. Czy backlog contentowy z §5 (39 fraz, luka wobec Polcalc) wchodzi do planu wrześniowego zamiast pozostałych czterech landingów.
3. Czy wizytówka Tarnów wchodzi do sierpnia (local_pack na głównej frazie) czy zostaje we wrześniu zgodnie z planem M3.
