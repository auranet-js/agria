# Baseline metryk M1 — AGRIA (punkt zerowy)

> Deliverable M1 #6. Data: 2026-06-15. Punkt odniesienia do porównania po M2–M6. Źródła: GSC API (`https://agria.pl/`), PageSpeed (audyt 19.05), GA4 (start zbierania 15.06).

## 1. Search Console — 28 dni (18.05–14.06.2026)

**Agregat:** 46 kliknięć · 1 389 wyświetleń · CTR 3,3% · **średnia pozycja 13,9**

**Profil zapytań — brand dominuje, frazy komercyjne słabo:**
| Typ | Przykłady | Pozycja | Wniosek |
|---|---|---|---|
| Brand (klikalne) | agria niedomice (1,7), agria (5,8), agria tarnów (1,2) | TOP 1–6 | jedyne realne kliknięcia |
| Komercyjne non-brand (0 klików) | producent nawozów tarnów (18,2), wapna rolnicze (34,6), granulaty wapienne (43,6), wapno bielik (27,8), tabela wapnowania (30,8) | poz 18–48 | **wyświetlenia są, ale poza TOP10 → 0 klików** |

**Diagnoza baseline:** strona widoczna brandowo, ale **frazy sprzedażowe siedzą na 3.–9. stronie**. To jest punkt zerowy — cel M2–M6: wepchnąć frazy komercyjne (rolnictwo/drogownictwo) do TOP10.

## 2. Core Web Vitals (baseline z audytu 2026-05-19, mobile)

> PageSpeed API przez OAuth zwrócił pusto (potrzebny klucz API) — wartości z audytu zerowego; do re-pull z kluczem w T4.

- Mobile LCP produktów: **5,0–5,2 s** (FAIL, cel < 2,5 s)
- TBT: 350–390 ms · home HTML 144 KB + ~17 duplikatów widgetu Elementor
- Naprawa: P0-4 w M3 (cache + CDN + Elementor perf)

## 3. Indeksacja (baseline 2026-06-15)

- Sitemap: 38 web submitted · **13 zaindeksowanych** (home, kalkulator + indexed produkty/strony)
- 24 poza indeksem (zaległy re-crawl) → **23 URL zgłoszone do Indexing API 15.06**
- Cel: pełna indeksacja sitemapy w M2

## 4. Ruch GA4

- GTM live od **2026-06-15** → GA4 `538301430` zaczyna zbierać.
- Baseline ruchu (użytkownicy, źródła, zachowanie) = snapshot po ~2 tygodniach (koniec czerwca), bo przed 15.06 brak danych.

## 5. Tabela do porównania M+6 (grudzień 2026)

| Metryka | Baseline (06.2026) | Cel M6 |
|---|---|---|
| Śr. pozycja GSC | 13,9 | < 10 |
| Kliknięcia/mies | ~46 | wzrost ×3–5 |
| Frazy komercyjne w TOP10 | ~0 | 10–15 |
| URL zaindeksowane | 13/38 | 38/38 |
| Mobile LCP | 5,0–5,2 s | < 2,5 s |
| Ruch GA4 organiczny | start 15.06 | trend wzrostowy |
