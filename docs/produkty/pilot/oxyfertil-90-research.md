# Research — #312 Oxyfertil 90 (pilot T-136)

> 11.09.2026 · pełny stan karty: [`../oxyfertil-90.md`](../oxyfertil-90.md) (nie przepisuję) · dane nowe: `data/produkty/pilot/`
> GSC 2026-06-10 … 09-07 (`gsc-frazy-312.json`, `gsc-karty-90d.json`), 28 dni 08-11 … 09-07 (`gsc-karty-28d-2026-09-11.json`) ·
> SERP mobile 09–11.09 (`data/produkty/dfs/serp-tlenkowe-311-313-2026-09-10.json`, `data/seo/2026-09-09-serp-karty.json`, `serp-pilot-2026-09-11.json`) ·
> elementy stron z top 5: `serp-elementy-2026-09-11.json` (`scripts/serp_elementy.py`, sygnał obecności słów, nie ocena)

## 1. Frazy, które należą do tej karty

| fraza | wyszukań/mies. | nasze adresy w GSC (90 dni) | kolizja |
|---|---|---|---|
| oxyfertil | 30 | #312 64 wyśw. poz. 5,9 · stary adres `…/wapno-oxyfertil-90-frakcja-3-8mm-big-bag-1000kg/` (301) 19 wyśw. poz. 5,4 | 2 adresy, drugi to 301 — wygaśnie sam |
| wapno oxyfertil | 20 | #312 55 / 4 klik. / poz. 3,9 · stary adres 6 | jw. |
| oxyfertil 90 | 10 | #312 22 / 2 / 4,9 | brak |
| oxyfertil wapno · oxyfertil 90 cena · oxifertil | 10 · 10 · 0 | tylko #312 (poz. 6,3 / 1,8 / 9,5) | brak |
| wapno tlenkowe oxyfertil · oxyfertil cena · wapno oxyfertil cena · oxyfertil dawkowanie · oxyfertil lhoist | po 10 | 0 wierszy | — |

**Nie przypisuję do #312** (frazy wspólne, wracają w D1 albo przy innych kartach):
- `wapno tlenkowe 90` (20) — ten sam parametr ma #311 Agrobielik 90; dziś SERP: #312 abs 8, #311 abs 22. Title #312 nie otwiera się tą frazą.
- `wapno nawozowe tlenkowe` (50) — **6 naszych adresów**, najlepszy #313 poz. 13,4, #312 poz. 10 (7 wyśw.). Fraza rodzajowa czterech kart tlenkowych → D1.
- `lhoist` 480 · `lhoist tarnów opolski` 170 · `lhoist górażdże` 70 · `lhoist wapno` 30 — wspólne dla 6 kart Lhoist; SERP nawigacyjny (lhoist.com, local pack). Nazwa producenta i magazynów wchodzi do treści jako fakt, bez celowania.
- `higienizacja osadów ściekowych` 175 wyśw. · `wapnowanie osadów ściekowych` 134 — w całości `/wapno-do-oczyszczalni/` (poz. 13,5–16,6), która **nie listuje #312**. Zauważone, nie ruszam (listing = kategoria).

## 2. Co Google nagradza

| fraza | top 5 organicznie (abs) | co mają |
|---|---|---|
| `oxyfertil 90` | OLX CARLOS (2) · **agria #312 (3)** · chemirol PDF (4) · agrolok (5) · OLX lista (6) | ceny: OLX CARLOS 790 zł/t, agria 790 zł/t; producent Lhoist u wszystkich; frakcja u wszystkich; schemat `Product`+`Offer`: OLX, agria, agrolok |
| `wapno oxyfertil` (11.09) | OLX lista (2) · **agria (3)** · agrofoto forum (4) · agrolok (7) · flora-praszka PDF (9) | jw.; forum z dyskusją o dawkach |
| `oxyfertil` | lhoist.com (2) · OLX (4) · **agria (6)** · chemirol PDF (7) · flora-praszka PDF (8) | producent i dwie karty PDF dystrybutorów w top 5 |
| `wapno tlenkowe 90` | dobromir (1) · chemirol (3) · allegro (5) · skleprafish (6) · agroprofil (7) · **agria (8)** | dokumenty na chemirol (karta PDF), cena na skleprafish |

Wniosek z tabeli (fakty): na frazach z nazwą **karty PDF producenta lub dystrybutora stoją w top 5** (chemirol, flora-praszka) — dokument jest treścią, której Google szuka. AGRIA ma swoją kartę PDF na `/do-pobrania/`, a karta produktu do niej nie linkuje.
Nad nami na `oxyfertil 90` stoi ogłoszenie **CARLOS: ta sama cena 790 zł/t, „wz-tka wystawiana przez producenta Lhoist", odbiór własny**.

**PAA:** „Jakie jest wapno Oxyfertil?" · „Co daje wapno tlenkowe?" · „Czy tlenek wapnia jest szkodliwy?" · „Kiedy najlepiej podawać wapno?" · „Ile kosztuje 1 tona wapna granulowanego?" · „Jaka dawka wapna tlenkowego na hektar?" · „Które wapno jest lepsze: tlenkowe czy węglanowe?"

## 3. Czego szuka kupujący

- **Zapytania ofertowe z tej karty (2 z 11 w serwisie):** 27.07 — big-bag 1000 kg, 2 t, treść: *„Czy byłaby możliwa dostawa?"* · 24.08 — gospodarstwo rolne, Dolny Śląsk, big-bag, *„5 big baków"*. Oba z rolnictwa, oba pytają o dostawę, **żadne z oczyszczalni**.
- **GSC karty, 28 dni:** 15 klik. / 313 wyśw. / CTR 4,79% / poz. 5,6. Zapytania: `wapno oxyfertil` 32 wyśw. 3 klik. poz. 3,3 · `oxyfertil` 34 / 0 / 5,7 · `oxyfertil 90` 22 / 2 / 4,9 · `oxyfertil 90 cena` 4 / 1 / 1,8 · `wapno tlenkowe dawkowanie` poz. 1. Próg prywatności ukrywa większość kliknięć (90 dni: 27 z 38).
- Kupujący szuka **nazwy, ceny i dostawy**; frazy dawkowe z nazwą (`oxyfertil dawkowanie` 10/mies.) nie mają dziś żadnego wiersza.

## 4. Co z tego wynika dla treści (tylko fakty z karty PDF)

1. Utrzymać nazwę na frazach, na których karta już stoi (poz. 3–6) — title zaczyna się od „Oxyfertil 90".
2. Dołożyć to, co ma konkurencja w top 5, a my mamy w karcie PDF: **Lhoist jako producent w lead i title**, **link do karty PDF**, magazyny wysyłkowe, porównanie z Agrobielikiem 90 (karta PDF sama pisze „alternatywa… inny producent").
3. Kolejność zastosowań jak na karcie: oczyszczalnie → neutralizacja → rolnictwo interwencyjnie. Zapytania ofertowe przyszły z rolnictwa — dawka 1–3 t/ha i dostawa big-bagiem muszą być widoczne wysoko.
4. FAQ z PAA i zapytań: czym jest, dawka w rolnictwie, dawka w osadach, różnica z Agrobielikiem 90, dostawa/cena, dokumenty.
5. Usunąć twierdzenia bez źródła (lista w `../oxyfertil-90.md` §6): ~100% reaktywność, pH >12, +0,5–2 pH w 2–4 tyg., stawy 40–60 kg/1000 m³, „karty charakterystyki, certyfikaty".
