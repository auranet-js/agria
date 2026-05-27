# M1 KICKOFF — czerwiec 2026 (AGRIA)

> Operacyjny plan startowy realizacji M1 pakietu Auranet po akcepcie oferty (2026-05-27). Uzupełnienie `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` o **harmonogram pre-M1 (2026-05-28 → 2026-05-31)** i **operacyjne wykonanie T1-T4**.
>
> **Plan biznesowy:** `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` (deliverables, godziny, akcepty).
> **Backlog ad-hoc Pawła:** `docs/operations/BACKLOG_TRIAGE.md` (tworzony po 2026-05-28).
> **ADR akcepcji:** `docs/decyzje/2026-05-27-akcept-oferty.md`.

---

## Kontakty po stronie AGRIA

| Kto | Rola | Kontakt | Obszar |
|---|---|---|---|
| **Paweł Bigos** | Specjalista ds. Handlu i Marketingu | `pawel.bigos@agria.pl` / +48 664 393 062 | Operacyjny PoC: backlog, decyzje produktowe, content merytoryczny, slot z handlowcem |
| **Kasjan** *(nazwisko do potwierdzenia)* | Zarząd / budżet | (przez Pawła) | Decyzje finansowe, format umowy, akcept raportów odbiorowych |

**Reguła:** cała komunikacja przez Janka (`js@auranet.com.pl`) — Claude/Auranet nigdy bezpośrednio do klienta (`feedback_never_email_clients_directly`).

---

## Faza 0 — przygotowanie pre-M1 (2026-05-27 → 2026-05-31)

### Reguły obsługi klienta tej fazy

**Obsługa Pawła = telefon Janka, NIE email triage agencyjny.** Paweł zapowiedział kontakt ze „kilkoma istotnymi rzeczami do poprawy na stronie" — Janek rozegra to telefonicznie + nauczy Pawła self-edit przez Elementor (najtańsza operacyjnie obsługa ad-hoc poprawek). **NIE piszemy draftów email z frameworkiem klasyfikacji backlog (klasy A/B/C/D).** Framework triage = fallback wyłącznie dla wyjątkowej sytuacji (pisemne zgłoszenie dużej rozbudowy funkcjonalnej). Patrz memory `feedback_agria_pawel_relacja_telefoniczna`.

**Współpraca bez umowy pisemnej.** Akcept oferty mailowy Pawła z 2026-05-27 = wystarczająca podstawa. Faktury miesięczne VAT (post-payment) = standardowa praktyka, klient akceptuje przez opłacenie. NIE proponuj umowy ramowej PDF / klauzul wypowiedzenia / formalnych załączników. Klauzule typu „SLA akcept 48h" / „14 dni odbiór" zostają w tym dokumencie i `MONTH_1_FOUNDATIONS_PLAN.md` jako wewnętrzna konwencja Auranet, NIE wpisuj ich w komunikację do klienta. Patrz memory `feedback_agria_no_written_contract_trust_based`.

### Zadania Janka (operacyjne, na bieżąco)

