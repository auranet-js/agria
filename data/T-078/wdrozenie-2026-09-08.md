# T-078 — wdrożenie opisu kategorii `/paszarstwo/`

**Data:** 2026-09-08 · **Term:** 770 (`product_cat`) · **Pola:** `term_taxonomy.description`,
`termmeta.rank_math_title`, `termmeta.rank_math_description`, `postmeta` karty 307
**Wzorzec:** T-092 (`data/T-092/wdrozenie-2026-09-04.md`)

## Stan przed i po

| | przed | po |
|---|---|---|
| `description` | **465 B**, zero nagłówków, tekst ciągły | **5 938 B**, MD5 `db2881bc999e47da5cdd85b4c6213930` |
| Nagłówki w opisie | **0** | **7 × H2, 5 × H3** |
| Tabele | 0 | **3** |
| Linki wewnętrzne | 1 (`/kontakt`) | **5** (kontakt ×2, wapno nawozowe, do pobrania, karta produktu) |
| Tekst całej strony (render) | ok. 421 słów | **8 619 znaków** po dekodowaniu encji |
| `rank_math_title` kategorii | „Kreda pastewna do żywienia zwierząt \| AGRIA" (43) | „Kreda pastewna — dawkowanie, frakcje, cena \| AGRIA" (49) |
| `rank_math_title` karty 307 | „Kreda pastewna \| AGRIA" (**22**) | „Kreda pastewna min. 37% CaO, cztery frakcje \| AGRIA" (50) |

H1 „Paszarstwo", struktura listingu produktów i `rank_math_focus_keyword` — **nietknięte**,
tak jak w T-092.

## Backup i rollback

`~/agria-backups/przed-T078-opis-paszarstwo-20260908-171104.sql` — 472 wiersze
(`wpfz_term_taxonomy` 408 + `wpfz_termmeta` 64), zrzut przez MCP `db_export`, poza web rootem.

Stare wartości `postmeta` karty 307, gdyby trzeba je było cofnąć ręcznie:
- `rank_math_title` = `Kreda pastewna | AGRIA`
- `rank_math_description` = `Kreda pastewna — zapytaj o ofertę. Agria, 37 lat doświadczenia.`

## Dlaczego akurat taka treść — SERP i GSC, nie przeczucie

**SERP mobile 07.09** (DataForSEO, `kreda pastewna`, location 2616): jest **AI Overview**
cytujący siedem domen (centrumnawozow, doradcatechmot, hodowlany, polcalc, euromar, hotfarm,
portalhodowcy) — **żadnej naszej**. W TOP10 mieszanka sklepów i artykułów, a w tytułach
konkurencji powtarza się jedno słowo: **frakcja** (0,1–0,4 mm, 0,4–3 mm) oraz „dla niosek".

**Cztery pytania z „ludzie pytają też"** stały się dosłownie czterema nagłówkami H3 w sekcji
częstych pytań:
- Na co pomaga kreda pastewna?
- Czy kreda pastewna to to samo co wapno?
- Jak stosować kredę pastewną dla kur?
- Ile kredy pastewnej dla kur na 100 kg?

**Baseline GSC 08.08–05.09** (`data/T-078/baseline-gsc-2026-09-08.json`) pokazał rzecz, której
nie było w rozpisce: **kategoria `/paszarstwo/` ma zero wyświetleń**, cała widoczność klastra
siedzi na karcie produktu (205 wyświetleń, 1 kliknięcie, poz. 8,6). A zapytania to niemal
wyłącznie **dawkowanie**:

| fraza | wyśw. | klik. | poz. |
|---|---|---|---|
| kreda pastewna dla bydła | 8 | 0 | 22,8 |
| kreda pastewna dla bydła dawkowanie | 7 | 0 | 21,4 |
| **ile kredy pastewnej dla kur na 100 kg** | 5 | 0 | **6,6** |
| kreda pastewna dawkowanie | 4 | 0 | 21,2 |
| kreda pastewna dla bydła co daje | 4 | 0 | 12,0 |

Razem klaster „pastewn": **11 fraz, 36 wyświetleń, zero kliknięć**; szerszy klaster „kreda":
54 frazy, 426 wyświetleń, **zero kliknięć**.

