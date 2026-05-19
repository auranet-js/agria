# 2026-05-19 — Analityka AGRIA skonfigurowana (Wątek 3 wykonany)

> ADR. Realizacja decyzji z `2026-05-19-analityka-konfig-pre-m1.md` — Wątek 3 dedykowany konfiguracji pre-M1.

---

## Status

Zaakceptowana 2026-05-19 (po wieczornym wątku konfiguracyjnym).

## Wykonane

### OAuth (Auranet token globalny dla wszystkich projektów)

Re-OAuth z dodanym scopem `tagmanager.edit.containerversions` → token w `~/secrets/google/tokens.json` ma teraz **13 scopes** (12 dotychczasowych + 1 nowy). Pełna automatyzacja `workspace:create_version` + `versions/{v}:publish` dla GTM przez API — działa cross-project (Victorini, PMP, Primaauto, Plakaty też zyskują).

### GA4 (property 538301430, account 395276957, stream G-KVFMR3NZDH)

Stan po konfiguracji (skrypt `scripts/google/ga4_setup.py`, idempotentny):

| Ustawienie | Wartość |
|---|---|
| Time zone | Europe/Warsaw (Janek ustawił przy tworzeniu property) |
| Currency | PLN (jw.) |
| Industry category | BUSINESS_AND_INDUSTRIAL_MARKETS (jw.) |
| Data retention | **14 months + reset on new activity** |
| Google Signals | **DISABLED** (default dla nowych property, zgodnie z ADR pre-M1) |
| Custom dimensions | **5 stworzonych** (event-scoped × 4 + user-scoped × 1) |
| Key events | **4 dodane** (form_submit, phone_click, file_download, generate_lead) |
| Domyślne enhanced measurement | enabled przez Janka przy tworzeniu (purchase, qualify_lead, close_convert_lead już istniały) |

**Custom dimensions (segmenty AGRIA z KEYWORD_RESEARCH_2026-05-19):**
1. `cluster` (EVENT) — rolnictwo/budownictwo/drogownictwo/rybactwo/oczyszczalnie/paszarstwo/marka
2. `intent_type` (EVENT) — informational/transactional/commercial
3. `content_type` (EVENT) — produkt_wc/landing/blog/faq/kontakt/karta_techniczna
4. `season_phase` (EVENT) — wiosna_rolnictwo/jesien_rolnictwo/lato_drogownictwo/przed_zima_rybactwo/caly_rok
5. `user_segment` (USER) — rolnik/instytucja_przetargowa/budownictwo_b2b/drogownictwo/rybactwo/handel_b2c

Wszystkie pięć wymagają **wysyłki z dataLayer** w GTM eventach — to robota T1 M1 razem z wstrzykiwaniem skryptu.

### GTM (container GTM-TDC85TQN / 252883347, workspace 3)

Stan po konfiguracji (skrypt `scripts/google/gtm_setup.py` + `gtm_publish.py`):

| Element | Liczba | Detale |
|---|---:|---|
| Built-in variables enabled | 19 | bazowe 5 + click (×6) + form (×6) + scroll (×2) |
| User-defined variables | 1 | `GA4 Measurement ID` (Constant) = G-KVFMR3NZDH |
| Triggers (custom) | 4 | Scroll 25/50/75/90, Outbound Link, File Download, Form Submit |
| Tags | 6 | Consent Default Denied (HTML), Google Tag (googtag), 4× GA4 Events |
| Version | **v1 published** | ID 3 |

**Tag flow (Consent Mode v2):**

```
1. Page load → Consent Init system trigger
   ↓
   "Consent Default Denied" tag (Custom HTML)
   - default consent: ad_storage=denied, analytics_storage=denied,
     ad_user_data=denied, ad_personalization=denied
   - region: EEA + PL, wait_for_update=500ms
   - ads_data_redaction=true, url_passthrough=true
   ↓
2. Complianz Pro banner pojawia się → user klika "Zaakceptuj"
   - Complianz wysyła event consent update do dataLayer
   - GTM Consent Mode v2 odbiera signal, ad_storage/analytics_storage → granted
   ↓
3. Wszystkie tagi GA4 z "Require additional consent" mogą się odpalić:
   - "GA4 - Google Tag" (page_view automatic)
   - "GA4 Event - Scroll" (scroll_depth event)
   - "GA4 Event - Outbound Link" (outbound_link event)
   - "GA4 Event - File Download" (file_download event)
   - "GA4 Event - Form Submit" (form_submit event)
```

**UWAGA:** Skrypt GTM **NIE jest** wstrzyknięty w `<head>` agria.pl. Container opublikowany czeka. Wstrzykiwanie = **T1 M1** (po podpisaniu oferty), bo to „dotykanie produkcji" w rozumieniu Auranet (globalny CLAUDE.md sekcja 13).

