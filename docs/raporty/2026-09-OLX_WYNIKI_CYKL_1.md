# OLX — wynik pierwszego cyklu i decyzja o odnowieniu pakietu

> **Pomiar własny 28.08.2026, 15:01** — `scripts/olx/statystyki.py` odczytał **200 z 200** ogłoszeń
> per `GET /partner/adverts/{id}/statistics`, nie z listy zbiorczej. Pomiar dopisany do
> `data/olx/statystyki.json` (piąty w historii). Snapshot rynku z tego samego dnia:
> `data/olx/market/2026-08-28.json`. Ads i GSC odczytane w tym samym wątku przez API.
>
> **Cykl:** emisja 20.08 18:01 → 19.09; pakiet ważny do **16.09**. W chwili pomiaru zmierzone
> **7,88 dnia z 30**. Wszystko, co dotyczy pełnego cyklu, jest projekcją i jest tak oznaczone.
>
> Ceny ofertownika nie występują w tym dokumencie w żadnej postaci.

---

## 1. Wynik — ile kanał dał w pierwszych ośmiu dniach

| Pomiar | Ogłoszeń | Odsłony | Odsłony numeru | Obserwujący |
|---|---|---|---|---|
| 21.08 10:38 | 200 | 120 | 1 | 10 |
| 24.08 07:35 | 200 | 307 | 3 | 15 |
| 25.08 09:53 | 200 | 366 | 10 | 15 |
| **28.08 15:01** | **200** | **634** | **22** | **21** |

Statystyki OLX są kumulatywne od wystawienia, więc tempo liczy się z różnic:

| Okno | Dni | Odsłony/dzień | Odsłony numeru/dzień |
|---|---|---|---|
| 21.08 → 24.08 | 2,87 | 65,1 | 0,70 |
| 24.08 → 25.08 | 1,10 | 53,8 | 6,39 |
| 25.08 → 28.08 | 3,21 | **83,5** | **3,74** |
| **całość 20.08 → 28.08** | **7,88** | **80,5** | **2,79** |

**Ruch nie wysyca się — narasta.** Ostatnie okno jest najmocniejsze w całym pomiarze, mimo że
ogłoszenia mają już tydzień. Odsłony numeru są zbyt rzadkie, żeby czytać z nich krzywą dzień po
dniu (22 zdarzenia na cały pomiar), ale kierunek jest zgodny: 1 → 3 → 10 → 22.

**Obserwujący: 21.** To osoby, które kliknęły „obserwuj" i dostaną powiadomienie o zmianie ceny.
Wartość tej liczby ujawni się dopiero przy korekcie cennika — dziś to zapas, nie wynik.

---

## 2. Rozkład — kanał ciągną nieliczne ogłoszenia

Przy 200 ogłoszeniach średnia zaciera obraz. Rozkład faktyczny:

- **19 ogłoszeń z 200** ma choć jedną odsłonę numeru. Pozostałe 181 — zero.
- **19 ogłoszeń** nie ma ani jednej odsłony w ogóle.
- Sto najlepszych ogłoszeń zbiera **81% wszystkich odsłon**; dwadzieścia najlepszych — 31%.

### Wariant treści (17 kombinacji tytuł+opis, geo-multiplikacja na wierzchu)

