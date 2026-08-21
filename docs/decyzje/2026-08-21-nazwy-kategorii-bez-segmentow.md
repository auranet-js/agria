# ADR 2026-08-21 — nazwy kategorii bez segmentów, slugi nietknięte

**Status:** przyjęta 2026-08-21 `[J]` · **Dotyczy:** T-056, T-065, architektura katalogu
**Uzupełnia** ADR `2026-08-11-podzial-rol-ads-seo.md`

---

## Problem

Przy T-056 (staw i rybactwo) trzeba było przypisać pięć produktów do kategorii
`Rybactwo - wapno do stawów`. Okazało się to niewykonalne bez skutków ubocznych, a przy okazji
wyszła wada głębsza, którą zgłosił Janek: **kategoria segmentowa opisuje wymyślony podział, nie towar.**
Agrobielik 70 idzie na pole, do stawu i do osadów ściekowych — to jeden produkt, nie trzy.

### Blokada techniczna (zmierzona w kodzie, nie z domysłu)

Adres produktu zawiera kategorię. Gdy produkt należy do kilku kategorii, adres buduje
`woo-permalink-manager` wg `src/PermalinkListener.php:248` → `getWcPrimaryTerm()`:

```php
$terms = wp_list_sort( $terms, 'term_id', 'DESC' );   // malejąco!
$category_object = $terms[0];
```

Kategorii głównej z Rank Matha ta wtyczka **nie czyta** — jej `checkSeoPlugin()` (linia 297) wymaga
**Yoasta** (`WPSEO_BASENAME` + `yoast_get_primary_term_id`), którego nie mamy. Sprawdzone na produkcji:
`yoast_get_primary_term_id` nie istnieje, Yoast nieaktywny. Żaden produkt nie ma też
`rank_math_primary_product_cat`.

Numery kategorii: Rolnictwo **764** · Sadownictwo **765** · Rybactwo **766** · Oczyszczalnie **767**.

Skutek dopisania Rybactwa (766) do produktów z Rolnictwa (764): sortowanie malejąco stawia 766
na pierwszym miejscu, więc **cztery z pięciu produktów zmieniłyby adres** na `/wapno-do-stawow/…`,
w tym rankujący Agrobielik 70. T-028 i T-032 dopiero co zamykały duplikaty adresów.

## Co rozważaliśmy i odrzuciliśmy

| Wariant | Dlaczego odrzucony |
|---|---|
| Filtr `wc_product_post_type_link_product_cat` zamrażający kategorię adresową (6 linii) | Działa, ale zbędny — landing z ręcznym listingiem rozwiązuje to bez kodu. **Odrzucony na rzecz prostszego.** |
| Przypisanie produktów i 301 ze starych adresów | Przenosi rankujący produkt rolniczy pod adres segmentu rybackiego. Bez sensu merytorycznie |
| **Pełna przebudowa struktury adresów** (`agria.pl/wapno/<produkt>/`, segmenty jako strony) | Kierunek słuszny — **odłożony na zimę**, patrz niżej |

## Decyzja

**1. Segmenty powstają jako landingi z ręcznie wybranym listingiem produktów**, wzorzec
`/wapno-granulowane/` (T-064, 21.08). Produkt zostaje w swojej jednej kategorii, adres się nie rusza,
a landing pokazuje dowolny zestaw. Problem kategorii głównej **przestaje istnieć**, filtr niepotrzebny.

**2. Nazwy kategorii tracą człon segmentowy. Slugi zostają nietknięte.**

| term_id | `name` przed | `name` po | `slug` |
|---|---|---|---|
| 764 | Rolnictwo - wapno nawozowe | **Wapno nawozowe** | `wapno-nawozowe-rolnictwo` — bez zmian |
| 766 | Rybactwo - wapno do stawów | **Wapno do stawów** | `wapno-do-stawow` — bez zmian |

Zmiana dotyczy **jednej kolumny w dwóch wierszach**. Nie rusza ani jednego adresu, więc nie dotyka
`/wapno-nawozowe-rolnictwo/` — **trzeciego najmocniejszego URL-a serwisu** (1 292 wyświetlenia,
poz. 9,1 przez 90 dni).

