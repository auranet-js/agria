# 2026-05-19 — Audyt baseline SEO (tech + analityka) zakończony

> ADR. Milestone wykonawczy etapu zerowego.

---

## Status

Zakończony 2026-05-19. Wynik wewnętrzny: `docs/audits/SEO_AUDIT_RESULTS.md`. Drop klient-facing: `https://auratest.pl/fe4f58fec53ctmp/agria-audit-baseline-2026-05-19.md`.

## Kontekst

`docs/seo/SEO_AUDIT_PLAN.md` zakładał 8 obszarów audytu zerowego na koszt Auranet (~20 h), wynik miał wylądować w `docs/audits/SEO_AUDIT_RESULTS.md`.

W sesji 2026-05-19 wykonano **obszar 1 (technical) + obszar 7 (analityka)** — szybsza ścieżka pozwalająca wystartować ofertę M1 bez czekania na pełne 20 h. Pozostałe obszary (2 on-page, 3 content, 4 keywords, 5 konkurencja, 6 backlinks diag-only po decyzji `2026-05-19-seo-bez-budzetu-linkbuilding.md`, 8 UX) zostają na kolejne sesje.

## Decyzja

**Audyt baseline obszarów 1 + 7 = zakończony.** Wynik:
- `docs/audits/SEO_AUDIT_RESULTS.md` (~30 KB) — pełen raport wewnętrzny Auranet
- Drop klient-facing executive summary: `https://auratest.pl/fe4f58fec53ctmp/agria-audit-baseline-2026-05-19.md`

## Główne ustalenia

### 5 P0 (krytyczne, do M1)

1. **Brak GA4/GTM/GSC** — zero danych frontowych od marca 2026 (6 tygodni live).
2. **Schema Organization `name="My Blog"`** — RankMath uruchomiony z defaultami (`website_name`, `knowledgegraph_name`, `og:site_name` wszystkie „My Blog").
3. **URL `kategoria-produktu/*` zwraca 404** zamiast 301 do nowych slugów Premmerce (`/wapno-nawozowe-rolnictwo/`, `/wapno-do-sadu/`, …). Każdy backlink na domyślny WC URL = stratny ruch.
4. **Mobile CWV FAIL na 4/5 audytowanych URL** — LCP 5,0–7,5 s (próg >4,0 s = fail), TBT 350–390 ms (INP proxy >200 ms). Wina: cache nazwa.pl off, CDN off, unused CSS Elementor.
5. **Premmerce 2.3.11 ma niefixed Freemius DOM-XSS** (CVSS 7,1 high, ujawniony 2026-04-30). Brak wersji z fixem. Wymaga WAF rule + plan B migracji.

### 9 P1, 8 P2

Szczegóły w pełnym raporcie. Najważniejsze P1: brak HSTS i security headers; title home 102 znaki (duplikuje AGRIA); zduplikowany canonical na kategoriach; brak product_cat w sitemap RankMath; 19/19 produktów ma `sku=null`; literówki `weglanowe`/`zawierajace` w 8 produktach; eksponowanie loginu admina (`js`) w schema/twitter:data1; HTML home 144 KB + duplikat widget Elementor 17×; brak Consent Mode v2 banner.

### 4 rekomendacje zależne od decyzji klienta

Wiążą się z otwartymi pytaniami z `docs/catalog/CATALOG_VS_WC_GAP.md`:
- bulk update SKU 19 produktów ↔ pyt #4 (cement/kruszywo numeracja AGR-XXX)
- aktualizacja decyzji o „Krędzie czarnej jeziornej" ↔ pyt #1 (decyzja Q1 mówiła „wycinamy", ale produkt nadal publish + jest w ulotce DL 2026-05-18)
- wariant frakcji Agrobielik 90 (2–8 mm) ↔ pyt z §2 mapy
- Cement / kruszywo / wapno drogowe w WC ↔ pyt z §1 mapy

## Konsekwencje

- **Obszary 2–6 + 8 audytu** — przeniesione na kolejne sesje, planowana kolejność:
  - **Wątek 2 (najbliższy):** rewrite oferty M1+M2-6 + keyword research (obszar 4)
  - **Wątek 3:** on-page audit (obszar 2) + slug optimization
  - **Wątek 4:** content audit + topic clusters (obszar 3)
  - **Wątek 5:** konkurencja content gap (obszar 5) + backlinks diag (obszar 6, skrócone)
  - **Wątek 6:** UX/landing pages per segment (obszar 8)
- **Pakiet M1 dla klienta** — uzasadnienie cyframi z tego audytu (np. „brak GA4 = 6 tyg live bez danych", „mobile LCP 7,5 s na home", „CVSS 7,1 niefixed na pluginie pkt 5").
- **Audyt jest wewnętrznym know-how Auranet** — klient dostaje executive summary + 5–7 findings, nie cały raport. Zgodnie z `docs/seo/SEO_AUDIT_PLAN.md` §„Deliverables audytu".

## Wykonane operacje techniczne podczas audytu

Dla kompletności — co Claude faktycznie zrobił:
- PSI batch: 5 URL × 2 strategie (mobile + desktop) + dorobiony URL kategorii Rolnictwo (źle podany w pierwotnym batchu jako `/kategoria-produktu/…` → 404)
- curl: HTTP headers, robots.txt, sitemap_index.xml + 4 sub-sitemapy (post, page, product, category)
- MCP `Agria.pl`: status, plugins_list, wc_products_list, query_db (rank-math-options-titles, rank_math_google_analytic_options, woocommerce_permalinks, premmerce_permalink_manager, terms, posts)
- CVE cross-check: Elementor 3.35.9, JetSmartFilters 3.7.5, Premmerce 2.3.11, WooCommerce 10.6.1 — Patchstack/WPScan
- WebFetch: wpscan.com/plugin/woo-permalink-manager — listing vulnerabilities
- Schema parsing: home + produkt Dolomit (Organization, WebSite, BreadcrumbList, ItemPage, Product z 19 PropertyValue)

Pełne pliki JSON PSI: `/tmp/agria-audit/psi/` (~8 MB, tymczasowe — nie w repo).

## Powiązane

- `docs/seo/SEO_AUDIT_PLAN.md` — plan 8 obszarów
- `docs/audits/SEO_AUDIT_RESULTS.md` — pełen raport wewnętrzny
- `docs/catalog/CATALOG_VS_WC_GAP.md` — niespójności PDF↔WC blokujące część rekomendacji
- `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md` — powiązana decyzja (obszar 6 skrócony)
- `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` — powiązana decyzja (raport uzasadnia M1)
- Drop klientowi: `https://auratest.pl/fe4f58fec53ctmp/agria-audit-baseline-2026-05-19.md`
