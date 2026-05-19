# Katalog drukowany AGRIA — specyfikacja

> Wersja skrócona. Pełna treść (z układami stron i opisami produktów) w `assets/KATALOG_AGRIA_24STR_KOMPLET.txt`.

---

## Format

| Parametr | Wartość |
|----------|---------|
| Format | A4 pionowo (210×297 mm) |
| Liczba stron | 24 (wielokrotność 4 dla saddle stitch) |
| Oprawa | Zszywki metalowe (saddle stitch, środek grzbietu) |
| Bleed | 3 mm na każdą krawędź |
| Safe zone | 5 mm od krawędzi tnięcia |
| Marginesy | top 12mm, bottom 12mm, left/right 15mm |
| Facing pages | false (jednostronne) |

## Stack drukarski

| Element | Specyfikacja |
|---------|--------------|
| Okładka (str. 1, 24) | 250 g Munken Lynx Rough mat |
| Wnętrze (str. 2–23) | 135 g Munken Pure Cream półmat |
| Druk | CMYK (Pantone opcjonalnie dla limonkowego — Pantone 382 C) |
| Wykończenie | Lakier UV selektywny na okładce |
| Plik finalny | PDF/X-1a:2001 (300 dpi, fonty embedded/outlined) |

## Nakłady i koszty

| Faza | Ilość | Koszt netto |
|------|-------|-------------|
| Proof | 10 szt | ~500 PLN |
| Seria 1 | 500 szt | 2 000 – 2 500 PLN |
| Seria 2 | 1 000 szt | 3 500 – 4 500 PLN |

Pełna lista zdjęć: 24 sztuki — sesja własna 1 500–2 500 PLN, alternatywa stock 360–600 USD.

---

## Struktura 24 stron

| Strona | Zawartość |
|--------|-----------|
| 1 | Okładka |
| 2 | O firmie (35 lat, 2 oddziały, flota) |
| 3–4 | Segmenty zastosowań (rolnictwo / rybactwo / oczyszczalnie / budownictwo) — spread |
| 5 | Jak dobrać produkt (3 grupy szybkości działania) |
| 6–23 | **18 kart produktów** (1 produkt = 1 strona A4) |
| 24 | Tył okładki + kontakt |

## 18 kart produktów (kolejność)

| Strona | ID | Produkt |
|--------|----|---------|
| 6 | AGR-001 | Wapno tlenkowe Agrobielik 70 |
| 7 | AGR-002 | Wapno tlenkowe Agrobielik 90 |
| 8 | AGR-002F | Agrobielik 90 frakcja 2–8 mm |
| 9 | AGR-003 | Mieszanka tlenkowo-węglanowa |
| 10 | AGR-004 | Wapno węglanowe Celiny |
| 11 | AGR-005 | Wapno węglanowe granulowane |
| 12 | AGR-006 | Wapno Laskowa (Mg 17–19%) |
| 13 | AGR-007 | Wapno Winna (Mg 8–20%) |
| 14 | AGR-008 | Wapno Jawica (Mg 8–10%) |
| 15 | AGR-009 | Wapno granulowane z Mg |
| 16 | AGR-012 | Kreda nawozowa granulowana |
| 17 | AGR-013 | Kreda nawozowa sypka |
| 18 | AGR-014 | Kreda pastewna |
| 19 | AGR-010 | Wapno palone wysokoreaktywne |
| 20 | AGR-011 | Wapno hydratyzowane Bielik |
| 21 | AGR-015 | Cement budowlany |
| 22 | AGR-016 | Kruszywo drogowe |
| 23 | AGR-017 | Wapno palone drogownictwo |

**Wycięte z katalogu:** Kreda czarna (jeziorna) — decyzja klienta.

---

## Szablon karty produktu

Każda karta (str. 6–23) zawiera:

1. **Header:** Logo AGRIA + pasek główny + ID produktu (AGR-XXX) limonkowy
2. **Nazwa produktu** (duża, ciemnozielona) + nazwa techniczna
3. **Zdjęcie produktu** okrągłe (clipping mask) — lewa kolumna
4. **Nagłówek opisowy** + **opis krótki** (3 zdania)
5. **Nagłówek sekcji** (2 linie, korzyść 1 / korzyść 2)
6. **Kluczowe korzyści** — 5 bullet pointów (cecha → korzyść)
7. **Opis długi** (3–4 zdania)
8. **Tabela 15 parametrów** (natywna tabela InDesign):
   - Zawartość CaO
   - Reaktywność
   - Typ reakcji
   - Forma fizyczna
   - Frakcja
   - Zastosowanie funkcjonalne
   - Efekt zastosowania
   - Dawkowanie
   - Szybkość działania
   - Dodatkowe zastosowanie
   - Segment
   - Forma dostawy
   - Magazyn
   - Producent
   - Dostępność
9. **Stopka:** QR kod (`agria.pl/produkt/[slug]`) + telefon + ikona

---

## Stan realizacji

| Strona | Status |
|--------|--------|
| Okładka + str. 2–5 | szkic, do dopracowania |
| Karta Agrobielik 70 (str. 6) | ✅ **gotowa** — szablon JSX w `assets/AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx` |
| Karty str. 7–23 (17 sztuk) | ⏳ do wygenerowania (duplikacja JSX + dane z MCP) |
| Tył okładki (str. 24) | szkic |

**Następny krok:** napisanie skryptu batchowego, który dla każdego z 17 produktów:
1. Pobierze dane przez `Agria.pl:catalog_product`.
2. Wygeneruje plik `.jsx` na wzór `AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx`.
3. Wymaga ręcznej podmiany zdjęć i QR kodów w InDesign (rzeczy spoza ExtendScript).
