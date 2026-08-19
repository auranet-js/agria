# T-032 — 301 dla starej bazy `/kategoria-produktu/*`

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 🔴 teraz — odblokowane od 18.08 (SSH + dostęp do `.htaccess`) |
| **Szacunek** | 1 h |

---

## 1. Czego to dotyka

Plik **`.htaccess`** w roocie WP (`~/agria.pl/.htaccess`, 3 947 B, 55 linii) — blok
`# BEGIN AGRIA 301 (rdzen URL 2026-07-08)`, w którym leży już 24 reguły z migracji lipcowej.
Pośrednio: Premmerce Permalink Manager (`category_base: kategoria-produktu`), archiwa kategorii
produktowych, GSC.

## 2. Strefy kruche

1. **`.htaccess` to plik, który potrafi położyć całą stronę.** Literówka w `RewriteRule` = 500
   na każdym URL-u. Zawsze: pobierz → edytuj lokalnie → **pokaż diff Jankowi** → upload →
   natychmiastowy `curl` na stronę główną.
2. **MCP `write_file` ma `.htaccess` na liście blokad.** Jedyne drogi: FTP (zweryfikowany 19.08,
   pełny cykl zapis/kasowanie działa) albo SSH.
3. **Reguła musi trafić do bloku AGRIA 301, przed `# BEGIN WordPress`.** Za blokiem WordPress
   nie zadziała, bo `RewriteRule . /index.php [L]` przechwyci żądanie wcześniej.
4. **`category_base` w Premmerce nadal wskazuje `kategoria-produktu`.** Jeśli 301 zadziała zbyt
   szeroko, może odciąć adresy, których panel albo JetSmartFilters używa wewnętrznie.
   Wyklucz `/wp-admin` i żądania AJAX.
5. **Canonical już wskazuje czysty URL** (sprawdzone: `/kategoria-produktu/wapno-nawozowe-rolnictwo/`
   → canonical `https://agria.pl/wapno-nawozowe-rolnictwo/`), ale strona odpowiada **200
   z `index, follow`** — czyli jest kandydatem do indeksu. To uzasadnia 301.
6. **Pięć kategorii, nie więcej** (`product_cat-sitemap.xml`): `wapno-nawozowe-rolnictwo`,
   `wapno-do-oczyszczalni`, `wapno-hydratyzowane`, `paszarstwo`, `kreda-malarska`.
   Reguła generyczna `^kategoria-produktu/(.+)$` obejmie też przyszłe — to zaleta, ale sprawdź,
   czy nie łapie czegoś, co ma zostać.
7. **`/kategoria-produktu/` (sam prefiks) daje dziś 404** — zostaw tak albo skieruj na `/oferta/`,
   spójnie z regułami z lipca (`^wapno-nawozowe-hurt/?$ → /oferta/`).

## 3. Stan zmierzony 19.08.2026

```
/kategoria-produktu/                            → 404
/kategoria-produktu/wapno-nawozowe-rolnictwo/   → 200, canonical /wapno-nawozowe-rolnictwo/, index+follow
/kategoria-produktu/test-abc/                   → 404
kategorie w sitemapie: 5
.htaccess: blok AGRIA 301 istnieje, 24 reguły R=301, przed blokiem WordPress
```

## 4. Warunki wejścia

- [ ] Kopia `.htaccess` pobrana FTP-em do `tmp/htaccess-<data>.txt`.
- [ ] Diff pokazany Jankowi, „ok" w czacie.

## 5. Co robisz

1. Pobierz `.htaccess`:
   ```bash
   curl -s --netrc-file ~/secrets/agria/netrc ftp://ftp.server371853.nazwa.pl/agria.pl/.htaccess \
     -o tmp/htaccess-$(date +%F).txt
   ```
2. Dopisz **w bloku AGRIA 301**, po ostatniej regule produktowej, przed `</IfModule>`:
   ```apache
   # kategorie pod stara baza -> czysty URL (T-032, 2026-08-xx)
   RewriteRule ^kategoria-produktu/([^/]+)/?$ /$1/ [R=301,L]
   RewriteRule ^kategoria-produktu/?$ /oferta/ [R=301,L]
   ```
3. Pokaż Jankowi `diff tmp/htaccess-<data>.txt tmp/htaccess-nowy.txt`.
4. Po „ok" — upload:
   ```bash
   curl -T tmp/htaccess-nowy.txt --netrc-file ~/secrets/agria/netrc \
     ftp://ftp.server371853.nazwa.pl/agria.pl/.htaccess
   ```
5. **Natychmiast** `curl -sI https://agria.pl/` — jeśli 500, wgraj kopię z kroku 1 bez pytania.

## 6. Jak sprawdzasz w trakcie

Po uploadzie, w tej kolejności: strona główna → jedna kategoria czysta → jedna kategoria stara →
panel `/wp-admin/` (kod 302 na login, nie 500).

## 7. Jak testujesz po wdrożeniu

```bash
# 1. wszystkie pięć kategorii przekierowuje jednym skokiem
for c in wapno-nawozowe-rolnictwo wapno-do-oczyszczalni wapno-hydratyzowane paszarstwo kreda-malarska; do
  printf '%-30s %s → %s\n' "$c" \
    "$(curl -s -o /dev/null -w '%{http_code}' https://agria.pl/kategoria-produktu/$c/)" \
    "$(curl -s -o /dev/null -w '%{redirect_url}' https://agria.pl/kategoria-produktu/$c/)"
done
# 2. docelowe nadal 200
for c in …; do curl -s -o /dev/null -w '%{http_code}\n' https://agria.pl/$c/; done
# 3. brak pętli
curl -sIL https://agria.pl/kategoria-produktu/paszarstwo/ | grep -c '^HTTP'    # ≤ 2
# 4. reguły z lipca nietknięte
curl -s -o /dev/null -w '%{http_code} %{redirect_url}\n' https://agria.pl/wapno-nawozowe-hurt/
# 5. panel i REST żyją
curl -s -o /dev/null -w 'admin %{http_code}\n' https://agria.pl/wp-admin/
curl -s -o /dev/null -w 'rest  %{http_code}\n' https://agria.pl/wp-json/
```

## 8. Dowód do rejestru

Tabela pięciu kategorii: kod + `redirect_url`, wynik testu pętli, potwierdzenie że reguły lipcowe
i panel działają, nazwa pliku kopii zapasowej.

## 9. Rollback

`curl -T tmp/htaccess-<data>.txt … ftp://…/.htaccess` — powrót do stanu sprzed zmiany.
Cykl zapisu FTP zweryfikowany 19.08.

## 10. Rozliczenie

Zakres **R**, ~1 h. DZIENNIK M3.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **natychmiast** | pięć kategorii + panel + REST |
| **+24 h** | logi serwera pod kątem 500 i pętli przekierowań |
| **+14 dni** | GSC: czy stare adresy wypadają z raportu pokrycia |
| **+30 dni** | czy aktualizacja Premmerce nie nadpisała `category_base` w sposób kolidujący z regułą |
