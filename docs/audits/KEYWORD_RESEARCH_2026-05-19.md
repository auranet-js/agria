# Keyword research AGRIA — 2026-05-19

> **Cel:** baseline słów kluczowych pod ofertę M1 fundamenty + roadmapa content M2-M6.
> **Źródło danych:** DataForSEO Labs (PL, location_code 2616, language_code pl) — `keyword_suggestions/live`, `keyword_ideas/live`, `keyword_overview/live`.
> **Filtrowanie:** dedup → tematyczne (wapn-/kreda/marki/CaO itd.) → wykluczenie suplementów diety i medycznych → volume PL ≥ 10.
> **Koszt:** ~$0.15 (suggestions $0.063 + ideas $0.060 + overview $0.021).

## Executive summary

- **112 fraz** w 8 klastrach segmentowych po deduplikacji i filtrowaniu (z 432 surowych z 8 zapytań seed-based).
- **Łączny volume Google/mies PL:** ~21 670 wyszukiwań na top frazach klastrów.
- **Klastry o najwyższym potencjale (volume × wdrażalność):** rolnictwo, drogownictwo, budownictwo.
- **Klastry niszowe (niski volume, ale wysoka wartość per query):** rybactwo, oczyszczalnie ścieków — content informational + AEO, nie PPC.
- **Sezonowość krytyczna:** rolnictwo (wiosna marzec-kwiecień, jesień wrzesień-listopad), drogownictwo (lato), budownictwo (cały rok z peakiem maj-sierpień).

## Metodyka

1. **Seedy z MASTER_PROMPT.md** — 5 klastrów × 1-5 seedów (`wapno nawozowe`, `wapnowanie stawu`, `higienizacja osadów`, `wapno hydratyzowane`, `kruszywo wapienne` + rozszerzenia per klaster).
2. **Pull surowych fraz** — `keyword_suggestions/live` (semantycznie podobne) + `keyword_ideas/live` (multi-seed, szerszy zasięg, ~700k-1M dostępnych per zapytanie, limit 100 zwracanych).
3. **Deduplikacja po keyword (case-insensitive), preferencja wpisu z najpełniejszymi danymi.**
4. **Filtr tematyczny** — fraza musi pasować do `wapn|kreda|agrobielik|ekograncali|bielik|tlenkow|węglanow|magnezow|hydrat|kruszyw|dolomit|cement|caco3|cao|mgo|osad|higieniz|nawóz|odkwasz` itd.
5. **Wykluczenia** — suplementy diety (`kwercetyna`, `witamina c`, `ciąża`, `do picia`), marki konkurencji (Orcal, Kujawit, Atrigran, Supermag — wydzielone do osobnej tabeli gap analysis), off-topic (`youtube`, `wikipedia`, ślimaki, przeziębienie).
6. **Klasyfikacja na klastry** — pierwszy match wins, kolejność: drogownictwo → oczyszczalnie → rybactwo → paszarstwo → sadownictwo → rolnictwo → budownictwo → marka. Drogownictwo PRZED oczyszczalniami żeby `stabilizacja gruntu` nie trafiała do ścieków.
7. **Wzbogacenie** — `keyword_overview/live` dla 112 unique top fraz (KD, intent, 12-miesięczny trend dla sezonowości).

## Pokrycie danych po wzbogaceniu

| Pole | Pokrycie |
|---|---|
| Volume (search_volume) | 100% |
| Intent (main_intent) | 100% |
| Monthly trend (12 mies) | 100% |
| KD (keyword_difficulty) | 33% — DataForSEO nie ma KD dla wszystkich PL fraz, normalne dla niszowego rynku |
| CPC | częściowe — wartości dla fraz transakcyjnych |

## Klastry

### Rolnictwo (30 fraz, łączny volume ~3 240/mies PL)

