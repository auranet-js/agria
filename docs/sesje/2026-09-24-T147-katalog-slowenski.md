# T-147 „katalog PDF po słoweńsku” — 24.09.2026

**Zlecenie `[J 24.09]`:** przetłumaczyć katalog `Agria-katalog-2026-05-13-druk.pdf` (Drive AGRIA) na słoweński.
Katalog nie będzie drukowany, potrzebny tylko PDF. Treść 1:1, sam język.

**Wynik:** `assets/print/catalog/Agria-katalog-2026-05-13-SL-web.pdf` — 23 strony, 10,5 MB,
bez spadów i pustej strony 2 (była pod druk), obrazy 150 dpi, `Lang sl-SI`.
Kopia robocza: `auratest.pl/fe4f58fec53ctmp/agria-katalog-2026-05-13-SL-2026-09-24.pdf`
i słownik PL→SL `…/agria-katalog-SL-slownik-2026-09-24.csv`.

## Jak zrobione

Bez InDesigna (decyzja Janka: „tylko PDF”). Pipeline w `scripts/katalog_sl/`:

1. `engine.py` składa akapity z linii PDF (styl + stała interlinia + kolumna), wycina polski tekst
   redakcją i wlewa słoweński w sloty oryginalnych linii — zachowuje opływanie okrągłych zdjęć,
   justowanie, wyrównania, runy dwukolorowe w tytułach.
2. Fonty: pełne Bai Jamjuree + Plus Jakarta Sans (OFL, `fonts/`). Grubość PJS mierzona pikselowo,
   bo w PDF wszystkie instancje zmiennego fontu nazywają się `Regular` (nagłówki to Bold, nie SemiBold jak w skillu).
3. `shadows.py` — cienie białych nagłówków to maski luminancji (obraz szary w SMask); podmieniane
   na rozmyty obraz nowego tekstu, rozmycie skalibrowane na polskim oryginale.
4. `tr_final.json` — słownik PL→SL, jedyne miejsce edycji treści. `\n` w wartości = wymuszone łamanie.
5. Uruchomienie (venv z PyMuPDF + Pillow: `~/scratch/pdf-venv`):
   `python build.py <druk.pdf> sl.pdf && python export_web.py sl.pdf wynik.pdf`

## Decyzje `[J 24.09]`

- Kreda pastewna: **usunięte wiersze pH >12 i „reakcja egzotermiczna”** (błąd oryginału, CaCO₃) — jak na stronie #307 od 11.09.
- Wapno palone mielone: **pH >16 → >12** (skala kończy się na 14; opis obok mówi >12).
- „Efekt do roku” vs 3–6 mies. (odmiana 05) — zostaje 1:1.
- Dostawa: „Dobava: Poljska 2–5 dni, tujina po dogovoru”; „v številnih regijah” zamiast „vojvodstvih”
  (Kasjan chciał „do uzgodnienia” w kontekście dostawy).
- Terminologia: kopalnie wapienia = **kamnolom** (nie rudnik), gleby średnie = **srednje težka tla**,
  „wypalanie próchnicy” = **razgradnja humusa**.

## Korekta zewnętrzna

Raporty Google Translate i Gemini: wszystkie „literówki” to błędy ich OCR obrazu strony — żadnej nie ma
w warstwie tekstowej (sprawdzone wyszukiwaniem). Raport ChatGPT: przyjęte kalki stylistyczne (lista w słowniku)
i **jeden prawdziwy błąd składu** — sklejona justowana linia na s. 13, poprawiony w silniku.
Odrzucone: „Sipko” (odnosi się do „apno”), „trošena” (poprawna liczba podwójna), „Svetokriško vojvodstvo” (oficjalna nazwa).

## Otwarte

- **Tłumaczenie nie przeszło przez native speakera** — przed wysyłką do odbiorców w Słowenii warto.
- **Polski katalog (`.indd`) ma te same błędy parametrów** (kreda pastewna pH/egzotermia, wapno palone pH >16) — nie ruszane.
- QR i link prowadzą do polskiego kalkulatora na agria.pl.
