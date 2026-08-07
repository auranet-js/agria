# OLX — analiza konkurencji w kategorii Nawozy

> Data: 2026-08-07. Kontekst: Paweł twierdzi, że **2–3 firmy żyją wyłącznie z OLX**, wystawiając setki ogłoszeń, i pyta, czy iść w ten model.
> Metoda: publiczne API wyszukiwania OLX (`/api/v1/offers/`, kategoria **4368 Nawozy**), 1 166 ogłoszeń z opisami i cenami, pobrane 07.08.2026. Dane surowe: `olx-market-full.json` w scratchpadzie sesji.
> Uzupełnia: `OLX_INWENTARYZACJA_2026-08-07.md` (stan konta AGRII) i `CENNIK_PAWEL_2026-08-07.md` (ceny AGRII).

---

## 1. Paweł ma rację co do skali

Kategoria Nawozy to **1 166 aktywnych ogłoszeń od 199 sprzedawców**. Czołówka:

| Sprzedawca | Ogłoszeń | Unikalnych tytułów | Miast | Promowanych | Mediana ceny |
|---|---|---|---|---|---|
| 699-712-071 | **191** | 26 | 120 | **0** | 205 zł |
| AGRO-KOTYNIA | **161** | 9 | 161 | 25 | 190 zł |
| EMPRO | 93 | 23 | 44 | 0 | 120 zł |
| DAREK | 70 | 8 | 70 | 2 | 180 zł |
| Agro-Siew | 58 | 42 | 58 | 0 | 170 zł |
| Marcin Rytel | 45 | 37 | 29 | 0 | 580 zł |
| **AGRIA (dziś)** | **20** (1 aktywne) | **4** | **18** | 0 | 400 zł |

Model lidera jest jednoznaczny: **kilka–kilkanaście ofert × dziesiątki lub setki miast**. AGRO-KOTYNIA to 9 tytułów rozstawionych na 161 miast, 699-712-071 to 26 tytułów na 120 miast. AGRIA robiła 4 tytuły na 18 miast — czyli **jedną ósmą skali lidera**, a od 18.07 nie ma jej tam wcale.

## 2. Korekta wcześniejszego wniosku

W `OLX_INWENTARYZACJA_2026-08-07.md` napisałem, że geo-multiplikacja ma słabą stopę zwrotu, bo duplikaty AGRII zbierały po ~110 wyświetleń. **To było przedwczesne.** Dane rynkowe pokazują, że powielanie geograficzne jest tu podstawowym modelem — tylko liderzy prowadzą je w innej skali i, co ważniejsze, **na wielu różnych produktach naraz**. AGRIA powielała jedną ofertę.

Co się broni z poprzednich wniosków: **intencja w tytule** nadal robi różnicę — własne dane AGRII pokazują 2 514 wyświetleń dla „Do stawu" wobec ~110 dla generycznego „Najtaniej!" przy tej samej ofercie i tych samych zdjęciach.

Obie rzeczy są prawdziwe naraz: wolumen daje zasięg, trafiony tytuł daje konwersję.

## 3. Promowanie nie jest tym, czym wygrywają

Promowanych jest **266 z 1 166 ogłoszeń (23%)**, ale dwaj najwięksi gracze prawie z tego nie korzystają: 699-712-071 ma **zero** promowanych przy 191 ogłoszeniach, AGRO-KOTYNIA 25 przy 161.

**To odpowiada na pytanie Pawła wprost: między „30 ogłoszeń" a „10 + promowanie" rynek wybiera wolumen.** Promowanie ma sens punktowo — na tych ofertach, które już dowiodły skuteczności.

## 4. Ceny AGRII na tle rynku — tu jest problem

Ceny z OLX porównywalne tonowo (odfiltrowane po jednostce z tytułu i opisu):

| Produkt | Rynek OLX (mediana zł/t) | AGRIA (cennik 07.08) | Pozycja |
|---|---|---|---|
| Węglanowe | **41** (min 30, max 195, n=12) | 57 (odm. 04) · 50 (z Mg odm. 04) · 36 (z Mg odm. 05) | **drożej ~40%** |
| Kreda nawozowa | **100** (n=35) | 125 luz | **drożej ~25%** |
| Granulowane | **380** (n=26) | 350–370 big-bag · 380–410 worki | w rynku |
| Tlenkowe / palone | 210 (n=3 — nisza!) | 220 luz · 400 big-bag | w rynku |

**Obawa, że każdy z OLX będzie tańszy, potwierdza się tylko przy węglanowych i kredzie sypkiej.** Przy granulowanych i tlenkowych AGRIA mieści się w rynku.

Zastrzeżenie metodologiczne: mediana OLX zaniża — mieszają się tam ceny loco kopalnia, materiał niższej jakości i drobni sprzedawcy odpadów poprodukcyjnych. To nie jest porównanie produktów o tej samej specyfikacji. Ale klient szukający na OLX widzi właśnie tę medianę.

## 5. Najważniejsze ustalenie: wapno tlenkowe to na OLX pustka

W całej kategorii znalazłem **trzy** ogłoszenia wapna tlenkowego/palonego z ceną tonową. Najbliższy konkurent to PHU Harabin — 210 zł/t, „na stawy", wobec 220 zł/t AGRII.

To spina się z własnymi statystykami konta: najskuteczniejsze ogłoszenie AGRII („Do stawu", 94 odsłony telefonu = 45% wszystkich kontaktów) trafiało dokładnie w tę niszę. **AGRIA ma na OLX przewagę tam, gdzie prawie nikogo nie ma — w tlenkowych i zastosowaniach stawowych — a nie w węglanowych, gdzie jest 40% drożej od mediany i konkuruje z kopalniami.**

Marka wychodzi poza AGRIĘ tylko raz: „Wapno tlenkowe AGROBIELIK 50, odm. 04" za 129 zł/t (CARLOS Karol Nawrocki, Barcin) — pośrednik odsprzedający produkt AGRII.

## 6. Rekomendacja robocza (do domknięcia po cenniku pakietów)

1. **Wolumen, nie promowanie** — pakiet większy niż 10, bo tak wygrywa rynek. Dokładna liczba po sprawdzeniu cennika OLX (OLX-01).
2. **Rozłożyć ogłoszenia na produkty, nie na kopie jednego** — 8–10 różnych ofert zamiast jednej powielonej 18 razy. Materiał jest: 19 kart produktowych z parametrami i zdjęciami, scope `write` w API pozwala je wystawiać i rotować programowo.
3. **Priorytet produktowy: tlenkowe i zastosowania stawowe**, gdzie konkurencji praktycznie nie ma i gdzie własne dane pokazują najwyższą konwersję. Węglanowe i kreda sypka na OLX będą przegrywać ceną — chyba że Paweł zejdzie, a tego nie może zrobić przez zobowiązania wobec stałych odbiorców.
4. **Tytuły pod intencję** („do stawu", „odkwaszanie gleby", „pod rzepak"), nie pod cenę („Najtaniej!").
5. **`auto_extend` na wszystkich** — dziś włączony na jednym ogłoszeniu z dwudziestu, stąd ciche wygaśnięcie całego konta 18.07.

## 7. Do rozmowy z Pawłem

Ceny węglanowych i kredy sypkiej są na OLX o 25–40% powyżej mediany rynkowej. To nie znaczy, że są złe — znaczy, że **OLX nie jest dla nich właściwym kanałem**. Warto, żeby Paweł świadomie zdecydował: albo te produkty na OLX nie idą, albo idą z komunikatem opartym na czymś innym niż cena (atesty, stabilność dostaw, ciągłość produkcji z jednego złoża).
