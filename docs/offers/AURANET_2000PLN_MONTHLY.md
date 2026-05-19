# Oferta Auranet: pakiet SEO + utrzymanie agria.pl

> Dokument roboczy oferty dla klienta AGRIA. Rozbity na dwa etapy z odrębną wyceną.
>
> **Wersja:** 2.0 (2026-05-19) — rewrite z monolitu 6×2000 PLN na M1 fundamenty + M2-M6 rozwój. Powód: `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md`.
>
> **Strategia bazowa:** `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md` — brak budżetu na linkbuilding zewnętrzny, wszystkie godziny pakietu na content / performance / baza wiedzy / narzędzia / analityka, jednocześnie pod future PPC.

---

## Struktura pakietu

| Etap | Okres | Zakres | Cena netto | Pracochłonność |
|---|---|---|---|---|
| **M1 — Fundamenty** | czerwiec 2026 (4 tygodnie) | Strategia + analityka + KR + content audit + plan on-page + baseline metryk | **~3 500–5 000 PLN** (do uściślenia) | ~20–25 h |
| **M2–M6 — Rozwój** | lipiec–listopad 2026 | Realizacja planu z M1: content, on-page, performance, narzędzia, raportowanie | **2 000 PLN / mies × 5 = 10 000 PLN** | 12–15 h / mies |
| **Razem** | 6 miesięcy | | **~13 500–15 000 PLN** | ~80–100 h |

**Sprzedaż M2–M6 uzależniona od dostarczenia M1.** Bez fundamentów M2–M6 jest spekulacją, nie strategią.

---

## Założenia handlowe (oba etapy)

- **Forma rozliczenia:** faktura VAT po dostarczeniu M1, następnie miesięczna VAT za M2–M6. Płatność do 14 dni.
- **Umowa:** ramowa na 6 miesięcy, klauzula 30-dniowego wypowiedzenia po stronie obu stron (działa od końca M1).
- **Zakres elastyczny w ramach godzin M2–M6** — klient może w danym miesiącu poprosić o przesunięcie akcentu (np. więcej content, mniej technical), o ile pula 12–15 h zachowana.
- **Co nie wchodzi w pakiet (oba etapy):**
  - Google Ads (budżet + obsługa — osobna pozycja, ~500–1 000 PLN obsługi + budżet reklamowy)
  - Sesja zdjęciowa (osobny projekt, 1 500–2 500 PLN)
  - Duże redesigny stron / nowe sekcje (>5 h projektu) — wycena osobno
  - Linkbuilding zewnętrzny płatny (artykuły sponsorowane, kupowane linki) — **świadoma decyzja**, patrz `docs/decyzje/2026-05-19-seo-bez-budzetu-linkbuilding.md`. Realokacja godzin → content i narzędzia.

---

## ETAP I — Miesiąc 1: Fundamenty

> Szczegółowy plan z roboczogodzinami per deliverable i harmonogramem tygodniowym T1–T4: `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md`.

### Dlaczego oddzielny etap

Miesiąc 1 to **inwestycja w fundamenty**, bez której kolejne 5 miesięcy byłoby strzelaniem do celu, którego nie widać. Auranet wcześniej (na własny koszt) wykonał audyt techniczny + analityczny agria.pl — wynik to **5 priorytetów P0, 9 P1, 8 P2** (executive summary niżej). M1 zamyka pętlę: od diagnozy do **planu wykonalnego** opartego o dane, nie założenia.

### 6 deliverables M1

1. **Strategia + plan 6-miesięczny**
   - Kierunek prac, segmenty priorytetowe (rolnictwo / sadownictwo / rybactwo / oczyszczalnie / budownictwo+drogownictwo+hurtownie+paszarstwo)
   - KPI biznesowe i SEO z baselinem
   - Harmonogram T1–T4 × M1–M6 (kalendarz prac)
   - Mapa odpowiedzialności Auranet ↔ AGRIA per miesiąc

2. **Wdrożenie analityki**
   - GA4 property (nowe lub w istniejącym koncie Auranet)
   - GTM container z konfiguracją eventów konwersji (formularze, kliknięcia telefonów, scroll, view_item dla WC)
   - Google Search Console verification (`sc-domain:agria.pl`) + sitemap submission
   - Consent Mode v2 banner (zgodność RODO + ePrivacy)
   - Looker Studio dashboard klientowi (3 widoki: ruch, frazy, konwersje)

3. **Keyword research**
   - 50–100 fraz priorytetowych w 5 klastrach segmentowych
   - Dane z DataForSEO Labs: volume, difficulty, CPC, intent, SERP features
   - Mapowanie do istniejących URL agria.pl (gdzie rankujemy → optymalizacja, gdzie brak → content gap → plan M2–M6)
   - Format: arkusz Google Sheets klientowi (kopia w `docs/seo/KEYWORDS_BASELINE.md`)

