# Prompt wątku: przełożenie 68 ogłoszeń OLX na teren wokół Niedomic i Radgoszczy (T-106)

> **Data zlecenia:** 2026-08-28, Janek. **Powód:** pomiar pierwszego cyklu pokazał, że o wyniku
> ogłoszenia decyduje **odległość od magazynów AGRII**, a jedna trzecia pakietu stoi ponad 200 km
> stąd i nie pracuje. Projekt przydziału jest policzony i zapisany — ten wątek go **wykonuje**.
>
> **Zadanie: przełożyć 68 ogłoszeń zgodnie z gotowym projektem, zweryfikować render i pozycje,
> ustawić punkt kontrolny na 14 dni.**

---

## 0. Zasada nadrzędna

Projekt w `data/olx/przelozenie-2026-08-28.json` jest **wejściem, nie wyrocznią**. Zanim ruszysz
serię, przelicz go od nowa (`scripts/olx/przelozenie.py`) — od 28.08 doszły pomiary z crona
i mogły zmienić, które ogłoszenia są najsłabsze. Jeśli wynik się różni od zapisanego, **pokaż
różnicę Jankowi**, nie nadpisuj po cichu.

Ceny ofertownika nie wychodzą nigdzie. Do klienta nic nie idzie — wszystko przez Janka.

---

## 1. Skąd to się wzięło — pomiar, nie przeczucie

Odległość od Niedomic i Radgoszczy tłumaczy wynik lepiej niż produkt, treść czy wielkość miasta
(pomiar 28.08, 200 ogłoszeń, 7,88 dnia emisji):

| Odległość od magazynów | Ogłoszeń | Kontaktów | Na ogłoszenie |
|---|---|---|---|
| 0–60 km | 31 | 2 | 0,065 |
| **60–120 km** | 37 | **10** | **0,270** |
| 120–200 km | 64 | 9 | 0,141 |
| 200–300 km | 58 | 1 | 0,017 |
| ponad 300 km | 10 | 0 | 0,000 |

**21 z 22 kontaktów przyszło z promienia do 200 km. Dalej stoi 68 ogłoszeń, które dały razem jeden.**

**Przyczyna rozlania siatki jest w danych, nie w modelu.** `scripts/olx/grid.py` liczy dystans od
magazynu wpisanego w kartę produktu, a karty wskazują magazyny **producentów** — kreda granulowana
z Kornicy pod Siedlcami, kreda sypka z Pierzchnicy, węglanowo-magnezowe odm. 04 z Chęcin. Stąd
55 slotów na Mazowszu przy firmie z Tarnowa. **Decyzja Janka 28.08: liczymy od magazynów AGRII,
a asortyment magazynu nie filtruje doboru — sprzedajemy nawozy, powiat dąbrowski i sąsiednie mają
być obsadzone.** Tematu braku Radgoszczy w danych produktowych na stronie **nie ruszamy w tym wątku**.

Pełny rachunek: `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md` §5a i §5b.

---

## 2. Co jest już zrobione i sprawdzone — nie powtarzaj tego

**Mechanika przekładania jest zmierzona na produkcji 28.08** (ogłoszenie 1092697758,
Białobrzegi → Izbicko). `PUT` ze zmienionym `location.city_id`:

- **HTTP 200, status `active` natychmiast** i po 4 minutach — bez moderacji;
- **`created_at` i `valid_to` bez zmian** — staż i emisja zachowane;
- **`auto_extend_enabled` zostaje `true`**;
- **`left: 0` przed i po — jednostki pakietu NIE zjada.** Przy `left: 0` nowe ogłoszenie zostałoby
  odrzucone, więc OLX nie traktuje tego jak nowej publikacji.

Stan sprzed: `data/backups/T-105-olx-1092697758-przed-2026-08-28.json`.
**To ogłoszenie jest już przełożone — nie licz go drugi raz** (`posted.json` ma przy nim adnotację).

---

## 3. Projekt przydziału — 68 ogłoszeń, 22 powiaty

Wyliczony przez `scripts/olx/przelozenie.py`, zapisany w `data/olx/przelozenie-2026-08-28.json`.

| Powiat | Nowych ogłoszeń | Miejscowości |
|---|---|---|
| **dąbrowski** (magazyn Radgoszcz) | **12** | Radgoszcz 4 · Dąbrowa Tarnowska 4 · Szczucin 4 |
| **tarnowski** (magazyn Niedomice) | **10** | Żabno 4 · Lisia Góra 4 · +2 |
| kazimierski · staszowski · bocheński | po 4 | Kazimierza Wielka · Połaniec · Bochnia |
| 17 pozostałych w promieniu 110 km | po 2 | siedziby powiatów i gminy z rynkiem |

