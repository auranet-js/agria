# ADR 2026-08-22 — audyt wycieku cen: NIESZCZELNE. Cena poza WooCommerce, bez wariantów

**Status:** obowiązująca · pomiar i decyzja 22.08.2026
**Dotyczy:** T-045 (etap zerowy ofertownika), spec `docs/specs/2026-08-18-ofertownik-design.md` §4.1, §7.1, §7.3
**Środowisko pomiaru:** `agria.auratest.pl` — staging odświeżony z produkcji tego samego dnia
(WP 7.1, WooCommerce **10.9.3** — identycznie jak produkcja)

---

## Werdykt

**Cena wpisana w natywne pole WooCommerce wycieka. Zmierzone, nie przypuszczane.**

Produkt testowy: Kreda malarska (ID 304, `AGR-016`) — najmniejszy w katalogu, jedna lokalizacja,
jedna forma. Kwota testowa `1234.56` w `_price` i `_regular_price`. Przejście wszystkich kanałów
anonimowym `curl`, bez ciasteczek i bez uwierzytelnienia:

| Kanał | HTTP | Wydaje cenę |
|---|---|---|
| `wp-json/wc/store/v1/products/304` | 200 | **TAK** — `prices.price: "123456"` |
| `wp-json/wc/store/v1/products?per_page=50` | 200 | **TAK** |
| **strona produktu — JSON-LD Rank Matha** | 200 | **TAK** — `offers.price: "1234.56"` |
| `wp-json/wc/store/v1/products` (bez `per_page`) | 200 | nie — **tylko dlatego, że produkt wypadł poza pierwszą dziesiątkę paginacji** |
| `wp-json/wc/store/v1/products/collection-data` | 200 | nie |
| `wp-json/wc/v3/products` | **401** | nie — kanał zamknięty kluczem |
| `wp-json/wp/v2/product` | 200 | nie |
| `/oferta/`, `product-sitemap.xml`, `/feed/`, wyszukiwarka | 200 | nie |

Dwie rzeczy warte odnotowania osobno:

- **`price_html` było puste**, czyli moduł `catalog-mode` działa — i to jest dokładnie ilustracja tezy z T-045:
  tryb katalogu ukrywa **wyświetlanie** ceny, a nie samą daną. Cena wyszła obok, dwiema drogami naraz.
- **Pierwszy strzał w `/products` bez `per_page` dał zero trafień.** To nie jest szczelność, tylko
  domyślna paginacja. Audyt zatrzymany na tym jednym zapytaniu wystawiłby werdykt „szczelne" — i byłby fałszywy.

## Plan awaryjny — zmierzony jako szczelny

Ta sama kwota przeniesiona do `_price` pustego, a wartości do własnej meta `_agria_of_price`
(podkreślenie na początku czyni ją *protected* w WordPressie, więc REST jej nie wydaje):

| Kanał | Trafień na `1234` |
|---|---|
| `store/v1/products?per_page=50` | **0** |
| `store/v1/products/304` | **0** |
| strona produktu (HTML + JSON-LD) | **0** |
| `/oferta/`, `product-sitemap.xml`, `wp/v2/product?per_page=50` | **0** |

Cena testowa usunięta po pomiarze; `_price` i `_agria_of_price` puste, Store API zwraca `"0"`.

## Decyzja

**1. Ceny ofertownika nigdy nie trafiają do `_price` ani `_regular_price`.** Warstwa B mieszka
we własnej strukturze, poza polami, które WooCommerce uważa za swoje.

**2. Rezygnujemy z cennika na wariantach WooCommerce** — a to jest zmiana wobec §4.1 specyfikacji.

Powód jest konsekwencją punktu 1, nie osobnym argumentem. Warianty miały sens dokładnie dlatego,
że niosły cenę w natywnym polu: dochodzi kopalnia → dopisujesz term i wariant, cena ląduje tam,
gdzie WooCommerce jej szuka, i nikt nie pisze modelu relacji. **Skoro cena i tak nie może tam zamieszkać,
warianty przestają cokolwiek dawać, a koszt zostaje:**

- konwersja 19 produktów prostych na wariantowe to zmiana w danych sklepu — **osobna wtyczka przed nią nie chroni**
  (§7.3), a WooCommerce renderuje kartę wariantową inaczej: zamiast opisu listy wyboru atrybutów;
- ~78 wpisów `product_variation` w bazie produkcyjnej, trudno odwracalnych;
- osie i tak czytamy z taksonomii `pa_agria-lokalizacja` / `pa_agria-forma-dostawy`, nie z wariantów;
- ekran edycji cennika i tak piszemy własny (§4.1 mówi to wprost — panel wariantów przy stu pozycjach
  jest nie do przejścia).

Zostaje sama strata: ryzyko dla kart, które dziś działają, w zamian za nic.

**3. Cennik jako własna tabela** `{prefix}agria_of_ceny`, klucz naturalny
`produkt × zakład × forma × frakcja`, obok ceny — cena minimalna (podłoga z §4.1)
oraz kto i kiedy zmienił (wymóg z §4.7). Osie pozostają dokładnie te, co w specyfikacji;
zmienia się wyłącznie miejsce zapisu, co §7.3 przewidywał jako dopuszczalne wyjście.

**4. Etap zerowy kurczy się o dwie pozycje.** Odpada konwersja próbna (§7.3) i odpada tworzenie
wariantów. Zostaje sprzątanie atrybutów — ale **już nie jako warunek cennika**, tylko jako dług
widoczny dla rolnika na kartach produktów: siedem zapisów słowa „Luz" i jedenaście przypisań.

## Co to zmienia w ryzyku

Zamknięcie Store API filtrem `rest_pre_dispatch` — wzorzec sprawdzony w tym projekcie przy T-029
(`security-user-enum.php`) — **rozważaliśmy i odrzuciliśmy jako podstawę**. Nie dlatego, że nie zadziała:
dlatego, że broni jednego znanego kanału, a lista kanałów zmienia się z każdą aktualizacją WooCommerce
i Rank Matha. Dane, których w polach WooCommerce nie ma, nie wyciekną **żadnym** kanałem,
także takim, który powstanie za pół roku. To jedyna obrona, która nie wymaga recheckingu przy każdym `wp plugin update`.

Recheck z T-045 §11 („przy każdej aktualizacji WooCommerce ponowny test kanałów") **przestaje być konieczny**
w dotychczasowym zakresie. Zostaje jeden, znacznie węższy: czy nasza własna tabela nie została
przypadkiem wystawiona przez kod, który sami napiszemy.

## Dowód

Pomiar wykonany na stagingu, na wersjach identycznych z produkcją. Produkcja **nietknięta** —
`_price` puste w 19/19, Store API zwraca `"0"`, sprawdzone tego samego dnia przed i po audycie.
