# T-029 — login administratora `js` eksponowany publicznie

| | |
|---|---|
| **Linia / zakres** | SEO / bezpieczeństwo · **R** |
| **Status** | 🔴 teraz — zgłoszone w audycie 15.06, otwarte **65 dni** |
| **Szacunek** | 1–1,5 h |

---

## 1. Czego to dotyka

**Zakres jest szerszy niż zapisany w rejestrze.** Rejestr mówi o schema na froncie; zmierzone
19.08 wycieki są trzy:

| Kanał | Co ujawnia | Zmierzone |
|---|---|---|
| Schema JSON-LD | `"@type":"Person","@id":"https://agria.pl/author/js/","name":"js"` | na `/`, `/o-firmie/`, `/kontakt/`, `/do-pobrania/`, `/wapnowanie-gleby/` — wszędzie, gdzie Rank Math generuje `Article`/`BlogPosting` |
| REST API | `/wp-json/wp/v2/users` → `"name":"js"`, `"slug":"js"`, **`"is_super_admin":true`** | publiczne, bez uwierzytelnienia |
| Enumeracja autora | `/?author=1` → **301** na `/author/js/` | działa |

Dotyka: użytkownika WP **ID 1** (`user_login: js`, `display_name: js`, `user_nicename: js`,
rola administrator, **45 opublikowanych obiektów**: 16 stron, 10 wpisów, 19 produktów),
ustawień Rank Math, ewentualnie modułu `agria-by-auranet/modules/seo-head/seo-head.php`.

## 2. Strefy kruche

1. **Nie zmieniaj `user_login`.** To pole logowania — zmiana wymaga UPDATE-u w bazie i grozi
   odcięciem Janka od panelu. Ujawniany publicznie jest `display_name` i `user_nicename`,
   i to one wystarczą do naprawy.
2. **`user_nicename` siedzi w URL-u archiwum autora.** Po zmianie `/author/js/` przestanie istnieć.
   Archiwa autora mają dziś `author_robots: ['noindex']` (sprawdzone w opcjach Rank Math),
   więc SEO-neutralnie — ale sprawdź, czy nic nie linkuje do `/author/js/`.
3. **Zmiana autora 45 postów jest niepotrzebna i ryzykowna.** Nie przepisuj `post_author` —
   wystarczy zmienić dane wyświetlane.
4. **Wyłączenie REST `users` może zepsuć panel.** Blokuj **anonimowy** odczyt, nie odczyt w ogóle.
   Zalogowany edytor musi widzieć listę autorów. Filtr `rest_endpoints` albo `rest_authentication_errors`
   — nie wycinanie trasy na twardo.
5. **Geoblok przepuszcza `/wp-json`** (jawnie, w regule ścieżek) — nie licz na to, że blokuje REST.
6. **Rank Math generuje `Article` na stronach statycznych** (`/`, `/o-firmie/`, `/kontakt/`).
   To osobny dług — strona główna jako `Article` jest wątpliwa. **Nie naprawiaj przy okazji**,
   zgłoś jako kandydata na osobny wiersz.
7. Kod poprawiający schema należy do `modules/seo-head/seo-head.php` — moduł już istnieje i robi
   dokładnie takie rzeczy (wyłącza duplikat meta description z Hello Elementor). Backup przed edycją.

## 3. Stan zmierzony 19.08.2026

```
wp user list:  ID 1 | js | js | js | administrator
posty:         16 page + 10 post + 19 product = 45 obiektów autora 1
front:         Person „js" na 5 z 7 sprawdzonych URL-i
REST:          /wp-json/wp/v2/users → 200, name „js", is_super_admin true
/?author=1:    301 → /author/js/
/author/js/:   200, robots „follow, noindex"
Rank Math:     knowledgegraph_type=company, knowledgegraph_name=„AGRIA Sp. z o.o.",
               author_custom_robots=on, author_robots=['noindex'], disable_author_archives=off
```

## 4. Warunki wejścia

- [ ] Zgoda Janka — to jego konto, zmiana `display_name` zmienia podpisy w panelu.
- [ ] `wp user get 1 --format=json` zapisane do `tmp/` jako stan sprzed zmiany.

## 5. Co robisz

1. **Zmiana danych wyświetlanych** (usuwa „js" ze schema i z URL-a):
   ```bash
   ssh agria-prod "wp --path=\$HOME/agria.pl user update 1 \
     --display_name='AGRIA Sp. z o.o.' --user_nicename='agria' --first_name='' --last_name=''"
   ```
2. **Wyłączenie archiwów autora** — Rank Math → `disable_author_archives = on`. Wtedy `/author/*`
   przestaje istnieć zamiast być noindex, a schema traci `@id` z URL-em autora.
3. **Zamknięcie REST `users` dla anonimów** — filtr w `modules/seo-head/seo-head.php`
   (albo osobny mały moduł), przepuszczający zalogowanych z `list_users`.
4. **Zablokowanie `?author=N`** — przekierowanie na stronę główną dla niezalogowanych,
   w tym samym module.
5. Po każdej zmianie: `curl` na wszystkich trzech kanałach z sekcji 1.

## 6. Jak sprawdzasz w trakcie

Po kroku 1 od razu: `curl -s https://agria.pl/ | grep -o '"name":"js"'` → pusto.
Po kroku 3: `curl -s https://agria.pl/wp-json/wp/v2/users` → 401 albo pusta tablica.
**Nie idź dalej, dopóki poprzedni krok nie jest zweryfikowany** — jeśli coś zepsuje panel,
chcesz wiedzieć który krok.

## 7. Jak testujesz po wdrożeniu

```bash
# 1. schema czysta na wszystkich stronach z Article
for u in / /o-firmie/ /kontakt/ /do-pobrania/ /wapnowanie-gleby/; do
  printf '%s Person=%s js=%s\n' "$u" \
    "$(curl -s https://agria.pl$u | grep -c '"@type":"Person"')" \
    "$(curl -s https://agria.pl$u | grep -c '"name":"js"')"
done                       # oczekiwane: js=0 wszędzie
# 2. REST zamknięty dla anonima
curl -s -o /dev/null -w '%{http_code}\n' https://agria.pl/wp-json/wp/v2/users     # 401
# 3. enumeracja martwa
curl -s -o /dev/null -w '%{http_code} %{redirect_url}\n' 'https://agria.pl/?author=1'
# 4. panel działa — zalogowanie Janka i sprawdzenie listy użytkowników
# 5. brak błędów PHP
mcp__agria__logs(lines=50)
```

## 8. Dowód do rejestru

Trzy `curl`-e z sekcji 7 z wynikami zero/401, potwierdzenie od Janka, że panel działa,
`wp user get 1` po zmianie, hash commitu z kopią modułu w `src/`.

## 9. Rollback

`wp user update 1 --display_name='js' --user_nicename='js'` + `backup_file` modułu przed edycją.
Ustawienie Rank Math wraca ręcznie w panelu.

## 10. Rozliczenie

Zakres **R**, 1–1,5 h. DZIENNIK M3, linia „bezpieczeństwo".

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | trzy kanały z sekcji 7 + logi PHP |
| **+24 h** | czy Janek się loguje bez problemu (login `js` niezmieniony) |
| **+7 dni** | `curl` na REST i `?author=N` — czy aktualizacja WP/Rank Math nie cofnęła filtra |
| **+30 dni** | GSC: czy `/author/js/` wypadło z indeksu (było noindex, więc nie powinno być) |
