# Prompt wdrożeniowy — dziesięć pozycji „teraz", do T-032 włącznie

> **Wątek wykonawczy.** Zamykasz dziesięć pozycji z sekcji 🔴 rejestru. To jest robota na produkcji
> klienta, nie planowanie — plan jest gotowy i leży w `docs/prompty/wdrozenie/`.
>
> **Zakres kończy się na `T-032`.** `T-039` (Ads), `T-042` (OLX), `T-046` (GBP) zostają poza tym
> wątkiem mimo że są w „teraz" — dotykają systemów zewnętrznych, w których nie ma cofnięcia,
> i dostają osobne prompty. To samo dotyczy `T-043` (kalkulator, sekcja 🟡).
> **Nie bierz ich „przy okazji", nawet jeśli zostanie czas.**

---

## Zanim napiszesz pierwsze słowo

Czytasz w tej kolejności, w całości:

1. **`CLAUDE.md`** — §2 cztery kanały dostępu, **§4 strefy kruche**, §5 czego nie wolno bez pytania.
2. **`docs/prompty/wdrozenie/00-PROTOKOL-WSPOLNY.md`** — zgoda na zapis, backupy, testy kanałów,
   pułapki narzędzi zmierzone 19.08, definicja dowodu, rozliczenie, terminy rechecku.
3. **`docs/REJESTR_ZOBOWIAZAN.md`** — wiersze dziesięciu pozycji. Rejestr jest nadrzędny:
   jeśli mówi co innego niż plik promptu, **pytasz Janka, skąd rozjazd**, zamiast wybierać.
4. **Plik konkretnej pozycji** z `docs/prompty/wdrozenie/` — dopiero gdy do niej dochodzisz.

`docs/FAKTY_KLIENTA.md` otwierasz przy `T-010`/`T-011` obowiązkowo (§7 — ustalenia cenowe).

Reguły komunikacji ładują się z memory (`feedback_agria_*`). Nie czytasz ich z dokumentu i nie
powtarzasz w odpowiedziach.

---

## Punkt decyzyjny na starcie — jedno pytanie, zadaj je zanim ruszysz

**Worki w `T-010`:** publikujemy wyłącznie przeliczenia na tonę, czy także ceny za sztukę?
`FAKTY_KLIENTA.md` §7 rekomenduje tylko tonę (Paweł podał ceny workowe i w tym samym mailu
napisał, że sprzedaży po worku nie prowadzi). **Bez odpowiedzi nie piszesz pierwszej karty** —
to jedyna rzecz w tym wątku, która blokuje start.

Wszystko inne rozstrzygasz sam albo zgodnie z plikiem pozycji.

---

## Kolejność i dlaczego taka

```
1. T-048                    20 min, dowód już zdobyty — najtańsze domknięcie w kolejce
2. T-008 ─┬─ T-009 ─→ T-027 jedna strona (ID 731), jedna wizyta, potem zgłoszenie
          └─ dwie warstwy treści naraz
3. T-010 ─── T-011          PRIORYTET 1, jedna edycja na tych samych 15 kartach
4. T-029                    bezpieczeństwo, otwarte 65 dni, trzy kanały wycieku
5. T-032                    .htaccess — osobno, bo ryzyko dotyczy całej witryny
6. T-028 ─── T-026          diagnostyczne; mogą skończyć się wnioskiem zamiast zmianą
```

`T-048` idzie pierwszy, bo zamyka się w dwadzieścia minut i **odblokowuje `T-031`** na wrzesień.
`T-010` jest priorytetem merytorycznym, ale nie startuje wątku — najpierw domykasz to,
co jest gotowe, żeby kolejka realnie zmalała.

`T-028` i `T-026` idą na koniec, bo **oba mogą zakończyć się decyzją „bez działania"**
i to jest ich pełnoprawne domknięcie. Nie rób z nich zadań wykonawczych na siłę.

---

## Dziesięć pozycji

