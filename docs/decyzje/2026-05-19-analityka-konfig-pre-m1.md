# 2026-05-19 — Konfiguracja analityki przed formalnym startem M1 (jako proof-of-value)

> ADR. Decyzja operacyjno-sprzedażowa, zapadła w rozmowie Janek ↔ Claude 2026-05-19 wieczorem (po Wątku 2.5 keyword research).

---

## Status

Zaakceptowana 2026-05-19. Janek założył puste konta GA4 + GTM, GSC istniał. Konfiguracja idzie w kolejnym wątku.

## Kontekst

Pierwotny plan z `2026-05-19-pakiet-rozbicie-m1-m2do6.md` zakładał, że wdrożenie analityki (GA4 + GTM + GSC + Consent Mode v2 + Looker Studio) wejdzie jako billable deliverable w T1-T2 miesiąca M1, **po** akceptacji oferty przez zarząd AGRIA.

W praktyce sprzedażowej Auranet (analogicznie jak z keyword research z Wątku 2.5 — `docs/audits/KEYWORD_RESEARCH_2026-05-19.md`) okazuje się efektywniejsze pokazać **konkretne artefakty** zanim zarząd zatwierdzi budżet. Sygnał handlowy: „to nie obietnica, to działa".

Wcześniejsza reguła z memory `feedback_analytics_billable_deliverable.md` mówi: „Janek może dodać Claude'owi dostępy do GA4/GSC/GTM klienta przed formalnym M1. W dokumentach klient-facing analityka pozostaje 'do wdrożenia w M1' (billable). Po odbiorze M1 zasada gaśnie." Ta decyzja jest jej **realizacją** — nie nadpisuje, doprecyzowuje.

## Decyzja

**Pre-M1 (teraz, koszt po stronie Auranet):**
- Konfiguracja GA4 property `agria.pl` przez **Admin API + Data API** (auth: OAuth `js@auranet.com.pl`, scope `analytics.edit` + `analytics.manage.users`)
- Konfiguracja GTM container przez **Tag Manager API v2** (auth: ten sam OAuth, scope `tagmanager.edit.containers` + `tagmanager.publish`)
- GSC: walidacja `sc-domain:agria.pl`, sitemap submit, linkowanie z GA4 — przez **Search Console API**
- Wszystko skonfigurowane w stanie „gotowe do uruchomienia" — pełna implementacja Consent Mode v2, base events (page_view, scroll, outbound_link, file_download), enhanced ecommerce hooks pod WC, Looker Studio template z 4 podstronami (overview / acquisition / behavior / segmenty AGRIA)
- **Tag GA4 + GTM nie odpalony jeszcze na produkcji** — kontener pozostaje opublikowany jako wersja `Draft` lub aktywny ale bez wstrzykniętego skryptu w `<head>` agria.pl. Wstrzykiwanie skryptu = T1 M1 (po podpisaniu oferty), to jest „dotykanie produkcji"

**Fallback chrome MCP:**
Tam gdzie API nie pokrywa (Consent Mode v2 banner config w pluginie WP, Looker Studio sharing settings, pewne rzeczy w GTM UI typu workspace permissions) — automatyzacja przez chrome MCP zalogowanego na `js@auranet.com.pl`. Preferencja: **API first, chrome MCP fallback**, nigdy odwrotnie.

**W dokumentach klient-facing:**
Analityka **nadal** prezentowana jako billable deliverable M1 T1-T2 (zgodnie z `MONTH_1_FOUNDATIONS_PLAN.md` i `feedback_analytics_billable_deliverable.md`). Pre-konfiguracja jest atutem prezentacji („mamy gotowe, klient widzi przykład"), nie obniżką ceny.

## Konsekwencje

**Pozytywne:**
- Prezentacja zarządowi AGRIA wzmocniona o **żywy dashboard Looker Studio** (mock z testowymi danymi lub pustymi metrykami strony produkcyjnej) — daje 10× większy efekt niż slajd z opisem.
- Skrócony cycle T1-T2 M1 — zamiast konfiguracji od zera, zostaje wstrzyknięcie skryptu + weryfikacja eventów + szkolenie klienta.
- Nauka konfiguracji GA4/GTM przez API w kontekście Auranet — wzorzec do reuse na innych projektach (Victorini, PrimaAuto, PMPFibertech już mają GA, ale config przez API by się przydał).

**Ryzyka:**
- Czas Auranet (~3-5 h) na pre-konfigurację bez gwarancji akceptu zarządu AGRIA. Mitigation: ROI z keyword research (Wątek 2.5) sygnalizuje że zarząd to docenia.
- Pomyłka w konfiguracji widoczna klientowi przed odbiorem. Mitigation: pre-config robiony w piaskownicy (Auranet account → później transfer ownership po akceptacji M1), klient nie dostaje dostępu zanim wszystko nie jest sprawdzone.
- Drift między pre-M1 config i finalną wersją M1. Mitigation: pre-config jest binarnym „gotowe / nie odpalone na agria.pl" — po podpisaniu M1 robimy code review konfiguracji + wstrzykiwanie skryptu + dokumentacja procedur dla klienta.

## Następstwa operacyjne

1. **Nowy wątek** `claude` w `~/projekty/agria/` z dedykowanym promptem skupiającym się tylko na konfiguracji analityki — żeby kontekst Wątku 2 (oferta, keyword research) nie rozcieńczał konfiguracji.
2. **Memory `reference_google_apis.md`** w `~/projekty/` zawiera już szczegóły OAuth + scopes — Claude w nowym wątku ma do tego dostęp przez cross-project memory.
3. Po skonfigurowaniu — update `docs/audits/SEO_AUDIT_RESULTS.md` sekcja analityka + nowy ADR `2026-05-XX-analityka-skonfigurowana.md` z linkami do konkretnych property/container ID + diagramem flow.
4. Pre-M1 deliverable artefakt → Looker Studio dashboard URL → drop klient-facing na auratest jako załącznik do prezentacji oferty M1+M2-M6.

## Powiązane dokumenty

- `docs/decyzje/2026-05-19-pakiet-rozbicie-m1-m2do6.md` — bazowa decyzja o M1 fundamentach
- `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — deliverable T1-T2 wdrożenia analityki (klient-facing wording bez zmian)
- `~/.claude/projects/-home-host476470-projekty-agria/memory/feedback_analytics_billable_deliverable.md` — reguła w mocy
- `~/.claude/projects/-home-host476470-projekty/memory/reference_google_apis.md` — OAuth + scopes Auranet

---

_ADR utworzony 2026-05-19, autor decyzji: Jan Schenk (Auranet). Realizacja: nowy wątek `claude` w `~/projekty/agria/`._
