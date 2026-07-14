# Pomiar „pod wynik" — log przebudów i fraz-celów (GSC)

> Dowód konceptu strategii `SEO_STRATEGIA_POD_WYNIK_2026-07-08.md`. Dla każdej przebudowanej/nowej strony: data, fraza-cel, baseline pozycji, okno pomiaru (4–8 tyg.), wynik.
> Baseline domenowy GSC (18.05–14.06.2026): 46 klik / 1389 wyśw / CTR 3,3% / śr. poz. 13,9.

---

## #1 — /wapnowanie-gleby/ (post 2074)

| Pole | Wartość |
|---|---|
| **Data przebudowy** | 2026-07-09 |
| **URL** | https://agria.pl/wapnowanie-gleby/ |
| **Fraza-cel główna** | „ile wapna na hektar" (720/mc) |
| **Fraza-cel poboczna** | „ile wapna na ha" (720/mc) |
| **Baseline pozycji (2026-07-08)** | poz. **14** („ile wapna na hektar"), poz. **17** („ile wapna na ha") |
| **Zgłoszono do indeksacji** | 2026-07-09 (index-submit, URL_UPDATED) |
| **Okno pomiaru** | 4–8 tyg. → **kontrola ~2026-08-06 i ~2026-09-03** |
| **Cel** | strona 1 (poz. ≤10) na „ile wapna na hektar" |

### Co zmieniono (dźwignie)
- Quick-answer z liczbami (1–6 t CaO/ha wg pH i typu gleby) na górze, przed teorią — pod featured snippet / AI Overview.
- Nowa sekcja „Jak odczytać badanie gleby" (pH w KCl + kategoria agronomiczna).
- Box przeliczenia dawki CaO → ilość produktu (wzór + przykłady) — ekspercki value-add.
- Tabela „Jakie wapno AGRIA dla jakiej gleby" spięta z 8 kartami produktów (nowe URL-e `/wapno-nawozowe-rolnictwo/...`).
- FAQ (5 pytań) + JSON-LD **FAQPage** i **HowTo** (kroki doboru dawki).
- Meta: title „Ile wapna na hektar? Dawki CaO i dobór wapna | AGRIA", focus keyword „ile wapna na hektar, wapnowanie gleby".
- Treść 11,4 KB → 16,1 KB.

### Pomiary
| Data kontroli | Poz. „ile wapna na hektar" | Wyświetlenia | Klik | CTR | Uwagi |
|---|---|---|---|---|---|
| 2026-07-08 (baseline) | 14 | — | — | — | przed przebudową |
| _(do uzupełnienia ~08.2026)_ | | | | | |

### Podgląd draftu (robocze, do skasowania)
https://auratest.pl/fe4f58fec53ctmp/agria-wapnowanie-gleby-draft-2026-07-09.html

---

## #2 — /ile-wapna-granulowanego-na-ha/ (post 2741, NOWY)

| Pole | Wartość |
|---|---|
| **Data publikacji** | 2026-07-09 |
| **URL** | https://agria.pl/ile-wapna-granulowanego-na-ha/ |
| **Fraza-cel** | „ile wapna granulowanego na ha" (590/mc) |
| **Baseline** | brak w rankingu (nowy content) |
| **Zgłoszono do indeksacji** | 2026-07-09 (index-submit, URL_UPDATED) |
| **Okno pomiaru** | pierwsza indeksacja + pozycja ~2026-08-06, dojrzewanie ~2026-09-03 |
| **Cel** | wejście do TOP 20 → TOP 10 na „ile wapna granulowanego na ha" |

