# Prompt kontynuacyjny — OLX: co najmniej 10 różnych frontów (T-138)

> Wklej całość do nowej sesji `claude` w `~/projekty/agria`. Wątek poprzedni: T-137 (11.09.2026),
> commit `952a816`, wiersz w dzienniku M4 `docs/REJESTR_ZOBOWIAZAN.md`.

## Zadanie

200 ogłoszeń AGRII na OLX ma dziś **16 plików pierwszego zdjęcia, ale tylko 3 różne sceny**
(wywrotka zsypuje na polu — 72 ogł., hałda na polu — 66, auto z HDS i big bagami — 61, załadunek — 1).
Na liście wyników rolnik widzi w kółko tę samą wywrotkę z innym napisem. **Cel Janka: co najmniej
10 różnych frontów.** Źródła:

1. **Zdjęcia Janka z placu** — Dysk `AGRIA/zdjęcia/2026.09.10` (folder `1GiaDWCiQwmm9x4WjD4dYLgZkK4ahxpu6`),
   6 plików wrzuconych 11.09 13:29, nazwy `WhatsApp Image 2026-09-10 at 10.34.02*.jpeg`, ID:
   `1FmWuO-PJkgKuRn34vGvMDDp-WNNX-M4J`, `1SS0Q31L7PAKzzBRMzpanr4xcPsvpKWrN`, `1ifYiiK6xs2tb2-OqryskE1SyNzGCuxzj`,
   `1Le6DTkhgLuBkqofhlFIZ_zmhpAxwpX3C`, `17FY0pAXoc_HDA_r8-A1ZvnpsOl3si65L`, `1AcUpI0ip61sTiOP5W5fuanD0x5ZYz9Mt`.
   Wg opisu Janka: worki wapna hydratyzowanego Bielik, big bagi z budynkiem AGRII w tle (kilka ujęć),
   big bagi z bliska. **Nie obejrzane jeszcze przez model** — zacznij od obejrzenia.
2. **Wygenerowane 11.09 (zaakceptowane)** — `~/domains/auratest.pl/public_html/agria-olx/v4/agria-foto-{wywrotka-zsyp,halda-pole,zaladunek,hds-bigbagi}.jpg`.
3. **8 nowych scen do wygenerowania** — propozycje w `scripts/olx/sceny_gemini.py` (słownik `NOWE`),
   **niewygenerowane**. Janek: „użyć wygenerowanych + te, które wybierzemy, lub wszystkie”.

**Każdy front dostaje białe pole z napisem** — także zdjęcia Janka.

## Kolejność

1. Pobierz 6 zdjęć Janka (Drive MCP `download_file_content` — wynik >200 tys. znaków ląduje w pliku
   `tool-results/…txt`, JSON z `content` w base64 → zdekoduj do scratchpadu). Obejrzyj, sprawdź rozdzielczość
   (WhatsApp kompresuje — kadr 4:5 musi mieć sensowną jakość), opisz każde jednym zdaniem.
2. Wygeneruj 8 scen z `NOWE` (`sceny_gemini.py <scratchpad>` — sekwencyjnie), plansza do wyboru na auratest.
   **Quiz do Janka** (AskUserQuestion, multiSelect): które jego zdjęcia i które nowe sceny wchodzą.
3. Wybrane → kadr 4:5 (896×1152, jak v4) → do `agria-olx/v4/agria-foto-<nazwa>.jpg` → napisy przez
   `scripts/olx/miniatury_v4.py` (dopisać sceny do `PLAN` albo wydzielić funkcję nakładania napisu).
4. **Rozkład frontów** — nowy plan przydziału: ten sam produkt w sąsiednich miastach nie powtarza sceny;
   zdjęcia z big bagami do produktów w big bagach, luz do luzu (patrz reguły niżej). Mockup przed/po jak
   `auratest.pl/fe4f58fec53ctmp/agria-olx-mockup-wymiana-zdjec-v2-2026-09-11.html` — **akcept Janka**.
5. Podmiana: `scripts/olx/zdjecia_v4.py` (GET → `putable()` → podmiana samego `images` → PUT;
   **nie** `post_adverts.py --update`). Najpierw `--backup`, pilot 3, potem reszta, bezpiecznik co 25.
   Po PUT aktualizuj `adverts-payload.json` (skrypt to robi) — inaczej późniejsze `--update` cofnie zdjęcia.
6. Weryfikacja per ogłoszenie 200/200 (`active`, `auto_extend`, liczba zdjęć = plan, miasto, `external_id`,
   telefon) + podgląd kilku pierwszych zdjęć z CDN OLX (`https://www.olx.pl/api/v1/offers/<id>/`).