4. **Content audit + topic clusters**
   - Mapa aktualnego stanu: 6 postów blog + 19 produktów WC + 7 stron + 7 kategorii vs gaps
   - Topic clusters per segment (hub & spoke): hub artykuł kategorii + spokes per produkt / pytanie
   - Plan content kalendarza na M2–M6 (4–6 artykułów/mies, tematy z briefami)
   - AEO/Google AI Overviews readiness — które FAQ podpiąć pod schema FAQPage, kalkulatory pod HowTo

5. **Plan on-page poprawek**
   - Rozbicie P0/P1 z audytu baseline na zadania per miesiąc M2–M6
   - Per produkt / kategoria / strona: title, meta, H1, alt, schema, slug (jeśli warto)
   - Linkowanie wewnętrzne hubów tematycznych
   - Format: backlog z priorytetem (P0 = M2, P1 = M3–M4, P2 = M5–M6)

6. **Baseline metryk**
   - Punkt zerowy do mierzenia efektów: pozycje fraz priorytetowych w GSC, CWV multirun median (mobile + desktop), struktura ruchu w pierwszych 2 tyg. GA4, top URL-e
   - Raport startowy klientowi (PDF, 8–12 stron) — porównanie do tego raportu będzie pokazywać postęp w M3, M6

### Executive summary z audytu baseline 2026-05-19