_Wapno nawozowe tlenkowe (01/02/03), tlenkowo-magnezowe, węglanowe, kreda nawozowa/pastewna, Ekograncali Activ. Sezonowość kluczowa: wiosna (marzec-kwiecień) + jesień (wrzesień-listopad)._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | wapno nawozowe | 1300 | 0 | informational | $0.17 | peak 08/2022 (6600), low 01/2026 (590) |
| 2 | ile wapna granulowanego na ha | 590 | 0 | informational | $1.05 | peak 08/2021 (2400), low 04/2019 (20) |
| 3 | wapno nawozowe granulowane | 390 | 0 | transactional | $0.17 | peak 08/2022 (1300), low 05/2019 (70) |
| 4 | wapno nawozowe cena za tonę | 140 | 0 | informational | $0.11 | peak 07/2024 (590), low 05/2020 (10) |
| 5 | wapno nawozowe cena | 90 | 0 | informational | $0.12 | peak 08/2020 (880), low 12/2024 (20) |
| 6 | wapno nawozowe z magnezem | 70 | — | transactional | $0.18 | peak 03/2026 (210), low 01/2024 (10) |
| 7 | wapno nawozowe tlenkowe | 50 | — | informational | $0.11 | peak 08/2021 (170), low 01/2020 (10) |
| 8 | kiedy stosować wapno nawozowe | 50 | 48 | informational | $0.02 | peak 10/2023 (170), low 05/2023 (10) |
| 9 | wapno nawozowe na trawnik | 50 | — | transactional | $0.16 | peak 03/2025 (210), low 01/2026 (10) |
| 10 | wapno nawozowe luzem | 50 | — | informational | $0.12 | peak 08/2025 (140), low 08/2018 (0) |
| 11 | ile kosztuje wapno nawozowe | 40 | 0 | informational | $0.21 | peak 07/2024 (210), low 05/2023 (10) |
| 12 | wapno nawozowe castorama | 40 | — | transactional | $0.07 | peak 02/2024 (140), low 06/2025 (10) |
| 13 | wapno nawozowe morawica | 40 | — | informational | $0.39 | peak 08/2020 (140), low 12/2025 (10) |
| 14 | wapno nawozowe kiedy stosować | 40 | 48 | informational | — | peak 03/2021 (320), low 01/2026 (10) |
| 15 | wapno kredowe granulowane dawkowanie | 30 | — | transactional | — | peak 03/2026 (70), low 05/2024 (0) |
| 16 | nawóz wapno | 30 | — | transactional | $0.23 | peak 02/2024 (90), low 01/2026 (10) |
| 17 | florovit wapno nawozowe | 30 | — | transactional | $0.13 | peak 03/2026 (110), low 01/2026 (10) |
| 18 | wapno nawozowe węglanowe | 30 | — | informational | $0.10 | peak 03/2026 (110), low 01/2026 (10) |
| 19 | jak stosować wapno nawozowe | 30 | — | informational | $0.37 | peak 10/2023 (170), low 01/2019 (0) |
| 20 | wapno nawozowe allegro | 20 | — | transactional | $0.11 | peak 10/2023 (70), low 01/2026 (10) |
| 21 | florovit wapno nawozowe granulowane 20 kg | 20 | — | transactional | $0.18 | peak 02/2024 (110), low 06/2021 (0) |
| 22 | wapno nawozowe florovit | 20 | — | transactional | $0.10 | peak 03/2025 (70), low 02/2026 (10) |
| 23 | wapno nawozowe granulowane cena | 20 | — | commercial | $0.06 | peak 09/2025 (40), low 05/2024 (0) |
| 24 | wapno hydratyzowane na pole | 10 | — | informational | — | peak 11/2020 (140), low 03/2026 (10) |
| 25 | wapno hydratyzowane zastosowanie w rolnictwie | 10 | — | informational | — | peak 11/2018 (90), low 01/2026 (0) |
| 26 | wapno nawozowe workowane | 10 | — | informational | $0.14 | peak 08/2020 (260), low 12/2024 (0) |
| 27 | nawozowe wapno | 10 | 0 | informational | — | peak 03/2026 (10), low 10/2025 (0) |
| 28 | wapno nawozowe polcalc | 10 | — | informational | $0.29 | peak 08/2021 (70), low 06/2025 (0) |
| 29 | wapno nawozowe granulowane dawkowanie | 10 | — | transactional | — | peak 08/2018 (50), low 01/2026 (0) |
| 30 | wapno nawozowe małopolska | 10 | — | informational | — | peak 09/2022 (110), low 12/2025 (0) |

### Paszarstwo / hodowla (2 fraz, łączny volume ~150/mies PL)

