# Symulacja rdzenia URL/taksonomii — 19 produktów AGRIA

> Data: 2026-07-08. Status: **PROPOZYCJA — do akceptu Janka** (przed jakimkolwiek zapisem).
> Źródło prawdy struktury: **katalog drukowany** `assets/print/catalog/Agria-katalog-2026-05-04-web.pdf` (badge'y segmentów = priorytet, kolejność stron = menu_order).
> Powiązane: ADR `docs/decyzje/2026-07-08-rdzen-url-taksonomia.md`.

## Model A (przyjęty kierunek)

- **`product_cat` = jedna kategoria wiodąca per produkt** (segment = pierwszy badge katalogu). Premmerce nie ma z czego źle wybierać → URL natywnie poprawny, **zero custom kodu**, bez Yoasta.
- **Filtr „Zastosowanie"** (JSF 1471) przełączony z `product_cat` → **`pa_agria-segment`** (już trzyma pełne, wielosegmentowe przypisania). Filtr działa dalej wielosegmentowo.
- **Hurtownie** znikają jako `product_cat` (zostają wartością w `pa_agria-segment`) → nigdy nie kształtują URL.
- **menu_order** wg kolejności katalogu.
- **Slugi produktów** czyszczone ze śmiecia opakowaniowego; kategoria w ścieżce niesie frazę segmentową, więc slug = dystynktywna część (marka/typ/wariant).
- Każda zmiana URL = **301** stary→nowy.

## Kategorie po zmianie (`product_cat` = segment wiodący)

| Segment | Slug kategorii | Produkty (primary) |
|---|---|---|
| Rolnictwo | `wapno-nawozowe-rolnictwo` | 15 |
| Paszarstwo | `paszarstwo` *(zmiana z `kreda-pastewna` — patrz nota P1)* | 1 (307) |
| Oczyszczalnie | `wapno-do-oczyszczalni` | 1 (320) |
| Wapno hydratyzowane | `wapno-hydratyzowane` *(nazwa węższa niż „Budownictwo" — nota P2)* | 1 (309) |
| Kreda malarska | `kreda-malarska` *(nowa mini-kat, poza segmentami — nota P3)* | 1 (304) |
| ~~Hurtownie~~ | — | usunięte z product_cat → atrybut |
| ~~Sadownictwo~~ | — | brak produktu z primary=Sadownictwo → zostaje tylko w filtrze (pa_agria-segment) |
| ~~Rybactwo~~ | — | j.w. (LP rybactwo osobno wg planu KR) |

## Pełna symulacja — 19 produktów

Kolumny: **MO** = menu_order (katalog). **Segmenty** = pełna lista (→ `pa_agria-segment`, filtr). **Primary** = segment wiodący (→ `product_cat`, URL). **Stary URL** → **Nowy URL**.

| MO | ID | Produkt | Segmenty (filtr) | Primary | Stary URL | Nowy URL |
|---:|---:|---|---|---|---|---|
| 1 | 310 | Agrobielik 70 | Rolnictwo, Rybactwo, Sadownictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/wapno-agrobielik-70-big-bag-1000kg/` | `/wapno-nawozowe-rolnictwo/agrobielik-70/` |
| 2 | 311 | Agrobielik 90 | Rolnictwo, Rybactwo, Oczyszczalnie, Hurt | **Rolnictwo** ⚠️P4 | `/wapno-nawozowe-hurt/wapno-agrobielik-90-big-bag-1000kg/` | `/wapno-nawozowe-rolnictwo/agrobielik-90/` |
| 3 | 312 | Oxyfertil 90 | Rolnictwo, Rybactwo, Oczyszczalnie, Hurt | **Rolnictwo** ⚠️P4 | `/wapno-nawozowe-hurt/wapno-oxyfertil-90-frakcja-3-8mm-big-bag-1000kg/` | `/wapno-nawozowe-rolnictwo/oxyfertil-90/` |
| 4 | 313 | Wapno tlenkowe zawierające magnez | Rolnictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/wapno-zawierajace-magnez-big-bag-1000kg/` | `/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/` |
| 5 | 308 | Mieszanka tlenkowo-węglanowa | Rolnictwo, Sadownictwo | **Rolnictwo** | `/wapno-do-sadu/mieszanka-tlenkowo-weglanowa-luz/` | `/wapno-nawozowe-rolnictwo/mieszanka-tlenkowo-weglanowa/` |
| 6 | 314 | Wapno węglanowe granulowane | Rolnictwo, Sadownictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/wapno-weglanowe-bez-magnezu-granulowane-big-bag-600kg/` | `/wapno-nawozowe-rolnictwo/weglanowe-granulowane/` |
| 7 | 315 | Wapno węglanowe Odmiana 04 | Rolnictwo, Sadownictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/wapno-weglanowe-bez-magnezu-luz/` | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/` |
| 8 | 316 | Wapno węglanowe Odmiana 05 | Rolnictwo, Sadownictwo | **Rolnictwo** | `/wapno-do-sadu/wapno-weglanowe-bez-magnezu-luz-2/` | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` |
| 9 | 317 | Wapno węglanowe z magnezem granulowane | Rolnictwo, Sadownictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/wapno-weglanowe-zawierajace-magnez-granulowane-big-bag-600kg/` | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/` |
| 10 | 318 | Wapno węglanowe z magnezem Odmiana 04 | Rolnictwo, Sadownictwo | **Rolnictwo** | `/wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz/` | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-04/` |
| 11 | 319 | Wapno węglanowe z magnezem Odmiana 05 | Rolnictwo, Sadownictwo | **Rolnictwo** | `/wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz-2/` | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-05/` |
| 12 | 305 | Kreda nawozowa granulowana | Rolnictwo, Rybactwo, Sadownictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/kreda-nawozowa-granulowana-big-bag-500kg/` | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-granulowana/` |
| 13 | 306 | Kreda nawozowa sypka | Rolnictwo, Rybactwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/kreda-nawozowa-sypka-luz/` | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-sypka/` |
| 14 | 307 | Kreda pastewna | Paszarstwo, Hurt, Rolnictwo | **Paszarstwo** | `/kreda-pastewna/kreda-pastewna-worek-30kg/` | `/paszarstwo/kreda-pastewna/` ⚠️P1 |
| 15 | 302 | Dolomit | Rolnictwo, Sadownictwo, Hurt | **Rolnictwo** | `/wapno-nawozowe-hurt/dolomit-worek-25kg/` | `/wapno-nawozowe-rolnictwo/dolomit/` 🔑 |
| 16 | 309 | Wapno hydratyzowane Bielik | Oczyszczalnie, Budownictwo, Hurt | **Wapno hydratyzowane** | `/wapno-hydratyzowane/wapno-hydratyzowane-bielik-luz/` | `/wapno-hydratyzowane/bielik/` ⚠️P2 |
| 17 | 320 | Wapno palone mielone wysokoreaktywne | Oczyszczalnie | **Oczyszczalnie** | `/wapno-do-oczyszczalni/wapno-palone-mielone-wysokoreaktywne-luz-24t/` | `/wapno-do-oczyszczalni/wapno-palone-mielone/` |
| 18 | 303 | Kreda czarna (jeziorna) | Rolnictwo, Sadownictwo, Hurt | **Rolnictwo** ⚠️P5 | `/wapno-nawozowe-hurt/kreda-czarnajeziorna-.../` | `/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/` |
| 19 | 304 | Kreda malarska | (poza segmentami) | **Kreda malarska** | `/wapno-nawozowe-hurt/kreda-malarska-worek-30kg/` | `/kreda-malarska/kreda-malarska/` ⚠️P3 |

Suma zmian: **19/19 produktów zmienia URL** (wszystkie dostają czysty slug; 16 zmienia też ścieżkę kategorii). → 19 reguł 301.

## Noty / punkty do decyzji

- **🔑 Dolomit (302):** fraza `dolomit` = **6600/mies**. Wyjście z `/hurt/dolomit-worek-25kg/` na `/wapno-nawozowe-rolnictwo/dolomit/` to największy pojedynczy zysk on-page tej operacji.
- **⚠️P1 Paszarstwo:** obecny slug kategorii to `kreda-pastewna` (nazwa produktu) → dawałoby `/kreda-pastewna/kreda-pastewna/` (podwójne). Propozycja: slug kategorii `paszarstwo`, produkt `kreda-pastewna` → `/paszarstwo/kreda-pastewna/`. **Zmienia URL archiwum kategorii → dodatkowy 301.**
- **⚠️P2 Bielik / „Budownictwo za szeroko":** zostawiam slug kategorii `wapno-hydratyzowane` (specyficzny, celuje w frazę 2400), a produkt = `bielik` → `/wapno-hydratyzowane/bielik/`. Nazwę wyświetlaną kategorii można zmienić z „Budownictwo" na „Wapno hydratyzowane". Do potwierdzenia.
- **⚠️P3 Kreda malarska (304):** poza katalogiem i poza 5 segmentami. Osobna mini-kat `kreda-malarska` — **wykluczona z filtra „Zastosowanie"** (żeby nie mieszać produktu wśród segmentów) i bez kafla na /oferta/. Łapie własny popyt (320/mies) własnym URL.
- **⚠️P4 Agrobielik 90 (311) / Oxyfertil 90 (312):** badge katalogu = ROLNICTWO first, ale treść kart mocno akcentuje **oczyszczalnie/higienizację osadów** (to ich realny lead sprzedażowy B2B). Alternatywa: primary = Oczyszczalnie (`/wapno-do-oczyszczalni/agrobielik-90/`). **Decyzja: trzymamy badge (Rolnictwo) czy realny lead (Oczyszczalnie)?**
- **⚠️P5 Kreda czarna jeziorna (303):** poza katalogiem, ale to polepszacz glebowy (kwasy humusowe) → Rolnictwo pasuje. Alternatywa: też osobno. Domyślnie Rolnictwo.

## Co Model A pociąga poza slugami/primary (do wdrożenia razem)

1. Przepięcie filtra „Zastosowanie" (JSF 1471): `_source_taxonomy` `product_cat` → `pa_agria-segment`.
2. Redukcja `product_cat` do jednej (wiodącej) kategorii per produkt; pełne segmenty zostają w `pa_agria-segment` (weryfikacja kompletności przed odpięciem).
3. Usunięcie „Hurtownie" z `product_cat` (zostaje w atrybucie).
4. `menu_order` wg kolumny MO.
5. 19× 301 (+ 301 dla archiwów kategorii, których slug się zmienia: Paszarstwo).
6. Kafle /oferta/: po redukcji product_cat pokażą tylko realne kategorie wiodące — sprawdzić prezentację (kafle vs filtr).

## Ryzyka / do weryfikacji przed zapisem

- **Kompletność `pa_agria-segment`** — potwierdzić, że każdy produkt ma w atrybucie WSZYSTKIE segmenty, które ma dziś w product_cat (inaczej filtr zgubi produkty). Liczności się zgadzają (7 wartości, te same counts), ale sprawdzić per-produkt.
- **Archiwa Rybactwo/Sadownictwo/Oczyszczalnie** jako `product_cat` znikają z URL (brak primary) — ale zostają jako wartości filtra; landing per segment wg planu KR (osobno).
- **Indeksacja:** 19 nowych URL do zgłoszenia przez `index-submit` po wdrożeniu; stare → 301 (nie zgłaszać).
- **Cache:** CDN nazwa.pl + Elementor element-cache — bust po każdej zmianie.
