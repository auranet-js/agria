# ADR 2026-07-08 — Poprawny rdzeń URL/taksonomii produktów (Model A)

**Status:** zaakceptowany (Janek, 2026-07-08) — wdrożenie w toku.
**Kontekst inicjujący:** Janek zauważył, że produkty mają złe slugi/ścieżki — np. Agrobielik pod `/wapno-nawozowe-hurt/…`, „jakby jego główną kategorią był hurt". Polecił zbadać strukturę, bo „od tego trzeba zacząć całe SEO".

## Problem (zdiagnozowany na MCP + kodzie + żywej stronie)

1. **URL produktu** = `/{kategoria-główna}/{produkt}/` (Premmerce: `product: hierarchical`, `use_primary_category: on`).
2. **„Kategorię główną" wybiera źle:** Premmerce czyta primary **tylko z Yoasta** (`PermalinkListener.php:301`, `WPSEO_BASENAME`). AGRIA ma **RankMath** → primary ignorowany. Fallback `getWcPrimaryTerm` (linia 268): `wp_list_sort($terms,'term_id','DESC')[0]` = **kategoria o najwyższym `term_id`**. „Hurtownie" (769) założono prawie ostatnie → wygrywa u 13 produktów.
3. **`product_cat` pełni potrójną rolę** (potwierdzone Chrome + JSF 1471 `_source_taxonomy=product_cat`): (a) ścieżka URL, (b) opcje filtra „Zastosowanie" na `/oferta/`, (c) kafle-nawigacja.
4. **Redundancja:** równoległy atrybut `pa_agria-segment` trzyma te same 7 segmentów z pełnym, wielosegmentowym przypisaniem (identyczne liczności). Miał być źródłem filtra — filtr podpięto pod `product_cat` przez pomyłkę.

## Odrzucone rozwiązania

- **Mu-plugin / filtr `wc_product_post_type_link_product_cat`** — hack, dodaje trwałą zależność od kodu. Odrzucone przez Janka. „Od kiedy tak robimy?".
- **Instalacja Yoasta** — drugi plugin SEO obok RankMath, konflikt. Nie.
- **Zostawienie multi-membership + próba poprawy primary** — bez Yoasta/kodu nie da się wyrazić per-produkt primary wśród wielu kategorii. Ślepa uliczka.

## Decyzja — Model A (rdzeń danych, zero kodu)

Źródłem prawdy struktury jest **katalog drukowany** (`Agria-katalog-2026-05-04-web.pdf`): badge'y segmentów (pierwszy = wiodący, Hurtownie nigdy pierwsze) + kolejność stron (= menu_order).

1. **`product_cat` = jedna kategoria wiodąca per produkt** (segment = pierwszy badge). Jedna kategoria → Premmerce nie ma z czego źle wybierać → URL natywnie poprawny, bez kodu.
2. **Filtr „Zastosowanie" (JSF 1471)** przepięty `product_cat` → **`pa_agria-segment`** (pełne, wielosegmentowe dane). Filtr działa dalej wielosegmentowo.
3. **Hurtownie** usunięte z `product_cat` (zostają wartością `pa_agria-segment`) → nigdy nie w URL.
4. **menu_order** = kolejność katalogu.
5. **Slugi produktów** czyszczone ze śmiecia opakowaniowego (kategoria w ścieżce niesie frazę segmentową).
6. **19× 301** stary→nowy (+ archiwa kategorii, których slug się zmienia).

## Ustalenia szczegółowe (Janek, 2026-07-08)

- **Agrobielik 90 (311) / Oxyfertil 90 (312):** primary = **Rolnictwo** (wg badge katalogu; marka Agrobielik razem), mimo że treść kart akcentuje oczyszczalnie.
- **Bielik (309):** „Budownictwo za szeroko" → kategoria wąska `wapno-hydratyzowane` (nie „Budownictwo"), produkt `bielik` → `/wapno-hydratyzowane/bielik/`.
- **Kreda pastewna (307):** slug kategorii Paszarstwo `kreda-pastewna` → **`paszarstwo`**; produkt `kreda-pastewna` → `/paszarstwo/kreda-pastewna/`.
- **Kreda malarska (304):** poza katalogiem/segmentami → osobna mini-kat `kreda-malarska`, **wykluczona z filtra „Zastosowanie"** i kafli.
- **Kreda czarna jeziorna (303):** poza katalogiem, ale polepszacz glebowy → primary Rolnictwo.

Pełna mapa 19 produktów: `docs/catalog/URL_TAXONOMY_SIM_2026-07-08.md`.

## Kolejność wdrożenia (bezpieczna) + rollback

1. **Backup** (DB): `term_relationships` product_cat + pa_agria-segment, `postmeta` slugów, JSF 1471 meta, opcje. Do `~/backups/agria/2026-07-08/` + meta_key `*_bak20260708`.
2. **Weryfikacja parytetu** `pa_agria-segment` vs `product_cat` per-produkt (filtr nie może zgubić produktów).
3. **Przepięcie filtra** JSF 1471 `_source_taxonomy` → `pa_agria-segment`; weryfikacja /oferta/ (Chrome).
4. **Slugi kategorii:** Paszarstwo → `paszarstwo`; utworzenie `kreda-malarska`.
5. **PILOT (Dolomit 302):** product_cat={Rolnictwo}, slug=`dolomit`, menu_order; weryfikacja że URL `/wapno-nawozowe-rolnictwo/dolomit/` renderuje się natywnie + 301 ze starego. **Checkpoint — pokazać Jankowi.**
6. **Bulk** pozostałe 18 (analogicznie).
7. **301** (.htaccess FTP) wszystkie stare→nowe + archiwa.
8. **Usunięcie Hurtownie** z product_cat (po zdjęciu ze wszystkich).
9. **Weryfikacja** (Chrome + curl cache-bust) + `index-submit` 19 nowych URL.

**Rollback:** przywrócenie `term_relationships`/`postmeta`/JSF z backupu; 301 zdjąć z .htaccess. Wszystko odwracalne.

## Konsekwencje

- **+:** URL-e zgodne z segmentami (Dolomit 6600, wapno nawozowe 1300, kreda nawozowa 1000 w ścieżce rolniczej); `product_cat` = jedno znaczenie; brak custom kodu; filtr wielosegmentowy zachowany.
- **–:** archiwa Rybactwo/Sadownictwo/Oczyszczalnie znikają jako `product_cat` (zostają w filtrze; landing per segment osobno wg planu KR). Jednorazowy koszt 301 + re-indeksacja.
