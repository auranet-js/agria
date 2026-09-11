# Kreda malarska (WC #304)

> Karta AGRII: **BRAK** — produktu nie ma w katalogu drukowanym `Agria-katalog-2026-05-04-web.pdf` (0 trafień „malarsk" w tekście katalogu, 10.09;
> archiwum §9.2 zapisuje kartę w wersji katalogu z 15.04 — do wersji web z 04.05 nie weszła) · karta na stronie: `/kreda-malarska/kreda-malarska/` ·
> kategoria dziś: Kreda malarska (`/kreda-malarska/`, term 830 — jedyny produkt) · SKU AGR-016 · **stan na 10.09.2026**
>
> **Źródła (skróty używane niżej):**
> **[R]** render karty 10.09, `data/produkty/render/kreda-malarska.{html,json}` — **stan strony, nie źródło prawdy** ·
> **[C]** `docs/operations/CENNIK_PAWEL_2026-08-07.md` · **[F]** `docs/FAKTY_KLIENTA.md` §3 ·
> **[S]** opisy w SERP 10.09 (`data/produkty/dfs/serp-kredy-dolomit-2026-09-10.json`, `data/seo/2026-09-09-serp-widoczne-bez-klikniec.json`) — zewnętrzne, nie źródło
>
> ⚠️ **Bez karty AGRII parametrów nie ustalamy.** Wszystko w §1–§3 poza nazwą, producentem i ceną (cennik) to zapis ze strony (tekst DescWriter / atrybuty)
> i ma status „niepotwierdzone". Nie uzupełniamy z kart innych produktów ani z rozumowania.

---

## 1. Tożsamość

| cecha | wartość | źródło |
|---|---|---|
| nazwa | „Kreda malarska" | WC, [C] |
| producent | Lhoist | [F], [C], atrybut `pa_agria-producent` [R] |
| cena | 30 kg → 645 zł/t netto | [C] |
| forma dostawy | worek 30 kg | [C], atrybut `pa_agria-forma-dostawy` [R] |
| magazyn | atrybut: „Bukowa (29-105)" · widoczna tabela: „Bukowa (29-105) Niedomice (33-132)" — **rozjazd na stronie** | [R] |
| forma / frakcja | „Sypkie" / „Bardzo drobne" — tylko strona | [R] |
| zawartość CaO | „min. 53% CaO" — tylko strona (title, meta, tabela, FAQ) | [R] |
| kopalnia / zakład | **nieznane** | — |
| odmiana, karta producenta, atest | **brak** na `/do-pobrania/` | — |

**Opisy zewnętrzne tego typu towaru (nie źródło, zbieżność niezweryfikowana):** sklepogrodniczy.pl — „Kreda malarska Mączka wapienna 30 kg
**Lhoist** – mielony kamień wapienny CaCO3 do farb, zapraw i klejów"; kim24.pl — „Kreda malarska **BUKOWA**. Produkt otrzymywany przez
wysuszenie, zmielenie i separację kamienia wapiennego. Waga 30 kg; Paleta 35 sztuk"; ceneo.pl — „Bukowa Kreda Malarska 30kg (PL21K35)";
sklep.dabest.pl — „Kreda malarska 30kg… Producent: Lhoist" [S]. Czy to ten sam towar co AGRII (Lhoist, magazyn Bukowa, 30 kg) — pytanie w §9.

## 2. Parametry

**Brak karty AGRII — tabeli źródłowej nie ma.** Poniżej wyłącznie **stan strony** (widoczna tabela vs atrybuty `pa_*` w schemacie), do porównania
wewnętrznego, nie jako wiedza o produkcie.