| Wariant | Ogłoszeń | Odsłony | Odsłony numeru | Tel./ogłoszenie | Przyrost odsłon/ogł./dzień (25→28.08) |
|---|---|---|---|---|---|
| oxyfertil-90 | 7 | 21 | **3** | **0,43** | 0,40 |
| weglanowe-odmiana-04 | 16 | 51 | **5** | **0,31** | 0,31 |
| kreda-nawozowa-granulowana | 14 | 39 | 3 | 0,21 | 0,38 |
| agrobielik-70-gleba | 30 | 93 | 3 | 0,10 | 0,43 |
| agrobielik-90 | 25 | 108 | 2 | 0,08 | 0,49 |
| weglanowe-magnez-odmiana-05 | 8 | 33 | 1 | 0,13 | 0,55 |
| weglanowe-magnez-odmiana-04 | 12 | 42 | 1 | 0,08 | 0,57 |
| kreda-nawozowa-sypka | 16 | 55 | 1 | 0,06 | 0,62 |
| weglanowe-magnez-granulowane | 18 | 82 | 1 | 0,06 | 0,62 |
| weglanowe-granulowane | 20 | 55 | 1 | 0,05 | 0,36 |
| agrobielik-70-staw | 22 | 40 | 1 | 0,05 | **0,20** |
| **kreda-pastewna** | 12 | 15 | **0** | **0,00** | **0,13** |

Dwa odczyty, które się rozjeżdżają: **odsłony zbiera magnez i Agrobielik 90, a odsłony numeru —
Oxyfertil 90 i węglanowe odm. 04.** Oglądalność i kontakt to nie ta sama rzecz; przy 22 zdarzeniach
nie rozstrzygam, czy to różnica realna, czy przypadek.

Jednoznacznie słabe są dwa końce tabeli: **kreda pastewna** (12 ogłoszeń, 15 odsłon, zero kontaktów,
4 ogłoszenia z zerem odsłon) i **Agrobielik do stawu** (22 ogłoszenia, najniższy przyrost, 5 ogłoszeń
z zerem). Przy stawie sezon jest jednak przeciw pomiarowi — wapnowanie stawu robi się jesienią po
spuszczeniu wody i wiosną, nie w sierpniu; ten wariant ocenimy uczciwie dopiero w drugim cyklu.

### Miejscowość — wieś pracuje dwa razy lepiej niż aglomeracja

| Klasa | Ogłoszeń | Odsłony/ogł. | Odsłony numeru | Tel./ogłoszenie |
|---|---|---|---|---|
| miasta poniżej 90 tys. i miejscowości rolnicze | 134 | 3,6 | **18** | **0,134** |
| miasta powyżej 90 tys. | 66 | 2,4 | 4 | 0,061 |

Slot w mniejszej miejscowości daje **2,2 razy więcej kontaktów** niż slot w dużym mieście.
Najlepsze: Zator (6 ogłoszeń → 53 odsłony, 5 kontaktów), Piotrków Trybunalski (4 → 22, 3),
Miechów (4 → 31, 2), Zwoleń (4 → 17, 2). Na drugim końcu Warszawa (6 → 10, 0), Katowice (5 → 6, 1),
Poznań (1 → 1, 0), Płock (4 → 4, 0).

To jest **ta sama obserwacja, którą 28.08 wprowadziliśmy do Google Ads** (przestawienie kampanii
Rolnictwo na obszary wiejskie). Dwa niezależne kanały pokazują to samo — próba jest mała
(4 kontakty po stronie dużych miast), ale kierunek zgadza się z drugim źródłem.

---

## 3. Czy prognoza się broni

Prognoza z planu (`docs/offers/2026-08-PLAN_OLX.md`): ostrożnie ~50, realnie ~150,
optymistycznie ~230 odsłon numeru miesięcznie, przy założeniu ~4 480 odsłon ogłoszeń i wskaźnika
kontaktu 3,35%.

| Wielkość | Założenie w prognozie | Pomiar 28.08 | Projekcja na cykl 30 dni |
|---|---|---|---|
| Odsłony | ~4 480 | 634 w 7,88 dnia | **2 400 – 2 500** |
| Wskaźnik kontaktu | 3,35% | **3,47%** | — |
| Odsłony numeru | ~150 | 22 w 7,88 dnia | **84 – 105** |

Dolna granica projekcji to tempo skumulowane, górna — tempo z ostatniego okna utrzymane do końca
cyklu. Zmierzono 7,88 z 30 dni, więc obie liczby są ekstrapolacją z jednej czwartej cyklu.

