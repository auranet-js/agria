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

## Stan

Etap 1 wg specyfikacji, częściowo. **Jest:** cennik, ustawienia, odległości, kalkulacja, ekran wyceny.
**Nie ma:** zapisu oferty (`agria_quote`), karty klienta (`agria_client`), PDF, nadpisywania cen
w interfejsie z powrotem do proponowanej.
