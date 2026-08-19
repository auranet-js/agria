# T-045 — ofertownik, etap zerowy: audyt wycieku cen → konwersja jednego produktu → sprzątanie atrybutów

| | |
|---|---|
| **Linia / zakres** | Ofertownik · **W** (własne Auranet, nie fakturujemy) |
| **Status** | 📅 wrzesień (M4), niezaczęty |
| **Spec** | `docs/specs/2026-08-18-ofertownik-design.md` |
| **Szacunek** | audyt 3 h · konwersja 2 h · sprzątanie atrybutów 4 h |

---

## 1. Czego to dotyka

**Audyt wycieku cen** — wszystkie kanały, którymi cena wariantu WooCommerce może wyjść na zewnątrz:
REST Store API, REST `wc/v3`, `wc_get_product` w motywie, JetSmartFilters, dane strukturalne
Rank Matha, sitemapa produktowa, feedy, moduł `catalog-mode`.
**Konwersja** — jeden produkt z prostego na wariantowy.
**Sprzątanie atrybutów** — taksonomie `pa_*`, duplikaty zakładów, formy dostawy pomieszane z ładownością.

## 2. Strefy kruche

1. **To jest warunek bezpieczeństwa danych, nie porządki.** Ceny ofertownika są różnicowane
   per zakład i obłożone transportem — to informacja handlowa, której konkurencja AGRII szuka
   na tym samym OLX-ie. **Nigdzie nie ujawniana.**
2. **Wyciek jest już potwierdzony jako możliwy.** Zmierzone 19.08: `https://agria.pl/wp-json/wc/store/v1/products`
   odpowiada **publicznie, bez uwierzytelnienia**, i zwraca obiekt `prices` z `price`, `regular_price`,
   `sale_price` dla każdego produktu. Dziś wartości to `"0"`, bo `_price` jest puste. **W sekundzie,
   w której wpiszesz pierwszą cenę wariantu, ten endpoint ją wyda.** `wc/store/v1/cart` też odpowiada 200.
3. **Tryb katalogu ukrywa przycisk kupna, nie cenę.** To nie to samo i moduł `catalog-mode`
   nie jest zabezpieczeniem danych.
4. **Plan awaryjny jest w specyfikacji i trzeba go traktować jako domyślny, nie ostateczny:**
   cena wariantu zostaje pusta, właściwa cena idzie w meta wariantu pod własnym kluczem,
   niewidocznym dla WooCommerce. Jeśli audyt nie da **pewności** szczelności — bierz plan awaryjny.
   „Prawdopodobnie nie wycieknie" nie jest wynikiem audytu.
5. **`T-010` (ceny w treści) i ten task to dwie różne warstwy.** Widełki „od X zł/t" w treści są
   publiczne i mają być publiczne. Ceny wariantów są niejawne. Nigdy ich nie mieszaj i nie próbuj
   „uspójnić" — to nie są te same kwoty i nigdy nie były.
6. **Sprzątanie atrybutów zmienia to, co widzi rolnik na kartach produktów** — te same śmieciowe
   wartości są dziś na froncie. To znaczy: zmiana jest widoczna publicznie i wymaga tej samej
   ostrożności co edycja treści.
7. **`wc_product_attributes` z pustą listą USUWA atrybut** z `_product_attributes`. Jedno wywołanie
   z pomyłką kasuje parametr z karty produktu.
8. **Konwersja produktu prostego na wariantowy jest trudno odwracalna** — WooCommerce tworzy
   wpisy `product_variation`. Wybierz produkt o **najmniejszym** ruchu, nie najważniejszy.

## 3. Stan zmierzony 19.08.2026

```
19 produktów WC, wszystkie proste, wszystkie z pustym _price
REST wc/store/v1/products → 200 publicznie, prices.price = "0" dla wszystkich
REST wc/store/v1/cart     → 200
REST wc/v3/products       → 401 (wymaga klucza) — ten kanał jest zamknięty
Store API zwraca też: sku, permalink, short_description, kategorie
```

