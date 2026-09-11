# agria.pl — co osiągnęliśmy i ścieżka SEO + sprzedaży

> **Data:** 2026-09-10 · **Status:** PROPOZYCJA do akceptu Janka — nic z sekcji 3–4 nie wchodzi na produkcję ani do rejestru bez zapisanego `[J]`.
> **Podstawa:** rekonstrukcja `docs/audits/2026-09-10-REKONSTRUKCJA-ARCHITEKTURY.md`, archiwum decyzji XII 2025 – V 2026
> `docs/archiwum/2025-12_2026-05-HISTORIA_DECYZJI_claude-ai.md`, pomiary z 10.09 (GSC miesiąc po miesiącu, CPT `agria_inquiry`,
> `e_submissions`), pomiar SERP i indeksu z 09.09.
> **Zasady nadrzędne (polecenie Janka 10.09):** (1) źródło prawdy o produktach = karty AGRII na `/do-pobrania/`, zrobione z papierowego
> katalogu; (2) produktów nie ruszamy — zestaw, nazwy, kategorie zostają; (3) parametrów nie zmieniamy; (4) wszystko obraca się wokół
> listingów produktów i kart produktów.

---

## 1. Co osiągnęliśmy przez pół roku — w liczbach

### 1.1 Ruch z Google (GSC, cały serwis, miesiące kalendarzowe)

| | V | VI | VII | VIII | IX (1–6) |
|---|---|---|---|---|---|
| **kliknięcia razem** | 48 | 63 | 221 | **361** | 82 |
| wyświetlenia razem | 1 212 | 2 821 | 10 220 | **28 804** | 5 904 |
| średnia pozycja | 15,6 | 13,9 | 8,8 | **7,1** | 6,5 |
| kliknięcia — **karty produktów** | 1 | 3 | 58 | **77** | 24 |
| kliknięcia — **kategorie** | 0 | 7 | 37 | 28 | 6 |
| kliknięcia — strona główna | 32 | 33 | 51 | 77 | 14 |
| kliknięcia — poradniki, hub, kalkulator | 0 | 4 | 52 | 159 | 36 |
| kliknięcia — landingi | 0 | 0 | 0 | **0** | 0 |
| kliknięcia bez marki (zapytania nad progiem GSC) | 0 | 1 | 11 | 41 | 8 |

Kliknięcia z Google wzrosły z 48 do 361 miesięcznie, karty produktów z 1 do 77. **Ale połowa wzrostu kliknięć (159 z 313) i trzy czwarte wyświetleń
to poradniki, hub i kalkulator** — ruch informacyjny, który dziś nie prowadzi do produktów (hub nie ma listingu).

### 1.2 Zapytania ofertowe — to jest miara sprzedaży strony

Formularz na kartach i na `/zamowienia/` (CPT `agria_inquiry`, pole `_source_url`) + formularz Elementora na `/kontakt/`:

| miesiąc | zapytania | skąd przyszły |
|---|---|---|
| III | 1 | `/zamowienia/` — 20.03, dzień uruchomienia formularza, najpewniej test |
| IV | 1 | karta wapna palonego mielonego |
| V–VI | 0 | — |
| VII | 4 | 2 × karta (Oxyfertil 90, Bielik), 2 × `/zamowienia/` (wapno palone, Agrobielik 90) |
| VIII | 5 + 1 kontakt | 2 × karta (Oxyfertil 90, kreda granulowana), 2 × `/zamowienia/` (Bielik, węglanowe z Mg odm. 05), **1 × landing `/wapno-granulowane/` — o kredę czarną, której landing nie opisuje** |
| IX (do 10.09) | 1 | karta węglanowe odm. 04 |

**Wniosek, który rozstrzyga architekturę:** 11 z 11 prawdziwych zapytań dotyczy **konkretnego produktu**. 6 przyszło z karty produktu,
4 ze strony zamówień, 1 z landingu. **Z kategorii, huba i poradników — zero bezpośrednio.** Sprzedaż tej strony to: karta produktu → formularz.

### 1.3 Zrobione i działające

