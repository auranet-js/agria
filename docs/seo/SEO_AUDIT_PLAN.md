# Plan audytu SEO + on-page agria.pl

> **Etap zerowy. Koszt po stronie Auranet.** Wynik: konkretna mapa zadań + uzasadnienie dla oferty 2000 PLN/mies × 6 mies.

---

## Cel audytu

Trzy poziomy:

1. **Operacyjny** — zidentyfikować błędy techniczne i contentowe, których naprawienie da klientowi szybki przyrost ruchu / pozycji.
2. **Sprzedażowy (dla Auranet)** — uzasadnić zakres prac wycenianych na 2000 PLN / mies × 6 mies. Pokazać klientowi konkretne deliverables, nie ogólne hasła.
3. **Baseline** — zapisać pomiary startowe (sesje, pozycje, CTR, Core Web Vitals), żeby za 6 miesięcy pokazać przyrost.

---

## Zakres audytu (8 obszarów)

### 1. Audyt techniczny
- **Core Web Vitals** (LCP, INP, CLS) — mobile + desktop, PageSpeed Insights + CrUX
- **Lighthouse** — Performance, Accessibility, Best Practices, SEO
- **Crawl Screaming Frog / Sitebulb** — błędy 4xx/5xx, redirecty, broken links, orphan pages, duplikaty
- **Indeksacja** — Search Console: pokrycie, wykluczone strony, błędy
- **Mapa strony XML** — czy istnieje, czy aktualna, czy podana w GSC
- **robots.txt** — czy nie blokuje czegoś wartościowego
- **Hreflang / canonical** — czy są poprawne (na razie tylko PL, ale sprawdzić canonicale na produktach z wariantami)
- **Schema.org** — Product, Organization, BreadcrumbList, LocalBusiness (2 oddziały!)
- **HTTPS, redirecty 301**, nagłówki HTTP, HSTS

### 2. Audyt on-page (struktura)
- **Title tags** wszystkie strony — długość, unikalne, fraza kluczowa, marka
- **Meta descriptions** — długość, CTA, unikalne
- **H1** — unikalne, jeden na stronę, ze słowem kluczowym
- **Hierarchia H2/H3/H4** — czy logiczna
- **Linkowanie wewnętrzne** — anchory, głębokość strony, kotwice
- **URL slugs** — czy SEO-friendly (np. `/wapno-nawozowe-agrobielik-70/` vs `/?p=310`)
- **Breadcrumbs** — czy są
- **Obrazy** — alty, kompresja (WebP / AVIF), lazy loading, wymiary

### 3. Audyt contentu
- **Strony produktowe (19 szt)** — długość opisów, struktura, parametry techniczne w tabelach, CTA
- **Strony kategorii** — czy mają opisy (nie tylko listę produktów)
- **Strona główna** — USP, segmentacja, social proof
- **Strony segmentowe** — czy istnieją landing page'e dla rolników / oczyszczalni / stawów (zgodnie ze strategią)
- **Blog** — czy istnieje, ile artykułów, czy są zoptymalizowane, czy są aktualizowane
- **FAQ** — czy są na produktach i segmentach

### 4. Audyt słów kluczowych
- **Aktualne pozycje** — Ahrefs / Senuto export — wszystkie frazy, na których domena jest w TOP 100
- **Frazy strategiczne (z strategii):** „wapno nawozowe", „wapno nawozowe Agrobielik", „wapno do stawów", „wapno do oczyszczalni" — na której pozycji są dziś?
- **Brakujące frazy** (keyword gap) — co rankuje konkurencja, a my nie
- **Frazy informacyjne** (długi ogon) — „kiedy wapnować glebę", „ile wapna na hektar", „pH stawu rybnego"
- **Lokalne frazy** — „wapno małopolska", „wapno Tarnów", „dostawa wapna Niedomice"

### 5. Audyt konkurencji
- **Top 5 konkurentów** w wynikach na frazy strategiczne (kogo Google pokazuje przed nami / razem z nami)
- **Backlink profile** porównawcze (Ahrefs)
- **Strategie contentowe** konkurencji — co publikują, ile, jak często
- **USP konkurencji** — co komunikują, czego my nie

