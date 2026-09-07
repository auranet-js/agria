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

---

# Część II — gdzie tracimy konwersję (analiza 07.09, na prośbę Janka)

Trzy znaleziska, w kolejności siły. Okno: Ads 14.08–07.09 (431 kliknięć, 1 158 zł), GA4 01.06–07.09.

## A. Ads mierzy kanał, którym prawie nikt się nie kontaktuje

Wszystkie zdarzenia kontaktowe w GA4 przez **trzy miesiące**, cały ruch:

| zdarzenie | ile | status w Ads |
|---|---|---|
| `form_start` | **37** | nieimportowane |
| **`form_submit`** | **32** | **pomocnicza** (DEFAULT, `include_in_conversions` = false) |
| `phone_click` | **3** | **główna** (PHONE_CALL_LEAD) |
| `email_click` | 2 | nieimportowane |
| `whatsapp_click` | 2 | nieimportowane |
| **`generate_lead`** | **1** | **główna** (SUBMIT_LEAD_FORM) |

**Formularz domyka się w 86%** (37 rozpoczęć → 32 wysłania) i jest jedynym kanałem o realnej masie.
Kolumna „Konwersje" w Ads liczy natomiast `phone_click` (3) i `generate_lead` (1) — **łącznie 4 zdarzenia
kwartalnie** — a ignoruje 32 wysłane formularze.

⚠️ **Uzasadnienie z 24.08 okazało się nieprawdziwe.** Zapisaliśmy wtedy: „`form_submit` świadomie zostaje
pomocniczy, bo formularz jest już pokryty przez `generate_lead` (główna), a podniesienie obu dawałoby
podwójne liczenie". Pomiar mówi, że **`generate_lead` odpalił się raz na 32 wysłania** — nie pokrywa
niczego, a ryzyka podwójnego liczenia praktycznie nie ma.

**Ruch:** `form_submit` → konwersja główna, kategoria SUBMIT_LEAD_FORM; `generate_lead` zdjąć z głównych
albo zdiagnozować, czemu nie odpala. To jedna zmiana w API, zero kosztu, i od razu odsłania leady, które
kampania już przywozi.

## B. 58,6% budżetu wychodzi, gdy biuro AGRII jest zamknięte

Biuro pracuje **pon.–pt. 8:00–16:00** (godziny ze strony). Emisja idzie 6:00–22:00.

| okno | biuro czynne | weekend | pn–pt poza 8–16 | **zamknięte razem** |
|---|---|---|---|---|
| 14.08–07.09, całe konto (1 158 zł) | 478,90 zł (41,4%) | 433,55 zł (37,4%) | 245,65 zł (21,2%) | **679,20 zł — 58,6%** |
| 30.08–07.09, samo Rolnictwo (469 zł) | 181,50 zł (38,7%) | **226,48 zł (48,3%)** | 60,82 zł (13,0%) | **287,30 zł — 61,3%** |

Przestawienie na niedzielę/poniedziałek/wtorek **podniosło** ten udział, bo niedziela to najdroższy dzień
tygodnia (105–121 zł) i biuro jest wtedy zamknięte w całości.

To nie jest argument za wyłączeniem niedzieli — teza o rytmie zakupowym rolnika trzyma się w danych
(niedziela ma najwyższy wolumen). To argument za tym, że **w niedzielę musi konwertować formularz, nie
telefon** — a formularz właśnie działa (32 wysłania, 86% domknięcia). Landingi mają już zdanie
„pon.–pt. 8:00–16:00. Poza godzinami — zostaw numer, oddzwonimy"; pytanie brzmi, czy w niedzielę to zdanie
i formularz są wyeksponowane tak samo mocno jak numer telefonu.

⚠️ **Godzina, której nie kupujemy:** rozkład prób kontaktu (cały ruch, 3 mies.) ma **10 zdarzeń o 5:00 rano**
— przed startem emisji o 6:00. Szczyt to 14:00–15:00 (31 zdarzeń) i 8:00 (13).

## C. Cena „od 36 zł/t netto" jako wiodąca na landingu, który zjadł 486 zł

`/wapno-nawozowe/` (249 kliknięć, **485,60 zł** — najdroższy adres w koncie) otwiera się zdaniem:

> Wapno węglanowe **od 36 zł/t netto**, tlenkowe od 220 zł/t netto — przy dostawie całosamochodowej 24 t.

Kwota 36 zł/t to cena **węglanowego odm. 05**, którą `FAKTY_KLIENTA.md` §3 wymienia wprost w sekcji
**„Anomalie cenowe do potwierdzenia"** (taniej niż odm. 04 z magnezem — 50 zł/t — i bez magnezu — 57 zł/t),
a karta produktu **#316 świadomie nie ma tej kwoty na froncie** (jedna z czterech kart bez ceny).
Landing publikuje więc jako cenę wiodącą całej kategorii liczbę, której nie publikujemy na karcie.

**Dlaczego to kosztuje:** zapytania cenowe to **27,1% budżetu (205,01 zł, 107 kliknięć)** — druga co do
wielkości grupa i najbardziej wrażliwa na wiarygodność liczby. Rolnik, który zna rynek, przy granulacie
po 350 zł/t czyta „36 zł/t" jako błąd albo haczyk. Do rozstrzygnięcia z Pawłem: czy 36 zł/t jest prawdziwe
i jakiej formy dotyczy.

## D. Tło — to, co działa i czego nie trzeba ruszać

- **Treść nie jest problemem.** GA4 dla ruchu płatnego: **80% sesji zaangażowanych**, średnio 90–130 s na
  stronie, odrzucenia 20–26%, 505 zdarzeń `scroll` na 129 użytkowników. Ludzie czytają do końca.
- **Wąskie gardło jest w ostatnim kroku:** 1,44 odsłony na sesję, `/kontakt/` zbiera **9 odsłon z 229**
  (3,9%), a karty produktów po 2 odsłony. Z landingu prawie nikt nie schodzi głębiej.
- **Marnotrawstwa w zapytaniach prawie nie ma:** 641 unikalnych fraz, z tego informacyjne **2,7% budżetu**
  (20,05 zł), cudze marki i marketplace **2,6%** (19,59 zł — Polcalc, Nordkalk, bez Allegro i OLX).
  Trzon to produktowe ogólne (61,9%) i cenowe (27,1%).
- **90,5% ruchu to telefon komórkowy** (599 z 662 kliknięć), CTR mobile 11,23% wobec 8,30% na desktopie.
  Każda zmiana w ścieżce kontaktu ma sens tylko wtedy, gdy działa na ekranie 390 px.
