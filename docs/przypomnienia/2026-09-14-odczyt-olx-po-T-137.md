# 14.09.2026 — odczyt OLX po T-137

**Co się zmieniło 11.09 (T-137, dziennik M4 w `docs/REJESTR_ZOBOWIAZAN.md`):**
1. Pierwsze zdjęcie we wszystkich 200 ogłoszeniach: zdjęcie „z placu” z białym polem i rodzajem wapna (v4).
2. „, AGRIA” na końcu tytułów (191 ogłoszeń + 9 nowych tytułów).
3. 9 ogłoszeń z zerem odsłon przełożone na odm. 05 / odm. 04 w świętokrzyskim
   (Iwaniska, Daleszyce, Bodzentyn, Szydłów, Staszów · Kije, Busko-Zdrój, Pińczów, Wiślica).

Decyzja Janka: odczyt „więcej czy mniej wejść” po 3 dniach — bez rozdzielania, która zmiana zadziałała.

## Co zrobić

1. Sprawdzić, że cron o 7:35 zapisał pomiar (`data/olx/statystyki.json`, wpis z 14.09) i poszedł Telegram.
   Jeśli nie — `python3 scripts/olx/statystyki.py --zapisz`.
2. Odsłony na dobę w oknie **11.09 12:08 → 14.09** wobec punktu odniesienia:
   - **27,2 / dobę** — okno 07.09 → 11.09 (główne porównanie),
   - 31,6 / dobę — 01.09 → 07.09,
   - 59,5 / dobę — 28.08 → 31.08 (to samo okno czwartek → poniedziałek, sierpień).
   Plus odsłony numeru (2 w 4,2 dnia przed zmianą) i obserwujący.
3. Osobno 9 przełożonych (`posted.json`, `przelozone: 2026-09-11`) — czy mają pierwsze odsłony.
4. `post_adverts.py --check` — 200 `active`.
5. **Pakiet wygasa 16.09** — sprawdzić z Jankiem, czy Paweł odnowił (T-105). Bez tego 19.09 wszystko gaśnie.

## Jak wygląda „zrobione”

Liczby w czacie dla Janka (tabela: przed / po / zmiana) + wiersz odczytu w dzienniku M4 rejestru.
Tło do interpretacji: ruch spada od końca sierpnia (szczyt sezonu to sierpień), a okno po zmianie
zawiera niedzielę — najmocniejszy dzień kategorii. Punkt odniesienia i tabela per wariant:
`docs/raporty/2026-09-11-OLX_STAN_PRZED_WYMIANA_ZDJEC.md`.

Kolejny krok po odczycie (jeśli Janek zechce): wariant B pierwszego zdjęcia przy granulowanych
i Oxyfertilu — czeka na zdjęcia big bagów z placu (Dysk `AGRIA/zdjęcia/2026.09.10`, 11.09 pusty).
