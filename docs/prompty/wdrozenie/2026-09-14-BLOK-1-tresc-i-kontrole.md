# Blok 1, wątek treści i kontroli — 14–20.09.2026

> **Projekt:** `agria` · **Zakres:** ryczałt R · **Obejmuje:** kontrola 15.09 · T-116 · T-117 ·
> kontrola 18.09 · T-085 · T-093
> **Kontekst:** `docs/PLAN_WRZESIEN_2026.md` §7 (blok 1, pozycje 11–16)
> **Poprzedni blok:** blok 0 domknięty 08.09, commity `4e49aed`, `dde4107`, `4c73caa`, `383b7d7`, `84f4965`
>
> **Wątek kampanijny (T-125, T-114, T-111) świadomie NIE jest tu opisany** — decyzja Janka 08.09:
> „mnie na razie kampanie nie interesują". Dopisujemy osobno, gdy wróci temat. Budżet (T-109)
> rozstrzyga Janek do 13.09 i dla tego wątku jest wejściem zewnętrznym, nie zadaniem.

---

## 0. Czego NIE zakładać

Dziesięć rzeczy zmierzonych, nie przypuszczanych. Każda już raz kosztowała sesję albo wywróciła tezę.

1. **`?cb=` nie jest narzędziem weryfikacji.** Po WP Rocket omija cache i pokazuje wersję, której
   użytkownik nie dostaje. Każdy pomiar: **rozgrzewka jednym żądaniem, potem pomiar na czystym
   adresie**. Do porównania „z Rocketem / bez" służy `?nowprocket=1` i opisujesz to jako stan bez
   Rocketa, nie jako doświadczenie użytkownika. ADR `2026-09-07-wp-rocket-…` §6 pkt 1.
2. **Inline z danymi w szablonie nie jest chroniony trybem bezpiecznym Rocketa.** Jeśli którakolwiek
   z przepisywanych stron dostanie skrypt wstrzykujący dane (`var cośTamData = {…}`), **wykluczysz
   go z odraczania**, inaczej powtórzysz T-133 — kalkulator przestał działać po wybraniu gruntu,
   bo dane poszły do odroczenia, a plik czyta je na starcie. Sposób sprawdzenia w ADR §6 pkt 2.
3. **WP-CLI `term update` przepuszcza opis przez `wp_filter_kses`** i wycina tabele oraz nagłówki.
   Opisy kategorii zapisujesz **przez MCP `query_db_write`**, po zapisie porównujesz **MD5 z plikiem
   źródłowym**. Pułapka nr 1 z T-092, potwierdzona ponownie przy T-078.
4. **Nie zeruj `_elementor_element_cache` przez `a:0:{}`** — Elementor czyta to jako poprawny pusty
   render i wygasza treść na produkcji (incydent 30.07). Po zmianie: `wp elementor flush-css`.
5. **Karty 307 / 310 / 320 renderują z `_elementor_data`, NIE z `post_content`.** Edycja treści posta
   nic tam nie zmienia. Weryfikuj render, nie bazę.
6. ⚠️ **Teza „krótszy tytuł = lepszy CTR" została ODRZUCONA pomiarem.** Crawl 07.09: tytuły poniżej
   45 znaków dają CTR **1,01%**, 45 znaków i dłuższe **1,16%** — różnica w szumie. **T-116 zaczyna
   od obejrzenia SERP-ów**, nie od liczenia znaków. Skracamy tam, gdzie tytuł się nie mieści, a nie
   po to, żeby podnieść CTR.