### Charakterystyka
- Nowy poradnik (KROK 2 strategii, content jesienny rolnictwo). Kategoria: poradniki (tt_id 829).
- Oś: granulat = ta sama dawka co sypkie (1–6 t/ha), granulacja to forma wysiewu; dawka podtrzymująca 0,5–1,5 t/ha; przeliczenie CaO→granulat; tabela granulat vs sypkie vs tlenkowe.
- Produkty: węglanowe granulowane #314, węglanowe z magnezem #317, kreda granulowana #305 (linki).
- JSON-LD FAQPage (4 Q) + HowTo. Klaster: link do/z `/wapnowanie-gleby/`.
- Meta: title „Ile wapna granulowanego na hektar? Dawki i stosowanie | AGRIA".

### Flaga danych (do on-page osobno)
Karta Kredy nawozowej granulowanej (#305) ma w polu `pa_agria-dawkowanie` uciętą/błędną wartość „5 t/ha, 5-1" — poprawić przy najbliższym on-page produktów.

### Podgląd draftu (robocze, do skasowania)
https://auratest.pl/fe4f58fec53ctmp/agria-ile-wapna-granulowanego-na-ha-draft-2026-07-09.html

---

## #3 — /wapno-nawozowe-na-trawnik/ (post 2742, NOWY)

| Pole | Wartość |
|---|---|
| **Data publikacji** | 2026-07-09 |
| **URL** | https://agria.pl/wapno-nawozowe-na-trawnik/ |
| **Fraza-cel** | „wapno nawozowe na trawnik" (50/mc, transakcyjne) |
| **Baseline** | brak w rankingu (nowy content) |
| **Zgłoszono do indeksacji** | 2026-07-09 (index-submit, URL_UPDATED) |
| **Okno pomiaru** | ~2026-08-06 (indeksacja/pozycja), ~2026-09-03 (dojrzewanie) |
| **Cel** | TOP 10 na „wapno nawozowe na trawnik" + ruch na karty kredy |

### Charakterystyka
- Nowy poradnik (KROK 2, transakcyjny). Kategoria: poradniki (829). Ton praktyczny, nie lifestyle.
- Oś sprzedażowa: kieruje na kredę (#305/#306) i węglanowe granulowane (#314); ostrzega przed wapnem palonym na trawnik.
- Tabela dawek kg/100 m² + t/ha wg pH; objawy zakwaszenia (mech); jak i kiedy wysiewać.
- JSON-LD FAQPage (4 Q) + HowTo.

### Klaster (hub-and-spoke) — spięty 2026-07-09
- Hub: `/wapnowanie-gleby/` → linkuje do granulatu i trawnika (sekcja „Powiązane" dodana).
- `/ile-wapna-granulowanego-na-ha/` → linkuje do huba i trawnika.
- `/wapno-nawozowe-na-trawnik/` → linkuje do huba i granulatu.

### Podgląd draftu (robocze, do skasowania)
https://auratest.pl/fe4f58fec53ctmp/agria-wapno-nawozowe-na-trawnik-draft-2026-07-09.html

---

## #4 — /jak-stosowac-wapno-nawozowe/ (post 2743, NOWY)

| Pole | Wartość |
|---|---|
| **Data publikacji** | 2026-07-09 |
| **URL** | https://agria.pl/jak-stosowac-wapno-nawozowe/ |
| **Fraza-cel** | „jak stosować wapno nawozowe" (30/mc, info) |
| **Baseline** | brak w rankingu (nowy content) |
| **Zgłoszono do indeksacji** | 2026-07-09 (index-submit, URL_UPDATED, 10/100) |
| **Okno pomiaru** | ~2026-08-06 (indeksacja/pozycja), ~2026-09-03 (dojrzewanie) |
| **Cel** | TOP 10 na „jak stosować wapno nawozowe" + wzmocnienie klastra (4/4) |

### Charakterystyka
- Nowy poradnik (domyka klaster rolniczy „wapnowanie" 4/4). Kategoria: poradniki (tt_id 829).
- Kąt **komplementarny** do 3 istniejących stron: te mówią „ile", ten mówi „jak" — technika stosowania (termin, rozprowadzenie/sprzęt, wymieszanie 10–20 cm, odstępy od obornika/azotu/fosforu, BHP wapna palonego, błędy).
- Produkty: tabela 6 kart AGRIA (Agrobielik 70/90, wapno tlenkowe z magnezem, węglanowe odm. 04, granulowane, kreda sypka) — linki na nowe URL-e `/wapno-nawozowe-rolnictwo/...`.
- JSON-LD **FAQPage** (5 Q) + **HowTo** (5 kroków) — zweryfikowane curl.
- Treść 17,4 KB.

### Klaster (hub-and-spoke) — domknięty 2026-07-09
- Nowy post → linkuje do huba `/wapnowanie-gleby/` + granulatu + trawnika + 6 kart produktów.
- Linki zwrotne dodane: hub (2074, „Powiązane"), granulat (2741, „Zobacz też"), trawnik (2742, „Powiązane") → nowy post. Zweryfikowane live (curl).

### Podgląd draftu (robocze, do skasowania)
https://auratest.pl/fe4f58fec53ctmp/agria-jak-stosowac-wapno-nawozowe-draft-2026-07-09.html

---

## #5 — /higienizacja-osadow-sciekowych-wapnem/ (post 2744, NOWY — landing B2B)

| Pole | Wartość |
|---|---|
| **Data publikacji** | 2026-07-09 |
| **URL** | https://agria.pl/higienizacja-osadow-sciekowych-wapnem/ |
| **Frazy-cel** | „higienizacja osadów ściekowych wapnem", „stabilizacja osadów wapnem", „wapno do oczyszczalni", „neutralizacja osadów" |
| **Baseline** | brak w rankingu (nowy content, nisza winnable — wapno-info.pl na 15 frazach) |
| **Zgłoszono do indeksacji** | 2026-07-09 (index-submit, URL_UPDATED, 24/100) |
| **Okno pomiaru** | ~2026-08-06 (indeksacja/pozycja), ~2026-09-03 (dojrzewanie) |
| **Cel** | wejście do TOP 20 → TOP 10, lead B2B (przetargi/oczyszczalnie, wysoka wartość per lead) |

### Charakterystyka
- **KROK 3 strategii** (segment Oczyszczalnie). Pierwszy landing B2B — najwyższa wartość per lead w projekcie.
- Ton instytucjonalny/przetargowy: mechanizm pH>12, dobór palone vs hydratyzowane, dawki % suchej masy, dokumentacja, CTA ofertowy.
- Produkty (linki na realne karty, URL 200): wapno palone mielone #320 (lead), Bielik #309, Agrobielik 90 #311.
- JSON-LD **FAQPage** (5 Q) + **HowTo** (proces higienizacji 5 kroków) — zweryfikowane curl.
- Treść 14,3 KB.

### Nowa taksonomia — kategoria „Zastosowania" (tt_id 831)
- Utworzona 2026-07-09 jako **dom dla landingów segmentowych** (nie „poradniki"). Slug `zastosowania`, term_id=831, tt_id=831.
- Landing #5 przypięty do 831. Kolejne landingi (rybactwo/stawy, drogownictwo, budownictwo) → tutaj. Do zrobienia: podpięcie kategorii pod menu / hub segmentowy.

### Flagi danych (do on-page produktów — NIE reprodukowane w treści landingu)
- Karta #320 (palone mielone): pole `pa_agria-ph` / spec „Odczyn pH >16" + FAQ „>16, >17" — **błąd** (skala pH ≤14). Landing używa poprawnego „pH powyżej 12".
- Karta #309 (Bielik): tytuł „min. 72% CaO" vs treść „min. 90% CaO" — sprzeczność do ujednolicenia. Landing: opisowo „wysoka zawartość CaO".

### Podgląd draftu (robocze, do skasowania)
https://auratest.pl/fe4f58fec53ctmp/agria-higienizacja-osadow-landing-draft-2026-07-09.html
