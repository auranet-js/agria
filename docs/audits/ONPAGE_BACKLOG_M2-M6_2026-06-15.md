# Plan on-page — backlog P0/P1/P2 per miesiąc (M2–M6)

> Deliverable M1 #5. Data: 2026-06-15. Źródło: `SEO_AUDIT_RESULTS.md` (5×P0 / 9×P1 / 8×P2) + stan live na 2026-06-15.
> **Zasada zakresu:** M1 = analityka + TEN plan. Wdrożenie P0/P1/P2 rozłożone na M2–M6 (`M1_KICKOFF.md` §Korekta zakresu).

## Status P0 na dziś (zmiany od audytu 19.05)

| Item | Audyt (19.05) | Stan 2026-06-15 |
|---|---|---|
| P0-1 GA4/GTM/GSC | brak danych | ✅ **GTM live wpięty** (Elementor Custom Code), GA4 `538301430` zbiera, GSC = `https://agria.pl/` |
| P0-6 indeksacja | 0 zaindeksowanych | ✅ zdiagnozowane (zaległy re-crawl) + **23 URL zgłoszone do Indexing API 15.06** |
| P0-2 schema „My Blog" | RankMath niezainicjalizowany | 🔴 **wciąż `knowledgegraph_name = "My Blog"`** — niezrobione |
| P0-3 `/kategoria-produktu/*` 404→301 | brak | ⬜ niezrobione (wymaga FTP/.htaccess) |
| P0-4 mobile CWV FAIL | LCP 5,0–5,2 s | ⬜ niezrobione |
| P0-5 Premmerce DOM-XSS | 2.3.11 niefixed | ⬜ monitoring 2.3.12+, WAF rule niezrobione |
| P1-9 Consent banner | brak | ⬜ CookieYes — ten tydzień |

## Backlog wdrożeniowy per miesiąc

### M2 (lipiec) — domknięcie P0 technicznych + start content
| Zadanie | Prio | Czas | Zależność |
|---|---|---|---|
| P0-2 Schema RankMath: Organization (NAP, NIP/REGON), LocalBusiness ×2 (Niedomice+Radgoszcz), poprawić „My Blog" | P0 | 1,5 h | dane firmowe od AGRIA |
| P0-3 `.htaccess` 301 dla `/kategoria-produktu/*` (test na 10 URL przed bulk) | P0 | 1 h | **dostęp FTP/SFTP nazwa.pl** |
| P0-5 WAF rule Premmerce DOM-XSS + monitoring release 2.3.12+ | P0 | 1 h | dostęp serwer/Cloudflare |
| P1-1 Security headers (HSTS, X-Content-Type, itp.) | P1 | 0,5 h | FTP/.htaccess |
| P1-4 product_cat w sitemap RankMath | P1 | 5 min | — |
| P1-2 Title home skrócić (102→~56 zn.) | P1 | 5 min | — |

### M3 (sierpień) — performance + porządki meta + content
| Zadanie | Prio | Czas | Zależność |
|---|---|---|---|
| P0-4 Mobile CWV: cache nazwa.pl + CDN + Elementor perf + preload LCP | P0 | 3 h | — |
| P1-3 Zduplikowany canonical na kategoriach product_cat | P1 | 15 min | — |
| P1-6 Literówki w 8 produktach (`weglanowe`→`węglanowe`, `zawierajace`→`zawierające`) | P1 | 30 min | — |
| P1-7 Eksponowanie loginu admina (`js`) w schema/twitter:data1 | P1 | 15 min | — |
| Content: 4 wpisy (rolnictwo, wg `CONTENT_AUDIT_2026-06-15.md`) | — | 6 h | — |

### M4 (wrzesień) — meta cleanup + on-page produktów + content
| Zadanie | Prio | Czas | Zależność |
|---|---|---|---|
| P1-8 HTML home 144 KB + ~17 duplikatów widgetu `elementor-element-3732dd1` | P1 | 1 h | — |
| On-page produkty: title/H1 pod realne frazy (per `ONPAGE_PLAN_2026-05-20`) | P1 | 2 h | — |
| `/cart/` wyciąć z sitemapy XML + sprawdzić duplikację `/category/poradniki/` vs `/poradniki/` | P2 | 30 min | — |
| Content: 4 wpisy (oczyszczalnie + rybactwo) | — | 6 h | — |

### M5 (październik) — katalog mode + SKU + content
| Zadanie | Prio | Czas | Zależność |
|---|---|---|---|
| P1-5 Bulk SKU dla 19 produktów (wszystkie `null`) | P1 | 2 h | **decyzja konwencji SKU (handlowiec)** |
| P2-4 WC katalog mode — refactor ukrywania CSS | P2 | 2 h | — |
| P2-3 Opening hours RankMath (weekend?) — weryfikacja z AGRIA | P2 | 15 min | dane AGRIA |
| Content: 4 wpisy (drogownictwo/budownictwo) | — | 6 h | **decyzja kruszywo/cement do WC** |

### M6 (listopad) — long-tail + AEO + domknięcia
| Zadanie | Prio | Czas | Zależność |
|---|---|---|---|
| Migracja Premmerce (P0-5 plan B jeśli brak fixa) | P0 | — | release vendora |
| P2-1 Orphans, P2-8 blog tempo → 4/mies | P2 | — | — |
| Content: 4 wpisy long-tail + FAQ/AEO (AI Overviews) | — | 6 h | — |

## Zależności od decyzji klienta (blokują pozycje powyżej)

| Decyzja (`CATALOG_VS_WC_GAP`) | Blokuje |
|---|---|
| Konwencja SKU (AGR-XXX finalna numeracja) | P1-5 bulk SKU (M5) |
| Kruszywo/cement do WC? | Klaster drogownictwo (14k vol) — kategoria + content M5 |
| Status Kredy czarnej jeziornej (#303) | inwentarz produktów |
| Warianty Agrobielik 90 | on-page produktów |
| Dane firmowe (NIP/REGON/godziny) | P0-2 schema (M2) |
