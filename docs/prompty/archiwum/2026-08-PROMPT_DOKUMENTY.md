# Prompt startowy — dokumenty na `/do-pobrania/` (STR-08, STR-09)

> Utworzony 2026-08-07. Czytaj najpierw: `docs/operations/STRONA_BACKLOG_POPRAWKI.md` (partia #2) + STR-04 z partii #1 (analiza obecnego stanu strony 731).

## Stan wejściowy

Paweł przysłał 8 PDF-ów (mail [201], kopie w `/tmp/claude-mails/201/` — **przenieść do trwałego miejsca zanim /tmp zostanie wyczyszczony**) i poprosił o usunięcie wszystkich certyfikatów. Zero blokerów po stronie klienta, całość wykonalna przez MCP write + FTP.

## Zadania

- **STR-08** — wgrać 5 atestów + 3 karty charakterystyki Nordkalk (wyd. 1.1, aktualizacja 26.03.2025) na `/do-pobrania/` (strona 731, `_elementor_data`). Atesty to skany bez warstwy tekstowej — zmapować do produktów wizualnie (Read na PDF). **Sprawdzić, czy nowe karty zastępują obecne** — w sekcji „Karty charakterystyki" siedzą 3 starsze pozycje; jeśli to te same substancje, stare zdjąć, nie dublować.
- **STR-09** — usunąć całą sekcję „Certyfikaty" (5 pozycji wraz z nagłówkiem). Znika przy okazji dług z STR-04 (duplikat linku poz. 1 = poz. 2, literówki „ertyfikat").

## Gotchas (sprawdzone wcześniej w tym projekcie)

- Po każdej zmianie `_elementor_data` / `post_content` czyścić `_elementor_element_cache` (`a:0:{}`) — inaczej front pokazuje starą treść.
- CDN nazwa.pl: weryfikacja **zawsze** z cache-bustem.
- Backup przed zapisem: `_elementor_data_bak<data>` w meta + kopia do `~/backups/agria/<data>/`.
- Konwencja nazw plików: `agria-karta-produktu-<produkt>.pdf` (tak nazwano 17 kart w czerwcu) — dla atestów analogicznie `agria-atest-<produkt>.pdf`, dla charakterystyk `karta-charakterystyki-<substancja>.pdf`.

## Po wdrożeniu

`/do-pobrania/` nie miało crawlu od 12.04 i wisi w GSC z werdyktem „noindex" sprzed naprawy — po zmianach zgłosić do reindeksacji przez `~/bin/index-submit --project agria` (budżet dzienny, patrz globalny CLAUDE.md §10a).
