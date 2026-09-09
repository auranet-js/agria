# T-117 — dwie karty granulowane, treść pod frazy z popytem

> **Projekt:** `agria` · **Zakres:** ryczałt R · **Termin:** 20.09.2026
> **Karty:** `#314 weglanowe-granulowane` · `#317 weglanowe-magnez-granulowane`
> **Zazębienie:** duplikat tytułu #317 (pozycja z T-116) — **robisz w tym samym przebiegu, jednym zapisem**
> **Pomiar wyjściowy:** `data/seo/2026-09-09-serp-i-indeksacja-przed-T116.md`, SERP-y `data/seo/2026-09-09-serp-*.json`
> **Wzorzec wykonania:** T-092 (`data/T-092/wdrozenie-2026-09-04.md`) i T-078 (`data/T-078/wdrozenie-2026-09-08.md`)
>
> **O co chodzi:** dwie karty mają razem 898 wyświetleń i **jedno kliknięcie** w 28 dni. Nie są cienkie
> (6 364 i 6 005 znaków) ani zduplikowane (pomiar 09.09: podobieństwo do reszty portfela 0,31 — tyle,
> co szablon). Stoją nisko, bo treść nie odpowiada na to, o co ludzie pytają.

---

## 0. Czego NIE zakładać

Dziewięć rzeczy zmierzonych 09.09 albo wcześniej. Każda już raz kosztowała sesję.

1. **Zapis idzie przez MCP `update_post_content`, nie przez WP-CLI.** `term update` i `post update`
   bez zalogowanego użytkownika przepuszczają treść przez `wp_filter_kses` i wycinają tabele oraz
   nagłówki — produkcja miała przez chwilę gorszy opis niż przed zmianą (T-092). Po zapisie
   **porównaj MD5 z plikiem źródłowym**.
2. **Obie karty renderują z `post_content`** — sprawdzone 09.09, żadna nie ma `_elementor_data`.
   To odróżnia je od kart 307 / 310 / 320. Edycja `post_content` wystarczy.
3. **Nie zeruj `_elementor_element_cache` przez `a:0:{}`** — Elementor czyta to jako poprawny pusty
   render i wygasza treść na produkcji (incydent 30.07). Po zmianie: `wp elementor flush-css` + `wp cache flush`.
4. **`?cb=` nie jest weryfikacją.** Po WP Rocket omija cache i pokazuje wersję, której użytkownik nie
   dostaje. Pomiar: rozgrzewka jednym żądaniem, potem odczyt na czystym adresie. Do porównania
   „z Rocketem / bez" służy `?nowprocket=1`.
5. **`_price` obu kart zostaje puste.** Tryb katalogu, ADR `2026-08-19-dwie-warstwy-cen`. Kwota żyje
   wyłącznie w treści, schema `offers` budowana z treści — nie z `_price`, nie z wariantów.
6. **Ceny ofertownika nie wychodzą na front w żadnej formie.** Kwoty poniżej pochodzą z cennika
   Pawła 07.08 i są cenami **za towar, bez transportu**.
7. **Dawkę na hektar trzymasz krótko, z linkiem do huba.** `/wapnowanie-gleby/` trzyma
   `ile wapna na hektar` na poz. 7,7 — nie budujemy sobie konkurencji (ta sama zasada co w T-092).
8. **Po wdrożeniu zgłaszasz obie karty ręcznie w panelu GSC**, nie przez Indexing API. Zmierzone 09.09:
   panelowe „Poproś o zindeksowanie" wprowadziło dwie karty do indeksu w kilkanaście minut, podczas
   gdy Indexing API (trzy próby, T-094) i linkowanie wewnętrzne (16 dni, Faza 0) nie zadziałały.
   ⚠️ Panel ma **limit kilku zgłoszeń na dobę** — 09.09 wyczerpany, planuj to na osobny dzień.
9. **Parametry wyłącznie z kart producentów** (Grankal, Celiny/Hochel, Lhoist) i z atrybutów karty.
   17 kart leży publicznie na `/do-pobrania/`. Nic z rozumowania.

---

## 1. Stan wyjściowy — zmierzony, nie zakładany

| | **#314** `weglanowe-granulowane` | **#317** `weglanowe-magnez-granulowane` |
|---|---|---|
| GSC 28 dni (09.08–05.09) | 511 wyśw. → **1 klik** (0,20%), poz. **18,9** | 387 wyśw. → **0 klik**, poz. **25,5** |
| skład | **min. 50% CaO** | **min. 31% CaO, min. 16% MgO** |
| frakcja | granulat **3–6 mm** | granulat **3–6 mm** |
| reaktywność | ~70–90% | ~70–90% |
| producent | Celiny (Hochel) + **Grankal** + Lhoist | **Grankal** |
| marka handlowa | Calcifertil | — |
| opakowania | big-bag 500 i 600 kg, worek 25 kg | big-bag 600 kg, worek 25 kg |
| **cena (cennik Pawła 07.08)** | big-bag **350 zł/t** · worek 25 kg → **380 zł/t** | big-bag **370 zł/t** · worek 25 kg → **410 zł/t** |
| treść dziś | 6 364 znaki | 6 005 znaków |
| meta | title 56 znaków | ⚠️ **title identyczny jak #318** |

