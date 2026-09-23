# OLX — audyt po pięciu tygodniach (23.09.2026)

> **Pomiar własny 23.09.2026, 10:49** — `scripts/olx/statystyki.py --zapisz`, **200 z 200** ogłoszeń
> odczytanych per `GET /partner/adverts/{id}/statistics` (pomiar nr 12 w `data/olx/statystyki.json`).
> Stan treści 200/200 per `GET /partner/adverts/{id}`: `data/olx/audyt-2026-09/ogloszenia-2026-09-23.json`.
> Analiza per ogłoszenie: `scripts/olx/audyt.py` → `data/olx/audyt-2026-09/ogloszenia-analiza.json`.
> Wszystkie liczby w tym dokumencie pochodzą z pomiaru sprzed zmian wykonanych 23.09 (T-142…T-146).
>
> Prompt wątku: `docs/prompty/2026-09-23-PROMPT_AUDYT_OLX.md`. Poprzedni raport:
> `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md`. Ceny ofertownika nie występują w tym dokumencie.

---

## Pięć zdań

1. **Działa:** kanał daje **54 odsłony numeru** w 34 dni (43 ogłoszenia z choć jednym kontaktem),
   przełożenie pod magazyny (T-106) podwoiło udział kontaktów z przełożonych ogłoszeń, a po odnowieniu
   19.09 tempo kontaktów wróciło do sierpniowego (**3,3 na dobę** w oknie 21→23.09).
2. **Nie działa:** połowa sierpniowego ruchu wyparowała na początku września, a przełożenie do miast
   konkurencji (T-139) dało **więcej wejść, nie więcej telefonów** (konwersja 1,6% wobec 2,3%).
3. **Koszt kontaktu:** przy tempie z całych 34 dni **ok. 27 zł netto**, nie 12–15 zł z raportu
   z 28.08 (tamto była projekcja z ośmiu sierpniowych dni); przy tempie po odnowieniu — ok. 13 zł,
   ale to dwa dni pomiaru. Obiecany przedział 6,50–30 zł trzyma się w obu wariantach.
4. **Zrobione 23.09:** treść 128 ogłoszeń zgodna z kartami po T-136, 29 martwych ogłoszeń przełożonych,
   8 slotów najsłabszego produktu zamienionych na najmocniejszy, poprawiony pomiar rynku — T-142…T-146.
5. **Pakiet wygasa 16.10, 11:19** (ogłoszenia ważne do 19.10); rekomendacja: **odnowić Premium 200** —
   decyzja po pomiarze **07.10**, pytanie do AGRII najpóźniej **10.10**.

---

## 1. Wynik drugiego cyklu i trend

| Okno | Dni | Odsłony | na dobę | Odsłony numeru | na dobę | Konwersja |
|---|---|---|---|---|---|---|
| 20.08 18:01 → 28.08 15:01 | 7,88 | 634 | **80,5** | 22 | **2,79** | 3,47% |
| 28.08 → 11.09 12:08 | 13,88 | 503 | 36,2 | 14 | 1,01 | 2,78% |
| 11.09 → 14.09 07:35 | 2,81 | 177 | 63,0 | 3 | 1,07 | 1,69% |
| 14.09 → 21.09 07:35 | 7,00 | 546 | 78,0 | 8 | 1,14 | 1,47% |
| 21.09 → 23.09 10:49 | 2,13 | 162 | 75,9 | 7 | **3,28** | 4,32% |
| **całość 20.08 → 23.09** | **33,7** | **2 022** | 60,0 | **54** | 1,60 | 2,67% |

Obserwujący: 21 (28.08) → 45 (23.09).

⚠️ **Korekta promptu:** pomiaru 17.09 nie ma — cron statystyk chodzi w poniedziałki. Okna 11.09–17.09
i 17.09–dziś zastąpione najbliższymi pomiarami (14.09, 21.09).

⚠️ **Odnowienie 19.09 zadziałało jak podbicie wszystkich 200 ogłoszeń.** Publiczne API ofert:
`last_refresh_time` = `pushup_time` = **19.09** na każdym ogłoszeniu, `activated_at` 19.09,
`valid_to` 19.10 (200/200). Poprzednie podbicie: 27.08 (7. dzień cyklu). Między 27.08 a 19.09 —
**23 dni bez podbicia** i to w tym czasie ruch spadł do 27 odsłon na dobę. Okno 14→21.09 ma podbicie
w środku, okno 21→23.09 zaczyna się dwa dni po nim — **część wzrostu to mechanika pakietu, nie nasze zmiany.**
Następne automatyczne podbicie: ok. **26.09** (7. dzień nowej emisji).