To rozstrzygnęło oś treści. Fraza `ile kredy pastewnej dla kur na 100 kg` stoi na **pozycji 6,6
z zerem kliknięć**, a odpowiedź — **1–2 kg / 100 kg paszy** — jest w atrybucie karty od dawna.
Była na stronie, ale nie w miejscu, w którym Google mógł ją podać. Teraz jest osobnym nagłówkiem
i osobnym akapitem.

## Parametry — wyłącznie z karty

Wzięte z atrybutów `pa_*` produktu 307, nie z rozumowania (`CLAUDE.md` §7):
min. **37% CaO** · forma sypka · frakcje **0–0,3 / 0,1–0,4 / 0,4–0,8 / 1–3 mm** ·
dawkowanie **1–2 kg / 100 kg paszy** · dostępność cały rok · producent **Lhoist, Celiny
(Hochel Group)**. Cena **od 190 zł/t netto luzem** z `FAKTY_KLIENTA.md` §7 (worki 30 kg od
610 zł/t — druga kwota świadomie **nie** podana, obowiązuje zasada jednej kwoty na kartę
ze swoim warunkiem).

## Znalezione przy okazji: rozjazd form dostawy

Stary opis kategorii i stara meta mówiły **„Worki 25 kg"** i **big-bag**. Atrybuty karty mówią
**worek 30 kg** i **luz 24 t**, big-baga nie ma. `FAKTY_KLIENTA.md` potwierdza worki 30 kg
(610 zł/t). Poprawione w opisie i w meta przy okazji tej samej edycji.

## Czego świadomie NIE napisałem

**Przypisania frakcji do gatunku.** Konkurencja robi to wprost („gruba dla niosek"), ale nasze
karty producentów tego nie zawierają, a `CLAUDE.md` §7 zakazuje wyprowadzania parametrów
z rozumowania. Opis wymienia cztery frakcje i mówi, że dobór ustalamy pod recepturę.
**To jest realna luka wobec konkurencji z SERP-u** — jeśli Kazimierz potwierdzi mapowanie
frakcja → gatunek, warto je dopisać; wtedy odpowiadamy na „dla kur" mocniej niż dziś.

Podobnie **rozbicie dawkowania na gatunki** — mamy jeden przedział 1–2 kg/100 kg dla wszystkich,
a zapytania pytają osobno o bydło i osobno o kury.

## Weryfikacja

Render sprawdzony **po rozgrzewce cache**, nie przez `?cb=` — po WP Rocket ten parametr omija
cache i pokazuje wersję, której użytkownik nie dostaje (ADR `2026-09-07-wp-rocket-…` §6 pkt 1).

- MD5 opisu w bazie **zgodny co do znaku** z plikiem `opis-do-wdrozenia-2026-09-08.html`
  — zapis przez MCP `query_db_write`, więc `wp_filter_kses` nie ruszył tabel ani nagłówków
  (pułapka nr 1 z T-092).
- Wszystkie 7 nagłówków H2 obecnych na renderze **po jednym razie** — pierwsze liczenie pokazało
  15 H2, bo doliczyło nagłówki motywu i stopki.
- Tytuł i meta description na żywej stronie zgodne z zapisanymi.
- Cache: Rocket, Rank Math i CSS Elementora wyczyszczone.

## Kontrola 14-dniowa — 26.09

Mierzona **na frazach formowych klastra**, nie na frazie głównej: `kreda pastewna dawkowanie`,
`kreda pastewna dla bydła dawkowanie`, `ile kredy pastewnej dla kur na 100 kg`,
`kreda pastewna dla kur dawkowanie`. Porównanie do `baseline-gsc-2026-09-08.json`.
Interesuje nas **CTR i pozycja tych fraz**, a nie sam wolumen — klaster ma dziś zero kliknięć
przy 462 wyświetleniach, więc każde kliknięcie jest zmianą jakościową.

⚠️ `lastmod` w `product_cat-sitemap.xml` się nie ruszy — dla archiwum kategorii bierze się
z produktów, nie z opisu termu (pułapka nr 3 z T-092). To nie jest błąd.