### 6. Audyt backlinków
- **Profil linków** agria.pl — ile, jakiej jakości, anchory, kontekst
- **Toxic links** — czy są jakieś do disavow
- **Brakujące linki** — gdzie powinniśmy być (katalogi branżowe, izby rolnicze, portale środowiskowe)

### 7. Audyt analityki
- **GA4** — czy zainstalowane, czy zbiera eventy konwersji
- **Google Tag Manager** — czy jest, czy poprawnie skonfigurowany
- **Google Search Console** — czy zweryfikowana, ile zapytań/mies, top fraz
- **Cele konwersji** — czy są zdefiniowane (formularz, telefon, kliknięcie maila)
- **GA4 → Looker Studio** — czy jest dashboard, czy można pokazać klientowi
- **GDPR / cookies** — banner zgody, Consent Mode v2

### 8. Audyt UX / konwersji
- **Formularze** — gdzie są, ile pól, czy mają trackowanie
- **CTA** — czy widoczne, jaki copy, kontrast
- **Telefon** — czy klikalny (`tel:`), czy w stopce
- **Mapa Google** — czy oba oddziały (Niedomice + Radgoszcz) są w Google Business Profile
- **Mobile UX** — flow zakupu / zapytania na telefonie

---

## Narzędzia, których użyjemy

| Narzędzie | Cel | Koszt |
|-----------|-----|-------|
| Google PageSpeed Insights / CrUX | Core Web Vitals | free |
| Google Lighthouse | audyt techniczny | free |
| Google Search Console | indeksacja, zapytania | free |
| GA4 | ruch, eventy, konwersje | free |
| Screaming Frog (lub Sitebulb) | crawl | licencja Auranet |
| Ahrefs / Senuto | słowa kluczowe + backlinki + konkurencja | licencja Auranet |
| Schema.org Validator | walidacja structured data | free |
| Wave / axe-core | accessibility | free |
| MCP `Agria.pl:*` | stan DB, plików, plugins | własny |

---

## Czas i koszt audytu (po stronie Auranet)

| Obszar | Czas (h) |
|--------|----------|
| Audyt techniczny | 3 |
| Audyt on-page | 3 |
| Audyt contentu | 2 |
| Audyt słów kluczowych | 3 |
| Audyt konkurencji | 2 |
| Audyt backlinków | 1 |
| Audyt analityki | 1 |
| Audyt UX / konwersji | 1 |
| **Pisanie raportu + rekomendacje** | **4** |
| **Razem** | **~20 h** |

**Wycena wewnętrzna Auranet:** 20 h × stawka wewnętrzna = koszt projektu nieobciążający klienta.

---

## Deliverables audytu (do pliku `docs/seo/SEO_AUDIT_RESULTS.md`)

1. **Executive summary** — 1 strona, dla zarządu klienta.
2. **Lista zadań krytycznych** (P0) — błędy techniczne blokujące indeksację / wydajność.
3. **Lista zadań ważnych** (P1) — on-page, content, structured data.
4. **Lista zadań średnich** (P2) — UX, content development, linkbuilding.
5. **Baseline metryk** — tabela z dziś, do porównania za 6 mies.
6. **Mapa fraz priorytetowych** — 30–50 fraz na 6 mies pracy.
7. **Wstępny plan content marketingu** — tematy na 6 mies (2 art./mies = 12 sztuk).
8. **Rekomendacje technologiczne** — co trzeba doinstalować / wyłączyć / zoptymalizować (pluginy, cache, CDN itd.).

---

## Następnie

Po zamknięciu audytu → przygotowanie i prezentacja oferty 6-miesięcznej:
`docs/offers/AURANET_2000PLN_MONTHLY.md`

**Raport audytu nie idzie 1:1 do klienta.** Idą do niego:
- executive summary,
- 5–7 najważniejszych findings,
- konkretna oferta z miesięcznym planem prac.

Reszta zostaje wewnętrznym know-how Auranet, którego klient odbiera w postaci miesięcznych raportów.
