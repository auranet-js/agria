# Odczyt konwersji Ads — 7 dni po przestawieniu kampanii na wieś

**Data pomiaru:** 2026-09-07 (poniedziałek, dzień emisji — dane niepełne, doba trwa)
**Zmiana mierzona:** 28.08.2026 (promień 150 km, emisja nd/pn/wt, budżet Rolnictwa 26 → 60 zł/dz,
8 wykluczonych miast, 44 frazy) · **Źródło:** Google Ads API v25, CID 6742071446 + GA4 Data API (538301430)
**Prompt wątku:** `docs/przypomnienia/2026-09-01-odczyt-konwersji-po-przestawieniu.md`

Odczyt z 01.09 (2 dni) pokazał wzrost ruchu i zero konwersji. Ten odczyt obejmuje **pięć dni emisji**:
nd 30.08 · pn 31.08 · wt 01.09 · nd 06.09 · pn 07.09 (częściowy).

---

## 1. Mechanizm ruszył — to jest rozstrzygnięte

| Miara | przed (24–28.08, 7 dni tyg.) | po (30.08–06.09, dni emisji) |
|---|---|---|
| udział w wyświetleniach | **0,0999** = próg „< 10%", nie pomiar | **0,624 – 0,749** |
| utrata przez budżet | **90%** codziennie | **0 – 8,1%** |
| wyświetlenia / dzień emisji | 87 – 117 | **352 · 518 · 466 · 542** |
| kliknięcia / dzień emisji | 14 | **54 · 54 · 48 · 63** |
| koszt / dzień emisji | 27,4 – 27,7 zł | **105,62 · 106,34 · 93,39 · 120,86 zł** |
| CPC | 1,95 zł | **1,95 zł** (426,21 / 219) |

**Suma Rolnictwa od zmiany:** 1 961 wyświetleń · 237 kliknięć · **461,27 zł** (z niepełnym 07.09).

Dwie tezy z 28.08 rozstrzygnięte pomiarem:
- ✅ **„udział w wyświetleniach ruszy"** — ruszył, siedmiokrotnie. Wąskie gardło budżetowe zniknęło.
- ❌ **„nisza nie wypełni 60 zł, ~1,3 kliknięcia w dniu emisji"** — nieprawda. Popyt w promieniu 150 km
  przy trzech dniach jest **większy niż budżet**: kampania schodzi 105–121 zł przy budżecie 60,
  czyli **do sufitu 2× dziennego budżetu**, jaki dopuszcza Google.

## 2. ⚠️ Wrzesień wychodzi poza budżet mediowy

Plan z 28.08 zakładał „13 dni × 60 zł ≈ 780 zł/mies". Pomiar mówi co innego, bo Google na dniach emisji
wydaje **do dwukrotności** dziennego budżetu, a harmonogram trzydniowy nie daje dni kompensujących.

| | wartość |
|---|---|
| Rolnictwo, średnia z 4 pełnych dni emisji | **106,55 zł** |
| dni emisji we wrześniu (4 nd + 4 pn + 5 wt) | **13** |
| projekcja Rolnictwa | **≈ 1 385 zł** |
| Paszarstwo (10,85 zł/dz × 30) + Marka (3,14 × 30) | ≈ 420 zł |
| **projekcja września łącznie** | **≈ 1 800 zł** wobec **1 200 zł** zatwierdzonych |

Wydane 1–6.09 (dni pełne): **298,22 zł w 6 dni**. Miesięczny limit Google dla samego Rolnictwa to
60 × 30,4 = **1 824 zł**, więc żaden mechanizm po stronie konta tego nie utnie. Precedens 27.08:
konto wyczerpało środki i emisja stanęła na dobę.

**Decyzja do podjęcia:** obniżyć budżet dzienny Rolnictwa (przy ~30 zł/dz wrzesień wychodzi ≈ 1 200 zł)
albo wystąpić do Kasjana o wyższy budżet mediowy. To jest dokładnie ta decyzja, która w prompcie
z 01.09 czekała na dowód, że mechanizm działa — dowód jest.

## 3. Konwersje — zero, ale mierzone przez nieszczelny licznik

**Rolnictwo: 0 konwersji na 237 kliknięć od zmiany.** Wszystkie zdarzenia konwersyjne konta od 24.08:

