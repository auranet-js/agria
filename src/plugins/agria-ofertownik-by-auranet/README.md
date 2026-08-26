# agria-ofertownik-by-auranet

Wycena zamówienia z transportem z właściwego zakładu — narzędzie wewnętrzne działu handlowego AGRII
(Bogdan, Paweł, Kazimierz). Nie sklep, nie samoobsługa dla rolnika.

**Spec:** `docs/specs/2026-08-18-ofertownik-design.md`
**Werdykt audytu cen:** `docs/decyzje/2026-08-22-audyt-wycieku-cen-werdykt.md`

## Dwie rzeczy, które trzeba wiedzieć przed dotknięciem kodu

1. **Ceny nie mieszkają w polach WooCommerce.** `_price` wycieka publicznie — zmierzone 22.08.2026
   przez Store API i JSON-LD Rank Matha. Cennik siedzi we własnych tabelach `{prefix}agria_of_*`.
2. **Odległości muszą być drogowe.** Ortodroma z `scripts/olx/grid.py` zaniża trasę o ~28%
   (Sitkówka→Mława: 255 km prostą, 327 drogą), co przy wannie liczonej w dwie strony
   daje 605 zł błędu na jednym aucie.

## Układ

| Plik | Za co odpowiada |
|---|---|
| `inc/db.php` | tabele cennika i historii, grosze ↔ złotówki |
| `inc/ustawienia.php` | stawki transportu, pojemność palety, wykrywanie skoku o rząd wielkości |
| `inc/zaklady.php` | osie z taksonomii `pa_agria-*`, normalizacja form w locie |
| `inc/cennik.php` | siatka pozycji, zasiew z cennika Pawła, zmiana ceny z historią |
| `inc/odleglosci.php` | 53 247 miejscowości, współrzędne zakładów, routing OSRM z fallbackiem |
| `inc/wycena.php` | dobór zakładu i metody, koszt przewozu, dopełnienie auta |
| `inc/ekran.php` | `/wycena/` za logowaniem + AJAX |
| `inc/admin.php` | panel: cennik i transport — ekrany dla AGRII |

| `inc/oferty.php` | CPT ofert i klientów, zapis zamrożony, wydruk, kolumny list, odczyt starych formatów |
| `inc/koszyk.php` | wycena wielopozycyjna, grupowanie transportu po zakładach |
| `inc/gus.php` | dane płatnika z rejestru REGON po NIP |
| `inc/panel-zaklady.php` | współrzędne zakładów i ich poprawianie |
| `inc/zestawienie.php` | zestawienie sprzedaży — kanały, produkty, rejony, rabaty |

## Stan

**Etap 1 domknięty, etap 2 w większości.** Arkusz wielopozycyjny, moduł ustawień, odległości
drogowe, płatnik z GUS, zapis zamrożony, karta klienta, wydruk, zestawienie sprzedaży.

Z etapu 3 zostaje: wycena prosto z zapytania `agria_inquiry` i wysyłka oferty do klienta.
Statusy ofert istnieją, ale nikt ich jeszcze nie ustawia — dopóki tak jest, tabela skuteczności
w zestawieniu nic nie mówi i tak to opisuje.

## Format ofert zmieniał się w trakcie

Do 0.4.0 oferta była jednopozycyjna (płaskie meta `produkt`, `tony`, `cena_podana`);
od 0.5.0 trzyma tablicę `pozycje`. Starych **nie przepisujemy** — oferta ma być zamrożona,
a przepisanie zmieniałoby dokument, który ktoś już wydrukował. Czytamy oba formaty przez
`agria_of_pozycje_oferty()` / `agria_of_grupy_oferty()` / `agria_of_roznica_oferty()`.

## Szczelność — sprawdzone, nie założone

Oferty zawierają ceny i dane klientów. CPT są `public:false`, `publicly_queryable:false`,
`exclude_from_search:true`, `show_in_rest:false`. Zmierzone znacznikiem, którego nie ma w URL:
zero trafień w `/?p=`, `/?post_type=`, `/?s=`, `/feed/`, sitemapie i REST.

**Uwaga przy testach:** `/?s=<fraza>` zwraca frazę w breadcrumbach schema Rank Matha, więc grep
po niej daje trafienia niezależnie od wycieku. Testuj wartością, której w zapytaniu NIE MA.
