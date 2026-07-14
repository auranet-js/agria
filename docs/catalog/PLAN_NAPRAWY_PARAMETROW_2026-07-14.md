# Plan naprawy parametrów produktowych — agria.pl

> Data: 2026-07-14. Status: **PRZYGOTOWANY, NIEWYKONANY.** Wymaga osobnej sesji z pełnym zrzutem bazy.
> Kontekst: `BACKLOG_SEZON_2026-07-14.md`, memory `feedback_agria_params_from_datasheets`.

---

## Dlaczego to trzeba zrobić

Około **jednej trzeciej atrybutów** produktowych w WooCommerce jest błędna. Dwie przyczyny:

1. **Bug importu.** Dane wpisano z przecinkami dziesiętnymi, a WooCommerce traktuje przecinek jako separator wartości atrybutu. `1,5–6 t/ha` rozpadło się na dwie wartości: `1` i `5-6 t/ha`. Stąd: dawkowanie `5-1`, frakcja `0-0`, `09mm`, `4-08mm`, efekt `Wzrost pH o 0`, forma dostawy `1- 0`, `4`, `8`.
2. **Parametry bez pokrycia w kartach producentów** — wartości nieznanego pochodzenia (np. Bielik `min. 72% CaO`).

Skutek biznesowy: na kartach B2B stoją liczby, na podstawie których rolnik dobiera dawkę na 30 ha, a oczyszczalnia liczy higienizację osadu. Odmiany 04 i 05 są sprzeczne z własnymi liczbami — konkurent zweryfikuje to w dwie minuty wg rozporządzenia.

---

## Hierarchia źródeł (ustalona 2026-07-14)

1. **Karta producenta** (DWU / CE / certyfikat ZKP) — zawsze wygrywa.
2. **Katalog AGRIA** (`Agria-katalog-2026-05-04-web.pdf`) — klient go zaakceptował, wydrukował i rozdaje. Prawomocne źródło tam, gdzie karty brak.
3. **Oferta handlowa AGRIA** — potwierdza formy dostawy, magazyny, składy kopalń.
4. **WooCommerce** — najniższa wiarygodność. **Nigdy nie jest źródłem prawdy.**

