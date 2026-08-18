# Usunięcie starej instalacji WordPressa z katalogu produkcyjnego

**Data:** 2026-08-18
**Decyzja:** Janek, w trakcie sesji o ofertowniku
**Wykonanie:** SSH `agria-prod` (dostęp uruchomiony tego samego dnia)

---

## Co znaleziono

Przy pierwszym rekonesansie po SSH, w katalogu strony `~/agria.pl/`, leżała kompletna
stara instalacja WordPressa w podkatalogu `!starastrona/`:

- **WordPress 6.9.4**, własny `wp-config.php`, data plików 27.03.2026 (dzień migracji na nową stronę);
- **1,2 GB / 30 556 plików** — w tym `wp-content/duplicator-backups/`, czyli kopie w kopii;
- baza **osobna** od produkcyjnej: `server371853_agria` vs żywa `server371853_agria2026`.

**Była dostępna z internetu.** Listowanie katalogu dawało 404, ale
`https://agria.pl/!starastrona/wp-login.php` odpowiadało **200** — działający ekran
logowania starej, nieaktualizowanej instalacji.

## Dlaczego to było istotne

Osobna baza **nie jest** zabezpieczeniem. Obie instalacje działały na tym samym koncie
systemowym, więc dowolne wykonanie kodu na starym WordPressie (stara wersja + stare
wtyczki = znane podatności, standardowy cel automatów skanujących) oznacza odczyt
`wp-config.php` żywej strony, a razem z nim dostęp do jej bazy.

Drugorzędnie: 1,2 GB miejsca zajęte przez rzecz nieużywaną od marca.

## Co zrobiono

1. **Archiwum** `~/agria-backups/starastrona-wp694-2026-08-18.tar.gz` — 961 MB, `chmod 600`.
   Świadomie **poza katalogiem stron**: w `~/agria.pl/` plik byłby publicznie pobieralny,
   a zawiera `wp-config.php` z hasłem do bazy. To byłoby gorsze niż stan wyjściowy.
2. **Weryfikacja przed usunięciem** — `tar -tzf` przeszedł całość bez błędu odczytu,
   liczby zgodne co do jednego: 30 556 plików i 5 137 katalogów na dysku, 35 693 wpisy
   w archiwum.
3. **`rm -rf ~/agria.pl/!starastrona/`** po drugim potwierdzeniu Janka.

## Stan po

| | Przed | Po |
|---|---|---|
| `~/agria.pl` | ~1,6 GB | **394 MB** |
| `/!starastrona/wp-login.php` | 200 | **404** |
| `agria.pl`, `/wapno-nawozowe-rolnictwo/`, `/do-pobrania/`, `/kontakt/` | 200 | 200 |
| MCP `status` | działa | działa |

Katalogi pozostałe w `~/agria.pl/`: `cgi-bin/`, `home/`, `mcp/`, `wp-admin/`,
`wp-content/`, `wp-includes/`.

## Odwracalność

Wyłącznie z archiwum. Odtworzenie wymagałoby też bazy `server371853_agria` — nie
sprawdzano, czy nadal istnieje. Przed skasowaniem archiwum (nie planowane) warto to ustalić.

## Otwarte

- Baza `server371853_agria` została nietknięta — do rozważenia przy porządkach, ale
  osobno i po sprawdzeniu, czy nic z niej nie jest potrzebne.
- W `~/agria.pl/` jest jeszcze katalog `home/` o nieustalonej roli.