| co | dowód |
|---|---|
| Karty produktów w indeksie Google: 13/38 adresów (15.06) → **19 z 19 kart** (URL Inspection 10.09) | ostatnie dwie weszły po ręcznym zgłoszeniu 09.09; ręczne zgłoszenie w panelu GSC działa w minuty — Indexing API i linkowanie nie działały |
| Parametry 19 kart zgodne z kartami producentów i atestami (bug importu naprawiony w 4 warstwach) | 15.07, commit `6a70484` |
| Ceny w treści 16 z 19 kart + `offers` w danych strukturalnych | 19.08 i 07.09 |
| Opisy kategorii: `/wapno-nawozowe-rolnictwo/` 958 → ~5 700 znaków, `/paszarstwo/` 465 B → 5 938 B | 04.09 i 08.09 |
| Szybkość strony głównej na telefonie: LCP 7,4 → 3,7 s | 07.09 |
| Kalkulator wapnowania z modułem magnezowym | 04.09 |
| Wizytówka Google Tarnów: **31 kliknięć „zadzwoń" za 0 zł** (06–09) | GBP Performance |
| OLX: 200 ogłoszeń, koszt kontaktu 12–15 zł netto; OLX stoi na 1–2 miejscu w Google na „wapno węglanowe", „magnezowe", „granulowane" | pomiar 28.08 i SERP 09.09 |
| Analityka GA4/GTM/GSC, schemat firmy, porządek adresów (19×301), nagłówki bezpieczeństwa | M1–M2 |

### 1.4 Zrobione i nie działające

| co | wynik |
|---|---|
| 4 landingi (`/wapno-nawozowe/`, `/wapno-granulowane/`, `/wapno-do-stawu/`, `/wapno-do-stabilizacji-gruntow/`) | **0 wyświetleń** w Google; w Ads 3 zdarzenia kontaktowe za 809 zł w sierpniu, 0 na 237 kliknięć po 30.08 |
| 7 nowych adresów po 09.07 (4 poradniki, terminarz, stabilizacja, staw) | 0 wyświetleń do 09.09 — Google ich nie pobrał |
| Przepisanie tytułów klastra dawkowego (T-053), nazwy kategorii | bez efektu w kontrolach 14-dniowych |
| Frazy ogólne (`wapno węglanowe`, `granulowane`, `magnezowe`, `hydratyzowane`) | poza TOP20 — SERP-y zajęte przez OLX, Allegro, sklepy i odpowiedź AI Google |

---

## 2. Dlaczego rankujemy słabo — pięć przyczyn

1. **Na frazy ogólne nasze karty nie wchodzą.** Nad nami stoją OLX, Allegro, sklepy i AI Overview. Wchodzimy tylko na nazwy własne:
   Oxyfertil 90 stoi na 7. miejscu i ma CTR 5%, Agrobielik 70 — 5%.
2. **Połowa kart przez część sezonu była poza indeksem** (8 z 19 do 24.08). Skoro sprzedaż idzie przez karty, to strata bezpośrednia.
   Działający mechanizm (ręczne zgłoszenie w panelu GSC) znaleźliśmy dopiero 09.09.
3. **Praca szła w nowe adresy i landingi, a nie w karty.** 7 nowych adresów i 4 landingi dały zero ruchu organicznego.
   W tym czasie karty z największą liczbą wyświetleń i zerem kliknięć (`weglanowe-granulowane`, `weglanowe-magnez-granulowane`) czekały.
4. **Ruch, który zbudowaliśmy, nie prowadzi do produktów.** Hub ma 19 572 wyświetleń w 28 dni, ale ani hub, ani terminarz nie mają
   listingu produktów — czytelnik nie ma jak dojść do karty.
5. **Kierunek zmieniał się co 2–3 tygodnie bez zapisanej decyzji.** 14.07 landingi, 11.08 landingi tylko pod reklamy, 21.08 hub i spoke
   oraz „kategorie poza adresem", 24.08 cofnięcie połowy. Cztery pytania o architekturę zadałem i nie zapisałem odpowiedzi
   (rekonstrukcja §8). Stąd poczucie powrotów do punktu wyjścia — ono jest uzasadnione.

---

## 3. Architektura — stała do 31.03.2027

