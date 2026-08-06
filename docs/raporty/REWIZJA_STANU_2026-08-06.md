# Rewizja stanu na żywo — 2026-08-06

> Weryfikacja listy z §1 promptu M3 (stan notatek: 2026-08-03) wobec produkcji.
> Źródła: `scripts/gsc_inspect.py`, `scripts/gsc_pull.py`, GSC Sitemaps API, GA4 Data API, PSI v5, MCP `query_db`, curl z cache-bustem.

---

## Tabela weryfikacji

| # | Pozycja | Stan 03.08 | Stan 06.08 (live) | Werdykt |
|---|---|---|---|---|
| 1 | 4 poradniki + landing stabilizacji | wszystkie „URL unknown", `lastCrawl` pusty | **2 z 5 ruszyły**: `/jak-stosowac-wapno-nawozowe/` i `/wapno-nawozowe-na-trawnik/` → „wykryta, niezindeksowana". Nadal unknown: `/ile-wapna-granulowanego-na-ha/`, `/higienizacja-osadow-sciekowych-wapnem/`, `/wapno-do-stabilizacji-gruntow/` | **częściowo obalone** |
| 2 | `/do-pobrania/` | werdykt „noindex" z crawlu 12.04, live `index, follow` | bez zmian — GSC dalej trzyma 12.04, live potwierdzone `index, follow` | potwierdzone |
| 3 | Duplikat sitemapy | `wp-sitemap.xml` zgłoszona obok RankMath | **plik daje 404**, ale w GSC **nadal zgłoszona** (ostatnie pobranie 03.08, zgłoszenie 28.05.2025) | potwierdzone (do wyrejestrowania przez API) |
| 4 | Blok linkowania na kartach | 15 z 20 | 15 z 20 potwierdzone. Bez bloku: `agrobielik-70` (flagowiec), `kreda-malarska`, `wapno-palone-mielone`, `kreda-pastewna` (+ `/oferta/`, które kartą nie jest) | potwierdzone **+ nowe ustalenie, patrz niżej** |
| 5 | Kanibalizacja „wapno bielik" | 6 URL | 6 URL w GSC, ale **3 z nich to stare adresy zwracające 301** celujące dokładnie w `/wapno-hydratyzowane/bielik/`. Realna kanibalizacja: kategoria + karta + strona główna | **częściowo obalone** |
| 6 | LCP mobile | 7,4 s home / 6,9 s karta / 6,0 s kategoria | **7,4 s home** (perf 68), **5,6 s kategoria** (perf 74). TBT 90/80 ms, CLS 0,002/0. SEO 100/100 | potwierdzone (kategoria lekko lepiej) |
| 7 | GA4 | atrybucja martwa, ~40% ruchu z 404 demo | lipiec: **Direct 141 / Organic Search 5** przy 221 klikach w GSC. W TOP-15 landingów **9 pozycji to demo motywu** (`/produkt/fresh-avocado`, `/product-category/orange`…), wszystkie zwracają 404 | potwierdzone |
| 8 | Element-cache Elementora | wyłączony | `elementor_element_cache_ttl = disable` | potwierdzone |
| 9 | Nagłówki bezpieczeństwa | 4 z 6, brak CSP i Permissions-Policy | **5 z 6** — `permissions-policy` jest (`geolocation=(), camera=(), microphone=(), payment=()`). Brak wyłącznie **CSP** | **obalone na plus** |
| 10 | Menu — 3 pozycje `draft` | nie ruszać do września | bez zmian | potwierdzone |

---

## Ustalenia spoza listy

### A. Indeksacja koreluje z liczbą linków wewnętrznych — to jest dowód, nie hipoteza

Przeskanowany render 20 URL z `product-sitemap.xml`. Rozkład linków do nowych treści:

| Docelowy URL | Linków z kart | Stan w GSC |
|---|---|---|
| `/wapnowanie-gleby/` | 15 | **zaindeksowana**, poz. 7,7 · 5 917 wyśw. |
| `/jak-stosowac-wapno-nawozowe/` | 15 | wykryta, niezindeksowana |
| `/ile-wapna-granulowanego-na-ha/` | 3 | **URL unknown** |
| `/wapno-do-stabilizacji-gruntow/` | 1 | **URL unknown** |
| `/higienizacja-osadow-sciekowych-wapnem/` | 1 | **URL unknown** |
| `/wapno-nawozowe-na-trawnik/` | 0 | wykryta, niezindeksowana (wejście z `/poradniki/` i huba) |