| # | ID | Co zamykasz | Plik | Szac. |
|---|---|---|---|---|
| 1 | **T-048** | geoblok vs Lighthouse — wpisanie dowodu PSI | [`T-048`](wdrozenie/T-048-geoblok-lighthouse.md) | 0,3 h |
| 2 | **T-008** | 8 atestów i kart Nordkalku na `/do-pobrania/` | [`T-008`](wdrozenie/T-008-atesty-i-karty-nordkalk.md) | 2–3 h |
| 3 | **T-009** | usunięcie sekcji „Certyfikaty" | [`T-009`](wdrozenie/T-009-usuniecie-sekcji-certyfikaty.md) | 1 h |
| 4 | **T-027** | zgłoszenie `/do-pobrania/` do reindeksacji | [`T-027`](wdrozenie/T-027-reindeksacja-do-pobrania.md) | 0,25 h |
| 5 | **T-010** | widełki cenowe w treści 15 kart + 2 landingi + poradnik | [`T-010`](wdrozenie/T-010-ceny-w-tresci-15-kart.md) | 6–8 h |
| 6 | **T-011** | nagłówki H2 z frazą cenową | [`T-011`](wdrozenie/T-011-naglowki-H2-cenowe.md) | z T-010 |
| 7 | **T-029** | login `js` w schema, REST i enumeracji autora | [`T-029`](wdrozenie/T-029-login-admina-w-schema.md) | 1,5 h |
| 8 | **T-032** | 301 dla `/kategoria-produktu/*` | [`T-032`](wdrozenie/T-032-301-kategoria-produktu.md) | 1 h |
| 9 | **T-028** | duplikaty pod starą bazą `/produkt/` + 15 sierot | [`T-028`](wdrozenie/T-028-duplikaty-produkt.md) | 2 h |
| 10 | **T-026** | sześć URL-i poza indeksem — diagnoza | [`T-026`](wdrozenie/T-026-szesc-url-poza-indeksem.md) | 2–3 h |

Razem 16–21 h. **Do końca M3 zostało dwanaście dni.**

---

## Osiem rzeczy, które zmierzyłem 19.08 i które zmieniają wykonanie

Nie są w rejestrze — rejestru nie zmieniałem. Przy każdej pozycji sprawdź, czy wiersz rejestru
nadal opisuje stan, zanim zaczniesz działać wg niego.

1. **`T-048` ma dowód.** Kwota PSI wróciła; pomiar 19.08 15:02: score 0,70, LCP 7,4 s,
   `runtimeError: None`, `finalUrl` prawidłowy. Lighthouse wyrenderował stronę — geoblok nie odciął.
   Zrób świeży pomiar w dniu domykania i wpisz go do wiersza.
2. **`T-028` jest opisany odwrotnie niż jest.** HTTP 200 pod `/produkt/*` **nie pochodzi**
   od piętnastu wpisów `post_type=produkt` (ID 60–74) — CPT `produkt` **nie jest zarejestrowany
   w WordPressie**. To stara baza URL serwująca produkty WooCommerce, z canonicalem na właściwy
   adres. Dowód: `/produkt/wapno-palone-wysokoreaktywne/` → **404**, bo produkt WC ma inny slug.
   **Zacznij od potwierdzenia tej diagnozy, nie od naprawy.**
3. **`T-029` ma szerszy zakres.** Poza schema login wycieka przez `/wp-json/wp/v2/users`
   (publicznie, z `is_super_admin: true`) i przez `/?author=1` → 301 na `/author/js/`.
   Naprawa samej schema zostawia dwa otwarte kanały.
4. **`T-026` ma dwa URL-e przypisane na krzyż.** Zmierzone: `/kreda-malarska/` jest „Discovered",
   `/wapno-nawozowe-na-trawnik/` jest „unknown". Dodatkowo cztery poradniki **są** w sitemapie
   i **są** linkowane z huba, a `lastCrawlTime` jest puste — Google nie pobrał ich ani razu.
   To przesuwa hipotezę w stronę duplikacji wobec huba, nie techniki.
5. **Tylko trzy karty produktowe renderują z Elementora.** Z 19 produktów `_elementor_data` mają
   **307** (kreda pastewna), **310** (agrobielik-70), **320** (wapno palone mielone) — i wszystkie
   trzy są w zakresie `T-010`. Pozostałych 16 nie ma tej meta w ogóle. Wszystkie 15 URL-i
   docelowych odpowiada dziś HTTP 200.
6. **ID 731 ma treść w obu warstwach naraz.** Fraza „ertyfikat" siedzi i w `post_content`
   (36 782 B), i w `_elementor_data` (14 478 B). `T-008` i `T-009` muszą objąć obie, inaczej
   zmiana wróci przy pierwszym otwarciu Elementora przez Pawła.
7. **`update_postmeta` nie tworzy nowej meta** — zwraca `postmeta not found`. Nową zakładasz
   `query_db_write` INSERT-em i **czyścisz cache**, bo INSERT idzie obok WordPressa.
   `query_db_write` blokuje DELETE (kasowanie tylko WP-CLI), a filtr łapie też słowo `REPLACE`
   w zwykłym `SELECT`-cie.
8. **`na-ls-cache-enabled: off`** na produkcji — cache LiteSpeed nazwa.pl jest dziś wyłączony,
   więc `curl` pokazuje stan bieżący. Sprawdź ten nagłówek, zanim uznasz cache-bust za zbędny
   albo za winowajcę.