**Wyjątek:** katalogu NIE kopiujemy tam, gdzie jest fizycznie niemożliwy (pH > 14; kreda pastewna jako „egzotermiczna", choć to węglan wapnia). To idzie do errat, nie na stronę.

---

## Trzy kubełki

- **A — naprawiam:** pokrycie w karcie / katalogu / ofercie, albo jednoznacznie odtwarzalny bug importu.
- **B — usuwam (parkuję):** wartość ewidentnie błędna i nie ma czym zastąpić. **Lepiej brak parametru niż parametr fałszywy.** Dotyczy całego `pa_agria-ph` (żadna karta nie deklaruje pH), typu reakcji kredy pastewnej, odmian bez pokrycia, `pa_min-cao` tam, gdzie karta deklaruje sumę CaO+MgO.
- **C — do klienta:** brak jakiegokolwiek źródła. Kreda malarska, kreda czarna jeziorna (CaO), Celiny (konflikt odmiana 04 vs 05), jednostka kredy pastewnej (Ca czy CaO).

Pełna tabela decyzji per produkt/atrybut — w transkrypcie agenta weryfikującego (sesja 2026-07-14).

---

## ⚠️ Dlaczego NIE wykonano tego od razu

Cztery blokery, wszystkie realne:

1. **Brak pełnego backupu bazy.** Operacja przepina **~45 relacji** w `term_relationships` i zakłada sztuczną taksonomię parkingową z ręcznie nadanymi ID (9001–9008). MCP nie zrobi `mysqldump` → potrzebny zrzut przez phpMyAdmin/FTP. Dzisiejsze poprawki były cofalne jednym UPDATE-em; ta — nie.
2. **SQL jest niekompletny.** Pary `object_id`/`term_taxonomy_id` dla fragmentów atrybutu `pa_agria-efekt` trzeba wygenerować zapytaniem kontrolnym — agent świadomie ich nie wypisał z pamięci.
3. **Część roboty nie jest SQL-em.** Gdy atrybut schodzi do zera, klucz zostaje w zserializowanej meta `_product_attributes` → WooCommerce renderuje **pusty wiersz**. Usunięcie wymaga `$product->set_attributes()` przez API WC (snippet PHP), nie ręcznego stringa.
4. **Elementor może mieć parametry zaklepane w treści.** Produkt **320** zawiera string „CaO" w `_elementor_data`. Jeśli tabela parametrów jest wklepana w widget, a nie generowana z atrybutów — **poprawka w bazie nie zmieni strony**. Ten sam mechanizm ugryzł nas dziś przy sitemapie (patrz memory `project_agria_render_caching`).

---

## Kolejność wykonania (osobna sesja)

1. **Zrzut bazy** (phpMyAdmin) → `~/backups/agria/<data>/`.
2. **Guard:** `SELECT MAX(term_id), MAX(term_taxonomy_id)` (jeśli ≥ 9000 — przenumerować parking).
3. **Skan Elementora:** `SELECT post_id FROM wpfz_postmeta WHERE meta_key='_elementor_data' AND (meta_value LIKE '%CaO%' OR meta_value LIKE '%pH%')` — ustalić, które produkty mają parametry zaklepane w treści.
4. **Rename in place** (`wpfz_terms`) — pokrywa ~60% napraw, zero ruszania relacji, zero sierot. Uwaga na unikalność slugów.
5. **Nowe termy + repointy** relacji.
6. **Parkowanie** kubełka B.
7. **Przeliczenie `count`** w `term_taxonomy`.
8. **PHP przez WC API** — czyszczenie `_product_attributes`.
9. **Elementor** — poprawa treści dla produktów z pkt 3 + `_elementor_element_cache` = `a:0:{}`.
10. **Weryfikacja renderu** na żywo (cache-bust CDN nazwa.pl), nie tylko bazy.

**Nie dotykamy `pa_agria-segment`** — siedzi na nim filtr JetSmartFilters (JSF 1471).

---

## Nowe atrybuty normowe (mocne B2B, dziś ich NIE MA)

| Atrybut | Produkty z twardym pokryciem |
|---|---|
| **Wapno czynne %** (min. 80%) | 309 (Bielik), 320 (palone mielone) — karty CL 90-S / CL 90-Q |
| **Klasa normowa PN-EN 459-1** | 309 → `CL 90-S`; 320 → `CL 90-Q (R5, P1)` |
| **CaO + MgO (suma)** | 302, 309, 313, 318, 319, 320 |
| **Reaktywność wg PN-EN 459-2** | 320 → `R5, t60 ≤ 2 min` |

**Suma CaO+MgO, nie CaO osobno, jest parametrem regulacyjnym** dla wapna z magnezem — dlatego nasze odmiany dziś nie zgadzają się z własnymi liczbami.

„Wapno czynne" i „klasa normowa" to dokładnie to, czego szukają oczyszczalnie i drogownictwo w specyfikacjach przetargowych. Konkurencja podaje gołe procenty.

---

## ERRATY DO KATALOGU (przy dodruku)

1. **„od 35 lat"** → **37 lat** (firma od 1989).
2. **Wiersz „Odczyn pH"** — usunąć z kart (mieszanka `>12`, kreda pastewna `>12`, Bielik `>13`, wapno palone `>16`). Skala pH kończy się na 14, żadna karta producenta pH nie deklaruje. Jeśli przekaz ma zostać — wyłącznie jako **efekt**: „pH osadu po zastosowaniu > 12".
3. **Kreda pastewna: „Typ reakcji: Egzotermiczna"** → usunąć. To węglan wapnia (materiał paszowy), reakcji egzotermicznej nie ma.
4. **Bielik: „Zawartość CaO min. 90%"** → `CaO+MgO ≥ 90%, wapno czynne ≥ 80% (CL 90-S wg PN-EN 459-1)`.
5. **Wapno palone mielone: „min. 90% CaO"** → `CaO+MgO ≥ 90%, wapno czynne ≥ 80% (CL 90-Q, R5)`.
6. **⚠️ Agrobielik 90: „min. 90% CaO"** → karta Nordkalk (odmiana 01) gwarantuje **min. 80%**, wynik badań 94,9%. Rekomendacja: *„odmiana 01 — CaO min. 80% (gwarantowane), typowo ~95%"*.
   **DECYZJA HANDLOWA JANKA / AGRII — to obniża liczbę, którą klient ma w druku i którą sprzedaje.** Nie zmieniam bez akceptu.
7. **Wapno tlenkowe z Mg: „CaO+MgO 70/25%"** → karta Lhoist (Oxyfertil Mg) mówi **75/25, frakcja 1–3 mm, odmiana 01**. Ustalić, który produkt AGRIA faktycznie bierze.
8. **Węglanowe z Mg granulowane: „31% CaO + 16% MgO"** → karta Grankal: **CaO min. 30%, MgO min. 17%**.
9. **Kreda pastewna „min. 37% CaO"** → w karcie analogu to **37% Ca** (370 g/kg), nie CaO. Potwierdzić jednostkę.
10. **Kreda nawozowa granulowana** — jeśli podajemy odmianę, to `06a` (kopalina), nie `06` (produkcja uboczna: posodowe/defekacyjne).

---

## Lista do AGRII — prośba o karty

Potrzebne karty produktów / Deklaracje Zgodności / atesty OSChR (aktualna partia). **Będą jedynym źródłem parametrów publikowanych na agria.pl.**

1. **Kopalnia Celiny (Hochel)** — wapno węglanowe: odmiana **04** (oferta: CaO 50–54%) czy **05** (strona: min. 40%)? Konflikt.
2. **Kopalnia Drugnia (Pierzchnica)** — kreda nawozowa sypka: odmiana, CaO.
3. **Kreda malarska (Bukowa / Lhoist)** — karta techniczna.
4. **Kreda czarna jeziorna (Grankal, Draby)** — czy to HumiPlus? Karta z zawartością CaO.
5. **Kreda pastewna (Celiny / Lhoist)** — etykieta paszowa: **Ca czy CaO**, frakcje, GMP+.
6. **Oxyfertil Ca 90 (Lhoist)** — frakcja **3–7 czy 3–8 mm**.
7. **Oxyfertil Mg (Lhoist)** — **75/25 czy 70/25**, frakcja, odmiana.
8. **Grankal** (Vital / Magnezowy / HumiPlus) — DZ z odmianą (magnezowy: 30+17 = 47% **nie spełnia** progu odmiany 04).
9. **KZK Kornica** — DZ z odmianą i CaO.
10. **Industria** (Jaźwica / Laskowa / Winna) — DZ per kopalnia.
11. **Nordkalk** — DWU/CE dla Bielik CL 90-S i wapna palonego CL 90-Q (**potrzebne oczyszczalniom do przetargów**).

**Do rozstrzygnięcia:** katalog ma **dwa warianty Agrobielika 90** (0–3 mm sypki, 2–8 mm kruszony), na stronie jest jeden produkt. Rozdzielamy?
