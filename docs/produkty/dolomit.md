# Dolomit (WC #302)

> Karta AGRII: `agria-karta-produktu-dolomit.pdf` · karta na stronie: `/wapno-nawozowe-rolnictwo/dolomit/` ·
> kategoria dziś: Wapno nawozowe (`/wapno-nawozowe-rolnictwo/`, term 764) · SKU AGR-012 · **stan na 10.09.2026**
>
> **Źródła (skróty używane niżej):**
> **[K]** karta AGRII PDF, `data/produkty/pdf/agria-karta-produktu-dolomit.pdf` (pobrana 10.09; 47 z 47 linii tekstu identyczne z katalogiem
> drukowanym `Agria-katalog-2026-05-04-web.pdf`; wg archiwum §9.1 karta Dolomitu była ręcznym szablonem całego katalogu) ·
> **[R]** render karty 10.09, `data/produkty/render/dolomit.{html,json}` · **[C]** `docs/operations/CENNIK_PAWEL_2026-08-07.md` ·
> **[F]** `docs/FAKTY_KLIENTA.md` §3 (ceny Dolomitu z 24.08, forma luz 24 t potwierdzona przez Janka 07.09) ·
> **[IUNG]** `data/zrodla/IUNG-PIB-2021-…txt` · **[S]** opisy w SERP 10.09 — zewnętrzne, nie źródło

---

## 1. Tożsamość (z karty PDF — cytaty)