**Rozstrzygnięcie: prognoza chybiła w jednym miejscu — w ruchu, nie w konwersji.**
Wskaźnik kontaktu wyszedł 3,47% wobec zakładanych 3,35%, czyli założenie z kohorty 16 ogłoszeń
się obroniło. Nie obroniło się tempo oglądalności: mamy ~54% zakładanego ruchu. Wynik ląduje
**między scenariuszem ostrożnym a realnym, bliżej realnego** — około dwóch trzecich „realnie 150".

Zastrzeżenie do góry: sierpień jest **szczytem roku** dla całej rodziny fraz „pole / dawka /
granulat" (`wapno granulowane` 9 900 wobec średniej 4 400). Pierwszy cykl stoi więc na najlepszym
miesiącu — drugi będzie niższy dla granulatu, ale wyższy dla wapna palonego (`wapno palone`
szczytuje X–XI: 3 600 wobec 1 600 w sierpniu).

---

## 4. Ile kosztuje jeden kontakt — i jak to wypada wobec Ads

**Koszt kanału na cykl:** pakiet Premium 200 = 1 199,99 zł brutto (975,60 netto) po stronie AGRII
+ 300 zł netto prowadzenia po stronie Auranet = **1 275,60 zł netto** (1 568,99 zł do zapłaty).
Setup 1 800 zł był jednorazowy i w tym rachunku nie występuje.

| Scenariusz | Odsłony numeru | Koszt kontaktu netto |
|---|---|---|
| Tempo skumulowane | 84 | **15,19 zł** |
| Tempo z ostatniego okna | 105 | **12,15 zł** |

Plan obiecywał 6,50–30 zł za kontakt. **Jesteśmy w obiecanym przedziale, w jego lepszej połowie.**

### Zestawienie z Google Ads, ten sam okres, ta sama jednostka

| Kanał | Okres | Koszt netto | Zmierzone kontakty | Koszt kontaktu |
|---|---|---|---|---|
| OLX | 20–28.08 | 334,85 (pro rata) | 22 odsłony numeru | **15,22 zł** |
| Google Ads | 20–28.08 | 309,62 | 3 konwersje | 103,21 zł |
| OLX | 25–28.08 | 136,49 (pro rata) | 12 odsłon numeru | **11,37 zł** |
| Google Ads | 25–28.08 | 108,43 | 3 konwersje | 36,14 zł |

Ads w tym oknie: 183 kliknięcia, 3 zmierzone konwersje — dwa wysłania formularza 25.08 i jedno
kliknięcie w numer 28.08 (`phone_click`, pierwszego dnia po przestawieniu celu).

**Trzy zastrzeżenia, bez których to zestawienie kłamie:**

1. **Pomiar konwersji w Ads zaczął działać dopiero 24–25.08.** Wcześniejsze „zero konwersji"
   (13–23.08: 215 kliknięć, 396,18 zł) to zero pomiaru, nie zero telefonów. Realny koszt kontaktu
   w Ads jest **niższy niż 103 zł** — o ile, nie wiemy.
2. **27.08 9:00 → 28.08 9:00 emisja Ads stała** (konto niedoładowane), co obcina okno o dobę.
3. **„Odsłona numeru" na OLX to nie telefon** — to odsłonięcie numeru przez zainteresowanego.
   `phone_click` w Ads jest tym samym zdarzeniem po stronie strony. Jednostki są porównywalne,
   ale żadna z nich nie jest zamówieniem.

Mimo tych zastrzeżeń różnica jest kilkukrotna i idzie w tę samą stronę w obu oknach.

### Skala wobec organiku

W tym samym oknie 20–27.08 wyszukiwarka dała **96 kliknięć** na agria.pl (GSC, 7 125 wyświetleń,
poz. 6,9). OLX w tym czasie — 634 odsłony ogłoszeń. Sierpień narastająco (1–27.08) to
**317 kliknięć** organicznych wobec 221 w całym lipcu, więc organik rośnie niezależnie.
Jednostki nie są tożsame (kliknięcie w wynik ≠ odsłona ogłoszenia), ale rząd wielkości ekspozycji
po stronie OLX jest kilkukrotnie wyższy. Kontaktów z organiku nie umiemy dziś policzyć —
warstwa zgód odcina pomiar.