### GSC (https://agria.pl/, siteOwner)

- **Sitemap RankMath dodany:** `https://agria.pl/sitemap_index.xml`
- **Stary `wp-sitemap.xml`** (default WP) — istnieje od 2025-08-07, **38 stron submitted, 0 zaindeksowanych**. To czerwona flaga — wpisana w SEO_AUDIT_RESULTS obszar 1 (technical).
- **GA4 ↔ GSC link:** nie istnieje w Google API publicznym (tylko UI). Zostaje dla Janka — 1 klik w GA4 admin → Product Links → Search Console.

## Co zostaje do zrobienia (Janek-side)

1. **Aktywacja Complianz Pro na agria.pl** — Janek napisał że zainstalował, w `wp_options` agria.pl brak. Możliwa pomyłka projektu lub wgranie ZIP bez instalacji. Po sprawdzeniu → Plugins → Aktywuj → Wizard (kraj PL, region EU, marketing+statistics ON, **Test mode** na start).
2. **GA4 ↔ GSC link** — GA4 admin → Property → Product Links → Search Console links → Link → wybrać `https://agria.pl/` → confirm.
3. **Looker Studio dashboard** — chrome MCP fallback w osobnej sesji (template z auranet property 498630415, podpięcie data source 538301430, 4 widoki: overview / acquisition / behavior B2B / segmenty AGRIA). Drop URL na auratest jako załącznik do prezentacji oferty.
4. **Wstrzykiwanie skryptu GTM-TDC85TQN w `<head>` agria.pl** — wraz z Complianz Pro w **T1 M1** (po podpisaniu oferty), nie pre-M1.
5. **`timezone_string` w WP options** — pusty (Janek przy tworzeniu GA4 ustawił Europe/Warsaw, ale WordPress nadal jest na UTC `gmt_offset=0`). WP admin → Settings → General → Timezone → Warsaw. Drobne, ale daty postów blog są w UTC.
6. **`date_format` w WP options** — obecnie `F j, Y` (US "May 19, 2026"). Zmienić na `j F Y` lub `Y-m-d`.

## Skrypty zaimplementowane

W `~/projekty/agria/scripts/google/`:

| Plik | Funkcja |
|---|---|
| `_lib.py` | Współna auth + api() helper (auto-refresh) |
| `ga4_setup.py` | GA4 base config (retention, custom dims, key events) — idempotent |
| `gtm_setup.py` | GTM workspace config (built-in vars, triggers, tags) — idempotent |
| `gtm_publish.py` | Create version + publish |
| `gsc_setup.py` | Sitemap submit + URL inspection |

Skrypty można odpalić ponownie bez psucia stanu (sprawdzają co istnieje). Wzorzec do reuse na innych projektach (PMP M1, Plakaty itd.).

## Konsekwencje

**Pozytywne:**
- Pre-M1 deliverable kompletny: GA4 + GTM + GSC skonfigurowane, gotowe do uruchomienia.
- Dashboard Looker Studio wystawimy przez chrome MCP w osobnej sesji.
- Skrypty Pythonowe jako trwały artefakt — reuse cross-project (Victorini, PMP, Plakaty).
- Scope `tagmanager.edit.containerversions` na globalnym tokenie = pełna automatyzacja GTM publish dla wszystkich projektów Auranet.

**Ryzyka / otwarte:**
- Klient widzi puste konta GA4/GTM (z perspektywy danych) dopóki skrypt GTM nie w `<head>`. Mitigation: prezentacja oferty z mockup Looker Studio + opisem „gotowe do uruchomienia po podpisaniu w T1 M1".
- Custom dimensions w GA4 wymagają wysyłki z dataLayer (GTM eventy nie wysyłają jeszcze cluster/intent_type/itd. — to mapping content_pages → cluster trzeba zrobić w T2 M1 jak landing pages dostaną dataLayer.push).
- Complianz Pro instalacja na agria.pl niejasna (brak w wp_options) — Janek-side weryfikacja.

## Powiązane dokumenty

- `docs/decyzje/2026-05-19-analityka-konfig-pre-m1.md` — pierwotna decyzja (intent)
- `docs/audits/SEO_AUDIT_RESULTS.md` — obszar 7 (analityka) + obszar 1 (sitemap 0 indexed)
- `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` — źródło custom dimensions (klastrów segmentowych)
- `~/.claude/projects/-home-host476470-projekty/memory/reference_google_apis.md` — token globalny + IDs AGRIA
- `~/.claude/projects/-home-host476470-projekty/memory/reference_complianz_consent_mode.md` — standard Auranet, workflow GTM Consent Mode v2

---

_ADR utworzony 2026-05-19, Wątek 3 wykonany w autonomous mode (Janek w screen). Realizacja w `~/projekty/agria/scripts/google/` + GA4/GTM/GSC API live._
