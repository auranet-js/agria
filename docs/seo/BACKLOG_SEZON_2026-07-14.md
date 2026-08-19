# BACKLOG — kampania sezonowa 2026 (wapnowanie pożniwne)

> **STATUS: CZĘŚCIOWO UNIEWAŻNIONY (2026-08-19).** **Bloki C4–C7, D1–D4 i E1–E3 są zdjęte z zakresu**
> przez ADR `docs/decyzje/2026-08-11-podzial-rol-ads-seo.md` — landingi organiczne nie powstają,
> bo zmierzono kanibalizację. C2 i C3 powstały, ale jako cele Ads poza indeksem, nie jako strony
> organiczne. Bloki A i B są w większości wykonane (weryfikacja na produkcji 19.08). Nadal ważne:
> rozstrzygnięcie MOQ, granica profesjonalista/hobbysta, parametry normowe Bielika, lista pytań F.
> Aktualny stan zobowiązań: `docs/REJESTR_ZOBOWIAZAN.md`.

> Data: 2026-07-14. Kontekst: `ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md`.
> **Zegar:** szczyt sezonu = sierpień–październik. Rozgrzanie nowej strony w Google = 2–6 tygodni. Nasza własna oferta dla AGRIA mówi: *„treści przygotowujemy z wyprzedzeniem ok. 6 tygodni przed szczytem sezonu"*. Dziś mamy 14 lipca — **jesteśmy po terminie, który sami wyznaczyliśmy.**
> Źródło parametrów produktowych: `Agria-katalog-2026-05-13-druk.pdf` (Drive).

---

## Zasada przewodnia — kogo odsiewamy i czym

### Źródła (dwa, o różnym statusie)

- **`Agria-katalog-2026-05-04/13-web.pdf`** (Auranet + AGRIA) — **wzorzec komunikacji marketingowej.** Stąd bierzemy ton, strukturę argumentu, hierarchię korzyści.
- **`Oferta Handlowa wapno (3).pdf`** (surowa, pisana przez AGRIA) — **wyłącznie źródło faktów handlowych.** NIE wzorzec komunikacji. Stąd bierzemy: co sprzedają, komu, w jakich formach, z jakich magazynów.

### Rozstrzygnięcie sporu o MOQ

Katalog, strona „Współpracuj z nami":
> Model **producent–klient** + wybrane hurtownie · **długoterminowe kontrakty** · **MOQ: worek / big-bag / 24 t** · terminy 14/30/60 dni B2B · pilne dostawy 24–48 h · dostawa cała Polska 2–5 dni · rozładunek HDS/wywrotka · **przetargi i kontrakty roczne** · doradztwo techniczne · własna flota 3–24 t

**MOQ jest *elastyczne*, nie *duże*.** Paweł (STR-02) nie kwestionował sprzedaży wolumenowej — kwestionował **sztywny zapis, który zamyka drogę mniejszym zamówieniom**. Miał rację.

### Korekta kluczowa: granica NIE przebiega „hurt vs detal"

Oferta handlowa AGRIA mówi wprost:
> „Oferujemy **sprzedaż hurtową i detaliczną**… **Detal** – małe, lokalne zamówienia: rolnicy indywidualni, sadownicy, małe gospodarstwa rybackie. **Hurt** – większe zamówienia: duże gospodarstwa, oczyszczalnie, hurtownie."

W cenniku są worki 20 / 25 / 40 kg sprzedawane na sztuki. **AGRIA sprzedaje detalicznie — rolnikom.**

Granica, której faktycznie pilnujemy, to **profesjonalista vs hobbysta**:
- ✅ rolnik indywidualny z workiem 40 kg — **klient**,
- ✅ oczyszczalnia, gospodarstwo 200 ha, hurtownia — **klient**,
- ❌ działkowiec sypiący 5 kg na trawnik — **nie klient**.

**Narzędziem odsiewu jest JĘZYK, nie tonaż.** Landing mówiący *pH, CaO, MgO, reaktywność, dawka t/ha, analiza gleby, frakcja* odrzuca hobbystę sam z siebie i zatrzymuje małego rolnika. Landing mówiący *„zazieleni trawnik"* robi dokładnie odwrotnie.

→ Dlatego poradnik `/wapno-nawozowe-na-trawnik/` jest błędem (F6), a worki 20–40 kg na karcie produktu **błędem nie są**.

### Wniosek operacyjny

Na stronę wraca **sygnał logistyczny jako atut**, nie MOQ jako bariera:
- „Dostępne: **luz 24 t / big-bag 1000 kg / worek 25 kg**" — możliwości, nie wymóg,
- własna flota (3 t / 5 t / 12 t / 24 t + kurier), magazyny, terminy płatności, przetargi, doradztwo,
- CTA **„zapytaj o ofertę — podaj tonaż"** zamiast koszyka.