Wniosek: **blok linkowania został wdrożony na 15 kartach, ale sam blok jest niepełny** — dwie treści dostały po 15 linków, trzy po 1–3. Zadanie P0 to nie tylko „dodaj blok na 4 brakujących kartach", ale **wyrównanie zawartości bloku na wszystkich 19 kartach**.

Hub `/wapnowanie-gleby/` (najmocniejsza strona witryny) linkuje do 4 poradników, ale **nie linkuje do `/wapno-do-stabilizacji-gruntow/`**.

### B. Slugi pod landingi Bloku 1 są wolne

- `/wapno-granulowane/` → **404** (slug wolny).
- `/wapno-nawozowe/` → 301 na `/wapno-nawozowe-na-trawnik/`, ale **to nie jest przekierowanie do zdjęcia**. W `.htaccess` nie ma reguły dla tego adresu (są wyłącznie 22 mapowania produktów po migracji z 08.07), w bazie nie ma wpisu o slugu `wapno-nawozowe`. To WordPress `redirect_guess_404_permalink` — przy braku dopasowania zgaduje najbliższy slug. **Publikacja strony pod tym adresem wyłącza zgadywanie automatycznie.**

Architektura docelowa była już rozstrzygnięta w `ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md` §6 (Blok 1): landingi komercyjne na exact-match slugach, typ strony = produktowy landing kategorii, bez ceny i koszyka.

**Nowe wobec 14.07:** kategoria `/wapno-nawozowe-rolnictwo/` weszła w lipcu na poz. **11,0 · 146 wyśw.** na frazę „wapno nawozowe" — w lipcu jeszcze nie rankowała. Poz. 11 to druga strona SERP, więc ruchu z tego nie ma, ale po publikacji landingu dwie własne strony celują w jedną frazę. Rozwiązanie w ramach ustalonej architektury: landing = strona docelowa (exact-match H1/title/self-canonical), kategoria = lista produktów z meta pod frazę rozszerzoną i linkiem w górę do landingu.

### C. Migracja URL-i domknięta poprawnie

Stare adresy (`/wapno-nawozowe-hurt/*`, `/wapno-do-sadu/*`, `/wapno-hydratyzowane/wapno-hydratyzowane-bielik-luz/`) zwracają **301** na właściwe karty. W lipcu wygenerowały jeszcze 500+ wyświetleń jako rezydualne wpisy w indeksie — to naturalnie wygaśnie.

Skutek praktyczny: rekomendacja „jedna strona docelowa dla »wapno bielik« = `/wapno-hydratyzowane/bielik/`" jest **zgodna z tym, co już robią przekierowania**. Zostaje uporządkowanie relacji kategoria ↔ karta ↔ strona główna.

### D. Sitemapy

`sitemap_index.xml` obejmuje: post, page, product, category, product_cat. Zero błędów, ostatnie pobranie 03.08. `wp-sitemap.xml` do wyrejestrowania (DELETE przez Sitemaps API).

---

## Co z tego wynika dla planu M3

1. **P0 indeksacyjne rośnie o jedną pozycję** — poza blokiem na 4 kartach dochodzi wyrównanie zawartości bloku na pozostałych 15 oraz link kontekstowy z huba do landingu stabilizacji.
2. **Kanibalizacja jest mniejszym problemem, niż zakładaliśmy** — trzy z sześciu adresów rozwiążą się same. Zadanie schodzi z P1 na drobną korektę meta i linkowania.
3. **CSP zostaje jako jedyny brak w nagłówkach** — Permissions-Policy już jest.
4. **Slug `/wapno-nawozowe/` wymaga decyzji** przed KROKIEM A.
5. **LCP home 7,4 s bez zmian** — pozostaje najdroższą pojedynczą stratą i wpływa na koszt kliknięcia w Ads.
