# 2026-05-19 — Fix indeksacji agria.pl: diagnoza i plan accelerator

> ADR. Wątek 4 audytu — diagnoza 9-miesięcznego okresu „0 zaindeksowanych" w GSC + plan dociągnięcia indexacji przez Indexing API.

---

## Status

Diagnoza zamknięta 2026-05-19 wieczorem. Plan executor: jutro od 02:00 PL (po reset quota Indexing API).

## Kontekst

GSC alarmuje od dawna: `wp-sitemap.xml` (default WP) submitted **2025-08-07** — **38 stron submitted, 0 zaindeksowanych**. Drugi sitemap `sitemap_index.xml` (RankMath) dodany **2026-05-18** w Wątku 3 (jeszcze nie zdążył wyemitować statusu).

Pierwotne podejrzenia (8 hipotez):

1. `blog_public = 0` w wp_options (Discourage search engines)
2. Meta robots `noindex` w motywie lub RankMath
3. `robots.txt Disallow: /` lub overrestrictive
4. `X-Robots-Tag: noindex` w HTTP headers
5. RankMath `registration_skip` nieustawione → moduły INACTIVE
6. Page-type matrix (noindex per typ)
7. Plugin Maintenance / Coming Soon aktywny
8. Content quality — „Discovered – currently not indexed"

## Diagnoza

### Konfiguracja techniczna obecnie — bez zarzutu

| Test | Wynik | Hipoteza |
|---|---|---|
| `wpfz_options.blog_public` | `"1"` | #1 — obecnie obalona, ale **historycznie była przyczyną** (patrz niżej) |
| RankMath modules (`rank_math_modules`) | 13 aktywnych (sitemap, woocommerce, instant-indexing, local-seo, …) | #5 obalona |
| `rank_math_registration_skip` | `"1"` ✓ | #5 obalona |
| RankMath robots flags per typ | `pt_post/page/product/tax_category = [index]`, `pt_attachment/tax_post_tag/author/date/search = [noindex]` (best practice) | #2 + #6 obalone |
| Aktywne pluginy | Agria by Auranet, Elementor + Pro, JetSmartFilters, Orphans, Premmerce, RankMath + Pro, UpdraftPlus, WC. **Brak Maintenance/Coming Soon** | #7 obalona |
| `https://agria.pl/robots.txt` | Disallow tylko wc-logs / transient / uploads / wp-admin / add-to-cart query. **Zero blokad content URL.** Sitemap directive aktualny. | #3 obalona |
| HEAD response na home + kategoria + produkt + post category (UA Googlebot) | **HTTP 200**, **zero `X-Robots-Tag`** w żadnym | #4 obalona |
| RankMath `sitemap_index.xml` (live) | Renderuje 4 sub-sitemap: post (6) + page (11) + product (20) + category (1) = **38 unique URL** | Sitemap działa |

**Wszystkie 7 hipotez konfiguracyjnych obalonych.** Strona dziś jest **technicznie poprawnie skonfigurowana do indeksacji**.

### Krytyczna korekta ramy: historia vs stan obecny

