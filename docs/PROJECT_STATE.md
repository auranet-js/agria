# PROJECT_STATE.md — Stan projektu AGRIA

> Ostatnia aktualizacja: **2026-05-27** (oferta zaakceptowana przez klienta — Paweł Bigos po rozmowie z Kasjanem). Plik aktualizowany przy istotnych zmianach. Czytany przez Claude'a na początku każdej sesji.

---

## Status ogólny

**Faza projektu:** **FAZA III — REALIZACJA M1 (czerwiec 2026)**. Oferta stałej opieki SEO **zaakceptowana 2026-05-27** przez zarząd AGRIA (Paweł Bigos po rozmowie wczorajszej z Kasjanem — mail w `/tmp/claude-mails/18/`). Pakiet: **6 × 2 000 PLN netto / mies**, M1 z odrębnym scope (fundamenty), start czerwiec 2026.

**Co dalej:** Paweł zapowiedział kontakt w sprawie „kilku istotnych rzeczy do poprawy na stronie" — Janek rozegra telefonicznie + nauczy Pawła self-edit przez Elementor (NIE email triage agencyjny, patrz `feedback_agria_pawel_relacja_telefoniczna`). Claude w pre-M1 (28-31 maja) realizuje deliverables M1 wykonalne offline (priorytetyzacja KR, content audit, plan on-page, strategia 6-mies), żeby czerwiec T1-T4 był reaktywny. Plan kickoff M1 w `docs/operations/M1_KICKOFF_2026-06.md`.

Patrz: `docs/decyzje/2026-05-27-akcept-oferty.md` (ADR akcepcji), `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` (rozbicie scope), `docs/decyzje/2026-05-19-korekta-ceny-m1-2000pln.md` (kwota).

**Auranet jako wykonawca:** zbudował stronę, identyfikację, katalog. Wykonał audyt baseline tech + analityka (`docs/audits/SEO_AUDIT_RESULTS.md`), keyword research baseline (`docs/audits/KEYWORD_RESEARCH_2026-05-19.md`), konfigurację GA4 + GTM + GSC pre-M1 i diagnozę + plan fix indeksacji. Wszystko jako proof-of-value na koszt Auranet (~18h). Teraz domyka monetyzację — pakiet **6 × 2 000 PLN = 12 000 PLN**.

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
- ✅ Pakiet rozbity na M1 (fundamenty, odrębny scope) + M2-M6 (rozwój) — `2026-05-19-pakiet-rozbicie-m1-m2do6.md`
- ✅ **Cena M1 = 2 000 PLN (jak każdy inny miesiąc, nie premium)** — `2026-05-19-korekta-ceny-m1-2000pln.md` (korekta wieczorem 2026-05-19 z widełek 3500-5000)
- ✅ Strategia SEO bez budżetu na linkbuilding zewnętrzny — focus content / performance / baza wiedzy / narzędzia / analityka + dual-use pod future PPC
- ✅ Audyt baseline tech+analityka zakończony — `2026-05-19-audyt-baseline-tech-analityka.md`
- ✅ Analityka konfigurowana pre-M1 jako proof-of-value (API + chrome MCP fallback) — `2026-05-19-analityka-konfig-pre-m1.md`
- ✅ Fix indeksacji — diagnoza zamknięta, plan executor Indexing API od 2026-05-20 02:00 — `2026-05-19-fix-indeksacji.md`

### Pisemna oferta dla AGRIA (Wątek 2, 2026-05-19 — z korektą wieczór)
- ✅ `docs/offers/AURANET_2000PLN_MONTHLY.md` v2.1 — pakiet 6 × 2000 PLN = 12 000 PLN, M1 z odrębnym scope (2 000 PLN, ~10-12h), M2-M6 (5×2000 PLN, 12-15h/mies). Executive summary inline, realokacja godzin LB → content (4 art/mies), dual-use pod PPC. **Korekta ceny wieczorem 2026-05-19** z widełek 3500-5000 → 2000 PLN (patrz ADR `2026-05-19-korekta-ceny-m1-2000pln.md`)
- ✅ `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — szczegółowy plan M1: 6 deliverables × roboczogodziny (~10-12h), harmonogram T1-T4, akcepty, checklisty dostępów dla AGRIA, ryzyka, komunikacja. Pre-M1 proof-of-value rozpisane osobno (~18h na koszt Auranet, zostaje przy kliencie)

### Keyword research baseline (Wątek 2.5, 2026-05-19)
- ✅ `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` — 112 fraz w 8 klastrach segmentowych z DataForSEO Labs (suggestions+ideas+overview, koszt ~$0.15)
- Drop klient-facing: `https://auratest.pl/fe4f58fec53ctmp/agria-keyword-research-2026-05-19.md` (załącznik proof-of-value do oferty M1)
- Wyniki kluczowe:
  - **Drogownictwo dominuje volume** (~14 040/mies PL na top 30 fraz — `kruszywo wapienne` 260/mies + długi ogon)
  - **Rolnictwo i budownictwo** ex aequo (~3 200-3 700/mies każdy) — najlepszy stosunek volume/wdrażalność
  - **Oczyszczalnie ścieków = mikronisza** (3 fraz, 170/mies) — content informational + AEO, nie PPC, sektor przetargowy B2B
  - **Sezonowość krytyczna** dla rolnictwa (peak marzec + sierpień), drogownictwa (lato), budownictwa (cały rok)
  - **Paszarstwo / hodowla drobiu** wynurzyło się jako sub-segment (kurniki, kreda pastewna) — do walidacji z klientem czy chcemy dedykowany content
  - **Konkurenci wapna nawozowego:** Orcal, Kujawit, Atrigran, Supermag — gap analysis pod „X vs Agrobielik"
