# Prompt startowy — SEO: ceny i nagłówki cenowe na stronach produktów (19.08.2026)

> Wątek wyodrębniony z diagnostyki Ads dzień 5 (`docs/sesje/2026-08-18-ads-dzien5-diagnoza.md`).
> Powód wyodrębnienia: to jest robota SEO/on-page, nie optymalizacja kampanii, a blokuje oba kanały naraz.
> **Stan faktyczny sprawdzony 19.08 — nie zakładaj, że coś jest zrobione, ale też nie audytuj tego drugi raz:**
> zero z 19 produktów ma cenę, w bazie ani w renderze.

---

## Prompt do skopiowania

```
Wątek: SEO on-page dla agria.pl — ceny i nagłówki cenowe na kartach produktów.

Przeczytaj najpierw:
- docs/sesje/2026-08-18-ads-dzien5-diagnoza.md (skąd się wziął ten wątek — sekcje 2 i 4)
- docs/decyzje/2026-08-11-podzial-rol-ads-seo.md (dokąd wolno kierować ruch)
- docs/operations/CEN_LISTA_URL_2026-08-13.md (cennik od Pawła, 15 pozycji)
- memory: project_agria_ceny_strategia, project_agria_render_caching,
  project_agria_architektura_kanalow, feedback_agria_bez_zargonu_loco


PUNKT WYJŚCIA — ustalony 19.08, nie sprawdzaj od nowa

Decyzja z 06.08 mówi: wchodzimy w widełki tonowe („od X zł/t"), nigdy cennik i nigdy
ceny za worek. Ta decyzja NIE ZOSTAŁA WDROŻONA NIGDZIE.

Dowody:
- baza: SELECT po 19 produktach post_type=product — _price NULL przy wszystkich 19,
  słowo „cena" nie występuje w post_content żadnego, żaden nie ma <h2> z „cena";
- render: /agrobielik-70/, /weglanowe-granulowane/, /oxyfertil-90/ — jedyne wystąpienie
  rdzenia „cen" to zwrot „indywidualną wycenę" w stopce sekcji kontaktowej;
- landingi Ads /wapno-granulowane/ i /wapno-nawozowe/ — zero cen, zero widełek.

Jednocześnie 33% kosztu kampanii Ads (44,87 z 137,24 zł w pięć dni) to zapytania wprost
cenowe, a najdroższym zapytaniem okresu jest „wapno granulowane cena" (15,64 zł).
Płacimy za ruch, który odbija się od strony bez ceny.


1. GDZIE WCHODZI CENA I W JAKIEJ FORMIE

Rozstrzygnij i wykonaj — to jest decyzja marketingowa, więc podejmujemy ją my
(MASTER_PROMPT, „Kto podejmuje decyzje marketingowe"):
- czy widełki idą na karty produktów, na landingi Ads, czy na oba,
- czy forma to „od X zł/t netto", przedział „X–Y zł/t", czy „od X zł/t przy dostawie
  całosamochodowej",
- czy powstaje osobna sekcja cenowa, czy cena wchodzi w istniejącą „Specyfikację techniczną".

Twarde ograniczenia, których nie negocjujemy:
- NIGDY ceny za worek ani za 25 kg — pozycjonowanie „dostawca całosamochodowy, nie sklep"
  (memory project_agria_ads_kampanie_zywe),
- NIGDY progu ilościowego („minimum 24 t") — prośba Pawła przy STR-02,
- ZERO żargonu: nie „loco magazyn", tylko „cena za towar, bez transportu"
  (feedback_agria_bez_zargonu_loco),
- ceny biorą się WYŁĄCZNIE z cennika Pawła, nic nie wyliczamy ani nie szacujemy
  (feedback_no_made_up_pricing_without_approval).


2. NAGŁÓWKI POD FRAZY CENOWE

Sprawdź w GSC i DataForSEO, które frazy cenowe realnie mają wolumen i na których
stoimy blisko TOP10 (punkt wyjścia: „wapno granulowane cena" 480/mies.,
„wapno nawozowe cena za tonę" 140, „wapno magnezowe cena" 90, „wapno na pole cena" 50,
„wapno tlenkowe cena" 50, „kreda nawozowa cena" 50).

Potem zdecyduj, gdzie te frazy mają zamieszkać w strukturze nagłówków — i zrób to
tak, żeby nie powielić błędu z ADR 2026-08-11: kanibalizacja jest zmierzona,
jeden URL na frazę, nie sześć.

Uwaga na warstwy renderu (memory project_agria_render_caching): produkty 307/310/320
renderują się z _elementor_data, nie z post_content. Po każdej zmianie czyść
_elementor_element_cache i weryfikuj RENDER, a nie bazę.


3. DŁUG ZNALEZIONY PRZY OKAZJI — do rozstrzygnięcia w tym wątku

Wyszło przy diagnostyce Ads 18–19.08, nikt tego jeszcze nie ruszał:

a) Agrobielik 70 ma DWA adresy, oba zbierają wyświetlenia w GSC (90 dni):
   /wapno-nawozowe-hurt/wapno-agrobielik-70-big-bag-1000kg/ — 168 wyśw., poz. 8,7
   /wapno-nawozowe-rolnictwo/agrobielik-70/ — 106 wyśw., poz. 7,4
   Do rozstrzygnięcia: który jest kanoniczny i co z drugim.

b) Stary typ wpisu `produkt` nadal opublikowany — ID 67, 68, 69
   (Agrobielik 70, Agrobielik 90, Agrobielik 90 frakcja 2-8 mm), równolegle do
   post_type=product ID 310, 311.

c) Demo-produkty motywu wciąż w indeksie — /produkt/organic-pineapple/ zebrało
   7 wyświetleń na pozycji 5,0 w 90 dni. Reszta demo generuje 404-ki opisane
   w ADR 2026-08-14.


4. CZEGO NIE ROBIMY

Nowych landingów organicznych (ADR 2026-08-11 — kanibalizacja zmierzona),
wpuszczania /wapno-granulowane/ i /wapno-nawozowe/ do indeksu, zmian w kampaniach
Ads (osobny wątek), publikowania pełnego cennika.

Zasada obowiązująca w całym wątku: każde twierdzenie o stanie strony z dowodem obok
(zapytanie do bazy albo URL po zmianie). Bez dowodu pisz „niezweryfikowane".
```

---

## Czego ten wątek NIE dotyka

- **Kampanie Ads** — stawki, wykluczenia, kampania Marka: wątek Ads.
- **Numer telefonu i CTA na landingach** — wątek Ads (punkty 1 i 3 rekomendacji z 18.08),
  bo to naprawa ścieżki konwersji płatnej, nie on-page SEO.
- **OLX, ofertownik, kalkulator Mg** — osobne wątki, patrz `docs/PROJECT_STATE.md`.
