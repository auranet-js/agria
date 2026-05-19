# PROJECT_STATE.md — Stan projektu AGRIA

> Ostatnia aktualizacja: **2026-05-19** (po Wątku 2: rewrite oferty `AURANET_2000PLN_MONTHLY.md` na M1+M2-6 + utworzenie szczegółowego `MONTH_1_FOUNDATIONS_PLAN.md`). Plik aktualizowany przy istotnych zmianach. Czytany przez Claude'a na początku każdej sesji.

---

## Status ogólny

**Faza projektu:** FAZA II — aktywacja + sprzedaż usług marketingowych. Pakiet 6-miesięczny po stronie Auranet w stadium finalizacji oferty (rozbita na **M1 fundamenty** + **M2-M6 rozwój** — patrz `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md`).

**Auranet jako wykonawca:** zbudował stronę, identyfikację, katalog. Wykonał audyt baseline tech + analityka (`docs/audits/SEO_AUDIT_RESULTS.md`). Teraz domyka monetyzację współpracy — **M1 fundamenty (~20-25 h, większy budżet)** + **M2-M6 rozwój (~2000 PLN netto / mies × 5)**.

---

## Co jest gotowe ✅

### Infrastruktura strony
- **agria.pl** — uruchomione, WP 6.9.4, WC 10.6.1, motyw `Agria By Auranet 2.0.0`, PHP 8.3.30
- Hosting nazwa.pl (serwer371853)
- MCP `Agria.pl` skonfigurowany i działający — read-only dostęp do bazy, plików, WC

### Identyfikacja
- Logo (refresh) — gotowe
- Kolory firmowe ustalone:
  - Główny ciemnozielony `#354E33`
  - Akcent jasnozielony `#61CE70`
  - Drugorzędny `#798D7A`
  - Tekst `#596A5A`
- Typografia: Plus Jakarta Sans (nagłówki) + Bai Jamjuree (tekst)
- Ulotka A6 — gotowa, w produkcji
- Wizytówki — w przygotowaniu

### Katalog produktowy (druk)
- Spec 24-stronicowy gotowy (`docs/catalog/PRINT_CATALOG_SPEC.md`)
- Wzorzec JSX dla InDesign przygotowany na bazie Agrobielik 70 (`assets/AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx`)
- **Do zrobienia:** 17 pozostałych kart produktów (duplikacja + podmiana danych z MCP)

### WooCommerce
- 19 produktów opublikowanych
- Kategorie: Rolnictwo, Sadownictwo, Rybactwo, Oczyszczalnie, Budownictwo, Hurtownie, Paszarstwo
- Stan: patrz `docs/catalog/PRODUCTS_INVENTORY.md`

### Audyt baseline SEO (2026-05-19)
- ✅ Obszar 1 (technical) + obszar 7 (analityka) — wykonane
- Wynik: `docs/audits/SEO_AUDIT_RESULTS.md` (~30 KB pełen raport wewnętrzny Auranet)
- Drop klient-facing: `https://auratest.pl/fe4f58fec53ctmp/agria-audit-baseline-2026-05-19.md`
- Główne ustalenia: 5 P0, 9 P1, 8 P2 — patrz `docs/decyzje/2026-05-19-audyt-baseline-tech-analityka.md`
- Pozostałe obszary 2-6+8 audytu — w kolejnych wątkach

### Decyzje 2026-05-19 (ADR w `docs/decyzje/`)
- ✅ Pakiet rozbity na M1 (fundamenty, oddzielnie wyceniany) + M2-M6 (rozwój ~2000 PLN/mies)
- ✅ Strategia SEO bez budżetu na linkbuilding zewnętrzny — focus content / performance / baza wiedzy / narzędzia / analityka + dual-use pod future PPC
- ✅ Audyt baseline tech+analityka zakończony

