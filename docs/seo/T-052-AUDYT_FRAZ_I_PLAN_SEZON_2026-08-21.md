# T-052 — audyt fraz od nowa i plan treści pod sezon

> **Data:** 2026-08-21 · **Zakres:** SEO organiczne, AGRIA · **Zastępuje:** `docs/audits/KEYWORD_RESEARCH_2026-05-19.md`
> **Wszystkie liczby z 21.08.2026:** DataForSEO (`keyword_suggestions`, `google_ads/search_volume`, `serp/organic/live`,
> PL/pl, location 2616), GSC Search Analytics API (24.07–20.08), Google Ads API v25 (14–20.08), MCP `agria` `query_db`
> na produkcji. Nie z dokumentów.

---

## 0. Sprostowanie do wcześniejszej wersji tej diagnozy

Napisałem „od 9 lipca nie opublikowaliśmy ani jednej treści". **To jest nieprawda** i tak nie wolno tego stawiać.
Prawdą jest węższe zdanie: **od 9 lipca nie powstał ani jeden nowy artykuł poradnikowy.** Zapis z bazy
(`post_modified >= 2026-07-09`, 30 rekordów):

| Data | Co | Status |
|---|---|---|
| 14.07 | `/wapno-do-stabilizacji-gruntow/` — nowa strona | opublikowana, w indeksie, w sitemapie |
| 15.07 | 4 karty produktów — parametry z kart producentów, wszystkie 4 warstwy | wdrożone |
| 06.08 | `/wapno-granulowane/` — landing | opublikowany, `noindex` (decyzja ADR 11.08) |
| 13.08 | 2 strony prawne (Complianz) | opublikowane |
| 14.08 | `/wapno-nawozowe/` — landing | opublikowany, `noindex` |
| 19.08 | 15 kart produktów + 2 landingi + hub — sekcje cenowe i nagłówki H2 (T-010/T-011) | wdrożone |
| 19.08 | `/do-pobrania/` — atesty i karty Nordkalk (T-008/T-009) | wdrożone |

Czyli ~20 adresów tkniętych w sześć tygodni. Zero **nowych artykułów** — i to jest realny problem,
bo artykuł to jedyna klasa strony, którą ta domena umie dziś wypozycjonować.

---

## 1. Co dokładnie było źle w audycie z 19.05 — trzy błędy, każdy sprawdzalny

### Błąd 1 — filtr tematyczny wyciął najważniejszy klaster

`KEYWORD_RESEARCH_2026-05-19.md`, metodyka pkt 4: fraza wchodziła do zbioru tylko, jeśli pasowała do
`wapn|kreda|agrobielik|ekograncali|bielik|tlenkow|węglanow|magnezow|hydrat|kruszyw|dolomit|cement|caco3|cao|mgo|osad|higieniz|nawóz|odkwasz`.

Frazy, które **nie zawierają słowa „wapno" ani „kreda"** i przez to nie miały prawa się w audycie pojawić
(wolumeny PL, pomiar 21.08):

| Fraza | Wyszukań/mies. |
|---|---|
| ph gleby | 1 000 |
| badanie gleby | 1 000 |
| zakwaszenie gleby | 390 |
| odczyn gleby | 260 |
| analiza gleby | 260 |
| stacja chemiczno-rolnicza | 260 |
| jak podnieść ph gleby | 210 |
| próbki gleby | 170 |
| gleba kwaśna | 90 |

**Razem ~3 640 wyszukań miesięcznie skasowanych mechanicznie.** To jest dokładnie ten klaster, o którym
w ADR z 11.08 sam napisałem, że **Polcalc zbudował na nim 95% swojej widoczności** (122 frazy w TOP10,
wolumen 71 010). Trzy miesiące po tym, jak własny filtr go usunął.

### Błąd 2 — seedy nie pokrywały tego, co AGRIA sprzedaje

Seedy: `wapno nawozowe`, `wapnowanie stawu`, `higienizacja osadów`, `wapno hydratyzowane`, `kruszywo wapienne`.
Nie ma seeda na paszarstwo ani na kredę. Skutek:

