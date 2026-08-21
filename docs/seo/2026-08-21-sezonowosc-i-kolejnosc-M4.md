# Przegląd zadań i kolejność na M4 — stan 21.08.2026

**Podstawa:** `docs/REJESTR_ZOBOWIAZAN.md` (odczyt programowy, nie z pamięci) + pomiar sezonowości
DataForSEO `keywords_data/google_ads/search_volume/live`, 24 frazy, location 2616, język pl,
okres **VIII 2025 – VI 2026**, koszt 0,09 USD. Dane surowe: `data/seo/sezonowosc-klastry-2026-08-21.json`.

---

## 1. Liczby

| | Ile |
|---|---|
| Zamknięte (dziennik M1–M3) | **39** pozycji z własnym ID |
| Otwarte na nas 🔴 | **13** |
| Z tego częściowo wykonane | **5** (T-055, T-058, T-059, T-061, T-063 — rdzeń w dzienniku, reszta w kolejce) |
| Czeka na AGRIĘ 🟡 | **4** |
| Zaplanowane M4 📅 | **4** |
| Do rozstrzygnięcia 🔵 | **3** |
| Unieważnione ⛔ | **7** |

---

## 2. Co zmienił pomiar sezonowości

**Założenie „wrzesień = stawy i oczyszczalnie" (mail do Kasjana z 06.08) jest sezonowo błędne.**
Klastry, które mieliśmy robić we wrześniu jako pilne, szczytują **wiosną**. A klastry, które
szczytują teraz, to te, na których **już stoimy** — czyli jesień jest czasem optymalizacji
istniejącego, nie budowania nowego.

### Szczytują TERAZ (IX–XI) — tu grają pieniądze z Ads

| Fraza | Śr./mies. | IX | X | XI |
|---|---|---|---|---|
| `wapno granulowane` | 4 400 | 6 600 | **8 100** | 5 400 |
| `wapno palone` | 2 400 | 2 400 | **3 600** | **3 600** |
| `wapnowanie gleby` | 1 000 | 1 900 | **1 900** | 1 300 |
| `wapno nawozowe` | 1 300 | 1 900 | **1 900** | 1 300 |
| `wapno na pole` | 390 | **720** | 590 | 390 |
| `kiedy wapnować glebę` | 320 | 480 | 590 | **590** |
| `wapno pod ziemniaki` | 50 | 110 | **110** | 70 |

### Szczytują WIOSNĄ (III–V) — publikować teraz, żeby dojrzały

| Fraza | Śr./mies. | III | IV | V | Uwaga |
|---|---|---|---|---|---|
| `kreda do stawu` | 1 300 | **2 900** | 2 400 | 2 400 | plan mówił „wrzesień, rybactwo" |
| `badanie gleby` | 1 000 | **1 900** | 1 300 | 880 | |
| `ph gleby` | 1 000 | 1 600 | **1 600** | 1 300 | |
| `wapno hydratyzowane` | 2 400 | **3 600** | 2 400 | 2 900 | |
| `zakwaszenie gleby` | 390 | 590 | 720 | **880** | |
| `wapnowanie drzew owocowych kiedy` | 210 | **720** | 260 | 140 | **T-065 zapisał „szczyt XI i III" — listopad nieprawdziwy, XI to 40** |
| `wapno na łąki` | 40 | **70** | 40 | 30 | **T-055 zakładał łąki na 15.09 „bo jesienią" — dane mówią marzec** |
| `kreda pastewna` | 2 400 | 2 900 | 2 400 | **2 900** | rozkład płaski, sezonu praktycznie brak |

**Wniosek operacyjny:** treść pod klaster wiosenny opublikowana we wrześniu ma **pięć–sześć miesięcy
rozbiegu** do szczytu, i to jest dobry moment na publikację. Ale uzasadnienie „robimy to teraz,
bo teraz jest sezon" było fałszywe i nie należy nim uzasadniać kolejności.

**Jedyna fraza z realnym szczytem sierpniowym:** `wapno granulowane big bag` — VIII 590 wobec
średniej 260. Szczyt już mija.

---

## 3. Otwarte na nas — 13

