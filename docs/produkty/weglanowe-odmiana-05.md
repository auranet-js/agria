# Wapno nawozowe węglanowe bez magnezu — Odmiana 05 (WC #316)

> Karta AGRII: **BRAK** (nie ma jej na `/do-pobrania/` ani w katalogu drukowanym `Agria-katalog-2026-05-04-web.pdf`) ·
> karta na stronie: `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` · kategoria dziś: Wapno nawozowe (`/wapno-nawozowe-rolnictwo/`, term 764) ·
> SKU AGR-007 · **stan na 10.09.2026**
>
> ⚠️ **Nie mylić z #319** „Wapno nawozowe węglanowe **zawierające magnez** — Odmiana 05" (Laskowa + Winna, 36 zł/t). To dwa różne produkty.
>
> **Źródła (skróty używane niżej):**
> **[R]** render karty 10.09, `data/produkty/render/weglanowe-odmiana-05.{html,json}` — **stan strony, nie źródło prawdy** ·
> **[F]** `docs/FAKTY_KLIENTA.md` §3 · **[C]** `docs/operations/CENNIK_PAWEL_2026-08-07.md` ·
> **[H]** `docs/archiwum/2025-12_2026-05-HISTORIA_DECYZJI_claude-ai.md` §9 · **[OLX]** `data/olx/market/2026-08-28.json` ·
> **[S]** SERP mobile 10.09 `data/produkty/dfs/serp-weglanowe-bez-mg-2026-09-10.json`
>
> Zasada (`feedback_agria_params_from_datasheets`): **bez karty AGRII parametrów nie uzupełniamy — ani z rozumowania, ani z kart producentów.**
> Wszystko w §1–§3 poniżej, co nie jest „brak", to **stan strony** i jako taki jest opisane.

---

## 1. Tożsamość

**Karta PDF AGRII: brak.** Nie ma cytatów z karty.

| cecha | karta AGRII | co mówi strona / baza (stan, nie źródło) | źródło |
|---|---|---|---|
| nazwa | brak | H1 „Wapno nawozowe węglanowe bez magnezu — Odmiana 05" (= nazwa WC) | [R] |
| odmiana | brak | „Odmiana 05" w nazwie; atrybut `pa_agria-norma` = „Odmiana 05" | [R] |
| marka | brak | atrybut `pa_agria-marka` — **brak** | [R] |
| producent | brak | **widoczna tabela: „Lhoist"** · **atrybut `pa_agria-producent`: „Kopalnia Celiny"** · **[F] §3: „Kopalnia Celiny"** — trzy miejsca, dwie różne odpowiedzi | [R], [F] |
| magazyn | brak | „Bukowa (29-105)" (tabela i atrybut) | [R] |
| rodzaj | brak | węglanowe, bez magnezu (nazwa WC) | [R] |
| forma / frakcja | brak | „Sypkie", „0–2 mm" | [R] |
| formy dostawy | brak | atrybut `pa_agria-forma-dostawy` = „Luz"; tabela — brak wiersza; formularz — tylko „Luz" | [R] |
| w katalogu drukowanym | — | był w wersji 15.04 (lista kart [H] §9.2, str. 4–21), **nie ma go w wersji 04.05** (tekst katalogu 04.05 nie zawiera strony węglanowego bez Mg odm. 05) | [H], katalog |

**Rozbieżność producenta — zapisana, nierozstrzygnięta:** widoczna tabela mówi Lhoist, atrybut i `FAKTY_KLIENTA` — Kopalnia Celiny.
Magazyn Bukowa pojawia się też na karcie #315 (tam jako jeden z czterech magazynów przy producentach Lhoist i Celiny).
`FAKTY_KLIENTA` §4 odnotowuje duplikat termu „Kopalnia Celiny" vs „Celiny (Hochel Group)" jako dług danych.

## 2. Parametry

**Karta PDF AGRII: brak — tabeli parametrów nie ma.** Atestu, karty producenta i karty charakterystyki na `/do-pobrania/` też nie ma.

Dla porządku — tabela widoczna dziś na stronie [R] (**stan strony, niepotwierdzony kartą; nie przepisywać do żadnego źródła**):

| parametr (strona) | wartość (strona) |
|---|---|
| Zawartość CaO | min. 40% CaO |
| Reaktywność | ~70-90% |
| Typ reakcji | Długodziałająca(bezpieczna) |
| Forma fizyczna | Sypkie |
| Frakcja | 0–2 mm |
| Zastosowanie funkcjonalne | działanie długoterminowe, Odkwaszanie gleb lekkich i piaszczystych, poprawa struktury |
| Efekt zastosowania | Wzrost pH |
| Dawkowanie | 1,5–6 t/ha |
| Szybkość działania | Długotrwałe (3-6 miesięcy) |
| Dodatkowe zastosowanie | Gospodarstwa ekologiczne, sadownictwo, uprawy wieloletnie |
| Segment | Rolnictwo, Sadownictwo |
| Magazyn | Bukowa (29-105) |
| Producent | Lhoist |
| Dostępność | Cały rok |