---

## Zasady, które łamiesz na własną odpowiedzialność

- **Każdy zapis na produkcję = zgoda Janka w czacie, per operacja.** Nie zbiorcza, nie domniemana
  z faktu, że pozycja jest w kolejce. Pokazujesz konkret („zmieniam meta X na ID Y, oto treść")
  i czekasz.
- **`_price` zostaje puste w 19/19.** Wariantów ani atrybutów cenowych nie tworzysz.
  `wc/store/v1/products` odpowiada **publicznie** i zwraca pole `prices` — pierwsza cena wpisana
  w WooCommerce jest w tej samej sekundzie widoczna dla każdego, kto zna URL.
- **Cztery karty bez ceny zostają nietknięte:** Dolomit (302), Kreda czarna (303),
  Tlenkowe z Mg (313), Węglanowe odm. 05 (316). Paweł ich nie wycenił.
- **Zero żargonu.** „loco", MOQ, franco, EXW, HDS — zakaz. Cennik źródłowy jest napisany tym
  językiem, strona nie będzie. Zamiast tego: **„cena za towar, bez transportu"**.
- **Bez progu ilościowego.** Nie „minimum 24 t", tylko „przy 24 t cena wynosi od X".
- **Nie proponujesz landingów organicznych ani hubów segmentowych** — `T-035`…`T-038`
  unieważnione ADR-em na zmierzonej kanibalizacji („wapno bielik": 6 URL-i → pozycja 15,3).
- **Indexing API wyłącznie przez `~/bin/index-submit`.** Surowy `curl` jest blokowany hookiem.
- **Nic nie idzie do klienta.** Wszystko przez Janka, `~/bin/send-to-jan`.
- **Nie pytasz Pawła o rzeczy z naszej kompetencji.** Lista dozwolonych pytań: rejestr
  („Pytania do Pawła") i `FAKTY_KLIENTA.md` §8. Forma: **telefon Janka**, nie mail z tabelą.

---

## Jak wygląda domknięcie jednej pozycji

1. **Backup** wg tabeli z protokołu (§3) — `db_export`, `backup_file` albo kopia `.htaccess`.
2. **Zmiana**, po zgodzie, z `expect_old_len` tam, gdzie narzędzie je przyjmuje.
3. **Weryfikacja na renderze, nie w bazie** — `curl` plus Chrome MCP tam, gdzie liczy się układ.
4. **Dowód** wklejony do wiersza rejestru: liczba, kod HTTP, werdykt GSC, wynik z API albo hash.
   **Wiersz bez dowodu nie ma prawa mieć ✅.** Bez dowodu piszesz „niezweryfikowane".
5. **Commit zamykający pozycję przenosi jej wiersz z KOLEJKI do DZIENNIKA M3 w tym samym
   commicie**, z realnymi godzinami. Format: `[obszar] T-NNN krótki opis`.
6. **Recheck** — termin i komenda są w pliku pozycji. Wpisz je sobie, zanim przejdziesz dalej.

Nie zbieraj dziesięciu zmian do jednego commita na koniec dnia. Jedna pozycja, jeden commit,
jeden zaktualizowany wiersz.

---

## Kiedy się zatrzymać i zapytać

- `expect_old_len` nie zgadza się z rzeczywistością → ktoś edytował równolegle. **Stop.**
- Strona zwraca 500 albo białe okno po zapisie → **rollback natychmiast**, diagnoza potem.
- Diagnoza `T-028` albo `T-026` prowadzi do wniosku „bez działania" → to jest wynik, przedstaw go
  Jankowi i domknij wiersz, nie szukaj roboty na siłę.
- Pozycja okazuje się większa, niż zakłada plik (np. poprawka matchera dotyka wszystkich produktów)
  → zgłoś rozszerzenie zakresu **zanim** zaczniesz, nie po fakcie.
- Trafiasz na coś przyległego, a niezleconego → jedna linia „Zauważone obok, nie ruszam: …".
  Zgłoszenie zamiast działania.

---

## Kontekst terminowy

**31.08 kończy M3.** Raport miesięczny dla AGRII — materiał zbierasz z sekcji `DZIENNIK` rejestru,
wzorzec `docs/raporty/DOWODY_M2_2026-07.md`. Tego samego dnia rozliczenie pierwszego miesiąca
budżetu Ads (na 19.08 wydane 199,62 zł z 1 200 zł).

`T-046` (GBP Tarnów) jest **obiecany klientowi na piśmie** w raporcie M2 jako zadanie sierpnia
i **nie wchodzi do tego wątku** — jeśli do 31.08 nie ruszy w swoim, musi trafić do raportu M3
jako jawnie przesunięty, nie przemilczany.
