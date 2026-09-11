# Wapno nawozowe tlenkowe zawierające magnez (WC #313)

> Karta AGRII: `agria-karta-produktu-tlenkowe-z-magnezem.pdf` · karta na stronie: `/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/` ·
> kategoria dziś: Wapno nawozowe (`/wapno-nawozowe-rolnictwo/`, term 764) · SKU AGR-004 · **stan na 10.09.2026**
>
> **Źródła (skróty używane niżej):**
> **[K]** karta AGRII PDF, `data/produkty/pdf/agria-karta-produktu-tlenkowe-z-magnezem.pdf` (pobrana 10.09) ·
> **[R]** render karty 10.09, `data/produkty/render/wapno-tlenkowe-magnez.{html,json}` · **[C]** `docs/operations/CENNIK_PAWEL_2026-08-07.md`
>
> Dla #313 **na `/do-pobrania/` nie ma atestu ani karty charakterystyki**. Produkt **nie ma nazwy handlowej** — nazwa WC jest opisem rodzaju.

---

## 1. Tożsamość (z karty PDF — cytaty)

| cecha | wartość | źródło |
|---|---|---|
| nazwa na karcie | „Wapno nawozowe tlenkowe / **zawierające magnez**" — zgodna z nazwą WC (w katalogu drukowanym dopuszczone skrócenie „z magnezem", archiwum §9.2) | [K] |
| nagłówek | „Szybkie odkwaszanie i uzupełnienie magnezu" · „Jeden rozsiew zamiast dwóch" | [K] |
| odmiana | **karta nie podaje**; atrybut `pa_agria-norma` = „Odmiana 02" (tylko schemat) | [R] |
| marka | brak | [K] |
| producent | „Producent: Lhoist." | [K] |
| zakład produkcji | **karta nie podaje** | [K] |
| magazyny wysyłkowe | „Niedomice (33-132), Częstochowa (42-200)" | [K] |
| rodzaj | wapno **tlenkowe z magnezem** („Wapno nawozowe tlenkowe wzbogacone o magnez") | [K] |
| forma fizyczna · frakcja | „Sypkie" · „0–1 mm" | [K] |
| formy dostawy | „Big-bag 1000 kg" | [K] |
| dostępność | „Cały rok" | [K] |

## 2. Parametry — tabela z karty AGRII 1:1

| parametr | wartość |
|---|---|
| Zawartość CaO + MgO | 70/25 % |
| Reaktywność | Wysoka |
| Forma fizyczna | Sypkie |
| Frakcja | 0–1 mm |
| Zastosowanie | Odkwaszanie gleb + uzupełnienie magnezu |
| Efekt zastosowania | Wzrost pH gleby i podniesienie zawartości magnezu |
| Dawkowanie | 1–1,5 t/ha |
| Szybkość działania | Szybkie (2–4 tygodnie) |
| Dodatkowe zastosowanie | Rośliny magnezolubne (zboża, ziemniaki, rzepak) |
| Segment | Rolnictwo, hurtownie |
| Forma dostawy | Big-bag 1000 kg |
| Magazyn | Niedomice (33-132), Częstochowa (42-200) |
| Producent | Lhoist |
| Dostępność | Cały rok |

Karta **nie ma wiersza „Typ reakcji"** (strona go ma). Karta **nie podaje**: odmiany, zakładu, pH, metali ciężkich, gwarancji.

⚠️ **Zawartość — trzy zapisy, których nie rozstrzygamy:**
- tabela karty: „Zawartość CaO + MgO | **70/25 %**";
- wypunktowanie tej samej karty: „Dwuskładnikowe działanie — **min. 70% CaO + 25% MgO** w jednym produkcie"; tekst: „(CaO + MgO - 70/25)";
- meta description strony: „**CaO+MgO min. 70% (w tym MgO min. 25%)**" — to inny odczyt niż wypunktowanie karty (suma 70 vs 70 + 25).
  Atrybuty w schemacie: `pa_min-cao` „min. 70% CaO", `pa_agria-mgo` „min. 25% MgO" — zgodne z wypunktowaniem karty.

⚠️ **Rozbieżność wewnątrz karty:** tekst „Idealne pod rośliny magnezolubne (zboża, ziemniaki, **buraki**, rzepak)" — tabela bez buraków.

## 3. Zastosowania (z karty)

| co | co mówi karta [K] |
|---|---|
| do czego | „rozwiązanie dla gospodarstw, które potrzebują jednoczesnego odkwaszenia i nawiezienia magnezem — bez konieczności dwukrotnego rozsiewu" |
| gleby | „Idealne dla gleb średniociężkich i ciężkich z deficytem magnezu." |
| uprawy | „rośliny magnezolubne (zboża, ziemniaki, buraki, rzepak)" (tekst) / „(zboża, ziemniaki, rzepak)" (tabela) |
| dawka | 1–1,5 t/ha |
| czas | „Efekty widoczne w 2–4 tygodnie." · „Szybkie odkwaszanie (2–4 tyg) — wapno tlenkowe reaguje znacznie szybciej niż węglanowe" |
| magnez | „Uzupełnienie deficytu magnezu — kluczowe dla fotosyntezy, jakości plonu, odporności roślin" |
| korzyść | „Jeden rozsiew zamiast dwóch — oszczędność czasu, paliwa i robocizny" |
| piktogramy | ROLNICTWO · HURTOWNIE (bez rybactwa, sadownictwa, oczyszczalni) |

**Karta nie mówi:** terminu w roku, sposobu wysiewu, łączenia z innymi nawozami, zastosowań poza rolnictwem.

## 4. Z czym go porównać

### 4.1 Produkty AGRII — różnice wyłącznie z kart PDF, ceny z [C] / `FAKTY_KLIENTA` §3 (od zł/t netto, bez transportu)

| | CaO / MgO (zapis karty) | forma / frakcja | dawka | szybkość | producent · magazyny | formy dostawy | cena |
|---|---|---|---|---|---|---|---|
| **#313 Tlenkowe zawierające magnez** | CaO+MgO 70/25 % | sypkie 0–1 mm | 1–1,5 t/ha | 2–4 tyg. | Lhoist · Niedomice, Częstochowa | BB | **brak ceny** |
| #310 Agrobielik 70 (tlenkowe bez Mg) | min. 70% CaO | sypkie 0–2 mm | 2–6 t/ha | 2–4 tyg. | Nordkalk · Niedomice, Sitkówka | BB, 20 kg, 40 kg, luz | 220 luz · 400 BB |
| #312 Oxyfertil 90 (tlenkowe, Lhoist) | min. 90% CaO | kruszone 3–8 mm | 1–3 t/ha | 7–14 dni | Lhoist · Niedomice, Tarnów Opolski, Góraźdźce | BB | 790 BB |
| #317 Węglanowe z magnezem granulowane | min. 31% CaO + 16% MgO | granulat 3–6 mm | 1–6 t/ha | 3–6 mies. | Grankal · Draby, Niedomice | BB 600 kg, worek 25 kg | 370 BB · 25 kg 410 |
| #318 Węglanowe z magnezem — odm. 04 | min. 41% CaO + min 8% MgO | sypka 0–2 mm | 1,5–6 t/ha | 3–6 mies. | Kopalnia Jażwica (Industria) · Chęciny | luz 25–27 t | 50 luz |
| #319 Węglanowe z magnezem — odm. 05 | min. 25–37% CaO, min. 8–20% MgO | sypkie 0–2 mm | 1,5–6 t/ha | 3–6 mies. | Laskowa, Winna (Industria) · Łagów, Kostomłoty Drugie | luz | 36 luz |
| #302 Dolomit | CaO + MgO min 45% w tym MgO min 15% | sypkie 0–2 mm | 1,5–6 t/ha | 3–6 mies. | Siarkopol · Tarnobrzeg, Niedomice | worek 10 kg, 25 kg | od 260 luz (frakcje 0,1–0,8 mm) |

Fakty z tabeli, bez wniosków: **#313 jest jedynym produktem AGRII łączącym formę tlenkową z magnezem.** Najwyższa zawartość MgO na kartach
(25 %), najniższa dawka (1–1,5 t/ha), najkrótszy czas wśród produktów z Mg (2–4 tygodnie wobec 3–6 miesięcy u węglanowych i dolomitu).
Jako jeden z trzech produktów AGRII **nie ma ceny** (obok #303 i #316) — cennik Pawła z 07.08 pominął go „bez komentarza" [C].

### 4.2 Konkurencja — odpowiedniki widoczne w SERP i na OLX

| sprzedawca | co | cena | gdzie widoczny | źródło |
|---|---|---|---|---|
| chemirol.com.pl | „Wapno nawozowe tlenkowe **70/25 0-1mm**" — ten sam zapis zawartości i frakcji co karta #313 | niezmierzone | abs 5 na `wapno tlenkowo magnezowe` | SERP 09.09 |
| chemiagro.pl | „Wapno tlenkowe odmiana 01 **Oxyfertil 70/25**" | niezmierzone | abs 24 | SERP 09.09 |
| esklep.mbwesolek.pl | „Nawóz Oxyfertil big-bag 500KG Lhoist 75%CaO+MgO25%MgO" | niezmierzone | abs 11 na `oxyfertil` | SERP 10.09 |
| flora-praszka.pl | „Oxyfertil® Mg 75/25, frakcja 3-7mm", „Oxyfertil® Mix Mg 70/15"; PDF „Wapno nawozowe tlenkowe zawierające magnez" | niezmierzone | abs 8–24 | SERP 10.09 |
| waprom.pl | „Wapno tlenkowe z magnezem" | niezmierzone | abs 7 | SERP 09.09 |
| ifarmer.pl | „Wapno tlenkowe magnezowe Dobromir 600 kg" | niezmierzone | abs 10 | SERP 09.09 |
| gospodarz.pl | „Nawóz wapniowy tlenkowo-magnezowy «OXYFERTIL Mix Mg 60…»" | niezmierzone | abs 20 | SERP 09.09 |

Nie ustalam, czy #313 jest którymś z produktów Oxyfertil — **karta AGRII nie podaje nazwy handlowej**; zbieżny jest tylko zapis „70/25" i frakcja
0–1 mm (chemirol), producent Lhoist (mbwesolek). **OLX, zrzut 28.08:** ogłoszeń z tlenkowym wapnem z magnezem — **AGRIA 0**, konkurencja 0
(jedyne trafienie filtra to ogłoszenie CARLOS-a o wapnie dolomitowym za 35 zł). Na `wapno tlenkowo magnezowe` SERP 09.09 otwierają dwa wyniki OLX (abs 1 i 3).

## 5. Frazy — popyt

Wolumen i CPC: planer Google Ads API (konto AGRII, PL/polski, średnia 12 mies. 2025-08 … 2026-07), pobrane 10.09 →
`data/produkty/ads/wapno-tlenkowe-magnez-planer.json`; DataForSEO Labs `keyword_suggestions` „wapno magnezowe" 10.09
(`data/produkty/dfs/sugestie-wapno-magnezowe.json`). GSC: cały serwis 2026-06-09 … 2026-09-06. Macierz: `data/produkty/macierz/wapno-tlenkowe-magnez.csv`.

| fraza | typ | wyszukań/mies. | CPC śr. zł | szczyt (rok-mies.) | nasz serwis w GSC 90 dni |
|---|---|---|---|---|---|
| wapno tlenkowo magnezowe (planer skleja z „wapno tlenkowe magnezowe") | nazwa-rodzaj | **50** | 0,35 | **2026-07: 110** | karta 35 wyśw. poz. 10,4 + 19 wyśw. poz. 10 („tlenkowe magnezowe"); stary adres 10 + 6; kategoria 5 poz. 9,2 |
| wapno magnezowe tlenkowe | nazwa-rodzaj | 20 | 0,09 | 2025-08: 40 | 0 wierszy |
| wapno tlenkowe z magnezem | nazwa-rodzaj | 10 | — | 2025-08: 10 | 0 wierszy |
| wapno tlenkowe z magnezem granulowane | nazwa-rodzaj (**#313 nie jest granulatem**) | 10 | 0,23 | 2026-07: 10 | 0 wierszy |
| wapno nawozowe tlenkowe z magnezem · …zawierające magnez · wapno tlenkowe 70/25 · wapno tlenkowe 25 mgo | nazwa-rodzaj | <10 | — | — | 0 wierszy |
| wapno nawozowe tlenkowe | rodzaj | 50 | 0,94 | 2026-03: 90 | **karta 78 wyśw. poz. 13,4**; stary adres 55 poz. 17,7; najlepszy nasz #312 poz. 10 |
| wapno tlenkowe | rodzaj | **720** | 0,52 | 2025-08: 1 300 | karta 33 wyśw. poz. 25,5; hub 20 poz. 2,5; SERP 10.09: **karta abs 22** |
| wapno tlenkowe nawozowe | rodzaj | (wariant) | — | — | karta 28 wyśw. poz. 20,7; stary adres 25 |
| sprzedaż wapna tlenkowego | rodzaj + zakup | <10 | — | — | **karta 31 wyśw. poz. 24,4** |
| wapno tlenkowe sypkie | rodzaj + forma | 20 (pilot) | 0,18 | — | karta 3 wyśw. poz. 19,3 |
| wapno magnezowe | rodzaj Mg | **1 900** | 0,60 | 2025-08: 4 400 | 27 wyśw.: #317 23 poz. 48,9, hub 4 poz. 2,5; **#313 brak** |
| wapno z magnezem | rodzaj Mg | 210 | 0,32 | 2026-03: 390 | 2 wyśw., hub; SERP 10.09: AGRIA poza top 20 |
| wapno nawozowe z magnezem | rodzaj Mg | 90 | 0,79 | 2026-03: 210 | karta 1 wyśw. poz. 36; SERP 10.09: AGRIA poza top 20 |
| wapno magnezowe sypkie | rodzaj Mg + forma | 30 | 0,68 | 2025-08: 70 | 0 wierszy |
| wapno magnezowe cena za tonę | rodzaj Mg + cena | 140 | 0,81 | 2025-08: 320 | 4 wyśw., hub |
| wapno magnezowe cena | rodzaj Mg + cena | 90 | 0,26 | 2025-08: 210 | 0 wierszy |
| wapno tlenkowo magnezowe cena | nazwa-rodzaj + cena | 10 | — | 2025-08: 10 | 0 wierszy |
| wapno magnezowe big bag · luzem | rodzaj Mg + forma | 40 · 40 | 0,32 · 0,65 | 2025-08: 90 | 2 wyśw. (stary adres #313 poz. 23) · 2 wyśw. (hub) |
| ile wapna magnezowego na hektar | rodzaj Mg + dawka | 90 | 5,59 | 2025-08: 260 | 212 wyśw., hub poz. 9,8 |
| wapno magnezowe ile na hektar | rodzaj Mg + dawka | 70 | — | 2025-08: 260 | 258 wyśw., hub poz. 8,0 |
| wapno magnezowe dawkowanie | rodzaj Mg + dawka | 20 | — | 2025-09: 50 | 28 wyśw., hub poz. 6,9 |
| wapno tlenkowo magnezowe dawkowanie | nazwa-rodzaj + dawka | <10 | — | — | 0 wierszy (#313: `wapno tlenkowe dawkowanie` 1 wyśw. poz. 12) |
| kiedy stosować wapno magnezowe | rodzaj Mg + termin | 70 | — | 2025-08: 140 | 1 wyśw., hub |
| wapno magnezowe pod ziemniaki | + uprawa z karty | 10 | — | 2025-09: 20 | 0 wierszy |
| wapno magnezowe pod rzepak · pod zboża · pod buraki | + uprawa z karty | <10 | — | — | 0 wierszy |
| lhoist częstochowa | producent + magazyn z karty | 40 | — | 2025-11: 50 | 0 wierszy |
| lhoist wapno magnezowe | producent | <10 | — | — | 0 wierszy |
| wapno tlenkowe czy magnezowe · wapno magnezowe czy zwykłe · wapno magnezowe czy dolomit | porównanie | <10 | — | — | 0 wierszy |

**Frazy „wapno magnezowe / z magnezem" są wspólne dla wszystkich produktów z Mg** (#313, #317, #318, #319, #302) — w GSC łapią je hub i #317;
w sugestiach DFS dominują warianty granulowane i ogrodowe („pod warzywa" 110, „na trawnik" 90, „granulowane" 880). Popyt na **odmianę
tlenkową** z Mg to ≈ 90/mies. (tlenkowo/tlenkowe magnezowe 50 + magnezowe tlenkowe 20 + tlenkowe z magnezem 10 + granulowane 10).

**Google Ads 13.08–09.09** (`data/produkty/ads/tlenkowe-311-313-st-magnez.json`): 63 frazy z „magnez" w kampanii „AGRIA - Rolnictwo",
m.in. `wapno magnezowe` 107 wyśw. 10 klik. 15,48 zł, `wapno magnezowe granulowane` 50/3, `wapno granulowane magnezowe` 18/4;
**z formą tlenkową jedna:** `wapno tlenkowo magnezowe` 4 wyśw., 0 klik.

## 6. Stan dziś na stronie (render 10.09, nie baza)

| element | stan | źródło |
|---|---|---|
| title | „Wapno nawozowe tlenkowe zawierające magnez \| AGRIA" | [R] |
| meta description | „…AGRIA szybko odkwasza gleby średnie i ciężkie, poprawiając strukturę i dostępność składników. **CaO+MgO min. 70% (w tym MgO min. 25%)**. Zapytaj o ofertę." | [R] |
| H1 | „Wapno nawozowe tlenkowe zawierające magnez" (= nazwa WC) | [R] |
| H2 | „…zawierające magnez: Szybkie odkwaszanie gleb" · „Skuteczne odkwaszanie – wyższe plony rolnicze" · „Specyfikacja techniczna" · „Najczęściej zadawane pytania" · „Zapytaj o ofertę, zamów próbkę" — **bez sekcji ceny** | [R] |
| treść | 5 143 znaki od H1 do formularza | [R] |
| FAQ | **7 pytań** (dawka, gleby, szybkość, dostawa, dokumentacja i producent, inne zastosowania, jak zamówić); **brak `FAQPage`** | [R] |
| cena w treści | **brak** (zgodnie z brakiem w cenniku) | [R], [C] |
| schema `Product` | **bez `offers`** (świadomy wyjątek T-097); `additionalProperty` = `pa_*` (zgodne z kartą; `pa_agria-norma` „Odmiana 02") | [R] |
| zdjęcie | `2026/02/wapno-nawozowe-tlenkowe-zawierajace-magnez-agria.webp` | [R] |
| PDF | brak linku do karty PDF | [R] |
| listingi z linkiem do #313 | `/oferta/`, `/wapno-nawozowe-rolnictwo/`, `/wapno-nawozowe/` (noindex), hub `/wapnowanie-gleby/`, strona główna · **bez linku:** `/wapno-do-stawu/`, `/wapno-granulowane/`, `/kalkulator-wapnowania/`, `/zamowienia/` | curl 10.09 |
| indeks | PASS, „Strona przesłana i zindeksowana", ostatni crawl 2026-09-08 | URL Inspection 10.09 |
| stary adres | `/wapno-nawozowe-hurt/wapno-zawierajace-magnez-big-bag-1000kg/` → 301 na #313; w oknie GSC 2 klik., 204 wyśw., poz. 14,9 | GSC, curl 10.09 |

**GSC karty 2026-06-09 … 2026-09-06** (`data/produkty/gsc/tlenkowe-311-313.json`): **2 kliknięcia, 420 wyświetleń, CTR 0,48 %, poz. 13,4**
(poziom strony). Zapytania widoczne: 10 fraz, **0 kliknięć, 230 wyświetleń** (55 %). Widoczne: `wapno nawozowe tlenkowe` 78 poz. 13,4 ·
`wapno tlenkowo magnezowe` 35 poz. 10,4 · `wapno tlenkowe` 33 poz. 25,5 · `sprzedaż wapna tlenkowego` 31 poz. 24,4 · `wapno tlenkowe nawozowe` 28 poz. 20,7 ·
`wapno tlenkowe magnezowe` 19 poz. 10 · `wapno tlenkowe sypkie` 3 · `agria niedomice` 1 · `wapno nawozowe z magnezem` 1 poz. 36 · `wapno tlenkowe dawkowanie` 1 poz. 12.
**Karta #313 zbiera wyświetlenia na frazy rodzaju „tlenkowe" bez magnezu** — w GSC to jej największe zapytania.

**Zapytania ofertowe:** **0 z 11**. **Google Ads 13.08–09.09:** 0 kliknięć z reklam na kartę.

### Rozbieżności karta PDF ↔ strona

| parametr | karta PDF [K] | widoczna tabela [R] | schemat `pa_*` [R] |
|---|---|---|---|
| Zawartość | CaO + MgO 70/25 % | „Min. 70/25%" | min. 70% CaO · min. 25% MgO |
| Typ reakcji | **brak wiersza** | „Egzotermiczna" | „Egzotermiczna" |
| Zastosowanie | Odkwaszanie gleb **+ uzupełnienie magnezu** | **„Zastosowanie funkcjonalne": Odkwaszanie gleb średnich i ciężkich, poprawa struktury, zwiększenie plonów** — magnez znika z zastosowania | = karta |
| Dodatkowe zastosowanie | Rośliny magnezolubne (zboża, ziemniaki, rzepak) | **przyspieszenie mineralizacji mułu stawowego, Rekultywacja terenów zdegradowanych** | = karta |
| Forma dostawy | Big-bag 1000 kg | **brak wiersza** | = karta |
| Magazyn | Niedomice (33-132), Częstochowa (42-200) | „Częstochowa ( 42-200 ) Niedomice ( 33-132)" | zgodne |
| reaktywność, forma, frakcja, efekt, dawka, szybkość, segment, producent, dostępność | — | zgodne | zgodne |

**Twierdzenia w treści, których nie ma w karcie PDF** (`[J 10.09]`: tekst n8n DescWriter, bez źródła):
- „odczyn pH >12" (lead, dwa razy);
- „wzrost plonów o 15-20%";
- „stabilizacja parametrów wody w stawach", „Poprawa środowiska wodnego w stawach", FAQ 6 „przyspieszenia mineralizacji mułu stawowego
  oraz rekultywacji terenów zdegradowanych" — **karta nie ma rybactwa ani w segmencie, ani w piktogramach**;
- „bardzo wysoka reaktywność", „Błyskawiczne odkwaszanie" — karta: „Wysoka";
- „Wsparcie w pozyskiwaniu dofinansowania… karty charakterystyki oraz dokumenty jakościowe" — na `/do-pobrania/` dla #313 nie ma KCh;
- meta „CaO+MgO min. 70% (w tym MgO min. 25%)" — patrz §2.

**Z karty PDF nieobecne na stronie:** „Jeden rozsiew zamiast dwóch — oszczędność czasu, paliwa i robocizny" · „gleb … z deficytem magnezu" ·
rośliny magnezolubne (zboża, ziemniaki, buraki, rzepak) · magnez „kluczowy dla fotosyntezy, jakości plonu, odporności roślin" ·
„wapno tlenkowe reaguje znacznie szybciej niż węglanowe".

## 7. Konkurencja w wynikach (SERP mobile PL)

| fraza | top wyniki (abs) | AGRIA |
|---|---|---|
| `wapno tlenkowo magnezowe` (09.09) | 1 OLX · 3 OLX · 5 chemirol (70/25 0-1mm) · 6 nawozy.eu · 7 waprom · 8 allegro · 9 dlaroslin · 10 ifarmer (Dobromir) · **11 agria.pl #313** · 12 osadkowski · 19 industria · 20 gospodarz.pl · 24 chemiagro (Oxyfertil 70/25) | abs 11 |
| `wapno tlenkowe` (10.09, pilot) | 1 OLX · 3 osadkowski · 5 sklepogrodniczy · 6 polcalc · 7 nawozy.eu · 8 dobromir · 9 allegro · 10 orcal · 11 agrolok · 12 tech-mot | **abs 22 (#313)** |
| `wapno nawozowe tlenkowe` (09.09) | 1 AI Overview · 2 OLX · 5 nawozy.eu · 6 osadkowski · 7 chemirol · 8 sklepogrodniczy · 9 allegro · 11 agrolok · 12 orcal · 15 polcalc | **abs 19 (#313)** |
| `wapno z magnezem` (10.09) | 1 nawozy.eu · 3 allegro · 5 rolmat (granulowane 25 kg) · 6 dlaroslin · 7 agrozam · 8 poradnikogrodniczy · 9 agrosimex · 10 OLX · 11 industria · 12 YouTube; w PAA pytania o suplement w ciąży | poza top 20 |
| `wapno nawozowe z magnezem` (10.09) | 1 OLX · 4 dlaroslin · 5 rolmat · 6 industria · 7 allegro · 9 nawozy.eu · 11 ifarmer · 12 fregata · 13 metal-trans · 14 agrozam | poza top 20 |

Dane: `data/seo/2026-09-09-serp-widoczne-bez-klikniec.json`, `data/seo/2026-09-09-serp-karty.json`, `data/produkty/dfs/serp-*-2026-09-10.json`.

## 8. Luki — czego brakuje (fakty, bez propozycji struktury)

1. **Wyświetlenia bez kliknięć:** 420 wyświetleń → 2 kliknięcia (CTR 0,48 %) przy poz. 13,4; największe zapytania to rodzaj „tlenkowe" bez magnezu.
2. **Brak ceny i `offers`** — jedyny z trzech produktów tlenkowych bez kwoty; cennik pominął go bez komentarza.
3. **Zapis zawartości niejednoznaczny:** tabela „70/25 %", karta „min. 70% CaO + 25% MgO", meta „CaO+MgO min. 70% (w tym MgO min. 25%)".
4. **Magnez znika z widocznej tabeli** („Zastosowanie" bez magnezu, „Dodatkowe" o stawach i rekultywacji zamiast roślin magnezolubnych).
5. **Treść o stawach bez podstawy w karcie** (karta: tylko rolnictwo i hurtownie).
6. **Frazy „wapno magnezowe" (1 900) i „wapno z magnezem" (210)** — #313 w nich nie występuje; popyt na odmianę tlenkową z Mg ≈ 90/mies.
7. **Uprawy z karty** (zboża, ziemniaki, buraki, rzepak) nieobecne na stronie; frazy „wapno magnezowe pod …" ≤ 10/mies.
8. **Porównania brak** — strona nie zestawia z węglanowymi z Mg ani dolomitem (dawka 1–1,5 vs 1–6 t/ha, 2–4 tyg. vs 3–6 mies. na kartach)
   ani z Agrobielikiem 70 (tlenkowe bez Mg).
9. **Dokumenty:** brak atestu, KCh i linku do karty PDF.
10. **Schemat:** brak `FAQPage` przy 7 pytaniach. **Sprzedaż:** 0 zapytań ofertowych, 0 ogłoszeń OLX, 0 kliknięć z Ads.

## 9. Pytania do Janka / klienta (tylko to, czego karty nie rozstrzygają)

1. **Cena #313** — cennik z 07.08 go pominął; czy AGRIA ma na niego cenę (big-bag)?
2. **Zawartość: „min. 70% CaO + 25% MgO" czy „CaO+MgO min. 70%, w tym MgO min. 25%"?** Karta ma oba zapisy, meta strony — drugi. (Nie zmieniamy — pytanie o fakt.)
3. **Nazwa handlowa i zakład Lhoist** — czy to „Oxyfertil 70/25" (konkurencja sprzedaje taki zapis z frakcją 0–1 mm)? Z którego zakładu (magazyn: Częstochowa)?
4. **Buraki** — w tekście karty są, w tabeli nie ma. Który zapis jest właściwy?
5. **Odmiana** — w schemacie „Odmiana 02", karta nie podaje. Skąd ta wartość?
