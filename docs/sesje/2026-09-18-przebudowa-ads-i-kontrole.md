# Sesja 2026-09-18 — kontrole wrześniowe, mapa konta Ads, przebudowa kampanii Marka

> **Commit:** `e1340b0` + ten plik · **Zakres:** R (kontrole, SEO) + P (Ads)
> **Stan konta na koniec sesji:** Rolnictwo 28 zł/dz, Paszarstwo 9, Marka 5 — siedem dni, Rolnictwo 8:00–16:00

---

## 1. Co zostało zrobione

### Kontrole (zaległe i terminowe)

**Indeksacja — 24 na 24 adresy `PASS`.** Ręczne zgłoszenie z 09.09 zadziałało i utrzymało się dziewięć dni.
**Faza 2 jest otwarta.** Przy okazji unieważnione T-094: cała ósemka „kart poza indeksem" z 24.08 jest w indeksie.
Zostały cztery karty z crawlem 09.09, czyli sprzed wdrożenia v2 — Google zna adresy, nie zna nowej treści.

**T-092 po 14 dniach — zadziałało na widoczności, nie na kliknięciach.** Pozycja lepsza na 8 z 8 fraz,
kategoria urosła o 99% wyświetleń przy 30% w całym serwisie. Ale CTR spadł 0,63 → 0,53%, a kanibalizacja
**wzrosła**, bo karty v2 weszły na te same zapytania.

### Ads — mapa, projekt i wykonanie

Powstały trzy dokumenty: `docs/ads/2026-09-18-MAPA-KAMPANII.md` (komplet 71 fraz, 150 wykluczeń, geo,
harmonogramy), `docs/ads/2026-09-18-PROJEKT-PRZEBUDOWY-KAMPANII.md` i `data/kontrole/2026-09-18-odczyt-ads.md`.

