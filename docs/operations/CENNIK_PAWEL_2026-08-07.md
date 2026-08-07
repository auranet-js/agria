# Cennik od AGRII — dane źródłowe i mapowanie na karty WooCommerce

> Źródło: mail Pawła Bigosa do Janka, **2026-08-07 12:49** („Aktualizacja cen i dokumentów na stronie"), fwd na `claude@auratest.pl` [201].
> Odpowiedź na `docs/operations/ZAPYTANIE_PAWEL_WIDELKI_CENOWE_2026-08-06.md`.
> Wszystkie kwoty: **netto, loco magazyn — bez transportu** (potwierdzenie Janka 07.08: „cena jak ktoś przyjedzie").

---

## 1. Dane surowe — jak przyszły

| Grupa wg Pawła | Forma | od zł/t netto |
|---|---|---|
| Agrobielik 70 (odm. 02) | luz, całopojazdowa 24 t | 220 |
| | big-bag, od 1 t | 400 |
| | worek 20 kg | **11,50 zł/szt** (= 575 zł/t) |
| | worek 40 kg | **19,00 zł/szt** (= 475 zł/t) |
| Agrobielik 90 (odm. 01), frakcja 0–3 mm | luz 24 t | 750 |
| | big-bag od 1 t | 850 |
| Agrobielik 90 (odm. 01), frakcja 2–8 mm | luz 24 t | 850 |
| | big-bag od 1 t | 940 |
| Oxyfertil 90 (odm. 01) | big-bag od 1 t | 790 |
| Mieszanka tlenkowo-węglanowa | luz 24 t | 120 |
| Wapno hydratyzowane | luz 24 t | 945 |
| | worki 25 kg | 1 220 |
| Wapno palone mielone wysokoreaktywne | luz 24 t | 950 |
| | big-bag od 1 t | 1 200 |
| Węglanowe bez magnezu (odm. 04) | luz 24 t | 57 |
| Węglanowe z magnezem (odm. 05) | luz 24 t | 36 |
| Węglanowe z magnezem (odm. 04) | luz 24 t | 50 |
| Węglanowe bez magnezu granulowane | big-bag od 1 t | 350 |
| | worki 25 kg | 380 |
| Węglanowe z magnezem granulowane | big-bag od 1 t | 370 |
| | worki 25 kg | 410 |
| Kreda nawozowa (odm. 06) | luz 24 t | 125 |
| Kreda nawozowa granulowana (odm. 06) | big-bag od 1 t | 410 |
| | worki 25 kg | 490 |
| Kreda pastewna | luz 24 t | 190 |
| | worki 30 kg | 610 |
| Kreda malarska | worki 30 kg | 645 |

---

## 2. Mapowanie na 19 kart WooCommerce

| ID | SKU | Produkt (WC) | luz 24 t | big-bag | opakowania |
|---|---|---|---|---|---|
| 310 | AGR-001 | Wapno nawozowe tlenkowe Agrobielik 70 | 220 | 400 | 20 kg 11,50/szt · 40 kg 19,00/szt |
| 311 | AGR-002 | Wapno nawozowe tlenkowe Agrobielik 90 | 750 (0–3) · 850 (2–8) | 850 (0–3) · 940 (2–8) | — |
| 312 | AGR-003 | Wapno nawozowe tlenkowe Oxyfertil 90 | — | 790 | — |
| 313 | AGR-004 | Wapno nawozowe tlenkowe zawierające magnez | **brak** | **brak** | — |
| 308 | AGR-005 | Mieszanka tlenkowo-węglanowa | 120 | — | — |
| 315 | AGR-006 | Węglanowe bez magnezu — Odmiana 04 | 57 | — | — |
| 316 | AGR-007 | Węglanowe bez magnezu — Odmiana 05 | **brak** | — | — |
| 314 | AGR-008 | Węglanowe bez magnezu granulowane | — | 350 | 25 kg → 380 zł/t |
| 318 | AGR-009 | Węglanowe z magnezem — Odmiana 04 | 50 | — | — |
| 319 | AGR-010 | Węglanowe z magnezem — Odmiana 05 | 36 | — | — |
| 317 | AGR-011 | Węglanowe z magnezem granulowane | — | 370 | 25 kg → 410 zł/t |
| 302 | AGR-012 | Dolomit | **brak** | **brak** | — |
| 305 | AGR-013 | Kreda nawozowa granulowana | — | 410 | 25 kg → 490 zł/t |
| 306 | AGR-014 | Kreda nawozowa sypka | 125 | — | — |
| 307 | AGR-015 | Kreda pastewna | 190 | — | 30 kg → 610 zł/t |
| 304 | AGR-016 | Kreda malarska | — | — | 30 kg → 645 zł/t |
| 320 | AGR-017 | Wapno palone mielone wysokoreaktywne | 950 | 1 200 | — |
| 309 | AGR-018 | Wapno hydratyzowane Bielik | 945 | — | 25 kg → 1 220 zł/t |
| 303 | (brak) | Kreda czarna (jeziorna) | **brak** | **brak** | — |

**Pokrycie: 15 z 19 kart.**

---

## 3. Luki — do dopytania Pawła

| Produkt | Dlaczego to boli |
|---|---|
| **Dolomit** (302) | fraza „dolomit" ma **6 600 wyszukań/mies** — największy wolumen w całym projekcie. Karta jest, ceny nie ma. W zapytaniu oznaczony „tylko worki 10/25 kg", ale skoro publikujemy zł/t dla worków 25 i 30 kg przy innych produktach, ten argument odpadł. |
| Tlenkowe z magnezem (313) | pominięte bez komentarza |
| Węglanowe bez Mg odm. 05 (316) | pominięte; odm. 04 wyceniona |
| Kreda czarna jeziorna (303) | pominięta; produkt od dawna niejednoznaczny (publish w WC, wycięty z katalogu drukowanego) — dobra okazja, żeby przy okazji rozstrzygnąć jego status |

**Do potwierdzenia przy tej samej rozmowie:** węglanowe z magnezem odm. 05 (36 zł/t) wychodzi **taniej** niż odm. 04 z magnezem (50) i bez magnezu (57), a kreda nawozowa sypka (125) jest ponad dwukrotnie droższa od węglanowego bez magnezu (57) — chemicznie oba to węglan. Może być poprawne (różne złoża i przemiał), ale jeśli to literówka, wyjdzie po publikacji, a nie przed.

---

## 4. Rozstrzygnięcia potrzebne przed publikacją

### 4a. Ceny za worki — decyzja Janka

Paweł podał ceny workowe **i jednocześnie** napisał: *„na ten moment nie będziemy prowadzić sprzedaży po worku"*. Cała zgoda na publikację cen (`ANALIZA_CENY_NA_STRONIE_2026-08-06.md` §2a) opierała się na tym, że **cena za tonę pełni rolę filtra** odsiewającego detalistę — a „11,50 zł za worek 20 kg" robi dokładnie odwrotnie.

Rekomendacja: **publikować wyłącznie przeliczenia na tonę** (575 / 475 zł/t) albo pomijać worki. Bez decyzji nie ruszamy CEN-04/05.

### 4b. Dopisek „mniejsze ilości — wycena indywidualna" — usuwamy

Paweł prosi wprost o jego usunięcie, argumentując, że podane ceny obejmują już sprzedaż 0,5–1 t. To akceptowalne, ale **klauzula prawna zostaje**: „ceny orientacyjne, netto, loco magazyn, nie stanowią oferty handlowej w rozumieniu Kodeksu cywilnego".

### 4c. Transport — rozstrzygnięte

Ceny są loco (odbiór własny). Na stronie musi to być napisane wprost przy widełkach — klient domyślnie zakłada odwrotnie. **To nie jest pytanie do Pawła**, tylko zadanie redakcyjne po naszej stronie.

### 4d. Agrobielik 90 — dwie frakcje, jedna karta

Cennik rozbija Agrobielika 90 na frakcje 0–3 mm i 2–8 mm z różnymi cenami (750/850 vs 850/940), a w WooCommerce to **jedna karta** (311). Do wyboru: jedna cena „od 750 zł/t" z tabelką frakcji w treści, albo rozbicie na warianty. Wraca tu stare otwarte pytanie z `CATALOG_VS_WC_GAP.md`.

---

## 5. Gdzie te ceny mają trafić

| Miejsce | Co |
|---|---|
| Landingi `/wapno-nawozowe/`, `/wapno-granulowane/` (Blok 1 M3) | sekcja „Ile kosztuje…" z widełkami + zastrzeżenie o tonażu i transporcie |
| 19 kart produktowych | cena „od" w WooCommerce → odblokowuje `offers` w schema `Product`, dziś generowanej bez oferty |
| Nowy poradnik „Ile kosztuje wapnowanie hektara" | przeliczenie widełek na hektar; „ile kosztuje tona wapna" ma najwyższy CPC w projekcie (5,32 USD) |
| Google Ads | frazy cenowe dokładane dopiero po wdrożeniu sekcji na landingach |
| OLX | ceny w ogłoszeniach muszą być spójne z tymi widełkami — patrz `OLX_INWENTARYZACJA_2026-08-07.md` |

**Ograniczenie kanałowe:** Paweł podniósł część cen, żeby nie były niższe niż ceny stałych odbiorców (np. Wialan). Ceny na stronie, w Ads i na OLX nie mogą schodzić poniżej tego poziomu — to ogranicza swobodę we wszystkich trzech kanałach naraz.
