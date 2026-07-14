# Prompt startowy — wątek AGRIA: #4 content M2 (dobicie puli lipca / start KROK 3)

> Wklej/uruchom na początku następnej sesji `claude` w `~/projekty/agria`.
> Cel: dowieźć **jeszcze 1 pozycję contentową** w budżecie M2 (lipiec) — dalej „pod wynik" (widoczność w Google), nie technika.

---

## Kontekst (przeczytaj najpierw)

1. `docs/MASTER_PROMPT.md` — tożsamość/zakres (Fractional CMO branży surowcowej; ton fakty/parametry/zastosowania; zero lifestyle; NIE dodawaj produktów spoza oferty).
2. `docs/seo/SEO_STRATEGIA_POD_WYNIK_2026-07-08.md` — baza strategiczna (SERP + konkurencja + lane ROI).
3. `docs/seo/POMIAR_POD_WYNIK.md` — **log przebudów + fraz-celów** (wpisy #1–#3 z 9.07). Tu dopisujesz #4.
4. `docs/audits/KR_PRIORYTETYZACJA_2026-06-15.md` — frazy i mapowanie.

## Stan na 2026-07-09 (co już zrobione w tej fali)

Klaster „wapnowanie" — 3 strony live, zgłoszone do indeksacji, z FAQPage+HowTo, spięte hub-and-spoke:
- **Hub:** `/wapnowanie-gleby/` (post 2074, przebudowa) — cel „ile wapna na hektar" (720), baseline poz. 14.
- `/ile-wapna-granulowanego-na-ha/` (post 2741, nowy) — cel „ile wapna granulowanego na ha" (590).
- `/wapno-nawozowe-na-trawnik/` (post 2742, nowy) — cel „wapno nawozowe na trawnik" (50).

Budżet content M2: zrobione 3 pozycje z ~4 → **został ~1 slot**.

## Zadanie tego wątku — wybór (zarekomenduj i zapytaj)

**Opcja A (szybka, domyka klaster rolniczy):** poradnik „jak stosować wapno nawozowe" (30/mc, info) — dobija 4/4 content M2, spójny sezonowo, tania robota. Kategoria: poradniki (829). Spiąć z klastrem.

**Opcja B (większa wartość, start KROK 3 strategii):** landing „higienizacja osadów ściekowych wapnem" (B2B, przetargi, high value per lead; konkurencja słaba — wapno-info na 15 frazach). Frazy: higienizacja osadów, neutralizator ścieków. Produkty: wapno palone mielone #320 + Bielik/Agrobielik 90. To NIE blog post — to landing pod segment Oczyszczalnie (parametry, pH>12, dokumentacja przetargowa) + schema. Większy zakres — jeśli B, potraktuj jako główny cel wątku, nie „na doczepkę".

Rekomendacja: jeśli chcesz tanio domknąć lipiec → A. Jeśli masz czas na mocniejszy ruch B2B → B (ale to raczej osobny, dedykowany wątek).

## Mechanika publikacji NOWEGO posta (sprawdzona 9.07 — trzymaj się jej)

1. **INSERT minimalny** (`mcp__agria__query_db_write`), placeholder w treści:
   `INSERT INTO {prefix}posts (post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) VALUES (1, NOW(), UTC_TIMESTAMP(), 'PLACEHOLDER', '<TYTUŁ>', '', 'publish', 'open', 'open', '', '<slug>', '', '', NOW(), UTC_TIMESTAMP(), '', 0, '', 0, 'post', '', 0)`
2. `SELECT ID FROM {prefix}posts WHERE post_name='<slug>' AND post_type='post'`.
3. **Pełna treść** przez `mcp__agria__update_post_content` (Gutenberg-blocki + JSON-LD FAQPage/HowTo w bloku `wp:html`). Dedykowany tool ogarnia escaping 15 KB — NIE wpychaj treści w SQL.
4. `UPDATE {prefix}posts SET guid='https://agria.pl/?p=<ID>' WHERE ID=<ID>`.
5. Kategoria: `INSERT INTO {prefix}term_relationships (object_id, term_taxonomy_id, term_order) VALUES (<ID>, 829, 0)` + `UPDATE {prefix}term_taxonomy SET count=count+1 WHERE term_taxonomy_id=829` (829 = „poradniki"; landing może iść inną kategorią/stroną).
6. Meta RankMath: `INSERT INTO {prefix}postmeta (post_id, meta_key, meta_value) VALUES (<ID>,'rank_math_title','...'),(<ID>,'rank_math_description','...'),(<ID>,'rank_math_focus_keyword','...')`.
7. **Linki klastra** przez `REPLACE()` na `post_content` (bez przesyłania całości) — anchor musi być unikalny; po edycji cudzej strony bumpnij `post_modified=NOW(), post_modified_gmt=UTC_TIMESTAMP()`.
8. **Weryfikacja** curl cache-bust (`?cb=$RANDOM`) — title, sekcje, linki, `"@type":"FAQPage"`/`"HowTo"`. Uwaga: Orphans wstawia `&nbsp;` (grep fixed-string myli się na spacjach).
9. `~/bin/index-submit --project agria --type URL_UPDATED --url <URL>` (pokaż budżet) + dopisz wpis do `docs/seo/POMIAR_POD_WYNIK.md` (data, fraza-cel, baseline, okno pomiaru).

## Zasady (twarde)

- Draft → **akcept Janka PRZED publikacją** (drop na auratest + inline). Ton MASTER_PROMPT.
- Content-facing: rozwojowo, bez krytyki stanu strony (memory `feedback_agria_no_self_criticism_built_site`).
- Komunikacja do klienta wyłącznie do Janka (`js@auranet.com.pl`).
- Sprawdź MCP `status` na starcie; CDN nazwa.pl → cache-bust przy weryfikacji.
- Indexing tylko przez `~/bin/index-submit` (budżet ad-hoc 100/dobę, pokaż zużycie).

## Do domknięcia niezależnie

- **Flaga danych:** karta Kredy nawozowej granulowanej (#305) ma w `pa_agria-dawkowanie` uciętą/błędną wartość „5 t/ha, 5-1" → poprawić przy najbliższym on-page produktów.
- **Raport M2 (lipiec)** — NIE teraz; koniec lipca/początek sierpnia (przypomnienie w kalendarzu „Auranet Claude" na 1.08). Wynik GSC dojrzewa 4–8 tyg → pomiar ~6.08 i ~3.09.

## Definicja „zrobione" dla tego wątku

Min. 1 strona opublikowana pod konkretną frazę z popytem, zgłoszona do indeksacji, z zapisaną datą i frazą-celem w `POMIAR_POD_WYNIK.md`. Wynik = obserwowalny ruch pozycji GSC (mierzony później), nie „zrobione technicznie".