**Na czym realnie zbierają wyświetlenia** (GSC 28 dni, per strona):
**#314** — `wapno węglanowe` 85 (poz. 33), `wapno nawozowe węglanowe` 74 (17,9),
`wapno węglanowe granulowane` 45 (17,0), `wapno węglanowe kredowe` 30, `wapno węglowe` 30,
`wapno nawozowe węglanowe granulowane` 28, `wapno węglanowe granulowane cena` 6 (10,8).
**#317** — te same frazy z pozycji **31–49**, plus `wapno magnezowe` 23 (48,9),
`wapno nawozowe węglanowo-magnezowe` 17 (37,5), `wapno węglanowe z magnezem` 3 (11,3).

---

## 2. Popyt — pomiar DataForSEO 09.09, `location_code 2616`

**Największe odkrycie i powód, dla którego #317 jest ważniejsza, niż wyglądała:**

| fraza | /mies | IX | X |
|---|---|---|---|
| **`wapno magnezowe granulowane`** | **880** | **1 300** | **1 300** |
| `wapno granulowane cena` | 480 | 720 | 590 |
| `wapno granulowane big bag` | 260 | 390 | 320 |
| `wapno nawozowe cena za tonę` | 140 | 210 | 170 |
| `wapno granulowane z magnezem` | 140 | 210 | 210 |
| `wapno w workach` | 90 | 110 | 90 |
| `wapno granulowane 25 kg` | 70 | 110 | 70 |
| `wapno big bag` | 70 | 110 | 70 |
| `wapno granulowane czy sypkie` | 50 | 70 | 50 |
| `wapno granulowane dawkowanie` | 40 | 50 | 70 (**CPC 1,28**) |
| `wapno nawozowe luzem` | 40 | 70 | 50 |
| `wapno węglanowe granulowane cena` | 30 | 40 | 20 |
| `wapno sypkie czy granulowane` | 10 | 20 | 20 |

**#317 stoi na 41–49 pozycji na frazie o wolumenie 880, we wrześniu i październiku 1 300.**
To jest najgrubszy pojedynczy zasób w tym zadaniu.

**Producenci — sprawdzone, bo pytałeś:**

