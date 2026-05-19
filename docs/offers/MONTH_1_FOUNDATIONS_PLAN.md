# Miesiąc 1 — Plan fundamentów AGRIA (czerwiec 2026)

> Szczegółowy rozkład pracy M1 pakietu Auranet (`docs/offers/AURANET_2000PLN_MONTHLY.md`). Harmonogram tygodniowy, deliverables, akcepty, odpowiedzialności.
>
> **Cena:** 2 000 PLN netto (standardowa stawka miesięczna pakietu, faktura VAT z 14-dniowym terminem płatności).
> **Pracochłonność:** ~10–12 h pracy Auranet w okresie 4 tygodni (czerwiec 2026).
>
> **Co skraca M1 do 10-12h:** część scope została wykonana przez Auranet w fazie pre-M1 jako proof-of-value — audyt techniczny + analityczny (~6h), keyword research baseline (~4h), konfiguracja GA4+GTM+GSC (~5h), diagnoza i plan fix indeksacji (~3h). To ~18h pracy zostaje przy AGRIA niezależnie od dalszej współpracy, w M1 zostaje dopełnienie.
>
> **Bazowe decyzje:**
> - `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` — dlaczego M1 odrębny scope
> - `docs/decyzje/2026-05-19-korekta-ceny-m1-2000pln.md` — dlaczego cena 2000 PLN (nie premium)
> - `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md` — strategia bez budżetu LB
> - `docs/decyzje/2026-05-19-audyt-baseline-tech-analityka.md` — co wyszło z audytu zerowego
> - `docs/decyzje/2026-05-19-analityka-konfig-pre-m1.md` — analityka konfigurowana pre-M1 jako proof-of-value
> - `docs/decyzje/2026-05-19-fix-indeksacji.md` — diagnoza i plan Indexing API (executor od 2026-05-20 02:00)

---

## Pre-M1 — co Auranet już dostarczył (na koszt Auranet, w pakiecie)

| Deliverable | Wynik | Forma | Status |
|---|---|---|---|
| Audyt techniczny + analityczny | 5 P0 / 9 P1 / 8 P2 findings z metrykami (mobile LCP 7,5 s, brak GA4 live, schema brak, 301 brak, Premmerce DOM-XSS) | `docs/audits/SEO_AUDIT_RESULTS.md` + drop klientowi | ✅ |
| Keyword research baseline | 112 fraz w 8 klastrach segmentowych z DataForSEO Labs (volume / intent / 12-mies trend) | `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` + drop klientowi | ✅ |
| Konfiguracja GA4 + GTM + GSC | GA4 property utworzona, GTM container skonfigurowany, GSC sitemap RankMath submitted 2026-05-18 (38 URL) | Konta klientowi przekazane w T1 M1 razem ze skryptem GTM w `<head>` | ✅ Kontener gotowy, skrypt jeszcze nie w `<head>` |
| Diagnoza fix indeksacji | 8 hipotez zbadanych, config OK obecnie, historycznie `blog_public=0` przez większość okresu — plan Indexing API od jutra | `docs/decyzje/2026-05-19-fix-indeksacji.md` + executor | ✅ Diagnoza, executor 2026-05-20 02:00 |

**Razem pre-M1: ~18 h pracy.** Zostaje przy AGRIA bez fakturowania.

---

## 6 deliverables M1 — rozkład godzin (dopełnienie pre-M1)

| # | Deliverable | Godziny | Forma deliverable |
|---|---|---|---|
| 1 | Strategia + plan 6-mies | 2 h | PDF 8–12 stron klientowi |
| 2 | Dokończenie analityki (GTM live w `<head>`, eventy konwersji, Consent v2 banner, Looker Studio dashboard) | 3 h | Live na produkcji + dashboard klientowi |
| 3 | Priorytetyzacja KR (mapowanie 112 fraz baseline → URL agria.pl, wybór 30-50 priorytetowych) | 1,5 h | Google Sheets klientowi |
| 4 | Content audit + topic clusters + kalendarz M2–M6 (20 tematów) | 2 h | PDF kalendarz + macierz hub-spoke |
| 5 | Plan on-page poprawek (rozbicie P0/P1/P2 per miesiąc) | 1,5 h | Backlog Trello/Sheets klientowi |
| 6 | Baseline metryk + raport startowy M1 (kompendium 15-25 stron) | 1,5 h | PDF raport startowy |
| **Buffer** | Komunikacja, kick-off call, akcepty, korekty | 0,5–1,5 h | — |
| **Razem M1** | | **~10–12 h** | |

