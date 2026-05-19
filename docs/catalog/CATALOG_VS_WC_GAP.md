# Katalog drukowany ↔ WooCommerce ↔ Spec — mapa niespójności

> Wygenerowane 2026-05-19 podczas restrukturyzacji repo. Audit krzyżowy:
> - **PDF**: `assets/print/catalog/Agria-katalog-2026-05-04-web.pdf` (realizowany, 24 strony)
> - **WC**: live z `mcp__claude_ai_Agria_pl__wc_products_list` (19 produktów, stan 2026-05-19)
> - **Spec**: `docs/catalog/PRINT_CATALOG_SPEC.md` (planowane 18 kart)
> - **Mapping**: `docs/catalog/PRODUCT_DATA_MAPPING.md` (planowane 22 produkty z innym numerowaniem AGR-XXX)
> - **TXT historyczny**: `assets/print/catalog/HISTORICAL_BRIEF_2026-02-05.txt` (wycofany, stara paleta)
> - **Ulotka DL**: `assets/print/ulotka-dl/ulotka-dl-2026-05-18-*.jpg`

---

## 1. Niespójność: liczba i lista produktów w katalogu

| Źródło | Liczba kart | Numerowanie | Cement | Kruszywo drogowe | Wapno drogowe | Dolomit | Kreda malarska | Kreda czarna |
|--------|------------|-------------|--------|------------------|---------------|---------|----------------|--------------|
| **PDF realizowany** | 17 | brak ID | ❌ brak | ❌ brak | ❌ brak | ✅ jest | ❌ brak | ❌ brak |
| **PRINT_CATALOG_SPEC.md** | 18 | AGR-001…017 + AGR-002F | ✅ AGR-015 | ✅ AGR-016 | ✅ AGR-017 | ❌ brak | ❌ brak | ❌ wycięta |
| **PRODUCT_DATA_MAPPING.md** | 22 | AGR-001…021 (inne!) | ✅ AGR-019 | ✅ AGR-020 | ✅ AGR-021 | ✅ AGR-012 | ✅ AGR-016 | ❌ wycięta |
| **WooCommerce (live)** | 19 produktów | brak SKU | ❌ brak | ❌ brak | ❌ brak | ✅ #302 | ✅ #304 | ✅ #303 (publish) |
| **Ulotka DL 2026-05-18** | przegląd | brak ID | ❌ brak | ❌ brak | ❌ brak | ✅ jest | ❌ brak | ✅ 44% CaO |

**Co z tego wynika:**

