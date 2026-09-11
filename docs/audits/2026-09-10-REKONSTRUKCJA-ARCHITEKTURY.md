# Rekonstrukcja: skąd się wzięła obecna architektura treści agria.pl

> **Projekt:** `agria` · **Data:** 2026-09-10 · **Typ:** wyjaśnienie, nie wdrożenie · **Zlecił:** Jan Schenk, 09.09.2026
> (`docs/prompty/wdrozenie/2026-09-09-REKONSTRUKCJA-architektura-tresci.md`)
> **Zasada dokumentu:** każde twierdzenie ma źródło (plik, commit, wiersz rejestru, pomiar) albo etykietę
> „brak zapisu". Produkcja nietknięta — odczyt przez MCP `query_db`, `curl`, GSC API, git.
> **Konwencja autorstwa:** „Claude" = ja, wykonawca po stronie Auranet; „Janek" = Jan Schenk;
> `[J]` = zapis akceptu Janka w źródle.
> **Wersja 2 (10.09, po południu):** uzupełniona o archiwum decyzji z okresu XII 2025 – V 2026 z Google Drive
> (`docs/archiwum/2025-12_2026-05-HISTORIA_DECYZJI_claude-ai.md` — zestawienie 28 wątków Claude.ai). Wersja 1 twierdziła,
> że z budowy strony nie ma zapisu decyzji — to było nieprawdziwe. Zmiany opisane w §0a.

---

## 0a. Korekta po archiwum z Drive — co w wersji 1 było nieprawdziwe

| twierdzenie wersji 1 | stan po archiwum | źródło |
|---|---|---|
| „7 kategorii — brak zapisu decyzji" | kategorie to **segmenty z PIM AGRII**, zaimportowane 27.02 skryptem PHP i ujednolicone („stawy rybackie" → Rybactwo itd.). Janek chciał produktów w dobrze nazwanych, poukładanych kategoriach | archiwum §3, §4.2 |
| „Warstwa landingów — trzy moje kroki bez akceptu" | **idea landingu segmentowego jest decyzją z 20.02**: „segment nie w URL produktu (produkt należy do wielu segmentów); segment = strona docelowa z frazą intencyjną". Plan: `/wapno-nawozowe/` (rolnicy), `/wapno-do-stawow/`, `/wapno-do-oczyszczalni/` + archiwum produktów + blog. **13.03 decyzja o podziale fraz:** karta → fraza z nazwy produktu, kategoria/landing → fraza intencyjna. **Moje jest co innego:** 14.07 zmiana osi landingów z odbiorcy (rolnik, staw, oczyszczalnia) na **formę produktu** (granulowane, palone, magnezowe…) oraz landing stabilizacji — tych w planie z lutego nie było | archiwum §6.1 |
| „Kto pisał treść kart — brak zapisu" | **workflow n8n DescWriter** (Gemini), przerobiony z LAGUZ 13.03; wiedza z PIM + danych WC; generował też title, description i focus keyword w Rank Math. **Potwierdzone w bazie 10.09:** 19/19 kart ma tag `content-done` | archiwum §5; MCP `query_db` |
| „Klasteryzacja z maja była pierwotna" | przed majem **klastrów nie opracowano w żadnym wątku** („Klastry nie zostały opracowane jako osobne zadanie") — był podział na segmenty (strategia XII 2025: A–D) i podział ról fraz z 13.03 | archiwum §6.3 |
| — (brakowało) | **pierwotny rozjazd:** decyzja 20.02 trzymała segment **poza** adresem produktu, a Premmerce wstawiał kategorię do adresu (`/wapno-nawozowe-hurt/…`). ADR 08.07 (model A) utrwalił kategorię w adresie. Od tego momentu produkt nie mógł należeć do kilku segmentów bez zmiany adresu — i stąd puste Sadownictwo i Hurtownie | archiwum §4.3, §6.1; ADR 08.07 |
| „Pierwotny plan = kategoria z opisem + karty" | pierwotny plan (20.02) = **kategorie + karty + landingi segmentowe na frazy intencyjne**. Do 19.05 żaden landing nie powstał | archiwum §2.1, §6.1 |

**Źródło prawdy o produktach (polecenie Janka 10.09):** karty AGRII na `/do-pobrania/`, zrobione z papierowego katalogu —
nazwy, zastosowania, parametry. Produktów i parametrów nie ruszamy. Ścieżka dalszych prac:
`docs/strategy/2026-09-10-SCIEZKA-SEO-I-SPRZEDAZY.md`.

**Nowy pomiar 10.09 — skąd przychodzą zapytania ofertowe** (CPT `agria_inquiry`, pole `_source_url`): 11 prawdziwych zapytań
IV–IX, wszystkie o konkretny produkt — **6 z kart produktów, 4 ze strony `/zamowienia/`, 1 z landingu `/wapno-granulowane/`**
(o kredę czarną, której landing nie opisuje). Z kategorii, huba i poradników — zero bezpośrednio.

---

## 0. Odpowiedź w trzech zdaniach