---

## 5. Co poprawić przed drugim cyklem — propozycje, nic nie wykonane

Żadna z tych zmian nie została wprowadzona; to wątek analityczny.

1. **Przesunąć 12 slotów kredy pastewnej.** Zero kontaktów, 15 odsłon, 4 ogłoszenia z zerem odsłon
   — najsłabsza pozycja w portfelu. **Zastrzeżenie: paszarstwo należy do rewizji sezonowej
   (listopad), która jest poza wyceną** — więc to liczba do tamtej rewizji, nie zadanie na teraz.
2. **Przesunąć część slotów z dużych miast na miejscowości rolnicze.** Materiał: 66 slotów
   pracujących 2,2 razy słabiej. Rezerwa siatki istnieje — plan wyliczył 2 708 sensownych
   kombinacji produkt–miejscowość, wykorzystujemy 200.
3. **Nie ruszać wariantu „do stawu" na podstawie sierpnia.** Sezon stawowy to jesień i wiosna;
   pomiar w szczycie sezonu polowego jest dla niego niesprawiedliwy. Wariant zastosowaniowy dzieli
   22 miejscowości z wariantem glebowym świadomie (decyzja 17.08) — to nie jest duplikat.
4. **Przed jakąkolwiek serią: sprawdzić na jednym ogłoszeniu, czy zmiana miejscowości w `PUT`
   nie liczy się jako nowe ogłoszenie i nie zjada jednostki pakietu.** Zmierzone jest tylko to, że
   edycja treści i zdjęć jednostki nie zjada (T-051). Zmiana miejscowości — niesprawdzona.

`PUT /partner/adverts/{id}` podmienia cały zasób, nie łata pola — jedno niedomknięte pole kasuje
numer telefonu, czyli jedyny kanał kontaktu. Każda taka seria idzie z bezpiecznikiem i testem na
jednym ogłoszeniu.

---

## 5a. Zmierzone 28.08 po południu — dystans do własnych magazynów i test przekładania

**Odległość od Niedomic i Radgoszczy tłumaczy wynik lepiej niż cokolwiek innego, co zmierzyłem.**

| Odległość od Niedomic/Radgoszczy | Ogłoszeń | Kontaktów | Na ogłoszenie |
|---|---|---|---|
| 0–60 km | 31 | 2 | 0,065 |
| **60–120 km** | 37 | **10** | **0,270** |
| 120–200 km | 64 | 9 | 0,141 |
| 200–300 km | 58 | 1 | 0,017 |
| ponad 300 km | 10 | 0 | 0,000 |

**21 z 22 kontaktów przyszło z promienia do 200 km; 68 ogłoszeń stoi dalej i dało razem jeden.**
Najbliższy pierścień (do 60 km) wypada słabo, bo Tarnów, Dębica i Brzesko mają najgęstszą
konkurencję z całej siatki (211–254 ogłoszenia w promieniu 50 km).

**Przyczyna rozlania siatki po Polsce jest w danych, nie w modelu.** `grid.py` liczy dystans od
magazynu wpisanego w kartę produktu, a karty wskazują **magazyny producentów** — kreda granulowana
z Kornicy pod Siedlcami, kreda sypka z Pierzchnicy, węglanowo-magnezowe odm. 04 z Chęcin.
**Radgoszcz nie występuje w żadnej z 19 kart** (taksonomia `pa_agria-lokalizacja`, 17 termów,
sprawdzone `query_db` 28.08) — magazyn własny AGRII, o którym własna strona milczy. Model nie miał
skąd wiedzieć, że towar leży w Radgoszczy. Pięć z jedenastu wystawionych produktów (kreda sypka,
kreda pastewna, węglanowe odm. 04 i 05, węglanowo-magnezowe odm. 04) **nie ma w Niedomicach w ogóle**.