---

## Harmonogram tygodniowy T1–T4

> Tydzień = T (T1 = pierwszy tydzień czerwca). Końcówka tygodnia = piątek do południa, drop deliverable + akcept klienta poniedziałek następnego tygodnia (lub szybciej).

### T1 — Kick-off + dokończenie analityki (1–8 czerwca 2026)

**Cel:** uruchomić projekt, pozyskać dostępy, GTM live, decyzje produktowe.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Kick-off call (30 min) — agenda, role, kontakt decyzyjny po stronie AGRIA | 0,5 h | Auranet + AGRIA |
| Pozyskanie dostępów: WP Admin, FTP/SFTP nazwa.pl, GBP Manager (2 oddziały) | 0,5 h | Auranet (instrukcje) + AGRIA (wdrożenie) |
| Slot z handlowcem AGRIA (30 min) — 4 pytania z `docs/catalog/CATALOG_VS_WC_GAP.md` | 0,5 h | Auranet (pytania) + AGRIA (decyzje) |
| GTM `<script>` w `<head>` agria.pl + Consent Mode v2 banner + test | 1,5 h | Auranet |

**Deliverable końca T1:** mail do klienta z raportem stanu dostępów + roadmapem T2–T4 + linkiem do GTM/GA4 live.

**Akcept klienta:** potwierdzenie dostępów + decyzje z CATALOG_VS_WC_GAP.

**Razem T1: ~3 h.**

---

### T2 — Content audit + priorytetyzacja KR (9–15 czerwca 2026)

**Cel:** baseline 112 fraz zmapowany do URL, content audit przeprowadzony, topic clusters zaprojektowane.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Priorytetyzacja KR — mapowanie 112 fraz baseline do istniejących URL agria.pl, wybór 30-50 priorytetowych pod content M2–M6 | 1,5 h | Auranet |
| Content audit — inwentaryzacja 6 postów + 19 produktów + 7 stron + 7 kategorii vs gaps | 1 h | Auranet |
| Topic clusters — projekt hub & spoke per segment | 1 h | Auranet |
| GTM eventy konwersji (formularze, telefony, scroll, view_item WC) | 0,5 h | Auranet |

**Deliverable końca T2:**
- **Google Sheets klientowi:** priorytetyzacja KR (30-50 fraz z mapowaniem do URL i intencją)
- **PDF do akceptu:** content audit + topic clusters (3–5 stron)

**Akcept klienta:** zgoda na priorytetyzację fraz + akceptacja struktury topic clusters.

**Razem T2: ~4 h.**

---

### T3 — Strategia + plan on-page + content kalendarz (16–22 czerwca 2026)

**Cel:** strategia 6-mies napisana, plan on-page rozbity per miesiąc, content kalendarz M2–M6 z briefami.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Strategia 6-mies — kierunek prac, segmenty priorytetowe, KPI, harmonogram | 1,5 h | Auranet |
| Plan on-page — rozbicie P0/P1/P2 z audytu na zadania per miesiąc M2–M6 | 1 h | Auranet |
| Content kalendarz M2–M6 — finalizacja (20 tematów z briefami: 4 art × 5 mies) | 0,5 h | Auranet |

**Deliverable końca T3:**
- **PDF do akceptu:** strategia 6-mies (8–12 stron)
- **Backlog klientowi (Trello/Sheets):** plan on-page z priorytetami P0 → M2, P1 → M3-M4, P2 → M5-M6
- **PDF kalendarz:** 20 briefów contentowych

**Akcept klienta:** strategia + plan on-page → zielone światło na realizację M2–M6.

**Razem T3: ~3 h.**

---

### T4 — Dashboard + baseline + raport startowy (23–30 czerwca 2026)

