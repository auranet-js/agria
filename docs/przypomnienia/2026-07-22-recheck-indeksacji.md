# Recheck indeksacji — agria.pl (zaplanowany 2026-07-22)

> Przypomnienie z 2026-07-15. Kontekst: sesja fix produkcji + naprawa parametrów.

## Co sprawdzić

7 dni po zgłoszeniu 32 URL do Indexing API (2026-07-15) — czy weszły do indeksu i czy stare URL-e wypadły.

1. **GSC — indeksacja nowych URL-i.** Ile z 32 zgłoszonych (19 produktów pod `/wapno-nawozowe-rolnictwo/…` itd. + 5 kategorii + 7 stron + landing stabilizacji) jest zaindeksowanych. Narzędzie: `scripts/google/` (GSC API, `_lib.py`) — URL Inspection lub coverage. Alternatywnie sprawdzić `site:agria.pl` w SERP przez DataForSEO.
2. **Stare URL-e (301) mają wypaść** — `/wapno-nawozowe-hurt/…`, `/wapno-do-sadu/…` (19 archiwów). Sprawdzić czy Google przestał je pokazywać / przeniósł na nowe.
3. **Landing stabilizacji gruntu** (`/wapno-do-stabilizacji-gruntow/`) — czy zaindeksowany, na jakiej pozycji „stabilizacja gruntu" (DataForSEO SERP, było: brak — nowa strona).
4. **Sitemapa** — czy nadal czysta (19 nowych URL, 0 starych); RankMath potrafi odbudować cache plikowy — jeśli znów stare, usunąć `uploads/rank-math/*.xml` przez FTP.

## Jak wygląda „zrobione"
Wiem, ile URL-i w indeksie vs zgłoszonych, czy 301 wypadają, i mam pozycję startową landingu stabilizacji. Jeśli indeksacja utknęła — diagnoza (nie kolejny masowy re-submit; budżet Indexing API wspólny 100/dobę, patrz global CLAUDE.md §10a).

## Narzędzia / dane
- GSC: `scripts/google/_lib.py` (OAuth `~/secrets/google/tokens.json`), property `https://agria.pl/` (URL-prefix).
- DataForSEO: `~/secrets/dataforseo/` (curl), location 2616, lang pl.
- MCP agria: `query_db` (stan produktów), FTP dla sitemapy.
- Memory: `project_agria_indexation_diagnosis`, `project_agria_render_caching`.
