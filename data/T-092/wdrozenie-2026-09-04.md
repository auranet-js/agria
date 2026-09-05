# T-092 — wdrożenie opisu kategorii `/wapno-nawozowe-rolnictwo/`

**Data:** 2026-09-04 · **Term:** 764 (`product_cat`) · **Pole:** `term_taxonomy.description`

## Stan przed i po

| | przed | po |
|---|---|---|
| `description` | 1 219 B, MD5 `7a566bb9db2f6fde559334352def29cc` | 6 664 B |
| Widoczny tekst opisu | 958 znaków | ok. 5 700 znaków |
| Nagłówki treściowe | 1 × H2 | **7 × H2, 7 × H3** |
| Linki wewnętrzne w opisie | 3 | **5** |
| Tekst całej strony (render) | 5 650 znaków | **10 425 znaków** (+4 775) |

Listing 15 produktów, H1 „Wapno nawozowe", meta i `rank_math_focus_keyword` — **nietknięte**.

## Backup i rollback

Zrzut tabeli `wpfz_term_taxonomy` przed zmianą, po stronie serwera:
`~/agria-backups/przed-T092-opis-kategorii-20260905-085214.sql` (21 241 B, WP-CLI `db export`).
Rollback: import tego pliku albo `UPDATE` pojedynczego wiersza z jego zawartości.

## Przebieg — trzy rzeczy, które nie poszły od razu

1. **WP-CLI `term update` bez zalogowanego użytkownika przepuszcza opis przez `wp_filter_kses`.**
   Pierwszy zapis wyciął **całą tabelę i wszystkie nagłówki** — z 6 665 B zostało 6 278 B, w treści
   przetrwały wyłącznie `<a>` i `<em>`. Przez chwilę produkcja miała opis gorszy strukturalnie
   niż przed zmianą (poprzedni miał przynajmniej jeden H2). Powtórka z `--user=1` nie doszła
   do skutku — SSH padł na timeout połączenia. Naprawione zapisem przez MCP (`query_db_write`),
   który idzie prosto do bazy i filtrów WP nie uruchamia.
2. **Kontener przewijania dla tabeli nie przeszedł.** Motyw Hello daje `table{width:100%}` bez
   `overflow`, więc pięciokolumnowa tabela przy 390 px zostawia ok. 48 px na kolumnę. Wzorzec z T-044
   (`<div style="overflow-x:auto">` + `min-width`) **nie zadziałał: render zjadł atrybut `style`
   z diva, zostawiając go na tabeli** — czyli tabela dostałaby `min-width:520px` w kontenerze,
   który nie przewija, i rozpychałaby layout. Cofnięte do czystego `<table>`: motywowe `width:100%`
   daje zawijanie zamiast przelewu poziomego. **Wariant zweryfikowany w HTML, nie wizualnie** —
   rozszerzenie Chrome rozłączyło się w trakcie sesji.
3. **`lastmod` w `product_cat-sitemap.xml` został na 2026-08-19.** Cache RankMath wyczyszczony
   (8 plików `uploads/rank-math/*.xml`), ale dla archiwum kategorii data bierze się z produktów,
   nie z opisu termu. Dat produktów nie ruszam — to 15 kart bez powodu. Adres jest crawlowany
   regularnie, więc sygnał dotrze bez tego.

## Czym mierzyć

Baseline: `data/T-092/baseline-gsc-2026-09-04.json` (okna 28 i 90 dni, per fraza × URL).
**Kontrola 18.09 z GSC** — nie na frazie `wapno nawozowe`, tylko na frazach formowych o realnym
wolumenie, gdzie dziś biją się karty produktów:

| Fraza | Wolumen/mies. | Stan 04.09 (28 dni) |
|---|---|---|
| `wapno węglanowe` | 1 000 | 627 wyśw., **5 URL-i**, poz. ważona 15,3 (najlepszy 9,9) |
| `kreda nawozowa` | 1 000 | 30 wyśw., 2 URL-e, poz. 24,2 |
| `wapno tlenkowe` | 720 | 40 wyśw., 2 URL-e, poz. 20,2 |
| `kreda nawozowa sypka` | — | 41 wyśw., 3 URL-e, kategoria już na **8,2** |
| `wapno nawozowe` (tło) | 1 300 | 318 wyśw., kategoria 11,1 · strona główna 6,5 |

Pytanie kontrolne: czy kategoria zaczyna pojawiać się na frazach formowych i czy liczba
konkurujących własnych URL-i spada. DataForSEO pokazuje nowe treści z opóźnieniem — postęp
czytamy z GSC, DFS zostaje do obrazu konkurencji.