| # | Co | Termin | Status |
|---|---|---|---|
| J1 | Telefoniczne rozmowy z Pawłem + nauka Elementor self-edit (ad-hoc poprawki) | bieżąco | ⏳ |
| J2 | Wysyłka checklist dostępów do AGRIA (template w sekcji „Checklist dostępów" niżej) | 2026-05-29 lub 2026-05-30 | ⏳ |
| J3 | Decyzja: termin płatności M1 (pre-payment 01.06 / post-payment 30.06) — sugestia post-payment | 2026-05-30 | ⏳ |

### Zadania Claude'a — sprint przygotowawczy deliverables M1 (28-31 maja)

Klient zaakceptował, dostępy będą dopiero 1-7 czerwca (T1). W okresie pre-M1 Claude realizuje **deliverables M1 wykonalne offline** (z MCP `Agria.pl` read-only + DataForSEO + repo + audyt baseline) tak, żeby w czerwcu T1-T4 były tylko: dostępy + wdrożenia live + akcepty klienta + raport.

| # | Deliverable M1 | Termin | Wynik | Status |
|---|---|---|---|---|
| C1 | **D3: Priorytetyzacja KR** — mapping 112 fraz baseline (`KEYWORD_RESEARCH_2026-05-19.md`) → URL agria.pl, wybór 30-50 priorytetowych z klastrami, intent, volume, difficulty | 2026-05-28 | Google Sheets do akceptu klienta (T2) | ⏳ |
| C2 | **D4: Content audit + topic clusters + kalendarz M2-M6** — inwentaryzacja 6 postów + 19 produktów + 7 stron + 7 kategorii vs gaps; topic clusters hub-spoke per segment; 20 briefów contentowych (4 art × 5 mies) | 2026-05-29 | PDF do akceptu (T2-T3) | ⏳ |
| C3 | **D5: Plan on-page** — rozbicie P0/P1/P2 z `SEO_AUDIT_RESULTS.md` na zadania per miesiąc M2-M6 | 2026-05-30 | Backlog Sheets (T3) | ⏳ |
| C4 | **D1: Strategia 6-mies** (syntetyzuje D3+D4+D5+audyt+KR baseline) | 2026-05-31 | PDF 8-12 stron klientowi (T3) | ⏳ |
| C5 | **D6 częściowo: Looker Studio template** — 3 widoki (ruch, frazy, konwersje), connectors GA4+GSC (puste do 1.06, struktura gotowa) | 2026-06-01 | Share link klientowi (T4) | ⏳ |
| C6 | ADR akcepcji + M1_KICKOFF + memory updates | 2026-05-27 | ✅ | ✅ |

**Co zostaje na czerwiec (T1-T4):**
- T1 (1-7.VI): kick-off call + pozyskanie dostępów + GTM live + Consent Mode v2 banner
- T2 (8-14.VI): wdrożenia P0 audytu (schema, .htaccess 301, WAF Premmerce) + akcept klienta D3+D4 z pre-M1
- T3 (15-21.VI): akcept D5+D1 z pre-M1 + ewentualne korekty
- T4 (22-30.VI): baseline metryk + raport startowy M1 (PDF kompendium) + końcowy call + faktura M1

**Efekt:** czerwiec staje się reaktywny (live wdrożenia, akcepty, ewentualne ad-hoc Pawła), nie produkcyjny — buffer pod nieprzewidziane sprawy klienta.

---

## Faza 1 — Realizacja M1 (1.06 → 30.06.2026)

### T1 — Kick-off + analityka live (1-7 czerwca)

**Cel produktowy:** GTM `<script>` w `<head>` agria.pl, Consent Mode v2 banner live, GA4 zbiera dane, dostępy pozyskane.

**Operacyjnie:**
- **Pon 01.06 rano** — kick-off call (30 min): agenda, role, kontakt decyzyjny, akcept harmonogramu
- **Pon-wto 01-02.06** — pozyskanie dostępów (WP Admin, FTP/SFTP, GBP Manager)
- **Śr-czw 03-04.06** — wdrożenie GTM + Consent Mode v2 (najpierw staging, potem prod wieczorem między 19-22 z backupem)
- **Pt 05.06** — test (DataLayer, GA4 DebugView, Consent Mode v2 statusy), mail raport tygodniowy
- **Pon 08.06** — akcept klienta + decyzje z `CATALOG_VS_WC_GAP.md` (slot z handlowcem)

**Ryzyko T1:** brak dostępu FTP do nazwa.pl blokuje P0-3/P0-5 w T2. **Mitygacja:** wymuszamy dostęp w T1 dzień 2-3, eskalacja do Pawła jeśli >3 dni.

**Deliverable końca T1:** mail raport + link do GA4 DebugView pokazujący live data.

### T2 — Wdrożenia P0 + audyt treści (8-14 czerwca)

**Cel produktowy:** schema RankMath (P0-2), `.htaccess` 301 (P0-3), WAF Premmerce (P0-5), audyt treści 19 produktów zakończony.

**Operacyjnie:**
- **Pon-wto 08-09.06** — schema RankMath: Organization, LocalBusiness ×2 (Niedomice + Radgoszcz, opening_hours, NAP zgodne z GBP)
- **Śr 10.06** — `.htaccess` 301 dla `/kategoria-produktu/*` (wieczorem, z testem na 10 URL przed bulk)
- **Czw 11.06** — WAF rule dla Premmerce DOM-XSS (Cloudflare/serwer-side, monitoring 2.3.12+ release w background)
- **Pt 12.06** — audyt treści 19 produktów + content gaps przeciwko KR baseline
- **Pt 12.06 EOD** — mail raport tygodniowy + Google Sheets z priorytetyzacją KR (30-50 fraz z mapowaniem do URL)

**Ryzyko T2:** schema RankMath wymaga akcept klienta dla danych firmowych (NIP, REGON, godziny otwarcia, telefon centralny). **Mitygacja:** szablon do akceptacji wysłany w T1 z mailem dostępowym.

**Deliverable końca T2:** Sheets KR priorytetyzacja + PDF audyt treści (3-5 stron) + schema live w GSC URL Inspector.

### T3 — Strategia + plan on-page + content kalendarz (15-21 czerwca)

**Cel produktowy:** strategia 6-mies PDF, plan on-page jako backlog Trello/Sheets, content kalendarz M2-M6 (20 briefów).

**Operacyjnie:**
- **Pon-wto 15-16.06** — strategia 6-mies (PDF 8-12 stron): kierunek, segmenty, KPI, harmonogram, miejsce pod ad-hoc Pawła z backlog M2-M6
- **Śr 17.06** — plan on-page (Trello/Sheets): rozbicie P0/P1/P2 audytu na zadania per miesiąc
- **Czw-pt 18-19.06** — content kalendarz M2-M6 (20 briefów: 4 art × 5 mies), zatwierdzenie tematów przez Pawła (handel ↔ marketing)
- **Pt 19.06** — mail raport tygodniowy + 3 deliverable do akceptu
- **Pon 22.06** — akcept klienta (strategia + plan on-page + kalendarz)

**Ryzyko T3:** akcept tematów contentu zajmuje >5 dni (handlowiec AGRIA musi merytorycznie ocenić). **Mitygacja:** klauzula umowy: brak feedback w 5 dni = automatyczna akceptacja.

**Deliverable końca T3:** strategia PDF + plan on-page Sheets + kalendarz PDF.

### T4 — Dashboard + baseline + raport startowy M1 (22-30 czerwca)

**Cel produktowy:** Looker Studio live, baseline metryk zarejestrowany, raport startowy M1 (PDF 15-25 stron), faktura M1 wystawiona.

**Operacyjnie:**
- **Pon-wto 22-23.06** — Looker Studio dashboard: 3 widoki (ruch, frazy, konwersje), GA4 + GSC connectors, share link klientowi
- **Śr 24.06** — baseline metryk: pozycje 30-50 fraz priorytetowych (GSC), CWV multirun median (PageSpeed Insights ×3), top URL-e GA4 (pierwsze 2 tyg czerwca), zapisane w `docs/audits/BASELINE_M1_2026-06.md`
- **Czw-pt 25-26.06** — raport startowy M1 (PDF 15-25 stron): executive summary, kompendium 6 deliverables M1, baseline, plan M2-M6, kalendarz, dashboard guide
- **Pon 29.06** — końcowy call z klientem (30 min): prezentacja raportu, Q&A, kalendarz M2
- **Wto-śr 30.06-01.07** — odbiór klienta + **faktura M1** (zgodnie z J4)

**Ryzyko T4:** klient nie odbiera raportu w terminie (>14 dni od T4). **Mitygacja:** klauzula umowy: deliverables uznane za odebrane po 14 dniach bez uwag.

**Deliverable końca M1:** raport startowy PDF + dashboard live + baseline + faktura M1.

---

## Checklist dostępów (template do wysyłki w J5)

> Mail do Pawła, do wysyłki ok. 2026-05-29/30. Treść w pierwszej osobie Janka, lista konkretna i klikalna.

**Co potrzebuję od Was, żeby ruszyć z M1 1 czerwca:**

1. **Konto WordPress** — utwórzcie rolę Administrator dla użytkownika `auranet-admin@agria.pl` (lub przekażcie istniejące dane logowania na adres `js@auranet.com.pl`)
2. **Dostęp FTP/SFTP do nazwa.pl** — login + hasło lub klucz SSH; potrzebujemy do wgrania 301 redirectów i security rule (Premmerce)
3. **Google Business Profile — centrala Tarnów** — dodajcie `js@auranet.com.pl` jako Manager
4. **(Opcjonalnie) GBP magazyny — Niedomice + Radgoszcz** — jeśli mają osobne profile, też Manager. Jeśli nie mają, omówmy czy warto je utworzyć (osobny temat).
5. **Kontakt decyzyjny merytoryczny** — kto z Was odpowiada na pytania dotyczące produktów (parametry techniczne, normy PN-EN, case studies klientów), z deklaracją 24-48h reakcji
6. **Slot 30 min z handlowcem** — w pierwszym tygodniu czerwca, mamy 4 konkretne pytania produktowe (cement/kruszywo w sklepie online, status Kredy czarnej jeziornej, warianty Agrobielik 90, konwencja kodów produktowych)
7. **NIP, REGON, dokładne godziny otwarcia centrali + magazynów, telefon główny** — do schema strony (chyba że potwierdzicie że dane na agria.pl/kontakt/ są aktualne)

Wszystkie dostępy do `js@auranet.com.pl` — Janek dystrybuuje wewnątrz Auranet.

Pozdrawiam,
Janek

---

## Komunikacja w trakcie M1

- **Cotygodniowy raport mailowy** — piątki ~17:00, format: co zrobione, co dalej, co czeka na klienta
- **Slot consultingowy** — środy 14:00-15:00 dostępny na request (call jeśli temat)
- **Eskalacja** — Janek (`js@auranet.com.pl`) zawsze do dyspozycji do pilnych decyzji
- **Drop na auratest** dla materiałów do oceny merytorycznej (audyty, raporty, drafty) — `https://auratest.pl/fe4f58fec53ctmp/agria-<typ>-YYYY-MM-DD.<ext>`

---

## Pre-M1 zostaje przy AGRIA bezpłatnie (przypomnienie)

Już dostarczone na koszt Auranet (proof-of-value, ~18h):
- Audyt techniczny + analityczny — `docs/audits/SEO_AUDIT_RESULTS.md`
- Keyword research baseline (112 fraz, 8 klastrów) — `docs/audits/KEYWORD_RESEARCH_2026-05-19.md`
- GA4 + GTM + GSC skonfigurowane (skrypt idzie live w T1)
- Diagnoza + plan fix indeksacji (executor Indexing API od 2026-05-20 02:00)

To zostaje przy AGRIA niezależnie od dalszej współpracy.

---

## Status

⏳ **Faza 0 w toku** (2026-05-27 → 2026-05-31).
🟢 **Faza 1 (M1) start 1.06.2026** zgodnie z `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md`.

**Następna aktualizacja tego pliku:** po przyjściu backlog Pawła (2026-05-28) — sekcja Faza 1 dopisana o pozycje klasy A.