**`rank_math_title` obu kategorii jest sztywny** („Wapno nawozowe do rolnictwa | AGRIA",
„Wapno do stawów rybnych | AGRIA"), więc **tytuł w wynikach Google się nie zmienia**.
Zmienia się wyłącznie **H1 i breadcrumb**.

**3. Sadownictwo, Paszarstwo, Oczyszczalnie, Budownictwo, Hurtownie zostają bez zmian** —
poza zakresem tej decyzji.

### Dlaczego to ma pomóc, nie tylko nie zaszkodzić

`/wapno-nawozowe-rolnictwo/` jest **jedynym** naszym adresem rankującym na frazę `wapno nawozowe`
(1 300/mies., **październik 1 900**): 251 wyświetleń, **pozycja 10,9**, 1 kliknięcie — pierwsze miejsce
drugiej strony. Landing `/wapno-nawozowe/` nie pojawia się w GSC ani razu, bo ma `noindex` —
**kanibalizacji nie ma**, podział ról z 11.08 działa.

Dzisiejszy H1 brzmi „Rolnictwo - wapno nawozowe", czyli nie odpowiada frazie dokładnie.
Po zmianie H1 to **dokładnie fraza główna**. Z 10,9 na pierwszą stronę to dystans, który taka
poprawka potrafi pokonać.

## Rollback

Backup pełnych tabel przed zmianą:
`~/agria-backups/przed-T056-nazwy-kategorii-20260821-20260821-170945.sql`
(886 wierszy: `terms` 408, `term_taxonomy` 408, `termmeta` 70).

Cofnięcie samej zmiany — dwa `UPDATE`, przez MCP `query_db_write` albo WP-CLI:

```sql
UPDATE wpfz_terms SET name = 'Rolnictwo - wapno nawozowe' WHERE term_id = 764;
UPDATE wpfz_terms SET name = 'Rybactwo - wapno do stawów'  WHERE term_id = 766;
```

Po cofnięciu obowiązkowo: `wp_cache_flush()`, czyszczenie `_elementor_element_cache`
i **cache-bust CDN nazwa.pl** — inaczej front pokazuje stan sprzed godziny.

Stan przed zmianą, zmierzony na froncie 21.08:

```
/wapno-nawozowe-rolnictwo/            H1 „Rolnictwo - wapno nawozowe”
                                      title „Wapno nawozowe do rolnictwa | AGRIA”
                                      13 wystąpień „Rolnictwo” w HTML
/wapno-nawozowe-rolnictwo/agrobielik-70/   HTTP 200, breadcrumb „Rolnictwo - wapno nawozowe”
                                           10 wystąpień „Rolnictwo” w HTML
```

**Uwaga przy weryfikacji:** ciąg „Rolnictwo, Rybactwo, Sadownictwo" na karcie produktu to
**atrybut produktu (zastosowanie), nie nazwa kategorii** — po zmianie ma zostać. Zero wystąpień
„Rolnictwo" na karcie byłoby błędem, nie sukcesem.

## Odłożone na zimę — przebudowa struktury adresów

Janek zaproponował 21.08 pełne odejście od kategorii w adresach: produkty pod
`agria.pl/wapno/<produkt>/`, segmenty jako landingi z listingami. **Kierunek przyjęty, termin nie.**

Za: kategoria segmentowa jest fałszywym podziałem; kategoria to słaby nośnik treści
(4 100 zapytań o stawy wymaga poradnika, nie akapitu opisu); serwis jest mały i młody.
Dowód wykonalności: **`/wapno-do-sadu/` trzyma pozycję 9,4 mimo że od miesięcy oddaje 301** —
Google przenosi wartość i długo pamięta.

Przeciw teraz: `wapno granulowane` szczytuje w **październiku na 8 100** (maj: 2 400), kampania
wydaje 40 zł dziennie, a przebudowa adresów oznacza kilka tygodni drgających pozycji.
Okno bez kosztu to **grudzień–luty**.

Przeszkoda do rozwiązania przy projektowaniu: **`/wapno-nawozowe/` jest zajęte** przez landing Ads
(ID 2757, `noindex`), więc `agria.pl/wapno-nawozowe/<produkt>/` nie wejdzie bez przenoszenia landingu.
Stąd propozycja `agria.pl/wapno/<produkt>/`. Płaski root odpada — produkty konkurowałyby o slugi
z landingami i poradnikami.

Pozycja w rejestrze: **T-068**.