| cecha | wartość | źródło |
|---|---|---|
| nazwa na karcie | „Dolomit" — zgodna 1:1 z nazwą w WC | [K] |
| nagłówek | „Odkwaszanie z magnezem dla gleb lekkich" | [K] |
| opis | „Naturalny nawóz wapniowo-magnezowy w formie sypkiej. CaO + MgO min 45%, reaktywność 70–90%, działanie długotrwałe (3–6 miesięcy). Dedykowany glebom lekkim i piaszczystym z deficytem Mg, gospodarstwom ekologicznym i sadom." | [K] |
| odmiana / typ wg rozporządzenia | **karta nie podaje**; atrybut `pa_agria-norma` na stronie: „Odmiana 05" (widoczny tylko w schemacie) | [K], [R] |
| producent | „Siarkopol" | [K] |
| kopalnia / zakład | **karta nie podaje** | [K] |
| magazyny wysyłkowe | „Tarnobrzeg (39-400), Niedomice (33-132)" | [K] |
| rodzaj | nawóz **wapniowo-magnezowy**, z magnezem („w tym MgO min 15%"); słowa „węglanowy" karta nie używa | [K] |
| forma fizyczna / frakcja | „Sypkie" / „0-2mm" | [K] |
| formy dostawy | tabela: „Worek 10 kg, worek 25 kg" · korzyści: „Worki 10 i 25 kg — wygodne dla mniejszych gospodarstw". **Luzu karta nie wymienia** | [K] |
| segment / piktogramy | tabela: „Hurtownie, rolnictwo" · piktogramy: ROLNICTWO, SADOWNICTWO, HURTOWNIE | [K] |
| dostępność | „Cały rok" | [K] |

⚠️ **Rozbieżność karta ↔ cennik:** ceny [F]/[C] dotyczą **luzu 24 t i frakcji 0,1–0,4 / 0,4–0,8 / 1–3 mm** (od 260 i 280 zł/t netto);
karta PDF ma **worki 10 i 25 kg i frakcję 0–2 mm**. Żadna z trzech frakcji z cennika nie występuje na karcie. Pytanie w §9.

Zewnętrznie (nie źródło): sklepchojnacki.pl — „Dolomit Mielony **Siarkopol** to naturalny nawóz wapniowo-magnezowy w formie węglanowej", worek 25 kg [S].

## 2. Parametry

### 2.1 Tabela z karty AGRII — 1:1

| parametr | wartość |
|---|---|
| Zawartość CaO | CaO + MgO min 45% w tym MgO min 15% |
| Reaktywność | ~70–90% |
| Typ reakcji | Długodziałająca (bezpieczna) |
| Forma fizyczna | Sypkie |
| Frakcja | 0-2mm |
| Zastosowanie | Działanie długoterminowe. Odkwaszanie gleb lekkich i piaszczystych, poprawa struktury gleby |
| Efekt zastosowania | Wzrost pH gleby. Uzupełnienie magnezu i wapnia pokarmowego |
| Dawkowanie | 1,5-6 t/ha |
| Szybkość działania | Długotrwałe (3-6 miesięcy) |
| Dodatkowe zastosowanie | Gospodarstwa ekologiczne, sadownictwo, uprawy wieloletnie |
| Segment | Hurtownie, rolnictwo |
| Forma dostawy | Worek 10 kg, worek 25 kg |
| Magazyn | Tarnobrzeg (39-400), Niedomice (33-132) |
| Producent | Siarkopol |
| Dostępność | Cały rok |

Karta **nie podaje**: CaO osobno (tylko sumę CaO + MgO i minimum MgO), odmiany, pH, metali ciężkich, kopalni. Wiersz nazywa się
„Zawartość CaO", a niesie sumę CaO + MgO — tak jest w samej karcie (por. T-108 w rejestrze: skrypt `extract_cao_percent` czyta tę sumę jako CaO).
**Atestu ani karty producenta Siarkopolu na `/do-pobrania/` nie ma.**

## 3. Zastosowania (z karty)

| co | co mówi karta [K] |
|---|---|
| do czego | „Odkwaszanie gleb lekkich i piaszczystych, poprawa struktury gleby" · „Uzupełnienie magnezu i wapnia pokarmowego" |
| gleby | „glebom lekkim i piaszczystym z deficytem Mg" |
| gdzie / dla kogo | „gospodarstwom ekologicznym i sadom" · „Gospodarstwa ekologiczne, sadownictwo, uprawy wieloletnie" · „idealny dla hurtowni, rolnictwa oraz gospodarstw ekologicznych" |
| korzyści | „Wapń i magnez w jednym przejeździe — bez osobnej aplikacji kizerytu" · „Bezpieczne dla próchnicy — nie wypala materii organicznej" · „Długotrwały efekt 3–6 miesięcy — stabilna korekta pH" |
| dawka | 1,5–6 t/ha |
| kiedy | termin **nie podany**; dostępność cały rok |

**Karta nie mówi:** terminu stosowania, dawek dla sadów i upraw wieloletnich, łączenia z innymi nawozami, trawników i ogrodów (piktogram SADOWNICTWO — tak).

Źródła uzupełniające — **o wapnie magnezowym ogólnie, nie o tym produkcie:** [IUNG] (tekst, linie 1001–1006): gleby kwaśne, „zwłaszcza lekkie,
wykazują z reguły niską zawartość przyswajalnego dla roślin magnezu… duże dawki wapnia powodują niekorzystne poszerzenie tego stosunku [Ca:Mg]
i dlatego powinny być stosowane w postaci wapna magnezowego"; s. 59: „Nawozy wapniowo-magnezowe są w Polsce głównym źródłem magnezu."

## 4. Z czym go porównać

### 4.1 Produkty AGRII z magnezem — różnice z kart PDF, ceny z [C]/[F]

| | CaO + MgO | forma / frakcja | dawka | szybkość | producent · magazyny | formy dostawy (karta) | od zł/t netto, bez transportu |
|---|---|---|---|---|---|---|---|
| **#302 Dolomit** | suma min. 45%, w tym MgO min. 15% | sypkie 0–2 mm | 1,5–6 t/ha | 3–6 mies. | Siarkopol · Tarnobrzeg, Niedomice | worek 10 kg, 25 kg | **260** (0,1–0,4 i 0,4–0,8 mm) · **280** (1–3 mm), luz 24 t [F] |
| #318 Węglanowe z Mg — odm. 04 | min. 41% CaO + min. 8% MgO | sypka 0–2 mm | 1,5–6 t/ha | 3–6 mies. | Kopalnia Jażwica (Industria) · Chęciny | luz 25–27 t | 50 luz |
| #319 Węglanowe z Mg — odm. 05 | CaO 25–37%, MgO 8–20% | sypkie 0–2 mm | 1,5–6 t/ha | 3–6 mies. | Kopalnia Laskowa, Kopalnia Winna (Industria) · Łagów, Kostomłoty Drugie | luz | 36 luz |
| #317 Węglanowe z Mg granulowane | min. 31% CaO + 16% MgO | granulat 3–6 mm | 1–6 t/ha | 3–6 mies. | Grankal · Draby, Niedomice | BB 600 kg, worek 25 kg | 370 BB · 25 kg → 410 |
| #313 Tlenkowe zawierające magnez | 70/25% | sypkie 0–1 mm | 1–1,5 t/ha | 2–4 tyg. | Lhoist · Niedomice, Częstochowa | BB 1000 kg | brak ceny |

Fakty z tabeli, bez wniosków: Dolomit ma na karcie **tę samą frakcję, dawkę i szybkość działania co #318 i #319**; minimum MgO 15% wobec 8%
(#318), 8–20% (#319) i 16% (#317). W cenniku Dolomit kosztuje 260–280 zł/t luz wobec 50 (#318) i 36 zł/t (#319). Wśród produktów z magnezem
tylko Dolomit ma na karcie **worki 10 kg**.

### 4.2 Konkurencja (SERP mobile 10.09, OLX 28.08)

| sprzedawca | co | cena | gdzie widoczny |
|---|---|---|---|
| target.com.pl, dlaroslin.pl | poradniki + dolomit ogrodniczy; leroymerlin „Nawóz dolomit 10kg Target" | niezmierzone | abs 1–6 |
| sklepchojnacki.pl | „NAWÓZ DOLOMIT MIELONY 25KG" — Siarkopol | niezmierzone | abs 11 `dolomit` |
| poradnikogrodniczy, ogrodomi, kwiateo, ochrona-roslin, fungichem, mrowka (Rolimpex) | dolomit 10–25 kg | niezmierzone | abs 5–12 |
| zielonepogotowie.pl, dziendobryogrod.pl | Biovita „Dolomit nawóz wapniowo-magnezowy 20 kg" | niezmierzone | abs 9–12 |
| agrolok.pl · agrii.pl | „Wapno dolomitowe z magnezem - luz" · „Nasze Wapno Dolomitowe Premium/luz" | niezmierzone | abs 7 / 13 `wapno dolomitowe` |
| cenynawozow.pl | „Dolomit - 22.07.2026 - Ceny nawozów" | — | abs 8 `dolomit cena za tonę` |
| holcim, handlobud, kaskada, kruszywa-mikolow | **dolomit jako kruszywo** | — | `dolomit`, `dolomit cena za tonę` |

**OLX, zrzut 28.08:** 15 ogłoszeń ze słowem „dolomit" w treści, 6 sprzedawców, **AGRIA 0**. W tytule „dolomitowe" ma tylko jedno
(Dawid, Siewierz, „Wapno nawozowe wapniowo-magnezowe dolomitowe", 95 zł — jednostka wg ogłoszenia niezweryfikowana); pozostałe to wapno
magnezowe „z przemiału surowego dolomitu" (Mateusz, 28–29,99 zł; Tadeusz — „Kopalnia JAŹWICA", 48 zł; CARLOS, 35 zł) i OrCal.

## 5. Frazy — popyt

Wolumen i CPC: planer Google Ads API (PL/polski, 12 mies. 2025-08 … 2026-07), 10.09 → `data/produkty/ads/dolomit-planer.json`;
dla „siarkopol" DataForSEO Labs 10.09 (`data/produkty/dfs/sugestie-siarkopol.json`, CPC w USD). GSC: cały serwis 2026-06-09 … 2026-09-06.
Macierz: `data/produkty/macierz/dolomit.csv`.

| fraza | typ | wyszukań/mies. | CPC śr. zł | szczyt (rok-mies.) | nasz serwis w GSC 90 dni |
|---|---|---|---|---|---|
| dolomit | nazwa | **6 600** | 0,36 | 2026-03: 9 900 | 0 wierszy · SERP 10.09: Wikipedia (minerał), poradniki, kruszywo, suplement w tabletkach, Dolomity (PAA); AGRIA poza top 20 |
| dolomit nawóz | nazwa + rodzaj | **880** | 0,54 | 2026-03: 1 900 | 1 wyśw., hub `/wapnowanie-gleby/` poz. 6 · SERP: poza top 20 |
| wapno dolomitowe | nazwa + rodzaj | **720** | 0,52 | 2025-09: 1 000 | 0 wierszy · SERP: poza top 20 |
| dolomit wapno | nazwa + rodzaj | 390 | 0,48 | 2026-03: 880 | 0 wierszy |
| dolomit nawozowy | nazwa | 10 | — | 2026-02: 20 | 0 wierszy |
| dolomit na trawnik | nazwa + zastosowanie | **590** | 0,68 | 2026-03: 1 900 | 0 wierszy |
| dolomit do ogrodu | nazwa + zastosowanie | 70 | 0,31 | 2026-03: 170 | 0 wierszy |
| dolomit na działkę · dolomit na warzywa | nazwa + zastosowanie | 10 | — | — | 0 wierszy |
| dolomit na pole · dolomit do sadu · dolomit rolnictwo ekologiczne | nazwa + zastosowanie | <10 | — | — | 0 wierszy |
| dolomit dawkowanie | nazwa + dawka | 40 | — | 2025-10: 90 | 0 wierszy |
| dolomit ile na hektar | nazwa + dawka | <10 | — | — | 0 wierszy |
| dolomit cena | nazwa + cena | 140 | 0,50 | 2026-03: 320 | 0 wierszy |
| dolomit cena za tonę | nazwa + cena | 90 | 0,52 | 2026-03: 140 | 0 wierszy · SERP: kruszywo dolomitowe |
| wapno dolomitowe cena | nazwa + cena | 50 | 0,85 | 2025-10: 140 | 0 wierszy (Ads: `wapno dolomitowe cena` 2 wyśw.) |
| dolomit nawóz cena | nazwa + cena | 10 | 0,42 | 2026-03: 30 | 0 wierszy |
| dolomit 25 kg · dolomit 10 kg | nazwa + forma | 50 · 40 | 1,33 · 0,53 | 2026-03: 210 · 110 | 0 wierszy |
| dolomit mielony | nazwa + forma | 40 | 0,21 | 2026-03: 90 | 0 wierszy |
| dolomit luzem | nazwa + forma | <10 | — | — | 0 wierszy |
| siarkopol | producent | 1 300 | 0,80 | 2026-03: 1 600 | 0 wierszy · DFS Labs: intencje firmowe — `siarkopol tarnobrzeg` 880, `siarkopol gdańsk` 320, `siarkopol grzybów` 260, praca; nawozowe: `siarkopol nawozy` 110, `nawóz siarkopol` 50, `siarczan magnezu siarkopol` 170 |
| siarkopol dolomit · dolomit tarnobrzeg | producent / magazyn | <10 | — | — | 0 wierszy |
| wapno magnezowe | rodzaj ogólny | **1 900** | 0,60 | 2025-08: 4 400 | 27 wyśw.: hub poz. 2,5; #317 poz. 48,9 |
| nawóz wapniowo magnezowy | rodzaj ogólny | 260 | 0,83 | 2026-03: 720 | 0 wierszy |
| wapno z magnezem | rodzaj ogólny | 210 | 0,32 | 2026-03: 390 | 2 wyśw., hub poz. 2 |
| dolomit czy wapno | porównanie | 20 | — | 2026-03: 50 | 0 wierszy |
| dolomit a wapno magnezowe · dolomit czy kreda | porównanie | <10 | — | — | 0 wierszy |

Szczyt popytu na dolomit to **marzec** (`dolomit` 9 900, `dolomit nawóz` i `dolomit na trawnik` po 1 900). Fraza główna jest rozszczepiona
(minerał, kruszywo, suplement, Dolomity) — ustalenie z [F] (24.08) potwierdzone SERP-em 10.09. Frazy nawozowe: `dolomit nawóz` 880,
`wapno dolomitowe` 720, `dolomit wapno` 390, `dolomit na trawnik` 590; SERP na nie jest **detaliczno-ogrodniczy (worki 10–25 kg)**.
Na producenta (Siarkopol) popyt jest, ale głównie firmowy, nie na dolomit.

**Google Ads 13.08–09.09** (`data/produkty/ads/search-terms-dolomit.json`, kampania Rolnictwo): 17 fraz z „dolomit", 39 wyśw., 5 klik.,
10,34 zł — m.in. `dolomit nawóz` 9 wyśw. 2 klik., `wapno dolomitowe` 6, `dolomit nawoz wapniowo magnezowy` 5.

## 6. Stan dziś na stronie (render 10.09, nie baza)

| element | stan | źródło |
|---|---|---|
| title | „Dolomit \| Nawóz wapniowo-magnezowy AGRIA" | [R] |
| meta description | „Dolomit AGRIA: naturalny nawóz wapniowo-magnezowy (**min. 30% CaO**, min. 15% MgO) do odkwaszania gleb lekkich i piaszczystych… Idealny dla ekologicznych gospodarstw." | [R] |
| H1 | „Dolomit" (= nazwa WC) | [R] |
| H2 | „Dolomit: naturalne odkwaszanie i poprawa struktury gleb" · „Trwałe odkwaszanie i regeneracja gleby" · „Specyfikacja techniczna" · „Dolomit — cena" · „Najczęściej zadawane pytania" · „Zapytaj o ofertę, zamów próbkę" | [R] |
| treść | **5 538 znaków** od H1 do formularza; na końcu blok „Poradniki techniczne" (2 linki) | [R] |
| FAQ | 7 pytań (dawkowanie, gleby lekkie, okres działania, ekologia, frakcja, opakowania, zamówienie); **brak `FAQPage`** | [R] |
| cena w treści | „Dolomit kosztuje od 260 zł/t netto przy dostawie całosamochodowej 24 t luzem — dotyczy frakcji 0,1–0,4 mm oraz 0,4–0,8 mm. Frakcja 1–3 mm kosztuje od 280 zł/t netto…" — zgodna z [F] (T-100, 07.09) | [R] |
| schema `Product` | `offers` 260 PLN, `unitCode: TNE`; `additionalProperty` = atrybuty `pa_*` (= karta) + „Odmiana 05" + „min. 15% MgO" | [R] |
| zdjęcie | `2026/02/wapno-nawozowe-weglanowe-zawierajace-magnez-agria.jpg` — nazwa pliku wskazuje na inny produkt | [R] |
| PDF | karta **nie linkuje** do swojej karty PDF | [R] |
| listingi z linkiem do #302 | `/oferta/`, `/wapno-nawozowe-rolnictwo/`, `/wapno-nawozowe/` (noindex), hub `/wapnowanie-gleby/` · **bez linku:** strona główna, `/kalkulator-wapnowania/`, `/zamowienia/` | curl 10.09 |
| indeks | **PASS, „Strona przesłana i zindeksowana", crawl 2026-09-09** — 24.08 [F] zapisał „Discovered — currently not indexed" | URL Inspection 10.09 |

**GSC karty, 2026-06-09 … 2026-09-06** (`data/produkty/gsc/dolomit.json`): **0 kliknięć, 0 wyświetleń** — karta weszła do indeksu dopiero po
ręcznym zgłoszeniu 09.09 (podsumowanie 10.09 §2.5), okno GSC kończy się 06.09. Wyświetleń po wejściu do indeksu jeszcze nie ma w danych.
W całym serwisie „dolomit" — 2 wiersze (hub): `dolomit nawóz` 1 wyśw. poz. 6, `wapno dolomitowe cena za tonę` 1 poz. 2.

**Zapytania ofertowe** (CPT `agria_inquiry`, MCP 10.09): **0 z 11 prawdziwych**. **Google Ads 13.08–09.09:** karta nie była celem reklam.

### Rozbieżności karta PDF ↔ strona

| parametr | karta PDF [K] | strona [R] | schemat `pa_*` [R] |
|---|---|---|---|
| Zawartość | CaO + MgO min 45% w tym MgO min 15% | tabela zgodna; **lead, meta, lista korzyści i punkt 1: „min. 30% CaO"** (4 miejsca) | „CaO + MgO min. 45% (w tym MgO min. 15%)" + „min. 15% MgO" |
| Odmiana | brak | brak | **„Odmiana 05"** |
| Forma dostawy | Worek 10 kg, worek 25 kg | **brak wiersza**; sekcja ceny: **„luz 24 t"**; FAQ 6: „od mniejszych ilości po dostawy całopojazdowe" | Worek 10 kg, Worek 25 kg |
| Frakcja | 0-2mm | tabela i FAQ 5: 0–2 mm; **sekcja ceny: 0,1–0,4 / 0,4–0,8 / 1–3 mm** | 0–2 mm |
| Dawkowanie | 1,5-6 t/ha | tabela zgodna; **FAQ 1: „od 1 do 5–6 ton na hektar"** | 1,5–6 t/ha |
| Magazyn | Tarnobrzeg, Niedomice | tabela zgodna; lead i korzyści: „z magazynu w Tarnobrzegu" (tylko jeden) | zgodny |
| Szybkość | Długotrwałe (3-6 miesięcy) | tabela zgodna; FAQ 3 bez liczby („utrzymują się przez dłuższy czas") | zgodna |
| Zastosowanie | Działanie długoterminowe. Odkwaszanie… | „Zastosowanie funkcjonalne: Działanie długoterminowe, Odkwaszanie…" | zgodne |
| Reaktywność, typ reakcji, forma, efekt, dodatkowe zastosowanie, segment, producent, dostępność | — | zgodne | zgodne |

**Twierdzenia w treści, których nie ma w karcie PDF** (`[J 10.09]`: tekst DescWriter, bez źródła): „min. 30% CaO"; „zwiększając ich zdolność
do zatrzymywania wody i składników odżywczych"; „sprzyja lepszemu ukorzenianiu i wzrostowi plonów"; „zgodność z wymogami certyfikowanych
produkcji"; magnez „kluczowy dla fotosyntezy"; „Wysoka reaktywność (~70-90%)" (karta: reaktywność ~70–90%, typ „Długodziałająca").

**Z karty PDF nieobecne na stronie:** „Wapń i magnez w jednym przejeździe — bez osobnej aplikacji kizerytu", „Worki 10 i 25 kg — wygodne dla
mniejszych gospodarstw", „z deficytem Mg", sadownictwo jako piktogram (w tekście strony jest).

## 7. Konkurencja w wynikach (SERP mobile PL, 10.09)

| fraza | top wyniki (abs) | AGRIA |
|---|---|---|
| `dolomit` | knowledge graph · 3 Wikipedia (minerał) · 5 target · 6 dlaroslin · 7 holcim (kruszywo) · 11 sklepchojnacki (Siarkopol 25 kg) · 13 doradcatechmot · 14 medicare (tabletki) · 15 fusima (kamienie) · 16 poradnikogrodniczy · 18 planta; local pack ×9 | **poza top 20** |
| `dolomit nawóz` | 1 target · 3 dlaroslin · 4 popular products · 5 ogrodomi · 7 poradnikogrodniczy · 8 ochrona-roslin · 9 doradcatechmot · 10 Biovita · 11 kwiateo · 12 dziendobryogrod · 14 leroymerlin | poza top 20 |
| `wapno dolomitowe` | 1 AI Overview · 2 fungichem · 4 OLX · 5 ph70.pl · 6 dlaroslin · 7 agrolok (luz) · 9 zielonepogotowie · 10 poradnikogrodniczy · 11 ochrona-roslin · 12 mrowka · 13 agrii (luz) | poza top 20 |
| `dolomit cena za tonę` | 1 OLX (kruszywo) · 3 handlobud · 7 kaskada · 8 cenynawozow.pl · 10 kruszywa-mikolow · 11 poradnikogrodniczy · 12 OLX · 13 sprzedajemy | poza top 20 |

PAA na `dolomit nawóz`: „Kiedy sypie się dolomit?", „Co jest lepsze, dolomit czy wapno?", „Pod jakie rośliny sypać dolomit?".
Dane: `data/produkty/dfs/serp-kredy-dolomit-2026-09-10.json`.

## 8. Luki — czego brakuje (fakty, bez propozycji struktury)

1. **Karta dopiero weszła do indeksu (09.09)** — w 90 dniach 0 wyświetleń; na żadną z 5 badanych fraz AGRIA nie ma w top 20.
2. **Popyt nawozowy ≈ 2 600/mies.** (`dolomit nawóz` 880, `wapno dolomitowe` 720, `dolomit na trawnik` 590, `dolomit wapno` 390) — SERP na te frazy
   to sklepy ogrodnicze z workami 10–25 kg; karta PDF ma worki 10 i 25 kg, strona o nich nie mówi (cena tylko dla luzu 24 t).
3. **Sprzeczność formy i frakcji:** karta PDF (worki, 0–2 mm) vs sekcja ceny (luz 24 t, trzy inne frakcje) — na jednej stronie.
4. **„min. 30% CaO"** w czterech miejscach treści — liczby nie ma w karcie.
5. **Termin stosowania** — karta go nie podaje; szczyt popytu w marcu, PAA pyta „Kiedy sypie się dolomit?".
6. **Porównania brak** — z #318/#319 (ta sama frakcja, dawka, szybkość; 36–50 wobec 260–280 zł/t) i z „wapnem" (PAA „dolomit czy wapno").
7. **Zdjęcie** z nazwą pliku innego produktu; karta nie linkuje do swojej karty PDF.
8. **OLX:** AGRIA 0 ogłoszeń z dolomitem (inni sprzedawcy — 15 ogłoszeń ze słowem „dolomit").
9. **Schemat:** brak `FAQPage` przy 7 pytaniach; atrybut „Odmiana 05" bez pokrycia w karcie.

## 9. Pytania do Janka / klienta (tylko to, czego karty nie rozstrzygają)

1. **Forma i frakcje:** karta PDF — worki 10/25 kg, frakcja 0–2 mm; cennik i strona — luz 24 t, frakcje 0,1–0,4 / 0,4–0,8 / 1–3 mm. Czy AGRIA ma
   dwa różne dolomity od Siarkopolu (workowany 0–2 mm i luzem w trzech frakcjach), czy któraś wersja jest nieaktualna? Czy worki mają cenę?
2. **„Odmiana 05"** w atrybucie strony — skąd? Karta PDF odmiany nie podaje.
3. **Kopalnia / zakład Siarkopolu** — karta podaje tylko magazyn Tarnobrzeg; skąd fizycznie wyjeżdża towar?
