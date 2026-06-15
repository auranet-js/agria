# ADR 2026-06-15 — Analityka agria.pl: GTM przez Elementor Custom Code (wzorzec ASEO)

> Status: **Zaakceptowane i wdrożone**. Decyzja: Jan Schenk. Realizacja: sesja 2026-06-15.

## Kontekst

W ramach M1 trzeba było uruchomić analitykę na agria.pl. Pre-M1 zbudowano już (przez API): GA4 property `538301430` (`G-KVFMR3NZDH`), kontener GTM `GTM-TDC85TQN` (Consent Mode v2 + 6 tagów, version 3 published), GSC. Brakowało **wpięcia kontenera na stronę** — bez tego GA4 nie zbierał (0 danych).

Rozważano trzy ścieżki:
1. **GTM4WP + Complianz Pro** (wzorzec Victorini) — pełny enhanced ecommerce dataLayer + Consent Mode v2.
2. **Ręczny mu-plugin** z GTM snippet.
3. **Elementor Pro Custom Code** (wzorzec aseosystem) — 2 snippety head/body.

## Decyzja

**Wybrano ścieżkę ASEO: GTM przez Elementor Pro → Custom Code.** Powód (Janek): agria to **katalog B2B „zapytaj o ofertę", bez transakcji online, GMC ani kampanii produktowych** — enhanced ecommerce (GTM4WP) i rozbudowany Complianz to przerost. ASEO ma analitykę „wystarczającą" tą samą metodą i działa.

### Wdrożenie (zweryfikowane)

- Snippet **„Gtm-head"** (ID 2711): location `elementor_head`, priority 1, Entire Site — loader gtm.js dla `GTM-TDC85TQN`.
- Snippet **„gtm-body"** (ID 2712): location `elementor_body_start`, priority 1, Entire Site — noscript iframe.
- Weryfikacja: HTML live (loader przed `</head>` l.178–180, noscript po `<body>` l.209); `gtm.js` = 389 KB version 3 z `G-KVFMR3NZDH` + Consent + tagami; GA4 property przyjmuje dane (testowy hit widoczny w Realtime API).

### Korekta identyfikatora GSC

Token Auranet ma dostęp `siteOwner` do **`https://agria.pl/`** (URL-prefix), **NIE** `sc-domain:agria.pl` (ten property nie istnieje — zwraca 403). Wcześniejsze ADR-y/plan RankMath błędnie odwoływały się do sc-domain. **Używać `https://agria.pl/`** (m.in. przy podłączaniu RankMath Analytics).

## Konsekwencje

- GA4 zbiera od momentu wpięcia (na razie tryb Consent Mode „denied" = pingi cookieless, do czasu banera zgody).
- **Otwarte (kolejny wątek):** CookieYes baner (jak ASEO) + RankMath Analytics OAuth (GSC `https://agria.pl/` + GA4 `538301430`) — wymaga WP Admin (MCP Agria read-only).
- **Caveat testowy:** lokalny Chrome ma bloker analityki maskujący GTM (`google_tag_manager` undefined, `window.ga` stub, gtm.js surrogate 200, brak błędów) — testować przez GA4 Realtime API / czyste urządzenie, nie przez konsolę.

## Powiązane

- Memory: `project-agria-analytics-stack`, `project-agria-indexation-diagnosis`
- `docs/audits/INDEXATION_DIAGNOSIS_2026-06-15.md` — diagnoza indeksacji (osobne znalezisko z tej samej sesji)
- Wzorzec źródłowy: aseosystem (Elementor Custom Code, container `GTM-NZBNWXDD`)