Pierwotna interpretacja audytu („9 miesięcy zero indexed = trwały problem") **była błędna**. Korekta klienta-strony (Janek, wieczór 2026-05-19):

> „w ustaiweniach wp bylo pros o nieindeksowanie i to wylaczylem, jakies tresci sa zaindeksowana"

Czyli **hipoteza #1 BYŁA prawdziwa przez większą część okresu**. Rekonstrukcja timeline'u:

- **2025-08-07 → ~2026-05-?? (~9 miesięcy)** — WP uruchomiony z `blog_public = 0` (default „Discourage search engines"). Sitemap złożona do GSC w sierpniu 2025 zawierała 38 URL strony **w budowie** (placeholder content + posty „Hello world"). Google miał wyraźny sygnał „nie indeksuj" w meta robots każdej strony (`<meta name='robots' content='noindex, follow'>` wstrzykiwane przez WP gdy `blog_public=0`). Stąd „38 submitted, 0 indexed".
- **Niedawno (data dokładna nieznana)** — Janek odkrył flagę, wyłączył. Google zaczął odblokowywać.
- **Aktualnie indexacja idzie** — Janek pokazuje GSC „Ostatnie zindeksowanie":

| URL | Typ | Last crawled |
|---|---|---|
| `/` | home | 15 maja 2026 |
| `/wykwity-na-murze/` | blog post | 13 maja 2026 |
| `/kontakt/` | page | 11 maja 2026 |
| `/wapno-nawozowe-hurt/kreda-malarska-worek-30kg/` | product | 10 maja 2026 |
| `/kreda-pastewna/kreda-pastewna-worek-30kg/` | product | 4 maja 2026 |

Mix typów (page + product + post) potwierdza brak per-typ noindex obecnie. Hipoteza #2 obalona także na poziomie konkretnych URL (gdyby były noindex w HTML, te 5 URL by nie weszło do indeksu).

### Wniosek diagnostyczny

**Nie ma technicznej blokady indeksacji od strony agria.pl.** Problem historyczny (`blog_public=0`) został zamknięty przez Janka. Stan obecny: **faza odbudowy zaufania Google** + dociągania przez nowy sitemap RankMath. Tempo naturalne dla młodej domeny B2B w niskoautorytetowej branży: tygodnie do miesięcy na pełną indexację 38 URL.

## Decyzja

**Accelerator: ping Indexing API** dla wszystkich strategicznych URL z sitemap, gdy quota się odnowi. Skraca czas indexacji z **tygodni do dni**.

**NIE dziś — quota Indexing API wyczerpana.**

Z `~/projekty/primaauto/tmp/single-indexing-push-2026-05-19.json` (09:40 dziś rano, primaauto):
- Attempted: 188 / OK: 187 / Error: 1 (HTTP 429)
- `quota_hit: true`
- GCP project `325733204269` (Auranet) — **współdzielona przez wszystkie projekty Auranet** używające tego samego desktop OAuth client
- Reset: **2026-05-20 ~02:00 PL** (północ UTC)

Plus istotny gate komunikacyjny: memory `feedback_ask_before_quota_burn` (świeże 2026-05-19, z incydentu primaauto rano) wprost mówi „pytaj o strategię ZANIM ruszysz batch". Dlatego nawet gdyby quota była — batch agria wymaga akceptacji listy URL od Janka.

## Plan execution (Wątek 5, 2026-05-20 od 02:00 PL)

### Krok 1: weryfikacja quota i przygotowanie listy

- Sprawdź `urlNotifications:publish` quota — 1 test ping na home (oczekiwane HTTP 200).
- Skoordynuj z primaauto: jutro przewidywane ~1 quota test `wp asiaauto indexing-test --live` + ewentualnie retry queue (1-5 URL z dzisiejszego 429) + per-publish hook (1 per nowy listing). Razem ~5-10 quota dla primaauto.
- **Dla agria: pozostaje ~190 quota** → bezpiecznie do batchu ~35 URL.

### Krok 2: lista URL z deduplikacją

Z sitemap `https://agria.pl/sitemap_index.xml` (stan 2026-05-19):

**Post-sitemap (6):**
- `/tynki-rodzaje-kategorie/`
- `/jak-murowac-klinkier/`
- `/cement-czym-jest-jak-powstaje-i-jakie-sa-jego-klasy/`
- `/wykwity-na-murze/` ← już zindeksowane (skip lub URL_UPDATED)
- `/wapnowanie-gleby/`
- `/czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/`

**Page-sitemap (11, minus utility):**
- `/` (home) ← już zindeksowane
- `/kontakt/` ← już zindeksowane
- `/o-firmie/`
- `/kalkulator-wapnowania/`
- `/oferta/` ← duplikat z product-sitemap
- `/poradniki/`
- `/do-pobrania/`
- `/zamowienia/` (utility WC — **SKIP**)
- `/wsparcie/`
- `/cart/` (utility WC — **SKIP**)
- `/rodo/`

**Product-sitemap (20):**
- `/oferta/` (duplikat — **SKIP**)
- 19 produktów (z bazy WC — wszystkie publish, audyt obszar 1 potwierdził)
- Duplikaty `-2/` slugi: `/wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz/` ORAZ `/wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz-2/` — **flag do decyzji** (oba pchnąć, sprawdzić w URL Inspection co jest canonical)

**Category-sitemap (1):**
- `/category/poradniki/` (post category)

**Razem do batchu po deduplikacji: ~33 URL** (38 - 2 duplikaty `/oferta/`+`-2/` - 2 utility `/cart/`+`/zamowienia/` - ew. już-zindeksowane jeśli decyzja pomijamy = bezpieczne ~33-35).

### Krok 3: skrypt `scripts/google/indexing_api_batch.py`

Wzorzec z `scripts/google/_lib.py` (helper `api()` + auto-refresh OAuth). Endpoint: `POST https://indexing.googleapis.com/v3/urlNotifications:publish` body: `{"url": "...", "type": "URL_UPDATED"}`. Dry-run default, `--live` flag dla execution. State w `/tmp/agria-indexing-state.json` (idempotent — można odpalić ponownie i pomija OK).

### Krok 4: monitoring (3-7 dni)

- GSC „Pages → Indexed" — obserwujemy przyrost. Oczekiwane: >50% z 33 zaindeksowanych w 72h.
- GSC „Sitemaps" — czy `sitemap_index.xml` przejmuje obrazek (stary `wp-sitemap.xml` zostaje w archive).
- URL Inspection ad-hoc dla URL które nie wskoczą — verdict + reason.

### Krok 5: cleanup starego sitemap

`wp-sitemap.xml` (default WP) — Janek-side: GSC UI → Sitemaps → Remove (lub zostawić, Google sam zignoruje). To stary sitemap z okresu blokady, mylące dla raportów.

## Powiązane finding w SEO_AUDIT_RESULTS

Update obszar 1 (technical) — dopisany nowy P0-6 (Indexation historia + plan recovery). Patrz `docs/audits/SEO_AUDIT_RESULTS.md`.

## Konsekwencje

**Pozytywne:**
- Diagnoza zamknięta szybko (1 sesja Wątku 4, ~2h roboty). Mit „9 miesięcy zero index" zdebunkowany.
- Plan accelerator gotowy do execute jutro w ~15 min.
- Skrypt batch będzie wzorcem reuse dla innych projektów Auranet wchodzących w SEO (PMP, Plakaty, etc.).
- **Wartość M1 wzrasta** — w prezentacji oferty mogę powiedzieć „w tygodniu 1 pchamy 33 URL przez Indexing API + sitemap migration. Tempo indexacji: 3-7 dni dla większości URL". Klient widzi konkretne accelerator-y, nie tylko „zrobimy SEO".

**Ryzyka / otwarte:**
- Quota Indexing API współdzielona z primaauto cron retry — przy pełnym dniu retry primaauto może zjeść quota agria. Mitigation: agria batch o 03:00-04:00 PL (przed primaauto cron startem), albo skoordynować w sesji jutrzejszej.
- Indexing API nie jest oficjalnie wspierany dla WC product / blog page (Google formalnie wspiera tylko JobPosting + BroadcastEvent live), ale w praktyce działa dla wszystkich URL — Google scrappa i decyduje. Nie ma ryzyka penalty, ale efekt może być mniej silny niż dla JobPosting.
- Stary `wp-sitemap.xml` w GSC może dalej raportować „0 indexed" jeszcze tygodnie — to artefakt, nie problem. Jeśli klient zobaczy ten widok, trzeba wyjaśnić („to stary sitemap z okresu w budowie").

