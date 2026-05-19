# SEO_AUDIT_RESULTS — agria.pl, baseline tech + analityka

> **Etap zerowy SEO audit. Sesja 2026-05-19. Koszt po stronie Auranet.**
> Pokrycie tej rundy: obszar **1 (technical)** + obszar **7 (analityka)** z `docs/seo/SEO_AUDIT_PLAN.md`.
> Obszary 2–6 + 8 (on-page, content, keywords, konkurencja, backlinks, UX) — kolejne sesje.
>
> **Metody:** PageSpeed Insights v5 (mobile + desktop, single-run lab, klucz `~/secrets/google/psi-crux-key.txt`), curl headers/robots/sitemap, MCP `Agria.pl` (query_db, plugins_list, wc_products_list), CVE cross-check WPScan/Patchstack.
>
> **Stan repo / live odczytany:** WP 6.9.4, WC 10.6.1, PHP 8.3.30, motyw `Agria By Auranet 2.0.0` (parent: `hello-elementor`), prefix `wpfz_`, 19 produktów publish, 6 postów blog.

---

## Executive summary (1 strona, dla zarządu klienta)

Strona agria.pl ma **dobre fundamenty techniczne** (HTTPS, HTTP→HTTPS redirect 301, www→non-www 301, WP+WC aktualne, RankMath Pro skonfigurowany dla treści, Product schema z 19 propertyValue, sitemap RankMath aktywny), ale **5 obszarów wymaga natychmiastowej naprawy** zanim ruszymy kampanie SEO/PPC:

1. **Brak jakiejkolwiek analityki frontowej.** Strona nie ma GA4, GTM, ani GSC verification meta. **Sześć tygodni live = zero danych o ruchu.** Bez tego nie da się ani zmierzyć efektu naszej pracy, ani uzasadnić oferty 6-miesięcznej cyframi.
2. **Schema.org Organization name = „My Blog".** RankMath uruchomiony z domyślnymi wartościami. Google indeksuje firmę pod nazwą „My Blog", nie „AGRIA Sp. z o.o.". Zerowy E-E-A-T, brak knowledge graph, brak LocalBusiness.
3. **Stary URL `kategoria-produktu/*` zwraca twarde 404** zamiast 301 do nowych slugów (efekt Premmerce). Każdy link zewnętrzny / zakładka klienta w domyślnej strukturze WC = stratny ruch + signal „broken" dla Google.
4. **Mobile Core Web Vitals na produktach FAIL** (LCP 5,0–5,2s, INP-proxy TBT 350–390ms — wszystkie poza progiem Google). To 80% ruchu mobilnego, więc rankowanie produktów ucierpi mimo dobrego on-page.
5. **Wtyczka Premmerce 2.3.11 ma niefixed Freemius DOM-XSS** (CVE czeka, CVSS 7,1 high, ujawnione 2026-04-30). Aktualnie nie ma wersji, która to naprawia. Trzeba monitorować update lub rozważyć podmianę pluginu.