Reguły zaszyte w skrypcie, do zachowania przy każdym przeliczeniu:
- **maks. 4 ogłoszenia na miejscowość** — więcej konkuruje ze sobą w jednym wyszukiwaniu;
- **ten sam wariant nie stoi dwa razy w jednej miejscowości**;
- **Agrobielik 90 i Oxyfertil 90 nigdy w tym samym mieście** — oba to tlenkowe 90% CaO;
- **warianty ZASTOSOWANIA (staw / gleba) mogą stać obok siebie** — to nie duplikat, decyzja
  Janka 17.08, raz już zostało to nadgorliwie wycięte;
- **Radgoszcz wchodzi wyjątkiem wymuszonym w kodzie** (`WYMAGANE`) — ma zerowy rynek na OLX
  i bez tego wypadłaby z rankingu, ale ogłoszenie z tą lokalizacją mówi, że towar leży na miejscu.

**Siatka po zmianie:** 60 miejscowości (było 53), **wszystkie w promieniu 200 km od magazynów**.

---

## 4. Zakres robót — dwie różne operacje

**A. 60 ogłoszeń — sama zmiana miejscowości.** Ładunek istnieje, zmienia się jedno pole.
Idzie przez `post_adverts.py --update` albo `PUT` z `putable()`. **Partiami po 25, z bezpiecznikiem
moderacyjnym**, przerwa 2 s między ogłoszeniami.

**B. 8 ogłoszeń — zmiana miejscowości I produktu.** To sloty kredy pastewnej. Powód: **rynek
paszowy siedzi w kategoriach 765 i 761, a pakiet obejmuje WYŁĄCZNIE 4368 (Nawozy)** — odczytane
z `categories_ids`, więc przeniesienia kategorii nie da się zrobić. W Nawozach wszystkie ogłoszenia
z „pastewna" w tytule to nasze, zero konkurencji i zero kontaktów w 8 dni. Zamienniki dobrane wg
zmierzonego zwrotu: węglanowe odm. 04, kreda granulowana, Agrobielik 70 na gleby. **Wymaga
regeneracji ładunku przez `build_adverts.py`** — nowy tytuł, opis, zdjęcia, cena, atrybuty.
Kreda pastewna schodzi z 12 pozycji do 4.

⚠️ **Wykonuj A i B osobno**, nie w jednej serii — inne ryzyko, inna weryfikacja.

---

## 5. Pułapki, na które ktoś już wszedł

**`PUT` podmienia CAŁY zasób, nie łata pola.** Jedno niedomknięte pole kasuje numer telefonu
z ogłoszenia, czyli kanał, który daje wszystkie kontakty. Zawsze buduj ładunek przez `putable()`
z odpowiedzi `GET`, nigdy ręcznie.

**`district_id` jest wymagany w siedmiu dużych miastach** (Warszawa, Kraków, Łódź, Wrocław, Poznań,
Katowice, Częstochowa) — POST/PUT bez niego zwraca `HTTP 400`. **Odwrotnie też: przy przenosinach
DO małej miejscowości `district_id` musi zniknąć z ładunku.** `putable()` bierze tylko te pola
lokalizacji, które są niepuste — sprawdź, czy stary `district_id` nie przecieka.

**Przeindeksowanie wyszukiwarki trwa kilkanaście minut.** Po 4 minutach ogłoszenie wciąż wisi pod
starym adresem, po 19 stoi już pod nowym. **Nie weryfikuj pozycji od razu po serii** — poczekaj
godzinę, inaczej odczytasz stan sprzed zmiany.

**`external_id` niesie w sobie stare `city_id`** (`agria-weglanowe-odmiana-04-2151`), a `posted.json`
jest kluczowany tym samym. Po serii przekładek klucze przestaną odpowiadać miejscowościom.
**Rozstrzygnij konwencję z Jankiem PRZED serią** — albo zostawiamy klucze historyczne i tylko
aktualizujemy pole `city`, albo przepisujemy klucze i `external_id` razem. Nie zostawiaj tego na
później, bo rejestr jest wejściem dla `statystyki.py` i `monitor.py`.