| fraza | /mies | co z tym |
|---|---|---|
| `nordkalk wapno` | **480** | nie dotyczy tych kart (to Agrobielik i Bielik) |
| `kopalnia jażwica` | 390 | ⚠️ **nie dotyczy tych kart** (to #318) i wygląda na zapytanie nawigacyjne o zakład, nie o wapno — nie budować na tym treści bez sprawdzenia SERP-u |
| `kopalnia celiny` | 320 | jw. — Celiny to jeden z trzech producentów #314 |
| **`grankal`** | **110** (IX 210) | **jest popyt na samą markę, i to producent obu kart** |
| `wapno grankal` | 20 | — |
| `wapno lhoist` | 20 | — |
| `wapno celiny` · `calcifertil` | 10 · 10 | — |
| `wapno węglanowe grankal` · `hochel wapno` · `wapno industria` | **0** | nie wchodzą |

**Zero wolumenu, nie wchodzą do treści jako frazy:** `wapno dostawa`, `wapno z dostawą`,
`wapno nawozowe transport`, `wapno rozsiew`, `usługa rozsiewu wapna`, `wapno nawozowe 500 kg`,
`czy wapno granulowane trzeba wymieszać`. **Transport i rozsiew opisujemy, bo to realne pytanie
kupującego, ale nie jako nagłówki pod frazę** — nikt ich tak nie szuka.

**SERP `wapno granulowane` (mobile, 09.09): BEZ AI Overview.** Pierwszy wynik organiczny to sklep
Rolmat z big-bagiem 500 kg i kwotą, dalej OLX, osadkowski, tygodnik-rolniczy, florovit, agrosklad.
Pytania z „ludzie pytają też": *kiedy stosować wapno granulowane · ile kosztuje 1 tona wapna
granulowanego · które wapno lepsze: sypkie czy granulowane · ile kg wapna granulowanego na hektar ·
czy wapno granulowane trzeba wymieszać z ziemią · jakie wapno na szybkie odkwaszenie gleby*.
Na `wapno magnezowe` **AI Overview już jest**, a nad wynikami stoją OLX i Rolmat.

---

## 3. Decyzje Janka z 09.09 — wiążące

1. **Kwoty wchodzą do treści OBU kart, i to do nagłówków** — nie tylko w akapicie. Wzorzec kart
   #315 i #319. Każda kwota ze swoim warunkiem dostawy i zdaniem „Podane kwoty dotyczą samego towaru,
   bez transportu". `_price` zostaje puste.
2. **Nazwy producentów wolno wymieniać w treści** — „są w katalogu przecież". Dotyczy Grankalu,
   Celin (Hochel), Lhoist. Marka **Calcifertil** dla #314 też. ⚠️ To **nie zmienia** statusu Nordkalku
   z T-040 — tam nadal czekamy na potwierdzenie autoryzacji, ale tych dwóch kart to nie dotyczy.
3. **Oś merytoryczna: granulat kontra sypkie.** Dlaczego granulat, kiedy się opłaca mimo wyższej ceny
   za tonę, rozsiewacz i brak pylenia, precyzja dawki. ⚠️ **Uwaga do wykonania:** sam klaster
   „granulat vs sypkie" to tylko ~60 wyszukań/mies. Oś porządkuje treść i odpowiada na PAA,
   ale **ruch przyjdzie z ceny, formy dostawy i magnezu** (razem ponad 1 800). Zbuduj tekst tak,
   żeby porównanie form było ramą, a nagłówki niosły frazy z popytem.

---

## 4. Kolejność pracy

1. **Backup** — `db_export` tabel `posts` i `postmeta` przed pierwszym zapisem. Jeden zrzut na obie karty.
2. **Baseline GSC do `data/T-117/`** — `python3 scripts/gsc_baseline.py --dni 28 --out data/T-117/baseline-gsc-2026-09-XX.json /wapno-nawozowe-rolnictwo/weglanowe-granulowane/ /wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/`
3. **Crawl kontrolny przed** — `python3 scripts/crawl_kontrolny.py --json data/kontrole/2026-09-XX-przed-T117.json`
4. **#317 najpierw** — ma frazę o wolumenie 880/1 300 i zero kliknięć, więc największy zwrot.
   W jednym zapisie: treść **oraz** nowy `rank_math_title` usuwający duplikat z #318.
   Tytuł ma odróżniać granulat od odmiany sypkiej i zmieścić się poniżej **561 px**.
5. **#314** — ta sama struktura, oś cenowa i formy dostawy, bez magnezu.
6. **Weryfikacja renderu po rozgrzewce cache** — nie `?cb=`, nie odczytem z bazy. Plus MD5 treści
   w bazie zgodny z plikiem źródłowym.
7. **Crawl kontrolny po** — zero nowych 404, **duplikat tytułu zniknął**, zero nowych duplikatów.
8. **Zgłoszenie obu kart ręcznie w panelu GSC** (osobny dzień, jeśli limit wyczerpany).
9. **Kontrola 14-dniowa w kalendarzu „Auranet Claude"**, mierzona z GSC na frazach z §2, nie z DataForSEO.
10. **Wiersze T-117 i T-116 w `docs/REJESTR_ZOBOWIAZAN.md` zaktualizowane w tym samym commicie**, z dowodem.

---

## 5. Czego w tym zadaniu nie robisz

- **Nie ustawiasz `_price` ani wariantów** — patrz §0 pkt 5.
- **Nie zgłaszasz nic do Indexing API.** Wejście do indeksu robimy panelem GSC.
- **Nie zakładasz nowych adresów.** Obie karty istnieją i są w indeksie.
- **Nie ruszasz H1 ani struktury listingu produktów** — T-092 i T-078 też ich nie ruszały.
- **Nie rozbudowujesz dawki na hektar** — link do huba, nie własna sekcja.
- **Nie wchodzisz w `kopalnia jażwica` ani `kopalnia celiny`** jako frazy docelowe bez sprawdzenia
  SERP-u — wolumen jest, ale intencja prawdopodobnie nawigacyjna i nie nasza.
- **Nie wysyłasz nic do klienta.** Wszystko przez Janka na `js@auranet.com.pl`.

---

## 6. Zrobione =

- **Obie karty przepisane**, treść rozbudowana wzorem T-092 i T-078, kwoty w nagłówkach z warunkiem dostawy.
- **Duplikat tytułu #317 zniknął** — potwierdzone crawlem kontrolnym, nie oględzinami.
- **MD5 treści w bazie zgodny** z plikiem źródłowym dla obu kart.
- **Render zweryfikowany po rozgrzewce cache**, nie przez `?cb=` i nie odczytem z bazy.
- **Backup przed zmianą** (`db_export`) i **baseline GSC** w `data/T-117/`.
- **Obie karty zgłoszone ręcznie w GSC**, ze zrzutem potwierdzenia.
- **Kontrola 14-dniowa w kalendarzu.**
- **Wiersze w rejestrze zaktualizowane w tym samym commicie, z dowodem.** Wiersz bez dowodu nie ma
  prawa mieć ✅.
