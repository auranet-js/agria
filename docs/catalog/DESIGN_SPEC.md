# Specyfikacja designu — Katalog AGRIA

## Format dokumentu

| Parametr | Wartość |
|----------|---------|
| Format | A4 (210×297mm) |
| Bleed | 3mm na każdą krawędź |
| Safe zone | 5mm od krawędzi tnięcia |
| Marginesy | top: 12mm, bottom: 12mm, left: 15mm, right: 15mm |
| Facing pages | false (jednostronne) |
| Oprawa | Saddle stitch (zszywki) |
| Strony | Wielokrotność 4 |

## Kolory CMYK

| Nazwa | CMYK | HEX (ref.) | Użycie |
|-------|------|------------|--------|
| Agria-Glowny | C32 M0 Y35 K69 | #354E33 | Nagłówki, paski, tła sekcji |
| Agria-Akcent | C53 M0 Y46 K19 | #61CE70 | Labele sekcji, tagi, przyciski |
| Agria-Drugorzedny | C14 M0 Y14 K45 | #798D7A | Nazwy techniczne, obrysy |
| Agria-Tekst | C16 M0 Y15 K58 | #596A5A | Tekst body, opisy, bullety |
| Agria-BG-Szare | C1 M0 Y3 K2 | #F8FBF3 | Tło wierszy tabeli (co drugi) |
| Paper | — | #FFFFFF | Tekst na ciemnym tle |

Źródło palety: Elementor Global Colors na agria.pl (nie stara specyfikacja katalogu).
Zweryfikować z ICC profilem drukarni przed finalnym eksportem.

## Fonty

| Rola | Rodzina | Grubość | Źródło |
|------|---------|---------|--------|
| Nagłówki | Plus Jakarta Sans | SemiBold (600) | Google Fonts |
| Tekst | Bai Jamjuree | Light (300) | Google Fonts |

Użytkownik musi zainstalować systemowo przed uruchomieniem skryptu InDesign.

## Layout karty produktowej (szablon Dolomit)

Układ strony A4 od góry do dołu:

```
┌─────────────────────────────────────┐
│ [Logo AGRIA]  ███ pasek główny ███  │  ~15mm
├─────────────────────────────────────┤
│                                     │
│    NAZWA PRODUKTU (duże, 2× skala) │  ~20mm
│                                     │
├──────────────┬──────────────────────┤
│ Nagłówek     │   Kluczowe korzyści  │
│ opisowy      │   • bullet 1         │  ~80mm
│              │   • bullet 2         │
│ Opis krótki  │   • bullet 3         │
│              │   • bullet 4         │
│ [ZDJĘCIE     │   • bullet 5         │
│  PRODUKTU]   │                      │
│              │   Opis długi...      │
│ Nagłówek     │                      │
│ sekcji       │                      │
├──────────────┴──────────────────────┤
│ PARAMETRY (tabela 15×2)             │  ~130mm
│ ┌──────────────┬───────────────────┐│
│ │ Parametr     │ Wartość           ││
│ │ Zawartość CaO│ min. 70% CaO     ││
│ │ ...          │ ...               ││
│ └──────────────┴───────────────────┘│
├─────────────────────────────────────┤
│ [QR] www.agria.pl   +48... [ikona] │  ~15mm
└─────────────────────────────────────┘
```

### Tabela parametrów
- Natywna tabela InDesign (nie fake ramki!)
- 15 body rows + 1 header row
- Kolumna 1 (parametr): ~60mm
- Kolumna 2 (wartość): ~125mm
- Wysokość wiersza: ~7mm (header: ~8mm)
- Styl nagłówka: Table-Head (biały na ciemnym)
- Styl wartości: Table-Value

### Zdjęcie produktu
- Okrągłe (clipping mask) w lewej kolumnie
- Zdjęcia ze strony: `H:/Mój dysk/AGRIA/www/zdjecia-do-strony/`
- Lub z WooCommerce media library
- Min. 300 dpi

### QR kod
- Generowany w InDesign: Obiekt → Wygeneruj kod QR
- URL: `https://agria.pl/produkt/[slug]`
- Embedded EPS w prostokącie ~15×15mm

### Logo
- Plik: `agria-logo-poziom-2026.png`
- Wersja biała na ciemnym tle (okładka, pasek górny)
- Wersja kolorowa w stopce

## Specyfikacja druku

| Parametr | Wartość |
|----------|---------|
| Papier okładka | 250g Munken Lynx Rough mat |
| Papier wnętrze | 135g Munken Pure Cream półmat |
| Druk | CMYK |
| Pantone opcjonalnie | Limonkowy = Pantone 382 C |
| Wykończenie | Lakier UV selektywny na okładce |
| Rozdzielczość | min. 300 dpi |
| Eksport | PDF/X-1a:2001 |
| Fonty | embedded / outlined |

## Nakłady

| Faza | Ilość | Koszt szacunkowy |
|------|-------|-----------------|
| Proof | 10 szt | 500 PLN |
| Seria 1 | 500 szt | 2000-2500 PLN |
| Seria 2 | 1000 szt | 3500-4500 PLN |