- Surowe dane: `~/scratch/agria-kw/` (suggestions/ideas/overview JSON + analyze.py + generate_report.py)

### Analityka pre-M1 (Wątek 3, 2026-05-19)
- ✅ GA4 property + GTM container skonfigurowane przez API (Janek założył puste, Claude skonfigurował)
- ✅ Google Search Console — `sc-domain:agria.pl` zweryfikowane, sitemap RankMath `sitemap_index.xml` submitted 2026-05-18 (38 URL: 6 post + 11 page + 20 product + 1 category)
- ⏳ GTM `<script>` jeszcze nie wstrzyknięty w `<head>` agria.pl — idzie live w T1 M1 razem z Consent Mode v2 banner
- ADR: `docs/decyzje/2026-05-19-analityka-konfig-pre-m1.md`

### Fix indeksacji (Wątek 4, 2026-05-19 wieczór)
- ✅ Diagnoza zamknięta — 8 hipotez zbadanych, dzisiaj config OK, historycznie `blog_public=0` przez większość okresu od sierpnia 2025 (alarm „38 submitted / 0 indexed" w GSC = problem historyczny, nie obecny)
- ✅ Plan executor Indexing API — od 2026-05-20 02:00 PL (po reset quota), 38 URL × ~3 dni quotа 200/dobę → ~1 dzień rzeczywistego dociągu
- ADR: `docs/decyzje/2026-05-19-fix-indeksacji.md`
- SEO_AUDIT_RESULTS.md zaktualizowany o sekcję historyczną indeksacji (38 linii)

---

## Co jest w toku 🟡

### Pakiet Auranet — REALIZACJA M1 (czerwiec 2026)
**Status:** oferta ZAAKCEPTOWANA 2026-05-27. Start M1 = 1 czerwca 2026. Plan: `docs/operations/M1_KICKOFF_2026-06.md`.

**Kolejność działań (sprzed startu M1, 2026-05-27 → 2026-05-31):**
1. ✅ Audyt baseline tech + analityka (obszar 1+7) — `docs/audits/SEO_AUDIT_RESULTS.md`
2. ✅ `docs/offers/AURANET_2000PLN_MONTHLY.md` v2.1 — pakiet 6 × 2000 PLN
3. ✅ `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — szczegóły M1
4. ✅ Drop klientowi: oferta wysłana 2026-05-25 13:34, **akcept 2026-05-27 10:39** (Paweł)
5. ⏳ **Sprint Claude pre-M1 (28-31 maja)** — D3 priorytetyzacja KR + D4 content audit/kalendarz + D5 plan on-page + D1 strategia 6-mies (offline, bez dostępów klienta)
6. ⏳ Janek rozegra ad-hoc Pawła telefonicznie + nauka Elementor (bez triage agencyjnego)
7. ⏳ Checklist dostępów do AGRIA (FTP nazwa.pl, GA4/GSC/GTM, GBP centrala, WP Admin) — wysyłka Janek 29-30 maja
8. ⏳ Decyzja Janka: pre-payment vs post-payment M1 (do 30 maja) — bez umowy pisemnej (Janek 2026-05-27: akceptacja mailowa wystarczy, patrz `feedback_agria_no_written_contract_trust_based`)

**Kolejność T1-T4 M1 (czerwiec 2026):** patrz `docs/operations/M1_KICKOFF_2026-06.md`.

**Uwaga operacyjna:** wszystkie deliverable M1 (analityka, audyt, KR, plan on-page) w dokumentach klient-facing pisz jako „do wykonania w M1" (billable). Patrz memory `feedback_analytics_billable_deliverable`.

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
| 2026-05-19 | Pakiet 6-mies rozbity na M1 fundamenty + M2-M6 rozwój (scope, nie cena) — `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` | ✅ |
| 2026-05-19 | **Cena M1 = 2 000 PLN, pakiet 6 × 2 000 = 12 000 PLN** (korekta wieczorem z widełek 3500-5000) — `docs/decyzje/2026-05-19-korekta-ceny-m1-2000pln.md` | ✅ |
| 2026-05-19 | SEO bez budżetu na linkbuilding zewnętrzny, focus content/perf/tools/analytics + dual-use pod PPC — `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md` | ✅ |
| 2026-05-19 | Analityka konfigurowana pre-M1 jako proof-of-value (API + chrome MCP fallback) — `docs/decyzje/2026-05-19-analityka-konfig-pre-m1.md` | ✅ |
| 2026-05-19 | Fix indeksacji — diagnoza zamknięta, executor Indexing API 2026-05-20 02:00 — `docs/decyzje/2026-05-19-fix-indeksacji.md` | ✅ |
| 2026-05-25 | Oferta stałej opieki SEO wysłana do AGRIA (mail + PDF, Paweł+Kasjan, 13:34) | ✅ |
| **2026-05-27** | **OFERTA ZAAKCEPTOWANA** przez Pawła po rozmowie z Kasjanem — `docs/decyzje/2026-05-27-akcept-oferty.md` | ✅ |
| 2026-05    | Format umowy: faktura miesięczna VAT, ramowa umowa na 6 mies            | ⏳ do uzgodnienia w T1 M1 |

---

## Otwarte pytania do klienta

1. ~~Czy AGRIA ma ustawione **konto Google Ads** + dostęp do **Google Search Console**?~~ → **Zaadresowane:** analityka (GA4/GSC/GTM) wchodzi jako billable deliverable M1 fundamentów. Janek konfiguruje pod konto Auranet z dostępami przekazywanymi klientowi.
2. **Dostępy FTP/SFTP** do nazwa.pl — wymagane do wdrożenia P0-3 (`.htaccess` 301 dla `/kategoria-produktu/*`) i P1-1 (security headers). Czy na koncie Auranet, czy klienta? — do potwierdzenia w T1 M1.
3. **Zakres umowy** — pakiet M2-M6 dotyczy on-page + content + analityka (+ utrzymanie). NIE obejmuje: social media, sesji zdjęciowych, Google Ads (osobne pozycje, patrz `docs/offers/AURANET_2000PLN_MONTHLY.md` §„Cennik dodatkowych usług").
4. **Sesja zdjęciowa katalogu** — kto finansuje (1500–2500 PLN)?
5. **CRM** — Google Sheets na start wystarczy, czy klient chce coś poważniejszego (HubSpot Free, Pipedrive)?
6. ~~**Kwota M1 fundamentów** — wstępnie zaakceptowana budżetowo (~3500-5000 PLN orientacyjnie, ~20-25 h pracy).~~ → **Zaadresowane:** decyzja Janka 2026-05-19 wieczór — M1 = 2 000 PLN jak każdy inny miesiąc (`docs/decyzje/2026-05-19-korekta-ceny-m1-2000pln.md`).
7. **4 pytania z `docs/catalog/CATALOG_VS_WC_GAP.md`** — cement/kruszywo w WC, status Kredy czarnej jeziornej, warianty Agrobielik 90, konwencja SKU. Wpływa na rekomendacje P1 z audytu baseline. Slot z klientem AGRIA do umówienia.

---

## Następne kroki (operacyjnie)

### Wątek 2 — pisemna oferta (status po sesji 2026-05-19 wieczór)
- [x] Rewrite `docs/offers/AURANET_2000PLN_MONTHLY.md` v2.1 — 6 × 2 000 PLN = 12 000 PLN, M1 odrębny scope, executive summary inline
- [x] `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — szczegóły M1 (~10-12 h), harmonogram T1-T4, pre-M1 proof-of-value rozpisane
- [x] **Keyword research baseline** — DataForSEO Labs, 112 fraz, 8 klastrów → `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` + drop na auratest
- [x] **Analityka pre-M1** — GA4 + GTM + GSC skonfigurowane (Wątek 3) + diagnoza fix indeksacji (Wątek 4)
- [x] **Korekta ceny M1** z widełek 3500-5000 → 2 000 PLN (decyzja Janka 2026-05-19 wieczór) — ADR + memory + dokumenty zaktualizowane
- [ ] Drop klientowi: pisemna oferta M1+M2-M6 + executive summary z audytu baseline + keyword research jako załącznik (po review Janka)
- [ ] Po akcepcie Janka — krótki mail + brandowany PDF jako załącznik (template z `~/projekty/auranet/docs/brand/pdf-templates.md`)

### Wątki 3-7 (zrealizowane częściowo, kontynuacja w trakcie M1 lub po akceptacji)
- [x] **Wątek 3:** konfiguracja analityki GA4 + GTM + GSC pre-M1 przez API (kontener opublikowany, skrypt jeszcze nie w `<head>` agria.pl — idzie live w T1 M1)
- [x] **Wątek 4:** diagnoza i plan fix indeksacji — `docs/decyzje/2026-05-19-fix-indeksacji.md`, executor Indexing API 2026-05-20 02:00
- [ ] **Wątek 5:** on-page audit (obszar 2 z `SEO_AUDIT_PLAN.md`) + slug optimization + mapowanie produktów WC na frazy z baseline KR
- [ ] **Wątek 6:** content audit + topic clusters (obszar 3) + plan content kalendarza M2-M6 (już ujęte w scope M1 T2-T3)
- [ ] **Wątek 7:** konkurencja content gap (obszar 5) + backlinks diag (obszar 6 skrócone)
- [ ] **Wątek 8:** UX + landing pages per segment (obszar 8) — pod PPC readiness

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
