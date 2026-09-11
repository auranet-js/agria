# Wapno hydratyzowane Bielik (WC #309)

> Karta AGRII: `agria-karta-produktu-wapno-hydratyzowane-bielik.pdf` · karta na stronie: `/wapno-hydratyzowane/bielik/` ·
> kategoria dziś: Budownictwo (term 768, adres `/wapno-hydratyzowane/` — nazwa kategorii ≠ adres) · SKU AGR-018 · **stan na 10.09.2026**
>
> **Źródła (skróty używane niżej):**
> **[K]** karta AGRII PDF, `data/produkty/pdf/agria-karta-produktu-wapno-hydratyzowane-bielik.pdf` (pobrana 10.09) ·
> **[KT]** karta produktu „Wapno budowlane CL 90-S — Wapno hydratyzowane", ZPW Trzuskawica S.A. Zakład Kujawy, wyniki 2008 (akt. 15.01.2009), `karta-produktu-wapno-hydratyzowane.pdf` ·
> **[KCh]** karta charakterystyki diwodorotlenku wapnia, Nordkalk Wapno Sp. z o.o., wyd. 1.1, akt. 26.03.2025 ·
> **[R]** render karty 10.09, `data/produkty/render/bielik.{html,json}` · **[C]** `docs/operations/CENNIK_PAWEL_2026-08-07.md` ·
> **[P14]** `docs/catalog/PLAN_NAPRAWY_PARAMETROW_2026-07-14.md` (commit `9681a80`, 14.07) · **[K320]** karta AGRII #320

---

## 1. Tożsamość (z karty PDF — cytaty)

