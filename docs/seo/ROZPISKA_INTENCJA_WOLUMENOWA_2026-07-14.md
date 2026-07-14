# ROZPISKA — stan faktyczny vs plan SEO, intencja wolumenowa, sezon

> Data: 2026-07-14. Powód: audyt po zgłoszeniu Janka („landing wapno nawozowe hurt przekierowuje na /oferta/").
> Wszystkie liczby zweryfikowane na żywo: GSC API, DataForSEO (SERP live + Labs), baza produkcyjna (MCP), `.htaccess` (FTP), curl na produkcji.

---

## 1. Zgłoszenie: co się stało z „wapno nawozowe hurt"

**Fakt:** `.htaccess` linia 25 — `RewriteRule ^wapno-nawozowe-hurt/?$ /oferta/ [R=301,L]`. Dodane 2026-07-08 (commit `fe3bdd7`, migracja taksonomii). Linia 26 robi to samo z `/wapno-do-sadu/`.

**Czym to było:** NIE landingiem. Archiwum kategorii WooCommerce „Hurtownie" (term 769, slug `wapno-nawozowe-hurt`) z doklejonym opisem SEO. Ta kategoria była *przyczyną* problemu, który migracja naprawiała (Premmerce brał ją jako primary → Agrobielik siedział pod `/wapno-nawozowe-hurt/…`). Po zdjęciu „Hurtowni" z produktów archiwum ma `count=0` → 301.

**Skala straty — dane, nie odczucia:**

| metryka | wartość |
|---|---|
| `/wapno-nawozowe-hurt/` w GSC, 90 dni | **1 klik**, 56 impresji, śr. poz. 22,6 |
| fraza „wapno nawozowe hurt" w GSC, 90 dni | **0 impresji** |
| wolumen „wapno nawozowe hurt" (DataForSEO) | **poniżej progu mierzalności** (<10/mies.) |
| pozycja w SERP (DataForSEO live) | potwierdzona, top-10 — ale na frazie bez wolumenu |

**Wniosek:** ranking-widmo. Pozycja 4 na frazie, której nikt nie wpisuje — przez 3 miesiące dowiozła 1 użytkownika.

**Realna strata z tego samego ruchu:** `/wapno-do-sadu/` (pozycja 11, fraza **30/mies.**) też poszło 301 → `/oferta/`. Mierzalne, choć małe.

**Bilans całej migracji (GSC, cała witryna):** przed 3,9 klik/dzień → po **4,3 klik/dzień**; śr. pozycja 13,2 → **11,7**. Produkty przekierowały się 1:1 i zbierają na nowych URL-ach. Migracja jako całość nie zaszkodziła.

**Błąd, który realnie popełniono:** ADR z 2026-07-08 zakładał, że w miejsce znikających archiwów wchodzą landingi per segment. 301 poszło, landingi nie powstały. Zła kolejność.

---

## 2. Prawdziwa diagnoza: nie mamy ani jednej strony komercyjnej

**agria.pl rankuje dziś w top-50 na 6 fraz. Wszystkie 6 to poradniki:**

| poz. | vol | fraza | URL |
|---|---|---|---|
| 14 | 720 | ile wapna na hektar | `/wapnowanie-gleby/` |
| 17 | 720 | ile wapna na ha | `/wapnowanie-gleby/` |
| 20 | 390 | wapń skorygowany kalkulator | `/kalkulator-wapnowania/` |
| 24 | 480 | ile wapna granulowanego na ha | `/wapnowanie-gleby/` |
| 24 | 480 | ile wapna granulowanego na hektar | `/wapnowanie-gleby/` |
| 28 | 210 | wapno bielik | `/` |

Zero stron pod frazy komercyjne. **Od startu współpracy nie powstała ani jedna nowa strona typu `page`** (najnowsza: 2026-03-20).

### Porównanie z Biovitą (wzorzec wskazany przez Janka)

| | biovita.com.pl | agria.pl |
|---|---|---|
| frazy w rankingu | **109** | **6** |
| pozycje 1 / 2–3 / 4–10 | 5 / 17 / 14 | 0 / 0 / 0 |
| backlinki / domeny odsyłające | 181 / 99 | **339 / 108** |

**AGRIA ma mocniejszy profil linków od Biovity i przegrywa 109:6.** Przepaść nie bierze się z autorytetu domeny — bierze się z architektury treści.

Biovita jest **#1 na „wapno nawozowe"** (1 300/mies., szczyt 6 600 w sierpniu) stroną `biovita.com.pl/pl/16-wapno-nawozowe.html`, która ma: ~200 słów, brak H1 (tylko H2), zero schema.org, brak ceny, brak koszyka, zepsutą sitemapę.

**Dowód kluczowy: brak koszyka NIE blokuje rankingu.** Google nie wymaga transakcji — wymaga zgodności typu strony z SERP-em.

*Korekta do tezy wyjściowej:* Biovita jednak trafia do detalu (worki 5/10/20 kg z EAN, sklepy ogrodnicze, Ceneo). To hurtownia ogrodnicza, nie konkurent AGRII w wapnie rolniczym. Ale wniosek operacyjny stoi: rankują landingiem produktowym bez sprzedaży online.

---

## 3. Jak naprawdę łapie się intencję wolumenową

**Kluczowa korekta założenia.** Intencji „poważne tonaże" **nie łapie się frazą „hurt"** — nikt jej nie wpisuje (0 impresji, 0 wolumenu). Rolnik z 200 ha i działkowiec wpisują **tę samą frazę**: „wapno nawozowe", „wapno granulowane".

Segregację robi **landing, nie fraza**:
- parametry techniczne (typ wg rozporządzenia, %CaO, %MgO, reaktywność, granulacja),
- formy dostawy: **luz 24 t / big-bag 1000 kg**, własna flota 3–24 t, dwa magazyny,
- CTA „zapytaj o ofertę / podaj tonaż" — **zero koszyka, zero ceny za worek**,
- brak opakowań detalicznych w komunikacie.

Detalista odbija się sam. Rolnik całopojazdowy zostaje. To jest dokładnie model, który działa u Biovity — z tą różnicą, że my kierujemy go w górę rynku, nie w dół.

**Kontra-fakt do rozwiązania:** STR-02 (poprawka Pawła, wdrożona 2026-06-29) **zdjęła formy dostawy, opakowania i MOQ z 19 kart produktów i z FAQ**. Cytat: *„czasami nawet małe ilości możemy wysyłać, a taki zapis nas ogranicza"*. Skutek: na agria.pl nie ma dziś **ani jednego sygnału**, że AGRIA wozi luzem 24 t własną flotą. Jedyny sygnał wolumenowy został świadomie usunięty. **Do uzgodnienia z Pawłem** — sprzeczność między „nie ograniczajmy się" a „chcemy poważnych klientów".

---

## 4. Sezonowość — okno zamyka się teraz

Krzywa „wapno nawozowe" (DataForSEO, 8 lat): dołek czerwiec (~880) → **szczyt sierpień–październik** (historycznie 4 400–6 600). Wapnowanie pożniwne.

**Dziś: 14 lipca. Do szczytu 2–6 tygodni. Indeksacja + rozgrzanie nowej strony zajmuje mniej więcej tyle samo.** To ostatni moment, żeby cokolwiek zdążyło zadziałać w tym sezonie.

### Gdzie realnie leżą pieniądze (wszędzie AGRIA ma fizyczny produkt)

| fraza | vol/mies. | szczyt sezonowy | mamy stronę? |
|---|---|---|---|
| wapno granulowane | 5 400 | **14 800** (sie) | nie |
| wapno palone | 2 400 | 9 900 (paź) | nie |
| wapno magnezowe | 2 400 | 8 100 (sie) | nie |
| wapno hydratyzowane | 2 400 | 3 600 (mar) | nie — Bielik jest kartą produktu |
| wapno nawozowe | 1 300 | 6 600 (sie) | nie — **tu stoi Biovita #1** |
| kreda nawozowa | 1 000 | 3 600 (mar) | nie |
| wapnowanie gleby | 1 000 | 3 600 (sie) | **tak** (poradnik, działa) |
| wapno nawozowe hurt | ~0 | — | była, zdjęta |

---

## 5. Dług z planu SEO (obiecane — niezrobione)

**Landingi:**
1. **LP „wapno do stabilizacji gruntów"** — treść, meta i schema **gotowe w repo od 2026-06-15** (`LP_STABILIZACJA_GRUNTU_2026-06-15.md`). Fraza 720/mies., **najwyższy CPC w projekcie ($2,13)**. Blokada „brak dostępu do WP Admin" przestała być prawdziwa w czerwcu (MCP write + FTP). Miesiąc leżenia bez powodu.
2. LP Rybactwo/stawy — zero. Własna strategia z 08.07 nazywa to „wysoka szansa (luka)". Regres: `/wapno-do-stawow/` → 301.
3. LP Oczyszczalnie — istnieje jako *post* (`/higienizacja-osadow-sciekowych-wapnem/`), poza menu, bez huba segmentowego.
4. `LANDING_PAGES_OUTLINES.md` — obiecany plik, nie istnieje.

**On-page (cały KROK 4 strategii nietknięty):**
5. **Meta na stronach statycznych: 0 z 6.** RankMath ma dane wyłącznie na stronie głównej. `/kalkulator-wapnowania/` (rankuje #20 bez żadnej optymalizacji!), `/oferta/`, `/o-firmie/`, `/poradniki/`, `/do-pobrania/`, `/kontakt/`. Status w planie z 20.05: P0, „pierwszy konkretny krok wdrożeniowy".
6. **Bielik #309** pod „wapno hydratyzowane" (2 400 — największa fraza portfolio) — on-page niezrobiony; w karcie nadal sprzeczność **72% vs 90% CaO**.
7. **Dolomit #302** (6 600) — zmieniono tylko URL.
8. Literówki w 8 nazwach produktów = H1 (`weglanowe`, `zawierajace`) — P0/P1 od maja.
9. SKU `null` na 19/19. `pa_agria-ph` #320 = „>16" (fizycznie niemożliwe). „35 lat" → „37 lat" w meta #307/#319.

**Techniczne (nowe, wykryte dziś):**
10. **Sitemapa produktów zawiera stare URL-e** — wszystkie 19 wpisów to `/wapno-nawozowe-hurt/…` i `/wapno-do-sadu/…`, czyli 301-ki od 8 lipca. Cache RankMath nieodświeżony. Karmimy Google mapą przekierowań. **P0.**
11. **Kategorie produktowe nie są w sitemapie** — `category-sitemap.xml` zawiera wyłącznie `/category/poradniki/`. Canonicale na kategoriach są poprawne (self-canonical), ale Google ich nie dostaje.
12. `/cart/` w sitemapie. Duplikacja `/category/poradniki/` vs `/poradniki/`.

**Rozjazd strategii z egzekucją:**
13. Poradnik **„wapno nawozowe na trawnik"** (opublikowany 09.07) celuje we frazę **jawnie wykluczoną** przez nasz własny `ONPAGE_PLAN` §A4 jako „konsumenckie/lifestyle, poza pozycjonowaniem B2B surowcowym". Opublikowany mimo to.
14. `SEO_STRATEGIA_POD_WYNIK` traktuje model B2B jako **wymówkę**, nie kierunek: *„AGRIA nie jest w top-8 na żadną i krótkoterminowo tam nie wygra (katalog B2B «zapytaj o ofertę», słaba domena)"*. Wszystkie 6 lane'ów ROI to lane informacyjne. Dane obalają tę tezę: domena jest **silniejsza od Biovity**, a Biovita stoi #1 z katalogiem bez cen.

---

## 6. Proponowana kolejność (pod sezon)

**Blok 0 — dni, nie tygodnie (odblokowanie, zero ryzyka):**
- odświeżenie sitemapy (P0 — obecnie same 301),
- wdrożenie **gotowej** LP stabilizacji gruntu (leży od miesiąca),
- meta na 6 stronach statycznych,
- `product_cat` do sitemapy.

**Blok 1 — landingi komercyjne (rdzeń, pod szczyt sierpniowy).** Typ strony = produktowy landing kategorii, wzorzec Biovity, ale w górę rynku:
`/wapno-nawozowe/` · `/wapno-granulowane/` · `/wapno-palone/` · `/wapno-hydratyzowane/` · `/wapno-magnezowe/` · `/kreda-nawozowa/`
Każdy: exact-match slug/title/H1 + tabela parametrów + formy dostawy (luz 24 t / big-bag) + CTA „zapytaj o ofertę, podaj tonaż". Bez ceny, bez koszyka.

**Blok 2 — segmenty:** `/wapno-do-stawow/`, hub oczyszczalni (podpiąć istniejący post), sadownictwo.

**Blok 3 — warstwa informacyjna** (to, co już działa): rozbudowa `/wapnowanie-gleby/` + `/kalkulator-wapnowania/`. Tu SERP nagradza treść i **Biovita nie istnieje** — wolne pole.

**Do decyzji Janka:** czy odtwarzamy `/wapno-do-sadu/` i `/wapno-nawozowe-hurt/` pod starymi URL-ami (ratunek pozycji w oknie 301), czy budujemy nową architekturę od zera i stare adresy zostawiamy jako 301 do właściwych landingów.

**Do uzgodnienia z Pawłem:** przywrócenie sygnału logistycznego (luz 24 t, big-bag, własna flota) — zdjętego przez STR-02 — w formie, która nie zamyka drogi mniejszym zamówieniom.