Pełny audyt (~30 KB) jest wewnętrznym know-how Auranet (etap zerowy „na koszt Auranet"). Klient w pakiecie M1 dostaje **5 najważniejszych findings z konkretnymi liczbami**:

1. **Mobile LCP = 7,5 s na home** (powinno być <2,5 s). Główna przyczyna: brak preload LCP image + ciężkie zasoby Elementor + brak cache nazwa.pl. Wpływ: ranking mobile + UX + Quality Score Ads. Plan: P0-4 wdrożenie w M2.
2. **Brak GA4 / GTM / GSC live na produkcji** — strona działa od kwietnia 2026 bez analityki. Sześć tygodni utraconych danych. Plan: P0-1 wdrożenie w T1–T2 M1.
3. **Premmerce Permalink Manager 2.3.11 — DOM-XSS** (CVE-2025-XXXX, plugin czeka na patch 2.3.12+). Plan: P0-5 WAF rule + monitoring upstream w T1 M1.
4. **301 redirecty `/kategoria-produktu/*` brak** — po refactorze permalinkow utracone juice z legacy URL. Plan: P0-3 `.htaccess` 301 w T2 M1 (po pozyskaniu dostępu FTP).
5. **Schema Product na 19 produktach + LocalBusiness na 2 oddziałach brak** — utrata Rich Results w SERP. Plan: P0-2 wdrożenie przez RankMath Pro w T3 M1.

### Co Auranet potrzebuje od AGRIA dla M1

1. **Decyzyjny kontakt po stronie AGRIA** (1 osoba, e-mail + telefon) — pytania, akcept treści, pytania merytoryczne (24–48 h reakcji).
2. **Dostęp do WordPressa** (rola Administrator, konto dedykowane dla Auranet).
3. **Dostęp FTP/SFTP do nazwa.pl** — do wdrożenia P0-3 (301 redirecty) i P0-5 (WAF). Decyzja: konto Auranet czy konto klienta z time-boxed dostępem.
4. **Dostęp do Google Business Profile** (Manager) dla obu oddziałów — Niedomice + Radgoszcz. Jeśli nie istnieje któryś profil — Auranet utworzy w M1.
5. **Decyzje produktowe** — 4 pytania z `docs/catalog/CATALOG_VS_WC_GAP.md` (cement/kruszywo w WC, status Kredy czarnej jeziornej, warianty Agrobielik 90, konwencja SKU) wpływają na rekomendacje on-page. Slot 30 min z handlowcem AGRIA.
6. **Materiały merytoryczne do content** — handlowcy / dział techniczny dostępni do pytań eksperckich do content marketingu w M2–M6 (24–48 h reakcji per pytanie). Bez tego content traci E-E-A-T.

### Akcepty M1

- **T1:** kick-off + dostępy + pierwszy raport stanu analityki
- **T2:** keyword research + content audit do akceptu (Google Sheets klientowi)
- **T3:** strategia + plan on-page do akceptu (PDF)
- **T4:** Looker Studio dashboard live + raport startowy M1 (baseline) + plan M2–M6

Po dostarczeniu i odbiorze M1 → faktura M1 → start M2.

---

## ETAP II — Miesiące 2–6: Rozwój

### Stała pula 12–15 h pracy / miesiąc na:

#### 1. Technical SEO i utrzymanie (3–4 h / mies)
- Monitoring Core Web Vitals (LCP, INP, CLS) + reagowanie na spadki
- Update WordPress, WooCommerce, motywu i wtyczek (testy na staging, potem produkcja)
- Backup tygodniowy off-site (UpdraftPlus + zewnętrzny storage)
- Naprawa błędów 4xx/5xx z Search Console
- Optymalizacja obrazów (kompresja, WebP/AVIF, lazy loading)
- Monitoring uptime + security (po wdrożeniu WAF rule w M1)
- Drobne hotfixy (np. wyłączony formularz, błąd JS)

#### 2. On-page SEO (3–4 h / mies)
- Realizacja **planu on-page z M1** rozbitego per miesiąc (P0 → M2, P1 → M3-M4, P2 → M5-M6)
- Optymalizacja title + meta description (priorytet: produkty rankujące w pozycjach 10–30)
- Optymalizacja H1/H2 i struktury contentu
- Linkowanie wewnętrzne — budowa hubów tematycznych (np. „wapno do stawów" → linki z produktów + artykułów)
- Uzupełnianie alt tagów
- Schema.org — wdrożenie pozostałych typów (BreadcrumbList, FAQPage, HowTo, Product variants)
- Optymalizacja GBP dla obu oddziałów (posts, photos, Q&A, attributes)

#### 3. Content marketing (5–6 h / mies — **realokacja godzin po decyzji bez LB**)
- **4 artykuły blogowe / miesiąc**, ~1 200–1 500 słów każdy (vs 2 art. w pierwotnej ofercie — realokacja z linkbuildingu)
- Tematy z content kalendarza M1, sezonowo dopasowane:
  - **M2 lipiec** — rybactwo (sezon stawów), 4 art.
  - **M3 sierpień** — oczyszczalnie + osad ściekowy, 4 art.
  - **M4 wrzesień** — evergreen (poradniki dawkowania, tabele pH), refresh starych, 4 art.
  - **M5 październik** — jesienne wapnowanie + długi ogon, 4 art.
  - **M6 listopad** — budownictwo + drogownictwo, dotychczas pomijany segment, 4 art.
- Każdy artykuł: research SERP → outline → tekst → optymalizacja on-page → publikacja → indeksacja w GSC + Indexing API (gdzie applicable)
- AEO optimization w każdym artykule: passage-level citability, FAQ schema, jasne odpowiedzi w nagłówkach

#### 4. Narzędzia / baza wiedzy (1–2 h / mies)
- Utrzymanie i rozbudowa **kalkulatora wapnowania** (istniejący, do optymalizacji UX + SEO)
- Planowane nowe kalkulatory (decyzja per miesiąc w ramach godzin):
  - Kalkulator dawkowania dla stawów rybnych (M2)
  - Kalkulator wapna do oczyszczalni (M3)
  - Tabela parametrów per produkt z filtrowaniem (M4–M5)
- FAQ per segment — rozbudowa istniejących + nowe pytania z GSC + Google PAA

#### 5. Analityka i raportowanie (1–2 h / mies)
- Utrzymanie GA4 + GSC + GTM (po wdrożeniu w M1)
- **Miesięczny raport PDF** z KPI:
  - Sesje, użytkownicy, źródła ruchu (delta vs M-1 i vs baseline M1)
  - Top 20 fraz w GSC z pozycjami i CTR
  - Konwersje (formularze, telefony)
  - Core Web Vitals trend
  - Lista wykonanych zadań w miesiącu (transparentność)
- **Raport kwartalny** szerszy (po M3, M6) — zestawienie 3 miesięcy + rekomendacje na kolejny kwartał + decyzje strategiczne

#### 6. Wsparcie ad-hoc (1 h / mies)
- Odpowiedzi mailowe / telefoniczne (24 h reakcji w dni robocze)
- Drobne edycje treści zgłoszone przez handlowców
- Konsultacje przy decyzjach (nowy produkt, akcja sezonowa, dodanie strony)

---

## Cele realistyczne po 6 miesiącach

| KPI | Baseline (M1, czerwiec) | Cel (M6, listopad) | Skąd |
|---|---|---|---|
| Sesje organiczne / mies | baseline z M1 | **+50–100%** | Realokacja z LB → 4 art/mies + technical wins z M1 |
| Frazy w TOP 10 Google | baseline z M1 | **+15–25 fraz** | KR M1 + on-page systematyczne |
| Średnia pozycja w GSC | baseline z M1 | **poprawa o 5–10 miejsc** | CWV M2 + schema M1+M3 |
| Konwersje (formularze, telefony) | baseline z M1 | **+30–50%** | CTA optimization + landing per segment |
| Core Web Vitals mobile LCP | 7,5 s | **<2,5 s** (zielony) | P0-4 cache + CDN + preload |
| Indeksacja wartościowych URL | baseline z M1 | **100%** | GSC + Indexing API |
| **PPC readiness** | — | **strona gotowa pod Quality Score** | Dual-use efekt wszystkich powyższych |

**Uczciwie:** SEO to gra długoterminowa. Pierwsze efekty widoczne w M3, prawdziwy zwrot — od M4–M5. Dlatego umowa minimum 6 miesięcy.

**Wszystkie inwestycje SEO są dual-use** — przygotowują stronę pod Google Ads. Wysoki Quality Score wymaga CWV + UX + relevance, czyli dokładnie tego, co budujemy organicznie. Gdy klient zdecyduje się na PPC (osobny budżet) — start odbywa się z gotowej strony.

---

## Cennik dodatkowych usług (poza pakietem M1+M2-M6)

| Usługa | Stawka |
|---|---|
| Google Ads — obsługa (oprócz budżetu reklamowego) | 500–1 000 PLN / mies |
| Sesja zdjęciowa (1 dzień, 3 lokalizacje) | 1 500–2 500 PLN |
| Redesign sekcji strony / nowa podstrona (>5 h) | 150 PLN / h |
| Wdrożenie newslettera (setup + integracja) | 800–1 200 PLN |
| Wdrożenie chatu (Tawk / Smartsupp) | 400–600 PLN |
| Audyt techniczny powtórny (po roku) | 2 000 PLN |
| Linkbuilding zewnętrzny płatny (gdy klient zdecyduje uruchomić budżet) | wycena per projekt + budżet linków |

---

## Co nie wchodzi w zakres (warto wyjaśnić wprost)

- Nie projektujemy ulotek, wizytówek ani innych materiałów drukowanych (osobny projekt, w toku per zlecenie)
- Nie prowadzimy fan page'ów / social mediów
- Nie odpowiadamy na komentarze / wiadomości klientów AGRIA
- Nie obsługujemy klientów AGRIA bezpośrednio (np. nie wysyłamy ofert handlowych)
- Nie tworzymy nowych produktów w WooCommerce ze swojej inicjatywy — tylko na prośbę z danymi
- Nie kupujemy linków, nie publikujemy artykułów sponsorowanych (decyzja klienta, patrz ADR `2026-05-19-seo-bez-budzetu-linkbuilding.md`)

---

## Wersja do klienta — szkic listy bullet points

Do uproszczenia w finalnym dokumencie / mailu / prezentacji:

> **Pakiet Auranet dla AGRIA — fundamenty + 5 miesięcy rozwoju**
>
> **Etap I (M1, czerwiec 2026) — Fundamenty: ~3 500–5 000 PLN netto**
> ✅ Strategia SEO + plan na 6 miesięcy
> ✅ Wdrożenie analityki (GA4 + GTM + GSC + Consent v2 + Looker Studio dashboard)
> ✅ Keyword research — 50–100 fraz w 5 klastrach segmentowych
> ✅ Content audit + plan kalendarza
> ✅ Plan on-page rozbity per miesiąc (z 5 priorytetami P0 z audytu)
> ✅ Baseline metryk — punkt zerowy do mierzenia efektów
>
> **Etap II (M2–M6, lipiec–listopad 2026) — Rozwój: 2 000 PLN netto/mies × 5 = 10 000 PLN**
> ✅ Utrzymanie i bezpieczeństwo strony (update, backup, monitoring)
> ✅ Optymalizacja SEO on-page (produkty, kategorie, struktura)
> ✅ **4 artykuły eksperckie / miesiąc** (~1 200–1 500 słów każdy)
> ✅ Rozbudowa narzędzi (kalkulatory + FAQ + baza wiedzy)
> ✅ Schema.org, Core Web Vitals, Google Business Profile
> ✅ Comiesięczny raport PDF + kwartalny szerszy
> ✅ Wsparcie ad-hoc (do 24 h reakcji)
>
> **Razem 6 miesięcy:** ~13 500–15 000 PLN netto
>
> **Cel po 6 miesiącach:** +50–100% ruchu organicznego, +15–25 fraz w TOP 10, mobile LCP <2,5 s, strona gotowa pod Google Ads.

---

## Status

⏳ **Do prezentacji zarządowi AGRIA — pisemna oferta M1+M2-M6 z executive summary z audytu baseline.**

Kolejność akceptacji:
1. Klient akceptuje strukturę i kwoty → podpisanie umowy ramowej 6-miesięcznej
2. Start M1 (czerwiec 2026) → dostarczenie 6 deliverables zgodnie z `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md`
3. Akcept M1 → faktura M1 → automatyczny start M2
4. M2–M6 fakturowane miesięcznie

**Wypowiedzenie:** klauzula 30-dniowego wypowiedzenia po obu stronach, aktywna od końca M1 (M1 zawsze dostarczony i opłacony w całości).
