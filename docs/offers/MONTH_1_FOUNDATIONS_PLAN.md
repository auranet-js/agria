# Miesiąc 1 — Plan fundamentów AGRIA (czerwiec 2026)

> Szczegółowy rozkład pracy etapu I pakietu Auranet (`docs/offers/AURANET_2000PLN_MONTHLY.md`). Wycena, harmonogram tygodniowy, deliverables, akcepty, odpowiedzialności.
>
> **Cena:** ~3 500–5 000 PLN netto (do uściślenia w pisemnej ofercie po akcepcie struktury).
> **Pracochłonność:** ~20–25 h pracy Auranet w okresie 4 tygodni (czerwiec 2026).
> **Stawka godzinowa orientacyjna:** 175–200 PLN/h netto.
>
> **Bazowe decyzje:**
> - `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` — dlaczego M1 oddzielnie
> - `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md` — strategia bez budżetu LB
> - `docs/decyzje/2026-05-19-audyt-baseline-tech-analityka.md` — co wyszło z audytu zerowego

---

## 6 deliverables M1 — rozkład godzin

| # | Deliverable | Godziny | % budżetu | Forma deliverable |
|---|---|---|---|---|
| 1 | Strategia + plan 6-mies | 3 h | 12–15 % | PDF 8–12 stron klientowi |
| 2 | Wdrożenie analityki (GA4 + GTM + GSC + Consent v2 + Looker Studio) | 7 h | 30–35 % | Live na produkcji + dashboard klientowi |
| 3 | Keyword research (50–100 fraz, 5 klastrów) | 4 h | 16–20 % | Google Sheets klientowi + `docs/seo/KEYWORDS_BASELINE.md` |
| 4 | Content audit + topic clusters + kalendarz M2–M6 | 4 h | 16–20 % | PDF kalendarz + macierz hub-spoke |
| 5 | Plan on-page poprawek (rozbicie P0/P1/P2 per miesiąc) | 3 h | 12–15 % | Backlog Trello/Sheets klientowi |
| 6 | Baseline metryk + raport startowy | 2 h | 8–10 % | PDF raport startowy (baseline reference) |
| **Buffer** | Komunikacja, kick-off, akcepty, korekty | 2–4 h | 8–15 % | — |
| **Razem** | | **~20–25 h** | **100 %** | |

---

## Harmonogram tygodniowy T1–T4

> Tydzień = T (T1 = pierwszy tydzień czerwca). Końcówka tygodnia = piątek do południa, drop deliverable + akcept klienta poniedziałek następnego tygodnia (lub szybciej).

### T1 — Kick-off i dostępy (1–8 czerwca 2026)

**Cel:** uruchomić projekt, pozyskać dostępy, rozpocząć analitykę i KR.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Kick-off call (30 min) — agenda, role, kontakt decyzyjny po stronie AGRIA | 0,5 h | Auranet + AGRIA |
| Pozyskanie dostępów: WP Admin, FTP/SFTP nazwa.pl, GBP Manager (2 oddziały) | 1 h | Auranet (instrukcje) + AGRIA (wdrożenie) |
| Slot z handlowcem AGRIA (30 min) — 4 pytania z `docs/catalog/CATALOG_VS_WC_GAP.md` | 0,5 h | Auranet (pytania) + AGRIA (decyzje) |
| Setup GA4 property + GTM container w koncie Auranet | 2 h | Auranet |
| Start keyword research — eksport DataForSEO Labs dla 5 klastrów | 2 h | Auranet |

**Deliverable końca T1:** raport stanu dostępów + roadmap pozostałych 3 tygodni (mail do klienta).

**Akcept klienta:** potwierdzenie dostępów + decyzje z CATALOG_VS_WC_GAP.

---

### T2 — Keyword research + content audit (9–15 czerwca 2026)

**Cel:** dane KR gotowe do akceptu, zmapowane do URL, content audit przeprowadzony.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| KR — finalizacja, klasteryzacja, mapowanie do istniejących URL agria.pl | 2 h | Auranet |
| Content audit — inwentaryzacja 6 postów + 19 produktów + 7 stron + 7 kategorii | 2 h | Auranet |
| Topic clusters — projekt hub & spoke per segment | 2 h | Auranet |
| GTM eventy konwersji (formularze, telefony, scroll, view_item WC) | 2 h | Auranet |
| GSC verification `sc-domain:agria.pl` + sitemap submission | 0,5 h | Auranet |

**Deliverable końca T2:**
- **Google Sheets klientowi:** keyword research 50–100 fraz z mapowaniem do URL (przekazane do akceptu)
- **PDF do akceptu:** content audit + topic clusters (3–5 stron)