- Numerowanie `AGR-XXX` istnieje TYLKO w `PRINT_CATALOG_SPEC.md` i `PRODUCT_DATA_MAPPING.md` — w PDF i w WC go nie ma. Te dwa pliki dodatkowo **mają różną numerację** (np. cement = AGR-015 w spec vs AGR-019 w mapping). **Niewyjaśniony rozjazd.**
- **Cement, kruszywo drogowe, wapno palone drogowe** są w obu planach (spec + mapping), ale **nie weszły do PDF** i **nie ma ich w WC**. Decyzja klienta? Brak danych? Do potwierdzenia.
- **Dolomit** (WC #302) jest w PDF jako karta i w ulotce, ale **nie ma go w PRINT_CATALOG_SPEC.md** (tam pominięty). PRODUCT_DATA_MAPPING.md ma go jako AGR-012.
- **Kreda malarska** (WC #304) — tylko w WC i w PRODUCT_DATA_MAPPING (AGR-016). Brak w PDF i ulotce.
- **Kreda czarna jeziorna** (WC #303, publish): decyzja Q1 2026 mówiła „wycinamy z katalogu" — ale **nadal jest w WC** (publikowana) **i pojawia się w ulotce DL** (44% CaO, sekcja „Kreda i Dolomit"). Niewykonana decyzja w ulotce albo zmiana decyzji.
- **Agrobielik 90 frakcja 2-8mm** — w PDF jest osobną kartą („Agrobielik 90 2 - 8 mm"), w WC jest TYLKO jeden Agrobielik 90 (#311) bez wariantów. Decyzja: utworzyć wariant produktu w WC czy osobny SKU?
- **Oxyfertil 90** (WC #312, Lhoist) — jest w PDF osobną kartą, ale brak w PRINT_CATALOG_SPEC.md i PRODUCT_DATA_MAPPING.md (mapping ma go jako AGR-003 ale to kolizja z mieszanką tlenkowo-węglanową).

---

## 2. Mapowanie PDF (rzeczywistość) → WC (live)

Faktyczna kolejność kart w realizowanym katalogu PDF:

| # | Karta PDF | Producent źródłowy | WC ID | WC nazwa |
|---|-----------|--------------------|-------|----------|
| 1 | Agrobielik 70 | Nordkalk (Sitkówka) | 310 | Wapno nawozowe tlenkowe Agrobielik 70 |
| 2 | Agrobielik 90 0-3mm | Nordkalk (Sitkówka) | 311 | Wapno nawozowe tlenkowe Agrobielik 90 |
| 3 | Agrobielik 90 2-8mm | Nordkalk (Sitkówka) | ⚠️ brak | — (wariant #311?) |
| 4 | Oxyfertil 90 | Lhoist | 312 | Wapno nawozowe tlenkowe Oxyfertil 90 |
| 5 | Wapno tlenkowe z magnezem | Lhoist (Częstochowa) | 313 | Wapno nawozowe tlenkowe zawierające magnez |
| 6 | Mieszanka tlenkowo-węglanowa | Nordkalk (Sitkówka) | 308 | Mieszanka tlenkowo-węglanowa |
| 7 | Wapno węglanowe Granulowane | Grankal/Lhoist/Celiny | 314 | Wapno nawozowe weglanowe bez magnezu granulowane |
| 8 | Wapno węglanowe Odmiana 04 | Lhoist/Celiny | 315 | Wapno nawozowe weglanowe bez magnezu — Odmiana 04 |
| 9 | Wapno węglanowe z magnezem - granulowane | Grankal | 317 | Wapno nawozowe weglanowe zawierajace magnez granulowane |
| 10 | Wapno węglanowe z magnezem - odmiana 04 | Industria/Jażwica | 318 | Wapno nawozowe weglanowe zawierajace magnez — Odmiana 04 |
| 11 | Wapno węglanowe z magnezem - odmiana 05 | Industria/Laskowa/Winna | 319 | Wapno nawozowe weglanowe zawierajace magnez — Odmiana 05 |
| 12 | Kreda nawozowa granulowana | KZK Kornica | 305 | Kreda nawozowa granulowana |
| 13 | Kreda nawozowa sypka Odmiana 06a | Drugnia | 306 | Kreda nawozowa sypka |
| 14 | Kreda pastewna | Celiny/Lhoist | 307 | Kreda pastewna |
| 15 | Dolomit | Siarkopol | 302 | Dolomit |
| 16 | Wapno hydratyzowane Bielik | Nordkalk (Sitkówka) | 309 | Wapno hydratyzowane Bielik |
| 17 | Wapno palone mielone wysokoreaktywne | Nordkalk (Sitkówka) | 320 | Wapno palone mielone wysokoreaktywne |

**W WC pozostają (nie ma karty w PDF):**
- #303 Kreda czarna jeziorna (decyzja „wycięta", ale w ulotce DL jest)
- #304 Kreda malarska (status: nigdy nie planowana do katalogu)
- #316 Wapno węglanowe bez magnezu Odmiana 05 — brak osobnej karty w PDF, choć Odmiana 04 ma (#315 → karta 8)

**Brakuje w WC (a są w PDF):**
- Wariant frakcji 2-8mm dla Agrobielik 90 (karta 3) — w WC tylko #311 zwykły

---

## 3. Niespójność brand — palety i fonty

| Źródło | Główny zielony | Akcent | Font nagłówków | Font tekstu | Data |
|--------|----------------|--------|----------------|-------------|------|
| **TXT historyczny** | `#1B4D3E` | `#9ACD32` limonkowy | Montserrat Bold | Montserrat Regular | 2026-02-05 |
| **IDENTITY.md / DESIGN_SPEC.md** | `#354E33` | `#61CE70` | Plus Jakarta Sans | Bai Jamjuree | 2026-03 |
| **Logo PNG (faktyczny)** | wyglądający na `#1B7339` (zieleń jaśniejsza niż #354E33) | — | — | — | — |
| **PDF realizowany** | zielony zbieżny z logo + ciemniejszy akcent | — | sans-serif podobny do Plus Jakarta Sans | — | 2026-05-04 |
| **Ulotka DL** | zielony zbieżny z logo + biały + jasnozielony akcent CTA | — | grotesque (Plus Jakarta?) | — | 2026-05-18 |

**IDENTITY.md eksplicitnie mówi:** „Stara paleta (z dokumentu „24 stron") `#1B4D3E`, `#9ACD32` — wycofana, używamy palety Elementor Global Colors".

**Otwarte:** logo `#1B7339` ≠ `#354E33` ≠ `#1B4D3E`. Trzy różne zielenie nazywane „głównym". Co jest source of truth?

---

## 4. Niespójność „35 lat" vs „37 lat"

- `PROJECT_STATE.md`, `STRATEGY_2025_2026.md`, `MASTER_PROMPT.md`, **PDF katalogu**, sekcja okładki: **35 lat**.
- **Ulotka DL 2026-05-18**: **37 lat na rynku, trzy pokolenia**.
- Matematyka: 2026 − 1989 = 37. **Ulotka ma poprawnie**, docs są reliktem 2024. Do aktualizacji docs.

---

## 5. Niespójność: numery telefonów

| Numer | Źródło | Funkcja |
|-------|--------|---------|
| `+48 14 621 88 21` | PDF (stopka każdej karty produktu) | centrala biurowa Tarnów |
| `+48 604 428 782` | PDF strona 24 + ulotka DL „ZADZWOŃ" + WORKING_AGREEMENT | zarząd/sprzedaż (głośna komórka) |
| `+48 660 768 691` | PDF strona 24 + README.md + ulotka DL | drugi numer kontaktowy |
| `+48 664 393 062` | PDF strona 24 — Niedomice | Paweł Bigos (oddział) |
| `+48 781 875 411` | PDF strona 24 — Radgoszcz | Kazimierz Nowak (oddział) |

**Trzeba ujednolicić w docs (PROJECT_STATE/README) listę kontaktową.**

---

## 6. Producenci — MASTER_PROMPT vs PDF

`MASTER_PROMPT.md` wymienia: **Nordkalk (Sitkówka)**, **Trzuskawica**.

PDF realizowany ma:
- **Nordkalk** (Sitkówka) — 6 kart
- **Lhoist** (Tarnów Opolski, Góraźdźce, Częstochowa) — 4 karty
- **Industria** (Jażwica, Laskowa, Winna) — 2 karty
- **Grankal** — 2 karty (granulaty)
- **Celiny / Hochel Group** — 3 karty
- **Kopalnia Drugnia** — 1 karta (kreda sypka)
- **KZK Kornica** — 1 karta (kreda granulowana)
- **Siarkopol** — 1 karta (dolomit)
- **Trzuskawica** — **0 kart w PDF** ❗

MASTER_PROMPT do zaktualizowania (sekcja „Dodatkowe zasady" → linia o producentach).

---

## 7. Magazyny — terminologia

`MASTER_PROMPT` mówi: „magazyny AGRIA: Niedomice + Radgoszcz".

PDF rozróżnia dwa konteksty:
- **Magazyny operacyjne AGRIA**: Niedomice (33-132) ul. Fabryczna 17, Radgoszcz (33-207) ul. Witosa 12 — z nich AGRIA fakturuje i wysyła własną flotą.
- **Magazyny producenta**: dziesiątki lokalizacji (Sitkówka, Tarnów Opolski, Góraźdźce, Częstochowa, Celiny, Bukowa, Górażdże, Draby, Chęciny, Kostomłoty Drugie, Łagów, Pierzchnica, Kornica, Tarnobrzeg) — z nich AGRIA organizuje dostawy bezpośrednie do klienta.

JSX `agrobielik-70.jsx` w polu "Magazyn" trzyma `"Niedomice (33-132), Sitkówka (26-052)"` — mieszanka obu, **OK** w kontekście karty produktu (klient widzi „skąd ten konkretny produkt"), ale do uściślenia w dokumencie strategii i kart kolejnych produktów.

---

## 8. SKU — wszystkie 19 produktów WC

**Wszystkie produkty WC mają `sku = null`.** Konwencja katalogu drukowanego (AGR-XXX) nie jest zaimplementowana w WC.

**Issue P1** dla SEO audit. Bez SKU:
- Brak unikalnych identyfikatorów dla integracji ERP/CRM,
- Schema.org `Product.sku` puste,
- Eksport CSV / B2B feedy bez identyfikatorów,
- W przypadku wariantów (np. Agrobielik 90 frakcja) brak sposobu rozróżnienia.

---

## 9. Literówki / brak polskich znaków w nazwach WC

- `weglanowe` zamiast `węglanowe` — 5 produktów (#314, 315, 316, 317, 318, 319)
- `zawierajace` zamiast `zawierające` — 3 produkty (#317, 318, 319)

Wpływ na SEO: title tag bez polskich znaków → niższe rankowanie na frazy z poprawną pisownią. Do naprawy w on-page audit.

---

## 10. Co dalej

Ten dokument jest **żywą mapą niespójności**. Aktualizuj go w czasie audytu SEO + w procesie domykania katalogu (decyzje klienta o cement/kruszywo/drogowe, wariantach Agrobielika 90, Kredzie czarnej itd.).

Decyzje do podjęcia z klientem AGRIA — szczegółowo w `docs/PROJECT_STATE.md` sekcja „Otwarte pytania".