| data | kampania | akcja | kategoria |
|---|---|---|---|
| 25.08 | Rolnictwo | `form_submit` ×2 | DEFAULT (pomocnicza) |
| 28.08 | Rolnictwo | `phone_click` ×1 | PHONE_CALL_LEAD (główna) |
| 03.09 | Paszarstwo | `phone_click` ×1 | PHONE_CALL_LEAD (główna) |

**Kanał importu żyje** — `phone_click` z 03.09 przeszedł z GA4 do Ads, więc powiązanie działa.

**Dlaczego „zero" nie znaczy „nikt nie dzwonił":** w tym samym oknie 30.08–07.09 Ads naliczył
**≈ 330 kliknięć płatnych**, a GA4 zobaczył **52 sesje Paid Search** — czyli **16%**. Warstwa zgód zjada
pięć na sześć wizyt (memory `project_agria_ga4_consent_blocker`), a `phone_click` i `form_submit` idą
**wyłącznie** przez GA4. Zdarzenia kontaktowe w GA4 w całym oknie: `phone_click` 1 (Paid Search),
`form_submit` 2 (Direct).

**AD_CALL — jedyny pomiar niezależny od zgód:** akcja `Połączenia z reklam (30s+)` (id 7720746866,
`ENABLED`, główna, próg 30 s) **nie zarejestrowała nic**. Ale rozszerzenie **serwuje i jest klikane**:
segmentacja po `click_type` daje w Rolnictwie **1 kliknięcie typu `CALLS` (01.09, 0,91 zł)** na 237.
Czyli mechanizm działa, a wolumen telefonów z reklamy jest po prostu bardzo niski — jedno tapnięcie
na 237 kliknięć, i to krótsze niż 30 s albo nieodebrane.

**Wniosek:** przy tej szczelności pomiaru „zero konwersji" nie jest jeszcze dowodem na brak leadów.
Jedyne twarde potwierdzenie daje **AGRIA** — Paweł (664 393 062) albo Kazimierz (781 875 411): czy
w niedziele i poniedziałki końca sierpnia i września telefonów przybyło.

## 4. Wykluczenia i profil zapytań działają zgodnie z projektem

- **Geografia:** wszystkie 100 kliknięć w oknie to `LOCATION_OF_PRESENCE` — fizyczna obecność, nie
  zainteresowanie. Kryteria Rolnictwa potwierdzone odczytem: dwa promienie **150 km KILOMETERS**
  (50,1350 / 20,8500 i 50,2170 / 21,0170) + **8 wykluczeń miejskich**, `positive/negative geo target
  type = PRESENCE`. Kraków, Katowice i Łódź w danych pochodzą **z Paszarstwa** (ogólnopolskie, bez
  wykluczeń), nie z Rolnictwa.
- **Zasięg Rolnictwa:** Lublin (17 klik., 33,61 zł), Sułoszowa, Biłgoraj, Leżajsk, Limanowa, Tuchów,
  Puławy, Mielec, Przemyśl, Sanok — wszystko w promieniu, z Lubelszczyzną i Podkarpaciem na krawędzi.
- **Zapytania zwiejszczały:** w TOP-40 po zmianie stoją `wapno granulowane cena`, `wapno nawozowe cena
  za tonę`, `ile kosztuje tona wapna`, `wapno granulowane big bag cena`, `gdzie kupić wapno na pole`.
  **Zero zapytań ogrodowych i miejskich** (`trawnik`, `bielenie`, `działka`) wśród fraz z kliknięciami.

## 5. Co z tego wynika dla rejestru

- **T-058** (ocena ścieżki kontaktu) — częściowo odpowiedziane: ścieżka telefoniczna z reklamy istnieje
  i jest klikana, ale raz na 237 kliknięć. Grupa „Producent" nadal nie istnieje, stawka grupy
  „Wapno magnezowe i kreda" nadal 1,00 zł — bez zmian od 24.08.
- **T-087** — kanał importu GA4 → Ads potwierdzony działającym `phone_click` z 03.09.
- **Nowe:** budżet września wychodzi ~50% poza 1 200 zł. Do decyzji Janka przed najbliższą niedzielą
  (13.09), bo każdy dzień emisji to ~107 zł.