Wszystkie pięć są **w zasięgu naprawy w pierwszym miesiącu pracy** (z wyjątkiem #5, który wymaga wydania od dostawcy — monitoring + plan B).

**Pakiet 2000 PLN / mies × 6 mies pokrywa to wszystko**, plus on-page, content, link building w kolejnych miesiącach (sesje audytu 2–6 + 8 dostarczą reszty rekomendacji).

---

## Baseline metryk (do porównania za 6 miesięcy)

### PageSpeed Insights — 6 URL × 2 strategie, 2026-05-19

| URL | Strategia | Perf | A11y | BP | SEO | LCP | TBT (INP-proxy) | CLS | FCP |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `/` (home) | mobile | **70** | 91 | 92 | 100 | **7,5 s** ❌ | 0 ms ✓ | 0,002 ✓ | 3,0 s |
| `/` (home) | desktop | 93 | 92 | 96 | 100 | 1,4 s ✓ | 0 ms ✓ | 0,01 ✓ | 0,8 s ✓ |
| `/wapno-nawozowe-rolnictwo/` | mobile | 75 | 94 | 96 | 100 | **5,6 s** ❌ | 0 ms ✓ | 0 ✓ | 2,7 s |
| `/wapno-nawozowe-rolnictwo/` | desktop | 95 | 84 | 100 | 100 | 1,3 s ✓ | 0 ms ✓ | 0,006 ✓ | 0,8 s ✓ |
| `/wapno-nawozowe-hurt/dolomit-worek-25kg/` | mobile | **66** | 81 | 96 | 100 | **5,0 s** ❌ | **350 ms** ❌ | 0,011 ✓ | 3,4 s |
| `/wapno-nawozowe-hurt/dolomit-worek-25kg/` | desktop | 92 | 82 | 100 | 100 | 1,2 s ✓ | 170 ms ✓ | 0,027 ✓ | 0,9 s ✓ |
| Kreda czarna (#303) | mobile | **65** | 82 | 96 | 100 | **5,2 s** ❌ | **360 ms** ❌ | 0,002 ✓ | 3,5 s |
| Kreda czarna (#303) | desktop | 84 | 82 | 100 | 100 | 1,2 s ✓ | 290 ms ❌ | 0,002 ✓ | 0,9 s ✓ |
| Kreda granulowana (#305) | mobile | **65** | 81 | 96 | 100 | **5,0 s** ❌ | **390 ms** ❌ | 0,007 ✓ | 3,4 s |
| Kreda granulowana (#305) | desktop | 95 | — | — | 100 | 1,2 s ✓ | 90 ms ✓ | 0,001 ✓ | — |

**Pełne pliki JSON:** `/tmp/agria-audit/psi/*.json` (kopia w `~/projekty/agria/` nie — duże, łącznie ~8 MB).

**Progi Google CWV (pass / needs / fail):** LCP ≤2,5 / 2,5–4,0 / >4,0 s; INP ≤200 / 200–500 / >500 ms; CLS ≤0,1 / 0,1–0,25 / >0,25.

**Caveat:** single-run PSI lab ma ~14–34% wariancji LCP/TBT na mobile slow (pomiar Victorini 2026-05-16/17, memory `feedback_psi_lab_variance`). **Pojedynczy run NIE wystarcza do wnioskowania o efekcie patcha** — dla baseline OK, dla decyzji „czy patch działa" potrzebny multirun (3–5) + median. CrUX field empty dla wszystkich URL (ruch za niski) — będzie dostępny dopiero po wzroście trafficu.

### Infrastruktura

| Parametr | Wartość |
|---|---|
| HTTPS | ✓ działa (Apache/2, hosting nazwa.pl) |
| HTTP → HTTPS | ✓ 301 |
| www → non-www | ✓ 301 |
| HSTS | ❌ brak headera |
| Inne security headers (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy) | ❌ brak |
| Cache nazwa.pl | ❌ wyłączony (`na-ls-cache-enabled: off`) |
| CDN nazwa.pl | ❌ wyłączony (`cdn=disabled`) |
| HTML size home | 144 621 bajtów (przed kompresją) |
| robots.txt | ✓ obecny, blokuje wc-logs/transient/uploads/wp-admin |
| sitemap_index.xml | ✓ obecny, RankMath; ujęte: post (6), page (8), product (20 url), category (1 — tylko `category/poradniki/`) |
| Canonical | ✓ obecny, ale **zduplikowany** na kategoriach product_cat (Rank Math + Premmerce wstrzykują osobno) |
| Schema Product | ✓ obecny na produktach, 19 PropertyValue (CaO, MgO, dawkowanie, reaktywność, frakcja, segment, dostępność) |
| Schema Organization | ❌ `name="My Blog"`, `logo.caption="My Blog"` |
| Schema WebSite | ❌ `name="My Blog"` |
| Schema BreadcrumbList | ✓ obecny |
| og:site_name | ❌ `"My Blog"` |
| twitter:data1 (autor) | ⚠️ `"js"` — eksponuje login admina |

### Analityka

| System | Status |
|---|---|
| GA4 | ❌ Brak. RankMath ma puste `rank_math_google_analytic_options` (measurement_id, property_id, account_id, view_id — wszystkie `""`). WC analytics enabled (`woocommerce_analytics_enabled = yes`), ale to tylko backend dashboard, **nie trackuje frontu**. |
| Google Tag Manager | ❌ Brak. Zero `GTM-*` w HTML home (144 KB sprawdzone). |
| Google Search Console | ❌ Brak. Zero `<meta name="google-site-verification">`. agria.pl **nie jest na liście 18 GSC sites** w GSC Auranet (potwierdzone z `reference_google_apis.md`). |
| Cookie consent / Consent Mode v2 | ❌ Brak banner zgody w HTML. Z GDPR perspective — wymagane jak tylko wejdą trackery. |
| IndexNow (Rank Math) | ✓ aktywny, klucz `4113d4a6e5834d6f9c3f8a9ab5f677d4`, log pokazuje 100 ostatnich submisji (status 200 OK) |

### CVE cross-check pluginów

| Plugin | Wersja live | Status CVE | Action |
|---|---|---|---|
| WordPress core | 6.9.4 | ✓ aktualna | — |
| PHP | 8.3.30 | ✓ aktualna | — |
| WooCommerce | 10.6.1 | ✓ patched (>10.5.3 fix CSRF admin creation CVE 2026-03-03) | — |
| Elementor | 3.35.9 | ✓ patched (>3.35.6 fix XSS, >3.33.1 fix Missing Authorization, >3.33.4 fix DOM XSS) | — |
| Elementor Pro | 3.35.1 | ✓ aktualna | — |
| JetSmartFilters | 3.7.5 | ✓ patched (>3.6.4 fix XSS CVE-2025-30963) | — |
| **Premmerce Permalink Manager** | **2.3.11** | ❌ **Freemius DOM-XSS niefixed** (CVSS 7,1 high, opublikowany 2026-04-30, brak dostępnej wersji z fixem na 2026-05-19) | **Monitoring update lub plan B** — patrz P0 |
| Rank Math SEO | 1.0.264.1 | ✓ aktualna | — |
| Rank Math SEO PRO | 3.0.107 | ✓ aktualna | — |
| UpdraftPlus | 1.26.2 | ✓ aktualna | — |
| Orphans (Sierotki) | 3.4.1 | ⚠️ plugin polski PL, brak w bazach CVE; sprawdzić ręcznie kod jeśli zostaje | rec: zweryfikować potrzebę utrzymania |
| Agria by Auranet (theme) | 2.0.0 | ✓ własny, audyt kodu w trakcie | — |

---

## P0 — krytyczne (do naprawy w pierwszym miesiącu pracy)

### P0-1. Brak GA4/GTM/GSC — zero danych o ruchu

**Problem:** Strona live od marca 2026, **zero trackerów frontowych**. Nie mamy:
- pomiaru sesji, użytkowników, ścieżek,
- pomiaru zdarzeń konwersji (formularz, telefon, mail, kliknięcie produktu),
- danych o zapytaniach z Google (GSC),
- danych o pozycjach (GSC Search Analytics).

**Konsekwencja:** Pakiet 6-mies bez baselinea ruchu = nie pokażemy klientowi „przed/po". Plus każda decyzja typu „który produkt promować pierwsze" = wróżenie.

**Naprawa:**
1. **GTM container** — założyć w Tag Manager Auranet (nowe account dla AGRIA), wdrożyć przez plugin `Insert Headers and Footers` lub bezpośrednio w `header.php` motywu `agria-by-auranet`. Plus Consent Mode v2 (banner zgody przed inicjalizacją tagów).
2. **GA4 property** — nowe property w GA4 Admin Auranet (konto `js@auranet.com.pl`, 14 properties już ma 1 wolne slot). Stream `agria.pl`, eventy konwersji: `generate_lead` (form submit), `click_phone`, `click_email`, `view_product`, `product_quote_request`.
3. **GSC verification** — domena `sc-domain:agria.pl` (TXT na DNS u nazwa.pl). Złożyć sitemap_index.xml.
4. **Wpięcie GA4 → GTM → strona przez Consent Mode** — gating na zgodzie z bannera.
5. **Looker Studio dashboard** — szablon Auranet (mamy `auranet_GA4_template`), connect do GA4 + GSC, dashboard URL do klienta.

**Czas pracy:** ~6 h (GTM/GA4 setup + Consent banner + Looker template).
**Priorytet:** **TYDZIEŃ 1**.

---

### P0-2. Schema.org Organization „My Blog" — RankMath niezainicjalizowany

**Problem:** RankMath SEO PRO uruchomiony z defaultami. Wartości w `rank-math-options-titles`:

```
website_name = "My Blog"
knowledgegraph_name = "My Blog"
knowledgegraph_type = "company"
local_business_type = "Organization" (powinno być LocalBusiness lub Store)
```

Co dostarcza Google na home:

```json
{"@type":"Organization","name":"My Blog","logo":{"caption":"My Blog"...}}
{"@type":"WebSite","name":"My Blog"}
<meta property="og:site_name" content="My Blog" />
```

**Konsekwencja:** Google indeksuje markę pod nazwą „My Blog", buduje knowledge graph na bzdurze, brak rich snippetów branded, zero E-E-A-T. **Każdy rich result dla AGRIA = nazwa „My Blog"**. To bezpośrednio uderza w CTR i widoczność branded.

**Naprawa (15 minut roboty):**
- WP Admin → Rank Math → Titles & Meta → Local SEO → **Knowledge Graph** → wpisać:
  - Person/Company: **Company**
  - Name: **AGRIA Sp. z o.o.**
  - Logo: `/wp-content/uploads/2026/02/agria_logo-napis-svg.svg`
  - Local Business Type: **LocalBusiness** (lub `Store` jeśli chcemy podtyp; AGRIA = wapno B2B, więc `Organization → LocalBusiness` najbardziej pasuje)
  - Address: Tarnów ul. Warsztatowa 5 + dwa oddziały (Niedomice, Radgoszcz) jako osobne `LocalBusiness` (multi-location schema)
  - Phone: `+48 14 621 88 21` (centrala) — listę numerów per oddział mamy w `docs/catalog/CATALOG_VS_WC_GAP.md` §5
  - Opening hours: weryfikacja z klientem (RankMath ma teraz 7×24h `09:00–17:00` — soboty/niedziele do potwierdzenia)
- Tytuły:
  - **`website_name` = "AGRIA Sp. z o.o."** (zamiast „My Blog")
  - **`homepage_title`** — sprawdzić: aktualne `%sitename% %page% %sep% %sitedesc%` → renderuje 102 znaki, **przerasta limit SERP 60 znaków**. Zmienić na np. `%sitename% %sep% Wapno nawozowe i budowlane od 1989` (~55 znaków).
- `knowledgegraph_type = "company"` jest OK; ale `local_business_type = "Organization"` → zmienić na `LocalBusiness` żeby ujawnić adres/hours w SERP.

**Czas pracy:** 30 min + 1 h weryfikacji z klientem opening_hours / dwóch oddziałów.
**Priorytet:** **TYDZIEŃ 1, tuż po GA/GSC**.

---

### P0-3. URL `/kategoria-produktu/*` zwraca 404 zamiast 301

**Problem:** Plugin **Premmerce Permalink Manager** przepisuje URL-e kategorii WC na własne slugi (np. `Rolnictwo - wapno nawozowe` → `/wapno-nawozowe-rolnictwo/`). Ale **nie ustawia 301 ze starego URL WC** (`/kategoria-produktu/rolnictwo-wapno-nawozowe/`) na nowy.

```
404  https://agria.pl/kategoria-produktu/rolnictwo-wapno-nawozowe/
404  https://agria.pl/product-category/rolnictwo-wapno-nawozowe/
404  https://agria.pl/produkt/
200  https://agria.pl/wapno-nawozowe-rolnictwo/
200  https://agria.pl/wapno-nawozowe-hurt/
```

**Konsekwencja:**
- Każdy backlink zewnętrzny, który użyje domyślnego URL WC = utracony ruch.
- Lighthouse na URL `kategoria-produktu/...` daje SEO score **50 / 100** (audyty `is-crawlable`, `meta-description`, `http-status-code` = fail) — co potencjalnie obniża rankowanie domeny.
- W przyszłych integracjach (feed do Merchant Center / Allegro / hurtowni) ktoś użyje WC default URL → broken.

**Naprawa:** Dodać reguły 301 w `.htaccess`:

```apache
# /.htaccess (przed WP rules)
RewriteEngine On
RewriteRule ^kategoria-produktu/rolnictwo-wapno-nawozowe/?$ /wapno-nawozowe-rolnictwo/ [R=301,L]
RewriteRule ^kategoria-produktu/hurtownie/?$ /wapno-nawozowe-hurt/ [R=301,L]
RewriteRule ^kategoria-produktu/sadownictwo/?$ /wapno-do-sadu/ [R=301,L]
RewriteRule ^kategoria-produktu/rybactwo-wapno-do-stawow/?$ /wapno-do-stawow/ [R=301,L]
RewriteRule ^kategoria-produktu/oczyszczalnie/?$ /wapno-do-oczyszczalni/ [R=301,L]
RewriteRule ^kategoria-produktu/budownictwo/?$ /wapno-hydratyzowane/ [R=301,L]
RewriteRule ^kategoria-produktu/paszarstwo/?$ /kreda-pastewna/ [R=301,L]
RewriteRule ^kategoria-produktu/?$ /oferta/ [R=301,L]
RewriteRule ^product-category/(.*)$ /$1 [R=301,L]
RewriteRule ^produkt/?$ /oferta/ [R=301,L]
```

Plus: **lustrzane 301 dla starych URL-i produktów** jeśli były publikowane wcześniej z `/product/...`. Sprawdzić z klientem czy strona była indeksowana ze starym base.

**Czas pracy:** 1 h (edit `.htaccess` + test każdej reguły + weryfikacja GSC po 7 dni).
**Priorytet:** **TYDZIEŃ 1–2**.

---

### P0-4. Mobile Core Web Vitals FAIL na produktach (LCP 5,0–5,2 s, TBT 350–390 ms)

**Problem:** Wszystkie 3 audytowane produkty mają mobile LCP w przedziale **5,0–5,2 sekundy** (próg FAIL Google: >4,0 s). TBT (proxy dla INP) **350–390 ms** (próg FAIL >500 ms; needs improvement >200 ms — wszystkie tu spadają).

Home mobile **LCP 7,5 s** ❌ (najgorszy w batchu). Kategoria Rolnictwo mobile **LCP 5,6 s** ❌.

Desktop wszędzie **OK** (LCP 1,2–1,4 s) — problem dotyczy 80% potencjalnego ruchu (mobile-first indexing).

**Główne winowajcy (z Lighthouse opportunities, home mobile):**
- `unused-css-rules`: 300 ms — duża ilość niewykorzystywanego CSS (likely WooCommerce + Elementor full bundle)
- `unused-javascript`: 140 ms
- HTML size 144 KB nieskompresowany — sprawdzić gzip/brotli
- `na-ls-cache-enabled: off` na hostingu nazwa.pl → każdy request idzie do PHP
- `cdn=disabled` → zero edge caching obrazów

**Naprawa (priorytetowana):**
1. **Włączyć cache nazwa.pl** (LightSpeed Cache lub LiteSpeed plugin po stronie WP) — to powinno samo dać LCP boost ~1–2 s.
2. **Włączyć CDN nazwa.pl** dla statics (obrazy, CSS, JS).
3. **Optymalizacja CSS Elementor** — Elementor settings → Performance → enable: „Improved CSS Loading", „Improved Asset Loading", „Optimized Markup". Zmniejszy unused CSS ~60%.
4. **Preload LCP image** — RankMath ma opcję, ewentualnie ręczny `<link rel="preload" as="image">` w header.
5. **WebP/AVIF** — wszystkie produkcyjne obrazy są już WebP (z sitemap widać `.webp`), to dobrze. Sprawdzić wymiary źródłowe (`dolomit.webp 2048×2048` na produkcie — overkill).
6. **Lazy loading** — sprawdzić atrybut `loading="lazy"` na obrazach below-the-fold.

**Czas pracy:** 4 h (włączenie cache/CDN + Elementor performance settings + image audit + preload LCP).
**Priorytet:** **TYDZIEŃ 2–3**.

**Caveat:** mierzymy multirun (3–5 pomiarów, median) **przed** patchem oraz **+1d po** wdrożeniu (memory `feedback_psi_lab_variance`). Pojedynczy run nie pozwoli wnioskować o efekcie.

---

### P0-5. Premmerce 2.3.11 — Freemius DOM-XSS niefixed (CVSS 7,1)

**Problem:** WPScan / Patchstack listuje na pluginie `woo-permalink-manager` (Premmerce) podatność:
- **Freemius < 2.11.0 — Reflected DOM-Based XSS via url Parameter**
- CVSS 7,1 (high)
- Opublikowana 2026-04-30
- **Brak znanych poprawek na 2026-05-19** — Premmerce nie wydał nowej wersji.

Atakujący tworzy złośliwy URL, który injekcjonuje JS do odpowiedzi pluginu. Wystarczy, że administrator (manager sklepu) kliknie link — wykonuje się skrypt w jego sesji → przejęcie konta.

**Naprawa:**
1. **Krótkoterminowo (tydzień 1):** Web Application Firewall na hostingu nazwa.pl + reguła w `.htaccess` blokująca query-stringi typowo używane w Freemius callbacks:

```apache
RewriteCond %{QUERY_STRING} fs_action= [NC,OR]
RewriteCond %{QUERY_STRING} fs_blog_admin= [NC]
RewriteRule .* - [F,L]
```

2. **Średnioterminowo (do 30 dni):** Monitoring strony WPScan / Patchstack na release Premmerce 2.3.12+. Włączyć auto-update plugins via WP Admin lub WP-CLI cron.
3. **Długoterminowo (do 60 dni):** **Plan B — migracja na alternatywę:**
   - `Yoast SEO` (ma własny permalink rewrite) — ale konflikt z RankMath, którego klient chce zachować.
   - `Custom Post Type UI` + ręczne rewrite_rules — opcja czysta, ale wymaga developmentu.
   - **`Permalink Manager Lite/Pro`** (Bartosz Kropielnicki) — dostępny, aktywnie utrzymywany, kompatybilny z RankMath i WC.
4. **Już nie używać Premmerce** w nowych projektach Auranet — zaktualizować `~/.claude/CLAUDE.md` sekcja 5 z notatką.

**Czas pracy:** 1 h monitoring + 2 h plan B + ewentualne 4 h migracja jeśli klient chce.
**Priorytet:** **TYDZIEŃ 1 — reguły WAF/.htaccess**. Migracja: do końca miesiąca 2.

---

## P1 — ważne (do naprawy w 1–2 miesiącu)

### P1-1. Brak HSTS i security headers

Nagłówki HTTP odpowiedzi `https://agria.pl/`:
- ❌ `Strict-Transport-Security` (HSTS)
- ❌ `X-Frame-Options` (clickjacking)
- ❌ `X-Content-Type-Options: nosniff`
- ❌ `Referrer-Policy`
- ❌ `Permissions-Policy`
- ❌ `Content-Security-Policy`

**Naprawa:** w `.htaccess`:

```apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains" env=HTTPS
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
```

CSP wymaga osobnego audytu zasobów (Elementor + WC + RankMath = sporo inline scripts) — zaplanować na osobną sesję.

**Czas:** 30 min. **Priorytet:** TYDZIEŃ 2.

### P1-2. Title home za długi (102 znaki)

Aktualne:
> `AGRIA | Wapno nawozowe i budowlane od 1989r - AGRIA Sp. z o.o. – Wapno nawozowe i budowlane`

Duplikacja „AGRIA / AGRIA Sp. z o.o." + „Wapno nawozowe i budowlane" × 2 = ucięty w SERP po ~60 znaków → `AGRIA | Wapno nawozowe i budowlane od 1989r – AGRIA Sp.…`

**Propozycja:** `Wapno nawozowe i budowlane od 1989 r. | AGRIA Sp. z o.o.` (~56 znaków).

**Czas:** 5 min w RankMath. Razem z P0-2.

### P1-3. Zduplikowany canonical na kategoriach product_cat

Na `/wapno-nawozowe-rolnictwo/` dwa `<link rel="canonical" href="...">` w `<head>`. RankMath + Premmerce wstrzykują niezależnie. Google przyjmuje pierwszy, ale to anti-pattern.

**Naprawa:** w `premmerce-permalink-manager` options ustawić `canonical = off` (Rank Math obsługuje) **lub** w Rank Math wyłączyć canonical dla taksonomii (mniej dobre).

**Czas:** 15 min + test. **Priorytet:** TYDZIEŃ 2.

### P1-4. Brak product_cat w sitemap RankMath

`category-sitemap.xml` zawiera tylko `category/poradniki/` (post category), ale **żadnej z 7 kategorii product_cat** (Rolnictwo, Sadownictwo, Rybactwo, Oczyszczalnie, Budownictwo, Hurtownie, Paszarstwo). Każda ma 1–17 produktów i własny opis SEO.

**Naprawa:** Rank Math → Sitemap Settings → włączyć Product Categories.

**Czas:** 5 min. **Priorytet:** TYDZIEŃ 1.

### P1-5. Wszystkie 19 produktów ma `sku = null`

Z `wc_products_list`: każdy produkt bez SKU. Schema Product bez `sku` field → mniejszy rich snippet eligibility. Plus brak identyfikatorów dla ERP/feed/integracji.

**Naprawa:** zależy od decyzji klienta (patrz **§ Zależności od decyzji klienta** poniżej, pytanie #4 z raportu CATALOG_VS_WC_GAP). Konwencja `AGR-XXX` jest w `docs/catalog/PRINT_CATALOG_SPEC.md`, ale spec vs mapping rozjeżdżają się — najpierw klient decyduje, potem wpisujemy.

**Czas:** 2 h bulk update przez WP-CLI gdy decyzja jest. **Priorytet:** zależne — TYDZIEŃ 3–4.

### P1-6. Literówki w nazwach 8 produktów (brak polskich znaków)

- `weglanowe` zamiast `węglanowe` — produkty #314, 315, 316, 317, 318, 319
- `zawierajace` zamiast `zawierające` — produkty #317, 318, 319

Dotyczy nazwy produktu (renderowanej w `<title>`), nie sluga (slug bez diakrytyków jest OK SEO-wise).

**Naprawa:** bulk update via WC admin lub WP-CLI. Pełna lista w `docs/catalog/CATALOG_VS_WC_GAP.md` §9.

**Czas:** 30 min. **Priorytet:** TYDZIEŃ 2.

### P1-7. Eksponowanie loginu admina w schema/meta

- Schema `Person` `name="js"` na home
- `twitter:data1: js` (twitter author label)
- Gravatar URL z hashem maila admina

**Naprawa:** RankMath → Titles & Meta → Authors → włączyć **Disable Author Archives** + ustawić display name admina != login. Alternatywnie zmienić `display_name` w `wp_users` na „Redakcja AGRIA" / „Auranet" przez WP Admin → Users → js → edit.

**Czas:** 15 min. **Priorytet:** TYDZIEŃ 2.

### P1-8. HTML home 144 KB + ~17 duplikatów `elementor-element-3732dd1`

W HTML home widać kilkanaście razy ten sam Elementor element ID `3732dd1` z `data-id` powtarzającym się dosłownie. To może być świadoma replikacja widgetu (np. lista logotypów producentów), **ale wygenerowała ~30 KB redundantnego markupu**. Sprawdzić w Elementor → home page edit.

**Czas:** 1 h analiza + ewentualna refaktoryzacja widgetu. **Priorytet:** TYDZIEŃ 3.

### P1-9. Brak Consent Mode v2 banner

Wymóg GDPR (od 6.03.2024) + warunkować GA4/GTM ładowanie zgodą. Bez tego po wpięciu GA4 (P0-1) Google będzie modelował consent_default = denied, traci 30–60% danych behavioral.

**Naprawa:** plugin `CookieYes` / `Complianz` (free tier wystarcza), konfiguracja Consent Mode v2 z banner PL, integracja z GTM (gtag('consent', 'default', {...})).

**Czas:** 2 h. **Priorytet:** wraz z P0-1.

---

## P2 — średnie (do naprawy w 2–6 miesiącu, w ramach miesięcznych prac)

### P2-1. Plugin Sierotki (Orphans 3.4.1)

Plugin polski (typografia — łączy spójniki/przyimki niełamliwą spacją), brak w bazach CVE. Zweryfikować:
- Czy faktycznie używany (output wpływa na widoczny tekst)?
- Czy autor utrzymuje (data ostatniego update)?
- Czy alternatywa typograficzna (np. `Sierotki w polskim WordPressie` od Daniel Wieczorek) lepiej utrzymywana?

### P2-2. Brak GSC po stronie agria.pl

Nie tylko brak `meta google-site-verification` (P0-1), ale też brak agria.pl na liście 18 GSC sites Auranet. Po dodaniu domain property `sc-domain:agria.pl` (P0-1, DNS) zaktualizować `~/.claude/projects/-home-host476470-projekty/memory/reference_google_apis.md` — sekcja „Search Console — 18 sites".

### P2-3. Opening hours w RankMath

`local_business_type = Organization` z `opening_hours = Mon-Sun 09:00-17:00` (włącznie sob/niedz). **Centrala AGRIA Tarnów prawdopodobnie nie pracuje w weekendy** — weryfikacja z klientem (przy okazji P0-2).

### P2-4. WC katalog mode — wszystko ukryte CSS

W `<head>` motywu inline CSS ukrywa: `add_to_cart_button`, `wc-proceed-to-checkout`, `cart-widget`, `single_add_to_cart_button`, ceny (`.price`). To **świadoma decyzja klienta** (sklep w trybie katalogu B2B — zapytanie ofertowe zamiast zakupu). **OK koncepcyjnie**, ale:
- CSS „display: none !important" ładuje się dla wszystkich, nawet bot Google. Bot widzi pełną strukturę WC + ukryte ceny. Lighthouse zalicza to jako CSS unused.
- Schema Product **bez `offers`/`priceSpecification`** → traci rich snippet eligibility w Google Shopping (ale i tak nie aplikujemy Shopping = OK).
- Alternatywa: użyć WC Wholesale plugin lub usunąć kompletnie display funkcji „price/cart" na poziomie hooks, nie CSS.

**Czas:** 2 h refaktoring. **Priorytet:** miesiąc 3+.

### P2-5. RankMath IndexNow aktywny — dobrze

Klucz `4113d4a6e5834d6f9c3f8a9ab5f677d4`, log pokazuje 100 ostatnich submisji ze statusem 200 OK. Bing/Yandex/Naver dostają natychmiastową informację o zmianach. To zostawiamy jak jest.

### P2-6. Theme + child theme structure

Motyw `agria-by-auranet` (child) + parent `hello-elementor`. Wersja child 2.0.0. **Filesystem motywu nie sprawdzony** — MCP `list_dir` ograniczone do `wp-content/uploads/*` (nie `themes/*`). Audyt kodu motywu w osobnej sesji.

### P2-7. Page-sitemap analiza

7 stron głównych: home, kontakt, o-firmie, kalkulator-wapnowania (`!`), oferta, poradniki, do-pobrania.

**Kalkulator wapnowania** — to mocna decyzyjna strona (tool-based content), zasługuje na własną sekcję w P1 audytu on-page i SXO. Sprawdzić w obszarze 8 (UX).

### P2-8. Blog tempo: 1 post / mies

6 postów blog od 2025-04-23 do 2026-03-12. Najnowszy: marzec 2026, sprzed 2 miesięcy. Plan strategii (`STRATEGY_2025_2026.md`) zakłada 2 posty / mies × 6 mies. Status: **niedostateczne tempo**, do nadgonienia w miesiącach 2–6.

---

## Zależności od decyzji klienta z `CATALOG_VS_WC_GAP.md`

Następujące rekomendacje **nie wykonujemy autonomicznie** — czekamy na decyzję klienta z otwartych pytań w `docs/catalog/CATALOG_VS_WC_GAP.md` (i §„Otwarte pytania" w `docs/PROJECT_STATE.md`):

| Rekomendacja | Zależy od pytania klienta |
|---|---|
| Bulk update SKU 19 produktów (P1-5) | **Pyt #4 z mapy niespójności** — która numeracja AGR-XXX jest finalna (spec vs mapping rozjeżdżają się; cement = AGR-015 czy AGR-019)? |
| Czy poprawić nazwę „Kreda czarna jeziorna" / decyzja indexable | **Pyt #1 mapy** — decyzja Q1 2026 mówiła „wycinamy", ale produkt w WC publish + jest w ulotce DL 2026-05-18. Aktualizacja decyzji? Wpływa na: czy zostawiamy w indeksie (`noindex` lub `draft`) lub czy poprawiamy do końca. |
| Wariant frakcji Agrobielik 90 (2–8 mm) w schema | **Pyt z §2 mapy** — czy tworzymy `variable_product` (drugi wariant w #311) czy osobny produkt? Wpływa na: schema Product + URL + linkowanie wewnętrzne. |
| Cement / kruszywo / wapno drogowe w WC | **Pyt z §1 mapy** — czy dodać do WC i sitemap? Jest w spec + mapping + MASTER_PROMPT.md (zakres), ale brak w PDF i WC. Wpływa na: czy strategia ma 19 czy 22 produkty. |

**Praktyka:** Każdą z tych rekomendacji **flaguj w prezentacji oferty** jako „wykonamy po decyzji klienta z punktów X, Y, Z". Nie próbujemy podejmować decyzji za AGRIA — to ich domena (logistyka, marketingowa selekcja).

---

## Następne kroki

### Audyt — kolejne sesje
1. **Obszar 2 — on-page audit** (struktura, H1-H4, alt, breadcrumbs, slugi produktów). Szczególnie sluga długie `wapno-czarnajeziorna-z-kwasami-humusowymi-i-weglem-organicznym-big-bag-600kg` (70+ znaków).
2. **Obszar 3 — content audit** (strony segmentowe, blog 6 postów, kalkulator wapnowania jako asset).
3. **Obszar 4 — keyword research** (DataForSEO + Senuto export, frazy z `STRATEGY_2025_2026.md`).
4. **Obszar 5 — konkurencja** (TOP 5 dla „wapno nawozowe" + frazy long-tail).
5. **Obszar 6 — backlink profile** (DataForSEO Backlinks API).
6. **Obszar 8 — UX + konwersja** (formularze, CTA, Google Business Profile dla 2 oddziałów).

### Pakiet 2000 PLN / mies — uzasadnienie z tego audytu

| Miesiąc | Główne pozycje (z P0-P2) | Roboczogodziny |
|---|---|---|
| 1 | P0-1 (GA/GTM/GSC), P0-2 (schema RankMath), P0-3 (.htaccess 301), P0-5 (Premmerce WAF rule), P1-1 (security headers), P1-2 (title home), P1-4 (sitemap product_cat), P1-9 (Consent banner) | ~14 h |
| 2 | P0-4 (cache + CDN + Elementor perf), P1-3 (canonical dedup), P1-6 (literówki), P1-7 (admin login), P1-8 (Elementor dup widget) + content (2 posty blog) | ~12 h + 6 h content |
| 3 | P2-2 GSC sync, P2-3 hours, P2-4 katalog mode refactor + content (2 posty) + reporting miesięczny | ~10 h + 6 h content + 2 h raport |
| 4–6 | Migracja Premmerce (P0-5 plan B), keyword/content pipeline ramping do 4 posty/mies, link building, optymalizacja konwersji | ~14 h/mies content+SEO+raport |

**Razem ~80 h pracy w 6 mies przy stawce ~150 PLN/h** = uzasadnione 12 000 PLN za pakiet (= 2 000 × 6).

### Memory — co aktualizujemy

- `~/.claude/projects/-home-host476470-projekty/memory/reference_google_apis.md` — dodać agria.pl do GSC sites + GA4 property po wykonaniu P0-1.
- `~/.claude/projects/-home-host476470-projekty-agria/memory/` — utworzyć katalog (na 2026-05-19 nie istnieje) z pierwszymi wpisami:
  - `feedback_agria_no_emails_to_client.md` — egzekwowane już przez globalny `feedback_never_email_clients_directly`, ale per-projekt warto wzmocnić.
  - `reference_agria_premmerce_xss_monitoring.md` — monitoring wersji 2.3.12+ (P0-5).
  - `reference_agria_rankmath_init.md` — checklist „co ustawiliśmy" po P0-2.

### Decyzje wymagane od Janka przed kolejną sesją

1. **Konto GA4** — używamy istniejącego account Auranet (363024991 lub innego) czy zakładamy nowe? Polecam: nowe property w istniejącym koncie `auranet` (363024991).
2. **GSC domena** — `sc-domain:agria.pl` przez DNS TXT? Wymaga dostępu do panelu DNS nazwa.pl klienta — kto ma?
3. **`.htaccess` na produkcji** — kto ma dostęp FTP/SSH? Czy klient akceptuje, że robimy edit `.htaccess` z prod (preferowane staging → cutover, ale agria.pl nie ma staging-a)?
4. **Czas na klienta** — najszybszy slot na call z klientem AGRIA do potwierdzenia 4 pytań z `CATALOG_VS_WC_GAP.md` (cement/kruszywo, kreda czarna, warianty Agrobielik 90, SKU).

---

**Koniec raportu baseline (obszar 1 + 7).**

**Kolejne sesje:** obszary 2 (on-page), 3 (content), 4 (keywords), 5 (konkurencja), 6 (backlinks), 8 (UX) — po decyzjach klienta z `CATALOG_VS_WC_GAP.md` i pierwszym tygodniu prac wdrożeniowych z P0-1, 2, 3.