## 4. Warunki wejścia

- [ ] Janek potwierdził, że wchodzimy w etap zerowy (to projekt własny, priorytet niższy niż zlecenia klienta).
- [ ] `db_export` produktów i atrybutów.

## 5. Co robisz

**Etap A — audyt (nic nie zmieniasz):**
1. Wypisz wszystkie kanały wyjścia ceny. Dla każdego: czy odpowiada anonimowi, czy zwraca pole ceny,
   czy da się go wyłączyć bez psucia sklepu.
2. Dla Store API: sprawdź, czy da się go wyłączyć (nie jest używany, skoro nie ma koszyka
   w trybie katalogu) — i czy wyłączenie nie zepsuje bloków WooCommerce w Elementorze.
3. Test empiryczny: wpisz cenę **jednemu** produktowi testowemu (draft, nie publish), przejdź
   wszystkie kanały, sprawdź, gdzie się pojawiła. **Usuń cenę po teście.**
4. Werdykt: szczelne / nieszczelne. Nieszczelne → plan awaryjny z meta.

**Etap B — konwersja jednego produktu** (po werdykcie): produkt o najmniejszym ruchu, warianty
wg osi z rozdz. 4.1 specyfikacji, ceny wg werdyktu z etapu A.

**Etap C — sprzątanie atrybutów:** usunięcie śmieciowych termów, scalenie duplikatów zakładów,
rozdzielenie formy dostawy od ładowności, usunięcie martwych taksonomii, SKU dla ID 303.
Każda zmiana z kontrolą renderu karty.

## 6. Jak sprawdzasz w trakcie

Po każdym kroku etapu A: `curl` na wszystkie kanały z listy i `grep` po kwocie testowej.
Kwota testowa ma być charakterystyczna (np. `1234.56`), żeby `grep` był jednoznaczny.

## 7. Jak testujesz

```bash
# kanały, po wpisaniu ceny testowej 1234.56 produktowi testowemu
for e in "wp-json/wc/store/v1/products" "wp-json/wc/store/v1/products?per_page=50" "product-sitemap.xml"; do
  printf '%s → %s\n' "$e" "$(curl -s https://agria.pl/$e | grep -c '1234')"
done
curl -s https://agria.pl/<url-produktu-testowego>/ | grep -c '1234'
curl -s https://agria.pl/<url-produktu-testowego>/ | grep -A5 '"@type":"Product"' | grep -c '1234'
```
Wynik `0` we wszystkich = szczelne. Jakiekolwiek `>0` = plan awaryjny.

## 8. Dowód do rejestru

Tabela kanałów: kanał → odpowiada anonimowi → ujawnia cenę → wniosek. Werdykt szczelności.
Jeśli plan awaryjny — decyzja zapisana jako ADR, nie tylko w rejestrze.

## 9. Rollback

`db_export` przed etapem B i C. Konwersja wariantowa: usunięcie wpisów `product_variation`
przez WP-CLI i powrót typu na `simple`. Atrybuty: przywrócenie z eksportu.

## 10. Rozliczenie

Zakres **W** — projekt własny Auranet, nie fakturujemy. W DZIENNIKU M4 ze znacznikiem W,
godziny liczone dla własnej wiedzy o koszcie narzędzia.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **po etapie A** | powtórz test kanałów na produkcie testowym — i **usuń cenę testową**, zanim pójdziesz dalej |
| **+7 dni po etapie B** | czy karta produktu wariantowego renderuje się poprawnie i czy cena nie wypłynęła |
| **przy każdej aktualizacji WooCommerce** | ponowny test kanałów — nowa wersja może otworzyć endpoint, który dziś jest zamknięty |
| **przed pierwszą realną ceną w cenniku** | pełny audyt jeszcze raz, na aktualnych wersjach wtyczek |
