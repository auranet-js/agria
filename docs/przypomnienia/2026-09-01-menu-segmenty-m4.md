# Menu: przywrócić Sadownictwo / Rybactwo / Hurtownie (M4, wrzesień)

> Przypomnienie z 2026-07-30. Kontekst: sesja domknięcia lipca (recheck indeksacji + odblokowanie crawl).

## Skąd to się wzięło

30.07 zdjąłem z **menu głównego i stopki** trzy pozycje: **Sadownictwo**, **Rybactwo**, **Hurtownie**. Prowadziły do kategorii produktowych, które po migracji taksonomii z 08.07 zostały **puste** (`wapno-do-sadu`, `wapno-do-stawow`, `wapno-nawozowe-hurt` — 0 produktów) i są objęte 301 → `/oferta/`.

Skutek przed zmianą: **18 linków do 301-ek z każdej strony witryny** (menu + stopka, każda pozycja ×2), palących crawl budget w szczycie sezonu — w tym samym czasie, gdy 5 nowych stron lipcowych nie było w ogóle crawlowanych. Użytkownik klikający „Rybactwo" dostawał generyczną ofertę, nie segment.

Decyzja Janka 2026-07-30: zdjąć teraz, wrócą w M4 razem z prawdziwymi landingami.

## Co zrobić (M4, wrzesień)

1. **Utworzyć landingi segmentowe** (rdzeń M4 wg `docs/strategy/STRATEGIA_AGRIA_6MIES_2026.md` §M4): `/wapno-do-stawow/` (rybactwo), `/wapno-do-sadu/` (sadownictwo). Szablon: `BACKLOG_SEZON_2026-07-14.md` blok C („Szablon landingu C1–C7").
2. **Przywrócić pozycje menu** — odwrotność zmiany, jeden UPDATE:
   ```sql
   UPDATE {prefix}posts SET post_status='publish'
   WHERE post_type='nav_menu_item' AND ID IN (763,764,765,1564,1565,1566);
   ```
   (763 = Hurtownie, 764 = Sadownictwo, 765 = Rybactwo — pozycje top-level; 1564/1565/1566 — te same w submenu „Oferta".)
3. **Przepiąć cele** tak, by nie było 301 w nawigacji: Rybactwo → `/wapno-do-stawow/` (landing), Sadownictwo → `/wapno-do-sadu/` (landing), Hurtownie → `/oferta/` **bezpośrednio** (typ `custom`, nie `taxonomy` — kategoria hurt zostaje pusta, „hurt" to model sprzedaży, nie segment produktowy).
4. **Przepiąć stare 301 w `.htaccess`** (linie 25–27) z generycznej `/oferta/` na landingi tematyczne — `BACKLOG_SEZON_2026-07-14.md` blok E, sekcja „Rozstrzygnięcie starych 301". Dziś rozmywają sygnał tematyczny.
5. **Sprawdzić, czy nie wróciły 301 w nawigacji:** `curl -sL https://agria.pl/ | grep -o 'agria.pl/\(wapno-do-sadu\|wapno-do-stawow\|wapno-nawozowe-hurt\)/' | wc -l` → ma być 0 dla starych, a linki mają wskazywać nowe landingi.

## Jak wygląda „zrobione"

Menu i stopka mają Sadownictwo i Rybactwo wskazujące na **własne landingi z treścią** (HTTP 200, nie 301), Hurtownie → `/oferta/` bez przekierowania, a stare URL-e segmentowe przekierowują tematycznie, nie do generycznej oferty.

## Uwagi

- Zmiana jest **odwracalna w całości** — pozycje menu siedzą jako `draft`, nic nie zostało usunięte.
- Stopka używa tego samego menu WP (widget), więc zmiana pozycji menu działa w obu miejscach naraz — nie trzeba dłubać w `_elementor_data` szablonu 334.
- Kategorie `wapno-do-sadu` / `wapno-do-stawow` / `wapno-nawozowe-hurt` (termy 765, 766, 769) **zostają w bazie** z opisami — nie usuwać, mogą być przydatne przy landingach.

## Narzędzia / dane

- MCP agria: `query_db`, `query_db_write` (menu, treści).
- FTP: `~/secrets/agria/ftp.txt` + `netrc` — `.htaccess` (uwaga: wysyłka `curl -T` bywa blokowana przez klasyfikator, backup w `~/backups/agria/`).
- Memory: `project_agria_render_caching` (cache Elementora — **nie zerować przez `a:0:{}`**), `project_agria_indexation_diagnosis`.