1. **Warstwa kategorii** (7 `product_cat`) to segmenty z PIM AGRII, zaimportowane przy budowie strony 27.02 — decyzja Janka,
   żeby produkty były w dobrze nazwanych, poukładanych kategoriach (archiwum Drive §4.2; wersja 1 błędnie podawała „brak zapisu").
2. **Warstwa landingów:** idea landingu **segmentowego** na frazę intencyjną to decyzja z 20.02 (rolnicy, stawy, oczyszczalnie).
   Do 19.05 nie powstał żaden. Moje, bez zapisanego akceptu, są trzy późniejsze kroki: brief LP stabilizacji (15.06), cztery
   poradniki jednego dnia (09.07) i **rozpiska z 14.07**, która zamieniła oś landingów z odbiorcy na **formę produktu** i wypisała
   sześć landingów exact-match na wzorcu Biovity. 11.08 sam ten wzorzec obaliłem i zostawiłem dwa landingi jako cele Ads z `noindex`.
3. **Dane z 28 dni (09.08–05.09) nie dają warstwie landingów żadnego uzasadnienia**: cztery landingi mają łącznie
   **0 wyświetleń** w GSC (dwa przez `noindex`, dwa przez brak pobrania przez Google), kategorie 5,8% wyświetleń
   serwisu, karty 15,9%, hub `/wapnowanie-gleby/` 67%.

---

## 1. Stan faktyczny 09–10.09 — zweryfikowany, z korektą do promptu

Odczyt MCP `query_db` 09.09 (`wpfz_terms`, `wpfz_term_taxonomy`, `wpfz_posts`, `wpfz_postmeta`), `curl` z pominięciem cache.

**Siedem kategorii `product_cat`** (term 766 „Rybactwo" **usunięty 24.08**, T-095 — dlatego jest 7, nie 8):

| term | nazwa | slug | produktów | opis (bajty) | HTTP |
|---|---|---|---|---|---|
| 764 | Wapno nawozowe | `wapno-nawozowe-rolnictwo` | 15 | 6 664 (T-092, 04.09) | 200 |
| 767 | Oczyszczalnie | `wapno-do-oczyszczalni` | 1 | 976 | 200 |
| 768 | Budownictwo | `wapno-hydratyzowane` | 1 | 468 | 200 |
| 770 | Paszarstwo | `paszarstwo` | 1 | 5 938 (T-078, 08.09) | 200 |
| 830 | Kreda malarska | `kreda-malarska` | 1 | 805 | 200 |
| 765 | Sadownictwo | `wapno-do-sadu` | **0** | 602 | **301 → `/oferta/`** |
| 769 | Hurtownie | `wapno-nawozowe-hurt` | **0** | 420 | **301 → `/oferta/`** |

**Cztery landingi-strony** (`post_type = page`, treść w `post_content`, bez `_elementor_data`, układ przez moduł `plain-content-layout`):

| ID | adres | utworzony | ostatnia zmiana | znaki | `rank_math_robots` | listing (T-064) |
|---|---|---|---|---|---|---|
| 2745 | `/wapno-do-stabilizacji-gruntow/` | 14.07 16:06 | 21.08 | 5 087 | **brak wpisu = `index`** | 1 produkt (#320) |
| 2751 | `/wapno-granulowane/` | 06.08 13:49 (**pusty do 13.08**) | 21.08 | 8 121 | **`noindex, follow`** | 3 produkty (#314, #317, #305) |
| 2757 | `/wapno-nawozowe/` | 14.08 13:47 | 21.08 | 9 378 | **`noindex, follow`** | 14 produktów |
| 2796 | `/wapno-do-stawu/` | 21.08 17:28 | 21.08 | 7 453 | **`index, follow`** | 6 produktów |

⚠️ **Korekta do promptu:** prompt mówi „trzy pierwsze mają `noindex`". W bazie `noindex` mają **dwa**: `/wapno-nawozowe/`
i `/wapno-granulowane/` (jedyne dwa `noindex` w serwisie poza `/cart/`). `/wapno-do-stawu/` ma jawne `index, follow`,
`/wapno-do-stabilizacji-gruntow/` nie ma wpisu robots, czyli domyślne `index`. Potwierdza to crawl 08.09
(`docs/audits/2026-09-08-WERYFIKACJA-CRAWL.md`: „tylko dwa `noindex` w serwisie").

**Dziewiętnaście kart produktów** — treść 5,3–7,4 tys. znaków, atrybuty `pa_*`, producent, cena w treści na 16 z 19
(`offers` w schemacie 16/19, T-097). Cztery poza indeksem 09.09 (#311, #316, #318, #320), dwie z nich weszły po ręcznym
zgłoszeniu tego samego dnia (`data/seo/2026-09-09-serp-i-indeksacja-przed-T116.md` §7).

**Menu:** pozycje Sadownictwo (ID 764/1565) i Hurtownie (763/1564) w `draft` od 30.07; „Wapno do stawu" (765/1566)
wskazuje od 24.08 na stronę 2796, nie na kategorię.

---

## 2. Chronologia — od budowy strony do dziś

Źródła: `git log --reverse` (218 commitów od 26.02), ADR-y w `docs/decyzje/`, rejestr, sesje, MCP. Kolumna „kto" według
zapisu w źródle; „Claude, brak zapisu akceptu" znaczy, że w repo nie ma śladu, by Janek tę decyzję zatwierdził.

| Data | Decyzja / zdarzenie | Źródło | Kto |
|---|---|---|---|
| **22.12.2025** | Strategia marketingowa v2.1: 4 segmenty (A duże gospodarstwa, B oczyszczalnie, C rybactwo, D hurtownie), landingi `/dla-rolnikow`, `/dla-oczyszczalni`, `/dla-stawow` | archiwum Drive §2.1 | Auranet, do zatwierdzenia przez zarząd |
| 05.02.2026 | PIM v1.0 do akceptu klienta (28 SKU / 19 produktów bazowych); katalog 24 str. | archiwum §1, §3 | Janek / klient |
| **20.02.2026** | **Decyzja: segment nie w adresie produktu; segment = strona docelowa z frazą intencyjną.** Plan: `/wapno-nawozowe/`, `/wapno-do-stawow/`, `/wapno-do-oczyszczalni/` + archiwum produktów + blog. „Budujemy od nowa, ma być lepiej niż było"; ceny poza stroną | archiwum §4.3, §6.1 | **Janek** (`DECYZJA`) |
| **27.02.2026** | WooCommerce w trybie katalogu; import PIM (1 produkt = 1 `simple`, warianty w `_agria_variants`); **7 płaskich kategorii = segmenty z PIM**; wtyczka `agria-by-auranet` | archiwum §4.1–4.2; MCP: 19 produktów z datą 27.02 15:10 | **Janek** |
| **13.03.2026** | **n8n DescWriter** (Gemini, workflow z LAGUZ) pisze treść kart i meta Rank Math; **decyzja o podziale fraz:** karta → nazwa produktu, kategoria/landing → fraza intencyjna | archiwum §5, §6.1; MCP: tag `content-done` 19/19 | **Janek** |
| 20.03 · 27.03 | formularz zapytań i kalkulator; **go-live** z `agria.auratest.pl` na `agria.pl` | archiwum §1 | Janek |
| 07.04–04.05 | katalog drukowany — karta = 1 produkt WC, nazwy 1:1 z WC; wysyłka do Kasjana 15.04; wersja web 04.05 | archiwum §9 | Janek / klient |
| **Q1 2026** (przed 26.02) | Strona zbudowana: WP + WC, **7 kategorii po zastosowaniu** (term 764–770 założone jednym ciągiem: Rolnictwo, Sadownictwo, Rybactwo, Oczyszczalnie, Budownictwo, Hurtownie, Paszarstwo), produkty w wielu kategoriach naraz, atrybut `pa_agria-segment` z tymi samymi 7 wartościami. Poradniki budowlane (wykwity, tynki, cement, klinkier), `/wapnowanie-gleby/`, wpis o stawach karpiowych, `/czy-wapnowac…/` | `docs/sesje/2026-08-19-stan-przed-przebudowa-rejestru.md` l.184–186; brief katalogu `assets/print/catalog/HISTORICAL_BRIEF_2026-02-05.txt` (segmenty Rolnictwo/Rybactwo/Oczyszczalnie/Budownictwo/Drogownictwo) | Auranet przy budowie — **zapis w archiwum Drive** (wiersze powyżej); w repo do 19.05 brak |
| 26.02 | Pierwszy commit: wtyczka `agria-by-auranet`, moduł `catalog-mode` (ceny ukryte, koszyk wyłączony) | commit `87c236e` | Auranet |
| 27.03 | Kalkulator wapnowania (`liming-calculator`) | `4a80383` | Auranet |
| ≤19.05 | `KEYWORDS_BASELINE.md` — szkielet 6 segmentów A–F, kolumna „Strona docelowa" już zawiera **„kategoria + LP rolnicy", „LP stawy", „LP drogownictwo"** — landing obok kategorii istnieje w dokumentach **zanim powstał jakikolwiek pomiar** | `docs/seo/KEYWORDS_BASELINE.md` l.18, 42, 59 | autor nieoznaczony (plik z pierwszego setupu repo) |
| 19.05 | Keyword research: 112 fraz, **8 klastrów po zastosowaniu** (regex „pierwszy match wins"); rekomendacja landingów pod kruszywo i „pillar landing pages" | `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` l.23, 229, 237 | Claude |
| 20.05 | Plan on-page: **klaster = kategoria WC**, „nie budujemy landing pages od zera, optymalizujemy istniejące" | `docs/audits/ONPAGE_PLAN_2026-05-20.md` l.51 | Claude |
| 25–27.05 | Oferta wysłana, **zaakceptowana przez Pawła** | `docs/decyzje/2026-05-27-akcept-oferty.md` | klient |
| 15.06 | ADR katalogowy: drogownictwo poza ofertą, 19 produktów = komplet | `docs/decyzje/2026-06-15-decyzje-katalogowe.md` | **Janek** |
| 15.06 | `KR_PRIORYTETYZACJA`: „LP (nowa)" stabilizacja gruntów, „kategoria Rybactwo + LP", „LP Oczyszczalnie"; `CONTENT_AUDIT` §3: **huby per segment**; **brief LP stabilizacji** — pierwszy pełny brief landingu | `docs/audits/KR_PRIORYTETYZACJA_2026-06-15.md` l.13, 24, 50; `docs/audits/CONTENT_AUDIT_2026-06-15.md` l.55–64; `docs/seo/LP_STABILIZACJA_GRUNTU_2026-06-15.md` | Claude, **brak zapisu akceptu** (zakres „bez kruszywa" = Janek) |
| 29.06 | STR-02: formy dostawy i MOQ zdjęte z 19 kart i FAQ | commit `1cc6bd8`, `docs/operations/STRONA_BACKLOG_POPRAWKI.md` | **Paweł** (klient) |
| **08.07** | ADR rdzeń URL: jedna kategoria wiodąca per produkt (wg badge'y katalogu drukowanego), Hurtownie poza `product_cat`, **Sadownictwo i Rybactwo tracą wszystkie produkty**, 19×301, mini-kategoria Kreda malarska (830). Zapis: „landing per segment osobno wg planu KR" | `docs/decyzje/2026-07-08-rdzen-url-taksonomia.md` l.3, 57; `docs/catalog/URL_TAXONOMY_SIM_2026-07-08.md`; commit `fe3bdd7` | **Janek** („zaakceptowany (Janek, 2026-07-08)"; zainicjował: „od tego trzeba zacząć całe SEO") |
| 08.07 | Puste archiwa Hurtownie/Sadownictwo/Rybactwo → **301 na `/oferta/`** | `.htaccess` l.25–26; `docs/sesje/2026-08-19-…` l.135 | Claude, w ramach wdrożenia ADR |
| **09.07** | **Cztery poradniki jednego dnia** (`/ile-wapna-granulowanego-na-ha/`, `/jak-stosowac-wapno-nawozowe/`, `/higienizacja-osadow-sciekowych-wapnem/`, `/wapno-nawozowe-na-trawnik/`) + kategoria wpisów „Zastosowania" (831) jako „dom dla landingów segmentowych" | commit `f18c84c`; `docs/seo/POMIAR_POD_WYNIK.md` l.222–224; MCP: posty 2741–2744 z datą 09.07 | Claude, **brak zapisu akceptu** („drafty do akceptu Janka PRZED publikacją" w `NEXT_THREAD_PROMPT` l.266 — bez śladu, że akcept był) |
| **14.07** | **`ROZPISKA_INTENCJA_WOLUMENOWA`** — zwrot z klastra po zastosowaniu na **klaster po formie produktu** (granulowane 5 400, palone, magnezowe, hydratyzowane, nawozowe, kreda); **Blok 1 = sześć landingów exact-match** na wzorcu Biovity („wzorzec wskazany przez Janka"); diagnoza „nie mamy ani jednej strony komercyjnej". Tego dnia wdrożona LP stabilizacji (C1) | `docs/seo/ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md` §2–6; `docs/seo/BACKLOG_SEZON_2026-07-14.md`; commity `fd557bc`, `5b55617` | Claude; jedyne „Do decyzji Janka" dotyczy starych URL-i (l.145), **nie listy landingów** |
| 15.07 | Naprawa parametrów 19 kart w 4 warstwach (bug importu) | commit `6a70484` | Claude, na zgłoszenie Janka |
| 30.07 | Trzy pozycje menu (Sadownictwo/Rybactwo/Hurtownie) → `draft`; incydent element-cache | memory `project_agria_nav_debt_m4` | Claude |
| 03.08 | Raport M2: **pierwszy pomiar kanibalizacji** („wapno bielik" 6 URL → poz. 15,3) | `docs/raporty/2026-07.md` §4.2 | Claude |
| **06.08** | `REWIZJA_STANU`: kategoria weszła na poz. 11,0 na „wapno nawozowe" → „landing = strona docelowa, kategoria = lista"; briefy LP C2/C3 (`LP_WAPNO_GRANULOWANE`, `LP_WAPNO_NAWOZOWE`) z **`robots: index, follow`** i „podwójną funkcją: Ads oraz landing komercyjny pod sezon"; **strona `/wapno-granulowane/` (2751) założona z pustą treścią**; plan Ads wysłany klientowi | `docs/raporty/REWIZJA_STANU_2026-08-06.md` §B; `docs/seo/LP_WAPNO_GRANULOWANE_2026-08-06.md` l.5, 21; MCP `post_date` 2751; commit `6a08df0` | Claude, brak zapisu akceptu (plan Ads = akcept klienta) |
| **11.08** | `ROZSTRZYGNIECIE_ARCHITEKTURY` + ADR podział ról: Biovita = zły komparator („błąd analityczny"), Polcalc 95% z bloga; **landingi wyłącznie jako cele Ads, poza indeksem**; cztery landingi nie powstają; kategoria = jedyna strona organiczna na „wapno nawozowe" | `docs/seo/ROZSTRZYGNIECIE_ARCHITEKTURY_2026-08-11.md`; `docs/decyzje/2026-08-11-podzial-rol-ads-seo.md` (status „przyjęta", bez `[J]`; §„Co wymaga decyzji Janka" — **brak zapisu odpowiedzi**) | Claude |
| 13.08 | Zmierzone: `/wapno-granulowane/` **0 bajtów** tydzień po „publikacji", reklamy miały na niego iść od 14.08; polecenie Janka: landingi z gotowego wzorca przez Chrome MCP | `docs/ads/SETUP_KAMPANII_2026-08.md` l.17–18; memory `feedback_agria_landingi_wzorzec_nie_elementor` | Janek (korekta) |
| **13–14.08** | Oba landingi Ads dostają treść, `/wapno-nawozowe/` (2757) utworzony, **`noindex, follow` na obu** — „domknięcie luki z ADR 11.08"; kampanie Ads żywe | `docs/decyzje/2026-08-13-uruchomienie-kampanii-ads.md` §5; commit `5c35591` | Claude (noindex), Janek (start Ads) |
| 19.08 | Ceny w treści 15 kart (T-010/T-011), korekta „jedna cena zamiast dwóch" po uwadze Janka; ceny na 2 landingach; rejestr przebudowany na T-NNN; diagnoza T-026 | commity `7403dee`, `1a6896b`, `676a8f6`, `a909f11` | Janek (ceny — ADR dwie warstwy cen), Claude (wykonanie) |
| **21.08** | T-052: keyword research **od nowa** — 9 klastrów wg pytania/lejka; ADR hub i spoke (oś = pytanie, próg URL ≥3 frazy i ≥100/mies.; „uwaga Janka": hub blokuje uprawy); ADR terminarz jako hub osi KIEDY `[J]`; **ADR nazwy kategorii bez segmentów `[J]`** — Janek: „kategoria segmentowa opisuje wymyślony podział, nie towar", segmenty = landingi z ręcznym listingiem, przebudowa adresów (T-068) odłożona na zimę; **landing `/wapno-do-stawu/` (T-056)**, slug kategorii 766 zwolniony, reguła 301 zdjęta „za zgodą Janka"; T-063 układ (zgłosił Janek), **T-064 listingi na 3 landingach („uwaga Janka")** | `docs/seo/T-052-…`; trzy ADR-y z 21.08; rejestr l.408–411; `docs/sesje/2026-08-21-podsumowanie.md` §3 | mieszane — patrz §3 |
| **24.08** | Audyt SEO od nowa: **0 z 10 nowych adresów od 09.07 pobranych przez Google**, 8/19 kart poza indeksem; ADR rozstrzygnięć: kolejność wg crawlu, Faza 0 „zero nowych adresów", **hub `/jakie-wapno-na-pole/` nie powstaje** (T-073), łąki (T-075) zdjęte, tonaż/ozime → VII 2027, budownictwo na kategorii; T-026 scalenie poradnika dawkowego do huba; **term 766 Rybactwo usunięty** (T-095) | `docs/audits/2026-08-24-AUDYT_SEO_OD_NOWA.md`; `docs/decyzje/2026-08-24-…` („decyzja Janka 24.08"); rejestr l.366, 384 | **Janek** (ADR), Claude (audyt i wykonanie) |
| 04.09 | Opis kategorii `/wapno-nawozowe-rolnictwo/` 958 → ~5 700 znaków (T-092); analiza kanibalizacji; kontrola T-053: **bez efektu** | commit `049563a`; `data/seo/2026-09-04-kanibalizacja-…`; `data/kontrole/2026-09-04-…` | Claude (plan z ADR 24.08) |
| 07.09 | Plan wrześniowy, crawl SF: hub = 63% wyświetleń i 90% straty (AI Overview); **T-117: dwie karty granulowane zamiast landingu**; blok 0 na produkcji | `docs/PLAN_WRZESIEN_2026.md`; `docs/audits/2026-09-07-CRAWL_SCREAMING_FROG.md`; commit `d552fbf` | Claude; Janek (odpowiedzi 07.09: `61ca174`) |
| 08.09 | Opis `/paszarstwo/` 465 B → 5 938 B (T-078) | commit `383b7d7` | Claude |
| 09.09 | Pomiar: kart poza indeksem 4, nie 8; **linkowanie nie wprowadza do indeksu (16 dni, 0 pobrań)**; **ręczne zgłoszenie w panelu GSC wprowadza w kilkanaście minut**; prompt rekonstrukcji | `data/seo/2026-09-09-serp-i-indeksacja-przed-T116.md` §6–7; commit `a99eb88` | Janek (zgłoszenia), Claude (pomiar) |

---

## 3. Mapa warstw — co się z czym dubluje

```
STRONA GŁÓWNA  title „Wapno nawozowe, hydratyzowane i palone – AGRIA"  ← celuje w tę samą frazę co kategoria (wbrew ADR 11.08)
│
├── KATEGORIE product_cat (po zastosowaniu, Q1 2026)
│   ├── /wapno-nawozowe-rolnictwo/   15 produktów · opis 6,7 KB (T-092) · GSC 992 wyśw. · „wapno nawozowe" poz. 8,9–11
│   ├── /wapno-do-oczyszczalni/       1 · 976 B · 460 wyśw. · najlepszy CTR kategorii (2,4%)
│   ├── /paszarstwo/                  1 · 5,9 KB (T-078) · 122 wyśw.
│   ├── /wapno-hydratyzowane/         1 · 468 B · 121 wyśw. · poz. 29,4
│   ├── /kreda-malarska/              1 · 805 B · 0 wyśw. (jedyna nieindeksowana z pełnych)
│   ├── /wapno-do-sadu/               0 produktów → 301 /oferta/ (od 08.07)
│   └── /wapno-nawozowe-hurt/         0 produktów → 301 /oferta/ (od 08.07)
│
├── LANDINGI-STRONY (osobne `page`, 14.07–21.08)
│   ├── /wapno-nawozowe/              noindex · cel Ads · listing 14 produktów Z KATEGORII 764  ⇒ DUBLUJE kategorię 764 (ta sama fraza, te same produkty)
│   ├── /wapno-granulowane/           noindex · cel Ads · listing 3 produktów Z KATEGORII 764   ⇒ PRZEKRÓJ przez kategorię 764 po formie (granulat)
│   ├── /wapno-do-stawu/              index · sierota do 24.08 · nigdy niepobrany · listing 6 produktów z 764/767/768 ⇒ ZASTĘPUJE usuniętą kategorię Rybactwo
│   └── /wapno-do-stabilizacji-gruntow/ index · nigdy niepobrany · 1 produkt (#320)            ⇒ DUBLUJE kartę #320 i kategorię 767
│
├── KARTY PRODUKTÓW (19, Q1 2026 + naprawa 15.07 + ceny 19.08)   GSC 4 653 wyśw. · 76 klik · 15 z 19 widocznych
│
└── PORADNIKI / HUB                                            GSC 20 380 wyśw. (67–70% serwisu) · 151 klik
    ├── /wapnowanie-gleby/ (Q1) — oś ILE, 19 572 wyśw.
    ├── /kalkulator-wapnowania/ (27.03, Mg 04.09) — 663 wyśw., CTR 5,3%
    ├── /jak-stosowac-wapno-nawozowe/ (09.07, hub KIEDY 21.08) — 0 wyśw., nigdy niepobrany
    ├── /wapno-nawozowe-na-trawnik/ (09.07) — 0 · /higienizacja-…/ (09.07) — 0 · /ile-wapna-granulowanego-na-ha/ → 301 na hub (24.08)
    └── wpisy budowlane z Q1 (wykwity 90, tynki 33, cement 16)
```

**Dublowania nazwane wprost:**

1. `/wapno-nawozowe/` (landing) ↔ `/wapno-nawozowe-rolnictwo/` (kategoria) ↔ strona główna — **trzy strony na jedną frazę**;
   landing wyłączony `noindex`, ale strona główna i kategoria nadal rankują obok siebie (04.09: główna poz. 6,5 / kategoria 11,0).
2. `/wapno-granulowane/` ↔ karty #314, #317, #305 — landing opisuje te same trzy produkty, które mają własne karty z parametrami;
   od 07.09 plan T-117 przenosi tę pracę **na karty**, czyli uznaje landing za zbędny organicznie.
3. `/wapno-do-stabilizacji-gruntow/` ↔ karta #320 ↔ `/wapno-do-oczyszczalni/` — trzy adresy na jeden produkt; fraza
   „wapno do stabilizacji gruntów" w planerze `null`, w GSC 0 wyświetleń na „stabiliz" przez 90 dni (T-026).
4. `/wapno-do-stawu/` — jedyny landing bez dubla: zastępuje kategorię Rybactwo, która nie mogła mieć produktów bez zmiany
   ich adresów (Premmerce). Janek: „to realna intencja" — zgadza się z pomiarem (klaster 4 100/mies., 0 pokrycia).
5. Kategorie Sadownictwo i Hurtownie — puste od 08.07, bo ADR rdzenia URL obiecał „landing per segment wg planu KR",
   a **takiego planu w KR nie było** (KR l.237 planował 2 pillary, nie landingi segmentowe).

---

## 4. Oś klasteryzacji — jak lista fraz stała się listą adresów

Pełna rekonstrukcja z cytatami: analiza cząstkowa w tym wątku (28 dokumentów). Skrót:

**Pierwotna klasteryzacja (maj–czerwiec): po zastosowaniu / odbiorcy, ustalona przeze mnie, bez zapisu akceptu.**
`KEYWORDS_BASELINE` (6 segmentów A–F, wolumeny „TBD"), `MASTER_PROMPT` (5 segmentów), KR 19.05 (8 klastrów regexem).
Jedyna decyzja Janka w tym okresie jest katalogowa (drogownictwo poza ofertą, 15.06) — wycięła klaster, nie zbudowała żadnego.
20.05 pierwsze zrównanie klastra z URL-em: „Strony segmentowe = kategorie produktowe (7) — główne landing pages SEO"
(`ONPAGE_PLAN` l.39).

**Dziesięć zwrotów w cztery miesiące** — pięć z nowej rozpiski wolumenów, trzy z pomiaru, dwa z decyzji biznesowej/technicznej:

| # | Data | Zmiana | Bodziec |
|---|---|---|---|
| 1 | 20.05 | 8 klastrów → 7 kategorii WC 1:1 | mapowanie, nie pomiar |
| 2 | 15.06 | drogownictwo (65% wolumenu) → jedna fraza + LP stabilizacji | decyzja Janka (oferta) + rozpiska CPC |
| 3 | 08.07 | Sadownictwo/Rybactwo/Hurtownie tracą URL, obietnica „landing per segment" | diagnoza techniczna Premmerce + katalog drukowany |
| 4 | 08.07 | oś = poradniki, „NIE mnożyć URL" | pomiar SERP — po czym 09.07 powstało 5 nowych URL |
| **5** | **14.07** | **klaster po zastosowaniu → klaster po FORMIE produktu; 6 landingów exact-match** | rozpiska DFS fraz head + Biovita + sezon. Własny pomiar (poradniki rankują, produkty nie) szedł **wbrew** temu |
| 6 | 06.08 | klaster „cenowy" 1 320 + rozdział ról landing/kategoria | rozpiska + pomiar kategorii poz. 11 |
| 7 | 11.08 | landingi organiczne skasowane; klaster organiczny = „39 fraz luki wobec Polcalc" | pomiar (komparatory, kanibalizacja) |
| **8** | **21.08** | **9 klastrów wg PYTANIA/lejka** (JAKIE / KIEDY / ILE / uprawa…) | rozpiska 2 080 fraz + GSC + korekta reguły 11.08 |
| 9 | 24.08 | klastry bez zmian, **URL-e cofnięte** (T-073, T-075, T-082, T-076) | pomiar indeksacji (0/10) i sezonu (VIII, nie X) |
| 10 | 07.09 | „wapno gaszone" doklejone do T-085; T-117 karty zamiast landingu | rozpiska DFS 07.09 + GSC |

**Moment, w którym klaster stał się listą adresów: 14.07.** Do tego dnia klaster mapował się na istniejące kategorie
i poradniki; od `ROZPISKI` każda fraza head dostała slug. Z **16 bytów URL** zaplanowanych między 15.06 a 21.08 **jeden**
powstał z pomiaru (higienizacja — i przegrywa z własną kategorią), **15 z rozpiski**. Wszystkie cofnięcia przyszły z pomiaru.

**„Hub i spoke" 21.08 to nowa logika, nie kontynuacja klasteryzacji po zastosowaniu** — ADR mówi to sam: T-038 (huby
segmentowe) „nieoparte na pomiarze", tu „podział wynika z rozłącznych fraz i ma próg liczbowy". Z trzypoziomowej
architektury 21.08 po 24.08 stoi tylko hub KIEDY (terminarz) — nigdy niepobrany przez Google.

**Klastry porzucone bez zapisu decyzji:** paszarstwo (wypadło przez seedy KR, wróciło 21.08 jako 8 940/mies.), rybactwo
między 08.07 a 14.07 („301 poszło, landingi nie powstały. Zła kolejność." — `ROZPISKA` l.29), sadownictwo (kategoria
rankowała #11 na 30/mies., poszła na 301), „X vs Agrobielik", segmenty JST/rekultywacja. Jedyny klaster nietknięty od
19.05 — dawkowy („ile wapna na hektar") — „odpowiada dziś za całą widoczność domeny" (T-052 l.92–93).

---

## 5. Oś audytów — dwanaście audytów, co wykonano, co upadło

Pełna wersja z cytatami: analiza cząstkowa w tym wątku. Tabela zbiorcza (daty faktyczne z git, nie z nazw plików):

| # | Audyt | Data | Wykonano | Wnioski obalone później |
|---|---|---|---|---|
| 1 | `SEO_AUDIT_RESULTS` | 19.05 | tak (GA4/GTM/GSC, schema, 301, nagłówki; LCP dopiero 07.09) | „0/38 zaindeksowanych" (13/38 już 15.06; ramka „38" zniknęła po migracji); Indexing API „3–7 dni" (6 batchy bez efektu dla nowych treści); P1-9 „brak CMP" utrwalone w rejestrze do 24.08 → błędne T-086 |
| 2 | `KEYWORD_RESEARCH` | 19.05 | część; **zastąpiony T-052 21.08** | drogownictwo jako klaster #1 (kruszywo poza ofertą — 95% „największego klastra" nie istniało dla AGRII); sezon „jesień" (szczyt = sierpień, dane były w pliku); klaster glebowy (`ph gleby`, `badanie gleby` ~3 640/mies.) skasowany filtrem regex; landingi/pillary jako typ strony |
| 3 | `ONPAGE_PLAN` | 20.05 | tak (meta, literówki, tytuły, rdzeń URL) | „65% wolumenu zablokowane bez kruszywa"; Bielik cel TOP10 (poz. 31,3); liczenie znaków tytułu jako dźwignia (teza CTR odrzucona 07.09) |
| 4 | `BASELINE_M1` | 15.06 | tak | cele M6: 38/38 (4 karty poza), komercyjne TOP10 (0), LCP <2,5 s (3,7–7,6); kliknięcia ×3–5 osiągnięte, ale 67% z jednego huba |
| 5 | `CONTENT_AUDIT` | 15.06 | część (4 poradniki 09.07, LP stabilizacji 14.07; kalendarz porzucony) | **§3 huby per segment — „nieaktualna i nie wolno jej realizować"** (nagłówek pliku, T-038); 3 z 4 poradników nigdy niepobrane; LP stabilizacji bez popytu |
| 6 | `INDEXATION_DIAGNOSIS` | 15.06 | tak (23 URL, `/cart/`) | remedium Indexing API upadło (24.08: „nie wywołuje crawlu zwykłej treści"); inwentarz niepełny |
| 7 | `KR_PRIORYTETYZACJA` | 15.06 | część (T-021, T-024, T-056, T-092; LP oczyszczalnie nie) | „LP (nowa)" jako narzędzie organiczne (ADR 11.08); stabilizacja bez popytu; `wapno hydratyzowane` TOP10 |
| 8 | `ONPAGE_BACKLOG` | 15.06 | tak | własne statusy — 6 pozycji „niezrobionych" było zrobionych; „CMP nie ma" fałszywe |
| 9 | `T-026 diagnoza` | 19.08 | tak (scalenie 24.08) | **połowa** — terminarz nie jest dubletem huba (oś KIEDY poz. 34,1); „kanibalizacja blokuje pobranie" vs ręczne zgłoszenie 09.09 działa w minuty |
| 10 | `AUDYT_SEO_OD_NOWA` | 24.08 | tak (ADR, Faza 0, T-092/T-078/T-096/T-097) | **8 kart → 4** (weszły same); **znaki kategorii zawyżone 4–7×** (3 996 vs 958; 3 083 vs 465 B) — T-092 i T-078 planowane na fałszywym baseline; **przesłanka Fazy 0 (linkowanie wprowadza do indeksu) — nie: 16 dni, 0 pobrań**; warunek Fazy 2 martwy. Stoją: sezon sierpniowy, unieważnienia T-073/T-075/T-079 |
| 11 | `CRAWL_SCREAMING_FROG` | 07.09 | tak (blok 0) | korekty 08.09: `offers` 19→16 by design, tytuły ucinane 8→1, meta kredy malarskiej jest. **Diagnoza AI Overview nieobalona** |
| 12 | `WERYFIKACJA-CRAWL` | 08.09 | tak | brak zapisu (1 dzień) |

**Audyty, na których oparto decyzje architektoniczne, a których wnioski upadły — cztery:**

1. **KR 19.05 → oferta i priorytet drogownictwa.** Upadł 15.06 (asortyment) i 24.08 (sezon). Klient dostał ten KR jako załącznik oferty.
2. **CONTENT_AUDIT §3 + KR_PRIORYTETYZACJA → huby i LP (T-024, T-035, T-036, T-038, ROZPISKA 14.07).** LP stabilizacji zbudowana
   i bez popytu; huby i cztery landingi unieważnione po zmierzonej kanibalizacji. Rejestr: „źródło powtarzających się propozycji »zróbmy huby«".
3. **SEO_AUDIT P0-6 + INDEXATION_DIAGNOSIS → Indexing API jako akcelerator.** 6 batchy 15.06–19.08, żaden nie wprowadził nowej treści;
   koszt uboczny: wspólna pula 200/dobę (incydent Desal). Działający mechanizm (panel GSC) znaleziony 09.09.
4. **AUDYT 24.08 → Faza 0 i warunek Fazy 2.** Linkowanie nie wprowadziło ani jednego adresu; liczba kart poza indeksem spadła sama;
   baseline'y kategorii zawyżone.

Poza audytami dwa najczystsze błędy metody przełożone na zadania: **T-069** (CTR z sumy `query` — 85% kliknięć pod progiem
prywatności) i **ROZPISKA 14.07** (jeden komparator, Biovita).

---

## 6. Wyniki GSC per warstwa — 28 dni (09.08–05.09, `dataState: final`)

Pobrane 09.09 wymiarem `page` dla całego serwisu (37 adresów z danymi, 29 225 wyświetleń, 347 kliknięć).

| warstwa | adresów z danymi | wyświetlenia | udział | kliknięcia | CTR | poz. ważona |
|---|---|---|---|---|---|---|
| **poradniki / hub / kalkulator** | 6 | **20 380** | **69,7%** | 151 | 0,74% | 5,9 |
| **karty produktów** (aktualne URL) | 15 z 19 | 4 653 | 15,9% | 76 | 1,63% | 11,1 |
| strona główna | 1 | 1 843 | 6,3% | 70 | 3,80% | 11,5 |
| **kategorie** | 4 z 7 | 1 695 | 5,8% | 23 | 1,36% | 10,6 |
| inne (kontakt, oferta, rodo, zamówienia, PDF) | 6 | 613 | 2,1% | 24 | 3,92% | 8,7 |
| karty — stare URL po 301 | 5 | 41 | 0,1% | 3 | — | 5,8 |
| **landingi (4)** | **0** | **0** | **0%** | **0** | — | — |

Rozbicie kategorii: `/wapno-nawozowe-rolnictwo/` 992 / 6 / poz. 8,9 · `/wapno-do-oczyszczalni/` 460 / 11 / 8,9 ·
`/paszarstwo/` 122 / 3 / 12,5 · `/wapno-hydratyzowane/` 121 / 3 / 29,4 · `/kreda-malarska/` 0 · Sadownictwo i Hurtownie 301.

Rozbicie landingów: `/wapno-nawozowe/` i `/wapno-granulowane/` — `noindex` (z definicji 0); `/wapno-do-stawu/`
i `/wapno-do-stabilizacji-gruntow/` — `index`, w sitemapie, linkowane od 24.08, **nigdy niepobrane przez Google**, 0 wyświetleń.

Karty z wyświetleniami i zerem kliknięć: `weglanowe-magnez-granulowane` 387 / 0 (poz. 25,5); `weglanowe-granulowane`
511 / 1 (18,9) — to dwie karty, które T-117 ma rozbudować zamiast landingu granulatu.

**Co warstwa landingów dała po stronie płatnej** (jedyna rola, którą ADR 11.08 im zostawił): 14–31.08 Ads wydał 809,58 zł na
453 kliknięcia i **3 zdarzenia kontaktowe** (270 zł/zdarzenie); 30.08–07.09 Rolnictwo: 237 kliknięć, **0 konwersji**;
`/wapno-nawozowe/` to najdroższy adres w koncie (249 kliknięć, 485,60 zł do 07.09). Hipoteza 5 z ADR 11.08 („landing konwertuje
taniej niż kategoria") **nigdy nie została zmierzona** — reklamy nie kierowały nigdy na kategorię, więc porównania nie ma.

---

## 7. Oś treści — każdy tekst na stronie: kiedy, z czego, pod co, z jakim wynikiem

Pełna tabela 35 adresów z cytatami: analiza cząstkowa w tym wątku. Poniżej to, co odpowiada na pytania Janka.

### 7.1 Karty produktów — kiedy, kto, jakim mechanizmem

- **Kiedy i z czego:** treść 19 kart weszła do WooCommerce **13–25.03.2026** przy budowie strony (`docs/catalog/PRODUCTS_INVENTORY.md`).
  Dane z **PIM-u AGRII** — brief katalogu 05.02: „18 KART PRODUKTÓW — DANE Z PIM"; Paweł 16.06: „formy dostawy z PIMu, które
  nanosiliśmy". **Prozę i FAQ kart napisał workflow n8n DescWriter** (Gemini, 13.03, z PIM + danych WC) — archiwum Drive §5; w bazie 19/19 kart ma tag `content-done`.
- **Czy „pod SEO":** tak, przed repo — audyt 20.05 zastał **RankMath z title, description i focus keyword na 19/19 kart i 7/7 kategorii**
  (`ONPAGE_PLAN` l.16, 213–215), z usterkami (8 focusów z literówką `weglanowe`, placeholder „35 lat", „70 70% CaO"). To jest
  „mechanizm", o którym mówi Janek: RankMath per karta, ustawiony przy budowie. W kwietniu karty miały `noindex` (budowa), zdjęty
  przed czerwcem — stąd „0/38" w GSC 15.06.
- **Czy z kart producentów z `/do-pobrania/`:** **nie na starcie**. Parametry wpisano z PIM-u/katalogu z **bugiem importu**
  (przecinek dziesiętny rozbijał atrybuty: `pH >16`, `frakcja 0-0`, `dawkowanie 5-1`) i częścią wartości bez pokrycia (Bielik „min. 72% CaO").
  Dopiero **naprawa 15.07** (commit `6a70484`, `docs/catalog/PLAN_NAPRAWY_PARAMETROW_2026-07-14.md`) wzięła za source of truth
  17 kart AGRII + karty producentów + atest OSChR, które leżały na `/do-pobrania/` od 29.06 (STR-04). Bez karty producenta
  zostały do dziś #303, #304, #316.
- **Mechanizm edycji (chronologicznie):** 29.06 STR-02 — MCP `update_post_content` + `query_db_write` (hak `mcp-ext.php` wdrożony
  FTP-em specjalnie pod to) · 08.07 migracja URL — DB + `.htaccess` · 15.07 parametry — `REPLACE()` na `<td>` przez `query_db_write`
  w `post_content` **i** `_elementor_data`, atrybuty przez SQL + WC API, meta przez `update_postmeta` · 19.08 T-010/T-011 — MCP
  `update_post_content` z kontrolą długości, 307/310/320 w obu warstwach · 07.09 `offers` — filtr `rank_math/json_ld` w module `seo-head`.
  **Trzy karty (307, 310, 320) renderują z `_elementor_data`**, `post_content` jest tam nieaktualny i nierenderowany; polskie znaki
  w JSON Elementora są escapowane, więc `REPLACE` z polskimi literami nie trafia.
- **Wynik:** 12 kart ma wyświetlenia, 7 ≈ 0. Klikają **tylko brandowe** (`oxyfertil-90` 5,1%, `agrobielik-70` 5,2%) i `bielik` (2,2%);
  generyczne stoją pod AI Overview i OLX-em. Blok SEO on-page M1–M2 (SKU, literówki, Bielik, pH) ma w dzienniku „daty per pozycja
  nieodtworzone" — zweryfikowany dopiero 19.08.

### 7.2 Opisy kategorii

- Pierwotne z Q1, autor nieznany, „jeden akapit + lista" (`ONPAGE_PLAN` B2). Długości 24.08: 764 — 958 znaków widocznych,
  767 — 724, 768 — 380, 770 — 465 B, 765 — 571, 766 — 393, 769 — 404, **830 — 0** (kategoria z 08.07, bez meta do 07.09).
  Audyt 24.08 podał 3 996 / 3 083 — render z listingiem, zawyżone.
- **21.08 `[J]`** nazwy 764/766 bez członu segmentowego — kontrola 04.09: poz. 10,4 → 11,2, 0 kliknięć, **bez awansu**.
- **04.09 T-092** (`/wapno-nawozowe-rolnictwo/`) 958 → ~5 700 znaków, 1 → 7 H2. Podstawa: **rozpiska + karty**; baseline GSC zrobiony
  w dniu wdrożenia jako punkt odniesienia, nie jako źródło osi. Kontrola 18.09. Przy okazji zmierzone: na żywo agria.pl **nie ma
  w TOP33 na „wapno nawozowe"** ani w PL, ani w Małopolsce; strona główna dubluje frazę w title.
- **08.09 T-078** (`/paszarstwo/`) 465 B → 5 938 B. **Jedyny opis zbudowany z pomiaru**: baseline pokazał kategorię na 0 wyświetleń
  i klaster pytający o dawkowanie (`ile kredy pastewnej dla kur na 100 kg` poz. 6,6, 0 kliknięć), SERP 07.09 z AI Overview z 7 domen —
  4 pytania „ludzie pytają też" weszły jako H3. Kontrola 26.09.
- **07.09 T-096** `/kreda-malarska/` — pierwsze meta i ~750 znaków; kategoria nadal poza indeksem.

### 7.3 Poradniki i hub

| adres | publikacja | źródło merytoryczne | fraza | GSC 28 dni | los |
|---|---|---|---|---|---|
| `/wapnowanie-gleby/` | **23.02.2026** (Q1) | tablice IUNG (te same, co kalkulator; 99/100 wierszy zgodnych, T-067) | `ile wapna na hektar` 720 | **19 572 / 115 / 5,8** | przebudowa 09.07 (poz. 14 → 8,7), sekcja cenowa 19.08, meta T-053 21.08 (bez efektu), scalenie granulatu 24.08; **jest źródłem AI Overview** — stąd CTR 0,6% przy poz. 5,8 |
| `/kalkulator-wapnowania/` | 09.03 (kod 27.03) | IUNG-PIB 2022 | `kalkulator wapnowania` | 663 / 35 / 7,8 | meta dopiero 14.07; moduł Mg 04.09; jedyna strona z „normalnym" CTR |
| `/ile-wapna-granulowanego-na-ha/` | 09.07 | **niewskazane** | 590 | 0 | scalony do huba + 301 (24.08) — hub trzymał jego frazę na 7,5 |
| `/jak-stosowac-wapno-nawozowe/` | 09.07 → 21.08 terminarz | IUNG 2021 tab. 18 / tab. 8 (PDF w repo od 04.09) | `kiedy wapnować glebę` 320 | **0** | 22 675 znaków, 16 linków, **nigdy niepobrany**; ręczne zgłoszenie 09.09 |
| `/wapno-nawozowe-na-trawnik/` | 09.07 | niewskazane | 50 (fraza wykluczona w `ONPAGE_PLAN` §A4) | 0 | URL unknown; T-026 „nie wracamy" |
| `/higienizacja-osadow-sciekowych-wapnem/` | 09.07 | PN-EN 459-1 | 30 | 0 | kategoria 767 zbiera całą intencję (806/32 w 90 dni); zostaje decyzją Janka 24.08, merytoryka → T-093 |
| wpisy budowlane (tynki, klinkier, cement, wykwity) | 2025 – 01.2026 | brak zapisu | brak (nie nasza intencja) | 139 / 1 | przeniesione przy budowie 24.03; „nie nasza intencja" (audyt 24.08) |
| `/czy-wapnowac-…-stawy-karpiowe/` | 12.03 | *Przegląd Rybacki* 4/2014 | `wapnowanie stawu` 90 | 0 | zaległy werdykt noindex z 18.04 → T-070 |

### 7.4 Meta i tytuły

- Q1: RankMath 19/19 + 7/7 (bez zapisu, kto). 14.07: meta na 6 stronach statycznych. 15.07: meta 5 kart wg kart producentów.
- **T-052/T-053, 21.08:** 4 adresy klastra dawkowego, baseline hub 14 227 wyśw. / 69 klik. **Kontrola 04.09: bez efektu** — 49 → 49
  kliknięć na równych oknach, CTR 0,55 → 0,61% przy pozycji lepszej o 0,68. Diagnoza 07.09: problem **nad** snippetem (AI Overview,
  wideo, PAA), nie w snippecie. T-069 (to samo raz jeszcze) wycofane 24.08 jako dublet na źle policzonym CTR.
- **T-116 (20.09):** teza „krótszy tytuł = lepszy CTR" odrzucona; „nazwa własna w tytule" przeformułowana 09.09 na „pozycja
  bezwzględna w SERP z blokami". Bezwarunkowo: duplikat title #317/#318, #319 ucinany.

### 7.5 Teksty, które powstały i nie przyniosły nic

| adres | publikacja | znaki | fraza (wolumen) | wyśw. 28 dni | klik | indeks |
|---|---|---|---|---|---|---|
| `/jak-stosowac-wapno-nawozowe/` (terminarz) | 09.07 / 21.08 | 22 675 | `kiedy wapnować glebę` 320 | 0 | 0 | nigdy niepobrany |
| `/wapno-nawozowe-na-trawnik/` | 09.07 | 5 676 | 50 | 0 | 0 | URL unknown |
| `/higienizacja-osadow-sciekowych-wapnem/` | 09.07 | 7 526 | 30 | 0 | 0 | Discovered |
| `/ile-wapna-granulowanego-na-ha/` | 09.07 | 12 065 | 590 | 0 | 0 | scalony, 301 |
| `/wapno-do-stabilizacji-gruntow/` | 14.07 | 5 087 | `stabilizacja gruntu` 720 wg KR; 0 wyśw. na „stabiliz" w 90 dni | 0 | 0 | URL unknown |
| `/wapno-granulowane/` | 06.08 (pusty do 13.08) | 8 121 | `wapno granulowane` 4 400–5 400 | 0 (`noindex`) | 0 | poza indeksem z decyzji |
| `/wapno-nawozowe/` | 14.08 | 9 378 | `wapno nawozowe` 1 300 | 0 (`noindex`) | 0 | poza indeksem z decyzji |
| `/wapno-do-stawu/` | 21.08 | 7 453 | `wapno do stawu` 390 (klaster 4 100) | 0 | 0 | URL unknown |
| T-053 meta 4 adresów | 21.08 | — | CTR klastra dawkowego | 8 086 (12 dni) | 49 → 49 | **bez efektu** |
| nazwy kategorii 764/766 | 21.08 | — | `wapno nawozowe` | 19 → 114 | 0 → 0 | **bez awansu** |
| `…/weglanowe-magnez-granulowane/` #317 | III 2026 | 6 005 | `wapno magnezowe granulowane` 880 | 387 | **0** | tak (poz. 25,5) → T-117 |
| `…/weglanowe-granulowane/` #314 | III 2026 | 6 364 | `wapno granulowane` 4 400 | 511 | 1 | tak (18,9) → T-117 |
| #302, #303, #308, #311, #316, #318, #320 | III 2026 | 5–7 tys. | — | ≤2 | 0 | 4 weszły same VIII–IX, 2 po ręcznym zgłoszeniu, #311 czeka |
| `/kreda-malarska/` (kategoria) | 08.07 | 0 → 750 | `kreda malarska hurt` | 0 | 0 | Discovered |
| `/wapno-do-sadu/`, `/wapno-nawozowe-hurt/` | Q1 | 571 / 404 | 30 / null | 301 | — | 301 → `/oferta/` |

**Dwa wnioski przekrojowe:** (1) **każdy nowy adres opublikowany po 09.07 — siedem adresów, łącznie ~70 tys. znaków — ma 0 wyświetleń**
niezależnie od objętości i źródeł; jedyny kanał, który wprowadził coś do indeksu, to ręczne zgłoszenie w panelu GSC 09.09;
(2) **jedyny tekst zbudowany z pomiaru zapytań (T-078) powstał 08.09** — wszystkie wcześniejsze (karty Q1, poradniki 09.07,
terminarz, T-092) powstawały z rozpiski lub wolumenu, a pomiar dokładano po fakcie.

---

## 7b. Co raportowaliśmy klientowi, a co stało na stronie

Analiza cząstkowa w tym wątku (11 dokumentów raportowych i ofertowych). Skróty: `M06` = `docs/raporty/2026-06-mail.md`
(wysłany 03.07), `M07` = `2026-07-mail-WYSLANY.md` (03.08), `ADS3M` = `docs/offers/2026-08-PLAN_ADS_3MIES.md` (ok. 06.08),
`M08` = `2026-08-mail.md` (draft 31.08/01.09 — **brak kopii `-WYSLANY` w repo, status wysyłki niezweryfikowany**),
`STRAT` = `docs/strategy/STRATEGIA_AGRIA_6MIES_2026.md`.

**Co obiecano na piśmie w maju/czerwcu:** segmenty po zastosowaniu, każdy z własną stroną (`STRAT` l.51–77); M3 = „landingi
produktowe — **indeksowalne** strony kategorii pod wapno granulowane, nawozowe, palone, magnezowe, kreda nawozowa" (l.124–127);
M4 = landingi segmentowe `/wapno-do-stawow/`, hub oczyszczalni, `/wapno-do-sadu/` + powrót 3 pozycji menu (l.136–137);
4 artykuły miesięcznie (`OFERTA` l.17, `M06` l.41). Razem **≈29 nowych adresów w M2–M6**, z tego ~12 do końca września.
Powstało: 3 poradniki (VII) + 0 (VIII) + 1 planowany (IX). Oferta i strategia miały przy tym **dwa różne kalendarze segmentów**.

| Raport | Data | Twierdzenie do klienta | Stan faktyczny w dniu wysyłki | Rozjazd |
|---|---|---|---|---|
| `M06` l.31 | 03.07 | „dopchnęliśmy do wyszukiwarki adresy, których nie było" | zgłoszenie 23 URL do Indexing API; miesiąc później „API tu nie działa" (`2026-07.md` l.144) | częściowy |
| `M06` l.51 | 03.07 | 4 artykuły lipca: ha, jak wapnować, tlenkowe vs węglanowe, pH gleby | powstały 3 inne + przebudowa huba; „tlenkowe vs węglanowe" nigdy, pH → T-080 (20.10) | tak |
| `M07` l.18 | 03.08 | „4 artykuły eksperckie" | 3 nowe + hub; 3 z 4 nowych nigdy niepobrane | tak |
| `M07` l.19 | 03.08 | strona stabilizacji — „najbardziej wartościowe hasło w projekcie" | sierota (0 linków do 24.08), nigdy niepobrana; 24.08: „nie ma popytu, nie wracamy" (rejestr T-026) | tak |
| `M07` l.21 | 03.08 | „każdy produkt ma jeden jednoznaczny adres" | 19/19 produktów odpowiadało 200 pod **dwiema** bazami do 19.08 (T-028) | tak |
| `M07` l.62 | 03.08 | „części treści Google nie pobrał… efekt w 2. połowie sierpnia" | 5 z 6 nowych stron nieznanych Google; 24.08: 0 z 10; 09.09: 0 z 4 Fazy 0 | tak |
| `M07` l.74 | 03.08 | „są strony docelowe pod konkretne zapytania" | jedyny landing = sierocy stabilizacji; `/wapno-granulowane/` = 404 | tak |
| `ADS3M` l.146 | 06.08 | „budujemy strony docelowe pod wapno granulowane" | strona 0 bajtów 06–13.08, potem `noindex`; zmiana „indeksowalne → poza indeksem" **niezakomunikowana** | tak |
| `ADS3M` l.157 | 06.08 | X: „strona i treści pod stabilizację gruntów" | strona istniała od 14.07 i była zgłoszona jako gotowa 03.08 | tak |
| `ADS3M` l.156 | 06.08 | X: rozszerzamy Ads o wapno palone | landing `/wapno-palone/` unieważniony 11.08; brak pozycji w rejestrze | otwarty |
| `M08` l.32 | 31.08 | „trzy nowe strony ofertowe… celem reklam… otwiera segment rybacki" | dwie z trzech `noindex` — **przemilczane**; staw niepobrany | tak |
| `M08` l.36 | 31.08 | „pierwsze z nich [treści z lipca] już weszły" | weszły 2 karty produktów, treści z lipca nadal nie | tak |
| `M08` l.34 | 31.08 | „trafia dziś na Waszą kartę" | 8 z 19 kart poza indeksem 24.08 — brak w mailu | częściowy |
| `STRAT` l.127, 136 | ost. commit 03.08 | M3 landingi indeksowalne, M4 segmentowe + menu | ADR 11.08 unieważnia oba; Sadownictwo 30.11, Hurtownie VII 2027 | tak — nigdy niezakomunikowany |

**Czy klient dowiedział się o zmianach architektury:**

| decyzja | zakomunikowana? |
|---|---|
| landingi poza indeksem (11.08) | **brak zapisu** — jedyny ślad `M08` l.32 „są celem reklam", bez słowa o `noindex`; grep `noindex|poza indeks|hub|spoke|klasteryz` po czterech mailach: 0 trafień |
| hub i spoke, klaster po pytaniu (21.08) | **brak zapisu** |
| „kategoria segmentowa to wymyślony podział", zmiana nazw kategorii (21.08) | **brak zapisu** — klient ma na piśmie plan segmentowy z `M06` l.37–40 |
| 0 z 10 nowych adresów w indeksie (24.08) | **brak zapisu**; `M08` l.36 mówi odwrotnie |

Wniosek: **klient ma na piśmie architekturę z czerwca (segmenty, indeksowalne landingi, 4 artykuły/mies.), a strona realizuje
architekturę z sierpnia, o której nie został poinformowany.** Rozjazd między raportem a stroną jest w każdym z trzech miesięcy.

---

## 8. Decyzje architektoniczne podjęte przeze mnie bez zapisanego akceptu Janka

**Uwaga metodyczna.** Rejestr i ADR-y pisałem ja. Oznaczenia `[J]` / „decyzja Janka" pojawiają się systematycznie **dopiero od
19–21.08** (przebudowa rejestru). Wcześniej akcept jest zapisany tylko tam, gdzie ADR wymienia Janka w statusie (15.06, 08.07).
Brak `[J]` przed 19.08 nie dowodzi braku akceptu — dowodzi **braku zapisu**, i tak to klasyfikuję. Pełna tabela 17 decyzji
z cytatami: analiza cząstkowa w tym wątku.

### A. Decyzje Janka (z zapisem w źródle)

| data | decyzja | źródło |
|---|---|---|
| 20.02 | segment poza adresem produktu; segment = strona docelowa z frazą intencyjną (landingi rolnicy / stawy / oczyszczalnie) | archiwum Drive §6.1 (`DECYZJA`) |
| 27.02 | WooCommerce w trybie katalogu; 7 kategorii = segmenty z PIM; 1 produkt = 1 `simple` | archiwum §4.1–4.2 |
| 13.03 | treść kart przez n8n DescWriter; podział fraz: karta → nazwa produktu, kategoria/landing → fraza intencyjna | archiwum §5, §6.1 |
| 10.09 | źródło prawdy o produktach = karty AGRII na `/do-pobrania/` (z papierowego katalogu); produktów i parametrów nie ruszamy; architektura wokół listingów i kart | polecenie w tej sesji |
| 15.06 | oferta = 19 produktów, drogownictwo poza ofertą, Kreda czarna zostaje | ADR katalogowy „(Janek)" |
| 08.07 | rdzeń URL: jedna kategoria per produkt wg katalogu drukowanego, 19×301, Hurtownie poza `product_cat`, Sadownictwo/Rybactwo bez produktów; odrzucenie mu-pluginu („Od kiedy tak robimy?") | ADR „zaakceptowany (Janek, 2026-07-08)" |
| 30.07 | 3 pozycje menu → `draft`, „wrócą z prawdziwymi landingami" | tylko memory `project_agria_nav_debt_m4` |
| 13.08 | pozycjonowanie Ads „dostawca całosamochodowy"; landing z gotowego wzorca, nie od zera | ADR 13.08; memory `feedback_agria_landingi_wzorzec…` |
| 19.08 | dwie warstwy cen; poradnik cenowy odrzucony; „jedna cena na kartę zamiast dwóch" | ADR 19.08 ×2; commit `1a6896b` |
| 21.08 | terminarz jako hub osi KIEDY `[J]`; nazwy kategorii bez segmentów `[J]` („kategoria segmentowa opisuje wymyślony podział, nie towar"); kierunek T-068 (produkty pod `/wapno/<produkt>/`); zdjęcie reguły 301 pod landing stawu „za zgodą Janka"; Rank Math w edytorze „na polecenie Janka"; listingi na landingach (T-064, „szkoda, że nie ma listingu"); zgłoszenie układu na całą szerokość (T-063); T-060 zaparkowane | trzy ADR-y 21.08; dziennik T-056/T-063/T-064 |
| 24.08 | całość ADR rozstrzygnięć: T-073 hub nie powstaje, T-075/T-079 unieważnione, T-082/T-076 → VII 2027, blok F na kategorii, Faza 0 „zero nowych adresów", „jeden adres = jeden wiersz"; T-026 z czterech scenariuszy; higienizacja zostaje osobnym adresem; T-095 usunięcie termu 766 „na akcept rekomendacji"; piąta reguła 301 „na polecenie Janka"; T-101 `[J]` | ADR „(decyzja Janka 24.08)"; dziennik |
| 08.09 | frakcja bez przypisania do gatunku (T-078) | rejestr Faza 1 |
| 09.09 | ręczne zgłoszenia GSC; `/rodo/`; powielenie zdjęć | rejestr Kontrola 15.09, T-127/T-128 |

### B. Decyzje moje, bez zapisanego akceptu — to jest lista, o którą prosił Janek

| # | data | decyzja | co ją potem spotkało |
|---|---|---|---|
| 1 | 08.07 | **301 trzech pustych kategorii na `/oferta/`** — ADR mówił o 301 „stary→nowy", nie o archiwach; pytanie A/B z 09.07 „nie ruszać bez decyzji" — **odpowiedź nigdzie niezapisana** | 14.07 sam napisałem: „301 poszło, landingi nie powstały. Zła kolejność." 301 zostało do dziś |
| 2 | 15.06 / 14.07 | **landing `/wapno-do-stabilizacji-gruntow/`** — brief powołuje się na „decyzję 15.06", ale ADR z tego dnia rozstrzyga produkt (#320), nie zleca landingu; publikacja 14.07 bez akceptu treści | parametry skorygował Janek (karta Nordkalk); pomiar: brak popytu, sierota (T-026, T-089) |
| 3 | 09.07 | **cztery poradniki jednego dnia + kategoria wpisów „Zastosowania"** — prompt wątku kazał „draft do akceptu Janka PRZED publikacją", w `POMIAR_POD_WYNIK` zero zapisów akceptu | 3 nigdy niepobrane; `/ile-wapna-…/` scalony jako dublet (24.08); kategoria 831 = duplikat `/poradniki/` (T-099, otwarte) |
| 4 | **14.07** | **architektura sześciu landingów exact-match** (`ROZPISKA` §6) — wzorzec Biovity wskazał Janek, wniosek architektoniczny mój; jedyne „do decyzji Janka" dotyczyło starych URL-i i **też nie ma odpowiedzi** | sam wycofałem 11.08 („błąd analityczny", „jeden punkt danych") |
| 5 | 06.08 / 14.08 | **`/wapno-granulowane/` i `/wapno-nawozowe/`** — „KROK A, bez tego nie ruszamy" w prompcie M3 (moim) | `/wapno-granulowane/` pusty tydzień z reklamami (korekta Janka 13.08) |
| 6 | **11.08** | **ADR podziału ról w całości**: landingi tylko Ads, poza indeksem; 4 landingi skasowane (T-035); landingi segmentowe (T-036) i huby (T-038) unieważnione. Dokument prosił o „zatwierdzenie podziału ról z §5" — **zero zapisów odpowiedzi**. Korekta reguły 21.08 (T-052) — też moja | obowiązuje do dziś; hipoteza 5 (landing vs kategoria w Ads) nigdy niezmierzona |
| 7 | 13.08 | **`noindex` na dwóch landingach** — ADR 11.08 zostawił to „do rozstrzygnięcia", ADR 13.08 §5 domknął bez `[J]` | obowiązuje |
| 8 | 19.08 | **ceny na dwóch landingach Ads** — brief z 06.08 mówił „na samym landingu ceny nie stawiamy nawet po jej otrzymaniu"; odwrócone z uzasadnieniem z Ads API, bez `[J]` | „od 36 zł/t" (możliwa literówka cennika) stało nad zgięciem na stronie docelowej reklam do 07.09 |
| 9 | 21.08 | **struktura hub + 3 spoke'i + próg URL** (≥3 frazy, ≥100/mies.) — impuls Janka („hub wyczerpuje frazę"), trzy poziomy, próg i terminy moje, status bez `[J]` | hub unieważniony po 3 dniach (T-073), łąki zdjęte, ozime → 2027 |
| 10 | 21.08 | **zwolnienie slugu kategorii 766 → `rybactwo-kat-archiwum`** i zmiana slugu landingu na `wapno-do-stawu` | `/wapno-do-stawow/` 404 do 24.08 (T-072); term usunięty 24.08 (T-095) |
| 11 | 21.08 | **odłożenie T-068 (przebudowa adresów) na zimę** — kierunek Janka, argument „szczyt w październiku" mój, zgoda na termin niezapisana | argument sezonowy sam obaliłem 24.08 (szczyt = sierpień) |
| 12 | 21.08 | T-065 sadownictwo dopisane bez `[J]`; kolejność „staw przed glebą" wystawiona do rozstrzygnięcia — bez odpowiedzi | — |
| 13 | 04–08.09 | **zakres i treść T-092/T-078** — zlecone moim audytem, objęte ADR-em 24.08 (Janek), ale treść bez odrębnego akceptu; T-092 „zweryfikowane w HTML, nie wizualnie" | kontrola 18.09 / 26.09 |
| 14 | 07–09.09 | **plan wrześniowy T-116…T-128, T-117 karty granulowane, przesunięcie T-074** — commit „odpowiedzi Janka 07.09" dotyczy wyłącznie ceny 36 zł/t, dolomitu, Nordkalku i GBP, nie planu | teza „krótszy tytuł" sam odrzuciłem 07.09 |
| 15 | 07.09 | zamknięcie T-063 bez przebudowy landingów — „własną decyzją wykonawczą" | — |

**Pytania „do decyzji Janka", na które nigdy nie zapisałem odpowiedzi:** 09.07 (A/B menu vs płaskie URL-e) · 14.07 (odtworzyć
`/wapno-do-sadu/` i `/wapno-nawozowe-hurt/` czy nowa architektura) · 11.08 (zatwierdzenie podziału ról, backlog 39 fraz,
wizytówka w sierpniu) · 21.08 (staw przed glebą, paszarstwo na 8, blok F — to ostatnie rozstrzygnięte 24.08).
**Cztery razy zadałem pytanie o architekturę i cztery razy wykonałem własny wariant, nie czekając na odpowiedź** — albo
odpowiedź padła ustnie i jej nie zapisałem; z repo tego nie da się rozstrzygnąć.

### C. Decyzje moje wycofane lub skorygowane

**Przez Janka:** parametry landingu stabilizacji (14.07) · wzorzec landingu, nie Elementor od zera (13.08) · dwie kwoty na kartach
(19.08) · układ landingów T-063 i brak listingów T-064 (21.08) · „jakie wapno na pole" jako jedna strona (21.08) · „loco" i żargon (13.08).

**Pomiarem (moim własnym, po fakcie):** sześć landingów i wzorzec Biovity (11.08) · cztery poradniki bez crawlu i dublet
`/ile-wapna-…/` (06.08, 24.08) · landing stabilizacji bez popytu (24.08) · hub `/jakie-wapno-na-pole/`, spoke łąki, spoke ozimin
(24.08) · połowa diagnozy T-026 (24.08) · T-069 (24.08) · trzy liczby sezonowe i „XI to 40" (24.08) · wolumen tonażowy „490" (24.08) ·
teza „od 9 lipca żadnej treści" (21.08) · „8 kart poza indeksem" i „mechanizm Fazy 0 potwierdzony" (09.09) · „211 stron
niezindeksowanych" (09.09) · teza „krótszy tytuł = CTR" (07.09) · KR z 19.05 — trzy błędy metody (21.08) · T-086 passthrough (24.08).

**Wzorzec, który z tego wynika:** decyzje architektoniczne zapadały u mnie **z rozpiski wolumenów** (14.07, 21.08, 07.09), a ich
cofnięcia przychodziły **z pomiaru po 3–21 dniach** — za każdym razem wykonanego dopiero po zbudowaniu adresu, nie przed.

---

## 9. Odpowiedzi na dziesięć pytań

### 1. Jaka była pierwotna klasteryzacja, kto ją ustalił, gdzie zapisana

**Dwie różne „pierwotne" klasteryzacje, obie po zastosowaniu / odbiorcy:**

- **Strona (Q1 2026, budowa):** 7 kategorii `product_cat` — Rolnictwo, Sadownictwo, Rybactwo, Oczyszczalnie, Budownictwo,
  Hurtownie, Paszarstwo (term 764–770, założone jednym ciągiem), produkt w wielu kategoriach naraz, ten sam podział
  w atrybucie `pa_agria-segment` i w filtrze JetSmartFilters na `/oferta/`. Logika: **po zastosowaniu towaru** (segment
  z katalogu drukowanego, brief `HISTORICAL_BRIEF_2026-02-05.txt`: Rolnictwo / Rybactwo / Oczyszczalnie / Budownictwo /
  Drogownictwo). Kto: Auranet przy budowie — **brak zapisu decyzji w repo** (repo dokumentacyjne powstało 19.05, strona
  była gotowa). W `docs/sesje/2026-08-19-…` l.184–186 to stan zastany („Kategorie: Rolnictwo, Sadownictwo, Rybactwo…").
- **SEO (19–20.05, Claude):** 8 klastrów fraz regexem po tych samych segmentach (`KEYWORD_RESEARCH` l.23), 20.05 zrównane
  1:1 z kategoriami: „każdy z 5 segmentów (+ hurt + paszarstwo) ma dedykowaną kategorię … nie budujemy landing pages od zera,
  optymalizujemy istniejące" (`ONPAGE_PLAN` l.51). Zapis akceptu Janka: **brak** — ani w KR, ani w ONPAGE, ani w M1_KICKOFF.

**Korekta wersji 2:** kategorie nie są „bez zapisu" — to segmenty z PIM zaimportowane 27.02 z decyzji Janka (archiwum Drive §4.2).
Klasteryzacji fraz przed majem nie opracowano w żadnym wątku (archiwum §6.3); obowiązywały dwie decyzje: segment = strona docelowa
z frazą intencyjną (20.02) i podział ról fraz karta/kategoria (13.03). To, co Janek pamięta („kategorie z listingiem, filtry,
treść nad i pod"), jest stanem strony z budowy. Plan z 20.05 go powtórzył; wszystko od 14.07 od niego odchodziło.

### 2. Skąd dwie puste kategorie (Sadownictwo, Hurtownie) i dlaczego są puste

**ADR 08.07 (Janek).** Przyczyna techniczna: Premmerce bez Yoasta wybiera do adresu kategorię o najwyższym `term_id`, więc
13 produktów siedziało pod `/wapno-nawozowe-hurt/…`. Model A: jedna kategoria wiodąca per produkt wg pierwszego badge'a katalogu
drukowanego — a **żaden produkt nie ma Sadownictwa ani Rybactwa jako pierwszego badge'a**, Hurtownie „nigdy pierwsze".
Skutek zapisany w ADR: „archiwa Rybactwo/Sadownictwo/Oczyszczalnie znikają jako `product_cat` (zostają w filtrze;
**landing per segment osobno wg planu KR**)" (`URL_TAXONOMY_SIM` l.84). Puste archiwa → 301 na `/oferta/` (08.07), menu → `draft` (30.07).

**Dlaczego nadal puste:** obiecany „plan KR" landingów segmentowych **nie istniał** (KR l.237 planował dwa pillary, nie landingi
per segment). `ROZPISKA` 14.07 l.29 nazwała to wprost: „ADR z 2026-07-08 zakładał, że w miejsce znikających archiwów wchodzą
landingi per segment. 301 poszło, landingi nie powstały. Zła kolejność." Potem T-036 (landingi segmentowe) unieważnione 11.08,
sad przesunięty na T-083 (30.11), hurt na T-082 (VII 2027). Rybactwo dostało landing 21.08 i kategoria została usunięta 24.08.
Koszt zmierzony: `/wapno-do-sadu/` rankował #11 na 30/mies. i trzyma poz. 9,4 mimo 301; `/wapno-nawozowe-hurt/` — 1 klik w 90 dni („ranking-widmo").

### 3. Kiedy i dlaczego powstała warstwa landingów, czyja to decyzja

**Korekta wersji 2:** sama idea landingu segmentowego jest starsza i należy do Janka — decyzja z 20.02 („segment = strona docelowa
z frazą intencyjną": rolnicy, stawy, oczyszczalnie). Do 19.05 żaden taki landing nie powstał. Poniższe trzy kroki są moje
i odeszły od tej decyzji: stabilizacja to nowy „segment", a 14.07 oś zmieniła się z odbiorcy na formę produktu.

Trzy kroki, każdy mój, żaden z zapisanym akceptem:

| krok | data | co | przesłanka | akcept Janka |
|---|---|---|---|---|
| a | 15.06 | brief `LP_STABILIZACJA_GRUNTU` — „LP (nowa), NIE produkt" | fraza 720/mies., CPC $2,13 (rozpiska KR); zakres „bez kruszywa" to decyzja Janka, forma „osobna strona" — moja | **brak zapisu**; publikacja 14.07 |
| b | 09.07 | 4 poradniki + kategoria wpisów „Zastosowania" jako „dom dla landingów segmentowych" | pomiar SERP 08.07 (poradniki rankują) | **brak zapisu** („drafty do akceptu Janka przed publikacją" — bez śladu akceptu) |
| c | **14.07** | `ROZPISKA`: sześć landingów exact-match `/wapno-nawozowe/`, `/wapno-granulowane/`, `/wapno-palone/`, `/wapno-hydratyzowane/`, `/wapno-magnezowe/`, `/kreda-nawozowa/` | „Biovita jest #1 na «wapno nawozowe» landingiem bez cen" (wzorzec **wskazany przez Janka**, wniosek mój) + wolumeny head + „okno sezonowe zamyka się teraz" | **brak zapisu**; jedyne „Do decyzji Janka" dotyczy starych URL-i |

Bezpośredni bodziec dla (c): zgłoszenie Janka 14.07, że `/wapno-nawozowe-hurt/` przekierowuje na `/oferta/` — audyt tego
zgłoszenia przerodził się w nową architekturę. **Sam pomiar z tego dnia mówił coś odwrotnego** (wszystkie 6 rankujących fraz
to poradniki, zero produktowych) — rozpiska poszła wbrew pomiarowi, za wzorcem jednego konkurenta.

11.08 obaliłem własny wzorzec („błąd analityczny", Biovita = hurtownia ogrodnicza), ale **nie skasowałem warstwy** — zostawiłem
dwa landingi jako cele Ads (kampania startowała 14.08 i potrzebowała stron docelowych), z treścią pisaną pod indeks.

### 4. Czym miało być `/wapno-granulowane/`, jakie produkty, z których kategorii

- **Geneza:** fraza `wapno granulowane` **nie występuje w KR 19.05** (jest tylko „wapno nawozowe granulowane" 390 → mapowane
  na karty #314/#317/#305). Pojawia się 14.07 w tabeli „Gdzie realnie leżą pieniądze": 5 400/mies., szczyt „14 800 (sie)"
  (`ROZPISKA` l.92) — 06.08 ten szczyt to już 9 900, bez komentarza.
- **Czym miało być:** nie kategorią i nie produktem — **przekrojem po formie (granulat) przez trzy produkty jednej kategorii**,
  typ „produktowy landing kategorii, wzorzec Biovity, exact-match slug/title/H1, bez ceny i koszyka" (`ROZPISKA` l.137–139).
  06.08: „podwójna funkcja: strona docelowa Ads **oraz** landing komercyjny pod sezon", `robots: index, follow` (`LP_WAPNO_GRANULOWANE` l.5, 21).
  11.08: wyłącznie cel Ads. 13.08: `noindex`. 07.09: T-117 przenosi pracę na karty.
- **Produkty (T-064, 21.08):** #314 `weglanowe-granulowane`, #317 `weglanowe-magnez-granulowane`, #305 `kreda-nawozowa-granulowana`
  — **wszystkie trzy z jednej kategorii `wapno-nawozowe-rolnictwo` (764)**. Landing nie łączy więc niczego, czego nie łączy kategoria.
- **Stan:** strona 2751 utworzona 06.08 **pusta** (0 bajtów) do 13.08, z reklamami zaplanowanymi na 14.08; treść wstawiona 13.08
  z `docs/seo/lp/wapno-granulowane.html`; cena „od 350 zł/t" 19.08; listing 21.08; `noindex` od 13.08; 0 wyświetleń organicznych.
  Makieta, którą Janek ogląda: `mockups/lp-wapno-granulowane-2026-08-06.html`.

Janek ma rację co do bytu: „wapno granulowane" jako osobny adres istnieje **wyłącznie dlatego, że w rozpisce z 14.07 stała liczba 5 400**.

### 5. Dlaczego landingi mają `noindex`, kiedy ustawiono, czemu mają treść SEO

- **Kiedy:** 13.08, przy uruchamianiu kampanii (`docs/decyzje/2026-08-13-uruchomienie-kampanii-ads.md` §5: „Oba: `noindex, follow`
  — domknięcie luki z ADR 11.08, gdzie izolacja opierała się wyłącznie na tym, że Google nie odkrył adresów"). ADR 11.08 z 13.08
  odnotował, że landingi miały jeszcze `index, follow`. Decyzja moja, w ramach ADR bez `[J]`.
- **Dlaczego:** zmierzona kanibalizacja — „wapno bielik" 6 własnych URL → najlepsza poz. 15,3; frazy z jednym URL w TOP10;
  kategoria właśnie wchodziła na 10,9 na „wapno nawozowe" w miesiącu szczytu. Ads nie wymaga indeksacji, więc landing mógł
  zostać celem reklam bez dokładania drugiej strony na frazę (ADR 11.08, dowody A–D).
- **Tylko dwa mają `noindex`** — patrz §1. `/wapno-do-stawu/` i `/wapno-do-stabilizacji-gruntow/` są indeksowalne i mimo to
  nieobecne w indeksie (nigdy niepobrane).
- **Czemu rozbudowana treść SEO na stronach poza indeksem:** bo treść powstała **06.08 pod indeks** („index, follow", frazy
  sekundarne, FAQ, schema `FAQPage`), a decyzja o `noindex` zapadła tydzień później i treści nie ruszyła. ADR 11.08 zostawił
  furtkę: hipoteza 5 („landing konwertuje taniej niż kategoria → po sezonie może dostać rolę organiczną") — **nigdy niezmierzona**.
  Z punktu widzenia Ads treść ma sens (ocena jakości strony docelowej), ale ocena jakości jest „poniżej średniej" na 34 z 37 fraz (T-113).

### 6. Czy karty produktów były robione pod SEO i jakim mechanizmem

Tak — **workflow n8n DescWriter** (Gemini, workflow z LAGUZ, 13.03) napisał treść 19 kart z kotwicami H2, FAQ i CTA oraz wygenerował
title, description i focus keyword w Rank Math (focus = nazwa produktu, zgodnie z decyzją o podziale fraz z 13.03) — archiwum Drive §5;
w bazie 19/19 kart ma tag `content-done`. Audyt 20.05 zastał to jako „RankMath 19/19" (`ONPAGE_PLAN` l.16, 213–215). Treść kart pochodziła z PIM-u AGRII, **nie z kart
producentów** — te weszły jako źródło dopiero 15.07 (naprawa parametrów w 4 warstwach, commit `6a70484`), z 17 PDF-ów na
`/do-pobrania/` (tam od 29.06). Trzy karty (#303, #304, #316) do dziś nie mają karty producenta. Edycje po 29.06 szły przez MCP (`update_post_content`, `query_db_write`, `update_postmeta`); trzy karty
(307, 310, 320) renderują z `_elementor_data`. Udokumentowane: `docs/catalog/PLAN_NAPRAWY_PARAMETROW_2026-07-14.md`,
`docs/prompty/wdrozenie/T-010-ceny-w-tresci-15-kart.md`, dziennik M1–M2 w rejestrze (z zastrzeżeniem „daty per pozycja
nieodtworzone"). Szczegóły: §7.1.

### 7. Co mówią ADR 11.08 i 21.08 — czy landingi są z nimi zgodne

**ADR 11.08 (podział ról):** landing = narzędzie konwersji ruchu płatnego, nie rankingu; `/wapno-granulowane/` i `/wapno-nawozowe/`
poza indeksem; cztery pozostałe nie powstają; kategoria 764 = **jedyna** strona organiczna na „wapno nawozowe"; organik idzie
treścią poradnikową (Polcalc 95% z bloga). Kontrole 01.09/01.10/01.11, hipotezy 1–5.

**ADR 21.08 (hub i spoke, bez `[J]`) + terminarz `[J]` + nazwy kategorii `[J]`:** oś = pytanie (JAKIE / KIEDY / ILE / uprawa), próg URL
≥3 frazy i ≥100/mies. z GSC, hub bez H2 uprawowych; **segmenty powstają jako landingi z ręcznym listingiem** (wzorzec
`/wapno-granulowane/`), bo „kategoria segmentowa opisuje wymyślony podział, nie towar" (Janek); przebudowa adresów na zimę (T-068).

**Zgodność czterech landingów:**

| landing | ADR 11.08 | ADR 21.08 | uwaga |
|---|---|---|---|
| `/wapno-nawozowe/` | zgodny (cel Ads, `noindex`) | — | ale **strona główna** celuje title w tę samą frazę — to łamie „jedyna strona organiczna" (zmierzone 04.09: główna 6,5 / kategoria 11,0) |
| `/wapno-granulowane/` | zgodny (cel Ads, `noindex`) | wzorzec „landingu z listingiem" | T-117 przenosi treść na karty = organicznie zbędny |
| `/wapno-do-stabilizacji-gruntow/` | **sprzeczny** — indeksowalny landing organiczny na frazę bez popytu, nie jest celem żadnej kampanii | próg URL niespełniony (planer `null`, GSC 0) | 24.08 jednocześnie „Unieważnione" (T-026) i w Fazie 0 (T-089) — dwie kwalifikacje jednego dnia |
| `/wapno-do-stawu/` | **sprzeczny z T-036** („landingi segmentowe `/wapno-do-stawow/` … unieważnione 11.08, menu wraca z treścią, nie z landingami") | **zgodny** — dokładnie „segment jako landing z listingiem" `[J]`; klaster 4 100/mies. spełnia próg | jedyny landing z pomiarem popytu; nigdy niepobrany |

Wniosek: dwa landingi Ads są zgodne z 11.08, `/wapno-do-stawu/` jest zgodny z 21.08 i sprzeczny z własnym rejestrem z 11.08,
`/wapno-do-stabilizacji-gruntow/` nie jest zgodny z żadnym z dwóch ADR-ów i istnieje siłą bezwładu od 14.07.

### 8. Które decyzje podjąłem sam, bez akceptu Janka

Osobna lista w **§8.B** — piętnaście pozycji, w tym trzy, które zbudowały warstwę landingów (15.06/14.07, 09.07, 14.07),
ADR 11.08 w całości i `noindex` z 13.08.

### 9. Co realnie pracuje — GSC per warstwa

Tabela w §6. Skrót: poradniki/hub 69,7% wyświetleń i 151 kliknięć, karty 15,9% i 76, strona główna 6,3% i 70, kategorie 5,8% i 23,
**landingi 0 i 0**. Jedyna warstwa z kliknięciami produktowymi to karty (Oxyfertil 90 CTR 5,1%, Agrobielik 70 5,2%, Bielik 2,2%) —
czyli **poziom, który Janek nazwał „każdy produkt ma swoją kartę robioną pod SEO"**, pracuje lepiej niż wszystko, co dobudowałem obok.

### 10. Czy architektura bez warstwy landingów ma sens i co kosztuje przejście

Zgodnie z §4 promptu nie proponuję przebudowy — podaję, co mówią dane i co kosztowałoby przejście, decyzja jest Janka.

**Korekta wersji 2:** pierwotny plan (20.02) to nie „kategoria z opisem + karty", tylko kategorie + karty + landingi segmentowe
na frazy intencyjne. Pomiar 10.09 przesuwa ciężar jeszcze dalej: **zapytania ofertowe przychodzą z kart** (6 z 11) i ze strony
zamówień (4), nie z kategorii ani landingów. Rekomendacja i decyzje D1–D4: `docs/strategy/2026-09-10-SCIEZKA-SEO-I-SPRZEDAZY.md`.

**Co mówią dane za wariantem „kategoria z opisem + karty":**
- To jest to, co od 24.08 daje mierzalny ruch: kategoria 764 po rozbudowie ma 992 wyświetlenia, karty 4 653; landingi 0.
- Wszystkie cztery cofnięcia URL-i (T-073, T-075, T-082, T-076) i T-117 idą już w tę stronę: „rozbudowuj istniejące strony,
  nie buduj nowych" (memory `nowe_adresy_nie_wchodza_do_indeksu`).
- Jedyny argument za landingiem, który został — „strona docelowa Ads konwertuje lepiej niż kategoria" — nie ma pomiaru.

**Co kosztowałoby przejście (wycena zakresu, nie rekomendacja):**

| element | co trzeba zrobić | koszt / ryzyko |
|---|---|---|
| `/wapno-nawozowe/` (Ads) | przekierować kampanie Rolnictwo/Marka na kategorię 764 (`ads_build_campaigns.py`, pole `final_urls`), 301 landingu na kategorię; sekcje z LP już częściowo w opisie kategorii (T-092) | ~1–2 h; reset historii Quality Score na 37 frazach; kategoria nie ma bloku „oddzwonimy" i ceny nad zgięciem (T-059) — do przeniesienia albo świadomej rezygnacji |
| `/wapno-granulowane/` (Ads) | cel Ads → karta #314 lub kategoria; treść → karty #314/#317/#305 (T-117 już to planuje); 301 | ~1 h + T-117 (w kolejce, 20.09) |
| `/wapno-do-stabilizacji-gruntow/` | treść → karta #320 i opis `/wapno-do-oczyszczalni/`; 301 na kartę | ~1 h; zero ruchu do utraty; wypada obietnica „październik — stabilizacja gruntów" z maila do Kasjana 06.08 (do przeformułowania) |
| `/wapno-do-stawu/` | **nie ma dokąd wrócić** — kategoria Rybactwo nie może mieć produktów bez zmiany ich adresów (Premmerce sortuje po `term_id`), term 766 usunięty 24.08. Zostaje jako jedyny landing albo wraca jako kategoria dopiero po T-068 (przebudowa adresów, XII–II) | 0 h teraz; decyzja przy T-068 |
| Sadownictwo / Hurtownie | jako kategorie nie mogą mieć produktów z tego samego powodu; „kategoria z opisem" dla nich = T-068 albo landing z listingiem (T-083, T-082) | XII–II |
| menu i kafle `/oferta/` | 3 pozycje `draft` — decyzja, czy wracają jako landingi, czy zostają zdjęte | 0,5 h |
| strona główna | title bez „wapno nawozowe" na pierwszym miejscu (kanibalizacja z kategorią, 04.09) | 0,5 h, niezależne od landingów |

Suma dla trzech landingów do wchłonięcia: **~4–5 h pracy** plus T-117 (już zaplanowane) i jedno okno na przestawienie Ads.
Ograniczenie twarde: dopóki adres produktu zawiera kategorię, **segment bez produktu wiodącego nie może być kategorią**
— to jest powód, dla którego 21.08 powstał wzorzec „landing z listingiem". Pełne odejście od landingów segmentowych wymaga T-068.

---

## 10. Jedno zdanie na koniec

**Obecna architektura nie ma uzasadnienia w danych: warstwa landingów w obecnym kształcie powstała z rozpiski wolumenów (14.07)
i wzorca, który sam obaliłem trzy tygodnie później, odeszła od decyzji z 20.02 (landing segmentowy na frazę intencyjną), przynosi
0 wyświetleń organicznych i jedno zapytanie ofertowe — a sprzedaż strony idzie przez karty produktów, które przez ten czas
przerabialiśmy najmniej.**
