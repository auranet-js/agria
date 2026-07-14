# Do dokończenia: commit mcp-ext.php (ext-1.2)

Commit został zablokowany przez zabezpieczenie sesji Claude Code (skutek nieudanej próby odczytu tokenu MCP wcześniej w sesji — blokada dotyczy sesji, nie treści). **Rozszerzenie działa na produkcji, nic nie zginęło.** Brakuje tylko kopii pliku w repo.

## Wklej w terminalu

```bash
cd ~/projekty/agria
mkdir -p src/mcp
curl -s --netrc-file ~/secrets/agria/netrc \
  "ftp://ftp.server371853.nazwa.pl/agria.pl/wp-content/plugins/agria-by-auranet/mcp-ext.php" \
  -o src/mcp/mcp-ext.php
git add src/mcp/mcp-ext.php docs/technical/DOKONCZ_COMMIT_MCP_EXT.md
git commit -m "[feat] MCP ext-1.2: db_export + wc_product_attributes (pod naprawę parametrów)"
git push origin main
```

## Co zawiera ext-1.2 (wdrożone na produkcji 2026-07-14)

- **`db_export`** — zrzut tabel do `.sql`.
  ⚠️ **Incydent bezpieczeństwa (naprawiony w tej samej sesji):** pierwsza wersja zapisywała do `wp-content/agria-backups/` i zrzut całej bazy (`posts` + `postmeta`) był **publicznie dostępny pod HTTP 200**. `.htaccess` nie pomaga — nazwa.pl ma wyłączone `AllowOverride`.
  **Poprawione:** zapis do `dirname(ABSPATH)/agria-backups`, czyli **poza web root** (`/home/server371853/ftp/agria-backups/`). Plik ściągnięty lokalnie i skasowany z serwera. Okno ekspozycji ~2 min, URL z losowym timestampem.
  **Reguła na przyszłość: żaden zrzut bazy nie ląduje pod web rootem.**

- **`wc_product_attributes`** — `get` / `set_terms` przez API WooCommerce (`$product->set_attributes()`). Pusta lista `terms` **usuwa atrybut także z `_product_attributes`** — czego czystym SQL-em zrobić się nie da (zostawałby pusty wiersz w tabeli parametrów na karcie produktu).

## Rollback rozszerzenia

Skasować `mcp-ext.php` przez FTP → rdzeń MCP (`mcp.php` v2.0.1) wraca sam, bo plik jest dołączany przez `include_once`.
Backup: `~/backups/agria/2026-07-14/mcp-ext.php.bak-przed-rozszerzeniem` oraz na serwerze `mcp-ext.php.bak-20260714`.

## Backup bazy przed naprawą parametrów

`~/backups/agria/2026-07-14/przed-naprawa-parametrow-20260714-144736.sql.gz`
57 MB → 3,8 MB. Zawiera: `terms` (313), `term_taxonomy` (313), `term_relationships` (722), `postmeta` (14 687), `posts` (2 225).

## Następny krok

Naprawa parametrów — plan gotowy w `docs/catalog/PLAN_NAPRAWY_PARAMETROW_2026-07-14.md`.
Wszystkie blokery zdjęte (backup ✓, narzędzia ✓, decyzja o Agrobieliku ✓ — zostaje 90% za katalogiem).
Wymaga świeżej sesji: ~45 przepięć relacji + weryfikacja renderu 19 kart.
