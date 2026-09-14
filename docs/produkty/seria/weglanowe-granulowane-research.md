# Research — #314 Węglanowe bez magnezu granulowane (T-136 seria, T-117)

> 14.09.2026 · pełny stan karty: [`../weglanowe-granulowane.md`](../weglanowe-granulowane.md) (§4–§8 — nie przepisuję) · T-116 i T-117 włączone do T-136 `[J 14.09]`
> GSC 28 dni 2026-08-14 … 09-10: `data/produkty/seria/gsc-314-317-28d-2026-09-14.json` · 90 dni: `data/produkty/gsc/weglanowe-granulowane.json` ·
> SERP mobile 09–10.09 z PAA: `data/produkty/dfs/serp-weglanowe-bez-mg-2026-09-10.json` · planer: `data/produkty/ads/weglanowe-granulowane-planer.json`
> **DataForSEO w tym etapie: 0 USD** — wszystkie frazy karty są w SERP-ach z 10.09.

## 0. Warstwa renderu

`_elementor_data` pusty (0 B), `_elementor_edit_mode` brak → render z **`post_content`** (SSH 14.09). Adres kanoniczny = `/wapno-nawozowe-rolnictwo/weglanowe-granulowane/` (curl 14.09).

## 1. Frazy, które należą do tej karty

| fraza | wyszukań/mies. | nasze adresy w GSC | kolizja / przydział |
|---|---|---|---|
| **wapno węglanowe granulowane** · wapno granulowane węglanowe · wapno nawozowe węglanowe granulowane · …bez magnezu granulowane | **390** · 50 · <10 · <10 | #314 50 wyśw. poz. 16,1 (28 dni) · #317 43 / 34,3 | **#314** (#317 zbiera przez przypadek) |
| wapno granulowane cena · big bag · cena za tonę · 25 kg · wapno węglanowe granulowane cena | **480** · 260 · 90 · 70 · 30 | hub 17 / 10 / 2 wyśw.; #314 8 / poz. 10,8 | rodzajowe dla 4 granulatów — **#314 jako najtańszy granulat (350 zł/t)**; do rewizji w D1 |
| wapno granulowane czy sypkie · wapno węglanowe czy magnezowe | 50 · 20 | hub 1 · #317 2 | **#314** (porównanie z #315, #317, #305) |
| wapno nawozowe węglanowe | 40 | **#314 75 wyśw. poz. 16,4** · #317 39 | #314 |
| kopalnia celiny · lhoist wapno · wapno celiny · wapno tarnów opolski | 320 · 30 · 10 · 10 | 0 | wspólne z #315, #307 — SERP nawigacyjny; producent w treści, bez celu frazowego |
| ile wapna granulowanego na hektar · …ile na hektar · …dawkowanie · wapno węglanowe granulowane ile na hektar | 480 · 170 · 40 · 20 | **hub `/wapnowanie-gleby/` 2 033 wyśw. poz. 7,2** | **zostaje przy hubie** — karta odpowiada liczbą z karty i linkuje |
| **wapno granulowane** | **4 400** | hub 45 wyśw. | **D1** (rodzajowa, cztery granulaty) |
| wapno węglanowe | 1 000 | #315 · #314 153 wyśw. poz. 20,5 | **#315** (przypisane w pilocie) |

## 2. Co Google nagradza (SERP mobile 09–10.09, bez nowych zapytań)

Na `wapno węglanowe granulowane`, `wapno granulowane cena`, `…big bag` pierwsze miejsce ma OLX albo sklep z big-bagiem POLCALC; AGRIA poza top 20
na każdej (baza §7). W tytułach top 5: **marka/forma dostawy (BB 500 kg, 25 kg) i cena**; poradniki (tygodnik-rolniczy, farmer) — dawka i termin.
**PAA:** „Ile kosztuje 1 tona wapna granulowanego?" · „Ile kosztuje wapno w big bagach?" · „Ile wapna węglanowego granulowanego na hektar?" ·
„Które wapno jest lepsze: sypkie czy granulowane?" · „Jakie wapno jest lepsze węglanowe czy magnezowe?" · „Co to jest wapno węglanowe?" ·
„Po jakim czasie działa wapno węglanowe?" · „Kiedy najlepiej siać wapno granulowane?" · „Z jakiej kopalni jest najlepsze wapno?"

## 3. Czego szuka kupujący

- **Zapytań ofertowych z karty: 0** (z 11 do 10.09; od 09.09 jedno nowe — #307). Reklamy nie kierowały na #314; na `/wapno-granulowane/`
  179 klik., 0 konw. (13.08–09.09).
- **GSC karty, 28 dni:** 1 klik. / 616 wyśw. / CTR 0,16% / poz. 16,6 (90 dni: 2 / 849 / poz. 18,8). Widoczne zapytania to rodzaj
  (`wapno węglanowe`, `wapno nawozowe węglanowe`) i nazwa — **żadne o cenie, big-bagu, siewniku**.
- Kupujący pyta o: cenę za tonę i big-bag, dawkę na hektar, porównanie sypkie/granulowane i węglanowe/magnezowe.

## 4. Co z tego wynika dla treści (tylko karta PDF, `[C]`, `[F]`)

1. **Wyróżnik z karty PDF, którego dziś nie ma na stronie:** wysiew siewnikiem nawozowym razem z NPK, jeden przejazd, bez pyłu i zbrylania,
   bez rozsiewacza i kombinezonów — do lead, H2 i FAQ.
2. **Tabela 1:1 z karty PDF** — wracają Celiny (magazyn i producent), „Forma dostawy", pełne „Zastosowanie" i „Efekt".
3. **Porównanie z granulatami i sypką odm. 04** — z kart PDF i cennika: #315, #317, #305 (baza §4.1), bez ocen.
4. **Cena:** od 350 zł/t w big-bagu; worek 25 kg jako możliwość, bez kwoty (`FAKTY_KLIENTA` §7). Znika „w big-bagach od 1 tony" (próg ilościowy).
5. **Magazyny:** 4 z tabeli karty PDF (tekst karty podaje 3 — tabela jest źródłem parametrów).
6. **Usunąć (DescWriter):** „zatrzymywania wody…system korzeniowy", „wysoka reaktywność…poprawia strukturę", „potencjał plonotwórczy",
   „dostawę na terenie całej Polski", „pełną dokumentację techniczną".
7. **Title:** duplikatu nie ma (#314 ≠ #317); obecny nie niesie `wapno węglanowe granulowane` w szyku z zapytań ani formy dostawy.
