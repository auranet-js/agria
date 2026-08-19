# Protokół wspólny — obowiązuje przy każdym tasku z tego katalogu

> Czytasz ten plik **raz, na starcie wątku wykonawczego**, a potem plik konkretnego taska.
> Wszystko, czego tu nie ma, a jest specyficzne dla zadania, stoi w pliku `T-NNN-*.md`.
> Stan kanałów zmierzony **2026-08-19 15:00–15:30** — sekcja „Testy kanałów" niżej.

## 1. Zanim cokolwiek dotkniesz

1. `CLAUDE.md` — §2 kanały dostępu, **§4 strefy kruche**, §5 czego nie wolno bez pytania.
2. `docs/REJESTR_ZOBOWIAZAN.md` — wiersz tego taska. Jeśli wiersz mówi co innego niż plik
   promptu, **wiersz rejestru wygrywa** i najpierw ustalasz z Jankiem, skąd rozjazd.
3. `docs/FAKTY_KLIENTA.md` — otwierasz, gdy task dotyka oferty, cen, ludzi, ustaleń handlowych.
4. Plik taska z tego katalogu — w całości, łącznie z sekcją „Strefy kruche".

## 2. Zgoda na zapis

**Każdy zapis na produkcję wymaga zgody Janka w czacie, per operacja.** Nie zbiorczej,
nie domniemanej z faktu, że task jest w kolejce. Prompt taska mówi, co zapisze — ty pokazujesz
to Jankowi jako konkret („zmieniam meta X na ID Y, oto diff") i czekasz.

Wyjątki nie istnieją. Odczyt (`query_db`, `read_file`, `curl`, GSC, Ads, PSI, GBP read) — bez pytania.

## 3. Backup przed zapisem — który mechanizm do czego

| Co zmieniasz | Backup |
|---|---|
| plik w `agria-by-auranet` / motywie | `mcp__agria__backup_file` (tworzy `.bak-YYYYMMDD-HHiiss`) — MCP `write_file` robi to sam, ale przy ręcznej edycji przez SSH **nie** |
| `post_content` / `postmeta` | `mcp__agria__db_export` na `posts` + `postmeta` **przed** pierwszym zapisem w sesji, plus zapisz `LENGTH()` starej wartości i podaj jako `expect_old_len` |
| `.htaccess` | pobierz FTP-em do `tmp/`, **pokaż diff Jankowi**, dopiero potem upload. Zawsze zostaw kopię z datą |
| ustawienia WP / opcje | `wp option get <klucz> --format=json` do pliku w `tmp/` przed zmianą |
| GBP, Ads, OLX | zrzut stanu przed zmianą do `tmp/` (JSON z API) — te systemy nie mają undo |

Backup zostaje **poza web rootem** albo pod nazwą, której serwer nie wyda (`db_export` pisze do
`wp-content/` — po użyciu przenieś przez SSH i skasuj oryginał, plik `.sql` w web rootcie to wyciek).

## 4. Testy kanałów — wynik z 2026-08-19, powtórz przed pracą

Każdy kanał ma komendę weryfikującą. Uruchom ten, którego task używa — zajmuje sekundy,
a oszczędza godzinę diagnozy „czemu nie zapisało".

| Kanał | Komenda | Wynik 19.08 |
|---|---|---|
| MCP odczyt | `mcp__agria__status` | ✅ PHP 8.3.33, WP 7.0.4, WC 10.9.3, prefix `wpfz_` |
| MCP zapis pliku | `write_file` → `read_file` → sprzątnięcie | ✅ zapisał 139 B do `_mcp-write-test.txt`, odczytał, usunięty przez SSH |
| MCP zapis meta | `query_db_write` INSERT → `update_postmeta` UPDATE → `wp post meta delete` | ✅ `affected: 1`, readback `match: true` |
| MCP `backup_file` | na `modules/seo-head/seo-head.php` | ✅ `.bak-20260819-150827`, skasowany po teście |
| SSH + WP-CLI | `ssh agria-prod 'wp --path=$HOME/agria.pl core version'` | ✅ `7.0.4`, WP-CLI 2.4.0 |
| FTP odczyt | `curl --netrc-file ~/secrets/agria/netrc ftp://ftp.server371853.nazwa.pl/agria.pl/` | ✅ widzi `.htaccess` (3 947 B, 55 linii) |
| FTP zapis + kasowanie | upload `_ftp-write-test.txt` → `curl` HTTP 200 → `-Q "-DELE …"` → HTTP 404 | ✅ pełny cykl przeszedł |
| HTTP produkcja | `curl -I https://agria.pl/` | ✅ 200, 5 nagłówków bezpieczeństwa |
| Chrome MCP | `navigate` + `get_page_text` na `/do-pobrania/` | ✅ zwrócił 32 pozycje listy |
| GSC URL Inspection | patrz `scripts/gsc_inspect.py` | ✅ zwróciło werdykt dla 7 URL-i |
| PSI / Lighthouse | `curl …pagespeedonline…&key=$(cat ~/secrets/google/psi-crux-key.txt)` | ✅ **kwota wróciła**, perf 0,70, LCP 7,4 s, `runtimeError: None` |
| Google Ads API | `bash scripts/google/ads_call.sh /googleAds:searchStream POST q.json` | ✅ 2 kampanie, koszt 199,62 zł / 0 zł |
| GBP API | `mybusinessbusinessinformation…/locations/11686460679773422640` | ✅ odczyt profilu Tarnów; oddziałów **brak na koncie** |
| Indexing API | `~/bin/index-submit --status` | ✅ 0/100 zużyte, `--dry-run` przechodzi |
| OLX Partner API | `~/bin/olx-agria status` → `refresh` → `api /partner/adverts` | ⚠️ **token wygasa po ~24 h** — `refresh` jest krokiem obowiązkowym przed każdą sesją OLX |
| Poczta do Janka | `~/bin/send-to-jan --dry-run` | kanał jedyny dozwolony; nic nie idzie do klienta |

## 5. Pułapki narzędzi — zmierzone, nie z dokumentacji

- **`update_postmeta` NIE tworzy nowej meta.** Zwraca `postmeta not found`, jeśli klucza nie ma.
  Nową meta zakładasz `query_db_write` INSERT-em albo `wp post meta add` — i wtedy **czyścisz cache**
  (`wp cache flush`), bo INSERT idzie obok WordPressa.
- **`query_db_write` blokuje DELETE, DROP, ALTER, TRUNCATE, CREATE.** Kasowanie czegokolwiek =
  WP-CLI przez SSH. Blokada łapie też słowo `REPLACE` w SELECT-cie — funkcja stringowa `REPLACE()`
  w `query_db` zwróci „Write operations not allowed", użyj `LIKE` albo policz lokalnie.
- **`query_db` tnie na 100 wierszach.** Przy większych zbiorach stronicuj `LIMIT/OFFSET`.
- **`na-ls-cache-enabled: off`** na produkcji 19.08 — cache LiteSpeed nazwa.pl jest dziś wyłączony,
  więc `curl` pokazuje stan bieżący. **Zweryfikuj ten nagłówek zanim uwierzysz, że cache-bust
  jest zbędny** — ustawienie może wrócić i wtedy `?cb=$(date +%s)` znowu jest obowiązkowy.
- **Treść stron istnieje równolegle w `post_content` i `_elementor_data`.** Na ID 731 słowo
  „ertyfikat" siedzi w **obu**. Zmiana jednej warstwy daje rozjazd, który wraca przy pierwszym
  otwarciu Elementora. Zmieniasz obie albo świadomie decydujesz, która jest źródłem.
- **Geoblok (`security-geoblock.php`) przepuszcza boty z listy `$good_bots` i jest fail-open**,
  ale działa tylko na ruchu docierającym do PHP. Po każdej zmianie w tym pliku sprawdzasz
  `curl -A "Googlebot" -I https://agria.pl/` **i** zwykłym UA.

## 6. Dowód — co ma się znaleźć w rejestrze

**Wiersz bez dowodu nie ma prawa mieć ✅.** Dowód to jedna z tych rzeczy, wklejona dosłownie:

- wynik `curl` z widocznym kodem HTTP i fragmentem treści po zmianie,
- wynik `query_db` pokazujący nowy stan (nie „zapisałem", tylko liczba wierszy i wartość),
- werdykt GSC URL Inspection z datą crawla,
- liczba z API (Ads: koszt/wyświetlenia; PSI: LCP; GBP: id opublikowanego postu),
- hash commitu, gdy artefaktem jest plik w repo.

Słowa **„zrobione / działa / naprawione / sprawdzone"** wolno napisać wyłącznie z dowodem obok.
Bez dowodu piszesz „niezweryfikowane" — i weryfikujesz, zanim zaraportujesz.

## 7. Rozliczenie

| Zakres | Co znaczy | Gdzie ląduje |
|---|---|---|
| **R** | ryczałt 2 000 netto/mies (M1–M6) | DZIENNIK M3, godziny realne |
| **P** | poza ryczałtem, osobna pozycja handlowa | DZIENNIK + nota do rozliczenia z Jankiem |
| **W** | własne Auranet, nie fakturujemy | DZIENNIK ze znacznikiem W |
| **K** | koszt albo robota po stronie AGRII | nie nasze godziny, tylko data zgłoszenia |

**Godziny wpisujesz przy domknięciu, realne** (od M4 gwiazdka `5 h*` już nie obowiązuje — to był
znacznik wartości nieodtworzonej wstecz). Commit zamykający pozycję **przenosi wiersz z KOLEJKI
do DZIENNIKA w tym samym commicie**.

## 8. Recheck — bo „wdrożone" nie znaczy „działa za tydzień"

Każdy task ma w swoim pliku własny termin i komendę rechecku. Reguła ogólna:

| Rodzaj zmiany | Pierwszy recheck | Drugi |
|---|---|---|
| treść / render strony | +1 h (cache, Elementor) | +7 dni (czy nikt nie nadpisał w Elementorze) |
| indeksacja | +72 h (GSC URL Inspection) | +14 dni (czy weszło i czy zostało) |
| `.htaccess`, przekierowania | natychmiast (`curl` na 3 wariantach URL) | +7 dni (logi 404) |
| Ads | +48 h (czy ruszyło) | +7–10 dni (punkt decyzyjny stawek) |
| GBP | +24 h (czy Google zatwierdził) | +30 dni (czy nie cofnął) |
| kod PHP | natychmiast (`curl` + `logs`) | +7 dni (`debug.log`) |

## 9. Czego nie robisz nigdy w tym katalogu

- Nie ustawiasz `_price` ani wariantów WooCommerce pod publikację (ADR dwie warstwy cen).
- Nie proponujesz landingów organicznych ani hubów segmentowych — `T-035`…`T-038` unieważnione.
- Nie strzelasz surowym `curl`-em do Indexing API — wyłącznie `~/bin/index-submit`.
- Nie wysyłasz niczego do klienta. Wszystko przez Janka, `~/bin/send-to-jan`.
- Nie pytasz Pawła o rzeczy z naszej kompetencji; lista dozwolonych pytań: rejestr + `FAKTY_KLIENTA.md` §8.
  Forma: telefon Janka, nie mail z tabelą.
- Nie krytykujesz stanu strony w materiałach dla klienta — zbudował ją Auranet.
