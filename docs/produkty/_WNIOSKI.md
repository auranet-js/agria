# Baza wiedzy produktowej — wnioski jako fakty do decyzji D1–D4

> 10.09.2026 · zlecenie `docs/prompty/2026-09-10-PROMPT_BAZA_WIEDZY_PRODUKTOWEJ.md` · źródła: 19 plików `docs/produkty/<slug>.md`,
> `README.md` (indeks), `_macierz-fraz.csv` (581 fraz). **Bez rekomendacji architektury** — D1–D4 rozstrzyga Janek quizem.
> GSC: okno 2026-06-09 … 2026-09-06. Planer: Google Ads API, PL, średnia 12 mies. Zapytania: CPT `agria_inquiry`, 11 prawdziwych IV–IX.
> Koszt DataForSEO całości: **0,5424 USD**.

---

## 1. Najkrócej

1. **Żadna z 19 kart na stronie nie jest w pełni zgodna z kartą PDF.** 16 ma rozbieżności, 3 (#303, #304, #316) nie mają karty AGRII,
   więc nie mają źródła prawdy. Wzór jest wszędzie ten sam: atrybuty `pa_*` (w schemacie) = karta PDF, a **widoczna tabela i treść**
   to tekst n8n DescWriter z 13.03 z dopisanymi zastosowaniami i liczbami bez źródła `[J 10.09]`.
2. **Sprzedaż skupia się na 8 produktach:** 11 zapytań ofertowych dotyczy #312 (2), #320 (2), #309 (2), #311, #315, #319, #305, #303 (po 1).
   Pozostałe 11 produktów — 0, w tym flagowy według karty Agrobielik 70.
3. **Ruch organiczny kart jest mały i skupiony:** 115 kliknięć w 90 dniach na 19 kart, z czego 5 kart ma 95 (#312 38, #315 17, #309 16, #319 13, #310 11).
4. **Popyt stoi na rodzaju wapna i na producencie/zakładzie, a nazwy produktów mają go mało.** Na frazy producentów i kopalń
   (Siarkopol, Nordkalk, Lhoist, Jażwica, Celiny, Laskowa, Wapniak Kornicki, Grankal) serwis ma **0 wyświetleń** — żadna karta ich nie wymienia jako źródła towaru.
5. **Z kart wynikają wyraźne grupy** (rodzaj × producent × zastosowanie) i **pary produktów o tych samych parametrach w różnych cenach** (§4).
6. **19/19 kart jest w indeksie** (URL Inspection 10.09), ale 5 weszło dopiero 06–09.09 — ich wynik w GSC będzie mierzalny od ok. połowy września.

---

## 2. Stan kart

### 2.1 Zestawienie

| WC | produkt | GSC 90 dni klik / wyśw | zapytania | stan | najważniejsze |
|---|---|---|---|---|---|
| 312 | Oxyfertil 90 | 38 / 575 | 2 | rozbieżności | najlepsza karta serwisu; konkurent CARLOS ta sama cena 790 zł/t, wyżej w SERP |
| 315 | Węglanowe bez Mg odm. 04 | 17 / 1 652 | 1 | rozbieżności | FAQ podaje frakcje 0–0,09 / 0–0,2 / 0–5 mm, karta i tabela 0–2 mm |
| 309 | Bielik | 16 / 621 | 2 | rozbieżności | luz 14–16 t (karta) vs 24 t (strona, cennik) |
| 319 | Węglanowe z Mg odm. 05 | 13 / 573 | 1 | rozbieżności | MgO „min. 8–20%" na karcie vs wymaganie „co najmniej 15%" w obu atestach |
| 310 | Agrobielik 70 | 11 / 237 | 0 | rozbieżności | tabela z innymi zastosowaniami; plony, pH, odkażanie bez źródła |
| 304 | Kreda malarska | 6 / 284 | 0 | brak karty | żaden parametr niepotwierdzony |
| 305 | Kreda nawozowa granulowana | 5 / 363 | 1 | luki, rozbieżności | BB 500 kg (karta, zapytanie) vs „od 1 t" (strona) |
| 307 | Kreda pastewna | 3 / 234 (+149 klik. Ads) | 0 | luki, rozbieżności | „37% CaO" na karcie vs „Ca min. 37%" (Lhoist) i „CaO min. 50%" (Celiny) — dokumenty od klienta 11.09; brak drobiu w treści przy ≈2 780 wyszukań/mies. |
| 313 | Tlenkowe z Mg | 2 / 420 | 0 | rozbieżności, brak ceny | zawartość zapisana trzema sposobami |
| 314 | Węglanowe bez Mg granulowane | 2 / 849 | 0 | luki, rozbieżności | wysiew siewnikiem z NPK (karta) — na stronie brak |
| 306 | Kreda nawozowa sypka | 2 / 82 | 0 | rozbieżności | odm. 06a (karta) vs 06 (cennik) |
| 317 | Węglanowe z Mg granulowane | 0 / 399 | 0 | luki, rozbieżności | BB 600 kg (karta) vs 1 t; title identyczny z #318 |
| 303 | Kreda czarna | 0 / 6 | 1 | brak karty, brak ceny | zapytanie z `/wapno-granulowane/`, gdzie produktu nie ma |
| 308 | Mieszanka tlenkowo-węglanowa | 0 / 2 | 0 | luki, rozbieżności | parametry #310 za 120 zamiast 220 zł/t |
| 311 | Agrobielik 90 | 0 / 0 (indeks 09.09) | 1 | rozbieżności | 90% CaO (karty) vs typ min. 80% (atest odm. 01) |
| 316 | Węglanowe bez Mg odm. 05 | 0 / 0 (indeks 09.09) | 0 | brak karty, brak ceny | producent sprzeczny: Lhoist vs Celiny |
| 318 | Węglanowe z Mg odm. 04 | 0 / 0 (indeks 09.09) | 0 | rozbieżności | CaO 41% (karta) vs 38,5% (atest 7/26) |
| 302 | Dolomit | 0 / 0 (indeks 09.09) | 0 | rozbieżności | karta PDF i sekcja ceny opisują dwa różne towary |
| 320 | Wapno palone mielone | 0 / 0 nowy adres (stary 20 klik.) | 2 | rozbieżności | pH „>16" (karta) vs 12,3 / 12,8 (karty charakterystyki) |

### 2.2 Rozbieżności w parametrach — karta PDF ↔ atest / strona / cennik (tylko zapisane, nic nie poprawiane)

| WC | parametr | karta PDF | drugie źródło |
|---|---|---|---|
| 311 | CaO | min. 90% | atest 47/25: typ odm. 01 „min. 80%", zmierzone 94,3% |
| 318 | CaO | min. 41% | atest 7/26: 38,5%; producent: 35–45% |
| 319 | MgO | min. 8–20% | atesty 8/26 i 9/26: wymaganie odm. 05 „co najmniej 15%" |
| 320 | pH | >16 | KCh Nordkalk 2025: 12,3; KCh Trzuskawica 2007: 12,8 |
| 315 | frakcja | 0–2 mm | FAQ na stronie: 0–0,09 / 0–0,2 / 0–5 mm |
| 302 | forma i frakcja | worki 10/25 kg, 0–2 mm | sekcja ceny na stronie: luz 24 t, 0,1–0,4 / 0,4–0,8 / 1–3 mm |
| 309 | luz | 14–16 t | strona i cennik: 24 t |
| 317 | big-bag | 600 kg | cennik, strona, OLX: 1 t |
| 305 | big-bag | 500 kg | strona, cennik, OLX AGRII: „od 1 t" (zapytanie 05.08 — 500 kg) |
| 306 | odmiana | 06a | cennik: 06 |
| 307 | zawartość wapnia | min. 37% CaO | Lhoist Bukowa (karta IV 2026 i worek 30 kg): Ca min. 37%; Celiny (F13, 29.04.2026): CaO min. 50%, Ca min. 389 g/kg |
| 313 | zawartość | „70/25 %" (tabela) i „min. 70% CaO + 25% MgO" (tekst) | meta strony: „CaO+MgO min. 70% (w tym MgO 25%)" |

### 2.3 Rozbieżności systemowe — te same na wielu kartach

- **Widoczna tabela ≠ atrybuty `pa_*`** — zastosowania i „dodatkowe zastosowania" podmienione (stawy, rekultywacja, odkażanie,
  mineralizacja mułu), wiersz „Forma dostawy" usunięty. Atrybuty w schemacie = karta PDF. `[J 10.09]`: tekst DescWriter, bez źródła.
- **Liczby bez źródła w treści:** plony „+15–20%" (#310) i „+15–30%" (#315, #319), pH „>12" na kartach, które pH nie mają, dawki dla stawów
  na kartach, które ich nie podają (#311, #312), „spełnia kryteria dopłat ARiMR" (#319), „atest do każdej partii" (meta #307).
- **Atrybut „Odmiana" bez pokrycia w dokumentach:** #313 „02", #314 „04", #317 „04", #302 „05" — karty PDF odmiany nie podają.
- **„Wapno czynne min. 80%" i klasa CL 90** na #309 i #320 — wprowadzone przez Auranet (plan `9681a80` 14.07, wykonanie `6a70484` 15.07);
  w 31 PDF-ach z `/do-pobrania/` „wapna czynnego" nie ma.
- **Sprzeczność na jednej stronie:** „35-letnie doświadczenie" (FAQ) i „37 lat" (formularz) — m.in. #310, #306, #307, #309.
- **Karty PDF sprzeczne wewnętrznie (tekst vs tabela):** #310 luz 24 / 24–26 t · #315 luz 24 / 25–27 t · #314 3 / 4 magazyny ·
  #318 kopalnia „w Łagowie" / magazyn Chęciny · #319 działanie 3–6 mies. / „do roku". Karta ↔ atest: #319 kod Kostomłotów 26-085 vs 26-025.

### 2.4 Dokumenty

- Atesty OSChR na `/do-pobrania/` mają tylko 4 produkty: #310, #311, #318, #319. Karty charakterystyki (Nordkalk) — produkty Nordkalku.
- **Ogłoszenia OLX AGRII deklarują „atest OSChR"** dla #305, #306, #317 i #312 — na `/do-pobrania/` żadnego z nich nie ma.
- **11.09 klient przysłał karty producentów kredy pastewnej** (Lhoist Bukowa, Kopalnia Celiny) ze zdjęciem worka 30 kg i numerami weterynaryjnymi
  PL2613013p / PL26043170p — `data/produkty/klient/kreda-pastewna/`, opis w `kreda-pastewna.md` §2.4.
- Żadna karta produktu nie linkuje do własnej karty PDF ani atestu (tylko ogólnie do `/do-pobrania/`).
- Konkurencja eksponuje atest i nazwę zakładu: CARLOS (Agrobielik 70 „Zakład Sitkówka", atest OSChR Kielce), Industria (Dewonit z nazwą kopalni).

---

## 3. Popyt a pokrycie

### 3.1 Rodzaj wapna (największy popyt w bazie)

| fraza | wyszukań/mies. | produkty z kart | nasz najlepszy adres w GSC, poz. |
|---|---|---|---|
| dolomit | 6 600 | #302 | — (intencja rozszczepiona: minerał, kruszywo, suplement) |
| wapno granulowane | 4 400 | #314, #317, #305 | hub 2,1 (45 wyśw.); w SERP 10.09 AGRIA poza top 20 |
| wapno gaszone | 2 900 | #309 | — |
| wapno hydratyzowane | 2 400 | #309 | kategoria 39,5 |
| wapno palone | 2 400 | #320 (+ #310, #311 tlenkowe palone) | 1 wyśw. |
| kreda pastewna | 2 400 | #307 | stary adres `/kreda-pastewna/` 21,7 |
| wapno magnezowe | 1 900 | #317, #318, #319, #313, #302 | #317 48,9 |
| wodorotlenek wapnia | 1 900 | #309 | — |
| wapno nawozowe | 1 300 | 15 kart | kategoria 11,1 (667 wyśw.) |
| tlenek wapnia | 1 300 | #320 | — |
| kreda nawozowa | 1 000 | #305, #306 | #305 23,9 |
| wapno węglanowe | 1 000 | #314, #315, #316 | **#315 9,9 (988 wyśw.)** |
| wapno tlenkowe | 720 | #310, #311, #312, #313 | #313 25,5 |

### 3.2 Zastosowanie i odbiorca

| fraza | wyszukań/mies. | co mówią karty | nasz adres |
|---|---|---|---|
| kreda pastewna dla kur · kreda dla kur · wapno dla kur niosek · … | 1 600 + 720 + 210 + 110 + 90 + 50 ≈ **2 780** | #307: „Ca w dietach zwierzęcych", bez gatunków | — (1 wiersz: `/paszarstwo/` 21,5) |
| kreda do stawu | 1 300 | stawy na kartach #305, #306 (bez dawki) | — |
| wapno do stawu | 390 | dawka dla stawów tylko na #310 (60–100 kg/1000 m³) | — |
| wapno tlenkowe do stawu | 90 | #310 | hub 2 |
| dolomit na trawnik · do ogrodu | 590 + 70 | #302: worki 10/25 kg | — |
| higienizacja / wapnowanie osadów ściekowych | 30 + 20 | #320, #311, #312 (karty: pierwsze zastosowanie) | `/wapno-do-oczyszczalni/` 13,5–16,6 (304 wyśw.) |
| wapno do szamba | 70 | — | `/wapno-do-oczyszczalni/` 11,1 |
| stabilizacja gruntu wapnem · wapno do stabilizacji gruntu | 50 + 10 | żadna karta nie ma stabilizacji jako zastosowania; #311 0–3 mm ma „stabilizacje gruntów" w **Segmencie** | — |

⚠️ KR z 19.05 podawał dla stabilizacji **720/mies.**; dwie frazy zmierzone 10.09 dają razem 60. Nie wiadomo, jakie frazy liczył KR — niezweryfikowane.

### 3.3 Producent, zakład, marka — serwis 0 wyświetleń na każdej

| fraza | wyszukań/mies. | produkt(y) z kart | uwaga |
|---|---|---|---|
| siarkopol | 1 300 | #302 | |
| nordkalk (+ wapno 480, wapno nordkalk 210) | 880 | #308, #309, #310, #311, #320 | obejmuje też produkty Nordkalku, których AGRIA nie ma (Standard Cal, Atrigran) |
| wapniak kornicki | 720 | #305 (atrybut marki, karta nie podaje) | producent KZK Kornica na 2. miejscu SERP |
| lhoist · lhoist bukowa · lhoist tarnów opolski · lhoist górażdże | 480 · 390 · 170 · 70 | #312, #313, #314, #315, #307, #304 | |
| kopalnia jażwica · kopalnia laskowa · kopalnia winna · kopalnia celiny | 390 · 320 · 170 · 320 | #318 · #319 · #319 · #314, #315, #307 | SERP-y nawigacyjne (dojazd, praca) — bez ofert wapna |
| grankal | 110 | #314, #317, #303 (strona) | na OLX 38 z 40 ogłoszeń z „grankal" to AGRIA |
| wapno trzuskawica · wapno bielik trzuskawica | 30 · 10 | #310 (zakład Sitkówka, dawniej Trzuskawica) | |
| dewonit | 10 | #318, #319 (nazwa z atestów) | nazwy nie ma w treści żadnej karty |

### 3.4 Nazwy produktów

Agrobielik ≈ 20/mies. (SERP: `agrobielik 70` abs 1) · Oxyfertil ≈ 140 (karta 5,9) · marka Bielik ≈ 500 (`wapno bielik` 210 → karta 12,2) ·
Mieszanka ≈ 20 (SERP abs 1) · `wapno odmiana 04` 30 → #315 3,6 · `wapno odmiana 05` 20 → #319 2,9 · czarna kreda / kreda jeziorna 720 / 320
(produkt bez karty) · `kreda malarska` 320 → karta 7,9.

### 3.5 Frazy dawkowe i „ile na hektar"

Zbiera je hub `/wapnowanie-gleby/`: `ile wapna granulowanego na hektar` 480/mies. → 2 033 wyśw., poz. 7,2, 5 klik.; dawkowe o wapnie
tlenkowym ≈ 290 wyśw., o magnezowym ≈ 500 wyśw. Karty produktów dostają z nich pojedyncze wyświetlenia.

---

## 4. Grupy produktów wynikające z kart (fakty, nie propozycja kategorii)

### 4.1 Według rodzaju (karta PDF)

| rodzaj | produkty |
|---|---|
| tlenkowe bez Mg | #310 (70%), #311 (90%), #312 (90%) |
| tlenkowe z Mg | #313 |
| mieszanka tlenkowo-węglanowa | #308 |
| palone mielone | #320 |
| hydratyzowane | #309 |
| węglanowe bez Mg | #314 (granulat), #315 (odm. 04), #316 (odm. 05, brak karty) |
| węglanowe z Mg + dolomit | #317 (granulat), #318 (odm. 04), #319 (odm. 05), #302 |
| kreda nawozowa | #305 (granulat), #306 (sypka), #303 (brak karty) |
| kreda paszowa / malarska | #307 / #304 (brak karty) |

### 4.2 Według producenta i zakładu

| producent · zakład / kopalnia | produkty |
|---|---|
| Nordkalk · Sitkówka | #308, #309, #310, #311, #320 |
| Lhoist · Tarnów Opolski, Górażdże, Bukowa, Częstochowa (magazyny) | #312, #313, #314, #315, #307, #304 (+ #316 wg tabeli) |
| Celiny (Hochel) | #314, #315, #307 (+ #316 wg atrybutu) |
| Grankal · Draby | #314, #317 (+ #303 wg strony) |
| Industria · Jażwica / Laskowa + Winna — nazwa handlowa „Dewonit" | #318 / #319 |
| Siarkopol · magazyn Tarnobrzeg | #302 |
| KZK Kornica | #305 |
| Kopalnia Drugnia · Pierzchnica | #306 |

### 4.3 Według pierwszego zastosowania na karcie

| zastosowanie z karty | produkty |
|---|---|
| gleby średnie i ciężkie | #310, #308 |
| gleby lekkie (i piaszczyste) | #313, #314, #315, #317, #318, #319, #302, #305, #306 |
| higienizacja osadów (oczyszczalnie) | #311, #312, #320 · stabilizacja osadów: #309 |
| stawy — w zastosowaniu | #310 (z dawką), #305, #306 (bez dawki) |
| pasza | #307 |
| budownictwo (zaprawy, tynki) | #309 |

Oczyszczalnie: kategoria `/wapno-do-oczyszczalni/` pokazuje tylko #320; #311 i #312 (higienizacja jako pierwsze zastosowanie) i #309 nie są w jej listingu.

### 4.4 Pary o tych samych parametrach na kartach, w różnych cenach (cennik 07.08, zł/t netto)

| para | co wspólne na kartach | cena |
|---|---|---|
| #310 Agrobielik 70 ↔ #308 Mieszanka | min. 70% CaO, 2–6 t/ha, 2–4 tyg., Nordkalk | 220 ↔ 120 |
| #311 Agrobielik 90 2–8 mm ↔ #312 Oxyfertil 90 | wiersze parametrów identyczne; karta #312: „alternatywa dla Agrobielika 90" | 850 luz / 940 BB ↔ 790 BB |
| #314 węglanowe granulowane ↔ #305 kreda granulowana | min. 50% CaO, granulat 3–6 mm | 350 BB ↔ 410 BB |
| #315 węglanowe odm. 04 ↔ #306 kreda sypka | min. 50% CaO, sypkie | 57 ↔ 125 |
| #319 / #318 ↔ #302 Dolomit | 0–2 mm, 1,5–6 t/ha, 3–6 mies. (#319: CaO+MgO min. 45% jak dolomit) | 36 / 50 ↔ 260–280 |
| #314 ↔ #317 (Grankal) | granulat 3–6 mm, 1–6 t/ha, magazyn Draby | 350 ↔ 370 BB |

---

## 5. Fakty pod decyzje D1–D4 (bez rekomendacji)

**D1 — podział kategorii.** Dziś 15 z 19 produktów w jednej kategorii „Wapno nawozowe". Karty dzielą produkty na 9 rodzajów (§4.1),
8 producentów (§4.2) i 6 zastosowań (§4.3). Popyt jest większy na rodzaj (§3.1: 13 fraz rodzajowych 720–6 600/mies.) niż na zastosowanie —
wyjątki z popytem: drób ≈ 2 780, staw ≈ 1 870, trawnik/ogród ≈ 660. Oczyszczalnie: frazy małe (30–70), ale kategoria ma 304 wyśw.
na frazach o osadach i 2 z 11 zapytań (#320). Żadna kategoria nie stoi w top 10 GSC na frazie rodzajowej — najlepsza: `wapno nawozowe` 11,1; w top 10 jest tylko karta #315 na `wapno węglanowe` (9,9).

**D2 — cel reklam.** Ads 13.08–09.09 (`landing_page_view`): 745 klik., 1 294 zł, 3 konwersje. Z kart produktów reklamy prowadziły
**tylko na #307** (149 klik., 1 konw.); na pozostałe 18 kart — 0. Strony z największym wydatkiem: `/wapno-nawozowe/` 539 zł (2 konw.),
`/wapno-granulowane/` 351 zł (0). CPC w planerze dla fraz produktowych: od 0,17 zł (`wapno tlenkowe cena`) do 4,03 zł (`ile wapna tlenkowego na hektar`).

**D3 — stabilizacja gruntów.** Żadna karta PDF nie ma stabilizacji gruntów jako zastosowania; #311 (0–3 mm) ma ją w wierszu „Segment".
Strona stabilizacji listuje tylko #320 i podaje parametry i dawkę, których karta #320 nie zawiera. Popyt zmierzony 10.09: 50 + 10/mies. (§3.2, wobec 720 w KR 19.05).
Stary serwis miał dla #320 dwie strony, dziś obie 404 (plik `wapno-palone-mielone.md`).

**D4 — staw.** Stawy są w zastosowaniu kart #310, #305, #306; dawkę podaje tylko #310. `/wapno-do-stawu/` listuje 6 produktów.
Popyt: `kreda do stawu` 1 300, `wapno do stawu` 390, `wapno tlenkowe do stawu` 90, `kreda granulowana do stawu` 50, `wapno hydratyzowane do stawu` 40 —
serwis ma na nich razem 3 wyświetlenia w 90 dniach.

---

## 6. Pytania — najpierw do Janka (quiz), dopiero reszta do klienta

Pełne listy w §9 każdego pliku (≈ 65 pytań). Zgrupowane:

| grupa | pytania | produkty |
|---|---|---|
| **A. Czy AGRIA to sprzedaje** | #303 kreda czarna (było zapytanie 25.08) · #316 odm. 05 bez Mg · wapno palone kruszone i w bryłach (karty na `/do-pobrania/`) · worek 30 kg Bielika · frakcje 0–0,09 / 0–0,2 / 0–5 mm odm. 04 · dolomit w workach 10/25 kg vs luz | 303, 316, 309, 315, 302 |
| **B. Dokumenty** | atesty OSChR obiecane w OLX (#305, #306, #312, #317) · karta Lhoist dla #304, #312, #313 · karta/atest dla #303, #316 · atest #311 — która frakcja | 305, 306, 312, 317, 304, 313, 303, 316, 311 |
| **C. Parametry sprzeczne z atestem / KCh** | #311 90 vs 80% · #318 41 vs 38,5% · #319 MgO 8 vs 15% · #320 pH >16 vs 12,3 · #307 pH >12 i egzotermia (T-079 errata) | 311, 318, 319, 320, 307 |
| **D. Logistyka** | luz 24 / 24–26 / 25–27 / 14–16 t · big-bag 500 / 600 kg / 1 t · który magazyn przy cenie (#312, #315, #319, #307) · zakład produkcji (#309, #311, #312, #313, #320, #302) | wiele |
| **E. Nazwy handlowe producentów** | czy wolno pisać „Dewonit" (#318, #319), „Wapniak Kornicki" (#305), „Grankal HumiPlus" (#303), „Calcifertil/Grankal" (#314), „Bukowiak/Opolwiak" (#315), „Oxyfertil Ca 90" / „70/25" (#312, #313) | wiele |
| **F. Ceny brakujące** | #313, #316, #303 · worek #305 25 kg (w cenniku jest, na stronie nie) | 313, 316, 303, 305 |


### Decyzje Janka `[J 11.09]`

- **#303 Kreda czarna i #316 Węglanowe bez Mg odm. 05 — zostają tak, jak są.** Bez zmian w WC i na stronie; pytania A dla tych dwóch nie idą do klienta.
- **Parametry sprzeczne z atestami (#311, #318, #319, #320) — zostawiamy bez zgłaszania.** Karta PDF pozostaje źródłem prawdy; rozbieżność
  zapisana tylko w plikach bazy (grupa C nie idzie do klienta).
- **Nazwy w treści: tylko producent i kopalnia** (np. Nordkalk, Sitkówka, Lhoist, Kopalnia Jażwica, Siarkopol). **Marek producenta nie używamy**
  (Dewonit, Wapniak Kornicki, Grankal HumiPlus, Calcifertil, Bukowiak, Opolwiak, Oxyfertil Ca 90) — grupa E rozstrzygnięta.

---

## 7. Zauważone obok, nie ruszam

- `FAKTY_KLIENTA` §3 pisze „zero `offers`" — nieaktualne od T-097 (07.09); także „#302 Discovered — not indexed" (24.08) — dziś PASS.
- `REJESTR` T-094 notuje #303 i #306 jako nieznane Google — oba są dziś w indeksie.
- `OLX_KONKURENCJA_2026-08-07.md` nazywa CARLOS-a „pośrednikiem odsprzedającym produkt AGRII" — CARLOS sprzedaje Agrobielik z odbiorem w Sitkówce.
- Adresy starego serwisu `/oferta/<segment>/<produkt>/` zwracają 404 (sprawdzone curl 10.09 na dwóch: `/oferta/rolnictwo/wapno-nawozowe-tlenkowe-palone-odmiany-01-02-i-03/`,
  `/oferta/budownictwo/wapno-hydratyzowane/`); wg plików #320 i #309 miały 4 130 i 1 517 wyświetleń w 2026. Archiwum 20.02: 301 „brak potwierdzenia wdrożenia".
- `/kreda-pastewna/` przekierowuje 301 na kategorię `/paszarstwo/`, nie na kartę; Google nadal pokazuje stary adres na `kreda pastewna` (poz. 21,7).
- Nowy adres #320 ma 0 wyświetleń, ruch (20 klik.) idzie na stary `…-luz-24t/` (301 od 08.07, Google ostatnio pobrał go 02.07).
- Własne ogłoszenia OLX AGRII podają zastosowania spoza kart („Agrobielik 90 pod zboża i rzepak", „Oxyfertil — gleby średnie i ciężkie").
- Tabela w prompcie przypisywała kartę Trzuskawicy „odm. 03" do #311 — nie dotyczy (atest #311 = odm. 01).