7. ⚠️ **Osiem z dziewiętnastu kart jest poza indeksem** (T-094: #302, #303, #306, #308, #311, #316,
   #318, #320). **Przepisanie tytułu karty, której Google nigdy nie pobrał, nie zmieni niczego.**
   Zanim ruszysz dziesięć kart w T-116 — sprawdź URL Inspection, które z nich są w indeksie,
   i zacznij od tych. Reszta czeka na linkowanie (T-094, blok 2), nie na lepszy tytuł.
8. **Szczyt roku dla `wapno granulowane` to SIERPIEŃ, nie październik** — VIII 9 900 wobec X 8 100
   (memory `project_agria_sezon_sierpniowy`). Październik jest szczytem wtórnym. T-117 robimy,
   bo karty są martwe, a nie dlatego, że okno ucieka.
9. **Parametry wyłącznie z kart producentów** (Nordkalk, Lhoist) i rozporządzeń — nigdy z rozumowania.
   17 kart leży publicznie na `/do-pobrania/`. Nazwa własna: `Bielik` to wapno hydratyzowane
   **Nordkalku**, AGRIA jest dystrybutorem, nie producentem.
10. **Nie zakładamy nowych adresów.** Faza 2 jest warunkowana kontrolą 15.09 — jeśli Google nie
    pobrał żadnego adresu z Fazy 0, **wracamy z pytaniem, nie z kolejnymi URL-ami**.

---

## 1. Kontrola 15.09 — warunek wejścia w Fazę 2

**To jest najważniejsza pozycja w całym bloku**, bo rozstrzyga, czy w ogóle wolno nam budować nowe
adresy. Ustalone ADR-em 24.08.

**Pytanie:** czy Google pobrał którykolwiek z adresów odblokowanych w Fazie 0 (zamknięta 24.08)?

Adresy do sprawdzenia — te, które przed 24.08 były sierotami albo miały zerowe linkowanie:

| adres | co zrobiliśmy 24.08 |
|---|---|
| `/wapno-do-stawu/` | linki z wpisu 2079, z huba `/wapnowanie-gleby/` i z sześciu kart listingu (T-089) |
| `/wapno-do-stabilizacji-gruntow/` | linki z karty #320 i z opisu kategorii `/wapno-do-oczyszczalni/` (T-089) |
| `/jak-stosowac-wapno-nawozowe/` | linki + odświeżenie `post_modified` i cache (T-090) |
| `/wapno-nawozowe-na-trawnik/` | jw. (T-090, T-091) |

**Metoda:** GSC URL Inspection API (`scripts/gsc_inspect.py`). Interesuje **`lastCrawlTime`** i werdykt
indeksacji, nie pozycje — pytanie brzmi „czy pobrał", nie „czy rankuje".

⚠️ **Nie mierz tego przez DataForSEO ani przez sprawdzenie, czy strona się otwiera.** Adres może
oddawać 200 i nadal być „URL unknown to Google" — dokładnie tak było przed 24.08.

**Dwa wyjścia i oba są wynikiem, nie porażką:**

- **Choć jeden pobrany** → linkowanie wewnętrzne działa jako mechanizm wejścia do indeksu. Faza 2
  otwarta, ale **z tą samą metodą**: nowy adres wchodzi z linkami z adresów crawlowanych codziennie,
  nie sam.
- **Żaden nie pobrany** → **STOP i wracamy do Janka z pytaniem.** Nie zgłaszamy do Indexing API
  (trzy zgłoszenia już nie zadziałały — T-094), nie budujemy nowych adresów, nie powtarzamy tego
  samego ruchu mocniej. Wtedy blok 2 przestawia się na wzmacnianie tego, co Google już czyta.

Wynik zapisz do `data/kontrole/2026-09-15-faza-0-crawl.md` — z datami ostatniego crawlu per adres
i jednozdaniowym werdyktem.

---

## 2. T-116 — tytuły i opisy kart

**Objaw:** `oxyfertil-90` ma CTR **6,05%**, `weglanowe-odmiana-04` **0,97%** przy lepszej pozycji.
Robocza teza z 03.09 mówiła, że różnicę robi nazwa własna w tytule.

**Co crawl 07.09 z tego zostawił, a co obalił.** Obalił długość tytułu (patrz §0 pkt 6). Zostawił
hipotezę o **nazwie własnej i typie zapytania** — brandowe kontra generyczne. To jest hipoteza,
nie ustalenie, i tak ją traktuj.

**Kolejność pracy:**

1. **Sprawdź, które z dziesięciu kart są w indeksie** (§0 pkt 7). Karty poza indeksem odkładasz.
2. **Obejrzyj SERP-y** dla fraz tych kart — DataForSEO, mobile, `location_code 2616`. Szukasz
   tego samego, co przy hubie: czy nad wynikami stoi AI Overview, PAA albo blok zakupowy, i co
   obiecują w tytułach ci, którzy są nad nami. **Dla huba ten pomiar wyjaśnił wszystko** i był
   powodem, dla którego T-053 nie mogło zadziałać.
3. Dopiero potem przepisujesz tytuły i opisy.

**Dwie rzeczy znalezione crawlem kontrolnym 08.09, które wchodzą tutaj:**

- ⚠️ **Duplikat tytułu na dwóch kartach.** `weglanowe-magnez-granulowane` i `weglanowe-magnez-odmiana-04`
  mają identyczne „Wapno nawozowe węglanowe zawierające magnez | AGRIA". Zgłoszone 07.09, nienaprawione
  — dwie karty konkurują tym samym tytułem. **To jest pierwsza pozycja do poprawy**, bo nie wymaga
  żadnej tezy o CTR: dwa różne produkty muszą mieć różne tytuły.
- `weglanowe-magnez-odmiana-05` ma tytuł ~595 px przy progu 561 — jedyna karta w indeksie ponad progiem.

**Uwaga o zazębieniu:** `weglanowe-magnez-granulowane` jest jednocześnie w T-117. Zrób obie pozycje
w jednym przebiegu na tej karcie, żeby nie zapisywać do niej dwa razy.

---

## 3. T-117 — dwie karty granulowane

| karta | wyświetlenia | kliknięcia | pozycja |
|---|---|---|---|
| `weglanowe-granulowane` | 569 | **1** | 19,1 |
| `weglanowe-magnez-granulowane` | 355 | **0** | 26,1 |

Frazy: `wapno granulowane` **8 100** w październiku (ale szczyt to sierpień, §0 pkt 8),
`wapno magnezowe` **3 600**.

**Dlaczego to jest osobna pozycja od T-116:** tam chodzi o tytuł i opis, tu o **treść karty**.
Obie karty mają wyświetlenia i praktycznie zero kliknięć przy pozycjach 19 i 26 — czyli są widoczne
na tyle, żeby dało się zmierzyć skutek zmiany, i głęboko na tyle, żeby sam tytuł nie wystarczył.

Wzorzec wykonania: T-092 i T-078 — rozbudowa treści z parametrami z kart, tabele, nagłówki
odpowiadające na realne zapytania z GSC. **Zacznij od wyciągnięcia zapytań** dla obu adresów
z ostatnich 28 dni; przy kredzie pastewnej to właśnie ten krok pokazał, że cały klaster pyta
o dawkowanie, a nie o produkt.

---

## 4. Kontrola 18.09 — T-092 po 14 dniach

Opis kategorii `/wapno-nawozowe-rolnictwo/` wdrożony 04.09 (958 → ok. 5 700 znaków).

**Mierz z GSC, nie z DataForSEO** — nowe treści widać tam z opóźnieniem. Baseline:
`data/T-092/baseline-gsc-2026-09-04.json`.

**Mierz frazy formowe klastra**, nie frazę główną: `wapno nawozowe cena`, `wapno nawozowe dawkowanie`,
`ile wapna nawozowego na hektar` i pochodne. Interesuje **CTR i pozycja**, nie sam wolumen.

⚠️ **`lastmod` w `product_cat-sitemap.xml` się nie ruszy** — dla archiwum kategorii bierze się
z produktów, nie z opisu termu. To nie jest błąd i nie jest sygnałem, że zmiana nie weszła.

---

## 5. T-085 — kategoria `/wapno-hydratyzowane/`

**Termin 20.09.** Fraza `wapno hydratyzowane` **2 400** (marzec 3 600). Kategoria **jest
zaindeksowana**, crawl 21.08 — i mimo to stoi na **31,3**.

Rozstrzygnięte ADR-em 24.08: **rozbudowa kategorii, nie nowy landing.**

⚠️ **Inny odbiorca i inny język.** To nie jest rolnik — to budownictwo. Zamiast dawki na hektar
i odczynu gleby: zaprawy, tynki, mleko wapienne, proporcje. Reguła „zero żargonu" obowiązuje dalej,
ale słownik jest inny.

**Do wykorzystania:** `Bielik` = **CL 90-S** (CaO+MgO ≥90%, wapno czynne ≥80%) — produkt Nordkalku,
AGRIA dystrybutorem. Karty na `/do-pobrania/`.

**Największa luka wolumenowa w portfelu siedzi obok:** `wapno gaszone` ma we wrześniu i październiku
**3 600**, a my stoimy na **34,9**. To ta sama substancja pod inną nazwą potoczną — rozbudowa
kategorii ma ją obsłużyć, bez zakładania osobnego adresu.

---

## 6. T-093 — `/wapno-do-oczyszczalni/`

**Termin 20.09.** Ta kategoria ma **najlepszy CTR kategorii w serwisie: 3,97%** (806 wyświetleń,
32 kliknięcia, poz. 9,5), crawl 22.08. Czyli działa — chodzi o to, żeby zebrała **całą** intencję
osadową.

Poradnik `/higienizacja-osadow-sciekowych-wapnem/` ma **zero wyświetleń i nigdy nie został pobrany**.
Jego merytoryka ma pracować w kategorii.

⚠️ **Poradnik zostaje osobnym adresem** — decyzja Janka 24.08. Nie kasujemy, nie przekierowujemy,
nie scalamy. Przenosimy merytorykę, nie adres.

Frazy: `higienizacja osadów ściekowych` 30, `wapnowanie osadów ściekowych` 20. Wolumen jest mały —
**to jest pozycja porządkowa i CTR-owa, nie wolumenowa.** Nie sprzedawaj jej w raporcie jako
źródła ruchu.

---

## 7. Czego w tym wątku nie robisz

- **Nie dotykasz kampanii.** T-125, T-114, T-111 i budżet T-109 są poza tym wątkiem.
- **Nie zakładasz nowych adresów** — patrz §0 pkt 10 i kontrola 15.09.
- **Nie zgłaszasz nic do Indexing API.** Wspólna pula 200/dobę na wszystkie projekty, a przy tych
  kartach trzy zgłoszenia już nie zadziałały. Wejście do indeksu robimy linkowaniem.
- **Nie ruszasz H1 ani struktury listingu produktów** — T-092 i T-078 też ich nie ruszały.
- **Nie zmieniasz cen** ani nie dodajesz drugiej kwoty. Jedna kwota `od X zł/t netto` na kartę,
  zawsze ze swoim warunkiem dostawy.
- **Nie wysyłasz nic do klienta.** Wszystko przez Janka na `js@auranet.com.pl`.

---

## 8. Zrobione =

- **Kontrola 15.09** wykonana i zapisana, z jednoznacznym werdyktem „Faza 2 otwarta / STOP".
- **Backup przed każdą zmianą w bazie** (`db_export`), MD5 po zapisie zgodny z plikiem źródłowym.
- **Render zweryfikowany po rozgrzewce cache**, nie przez `?cb=` i nie odczytem z bazy.
- **Crawl kontrolny przed i po** — `python3 scripts/crawl_kontrolny.py --json data/kontrole/<data>.json`.
  Zero nowych 404, zero nowych duplikatów tytułu, duplikat magnezowy **zniknął**.
- **Baseline GSC zapisany przed każdą zmianą treści** do `data/T-NNN/`, na wzór `data/T-078/`.
- **Kontrole 14-dniowe wpisane w kalendarz „Auranet Claude"** dla każdej wdrożonej pozycji.
- **Wiersze w rejestrze zaktualizowane w tym samym commicie**, z dowodem. Wiersz bez dowodu nie ma
  prawa mieć ✅.

⚠️ **Do naprawienia przy okazji, jeśli nie zrobi tego kto inny:** T-116, T-117 i T-125 **nadal nie
mają wierszy w `docs/REJESTR_ZOBOWIAZAN.md`** — żyją wyłącznie w planie wrześniowym. To ten sam
rozjazd, przez który blok 0 wyglądał na zamknięty, kiedy nie był. Dopisz je, zanim zaczniesz.
