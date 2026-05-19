# Dane produktowe AGRIA — Mapowanie WooCommerce → Katalog

## Źródło danych
Eksport WooCommerce CSV: kolumny Rodzaj, SKU, Nazwa, Krótki opis, Opis (HTML z tabelami), Kategorie.
Parametry techniczne: wewnątrz kolumny Opis w tabelach HTML `<table>`.

## Lista produktów do katalogu (22 szt.)

### Z WooCommerce (18 produktów, bez Kredy czarnej):

| # | Nazwa WooCommerce | ID katalog | Kategorie |
|---|-------------------|-----------|-----------|
| 1 | Wapno nawozowe tlenkowe Agrobielik 70 | AGR-001 | Rolnictwo, Rybactwo, Sadownictwo, Hurtownie |
| 2 | Wapno nawozowe tlenkowe Agrobielik 90 | AGR-002 | Rolnictwo, Rybactwo, Oczyszczalnie, Hurtownie |
| 3 | Wapno nawozowe tlenkowe Oxyfertil 90 | AGR-003 | Rolnictwo, Rybactwo, Oczyszczalnie, Hurtownie |
| 4 | Wapno nawozowe tlenkowe zawierające magnez | AGR-004 | Rolnictwo, Hurtownie |
| 5 | Mieszanka tlenkowo-węglanowa | AGR-005 | Rolnictwo, Sadownictwo |
| 6 | Wapno nawozowe weglanowe bez magnezu — Odmiana 04 | AGR-006 | Rolnictwo, Sadownictwo, Hurtownie |
| 7 | Wapno nawozowe weglanowe bez magnezu — Odmiana 05 | AGR-007 | Rolnictwo, Sadownictwo |
| 8 | Wapno nawozowe weglanowe bez magnezu granulowane | AGR-008 | Rolnictwo, Sadownictwo, Hurtownie |
| 9 | Wapno nawozowe weglanowe zawierajace magnez — Odmiana 04 | AGR-009 | Rolnictwo, Sadownictwo |
| 10 | Wapno nawozowe weglanowe zawierajace magnez — Odmiana 05 | AGR-010 | Rolnictwo, Sadownictwo |
| 11 | Wapno nawozowe weglanowe zawierajace magnez granulowane | AGR-011 | Rolnictwo, Sadownictwo, Hurtownie |
| 12 | Dolomit | AGR-012 | Rolnictwo, Hurtownie |
| 13 | Kreda nawozowa granulowana | AGR-013 | Rolnictwo, Rybactwo, Hurtownie |
| 14 | Kreda nawozowa sypka | AGR-014 | Rolnictwo, Rybactwo, Hurtownie |
| 15 | Kreda pastewna | AGR-015 | Rolnictwo (Paszarstwo), Hurtownie |
| 16 | Kreda malarska | AGR-016 | Hurtownie, Rolnictwo |
| 17 | Wapno palone mielone wysokoreaktywne | AGR-017 | Oczyszczalnie |
| 18 | Wapno hydratyzowane Bielik | AGR-018 | Budownictwo, Oczyszczalnie |

### Tylko w katalogu (4 produkty, brak w WooCommerce):

| # | Nazwa | ID katalog | Kategorie |
|---|-------|-----------|-----------|
| 19 | Agrobielik 90 Frakcja 2–8mm | AGR-002F | Rolnictwo, Rybactwo |
| 20 | Cement budowlany | AGR-019 | Budownictwo |
| 21 | Kruszywo drogowe | AGR-020 | Drogownictwo |
| 22 | Wapno palone drogownictwo | AGR-021 | Drogownictwo |

## USUNIĘTE z katalogu
- Kreda czarna (jeziorna) z kwasami humusowymi — decyzja klienta

## Mapowanie pól WooCommerce → PROD

```
WooCommerce CSV          →  PROD (ExtendScript)
─────────────────────────────────────────────────
Nazwa                    →  PROD.name (skrócona do druku)
Krótki opis              →  baza do PROD.shortDesc (przerobić!)
Opis > <h2> pierwszy     →  PROD.descHead
Opis > <h2> drugi        →  PROD.sectionHead
Opis > bullety <strong>  →  PROD.bullets[] (5 szt, przepisać)
Opis > <table> parametry →  PROD.params[][] (15 wierszy)
Opis > tekst główny      →  PROD.longDesc (napisać od nowa)
Kategorie                →  tagi segmentów na karcie
```

## 15 parametrów tabeli (kolejność w katalogu)

1. Zawartość CaO
2. Reaktywność
3. Typ reakcji
4. Forma fizyczna
5. Frakcja
6. Zastosowanie funkcjonalne
7. Efekt zastosowania
8. Dawkowanie
9. Szybkość działania
10. Dodatkowe zastosowanie
11. Segment
12. Forma dostawy
13. Magazyn
14. Producent
15. Dostępność

## Wzorzec PROD — Agrobielik 70 (gotowy, przetestowany)

```javascript
var PROD = {
    name: "AGROBIELIK 70",
    descHead: "Agrobielik 70: szybka korekta pH gleb i stawów",
    shortDesc: "Szybkodziałające wapno tlenkowe o reaktywności ~100%...",
    longDesc: "Agrobielik 70 to flagowy produkt AGRIA...",
    sectionHead: "Szybkie odkwaszanie\ri wzrost plonów",
    benefitsHead: "Kluczowe korzyści",
    bullets: [
        "Szybka korekta pH — efekty widoczne w 2–4 tygodnie...",
        "Uniwersalność zastosowania — gleby, sady, stawy...",
        "Wysoka reaktywność (~100%) — pełne wykorzystanie CaO...",
        "Elastyczność dostaw — luz, big-bag, worki...",
        "Stabilność parametrów — Nordkalk + 35 lat AGRIA..."
    ],
    params: [
        ["Zawartość CaO", "min. 70% CaO"],
        ["Reaktywność", "~100%"],
        // ... 15 wierszy
    ]
};
```

## Zasady pisania treści pod druk

### shortDesc (max 3 zdania)
Format: [Typ produktu] o [kluczowy parametr]. Przeznaczone do [zastosowanie]. [Forma dostawy + logistyka].

### bullets (5 pozycji)
Format: **Cecha** — efekt/korzyść dla klienta, konkretna liczba jeśli możliwa.

### descHead
Format: [Nazwa]: [główna korzyść w 5-6 słowach]

### sectionHead
Format: [Korzyść 1]\r[Korzyść 2] (2 linie, max 4 słowa każda)

### longDesc
3-4 zdania: co to jest → jak działa → dla kogo → producent/marka.
Bez powtarzania parametrów z tabeli.
