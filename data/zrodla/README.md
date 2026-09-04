# Źródła merytoryczne — IUNG-PIB (T-067)

Pliki źródłowe do twierdzeń o wapnowaniu, które publikujemy na agria.pl i które liczy kalkulator.
Zasada projektu: **parametry i zalecenia biorą się z kart producentów, rozporządzeń albo publikacji
naukowych — nigdy z rozumowania** (memory `feedback_agria_params_from_datasheets`).
Do 04.09.2026 terminarz `/jak-stosowac-wapno-nawozowe/` cytował IUNG-PIB, a w repo nie było ani
jednego pliku źródłowego — ten katalog spłaca ten dług.

## Co tu leży

| Plik | Tytuł, autorzy | Wyd. | ISBN | Stron |
|---|---|---|---|---|
| `IUNG-PIB-2021-poradnik-wapnowania-gleb-gruntow-ornych.pdf` | *Poradnik wapnowania gleb gruntów ornych* — Hołubowicz-Kliza G., Jadczyszyn T., Sułek A. | IUNG-PIB, Puławy 2021 | 978-83-7562-378-9 | 70 |
| `IUNG-PIB-2022-zasady-ustalania-dawek-wapna.pdf` | *Zasady ustalania dawek wapna w doradztwie nawozowym* — Jadczyszyn T., Lipiński W. | IUNG-PIB, Puławy 2022 | 978-83-7562-385-7 | 19 |

Pobrane **04.09.2026** ze stron instytutu (dostęp otwarty, publikacje finansowane z dotacji celowej
MRiRW / projektu INTER-NAW):

- https://iung.pl/dotacja_celowa/dc_2021/publikacje/poradnik_wapnowania_gleb.pdf
- https://dpr.iung.pl/wp-content/uploads/Zasady_ustalania_dawek_wapna_2022_cyfrowy.pdf

Sumy kontrolne SHA-256:

```
9c8485d0ae178725283426443b6398f7ed7939f84290cac1cbaf11fc00f2aff6  IUNG-PIB-2021-poradnik-wapnowania-gleb-gruntow-ornych.pdf
c6afbb8e987bd4d1909788a4b0257ac5c84b51d21409b3e63f9a8a879a44a146  IUNG-PIB-2022-zasady-ustalania-dawek-wapna.pdf
```

Pliki `.txt` to warstwa do wyszukiwania i do skryptu weryfikacyjnego — `pdftotext -layout <plik>.pdf`,
regenerowalne w każdej chwili. **PDF-y zostają w repo jako źródło, nie trafiają na agria.pl** —
cytujemy je z podaniem tytułu, wydawcy, roku i numeru tabeli, a czytelnik pobiera je od instytutu.

## Mapa cytowań — co skąd bierzemy

| Twierdzenie u nas | Gdzie | Źródło |
|---|---|---|
| Tabela „kiedy wolno, kiedy nie" (pożniwne = najlepszy termin, przedsiewne wiosenne = nie stosować, pielęgnacyjne wyjątkowo pogłównie na ziemniaki) | `/jak-stosowac-wapno-nawozowe/` | **2021, tab. 18** „Miejsce wapnowania w systemie zabiegów agrotechnicznych", s. 52 (źródło pierwotne: Boguszewski W., 1980) |
| Trzy grupy reakcji upraw na zakwaszenie (pH 6,0–7,5 / 5,0–6,5 / <5,0) | `/jak-stosowac-wapno-nawozowe/` | **2021, tab. 8** „Reakcja roślin na zakwaszenie gleby", s. 33 (źródło pierwotne: Szczepaniak W., 2017) |
| Ziemniak najsłabiej reaguje na wapnowanie | jw. | **2021, s. 34** — szereg „kukurydza = burak → jęczmień = pszenica → owies → żyto → ziemniak" |
| Parch zwykły a wapnowanie; pogłównie w redliny **0,5–0,75 t CaO/ha** | jw. | **2021, s. 50** |
| Lucerna i koniczyna — wapno pod roślinę ochronną, lucerna dodatkowo jesienią w drugim roku | jw. | **2021, s. 50** |
| Duże dawki dzielić: **3/4 jesienią przed orką, 1/4 w drugim roku** | jw. | **2021, s. 49** |
| Nie wysiewać na mokrą glebę ani w deszcz | jw. | **2021, s. 49** |
| Przykład podziału: gleba ciężka pH 4,0 → 9,8 t CaO = 6,0 + 3,8 | jw. | **2022, „Dawki CaO na gruntach ornych", s. 9** |
| Tablice dawek kalkulatora — 4 kategorie gruntów ornych po 0,1 pH | moduł `liming-calculator` | **2022, s. 7–9** (grunty orne) i **s. 9–10** (użytki zielone wg zawartości C) |
| Kategorie agronomiczne gleb, ocena odczynu, klasy potrzeb wapnowania | zaplecze kalkulatora | **2022, tab. 1–3, s. 5–6**; dawki zbiorcze w tab. 4, s. 6 |
| Przeliczenie dawki CaO na tony nawozu wg % CaO | kalkulator, dobór produktu | **2022, tab. 5, s. 12** |

## Weryfikacja tablic kalkulatora wobec źródła

`scripts/weryfikacja_tablic_iung.py` parsuje publikację 2022 i `class-iung-data.php`, po czym
porównuje je wiersz po wierszu. Stan 04.09.2026:

```
Porównanych wierszy: 100 (grunty orne 78, użytki zielone 22)
ROZJAZDY (1):
  ⚠️ [ciezka] pH 4.4: źródło (7.0, 6.0, 0.0) ≠ kod (7.0, 6.0, 1.0)
```

**99 na 100 wierszy zgadza się co do dziesiątej tony.** Jedyna różnica to podział dawki dla gleby
ciężkiej o pH 4,4: publikacja podaje dawkę **7,0 t CaO**, część I **6,0** i w kolumnie części II
myślnik — co się nie sumuje. Ta sama luka jest w obu publikacjach (2022 s. 9 oraz 2021 tab. 17, s. 47),
potwierdzona dwoma niezależnymi ekstraktorami tekstu (`pdftotext -layout` i `pypdf`), więc nie jest
artefaktem konwersji, tylko przeoczeniem w samym źródle. Nasz kod ma tam **1,0**, czyli domyka
arytmetykę. **Dawka całkowita jest identyczna** (7,0 t), różnica dotyczy wyłącznie rozpisania jej
na dwa lata. Zostawione bez zmian — poprawianie kodu „pod literę" dałoby użytkownikowi rozpiskę,
która się nie sumuje. Zgłoszone jako świadome odstępstwo, nie jako błąd.

## Uwagi

- **Obie tabele terminowe mają źródła pierwotne sprzed lat** — tab. 18 za Boguszewskim (1980),
  tab. 8 za Szczepaniakiem (2017). Terminarz cytuje pierwotne źródło przy tab. 18, a przy trzech
  grupach upraw pisze samo „IUNG-PIB dzieli gatunki" — do wyrównania przy najbliższej edycji tej strony.
- Publikacja 2022 **nie zawiera** rozdziału o terminach ani o uprawach — to poradnik 2021 jest
  źródłem dla terminarza, a 2022 dla dawek. Przy cytowaniu nie mieszać.
- Tabele dawek w obu publikacjach są tożsame (2021 tab. 15–17 = 2022 „Dawki CaO na gruntach ornych"),
  obie odsyłają do Jadczyszyn T., 2021. Cytujemy 2022 jako nowszą i zwięźlejszą.