**Kontakty rosną wolniej niż ruch, ale rosną.** Od 11.09: odsłony ×2,0 wobec okna 28.08–11.09,
odsłony numeru ×1,5. Teza z promptu „odsłony numeru dużo słabiej” jest prawdziwa dla 11→21.09,
nieaktualna dla 21→23.09.

## 2. Co dały zmiany — grupy kontrolne

Liczone na tej samej liście `advert_id` przed i po, na 100 ogłoszeń na dobę; grupa kontrolna = ogłoszenia
nie ruszane w danej zmianie. Źródło: `data/olx/audyt-2026-09/ogloszenia-analiza.json`.

**T-106 — 68 ogłoszeń przełożonych pod magazyny 28.08:**

| | przed (20→28.08) odsł. / numer | po (28.08→11.09) odsł. / numer |
|---|---|---|
| T-106 (68) | 35,5 / 0,19 | 17,6 / **0,74** |
| kontrola (132) | 42,7 / 2,02 | 18,4 / 0,38 |

Ruch spadł w obu grupach tak samo (sezon), **kontakty z przełożonych urosły czterokrotnie, z kontrolnych
spadły pięciokrotnie.** 7 z 14 kontaktów okna przyszło z 34% ogłoszeń. **T-106 zadziałało.**

**T-139 — 56 ogłoszeń do miast konkurencji 11.09:**

| | 28.08→11.09 odsł. / numer | 11.09→23.09 odsł. / numer | konwersja po |
|---|---|---|---|
| T-139 (56) | 17,8 / 0,00 | **46,3** / 0,75 | 1,61% |
| kontrola (135) | 19,5 / 0,75 | 33,1 / 0,74 | 2,25% |

Ruch **+40%** względem kontroli, kontakty na poziomie kontroli (z zera). **T-139 dało ruch, nie telefony.**

**Seria C — 9 ogłoszeń najtańszych produktów w świętokrzyskim (11.09):** 0 → 42 odsłony, 1 kontakt
(Iwaniska). Za mało zdarzeń na ocenę.

**T-137/T-138 — zdjęcia:** zmienione na 200/200, więc grupy kontrolnej nie ma. Porównanie w oknie
11.09→23.09: **prawdziwe zdjęcia z placu** (62 ogł.) 37,8 odsł. / 0,41 numeru, konwersja 1,07%;
**sceny generowane** (138 ogł.) 36,7 / 0,91, konwersja 2,48%. Wśród samych Agrobielików (ta sama pula
scen): plac 30,0 / 0,25, sceny 41,0 / 0,42. **Prawdziwe zdjęcia nie biją generowanych** — przy 18 kontaktach
w oknie różnica jest w granicach przypadku; teza „plac sprzedaje lepiej” się nie potwierdziła.

## 3. Dlaczego ruch rośnie szybciej niż kontakty

- **Miasta konkurencji (T-139):** +40% ruchu, konwersja 1,6% wobec 2,3% w kontroli. Tam, gdzie rynek jest, klient
  porównuje oferty.
- **Premium tlenkowe po 11.09:** Agrobielik 90 — 47,6 odsł. / **0** numerów; Oxyfertil 90 — 48,1 / **0**.
  Najwięcej wejść, zero telefonów w 12 dniach. Na całym okresie: Agrobielik 90 0,59, Oxyfertil 1,11.
- **Najlepsza konwersja (cały okres, numer na 100 ogł./dobę):** węglanowe granulowane **1,48** (5,1%),
  kreda granulowana **1,38** (5,2%), Oxyfertil 1,11, węglanowe odm. 04 0,99, odm. 05 0,91.
- **Najsłabsza:** węglanowe z Mg granulowane **0,33** (208 odsłon, 2 kontakty, 0,96%) → T-146.
- **Pierścień od magazynów (po 11.09):** 0–60 km **0,96**, 60–120 km 0,81, 120–200 km 0,50.
  Najbliższy pierścień, słaby w sierpniu, jest dziś najlepszy.
- **Miasta z kontaktami:** Dębica 6, Zator 6, Zwoleń 4, Piotrków Tryb. 4, Nowy Sącz 4.

## 4. Martwe ogłoszenia

`data/olx/audyt-2026-09/martwe-2026-09-23.json` — pełna lista 200 z liczbami od wystawienia i od ostatniego
przełożenia, odległość od magazynów AGRII i od zakładu wysyłkowego produktu.

- **157 z 200** ogłoszeń nie ma ani jednej odsłony numeru od wystawienia — przy 54 kontaktach na konto
  to rozkład oczekiwany, nie diagnoza.
- **Martwe = zero numerów i ≤5 odsłon przez ≥25 dni w jednym miejscu: 40 ogłoszeń.** 19 z nich stoi
  ponad 120 km od magazynów; 13 w śląskim (Katowice, Dąbrowa Górnicza, Sosnowiec, Bielsko-Biała, Racibórz,
  Częstochowa), dalej Grójec, Lublin, Radom.