| pozycja na stronie | widoczna tabela [R] | atrybut `pa_*` [R] |
|---|---|---|
| Zawartość CaO | Min. 53% CaO | min. 53% CaO |
| Typ reakcji | Długodziałająca(bezpieczna) | Długodziałająca(bezpieczna) |
| Forma fizyczna | Sypkie | Sypkie |
| Frakcja | Bardzo drobne | Bardzo drobne |
| Zastosowanie (funkcjonalne) | Poprawia przyczepność i krycie farby, wykorzystywana także jako dodatek do farb i zapraw | = |
| Efekt zastosowania | Poprawia mikroklimat wnętrza poprzez regulację wilgotności i jest bezpieczna oraz trwała. | = |
| Dawkowanie | 1 kg kredy na około 6–8 m² | = |
| Dodatkowe zastosowanie | Rolnictwo — odkwaszanie gleb, Rybactwo — wapnowanie stawów, Budownictwo i drogownictwo | **brak atrybutu** |
| Segment | Hurtownie, Rolnictwo | **pusty** (`value` = null) |
| Magazyn | Bukowa (29-105) Niedomice (33-132) | **Bukowa (29-105)** |
| Producent | Lhoist | Lhoist |
| Dostępność | Cały rok | Cały rok |
| Forma dostawy | brak wiersza | Worek 30 kg |

## 3. Zastosowania

**Karta AGRII nie istnieje — zastosowań źródłowo nie znamy.** Strona twierdzi (niepotwierdzone): poprawa przyczepności i krycia farby,
dodatek do farb i zapraw, regulacja wilgotności wnętrz, „1 kg kredy na około 6–8 m²", a także rolnictwo (odkwaszanie gleb), rybactwo
(wapnowanie stawów), budownictwo i drogownictwo. Meta: „Idealna dla hurtowni i rolnictwa".

Zapytania GSC, na które karta się pokazuje, są **ogrodnicze**: `kreda malarska w ogrodnictwie` 24 wyśw. (§6) — strona nie ma słowa „ogród".

## 4. Z czym go porównać

### 4.1 Produkty AGRII z rodziny kred

| | CaO | forma / frakcja | zastosowanie | producent · magazyn | forma dostawy | od zł/t netto |
|---|---|---|---|---|---|---|
| **#304 Kreda malarska** | strona: min. 53% | strona: sypkie, bardzo drobne | strona: farby, zaprawy | Lhoist · Bukowa (atrybut) | worek 30 kg | **645** (30 kg) |
| #307 Kreda pastewna | karta: min. 37% | sypkie, 4 frakcje | uzupełnienie Ca w paszach | Celiny (Hochel), Lhoist · Bukowa, Celiny | luz 24 t, worek 30 kg | 190 luz · 30 kg → 610 |
| #305 Kreda nawozowa granulowana | karta: min. 50% | granulat 3–6 mm | odkwaszanie gleb lekkich, stawy | KZK Kornica · Kornica, Niedomice | BB 500 kg, worek 25 kg | 410 BB · 25 kg → 490 |
| #306 Kreda nawozowa sypka odm. 06a | karta: min. 50% | sypkie, zmienna | odkwaszanie gleb lekkich, stawy | Kopalnia Drugnia · Pierzchnica | luz 24 t | 125 luz |

Fakty, bez wniosków: #304 i #307 mają **wspólnego producenta (Lhoist) i wspólny magazyn (Bukowa)** oraz ten sam worek 30 kg; worek kredy
malarskiej kosztuje wg cennika 645 zł/t, kredy pastewnej 610 zł/t. #304 jako jedyna kreda nie ma karty PDF.

### 4.2 Konkurencja (SERP mobile 09.09 i 10.09)

| sprzedawca | co | cena | gdzie widoczny |
|---|---|---|---|
| kim24.pl | „Kreda malarska 30 kg BUKOWA" | niezmierzone | **abs 1** `kreda malarska 30 kg`; abs 7 `kreda malarska` |
| ceneo.pl | „Bukowa Kreda Malarska 30kg (PL21K35)"; „Kreda Malarska 2Kg" | niezmierzone | abs 5 / abs 8 |
| sklepogrodniczy.pl | „Kreda malarska Mączka wapienna - 30 kg" (Lhoist) | niezmierzone | abs 4 / 11 |
| sklep.dabest.pl | „Kreda malarska 30kg", Producent: Lhoist | snippet: „28,40 zł brutto / szt. 23,09 zł netto" | abs 6 / 12 |
| allegro.pl, erli.pl | kreda malarska 1–30 kg, „ogrodnicza", „proszek" | niezmierzone | abs 2–23 |
| farbypigment, mrowka (Dragon 3 kg), bricomarche (Dorex 2 kg), sewera (Maluj Sam 5 kg), artmal | kreda malarska detal | niezmierzone | abs 6–19 |
| anex-wielichowo.pl | „Kreda malarska - Uprawa pieczarek" | — | abs 12 `…30 kg` |
| hurtowniasportowa.gniezno.pl | „Kreda do malowania linii boiskowych 30kg" | — | abs 13 `…30 kg` |

