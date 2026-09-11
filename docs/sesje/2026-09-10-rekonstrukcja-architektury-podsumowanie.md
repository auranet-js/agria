# Sesja 09–10.09.2026 — rekonstrukcja architektury: co ustaliliśmy, co zostało otwarte

> Wątek zaczął się od prompta `docs/prompty/wdrozenie/2026-09-09-REKONSTRUKCJA-architektura-tresci.md`
> (Janek: „przestałem rozumieć, dlaczego strona wygląda tak, jak wygląda"). Skończył się poleceniem zbudowania
> bazy wiedzy o produktach — prompt: `docs/prompty/2026-09-10-PROMPT_BAZA_WIEDZY_PRODUKTOWEJ.md`.
> Produkcja nietknięta przez cały wątek (odczyt: MCP `query_db`, `curl`, GSC API, git).

---

## 1. Pliki, które powstały

| plik | co to jest |
|---|---|
| `docs/audits/2026-09-10-REKONSTRUKCJA-ARCHITEKTURY.md` | rekonstrukcja wersja 2: chronologia XII 2025 – IX 2026, mapa warstw, osie klasteryzacji / treści / audytów, decyzje moje bez akceptu, GSC per warstwa, raporty do klienta vs stan strony |
| `docs/strategy/2026-09-10-SCIEZKA-SEO-I-SPRZEDAZY.md` | podsumowanie osiągnięć + propozycja ścieżki; **status: propozycja, decyzje D1–D4 NIEPODJĘTE** (quiz zatrzymany przez Janka) |
| `docs/archiwum/2025-12_2026-05-HISTORIA_DECYZJI_claude-ai.md` | kopia `AGRIA/Archiwum/AGRIA_HISTORIA_DECYZJI.md` z Google Drive — zestawienie 28 wątków Claude.ai z budowy strony (źródło wtórne) |
| ten plik | podsumowanie wątku |
| `docs/prompty/2026-09-10-PROMPT_BAZA_WIEDZY_PRODUKTOWEJ.md` | prompt do następnego wątku |

---

## 2. Ustalenia — fakty z dowodem

### 2.1 Zasady ustalone przez Janka w tym wątku (obowiązują)

1. **Źródło prawdy o produktach = karty AGRII na `/do-pobrania/`**, zrobione z papierowego katalogu (najdłużej weryfikowany
   materiał). Nazwy, zastosowania, parametry — stamtąd.
2. **Produktów nie ruszamy.** Zestaw 19 produktów i nazwy zostają. **Parametrów nie zmieniam w ogóle.** Treść opisową kart — wolno.
3. **Wszystko obraca się wokół listingów produktów i kart produktów.** Strona grupy produktów może zostać (także staw,
   także stabilizacja), **o ile jest zrobiona według szablonu i ma listing produktów**. Strona z tabelkami bez produktów = błąd.
4. Produkt **może** należeć do kilku kategorii — Janek dopuszcza to co do zasady; sposób nierozstrzygnięty.
5. **Słownik (ustalony 10.09):** kategoria = strona z listą produktów, filtrami i opisem (technicznie kategoria WooCommerce
   albo strona z listingiem — sprawa wykonawcza); karta = strona jednego produktu; poradnik = artykuł. Słów „landing"
   i „segment" nie używam. „Zastosowanie" = wyłącznie filtr na `/oferta/`.
6. **Decyzje zapadają w quizie** (AskUserQuestion), każda zapisana z datą.

### 2.2 Historia — czego wcześniej nie wiedziałem (archiwum z Drive)

- **20.02 decyzja Janka:** segment nie w adresie produktu; segment = strona docelowa z frazą intencyjną
  (`/wapno-nawozowe/`, `/wapno-do-stawow/`, `/wapno-do-oczyszczalni/`). Do 19.05 nic z tego nie powstało.
- **27.02:** WooCommerce w trybie katalogu, import PIM skryptem PHP; **7 kategorii = segmenty z PIM**, produkt w 1–4 naraz.
- **13.03:** treść 19 kart napisał **n8n DescWriter** (Gemini, workflow z LAGUZ), z PIM + danych WC; meta Rank Math też.
  W bazie 19/19 kart ma tag `content-done`. **Decyzja o podziale fraz:** karta → nazwa produktu, kategoria → fraza intencyjna.
- **Klastrów fraz przed majem nie opracowano w żadnym wątku.**
- Pierwotny rozjazd: decyzja z 20.02 trzymała segment poza adresem, a wtyczka Premmerce wstawia kategorię do adresu
  (wybiera tę o **najwyższym `term_id`**). ADR 08.07 utrwalił kategorię w adresie.

### 2.3 Kategorie — przed 08.07 i dziś (kopia `~/backups/agria/2026-07-08/pre-migration-state.json`, MCP 10.09)

| kategoria | term | adres dziś | produktów do 08.07 | dziś |
|---|---|---|---|---|
| Wapno nawozowe (dawniej Rolnictwo) | 764 | `/wapno-nawozowe-rolnictwo/` | 17 | 15 |
| Hurtownie | 769 | 301 → `/oferta/` | 13 | 0 |
| Sadownictwo | 765 | 301 → `/oferta/` | 9 | 0 |
| Rybactwo | 766 | usunięta 24.08 → strona `/wapno-do-stawu/` | 5 | — |
| Oczyszczalnie | 767 | `/wapno-do-oczyszczalni/` | 4 | 1 (#320) |
| Budownictwo | 768 | **`/wapno-hydratyzowane/`** (nazwa ≠ adres) | 1 | 1 (Bielik) |
| Paszarstwo | 770 | `/paszarstwo/` | 1 | 1 |
| Kreda malarska | 830 | `/kreda-malarska/` (produkt: `/kreda-malarska/kreda-malarska/`) | — | 1 |

- 08.07 zmieniło **przypisania i adresy produktów**, nie listę kategorii. „Jedna kategoria na produkt = pierwsza ikonka
  z katalogu" → 15 produktów ma Rolnictwo jako pierwszą ikonkę, stąd 15 w jednej kategorii i reszta po 1.
- Pełne przypisania przetrwały w atrybucie `pa_agria-segment` (filtr „Zastosowanie" na `/oferta/`).
- Kreda malarska jako osobna kategoria — **moja propozycja 08.07, kiepska**: 1 produkt, podwójny adres, kategoria nieznana Google.
- Mechanika adresów (z kodu Premmerce, niesprawdzone na żywo): produkt można dodać do kategorii o **niższym** numerze niż
  jego obecna bez zmiany adresu (np. Bielik 768 → do 764/765/767; kreda pastewna 770 → do dowolnej). Produktów z 764
  (najniższy numer) nie da się dodać nigdzie bez zmiany adresu.

### 2.4 Landingi (w nowym słowniku: strony z listingiem, do decyzji)

| adres | powstał | robots | listing | indeks | GSC 28 dni |
|---|---|---|---|---|---|
| `/wapno-nawozowe/` | 14.08 | `noindex` | 14 produktów | poza z decyzji | 0 |
| `/wapno-granulowane/` | 06.08, **pusty do 13.08** | `noindex` | 3 (#314, #317, #305 — wszystkie z kat. 764) | poza z decyzji | 0 |
| `/wapno-do-stawu/` | 21.08 | `index` | 6 | **zaindeksowana 09.09** (ręczne zgłoszenie) | 0 do 05.09 |
| `/wapno-do-stabilizacji-gruntow/` | 14.07 (brief 15.06) | `index` | 1 (#320) | **zaindeksowana 09.09** | 0 do 05.09 |

- Stabilizacja: pomysł mój (KR 19.05: 720/mies., audyt treści 15.06); trafiła do strategii dla klienta i maila czerwcowego
  („październik: nowa strona"); w briefie katalogu z lutego był produkt „Wapno palone drogownictwo", który wypadł 15.06.
  Janek 10.09: zaindeksowana → nie odpublikowujemy, „coś z nią zrobimy".
- Terminarz `/jak-stosowac-wapno-nawozowe/` (to prawdopodobnie „okno dostawy" z uwagi Janka) — tabele terminów,
  **zero produktów**; zaindeksowany 09.09.

### 2.5 Wyniki — liczby

**GSC, kliknięcia miesięcznie:** cały serwis V 48 · VI 63 · VII 221 · **VIII 361**; karty 1 · 3 · 58 · **77**;
kategorie 0 · 7 · 37 · 28; poradniki/hub/kalkulator 0 · 4 · 52 · **159**; landingi 0 we wszystkich miesiącach.
Wyświetlenia VIII 28 804, z czego ~75% poradniki (hub `/wapnowanie-gleby/` 19 572 w 28 dniach, CTR 0,6% — AI Overview).

**Zapytania ofertowe (CPT `agria_inquiry`, `_source_url`) — 11 prawdziwych IV–IX, wszystkie o konkretny produkt:**
6 z kart produktów · 4 z `/zamowienia/` · 1 z `/wapno-granulowane/` (o kredę czarną, której strona nie opisuje) ·
**0 z kategorii, huba, poradników**. 20.03 = test przy uruchomieniu formularza. Elementor `/kontakt/`: 1 w III, 1 w VIII.

**Indeks:** 19/19 kart zaindeksowane (URL Inspection 10.09). **Ręczne „Poproś o zindeksowanie" w panelu GSC działa
w minuty**; Indexing API (6 serii) i linkowanie wewnętrzne (16 dni) nie wprowadziły nowych adresów. `/kreda-malarska/`
(kategoria) nadal nieznana Google.

**Popyt vs pokrycie (wolumen z repo, GSC 90 dni):**

| fraza | wyszukań/mies. | ile naszych adresów ją dzieli | najlepiej stoi |
|---|---|---|---|
| wapno granulowane | 4 400–5 400 | 6 | hub 7,7 |
| wapno magnezowe | 2 400 | 4 | hub 8,2 |
| wapno hydratyzowane | 2 400 | 6 | karta Bielik 8,6 |
| wapno palone | 2 400 | 6 | brak |
| kreda pastewna | 2 400 | 4 | karta 15,4 |
| wapno nawozowe | 1 300 | 15 | kategoria 11,1 |
| wapno węglanowe | 1 000 | 6 | karta odm. 04 9,9 |
| kreda nawozowa | 1 000 | 5 | hub 5,7 |
| wapno tlenkowe | 720 | 7 | hub 6,5 |
| staw (kreda + wapno do stawu) | 1 690 | 2 | brak |
| wapno do sadu | 30 | 1 | — |

Wniosek z danych (nie decyzja): **popyt jest na rodzaj wapna i nazwy produktów, nie na zastosowania** (wyjątek: staw).
Pomiar 04.09: fraza z 1 naszym adresem → śr. poz. 10,1; 2 adresy → 17,6; 3+ → 22,5 (korelacja).

**Kanały:** wizytówka Tarnów 31 kliknięć „zadzwoń" za 0 zł (06–09); OLX koszt kontaktu 12–15 zł, OLX na 1–2 miejscu
w Google na frazach rodzajowych; Ads VIII: 3 zdarzenia kontaktowe za 809 zł, po 30.08 0 konwersji na 237 kliknięć
Rolnictwa; kampanie pauzowane do 14.09.

### 2.6 Co z moich wcześniejszych ustaleń upadło (skrót — pełna lista w rekonstrukcji §5 i §8.C)

Biovita jako wzorzec (14.07) · sześć landingów exact-match · Indexing API jako akcelerator · „8 z 19 kart poza indeksem"
(było 4, dziś 0) · znaki opisów kategorii zawyżone 4–7× (audyt 24.08) · „linkowanie wprowadzi do indeksu" (Faza 0) ·
T-069 CTR z sumy zapytań · sezon październikowy (szczyt = sierpień) · „krótszy tytuł = lepszy CTR" · T-053 i nazwy
kategorii bez efektu · „7 kategorii bez zapisu decyzji" i „kto pisał karty — brak zapisu" (rekonstrukcja v1).

### 2.7 Komunikacja z klientem

Klient ma na piśmie architekturę z czerwca (segmenty, indeksowalne strony produktowe, 4 artykuły/mies.). Nigdy nie dostał
informacji o: stronach Ads z `noindex`, hub i spoke, zmianie podziału fraz, 0/10 nowych adresów w indeksie.
Mail sierpniowy (`2026-08-mail.md`) — brak kopii „WYSŁANY" w repo.

---

## 3. Decyzje OTWARTE — quiz zatrzymany przez Janka 10.09 („stop")

| # | temat | stan |
|---|---|---|
| D1 | podział kategorii (rodzaj / zastosowanie / oba / bez zmian) + sposób na adresy produktów przy wielu kategoriach (kod w wtyczce / przenumerowanie / adres bez kategorii T-068) | **otwarte** — Janek: „najpierw ustalmy resztę"; najpierw baza wiedzy o produktach |
| D2 | cel reklam po 14.09 (karty / kalkulator / bez zmian) | otwarte; Janek: „mały budżet, równie dobrze kalkulator" |
| D3 | stabilizacja gruntów | zaindeksowana → **nie odpublikowujemy**; co dalej — otwarte |
| D4 | staw i „kreda do stawu" — czy wchłonięcie wzmacnia | otwarte; zasada: strona z listingiem może współistnieć |

**Kolejność wskazana przez Janka:** najpierw **baza wiedzy o każdym produkcie** (prompt nowego wątku), dopiero potem
architektura, kategorie i reklamy.

---

## 4. Błędy procesu po mojej stronie — żeby nie powtórzyć

1. Budowałem nowe adresy przed pomiarem, mierzyłem po fakcie (cofnięcia po 3–21 dniach).
2. Cztery pytania o architekturę zadałem i wykonałem własny wariant bez zapisanej odpowiedzi.
3. Nazwy robocze zmieniałem w trakcie („segment" → „kategoria" → „landing") — ustalony słownik w §2.1.
4. Liczby z audytów przepisywałem do rejestru bez weryfikacji (znaki kategorii, sezonowość, liczba kart poza indeksem).
5. Nie znałem historii z budowy strony (archiwum Drive) i opisałem ją jako „brak zapisu".
6. Nie zbudowałem nigdy wiedzy o produktach z kart PDF — pracowałem na frazach, nie na produktach.
