# Pomiar przed T-116 — SERP-y i stan indeksu, 09.09.2026

> Wykonane jako krok 1 i 2 z promptu bloku 1 (`docs/prompty/wdrozenie/2026-09-14-BLOK-1-tresc-i-kontrole.md` §2).
> Źródła: GSC URL Inspection (19 kart, 09.09), GSC Search Analytics 09.08–05.09 (28 dni, dane dojrzałe),
> DataForSEO SERP live/advanced, `location_code 2616`, `language_code pl`, mobile o ile nie zaznaczono.
> Dane surowe: `data/seo/2026-09-09-serp-*.json`.

---

## 1. Kart poza indeksem jest CZTERY, nie osiem

Stan z T-094 (24.08) się zdezaktualizował. URL Inspection 09.09 dla wszystkich 19 kart:

| poza indeksem 09.09 | stan |
|---|---|
| `/wapno-nawozowe-rolnictwo/agrobielik-90/` (#311) | URL unknown to Google |
| `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` (#316) | URL unknown to Google |
| `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-04/` (#318) | URL unknown to Google |
| `/wapno-do-oczyszczalni/wapno-palone-mielone/` (#320) | URL unknown to Google |

**Weszły do indeksu od 24.08 same, bez zgłoszenia do Indexing API:** `kreda-czarna-jeziorna` (#303,
crawl 04.09), `kreda-nawozowa-sypka` (#306, 29.08), `mieszanka-tlenkowo-weglanowa` (#308, 28.08)
i **`dolomit` (#302, crawl 09.09 — dzisiaj)**. Cztery z ośmiu w dwa tygodnie.

To jest **sygnał wyprzedzający dla kontroli 15.09**: mechanizm wchodzenia do indeksu działa i nie
wymaga Indexing API. Kontroli 15.09 to nie zastępuje — tam pytanie dotyczy czterech innych adresów
(Faza 0), nie kart.

## 2. Baseline GSC 19 kart, 28 dni (09.08–05.09)

| karta | wyśw | klik | CTR | poz |
|---|---|---|---|---|
| `weglanowe-odmiana-04` | **1 105** | 10 | 0,90% | 7,7 |
| `weglanowe-granulowane` | 511 | 1 | 0,20% | 18,9 |
| `bielik` | 495 | 11 | 2,22% | 7,2 |
| `weglanowe-magnez-odmiana-05` | 459 | 8 | 1,74% | 11,0 |
| `weglanowe-magnez-granulowane` | 387 | **0** | 0,00% | 25,5 |
| `wapno-tlenkowe-magnez` | 372 | 2 | 0,54% | 13,6 |
| `kreda-nawozowa-granulowana` | 352 | 4 | 1,14% | 9,4 |
| `oxyfertil-90` | 331 | **17** | **5,14%** | 5,8 |
| `kreda-pastewna` | 203 | 1 | 0,49% | 8,6 |
| `agrobielik-70` | 174 | **9** | **5,17%** | 6,3 |
| `kreda-malarska` | 159 | 3 | 1,89% | 6,7 |
| `kreda-nawozowa-sypka` | 79 | 2 | 2,53% | 7,3 |
| pozostałe 7 | ≤2 | 0 | — | — |

## 3. Co pokazały SERP-y — teza „nazwa własna w tytule" wymaga przeformułowania

Obejrzane frazy (mobile): `wapno węglanowe`, `wapno granulowane`, `wapno magnezowe`,
`wapno nawozowe tlenkowe`, `wapno tlenkowo magnezowe`, `kreda malarska`,
`kreda nawozowa granulowana cena`, `oxyfertil`, `wapno bielik`, `wapno hydratyzowane`,
`wapno gaszone`. Plus `wapno węglanowe` na desktopie, `depth 30`.

**Gdzie AGRIA fizycznie stoi w wynikach, licząc pozycje bezwzględne (z blokami Google):**

| fraza | AI Overview | pierwszy wynik organiczny | AGRIA |
|---|---|---|---|
| `oxyfertil` | tak | OLX (abs 2) | **abs 7** — CTR karty 5,14% |
| `wapno tlenkowo magnezowe` | nie | OLX (abs 1) | abs 11 |
| `wapno bielik` | tak | Allegro (abs 2) | abs 19 |
| `wapno nawozowe tlenkowe` | tak | OLX (abs 2) | abs 19 |
| `wapno węglanowe` | tak | OLX (abs 2) | **poza abs 24 (mobile) i poza abs 30 (desktop)** |
| `wapno magnezowe` | tak | OLX (abs 2) | poza abs 20 |
| `wapno granulowane` | nie | Rolmat (abs 1) | poza abs 20 |
| `kreda malarska` | — | (abs 5) | poza abs 20 |
| `kreda nawozowa granulowana cena` | nie, ale **5 × blok produktowy** | OLX (abs 1) | poza abs 20 |
| `wapno hydratyzowane` | **nie** | epicentra.pl (abs 1) | poza abs 20 |
| `wapno gaszone` | tak | Castorama (abs 2) | poza abs 20 |

**Wniosek:** różnicy między `oxyfertil-90` (CTR 6,05%) a `weglanowe-odmiana-04` (0,97%) **nie robi
brzmienie tytułu, tylko miejsce w wynikach** — abs 7 kontra kilkanaście pozycji niżej, pod AI Overview,
pod OLX-em, pod „ludzie pytają też" i pod blokiem obrazów. Hipoteza o nazwie własnej broni się
w innym ujęciu: **na frazę brandową w ogóle wchodzimy wysoko**, bo konkurencja jest płytka; na frazę
generyczną nie wchodzimy, bo SERP jest pełen sklepów i OLX-a.

To jest ta sama diagnoza, która unieważniła T-053 na hubie: przy takim otoczeniu SERP-u
**przepisanie meta nie ma czego podnieść.** Dźwignią jest pozycja (treść, T-117), nie tytuł.

⚠️ **Rozjazd wart odnotowania:** GSC podaje dla `weglanowe-odmiana-04` na frazie `wapno węglanowe`
średnią pozycję 10,0 z 561 wyświetleń w 28 dniach, a pomiar na żywo 09.09 nie znajduje agria.pl
ani w 24 wynikach mobile, ani w 30 na desktopie. Nie wiadomo, czy to spadek z ostatnich dni,
czy różnica metody (GSC uśrednia po wariantach frazy i personalizacji). **Niezweryfikowane** —
do rozstrzygnięcia osobnym pomiarem, nie zakładać spadku.

## 4. Co z tego zostaje do zrobienia w T-116

Bezwarunkowo, bez żadnej tezy o CTR:

1. **Duplikat tytułu** — `weglanowe-magnez-granulowane` i `weglanowe-magnez-odmiana-04` mają identyczne
   „Wapno nawozowe węglanowe zawierające magnez | AGRIA". Dwa różne produkty, jeden tytuł.
2. **`weglanowe-magnez-odmiana-05`** — tytuł ~595 px przy progu 561, ucinany w wynikach.

Warunkowo, tam gdzie jesteśmy widoczni i mimo to nie klikani (`kreda-nawozowa-granulowana` poz. 9,4,
`kreda-malarska` poz. 6,7, `weglanowe-odmiana-04` poz. 7,7): przepisanie tytułu ma sens jako **próba
z pomiarem**, nie jako pewnik — z jednym istotnym zastrzeżeniem, że w każdym z tych SERP-ów nad nami
stoi OLX albo blok produktowy z ceną, a nasze karty w wynikach ceny nie pokazują.

## 5. Zauważone obok, nie ruszane

**OLX jest wynikiem organicznym numer 1 albo 2 na `wapno węglanowe`, `wapno magnezowe`,
`wapno tlenkowe`, `wapno granulowane`, `kreda nawozowa granulowana cena` i `kreda malarska`** —
czyli na całym rdzeniu, na którym nasze własne karty nie wchodzą do pierwszej dwudziestki.
AGRIA ma tam 200 aktywnych ogłoszeń od 20.08. **Decyzja o odnowieniu pakietu OLX (T-105) zapada
do 10.09** i ten pomiar jest dla niej argumentem, którego nie było w kalkulacji z 28.08 —
tam liczony był wyłącznie ruch wewnątrz OLX-a, nie widoczność OLX-a w Google.

---

## 6. Przedbieg kontroli 15.09 — cztery adresy Fazy 0, stan 09.09

Odczyt wykonany 6 dni przed terminem, **nie zastępuje kontroli 15.09** — jest wcześniejszym
odczytem tego samego pomiaru.

| adres | 24.08 (audyt) | 09.09 | ostatni crawl |
|---|---|---|---|
| `/wapno-do-stawu/` | URL unknown, **poza sitemapą** | URL unknown | nigdy |
| `/wapno-do-stabilizacji-gruntow/` | URL unknown, **poza sitemapą** | URL unknown | nigdy |
| `/wapno-nawozowe-na-trawnik/` | URL unknown, **poza sitemapą** | URL unknown | nigdy |
| `/jak-stosowac-wapno-nawozowe/` | Discovered – not indexed | Discovered – not indexed | nigdy |

**Żaden z czterech nie został pobrany w 16 dni od T-089/T-090.** Trzy nadal „URL unknown", czwarty
nadal „wykryty, niezindeksowany".

**Przyczyny, które udało się wykluczyć pomiarem (09.09):**

1. **Nie brak linków.** Odnośniki do wszystkich czterech są w **renderze HTML** stron, które Google
   czyta na bieżąco: `/wapnowanie-gleby/` (crawl **09.09**), `/wapno-do-oczyszczalni/` (07.09),
   karta `weglanowe-odmiana-04` (22.08). Sprawdzone `curl`-em po rozgrzewce cache, nie w bazie.
2. **Nie brak w sitemapie.** Dziś wszystkie cztery są w mapach (`post-sitemap.xml` ×2,
   `page-sitemap.xml` ×2) — to zmiana wobec 24.08, kiedy trzy z nich były poza sitemapą.
3. **Nie technika strony.** Crawl kontrolny 08.09: cztery razy `200`, `noindex=false`,
   canonical na siebie, 157–184 KB.

Czyli **mechanizm z Fazy 0 wykonaliśmy poprawnie i on nie zadziałał** — a równolegle, w tym samym
oknie, **cztery karty produktowe weszły do indeksu same** (§1). Różnica między jednymi a drugimi:
karty siedzą w `product-sitemap.xml` i w listingu kategorii, którą Google przechodzi regularnie;
te cztery adresy stoją poza ścieżką, którą robot faktycznie chodzi.

**Dla decyzji 15.09 to jest przesłanka za wariantem „STOP":** nie budujemy nowych adresów, tylko
wzmacniamy te, które Google już czyta. Formalny odczyt i zapis do `data/kontrole/2026-09-15-faza-0-crawl.md`
zostaje na 15.09 — jeśli do tego czasu któryś zostanie pobrany, werdykt się zmieni.

⚠️ **Do rozstrzygnięcia z Jankiem, nie samemu:** ten sam objaw ma `/higienizacja-osadow-sciekowych-wapnem/`
(URL unknown, nigdy niepobrany) — czyli poradnik, którego merytorykę T-093 ma przenieść do kategorii.

---

## 7. Ręczne zgłoszenia w GSC, 09.09 — mechanizm, który zadziałał

Wykonane na polecenie Janka, przez panel Search Console („Poproś o zindeksowanie"), **nie przez
Indexing API** — więc poza pulą 200/dobę z globalnego CLAUDE.md §10a.

**Cztery karty produktowe, zgłoszone jako pierwsze. Wynik po kilkunastu minutach:**

| karta | stan przed | stan po |
|---|---|---|
| `weglanowe-magnez-odmiana-04` | **URL nieznany Google**, „nie wykryto odsyłających map witryn" | **zindeksowana**, crawl 09.09 |
| `wapno-palone-mielone` | wykryta, niezindeksowana | **zindeksowana**, crawl 09.09 |
| `weglanowe-odmiana-05` | wykryta, niezindeksowana | zeskanowana, jeszcze nie zindeksowana, crawl 09.09 |
| `agrobielik-90` | wykryta, niezindeksowana | bez zmiany, brak crawla |

**To jest ustalenie, nie hipoteza: ręczne zgłoszenie działa tam, gdzie nie zadziałało ani linkowanie
(16 dni, T-089/T-090), ani Indexing API (trzy zgłoszenia, T-094).** Wąskim gardłem nie jest to, że
Google odrzuca te strony — tylko to, że sam z siebie po nie nie sięga.

**Następnie zgłoszone (decyzja Janka: „zgłośmy co możemy od razu"):**
`/wapno-do-stawu/` · `/wapno-do-stabilizacji-gruntow/` · `/jak-stosowac-wapno-nawozowe/` ·
`/wapno-nawozowe-na-trawnik/` — komplet Fazy 0 — oraz `/higienizacja-osadow-sciekowych-wapnem/`
(poradnik z T-093, nigdy niepobrany). Wszystkie z potwierdzeniem „Przesłano prośbę o zindeksowanie".

⚠️ **`/kreda-malarska/` NIE zostało zgłoszone — „Przekroczono limit" (dzienny limit GSC).**
Do zgłoszenia jutro, razem z ewentualnym powtórzeniem `agrobielik-90`, jeśli do tego czasu nie wejdzie.
Jeden slot limitu poszedł na niezamierzone ponowne zgłoszenie `/wapno-do-stawu/` — kliknięcie w pasek
inspekcji nie złapało focusu po zmianie rozmiaru okna i Enter powtórzył poprzednie żądanie.
Skutku merytorycznego brak (Google: „ponowne zgłoszenie nie wpływa na pozycję w kolejce"), koszt to
jedno miejsce z dziennej puli.

**Wszystkie zgłoszone adresy mają w panelu „Strona odsyłająca: Nie wykryto"** — mimo że linki są
w renderze stron crawlowanych codziennie. Google nie kojarzy linkowania wewnętrznego na tym serwisie.

⚠️ **Licznik „211 stron niezindeksowanych" sprawdzony i odłożony — to nie jest problem.**
Rozwinięcie raportu „Strony" (09.09): 107 × 404 po migracji, 21 przekierowań własnych, 12 × `noindex`
(landingi Ads), 6 × robots.txt. W grupie „zeskanowana, nie zindeksowana" (44 pozycje) jest 17 feedów RSS,
trzy wersje `wp-emoji-release.min.js`, sześć PDF-ów, `?jsf_ajax=1`, `/wp-json/complianz/v1/`,
`/locations.kml`, stare adresy DuoCMS `/pl/produkt/…` i **demo motywu WooCommerce**
(`organic-pineapple`, `product-category/vegetable`, `product-category/orange/?add-to-cart=`).
Realne strony treściowe: **dwie** — `/gospodarstwa-rybackie/` i `/polityka-plikow-cookies-eu/`.
Serwis ma ~50 adresów w sitemapie, więc licznik mierzy historię i pliki, nie treść.

### Co z tego wynika dla kontroli 15.09

Kontrola w pierwotnej postaci miała odpowiedzieć, czy samo linkowanie wystarcza do wejścia do indeksu.
**Odpowiedź jest już znana i brzmi: nie** — 16 dni bez jednego pobrania, przy poprawnych linkach,
sitemapie i technice. Zgłoszenie ręczne 09.09 zmienia warunki, więc 15.09 **mierzymy co innego**:
czy strony zgłoszone ręcznie faktycznie weszły i utrzymały się w indeksie. Szczegóły w rejestrze.
