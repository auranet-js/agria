# Plan wrzesień 2026 — rewizja na świeżych danych

> **Data:** 2026-09-07 · **Źródła pomiaru:** DataForSEO Keywords Data (07.09), GSC Search Analytics
> 01.08–03.09 (dane dojrzałe), Google Ads API v25 14.08–07.09, GA4 Data API, GBP Business Information
> + Performance API 01.06–05.09.
> **Zastępuje** kolejność z ADR `2026-08-24-audyt-seo-od-nowa-rozstrzygniecia.md` w części wrześniowej.
> Pomiar bazowy: `data/kontrole/2026-09-07-odczyt-ads-7-dni.md`.

---

## 1. Jedno zdanie, które ustawia cały wrzesień

**Serwis ma 32 047 wyświetleń i 410 kliknięć — CTR 1,28%.** Nie brakuje nam widoczności, brakuje
kliknięć. Plan wrześniowy w obecnej postaci dokłada widoczność (pięć nowych treści), a nie rusza
tego, co już mamy i czego nie umiemy zamienić na wejścia.

Dowód wprost z kart produktowych, ten sam serwis i ten sam szablon:

| karta | wyświetlenia | kliknięcia | CTR | pozycja |
|---|---|---|---|---|
| `oxyfertil-90` | 413 | **25** | **6,05%** | 5,6 |
| `agrobielik-70` | 198 | **11** | **5,56%** | 6,2 |
| `weglanowe-odmiana-04` | **1 233** | 12 | **0,97%** | **7,5** |
| `weglanowe-granulowane` | 569 | **1** | **0,18%** | 19,1 |
| `weglanowe-magnez-granulowane` | 355 | **0** | **0,00%** | 26,1 |
| `wapno-tlenkowe-magnez` | 391 | 2 | 0,51% | 13,5 |

