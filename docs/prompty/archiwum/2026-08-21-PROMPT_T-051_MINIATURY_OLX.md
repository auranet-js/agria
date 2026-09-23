# Prompt startowy — T-051, miniatury OLX nieczytelne na telefonie (21.08.2026)

> **Skąd to się wzięło:** T-041 (publikacja 200 ogłoszeń) zamknąłem dowodem ze statusów, `auto_extend`
> i zgodności rejestru — **ani razu nie sprawdzając, jak ogłoszenie wygląda oczami klienta na telefonie**.
> Janek obejrzał i zobaczył pocięte miniatury. Weryfikacja przez API nie zastępuje obejrzenia strony.
>
> Wszystkie liczby poniżej zmierzone 21.08 na realnym OLX, emulacja iPhone 390 × 844 / DPR 2,
> mobilny User-Agent. Nie przepisane z dokumentów.

---

## Stan zmierzony — punkt wyjścia

| Miejsce | Kadr OLX | Nasz plik | Efekt |
|---|---|---|---|
| **Lista wyników, telefon** | **150 × 183 px, proporcja 0,82** (pionowy), `object-fit: cover` | 1500 × 1050, proporcja **1,43** | **widać środkowe 57% szerokości**, ginie po 21,5% z każdej strony |
| Lista wyników, komputer | 216 × 132 px, proporcja 1,64 | 1,43 | ucina górę/dół ~13%, tekst przetrwa |
| Karta ogłoszenia (mobile i desktop) | pełna szerokość, proporcje zachowane | 1,43 | **bez strat** |

**Problem dotyczy wyłącznie miniatury na liście** — czyli jedynego miejsca, w którym zapada decyzja o kliknięciu.
Karta ogłoszenia jest w porządku i jej nie ruszamy.

Co ginie na wszystkich 12 wzorach: pierwsza i ostatnia sylaba hasła („**apno na gleby ciężk**”),
początek paska korzyści („**2–4 TYGODNIE**” zamiast „EFEKT W 2–4 TYGODNIE”), sygnet Agria ucięty do „Ag”,
nagłówek produktowy u góry ucięty z obu stron.

Dowody: `https://auratest.pl/fe4f58fec53ctmp/agria-olx-miniatury-2026-08-21.html`
(zrzut listy, zrzut karty, bezpieczna strefa, siatka 12 kadrów).

## Narzędzie do weryfikacji — używać go, nie zgadywać

```
cp scripts/olx/zrzut_mobile.mjs ~/opt/pptr/narzedzia/agria-olx-mobile.mjs
pptr agria-olx-mobile "https://www.olx.pl/oferty/q-agrobielik/" /tmp/lista.png "Agrobielik 70"
```

Zwraca zrzut **i pomiar kadru** (`w`, `h`, `ratio`, `object-fit`). Trzy pułapki, każda kosztowała podejście:

1. **User-Agent musi być mobilny.** Przy desktopowym UA OLX podmienia meta viewport na `width=887`
   i mierzy się layout, którego na telefonie nie ma. Sam `setViewport` nie wystarcza.
2. **Reklamy trzeba zablokować** (`googlesyndication`, `baxter`, `btloader`…) — rozpychają stronę
   i tytuł łamie się po jednej literze na wiersz.
3. **Chrome MCP w tej sesji nie emuluje telefonu** — `resize_window` zwraca sukces, a okno zostaje 1920.
   Iframe 390 px na olx.pl też odpada: renderuje zniekształcony layout. Do zrzutów mobilnych: Puppeteer.

CDN OLX (`;s=150x160` itd.) **nie przycina** — skaluje z zachowaniem proporcji. Cały crop robi CSS
kontenera przez `object-fit: cover`. Nie ma sensu szukać rozwiązania po stronie parametrów URL.

## Trzy warianty — decyzja Janka, nie wykonawcy

**A. Miniatura pionowa 4:5 (1080 × 1350) jako pierwsze zdjęcie — rekomendacja.**
Kadr listy ma 0,82, format 4:5 ma 0,80 — przycięcie rzędu 2%. Hasło może zostać duże.
Plansze poziome zostają w dalszych slotach, karta ogłoszenia nie traci nic.
Robota: nowy generator (wzorzec `scripts/olx/miniatury.py`), 12 wzorów, podmiana w 200 ogłoszeniach.

**B. Zostawić 1500 × 1050, przeprojektować layout w bezpieczny środek 861 px.**
Nic nie ginie w żadnym widoku, ale hasło musi być krótsze albo drobniejsze, a boki zdjęcia
stają się dekoracją — płacimy połową kadru za zgodność z dwoma widokami naraz.

**C. Miniatura bez tekstu — sam towar.** Nie ma czego uciąć; tekst niesie tytuł ogłoszenia obok miniatury.
Minus: tracimy wyróżnik, który na liście faktycznie odróżnia nas od reszty (widać na zrzucie).

## Do sprawdzenia ZANIM ruszy masowa podmiana

- **Czy `PUT` ze zmienionymi zdjęciami wraca do moderacji** i po jakim czasie status wraca na `active`.
  Sprawdzić **na jednym ogłoszeniu**, nie na dwustu. Statusy `new`/`disabled` tuż po edycji są przejściowe
  (aktywacja 2–3 min, pomiar z T-041) — bezpiecznik w `post_adverts.py` już to uwzględnia.
- **Czy podmiana zdjęć zużywa miejsce z pakietu.** Pakiet ma `left: 0`; gdyby edycja liczyła się jak nowe
  ogłoszenie, nie mamy zapasu. Odczyt: `GET /partner/users/me/packets` przed i po teście na jednym.
- **Termin.** Pakiet wygasa **16.09**, emisja do 19.09. Podmiana ma sens tylko wtedy, gdy zdąży przed
  odnowieniem — inaczej robimy ją dwa razy.
- Tryb `--update` w `post_adverts.py` wgrywa całą treść z payloadu na wystawione ogłoszenia; po zmianie
  miniatur wystarczy zregenerować payload i puścić `--update`, ale **partiami i z bezpiecznikiem**, nie hurtem.

## Czego NIE cofać (poprawki po moderacji z 20.08)

Zero „netto”/„brutto” w opisie · zero klauzuli „nie stanowią oferty handlowej” · zero worków w tytułach
i liniach cenowych (big-bagi zostają, są w 136 tytułach; worki tylko w sekcji TRANSPORT) · zero telefonu
i e-maila w treści · zero kodów QR na zdjęciach produktowych.

## Czego ten wątek NIE dotyka

Treści ogłoszeń (zaakceptowane, przeszły moderację) · cen · karty ogłoszenia · zdjęć GBP (T-050) ·
T-039 (Ads) i T-026 (indeksacja).