| cecha | wartość | źródło |
|---|---|---|
| nazwa na karcie | „Wapno Hydratyzowane / Bielik" — zgodna z nazwą w WC („Wapno hydratyzowane Bielik") | [K] |
| podtytuł karty | „Wapno hydratyzowane Bielik 90% CaO — Ca(OH)₂ bez egzotermii" | [K] |
| czym jest | „Wapno gaszone fabrycznie z Nordkalku, min. 90% CaO, reaktywność ~90%, pH >13." | [K] |
| klasa wg PN-EN 459-1 | **brak w karcie AGRII**; [KT]: „Wapno budowlane CL 90-S"; [KCh]: nazwa handlowa „wapno budowlane EN 459-1 CL 90-S, wapno hydratyzowane…, **Bielik**, …, **AgroBIELIK**" | [KT], [KCh] |
| marka | Bielik (`pa_agria-marka` = „Bielik"); w karcie: „Bielik to siostra rodziny Agrobielik w portfelu AGRIA — ten sam producent Nordkalk" | [K], [R] |
| producent | „Nordkalk" | [K] |
| zakład produkcji | **brak w karcie**; [KCh] (Nordkalk 2025): „Zakład Sitkówka, Sitkówka 24, 26-052 Nowiny"; [KT] (2008): ZPW Trzuskawica, **Zakład Kujawy** (Bielawy, Piechcin) | [KCh], [KT] |
| magazyny wysyłkowe | „Niedomice (33-132), Sitkówka (26-052)" · „z magazynów Niedomice i Sitkówka" | [K] |
| rodzaj | wapno hydratyzowane (Ca(OH)₂) — nie nawóz | [K] |
| forma fizyczna | „Sypkie" · „Drobnopyliście mielona forma" | [K] |
| frakcja | „Bardzo drobna" | [K] |
| formy dostawy | tabela: „**Luz 14-16 t**, worek 25 kg" · tekst: „Dostępne luzem i w workach 25 kg" | [K] |
| dostępność | **brak wiersza** (karta ma 16 wierszy z „Odczyn pH") | [K] |

## 2. Parametry

### 2.1 Tabela z karty AGRII — 1:1

| parametr | wartość |
|---|---|
| Zawartość CaO | min. 90% CaO |
| Odczyn pH | >13 |
| Reaktywność | ~90% |
| Typ reakcji | Umiarkowana (bezpieczniejsza) |
| Forma fizyczna | Sypkie |
| Frakcja | Bardzo drobna |
| Zastosowanie | Stabilizacja osadów, zaprawy, tynki, ochrona środowiska |
| Efekt zastosowania | stabilizacja biologiczna |
| Dawkowanie | 15–30% sm osadu / wg projektu |
| Szybkość działania | Kontrolowana, wolniejsza niż tlenkowego |
| Dodatkowe zastosowanie | Oczyszczalnie komunalne, zaprawy, uzdatnianie wód |
| Segment | Oczyszczalnie, budownictwo |
| Forma dostawy | Luz 14-16 t, worek 25 kg |
| Magazyn | Niedomice (33-132), Sitkówka (26-052) |
| Producent | Nordkalk |

Karta **nie podaje**: klasy normowej, MgO, wapna czynnego, uziarnienia liczbowo, wilgotności, gęstości nasypowej, okresu gwarancji, dostępności.

### 2.2 Źródła uzupełniające (nie zastępują karty)

| cecha | [KT] Trzuskawica Kujawy (średnie 2008) | [KCh] Nordkalk 2025 |
|---|---|---|
| norma / klasa | „Wapno budowlane CL 90-S", PN-EN 459-1:2003 | nazwa handlowa „wapno budowlane EN 459-1 CL 90-S" |
| CaO + MgO | wymaganie „powyżej 90,0", wynik **92,55 %** | — |
| MgO | „poniżej 5", wynik 0,58 % | — |
| CO₂ / SO₃ / wilgotność | < 4 (1,19) / < 2 (0,32) / < 2 (1,40) % | — |
| pozostałość na sicie 0,2 mm / 0,09 mm | < 2 (1,13) / < 7 (4,10) % | — |
| ciężar nasypowy | 0,47 kg/l | — |
| pH | — | **„12,4 (roztwór nasycony w temperaturze 20 °C)"** |
| opakowanie | „worki papierowe o wadze 25 kg… luzem… Big-Bag" | — |
| gwarancja | 270 dni w nieotwartych workach | — |
| zastosowania | uzdatnianie wody pitnej — „ATEST HIGIENICZNY HK/W/0618/01/2007", EN 12518 | „Do zapraw murarskich i tynkarskich, betonów, farb wapiennych, w przemyśle chemicznym, ochronie środowiska i drogownictwie, do uzdatniania wody" |

⚠️ **Rozbieżności karta AGRII ↔ źródła uzupełniające** (zapisuję, nie rozstrzygam — memory `feedback_agria_params_from_datasheets`):
zawartość — karta AGRII „min. 90% CaO", [KT] „CaO + MgO powyżej 90,0"; pH — karta AGRII „>13", [KCh] 12,4. [KT] dotyczy Zakładu Kujawy
z 2008 r., karta AGRII nie podaje zakładu.

## 3. Zastosowania (z karty)

| co | co mówi karta [K] |
|---|---|
| do czego | „Stabilizacja osadów, zaprawy, tynki, ochrona środowiska" · dodatkowo „Oczyszczalnie komunalne, zaprawy, uzdatnianie wód" |
| gdzie | piktogramy: OCZYSZCZALNIE, BUDOWNICTWO, **HURTOWNIE** (tabela „Segment": oczyszczalnie, budownictwo) |
| przewaga (wg karty) | „brak gwałtownej reakcji egzotermicznej w kontakcie z wodą — operator dostaje gotowy Ca(OH)₂ bez ryzyka wydzielania ciepła, pyłu i niekontrolowanego wzrostu pH" |
| w oczyszczalni | „Dozowanie w oczyszczalniach stabilne i przewidywalne" · „skuteczna stabilizacja biologiczna osadu, podnosi pH do 12–13 w procesie higienizacji" · dawka 15–30% sm osadu |
| na budowie | „na budowie mieszanie z piaskiem i cementem bez etapu gaszenia" · „szybkie wymieszanie z osadem lub zaprawą bez grudek" · dawka „wg projektu" |
| logistyka (wg karty) | „ten sam producent Nordkalk, te same dwa magazyny, ta sama flota dostawcza. Oczyszczalnia lub firma budowlana zamawiająca równolegle wapno nawozowe i hydratyzowane otrzymuje jedną synchroniczną dostawę, jeden kontakt handlowy, jedną dokumentację." |

**Karta nie mówi o:** rolnictwie, odkwaszaniu gleby, stawach. Wobec #320 [K320]: „Wapno hydratyzowane do rutynowego, stabilnego dozowania".

## 4. Z czym go porównać

### 4.1 Produkty AGRII — różnice wyłącznie z kart PDF, ceny z [C]

| | zawartość (karta) | pH (karta) | reakcja | zastosowanie | dawka | formy dostawy | magazyny | od zł/t netto |
|---|---|---|---|---|---|---|---|---|
| **#309 Bielik** | min. 90% CaO | >13 | „Umiarkowana (bezpieczniejsza)", reaktywność ~90% | stabilizacja osadów, zaprawy, tynki | 15–30% sm osadu / wg projektu | luz 14–16 t, worek 25 kg | Niedomice, Sitkówka | **945** luz · **1 220** worki 25 kg |
| #320 Wapno palone mielone [K320] | min. 90% CaO | >16 | „Bardzo egzotermiczna", reaktywność ~100% | higienizacja osadów | 20–40% sm osadu | BB 1000 kg, luz 24 t | Niedomice, Sitkówka | 950 luz · 1 200 BB |
| #310 Agrobielik 70 (karta) | min. 70% CaO | — | „Szybka (egzotermiczna)" | odkwaszanie gleb, stawy, sadownictwo | 2–6 t/ha | BB, 20 kg, 40 kg, luz 24–26 t | Niedomice, Sitkówka | 220 luz |

Fakty z tabeli, bez wniosków:
- **#309 i #320 opisują się na kartach jako para dla oczyszczalni** — Bielik do rutynowego dozowania, #320 do sytuacji awaryjnych; ceny luz 945 vs 950 zł/t.
- **Kolizja nazwy z Agrobielikiem 70:** oba produkty Nordkalku, oba w magazynach Niedomice i Sitkówka; karta #309 sama nazywa Bielika „siostrą
  rodziny Agrobielik". [KCh] diwodorotlenku wapnia wymienia jako nazwy handlowe zarówno „Bielik", jak i „AgroBIELIK". W GSC zapytanie `wapno bielik`
  wyświetla też kartę #310 (3 wyśw., poz. 64) i dawny adres big-bag Agrobielika 70 (3 wyśw., poz. 57,3); w Ads padło `wapno bielik trzuskawica`.
- Karta #309 nie przewiduje zastosowania rolniczego; w GSC widoczne są zapytania rolnicze o wapno hydratyzowane (`…na pole`, `…do stawu`,
  „czy wapno hydratyzowane można stosować w ogrodzie") — trafiają na hub, nie na #309.

### 4.2 Konkurencja — ten sam produkt lub bezpośredni odpowiednik (SERP 09–10.09)

| kto | co | cena | gdzie widoczny |
|---|---|---|---|
| sklep.ramex.pl | „wapno hydratyzowane bielik 25 kg paleta 36 sztuk nordkalk" | niezmierzone | abs 1 na `wapno bielik 25 kg`, abs 5 na `wapno bielik`, abs 9 na `wapno hydratyzowane cena` |
| allegro.pl | „WAPNO HYDRATYZOWANE BIELIK **30KG**" | niezmierzone | abs 2 na `wapno bielik`, abs 6 na `wapno bielik 25 kg` |
| esklep.mbwesolek.pl | „Wapno hydratyzowane Bielik 25kg Nordkalk Wapno" | niezmierzone | abs 8 / abs 5 |
| facebook.com | „Wapno BIELIK 25kg **cena 30zł** Polecamy" | **30 zł / 25 kg** (w tytule) | abs 9 na obu frazach |
| www.trzuskawica.pl | „Bielik" — strona na domenie Trzuskawicy | — | abs 10 na `wapno bielik`, abs 13 na `wapno bielik 25 kg` |
| nordkalk-wapno.pl | „Bielik - Wapno hydratyzowane" (producent) | — | abs 7 / abs 16 |
| artbud.pl, grupapsb.com.pl, sklepemax.pl | Bielik 25 kg w sklepach budowlanych | niezmierzone | abs 8–15 |
| Lhoist (leroymerlin, ceneo, handlobud), Alpol (castorama), unibuild | wapno hydratyzowane innych producentów, 20–25 kg, CL 90-S; unibuild „1 tona" | niezmierzone | `wapno hydratyzowane` i `…cena` |

Na `wapno bielik 25 kg` i `wapno hydratyzowane cena` Google pokazuje blok `popular_products` (karuzela produktów ze sklepów).
**OLX, zrzut 28.08** (kategoria rolnicza): brak ogłoszeń Bielika / wapna hydratyzowanego — ani AGRII, ani innych.

## 5. Frazy — popyt

Wolumen i CPC: **planer Google Ads API** (PL/polski, średnia 12 mies. 2025-08 … 2026-07), pobrane 10.09 → `data/produkty/ads/bielik-planer.json`.
„<10" = poniżej progu planera (nie zero). GSC: cały serwis, 2026-06-09 … 2026-09-06. Pełna lista: `data/produkty/macierz/bielik.csv`.

| fraza | typ | wyszukań/mies. | CPC śr. zł | szczyt (rok-mies.) | nasz serwis w GSC 90 dni |
|---|---|---|---|---|---|
| **wapno bielik** | nazwa / marka | **210** | 0,80 | 2026-03: 390 | **112 wyśw.** na 6 adresach: karta 32 poz. 12,2 · strona główna 28 poz. 28,4 · stary adres `…-bielik-luz/` 23 poz. 15,3 · kategoria 23 poz. 50,3 · #310 i dawny big-bag AB70 po 3 · SERP 09.09: karta abs 19 |
| wapno hydratyzowane bielik | nazwa + rodzaj | 50 | 0,58 | 2026-03: 90 | 101 wyśw.: stary adres 31 poz. 16,1 · **karta 27 poz. 8,6 (2 klik.)** · strona główna 24 · kategoria 19 |
| wapno bielik 25 kg | nazwa + opakowanie | 50 | — | 2026-04: 90 | 6 wyśw., karta poz. 17,2 · SERP 10.09: karta abs 22 |
| wapno bielik cena | nazwa + cena | 40 | 0,06 | 2026-03: 70 | 27 wyśw., karta **poz. 4,9** |
| wapno bielik 30 kg cena | nazwa + opakowanie + cena | 40 | — | 2025-09: 70 | 42 wyśw., karta poz. 11,5 (21 wyśw.) |
| wapno budowlane bielik | nazwa + rodzaj | 30 | — | 2026-03: 50 | 6 wyśw., karta poz. 10,6 |
| wapno bielik 25 kg cena | nazwa + opakowanie + cena | 30 | — | 2026-03: 70 | 1 wyśw., karta poz. 21 |
| bielik wapno | nazwa | 20 | — | 2026-07: 40 | 24 wyśw., karta poz. 9,7 (1 klik.) |
| wapno bielik castorama | nazwa + sklep | 20 | — | 2026-03: 30 | 1 wyśw., stary adres poz. 13 |
| wapno bielik 30 kg | nazwa + opakowanie | 10 | — | 2025-08: 10 | 0 wierszy |
| bielik nordkalk · wapno bielik opinie | nazwa / producent | <10 | — | — | 0 wierszy |
| **wapno gaszone** | rodzaj | **2 900** | 0,26 | 2026-03: 4 400 | 0 wierszy · SERP 09.09: AGRIA brak w wynikach |
| **wapno hydratyzowane** | rodzaj | **2 400** | 0,21 | 2026-03: 3 600 | 24 wyśw.: kategoria 22 poz. 39,5, hub 1, #310 1 · **karta #309 brak** · SERP 09.09: AGRIA brak w wynikach |
| **wodorotlenek wapnia** | rodzaj (chemia) | 1 900 | 0,65 | 2025-10: 2 900 | 0 wierszy |
| **wapno budowlane** | rodzaj | 1 600 | 0,22 | 2026-03: 2 900 | 0 wierszy |
| wapno budowlane cena | rodzaj + cena | 260 | 0,12 | 2026-03: 590 | 0 wierszy |
| wapno hydratyzowane cena | rodzaj + cena | 170 | 0,29 | 2026-05: 320 | 0 wierszy · SERP 10.09: AGRIA poza top 20 |
| wapno hydratyzowane zastosowanie | rodzaj + zastosowanie | 140 | 0,33 | 2025-10: 260 | 6 wyśw., hub poz. 44,7 |
| wapno do zaprawy | zastosowanie z karty | 50 | 0,31 | 2025-10: 70 | 1 wyśw., kategoria poz. 20 |
| wapno hydratyzowane do stawu | zastosowanie spoza karty | 40 | 0,66 | 2026-03: 70 | 2 wyśw., hub poz. 35 |
| wapno tynkarskie | zastosowanie z karty | 30 | 0,24 | 2025-10: 50 | 1 wyśw., kategoria poz. 37 |
| wapno hydratyzowane cena za tonę | rodzaj + cena | 30 | 0,11 | 2025-10: 50 | 4 wyśw., kategoria poz. 37,2 |
| wapno hydratyzowane 25 kg | rodzaj + opakowanie | 10 | 0,33 | 2026-07: 30 | 0 wierszy |
| wapno hydratyzowane na pole | zastosowanie spoza karty | 10 | — | 2025-08: 30 | 5 wyśw. (strona główna, hub) |
| wapno cl 90-s | klasa | <10 | — | — | 4 wyśw. (`cl 90-s` 3 poz. 9,3, `cl 90` 1) — karta |
| wapno budowlane tarnów | rodzaj + miasto | **<10** | — | — | **217 wyśw.**: strona główna 76 poz. 7,6 · `/oferta/` 56 · kategoria 42 poz. 76,3 · Rolnictwo 41 |
| wapno hydratyzowane do oczyszczalni · wapno do uzdatniania wody · wapno hydratyzowane dawkowanie | zastosowanie / dawka | <10 | — | — | 0 wierszy |
| wapno hydratyzowane nordkalk · …trzuskawica · …kujawy | producent / zakład | <10 | — | — | 0 wierszy |
| wapno hydratyzowane a palone · …czy palone | porównanie | <10 | — | — | 0 wierszy (odwrotna kolejność: `wapno palone a gaszone` 90, `wapno palone a hydratyzowane` 10 — plik #320) |

Suma popytu na markę Bielik (10 wariantów z „bielik"): **≈ 500 wyszukań/mies.**; na rodzaj (gaszone + hydratyzowane + budowlane + wodorotlenek): ≈ 8 800.
`wapno budowlane tarnów` — planer poniżej progu, a GSC ma 217 wyświetleń w 90 dniach (przykład, że „<10" nie znaczy zero).

**Google Ads 13.08–09.09** (`data/produkty/ads/agrobielik-70-q2.json`, `st-hydratyz.json`, `st-budowlan.json`), wszystko w kampanii „AGRIA - Marka":
`wapno bielik` 42 wyśw. 1 klik. · `wapno hydratyzowane bielik` 25 wyśw. 2 klik. · `wapno bielik cena` 10 / 1 · `wapno bielik 25 kg` 9 / 0 ·
`wapno bielik 30 kg cena` 8 / 1 · `bielik wapno` 5 · `wapno bielik 25 kg cena` 4 · `wapno budowlane bielik` 2 · `wapno bielik trzuskawica` 2.
Strony docelowe reklam: karty #309 wśród nich nie ma.

## 6. Stan dziś na stronie (render 10.09, nie baza)

| element | stan | źródło |
|---|---|---|
| title | „Wapno hydratyzowane Bielik **CL 90-S \| CaO+MgO 90%** \| AGRIA" | [R] |
| meta description | „…klasa CL 90-S (PN-EN 459-1), **CaO+MgO min. 90%, wapno czynne min. 80%**. Do oczyszczalni i budownictwa: higienizuje osady, wzmacnia zaprawy. Zapytaj o ofertę." | [R] |
| H1 | „Wapno hydratyzowane Bielik" (= nazwa WC) | [R] |
| H2 | „…Bielik: wysoka czystość dla budownictwa i oczyszczalni" · „Efektywna higienizacja i wytrzymałe zaprawy" · „Specyfikacja techniczna" · „Wapno hydratyzowane Bielik — cena" · „Najczęściej zadawane pytania" · „Zapytaj o ofertę, zamów próbkę" | [R] |
| treść | **5 945 znaków** od H1 do formularza | [R] |
| FAQ | 7 pytań (do czego, parametry, różnica z palonym, dawkowanie, formy dostawy, dokumentacja, zamówienie); **brak `FAQPage`** | [R] |
| cena w treści | „kosztuje od 945 zł/t netto przy dostawie **całosamochodowej 24 t**. Produkt jest dostępny także w workach 25 kg…" — luz zgodny z [C] („luz 24 t 945"), **karta PDF: luz 14–16 t**; kwoty za worki (1 220 zł/t w [C]) na stronie brak | [R], [C], [K] |
| schema `Product` | `offers`: 945 PLN, `unitCode: TNE`, netto; `additionalProperty` = `pa_*` (w tym `pa_agria-norma` „CL 90-S (PN-EN 459-1)", `pa_agria-forma-dostawy` „Luz 14–16 t, Worek 25 kg") | [R] |
| formularz | „Luz", „Worek 25 kg" — zgodne z kartą | [R] |
| zdjęcie | `2026/02/wapno-hydratyzowane-bielik.jpg` | [R] |
| PDF | karta **nie linkuje** do karty PDF ani do [KCh]; FAQ 6: „W razie potrzeby kart charakterystyki… prosimy o bezpośredni kontakt" | [R] |
| linki „Zastosowania i poradniki" | „Higienizacja osadów ściekowych wapnem — dobór i dawki", „Wapno do stabilizacji gruntów — CL 90-Q" | [R] |
| listingi z linkiem do #309 | strona główna, `/oferta/`, `/wapno-hydratyzowane/`, `/wapno-do-stawu/`, poradnik `/higienizacja-osadow-sciekowych-wapnem/` (2 linki) · **bez linku:** `/wapno-do-oczyszczalni/` (kategoria pierwszego zastosowania z karty), hub, kalkulator, `/zamowienia/`, `/do-pobrania/` | curl 10.09 |
| indeks | PASS, zindeksowana, ostatni crawl 2026-08-30, canonical własny | URL Inspection 10.09 |
| adres sprzed 08.07 | `/wapno-hydratyzowane/wapno-hydratyzowane-bielik-luz/` → 301 (curl 10.09); Google widzi przekierowanie (crawl 29.08, canonical → karta) | URL Inspection 10.09 |

**GSC karty, 2026-06-09 … 2026-09-06** (`data/produkty/gsc/trzy-nordkalk-baseline.json`): **16 kliknięć, 621 wyświetleń, CTR 2,58%, poz. 7,2**
(poziom strony). Miesięcznie: VII 4/49, VIII 8/428, IX (do 06.09) 4/144. Zapytań widocznych 14 — razem 3 kliknięcia i 139 wyświetleń;
próg prywatności ukrywa **13 z 16 kliknięć i 78% wyświetleń**. Widoczne m.in.: `wapno bielik` 32 poz. 12,2 · `wapno hydratyzowane bielik` 27 poz. 8,6 (2 klik.) ·
`wapno bielik cena` 26 poz. 4,9 · `wapno bielik 30 kg cena` 21 poz. 11,5 · `bielik wapno` 15 poz. 9,7 (1 klik.) · `wapno budowlane bielik` 5 ·
`wapno bielik 25 kg` 4 · `cl 90-s` 3 poz. 9,3 · po 1: `agria tarnów`, `cao mgo`, `cl 90`, `wapno bielik 25 kg cena`, `wapno do szamba`, `wapno palone`.
Stary adres `…-bielik-luz/`: 5 klik., 181 wyśw., poz. 10,1 (VI 0/44, VII 5/137, od VIII 0). Kategoria `/wapno-hydratyzowane/`: 3 klik., 248 wyśw., poz. 31,6.

**Stary serwis — dziś 404:** `/oferta/budownictwo/wapno-hydratyzowane/` — **24 klik., 1 517 wyśw. w IX 2025 – III 2026**, zapytania głównie
`wapno bielik` (49, poz. 34,4), `wapno bielik 30 kg cena` (17), `wapna hydratyzowanego` (14); od IV 2026 zero (`data/produkty/gsc/trzy-nordkalk-stare-adresy.json`, curl 10.09).

**Zapytania ofertowe** (CPT `agria_inquiry`, MCP 10.09): **2 z 11** — 28.07 **z karty** `/wapno-hydratyzowane/bielik/` (worek 25 kg);
13.08 z `/zamowienia/` (luz). **Google Ads:** 0 kliknięć z reklam na kartę.

### Rozbieżności karta PDF ↔ strona

| parametr | karta PDF [K] | widoczna tabela [R] | schemat `pa_*` [R] |
|---|---|---|---|
| Zawartość | min. 90% CaO | **„CaO + MgO min. 90%"** | `pa_min-cao`: min. 90% CaO (= karta) |
| Klasa (PN-EN 459-1) | **brak** | **„CL 90-S"** | `pa_agria-norma`: „CL 90-S (PN-EN 459-1)" |
| Wapno czynne | **brak** | **„min. 80%"** | brak |
| Odczyn pH | >13 | **brak wiersza** (FAQ 2: „silnie zasadowym odczynem pH (>12)"; korzyści: „pH do poziomu 12-13") | brak |
| Zastosowanie | Stabilizacja osadów, zaprawy, tynki, ochrona środowiska | „Zastosowanie funkcjonalne": materiał budowlany zaprawy, Stabilizacja i higienizacja osadów ściekowych | = karta |
| Dodatkowe zastosowanie | Oczyszczalnie komunalne, zaprawy, **uzdatnianie wód** | Oczyszczalnie komunalne, produkcja zapraw budowlanych (**bez uzdatniania wód**) | = karta |
| Forma dostawy | Luz 14-16 t, worek 25 kg | **brak wiersza**; sekcja ceny: „dostawie całosamochodowej **24 t**" | „Luz 14–16 t, Worek 25 kg" (= karta) |
| Dostępność | brak | Cały rok | Cały rok |
| reaktywność, typ reakcji, forma, frakcja, efekt, dawkowanie, szybkość, segment, magazyn, producent | — | zgodne (różnice w wielkości liter) | zgodne |

**Pochodzenie „CaO + MgO", klasy CL 90-S i „wapna czynnego" — NIE DescWriter:** dodane przez Auranet 14.07 według [P14] (pkt 4: „Bielik:
»Zawartość CaO min. 90%« → CaO+MgO ≥ 90%, wapno czynne ≥ 80% (CL 90-S wg PN-EN 459-1)"; commit `9681a80`). „CL 90-S" i „CaO + MgO powyżej 90"
mają pokrycie w [KT] i [KCh]; **„wapna czynnego" nie ma w żadnym z 31 PDF-ów na `/do-pobrania/`**. Karta AGRII (katalog) podaje „min. 90% CaO".

**Twierdzenia w treści, których nie ma w karcie PDF** (`[J 10.09]`: tekst DescWriter, niepotwierdzone kartą):
- „Jego wysoka czystość przekłada się na trwałość i estetykę wykonanych prac", „wysoka czystość dla budownictwa" (H2);
- „silnie zasadowy odczyn pH (>12)" (FAQ 2) — karta: >13;
- „Korzystaj z 35-letniego doświadczenia Agria" — ta sama strona w sekcji formularza: „Agria — 37 lat doświadczenia".

**Z karty PDF nieobecne na stronie:** „Wapno gaszone fabrycznie", brak wydzielania ciepła i pyłu, „na budowie mieszanie z piaskiem i cementem
bez etapu gaszenia", „drobnopyliście mielona forma… bez grudek", logistyka wspólna z Agrobielikiem („jedna synchroniczna dostawa, jeden kontakt
handlowy, jedna dokumentacja"), uzdatnianie wód, HURTOWNIE (piktogram), pH >13 w tabeli, luz 14–16 t.

## 7. Konkurencja w wynikach (SERP mobile PL)

| fraza | top wyniki (abs) | AGRIA |
|---|---|---|
| `wapno bielik` (09.09) | 1 AI Overview · 2 allegro (Bielik 30 kg) · 5 sklep.ramex · 7 nordkalk-wapno.pl · 8 mbwesolek · 9 facebook (30 zł) · 10 trzuskawica.pl · 11 artbud · 12 materialybudowlane · 14 grupapsb | **abs 19** — karta |
| `wapno bielik 25 kg` (10.09) | 1 sklep.ramex · 2 popular_products · 5 mbwesolek · 6 allegro (30 kg) · 8 artbud · 9 facebook · 11 sklepemax · 13 trzuskawica.pl · 14 OLX · 15 grupapsb · 16 nordkalk-wapno.pl | abs 22 — karta |
| `wapno hydratyzowane` (09.09) | 1 epicentra („hydratyzowane czy palone?") · 3 ramex · 5 unibuild (1 tona) · 6 allegro · 7 lhoist.com · 8 castorama (słowniczek) · 10 sklep-lubar · 11 izolacje.com.pl · 12 handlobud (Lhoist CL 90-S 25 kg) · 14 leroymerlin | brak w wynikach |
| `wapno hydratyzowane cena` (10.09) | 1 popular_products · 5 allegro · 6 unibuild · 7 leroymerlin · 9 ramex · 10 sklep-lubar · 11 ceneo · 12 OLX · 14 adamex · 15 mrowka · 17 castorama | poza top 20 |
| `wapno gaszone` (09.09) | 1 AI Overview · 2 castorama · 4 allegro · 6 Wikipedia · 7 leroymerlin · 9 wenekor · 10 grupapsb · 11 mgprojekt · 12 mrowka | brak w wynikach |

Dane: `data/produkty/dfs/serp-nordkalk-308-320-309-2026-09-10.json`, `data/seo/2026-09-09-serp-marka-i-kategorie.json`.

## 8. Luki — czego brakuje (fakty, bez propozycji struktury)

1. **Marka ma realny popyt (≈ 500/mies. na warianty z „bielik"), karta stoi na poz. 5–22** — najlepiej na `wapno bielik cena` (4,9);
   na główne `wapno bielik` (210/mies.) abs 19 w SERP, a w GSC wyświetlenia rozkładają się na 6 naszych adresów (karta, strona główna,
   stary adres, kategoria, #310, dawny big-bag AB70).
2. **Rynek szuka Bielika w opakowaniu** (`25 kg`, `30 kg`, `cena`, `castorama` — ≈ 190/mies.) i dostaje karuzelę produktów i sklepy budowlane;
   karta #309 ma worek 25 kg bez ceny na stronie (w [C]: 1 220 zł/t), a allegro sprzedaje „Bielik 30 kg", którego karta nie zna.
3. **Na rodzaj** (`wapno gaszone` 2 900, `wapno hydratyzowane` 2 400, `wapno budowlane` 1 600) karta się nie pokazuje; kategoria
   `/wapno-hydratyzowane/` stoi na poz. 31–50.
4. **Zastosowania z karty bez pokrycia w wynikach:** oczyszczalnie (kategoria `/wapno-do-oczyszczalni/` nie ma Bielika w listingu),
   uzdatnianie wód (nieobecne na stronie), zaprawy i tynki (`wapno do zaprawy` 50, `wapno tynkarskie` 30 — kategoria poz. 20–37).
5. **Parametry na stronie ≠ karta PDF** (CaO + MgO, klasa, wapno czynne — 14.07; luz 24 t vs 14–16 t; pH >12 vs >13).
6. **Porównań brak:** z #320 (para opisana na obu kartach), z wapnem palonym ogólnie (`wapno palone a gaszone` 90/mies.) — FAQ 3 porusza
   różnicę jednym akapitem.
7. **Stary serwis:** `/oferta/budownictwo/wapno-hydratyzowane/` (1 517 wyśw., 24 klik. w 7 mies.) zwraca 404.
8. **Dokumenty:** karta nie linkuje do karty PDF ani do [KCh] (FAQ odsyła do kontaktu).
9. **Schemat:** brak `FAQPage`; title i meta niosą parametry spoza karty.
10. **Sprzedaż:** 2 zapytania ofertowe (jedno z karty — worek 25 kg), 16 kliknięć organicznych w 90 dniach, 0 kliknięć z Ads na kartę
    (reklamy marki klikane, ale kierują gdzie indziej).

## 9. Pytania do Janka / klienta (tylko to, czego karty nie rozstrzygają)

1. **Luz: 14–16 t (karta PDF) czy 24 t (cennik Pawła 07.08, strona)?** Cena 945 zł/t — przy której wielkości dostawy?
2. **Zakład produkcji** — karta nie podaje; [KCh] Nordkalk wskazuje Sitkówkę, dołączona karta producenta z `/do-pobrania/` jest z Zakładu Kujawy (2008).
   Z którego zakładu jest Bielik AGRII?
3. **„Wapno czynne min. 80%"** — z jakiego dokumentu? W PDF-ach na `/do-pobrania/` go nie ma.
4. **Worek 30 kg** — allegro i zapytania GSC (`wapno bielik 30 kg cena`) mówią o 30 kg; karta AGRII zna tylko 25 kg. Czy AGRIA ma 30 kg?