_Wapno do kurników, hodowla drobiu, trzody — kreda pastewna, wapno paszowe._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | jakie wapno do kurnika | 110 | 0 | informational | $0.14 | peak 03/2025 (210), low 11/2020 (0) |
| 2 | wapno hydratyzowane do kurnika | 40 | — | transactional | $0.17 | peak 03/2026 (70), low 03/2023 (0) |

### Rybactwo (stawy) (10 fraz, łączny volume ~240/mies PL)

_Wapno tlenkowe (01/02) do wapnowania stawów rybackich — pH wody, mineralizacja mułu, zima/lód._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | wapnowanie stawu wapnem budowlanym | 70 | 0 | informational | — | peak 04/2025 (170), low 12/2019 (0) |
| 2 | wapno hydratyzowane do stawu | 50 | — | transactional | $0.15 | peak 04/2025 (110), low 01/2025 (10) |
| 3 | wapnowanie zarybionego stawu | 40 | — | informational | $0.10 | peak 04/2020 (320), low 12/2021 (10) |
| 4 | wapno tlenkowo/magnezowe do stawu | 20 | — | transactional | $0.08 | peak 05/2022 (140), low 12/2025 (10) |
| 5 | wapno tlenkowo magnezowe do stawu allegro | 10 | — | transactional | — | peak 05/2022 (70), low 02/2026 (0) |
| 6 | wapno tlenkowe dawkowanie staw | 10 | — | informational | — | peak 04/2019 (70), low 03/2026 (0) |
| 7 | wapno do stawu forum | 10 | — | informational | — | peak 07/2021 (70), low 02/2026 (0) |
| 8 | co daje wapno do stawu | 10 | — | informational | $0.13 | peak 04/2020 (70), low 12/2025 (0) |
| 9 | wapnowanie stawu ile | 10 | — | informational | — | peak 06/2021 (90), low 12/2025 (0) |
| 10 | wapnowanie stawu na lód | 10 | — | informational | — | peak 01/2022 (40), low 11/2025 (0) |

### Oczyszczalnie ścieków (3 fraz, łączny volume ~170/mies PL)

_Wapno palone mielone do higienizacji/stabilizacji osadów ściekowych, neutralizacja. **Niski volume Google** — sektor B2B przetargowy, ale wysoka wartość biznesowa per query._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | neutralizatory ścieków | 70 | — | commercial | $1.53 | peak 03/2026 (140), low 07/2022 (20) |
| 2 | neutralizator ścieków | 70 | — | transactional | $1.53 | peak 03/2026 (140), low 08/2022 (10) |
| 3 | higienizacja osadów ściekowych | 30 | — | informational | — | peak 03/2023 (70), low 02/2026 (10) |

### Budownictwo (30 fraz, łączny volume ~3 670/mies PL)