### Test przekładania ogłoszenia — wykonany na produkcji 28.08, jedno ogłoszenie

Ogłoszenie 1092697758 (węglanowe odm. 04, jedyne z zerem odsłon w 8 dni), `PUT` ze zmienionym
`location.city_id`: **Białobrzegi → Izbicko**. Stan sprzed: `data/backups/T-105-olx-1092697758-przed-2026-08-28.json`.

| Co sprawdzone | Wynik |
|---|---|
| Odpowiedź API | **HTTP 200**, status `active` natychmiast i po 4 minutach — bez moderacji |
| `created_at` | **bez zmian** (2026-08-20 17:55:39) — staż ogłoszenia zachowany |
| `valid_to` | **bez zmian** (2026-09-19 17:55:39) — emisja nietknięta |
| `auto_extend_enabled` | **true** — zachowane |
| Miejsce w pakiecie | **`left: 0` przed i po** — nie skonsumowało jednostki |

Dowód, że OLX nie traktuje tego jak nowego ogłoszenia: przy `left: 0` publikacja nowego zostałaby
odrzucona, a `PUT` przeszedł i zachował datę utworzenia. **Przekładanie ogłoszeń jest darmowe.**

⚠️ **Przeindeksowanie wyszukiwarki trwa kilkanaście minut** — po 4 minutach ogłoszenie wciąż było
widoczne pod starym adresem, po 19 stało już w Izbicku i zniknęło z Białobrzegów.

⚠️ **Sama zmiana na rzadszy region nie podnosi pozycji.** Białobrzegi: 110. miejsce na 211 ogłoszeń.
Izbicko: 56. na 99. Ta sama połowa stawki. O pozycji decyduje coś innego niż liczba konkurentów
w promieniu — czego to jest funkcja, nie wiemy.

⚠️ **`external_id` niesie stare `city_id`** (`agria-weglanowe-odmiana-04-2151`), więc po serii
przekładek klucze rejestru przestaną odpowiadać miejscowościom. W teście zostawiony celowo, żeby
zmienna była jedna; w `posted.json` dopisana adnotacja.

## 5b. Projekt przełożenia 68 ogłoszeń na teren wokół magazynów

Wyliczony skryptem `scripts/olx/przelozenie.py`, wynik w `data/olx/przelozenie-2026-08-28.json`.
Kryterium doboru zmienione względem `grid.py`: **dystans liczony od magazynów AGRII
(Niedomice, Radgoszcz), nie od magazynów producentów**, a w obrębie powiatu wybierana miejscowość
z realnym rynkiem lokalnym zamiast najbliższej wsi. Decyzja Janka 28.08: powiat dąbrowski
i sąsiednie mają być obsadzone; asortyment magazynu nie filtruje doboru — sprzedajemy nawozy.

**Obsadzenie powiatów** — 22 powiaty, ciężar na terenie własnym:

| Powiat | Nowych ogłoszeń | Miejscowości |
|---|---|---|
| **dąbrowski** (magazyn Radgoszcz) | **12** | Radgoszcz 4 · Dąbrowa Tarnowska 4 · Szczucin 4 |
| **tarnowski** (magazyn Niedomice) | **10** | Żabno 4 · Lisia Góra 4 · +2 |
| kazimierski · staszowski · bocheński | po 4 | Kazimierza Wielka · Połaniec · Bochnia |
| 17 pozostałych w promieniu 110 km | po 2 | siedziby powiatów i gminy z rynkiem |

Radgoszcz weszła jako **wyjątek wymuszony w kodzie** — ma zerowy rynek na OLX i bez tego wypadłaby
z rankingu, ale ogłoszenie z tą lokalizacją mówi kupującemu, że towar leży na miejscu.

