# Research — #317 Węglanowe z magnezem granulowane (T-136 seria, T-117 + T-116)

> 14.09.2026 · pełny stan karty: [`../weglanowe-magnez-granulowane.md`](../weglanowe-magnez-granulowane.md) (§4–§8 — nie przepisuję)
> GSC 28 dni 2026-08-14 … 09-10: `data/produkty/seria/gsc-314-317-28d-2026-09-14.json` · 90 dni: `data/produkty/gsc/weglanowe-magnez-granulowane.json` ·
> SERP mobile 10.09 z PAA: `data/produkty/dfs/serp-weglanowe-magnez-2026-09-10.json` · planer: `data/produkty/ads/weglanowe-magnez-granulowane-planer.json`
> **DataForSEO: 0 USD** — frazy karty są w SERP-ach z 10.09.

## 0. Warstwa renderu i T-116

`_elementor_data` pusty (0 B), bez `_elementor_edit_mode` → render z **`post_content`** (SSH 14.09); canonical własny.
**T-116:** title identyczny z #318 („Wapno nawozowe węglanowe zawierające magnez | AGRIA", zapytanie SQL 14.09) i bez słowa „granulowane" —
zamykane tutaj nowym title; `Product.name` przechodzi na nazwę WC (`AGRIA_KARTY_SCHEMA_V2`), więc duplikat znika też w schemacie.

## 1. Frazy, które należą do tej karty

| fraza | wyszukań/mies. | nasze adresy w GSC | przydział |
|---|---|---|---|
| **wapno magnezowe granulowane** · wapno granulowane magnezowe · wapno granulowane z magnezem · wapno węglanowo magnezowe granulowane · granulat wapniowo magnezowy | **880** · 170 · 140 · 20 · <10 | #317 12 wyśw. poz. 38,5 (28 dni); hub 6 | **#317** — jedyny granulat z magnezem |
| wapno magnezowe granulowane cena · big bag · 25 kg · wapno granulowane z magnezem cena | 50 · 50 · 10 · 10 | hub po 1 wyśw. | **#317** |
| wapno magnezowe granulowane dawkowanie | 70 | 0 wierszy | **#317** (H2) |
| wapno magnezowe granulowane ile na hektar · ile wapna magnezowego granulowanego na hektar | 50 · 10 | **hub 155 + 43 wyśw.** | zostaje przy hubie — karta odpowiada liczbą z karty i linkuje |
| wapno magnezowe czy węglanowe · wapno magnezowe czy kizeryt | 10 · <10 | 0 | #317 (porównanie z #314 i z siarczanem magnezu — karta PDF sama je wprowadza) |
| grankal · wapno grankal | 110 · 20 | 0 | producent w treści; SERP nawigacyjny (grankal.pl) — bez celu frazowego |
| wapno magnezowe · wapno granulowane · wapno węglanowo magnezowe | 1 900 · 4 400 · 170 | #317 23 / poz. 48,9 · hub · #319 | **D1** (rodzajowe, kilka kart) |

## 2. Co Google nagradza (SERP mobile 10.09)

Na `wapno magnezowe granulowane`, `…z magnezem`, `…cena` pierwsze miejsce ma sklep z big-bagiem SuperMag (rolmat), dalej OLX i sklepy z workami;
AGRIA poza top 20 (baza §7). W tytułach: **nazwa rodzajowa + forma dostawy (BB 500/600 kg, 25 kg)**.
**PAA:** „Ile wapna magnezowego granulowanego należy zastosować na hektar?" · „Kiedy najlepiej stosować granulowane wapno magnezowe?" ·
„Jaki odstęp czasu między wapniem a magnezem?" · „Które wapno jest lepsze węglanowe czy magnezowe?" · „Co jest lepsze wapno granulowane czy sypkie?" ·
„Ile kosztuje tona wapna z magnezem?" · „Na co jest dobre wapno magnezowe?" · „Czy wapno magnezowe należy siać przed siewem?"

## 3. Czego szuka kupujący

- **Zapytań ofertowych z karty: 0** (do 14.09). Ads 13.08–09.09: 41 klik. na frazy z „magnez", **żaden na #317**.
- **GSC karty, 28 dni:** 1 klik. / 480 wyśw. / CTR 0,21% / poz. 25,1 — widoczne zapytania to głównie węglanowe **bez** magnezu
  (`wapno węglanowe` 50, `wapno węglanowe granulowane` 43, `wapno nawozowe węglanowe` 39, `wapno węglowe` 35); z „magnez" ≈ 65 wyśw.
- Kupujący pyta o: dawkę na hektar, termin, czy wapno i magnez podawać osobno, cenę za tonę, big-bag.

## 4. Co z tego wynika dla treści (tylko karta PDF, `[C]`, `[F]`)

1. **Nazwa rodzajowa `wapno magnezowe granulowane`** do title, H2 i FAQ — dziś nie pada na karcie ani razu w szyku zapytań.
2. **Wyróżnik z karty PDF, którego nie ma na stronie:** „dwa składniki w jednym wysiewie" — jeden wjazd zamiast osobno wapna i siarczanu magnezu;
   magnez węglanowy „nie obciąża gleby siarczanami, nie zakwasza"; siewnik NPK, bez pyłu, bez strat na wietrze, przez cały sezon wegetacyjny.
   Odpowiada wprost na PAA o odstępie między wapniem a magnezem.
3. **Tabela 1:1 z karty PDF** — etykieta „Zawartość CaO + MgO", pełne „Zastosowanie" (z Mg) i „Efekt", „Forma dostawy: Big-bag 600 kg, Worek 25 kg".
4. **Porównanie** z #314 (granulat bez Mg), #318 i #319 (sypkie z Mg) — z kart PDF i cennika, bez ocen. Dolomit #302 poza porównaniem (prompt §5: dwa towary, do quizu).
5. **Cena:** od 370 zł/t w big-bagu; worek 25 kg bez kwoty; znika „w big-bagach od 1 tony".
6. **Usunąć (DescWriter):** fotosynteza i chloroza, „brak ryzyka wypalenia" (to karta #318), „szybko wchodzi w reakcję", przewiewność i gospodarka wodna,
   „zrównoważone rolnictwo", „Idealne dla hurtowni".
7. **Nie używać** nazw produktów producenta („Grankal Magnezowy", „Grankal Vital") ani liczb 30/17% z grankal.pl — tożsamość niezweryfikowana; producent „Grankal" — tak.
