# Zaległe kontrole SEO i Ads — jeden odczyt 08.10.2026

**Kontrole:** T-078 „opis kategorii /paszarstwo/” (termin 26.09) · przebudowa kampanii Marka (02.10) ·
T-092 „opis kategorii /wapno-nawozowe-rolnictwo/” po 30 dniach (04.10) · T-085 „opis /wapno-hydratyzowane/”
i T-093 „opis /wapno-do-oczyszczalni/” (05.10).
**Metoda:** GSC Search Analytics (property `https://agria.pl/`), dane do **04.10** (4 dni dojrzewania),
**okna równej długości**, „przed” kończy się w dniu wdrożenia. Pozycja fraz ważona wyświetleniami po
wszystkich naszych adresach; CTR strony liczony z poziomu strony, nie z sumy zapytań.
Ads: API v25, `scripts/google/ads_call.sh`, wyłącznie odczyt.
**Dane surowe:** `data/kontrole/2026-10-08-kontrole-zalegle-seo-gsc.json`, `data/kontrole/2026-10-08-ads-marka.json`.
**Zero zmian na produkcji i na koncie Ads.**

⚠️ **Tło sezonowe jest duże** — serwis w oknach 26–30-dniowych urósł o **70–80% wyświetleń**
(wrzesień–październik to szczyt rolniczy). Każdy wzrost strony porównuj z tłem w tabeli.

| | werdykt |
|---|---|
| **T-078** `/paszarstwo/` | **Zadziałało mocno** — kategoria weszła do TOP 5 na frazach formowych, klaster „pastewn” 37 → 1 843 wyśw. |
| **Marka** | **Zadziałało na udziale w wyświetleniach, nie na ocenie strony** — IS 46 → 73%, QS `bielik wapno` nadal 3 |
| **T-092** po 30 dniach | **Obraz z 18.09 się utrwalił** — widoczność ×2,6 przy tle ×1,7, kliknięcia z fraz 1 → 17, kanibalizacja rośnie |
| **T-085** `/wapno-hydratyzowane/` | **Kategoria ruszyła z pozycji 25 → 11, karcie nic nie zabrała** — frazy celu bez wolumenu do oceny |
| **T-093** `/wapno-do-oczyszczalni/` | **Role rozdzielone, kliknięć brak** — kategoria poz. 9,4 → 5,3, na frazach bazowych nadal 0 kliknięć |

---

## 1. T-078 „opis kategorii /paszarstwo/” — 26 dni po wdrożeniu

**Okna:** przed 14.08–08.09 · po 09.09–04.10 (26 dni). Baseline wdrożeniowy: `data/T-078/baseline-gsc-2026-09-08.json`.