**Siatka po zmianie:** 200 ogłoszeń, 60 miejscowości (było 53), **wszystkie w promieniu 200 km
od magazynów** — dziś 68 stoi dalej.

| Pierścień | Przed | Po |
|---|---|---|
| 0–60 km | 31 | **73** |
| 60–120 km | 37 | 63 |
| 120–200 km | 64 | 64 |
| 200–300 km | 58 | **0** |
| ponad 300 km | 10 | **0** |

⚠️ **Zastrzeżenie pomiarowe, którego nie wolno zgubić:** pierścień 0–60 km ma dziś **najgorszy
zmierzony wynik ze wszystkich bliskich** (0,065 na ogłoszenie) i rośnie w tym projekcie z 31 do 73
pozycji. Powód dzisiejszego słabego wyniku jest jednak inny niż odległość — siedzą tam Tarnów,
Dębica i Brzesko, czyli **trzy miejsca o najgęstszej konkurencji w całej siatce** (211–254 ogłoszenia
w promieniu 50 km). Dokładamy gminy wiejskie o rynku bliskim zera. **Czy zadziałają — nie wiemy**,
i to jest największa niepewność tego planu. Sprawdzalne jednym pomiarem 14 dni po przełożeniu.

**Zakres robót:**
- **60 ogłoszeń — sama zmiana miejscowości.** `PUT` z istniejącym ładunkiem, mechanika sprawdzona.
- **8 ogłoszeń — zmiana miejscowości i produktu.** To sloty kredy pastewnej: rynek paszowy siedzi
  w kategoriach 765 i 761, pakiet obejmuje wyłącznie 4368, więc przeniesienie kategorii jest
  niewykonalne. Zamienniki dobrane wg zmierzonego zwrotu: węglanowe odm. 04, kreda granulowana,
  Agrobielik 70 na gleby. Wymaga regeneracji ładunku przez `build_adverts.py`.
  Kreda pastewna schodzi z 12 pozycji do 4.

**Czego ten projekt nie obejmuje:** treści ogłoszeń, cen, zdjęć i pozostałych 132 ogłoszeń.


---

## 6. Rynek — co się zmieniło od baseline'u 07.08

Snapshot 28.08 (`market_snapshot.py`, kategorie 4368 Nawozy + 765 Pozostałe rolnicze) wobec
baseline'u z 07.08, okres 20,8 dnia:

| | 07.08 | 28.08 |
|---|---|---|
| Ogłoszeń w kategoriach | 2 486 | 2 588 |
| **w tym AGRIA** | 0 | **196** |
| **Rynek bez AGRII** | 2 486 | **2 392 (−3,8%)** |
| Sprzedawców | 544 | 534 |
| Sprzedawców obecnych w obu pomiarach | — | **128** |
| Ogłoszeń promowanych | 603 | 659 |

**Rynek się nie zagęścił — to my go zagęściliśmy.** Cały przyrost kategorii to nasze ogłoszenia;
po ich odjęciu rynek skurczył się o 94 pozycje. AGRIA jest dziś **drugim sprzedawcą w kategorii**
z 7,6% wszystkich ogłoszeń, z pozycji „jedno ogłoszenie" trzy tygodnie temu.

Rotacja jest ogromna: **tylko 128 z ponad 500 sprzedawców występuje w obu pomiarach.** Reszta to
wystawki, które wygasają po miesiącu. To jest dokładnie ta różnica, którą kupuje pakiet — obecność
ciągła zamiast epizodycznej.

Dwie zmiany po stronie liderów:

- **Dotychczasowy lider `699-712-071` spadł z 510 do 122 ogłoszeń.** Nie wiemy, czy to decyzja,
  czy wygasły pakiet — z API tego nie widać.
- **Wszedł nowy gracz: AGRICOM (Spółka Cywilna) z 269 ogłoszeniami plus 43 na drugim koncie**,
  z zera. Konto „Ewelina" ze 103 ogłoszeniami zniknęło w tym samym czasie, więc najpewniej jest to
  ta sama firma przechodząca z konta prywatnego na firmowe — i **robiąca to samo, co my**:
  masową obecność geograficzną.

