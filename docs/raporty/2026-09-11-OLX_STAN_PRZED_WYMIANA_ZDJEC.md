# OLX AGRIA — stan przed wymianą zdjęć (11.09.2026)

Punkt odniesienia dla wymiany pierwszego zdjęcia na zdjęcia „z placu” z napisem (mockup
zaakceptowany 11.09: `auratest.pl/fe4f58fec53ctmp/agria-olx-mockup-wymiana-zdjec-v2-2026-09-11.html`).
Pomiar `statystyki.py --zapisz` o **12:08**, pilot podmiany ruszył o 12:11, więc liczby są w całości sprzed zmiany.
Źródło: `data/olx/statystyki.json` (pomiar nr 9), backup ogłoszeń: `data/backups/olx-zdjecia-v4-przed-2026-09-11-1210.json`.

## Stan

| | |
|---|---|
| Ogłoszenia | 200 / 200 odpytanych, wszystkie `active`, emisja do 19.09, pakiet do 16.09 |
| Odsłony (od wystawienia) | **1 137** |
| Odsłony numeru | **36** |
| Obserwujący | **31** |
| Ogłoszenia z choć jedną odsłoną numeru | 30 |
| Ogłoszenia z zerem odsłon | 9 |

## Tempo w kolejnych oknach

| Okno | Dni | Odsłony | Na dobę | Odsłony numeru | Obserwujący |
|---|---|---|---|---|---|
| 21.08 → 24.08 | 2,87 | +187 | 65,1 | +2 | +5 |
| 24.08 → 25.08 | 1,10 | +59 | 53,8 | +7 | +0 |
| 25.08 → 28.08 | 3,21 | +268 | 83,4 | +12 | +6 |
| 28.08 → 31.08 | 2,69 | +160 | 59,5 | +5 | +4 |
| 31.08 → 01.09 | 1,05 | +41 | 38,9 | +2 | +0 |
| 01.09 → 07.09 | 5,95 | +188 | 31,6 | +5 | +4 |
| **07.09 → 11.09** | **4,19** | **+114** | **27,2** | **+2** | **+2** |

**Ruch spada od końca sierpnia** — z 60–83 odsłon na dobę do 27–32. Punktem odniesienia dla wymiany zdjęć
jest więc ostatnie okno (**27,2 odsłony na dobę, 2 odsłony numeru w 4,2 dnia**), nie sierpień. Szczyt roku
w wapnie nawozowym to sierpień (memory `project_agria_sezon_sierpniowy`), więc wynik „bez zmian” w poniedziałek
przy spadającym trendzie nie znaczy „bez efektu”.

## Per wariant (11.09, 12:08)

| Wariant | Ogł. | Odsłony | Odsł. numeru | Odsłon / ogł. | Odsłony 07→11.09 | Numer 07→11.09 |
|---|---|---|---|---|---|---|
| Węglanowo-magnezowe odm. 05 | 8 | 71 | 1 | 8,9 | 7 | 0 |
| Agrobielik 90 | 25 | 188 | 5 | 7,5 | 19 | 0 |
| Węglanowo-magnezowe granulowane | 18 | 131 | 1 | 7,3 | 10 | 0 |
| Węglanowo-magnezowe odm. 04 | 12 | 76 | 1 | 6,3 | 10 | 0 |
| Węglanowe odm. 04 | 20 | 121 | 6 | 6,0 | 11 | 0 |
| Agrobielik 70 — gleba | 32 | 178 | 4 | 5,6 | 17 | 0 |
| Kreda nawozowa sypka | 16 | 87 | 3 | 5,4 | 7 | 1 |
| Węglanowe granulowane | 20 | 104 | 5 | 5,2 | 7 | 0 |
| Oxyfertil 90 | 8 | 40 | 3 | 5,0 | 5 | 0 |
| Kreda nawozowa granulowana | 15 | 74 | 5 | 4,9 | 10 | 1 |
| Agrobielik 70 — staw | 22 | 64 | 2 | 2,9 | 10 | 0 |
| Kreda pastewna | 4 | 3 | 0 | 0,8 | 1 | 0 |

## Odczyt w poniedziałek 14.09

Cron `statystyki.py` o 7:35 w poniedziałek zapisze pomiar sam. Porównanie: odsłony na dobę w oknie
**11.09 12:08 → 14.09** wobec **27,2** z okna 07→11.09 (i 59,5 z analogicznego okna czwartek → poniedziałek
28.08 → 31.08, dla skali). Okno po zmianie obejmuje weekend, a niedziela jest w tej kategorii najmocniejsza
(memory `project_agria_ads_sezonowosc`) — okno 07→11.09 go nie ma, więc część wzrostu może być kalendarzowa.
Drugi odczyt po pełnym tygodniu: pomiar poniedziałkowy 21.09 wobec 01.09 → 07.09 (31,6 na dobę) —
**pod warunkiem, że Paweł odnowi pakiet przed 16.09** (T-105).
