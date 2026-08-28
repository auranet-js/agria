# T-044 — wdrożenie modułu magnezowego do kalkulatora produkcyjnego

> Data: 2026-08-28 · Poprzednik: T-043 (mockup zweryfikowany przez Kazimierza)
> Prototyp: `mockups/agria-kalkulator-mg-test-2026-08-18.html` (wersja z poprawkami z 28.08)
> Cel: przenieść moduł Mg z prototypu HTML do `modules/liming-calculator/` na produkcji

---

## 1. Stan produkcji — zmierzony 28.08 przez MCP

`agria-by-auranet/modules/liming-calculator/`:

| Plik | Rozmiar | mtime |
|---|---|---|
| `liming-calculator.php` | 4 587 B | 27.03 |
| `includes/class-iung-data.php` | 8 118 B | 27.03 |
| `includes/class-product-matcher.php` | 5 724 B | **18.06** (T-001, wykluczenie #304/#307) |
| `templates/calculator-form.php` | 6 695 B | 27.03 |
| `assets/calculator.js` | 10 546 B | 27.03 |
| `assets/calculator.css` | 6 483 B | 27.03 |

Moduł nie zna magnezu w żadnej warstwie. **W repo nie ma kopii w `src/`** — source of truth to serwer,
każdy plik czytamy przez MCP `read_file` bezpośrednio przed edycją.

**Atrybut `pa_agria-mgo` istnieje i jest wypełniony** (zapytanie do bazy, 28.08):
`#302` Dolomit `min-15-mgo` · `#313` tlenkowe z Mg `min-25-mgo` · `#317` granulowane `min-16-mgo` ·
`#318` odm. 04 `min-8-mgo` · `#319` odm. 05 `min-8-mgo`. Ten sam `preg_match('/(\d+)/')`, którego
używa dziś `extract_cao_percent`, wyciągnie z nich liczbę — nie trzeba nowego parsera ani
zaszywania wartości w kodzie, jak było w prototypie (`MG_PRODUCTS` z twardymi liczbami).

---

## 2. Delta prototyp → produkcja, plik po pliku

### 2.1 `includes/class-mg-data.php` — NOWY

Dane agronomiczne magnezu po stronie PHP, przez analogię do `class-iung-data.php`
(w prototypie siedziały w JS — na produkcji trzymamy je tam, gdzie reszta metodyki):

- `MG_THRESHOLDS` — granice zasobności dla 4 grup mechanicznych (bardzo lekka / lekka / średnia / ciężka),
  granica „do X" **włącznie** do klasy niższej;
- `target_range( $group )` — widełki celu: od dolnej granicy „średniej" (2,1/3,1/5,1/6,1)
  do górnej granicy „wysokiej" (6/7/9/14), **default = górna**;
- `assess( $group, $mg, $target )` — klasa zasobności, deficyt, dawka w kg Mg/ha i kg MgO/ha;
- stałe: `+1 mg Mg/100 g = 30 kg Mg/ha`, `Mg → MgO × 1,658` (40,304/24,305).

### 2.2 `includes/class-product-matcher.php`

- `extract_mgo_percent( $product_id )` — bliźniak istniejącego `extract_cao_percent`, taksonomia `pa_agria-mgo`;
- `get_mg_products( $mgo_dose, $cao_dose )` — dobór **dwuetapowy (Mg-first)**: sort po MgO malejąco,
  dawka nawozu z niedoboru Mg, kolumny „CaO pokryte tą dawką" i „CaO do uzupełnienia",
  ostatnia kolumna = dopokrycie wapnem bez magnezu;
- **produkt referencyjny do kroku 2** — prototyp zaszywał „Agrobielik 70". Na produkcji wybieramy go
  zapytaniem: najwyższe `pa_min-cao` wśród produktów **bez** `pa_agria-mgo`, żeby nazwa nie żyła w kodzie;
- **filtr z T-043 (24.08):** gdy rolnik nie deklaruje magnezu, z listy CaO wypadają produkty
  mające `pa_agria-mgo` — 15 pozycji → 10. Dziś matcher zwraca wszystkie.

### 2.3 `liming-calculator.php` (AJAX)

Nowe pola wejścia: `mg_enabled`, `mg_value`, `mg_soil_group`, `mg_target`. Walidacja jak istniejąca
(whitelist grup, format liczby), przycięcie `mg_value` do górnej granicy „wysokiej". Odpowiedź JSON
rozszerzona o blok `mg` (klasa, deficyt, dawki, widełki celu) i `mg_products`.

### 2.4 `templates/calculator-form.php`

- **krok 3b** — checkbox „Znam zawartość magnezu z badania gleby" + pole mg/100 g (default 0);
- **krok 3c** — grupa mechaniczna gleby, **tylko dla użytków zielonych** (ścieżka gruntów ornych
  bierze grupę z kroku 2);
- **krok 3d** — cel nawożenia z widełkami i wartością domyślną = górna granica „wysokiej";
- **wyniki** — blok oceny zasobności Mg (badge klasy + dawka kg Mg/ha ≈ kg MgO/ha) i tabela doboru
  dwuetapowego, z tekstem zaakceptowanym 28.08: *„…uzupełniasz w kroku 2 zwykłym wapnem bez magnezu"*.

⚠️ **Zmiana strukturalna, nie kosmetyczna:** dziś „wapnowanie zbędne" to osobny blok `#agria-calc-zero`
**poza** `#agria-calc-results` — pokazuje się albo wynik, albo zero. Przy magnezie potrzebny jest stan
„wapnowanie zbędne, ale magnez do uzupełnienia", czyli oba naraz. Blok zerowy wchodzi do środka wyników
(jak w prototypie). Dotyka to również resetu w JS.

### 2.5 `assets/calculator.js`

Obsługa nowych kroków, render bloku Mg i tabeli dwuetapowej, filtr listy CaO. Plus tekst podziału dawki:
produkcja pokazuje dziś „Część I / Część II" **bez nawiasu z terminem** — nawias
*„(w drugim, trzecim roku)"* w brzmieniu Kazimierza dochodzi razem z modułem.

### 2.6 `assets/calculator.css`

Style bloku Mg, badge klasy zasobności i tabeli. Tabela magnezowa ma **7 kolumn** — na telefonie
musi mieć własny przewijany kontener, inaczej powtórzymy przelew poziomy z T-063.

---

## 3. Nic nie blokuje kodu — prototyp stoi na żywych danych

Sprawdzone zapytaniem do bazy 28.08: lista `CAO_PRODUCTS` i `MG_PRODUCTS` w prototypie to **te same
15 produktów i te same wartości**, które siedzą w taksonomiach na produkcji (segment rolnictwo/sadownictwo,
bez #304 i #307):

| ID | Produkt | `pa_min-cao` → CaO | `pa_agria-mgo` → MgO |
|---|---|---|---|
| 302 | Dolomit | `cao-mgo-min-45-w-tym-mgo-min-15` → **45** | `min-15-mgo` → **15** |
| 303 | Kreda czarna (jeziorna) | `min-44-cao` → 44 | — |
| 305 | Kreda nawozowa granulowana | `min-50-cao` → 50 | — |
| 306 | Kreda nawozowa sypka | `min-50-cao` → 50 | — |
| 308 | Mieszanka tlenkowo-węglanowa | `min-70-cao` → 70 | — |
| 310 | Agrobielik 70 | `min-70-cao` → 70 | — |
| 311 | Agrobielik 90 | `min-90-cao` → 90 | — |
| 312 | Oxyfertil 90 | `min-90-cao` → 90 | — |
| 313 | Tlenkowe zawierające magnez | `min-70-cao` → **70** | `min-25-mgo` → **25** |
| 314 | Węglanowe bez Mg granulowane | `min-50-cao` → 50 | — |
| 315 | Węglanowe bez Mg odm. 04 | `min-50-cao` → 50 | — |
| 316 | Węglanowe bez Mg odm. 05 | `min-40-cao` → 40 | — |
| 317 | Węglanowe z Mg granulowane | `min-31-cao` → **31** | `min-16-mgo` → **16** |
| 318 | Węglanowe z Mg odm. 04 | `min-41-cao` → **41** | `min-8-mgo` → **8** |
| 319 | Węglanowe z Mg odm. 05 | `min-25-37-cao` → **25** | `min-8-20-mgo` → **8** |

Wniosek: **wdrożenie to odtworzenie 1:1 zaakceptowanego prototypu na danych, które kalkulator i tak czyta.**
Ten sam `preg_match('/(\d+)/')` daje z każdego sluga tę samą liczbę, którą prototyp ma wpisaną ręcznie —
wynik po wdrożeniu musi być identyczny z tym, co Kazimierz przetestował. Zachowania sporne (przycinanie
wartości Mg do maksimum, lista 15 pozycji przy Mg wysokim, disclaimer zamiast ostrzeżenia przy dawce
powyżej 4/5 t) **odtwarzamy tak, jak działają w prototypie** — został zaakceptowany w tym kształcie.

### Dwie rzeczy do rozstrzygnięcia osobno — poza tym wdrożeniem

Obie dotyczą **poprawności atrybutu**, nie kodu modułu, i obie działają już dziś w żywym kalkulatorze:

1. **Dolomit 45 vs 30.** Slug `cao-mgo-min-45-w-tym-mgo-min-15` opisuje **sumę** CaO+MgO, więc samo CaO
   to ≈ 30. Parser bierze pierwszą liczbę → 45. Prototyp powiela ten rozjazd świadomie: tabela magnezowa
   liczy z 30, tabela CaO z 45 — wierność produkcji. Poprawka (parser albo wartość atrybutu) zmieni dawki
   **także w kalkulatorze, który stoi na stronie od marca**, więc jest osobnym zadaniem z własną regresją.
2. **#313 „min. 70% CaO" obok 25% MgO** — czy 70 to CaO samo, czy suma z magnezem. Jeśli suma, dawka
   wg CaO rośnie z 6,86 do ~10,7 t/ha. Pytanie do karty Lhoist, nie do modułu.

## 4. Kolejność i weryfikacja

1. `backup_file` na każdym dotykanym pliku (MCP robi auto-backup, ale świadomie przed serią zmian).
2. Kolejność: `class-mg-data.php` → matcher → AJAX → template → JS → CSS.
3. **Bump `AGRIA_VERSION`** — inaczej przeglądarki i CDN nazwa.pl podadzą stary `calculator.js`.
4. **Weryfikacja renderem przez Chrome MCP**, nie odczytem z bazy (§4 CLAUDE.md) — front `/kalkulator-wapnowania/`,
   cache-bust w URL-u.
5. **Regresja obowiązkowa:** ścieżka bez magnezu (checkbox odznaczony) musi dawać **dokładnie te same dawki
   CaO co dziś** — porównanie przed/po na trzech zestawach parametrów (grunty orne lekka pH 4,5 ·
   grunty orne ciężka pH 5,5 · użytki zielone C 2,6–5,0 pH 4,8), zrzut wyników przed zmianą.
6. Kontrola kodów HTTP: `/kalkulator-wapnowania/` = 200, brak błędów w `logs`.

**Szacunek:** ~4 h kodu (zgodnie z wyceną T-044) + rozstrzygnięcia z §3.