**Uwaga metodyczna:** nazwa sprzedawcy nie jest identyfikatorem — konta zmieniają nazwy przy
przejściu na firmowe. Diff liczony po `user_id`, nie po nazwie; pierwszy odczyt po nazwie pokazywał
nieistniejące „nowe firmy".

---

## 7. Rekomendacja

**Odnawiamy pakiet Premium 200. Bez zmiany progu w żadną stronę. Decyzja do 10.09.**

**Dlaczego 200, a nie mniej:** zmierzony koszt kontaktu 12–15 zł netto mieści się w obiecanym
przedziale i jest **trzy do siedmiu razy niższy niż jedyny zmierzony koszt kontaktu z Google Ads**
w tym samym okresie. Zejście na 100 ogłoszeń podnosi cenę jednostkową slotu z 6,00 do 7,20 zł
i obcina zasięg o połowę — płacimy więcej za mniej.

**Dlaczego 200, a nie więcej:** próg 300 to +720 zł brutto za sloty, o których **własny pomiar mówi,
że będą słabsze** — kolejne miejscowości są niżej w rankingu popytu, a już dziś widzimy, że gorzej
dobrany slot pracuje dwa razy słabiej. Suwak pakietu kończy się na 200 (progi 5/10/20/50/100/200),
więc 400 to dwa osobne zakupy o **niesprawdzonej sumowalności**. Zanim dołożymy pieniądze do skali,
tańszą poprawę mamy wewnątrz obecnych 200 — przełożenie najsłabszych slotów kosztuje zero.

**Dlaczego w ogóle odnawiamy, skoro wynik jest poniżej „realnego" scenariusza:** bo chybiła
prognoza ruchu, a nie mechanika kanału — wskaźnik kontaktu wyszedł powyżej założenia. Kanał na
zmierzonych liczbach jest najtańszym źródłem kontaktu, jakim dziś dysponujemy. Drugi cykl trafia
w szczyt wapna palonego (X–XI), czyli w produkty, w których AGRIA jest mocna.

### Termin jest tu ważniejszy niż rekomendacja

**Pakiet wygasa 16.09, emisja kończy się 19.09.** `auto_extend` przedłuża ogłoszenia **tylko
dopóki żyje pakiet**. Precedens zmierzony: 18.07 ogłoszenie 858802418 odnowiło się o 08:43:52,
pakiet wygasł o 08:55 — pozostałych siedemnaście zgasło tego samego dnia, w środku sezonu.

Jeśli decyzja nie zapadnie i przelew nie przejdzie przed 16.09, **wszystkie 200 ogłoszeń gasną
jednego dnia**, a odbudowa to nie jest kliknięcie — to ponowna publikacja z moderacją.
Dlatego pytanie do Pawła idzie z datą **10.09**, nie 16.09: sześć dni zapasu na decyzję i płatność.

---

## 8. Czego nie zmierzono

- **Ile z tych kontaktów zamieniło się w rozmowę i w zamówienie.** OLX oddaje odsłonę numeru,
  nie połączenie. Rozstrzygnąć może wyłącznie AGRIA — to pytanie do Pawła i Kazimierza:
  czy od 20.08 dzwoni więcej ludzi „z internetu".
- **Rozkład kontaktów w czasie w skali dnia** — cztery punkty pomiarowe na osiem dni.
  Poniedziałkowy cron (`statystyki.py`, 7:35) da gęstszą serię; następny wpada **31.08**.
- **Efekt drugiego cyklu na tych samych ogłoszeniach** — czy ogłoszenie odświeżane przez
  `auto_extend` trzeci tydzień utrzymuje tempo, czy opada.
- **Realny koszt kontaktu w Ads** przed 25.08 — pomiaru wtedy nie było.
