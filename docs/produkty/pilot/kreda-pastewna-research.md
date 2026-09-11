# Research — #307 Kreda pastewna (pilot T-136)

> 11.09.2026 · pełny stan karty: [`../kreda-pastewna.md`](../kreda-pastewna.md) (nie przepisuję) · dane nowe: `data/produkty/pilot/`
> GSC 2026-06-10 … 09-07 (`gsc-frazy-307.json`, `gsc-karty-90d.json`), 28 dni 08-11 … 09-07 (`gsc-karty-28d-2026-09-11.json`) ·
> SERP mobile 10–11.09 (`data/produkty/dfs/serp-kredy-dolomit-2026-09-10.json`, `serp-pilot-2026-09-11.json`) · elementy top 5: `serp-elementy-2026-09-11.json` ·
> Ads: `data/produkty/ads/search-terms-kreda.json` (13.08–09.09)

## 0. Warstwa renderu — ustalona 11.09

Karta **renderuje się z `post_content`**, nie z `_elementor_data`. Dowód (curl z cache-bustem 11.09): w renderze jest tekst
występujący **tylko w `post_content`** („transport różnej skali" — 1 trafienie, „Celiny(Hochel Group), Lhoist" — 1), a nie ma tekstu,
który jest **tylko w `_elementor_data`** (tabela SKU „KREPAST" — 0, „transport od 3 do 24" — 0, „Kopalnia Celiny, Lhoist" — 0).
`_elementor_data` (7 951 B, bez `_elementor_edit_mode`) to martwa kopia. **`CLAUDE.md` §4 pkt 2 — wpis „307 renderuje z `_elementor_data`" jest dla #307 nieaktualny.**

## 1. Frazy, które należą do tej karty

| fraza | wyszukań/mies. | nasze adresy w GSC (90 dni) | kolizja |
|---|---|---|---|
| **kreda pastewna** | **2 400** | stary `/kreda-pastewna/` 3 wyśw. poz. 21,7 · #307 3 / poz. 12 | 2 adresy; stary przekierowuje 301 na **kategorię `/paszarstwo/`, nie na kartę** |
| kreda paszowa | 90 | `/kreda-pastewna/` 2 / 25,5 · `/paszarstwo/` 1 / 15 | 2 adresy, karty brak |
| **kreda pastewna dla kur** · kreda dla kur · wapno dla kur niosek · …dla kur niosek | **1 600 · 720 · 210 · 110** | **0 wierszy** (jedynie `kreda paszowa dla kur` 2 wyśw.) | — |
| kreda pastewna dla bydła · kreda dla bydła | 210 · 70 | `/kreda-pastewna/` 8 / 32,8 · `/paszarstwo/` 7 / 29,9 · **#307 2 / poz. 2** | **3 adresy** |
| kreda pastewna dawkowanie · …dla bydła dawkowanie · …dla kur dawkowanie | 30 · 70 · 90 | #307 5 / 21,2 · `/kreda-pastewna/` 4–6 · `/paszarstwo/` 2–7 | 2–3 adresy |
| ile kredy pastewnej dla kur (na 100 kg) | 50 | **#307 5 wyśw. poz. 6,6** | brak |
| kreda pastewna cena · cena za tonę · ile kosztuje | 40 · 20 · 20 | 0 wierszy | — |
| kreda pastewna gruboziarnista · drobnoziarnista · co to jest kreda pastewna | 30 · 30 · 20 | 0 wierszy | — |

Wszystkie frazy paszowe należą do jednej karty — w serwisie **nie ma drugiego produktu paszowego** (`/paszarstwo/` listuje tylko #307).
Kolizja jest z własną kategorią i starym adresem: w 28 dniach `/paszarstwo/` zebrała na frazach o bydle 20 wyśw., karta 7.

## 2. Co Google nagradza

| fraza | top 5 organicznie (abs) | co mają |
|---|---|---|
| `kreda pastewna` | allegro (2) · jarpasz (7) · hotfarm (8) · tech-mot poradnik (9) · portalhodowcy (10) · holcim (14) | sklepy: cena, frakcja, dawka, gatunki; portalhodowcy: producent, dokumenty |
| `kreda pastewna dla kur` | allegro (1) · hotfarm (5) · rolnet (7) · hodowlany (8) · fermo (10) | **worki 5–25 kg, frakcja gruboziarnista w tytule**, cena, gatunek w tytule |
| `kreda dla kur` (11.09) | allegro (1) · hotfarm (4) · fermo (8) · rolnet (11) · vitalzam poradnik (12) | jw.; blok „popular products" ×2 |
| `kreda pastewna dla bydła` | **atl-agro „Animacal 1000 kg" (1)** — z nazwą kopalni (Czatkowice) · allegro (3) · polcalc poradnik z FAQPage (5) · agrofoto forum (7) · agsol (9) | producent/kopalnia, frakcja, big-bag, `FAQPage` |

Fakty: w top 5 **każda strona sprzedażowa ma gatunek w tytule** („dla kur", „dla niosek", „dla bydła"), frakcję i opakowanie.
**Dawki dla kur sklepy nie podają liczbowo** — hotfarm i fermo: „dawkowanie powinno być dostosowane do potrzeb hodowli". Liczby per gatunek
ma tylko poradnik polcalc (bydło 40–100 g/szt./dzień) — to cudzy tekst, nie źródło o towarze AGRII. Na bydło wygrywa **big-bag 1000 kg z nazwą kopalni** — to profil AGRII.

**PAA:** „Czy kreda pastewna to to samo co wapno?" · „Ile kredy pastewnej dla kur na 100 kg?" · „Jak stosować kredę pastewną dla kur?" · „Czy kury powinny jeść kredę?" ·
„Co daje kreda pastewna dla bydła?" · „Jaka dawka kredy pastewnej dla bydła?" · „Jak podawać kredę pastewną?" · „Jaki jest skład kredy pastewnej?" · „Co jest lepsze wapno czy kreda?"

## 3. Czego szuka kupujący

- **Zapytań ofertowych z karty: 0** (z 11). Ads 13.08–09.09 prowadziły na kartę: **149 klik., 175,07 zł, 1 konwersja** (`landing_page_view`).
- **Ads — wyszukiwane hasła:** `kreda pastewna dla kur` 551 wyśw. 36 klik. · `kreda pastewna` 504 / 22 · `kreda dla kur` 126 / 12 · `…dla kur niosek` 68 · `kreda dla kur niosek` 59 ·
  `…dla bydła` 35 · `gruboziarnista` / `drobnoziarnista` 12 / 10 · `labtar kreda pastewna` 9. Kampania „AGRIA - Paszarstwo", hasła widoczne:
  **drób 64 z 104 kliknięć (62%)**, bydło 5, reszta 35 — a na karcie nie pada słowo „kur" ani „niosek".
- **GSC karty, 28 dni:** 2 klik. / 203 wyśw. / poz. 8,6; widoczne: `ile kredy pastewnej dla kur na 100 kg` poz. 6,6 · `kreda pastewna` poz. 12 · `…dla bydła` poz. 2.
- Kupujący pyta o: **dawkę na 100 kg paszy**, frakcję (gruba/drobna), gatunek, cenę, opakowanie.

## 4. Co z tego wynika dla treści (tylko karta PDF i dokumenty producentów)

1. **Gatunki w zakresie karty PDF:** „budowa kośca, zębów i skorup jajowych, krytyczne dla **bydła mlecznego i niosek**" — oba gatunki wolno nazwać
   w H2, lead i FAQ. Dawka tylko ta z karty: **1–2 kg / 100 kg paszy**; per gatunek — brak źródła (quiz do Janka).
2. Z dokumentów producentów (fakty, `[J 11.09]`: producent i kopalnia tak): **Lhoist Bukowa** (frakcja 0–0,3 mm, worek 30 kg, nr wet. PL2613013p) i **Kopalnia Wapienia „Celiny"**
   (frakcje 0,1–0,4 / 0,4–0,8 / 1–3 mm, nr wet. PL26043170p, GMP+). Obaj producenci nazywają produkt **materiałem paszowym**.
3. Frakcje z karty PDF z przypisaniem do źródła (z dokumentów) — bez przypisania do gatunku.
4. Cena: 190 zł/t luz; worek 30 kg jako możliwość zakupu, bez kwoty `[J 11.09]`.
5. Usunąć: „atest do każdej partii" (meta), „pH powyżej 12" (FAQ), „35-letnie doświadczenie", „zwiększa przyswajanie składników".
6. Poza treścią karty (zauważone, nie ruszam): 301 `/kreda-pastewna/` → `/paszarstwo/` zamiast na kartę; T-135 zdjęcie worka jako główne.
