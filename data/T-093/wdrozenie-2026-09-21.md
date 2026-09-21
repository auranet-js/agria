# T-093 — wdrożenie opisu kategorii `/wapno-do-oczyszczalni/`

**Data:** 2026-09-21 · **Term:** 767 (`product_cat`) · **Pole:** `term_taxonomy.description`
**Wzorzec:** T-092 (`data/T-092/wdrozenie-2026-09-04.md`) i T-078 (`data/T-078/wdrozenie-2026-09-08.md`)

## Stan przed i po

| | przed | po |
|---|---|---|
| `description` | **976 B**, MD5 `145ab29f4cf60d02746d2f35d9a03eab` | **8 732 B**, MD5 `a4954c75151598b2587dececbcaa83ae` |
| Nagłówki w opisie | 1 × H2 | **7 × H2, 4 × H3** |
| Tabele | 0 | **1** (5 kolumn, cztery produkty z linkami do kart) |
| Linki wewnętrzne w opisie | 2 | **8** (4 karty, poradnik, `/do-pobrania/` ×2, `/kontakt/` ×2, stabilizacja gruntów) |
| Tekst całej strony (render) | 4 983 znaki | **11 311 znaków** |

H1 „Oczyszczalnie", listing czterech produktów, `rank_math_title` i meta description — **nietknięte**.
MD5 opisu w bazie zgodny co do znaku z plikiem `opis-do-wdrozenia-2026-09-21.html`.

## Backup i rollback

- `~/agria-backups/przed-T093-opis-oczyszczalnie-20260921-112201.sql` — 472 wiersze
  (`wpfz_term_taxonomy` 408 + `wpfz_termmeta` 64), zrzut przez MCP `db_export`, poza web rootem.
- Poprzedni opis 1:1 w repo: `data/T-093/opis-przed-2026-09-21.html`.

## Przebieg

Zapis przez **`$wpdb->update`** (`wp eval-file`, skrypt wysłany na serwer poza web root), nie przez
`wp term update` ani `wp_update_term` — filtr `wp_filter_kses` zdejmuje tabele i nagłówki przy zapisie
bez zalogowanego użytkownika (incydent T-092 04.09, memory `feedback_agria_term_description_kses`).
Po zapisie `clean_term_cache(767)`, potem `rocket_clean_domain()`. Render zweryfikowany dwa razy:
z cache-bustem i bez — obie wersje oddają nową treść.

**Kontener `<div style="overflow-x:auto">` wokół tabeli pominięty świadomie** — render zjada atrybut
`style` z diva i zostawia go na tabeli (pomiar T-092 §2). Tabela skrócona z 7 kolumn do **5**:
kolumna „Zawartość CaO" wypadła, bo wszystkie cztery produkty mają min. 90% i nie różnicuje wyboru;
„Typ reakcji" przeszedł do prozy.

## Dlaczego taka treść — GSC, nie przeczucie

Baseline 21.08–17.09: `data/T-093/baseline-gsc-2026-09-21.json`.

| fraza | wyśw. | klik. | poz. |
|---|---|---|---|
| higienizacja osadów ściekowych | 78 | 0 | 14,8 |
| **wapno do szamba** | **55** | 0 | **10,3** |
| wapnowanie osadów ściekowych | 52 | 0 | 12,8 |
| proces higienizacji osadów ściekowych | 20 | 0 | 19,9 |
| urządzenie do higienizacji osadów ściekowych | 20 | 0 | 9,8 |

Strona: **458 wyświetleń, 12 kliknięć, poz. 9,1**. Siedem zapytań nad progiem daje 230 wyświetleń
i **zero kliknięć** — 12 kliknięć przyszło z zapytań pod progiem prywatności.

⚠️ **Korekta wobec rejestru:** zapis „poradnik `/higienizacja-osadow-sciekowych-wapnem/` ma zero
wyświetleń i nigdy nie był pobrany" jest nieaktualny. Po ręcznym zgłoszeniu z 09.09 poradnik ma
**157 wyświetleń i 2 kliknięcia** w tym samym oknie. Obie strony rankują na cztery te same frazy,
kategoria we wszystkich wyżej — kierunek „merytoryka w kategorii, poradnik zostaje" się broni,
ale kanibalizacja jest realna i idzie do materiału na D1.

## Sekcja o szambie — źródło i ograniczenia

Frazy szambowe są w bazie wiedzy oznaczone jako **zastosowanie spoza kart producentów**
(`docs/produkty/wapno-palone-mielone.md` §5). Treść powstała na podstawie rozstrzygnięcia
**Kazimierza (21.09, przez Janka)**, w dwóch krokach:

1. Bielik nadaje się — „najtańszy naturalny środek dezynfekcyjny grzybo- i bakteriobójczy,
   odkażający gleby, kurniki, obory, kompostowniki".
2. Doprecyzowanie: **wapno wchodzi wyłącznie do zbiornika opróżnionego z osadu**, do odkażenia
   i wybielenia ścian od środka. Do zbiornika w pracy — nie, jeśli stosowane są biopreparaty,
   bo wapno zabija bakterie rozkładające zawartość. To samo dotyczy przydomowej oczyszczalni
   biologicznej z drenażem, złożem lub osadem czynnym.

Na stronie opisany jest **mechanizm** (podniesiony odczyn, środowisko przestaje sprzyjać bakteriom
i grzybom), nie właściwości produktu — świadomie nie pada sformułowanie „środek dezynfekcyjny
grzybo- i bakteriobójczy", bo produkty biobójcze mają własny reżim rejestracyjny (BPR 528/2012),
a wapno AGRII jest sprzedawane jako wapno nawozowe i budowlane.

**Kanał:** worki 25 kg wychodzą paletami do sklepów i hurtowni oraz do firm asenizacyjnych i gmin
(decyzja Janka 21.09; „hurtownie" są jednym z czterech segmentów oferty handlowej, kurier paletowy
120 zł za paletę). Sprzedaży po pojedynczym worku nie ma — zapis Pawła z 07.08.
Cena workowa **1 220 zł/t** publikowana po raz pierwszy, wyłącznie jako przeliczenie na tonę.

## Listing wobec opisu — pomiar

Szablon renderuje opis **nad** listingiem produktów (sprawdzone na trzech kategoriach).

| | znaków tekstu przed listingiem |
|---|---|
| `/wapno-do-oczyszczalni/` przed zmianą | 2 806 |
| `/paszarstwo/` (opis z 08.09) | 6 633 |
| `/wapno-do-oczyszczalni/` po zmianie | ok. 9 150 |

Droga do kart się nie wydłużyła: tabela z linkami do wszystkich czterech produktów stoi po
**771 znakach** opisu, czyli mniej więcej tam, gdzie wcześniej zaczynał się listing kafelków.
Otwarte: czy wypiąć część opisu pod listing (`woocommerce_after_main_content`) — dotknęłoby
wszystkich kategorii, więc osobne zadanie, nie tutaj.

## Czym mierzyć

**Kontrola 14-dniowa 05.10** z GSC, na frazach z baseline'u — `higienizacja osadów ściekowych`,
`wapnowanie osadów ściekowych`, `wapno do szamba`, `proces higienizacji osadów ściekowych`.
Baseline: 230 wyświetleń nad progiem i **zero kliknięć**, więc każde kliknięcie na tych frazach
jest zmianą jakościową. Drugi wskaźnik: czy kategoria przesuwa się wobec poradnika na czterech
wspólnych frazach.