Popyt nawigacyjny na markety (DataForSEO Labs 10.09): `kreda malarska castorama` 90 · `leroy merlin` 50 · `mrówka` 40 · `obi` 40 · `bricomarche` 20.
**OLX, zrzut 28.08:** 0 ogłoszeń z „kreda malarska" (także AGRIA 0).

## 5. Frazy — popyt

Wolumen i CPC: planer Google Ads API (PL/polski, 12 mies. 2025-08 … 2026-07), 10.09 → `data/produkty/ads/kreda-malarska-planer.json`;
długi ogon: DataForSEO Labs `keyword_suggestions` 10.09 (`data/produkty/dfs/sugestie-kreda-malarska.json`, CPC w USD).
GSC: cały serwis 2026-06-09 … 2026-09-06. Macierz: `data/produkty/macierz/kreda-malarska.csv`.

| fraza | typ | wyszukań/mies. | CPC śr. zł | szczyt (rok-mies.) | nasz serwis w GSC 90 dni |
|---|---|---|---|---|---|
| kreda malarska | nazwa | **320** | 0,39 | **2026-06: 880** | **86 wyśw.**: karta 85 poz. 7,9; stary adres 1 poz. 10 · SERP mobile 09.09: AGRIA poza top 24 |
| kreda malarska 30 kg | nazwa + forma | 40 | 0,34 | 2026-06: 90 | 1 wyśw., karta poz. 20 · SERP 10.09: poza top 20 |
| kreda malarska w ogrodnictwie | nazwa + zastosowanie | 20 | 0,11 | 2026-05: 50 | **24 wyśw., karta poz. 8,9** |
| kreda malarska pod pomidory · ogrodnicza · zastosowanie · jak malować · skład · co to jest (DFS Labs) | nazwa + zastosowanie | po 10 | — | — | 0 wierszy |
| kreda malarska do bielenia · do drzew · do ogrodu · na ściany · do farby · na trawnik · do malowania · bielenie drzew kredą | nazwa + zastosowanie | <10 | — | — | 0 wierszy |
| kreda malarska proporcje · jak rozrobić kredę malarską | nazwa + dawka | <10 | — | — | 0 wierszy |
| kreda malarska castorama | nazwa + sklep | 90 | 0,53 | 2026-06: 210 | 0 wierszy |
| kreda malarska gdzie kupić | nazwa + zakup | 20 | 0,12 | 2026-06: 40 | 1 wyśw., karta poz. 5 |
| kreda malarska cena | nazwa + cena | 10 | 0,25 | 2026-06: 30 | 0 wierszy |
| kreda malarska 25kg (DFS Labs) | nazwa + forma | 10 | — | — | 0 wierszy |
| kreda malarska lhoist · kreda malarska sypka | producent / forma | <10 | — | — | 0 wierszy |
| kreda techniczna | rodzaj ogólny | 90 | 0,67 | 2025-10: 110 | 0 wierszy · SERP 10.09: kreda do znakowania (Topex, Castorama); trzuskawica.pl abs 10 |
| kreda pylista | rodzaj ogólny | 20 | 0,42 | 2026-03: 40 | 0 wierszy |
| kreda do bielenia · mączka kredowa | rodzaj ogólny | <10 | — | — | 0 wierszy |
| kreda malarska czy wapno · …a wapno do bielenia · …a kreda nawozowa | porównanie | <10 | — | — | 0 wierszy |