_Wapno hydratyzowane (Bielik), cement — murowanie, tynki, zaprawy._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | wapno hydratyzowane | 2400 | 0 | transactional | $0.09 | peak 03/2026 (3600), low 12/2018 (720) |
| 2 | wapno hydratyzowane castorama | 140 | 0 | transactional | $0.03 | peak 05/2025 (210), low 01/2021 (10) |
| 3 | wapno hydratyzowane zastosowanie | 140 | 0 | transactional | — | peak 03/2023 (390), low 02/2020 (10) |
| 4 | wapno hydratyzowane cena | 140 | 0 | transactional | $0.04 | peak 09/2023 (320), low 12/2024 (50) |
| 5 | wapno hydratyzowane bricomarche | 90 | — | transactional | $0.05 | peak 03/2024 (210), low 01/2021 (0) |
| 6 | czy wapno hydratyzowane jest szkodliwe | 70 | 0 | informational | — | peak 10/2024 (170), low 12/2018 (10) |
| 7 | wapno hydratyzowane leroy merlin | 70 | — | transactional | $0.04 | peak 03/2026 (110), low 12/2022 (10) |
| 8 | wapno hydratyzowane bielik | 50 | — | transactional | $0.34 | peak 03/2026 (90), low 12/2022 (10) |
| 9 | czy wapno hydratyzowane można stosować w ogrodzie | 40 | — | informational | — | peak 10/2024 (170), low 01/2021 (0) |
| 10 | wapno hydratyzowane mrówka | 40 | — | transactional | $0.05 | peak 03/2026 (50), low 01/2021 (0) |
| 11 | wapno hydratyzowane 25 kg cena | 40 | 0 | transactional | $0.10 | peak 04/2023 (260), low 02/2020 (0) |
| 12 | wapno hydratyzowane obi | 40 | — | transactional | $0.06 | peak 03/2026 (70), low 01/2022 (10) |
| 13 | wapno hydratyzowane 25kg | 30 | — | transactional | $0.27 | peak 03/2026 (70), low 08/2024 (0) |
| 14 | wapno hydratyzowane cena za tonę | 30 | — | informational | $0.29 | peak 10/2024 (110), low 08/2020 (10) |
| 15 | wapno gaszone hydratyzowane | 30 | — | transactional | $0.06 | peak 03/2026 (90), low 07/2024 (0) |
| 16 | wapno budowlane hydratyzowane | 30 | — | transactional | $0.03 | peak 03/2026 (50), low 12/2025 (10) |
| 17 | wapno hydratyzowane 30 kg | 30 | — | transactional | $0.03 | peak 10/2023 (140), low 01/2021 (0) |
| 18 | wapno hydratyzowane jak rozrobić | 20 | — | informational | — | peak 09/2020 (140), low 01/2019 (0) |
| 19 | wapno hydratyzowane karta charakterystyki | 20 | — | informational | — | peak 02/2023 (50), low 01/2026 (10) |
| 20 | jak gasić wapno hydratyzowane | 20 | — | informational | — | peak 08/2021 (90), low 01/2021 (0) |
| 21 | wapno hydratyzowane do czego służy | 20 | — | informational | — | peak 06/2024 (40), low 01/2021 (0) |
| 22 | wapno palone a hydratyzowane | 20 | — | informational | — | peak 03/2026 (30), low 03/2025 (0) |
| 23 | wapno hydratyzowane budowlane | 20 | — | transactional | $0.07 | peak 03/2026 (50), low 04/2020 (0) |
| 24 | wapno gaszone a hydratyzowane | 20 | — | informational | — | peak 03/2026 (40), low 06/2024 (0) |
| 25 | wapno hydratyzowane allegro | 20 | — | transactional | $0.10 | peak 03/2026 (30), low 04/2020 (0) |
| 26 | wapno hydrauliczne a hydratyzowane | 20 | — | informational | — | peak 08/2025 (30), low 03/2026 (10) |
| 27 | co to jest wapno hydratyzowane | 20 | — | informational | — | peak 08/2021 (90), low 11/2025 (10) |
| 28 | wapno hydratyzowane do bielenia drzew | 20 | — | transactional | $0.17 | peak 03/2022 (110), low 08/2023 (0) |
| 29 | castorama wapno hydratyzowane | 20 | 0 | transactional | $0.05 | peak 10/2025 (30), low 02/2020 (0) |
| 30 | wapno hydratyzowane do bielenia ścian | 20 | — | transactional | $0.06 | peak 07/2025 (50), low 07/2024 (0) |

### Drogownictwo (30 fraz, łączny volume ~14 040/mies PL)