7. Wiersz w dzienniku M4 rejestru, zamknięcie T-138, commit + push (Janek zlecił ten tryb w T-137).

## Wzór napisu — zaakceptowany 11.09, nie zmieniać

Białe pole u góry, **marginesy 7%** z boków i od góry, **wysokość pola 20%** zdjęcia, napis
**Plus Jakarta Sans ExtraBold** (`assets/brand/fonts/`), kolor **`#07571e`**, wielkie litery, wyśrodkowany,
dopasowany do 92% szerokości i 62% wysokości pola. Implementacja: `miniatury_v4.py`.

Napisy per produkt (akcept Janka 11.09):
WAPNO DO STAWU (Agrobielik 70 staw) · WAPNO NAWOZOWE (Agrobielik 70 gleba, Agrobielik 90, Oxyfertil 90) ·
WAPNO GRANULOWANE (węglanowe granulowane) · WAPNO MAGNEZOWE (węglanowo-magnezowe granulowane, odm. 04, odm. 05) ·
WAPNO WĘGLANOWE (węglanowe odm. 04) · KREDA NAWOZOWA (sypka) · KREDA GRANULOWANA · KREDA PASTEWNA.

## Reguły — decyzje już zapadły, nie wracać do nich

- **Etykieta na zdjęciu musi pasować do produktu.** Big bag z napisem Agrobielik tylko przy Agrobielikach.
  **Worki Bielik (wapno hydratyzowane) nie idą do ogłoszeń nawozowych** — Bielik nie jest w ofercie OLX,
  a worki wypadły z tytułów po uwadze moderacji (cena za tonę). Ads: „dostawca całosamochodowy, nie sklep z workami”.
- **Zero scen z rozsiewem** (auto wapnujące, ciągnik z rozsiewaczem) — Janek odrzucił; AGRIA nie świadczy rozsiewu.
- **Zero ceny w tytule** — decyzja 20.08 po wstrzymaniu pilota przez moderację (`scripts/olx/plan.py`).
- Tytuły kończą się „, AGRIA” (T-137) — zdjęć to nie dotyczy, tytułów nie ruszasz.
- Każdy zapis na koncie OLX klienta **po „ok” Janka per operacja**. „Ok” na mockup = zgoda na podmianę zdjęć,
  nic więcej (lekcja z 11.09: nie wyprowadzać zgody z wiadomości, która jej wprost nie zawiera).
- **Jeśli czegoś nie widzisz** (pusty folder, brak plików) — zatrzymaj się i powiedz wprost, co wypada z planu.
  11.09 zdjęcia Janka nie dotarły na Dysk, a model przerobił plan na same wygenerowane bez zgłoszenia —
  stąd 3 fronty zamiast 10+.

## Kontekst pomiarowy

- Punkt odniesienia przed T-137 (11.09 12:08): 1 137 odsłon, 36 odsłon numeru, **27,2 odsłony/dobę**
  w oknie 07→11.09 — `docs/raporty/2026-09-11-OLX_STAN_PRZED_WYMIANA_ZDJEC.md`.
- **Odczyt 14.09** — cron `statystyki.py --zapisz --telegram` o 7:35, kalendarz „Auranet Claude” 9:00,
  prompt `docs/przypomnienia/2026-09-14-odczyt-olx-po-T-137.md`. Zmiana frontów przed poniedziałkiem
  miesza się z T-137 — Janek: „nieważne, z jakiego powodu ruch się zwiększy”. Zapisz, kiedy weszła.
- ⛔ **Pakiet OLX wygasa 16.09** (T-105, przelew po stronie Pawła). Bez odnowienia 200 ogłoszeń gaśnie —
  podmiana zdjęć po tej dacie ma sens tylko po odnowieniu. Wiadomość do Pawła poszła Jankowi na Telegram 11.09.

## Pułapki techniczne

- **LVE: limit procesów.** 11.09 `ThreadPoolExecutor` z `curl` na wątkach + 4 sesje Claude = `fork: Resource
  temporarily unavailable`, komendy padały bez wyniku. Odpytywanie OLX **sekwencyjnie**.
- Wyjście Pythona do pliku w tle jest buforowane — `python3 -u`.
- `seria_c.py --przeloz` przed poprawką przepuszczał już przełożone ogłoszenie (naprawione).
- 8 ogłoszeń nie ma zdjęcia „studio” (kreda granulowana — karta ID 305 ma zdjęcie innego produktu), stąd 5 zdjęć w galerii.
- Kategoria 4368: limit 8 zdjęć na ogłoszenie; QR z kalkulatorem musi zostać ostatni (opis ogłoszenia się do niego odwołuje).