- Z przełożenia wyłączone: 9 × „do stawu” (sezon X–XI), 1 kreda pastewna (rewizja listopadowa),
  1 przy magazynie (Żabno). **29 przełożonych w T-144.**

## 5. Zgodność treści ze stroną po T-136

Render 11 kart z produkcji 23.09 (`data/olx/audyt-2026-09/karty/`), porównanie pole po polu
(`data/olx/audyt-2026-09/rozbieznosci-parametry.json`).

- **Ceny: zgodne w 17/17 wariantach** (pole ceny i treść: 220, 750, 790, 350, 370, 410, 125, 190, 57, 50, 36 zł/t).
- **Żargon (loco, MOQ, franco, EXW, HDS): zero trafień.** Marki producentów (Dewonit, Wapniak Kornicki,
  HumiPlus): zero.
- **Przyczyna rozbieżności parametrów:** OLX niósł tabele kart z 17.08 (`product-specs.json`), a T-136
  przepisał tabele 1:1 z kart PDF producentów. Wzorcem jest karta dzisiejsza.
- **Rozbieżności merytoryczne (poprawione w T-143, 126 ogłoszeń):**
  „intensywna hodowla ryb, neutralizacja ścieków przemysłowych” (Agrobielik 90, Oxyfertil — karta:
  „Stabilizacja pH przed rekultywacją”), dawka stawowa 40–60 kg/1000 m³ przy 90% CaO (nie ma jej na kartach),
  szybkość i reaktywność Oxyfertilu, „odkażanie dna / mineralizacja mułu” w 17 ogłoszeniach „do stawu”
  (karta: „korekta pH stawów”), brak Celin w producentach węglanowego granulowanego, literówka „Hochcel”.
- **5 ogłoszeń przełożonych poza łódzkie zapowiadało „NABÓR W WOJEWÓDZTWIE ŁÓDZKIM”** (Gawłów, Charsznica,
  Jasło, Jeżowe, Polanów) → T-142.
- ⚠️ **Niepoprawione, do decyzji:** tytuły węglanowego granulowanego i z Mg granulowanego mówią
  „**big bag 1 t**”, karty — big-bag **500/600 kg** (węglanowe) i **600 kg** (z Mg). Dotyczy 28 + 10 ogłoszeń.
  Tytuł węglanowego odm. 04 zaczyna się od „kreda nawozowa” — to osobny produkt w ofercie.

## 6. Zdjęcia — kontrola poprawności

Obejrzane obrazy (nie nazwy plików): 14 scen v4 (6 luzem, 8 big bagowych), 41 grafik v2, 24 miniatury v3 —
135 unikalnych plików w galeriach; liczba zdjęć na koncie zgodna z ładunkiem 200/200.

- **Kierunek wysypu:** `wysyp-bok`, `wysyp-tyl`, `wysyp-podworze` — przód skrzyni w górze, wysyp tyłem. Poprawne.
- ⚠️ `wysyp-podworze` (20 galerii, 8 frontów): skrzynia stoi **za tylną osią**, podwozie między kabiną
  a osią puste — geometria nietypowa, kierunek poprawny. Do oceny Janka, nie wycofane.
- `wywrotka-zsyp` (T-140): **0 wystąpień** na koncie.
- Napisy na frontach zgodne z produktem 200/200; pseudonapisów i obcych logotypów w scenach brak
  (kontrola w rozdzielczości arkusza, nie 1:1). Na grafikach v2 jest logo AGRII (własne).
- Grafika „Sypkie z magnezem” ma widoczny szew lustrzanego odbicia tekstury — kosmetyka.

## 7. Rynek

⚠️ **Korekta metodologiczna — tezy z cyklu 1 o rynku były artefaktem próbki.**
`market_snapshot.py` zbierał ogłoszenia od najnowszych, a OLX ucina paginację na offsecie ~1000:
snapshot to **~1 200 najnowszych ogłoszeń na kategorię z ~17 000 (Nawozy)**, nie spis. 28.08 AGRIA
(wystawiona 20.08) była w tej próbce cała, 23.09 — wcale. Nowy tryb spisu: `market_snapshot.py --spis`
(kat. 4368, „wapno”, województwo po województwie) → `data/olx/market/spis-2026-09-23.json`.

**Spis 23.09:** 6 748 ogłoszeń z 6 928 widocznych (mazowieckie ~1 050 z 1 222), **451 sprzedawców**.

| # | Sprzedawca (`user_id`) | Ogłoszeń |
|---|---|---|
| 1 | 699-712-071 (729325007) | **496** |
| 2 | Wapna Świętokrzyskie / plusplon (594644825) | 269 |
| 3 | Agro-Siew (829365914) | 224 |
| 4 | Robert (18710719) | 204 |
| 5 | WAP-POL / wapno.29 (1620934466) | 200 |
| … | WAP POL, Nawozy wapniowe granulowane, 730-918-232 | ~200 każdy |
| **8** | **AGRIA (43762401)** | **200 (3,1%)** |

