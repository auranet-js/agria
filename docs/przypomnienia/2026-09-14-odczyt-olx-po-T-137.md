# 14.09.2026 — odczyt OLX po T-137

**Co się zmieniło 11.09 (T-137, dziennik M4 w `docs/REJESTR_ZOBOWIAZAN.md`):**
1. Pierwsze zdjęcie we wszystkich 200 ogłoszeniach: zdjęcie „z placu” z białym polem i rodzajem wapna (v4).
2. „, AGRIA” na końcu tytułów (191 ogłoszeń + 9 nowych tytułów).
3. 9 ogłoszeń z zerem odsłon przełożone na odm. 05 / odm. 04 w świętokrzyskim
   (Iwaniska, Daleszyce, Bodzentyn, Szydłów, Staszów · Kije, Busko-Zdrój, Pińczów, Wiślica).

**Tego samego dnia wieczorem (dziennik M4, T-138 i T-139):**
4. **T-138** (do 17:14): pierwsze zdjęcie z 12 frontów zamiast 3 scen — 4 zdjęcia Janka z placu AGRII,
   4 nowe sceny Gemini, 4 z v4; rozkład: w jednym mieście każde ogłoszenie ma inną scenę.
5. **T-139** (17:15–17:20): **56 ogłoszeń przełożonych do miast konkurencji** (Wapna Świętokrzyskie,
   Robert, WAP POL, WAPNO-PRODUCENT) w małopolskim, świętokrzyskim, podkarpackim i mazowieckim.
   Lista: `data/olx/przelozenie-2026-09-11.json`. Ich stan 11.09 12:08: **319 odsłon, 0 odsłon numeru**.
6. **T-140** (do 18:17): wycofana scena wywrotki z błędnym wysypem (107 ogłoszeń) — w jej miejsce trzy
   poprawne wysypy; 25 frontów i 82 miejsca w galerii. Na liczby odsłon wpływa marginalnie.

Decyzja Janka: odczyt „więcej czy mniej wejść” po 3 dniach — bez rozdzielania, która zmiana zadziałała.

## Co zrobić

1. Sprawdzić, że cron o 7:35 zapisał pomiar (`data/olx/statystyki.json`, wpis z 14.09) i poszedł Telegram.
   Jeśli nie — `python3 scripts/olx/statystyki.py --zapisz`.
2. Odsłony na dobę w oknie **11.09 12:08 → 14.09** wobec punktu odniesienia:
   - **27,2 / dobę** — okno 07.09 → 11.09 (główne porównanie),
   - 31,6 / dobę — 01.09 → 07.09,
   - 59,5 / dobę — 28.08 → 31.08 (to samo okno czwartek → poniedziałek, sierpień).
   Plus odsłony numeru (2 w 4,2 dnia przed zmianą) i obserwujący.
3. Osobno dwie grupy przełożone 11.09 — **nie rozpoznawaj ich po polu `przelozone`** (ma je 65 wpisów,
   a 3 z 56 niosą `poprzedni_external_id` jeszcze z serii B 28.08):
   - 9 z serii C — po miastach z punktu 3 wyżej: czy mają pierwsze odsłony,
   - 56 z T-139 — po `advert_id` z `data/olx/przelozenie-2026-09-11.json`: odsłony i odsłony numeru
     w oknie wobec 319 / 0 (baseline sprzed przełożenia). Hipoteza T-139: miasta konkurencji dawały
     0,25 odsłony numeru na ogłoszenie, miasta bez konkurencji 0,09.
4. `post_adverts.py --check` — 200 `active`.
5. **Pakiet wygasa 16.09** — sprawdzić z Jankiem, czy Paweł odnowił (T-105). Bez tego 19.09 wszystko gaśnie.

## Jak wygląda „zrobione”

Liczby w czacie dla Janka (tabela: przed / po / zmiana) + wiersz odczytu w dzienniku M4 rejestru.
Tło do interpretacji: ruch spada od końca sierpnia (szczyt sezonu to sierpień), a okno po zmianie
zawiera niedzielę — najmocniejszy dzień kategorii. Punkt odniesienia i tabela per wariant:
`docs/raporty/2026-09-11-OLX_STAN_PRZED_WYMIANA_ZDJEC.md`.

Zdjęcia big bagów z placu doszły 11.09 i weszły w T-138 — ten wątek jest zamknięty.
Weryfikacja stanu konta po wszystkich zmianach: `python3 scripts/olx/fronty_v5.py --sprawdz` (11.09 wieczorem: 200/200).