Popyt na nazwę jest **sezonowy z górką w czerwcu** (880 wobec średniej 320). Ogon ma dwie osie: **zakup w marketach** (castorama/leroy/mrówka/obi
≈ 240 łącznie) i **ogród** (`w ogrodnictwie`, `pod pomidory`, `ogrodnicza`). Popytu na producenta nie ma.
**Google Ads 13.08–09.09:** fraz z „kreda malarska" w wyszukiwanych brak; `kreda ogrodnicza` 7 wyśw. (kampania Rolnictwo).

## 6. Stan dziś na stronie (render 10.09, nie baza)

| element | stan | źródło |
|---|---|---|
| title | „Kreda malarska min. 53% CaO \| AGRIA" | [R] |
| meta description | „Kreda malarska Agria (min. 53% CaO) to sypki produkt poprawiający przyczepność i krycie farby. Idealna dla hurtowni i rolnictwa. Zapytaj o ofertę!" | [R] |
| H1 | „Kreda malarska" (= nazwa WC) | [R] |
| H2 | „Kreda malarska: poprawa przyczepności i krycia farby" · „Wszechstronne zastosowanie, mierzalne efekty" · „Specyfikacja techniczna" · „Kreda malarska — cena" · „Najczęściej zadawane pytania" · „Zapytaj o ofertę, zamów próbkę" | [R] |
| treść | **4 856 znaków** od H1 do formularza | [R] |
| FAQ | 7 pytań (dawkowanie, zastosowania poza malowaniem, bezpieczeństwo, CaO, forma, dostępność, zamówienie); **brak `FAQPage`** | [R] |
| cena w treści | „Kreda malarska kosztuje od 645 zł/t netto w workach 30 kg. Podane kwoty dotyczą samego towaru, bez transportu." — zgodna z [C] | [R] |
| schema `Product` | `offers` 645 PLN, `unitCode: TNE`; atrybut `pa_agria-segment` pusty | [R] |
| zdjęcie | `2026/09/kreda-malarska-agria.webp` | [R] |
| PDF | brak (karty nie ma) | [R] |
| listingi z linkiem do #304 | `/kreda-malarska/` (2), `/oferta/page/2/` · **bez linku:** strona główna, `/oferta/` str. 1, `/wapnowanie-gleby/`, `/zamowienia/` | curl 10.09 |
| indeks karty | PASS, „Strona przesłana i zindeksowana", crawl 2026-08-18 | URL Inspection 10.09 |
| indeks kategorii `/kreda-malarska/` | **„Adres URL jest Google nieznany"**; GSC 90 dni: 0 wyświetleń | URL Inspection 10.09, `data/produkty/gsc/kredy-stare-adresy.json` |
| stary adres | `/wapno-nawozowe-hurt/kreda-malarska-worek-30kg/` → 301 na kartę; GSC 90 dni: 27 wyśw., 1 klik., poz. 6,2 | curl 10.09, GSC |

**GSC karty, 2026-06-09 … 2026-09-06** (`data/produkty/gsc/kreda-malarska.json`): **6 kliknięć, 284 wyświetlenia, CTR 2,11 %, poz. 7,1**.
Zapytania widoczne: 5 fraz, 0 kliknięć, 112 wyświetleń — próg prywatności ukrywa wszystkie 6 kliknięć i 61 % wyświetleń.
Widoczne: `kreda malarska` 85 poz. 7,9 · `kreda malarska w ogrodnictwie` 24 poz. 8,9 · `kreda malarska 30 kg` 1 poz. 20 ·
`kreda malarska gdzie kupić` 1 poz. 5 · `podaj producentów` 1 poz. 5. ⚠️ GSC (średnia 90 dni, wszystkie urządzenia) poz. 7,9 na `kreda malarska`
wobec **braku AGRII w top 24 SERP mobile 09.09** — dwie różne miary, obie zapisane.

**Zapytania ofertowe** (CPT `agria_inquiry`, MCP 10.09): **0 z 11 prawdziwych**. **Google Ads 13.08–09.09:** karta nie była celem reklam (brak w `landing_page_view`).

### Rozbieżności

