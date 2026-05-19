# 2026-05-19 — Pakiet 6-miesięczny rozbity na M1 (fundamenty) + M2-M6 (rozwój)

> ADR. Decyzja biznesowo-handlowa, zapadła w rozmowie Janek ↔ Claude 2026-05-19 po dostarczeniu raportu audytu baseline.

---

## Status

Zaakceptowana 2026-05-19. Wstępnie zaakceptowana budżetowo przez klienta AGRIA (zarząd) — kwota M1 do uzgodnienia w pisemnej ofercie.

## Kontekst

Pierwotna oferta `docs/offers/AURANET_2000PLN_MONTHLY.md` zakładała jednorodny pakiet **6 × 2000 PLN/mies = 12 000 PLN total** za 6 miesięcy. W trakcie rozmowy 2026-05-19 Janek poinformował, że **klient AGRIA wstępnie zaakceptował większy budżet w miesiącu 1** — pod warunkiem konkretnego deliverable „fundamenty SEO + strategia + analityka + plan".

To wzorzec sprzedażowy Auranet stosowany wcześniej w innych projektach SEO. Cytat Janka 2026-05-19: „pierwszy miesiąc to powinno być właśnie ułożenie całego planu i strategii, powinno to zapłacić, wykonanie tej wszystkiej analityki, bo to samo robiliśmy kiedyś w SEO. Więc zbudowanie porządnych fundamentów, określenie co będziemy robić".

Kluczowy argument: bez fundamentów nie da się sprzedać miesięcy rozwojowych, bo klient nie wie co kupuje.

## Decyzja

Pakiet 6-mies dla AGRIA rozbity na **dwa etapy** z odrębną wyceną:

### Miesiąc 1 — Fundamenty (oddzielnie wyceniany, większy budżet)

Deliverables:

1. **Strategia + plan** na 6 mies — kierunek prac, segmenty priorytetowe, KPI, harmonogram T1–T4 × M1–M6
2. **Wdrożenie analityki** — GA4 property, GTM container, GSC verification (`sc-domain:agria.pl`), Consent Mode v2 banner, Looker Studio dashboard
3. **Keyword research** — DataForSEO Labs, 50–100 fraz priorytetowych w 5 klastrach segmentowych (rolnictwo, sadownictwo, rybactwo, oczyszczalnie, budownictwo/drogownictwo/hurtownie/paszarstwo)
4. **Content audit + topic clusters** — mapa aktualnych 6 postów + 19 produktów + 7 stron + 7 kategorii vs gaps, plan content kalendarza na M2–M6
5. **Plan on-page poprawek** — szczegółowe instrukcje z audytu baseline (P0/P1 z `docs/audits/SEO_AUDIT_RESULTS.md`) rozbite na zadania per miesiąc
6. **Baseline metryk** — punkt zerowy: pozycje fraz priorytetowych, CWV multirun median, struktura ruchu w pierwszych 2 tygodniach GA4

Realna pracochłonność M1: **~20–25 h**. Kwota M1 do uzgodnienia w pisemnej ofercie (większa niż 2000 PLN, mniejsza niż 5000 PLN — orientacyjnie).

### Miesiące 2–6 — Rozwój (~2000 PLN/mies × 5 = 10 000 PLN)

Według planu z `docs/offers/AURANET_2000PLN_MONTHLY.md` (po rewrite), kontynuacja zgodna z planem ustalonym w M1. Stała pula 12–15 h/mies.

## Konsekwencje

- **`docs/offers/AURANET_2000PLN_MONTHLY.md` — rewrite na dwa segmenty** (M1 fundamenty + M2-M6 rozwój). Robota nowego wątku.
- **Utworzenie `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md`** — szczegółowy plan M1 z roboczogodzinami per deliverable, harmonogramem T1–T4, milestones, akceptami. Robota nowego wątku.
- **Sprzedaż M2-M6 uzależniona od dostarczenia M1.** Argument w prezentacji: „bez fundamentów M2-M6 to spekulacja, nie strategia".
- **Audyt baseline (`docs/audits/SEO_AUDIT_RESULTS.md`) pozostaje wewnętrznym know-how Auranet** (etap zerowy „na koszt Auranet"). Klient dostaje **executive summary + 5–7 najważniejszych findings** zaszyte w ofercie M1.

## Operacyjne — kiedy Janek doda Claude'owi dostępy do GA4/GSC/GTM klienta

Janek może (i prawdopodobnie wkrótce) doda Claude'owi dostępy do narzędzi klienta — żeby operacyjnie mieć pełen kontekst do pisania planów, content kalendarza, baseline'a.

**Reguła:** Claude technicznie widzi GA4/GSC/GTM jako aktywne i może czytać dane przez API, ale w **dokumentach klient-facing** (oferty, raporty miesięczne, dropy na auratest oznaczone do klienta) analityka pozostaje **„do wdrożenia w M1"** — billable deliverable. Po dostarczeniu i odbiorze M1 zasada gaśnie (od M2 raporty mogą legalnie cytować dane GA4/GSC jako „aktualne metryki").

Cytat Janka 2026-05-19: „jeżeli ja ci dodam dostępy do GSC, GA4 i tak dalej, to my je dopiero sprzedajemy w pierwszym miesiącu, więc o tym po prostu nie pisz na razie, ustalmy że masz analitykę skończną".

Szczegóły operacyjne: memory `~/.claude/projects/-home-host476470-projekty-agria/memory/feedback_analytics_billable_deliverable.md`.

## Alternatywy odrzucone

- **Jednolity pakiet 6 × 2000 PLN bez M1** — odrzucony, bo pierwszy miesiąc miałby wtedy nieproporcjonalnie dużo pracy (~25–30 h vs 12–15 h), klient byłby niezadowolony w T2–T3 M1 widząc tylko cząstkę deliverables.
- **Audyt + plan jako osobna umowa przed pakietem** — odrzucony, bo wymaga osobnego procesu sprzedaży i ryzyka „klient nie kupi etapu 2".
- **Bezpłatne M1 jako wabik** — odrzucony, bo poświęca ~20–25 h pracy bez kompensaty + ustawia oczekiwania klienta na „darmowe fundamenty".

## Powiązane

- Memory: `~/.claude/projects/-home-host476470-projekty-agria/memory/project_first_month_foundations_offer.md`
- Memory: `~/.claude/projects/-home-host476470-projekty-agria/memory/feedback_analytics_billable_deliverable.md`
- Memory cross-project: `~/.claude/projects/-home-host476470-projekty/memory/reference_auranet_seo_pricing_model.md`
- `docs/offers/AURANET_2000PLN_MONTHLY.md` — do rewrite w nowym wątku
- `docs/seo/SEO_AUDIT_PLAN.md` — §„Deliverables audytu" — wzorzec executive summary do klienta
- `docs/audits/SEO_AUDIT_RESULTS.md` — pełen audyt baseline (wewnętrzny know-how)
