# Audyt SEO agria.pl od nowa — kategorie, produkty, indeksacja, plan VIII–X

> **Data pomiarów:** 2026-08-24 · **Zlecenie:** `docs/prompty/2026-08-24-PROMPT_AUDYT_SEO_OD_NOWA.md`
> **Zakres:** audyt. **Zero zmian na produkcji, zero zgłoszeń do Indexing API, zero nowych treści.**
>
> **Zasada dowodu.** Każdy wiersz pochodzi z pomiaru wykonanego tego dnia, nie z dokumentu.
> Gdzie czegoś nie zmierzyłem, jest napisane „niezmierzone". Gdzie pomiar przeczy dokumentowi,
> jest to nazwane wprost w §6.

## Źródła i okna pomiarowe

| Co | Jak | Okno / koszt |
|---|---|---|
| Stan bazy | MCP `agria` `query_db` (`wpfz_`) | 24.08 |
| Kody HTTP, `robots`, canonical, render | `curl` z cache-bustem, 62 adresy + 26 historycznych | 24.08 |
| Sitemapy | `sitemap_index.xml` i 6 podmap | 24.08 |
| Indeksacja | GSC URL Inspection API, 66 adresów | 24.08 |
| Ruch i pozycje | GSC Search Analytics API, wymiar `page` oraz `page × query` | **26.05–23.08 (90 dni)** |
| Wolumeny i sezonowość | DataForSEO `google_ads/search_volume`, PL/pl, loc 2616 | seria VIII 2025 – **VII 2026**, 0,18 USD |
| SERP | DataForSEO `serp/google/organic/live/regular`, 7 fraz | 24.08, 0,01 USD |
| Kampania | Google Ads API v25, `landing_page_view` | 13–23.08 |
| `.htaccess` | FTP `ftp.server371853.nazwa.pl` | 24.08 |

**Uwaga metodyczna, której trzymam się w całym dokumencie:** kliknięcia i CTR liczone są
**z wymiaru `page`**, nigdy przez sumowanie wierszy `query`. Wymiar `query` służy wyłącznie
do struktury intencji (memory `feedback_gsc_ctr_z_poziomu_strony`).

---

## Punkt odniesienia — cały serwis w 90 dniach

| Miara | Wartość |
|---|---|
| Adresy zbierające wyświetlenia | **61** |
| Wyświetlenia | **34 954** |
| Kliknięcia | **563** |
| CTR serwisu | 1,61% |
| Leady z formularza (`agria_inquiry`, dane pierwszej strony) | **6** (03.07, 16.07, 27.07, 28.07, 05.08, 13.08) |
| Ads 13–23.08 | 215 kliknięć, **396,18 zł**, **0 konwersji** |

Jedna strona — `/wapnowanie-gleby/` — daje **61% wyświetleń** serwisu (21 183) i 22% kliknięć.
Najwięcej kliknięć zbiera jednak strona główna — **143**, w tym 22 na samą frazę `agria`.
**Poza hubem i marką serwis praktycznie nie zbiera kliknięć organicznych.**

---

# ETAP 1 — kategorie produktowe

Tabela zastana z promptu **potwierdzona co do jednego wiersza** (`query_db`, `product_cat`, 24.08):
osiem termów, liczby produktów i długości opisów zgadzają się. Poniżej to, czego w tamtej tabeli
nie było — co każdy adres realnie oddaje i czy ktokolwiek go szuka.

| term | Nazwa | Adres | HTTP | `robots` | Werdykt GSC | Ost. crawl | Sitemapa | 90 dni: wyśw / klik / poz |
|---|---|---|---|---|---|---|---|---|
| **764** | Wapno nawozowe | `/wapno-nawozowe-rolnictwo/` | 200 | index | **Zaindeksowana** | 21.08 | TAK | **1 360 / 19 / 9,1** |
| **767** | Oczyszczalnie | `/wapno-do-oczyszczalni/` | 200 | index | **Zaindeksowana** | 22.08 | TAK | **806 / 32 / 9,5** |
| **768** | Budownictwo | `/wapno-hydratyzowane/` | 200 | index | **Zaindeksowana** | 21.08 | TAK | 172 / 2 / 31,3 |
| **770** | Paszarstwo | `/paszarstwo/` | 200 | index | **Zaindeksowana** | 16.08 | TAK | 67 / 2 / 13,4 |
| **830** | Kreda malarska | `/kreda-malarska/` | 200 | index | **Discovered — not indexed** | nigdy | TAK | **0 / 0 / —** |
| **765** | Sadownictwo | `/wapno-do-sadu/` | **301 → `/oferta/`** | — | Page with redirect | 24.08 | nie | 31 / 0 / 9,4 |
| **769** | Hurtownie | `/wapno-nawozowe-hurt/` | **301 → `/oferta/`** | — | Page with redirect | 14.08 | nie | **107 / 5 / 20,4** |
| **766** | Wapno do stawów | `/rybactwo-kat-archiwum/` | **200** | **noindex** | URL unknown | nigdy | nie | 0 / 0 / — |

Adresy historyczne tych samych kategorii (`/kategoria-produktu/<slug>/`) — patrz ETAP 3.

## Rozstrzygnięcie 766 — co jest czym

Prompt słusznie kazał to rozplątać. Stan faktyczny:

- **Term 766 „Wapno do stawów"** ma dziś slug `rybactwo-kat-archiwum` i **0 produktów**.
  Adres `/rybactwo-kat-archiwum/` **odpowiada 200** z `follow, noindex` (Rank Math sam noindeksuje
  pusty term) i jest linkowany z `/oferta/`. Google go nie zna.
- **Landing o stawie żyje pod `/wapno-do-stawu/`** (strona ID 2796, nie kategoria), 8 725 znaków,
  `index, follow`, w `page-sitemap.xml` z `lastmod 2026-08-21`.
- **Adres, który Google znał z lipca — `/wapno-do-stawow/` — oddaje 404.** W GSC ma werdykt
  „Excluded by `noindex`" z crawla **28.03**, zero wyświetleń w 90 dniach.

Czyli: slug kategorii został **zwolniony** pod landing (T-056, 21.08), landing dostał liczbę
pojedynczą po audycie Rank Matha, a stary adres w liczbie mnogiej został bez reguły.

