# 2026-05-19 — SEO bez budżetu na linkbuilding zewnętrzny

> ADR (Architecture Decision Record). Decyzja strategiczna, biznesowo-handlowa, zapadła w rozmowie Janek ↔ Claude 2026-05-19 po dostarczeniu raportu audytu baseline.

---

## Status

Zaakceptowana 2026-05-19. Obowiązuje na cały pakiet 6-mies AGRIA (M1 czerwiec 2026 – M6 listopad 2026) i każdą jego potencjalną renegocjację.

## Kontekst

Klient AGRIA wchodzi w pakiet utrzymaniowo-rozwojowy Auranet (6 mies). W trakcie rozmowy 2026-05-19 ustalono, że **nie ma budżetu na płatny linkbuilding** (artykuły sponsorowane, kupowane linki, outreach z $/€). Standardowy audyt SEO zerowy (`docs/seo/SEO_AUDIT_PLAN.md`) zakładał obszar 6 (backlinks) jako jeden z 8 obszarów do rozbudowy w pełnym planie pracy.

Cytat Janka (2026-05-19): „linkbuilding zewnętrzny to trudno będzie zrobić bo nie mam na to budżetu, wszystko musimy wokół kontentu, performance, bazy wiedzy, narzędzi, analityki itd. przygotować również pod przyszłe reklamy".

## Decyzja

Strategia SEO dla AGRIA budowana **wyłącznie** wokół pięciu filarów:

1. **Content** — E-E-A-T, eksperckie poradniki, długi ogon, AEO/Google AI Overviews
2. **Performance** — Core Web Vitals (mobile LCP/INP/CLS), TTFB, cache, CDN
3. **Baza wiedzy** — FAQ, kalkulatory, normy, parametry, tabele, technicznie głębokie zasoby
4. **Narzędzia interaktywne** — `kalkulator-wapnowania` już istnieje, planowane rozszerzenie (np. kalkulator dawkowania pH stawu, kalkulator wapna do oczyszczalni)
5. **Analityka** — fundament pod każdą iterację (GA4 + GSC + Looker Studio dashboard)

Wszystkie te działania mają jednocześnie przygotować stronę pod **future kampanie PPC** (Quality Score Ads zależy od CWV + UX + relevance, więc SEO inwestycje są dual-use: organic + paid).

Z audytu zerowego **obszar 6 (backlinks) skrócony do diagnostyki** — analiza profilu linków + toxic link detection (DataForSEO Backlinks API), bez planu aktywnego pozyskania.

## Konsekwencje

- **Audyt obszar 6** — skrócony do „is there anything toxic to disavow?" raz, zamiast pełnego planu LB.
- **Audyt obszar 5 (konkurencja)** — focus na **content gap**, nie **link gap**.
- **Pakiet 6-mies — realokacja godzin** które normalnie szły na outreach/guest posty/broken link building → przekierowanie na:
  - więcej postów blog (4–6/mies zamiast 2 zakładanych w `docs/offers/AURANET_2000PLN_MONTHLY.md`)
  - rozbudowa kalkulatorów / narzędzi
  - rozbudowa FAQ per segment
  - rozbudowa stron segmentowych (landing pages per branża)
  - AEO optimization (passage-level citability, llms.txt, schema FAQ/HowTo)
- **„Naturalne" linki przez wartość** mogą się pojawić (kalkulator wapnowania, poradniki techniczne, tabele parametrów), ale **nie są celem mierzonym w KPI pakietu** — traktujemy jako bonus.
- **Komunikacja klientowi** — nigdy nie proponujemy „kupimy linki / artykuły sponsorowane". Linkbuilding w raportach pojawia się tylko jako „organic, value-driven".
- **PPC readiness w każdej decyzji on-page** — przy projektowaniu landing pages, formularzy, CTA, schema pytamy „czy to dobrze zadziała też w kampanii Google Ads?".

## Alternatywy odrzucone

- **Budżet LB ~500–1500 PLN/mies** — odrzucony przez klienta. Brak deklaracji kiedy mógłby zostać uruchomiony.
- **Rezygnacja z SEO i tylko PPC** — nieprzyjęta, bo SEO + PPC działa lepiej (SEO wspiera Quality Score, content wspiera ad copy).
- **Tylko PR digital (free outreach do branżowych portali)** — opcja teoretyczna, ale czasochłonna i bez gwarancji ROI; zostawiona jako „możliwa do rozważenia w M5–M6 jeśli zostanie pula godzin".

## Powiązane

- `docs/audits/SEO_AUDIT_RESULTS.md` — sekcja „Następne kroki" zgodna z tą decyzją
- Memory: `~/.claude/projects/-home-host476470-projekty-agria/memory/project_seo_strategy_constraints.md`
- Memory cross-project: `~/.claude/projects/-home-host476470-projekty/memory/reference_auranet_seo_pricing_model.md`
- `docs/strategy/STRATEGY_2025_2026.md` — sekcja „Ryzyka" aktualizowana o brak budżetu LB