- **AGRIA nie jest 2. sprzedawcą (raport 28.08), tylko 8.** Lider **nie spadł** z 510 do 122 — ma 496,
  ostatnio podbite 22.09. Siedmiu graczy trzyma dokładnie ~200 ogłoszeń — to ten sam pakiet Premium 200.
- **AGRICOM** i konto „Ewelina” (teza 28.08): **brak w spisie** pod tymi nazwami — nierozstrzygalne
  wstecz, bo 28.08 nie było spisu.
- **Diff z 07.08 i 28.08 po `user_id` jest niewykonalny** — tamte pliki to próbki. Pierwszy porównywalny
  diff: następny spis (`--spis-diff`). Z próbek wolno czytać tylko napływ: od 09.09 weszło 133 nowe ogłoszenia
  wapienne, najwięcej `511521347` (33), SILUX (21), wapno.apmagro (20).
- **Kopie:** dwa cudze tytuły z „Agrobielik” (odsprzedaż towaru Nordkalk, nie kopia naszych tytułów);
  fraz „cena za towar”, „luzem i big bag”, „, AGRIA” u innych — zero. **Zdjęć nie porównywano** pikselowo.
- **Promowanych** w spisie: 202 z 6 528 (3%).

## 8. Co dalej przed sezonem zimowym

- **Wykonane (T-146, decyzja Janka 23.09):** 8 z 18 ogłoszeń węglanowego z Mg granulowanego (0,33) →
  węglanowe granulowane (1,48): Żabno, Grybów, Dąbrowa Tarnowska, Chełm, Puławy, Oświęcim, Wieliczka, Pruchnik.
- **Bez zmian do listopada:** Agrobieliki (74 ogł.) — słabe w VIII–IX, ale to wapno palone ze szczytem X–XI;
  „do stawu” (17) — sezon stawowy to jesień po spuszczeniu wody.
- **Ograniczenie kategorii:** pakiet obejmuje wyłącznie Nawozy (4368). Zimowe paszarstwo (kreda pastewna —
  rynek w 765/761) i wapno hydratyzowane (budownictwo) nie mają tu miejsca; 2 ogłoszenia kredy pastewnej
  zostają do rewizji.
- **Rewizja sezonowa — listopad**, na danych z października; poza wyceną obsługi, kwotę ustala Janek.

## 9. Wykonane 23.09 (T-142…T-146)

| Zadanie | Ogłoszeń | Wynik |
|---|---|---|
| T-145 spis rynku | — | `market_snapshot.py --spis` / `--spis-diff`, spis 23.09 zapisany |
| T-142 nabór łódzki | 5 | sekcja usunięta |
| T-143 parametry wg kart (+ T-142) | 126 + 5, razem 128 unikalnych | pilot 3 → 125, zero odrzutów |
| T-146 Mg granul. → węgl. granul. | 8 | nowy `external_id`, front bez powtórzeń w 100 km |
| T-144 przełożenie martwych | 29 | pilot 3 → 26, zero odrzutów, 29/29 zgodnych |

**Weryfikacja:** odczyt per ogłoszenie **200/200 `active`**, telefon, `auto_extend`, brak starych fraz
(`tresc.py --sprawdz`: 0 problemów); konto = `posted.json` = `adverts-payload.json` co do `external_id`,
miasta, tytułu, opisu i liczby zdjęć (0 rozjazdów); pakiet `left: 0` bez zmian (nic nie zjadło jednostki).
Render przez przeglądarkę: Zator (staw), Żabno (T-146), Żarnowiec (T-144). Backupy:
`data/backups/olx-tresc-przed-2026-09-23.json`, `olx-przelozenie-przed-2026-09-23.json`.

Punkt kontrolny: **07.10** (kalendarz „Auranet Claude”, `docs/przypomnienia/2026-10-07-recheck-olx-audyt.md`).

## Czego nie zmierzono

- **Ile odsłon numeru zamieniło się w telefon i w sprzedaż.** Janek dowiaduje się u Pawła przy okazji;
  bez tego koszt kontaktu to koszt odsłony numeru, nie zapytania.
- **Porównanie z Google Ads** — w tym wątku nie odświeżane.
- **Efekt zmian z 23.09** — pomiar 07.10.
- **Rozkład dzienny** — pomiary co tydzień, podbicie 19.09 i weekendy nie dają się odciąć.
- **Czy zdjęcia konkurencji kopiują nasze** — brak porównania obrazów.
- **Rynek w mazowieckim** — spis łapie ~86% ogłoszeń tego województwa.