**Cel:** wszystkie deliverables zamknięte, klient ma raport startowy i dashboard live, faktura M1.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Looker Studio dashboard — 3 widoki: ruch, frazy, konwersje | 1 h | Auranet |
| Baseline metryk — pozycje fraz priorytetowych (GSC), CWV multirun median (PageSpeed Insights), top URL-e (GA4 pierwsze 2 tyg) | 0,5 h | Auranet |
| Raport startowy M1 (PDF) — kompendium 6 deliverables + baseline + plan M2–M6 + executive summary z audytu | 1 h | Auranet |
| Końcowy call z klientem (30 min) — prezentacja raportu startowego, Q&A, kalendarz M2 | 0,5 h | Auranet + AGRIA |
| Faktura M1 | — | Auranet |

**Deliverable końca T4:**
- **PDF klientowi:** raport startowy M1 (15–25 stron) — kompendium fundamentów
- **Live klientowi:** Looker Studio dashboard (link share)
- **Faktura M1** wystawiona po finalnym akcepcie

**Akcept klienta:** raport startowy M1 → **odbiór M1** → start M2 (lipiec 2026).

---

## Co Auranet potrzebuje od AGRIA — checklista T1

> Każda pozycja blokująca = ryzyko opóźnienia M1 i przesunięcia M2. Wszystkie do dostarczenia w T1 (pierwszy tydzień).

| Co | Forma | Termin | Wymaganie |
|---|---|---|---|
| Decyzyjny kontakt po stronie AGRIA | e-mail + telefon | T1 dzień 1 | 1 osoba, 24–48 h reakcji na pytania |
| Dostęp do WordPressa | rola Administrator dla konta Auranet | T1 dzień 1–2 | Konto dedykowane (`auranet-admin@`) |
| Dostęp FTP/SFTP nazwa.pl | login + hasło lub klucz SSH | T1 dzień 2–3 | Do P0-3 (301 redirecty) + P0-5 (WAF) |
| Dostęp do GBP — Niedomice | rola Manager dla konta Auranet | T1 dzień 1–3 | Jeśli profil nie istnieje, Auranet utworzy |
| Dostęp do GBP — Radgoszcz | rola Manager dla konta Auranet | T1 dzień 1–3 | Jeśli profil nie istnieje, Auranet utworzy |
| Decyzje produktowe — slot 30 min z handlowcem | call lub e-mail | T1 dzień 3–5 | 4 pytania: cement/kruszywo w WC, Kreda czarna jeziorna, warianty Agrobielik 90, SKU |
| Materiały merytoryczne (kontekst do content M2–M6) | mail z linkami / dokumentami | T2 koniec | Karty produktów, normy PN-EN, parametry techniczne, case studies klientów AGRIA (jeśli są) |
| Dostęp do skrzynki mailowej do weryfikacji GSC (jeśli weryfikacja przez e-mail, nie DNS) | login + hasło lub forwarding | T2 dzień 1 | Tylko w awaryjnej ścieżce (preferujemy weryfikację DNS przez TXT record) |

**Eskalacja:** brak dostępów dłużej niż 5 dni roboczych = pisemne ostrzeżenie do klienta + ewentualne przesunięcie terminu M1.

---

## Co AGRIA dostaje w postaci dokumentów / aktywów

Na koniec M1 klient ma **fizycznie zgromadzony pakiet fundamentów**:

1. **Raport startowy M1** (PDF, 15–25 stron) — kompendium: stan strony, executive summary z audytu (pre-M1), strategia 6-mies, priorytetyzacja KR, content kalendarz, plan on-page, baseline metryk
2. **Strategia SEO 6-mies** (PDF, 8–12 stron) — kierunek, segmenty, KPI, harmonogram
3. **Priorytetyzacja keyword research** (Google Sheets) — 30–50 fraz priorytetowych wybranych z baseline 112 (pre-M1), z klastrami, mapowaniem do URL, intent, volume, difficulty
4. **Content kalendarz M2–M6** (PDF + Sheets) — 20 tematów (4 art × 5 mies) z briefami
5. **Plan on-page** (Trello/Sheets) — backlog zadań rozbity P0 → M2, P1 → M3–M4, P2 → M5–M6
6. **GA4 + GTM + GSC + Consent Mode v2 banner — live na agria.pl** (konta + dashboard skonfigurowane pre-M1, w T1 M1 idzie skrypt w `<head>` + banner)
7. **Looker Studio dashboard** — 3 widoki (ruch, frazy, konwersje), zostaje klientowi na zawsze
8. **Baseline metryk** — punkt zerowy do mierzenia efektów w M3, M6 i kolejnych
9. **Audyt baseline + KR baseline + diagnoza fix indeksacji** (już dostarczone w pre-M1 jako proof-of-value) — zostają niezależnie od kontynuacji

