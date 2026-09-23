# 07.10.2026 — kontrola OLX 14 dni po audycie (T-142…T-146)

**Projekt:** agria · **Kalendarz:** „Auranet Claude” · **Termin decyzji AGRII o pakiecie:** 10.10
(pakiet Premium 200 wygasa **16.10 11:19**, ogłoszenia ważne do 19.10).

## Kontekst

Audyt 23.09: `docs/raporty/2026-09-OLX_AUDYT.md` (HTML: `auratest.pl/fe4f58fec53ctmp/agria-olx-audyt-2026-09-23.html`).
Punkt odniesienia — pomiar **23.09 10:49** (nr 12 w `data/olx/statystyki.json`), wykonany **przed** zmianami:
2 022 odsłony, 54 odsłony numeru, 45 obserwujących. Tempo 21→23.09: 75,9 odsłony i 3,28 numeru na dobę
(dwa dni po podbiciu 19.09). Następne automatyczne podbicie ok. 26.09.

Zmiany 23.09 (wiersze w `docs/REJESTR_ZOBOWIAZAN.md`):
- **T-144** — 29 martwych przełożonych: `data/olx/przelozenie-2026-09-23.json` (lista `advert_id`).
- **T-146** — 8 × Mg granulowane → węglanowe granulowane (Żabno, Grybów, Dąbrowa Tarn., Chełm, Puławy,
  Oświęcim, Wieliczka, Pruchnik) — w `posted.json` pole `zmiana_produktu: 2026-09-23`.
- **T-143** — 126 ogłoszeń z parametrami wg kart, w tym 17 „do stawu” z nowym tytułem („korekta pH wody w stawie”).
- **T-142** — 5 ogłoszeń bez naboru łódzkiego.

## Co zrobić

1. `python3 scripts/olx/statystyki.py --zapisz` (albo pomiar cronu 05.10 07:35, jeśli jest).
2. `python3 scripts/olx/audyt.py` → przekroje okna **23.09 10:49 → dziś** (funkcje `przyrost`, `dni`):
   - T-144 (29) wobec reszty — odsłony i numery na 100 ogł./dobę; przed przełożeniem te 29 miały ≤5 odsłon w ≥25 dni;
   - T-146 (8) wobec 20 dotychczasowych węglanowych granulowanych;
   - „do stawu” (17) — czy zmiana tytułu nie obcięła ruchu (sezon stawowy X–XI działa na korzyść, porównaj z gleba).
3. `python3 scripts/olx/monitor.py` / `monitor-log.json` — 200 `active`, `auto_extend`, dni pakietu.
4. `python3 scripts/olx/market_snapshot.py --spis` i `--spis-diff data/olx/market/spis-2026-09-23.json <nowy>` —
   pierwszy rzetelny diff rynku po `user_id`.
5. Koszt kontaktu: 1 275,60 zł netto / cykl (pakiet 975,60 + obsługa 300) ÷ odsłony numeru na 30 dni.
6. **Pytanie do Pawła** (przez Janka, telefonicznie): ile telefonów „z OLX” i ile zamówień — jeśli Janek
   jeszcze nie wie.

## Jak wygląda „zrobione”

Krótka notatka dla Janka: tempo kontaktów po 23.09, wynik T-144/T-146, koszt kontaktu, **rekomendacja
odnowienia pakietu z liczbą** — do rozmowy z AGRIĄ przed 10.10. Nic nie wysyłamy do klienta.
Event w kalendarzu → prefiks ✅.

## Otwarte z audytu (nie ruszone 23.09)

- Tytuły „big bag 1 t” przy granulowanych (28 + 10 ogł.) — karty mówią 500/600 kg.
- „kreda nawozowa” w tytule węglanowego odm. 04.
- `wysyp-podworze` — nietypowa geometria skrzyni (do oceny Janka).
- Rewizja sezonowa składu — listopad, poza wyceną.
