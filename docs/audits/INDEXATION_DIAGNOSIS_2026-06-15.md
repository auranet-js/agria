# Diagnoza indeksacji agria.pl — 2026-06-15

> Źródło: GSC URL Inspection API (property `https://agria.pl/`) + live HTML + RankMath options. Sesja 2026-06-15.

## Wniosek

„**0/38 zaindeksowanych**" w GSC sitemap report to **NIE aktywny noindex** — to **zaległy re-crawl** po zdjęciu kwietniowego noindex.

- Kwiecień 2026 (budowa): produkty/wpisy/część stron miały `noindex` → Google przecrawlował (31.03–22.04) i wykluczył.
- Noindex **zdjęto**: RankMath globalnie `pt_post_robots` / `pt_page_robots` / `pt_product_robots` = `index`; live HTML serwuje `index, follow`.
- Google od kwietnia tych URL nie odwiedził → GSC trzyma nieaktualny werdykt.
- Home + `/kalkulator-wapnowania/` (re-crawl 11–12.06) = zaindeksowane.

## Inwentaryzacja 37 URL z sitemapy

| Stan | Liczba |
|---|---|
| Submitted and indexed | 13 |
| Excluded by 'noindex' (stary crawl, teraz index,follow) | 14 |
| URL is unknown to Google | 5 |
| Discovered – currently not indexed | 4 |
| Page with redirect (`/cart/`) | 1 |

## Fix: 23 URL do re-submit (Indexing API, URL_UPDATED)

Przez `~/bin/index-submit --project agria --type URL_UPDATED --urls-file <plik>`. **Sprawdzić budżet `--status` przed** (pula wspólna 200/dobę; 2026-06-14 wyczerpana przez PrimaAuto → czekać na reset Pacific). `/cart/` **pominięty** (redirect, transakcyjna).

**Produkty (priorytet handlowy):**
- /wapno-nawozowe-hurt/wapno-agrobielik-70-big-bag-1000kg/
- /wapno-nawozowe-hurt/wapno-agrobielik-90-big-bag-1000kg/
- /wapno-nawozowe-hurt/dolomit-worek-25kg/
- /wapno-nawozowe-hurt/wapno-oxyfertil-90-frakcja-3-8mm-big-bag-1000kg/
- /wapno-nawozowe-hurt/wapno-weglanowe-bez-magnezu-granulowane-big-bag-600kg/
- /wapno-nawozowe-hurt/wapno-weglanowe-bez-magnezu-luz/
- /wapno-nawozowe-hurt/wapno-weglanowe-zawierajace-magnez-granulowane-big-bag-600kg/
- /wapno-hydratyzowane/wapno-hydratyzowane-bielik-luz/
- /wapno-do-oczyszczalni/wapno-palone-mielone-wysokoreaktywne-luz-24t/
- /wapno-do-sadu/wapno-weglanowe-bez-magnezu-luz-2/
- /wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz/
- /wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz-2/

**Wpisy blog:**
- /czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/
- /jak-murowac-klinkier/
- /wapnowanie-gleby/

**Strony:**
- /oferta/
- /o-firmie/
- /poradniki/
- /category/poradniki/
- /do-pobrania/
- /rodo/
- /wsparcie/
- /zamowienia/

## Dodatkowe znaleziska on-page (do backlogu)

1. **`/cart/` w sitemapie XML** — koszyk WooCommerce (redirect), wyciąć z sitemapy RankMath (nie indeksować strony transakcyjnej).
2. **Duplikacja poradników** — `/category/poradniki/` + `/poradniki/`, sprawdzić permalink/taxonomy (możliwy duplikat).
