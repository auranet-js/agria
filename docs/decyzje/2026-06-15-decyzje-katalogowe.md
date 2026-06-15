# ADR 2026-06-15 — Decyzje katalogowe AGRIA (Janek)

> Status: zatwierdzone. Rozstrzyga część otwartych pytań z `docs/catalog/CATALOG_VS_WC_GAP.md`.

## Decyzje

1. **Oferta WC jest kompletna — 19 produktów.** AGRIA **nie sprzedaje materiałów drogowych** (cement / kruszywo drogowe / wapno palone drogowe). Pozycje te figurowały w planistycznych `PRINT_CATALOG_SPEC.md` / `PRODUCT_DATA_MAPPING.md`, ale to było aspiracyjne / błędne — **nie dodajemy ich do sklepu**. Klaster „drogownictwo" z keyword researchu (14k vol) = poza zakresem oferty, NIE traktować jako luki.

2. **Kreda czarna jeziorna (#303) — zostaje (publish).** Pierwotna decyzja Q1 „wycięta" zdezaktualizowana: produkt jest w ulotce DL (44% CaO, w produkcji) i opublikowany w WC. Pozostaje w ofercie. Aktualizuje `CATALOG_VS_WC_GAP` §1.

3. **Agrobielik 90 #311 — bez zmian.** Rzekoma niespójność „frakcja 2-8mm jako osobna karta" to artefakt PDF vs WC, nie problem produktu. Produkt opisany poprawnie, nie tworzymy wariantu ani osobnego SKU.

4. **Konwencja SKU — `PRODUCT_DATA_MAPPING.md` (AGR-001…021).** Finalna numeracja wg pełniejszego planu (obejmuje dolomit, kredę malarską). Bulk update 19 produktów przez WP-CLI **po potwierdzeniu dostępu** (P1-5, zaplanowane M5). Numeracja z `PRINT_CATALOG_SPEC.md` (AGR-001…017) odrzucona.

## Konsekwencje

- Content audit (`docs/audits/CONTENT_AUDIT_2026-06-15.md`) — skorygowany: usunięta rekomendacja rozbudowy produktowej o drogownictwo.
- `CATALOG_VS_WC_GAP.md` — pytania o cement/kruszywo (drogownictwo) i Agrobielik 90 zamknięte; Kreda czarna potwierdzona jako zostająca; SKU rozstrzygnięty.
- P1-5 (bulk SKU) odblokowany co do konwencji — czeka tylko na dostęp WP-CLI/FTP.

## Powiązane

- Memory: `project-agria-catalog-decisions`
- `docs/catalog/CATALOG_VS_WC_GAP.md`, `docs/catalog/PRODUCT_DATA_MAPPING.md`