Dwie karty z **nazwą własną produktu** (Oxyfertil, Agrobielik) mają CTR 5,5–6%. Karty z nazwą
generyczną („węglanowe odmiana 04") mają 0–1% **przy lepszej pozycji**. Gdyby `weglanowe-odmiana-04`
klikało się jak Oxyfertil, dałoby **74 kliknięcia zamiast 12** — z ruchu, który już mamy, bez jednego
nowego adresu.

## 2. Sezonowość: szczyt rdzenia jest w PAŹDZIERNIKU, a tam jesteśmy najsłabsi

Świeży pomiar DFS (07.09), wolumeny miesięczne:

| fraza | /mies | **IX** | **X** | pozycja organiczna | QS w Ads |
|---|---|---|---|---|---|
| `wapno granulowane` | 4 400 | 6 600 | **8 100** | hub 2,0 (41 wyśw., 0 klik.) | 5 |
| `wapno magnezowe` | 1 900 | 2 900 | **3 600** | **43,6** | **2** |
| `kreda nawozowa` | 1 000 | 1 600 | **1 600** | **24,2** | 3 |
| `wapno tlenkowe` | 720 | 880 | **1 000** | **20,4** | **1** |
| `wapno nawozowe` | 1 300 | 1 900 | 1 900 | kategoria 11,0 | 5 |
| `wapno węglanowe` | 260 | 390 | 390 | karta 9,9 (718 wyśw., 1 klik.) | **1** |

**Trzy z sześciu fraz rdzeniowych mamy poza TOP20 w organiku i z wynikiem jakości 1–3 w Ads**,
a październik to ich szczyt. To jest konkretna treść zdania „jesteśmy za późno".

## 3. Rewizja pozycji zaplanowanych na wrzesień

| pozycja | plan | co mówi pomiar | werdykt |
|---|---|---|---|
| **T-078** `/paszarstwo/` 12.09 | opis kategorii | klaster „kreda" w organiku: **463 wyświetlenia, 0 kliknięć**, poz. ważona 10,0. `kreda pastewna` 2 400/mies, rozkład płaski (IX–XI 1 900) | **zostaje**, ale celem jest CTR, nie nowa widoczność |
| **T-085** `/wapno-hydratyzowane/` 20.09 | przepisanie pod frazę | ⚠️ **`wapno gaszone` ma 2 900/mies i IX–X 3 600 — więcej niż `wapno hydratyzowane` (2 400)**; `wapno budowlane` 1 600. My: `wapno hydratyzowane` poz. **34,9** | **zostaje, zakres poszerzyć** o gaszone i budowlane |
| **T-093** `/wapno-do-oczyszczalni/` 20.09 | wchłonięcie poradnika | wszystkie frazy osadowe **poniżej progu w DFS**; w GSC 202 wyświetlenia, **0 kliknięć**, poz. 13,9 | **zostaje jako konsolidacja**, nie jako pogoń za wolumenem |
| **T-074** spoke ziemniaki 20.09 | nowy spoke | `wapno pod ziemniaki` **50/mies** (IX–X 110); w GSC **0 fraz, 0 wyświetleń**; `/wapno-pod-ziemniaki/` oddaje **404** — czyli nowy adres, a nowe adresy to Faza 2 warunkowana kontrolą 15.09 | **do przesunięcia** — najsłabszy kandydat w całej kolejce |
| **T-077** poradnik kreda 30.09 | nowy poradnik | `kreda pastewna dla kur` 1 600, `kreda dla kur` 720 (**XI 1 000**), rozkład płaski | **zostaje**, termin bez zmian |
| **T-080** pH 20.10 | nowy poradnik | `ph gleby` 1 000, szczyt **IV 1 600**; w GSC **1 wyświetlenie** | zostaje, ale to robota pod wiosnę |
| **T-081** badanie gleby 31.10 | nowy poradnik | ⚠️ **`badanie gleby` ma IX 1 300 — wrzesień wyżej od średniej 1 000**; termin 31.10 wypada po szczycie | **termin do przesunięcia w przód**, nie w tył |

## 4. Wizytówka Google — najskuteczniejszy kanał kontaktowy, jaki mamy

Pomiar GBP Performance, **01.06–05.09 (97 dni)**, wizytówka Tarnów:

| metryka | wynik |
|---|---|
| wyświetlenia razem | **1 810** (mobile search 1 353 = **75%**) |
| **kliknięcia „zadzwoń"** | **31** |
| prośby o trasę dojazdu | **138** |
| kliknięcia w stronę | 15 |
| wiadomości / rezerwacje | 0 (kanały wyłączone) |

**Zestawienie, które ustawia priorytet:** kampania Ads za **1 158 zł** dała **1 kliknięcie typu CALLS**
i 2 formularze. Wizytówka **za 0 zł** dała **31 kliknięć telefonu** i 138 nawigacji do magazynu.

### Czego na wizytówce nie ma (stan 07.09)

| pole | stan |
|---|---|
| **atrybuty** | **0 ustawionych** — w tym niewykorzystane `has_delivery` (mamy własny transport), `url_whatsapp` (WhatsApp jest na stronie), `url_youtube`, `url_facebook`, `url_appointment` |
| **obszar obsługi** (`serviceArea`) | **puste** — przy dostawach w promieniu 150 km to pole stworzone dla tej firmy |
| **publikacje** | 4 sztuki, **wszystkie z 20.08** — 18 dni ciszy |
| **opinie** | 9 opinii, średnia **4,3**, wszystkie z odpowiedzią — ale **najnowsza z lutego 2025**, czyli **19 miesięcy bez nowej** |
| **zdjęcia** | 10, wszystkie wgrane 02.07, tylko 2 zewnętrzne i 8 „dodatkowych" — brak produktu, magazynu, transportu (T-050 czeka na materiał od AGRII) |
| **telefon** | `14 621 88 21` (stacjonarny) — w Ads rotujemy komórki Pawła i Kazimierza; brak numerów dodatkowych |
| godziny | pn–pt 8:00–16:00, brak sobót i brak `moreHours` typu „Dostawa" |
| kategorie | **dobrze**: główna „Dostawca nawozów" + 3 dodatkowe (hurtownia rolna, chemia rolnicza, materiały budowlane) |
| opis | 662 z 750 znaków, treściwy, wymienia Niedomice i Radgoszcz |

### Trzy wizytówki czy jedna — rozstrzygnięcie

**W Mapach nie ma opcji „jedna wizytówka na trzy lokalizacje".** Google wiąże pinezkę z fizycznym
adresem, a ranking lokalny liczy **odległość użytkownika od pinezki**. Rolnik pod Dąbrową Tarnowską
szukający w Mapach widzi Radgoszcz (ok. 7 km), a Tarnowa (ok. 30 km) może nie zobaczyć wcale.
Przy 138 prośbach o trasę na jednej wizytówce trzy pinezki to trzykrotnie większa powierzchnia,
na której w ogóle istniejemy.

⚠️ **Ale rozwarstwienia marki da się uniknąć — hierarchią, nie rezygnacją:**

1. **Tarnów zostaje jedyną wizytówką „firmową"** — pełna nazwa `AGRIA Sp. z o.o. — Wapna Nawozowe`,
   pełny opis, wszystkie publikacje, wszystkie zdjęcia, **i to na nią kierujemy prośby o opinie**.
2. **Niedomice i Radgoszcz jako magazyny, nie jako firmy** — nazwa `AGRIA Sp. z o.o. — Magazyn
   Niedomice`, ten sam telefon i ta sama strona, opis krótki i odsyłający do centrali, kategoria
   główna ta sama. Wtedy w Mapach są punktami odbioru towaru, a nie trzema konkurującymi firmami.
3. **Jedna grupa lokalizacji** w koncie GBP — jedno zarządzanie, spójne dane, jeden zrzut.
4. **Ryzyko realne jest jedno: rozproszenie opinii.** Dlatego prośby o opinię zawsze na Tarnów.
   Kanibalizacji rankingowej między własnymi pinezkami w Mapach nie ma — Google pokazuje najbliższą.

⚠️ **Czego wizytówki NIE zrobią:** nie zbudują ruchu z lokalnych fraz. Pomiar DFS 07.09:
`wapno nawozowe tarnów`, `wapno tarnów`, `hurtownia nawozów tarnów`, `wapno nawozowe niedomice`,
`wapno radgoszcz`, `wapno nawozowe w pobliżu` — **wszystkie poniżej progu**, jedyne `nawozy tarnów`
ma **10/mies**. Wartość wizytówek leży w Mapach i w panelu wiedzy przy zapytaniach o firmę
i przy przeglądaniu okolicy, **nie w klasycznym SEO lokalnym**.

---

## 5. Lista zadań — do wyboru pod „zbuduj prompt do…"

Kolejność w grupach = kolejność wartości. `[nowe]` = pozycja założona 07.09.

### A. CTR — ruch, który już mamy (najwyższy zwrot, zero czekania na Google)

| ID | Hasło | Co to jest |
|---|---|---|
| **T-097** | Schema `offers` na 19 kartach | Karty emitują `Product` bez `offers`, więc w SERP pełnym sklepów nasz wynik nie pokazuje ceny. 15 kart ma kwotę w treści, z której da się zbudować `offers` ręcznie — bez dotykania `_price`. |
| **T-116** `[nowe]` | Title i description kart wg wzorca Oxyfertil | `oxyfertil-90` ma CTR **6,05%**, `weglanowe-odmiana-04` **0,97%** przy lepszej pozycji — różnicę robi nazwa własna w tytule. Przepisanie tytułów i opisów 10 kart pod wzorzec, który w tym samym serwisie już działa. |
| **T-117** `[nowe]` | Dwie karty granulowane przed szczytem X | `weglanowe-granulowane` ma 569 wyświetleń i **1 kliknięcie** (poz. 19,1), `weglanowe-magnez-granulowane` 355 i **zero** (poz. 26,1). Obie na frazach, które w październiku szczytują (`wapno granulowane` 8 100, `wapno magnezowe` 3 600). |
| **T-094** | Osiem kart poza indeksem | Osiem z dziewiętnastu kart ma werdykt „URL unknown to Google" — nie istnieją w wyszukiwarce mimo obecności w sitemapie. Wejście przez linkowanie ze stron crawlowanych, wzorem Fazy 0. |

### B. Treść — rewizja planu wrześniowego

| ID | Hasło | Co to jest |
|---|---|---|
| **T-078** | Opis kategorii `/paszarstwo/` | Klaster kredowy ma **463 wyświetlenia i zero kliknięć** przy pozycji ważonej 10,0, `kreda pastewna` to 2 400/mies. Termin 12.09 bez zmian, ale celem jest zamiana istniejących wyświetleń na wejścia, nie budowa nowych. |
| **T-085+** `[zakres]` | `/wapno-hydratyzowane/` **plus gaszone i budowlane** | Pomiar 07.09: `wapno gaszone` ma **2 900/mies i IX–X 3 600**, więcej niż `wapno hydratyzowane` (2 400), a `wapno budowlane` 1 600 — plan celował tylko w jedną z trzech fraz. Stoimy na **34,9**, więc jest cały zapas. |
| **T-093** | `/wapno-do-oczyszczalni/` — konsolidacja | 202 wyświetlenia, zero kliknięć, pozycja 13,9; wszystkie frazy osadowe poniżej progu w planerze. Robimy jako porządek w intencji, nie jako pogoń za wolumenem. |
| **T-077** | Poradnik o kredzie pastewnej | `kreda pastewna dla kur` 1 600, `kreda dla kur` 720 ze szczytem listopadowym 1 000, rozkład płaski cały rok. Termin 30.09 bez zmian. |
| **T-118** `[nowe]` | Badanie gleby — termin do przodu, nie do tyłu | `badanie gleby` ma **IX 1 300** wobec średniej 1 000, a plan stawia to na 31.10, czyli po szczycie. Góra lejka, karmi kalkulator i wszystkie strony dawkowe. |
| **T-074** `[przesunąć]` | Spoke ziemniaki — odłożyć | 50 wyszukań miesięcznie, zero wyświetleń w GSC, adres oddaje **404**, czyli byłby nowym URL-em przed kontrolą 15.09. Najsłabszy kandydat w całej kolejce wrześniowej. |

### C. Wizytówka Google — kanał, który dowozi telefony za darmo

| ID | Hasło | Co to jest |
|---|---|---|
| **T-119** `[nowe]` | Atrybuty wizytówki — dziś zero | Profil ma **0 ustawionych atrybutów**, a kategoria udostępnia m.in. „Dostawa", WhatsApp, YouTube, Facebook i link do umówienia. Każdy z nich to widoczny element w panelu i sygnał dla Map. |
| **T-120** `[nowe]` | Obszar obsługi | Pole `serviceArea` jest **puste**, choć firma dowozi całosamochodowo w promieniu 150 km. To pole wprost odpowiada temu, jak ta firma działa, i wchodzi do dopasowania w Mapach. |
| **T-121** `[nowe]` | Publikacje cykliczne | Ostatnie cztery posty są z **20.08** — 18 dni ciszy na kanale, który dał 31 telefonów w kwartał. Rytm tygodniowy oparty na tym, co już mamy: kalkulator, atesty, terminarz, ceny. |
| **T-122** `[nowe]` | Opinie — 19 miesięcy bez nowej | Najnowsza opinia jest z **lutego 2025**, przy średniej 4,3 z dziewięciu. Świeżość opinii to jeden z mocniejszych czynników rankingu w Mapach, a AGRIA ma stałych odbiorców, których da się poprosić. |
| **T-123** `[nowe]` | Telefon i godziny dostaw | Wizytówka podaje stacjonarny `14 621 88 21`, podczas gdy w Ads rotujemy komórki Pawła i Kazimierza; numerów dodatkowych brak. Do tego `moreHours` typu „Dostawa" i decyzja o sobotach. |
| **T-124** `[nowe]` | Architektura trzech wizytówek | Tarnów zostaje jedyną wizytówką firmową i jedynym celem próśb o opinie, Niedomice i Radgoszcz wchodzą jako **magazyny** z tym samym telefonem i stroną. Zdejmuje ryzyko rozwarstwienia marki, zachowując trzy pinezki w Mapach. |
| **T-047** | Odzysk profili oddziałów | Czeka od 15.07 na dostęp — Request access z konta Auranet plus weryfikacja własności. Bez tego T-124 nie ma czego porządkować. |
| **T-050** | Zdjęcia na wizytówkę | Dziesięć kadrów z 02.07, z czego osiem „dodatkowych" i ani jednego produktu, magazynu czy transportu. Materiał musi przyjść od AGRII — zastępników nie generujemy. |

### D. Ads — przed wznowieniem 14.09 i po nim

| ID | Hasło | Co to jest |
|---|---|---|
| **T-113** | Jakość landingów — przed 14.09 | `post_click_quality_score` jest „poniżej średniej" na **34 z 37 fraz**, a przy MANUAL_CPC to podnosi nam CPC na wszystkim naraz. Wchodzi razem z T-031, T-063, T-112 i T-059 jako jedna robota, nie pięć osobnych. |
| **T-112** | Cena „od 36 zł/t" na najdroższym landingu | `/wapno-nawozowe/` zjadło **485,60 zł** i otwiera się kwotą, którą własne `FAKTY_KLIENTA` trzymają w sekcji „anomalie do potwierdzenia". Pytanie do Pawła: czy prawdziwa i jakiej formy dotyczy. |
| **T-114** | Stawki Paszarstwa i Marki | Obie kampanie tracą **~50% wyświetleń przez ranking**, nie przez budżet, przy CPC 1,17 i 1,40 wobec 1,95 w Rolnictwie. Przy wznowieniu 14.09 to tańszy ruch niż dokładanie do Rolnictwa. |
| **T-125** `[nowe]` | Auction Insights na markę | Tracimy połowę wyświetleń na własną nazwę przy wyniku jakości 8–10, czego API nie tłumaczy — trzeba zobaczyć w panelu, kto tam licytuje. Bez tego nie wiadomo, czy T-114 na Marce ma sens. |
| **T-111** | Godziny emisji wobec godzin biura | **58,6% budżetu** wychodzi przy zamkniętym biurze, a po przejściu na niedziele — 61,3%. Decyzja: albo emisja bliżej godzin pracy, albo formularz jako główna ścieżka w weekend. |
| **T-110** | Konwersja główna na `form_submit` | `generate_lead` odpala się raz na 32 wysłania, a to on jest w Ads główną konwersją formularzową. Wartość wyłącznie raportowa — przy MANUAL_CPC nie zmienia licytacji. |

### E. Technika, która wchodzi do powyższych

| ID | Hasło | Co to jest |
|---|---|---|
| **T-031** | LCP mobile 7,4 s | Hero waży 686 KB przy **90,5% ruchu mobilnego**, a szybkość jest składową oceny strony docelowej w Ads. Przestaje być osobną pozycją o wydajności — wchodzi jako część T-113. |
| **T-059** | Lekki formularz „oddzwonimy" | Dzisiejszy formularz wymaga wyboru produktu z dwudziestu opcji, a to on jest jedynym realnie działającym kanałem (**37 rozpoczęć → 32 wysłania**). Wariant callback na landingach ruchu płatnego. |
| **T-063** | Landingi na wzorcu zamiast surowego HTML | Trzy landingi to nadal surowy HTML w `post_content` przykryty modułem-łatką z 21.08. Przyczyna nie została usunięta, tylko zasłonięta. |
| **T-108** | Kalkulator czyta CaO+MgO dolomitu jako CaO | Slug niesie sumę, nie samą zawartość wapnia, więc dawka dla dolomitu wychodzi zaniżona. Wykryte przy T-044, nietknięte. |

---

## 6. Poprawka po crawlu Screaming Frog (07.09, wieczór)

Pełny raport: `docs/audits/2026-09-07-CRAWL_SCREAMING_FROG.md`. Crawl 228 adresów z podpiętym GSC
**zmienia hierarchię z sekcji 5** — grupa A dostaje nową pozycję pierwszą, a jedna teza z T-116 upada.

**`/wapnowanie-gleby/` zbiera 63% wyświetleń całego serwisu** (20 106 z 32 047) i oddaje **120 kliknięć
przy CTR 0,60%**. Brakuje tam **~483 kliknięć miesięcznie** — przy 410, które cały serwis robi dziś.
Wszystkie karty produktowe razem to ~57 brakujących kliknięć, czyli jedna dziesiąta tego.

**Przyczyna sprawdzona w SERP-ie, nie zgadnięta** (DFS 07.09, mobile): nad wynikami organicznymi stoi
**AI Overview** (cytujący m.in. `agria.pl`), **video** i **people also ask**. Jesteśmy trzecim wynikiem
organicznym i jesteśmy w źródłach AI Overview — a kliknięć nie ma, bo pytanie zostaje rozstrzygnięte
nad wynikami. To wyjaśnia, czemu T-053 nie dało efektu: problem nie jest w snippecie.

| ID | Hasło | Co to jest |
|---|---|---|
| **T-126** `[nowe]` | Hub `/wapnowanie-gleby/` — oś zakupowa zamiast walki o CTR | Największy zasób ruchu w serwisie stoi na zapytaniach, które AI Overview rozstrzyga za nas, więc podnoszenie CTR na nich jest walką z formatem SERP-a. Kierunek: przechwycić z tego ruchu intencję zakupową i przekierować ją na strony ofertowe, oraz mierzyć obecność w AI Overview jako osobny cel. |
| **T-127** `[nowe]` | Trzy adresy 404 znalezione crawlem | `/polityka-prywatnosci/` oddaje **404**, mimo że to strona wymagana prawnie i linkowana; `/rolnictwo` też 404; na stronie kontaktu adres e-mail Pawła wstawiono jako link **względny**, przez co powstał adres `/kontakt/pawel.bigos@agria.pl`. Trzy drobne naprawy, jedna z nich formalna. |
| **T-128** `[nowe]` | 1,7 MB obrazów bez ani jednego użycia | Pięć plików (trzy kredy pastewnej po 402–479 KB, dwa Agrobielika) leży w uploadach z zerem odwołań. Do usunięcia albo do wykorzystania na kartach, które dziś nie mają zdjęcia produktu. |

⚠️ **Korekta T-116:** teza, że różnicę w CTR robi **długość tytułu**, nie potwierdziła się. Dla stron
z ≥100 wyświetleń tytuły <45 znaków dają CTR **1,01%**, a ≥45 znaków **1,16%** — różnica w szumie.
Zadanie zostaje, ale przed przepisaniem kart trzeba obejrzeć ich SERP-y, tak jak zrobiliśmy dla huba.

⚠️ **Potwierdzone bez zastrzeżeń:** **19 z 19 kart** ma ten sam błąd walidacji —
`Either 'review', 'aggregateRating' or 'offers' is required`. T-097 stoi.