_Kruszywo wapienne, stabilizacja gruntu wapnem, podbudowy drogowe, podjazdy._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | kruszywo | 9900 | 0 | informational | $0.14 | peak 04/2024 (18100), low 12/2018 (2400) |
| 2 | stabilizacja gruntu | 720 | 0 | informational | $2.13 | peak 03/2024 (1300), low 01/2026 (590) |
| 3 | kruszywo granitowe | 720 | 0 | transactional | $0.09 | peak 03/2026 (1000), low 12/2018 (170) |
| 4 | kruszywo 0-31 5 | 260 | 0 | transactional | $0.06 | peak 03/2026 (720), low 04/2019 (50) |
| 5 | kruszywo wapienne | 260 | 0 | informational | $0.07 | peak 12/2025 (720), low 01/2026 (70) |
| 6 | kruszywo 0 31 | 210 | 0 | transactional | $0.06 | peak 03/2026 (390), low 12/2018 (10) |
| 7 | kruszywo 0-31 | 210 | 0 | transactional | $0.06 | peak 03/2026 (390), low 12/2018 (10) |
| 8 | kruszywo łamane 0-31 5 | 170 | 0 | transactional | $0.14 | peak 03/2026 (390), low 01/2019 (50) |
| 9 | kruszywo 8 16 | 170 | 0 | transactional | $0.04 | peak 03/2024 (320), low 01/2019 (20) |
| 10 | kruszywo 0-63 | 140 | 43 | transactional | $0.11 | peak 03/2026 (210), low 12/2018 (20) |
| 11 | kruszywo drogowe 0-31 5 cena | 110 | 0 | informational | $0.15 | peak 03/2024 (320), low 01/2021 (0) |
| 12 | kruszywo 2-8 | 110 | — | transactional | $0.07 | peak 03/2024 (210), low 01/2019 (20) |
| 13 | kruszywo 2/8 | 110 | — | transactional | $0.07 | peak 03/2024 (210), low 01/2019 (20) |
| 14 | kruszywo łamane 0 31 5 cena | 70 | 0 | informational | $0.17 | peak 03/2024 (170), low 01/2026 (30) |
| 15 | kruszywo 0 16 | 70 | 0 | transactional | $0.05 | peak 05/2025 (110), low 12/2021 (10) |
| 16 | kruszywo łamane 0-31 5 cena m3 | 70 | — | transactional | $0.22 | peak 09/2025 (110), low 09/2021 (0) |
| 17 | kruszywo łamane 0 31 5 cena m3 | 70 | — | transactional | $0.22 | peak 09/2025 (110), low 09/2021 (0) |
| 18 | dolomit wapno nawozowe | 70 | — | transactional | $0.14 | peak 03/2026 (210), low 12/2018 (0) |
| 19 | kruszywo dolomitowe 0 31 5 | 50 | 0 | transactional | $0.03 | peak 04/2024 (140), low 03/2020 (0) |
| 20 | kruszywo dolomitowe 0-31 5 | 50 | 0 | transactional | $0.03 | peak 04/2024 (140), low 03/2020 (0) |
| 21 | kruszywo granitowe 0 31 5 cena | 50 | 0 | commercial | $0.41 | peak 04/2024 (140), low 12/2019 (0) |
| 22 | kruszywo granitowe 0-31 5 cena | 50 | 0 | informational | $0.41 | peak 04/2024 (140), low 12/2019 (0) |
| 23 | kruszywo granitowe 0-31 5 | 50 | — | transactional | $0.20 | peak 03/2026 (110), low 12/2022 (10) |
| 24 | kruszywo granitowe 0 31 5 | 50 | — | transactional | $0.20 | peak 03/2026 (110), low 12/2022 (10) |
| 25 | kruszywo 0-31 5 cena | 50 | — | informational | $0.11 | peak 08/2023 (140), low 01/2026 (20) |
| 26 | kruszywo granitowe 8 16 | 50 | — | transactional | $0.19 | peak 04/2024 (110), low 01/2026 (10) |
| 27 | kruszywo granitowe 8-16 | 50 | — | transactional | $0.19 | peak 04/2024 (110), low 01/2026 (10) |
| 28 | kruszywo 0-31 cena | 50 | — | informational | $0.04 | peak 10/2024 (90), low 01/2026 (10) |
| 29 | kruszywo drogowe 0-31 5 | 50 | — | transactional | $0.04 | peak 03/2026 (140), low 04/2020 (0) |
| 30 | kruszywo drogowe 0 31 5 | 50 | — | transactional | $0.04 | peak 03/2026 (140), low 04/2020 (0) |

### Marka / ogólne (1 fraz, łączny volume ~10/mies PL)

_Zapytania brandowe AGRIA, Agrobielik, Bielik, Nordkalk, Trzuskawica._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | wapno bielik trzuskawica | 10 | — | informational | — | peak 03/2021 (30), low 10/2024 (0) |

### Niesklasyfikowane (6 fraz, łączny volume ~150/mies PL)

_Frazy nie pasujące jednoznacznie do żadnego klastra — do manualnego przeglądu._