Wszystko zostaje przy kliencie nawet po zakończeniu współpracy (vendor lock-in tylko po stronie Auranet, nie odwrotnie).

---

## Ryzyka i mitigacje

| Ryzyko | Prawdopodobieństwo | Mitigacja |
|---|---|---|
| Brak dostępu FTP w T1 → przesunięcie P0-3/P0-5 do M2 | Średnie | Wykonujemy te wdrożenia w T2 M2, bez wpływu na cenę M1 |
| Brak akceptu priorytetyzacji KR / content kalendarza w terminie | Niskie | Ustalamy SLA klienta 48 h na akcept; brak akceptu = automatyczne przyjęcie po 5 dniach (klauzula umowy) |
| Klient zmienia priorytety segmentów w T3 | Średnie | Strategia ma w sobie 20 % bufora godzin (M2–M6) na realokacje; ad-hoc decyzje OK |
| GTM `<script>` nie zostaje wstrzyknięty w `<head>` w T1 | Niskie | Wdrożenie pierwsze w T1; jeśli dostęp WP się opóźnia, ścieżka alternatywna przez RankMath Custom Code |
| Premmerce patch 2.3.12+ nie wychodzi → WAF rule jako trwałe rozwiązanie | Średnie | WAF rule traktujemy jako trwałe; monitoring upstream w M2–M3 |
| Decyzje klienta z CATALOG_VS_WC_GAP zajmują >T1 | Wysokie | Plan on-page (deliverable 5) bazuje na worst-case (zachowujemy status quo); refinement po decyzjach |
| Klient odbiera M1 z opóźnieniem (>14 dni od T4) | Niskie | Klauzula umowy: deliverables uznane za odebrane po 14 dniach bez uwag |
| Indexing API (pre-M1 plan z 2026-05-19) wyczerpie quota przed zindeksowaniem 38 URL | Średnie | Quota 200/dobę, 38 URL = ~1 dzień; alternatywa: Bing Webmaster URL Submit + naturalna indeksacja przez Googlebot crawl po fix sitemap |

---

## Komunikacja w trakcie M1

- **Cotygodniowy raport mailowy** (piątki, ~17:00) — co zrobione, co dalej, co czeka na klienta
- **Slot consultingowy** — środy 14:00–15:00, dostępny na request (call jeśli temat)
- **Eskalacja** — Janek Schenk (`js@auranet.com.pl`) zawsze do dyspozycji do pilnych decyzji
- **Komunikacja do klienta** — wyłącznie przez Janka (zgodnie z globalnym `CLAUDE.md` §13). Drafty Claude/Auranet → gate Janka → klient

---

## Po M1 — co dalej

1. **Akcept raportu startowego M1** → faktura M1 wystawiona
2. **Automatyczny start M2** (lipiec 2026) zgodnie z planem on-page + content kalendarza
3. **Raport miesiąca M2** dostarczony 31 lipca 2026 (lub pierwszego roboczego sierpnia)
4. **Klauzula wypowiedzenia** aktywna od końca M1 — klient lub Auranet mogą zakończyć współpracę z 30-dniowym wypowiedzeniem (M1 zawsze zostaje opłacony w całości)

**Po M6 (listopad 2026):**
- Pełny re-audyt baseline → porównanie 6-mies vs M1 baseline
- Raport końcowy + rekomendacje na 2027
- Propozycja kontynuacji (renegocjacja stawki, ewentualne rozszerzenie zakresu o PPC / social / sesje zdjęciowe)

---

## Status

⏳ **Plan gotowy do prezentacji klientowi razem z `docs/offers/AURANET_2000PLN_MONTHLY.md`.**

Akceptacja klienta tej oferty + planu M1 → podpisanie umowy ramowej 6-miesięcznej → start T1 M1 (1 czerwca 2026 lub data uzgodniona).