**Statusy `new` i `disabled` tuż po zmianie są przejściowe** (moderacja przepuszcza w 2 min 14 s –
2 min 58 s). Werdykt negatywny to `moderated` albo `blocked`. Pierwsze wersje bezpiecznika
przerywały serię fałszywym alarmem — stąd karencja 300 s w `post_adverts.py`.

**Lista zbiorcza `GET /partner/adverts` oddaje statusy z opóźnieniem** — wiarygodny jest odczyt
`GET /partner/adverts/{id}` per ogłoszenie.

**Nie dotykaj crontaba** inaczej niż przez `~/bin/cron-install`. `monitor.py` chodzi codziennie
o 7:25, `statystyki.py` w poniedziałki o 7:35.

---

## 6. Największa niepewność tego planu — powiedz o niej wprost w podsumowaniu

**Pierścień 0–60 km rośnie z 31 do 73 pozycji, a ma dziś najgorszy zmierzony wynik ze wszystkich
bliskich (0,065 na ogłoszenie).** Powód dzisiejszego słabego wyniku jest jednak inny niż odległość:
siedzą tam Tarnów, Dębica i Brzesko — **trzy miejsca o najgęstszej konkurencji w całej siatce**
(211–254 ogłoszenia w promieniu 50 km). Dokładamy gminy wiejskie o rynku bliskim zera.
**Czy zadziałają, nie wiemy.**

Druga niewiadoma: **sama przeprowadzka do rzadszego regionu nie podnosi pozycji w wynikach.**
Zmierzone na teście — Białobrzegi 110. miejsce na 211 ogłoszeń, Izbicko 56. na 99. Ta sama połowa
stawki. O pozycji decyduje coś innego niż liczba konkurentów w promieniu; czego to funkcja — nie wiadomo.

Cała rekomendacja stoi więc na **wyniku faktycznym** (21 z 22 kontaktów w promieniu 200 km),
nie na obietnicy lepszych pozycji. Przy 22 zdarzeniach to jest mocna wskazówka, nie dowód.

---

## 7. Czym się kończy wątek

1. **68 ogłoszeń przełożonych**, zero odrzutów moderacji, `left: 0` niezmienione, wszystkie `active`.
2. **`posted.json` zgodny ze stanem na koncie** co do jednego wpisu — sprawdzone odczytem per ogłoszenie.
3. **Weryfikacja renderu przez Chrome MCP** na 2–3 przełożonych ogłoszeniach: czy miniatura,
   tytuł i numer telefonu są na miejscu. Nie ufaj samemu API — przy T-041 weryfikacja poszła
   wyłącznie przez API i przegapiła, że miniatury są ucięte na telefonie.
4. **Pomiar wyjściowy** `pozycje.py` na nowej siatce — punkt odniesienia dla kontroli za 14 dni.
5. **Wiersz T-106 w rejestrze zamknięty w tym samym commicie**, z dowodem.
6. **Punkt kontrolny w „Terminach najbliższych"** na 14 dni po przełożeniu: czy pierścień 0–60 km
   zaczął pracować. Odniesienie: 0,065 dziś, 0,270 w pierścieniu 60–120 km.

---

## 8. Skąd czytać

| Co | Gdzie |
|---|---|
| Rachunek i uzasadnienie | `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md` §5a, §5b |
| Projekt przydziału | `data/olx/przelozenie-2026-08-28.json` · `scripts/olx/przelozenie.py` |
| Pomiar pozycji lokalnych | `data/olx/pozycje-2026-08-28.json` · `scripts/olx/pozycje.py` |
| Rejestr wystawionych | `data/olx/posted.json` · ładunek `data/olx/adverts-payload.json` |
| Narzędzie zmiany | `scripts/olx/post_adverts.py` (`--update`, `putable()`, bezpiecznik) |
| Statystyki i monitoring | `scripts/olx/statystyki.py` · `monitor.py` · `data/olx/statystyki.json` |
| Backup sprzed testu | `data/backups/T-105-olx-1092697758-przed-2026-08-28.json` |
| Sekrety | `~/secrets/olx/agria-app.env`; token: `~/domains/auratest.pl/olx-private/agria-tokens.json` |
| Memory | `project_agria_olx_kanal` · `reference_agria_olx_api` |

**Termin nadrzędny, ważniejszy niż ten wątek: pakiet wygasa 16.09, decyzja o odnowieniu do 10.09
(T-105).** Bez odnowienia wszystkie 200 ogłoszeń gasną jednego dnia i przekładanie traci sens.