### Pisemna oferta dla AGRIA (Wątek 2, 2026-05-19)
- ✅ `docs/offers/AURANET_2000PLN_MONTHLY.md` v2.0 — rewrite na M1 (~3500-5000 PLN) + M2-M6 (5×2000 PLN), z realokacją godzin LB → content (4 art/mies zamiast 2), z executive summary 5 findings z audytu baseline, dual-use pod PPC
- ✅ `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — szczegółowy plan M1: 6 deliverables × roboczogodziny, harmonogram T1-T4, akcepty, checklisty dostępów dla AGRIA, ryzyka, komunikacja

---

## Co jest w toku 🟡

### Pakiet Auranet — prezentacja klientowi
**Status:** dokumenty oferty gotowe. Czekamy na review Janka i prezentację zarządowi AGRIA.

**Kolejność działań:**
1. ✅ Audyt baseline tech + analityka (obszar 1+7) — `docs/audits/SEO_AUDIT_RESULTS.md`
2. ✅ Rewrite `docs/offers/AURANET_2000PLN_MONTHLY.md` na M1 fundamenty + M2-M6 rozwój
3. ✅ Utworzenie `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` (szczegóły M1)
4. ⏳ Review Janka + ew. korekty wycen / godzin / wording → finalna wersja prezentacji
5. ⏳ Drop klientowi: pisemna oferta M1+M2-M6 + executive summary z audytu baseline (drop na auratest)
6. ⏳ Keyword research jako proof-of-value oferty M1 — DataForSEO Labs, 50-100 fraz, 5 klastrów (opcjonalnie, jako załącznik do oferty)
7. ⏳ Prezentacja oferty zarządowi AGRIA → akcept → start umowy ramowej
8. ⏳ Audyt obszary 2-6+8 — w trakcie M1 (keyword research M4 pierwszy, on-page M2, content M3, konkurencja M5, UX M8)
9. ⏳ Po akceptacji M1: wdrożenie analityki (GA4, GSC, GTM, Consent v2, Looker Studio) jako billable deliverable T1-T2

**Uwaga operacyjna:** Janek może dodać Claude'owi dostępy do GA4/GSC/GTM klienta przed formalnym M1. W dokumentach klient-facing analityka pozostaje „do wdrożenia w M1" (billable). Po odbiorze M1 zasada gaśnie. Patrz `~/.claude/projects/-home-host476470-projekty-agria/memory/feedback_analytics_billable_deliverable.md`.

### Katalog 24-str
- 1/18 kart produktów gotowa (Agrobielik 70)
- Pozostałe 17 — generowanie z MCP `Agria.pl:catalog_product`

---

## Co jest zablokowane / czeka 🔴

- **Google Ads** — czeka na akceptację oferty miesięcznej i zatwierdzenie budżetu 3000 PLN/mies przez zarząd AGRIA
- **Baza oczyszczalni (Segment B)** — przygotowanie po stronie klienta (handlowiec B2B)
- **Sesja zdjęciowa** dla katalogu i strony — niezakontraktowane

---

## Decyzje, ustalenia, kompromisy

| Data       | Decyzja                                                                  | Status |
|------------|--------------------------------------------------------------------------|--------|
| Q1 2026    | Stack: WordPress + WooCommerce + Elementor (motyw autorski Auranet)     | ✅     |
| Q1 2026    | Paleta kolorów: zielenie zgodne z Elementor Global Colors                | ✅     |
| Q1 2026    | Z katalogu drukowanego wycinamy „Kredę czarną (jeziorną)" — **rozjazd** (produkt nadal publish w WC + jest w ulotce DL 2026-05-18) | ⚠️ do reweryfikacji |
| Q1 2026    | Katalog: 24 strony A4 zszywane, oprawa saddle stitch                     | ✅     |
| 2026-05-19 | Audyt baseline tech+analityka (obszar 1+7) zakończony — `docs/decyzje/2026-05-19-audyt-baseline-tech-analityka.md` | ✅ |
| 2026-05-19 | Pakiet 6-mies rozbity na M1 fundamenty + M2-M6 rozwój — `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` | ✅ |
| 2026-05-19 | SEO bez budżetu na linkbuilding zewnętrzny, focus content/perf/tools/analytics + dual-use pod PPC — `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md` | ✅ |
| 2026-05    | Format umowy: faktura miesięczna VAT, ramowa umowa na 6 mies            | ⏳     |

---

## Otwarte pytania do klienta

1. ~~Czy AGRIA ma ustawione **konto Google Ads** + dostęp do **Google Search Console**?~~ → **Zaadresowane:** analityka (GA4/GSC/GTM) wchodzi jako billable deliverable M1 fundamentów. Janek konfiguruje pod konto Auranet z dostępami przekazywanymi klientowi.
2. **Dostępy FTP/SFTP** do nazwa.pl — wymagane do wdrożenia P0-3 (`.htaccess` 301 dla `/kategoria-produktu/*`) i P1-1 (security headers). Czy na koncie Auranet, czy klienta? — do potwierdzenia w T1 M1.
3. **Zakres umowy** — pakiet M2-M6 dotyczy on-page + content + analityka (+ utrzymanie). NIE obejmuje: social media, sesji zdjęciowych, Google Ads (osobne pozycje, patrz `docs/offers/AURANET_2000PLN_MONTHLY.md` §„Cennik dodatkowych usług").
4. **Sesja zdjęciowa katalogu** — kto finansuje (1500–2500 PLN)?
5. **CRM** — Google Sheets na start wystarczy, czy klient chce coś poważniejszego (HubSpot Free, Pipedrive)?
6. **Kwota M1 fundamentów** — wstępnie zaakceptowana budżetowo, do uściślenia w pisemnej ofercie (~3500-5000 PLN orientacyjnie, ~20-25 h pracy).
7. **4 pytania z `docs/catalog/CATALOG_VS_WC_GAP.md`** — cement/kruszywo w WC, status Kredy czarnej jeziornej, warianty Agrobielik 90, konwencja SKU. Wpływa na rekomendacje P1 z audytu baseline. Slot z klientem AGRIA do umówienia.

---

## Następne kroki (operacyjnie)

### Wątek 2 — pisemna oferta (status po sesji 2026-05-19)
- [x] Rewrite `docs/offers/AURANET_2000PLN_MONTHLY.md` na M1 fundamenty + M2-M6 rozwój
- [x] Utworzenie `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` (szczegóły M1: roboczogodziny per deliverable, harmonogram T1-T4, milestones, akcepty)
- [ ] **Keyword research** — DataForSEO Labs, 50-100 fraz w 5 klastrach segmentowych (proof-of-value oferty M1; opcjonalnie jako załącznik do prezentacji)
- [ ] Drop klientowi: pisemna oferta M1+M2-M6 z executive summary z audytu baseline (drop na auratest po review Janka)

### Wątki 3-6 (kolejne sesje, w trakcie M1 lub po akceptacji)
- [ ] **Wątek 3:** on-page audit (obszar 2 z `SEO_AUDIT_PLAN.md`) + slug optimization
- [ ] **Wątek 4:** content audit + topic clusters (obszar 3) + plan content kalendarza
- [ ] **Wątek 5:** konkurencja content gap (obszar 5) + backlinks diag (obszar 6 skrócone)
- [ ] **Wątek 6:** UX + landing pages per segment (obszar 8) — pod PPC readiness

### Po akceptacji oferty M1 — T1-T4 czerwiec 2026
- [ ] Plan prac M1 wdrożeniowy: GA4 + GTM + GSC + Consent Mode v2 + Looker Studio
- [ ] Wdrożenie P0-2 (schema RankMath: Organization, LocalBusiness 2 oddziały, opening_hours)
- [ ] Wdrożenie P0-3 (`.htaccess` 301 dla `/kategoria-produktu/*`)
- [ ] Wdrożenie P0-5 (WAF rule dla Premmerce DOM-XSS + monitoring 2.3.12+ release)
- [ ] Wdrożenie P0-4 (cache nazwa.pl + CDN + Elementor performance settings + preload LCP)
- [ ] Raport końcowy M1 + baseline metryk + plan M2-M6 do akceptacji klienta

### Generacja katalogu drukowanego (niezależnie od pakietu SEO)
- [ ] Generacja JSX dla 16 pozostałych kart katalogu (wzorzec `assets/print/catalog/jsx/agrobielik-70.jsx`)
- [ ] Decyzje klienta z `docs/catalog/CATALOG_VS_WC_GAP.md` przed finalizacją katalogu