| poziom | co | rola | co wolno zmieniać |
|---|---|---|---|
| **1. Karty produktów (19)** | zestaw i nazwy z katalogu | **strona sprzedażowa** — tu przychodzą zapytania; frazy produktowe, formowe i cenowe | opis, H2, FAQ, tytuł SEO, cena w treści, linki. **Tabeli parametrów nie** |
| **2. Kategorie (5 z produktami)** | listing + filtry + opis nad i pod | frazy ogólne (`wapno nawozowe`, `wapno do oczyszczalni`, `kreda pastewna`, `wapno hydratyzowane`, `kreda malarska`) | opis kategorii |
| **3. Poradniki: hub, kalkulator, terminarz** | treść o glebie i dawce | zbierają ruch informacyjny i **przekazują go na karty** — każdy dostaje listing produktów | treść + listing produktów |
| 4. Wizytówka, OLX, Ads | kanały zewnętrzne | kierują na karty produktów | — |

**Nie budujemy:** nowych landingów, nowych kategorii, nowych adresów bez zapisanego `[J]`.

### Cztery decyzje do Ciebie

| # | decyzja | moja rekomendacja | uzasadnienie |
|---|---|---|---|
| **D1** | Unieważnić T-068 („kategorie poza adresem produktu", okno zimowe) | **tak** — kategorie zostają | chciałeś produktów w dobrze nazwanych kategoriach; przebudowa adresów = kilka tygodni drgających pozycji bez dowodu zysku. ADR z 21.08 zapisuje ten kierunek jako Twoją propozycję, ale ADR pisałem ja — nie traktuję tego zapisu jako rozstrzygającego |
| **D2** | Reklamy po wznowieniu 14.09 kierować na **karty** (frazy produktowe i cenowe) i na **kategorię 764** (frazy ogólne); `/wapno-nawozowe/` i `/wapno-granulowane/` → 301 na kategorię | **tak** | zapytania przychodzą z kart (6 z 11); karty mają cenę (16 z 19), formularz i pasek telefonu; formularz na landingach dał 1 zapytanie, i to o produkt, którego landing nie opisuje; hipoteza „landing konwertuje lepiej niż kategoria" nigdy nie była zmierzona |
| **D3** | `/wapno-do-stabilizacji-gruntow/` — treść do karty #320, 301 na kartę | **tak** | 0 wyświetleń na „stabiliz" przez 90 dni, fraza bez popytu w planerze, jeden produkt |
| **D4** | `/wapno-do-stawu/` — zostaje | **zostaje** | ma listing 6 produktów, jest w menu, jedyny adres segmentu rybackiego (klaster 4 100 wyszukań/mies., zero pokrycia) — sam uznałeś, że to realna intencja |

Terminarz `/jak-stosowac-wapno-nawozowe/` (strona z tabelami terminów, bez produktów — zakładam, że o nią chodziło
w „oknie dostawy") **zostaje pod swoim adresem i dostaje listing produktów**, jak hub.

Puste kategorie Sadownictwo i Hurtownie zostają bez zmian (301 na `/oferta/`). Wypełnienie ich oznaczałoby przypisanie produktów
do drugiej kategorii, a to zmienia adresy produktów (Premmerce) — czyli ruszanie produktów, czego nie robimy.

---

## 4. Plan prac — kolejność

### Wrzesień (10–30.09) — karty i listingi

| # | zadanie | termin | miara |
|---|---|---|---|
| 1 | Ręczne zgłoszenie w GSC: `/kreda-malarska/` (jedyny adres z listy nadal nieznany Google; karty 19/19 w indeksie od 09.09) | 11.09 | URL Inspection |
| 2 | **Dwie karty granulowane** (#314, #317) + duplikat tytułu #317/#318 + ucięty tytuł #319 (T-117, T-116). Treść pod realne zapytania z GSC, parametry z karty z `/do-pobrania/` bez zmian | 20.09 | kliknięcia i pozycja kart po 14 dniach |
| 3 | **Kolejne karty** w kolejności „dużo wyświetleń, mało kliknięć": #315 odm. 04 (1 105 wyśw. / 10 klik.), #313 tlenkowe z Mg (372 / 2), #305 kreda granulowana (352 / 4), #307 kreda pastewna (203 / 1) | 30.09 | jw., para karta przerobiona / nieprzerobiona w tym samym oknie |
| 4 | **Listing produktów w hubie `/wapnowanie-gleby/` i w terminarzu** — ten sam widget co na landingach (T-064), produkty, które treść już wymienia | 20.09 | wejścia na karty z huba (GA4, z zastrzeżeniem zgód) |
| 5 | Opisy kategorii `/wapno-do-oczyszczalni/` (T-093) i `/wapno-hydratyzowane/` (T-085) | 20.09 | kontrola 14-dniowa |
| 6 | Tytuł strony głównej bez „wapno nawozowe" na pierwszym miejscu — dziś konkuruje z kategorią 764 o tę samą frazę | 20.09 | pozycja kategorii na `wapno nawozowe` |

### Październik — sprzedaż

| # | zadanie | miara |
|---|---|---|
| 7 | Reklamy według D2, konwersja główna = formularz + telefon | koszt zapytania, porównanie z sierpniem |
| 8 | Wizytówka Google: wtorkowe publikacje (działa od 08.09) + prośby o opinie | kliknięcia „zadzwoń" |
| 9 | OLX: odnowienie pakietu to decyzja AGRII (T-105). Każde ogłoszenie linkuje do karty produktu | kontakty z OLX, wejścia z OLX na karty |
| 10 | Kontrole 14-dniowe kart przerobionych we wrześniu | tabela w `data/kontrole/` |

### Listopad – luty — treść z popytem, tylko wokół produktów

| # | zadanie | warunek |
|---|---|---|
| 11 | Tematy z popytem i zerowym pokryciem: kreda pastewna dla kur (1 600/mies.), kreda do stawu (1 300), pH gleby (1 000), badanie gleby (1 000) | **najpierw sprawdzam, czy temat mieści się w istniejącej karcie lub kategorii**; nowy adres tylko z `[J]` i zawsze z listingiem produktów |
| 12 | Przegląd całości po sezonie | 31.01 |

---

## 5. Miary — trzy liczby w każdym raporcie

| miara | punkt odniesienia (VIII 2026) |
|---|---|
| kliknięcia z Google na **karty + kategorie** | **105** (77 + 28) |
| **zapytania** z formularzy (karty, `/zamowienia/`, kontakt) | **6** |
| pozycja kart na frazy formowe (GSC) | `wapno węglanowe` → odm. 04: **7,7** · `wapno granulowane` → #314: **18,9** · `wapno magnezowe granulowane` → #317: **25,5** |

Celu liczbowego nie wyznaczam na oko. Pierwszą ocenę robię 01.10 na parach kart: przerobiona wobec nieprzerobionej w tym samym oknie.
Dopiero to pokaże, ile daje praca na karcie, i z tego wyliczę cel na listopad.

---

## 6. Zasady pracy — żeby nie wracać do punktu wyjścia

1. **Ta tabela architektury (§3) obowiązuje do 31.03.2027.** Zmiana tylko z Twoim zapisanym „tak", wpisanym jako `[J]` z datą.
2. **Zero nowych adresów, landingów i kategorii bez `[J]`.** Propozycję zgłaszam, nie buduję.
3. **Produkty i parametry z kart na `/do-pobrania/`**, nigdy z rozumowania. Tabel parametrów nie ruszam.
4. **Pomiar przed budową, nie po.** Każde zadanie ma przed startem: jedno zdanie hipotezy, miarę i datę kontroli.
5. **Każda strona prowadzi do karty produktu.** Strona bez listingu produktów albo bez linku do karty jest niedokończona.
6. **Liczby tylko z pomiaru z datą.** Korekta własnej liczby to jawny wpis w rejestrze, nie cicha podmiana.
7. **Pytanie o decyzję czeka na odpowiedź.** Nie wykonuję własnego wariantu, gdy pytanie wisi.

Po Twoim akcepcie D1–D4 aktualizuję rejestr: T-068 do „Unieważnione", D2/D3 jako nowe pozycje, reszta wg §4.