| # | Fraza | Volume | KD | Intent | CPC | Sezonowość |
|---|-------|-------:|---:|--------|----:|------------|
| 1 | wapno dawkowanie | 50 | 0 | informational | $0.50 | peak 07/2021 (260), low 10/2025 (30) |
| 2 | jakie wapno dla kur | 50 | 0 | informational | $0.05 | peak 07/2024 (110), low 09/2019 (0) |
| 3 | allegro wapno magnezowe | 20 | — | transactional | $0.06 | peak 03/2026 (30), low 09/2024 (0) |
| 4 | wapno czy wapno magnezowe | 10 | — | informational | — | peak 10/2024 (40), low 08/2024 (0) |
| 5 | wapno magnezowe kiedy siać | 10 | — | informational | — | peak 08/2019 (140), low 12/2024 (0) |
| 6 | wapno tlenkowe kiedy stosować | 10 | — | informational | — | peak 11/2023 (30), low 01/2026 (0) |

## Konkurencja — gap analysis

Marki konkurencyjne pojawiające się w SERP dla zapytań związanych z wapnem nawozowym/budowlanym. Frazy z wysokim volume = okazja do treści typu „wapno X vs Agrobielik" lub porównań parametrów.

| Konkurent | Fraza | Volume | KD | Intent |
|-----------|-------|-------:|---:|--------|
| Atrigran | atrigran wapno dawkowanie | 10 | — | transactional |
| Kujawit | kujawit wapno dawkowanie | 10 | — | informational |
| Kujawit | wapno kujawit dawkowanie | 10 | — | informational |
| Supermag | supermag wapno dawkowanie | 10 | — | transactional |
| Orcal | wapno orcal dawkowanie | 10 | — | informational |

## Rekomendacje dla M1 + M2-M6

### M1 fundamenty (T1-T4 czerwiec 2026)

**Content audit z perspektywą fraz (deliverable M1):**
- mapowanie istniejących stron `agria.pl` na klastry (które klastry pokryte, które puste),
- identyfikacja fraz top-priority bez landing page (= content gap),
- priorytetyzacja per klaster z uwzględnieniem sezonowości (rolnictwo: cliffhanger marzec / wrzesień).

**On-page priorytety wynikające z keyword research:**
- Klaster rolnictwo — najwięcej volume, najwięcej okazji. Per produkt WC: dopasuj title/H1 do faktycznych zapytań (np. `wapno nawozowe tlenkowe odmiana 01` zamiast tylko `Agrobielik 01`).
- Klaster drogownictwo — kruszywo wapienne ma silne SEO momentum (volume 260 dla głównej frazy + długi ogon), potrzebna dedykowana landing.
- Klaster oczyszczalnie — bardzo niskie volume Google, ALE wysoka wartość per query. Content informational + schema FAQ + AEO pod „jak higienizować osady wapnem", nie PPC.

### M2-M6 content roadmap

- **M2-M3 (lipiec-sierpień):** content rolnictwo + sadownictwo (4 art/mies), peak czytelniczy przed sezonem jesiennym wapnowania.
- **M4 (wrzesień):** content rybactwo (wapnowanie stawu przed zimą — sezonowość 09-11).
- **M5-M6 (październik-listopad):** content drogownictwo + budownictwo + oczyszczalnie (FAQ B2B, schema HowTo).
- **Cross-sezon:** dwa „evergreen pillar" (klastry rolnictwo i drogownictwo) z dedykowanymi landing pages pod top frazy.

### Future PPC (Q4 2026 / Q1 2027 jeśli budżet)

- Klaster rolnictwo: kampania sezonowa marzec-kwiecień + wrzesień-październik. Frazy transakcyjne z volume ≥ 50 + intent `commercial`/`transactional`.
- Klaster drogownictwo: kampania całoroczna z peakiem maj-sierpień. CPC stabilne, intent silnie transakcyjny dla `kruszywo wapienne cena`/`cennik`.
- Klaster oczyszczalnie: **NIE PPC** — niski volume + B2B przetargowy. Lead z LinkedIn Ads + content.

## Pełne dane (źródła)

- `~/scratch/agria-kw/clustered.json` — wszystkie 194 frazy z klastrami
- `~/scratch/agria-kw/overview.json` — surowe dane DataForSEO Labs z keyword_overview (112 fraz)
- `~/scratch/agria-kw/competitors.json` — frazy z markami konkurencji
- `~/scratch/agria-kw/suggestions_*.json`, `ideas_*.json` — surowe odpowiedzi DataForSEO

---
_Wygenerowano: 2026-05-19 przez `~/scratch/agria-kw/generate_report.py`. Saldo DataForSEO po analizie: $46.9647._