Atrybuty `pa_*` w schemacie pokrywają się z tą tabelą **poza producentem** (atrybut: Kopalnia Celiny) i dodają formę dostawy „Luz".

## 3. Zastosowania

**Karta PDF AGRII: brak.** Zastosowań, gleb, terminu i dawki nie ustalamy.

Strona [R] podaje: „Odkwaszanie gleb lekkich i piaszczystych", „Gospodarstwa ekologiczne, sadownictwo, uprawy wieloletnie", dawka 1,5–6 t/ha —
**stan strony, niepotwierdzony kartą.**

## 4. Z czym go porównać

### 4.1 Produkty AGRII tego samego rodzaju

Porównanie parametrów **niemożliwe bez karty**. Fakty, które da się zestawić bez karty:

| | karta AGRII | cena [C] | producent (wg karty lub, dla #316, wg strony / atrybutu) | magazyn | forma dostawy |
|---|---|---|---|---|---|
| **#316 Węglanowe bez Mg — Odm. 05** | **brak** | **brak** („pominięte; odm. 04 wyceniona") | Lhoist (tabela) / Kopalnia Celiny (atrybut, [F]) | Bukowa (strona) | luz (atrybut) |
| #315 Węglanowe bez Mg — Odm. 04 | jest | 57 zł/t luz | Lhoist, Celiny (Hochel Group) | Bukowa, Celiny, Górażdże, Tarnów Opolski | BB 1000 kg, worek 25 kg, luz 25–27 t |
| #319 Węglanowe **z Mg** — Odm. 05 | jest | 36 zł/t luz | Kopalnia Laskowa, Kopalnia Winna (Industria) | Łagów, Kostomłoty Drugie | luz |
| #314 Węglanowe bez Mg granulowane | jest | 350 BB · 380 worek | Grankal, Lhoist, Celiny | Niedomice, Draby, Tarnów Opolski, Celiny | BB 500/600 kg, worek 25 kg |

Fakty bez wniosków: #316 i #315 dzielą **nazwę rodzaju, magazyn Bukowa i jednego z producentów** (Lhoist albo Celiny — zależnie od źródła).
Z tych dwóch tylko #315 ma kartę, cenę i zapytanie ofertowe.

### 4.2 Konkurencja — co w wynikach nosi nazwę „odmiana 05"

| sprzedawca | co | cena | gdzie widoczny | źródło |
|---|---|---|---|---|
| chemiagro.pl | „Wapno kujawskie Kujawit odmiana 05" | niezmierzone | abs 2 na `wapno odmiana 05` (pod AI Overview) | [S] |
| agrolok.pl | „Wapno węglanowe Kujawit" | niezmierzone | abs 10 | [S] |
| wapno-kruszywo.pl | „Nawóz wapniowy – RODAM & INOWAP" | niezmierzone | abs 7 | [S] |
| CARLOS — Karol Nawrocki (45202079) | „Wapno nawozowe węglanowe KUJAWIT, Faktura VAT" — **jedyne na OLX ogłoszenie z „odm. 05" bez magnezu w tytule** | 71 (pole `price`, jednostka niepodana) | OLX, zrzut 28.08 | [OLX] |

**OLX, zrzut 28.08** [OLX]: „odm. 05" bez „magnez" w tytule — **1 ogłoszenie, 1 sprzedawca, AGRIA 0**. W wynikach wyszukiwania nazwa
„odmiana 05" łączy się z marką Kujawit, nie z Lhoist ani z Celinami.

## 5. Frazy — popyt

Wolumen i CPC: **planer Google Ads API** (konto AGRII, PL/polski, średnia 12 mies. 2025-08 … 2026-07), pobrane 10.09 →
`data/produkty/ads/weglanowe-odmiana-05-planer.json`. „<10" = poniżej progu (**nie zero**). GSC: cały serwis, 2026-06-09 … 2026-09-06
(`data/produkty/gsc/weglanowe-bez-mg-frazy*.json`). Frazy rodzaju ogólnego (`wapno węglanowe` itd.) opisane szczegółowo w `weglanowe-odmiana-04.md` §5.

| fraza | typ | wyszukań/mies. | CPC śr. zł | szczyt (rok-mies.) | nasz serwis w GSC 90 dni |
|---|---|---|---|---|---|
| wapno odmiana 05 | nazwa | 20 | — | 2025-08: 50 | 60 wyśw.: **#319 (z Mg) 51 poz. 2,9**; stary adres z Mg 9 poz. 2,6 · **#316 brak** · SERP 10.09: #319 abs 9, **#316 abs 22** |
| wapno węglanowe odmiana 05 | nazwa | 10 | — | 2025-08: 10 | 0 wierszy |
| wapno węglanowe bez magnezu | nazwa | 10 | 0,55 | 2025-08: 10 | 0 wierszy |
| wapno nawozowe odmiana 05 · wapno węglanowe 40 | nazwa | <10 | — | — | 0 wierszy |
| kopalnia celiny | kopalnia (atrybut, [F]) | 320 | — | 2025-08: 480 | 0 wierszy · DFS Labs: „kopalnia wapienia celiny k/chmielnika" 390 |
| wapno celiny | kopalnia | 10 | — | 2025-08: 50 | 0 wierszy |
| lhoist bukowa | producent + magazyn (strona) | 390 | 2,37 | 2025-08: 480 | 0 wierszy |
| wapno bukowa | magazyn | 50 | 1,40 | 2025-08: 110 | 0 wierszy · SERP 10.09: AGRIA poza top 20 |
| ile wapna węglanowego na hektar | dawka | 40 | 3,76 | 2025-08: 110 | 134 wyśw., hub poz. 8,1 |
| wapno węglanowe cena | cena | 70 | 0,91 | 2025-08: 140 | 1 wyśw., hub |
| wapno węglanowe luzem | cena / forma | <10 | — | — | 0 wierszy |
| wapno węglanowe | rodzaj ogólny | 1 000 | 0,80 | 2025-08: 2 400 | 988 wyśw.; #315 765 poz. 9,9 · #316 brak |
| wapno nawozowe węglanowe | rodzaj ogólny | 40 | 0,01 | 2026-03: 110 | 187 wyśw. · #316 brak |
| wapno węglanowe sypkie | rodzaj + forma | 20 | 1,32 | 2026-03: 40 | 6 wyśw. (#319, #314) · #316 brak |
| wapno węglanowe czy tlenkowe | porównanie | 10 | — | 2025-08: 30 | 0 wierszy |
| wapno odmiana 04 czy 05 | porównanie | <10 | — | — | 0 wierszy |

Na własną nazwę (`wapno odmiana 05`, 20/mies.) Google pokazuje **inny produkt AGRII — #319 z magnezem** (GSC poz. 2,9, SERP abs 9);
#316 jest na tej frazie na abs 22. Na żadną frazę karta nie zebrała wyświetleń w 90 dniach.

**Google Ads 13.08–09.09:** z „odmiana" — 0 wyszukiwań; żadna reklama nie kierowała na #316.

## 6. Stan dziś na stronie (render 10.09, nie baza)

| element | stan | źródło |
|---|---|---|
| title | „Wapno węglanowe bez magnezu Odmiana 05 \| AGRIA" | [R] |
| meta description | „Wapno węglanowe bez magnezu: długotrwałe odkwaszanie gleb lekkich. Min. 40% CaO, reaktywność 70-90%. Rolnictwo ekologiczne i sadownictwo. Zapytaj o ofertę!" | [R] |
| H1 | „Wapno nawozowe węglanowe bez magnezu — Odmiana 05" (= nazwa WC) | [R] |
| H2 | „Wapno węglanowe bez magnezu Odmiana 05: Długotrwałe odkwaszanie gleb" · „Trwałe odkwaszanie gleb — wyższe plony" · „Specyfikacja techniczna" · „Najczęściej zadawane pytania" · „Zapytaj o ofertę, zamów próbkę" — **bez sekcji ceny** | [R] |
| treść | **5 501 znaków** od H1 do formularza | [R] |
| FAQ | 7 pytań (dawkowanie, gleby, czas działania, eko i sady, parametry, forma i ilość, zamówienie); **brak `FAQPage` w schemacie** | [R] |
| cena w treści | **brak** — zgodnie z [C] (brak ceny) | [R], [C] |
| schema `Product` | **bez `offers`** (świadomy wyjątek T-097); `name` = title strony; `additionalProperty` = `pa_*` z producentem „Kopalnia Celiny" | [R] |
| zdjęcie | `2026/02/Wapno-nawozowe-weglanowe-bez-magnezu-Odmiana-05.webp` | [R] |
| PDF | brak linku do karty PDF (karty nie ma) — tylko ogólnie `/do-pobrania/` | [R] |
| listingi z linkiem do #316 | `/oferta/`, `/wapno-nawozowe-rolnictwo/`, `/wapno-nawozowe/` (noindex), strona główna · **bez linku:** hub, `/wapno-granulowane/`, `/wapno-do-stawu/`, `/kalkulator-wapnowania/`, `/zamowienia/` | curl 10.09 |
| indeks | PASS, „Strona przesłana i zindeksowana", ostatni crawl **2026-09-09**, canonical własny | URL Inspection 10.09 |

**GSC karty, 2026-06-09 … 2026-09-06** (`data/produkty/gsc/weglanowe-odmiana-05.json`): **0 kliknięć, 0 wyświetleń** na poziomie strony
(to liczba ze strony, nie z sumy zapytań — próg prywatności tu nie gra roli). SERP 10.09: abs 22 na `wapno odmiana 05`.

**Zapytania ofertowe** (CPT `agria_inquiry`, MCP 10.09): **0 z 11**. (Zapytanie 2800 z 28.08 dotyczy „…zawierające magnez — Odmiana 05", czyli #319.)

### Rozbieżności

Karty PDF nie ma, więc **nie ma rozbieżności karta ↔ strona** do wypisania. Rozbieżności wewnątrz danych strony i repo:

| co | miejsce A | miejsce B |
|---|---|---|
| producent | widoczna tabela: „Lhoist" | atrybut `pa_agria-producent` i `FAKTY_KLIENTA` §3: „Kopalnia Celiny" |
| forma dostawy | atrybut: „Luz" | tabela: brak wiersza |
| doświadczenie firmy | FAQ: „z ponad 35-letnim doświadczeniem" | sekcja formularza: „37 lat doświadczenia" |

**Twierdzenia w treści, których nie potwierdza żadna karta** (tekst n8n DescWriter, `[J 10.09]`): cała tabela parametrów i opis — w tym
„min. 40% CaO", „reaktywność ~70–90%", „dawka 1,5–6 t/ha", „wolnemu uwalnianiu składników", „idealny dla rolnictwa ekologicznego".

## 7. Konkurencja w wynikach (SERP mobile PL)

| fraza | top wyniki (abs) | AGRIA |
|---|---|---|
| `wapno odmiana 05` (10.09) | 1 AI Overview · 2 chemiagro (Kujawit odm. 05) · 4 tech-mot · 6 nawozy.eu · 7 wapno-kruszywo (RODAM & INOWAP) · **9 agria.pl #319** · 10 agrolok (Kujawit) · 11 agro-max (Lafarge) · 12 wkg.pl · 14 metal-trans · 16 ifarmer | #319 abs 9, **#316 abs 22** |
| `wapno bukowa` (10.09) | 4 OLX · 5 AI Overview · 7 lhoist.com · 9 allegro („Bukowa Super Białe") · 11 barbud · 12 kim24 · 13 chemiaibiznes · 15 ankom-phu („Wapno nawozowe niezawierające magnezu «Bukowa»") | poza top 20 |

## 8. Luki — czego brakuje (fakty, bez propozycji struktury)

1. **Brak karty AGRII** — produkt nie ma źródła prawdy: ani parametrów, ani zastosowań, ani producenta. Wypadł z katalogu między 15.04 a 04.05.
2. **Brak ceny** w cenniku („pominięte") i na stronie; schemat bez `offers`.
3. **Producent sprzeczny** w dwóch miejscach strony/bazy (Lhoist vs Kopalnia Celiny).
4. **Zero wyświetleń w 90 dniach** przy zaindeksowanej karcie (crawl 09.09) — na własną nazwę Google pokazuje #319.
5. **Zero zapytań ofertowych i zero ogłoszeń OLX AGRII** dla tego produktu (w zrzucie 28.08 AGRIA ma 0 ogłoszeń „odm. 05" bez magnezu).
6. Na rynku „odmiana 05" bez magnezu to w wynikach **Kujawit** (chemiagro, agrolok, CARLOS na OLX) — nazwa, której nie ma w żadnym dokumencie AGRII.

## 9. Pytania do Janka / klienta (tylko to, czego karty nie rozstrzygają — tu: wszystko)

1. **Czy AGRIA nadal sprzedaje ten produkt?** Nie ma karty AGRII, nie ma ceny, zniknął z katalogu 04.05.
2. Jeśli tak — **kto jest producentem: Lhoist czy Kopalnia Celiny** — i skąd towar wyjeżdża (Bukowa?)?
3. Jeśli tak — **czy klient ma kartę lub atest** z parametrami (zawartość CaO, frakcja, dawka)? Bez nich parametrów na stronie nie potwierdzamy.
4. Cena luzu (Paweł pominął ją w mailu 07.08).