| Klaster | Audyt 19.05 | Pomiar 21.08 | Rozjazd |
|---|---|---|---|
| Paszarstwo / hodowla | 2 frazy, **150**/mies. | 82 frazy, **8 940**/mies. | **×60** |
| Rybactwo / stawy | 10 fraz, **240**/mies. | 42 frazy, **4 100**/mies. | **×17** |
| Pole / uprawa | brak klastra | 45 fraz, **1 890**/mies. | — |
| Termin zabiegu | brak klastra | 18 fraz, **1 400**/mies. | — |
| Tonaż / luz / big-bag | brak klastra | 32 frazy, **2 210**/mies. | — |

Największa pojedyncza fraza w całym portfelu produktowym AGRII to **„kreda pastewna" — 2 400/mies.**,
plus „kreda pastewna dla kur" 1 600, „wapno dla kur" 1 000, „kreda dla kur" 720. AGRIA ma ten produkt
(#307, AGR-015) i to on ma **najwyższy skok marży w całym cenniku: 190 zł/t luzem → 610 zł/t w workach 30 kg
(+221%)**. W kampanii Google Ads mamy dziś `pastewna`, `kury`, `drób` **na liście wykluczeń**.

Druga: **„kreda do stawu" — 1 600/mies.** Nie pojawiła się w żadnym z trzech audytów, mimo że seed
„wapnowanie stawu" był użyty — bo `keyword_suggestions` na „wapnowanie stawu" nie zwraca fraz z „kredą".

### Błąd 3 — 82% zmierzonego wolumenu opisywało rynki, na których AGRIA nie gra

| Klaster audytu 19.05 | Wolumen | Status |
|---|---|---|
| Drogownictwo (kruszywo, stabilizacja) | 14 040 (65%) | AGRIA **nie sprzedaje kruszyw** — `CATALOG_VS_WC_GAP`, oferta handlowa ich nie wymienia |
| Budownictwo (wapno hydratyzowane) | 3 670 (17%) | detal DIY — castorama, leroy, obi, bricomarche, mrówka, allegro. Sami wykluczyliśmy ten segment w Ads 13.08 |
| Rolnictwo | 3 240 (15%) | częściowo trafny, ale zbudowany z wariantów jednej frazy head + marek detalicznych (florovit, castorama, allegro) |

Na tej podstawie w raporcie czerwcowym **napisaliśmy klientowi, że największy potencjał to
„wapno hydratyzowane (budownictwo, ok. 2 400 wyszukań)"** — a dwa miesiące później wykluczyliśmy
ten segment z reklam jako niewłaściwy. Kasjan i Paweł dostali priorytet, którego sami potem nie uznaliśmy.

### Czego audyt nie pomylił

Klaster dawkowy („ile wapna na hektar") był w audycie i został dowieziony — to on odpowiada dziś
za całą widoczność domeny. Kalkulator jest z nim spięty poprawnie: **10 linków do `/kalkulator-wapnowania/`
z każdego z trzech artykułów dawkowych** plus 27–32 linki do kategorii i kart produktów. Struktura
linkowania nie jest problemem.

---

## 2. Gdzie naprawdę stoimy — dane z produkcji

### Widoczność organiczna, 24.07–20.08

| Miara | Wartość |
|---|---|
| Wyświetlenia | 19 395 (czerwiec 2 821 → lipiec 10 220 → sierpień 1–20: 15 709) |
| Kliknięcia | 264 |
| CTR | **1,36%** (czerwiec 2,23% → sierpień 1,26%) |
| Stron z jakąkolwiek widocznością | **38** |
| Z tego jedna strona `/wapnowanie-gleby/` | **14 227 wyświetleń, 69 kliknięć, poz. 6,7** |

**Wyświetlenia rosną siedmiokrotnie, kliknięcia stoją.** Cała widoczność siedzi w jednym klastrze
informacyjnym o CTR poniżej 1%: „ile wapna na hektar" 1 219 wyświetleń → **1 kliknięcie**,
„ile wapna granulowanego na hektar" 1 170 → 2, „wapno granulowane ile na ha" 168 → 0.

W SERP na „ile wapna na hektar" (desktop, 21.08) jesteśmy **5. organicznie**, nad nami polcalc.pl,
distripark, farmer.pl i topagrar.pl. Nasz tytuł: „Ile wapna na hektar? Dawki CaO i dobór wapna" —
„CaO" w tytule wyniku dla rolnika nie sprzedaje kliknięcia.

### Czego nie ma w GSC w ogóle

| Klaster | Wyświetlenia 28 dni |
|---|---|
| staw / rybactwo | **0** |
| ph gleby / badanie gleby | **0** |
| kreda pastewna dla kur / bydła | poza progiem |
| rzepak, zboża ozime, ściernisko | 4 wyświetlenia łącznie |

### Dlaczego — stan katalogu na produkcji

| Kategoria | Produktów |
|---|---|
| Rolnictwo — wapno nawozowe | 15 |
| Budownictwo / Oczyszczalnie / Paszarstwo / Kreda malarska | po 1 |
| **Rybactwo — wapno do stawów** | **0** |
| **Sadownictwo** | **0** |
| **Hurtownie** | **0** |

Trzy kategorie segmentowe są puste, ich pozycje zdjęto z menu 30.07, a landingi, które miały je zastąpić
(T-036), zostały unieważnione 11.08. Nic ich nie zastąpiło.

### Frazy tonażowe — tu akurat wygrywamy

GSC 28 dni, pozycje na frazach z językiem B2B:

| Fraza | Pozycja |
|---|---|
| wapno granulowane cena | 2,0 |
| wapno luzem cena | 2,0 |
| cena wapna na pole | 2,0 |
| wapno cena za tonę | 2,3 |
| wapno granulowane big bag cena | 2,5 |
| wapno na pole cena za tonę | 2,7 |

**Na języku „luz / tona / big-bag" jesteśmy w TOP3.** Problem nie polega na tym, że nie rankujemy
na frazy całosamochodowe — polega na tym, że tych fraz jest mało (2 210/mies. łącznie) i nikt nie
zaczyna od nich ścieżki zakupowej. Rolnik zaczyna od „ile wapna na hektar", „jakie wapno na pole",
„kiedy wapnować", „badanie gleby" — a kończy na „cena za tonę", gdzie już jesteśmy drugą pozycją.
**Brakuje nam góry lejka, nie dołu.**

---

## 3. Nowa mapa fraz — 28 720 wyszukań/mies. realnego popytu

Po odrzuceniu detalu ogrodowego, DIY, marketplace'ów, medycznych („wapno na uczulenie") i miejscowości
Wapno w Wielkopolsce.

| # | Klaster | Fraz | Wolumen/mies. | Nasze pokrycie dziś |
|---|---|---|---|---|
| 1 | **Paszarstwo / hodowla** | 82 | **8 940** | 1 karta, poz. 9,2, brak treści |
| 2 | **Gleba / odczyn** | 57 | **6 320** | 0 na frazach head, sekcje wewnątrz huba |
| 3 | **Staw / rybactwo** | 42 | **4 100** | **0** — kategoria pusta |
| 4 | **Dawka (rolnicza)** | 36 | 3 360 | pełne, CTR 0,5% |
| 5 | **Tonaż / luz / big-bag** | 32 | 2 210 | TOP3, wolumen wyczerpany |
| 6 | **Pole / uprawa** | 45 | **1 890** | **0** |
| 7 | **Termin zabiegu** | 18 | **1 400** (szczyt X) | sekcja w hubie |
| 8 | Sad / drzewa owocowe | 9 | 470 | 0 — kategoria pusta |
| 9 | Oczyszczalnie | 1 | 30 | 1 artykuł, poz. 13,6–17,3 |

**Trzy klastry o łącznym wolumenie 14 330/mies. mają dziś zerowe pokrycie: paszarstwo (częściowo),
staw, pole/uprawa.**

### Jak to się ma do „sprzedajemy całosamochodowo, luzem, w tonach"

Zapytań z językiem tonażowym jest 2 210/mies. i **już je mamy**. Filtr profesjonalista/hobbysta
nie może siedzieć w doborze fraz, bo frazy „dla dużych" nie mają wolumenu — musi siedzieć
w **treści**. Klastry 1, 3, 6, 7 są z natury polowe i towarowe:

- „wapno na pole", „jakie wapno na pole", „wapno na pole luzem", „czy można siać wapno na zboże",
  „kiedy siać wapno pod zboża ozime", „wapno pod ziemniaki", „wapno na łąki" — nikt nie pyta tak
  o 5 kg na trawnik,
- „kreda pastewna dla bydła", „kreda pastewna dla kur niosek dawkowanie" — ferma, nie kurnik na 6 kur,
- „wapnowanie zarybionego stawu", „wapno tlenkowe do stawu", „ile wapna do stawu" — gospodarstwo
  rybackie i łowisko, nie oczko wodne.

**Rozdział wewnątrz klastrów:** „kreda do stawu" (1 600) i „kreda pastewna dla kur" (1 600) mają
w SERP-ach paczki 5–10 kg z Allegro. Wchodzimy w nie **językiem parametru i tonażu** (Ca %, frakcja,
big-bag 500/1000 kg, worek 30 kg, luz 24 t) — kto szuka paczki 5 kg, odbije się sam.

---

## 4. Korekta ADR 11.08 — reguła była czytana za szeroko

ADR mówi: **nie dokładamy drugiego własnego URL-a na frazę, na której już coś rankujemy.**
Dowód (6 URL-i na „wapno bielik" → poz. 15,3; frazy z jednym URL-em w TOP10) jest poprawny i zostaje.

Ale reguła została w praktyce rozciągnięta na „nie budujemy stron" — i to jest błąd. Dla fraz,
na których mamy **zero URL-i** (staw, kreda pastewna, wapno na pole, badanie gleby, kiedy wapnować),
kanibalizacja nie istnieje, bo nie ma czego kanibalizować.

**Rozstrzygnięcie:**

| Frazy | Reguła |
|---|---|
| `wapno nawozowe`, `wapno granulowane`, `wapno bielik`, `wapno węglanowe`, `wapno tlenkowe` — mamy 1+ URL | ADR obowiązuje. Landingi Ads zostają `noindex`. Bez nowych stron |
| `staw`, `kreda pastewna`, `wapno na pole`, `ph gleby`, `badanie gleby`, `kiedy wapnować`, `sad` — **0 URL-i** | ADR nie ma zastosowania. Budujemy pierwszy URL na intencję |

Zasada operacyjna: **jedna intencja = jeden URL**, sprawdzana przed publikacją zapytaniem GSC
query×page. Nie „nie budujemy stron".

---

## 5. Plan wykonania — 21.08 → 31.10

Zegar: nowa strona potrzebuje w Google 2–6 tygodni. **Drugi szczyt sezonu to październik**
(„wapno granulowane" 8 100, „wapno palone" 3 600, „kiedy wapnować glebę" 590, „kiedy wapnować pole" 260).
Wszystko, co ma pracować w październiku, musi być opublikowane **do 20 września**.

### Blok A — 21–24.08 · naprawa CTR na tym, co już mamy (0 nowych stron)

14 227 wyświetleń przy 69 kliknięciach. Podniesienie CTR z 0,5% do 2% to **+200 wejść/mies.**
bez ani jednej nowej treści — najtańszy ruch w całym projekcie.

| Co | Gdzie |
|---|---|
| Przepisanie `title` i `description` pod kliknięcie (liczba, dawka, konkret zamiast „CaO") | `/wapnowanie-gleby/`, `/ile-wapna-granulowanego-na-ha/`, `/jak-stosowac-wapno-nawozowe/`, `/kalkulator-wapnowania/` |
| Tabela dawek jako pierwszy element treści (pod snippet i AI Overview) | j.w. |

**Dowód domknięcia:** CTR tych 4 URL-i w GSC po 14 dniach, porównanie do baseline 24.07–20.08.

### Blok B — 25.08–05.09 · paszarstwo (8 940/mies.)

Największy klaster, popyt płaski cały rok, produkt o najwyższej marży, SERP wygrywalny
(na „kreda pastewna" #4 to Holcim stroną z parametrami).

| # | Co | Cel |
|---|---|---|
| B1 | Karta #307 „Kreda pastewna" — parametry (Ca %, frakcja, wilgotność), formy dostawy, H2 cenowe | `kreda pastewna` 2 400 |
| B2 | Opis kategorii `/paszarstwo/` + przypisanie produktów | `kreda pastewna dla bydła` 210, `wapno dla kur niosek` 210 |
| B3 | Poradnik „Kreda pastewna — dawkowanie dla niosek, bydła i trzody" | `kreda pastewna dla kur` 1 600, `…jak podawać` 170, `…dawkowanie` 90 |
| B4 | Wycofanie `pastewna`/`kury`/`drób` z wykluczeń Ads → osobna grupa reklam | patrz T-053 |

⚠️ **Do rozstrzygnięcia przez Janka:** karta #307 opisuje dziś kredę pastewną parametrami wapna
tlenkowego (reakcja egzotermiczna, pH >12 — węglan tego nie robi). Zgłoszone w `FAKTY_KLIENTA` §9,
niezamknięte. Bez poprawnych parametrów nie publikujemy B1.

### Blok C — 01–15.09 · pole, uprawa, termin (3 290/mies., szczyt X)

To jest klaster rolnika całosamochodowego.

| # | Co | Cel |
|---|---|---|
| C1 | Poradnik „Jakie wapno na pole — dobór do gleby i uprawy" | `wapno na pole` 390, `jakie wapno na pole` 140, `wapno na pole luzem` 40, `gdzie kupić wapno na pole` 30 |
| C2 | Poradnik „Kiedy wapnować glebę i pole — terminarz zabiegu" | `kiedy wapnować glebę` 320 (**X: 590**), `kiedy siać wapno granulowane` 420, `kiedy wapnować pole` 90 (**X: 260**) |
| C3 | Sekcje uprawowe wewnątrz C1/C2, nie osobne URL-e | `czy można siać wapno na zboże` 90, `wapno pod ziemniaki` 100, `wapno na łąki` 100, `kiedy siać wapno pod zboża ozime` 30, `wapno pod rzepak` 20 (**VIII: 140**) |

**C2 musi być opublikowany do 05.09**, żeby zdążył na październikowy szczyt.

### Blok D — 05–20.09 · staw i rybactwo (4 100/mies.)

Zobowiązanie wobec Kasjana z maila 06.08: *„wrzesień — treści pod sezon jesienny w oczyszczalniach
i rybactwie"*. SERP jest pusty merytorycznie — **na „wapno do stawu" trzy z siedmiu wyników TOP7
to posty z Facebooka**.

| # | Co | Cel |
|---|---|---|
| D1 | Kategoria `/wapno-do-stawow/` — przypisanie produktów (#320 palone mielone, #310/#311 tlenkowe, #305/#306 kreda) + opis | `wapno do stawu` 390, `jakie wapno do stawu` 90 |
| D2 | Poradnik „Wapnowanie stawu — jakie wapno, ile i kiedy" (przebudowa marcowego wpisu, **ten sam URL**, nie drugi) | `wapnowanie stawu` 90, `ile wapna do stawu` 50, `wapnowanie zarybionego stawu` 30, `kiedy sypać wapno do stawu` 50 |
| D3 | Poradnik „Kreda do stawu — dawkowanie i różnica wobec wapna tlenkowego" | `kreda do stawu` 1 600, `kreda do stawu rybnego` 260, `kreda do stawu z rybami` 140 |
| D4 | Powrót pozycji „Rybactwo" do menu (dług z 30.07) | — |

### Blok E — 15–30.09 · gleba i odczyn (6 320/mies.)

Droga, którą Polcalc zbudował 95% widoczności. Góra lejka, karmi wszystko poniżej.

| # | Co | Cel |
|---|---|---|
| E1 | Poradnik „Badanie gleby — jak pobrać próbki i odczytać wynik ze stacji chemiczno-rolniczej" | `badanie gleby` 1 000, `analiza gleby` 260, `stacja chemiczno-rolnicza` 260, `próbki gleby` 170 |
| E2 | Poradnik „pH i odczyn gleby — jak go podnieść" | `ph gleby` 1 000, `zakwaszenie gleby` 390, `odczyn gleby` 260, `jak podnieść ph gleby` 210, `gleba kwaśna` 90 |
| E3 | Strona tonażowa na pustej kategorii `/wapno-nawozowe-hurt/` | `wapno granulowane big bag` 260 + `…cena` 260, `wapno … cena za tonę` 490 łącznie |

### Blok F — październik · zgodnie z mailem do Kasjana

Stabilizacja gruntów i budownictwo + rozszerzenie kampanii o wapno palone (szczyt X 3 600)
+ podsumowanie trzech miesięcy reklam.

---

## 6. Nazewnictwo produktów

Dziś 15 z 19 kart nazywa się językiem rozporządzenia: „Wapno nawozowe węglanowe bez magnezu — Odmiana 04".
Wolumen frazy „wapno nawozowe odmiana 04" — 10/mies. Fraza „wapno węglanowe" — 319 wyświetleń w GSC
na pozycji 14,9.

**Problem nie jest głównie w nazwach — jest w tym, że żaden produkt nie jest przypisany do zastosowania.**
Nikt nie szuka „odmiany 04"; szukają „wapna na pole", „wapna do stawu", „kredy pastewnej dla kur".
Kolejność napraw: najpierw przypisanie produktów do kategorii segmentowych (Blok B2, D1), potem
uzupełnienie tytułów o zastosowanie i formę, **bez zmiany URL-i** (adresy migrowaliśmy 08.07, drugi
raz w sezonie nie ruszamy).

---

## 7. Co to zmienia w zobowiązaniach wobec klienta

Sprawdzone w mailach faktycznie wysłanych na `biuro@aseosystem.pl` (Kasjan) i `pawel.bigos@agria.pl`:

| Mail | Data | Co obiecane |
|---|---|---|
| Oferta | 25.05 | opieka 2 000/mies., plan M1–M6 w PDF |
| Raport czerwiec | 03.07 | *„każdy miesiąc to stały zestaw: 4 artykuły eksperckie + rozwój strony + wizytówka + raport"*; wrzesień = oczyszczalnie i stawy rybne; październik = stabilizacja gruntów i budownictwo |
| Raport lipiec | 03.08 | sierpień = Ads, dociśnięcie treści do indeksu, szybkość mobile, wizytówka. Setup Ads (8–10 h) *„przesunie część zaplanowanych na sierpień prac na wrzesień"* — **które konkretnie, nigdy nie ustalono** |
| Plan 3-miesięczny | **06.08, wysłany** | 3 800 zł/mies. VIII–X; wrzesień = treści pod oczyszczalnie i rybactwo; październik = stabilizacja gruntów i budownictwo + podsumowanie |

**Bilans sierpnia wobec tego, co klient dostał na piśmie:** konto i pomiar ✅, landingi ✅,
start 14.08 ✅, wizytówka Tarnów ✅ (T-046), ceny na kartach ✅, OLX ✅ (osobna pozycja),
**szybkość mobile ❌** (LCP 7,3 s, T-031 otwarte), **dociśnięcie treści do indeksu ⚠️**
(T-026 zdiagnozowane, nierozstrzygnięte).

Zobowiązanie „4 artykuły miesięcznie" pochodzi z raportu czerwcowego i **nie zostało powtórzone
w mailu sierpniowym** — ale też nigdy nie zostało odwołane. W lipcu dowieziono 4, w sierpniu 0.

**Wrzesień jest przeładowany:** stawy i oczyszczalnie (obietnica z 06.08) + przesunięte prace
z sierpnia + bloki C, D, E z tego planu + prowadzenie kampanii. Do decyzji Janka, co z tego wypada.

---

## 8. Jak to zweryfikować

| Miernik | Baseline 21.08 | Próg |
|---|---|---|
| CTR 4 URL-i klastra dawkowego | 0,49% | ≥1,5% do 10.09 |
| Wyświetlenia GSC na frazach z „staw" | **0** | ≥300/mies. do 31.10 |
| Wyświetlenia na „kreda pastewna" i pochodnych | poniżej progu | ≥500/mies. do 31.10 |
| Wyświetlenia na „wapno na pole" i pochodnych | 0 | ≥200/mies. do 31.10 |
| Stron z widocznością w GSC | 38 | ≥50 do 31.10 |
| Kliknięcia organiczne / mies. | 264 (28 dni) | ≥450 w październiku |

Pomiar odtwarzalny: `python3 scripts/seo_baseline.py` + pull GSC 28-dniowy.