**Wykonane na koncie:** kampania Marka przebudowana w całości (26 wykluczeń, trzy frazy wstrzymane,
`agria niedomice` dodane, dwie grupy z reklamami na karty #309 i #312), harmonogram Rolnictwa przestawiony
na siedem dni 8:00–16:00, budżet Rolnictwa 60 → 28 zł/dz (ostatnie kliknął Janek).

---

## 2. Siedem ustaleń, które zmieniają wcześniejsze zapisy

1. **Kampanie nigdy nie były wstrzymane.** Rejestr twierdził, że pauza trwa od 14.09 — API pokazuje ciągłą
   emisję. Wrzesień 01–17 to **749,17 zł**, nie prognozowane ~1 800 zł.
2. **72% wydatku prowadzi na dwa landingi `noindex`**, których T-136 nie dotknął. Dlatego ocena strony
   docelowej `poniżej średniej` na 40 z 50 fraz nie mogła drgnąć po przepisaniu kart.
3. **453 kliknięcia wobec 74 sesji „Paid Search" w GA4 (16,3%).** Albo ludzie odpadają przed załadowaniem
   (LCP mobile 3,7–7,6 s), albo consent nie pozwala mierzyć. **Nierozstrzygnięte — to największa niewiadoma projektu.**
4. **`form_submit` jest w Ads konwersją pomocniczą, nie główną.** Stąd rozjazd „2 konwersje" wobec „5".
   Atrybucja do haseł istnieje tylko dla `phone_click`: `wapno nawozowe` (28.08) i `kreda nawozowa mielnik` (08.09).
5. **T-111 miało odwrotną liczbę.** Nie 58,6% przy zamkniętym biurze, tylko **66,1% budżetu w godzinach 8:00–16:00**.
6. **Wykluczenia z 21.08 działają.** Marki konkurencji przestały przeciekać po 31.08; zostały dwie spoza listy
   (`nordkalk`, `wapniak jurajski`) za ~8 zł miesięcznie.
7. **T-141 — rozkład 13 zapytań z formularza** (CPT `agria_inquiry`, komplet od marca): 77% w godzinach 8–16,
   **54% w dni, w których Rolnictwo nie emitowało**, 6 z 13 spoza promienia 150 km (do 600 km), **6 z 13 wysłanych
   z kart produktów** wobec jednego z landingu Ads.

---

## 3. Co jest otwarte — w kolejności ważności

### P1. Gdzie znikają kliknięcia (W1 z projektu Ads)

453 kliknięcia, 74 sesje w GA4. Dopóki tego nie wiemy, **każda decyzja o budżecie stoi na piasku**.
Pomiar: licznik żądań z `gclid` po stronie serwera (logi `/home/server371853/logs` są dla nas nieczytelne).
Robota na ok. godzinę, wartość: rozstrzyga, czy 1 200 zł miesięcznie kupuje klientów, czy powietrze.

### P2. D2 — dokąd prowadzi Rolnictwo

Rozjazd między ADR 11.08 („Ads prowadzi na landingi") a architekturą z 10.09 („wszystko prowadzi do kart").
Karty mają dziś cenę, telefon, callback i **więcej treści niż landingi** (10 869 wobec 9 779 znaków);
brakuje im tylko ramki `agria-cta-hero` nad zgięciem. Pierwszy twardy sygnał: **kontrola 02.10** na kampanii Marka.

### P3. Zasięg dostaw — pytanie do Pawła

Sześć z trzynastu zapytań przyszło z 280–600 km. Jeśli te dostawy się odbywają, promienie 150 km w Rolnictwie
odcinają połowę popytu i zawężenie geo Paszarstwa do pięciu województw byłoby błędem. Jeśli nie — geo zostaje,
a dalekie zapytania to naturalny odpad z organiku i OLX-a.

### P4. D1, D3, D4

Baza wiedzy gotowa od 11.09, karty wdrożone 14.09, warunek Janka spełniony. Kanibalizacja zmierzona 18.09
(`kreda nawozowa` 3 → 5 własnych URL-i) jest nowym materiałem do D1. Pułapka: Premmerce bierze kategorię
o najwyższym `term_id`, ale `rank_math_primary_product_cat` to nadpisuje — sprawdzić primary na 19 kartach
przed jakąkolwiek propozycją.

---

## 4. Terminy

| kiedy | co | kto |
|---|---|---|
| **19.09** | zgłoszenie 4 kart v2 w GSC (#311, #318, #302, #320) | Auranet |
| **20.09** | T-085 `/wapno-hydratyzowane/`, T-093 `/wapno-do-oczyszczalni/`, T-074 spoke ziemniaki | Auranet |
| **23.09 · 30.09** | publikacje na wizytówce (wtorki); 30.09 przygotować cztery na październik | Auranet |
| **26.09** | kontrola T-078 `/paszarstwo/` na frazach formowych | Auranet |
| **30.09** | T-077 poradnik o kredzie pastewnej | Auranet |
| **02.10** | kontrola przebudowy Marki — test dźwigni dla całego konta | Auranet |
| **04.10** | T-092 po 30 dniach + kanibalizacja do D1 | Auranet |
| **15.10** | koniec cyklu Ads, rozliczenie 1 200 zł | Auranet + Janek |
| **31.10** | T-107 podsumowanie trzech miesięcy Ads dla klienta | Auranet |

---

## 5. Czego nie zakładać w następnej sesji

1. **Nie wracaj do tezy o pauzie Ads** — kampanie chodziły nieprzerwanie, jest to sprostowane w T-109.
2. **Nie licz, że karty są poza indeksem** — 19/19 ma `PASS` od 18.09.
3. **Nie obiecuj poprawy kosztu konwersji do 31.10.** Przy pięciu konwersjach na pięć tygodni wykazanie
   spadku z 311,75 zł wymaga dwudziestu–trzydziestu zdarzeń, czyli kwartału. T-107 pokaże koszt i jakość
   ruchu, nie zwrot ze sprzedaży.
4. **Wywołuj `ads_call.sh` jako pojedynczą komendę** — bez `cd &&` i bez pipe'a. Łańcuch nie dopasowuje się
   do reguły w `.claude/settings.json` i trafia do klasyfikatora.
5. **Pliki operacji API nie mogą mieć pól `_opis`/`_endpoint`** — Google je odrzuca. Wersje wykonawcze leżą
   w `scripts/ads/brand-2026-09-18/exec/`.
6. **`ad_group_criterion` ma resourceName `.../adGroupCriteria/{grupa}~{kryterium}`**, nie `.../adGroups/...`.
7. **Budżet cyklu to 15.09–15.10, nie miesiąc kalendarzowy.** Ryczałt 2 000 zł (nasza praca) i 1 200 zł
   (media Ads) to **dwa osobne budżety** — GBP, treść i kontrole idą z ryczałtu i nie konkurują z mediami.

---

## 6. Bilans wrześniowy

Dziennik M4 ma **34 pozycje, z czego 20 z zapisanymi godzinami — razem 37 h**. Przy ryczałcie 2 000 zł netto
miesiąc jest przerobiony powyżej zakresu, a do końca zostaje jeszcze pięć pozycji treściowych (T-085, T-093,
T-074, T-077) i cztery kontrole. ⚠️ **To jest sygnał handlowy, nie techniczny** — wrzesień dowiózł najwięcej
w historii projektu (19 kart v2, dwa opisy kategorii, przebudowa kanału Ads, cztery pozycje OLX),
ale przy tej intensywności ryczałt przestaje się spinać. Do rozmowy z Jankiem przy rozliczeniu M4.
