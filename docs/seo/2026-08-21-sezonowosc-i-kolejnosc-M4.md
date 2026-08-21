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

## 3. Pełna lista — wszystkie 67 pozycji

Legenda statusu: ✅ zamknięte · 🟠 częściowo (rdzeń zamknięty, reszta w kolejce) · 🔴 otwarte na nas ·
🟡 czeka na AGRIĘ · 📅 zaplanowane M4 · 🔵 do rozstrzygnięcia · ⛔ unieważnione

| ID | Zadanie | Linia | Status | Kiedy / co dalej |
|---|---|---|---|---|
| T-001 | Kalkulator przestał proponować kredę pastewną i malarską | Kalkulator | ✅ | 18.06, M1 |
| T-002 | Formy dostawy zdjęte ze specyfikacji 19 kart + FAQ | Treść | ✅ | 29.06, M1 |
| T-003 | Telefony na mapie zgodne z oddziałami, numer 660 usunięty | Strona | ✅ | 01.07, M2 |
| T-004 | Karty produktu i charakterystyki na `/do-pobrania/` | Treść | ✅ | 29.06, M1 |
| T-005 | Zdjęcia produktów zgodne z katalogiem | Strona | ✅ | 29.06, M1 |
| T-006 | Przebudowa sekcji „Dział sprzedaży" | Strona | ⛔ | zdjęte przez Janka 20.08 |
| T-007 | Korekta interpunkcji w tekstach | Treść | ⛔ | zrobił Paweł sam |
| T-008 | 8 atestów i kart charakterystyki Nordkalku na `/do-pobrania/` | SEO | ✅ | 19.08, M3 |
| T-009 | Sekcja „Certyfikaty" zdjęta z `/do-pobrania/` | SEO | ✅ | 19.08, M3 |
| T-010 | Widełki cenowe na 15 kartach + 2 landingach + hub | SEO / ceny | ✅ | 19.08, M3 |
| T-011 | Nagłówki H2 z frazą cenową na kartach | SEO | ✅ | 19.08, razem z T-010 |
| T-012 | Schema Organization zamiast „My Blog" | SEO | ✅ | M1–M2 |
| T-013 | Nagłówki bezpieczeństwa (4 z 6 — brak CSP i Permissions-Policy) | Bezpieczeństwo | ✅ | M1–M2 |
| T-014 | Title strony głównej skrócony do 56 znaków | SEO | ✅ | M1–M2 |
| T-015 | `product_cat` w sitemapie | SEO | ✅ | M1–M2 |
| T-016 | SKU dla produktów (18 z 19, #303 świadomie bez) | SEO | ✅ | M1–M2 |
| T-017 | Literówki w nazwach produktów | Treść | ✅ | M1–M2 |
| T-018 | Sitemapa RankMath po migracji URL | SEO | ✅ | M1–M2 |
| T-019 | `/cart/` poza sitemapą | SEO | ✅ | M1–M2 |
| T-020 | Meta title i description na 6 stronach statycznych | SEO | ✅ | M1–M2 |
| T-021 | Bielik #309 on-page — parametry normowe z karty Nordkalk | Treść | ✅ | M1–M2 |
| T-022 | pH wapna palonego („>16" było fizycznie niemożliwe) | Treść | ✅ | M1–M2 |
| T-023 | „35 lat" → „37 lat" | Treść | ✅ | M1–M2 |
| T-024 | Landing `/wapno-do-stabilizacji-gruntow/` | Strona | ✅ | M1–M2 |
| T-025 | Landingi Ads poza indeksem (`noindex, follow`) | SEO | ✅ | M1–M2 |
| T-026 | Sześć URL-i poza indeksem — diagnoza gotowa | SEO | 🔴 | **decyzja Janka** z 4 scenariuszy. Nie zgłaszać 4. raz do Indexing API |
| T-027 | `/do-pobrania/` — reindeksacja | SEO | 🔴 | zgłoszone 19.08; **recheck GSC 22.08 i 02.09** |
| T-028 | Duplikaty pod `/produkt/` + 15 osieroconych wpisów | SEO | ✅ | 19.08, M3 |
| T-029 | Login administratora przestał wyciekać (3 kanały) | Bezpieczeństwo | ✅ | 19.08, M3 |
| T-030 | LocalBusiness ×2 (Niedomice, Radgoszcz) w schema | SEO | 📅 | M4 |
| T-031 | CWV mobile — LCP 7,3 s przy desktopie 1,5 s | Wydajność | 📅 | M4, po sezonie |
| T-032 | 301 dla starej bazy `/kategoria-produktu/*` | SEO | ✅ | 19.08, M3 |
| T-033 | GA4 nie mierzy mimo działającego CMP | Analityka | 🔵 | rediagnoza od zera; sprawdzić po T-062, po 28.08 |
| T-034 | Premmerce DOM-XSS — wersja 2.3.13 | Bezpieczeństwo | 🔵 | potwierdzić u vendora albo z `readme.txt` |
| T-035 | Landingi organiczne (palone, magnezowe, hydratyzowane, kreda) | SEO | ⛔ | ADR 11.08 — landingi tylko jako cele Ads |
| T-036 | Landingi segmentowe (stawy, sad, oczyszczalnie) | SEO | ⛔ | jw. — menu wraca z treścią |
| T-037 | `/transport-i-dostawa/`, formy dostawy z powrotem na karty | Strona | ⛔ | sprzeczne z T-002, wymaga zgody Pawła |
| T-038 | Huby segmentowe (Rolnictwo / Rybactwo / Oczyszczalnie) | SEO | ⛔ | nieoparte na pomiarze |
| T-039 | Korekty kampanii Marka | Ads | ⛔ | wchłonięte przez T-058 |
| T-040 | Teksty reklam z nazwą „Nordkalk" | Ads | 🟡 | od 19.08 — status autoryzowanego dystrybutora |
| T-041 | Publikacja 200 ogłoszeń OLX | OLX | ✅ | 20.08, M3 |
| T-042 | Poprawki mockupu ogłoszeń OLX po uwagach Kazimierza | OLX | ✅ | 20.08, M3 |
| T-043 | Weryfikacja mockupu kalkulatora Mg przez Kazimierza | Kalkulator | 🟡 | od 18.08 |
| T-044 | Wdrożenie modułu Mg w kalkulatorze na produkcję | Kalkulator | 📅 | M4, po T-043, 4 kwestie otwarte |
| T-045 | Ofertownik, etap zerowy — audyt wycieku cen | Ofertownik | 📅 | M4, osobny wątek |
| T-046 | Optymalizacja profilu GBP Tarnów | GBP | ✅ | 20.08, M3 |
| T-047 | Odzysk profili GBP Niedomice i Radgoszcz | GBP | 🟡 | od 15.07 — dostęp |
| T-048 | Boty pomiarowe dopisane do geobloku (odblokowało PSI) | Strona | ✅ | 19.08, M3 |
| T-049 | Zdjęcia, tytuły i opisy OLX przed emisją | OLX | ✅ | 20.08, M3 |
| T-050 | Zdjęcia na wizytówkę GBP Tarnów | GBP | 🟡 | od 20.08 — materiał od AGRII |
| T-051 | Miniatury OLX nieczytelne na telefonie | OLX | ✅ | 21.08, M3 |
| T-052 | Audyt fraz od nowa + plan treści na sezon | SEO | ✅ | 21.08, M3 |
| T-053 | Blok A — CTR klastra dawkowego (4 adresy) | SEO | ✅ | 21.08; **kontrola CTR w GSC 04.09** |
| T-054 | Blok B — paszarstwo (8 940/mies., największy klaster) | SEO | 🔴 | poradnik i kategoria mogą iść; **karta #307 czeka na Pawła** |
| T-055 | Blok C — klaster „pole" | SEO | 🟠 | terminarz ✅ 21.08. Zostają: hub 10.09, ziemniaki 20.09, łąki, ozime po T-067 |
| T-056 | Blok D — staw i rybactwo (4 100/mies., zero pokrycia) | SEO | 🔴 | kategoria + 2 poradniki + powrót menu „Rybactwo" |
| T-057 | Blok E — gleba i odczyn (6 320/mies., zero pokrycia) | SEO | 🔴 | 2 poradniki + strona tonażowa `/wapno-nawozowe-hurt/` |
| T-058 | Ads — pozostałe | Ads | 🟠 | rdzeń ✅ 21.08. Zostają: grupa „Producent", rewizja grupy Mg/kreda, **ocena 28.08** |
| T-059 | Landingi Ads — ścieżka kontaktu | Strona / Ads | 🟠 | rdzeń ✅ 21.08. Zostaje: lekki formularz `mode="callback"` |
| T-060 | Magnez i fosfor jako kierunek treści | SEO | 🔵 | zaparkowane świadomie przez Janka 21.08 |
| T-061 | `/oferta/` bez H1 | SEO | 🟠 | klasa naprawiona ✅ 21.08 (10 wpisów + główna). Zostaje jeden adres |
| T-062 | Baner zgód zasłaniał ścieżkę kontaktu | Ads / Strona | ✅ | 21.08; **dowód skuteczności: `phone_calls` 28.08** |
| T-063 | Landingi na sprawdzonym wzorcu | Strona | 🟠 | łatka CSS ✅ 21.08. Przebudowa **po sezonie** |
| T-064 | Listingi produktów na trzech landingach | Strona | ✅ | 21.08, M3 |
| T-065 | Sadownictwo — kategoria `/wapno-do-sadu/` (470/mies.) | SEO | 🔴 | **korekta: szczyt marzec 720, nie listopad — XI to 40** |
| T-066 | Terminarz jako hub osi KIEDY + mapa roczna | SEO | 🔴 | ADR 21.08; realizacja rozłożona na rok |
| T-067 | Źródła IUNG-PIB do repo | SEO | 🔴 | **blokuje** ozime, kukurydzę i tabelę uprawową w hubie |

**Bez własnego ID (prace M3):** uruchomienie kampanii Google Ads (13.08) · geoblok bezpieczeństwa (14.08) ·
dostęp SSH i WP-CLI do produkcji (18.08) · ADR dwie warstwy cen (19.08) · spec ofertownika (18.08) ·
porządek dokumentacji: `FAKTY_KLIENTA`, rejestr, `CLAUDE.md` · rdzeń URL/taksonomii (08.07) · raport M2 (03.07)

---

## 4. Proponowana kolejność

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

## 5. Co w tej kolejności jest do rozstrzygnięcia przez Janka

- **Staw przed glebą, mimo że gleba ma większy wolumen** (4 100 vs 6 320). Uzasadnienie: zobowiązanie
  wobec Kasjana, najsłabsza konkurencja, spłata długu nawigacyjnego i produktowego. Odwracalne.
- **Paszarstwo dopiero na pozycji 8, mimo że to największy klaster** (8 940). Uzasadnienie: rozkład
  płaski, więc opóźnienie nic nie kosztuje sezonowo, a karta produktu i tak jest zablokowana.
- **Czy blok F z audytu (październik: stabilizacja gruntów i budownictwo, `wapno palone` X–XI 3 600)
  wchodzi w tę kolejność**, czy zostaje osobno jako zobowiązanie z maila do Kasjana.
