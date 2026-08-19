# `.htaccess` produkcji — kopia referencyjna

`agria.pl.htaccess` to **snapshot** pliku z `~/agria.pl/.htaccess` na produkcji,
nie źródło prawdy. Źródłem prawdy jest serwer.

**Dostęp:** wyłącznie FTP (`ftp.server371853.nazwa.pl`, creds `~/secrets/agria/ftp.txt`)
albo SSH. MCP `write_file` ma ten plik na liście blokad.

**Przed każdą zmianą:** pobierz aktualny plik, zrób diff, pokaż Jankowi, dopiero potem upload.
Kopia z datą zostaje w `agria-backups/` na serwerze (poza web rootem).

**Po każdej zmianie, natychmiast:** `curl -sI https://agria.pl/` — literówka w regule
kładzie całą witrynę. Rollback to ponowny upload kopii sprzed zmiany.

## Bloki w pliku (stan 2026-08-19)

| Blok | Co robi |
|---|---|
| `# BEGIN AGRIA 301` | przekierowania po migracji URL z 08.07 (20 reguł produktowych, 3 puste archiwa kategorii) + **6 reguł T-032** dla starej bazy `/kategoria-produktu/*` |
| `# BEGIN WordPress` | standardowy routing WP — **nie edytować ręcznie**, WordPress nadpisuje |
| `# BEGIN AGRIA SECURITY HEADERS` | HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy (2026-07-30). Brakuje CSP i Permissions-Policy w pełnej formie |

**Kolejność ma znaczenie:** reguły 301 muszą stać **przed** blokiem WordPress.
Za nim `RewriteRule . /index.php [L]` przechwyci żądanie i reguła nigdy się nie odpali.
