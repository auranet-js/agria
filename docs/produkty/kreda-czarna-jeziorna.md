# Kreda czarna(jeziorna) z kwasami humusowymi i węglem organicznym (WC #303)

> Karta AGRII: **BRAK** — produkt wycięty z katalogu drukowanego decyzją klienta (archiwum `docs/archiwum/2025-12_2026-05-HISTORIA_DECYZJI_claude-ai.md`
> §9.2: „❌ decyzja klienta — pomijamy (⚠️ nadal w WC)") · karta na stronie: `/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/` ·
> kategoria dziś: Wapno nawozowe (`/wapno-nawozowe-rolnictwo/`, term 764) · SKU: brak w schemacie · **stan na 10.09.2026**
>
> **Źródła (skróty używane niżej):**
> **[R]** render karty 10.09 17:33, `data/produkty/render/kreda-czarna-jeziorna.{html,json}` — **stan strony, nie źródło prawdy** ·
> **[GK]** grankal.pl, strona „Produkty" (plik `data/produkty/zewn/grankal-produkty.html`, pobrany 10.09 w równoległym wątku bazy) ·
> **[C]** `docs/operations/CENNIK_PAWEL_2026-08-07.md` · **[F]** `docs/FAKTY_KLIENTA.md` §3 ·
> **[OLX]** `data/olx/market/2026-08-28.json` (zrzut 28.08, 2 588 ogłoszeń)
>
> **Zasada dla tego pliku:** bez karty AGRII nie ma źródła prawdy o parametrach. Wszystko w §1–§3 poza „brak karty" to **stan strony**
> (render i atrybuty WC, pisane 13.03 przez n8n DescWriter z danych PIM) — nie uzupełniamy tego ani z kart producentów, ani z rozumowania.

---

## 1. Tożsamość

**Karta AGRII: brak.** Poniżej wyłącznie to, co dziś pokazuje strona i baza.

| cecha | stan strony / bazy | źródło |
|---|---|---|
| nazwa WC (H1) | „Kreda czarna(jeziorna) z kwasami humusowymi i węglem organicznym" | [R] |
| title / nazwa w schemacie | „kreda czarna jeziorna kwasy humusowe CaO 44% \| AGRIA" (małe litery, inne brzmienie niż H1) | [R] |
| odmiana | brak atrybutu `pa_agria-norma` | [R] |
| marka | `pa_agria-marka` = „Grankal" | [R] |
| producent | „Grankal" (tabela i `pa_agria-producent`) · w taksonomii producentów Grankal ma 3 produkty [F] §4 | [R], [F] |
| producent — dane u źródła | „Grankal Spółka z ograniczoną odpowiedzialnością, Draby 21b, 98-355 Działoszyn" | [GK] |
| magazyn | widoczna tabela: „Draby (98-355) Niedomice ( 33-132)" · atrybut `pa_agria-lokalizacja`: **tylko „Draby (98-355)"** | [R] |
| forma / frakcja | „Granulat", „3-6mm" | [R] |
| formy dostawy | „Big-bag 600 kg, Worek 25 kg" (atrybut, lead, formularz) | [R] |
| cena | **brak** (w cenniku Pawła „brak / brak") [C]; na stronie brak sekcji ceny i brak `offers` | [C], [R] |
| katalog drukowany | brak (tekst `Agria-katalog-2026-05-04-web.pdf` nie zawiera „czarn" ani „jeziorn") | pdftotext 10.09 |

**Producent o podobnym produkcie** [GK] — źródło uzupełniające, **niezweryfikowane jako ten sam towar:** „Grankal HumiPlus — Ekologiczny środek
wapnujący na bazie kredy jeziornej… granulowany nawóz wapniowy, na bazie wysoko reaktywnej kredy jeziornej o wysokiej zawartości kwasów
humusowych oraz węgla organicznego. Osiągający 96,8% reaktywności!" — opis pokrywa się z nazwą WC #303 („kwasy humusowe, węgiel organiczny").
Na OLX konkurent sprzedaje „GRANKAL HumiPlus (kreda z humusami)" jako „czarną kredę" (§4.2).

## 2. Parametry

**Tabeli z karty AGRII brak.** Poniżej widoczna tabela „Specyfikacja techniczna" — **stan strony, nie parametry potwierdzone**:

| parametr | widoczna tabela [R] | atrybut `pa_*` [R] |
|---|---|---|
| Zawartość CaO | min. 44% CaO | min. 44% CaO |
| Reaktywność | ~70-90% | ~70–90% |
| Typ reakcji | Długodziałająca(bezpieczna) | = |
| Forma fizyczna | Granulat | = |
| Frakcja | 3-6mm | = |
| Zastosowanie funkcjonalne | Działanie długoterminowe, Odkwaszanie gleb lekkich i piaszczystych, poprawa struktury gleby | = |
| Efekt zastosowania | Wzrost pH | = |
| Dawkowanie | 1-6 t/ha | = |
| Szybkość działania | Długotrwałe (3-6 miesięcy) | = (`pa_agria-czas` „3-6 miesięcy") |
| Dodatkowe zastosowanie | Gospodarstwa ekologiczne, sadownictwo, uprawy wieloletnie | = |
| Segment | Hurtownie, Rolnictwo, Sadownictwo | = |
| Magazyn | Draby (98-355) Niedomice ( 33-132) | **Draby (98-355)** |
| Producent | Grankal | = |
| Dostępność | Cały rok | = |

Brak na stronie i w bazie: zawartości kwasów humusowych i węgla organicznego (są w nazwie produktu, nie ma ich wśród parametrów), MgO,
odczynu, metali ciężkich, wilgotności. Atestu i karty producenta na `/do-pobrania/` brak.

## 3. Zastosowania

**Karta AGRII: brak.** Stan strony (niepotwierdzony kartą): „długoterminowego odkwaszania gleb lekkich i piaszczystych, poprawiając ich strukturę",
„rolnictwa, sadownictwa oraz gospodarstw ekologicznych", „uprawy wieloletnie"; dawka „1–6 t/ha"; czas „3-6 miesięcy".
Twierdzenia opisowe strony bez żadnego źródła: „zwiększając ich zdolność do zatrzymywania wody i składników odżywczych oraz wspierając mikroflorę",
„stopniowym i bezpiecznym uwalnianiem składników".

## 4. Z czym go porównać

### 4.1 Produkty AGRII — z kart PDF (dla #303 stan strony, oznaczony)

| | CaO | forma / frakcja | dawka | szybkość | producent · magazyny | formy dostawy | od zł/t netto |
|---|---|---|---|---|---|---|---|
| **#303 Kreda czarna** (stan strony) | min. 44% | granulat 3–6 mm | 1–6 t/ha | 3–6 mies. | Grankal · Draby (+ Niedomice w tabeli) | BB 600 kg, worek 25 kg | **brak** |
| #314 Węglanowe bez Mg granulowane (karta) | min. 50% | granulat 3–6 mm | 1–6 t/ha | 3–6 mies. | **Grankal**, Lhoist, Celiny · Niedomice, **Draby**, Tarnów Op., Celiny | BB 500/**600** kg, worek 25 kg | 350 BB · 25 kg → 380 |
| #317 Węglanowe z Mg granulowane (karta) | min. 31% CaO + 16% MgO | granulat 3–6 mm | 1–6 t/ha | 3–6 mies. | **Grankal** · **Draby**, Niedomice | BB **600** kg, worek 25 kg | 370 BB · 25 kg → 410 |
| #305 Kreda nawozowa granulowana (karta) | min. 50% | granulat 3–6 mm | 0,5–1,5 t/ha | 3–6 mies. | KZK Kornica · Kornica, Niedomice | BB 500 kg, worek 25 kg | 410 BB |

Fakty, bez wniosków: #303 dzieli z #314 i #317 producenta (Grankal), magazyn Draby, formę granulatu 3–6 mm, dawkę 1–6 t/ha i big-bag 600 kg.
#303 jest jedynym z czterech bez karty i bez ceny.

### 4.2 Konkurencja

| sprzedawca | co | cena | gdzie widoczny | źródło |
|---|---|---|---|---|
| **czarnakreda.pl** | „Nawozy dla rolników…", „odkwaszanie gleby kredą" — 3 wyniki w top 11 | niezmierzone | **abs 1** na `czarna kreda` i `czarna kreda granulowana`; abs 6 na `kreda nawozowa sypka`; abs 8 na `kreda jeziorna` | SERP 10.09 |
| sklep.activ.com.pl | „wapno-czarna-kreda-**bigbag-600kg**2-6" | niezmierzone | abs 3 | SERP 10.09 |
| ampol-merol, agrosimex (GreenCal), sklepydelta (600 kg), agrospec (Karbonann 20 kg; Eko-Calcium PGE luz), gardenstart (5 kg) | czarna kreda w różnych opakowaniach | niezmierzone | abs 7–21 | SERP 10.09 |
| kwbbelchatow.pgegiek.pl | „Kreda jeziorna surowa" | niezmierzone | abs 7 na `kreda jeziorna` | SERP 10.09 |
| **AGRO-KOTYNIA (OLX)** | 122 ogłoszenia z czarną kredą (m.in. „Wapno Granulowane TurboCal plus…, Czarna Kreda") | 180 (pole ceny OLX, jednostka niezweryfikowana) | OLX | [OLX] |
| „Tadeusz" (OLX) | „Kreda HumiPlus, Kreda z humusem (Czarna kreda)" — „Posiadamy w ofercie GRANKAL HumiPlus" | 370 | OLX | [OLX] |
| „Tomasz" (OLX), „Mateusz" (OLX, 2 konta, 4 ogłoszenia) | **„wapno kredowe odm. 07a [CZARNA KREDA]", big-bag 600 kg** · „Czarna kreda z humusami 07a" · „Eko-Calcium Czarna Kreda Jeziorna" luz 27 t | 420 · 400 · 54–60 | OLX | [OLX] |

**OLX, zrzut 28.08:** ogłoszeń z czarną/jeziorną kredą — **172, od 24 sprzedawców, AGRIA — 0**. W treści: „odm. 07a" w 5, „humus/hummus" w 21,
„600 kg" w 3, „Grankal" w 1, Bełchatów/PGE/Eko-Calcium w 4. Ceny innych (pole ceny OLX): min. 40, mediana 190, maks. 500 — jednostka
(za tonę / za big-bag) **niezweryfikowana**. Liczone po `user_id`.

## 5. Frazy — popyt

Wolumen i CPC: **planer Google Ads API** (konto AGRII, PL/polski, średnia 12 mies. 2025-08 … 2026-07), pobrane 10.09 →
`data/produkty/ads/kreda-czarna-jeziorna-planer.json` (pierwsze wywołanie zwróciło pusty wynik — prawdopodobnie limit zapytań przy równoległych
wątkach; ponowione po 20 s, komplet). „<10" = poniżej progu (**nie zero**). DataForSEO Labs 10.09: `data/produkty/dfs/sugestie-czarna-kreda.json`,
`sugestie-kreda-jeziorna.json` (CPC w USD). GSC: cały serwis, 2026-06-09 … 2026-09-06. Macierz: `data/produkty/macierz/kreda-czarna-jeziorna.csv`.

| fraza | typ | wyszukań/mies. | CPC śr. zł | szczyt (rok-mies.) | nasz serwis w GSC 90 dni |
|---|---|---|---|---|---|
| **czarna kreda** | nazwa | **720** | 0,51 | 2025-08: 1 300 | 3 wyśw. (#305 poz. 2, hub); **#303 brak**; SERP 10.09: AGRIA poza top 20 |
| **kreda jeziorna** | nazwa | **320** | 0,64 | 2026-06: 480 | #303 **3 wyśw. poz. 29,7**; SERP 10.09: AGRIA poza top 20 |
| czarna kreda granulowana | nazwa + forma | 140 | 0,33 | 2025-08: 210 | 4 wyśw., hub poz. 2; SERP 10.09: AGRIA poza top 20 |
| czarna kreda z hummusem (DFS Labs, pisownia „hummus") | nazwa | 140 | — | — | 2 wiersze: hub poz. 3, #303 poz. 5 („…ile na hektar", po 1 wyśw.) |
| kreda czarna | nazwa | 70 | 0,53 | 2025-08: 110 | 0 wierszy |
| wapno czarna kreda · czarna kreda wapno (DFS Labs) | nazwa | 70 · 50 | — | — | 0 wierszy |
| kreda czarna jeziorna · czarna kreda jeziorna | nazwa | <10 (planer) · 20 (DFS Labs) | — | — | 0 wierszy (w Ads: `czarna kreda jeziorna` 3 wyśw.) |
| kreda z kwasami humusowymi · czarna kreda z humusem · wapno kredowe czarne | nazwa | <10 | — | — | 0 wierszy |
| grankal | producent | **110** | 1,41 | 2025-08: 210 | 0 wierszy |
| grankal kreda · czarna kreda grankal · grankal draby | producent | <10 | — | — | 0 wierszy |
| czarna kreda bełchatów · kreda jeziorna bełchatów (DFS Labs) | źródło surowca u konkurencji | 40 · 40 | — | — | 0 wierszy (w Ads: 1 wyśw.) |
| czarna kreda do ogrodu · na trawnik · na pole | nazwa + zastosowanie | <10 | — | — | 0 wierszy |
| ile czarnej kredy na hektar | nazwa + dawka | 10 | — | 2025-08: 20 | **41 wyśw.**, hub poz. 8,4 |
| czarna kreda ile na hektar | nazwa + dawka | 40 | — | 2025-08: 90 | 17 wyśw., hub poz. 9,8 |
| czarna kreda dawkowanie · kreda jeziorna dawkowanie | nazwa + dawka | 20 · 10 | — | — | 0 · 1 wyśw. (#303 poz. 18) |
| czarna kreda cena | nazwa + cena | 70 | 0,53 | 2025-08: 140 | 1 wyśw. (#305 poz. 2) |
| czarna kreda cena za tonę (DFS Labs) | nazwa + cena | 90 | — | — | 0 wierszy (w Ads: 14 wyśw. 2 klik.) |
| kreda jeziorna cena | nazwa + cena | 40 | 0,49 | 2025-08: 70 | 1 wyśw. (#305 poz. 2) |
| czarna kreda big bag · czarna kreda 25 kg | nazwa + forma | <10 (planer) · „czarna kreda big bag cena" 30 (DFS Labs) | — | — | 0 wierszy |
| **czarna kreda opinie** | nazwa + opinie | **170** | — | 2025-08: 390 | 3 wyśw., hub poz. 3 |
| czarna kreda czy wapno · kreda czarna czy biała | porównanie | <10 | — | — | 0 wierszy |

Suma popytu na nazwy tego produktu (czarna kreda, kreda jeziorna, czarna kreda granulowana, kreda czarna, opinie, cena): **≈ 1 500 wyszukań/mies.**
(planer; warianty mogą się częściowo pokrywać). Serwis ma na te frazy łącznie kilkanaście wyświetleń; zapytania dawkowe zbiera hub.

**Google Ads 13.08–09.09** (`data/produkty/ads/kredy-nawozowe-st-*.json`): frazy z „czarn/jeziorn" — **20 fraz, 122 wyśw., 8 klik., 15,82 zł**
(`czarna kreda granulowana` 39 wyśw. 4 klik., `czarna kreda` 22/1, `czarna kreda cena za tonę` 14/2, `wapno czarna kreda cena` 3/1),
kampania „AGRIA - Rolnictwo". Karta #303 nie była celem reklam (`landing_page_view` nie ma tego adresu — odczyt z pilota).

## 6. Stan dziś na stronie (render 10.09, nie baza)

| element | stan | źródło |
|---|---|---|
| title | „kreda czarna jeziorna kwasy humusowe CaO 44% \| AGRIA" | [R] |
| meta description | „Kreda czarna jeziorna kwasy humusowe to granulat do długoterminowego odkwaszania gleb. Min. 44% CaO, reaktywność 70-90%. Poprawia strukturę gleby w rolnictwie ekologicznym. Zapytaj o ofertę." | [R] |
| H1 | „Kreda czarna(jeziorna) z kwasami humusowymi i węglem organicznym" (= nazwa WC, bez spacji przed nawiasem) | [R] |
| H2 | „Kreda czarna jeziorna kwasy humusowe: Długotrwałe odkwaszanie gleb lekkich" · „Stabilne pH gleby, lepsza żyzność i plony" · „Specyfikacja techniczna" · „Najczęściej zadawane pytania" · „Zapytaj o ofertę, zamów próbkę" | [R] |
| treść | **5 378 znaków** od H1 do formularza | [R] |
| FAQ | 7 pytań; w odpowiedziach produkt nazywany **„Kreda czarna Agria"** (producent wg tej samej strony: Grankal); **brak `FAQPage`** | [R] |
| cena w treści | **brak** sekcji ceny (jako jedyna z trzech kred) | [R] |
| schema `Product` | **bez `offers`**, **bez `sku`**; `additionalProperty` = atrybuty | [R] |
| zdjęcie | `2026/02/kreda-czarna-jeziorna.webp` | [R] |
| PDF | brak linku; brak karty PDF w ogóle | [R] |
| listingi z linkiem do #303 | **tylko** `/wapno-nawozowe-rolnictwo/` · **bez linku:** `/oferta/`, `/wapno-nawozowe/`, `/wapno-do-stawu/`, `/wapno-granulowane/`, hub, strona główna, kalkulator, `/zamowienia/` | curl 10.09 |
| indeks | PASS, „Strona przesłana i zindeksowana", ostatni crawl 2026-09-04 (rejestr T-094 z 24.08 notował „URL unknown to Google" — dziś w indeksie) | URL Inspection 10.09 |

**GSC karty, 2026-06-09 … 2026-09-06** (`data/produkty/gsc/kreda-czarna-jeziorna.json`): **0 kliknięć, 6 wyświetleń, poz. 19,7**.
Zapytania widoczne (5 z 6 wyśw.): `kreda jeziorna` 3 poz. 29,7 · `czarna kreda z hummusem ile na hektar` 1 poz. 5 · `kreda jeziorna dawkowanie` 1 poz. 18.

**Zapytania ofertowe** (CPT `agria_inquiry`, MCP 10.09):
- **wpis 2799, 25.08.2026 — prawdziwe:** „Kreda czarna(jeziorna) z kwasami humusowymi…", typ „oferta", forma **„Worek 25 kg"**, ilość **3 t**,
  kod pocztowy 84-… (pomorskie), źródło **`/wapno-granulowane/`** (strona z `noindex`, cel reklam, na której #303 **nie ma** w listingu);
  `_product_id` = 0 (formularz nie powiązał wpisu z produktem #303); status `inquiry_new`.
- **wpis 2816, 07.09.2026 — test, nie zapytanie:** miejscowość „test", wiadomość „test", ilość „324", źródło `/zamowienia/`; status `trash`.
- Razem: **1 z 11 prawdziwych** zapytań (IV–IX) dotyczy #303 — produktu bez ceny, bez karty i poza katalogiem.

### Rozbieżności

Karty PDF brak, więc rozbieżność karta ↔ strona nie istnieje. Rozbieżności wewnątrz strony i bazy:
- **Magazyn:** widoczna tabela „Draby, Niedomice" vs atrybut „Draby".
- **Nazwa:** H1 „Kreda czarna(jeziorna) z kwasami humusowymi i węglem organicznym" vs title/schemat „kreda czarna jeziorna kwasy humusowe CaO 44%"
  vs FAQ „Kreda czarna Agria".
- **Kwasy humusowe i węgiel organiczny** są w nazwie, w tabeli parametrów ich zawartości nie ma.
- **Brak ceny i `offers`** przy obecnym formularzu zapytań i widoczności w listingu kategorii.

## 7. Konkurencja w wynikach (SERP mobile PL)

| fraza | top wyniki (abs) | AGRIA |
|---|---|---|
| `czarna kreda` (10.09) | 1 czarnakreda.pl · 3 sklep.activ (BB 600 kg) · 5 OLX · 6 czarnakreda.pl · 7 ampol-merol · 9 agrosimex (GreenCal) · 11 czarnakreda.pl · 15 sklepydelta (600 kg) · 17 facebook · 19 sprzedajemy · 20 agrospec (Karbonann) · 22 facebook („opinie") | poza top 20 |
| `kreda jeziorna` (10.09) | 1 AI Overview · 2 OLX · 6 Wikipedia · 7 kwbbelchatow.pgegiek.pl · 8 czarnakreda.pl · 9 surowce-naturalne · 10 allegro · 11 encyklopedialesna · 12 PGI · 15 agro-kam (APGROW) · 18 ampol-merol | poza top 20 |
| `czarna kreda granulowana` (10.09) | 1 czarnakreda.pl · 3 sklep.activ · 4 OLX · 7 czarnakreda.pl · 9 ampol-merol · 10 czarnakreda.pl · 12 agrospec · 13 agrosimex · 18 sprzedajemy · 19 allegro · 20 facebook · 21 gardenstart | poza top 20 |

Dane: `data/produkty/dfs/serp-kredy-nawozowe-2026-09-10.json`.

## 8. Luki — czego brakuje (fakty, bez propozycji struktury)

1. **Brak karty AGRII** — nie ma źródła prawdy o parametrach, zastosowaniach i dawce; wszystko na stronie pochodzi z DescWriter / PIM.
2. **Brak ceny** (cennik Pawła: „brak"), brak `offers`, brak sekcji ceny.
3. **Popyt ≈ 1 500 wyszukań/mies. na nazwy produktu** (`czarna kreda` 720, `kreda jeziorna` 320, `czarna kreda opinie` 170, `czarna kreda granulowana` 140)
   — karta #303 ma 6 wyświetleń w 90 dniach; w SERP AGRIA poza top 20 na trzech sprawdzonych frazach.
4. **Producent** `grankal` (110/mies.) — serwis 0 wierszy.
5. **Listingi:** karta jest tylko w jednej kategorii; nie ma jej na `/oferta/`, `/wapno-granulowane/` ani `/wapno-nawozowe/`.
6. **Zapytanie z 25.08 przyszło ze strony, na której produktu nie ma** (`/wapno-granulowane/`), a reklamy na frazy „czarna kreda" (8 kliknięć, 15,82 zł)
   prowadziły na strony bez tego produktu.
7. **OLX:** 172 ogłoszenia czarnej kredy od 24 sprzedawców, AGRIA — 0.
8. **Parametry kluczowe dla nazwy** (kwasy humusowe, węgiel organiczny) — nieobecne w tabeli.
9. **Schemat:** brak `FAQPage`, brak `sku`.

## 9. Pytania do Janka / klienta (tylko to, czego brak karty nie pozwala rozstrzygnąć)

1. **Czy AGRIA sprzedaje ten produkt?** Opublikowany w WC, wycięty z katalogu decyzją klienta, bez ceny — a 25.08 przyszło o niego prawdziwe zapytanie (3 t, worki 25 kg).
   Cennik Pawła z 07.08 sam proponuje „przy okazji rozstrzygnąć jego status".
2. **Czy to Grankal HumiPlus?** Opis producenta pokrywa się z nazwą WC; strona tego nie mówi.
3. **Jeśli sprzedaje:** cena (luz / BB 600 kg / worek 25 kg), magazyn (Draby czy także Niedomice) i dokument źródłowy parametrów (karta producenta / atest) —
   bez niego baza nie ma czego cytować.
4. **Odmiana wg rozporządzenia** — konkurencja sprzedaje czarną kredę jako „odm. 07a"; w bazie AGRII odmiany brak.