| ID | Zadanie | Linia | Rzecz do zrobienia | Sezon |
|---|---|---|---|---|
| **T-058** | Ads — reszta | Ads | grupa „Producent", rewizja grupy „Wapno magnezowe i kreda" (1,00 zł przy suficie 2,00 — 38 wyśw. i 1 klik przez 7 dni), **ocena efektu 28.08** | **teraz** |
| **T-059** | Ścieżka kontaktu — reszta | Strona | lekki formularz `mode="callback"` (imię, telefon, tonaż, lokalizacja) zamiast wyboru z 20 produktów | **teraz** |
| **T-061** | `/oferta/` bez H1 | SEO | jedna strona, `_elementor_data` puste (2 B) — do zdiagnozowania, jaki szablon ją obsługuje. 165 wyśw., poz. 13,6 | **teraz** |
| **T-027** | `/do-pobrania/` reindeksacja | SEO | **recheck GSC 22.08 i 02.09** — zgłoszone 19.08, dowodem jest zmiana werdyktu, nie zgłoszenie | **teraz** |
| **T-026** | Sześć URL-i poza indeksem | SEO | diagnoza gotowa, **czeka na decyzję Janka** z czterech scenariuszy. Nie zgłaszać czwarty raz do Indexing API | — |
| **T-055** | Klaster „pole" — reszta | SEO | hub `/jakie-wapno-na-pole/` (980, IX 720), łąki, ziemniaki. Ozime za stawem, oś na przedplon | hub **jesień**, łąki wiosna, ziemniaki X |
| **T-056** | Staw i rybactwo | SEO | kategoria `/wapno-do-stawow/` (0 produktów, 301), 2 poradniki, powrót menu „Rybactwo" | wiosna, publikacja teraz |
| **T-057** | Gleba i odczyn | SEO | 2 poradniki + strona tonażowa `/wapno-nawozowe-hurt/`. **6 320/mies., największy klaster góry lejka** | wiosna, publikacja teraz |
| **T-054** | Paszarstwo | SEO | poradnik + opis kategorii mogą iść; **karta #307 zablokowana** — opisuje kredę pastewną parametrami wapna tlenkowego | bez sezonu |
| **T-065** | Sadownictwo | SEO | kategoria `/wapno-do-sadu/`, 470/mies. Stary adres wciąż zbiera 23 wyśw. na poz. 7,6 przez 301 | wiosna |
| **T-066** | Terminarz jako hub + mapa roczna | SEO | realizacja mapy z ADR 21.08 | ciągłe |
| **T-067** | Źródła IUNG-PIB do repo | SEO | **blokuje** ozime, kukurydzę i tabelę uprawową w hubie | warunek |
| **T-063** | Landingi na wzorcu | Strona | łatka CSS działa, przebudowa **po sezonie** | po sezonie |

## 4. Czeka na AGRIĘ — 4

| ID | Na co | Od |
|---|---|---|
| **T-040** | status autoryzowanego dystrybutora Nordkalku — bez tego nazwa nie wchodzi w treść reklam | 19.08 |
| **T-050** | zdjęcia na wizytówkę GBP Tarnów (brak wnętrza, produktu, transportu) | 20.08 |
| **T-043** | weryfikacja mockupu kalkulatora Mg przez Kazimierza | 18.08 |
| **T-047** | dostęp do profili GBP Niedomice i Radgoszcz | 15.07 |

## 5. Zaplanowane M4 — 4

**T-044** moduł Mg na produkcję (po T-043) · **T-031** LCP mobile 7,3 s przy desktopie 1,5 s ·
**T-030** LocalBusiness ×2 w schema · **T-045** ofertownik, etap zerowy (audyt wycieku cen)

## 6. Do rozstrzygnięcia — 3

**T-033** GA4 nie mierzy mimo działającego CMP — rediagnoza od zera (T-062 mógł to ruszyć) ·
**T-034** Premmerce DOM-XSS, wersja 2.3.13 · **T-060** magnez i fosfor jako kierunek treści

## 7. Unieważnione — 7

T-035, T-036 (landingi organiczne i segmentowe — ADR 11.08) · T-037 (transport, wymaga zgody Pawła) ·
T-038 (huby segmentowe) · T-006 (dział sprzedaży — zdjęte przez Janka) · T-007 (interpunkcja — zrobił Paweł) ·
T-039 (wchłonięte przez T-058)

## 8. Zamknięte — 39

**M1 (czerwiec):** T-001 kalkulator bez kredy pastewnej i malarskiej · T-002 formy dostawy zdjęte z 19 kart ·
T-004 karty na `/do-pobrania/` · T-005 zdjęcia produktów

**M2 (lipiec):** T-003 telefony na mapie · rdzeń URL/taksonomii · raport M2

**M1–M2, blok SEO on-page (14):** T-012 schema Organization · T-013 nagłówki bezpieczeństwa ·
T-014 title strony głównej · T-015 `product_cat` w sitemapie · T-016 SKU · T-017 literówki ·
T-018 sitemapa po migracji · T-019 `/cart/` poza sitemapą · T-020 meta na 6 stronach ·
T-021 Bielik #309 · T-022 pH wapna palonego · T-023 „35 lat" → „37 lat" ·
T-024 landing stabilizacji · T-025 landingi Ads poza indeksem