**Akcept klienta:** zgoda na priorytetyzację fraz (które segmenty pchamy w M2–M6 najmocniej) + akceptacja content kalendarza.

---

### T3 — Strategia + plan on-page (16–22 czerwca 2026)

**Cel:** strategia 6-mies napisana, plan on-page rozbity per miesiąc, Consent Mode v2 wdrożony.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Strategia 6-mies — kierunek prac, segmenty priorytetowe, KPI, harmonogram | 3 h | Auranet |
| Plan on-page — rozbicie P0/P1/P2 z audytu na zadania per miesiąc M2–M6 | 3 h | Auranet |
| Consent Mode v2 banner — wdrożenie + test | 1,5 h | Auranet |
| Content kalendarz M2–M6 — finalizacja (16 tematów + briefy) | 1 h | Auranet |

**Deliverable końca T3:**
- **PDF do akceptu:** strategia 6-mies (8–12 stron)
- **Backlog klientowi (Trello/Sheets):** plan on-page z priorytetami P0 → M2, P1 → M3-M4, P2 → M5-M6
- **Live na produkcji:** Consent Mode v2 banner

**Akcept klienta:** strategia + plan on-page → zielone światło na realizację M2–M6.

---

### T4 — Dashboard + baseline + raport startowy (23–30 czerwca 2026)

**Cel:** wszystkie deliverables zamknięte, klient ma raport startowy i dashboard live, faktura M1.

| Działanie | Godz. | Odpowiedzialny |
|---|---|---|
| Looker Studio dashboard — 3 widoki: ruch, frazy, konwersje | 2 h | Auranet |
| Baseline metryk — pozycje fraz priorytetowych (GSC), CWV multirun median (PageSpeed Insights), top URL-e (GA4 pierwsze 2 tyg) | 1,5 h | Auranet |
| Raport startowy M1 (PDF) — wszystkie 6 deliverables + baseline + plan M2–M6 + executive summary z audytu | 2,5 h | Auranet |
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

1. **Raport startowy M1** (PDF, 15–25 stron) — kompendium: stan strony, audyt findings, strategia 6-mies, KR, content kalendarz, plan on-page, baseline metryk
2. **Strategia SEO 6-mies** (PDF, 8–12 stron) — kierunek, segmenty, KPI, harmonogram
3. **Keyword research** (Google Sheets) — 50–100 fraz, klastry, mapowanie do URL, intent, volume, difficulty
4. **Content kalendarz M2–M6** (PDF + Sheets) — 16 tematów (4 × 4 mies × 1 art tytułowo + 4 art ulgowo M6) z briefami
5. **Plan on-page** (Trello/Sheets) — backlog zadań rozbity P0 → M2, P1 → M3–M4, P2 → M5–M6
6. **Konto GA4 + GTM + GSC + Consent Mode v2 banner** — wszystko live na agria.pl, z dostępami przekazanymi klientowi
7. **Looker Studio dashboard** — 3 widoki (ruch, frazy, konwersje), zostaje klientowi na zawsze
8. **Baseline metryk** — punkt zerowy do mierzenia efektów w M3, M6 i kolejnych

Wszystko zostaje przy kliencie nawet po zakończeniu współpracy (vendor lock-in tylko po stronie Auranet, nie odwrotnie).

---

## Ryzyka i mitigacje

| Ryzyko | Prawdopodobieństwo | Mitigacja |
|---|---|---|
| Brak dostępu FTP w T1 → przesunięcie P0-3/P0-5 do M2 | Średnie | Wykonujemy te wdrożenia z M1 zakresu w T2 M2, bez wpływu na cenę M1 |
| Brak akceptu KR / content kalendarza w terminie | Niskie | Ustalamy SLA klienta 48 h na akcept; brak akceptu = automatyczne przyjęcie po 5 dniach (klauzula umowy) |
| Klient zmienia priorytety segmentów w T3 | Średnie | Strategia ma w sobie 20 % bufora godzin (M2–M6) na realokacje; ad-hoc decyzje OK |
| GA4 trafia w okno przerwy w live → 6 tyg utraconych danych extended | Niskie | Wdrożenie w T1–T2, nie czekamy na koniec M1 |
| Premmerce patch 2.3.12+ nie wychodzi → WAF rule jako trwałe rozwiązanie | Średnie | WAF rule traktujemy jako trwałe; monitoring upstream w M2–M3 |
| Decyzje klienta z CATALOG_VS_WC_GAP zajmują >T1 | Wysokie | Plan on-page (deliverable 5) bazuje na worst-case (zachowujemy status quo); refinement po decyzjach |
| Klient odbiera M1 z opóźnieniem (>14 dni od T4) | Niskie | Klauzula umowy: deliverables uznane za odebrane po 14 dniach bez uwag |

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