**Karta PDF ↔ strona — nie da się sprawdzić (brak karty).** Rozbieżności wewnątrz strony:
- **Magazyn:** widoczna tabela „Bukowa, Niedomice", atrybut tylko „Bukowa";
- **Dodatkowe zastosowanie** (rolnictwo, rybactwo, budownictwo, drogownictwo) i **Segment** — są w widocznej tabeli, nie ma ich w atrybutach;
- **Forma dostawy:** FAQ 5 „od mniejszych ilości po dostawy całopojazdowe", a atrybut, cennik i sekcja ceny — tylko worek 30 kg;
- „35-letniemu doświadczeniu" (FAQ 6) vs „Agria — 37 lat doświadczenia" (sekcja formularza).

**Wszystkie parametry i zastosowania na stronie** (53% CaO, typ reakcji „długodziałająca", 6–8 m²/kg, regulacja wilgotności, odkwaszanie gleb,
wapnowanie stawów, drogownictwo) — **bez źródła** (`[J 10.09]`: tekst DescWriter).

## 7. Konkurencja w wynikach (SERP mobile PL)

| fraza | top wyniki (abs) | AGRIA |
|---|---|---|
| `kreda malarska` (09.09) | 1 AI Overview · 2 allegro · 6 farbypigment · 7 kim24 (Bukowa 30 kg) · 8 ceneo · 9 OLX · 10 mrowka · 11 sklepogrodniczy · 12 dabest · 14 erli · 17 sewera · 18 artmal · 19 bricomarche · 22 szarada · 24 Wikipedia | **poza top 24** |
| `kreda malarska 30 kg` (10.09) | **1 kim24 (Bukowa)** · 3 allegro · 4 sklepogrodniczy (Lhoist) · 5 ceneo (Bukowa) · 6 dabest (Lhoist) · 8 popular products · 9 erli · 10 farbypigment · 11 OLX · 12 anex-wielichowo (pieczarki) · 13 linie boiskowe | poza top 20 |
| `kreda techniczna` (10.09) | 1 castorama (Topex) · 4 najder · 6 toya24 · 7 kreda.pl · 8 speckable · 9 bricomarche · 10 trzuskawica.pl · 11 bricoman · 12 tim · 15 leroymerlin | poza top 20 |

## 8. Luki — czego brakuje (fakty, bez propozycji struktury)

1. **Brak karty AGRII, karty producenta i atestu** — żadnego parametru na stronie nie da się potwierdzić; produkt nie wszedł do katalogu 04.05.
2. **Kategoria `/kreda-malarska/` jest Google nieznana**; karta zindeksowana, ostatni crawl 18.08.
3. **Popyt ogrodniczy** (`w ogrodnictwie` 24 wyśw. karty w GSC, `pod pomidory`, `ogrodnicza`) wobec treści o farbach i hurtowniach — słowo „ogród" nie pada.
4. **Popyt sezonowy** — szczyt czerwiec (880/mies.); karta ma 85 wyświetleń na frazę główną w 90 dniach VI–IX.
5. **Konkurencja z tym samym oznaczeniem** — „Bukowa" i „Lhoist" w tytułach sklepów w top 6 na `kreda malarska 30 kg`; AGRIA poza top 20.
6. **Rozjazd wewnątrz strony** (magazyn, segment, dodatkowe zastosowanie, forma dostawy) — lista w §6.
7. **Sprzedaż:** 0 zapytań ofertowych, 6 kliknięć organicznych w 90 dniach, brak w Ads i na OLX.
8. **Schemat:** brak `FAQPage` przy 7 pytaniach; atrybut segmentu pusty.

## 9. Pytania do Janka / klienta (tylko to, czego karty nie rozstrzygają)

1. **Czy klient ma kartę techniczną / kartę producenta Lhoist dla kredy malarskiej?** Bez niej 53% CaO, „6–8 m² z 1 kg" i wszystkie zastosowania
   ze strony zostają bez źródła.
2. **Magazyn:** tylko Bukowa (atrybut, cennik nie mówi) czy także Niedomice (widoczna tabela)?
3. **„Kreda malarska Bukowa 30 kg"** w kim24 / ceneo i „Lhoist 30 kg" w sklepogrodniczy / dabest — czy to ten sam towar, który sprzedaje AGRIA?