---

## Segmenty odkryte w ofercie handlowej (brak w katalogu i w planie SEO)

Sekcja „Klienci uzupełniający" wymienia odbiorców, na których **nie mamy ani jednej treści**, a są to dokładnie ci „poważni klienci":

- jednostki samorządu terytorialnego i podmioty komunalne,
- **firmy rekultywacyjne** — grunty zdegradowane, tereny poprzemysłowe,
- **firmy usługowe wapnowania** i rekultywacji gleb (usługi agrotechniczne),
- zarządcy zbiorników retencyjnych i **łowisk komercyjnych**,
- spółdzielnie i grupy producenckie (rolne, sadownicze, ekologiczne),
- przedsiębiorstwa gospodarki osadami i odpadami,
- zarządcy dużych terenów zielonych (parki, ośrodki).

→ Kandydaci na landingi segmentowe po sezonie (BLOK E+). Wymaga keyword researchu — wolumeny nieznane.

**Rozbieżność do odnotowania:** oferta handlowa **nie wymienia** cementu, kruszyw, drogownictwa, budownictwa ani paszarstwa. Katalog marketingowy je dodaje. Potwierdza to decyzję z `CATALOG_VS_WC_GAP` (AGRIA nie sprzedaje drogowych/kruszyw) i **podważa** obecność budownictwa/drogownictwa jako segmentów w planie SEO. **Do potwierdzenia u Pawła.**

---

## Dane wrażliwe — NIE do repo

Oferta handlowa zawiera **pełny cennik netto** (per produkt × forma dostawy × magazyn). **Nie commitujemy cen do repo, nie wystawiamy na auratest, nie publikujemy na stronie.** Landingi operują wyłącznie CTA „zapytaj o ofertę".

Do zgłoszenia klientowi: pozycja „Wapno hydratyzowane Bielik, worki 25 kg — **1245/SZT**" — niemal na pewno literówka (12,45).

---

## BLOK A — odblokowanie techniczne (P0, zero ryzyka, dni 1–2)

| # | Task | Dlaczego teraz |
|---|---|---|
| **A1** | **Odświeżyć sitemapę RankMath** | `product-sitemap.xml` zawiera 19 produktów pod **starymi URL-ami** (`/wapno-nawozowe-hurt/…`, `/wapno-do-sadu/…`) — czyli 301-kami od 08.07. Karmimy Google mapą przekierowań i palimy crawl budget w szczycie sezonu. **Najpilniejsze zadanie w całym backlogu.** |
| **A2** | `product_cat` do sitemapy | Kategorie = przyszłe landingi. Dziś `category-sitemap.xml` zawiera wyłącznie `/category/poradniki/`. Canonicale są poprawne (self-canonical) — problem jest tylko w zgłaszaniu. |
| **A3** | Usunąć `/cart/` z sitemapy | Śmieć indeksacyjny. |
| **A4** | Re-submit URL przez `~/bin/index-submit` | 19 nowych URL produktów + kategorie. **Uwaga: budżet dzienny 100 ad-hoc** (wspólna pula, patrz global CLAUDE.md §10a) — rozłożyć, pokazać stan przed. |
| **A5** | Duplikacja `/category/poradniki/` vs `/poradniki/` | Kanibalizacja własnych poradników — jedynego, co dziś rankuje. |

---

## BLOK B — on-page zaległy (P0, dni 2–5)

Wszystko poniżej miało status P0 w `ONPAGE_PLAN` z 20.05 i nie zostało tknięte.