**M3 (sierpień, 15 + prace bez ID):** T-008 atesty Nordkalku · T-009 sekcja „Certyfikaty" zdjęta ·
T-010 + T-011 widełki cenowe na 15 kartach i landingach · T-028 duplikaty `/produkt/` ·
T-029 login administratora (3 kanały) · T-032 301 dla `/kategoria-produktu/*` · T-041 200 ogłoszeń OLX ·
T-042 poprawki mockupu OLX · T-046 profil GBP Tarnów · T-048 boty pomiarowe w geobloku ·
T-049 zdjęcia i teksty OLX · T-051 miniatury OLX · T-052 audyt fraz od nowa · T-053 CTR klastra dawkowego ·
T-062 baner zgód · T-064 listingi na landingach · plus rdzenie T-055, T-058, T-059, T-061, T-063.
Bez ID: uruchomienie Ads, geoblok, dostęp SSH, ADR dwie warstwy cen, spec ofertownika, porządek dokumentacji

---

## 9. Proponowana kolejność

Kryteria w tej hierarchii: **(1)** gdzie lecą pieniądze teraz, **(2)** wolumen razy brak pokrycia,
**(3)** czas dojrzewania treści do szczytu, **(4)** co blokuje co.

### A. Do 31.08 — tam, gdzie kampania wydaje 40 zł dziennie

1. **T-027** — recheck GSC (22.08, potem 02.09). Kilka minut.
2. **T-061** — H1 na `/oferta/`. Jedna strona, mała robota, natychmiastowy efekt.
3. **T-058** — ocena efektu ścieżki kontaktu **28.08**, potem decyzja o grupie „Wapno magnezowe
   i kreda" (podnieść stawkę albo wygasić i oddać budżet) i teksty grupy „Producent" bez nazwy Nordkalk.
4. **T-059 (reszta)** — lekki formularz callback. Ta sama sprawa co T-062: usuwanie tarcia
   na ścieżce, na której już płacimy za ruch.

### B. 01–20.09 — produkcja treści, kolejność wg wolumenu i konkurencji

5. **T-056 staw** — 4 100/mies., **zero pokrycia**, trzy posty z Facebooka w TOP7 (najsłabsza
   konkurencja w portfelu). Spłaca dług nawigacyjny z 30.07, zdejmuje 301 z pustej kategorii
   i jest zobowiązaniem z maila do Kasjana. Szczyt marcowy — pięć miesięcy rozbiegu.
6. **T-055 hub `/jakie-wapno-na-pole/`** — 980/mies., **jedyny klaster treściowy ze szczytem
   jesiennym** (IX 720). Bez tabeli uprawowej, bo ta czeka na T-067.
7. **T-057 gleba i odczyn** — 6 320/mies., zero pokrycia, góra lejka, droga którą Polcalc zbudował
   95% widoczności. Szczyt marzec–maj.

### C. Wrzesień–październik — reszta sezonowa

8. **T-054 paszarstwo** — 8 940/mies., **największy klaster w portfelu**. Poradnik i opis kategorii
   idą niezależnie; karta #307 czeka na parametry od Pawła.
9. **T-055 ziemniaki** — jedyny spoke uprawowy z potwierdzonym szczytem październikowym.
10. **T-065 sadownictwo** — 470/mies., szczyt marcowy.
11. **T-055 łąki** — 210/mies., szczyt marcowy (nie wrześniowy, jak zakładał plan).

### D. Równolegle, gdy pojawi się okno

12. **T-067 źródła IUNG** — odblokowuje ozime, kukurydzę i tabelę uprawową.
13. **T-026** — decyzja Janka z czterech scenariuszy indeksacji.
14. **T-033** — rediagnoza GA4. T-062 mógł ją ruszyć, warto sprawdzić po 28.08.

### E. Po sezonie

15. **T-063** landingi na wzorcu · **T-031** LCP mobile · **T-045** ofertownik · **T-066** kolejne
    wpisy z mapy rocznej.

---

## 10. Co w tej kolejności jest do rozstrzygnięcia przez Janka

- **Staw przed glebą, mimo że gleba ma większy wolumen** (4 100 vs 6 320). Uzasadnienie: zobowiązanie
  wobec Kasjana, najsłabsza konkurencja, spłata długu nawigacyjnego i produktowego. Odwracalne.
- **Paszarstwo dopiero na pozycji 8, mimo że to największy klaster** (8 940). Uzasadnienie: rozkład
  płaski, więc opóźnienie nic nie kosztuje sezonowo, a karta produktu i tak jest zablokowana.
- **Czy blok F z audytu (październik: stabilizacja gruntów i budownictwo, `wapno palone` X–XI 3 600)
  wchodzi w tę kolejność**, czy zostaje osobno jako zobowiązanie z maila do Kasjana.