| strona | wyśw. | klik. | CTR | poz. |
|---|---|---|---|---|
| **serwis** (tło) | 25 650 → 46 060 (**+80%**) | 320 → 585 | 1,25 → 1,27% | 6,80 → 6,45 |
| **`/paszarstwo/`** | **114 → 2 626** (×23) | **3 → 32** | 2,63 → 1,22% | **11,1 → 5,7** |
| `/paszarstwo/kreda-pastewna/` (#307) | 181 → 2 964 (×16) | 2 → 22 | 1,10 → 0,74% | 8,0 → 8,3 |

Frazy formowe z planu kontroli (wszystkie nasze adresy):

| fraza | wyśw. | klik. | poz. | kto wygrywa po |
|---|---|---|---|---|
| `kreda pastewna dawkowanie` | 7 → 18 | 0 → 0 | **30,4 → 4,3** | kategoria 3,5 |
| `kreda pastewna dla bydła dawkowanie` | 7 → 38 | 0 → 0 | **20,7 → 6,0** | kategoria 4,6 |
| `ile kredy pastewnej dla kur na 100 kg` | 5 → 59 | 0 → 0 | 6,6 → 5,6 | kategoria 4,4 |
| `kreda pastewna dla kur dawkowanie` | 0 → 54 | 0 → 1 | — → 5,7 | kategoria 3,8 (klik na karcie) |
| `kreda pastewna` (główna) | 3 → 44 | 0 → 0 | 12,0 → 13,8 | karta 16,0 · kategoria 11,3 |
| `kreda pastewna dla bydła` | 6 → 44 | 0 → 1 | 19,8 → 10,4 | karta 8,8 |
| **klaster „pastewn” (contains)** | **37 → 1 843** | **0 → 8** | 17,4 → 9,0 | |

**Werdykt:** zadziałało mocno — wzrost kategorii (×23) wielokrotnie przewyższa tło (+80%), a na frazach
o dawkowaniu kategoria jest na pozycjach 3,5–4,6; klaster przestał mieć zero kliknięć (0 → 8).
**Co z tego wynika:** oś „dawkowanie” trafiła — kategoria przejęła frazy formowe, karta trzyma frazę
produktową; CTR obu stron spadł, bo wyświetleń przybyło szybciej niż kliknięć (ten sam obraz co T-092).
Zauważone obok: na frazach formowych wciąż pokazują się **oba** adresy (kategoria + karta) — materiał do D1, nie do ruszania teraz.

---

## 2. Przebudowa kampanii „AGRIA - Marka” — 19 dni po zmianie (18.09)

**Stan konta (odczyt 08.10):** przebudowa z `scripts/ads/brand-2026-09-18/` **jest wykonana** — 26 wykluczeń
kampanii, trzy grupy (Brand, „Bielik - wapno hydratyzowane” → karta #309, „Oxyfertil 90” → karta #312),
produktowe frazy w Brand wstrzymane, `agria niedomice` dodana.
**Okna:** przed 20.08–18.09 (30 dni) · po 19.09–07.10 (19 dni) — wskaźniki udziałowe porównywalne, sumy nie.

| | przed | po |
|---|---|---|
| wyświetlenia / kliknięcia / koszt | 597 / 60 / 84,23 zł | 617 / 81 / 113,69 zł |
| **udział w wyświetleniach (IS)** | **45,9%** | **72,5%** |
| **utrata przez ranking** | **47,8%** | **20,9%** |
| utrata przez budżet | 6,3% | 6,5% |
| konwersje | 0 | 0 |

`bielik wapno`: przed (Brand → `/`) 197 wyśw., 9 klik., **CTR 4,6%** · po (grupa Bielik → #309) 260 wyśw.,
30 klik., **CTR 11,5%**, 43,65 zł.

Quality Score dziś:

| fraza (grupa) | QS | strona docelowa | reklama | przew. CTR |
|---|---|---|---|---|
| `bielik wapno` (Bielik) | **3** | **poniżej średniej** | powyżej | poniżej |
| `wapno bielik` (Bielik) | 5 | poniżej średniej | powyżej | średni |
| `wapno hydratyzowane bielik` (Bielik) | 5 | poniżej średniej | powyżej | średni |
| `oxyfertil` (Oxyfertil 90) | 7 (było 5) | średnia | powyżej | średni |
| `oxyfertil 90` (Oxyfertil 90) | 8 | średnia | powyżej | powyżej |
| `agria` / `agria tarnów` / `agria wapno` | 8 / 10 / 10 | powyżej | powyżej | — |
| `agria niedomice` (nowa) | 6 | powyżej | poniżej | średni |

**Werdykt:** `bielik wapno` **nie wyszło** z QS 3 ani z oceny strony „poniżej średniej” po przeniesieniu na
kartę #309; kampania mimo to odzyskała udział (IS 46 → 73%, utrata przez ranking 48 → 21%), a CTR frazy
wzrósł 4,6 → 11,5% — zysk przyszedł z dopasowania reklamy do grupy, nie ze strony docelowej.
**Co z tego wynika:** rozstrzygnięcie „czy tę samą dźwignię stosować w Rolnictwie” jest **dwuznaczne** —
osobne grupy z dopasowanymi reklamami działają, ale przeniesienie na kartę v2 **nie podniosło** oceny
strony docelowej (Oxyfertil: tylko „średnia”). Zero konwersji w obu oknach — kampania nie ma jeszcze
dowodu sprzedażowego.

---

## 3. T-092 „opis kategorii /wapno-nawozowe-rolnictwo/” — 30 dni po wdrożeniu

**Okna:** przed 06.08–04.09 · po 05.09–04.10 (30 dni). Porównanie z kontrolą 14-dniową
`data/kontrole/2026-09-18-kontrola-T-092.md` (okna 11-dniowe).

| | wyśw. | klik. | CTR | poz. |
|---|---|---|---|---|
| **serwis** (tło) | 29 416 → 49 898 (**+70%**) | 364 → 639 | 1,24 → 1,28% | 6,95 → 6,44 |
| **kategoria** | 1 062 → **2 730** (**+157%**) | 8 → 17 | **0,75 → 0,62%** | 8,94 → 8,74 |
| *kontrola 18.09 (11 dni)* | *475 → 944 (+99%, tło +30%)* | *3 → 5* | *0,63 → 0,53%* | *9,31 → 8,89* |

| fraza | wyśw. | klik. | poz. | własnych URL-i |
|---|---|---|---|---|
| **`wapno nawozowe`** (fraza główna, 1 300) | **386 → 1 473** | 0 → 3 | 9,30 → 8,71 | 3 → 6 |
| `wapno węglanowe` (1 000) | 686 → 620 | 1 → 1 | 15,22 → 12,61 | 5 → 6 |
| `kreda nawozowa` (1 000) | 35 → 154 | 0 → 3 | **24,86 → 11,38** | 3 → **7** |
| `wapno tlenkowe` (720) | 41 → 36 | 0 → 0 | 20,39 → 18,58 | 2 → 5 |
| `kreda nawozowa sypka` | 46 → 91 | 0 → **9** | **9,98 → 5,35** | 3 → 4 |
| `wapno węglanowe granulowane` | 107 → 144 | 0 → 0 | 20,70 → 15,37 | 3 → 6 |
| `wapno nawozowe tlenkowe` | 92 → 77 | 0 → 1 | 12,79 → 12,10 | 3 → 6 |
| `wapno nawozowe węglanowe` | 129 → 125 | 0 → 0 | 21,77 → 20,05 | 4 → 6 |

Na `wapno nawozowe` kategoria ma 1 225 wyśw. na poz. 9,31, strona główna 214 na poz. 6,23.

**Werdykt:** obraz z 18.09 się utrwalił — pozycja lepsza na **8/8 fraz**, kategoria rośnie ponad dwa razy
szybciej niż tło (+157% wobec +70%), kliknięcia z mierzonych fraz **1 → 17**, ale CTR kategorii dalej
spada (0,75 → 0,62%), a liczba własnych adresów na frazę wzrosła na **wszystkich 8**.
**Co z tego wynika:** wzorzec „rozbudowa opisu kategorii” działa na widoczność — kliknięcia przychodzą,
ale głównie na karty (z 9 kliknięć na `kreda nawozowa sypka` 8 poszło na kartę). Kanibalizacja kategoria ↔
strona główna na frazie głównej trwa (D1).

---

## 4. T-085 „opis /wapno-hydratyzowane/” — 13 dni po wdrożeniu

**Okna:** przed 09.09–21.09 · po 22.09–04.10 (13 dni). Baseline wdrożeniowy (28 dni 21.08–17.09):
kategoria 122 / 2 / poz. 30,0, karta #309 584 / 10 / poz. 7,3.

| | wyśw. | klik. | CTR | poz. |
|---|---|---|---|---|
| **serwis** (tło) | 22 075 → 23 985 (+9%) | 266 → 319 | 1,20 → 1,33% | 6,80 → 6,14 |
| **kategoria `/wapno-hydratyzowane/`** | 51 → 86 | 0 → 1 | 0 → 1,16% | **25,3 → 10,8** |
| **karta #309 Bielik** | 293 → 502 | 7 → 12 | 2,39 → 2,39% | **7,16 → 7,35** |

| fraza | wyśw. | klik. | poz. |
|---|---|---|---|
| `cl 90-s` / „cl 90” (contains) | 0 → 0 | — | — |
| frazy dostawowe („dostaw”, contains w klastrze) | 1 → 0 | 1 → 0 | — |
| `wapno budowlane bielik` | 1 → 6 | 0 → 0 | 10,0 → 10,2 (tylko karta) |
| `wapno bielik` | 10 → 35 | 0 → 0 | 15,0 → 11,4 (karta 8,6) |
| `wapno hydratyzowane` (świadomie nie gonimy) | 17 → 15 | 0 → 0 | 39,1 → 17,1 (kategoria 18,1) |
| klaster „hydratyz” (contains) | 45 → 47 | 0 → 0 | 20,0 → 11,5 |

**Werdykt:** kategoria awansowała z pozycji **25,3 na 10,8** przy tle +9% i **nie zabrała** karcie #309
pozycji (7,16 → 7,35, CTR bez zmian 2,39%, kliknięcia 7 → 12); na frazach celu (`cl 90-s`, dostawowe)
nie ma wyświetleń, więc tej części nie da się ocenić.
**Co z tego wynika:** cel „nie szkodzić karcie” spełniony; o frazach celu rozstrzygnie dopiero dłuższe okno.
⚠️ H1 kategorii zmieniony 08.10 („Wapno budowlane”) — kolejny pomiar zmiesza dwie zmiany.

---

## 5. T-093 „opis /wapno-do-oczyszczalni/” — 13 dni po wdrożeniu

**Okna:** jak T-085 (09.09–21.09 wobec 22.09–04.10).

| | wyśw. | klik. | CTR | poz. |
|---|---|---|---|---|
| **kategoria `/wapno-do-oczyszczalni/`** | 163 → 210 | 7 → 8 | 4,29 → 3,81% | **9,37 → 5,27** |
| poradnik `/higienizacja-osadow-sciekowych-wapnem/` | 217 → 231 | 3 → 5 | 1,38 → 2,16% | 10,79 → 9,35 |

| fraza z baseline'u | wyśw. | klik. | poz. | URL-i | kto po |
|---|---|---|---|---|---|
| `higienizacja osadów ściekowych` | 42 → 19 | 0 → 0 | 19,3 → 19,4 | 2 → 1 | poradnik |
| `wapnowanie osadów ściekowych` | 27 → 21 | 0 → 0 | 18,8 → 12,8 | 2 → 2 | **kategoria 9,3** (poradnik 33,7) |
| `wapno do szamba` | 28 → 16 | 0 → 0 | **11,5 → 4,7** | 2 → 1 | kategoria |
| `proces higienizacji osadów ściekowych` | 13 → 14 | 0 → 0 | 23,3 → 22,1 | 2 → 1 | poradnik |

**Werdykt:** kategoria poprawiła pozycję (9,4 → 5,3) i przejęła `wapno do szamba` (poz. 4,7) oraz
`wapnowanie osadów ściekowych` (9,3), poradnik został sam na frazach „higienizacja” — ale na czterech
frazach bazowych nadal **zero kliknięć** (110 → 70 wyśw.).
**Co z tego wynika:** drugi wskaźnik (rozdział ról kategoria/poradnik) spełniony — na 3 z 4 fraz zostaje
jeden nasz adres; pierwszy (kliknięcia) nie. ⚠️ 08.10 zmieniono tytuł i H2 kategorii — okna powyżej
kończą się 04.10, więc tego nie obejmują.