| # | Task | Fraza / powód |
|---|---|---|
| **B1** | **Meta title + description na 6 stronach statycznych** | RankMath ma dane **wyłącznie na stronie głównej**. `/kalkulator-wapnowania/` rankuje **#20 bez ani jednego tagu** (`wapń skorygowany kalkulator` 390, `ile wapna na ha` 590) — najtańszy możliwy zysk w całym projekcie. Dalej: `/oferta/`, `/o-firmie/`, `/poradniki/`, `/do-pobrania/`, `/kontakt/`. |
| **B2** | **Bielik #309 on-page** | `wapno hydratyzowane` **2 400** — największa pojedyncza fraza portfolio. Blokada: rozstrzygnąć **72% vs 90% CaO** (patrz F2). |
| **B3** | **Dolomit #302 on-page** | `dolomit` **6 600**. Do tej pory zmieniliśmy mu wyłącznie URL. |
| **B4** | Literówki w 8 nazwach produktów = H1 | `weglanowe` → `węglanowe`, `zawierajace` → `zawierające`. H1 z literówką na produkcie B2B. |
| **B5** | SKU dla 19 produktów | Wszystkie `sku = null`. Mapping gotowy w `PRODUCT_DATA_MAPPING.md`. Warunek schema `Product/Offer`. |
| **B6** | Fix `pa_agria-ph` #320 = „>16" | **Fizycznie niemożliwe** (skala pH kończy się na 14). Ten sam błąd jest w katalogu drukowanym — patrz F3. |
| **B7** | „35 lat" → „37 lat" (meta #307/#319) | Firma od 1989. Błąd także w katalogu. |

---

## BLOK C — landingi komercyjne (RDZEŃ, pod szczyt sierpniowy)

**To jest brakujące ogniwo.** agria.pl rankuje w top-50 na 6 fraz i wszystkie są poradnikowe. Zero stron komercyjnych. Biovita ma słabszy profil linków od nas (181 vs **339** backlinków) i rankuje na 109 fraz — bo ma landingi produktowe.

### Szablon landingu (jednolity dla C1–C7)

1. **H1 exact-match** z frazą (`Wapno nawozowe granulowane`), title + meta desc.
2. **Tabela parametrów** — prosto z katalogu: CaO, MgO, reaktywność, typ reakcji, frakcja, dawkowanie, szybkość działania, producent.
3. **Formy dostawy jako atut** — luz 24 t / big-bag 1000 kg / worek 25 kg (per produkt wg katalogu).
4. **Blok logistyczny** — własna flota 3–24 t, magazyny (Niedomice, Radgoszcz + producenckie), dostawa 2–5 dni, pilne 24–48 h, rozładunek HDS/wywrotka.
5. **Blok B2B** — przetargi i kontrakty roczne, dokumentacja techniczna, terminy 14/30/60 dni, doradztwo przy doborze.
6. **CTA: „Zapytaj o ofertę — podaj tonaż"**. Bez ceny, bez koszyka. *(Dowód, że to działa: Biovita jest #1 na „wapno nawozowe" stroną bez ceny, bez kosztu, bez H1 i bez schema.)*
7. **Schema** `Product` + `Offer` (`priceSpecification` = „na zapytanie").
8. **Linkowanie** → kalkulator wapnowania + poradniki (hub-and-spoke wykorzystujący to, co JUŻ rankuje).

### Lista landingów wg wolumenu × szczyt sezonowy

| # | Landing | vol/mies. | szczyt | uwaga |
|---|---|---|---|---|
| ~~**C1**~~ | ~~`/wapno-do-stabilizacji-gruntow/`~~ | 720 | — | ✅ **WDROŻONY 2026-07-14** — strona ID **2745**, HTTP 200, H1 + 7×H2 + tabela parametrów + FAQ, meta RankMath, w sitemapie, zgłoszony do indeksacji. **Parametry wzięte z karty Nordkalk, NIE z draftu**: draft mówił „min. 90% CaO", karta CL 90-Q (R5, P1) mówi **CaO+MgO ≥90%, wapno czynne ≥80%, reaktywność R5** — mocniejszy, normowy język pod specyfikacje robót drogowych. Dawkowanie 2–4% wagowych za katalogiem AGRIA + zastrzeżenie projektowe. **TODO:** linkowanie wewnętrzne (z karty #320 i z /oferta/), schema FAQPage, decyzja o miejscu w nawigacji. |
| **C2** | `/wapno-granulowane/` | **5 400** | **14 800** (sie) | Największy wolumen w portfolio. AGRIA ma: węglanowe granulowane, węglanowe z Mg granulowane, kreda granulowana. |
| **C3** | `/wapno-nawozowe/` | 1 300 | 6 600 (sie) | **Tu stoi Biovita #1.** Fraza-flagowiec segmentu. |
| **C4** | `/wapno-palone/` | 2 400 | 9 900 (paź) | AGRIA ma wapno palone mielone wysokoreaktywne (90% CaO). |
| **C5** | `/wapno-magnezowe/` | 2 400 | 8 100 (sie) | AGRIA ma 4 produkty z MgO. |
| **C6** | `/wapno-hydratyzowane/` | 2 400 | — | Kategoria istnieje — rozbudować do formatu filarowego (Bielik). |
| **C7** | `/kreda-nawozowa/` | 1 000 | 3 600 (mar) | Granulowana + sypka. Niższy priorytet — szczyt wiosenny. |

**Kolejność pod sezon:** C1 (gotowe) → C2 → C3 → C4 → C5 → C6 → C7.

---

## BLOK D — sygnał wolumenowy B2B (dni 5–10)

Dziś na agria.pl **nie ma ani jednego sygnału**, że AGRIA wozi luzem 24 t własną flotą. STR-02 usunęła ostatni.

| # | Task |
|---|---|
| **D1** | Strona **`/transport-i-dostawa/`** — flota **3 t / 5 t / 12 t / 24 t + wysyłka kurierska**, magazyny Niedomice + Radgoszcz + producenckie w całej PL, dostawa 2–5 dni, pilne 24–48 h, rozładunek HDS/wywrotka. Formy dostawy wg oferty handlowej: **luz w beczkach (do silosu) lub w wannach (na pole)**, big-bagi samochodami z plandeką/firanką. To jest konkret, którego nie ma żaden konkurent — a my go nie pokazujemy. |
| **D2** | Sekcja **„Współpraca B2B"** — przetargi i kontrakty roczne, dokumentacja techniczna pod postępowania, terminy płatności 14/30/60 dni, doradztwo przy doborze wapna. Wprost z katalogu. |
| **D3** | **Formularz zapytania ofertowego** z polami: segment, **tonaż**, forma dostawy, lokalizacja. To jest mechanizm segregacji intencji — nie fraza. |
| **D4** | **Formy dostawy z powrotem na 19 kart** — jako atut („dostępne: luz 24 t / big-bag / worek"), **nie** jako MOQ. Uzgodnić z Pawłem (F1). |

---

## BLOK E — segmenty (po szczycie rolniczym / równolegle)

| # | Task |
|---|---|
| **E1** | `/wapno-do-stawow/` — landing rybacki. Własna strategia z 08.07 nazywa to „wysoka szansa (luka)" — SERP to YouTube i fora. Dziś: 301 → `/oferta/`. |
| **E2** | `/wapno-do-sadu/` — landing sadowniczy (fraza 30/mies., rankowała #11 zanim ją przekierowaliśmy). |
| **E3** | Hub **Oczyszczalnie** — istniejący post `/higienizacja-osadow-sciekowych-wapnem/` podpiąć do menu i huba segmentowego (dziś wisi poza nawigacją). |

### Rozstrzygnięcie starych 301 (`.htaccess` linie 25–27)

Obecny stan jest zły **nie dlatego, że przekierowaliśmy, tylko dlatego, że przekierowaliśmy w generyczną `/oferta/`** — to rozmywa sygnał tematyczny i gwarantuje utratę pozycji.

**Rekomendacja:** przepiąć 301 na **tematycznie zbieżne** landingi, gdy tylko powstaną:
- `/wapno-nawozowe-hurt/` → **`/wapno-nawozowe/`** (C3) — *nie* odtwarzamy archiwum; fraza „hurt" ma zerowy wolumen, ale URL ma link equity i pozycję do przeniesienia,
- `/wapno-do-sadu/` → **`/wapno-do-sadu/`** landing (E2),
- `/wapno-do-stawow/` → **`/wapno-do-stawow/`** landing (E1).

---

## BLOK F — do decyzji (Janek / Paweł / dział techniczny)

| # | Sprawa |
|---|---|
| **F1** | **Paweł:** przywrócenie form dostawy na kartach jako atutu, nie MOQ (D4). Argument: nic nie zamyka, a dziś strona milczy o Waszej największej przewadze — własnej flocie i dostawach całopojazdowych. |
| **F2** | ~~Bielik — 72% czy 90% CaO?~~ **ROZSTRZYGNIĘTE 2026-07-14 kartą producenta** (Nordkalk, PN-EN 459-1). Patrz sekcja „Bielik — parametry normowe" niżej. **Nie blokuje B2.** Zostaje jedno pytanie: **skąd w WooCommerce wzięło się „min. 72% CaO"** — brak pokrycia w karcie. |
| **F7** | **Paweł: czy budownictwo i drogownictwo to realne segmenty?** Oferta handlowa AGRIA (ich własna) **nie wymienia** cementu, kruszyw, budownictwa ani paszarstwa — wymienia wyłącznie rolników/sadowników, gospodarstwa rybackie, oczyszczalnie i hurtownie. Katalog marketingowy je dodaje. Jeśli nie sprzedają — wypada segment z planu SEO i z kafli na `/oferta/`. |
| **F8** | **Cennik** (oferta handlowa) — co z nim robimy? Nie idzie do repo ani na stronę. Przydatny wyłącznie wewnętrznie (np. przy Google Ads i przy ocenie, które produkty warto pozycjonować pod marżę). |
| **F3** | **Katalog + WC: „Odczyn pH >16"** (wapno palone mielone) — skala pH kończy się na 14. Błąd w druku i w bazie. |
| **F4** | **Katalog: Kreda pastewna — „pH >12, reakcja egzotermiczna"** — kreda to węglan wapnia, nie jest egzotermiczna i nie daje pH >12. Parametry najwyraźniej skopiowane z karty wapna tlenkowego. |
| **F5** | **Katalog: „35 lat na rynku"** (dwa miejsca) — od 1989 to 37 lat. |
| **F6** | **Poradnik `/wapno-nawozowe-na-trawnik/`** — fraza wykluczona przez nasz własny plan jako lifestyle/detal, opublikowana 09.07. Zostawiamy (ruch to ruch) czy wycofujemy jako niezgodną z pozycjonowaniem B2B? |

---

## Bielik — parametry normowe (rozstrzygnięte kartą producenta)

Źródło: **Nordkalk Wapno sp. z o.o., Karta produktu „Bielik", Wapno budowlane EN 459-1 CL 90-S**, zakład Sitkówka. Deklaracja Właściwości Użytkowych 3/S/24, oznakowanie CE, certyfikat ZKP 1487-CPR-226-01 (ICiMB Kraków). Aktualizacja karty: 2024-11-04.

| Właściwość (PN-EN 459-1) | Wymaganie normowe | Deklarowane |
|---|---|---|
| **CaO + MgO** | ≥ 90 % | **≥ 90 %** |
| MgO | ≤ 5 % | ≤ 5 % |
| SO₃ | ≤ 2 % | ≤ 2 % |
| CO₂ | ≤ 4 % | ≤ 4 % |
| **Wapno czynne** | ≥ 80 % | **≥ 80 %** |
| Wolna woda | ≤ 2 % | ≤ 2 % |
| Odsiew 90 µm / 200 µm | ≤ 7 % / ≤ 2 % | ≤ 7 % / ≤ 2 % |
| Gęstość nasypowa | — | 0,41 kg/dm³ |

### Ustalenia

1. **Liczba „90" jest prawidłowa** i ma pokrycie w certyfikowanej karcie. Katalog jej nie zmyślił.
2. **Błąd jest w ETYKIECIE parametru, nie w wartości.** Katalog pisze „Zawartość CaO — min. 90% CaO"; producent deklaruje **CaO + MgO ≥ 90%**. To inne pole. Poprawny zapis: **„CaO + MgO ≥ 90% (PN-EN 459-1, klasa CL 90-S)"**.
3. **„min. 72% CaO" w WooCommerce nie ma źródła** w karcie producenta — wartość niewiadomego pochodzenia. **Do wyjaśnienia i najpewniej do zastąpienia** parametrami normowymi.
4. **Dodać „wapno czynne ≥ 80%"** — parametr kluczowy dla oczyszczalni (specyfikacje przetargowe), dziś nieobecny nigdzie.
5. **Klasa CL 90-S + norma PN-EN 459-1** to mocny sygnał pod przetargi — silniejszy niż jakikolwiek procent bez kontekstu. Wyeksponować na landingu.
6. **Zastosowania wg karty** (rozszerzają landing): zaprawy murarskie i tynkarskie, betony, farby wapienne, przemysł chemiczny, **ochrona środowiska**, drogownictwo, **uzdatnianie wody do spożycia**.
7. Konfekcja wg karty: **worki papierowe 25 kg na paletach (foliowane) + luz** na środki transportowe.

*Uwaga procesowa: moja pierwotna diagnoza („90% chemicznie niemożliwe dla Ca(OH)₂") była BŁĘDNA — liczyłem CaO w produkcie z wodą związaną, podczas gdy EN 459-1 definiuje parametr inaczej. Skorygowane po przedstawieniu karty przez Janka (2026-07-14). Wniosek na przyszłość: parametry produktowe bierzemy z kart producentów, nie z rozumowania.*

---

## Co z tego jest w zakresie oferty M2/M3

Oferta dla AGRIA (maj 2026) obiecuje w **M2 (lipiec)**: *„Optymalizacja on-page: kategoria Rolnictwo + karty produktów wapna nawozowego (tytuły, opisy, nagłówki)"* oraz *„Struktura pod SEO — porządkujemy adresy i powiązania między stronami"*.

→ **Bloki A, B i C mieszczą się w tym, co już sprzedaliśmy.** 4 artykuły M2 są dowiezione (4/4). On-page i struktura — nie. Bloki D i E wchodzą w M3 (sierpień: *„kategorie Rybactwo i Sadownictwo + powiązane produkty"*).

Nie jest to rozszerzanie zakresu. To jest jego nadrobienie.