**Nowy pomiar, którego nie ma w rejestrze: `/wapno-do-stawu/` jest sierotą.** Na 22 przeskanowanych
stronach serwisu **zero linków** prowadzi do tego adresu, a URL Inspection mówi **„URL is unknown
to Google"** — trzy dni po publikacji, mimo obecności w sitemapie. Sama reguła 301 z T-072 tego
nie naprawi; potrzebne są linki (menu „Rybactwo", `/oferta/`, hub, karty sześciu produktów z listingu).

## Popyt — czy kategoria ma po co istnieć

| Adres | Fraza główna | Wolumen/mies. | Szczyt roczny | Kto wygrywa SERP i jakim typem strony |
|---|---|---|---|---|
| `/wapno-nawozowe-rolnictwo/` | `wapno nawozowe` | **1 300** | **VIII–X 1 900** | OLX #1, sklepy, **treść producentów** (industria.eu, nawozy.eu, osadkowski, holcim) |
| `/wapno-hydratyzowane/` | `wapno hydratyzowane` | **2 400** | III 3 600 | niezmierzone SERP-em |
| `/paszarstwo/` | `kreda pastewna` | **2 400** | III/V 2 900 | sklepy (hotfarm, fermo, allegro) + **treść** (vitalzam, polcalc), featured snippet |
| `/wapno-do-oczyszczalni/` | `higienizacja osadów ściekowych` | **30** | XI/VII 50–70 | niezmierzone SERP-em |
| `/kreda-malarska/` | `kreda malarska` | **320** | **VI 880**, trend rosnący | **wyłącznie sklepy z ceną + OLX + Allegro + Ceneo**, zero treści |
| `/wapno-do-sadu/` | `wapno do sadu` | **30** | X–XI 70 | niezmierzone SERP-em |
| `/wapno-nawozowe-hurt/` | `wapno nawozowe hurt` | **brak danych** (poniżej progu) | — | — |
| `/rybactwo-kat-archiwum/` | — | — | — | — |

**`wapno nawozowe hurt`, `wapno hurt`, `wapno do oczyszczalni`, `wapno do stabilizacji gruntów`
i `wapno dla sadownictwa` zwracają z planera `null`** — to nie jest „mały wolumen", to brak
mierzalnego popytu na samą nazwę. Wnioski o tych adresach muszą stać na innych frazach.

## Kanibalizacja wewnątrz kategorii — zmierzona, nie założona

`page × query`, ta sama fraza, różne nasze adresy:

| Fraza | Nasze adresy | Najlepsza pozycja |
|---|---|---|
| `wapno węglanowe` (1 000/mies.) | `/weglanowe-odmiana-04/` 388 wyśw. poz. 9,9 · `/weglanowe-granulowane/` 79 poz. 37,5 · `/weglanowe-magnez-granulowane/` 10 poz. 26,3 | **9,9** |
| `wapno nawozowe tlenkowe` | `/wapno-tlenkowe-magnez/` 43 poz. 13,4 · **stary** `/wapno-nawozowe-hurt/wapno-zawierajace-magnez-big-bag-1000kg/` 55 poz. 17,7 · `/agrobielik-70/` 10 poz. 12,3 · **stary** `…agrobielik-70-big-bag…` 1 poz. 43 | **12,3** |
| `wapno bielik` (210/mies.) | `/bielik/` 21 poz. 11,5 · **stary** `/wapno-hydratyzowane/…bielik-luz/` 23 poz. 15,3 · `/wapno-hydratyzowane/` 16 poz. 50,1 · `/agrobielik-70/` 3 poz. 64 · **stary** `…agrobielik-70-big-bag…` 3 poz. 57,3 | **11,5** |
| `wapno budowlane tarnów` | `/` 80 poz. 7,1 · `/oferta/` 47 poz. 25,7 · `/wapno-hydratyzowane/` 34 poz. 74,2 · `/rodo/` 2 poz. 6 | **7,1** |
| `oxyfertil` | `/oxyfertil-90/` 54 poz. 6,0 · **stary** `…oxyfertil-90-frakcja…` 19 poz. **5,4** | 5,4 (stary!) |
| `wapno odmiana 05` | `/weglanowe-magnez-odmiana-05/` 33 poz. 3,7 · **stary** `/wapno-do-sadu/…luz-2/` 9 poz. **2,6** | 2,6 (stary!) |

**Wzorzec z ADR 11.08 utrzymuje się w niezależnym oknie pomiarowym** (26.05–23.08): pięć adresów
na `wapno bielik` → najlepsza pozycja 11,5. Nowy element, którego ADR nie znał: **część rywali
to nasze własne, przekierowane adresy sprzed migracji lipcowej** — na dwóch frazach stary adres
stoi **wyżej** niż kanoniczny, mimo działającego 301.

## Decyzja per kategoria

| term | Adres | Decyzja | Uzasadnienie z pomiaru |
|---|---|---|---|
| **764** | `/wapno-nawozowe-rolnictwo/` | **zostaje jako kategoria, do wzmocnienia treścią** | Trzeci adres serwisu (1 360 wyśw.), jedyny rankujący na `wapno nawozowe` (251 wyśw., poz. 10,9). SERP na tę frazę nagradza treść producenta — dziś kategoria ma 3 996 znaków i 3 × H2 |
| **767** | `/wapno-do-oczyszczalni/` | **zostaje jako kategoria** | 806 wyśw., 32 kliknięcia, CTR 3,97% — druga najlepsza konwersja uwagi w serwisie. Zbiera całą intencję „higienizacja osadów" (128 + 100 + 53 wyśw.), której **poradnik `/higienizacja-osadow-sciekowych-wapnem/` nie zbiera wcale** |
| **768** | `/wapno-hydratyzowane/` | **zostaje, ale pozycja 31,3 znaczy, że nie odpowiada na frazę** | `wapno hydratyzowane` 2 400/mies., my na 50,8 na własnej marce `wapno bielik`. To adres do przepisania w T-085, nie do budowy nowego landingu |
| **770** | `/paszarstwo/` | **zostaje jako kategoria, priorytet opisu** | Największy klaster portfela, kategoria ma 3 083 znaki i **jeden** H2. Stary adres `/kreda-pastewna/` (301) zbiera **253 wyśw. poz. 11,0** — więcej niż kategoria (67) i karta (132) razem |
| **830** | `/kreda-malarska/` | **do rozstrzygnięcia: zostaje bez pracy albo znika** | **Jedyna z ośmiu kategorii bez `rank_math_title` i bez `rank_math_description`** (sprawdzone w `termmeta`), z **zerowym** opisem taksonomii i werdyktem „Discovered — not indexed". Karta produktu wygrywa z nią na tę samą frazę (215 wyśw., poz. 7,4). SERP to wyłącznie sklepy detaliczne — B2B tonowe tam nie wygra |
| **765** | `/wapno-do-sadu/` | **301 zostaje do 30.11**, potem treść na tym adresie | Popyt realny, ale mały (`wapno do sadu` 30, `wapnowanie drzew owocowych kiedy` 210). **301 zdejmować razem z treścią, nigdy przed** — adres nadal zbiera 31 wyśw. na poz. 9,4 |
| **769** | `/wapno-nawozowe-hurt/` | **301 zostaje; strona tonażowa wymaga rewizji uzasadnienia** | Sama nazwa nie ma mierzalnego popytu. 107 wyśw. na poz. 20,4 to resztki po starej strukturze. Frazy tonażowe zmierzone niżej niż zakłada rejestr — patrz §6 |
| **766** | `/rybactwo-kat-archiwum/` | **usunąć term albo dać 410/301** | 0 produktów, 200 z `noindex`, linkowany z `/oferta/`, Google go nie zna. Trzyma slug o nazwie roboczej w publicznym adresie — dług wprowadzony przy T-056 |

**Pułapka Premmerce jest realna, ale dziś nieaktywna.** Każdy z 19 produktów należy do
**dokładnie jednej** kategorii (`query_db`, `term_relationships`), więc sortowanie po najwyższym
`term_id` nie ma czego rozstrzygać. Ryzyko wraca w chwili, gdy przypiszemy produkt do drugiej
kategorii — na przykład przy listingu stawowym.

---

# ETAP 2 — produkty, 19 kart

**`_price` puste w 19 na 19** (`query_db`) — tryb katalogu utrzymany zgodnie z ADR
`2026-08-19-dwie-warstwy-cen.md`. Store API i schema nie ujawniają żadnej kwoty.
SKU ma 18 z 19 (#303 świadomie bez).

| ID | SKU | Adres kanoniczny | HTTP | Werdykt GSC | Ost. crawl | 90 dni: wyśw / klik / poz | Cena w treści |
|---|---|---|---|---|---|---|---|
| 315 | AGR-006 | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/` | 200 | **zaindeksowana** | 22.08 | **997 / 11 / 6,9** | TAK |
| 314 | AGR-008 | `…/weglanowe-granulowane/` | 200 | **zaindeksowana** | 22.08 | 455 / 1 / 19,7 | TAK |
| 312 | AGR-003 | `…/oxyfertil-90/` | 200 | **zaindeksowana** | 22.08 | **430 / 29 / 6,2** | TAK |
| 309 | AGR-018 | `/wapno-hydratyzowane/bielik/` | 200 | **zaindeksowana** | 22.08 | 301 / 9 / 7,3 | TAK |
| 319 | AGR-010 | `…/weglanowe-magnez-odmiana-05/` | 200 | **zaindeksowana** | 23.08 | 289 / 6 / 6,3 | TAK |
| 313 | AGR-004 | `…/wapno-tlenkowe-magnez/` | 200 | **zaindeksowana** | 22.08 | 245 / 1 / 13,9 | **NIE** |
| 304 | AGR-016 | `/kreda-malarska/kreda-malarska/` | 200 | **zaindeksowana** | 18.08 | 215 / 6 / 7,4 | TAK |
| 310 | AGR-001 | `…/agrobielik-70/` | 200 | **zaindeksowana** | 22.08 | 163 / 7 / 7,5 | TAK |
| 307 | AGR-015 | `/paszarstwo/kreda-pastewna/` | 200 | **zaindeksowana** | 22.08 | 132 / 2 / 8,4 | TAK |
| 317 | AGR-011 | `…/weglanowe-magnez-granulowane/` | 200 | **zaindeksowana** | 21.08 | 61 / 0 / 13,4 | TAK |
| 305 | AGR-013 | `…/kreda-nawozowa-granulowana/` | 200 | **zaindeksowana** | 21.08 | 25 / 0 / 15,8 | TAK |
| 302 | AGR-012 | `…/dolomit/` | 200 | **Discovered — not indexed** | nigdy | **0** | **NIE** |
| 320 | AGR-017 | `/wapno-do-oczyszczalni/wapno-palone-mielone/` | 200 | **Discovered — not indexed** | nigdy | **0** | TAK |
| 303 | — | `…/kreda-czarna-jeziorna/` | 200 | **URL unknown** | nigdy | **0** | **NIE** |
| 306 | AGR-014 | `…/kreda-nawozowa-sypka/` | 200 | **URL unknown** | nigdy | **0** | TAK |
| 308 | AGR-005 | `…/mieszanka-tlenkowo-weglanowa/` | 200 | **URL unknown** | nigdy | **0** | TAK |
| 311 | AGR-002 | `…/agrobielik-90/` | 200 | **URL unknown** | nigdy | **0** | TAK |
| 316 | AGR-007 | `…/weglanowe-odmiana-05/` | 200 | **URL unknown** | nigdy | **0** | **NIE** |
| 318 | AGR-009 | `…/weglanowe-magnez-odmiana-04/` | 200 | **URL unknown** | nigdy | **0** | TAK |

**Osiem z dziewiętnastu kart jest poza indeksem** — sześć Google nigdy nie odkrył, dwie odkrył
i nie pobrał. Wszystkie osiem siedzi w `product-sitemap.xml` od 15.07 lub 19.08.
To jest największa pojedyncza liczba w tym audycie i **w rejestrze nie występuje**: dziennik M1–M2
zamyka T-018 („sitemapa z aktualnymi adresami") i T-016 („SKU"), ale nikt nie sprawdził,
czy Google te adresy w ogóle wziął.

## Stare adresy produktowe — wszystkie 301, wszystkie nadal w SERP-ie

Każdy z 19 produktów odpowiada dziś **200 pod dokładnie jednym adresem**. Sprawdzone dwie bazy
historyczne, po jednym skoku, bez pętli:

- `/produkt/<slug>/` → **301 na adres kanoniczny, 19 z 19** (moduł `modules/legacy-urls/`)
- `/<stara-kategoria>/<stary-slug>/` → **301, 20 reguł w `.htaccess`, wszystkie trafiają**

**Ale te adresy nadal pracują w Google.** Piętnaście przekierowanych adresów (czternaście produktowych
plus stara kategoria `/kreda-pastewna/`) zebrało w 90 dniach **1 556 wyświetleń i 46 kliknięć** —
czyli **8% kliknięć organicznych całego serwisu na adresach, które od lipca oddają 301**:

| Stary adres (301) | wyśw. | klik. | poz. | Cel |
|---|---|---|---|---|
| `/kreda-pastewna/` | **253** | 6 | 11,0 | `/paszarstwo/` |
| `/wapno-nawozowe-hurt/wapno-zawierajace-magnez-big-bag-1000kg/` | 204 | 2 | 14,9 | `…/wapno-tlenkowe-magnez/` |
| `/wapno-hydratyzowane/wapno-hydratyzowane-bielik-luz/` | 181 | 5 | 10,1 | `/wapno-hydratyzowane/bielik/` |
| `/wapno-nawozowe-hurt/wapno-agrobielik-70-big-bag-1000kg/` | 168 | 7 | 8,7 | `…/agrobielik-70/` |
| `/wapno-do-sadu/wapno-weglanowe-zawierajace-magnez-luz-2/` | 133 | 2 | 5,7 | `…/weglanowe-magnez-odmiana-05/` |
| `/wapno-nawozowe-hurt/wapno-oxyfertil-90-frakcja-3-8mm-big-bag-1000kg/` | 127 | 3 | 6,0 | `…/oxyfertil-90/` |
| `/wapno-nawozowe-hurt/wapno-weglanowe-bez-magnezu-luz/` | 126 | 2 | 8,4 | `…/weglanowe-odmiana-04/` |
| `/wapno-nawozowe-hurt/kreda-nawozowa-granulowana-big-bag-500kg/` | 81 | 2 | 6,0 | `…/kreda-nawozowa-granulowana/` |
| `/wapno-do-oczyszczalni/wapno-palone-mielone-wysokoreaktywne-luz-24t/` | 68 | **13** | **3,7** | `…/wapno-palone-mielone/` |
| pozostałe 6 (`…granulowane-big-bag-600kg` 56 · `kreda-czarna…` 45 · `kreda-nawozowa-sypka-luz` 43 · `kreda-pastewna-worek-30kg` 39 · `kreda-malarska-worek-30kg` 31 · `…mieszanka…-luz` 1) | 215 | 4 | 4,2–10 | — |

**Najlepszy CTR w całym serwisie — 19,12% przy pozycji 3,7 — ma przekierowany adres wapna palonego**,
podczas gdy jego cel `…/wapno-palone-mielone/` ma werdykt „Discovered — not indexed" i zero wyświetleń.
To nie jest usterka przekierowania: 301 działa poprawnie. To jest sygnał, że **konsolidacja po
migracji lipcowej trwa nadal po siedmiu tygodniach**, a Google w części przypadków woli stary adres.
Roboty tu nie ma — jest wniosek: nie liczyć tych adresów jako straconych i nie ruszać reguł.

## Znane wątpliwości z promptu — rozstrzygnięcie

**#307 Kreda pastewna: zarzut jest nieprawdziwy na stronie.** Sprawdziłem **wszystkie cztery warstwy**
(render przez `curl`, `post_content`, `_elementor_data`, atrybuty `pa_*`, meta Rank Math):

- render karty: **0 wystąpień „egzoterm", 0 wystąpień „pH >12"**, tabela specyfikacji podaje
  `min. 37% CaO`, `Sypkie`, frakcje 0–0,3 / 0,1–0,4 / 0,4–0,8 / 1–3 mm, dawkowanie `1–2 kg / 100 kg paszy`,
- atrybuty taksonomiczne: 16 termów, komplet paszowy, zero parametrów tlenkowych,
- meta: `Kreda pastewna | AGRIA`.

Parametry wapna tlenkowego przy kredzie pastewnej **są w katalogu drukowanym** (`FAKTY_KLIENTA` §8 pkt 7,
errata) — i tam zostają do poprawy. **Na stronie zostały naprawione 15.07** przy naprawie parametrów
w czterech warstwach. Konsekwencja: **T-079 nie ma dziś przedmiotu w tej postaci** (patrz §6).

**#303 Kreda czarna, #302 Dolomit, #313 Tlenkowe z Mg, #316 Węglanowe odm. 05** — potwierdzone:
`0 wystąpień „zł/t netto"` na froncie, brak wyceny Pawła. Trzy z tych czterech są jednocześnie
poza indeksem. **#313 jest wyjątkiem: zaindeksowana, 245 wyświetleń, poz. 13,9 — jedyna z tej
czwórki, dla której cena realnie coś zmieni.**

**`/kreda-malarska/kreda-malarska/`** — zdublowany człon potwierdzony, adres 200, **zaindeksowany
i najlepiej pracujący produkt kredowy** (215 wyśw., poz. 7,4). Dług zostaje w T-068 (okno zimowe).
Nie ruszać przed przebudową struktury: to jedyny adres, który na `kreda malarska` w ogóle rankuje.

**Demo-produkt motywu** — `/produkt/organic-pineapple/` **404**, `product-category/orange/` **404**,
`/em_services/…` **404**, `/wishlist-2/` **404**. Zamknięte. W bazie zostaje 15 szkiców
nierejestrowanego CPT `produkt` (T-028) — niewidoczne publicznie.

**Schema `Product` bez `offers` w 19 na 19.** Karta emituje `Product` z 11–19 `PropertyValue`
i **zero `offers`**. Zgodnie z ADR 19.08 `offers` mają powstać **ręcznie z treści**, nie z `_price` —
i nie powstały. 15 kart ma kwotę w tekście, żadna nie ma jej w danych strukturalnych.

---

# ETAP 3 — przekierowania i zgłoszenia

Trzy warstwy, każda reguła sprawdzona na żywo `curl`-em z cache-bustem. **Wszystkie mają
dokładnie jeden skok, żadna nie tworzy pętli, każdy cel oddaje 200.**

## Warstwa 1 — `.htaccess`, blok `# BEGIN AGRIA 301`

Pobrany FTP-em 24.08. **30 reguł**, trzy pokolenia.

| # | Wzorzec | Cel | Zmierzone | Ocena |
|---|---|---|---|---|
| 1–20 | stare adresy produktowe (`^wapno-nawozowe-hurt/…`, `^wapno-do-sadu/…`, `^wapno-hydratyzowane/…-luz`, `^kreda-pastewna/…-worek-30kg`, `^wapno-do-oczyszczalni/…-luz-24t`) | adres kanoniczny produktu | **20/20 → 301, 1 skok, cel 200** | **zostają** — nadal zbierają 1 556 wyśw. |
| 21 | `^kreda-pastewna/?$` | `/paszarstwo/` | 301, cel 200 | **zostaje** — 253 wyśw. poz. 11,0 |
| 22 | `^wapno-nawozowe-hurt/?$` | `/oferta/` | 301, cel 200 | **zostaje do T-082** — 107 wyśw. poz. 20,4 |
| 23 | `^wapno-do-sadu/?$` | `/oferta/` | 301, cel 200 | **zostaje do 30.11** — 31 wyśw. poz. 9,4, zdejmować razem z treścią |
| 24–28 | `^kategoria-produktu/<5 kategorii>/?$` | czysty adres kategorii | **5/5 → 301** | **zostają** — profilaktyka, wszystkie „URL unknown" w GSC |
| 29 | `^kategoria-produktu/?$` | `/oferta/` | 301 | zostaje |
| 30 | reguła generyczna | — | **świadomie nie istnieje** | poprawnie: `/kategoria-produktu/nieistnieje/` → **404**, nie 301-do-404 |

**Luka w T-032, znaleziona dziś.** Reguły z 19.08 objęły **pięć** kategorii — te, które są
w `product_cat-sitemap.xml`. Trzy puste kategorie zostały pominięte, więc:

```
/kategoria-produktu/wapno-do-sadu/          → 200, noindex, canonical → /wapno-do-sadu/ (301)
/kategoria-produktu/wapno-nawozowe-hurt/    → 200, noindex, canonical → /wapno-nawozowe-hurt/ (301)
/kategoria-produktu/rybactwo-kat-archiwum/  → 200, noindex, canonical → /rybactwo-kat-archiwum/
```

Stara baza jest tu **dostępniejsza niż nowa** (200 wobec 301) i wskazuje canonicalem na adres,
który przekierowuje. Koszt: zerowy w ruchu (Google żadnego z nich nie zna), niezerowy w porządku.
Trzy linijki dopisu przy najbliższej edycji `.htaccess`.

**Brakuje jednej reguły — potwierdzone:** `^wapno-do-stawow/?$` została usunięta 21.08 przy T-056,
żeby zwolnić slug, i nie wróciła w nowej postaci. Stąd **404**. GSC: zero wyświetleń w 90 dniach,
werdykt „Excluded by `noindex`" z crawla **28.03** — czyli Google zna ten adres wyłącznie ze stanu
sprzed pięciu miesięcy. **Koszt zaniechania jest zerowy, koszt naprawy to jedna linia.**

## Warstwa 2 — moduł `modules/legacy-urls/legacy-urls.php`

Dwie funkcje, obie na `template_redirect` z priorytetem 1, obie obsługują **GET i HEAD**.

| Funkcja | Zakres | Zmierzone |
|---|---|---|
| `agria_redirect_legacy_product_base()` | `/produkt/<slug>/` → permalink z WooCommerce | **19/19 → 301, 1 skok**; `/produkt/nieistnieje/` → 404 |
| `agria_redirect_wycofane_wpisy()` | mapa: `/ile-wapna-granulowanego-na-ha/` → `/wapnowanie-gleby/` | **301, cel 200** |

Zabezpieczenie przed pętlą (odmowa, gdy permalink sam siedzi pod `/produkt/`) obecne w kodzie.

**Dwa martwe linki, których T-026 nie domknął.** W treści dwóch opublikowanych wpisów nadal stoją
odnośniki do wycofanego poradnika:

```
/jak-stosowac-wapno-nawozowe/     → /ile-wapna-granulowanego-na-ha/   (301)
/wapno-nawozowe-na-trawnik/       → /ile-wapna-granulowanego-na-ha/   (301)
```

Zapis w dzienniku mówi, że hub „stracił martwy link w Powiązanych" — i to prawda, ale dotyczyła
tylko huba. Linki wewnętrzne prowadzące przez 301 to nie błąd, tylko strata: dwa z nielicznych
sygnałów, jakie mamy, idą przez przekierowanie.

## Warstwa 3 — Premmerce Permalink Manager

Wtyczka buduje adresy produktów jako `/<kategoria>/<produkt>/`, adres wynika z kategorii
o **najwyższym `term_id`** (sortowanie `DESC`, ADR `2026-08-21-nazwy-kategorii-bez-segmentow.md`).

**Zmierzone dziś: każdy z 19 produktów należy do dokładnie jednej kategorii**, więc reguła
nie ma dziś czego rozstrzygać. Konsekwencje przypisania widoczne w adresach:

- #320 wapno palone mielone → jedyna kategoria `wapno-do-oczyszczalni` → `/wapno-do-oczyszczalni/wapno-palone-mielone/`,
  **mimo że produkt jest jednocześnie towarem stabilizacyjnym i stawowym**,
- #309 Bielik → `wapno-hydratyzowane` (term 768 „Budownictwo"),
- #304 kreda malarska → `kreda-malarska` → **zdublowany człon** `/kreda-malarska/kreda-malarska/`.

Premmerce **nie generuje własnych przekierowań** poza kanonizacją — `/kategoria-produktu/*`
przekierowuje `.htaccess`, `/produkt/*` moduł PHP.

## Zgłoszenia do Indexing API — co zgłosiliśmy i co z tego wyszło

`~/.claude/indexing-submit.log`, wszystkie wpisy `project=agria`:

| Data | Ile URL | Co z tego wyszło (werdykt GSC 24.08) |
|---|---|---|
| 15.06 | 23 | częściowo zadziałało — kategorie i część kart są dziś w indeksie |
| 08.07 | 19 | jw. |
| 09.07 | 5 (pojedynczo) | **nie zadziałało** — `/jak-stosowac-…/`, `/higienizacja-…/`, `/wapno-nawozowe-na-trawnik/` do dziś nie pobrane |
| 14.07 | 32 | **nie zadziałało dla nowych treści** |
| 30.07 | 5 | **nie zadziałało** |
| 19.08 | 1 (`/do-pobrania/`) | **nie zadziałało** — werdykt nadal `BLOCKED_BY_META_TAG`, crawl **12.04** |

**Diagnoza z T-026 była trafna i pozostaje trafna: problem nie leży po stronie odkrycia.**
Zgłoszenie przez Indexing API nie wywołuje crawlu zwykłej treści. Po scaleniu z 24.08 zmieniło się
jedno: `/jak-stosowac-wapno-nawozowe/` i `/higienizacja-osadow-sciekowych-wapnem/` awansowały
z „URL is unknown" (19.08) na **„Discovered — currently not indexed"** (24.08). Google je zna,
ale nadal nie pobrał.

**Korekta jednej tezy z promptu:** teza „crawl na tej domenie bywa liczony w tygodniach" **nie
utrzymuje się w pomiarze**. Daty ostatniego crawlu z 24.08: `/oferta/` **24.08**, `/wapno-do-sadu/`
**24.08**, `/` 23.08, `/wapnowanie-gleby/` 23.08, `/kontakt/` 23.08, dziesięć kart produktów
21–23.08. **Google crawluje ten serwis codziennie.** Problem jest selektywny: crawluje to,
co już zna, i nie sięga po nowe adresy.

## Zaległe werdykty — pełna lista

Sześć adresów ma w GSC werdykt „Excluded by `noindex`", choć **na żywo wszystkie oddają
`index, follow`**. Wszystkie sześć crawlowane po raz ostatni w kwietniu:

| Adres | Ostatni crawl | 90 dni |
|---|---|---|
| `/do-pobrania/` | **12.04** | 0 wyśw. |
| `/wsparcie/` | **12.04** | 0 wyśw. |
| `/o-firmie/` | **20.04** | 0 wyśw. |
| `/czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/` | **18.04** | 0 wyśw. |
| `/jak-murowac-klinkier/` | **08.04** | 0 wyśw. |
| `/wapno-do-stawow/` | **28.03** | 0 wyśw. (dziś 404) |

**`/o-firmie/` i `/wsparcie/` nie występują w rejestrze ani w diagnozie T-026** — to jest ta sama
kwietniowa zaległość, wykryta w czerwcu i częściowo naprawiona, ale nigdy nie zinwentaryzowana
do końca. Praktyczny wniosek jest jednak ten sam co przy `/do-pobrania/`: warunki po naszej stronie
są spełnione, wrócenie Google'a to nie jest zadanie, które da się wykonać.

---

# ETAP 4 — treści, które istnieją

Wszystkie opublikowane wpisy i strony (`query_db`: 17 stron + 9 wpisów `publish` + 1 `draft`),
z pomiarem 90 dni i werdyktem indeksacji.

| Adres | Opubl. | Realna edycja | Znaki treści | Werdykt GSC | Crawl | 90 dni: wyśw / klik / poz | Werdykt |
|---|---|---|---|---|---|---|---|
| `/wapnowanie-gleby/` | 23.02 | **24.08** | 11 327 | zaindeksowany | 23.08 | **21 183 / 122 / 7,1** | **pracuje** |
| `/` | 27.02 | 02.06 | — | zaindeksowana | 23.08 | **3 528 / 143 / 14,4** | **pracuje** (marka + geo) |
| `/kalkulator-wapnowania/` | 09.03 | 08.06 | 5 117 | zaindeksowany | 22.08 | **1 173 / 45 / 7,2** | **pracuje** |
| `/kontakt/` | 27.02 | 01.07 | 3 515 | zaindeksowany | 23.08 | 799 / 69 / 4,8 | **pracuje** (marka) |
| `/oferta/` | 26.02 | 24.03 | 3 776 | zaindeksowana | 24.08 | 316 / 4 / 11,3 | pracuje słabo |
| `/zamowienia/` | 20.03 | 08.06 | 2 757 | zaindeksowana | 16.08 | 99 / 0 / 2,8 | **dubluje** `/kontakt/` na `agria tarnów` |
| `/rodo/` | 09.03 | 09.03 | 0 | zaindeksowana | 17.08 | 34 / 0 / 2,6 | rankuje na `agria tarnów` poz. 1,9 — **szum** |
| `/poradniki/` | 09.03 | 24.03 | 2 998 | zaindeksowana | 12.08 | 16 / 0 / 4,3 | listing, bez H2 |
| `/wykwity-na-murze/` | 23.01 | 24.03 | 4 562 | zaindeksowany | **12.05** | 159 / **0** / 7,2 | **nie nasza intencja** |
| `/tynki-rodzaje-kategorie/` | 23.04.25 | 24.03 | 4 641 | zaindeksowany | **24.05** | 84 / **0** / 9,3 | **nie nasza intencja** |
| `/cement-…-klasy/` | 23.12.25 | 24.03 | 4 433 | zaindeksowany | **23.05** | 25 / **0** / 9,7 | **nie nasza intencja** — AGRIA nie sprzedaje cementu |
| `/jak-murowac-klinkier/` | 23.05.25 | 24.03 | 5 308 | **noindex z 08.04** | **08.04** | 0 | **nie nasza intencja** |
| `/jak-stosowac-wapno-nawozowe/` | 09.07 | **21.08** | **13 455** | **Discovered — not indexed** | **nigdy** | **0** | **nie pracuje, ma popyt** |
| `/higienizacja-osadow-sciekowych-wapnem/` | 09.07 | 09.07 | 7 526 | **Discovered — not indexed** | **nigdy** | **0** | **dubluje** `/wapno-do-oczyszczalni/` |
| `/wapno-nawozowe-na-trawnik/` | 09.07 | 09.07 | 5 676 | **URL unknown** | **nigdy** | **0** | **nie ma popytu** |
| `/czy-wapnowac-…-stawy-karpiowe/` | 12.03 | 12.03 | 4 746 | **noindex z 18.04** | **18.04** | **0** | **nie pracuje, ma popyt** |
| `/wapno-do-stawu/` | **21.08** | 21.08 | 8 725 | **URL unknown** | **nigdy** | 0 (3 dni) | **za wcześnie — ale sierota** |
| `/wapno-do-stabilizacji-gruntow/` | 14.07 | 21.08 | 5 934 | **URL unknown** | **nigdy** | **0** | **sierota, brak popytu na frazę** |
| `/do-pobrania/` | 09.03 | 19.08 | 3 583 | **noindex z 12.04** | **12.04** | 0 | zaległy werdykt |
| `/o-firmie/` | 27.02 | 08.06 | 3 456 | **noindex z 20.04** | **20.04** | 0 | zaległy werdykt |
| `/wsparcie/` | 13.03 | 13.03 | 0 | **noindex z 12.04** | **12.04** | 0 | **strona pusta — do usunięcia** |
| `/wapno-granulowane/` (Ads) | 06.08 | 21.08 | 9 299 | URL unknown | nigdy | 0 | **izolacja działa zgodnie z ADR** |
| `/wapno-nawozowe/` (Ads) | 14.08 | 21.08 | 10 144 | URL unknown | nigdy | 0 | **izolacja działa zgodnie z ADR** |
| `/polityka-…-cookies-eu/`, `/oswiadczenie-…-eu/` | 13.08 | 13.08 | 52 / 53 | URL unknown | nigdy | 0 | prawne, bez znaczenia |
| `/cart/` | 26.02 | 10.03 | — | Page with redirect → `/` | 22.08 | 0 | poza sitemapą, OK |
| `/ile-wapna-granulowanego-na-ha/` | 09.07 | 09.07 | 12 065 | Discovered — not indexed | nigdy | 0 | **`draft` + 301, scalone 24.08** |

**Alarm z ADR 11.08 jest negatywny:** oba landingi Ads mają werdykt „URL is unknown to Google",
zero linków wewnętrznych i nie ma ich w sitemapie. Izolacja stoi.

## Cztery rzeczy, które ta tabela mówi, a rejestr nie

**1. Trzy najbardziej rozbudowane treści serwisu mają zero wyświetleń.** `/jak-stosowac-wapno-nawozowe/`
(13 455 znaków renderu, 22 675 w bazie), `/wapno-do-stawu/` (8 725) i `/higienizacja-…/` (7 526)
nie zostały nigdy pobrane przez Google. Razem **29 706 znaków** wobec ~118 000 renderowanej treści całego serwisu — **jedna czwarta**.

**2a. Strona główna nie linkuje do żadnej treści.** Pomiar grafu linków (24.08, wieczór):
`/` — najmocniejszy crawlowany adres serwisu (crawl 23.08, 3 528 wyświetleń) — linkuje do
**dwunastu kart produktów i czterech kategorii, a do zera poradników**. Terminarz
`/jak-stosowac-wapno-nawozowe/` ma pięć linków przychodzących, ale **cztery z nich stoją na
stronach, które same są poza indeksem** (`/wapno-nawozowe-na-trawnik/`, `/higienizacja-…/`,
`/czy-wapnowac-…/`); indeksowane źródła to wyłącznie `/poradniki/` (crawl 12.08, najstarszy
w serwisie) i hub. **Liczba linków nie jest miarą — miarą jest, czy źródło linku jest crawlowane.**

**2. Sieroty.** Na 22 przeskanowanych stronach **zero linków wewnętrznych** prowadzi do
`/wapno-do-stawu/` i do `/wapno-do-stabilizacji-gruntow/`. Oba są w sitemapie, oba nieznane Google'owi.
Dla porównania `/jak-stosowac-wapno-nawozowe/` ma **16 linków w treści** i też nie został pobrany —
czyli linkowanie jest warunkiem koniecznym, nie wystarczającym. Sieroty to jednak jedyna część,
którą da się naprawić bez czekania na Google.

**3. Cztery wpisy budowlane to obcy zasób.** `wykwity`, `tynki`, `cement`, `klinkier` — 18 944 znaki
łącznie, **268 wyświetleń i zero kliknięć** w 90 dniach, żadna fraza nad progiem prywatności,
crawl ostatni raz w maju. Cement i klinkier nie są towarem AGRII. To zaległość po budowie strony,
nie zasób do rozwijania. Nie kasować (zero kosztu, minimalny zysk z kasowania), ale też nie
odświeżać i nie liczyć jako pokrycia.

**4. `/higienizacja-osadow-sciekowych-wapnem/` przegrywa z własną kategorią i to jest rozstrzygnięte
liczbą.** Kategoria `/wapno-do-oczyszczalni/` zbiera **całą** intencję osadową: `higienizacja osadów
ściekowych` 128 wyśw. poz. 17,4, `wapnowanie osadów ściekowych` 100 poz. 14,1, `urządzenie do
higienizacji osadów ściekowych` 53 poz. 10,8, `wapno do szamba` 33 poz. 11,8 — razem 806 wyświetleń
i 32 kliknięcia przy CTR 3,97%. Poradnik ma zero. Decyzja Janka z 24.08 (zostawić jako osobny adres,
wzmocniony linkiem) jest wykonana, ale **pomiar jej nie potwierdza** — patrz §6.

---

# ETAP 5 — plan VIII–X od nowa

## 5.1. Pomiar, który zmienia kolejność: sierpień, nie październik

Seria DataForSEO sięga dziś **VII 2026**, czyli o miesiąc dalej niż pomiar z 21.08.
Zestawienie miesiąc po miesiącu (wartość w VIII 2025 wobec średniej rocznej):

| Fraza | Śr./mies. | **VIII** | IX | X | XI | III | Szczyt roku |
|---|---|---|---|---|---|---|---|
| `wapno granulowane` | 4 400 | **9 900** | 6 600 | 8 100 | 5 400 | 6 600 | **VIII** |
| `wapno węglanowe` | 1 000 | **2 400** | 1 300 | 1 600 | 1 000 | 1 600 | **VIII** |
| `ile wapna na hektar` | 720 | **1 900** | 1 300 | 880 | 590 | 720 | **VIII** |
| `badanie gleby` | 1 000 | **1 900** | 1 300 | 1 000 | 1 000 | **1 900** | VIII i III |
| `wapno nawozowe` | 1 300 | **1 900** | 1 900 | 1 900 | 1 300 | 1 900 | VIII–X i III |
| `ile wapna granulowanego na hektar` | 480 | **1 600** | 1 000 | 720 | 480 | 480 | **VIII** |
| `wapno tlenkowe` | 720 | **1 300** | 880 | 1 000 | 880 | 1 000 | **VIII** |
| `wapno na pole` | 390 | **1 000** | 720 | 590 | 390 | 390 | **VIII** |
| `wapno granulowane big bag cena` | 260 | **590** | 390 | 320 | 260 | 320 | **VIII** |
| `jakie wapno na pole` | 140 | **480** | 320 | 320 | 210 | 90 | **VIII** |
| `kiedy siać wapno granulowane` | 210 | **390** | 320 | 320 | 210 | 320 | **VIII** |
| `wapno palone` | 2 400 | 1 600 | 2 400 | **3 600** | **3 600** | 3 600 | **X–XI** |
| `kiedy wapnować glebę` | 320 | 260 | 480 | **590** | **590** | 590 | **X–XI** |
| `kiedy wapnować pole` | 90 | 210 | 210 | **260** | 110 | 70 | **X** |
| `kreda do stawu` | 1 300 | 1 600 | 1 000 | 1 000 | 720 | **2 900** | **III** |
| `wapno hydratyzowane` | 2 400 | 2 400 | 2 400 | 2 400 | 1 900 | **3 600** | **III** |
| `ph gleby` | 1 000 | 1 000 | 1 000 | 1 000 | 880 | **1 600** | **III–IV** |
| `wapnowanie drzew owocowych kiedy` | 210 | 70 | 110 | 210 | **260** | **720** | III, wtórnie XI |
| `kreda pastewna` | 2 400 | 2 400 | 1 900 | 1 900 | 1 900 | 2 900 | płaski |
| `wapno na łąki` | 40 | 70 | 70 | 50 | 70 | 70 | **brak sezonu** (30–70) |

**Wniosek, który przewraca uzasadnienie dotychczasowego planu: dla całej rodziny „pole / dawka /
granulat" szczytem roku jest sierpień, nie październik.** Dokument `2026-08-21-sezonowosc-i-kolejnosc-M4.md`
zbudował tabelę „szczytują TERAZ (IX–XI)" **od września w górę** i przez to nie pokazał sierpnia —
miesiąca, w którym powstawał. Październik jest szczytem **wtórnym** i tylko dla `wapno granulowane`
(8 100 wobec 9 900) oraz **pierwszym** dla `wapno palone` i `kiedy wapnować`.

**Co z tego wynika praktycznie:** najlepszy miesiąc roku właśnie mija i nie da się go odzyskać.
Okno VIII–X nie jest już oknem budowania nowych adresów pod szczyt — jest oknem **domknięcia
tego, co gotowe, na szczyt wtórny (X) i na wiosnę**.

## 5.2. Pomiar drugi: na tej domenie nowe adresy nie wchodzą do indeksu

Od 09.07 opublikowaliśmy **dziesięć nowych adresów**. Werdykt GSC 24.08:

| Adres | Opubl. | Werdykt | Kiedy pobrany |
|---|---|---|---|
| `/ile-wapna-granulowanego-na-ha/` | 09.07 | Discovered — not indexed | **nigdy** |
| `/jak-stosowac-wapno-nawozowe/` | 09.07 | Discovered — not indexed | **nigdy** |
| `/wapno-nawozowe-na-trawnik/` | 09.07 | URL unknown | **nigdy** |
| `/higienizacja-osadow-sciekowych-wapnem/` | 09.07 | Discovered — not indexed | **nigdy** |
| `/wapno-do-stabilizacji-gruntow/` | 14.07 | URL unknown | **nigdy** |
| `/wapno-granulowane/` | 06.08 | URL unknown | **nigdy** (świadomie) |
| `/polityka-plikow-cookies-eu/` | 13.08 | URL unknown | **nigdy** |
| `/oswiadczenie-o-ochronie-prywatnosci-eu/` | 13.08 | URL unknown | **nigdy** |
| `/wapno-nawozowe/` | 14.08 | URL unknown | **nigdy** (świadomie) |
| `/wapno-do-stawu/` | 21.08 | URL unknown | **nigdy** |

**Zero na dziesięć w niespełna siedem tygodni.** W tym samym czasie Google crawluje serwis **codziennie**:
`/oferta/` 24.08, `/wapno-do-sadu/` 24.08, `/` 23.08, hub 23.08, `/kontakt/` 23.08, dziesięć kart
produktów 21–23.08, kategorie 16–22.08. **Adresy, które Google już zna, odwiedza co dzień.
Po nowe nie sięga w ogóle.**

To jest najważniejszy wynik tego audytu i on rozstrzyga kolejność planu.
**Publikowanie kolejnych nowych adresów pod szczyt październikowy jest obarczone ryzykiem,
którego dziesięć obserwacji nie pozwala zignorować.** Kanałem, który na tej domenie działa,
jest **dopisywanie treści do adresów już zaindeksowanych** — bo te Google czyta następnego dnia.

## 5.3. Plan — jeden adres, jeden wiersz

Kolejność wynika z trzech kryteriów w tej hierarchii: **(1)** czy adres jest już crawlowany,
**(2)** wolumen razy brak pokrycia zmierzony w GSC, **(3)** odległość do szczytu sezonowego.

### Faza 0 — do 31.08 · odblokowanie tego, co już napisane. **Zero nowych adresów**

| # | Adres | Co zrobić | Fraza wiodąca i popyt | Szczyt | Dlaczego pierwsze |
|---|---|---|---|---|---|
| **0.1** | `/jak-stosowac-wapno-nawozowe/` | linki z huba (jest), `/poradniki/`, kategorii 764 i strony głównej; odświeżenie `post_modified` i cache sitemapy | `kiedy wapnować glebę` 320 (**X–XI 590**) · `kiedy wapnować pole` 90 (**X 260**) · `kiedy siać wapno granulowane` 210 | **X–XI** | 13 455 znaków gotowej treści na jedyną oś ze szczytem październikowym. Hub trzyma tę oś na **36,4** — jest po co |
| **0.2** | `/wapno-do-stawu/` | **zero linków wewnętrznych** — dodać z `/oferta/`, z wpisu 2079, z sześciu kart listingu; menu „Rybactwo" | `wapno do stawu` 390 (III 880) · `jakie wapno do stawu` 90 (III 260) | III | Sierota trzy dni po publikacji. Bez linków ta strona nie istnieje |
| **0.3** | `/wapno-do-stabilizacji-gruntow/` | **zero linków** — dodać z karty #320 i z `/oferta/` | `wapno palone` 2 400 (**X–XI 3 600**) | **X–XI** | Jedyna strona pod największy jesienny klaster, sierota od 14.07. Dziś na `wapno palone kruszone` rankuje **PDF z 2023 roku** (18 wyśw., poz. 5,7) |
| **0.4** | `/jak-stosowac-…/` i `/wapno-nawozowe-na-trawnik/` | przepiąć dwa martwe linki z `/ile-wapna-granulowanego-na-ha/` na `/wapnowanie-gleby/` | — | — | Dług po T-026 |
| **0.5** | `/rybactwo-kat-archiwum/` | rozstrzygnąć term 766: usunąć albo 301 | — | — | Slug roboczy w publicznym adresie, linkowany z `/oferta/` |

### Faza 1 — 01–20.09 · treść na adresach, które Google czyta codziennie

| # | Adres | Fraza wiodąca i popyt | Szczyt | Stan dziś | Termin |
|---|---|---|---|---|---|
| **1.1** | `/wapno-nawozowe-rolnictwo/` | `wapno nawozowe` **1 300** (VIII–X **1 900**) | **X** | poz. **10,9**, crawl 21.08, **3 996 znaków, 3 × H2** | **05.09** |
| **1.2** | `/paszarstwo/` | `kreda pastewna` **2 400** · `kreda pastewna dla bydła` 210 · `wapno dla kur niosek` 210 | płaski | poz. 13,4, crawl 16.08, **3 083 znaki, 1 × H2** | **12.09** |
| **1.3** | `/wapno-hydratyzowane/` | `wapno hydratyzowane` **2 400** (III 3 600) | III | poz. **31,3** przy 172 wyśw., crawl 21.08 | **20.09** |
| **1.4** | `/wapno-do-oczyszczalni/` | `higienizacja osadów ściekowych` 30 · `wapnowanie osadów ściekowych` 20 | XI | poz. 9,5, **CTR 3,97%**, crawl 22.08 — najlepsza kategoria serwisu | **20.09** |

Wszystkie cztery to strony **zaindeksowane i crawlowane w ostatnim tygodniu**. To jedyny kanał,
o którym mamy dowód, że dociera do Google w dniach, a nie w tygodniach.

### Faza 2 — 21.09–31.10 · nowe adresy, warunkowo

**Warunek wejścia: co najmniej jeden adres z Fazy 0 musi zostać pobrany przez Google.**
Kontrola 15.09 (URL Inspection). Jeśli żaden nie zostanie — Faza 2 nie ma sensu w tej postaci
i wracamy z pytaniem, zamiast pisać do szuflady.

| # | Adres | Fraza wiodąca i popyt | Szczyt | Pokrycie dziś | Blokada | Termin |
|---|---|---|---|---|---|---|
| **2.1** | poradnik „Kreda pastewna — dawkowanie dla niosek, bydła i trzody" | `kreda pastewna dla kur` **1 600** · `kreda pastewna dla bydła dawkowanie` 90 | płaski | **zero** — stary adres `/kreda-pastewna/` trzyma poz. 22–33 | — | **30.09** |
| **2.2** | poradnik „Kreda do stawu — dawkowanie i różnica wobec wapna tlenkowego" | `kreda do stawu` **1 300** (**III 2 900**) | III | **zero fraz nad progiem** | — | **10.10** |
| **2.3** | `/czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/` — przebudowa, **ten sam adres** | `wapnowanie stawu` 90 (III 170) · `ile wapna do stawu` 50 | III | zero | zaległy werdykt `noindex` z 18.04 | **10.10** |
| **2.4** | poradnik „pH i odczyn gleby — jak go podnieść" | `ph gleby` **1 000** (III–IV 1 600) · `zakwaszenie gleby` 390 · `odczyn gleby` 260 | III–IV | **zero fraz nad progiem** | — | **20.10** |
| **2.5** | poradnik „Badanie gleby — próbki i odczyt wyniku" | `badanie gleby` **1 000** (**VIII 1 900**, III 1 900) | **VIII i III** | **zero fraz nad progiem** | — | **31.10** |

### Poza oknem VIII–X — z uzasadnieniem, nie z pominięcia

| Pozycja | Decyzja | Dlaczego |
|---|---|---|
| `/wapno-do-sadu/` — treść i zdjęcie 301 | **30.11 zostaje** | Szczyt III (720), wtórny XI (260). Termin daje rozbieg. **Uzasadnienie w rejestrze jest jednak fałszywe** — patrz §6 |
| Spoke „łąki i pastwiska" | **odpuścić w tym roku** | Cały rok 30–70 wyszukań. To nie jest klaster, to szum. 15.12 wypada w dołku (30) |
| Spoke „zboża ozime i rzepak" | **VII 2027** | Blokada `T-067` (źródła IUNG). Okno VIII–IX mija; hub już rankuje na `jakie wapno pod rzepak` i `czy można siać wapno na zboże` |
| Spoke „ziemniaki" | **20.09 zostaje** | `wapno pod ziemniaki` 50 (IX–X 110) — jedyny spoke uprawowy ze szczytem jesiennym. Mały, ale termin trafiony |
| Budownictwo / zaprawy (blok F) | **jako 1.3, nie nowy adres** | `wapno hydratyzowane` 2 400 przy naszej pozycji 31,3 — to jest praca na istniejącej kategorii, nie budowa |
| Strona tonażowa na `/wapno-nawozowe-hurt/` | **przenieść na VII 2027** | Frazy tonażowe szczytują w **VIII** (`wapno granulowane big bag cena` 590, `…cena za tonę` 320). Publikacja 05.10 trafia w opadający zbocze. Dodatkowo wolumen zmierzony niżej niż w rejestrze — §6 |

### Hub `/jakie-wapno-na-pole/` — rekomendacja: **nie budować**

To jedyna pozycja, w której odchodzę od planu z rejestru wprost, więc uzasadnienie osobno.

- Fraza `wapno na pole` (390/mies., **VIII 1 000**) **już ma nasz adres**: `/wapnowanie-gleby/`
  rankuje na nią na **pozycji 2,0**, a na `ile kosztuje wapno na pole` również 2,0
  (dane cienkie — 4 i 2 wyświetlenia — ale kierunek jednoznaczny).
- `jakie wapno na pole` (140/mies.) hub trzyma na **30,7**. To jest **problem treści huba,
  nie brak adresu** — hub ma 17 × H2 i 11 327 znaków, w których tej odpowiedzi nie ma wprost.
- Nowy adres na tę frazę byłby **drugim naszym URL-em na intencję, na której już jesteśmy w TOP3** —
  czyli dokładnie tym, czego zakazuje ADR `2026-08-11-podzial-rol-ads-seo.md`,
  potwierdzony w tym audycie na sześciu frazach (§ETAP 1).
- Szczyt `jakie wapno na pole` to **sierpień (480)**, nie wrzesień. Termin 10.09 trafia już po nim.

**Zamiast huba:** sekcja „Jakie wapno na pole — dobór do gleby i uprawy" **wewnątrz `/wapnowanie-gleby/`**,
czyli na stronie crawlowanej 23.08. Koszt mniejszy, kanał sprawdzony, zero ryzyka kanibalizacji.

---

# §6 — rozbieżności między dokumentami a produkcją

Każda z rozstrzygnięciem. To jest materiał na sprostowania w rejestrze.

## A. Sezonowość — cztery liczby przeczytane źle

**A1. `wapnowanie drzew owocowych kiedy` — „XI to 40" jest nieprawdą.**
Źródło błędu: `docs/seo/2026-08-21-sezonowosc-i-kolejnosc-M4.md` wiersz w §2, przepisany dosłownie
do rejestru (T-083 i T-065). Surowa seria z `data/seo/sezonowosc-klastry-2026-08-21.json`:

```
25-08:70  25-09:110  25-10:210  25-11:260  25-12:110
26-01:170 26-02:320  26-03:720  26-04:260  26-05:140  26-06:40
```

**Listopad to 260, powyżej średniej 210. Wartość 40 to czerwiec** — ostatni element serii,
wzięty za listopad. Konsekwencja: zapis „listopadowego szczytu nie ma" jest odwrotnością pomiaru.
Termin 30.11 nie szkodzi (III to nadal główny szczyt), ale **uzasadnienie trzeba odwrócić**:
publikujemy w listopadzie **dlatego, że listopad jest wtórnym szczytem**, a nie „mimo że go nie ma".

**A2. `wapno granulowane` — „szczytuje w październiku na 8 100" jest nieprecyzyjne.**
Szczytem roku jest **sierpień: 9 900**. Październik (8 100) jest szczytem wtórnym.
Źródło błędu jest metodyczne: tabela z 21.08 miała kolumny IX / X / XI i nie pokazywała sierpnia —
miesiąca, w którym powstawała. Ten sam mechanizm zniekształcił obraz `wapno nawozowe`,
`wapno na pole`, `ile wapna na hektar`, `wapno węglanowe`, `jakie wapno na pole`
i cały klaster tonażowy. **Pełne serie w §5.1.**

**A3. `wapno na łąki` — „szczyt marcowy" to odczyt szumu.**
Seria: `70 70 50 70 30 30 40 70 40 30 30`. Marzec = 70, ale tyle samo mają sierpień, wrzesień
i listopad. Przy takich wartościach nie ma sezonu, jest szum pomiarowy.
Rekomendacja: **zdjąć z planu**, nie przesuwać na 15.12 (grudzień = 30, dołek roku).

**A4. `badanie gleby` szczytuje **także w sierpniu** (1 900, tyle samo co marzec).**
W planie stoi na 15.11 — najdalszym możliwym punkcie od obu szczytów. Nie jest to błąd
odczytu, tylko skutek klasyfikacji „klaster wiosenny", która pominęła sierpień.

## B. Zadania, które stoją na nieaktualnym stanie

**B1. T-079 — „karta #307 nadal opisuje kredę pastewną parametrami wapna tlenkowego".**
**Nieprawda na stronie.** Sprawdzone 24.08 we wszystkich czterech warstwach: render, `post_content`,
`_elementor_data`, atrybuty `pa_*` i meta Rank Math — **zero wystąpień „egzoterm", zero „pH >12"**,
specyfikacja podaje `min. 37% CaO` i dawkowanie `1–2 kg / 100 kg paszy`. Naprawione 15.07
przy naprawie parametrów w czterech warstwach. Wadliwy opis został **w katalogu drukowanym**
(`FAKTY_KLIENTA` §8 pkt 7).
**Rozstrzygnięcie: T-079 traci przedmiot.** Karta ma poprawne parametry, ma cenę i jest
zaindeksowana (132 wyśw., poz. 8,4). Zostaje errata do katalogu — u klienta, nie u nas.

**B2. T-082 — „`wapno … cena za tonę` **490 łącznie**".**
Zmierzone 24.08 osobno, po jednej frazie: `wapno cena za tonę` **50** · `wapno granulowane cena
za tonę` **90** · `wapno na pole cena za tonę` **10** — razem **150**, nie 490.
Do tego cała rodzina tonażowa szczytuje w **sierpniu** (`wapno granulowane big bag cena` VIII 590
wobec średniej 260). Termin 05.10 trafia w opadające zbocze. **Rekomendacja: przenieść na VII 2027.**

**B3. T-077 — „`kreda pastewna jak podawać` 170".**
Zmierzone 24.08: **10**. ⚠️ **Nie traktuję tego jako rozstrzygnięcia** — obie frazy mierzyłem
w batchu zawierającym warianty bliskie (`kreda pastewna dla kur dawkowanie`), a planer Google
grupuje warianty i zeruje pozostałe (pułapka opisana przy T-056). **Do jednego czystego pomiaru
przed pisaniem.** Klaster stoi jednak nie na tej frazie, tylko na `kreda pastewna dla kur` 1 600 —
zadanie zostaje.

**B4. T-013 — „4 z 6 nagłówków, brak CSP i Permissions-Policy".**
Zmierzone `curl -I` 24.08: obecne są `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`,
**`Permissions-Policy`** i `Strict-Transport-Security`. **Brakuje wyłącznie CSP — czyli 5 z 6.**
`Permissions-Policy` dopisano w bloku `# BEGIN AGRIA SECURITY HEADERS` 30.07; wiersz dziennika
opisuje stan sprzed tej zmiany.

**B5. `FAKTY_KLIENTA` §3 — „żaden z 19 produktów nie ma ceny, słowo »cena« w treści w 0/19".**
Nieaktualne od 19.08: **15 z 19 kart ma na froncie `zł/t netto`** (zweryfikowane per URL 24.08).
`_price` puste w 19/19 — ta część zapisu jest nadal prawdziwa i musi taka zostać.

**B6. `data/zrodla/` nie istnieje — potwierdzone.** Blokada T-067 realna. Terminarz
`/jak-stosowac-wapno-nawozowe/` cytuje IUNG-PIB (tab. 8, tab. 18) bez ani jednego pliku w repo.

## C. Domknięcia, które domknęły mniej, niż mówią

**C1. T-026 — scalenie nie objęło dwóch linków.** Wpisy `/jak-stosowac-wapno-nawozowe/`
i `/wapno-nawozowe-na-trawnik/` nadal linkują do wycofanego `/ile-wapna-granulowanego-na-ha/`,
czyli przez 301. Dziennik odnotowuje wyłącznie link zdjęty z huba.

**C2. T-026 — decyzja o `/higienizacja-osadow-sciekowych-wapnem/` nie ma pokrycia w pomiarze.**
Wpis został osobnym adresem, wzmocnionym linkiem z kategorii i karty #320. Stan 24.08:
**werdykt „Discovered — not indexed", nigdy nie pobrany, zero wyświetleń**, podczas gdy kategoria
`/wapno-do-oczyszczalni/` zbiera **całą** intencję osadową (806 wyśw., 32 kliknięcia, CTR 3,97%).
Decyzja jest Janka i zostaje, ale **wiersz w rejestrze powinien mówić, że dowodu skuteczności nie ma**.

**C3. T-032 — trzy adresy poza zakresem reguł.** `/kategoria-produktu/wapno-do-sadu/`,
`…/wapno-nawozowe-hurt/` i `…/rybactwo-kat-archiwum/` oddają **200** (z `noindex`, canonical
wskazujący na adres, który przekierowuje). Reguły objęły pięć kategorii z sitemapy, trzy puste
pominęły. Koszt zerowy w ruchu, trzy linie dopisu.

**C4. T-027 — „duplikat `wp-sitemap.xml` rozwiązał się sam".** Potwierdzone: `wp-sitemap.xml`
oddaje **301 na `sitemap_index.xml`**. Werdykt `/do-pobrania/` nadal `BLOCKED_BY_META_TAG`
z crawla 12.04 — bez zmian.

## D. Rzeczy, których nie ma w żadnym dokumencie

**D1. Osiem z dziewiętnastu kart produktów jest poza indeksem** — sześć „URL unknown",
dwie „Discovered — not indexed", wszystkie w sitemapie od 15.07 lub 19.08, żadnej Google
nigdy nie pobrał. Największa pojedyncza liczba tego audytu.

**D2. Dwie strony są sierotami** — `/wapno-do-stawu/` i `/wapno-do-stabilizacji-gruntow/`
mają **zero linków wewnętrznych** na 22 przeskanowanych stronach. Obie w sitemapie, obie
nieznane Google'owi.

**D3. `/o-firmie/` i `/wsparcie/` mają zaległy werdykt `noindex`** z crawli 20.04 i 12.04 —
ta sama kwietniowa zaległość co `/do-pobrania/`, nigdy nie zinwentaryzowana do końca.
`/wsparcie/` ma dodatkowo **zerową treść** (`post_content` 0 B) i jest linkowana z **każdej**
strony serwisu (22 z 22).

**D4. `/category/poradniki/` — Google sam rozstrzygnął duplikat.** Werdykt:
„Duplicate, Google chose different canonical than user", wybrany canonical to `/poradniki/`.
Adres jest w `category-sitemap.xml`, ma `index, follow` i **pusty `<h1>`**.
Obok niego `/category/zastosowania/` — również indeksowalna, również z pustym H1, „URL unknown".
Sygnalizowane w memory od czerwca, nierozstrzygnięte.

**D5. `/rybactwo-kat-archiwum/` to publiczny adres z roboczym slugiem.** 200, `noindex`,
linkowany z `/oferta/`. Dług wprowadzony 21.08 przy zwalnianiu slugu pod landing.

**D6. `/oferta/` jest w dwóch sitemapach naraz** — w `page-sitemap.xml` z `lastmod 2026-03-24`
i w `product-sitemap.xml` z `lastmod 2026-08-19`. Dwie różne daty tego samego adresu.

**D7. Sześć leadów z formularza w 90 dniach** (`agria_inquiry`, dane pierwszej strony,
niezależne od zgód): 03.07 · 16.07 · 27.07 · 28.07 · 05.08 · **13.08 — ostatni**.
Kampania ruszyła 13.08 i przez jedenaście dni nie przyniosła ani jednego zgłoszenia formularzowego
ani konwersji w Ads (215 kliknięć, 396,18 zł). To nie jest wniosek o kampanii — telefon jest
głównym kanałem, a jego pomiar naprawiono dopiero 24.08 — ale liczba należy do obrazu.

**D8. Klaster geograficzny na stronie głównej.** `/` zbiera ~1 000 wyświetleń na frazach
typu `wapno kraków`, `wapno małopolskie`, `wapno sosnowiec`, `wapno tarnowskie góry`,
`wapno nawozowe włocławek` — wszystkie na pozycjach **18–36, zero kliknięć**. Pojedyncze
frazy mają 10–30 wyszukań/mies., więc to długi ogon wielu miast.
**Nie rekomenduję stron miejskich** (ryzyko cienkiej treści na skalę), ale zapisuję pomiar,
bo to jedyny nieobsłużony popyt o czterocyfrowej liczbie wyświetleń.

**D9. Zdjęcie na `/wapno-do-stawu/` i `/czy-wapnowac-…/` przedstawia tarasy ryżowe.**
Obejrzane 24.08: azjatycki krajobraz, stożkowy kapelusz, dom na palach, pola ryżowe.
Podpis mówi „wapnowanie stawu karpiowego". Plik `2026/03/wapnowanie-stawow-karpiowych.jpg`
wisi na **obu** stronach (na wpisie 7 wystąpień). Sygnalizowane w rejestrze przy T-056,
tu potwierdzone i rozszerzone o drugą stronę.

**D10. `dolomit` (6 600/mies.) nie jest frazą do przechwycenia kartą produktu.**
SERP 24.08: Wikipedia #1 (minerał), dalej treść ogrodnicza, kruszywo Holcim, sklepy detaliczne
i **suplement diety w tabletkach**. Intencja jest rozszczepiona. Zapis w `FAKTY_KLIENTA` §3
(„Dolomit boli najbardziej — 6 600 wyszukań") przecenia dostępność tego wolumenu.
Adresowalna jest wąska część: `dolomit nawóz`, `wapno dolomitowe`. Karta #302 jest przy tym
**„Discovered — not indexed" i bez ceny**.

## E. Twierdzenia z promptu, które pomiar koryguje

**E1. „Crawl na tej domenie bywa liczony w tygodniach" — nie.** Google crawluje agria.pl
**codziennie**: `/oferta/` i `/wapno-do-sadu/` 24.08, `/`, hub i `/kontakt/` 23.08, dziesięć
kart produktów 21–23.08. Problem jest selektywny — crawluje wyłącznie to, co już zna (§5.2).

**E2. „Na »wapno do stawu« trzy z siedmiu wyników TOP7 to posty z Facebooka".**
Zmierzone 24.08 (DataForSEO, PL/pl, desktop, TOP10): **dwa** wyniki organiczne z Facebooka
(pozycje 7 i 8), plus featured snippet na 1, Allegro na 3, OLX na 10 i dwa sklepy.
**Teza się utrzymuje** (SERP merytorycznie pusty, konkurencja najsłabsza w portfelu),
liczba jest inna.

**E3. „Landing o stawach żyje pod osobnym adresem" — potwierdzone i rozszerzone.**
`/wapno-do-stawu/` to strona (ID 2796), nie kategoria; term 766 ma slug `rybactwo-kat-archiwum`
i 0 produktów; `/wapno-do-stawow/` oddaje 404. Pełne rozplątanie w §ETAP 1.

---

# §7 — propozycja przepisanej sekcji treściowej rejestru

**Nie wprowadzona.** `docs/REJESTR_ZOBOWIAZAN.md` jest nietknięty — poniżej propozycja
do akceptu Janka, zgodnie z zakresem zlecenia.

## Co się zmienia wobec stanu z 24.08 rano

| Było | Ma być | Powód |
|---|---|---|
| 14 pozycji treściowych, kolejność od stawu | **5 pozycji odblokowujących (Faza 0), potem 4 na istniejących kategoriach, potem 5 nowych adresów warunkowo** | 0/10 nowych adresów pobranych w 7 tygodni; adresy zaindeksowane crawlowane codziennie (§5.2) |
| T-073 hub `/jakie-wapno-na-pole/`, 10.09 | **⛔ nie budować** — sekcja w `/wapnowanie-gleby/` | hub rankuje na `wapno na pole` na poz. 2,0; drugi URL łamie ADR 11.08 |
| T-075 spoke łąki, 15.12 | **⛔ zdjąć z planu** | 30–70 wyszukań cały rok, brak sezonu; 15.12 to dołek |
| T-082 strona tonażowa, 05.10 | **przenieść na VII 2027** | klaster tonażowy szczytuje w VIII; wolumen 150, nie 490 |
| T-079 karta #307 (zablokowana) | **⛔ zamknąć — brak przedmiotu** | parametry poprawne na stronie od 15.07 we wszystkich 4 warstwach |
| T-085 budownictwo jako nowy landing/rozbudowa | **rozbudowa kategorii `/wapno-hydratyzowane/`, 20.09** | kategoria zaindeksowana i crawlowana, poz. 31,3 przy 2 400/mies. |
| T-084 wzmocnienie `/wapno-do-stabilizacji-gruntow/`, 10.10 | **najpierw linki (Faza 0, do 31.08)**, treść później | strona jest sierotą i nieznana Google — treść bez linków nie zadziała |
| — | **nowa pozycja: 8 kart produktów poza indeksem** | D1 |
| — | **nowa pozycja: sieroty — 2 strony bez linków wewnętrznych** | D2 |
| — | **nowa pozycja: term 766 `rybactwo-kat-archiwum` do rozstrzygnięcia** | D5 |
| — | **nowa pozycja: `/kreda-malarska/` bez title i opisu, Discovered — not indexed** | ETAP 1 |
| — | **nowa pozycja: schema `Product` bez `offers` w 19/19** | ETAP 2 |

## Proponowana treść sekcji „🔴 Teraz — treść"

```
| # | ID    | Zadanie                                                    | Fraza wiodąca i popyt                       | Termin | Uwaga |
|---|-------|------------------------------------------------------------|---------------------------------------------|--------|-------|
| 1 | T-089 | Linki do sierot: /wapno-do-stawu/, /wapno-do-stabilizacji-gruntow/ | wapno palone 2 400 (X–XI 3 600)      | 28.08  | zero linków wewnętrznych, obie nieznane Google |
| 2 | T-090 | /jak-stosowac-wapno-nawozowe/ — linki + odświeżenie lastmod | kiedy wapnować glebę 320 (X–XI 590)         | 28.08  | 13 455 zn. gotowej treści, nigdy nie pobrana |
| 3 | T-091 | Dwa martwe linki po scaleniu T-026                          | —                                           | 28.08  | dług po T-026 |
| 4 | T-092 | Opis kategorii /wapno-nawozowe-rolnictwo/                    | wapno nawozowe 1 300 (VIII–X 1 900)         | 05.09  | poz. 10,9; 3 996 zn., 3 × H2; crawl 21.08 |
| 5 | T-078 | Opis kategorii /paszarstwo/                                  | kreda pastewna 2 400                        | 12.09  | 3 083 zn., 1 × H2; crawl 16.08 |
| 6 | T-074 | Spoke ziemniaki                                              | wapno pod ziemniaki 50 (IX–X 110)           | 20.09  | jedyny spoke ze szczytem jesiennym |
| 7 | T-085 | Kategoria /wapno-hydratyzowane/ — przepisanie pod frazę       | wapno hydratyzowane 2 400 (III 3 600)       | 20.09  | poz. 31,3; blok F z maila do Kasjana |
| 8 | T-093 | /wapno-do-oczyszczalni/ — wchłonięcie merytoryki poradnika    | higienizacja osadów ściekowych 30           | 20.09  | najlepszy CTR kategorii (3,97%) |
|   |       | ── KONTROLA 15.09: czy Faza 0 została pobrana ──              |                                             |        | warunek wejścia w nowe adresy |
| 9 | T-077 | Poradnik „Kreda pastewna — dawkowanie"                        | kreda pastewna dla kur 1 600                | 30.09  | rozkład płaski |
|10 | T-071 | Poradnik „Kreda do stawu"                                     | kreda do stawu 1 300 (III 2 900)            | 10.10  | zero pokrycia |
|11 | T-070 | Przebudowa /czy-wapnowac-…-stawy-karpiowe/                    | wapnowanie stawu 90 (III 170)               | 10.10  | ten sam URL; zaległy noindex z 18.04 |
|12 | T-080 | Poradnik „pH i odczyn gleby"                                  | ph gleby 1 000 (III–IV 1 600)               | 20.10  | zero pokrycia |
|13 | T-081 | Poradnik „Badanie gleby"                                      | badanie gleby 1 000 (VIII 1 900, III 1 900) | 31.10  | dwa szczyty, nie tylko wiosenny |
|14 | T-083 | Landing /wapno-do-sadu/ + zdjęcie 301 + menu Sadownictwo      | wapnowanie drzew owocowych kiedy 210 (III 720, XI 260) | 30.11 | XI jest wtórnym szczytem — korekta A1 |
```

**Pozycje techniczne do dopisania** (poza sekcją treściową): 8 kart poza indeksem ·
`/kreda-malarska/` bez `rank_math_title` i opisu · term 766 · `offers` w schemacie 19 kart ·
trzy reguły `/kategoria-produktu/*` · `/wsparcie/` pusta i linkowana z 22 stron ·
`/category/poradniki/` i `/category/zastosowania/` w sitemapie z pustym H1.

**Pozycje do przeniesienia poza okno:** T-082 (VII 2027) · T-076 zboża ozime (VII 2027, blokada T-067).
**Do unieważnienia:** T-073 (hub pole) · T-075 (łąki) · T-079 (karta #307 — brak przedmiotu).

---

# Co zrobić najpierw — trzy zdania

1. **Do 31.08 nie publikować nic nowego.** Podlinkować dwie sieroty i terminarz, przepiąć dwa
   martwe linki, odświeżyć `post_modified` i cache sitemapy. Koszt: kilka godzin. To jedyne
   zadania, w których wiemy, że efekt zależy od nas.
2. **We wrześniu pisać na czterech kategoriach, które Google czyta codziennie**, zamiast budować
   piąty i szósty nowy adres, których od siedmiu tygodni nie pobiera.
3. **15.09 sprawdzić URL Inspection dla Fazy 0.** Jeśli żaden adres nie zostanie pobrany,
   problem nie leży w treści ani w linkowaniu i trzeba wrócić z pytaniem, a nie z kolejnym artykułem.

---

**Wykonane pomiary bez zmian na produkcji.** Zero zapisów do bazy, zero edycji plików,
zero zgłoszeń do Indexing API, zero publikacji. Koszt zewnętrzny: **0,19 USD** (DataForSEO).
Dane surowe (w repo, nie w `tmp/`): `data/seo/audyt-2026-08-24/` — `sweep.tsv` (kody, robots, canonical),
`gsc_pages.json` i `gsc_pq.json` (GSC 90 dni), `inspect.json` (66 werdyktów URL Inspection),
`htaccess.txt`, `vol.json` i `vol2.json` (DataForSEO), `serpres.json` (SERP), `links.tsv` (graf linków wewnętrznych).