## Memory utworzone w tym wątku

- Brak memory per-projekt agria — pierwsza wartość per-projekt powstanie w Wątku 5 jutro (np. `reference_indexing_api_quota_shared.md`) po realnym wykorzystaniu.
- **Cross-project memory `feedback_check_indexation_baseline_pre_m1.md`** — propozycja do dodania: „Przed M1 SEO sprawdź historię `blog_public` (kiedy zmieniony, czy w ogóle) i status indexacji w GSC. To częsta cicha blokada na świeżych WP". Wzorzec do reuse PMP/Plakaty/Auranet/innych.

## Powiązane dokumenty

- `docs/audits/SEO_AUDIT_RESULTS.md` — obszar 1 (po update)
- `docs/decyzje/2026-05-19-analityka-skonfigurowana.md` — ADR Wątku 3 (sitemap_index.xml submit)
- `~/projekty/primaauto/tmp/single-indexing-push-2026-05-19.json` — źródło danych quota
- `~/.claude/projects/-home-host476470-projekty-primaauto/memory/feedback_ask_before_quota_burn.md` — feedback rule

---

_ADR utworzony 2026-05-19 w Wątku 4 (autonomous diagnostic). Realizacja accelerator-a: Wątek 5, 2026-05-20 od 02:00 PL._
