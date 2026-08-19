# T-028 — duplikaty pod starą bazą URL `/produkt/` + 15 osieroconych wpisów `post_type=produkt`

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 🔴 teraz |
| **Znalezione** | 19.08.2026 przez Claude, wcześniej nieujęte w żadnym dokumencie |
| **Szacunek** | 2 h (diagnoza 30 min + 301 + weryfikacja) |

---

## 1. Czego to dotyka

**Dwie różne rzeczy pod jednym numerem — rozdziel je, zanim cokolwiek zrobisz.**

**(A) Stara baza URL `/produkt/<slug>`** serwuje **HTTP 200** dla produktów WooCommerce,
z canonicalem wskazującym właściwy adres. To nie są osobne strony — to ten sam produkt pod
drugim adresem. Dotyka: Premmerce Permalink Manager, `.htaccess`, sitemapy, GSC.

**(B) 15 wpisów `post_type=produkt`, ID 60–74**, wszystkie `publish`, wszystkie z `post_content`
o **zerowej długości** i **bez żadnej meta** (`rank_math_robots`, `_elementor_data`, `_wp_page_template`
— wszystkie `NULL`). CPT `produkt` **nie jest dziś zarejestrowany w WordPressie** — nie ma go na
liście `wp post-type list`. To sieroty po migracji, niedostępne przez front, ale zajmujące ID
i widoczne w eksportach.

## 2. Strefy kruche

1. **Rejestr opisuje to inaczej, niż jest.** Wiersz mówi „15 opublikowanych `post_type=produkt`
   … `/produkt/agrobielik-70/` i `/produkt/dolomit/` → HTTP 200". Zmierzone 19.08: te 200-ki
   **nie pochodzą** od wpisów 60–74, tylko od produktów WooCommerce pod starą bazą URL.
   Dowód: `/produkt/wapno-palone-wysokoreaktywne/` (slug wpisu ID 74) → **404**, bo produkt WC
   ma inny slug. Zacznij od potwierdzenia tej diagnozy, nie od naprawy.
2. **Canonical już wskazuje właściwy URL** — Google w większości przypadków to uszanuje. To znaczy,
   że sprawa jest niższego ryzyka, niż wyglądała, i **nie usprawiedliwia pośpiesznego 301**,
   który może zderzyć się z regułami Premmerce.
3. **Premmerce ma `product_base: /product/%product_cat%`** (sprawdzone 19.08), a mimo to działa
   `/produkt/`. Zanim dopiszesz regułę do `.htaccess`, ustal, **co** dziś obsługuje `/produkt/` —
   inaczej reguła może zapętlić przekierowanie albo wyłączyć działający adres.
4. **`/produkt/kreda-malarska/` prowadzi do `/kreda-malarska/kreda-malarska/`** — czyli do URL-a
   ze zdublowanym członem, który sam w sobie jest długiem (zauważony w `CEN_LISTA_URL`, świadomie
   nietknięty). Nie próbuj naprawiać obu naraz.
5. **Kasowanie wpisów 60–74 przez `query_db_write` jest niemożliwe** (DELETE zablokowany).
   Wyłącznie WP-CLI: `wp post delete <ID>` — i **najpierw `--dry-run` przez `wp post list`**,
   żeby potwierdzić, że kasujesz sieroty, a nie produkty.
6. **ID 60–74 mogą być zalinkowane w menu, w Elementorze albo w starych wpisach.** Sprawdź
   `grep` po `_elementor_data` i `post_content` za `?p=6X` i za slugami, zanim skasujesz.
7. **Trash zamiast delete.** `wp post delete` bez `--force` idzie do kosza — odwracalne.
   Użyj tego, nie `--force`.

## 3. Stan zmierzony 19.08.2026

```
query_db: 15 wpisów post_type='produkt', ID 60–74, wszystkie publish, len(post_content)=0,
          rank_math_robots / _elementor_data / _wp_page_template = NULL we wszystkich

wp post-type list: brak typu 'produkt' na liście zarejestrowanych

/produkt/dolomit/                    → 200, canonical https://agria.pl/wapno-nawozowe-rolnictwo/dolomit/
/produkt/agrobielik-70/              → 200, canonical https://agria.pl/wapno-nawozowe-rolnictwo/agrobielik-70/
/produkt/kreda-malarska/             → 200, canonical https://agria.pl/kreda-malarska/kreda-malarska/
/produkt/wapno-palone-wysokoreaktywne/ → 404
/produkt/nieistniejacy-test-abc/     → 404

sitemapy: /produkt/ nie występuje w żadnej z pięciu
```

## 4. Warunki wejścia

- [ ] Ustalone z GSC, **ile realnie wyświetleń** zbierają adresy `/produkt/*` (Search Analytics
      z filtrem po ścieżce). Jeśli zero — problem jest teoretyczny i priorytet spada.
- [ ] Ustalone, co obsługuje `/produkt/` (Premmerce, `.htaccess`, czy reguła WP).

## 5. Co robisz

1. **Diagnoza (30 min, zero zapisu):**
   ```bash
   # ile adresów /produkt/* Google w ogóle zna
   python3 scripts/gsc_pull.py   # przefiltruj po '/produkt/'
   # które slugi WC odpowiadają pod starą bazą
   for s in $(mcp query_db "SELECT post_name FROM {prefix}posts WHERE post_type='product' AND post_status='publish'"); do
     printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' https://agria.pl/produkt/$s/)" "$s"
   done
   ```
2. Pokaż Jankowi wynik: ile adresów odpowiada 200, ile z nich ma wyświetlenia w GSC.
3. **Jeśli wyświetlenia są** → reguła 301 w bloku `# BEGIN AGRIA 301` w `.htaccess`
   (przed blokiem WordPress), mapująca `/produkt/<slug>` na canonical z odpowiedzi HTTP.
   **Diff pokazujesz Jankowi przed uploadem**, kopia z datą zostaje.
4. **Jeśli wyświetleń nie ma** → wystarczy canonical, task zamykasz adnotacją „bez działania,
   canonical wystarcza" i dowodem z GSC. To jest pełnoprawne domknięcie.
5. **Sieroty 60–74** — osobna operacja: sprawdź linkowanie, potem `wp post delete 60 61 … 74`
   (do kosza, nie `--force`), readback `wp post list --post_type=produkt`.

## 6. Jak sprawdzasz w trakcie

Po każdej regule w `.htaccess`: `curl -s -o /dev/null -w '%{http_code} %{redirect_url}\n'`
na starym URL-u **i** na docelowym (docelowy musi zostać 200, nie wpaść w pętlę).

## 7. Jak testujesz po wdrożeniu

```bash
# 1. stare adresy przekierowują jednym skokiem
for s in dolomit agrobielik-70 kreda-malarska; do
  curl -s -o /dev/null -w "%{http_code} → %{redirect_url}\n" "https://agria.pl/produkt/$s/"
done          # oczekiwane: 301 → canonical
# 2. docelowe nadal 200
curl -s -o /dev/null -w '%{http_code}\n' https://agria.pl/wapno-nawozowe-rolnictwo/dolomit/
# 3. brak pętli
curl -sIL https://agria.pl/produkt/dolomit/ | grep -c '^HTTP'    # ≤ 2
# 4. sieroty zniknęły
ssh agria-prod "wp --path=\$HOME/agria.pl post list --post_type=produkt --format=count"   # 0
```

## 8. Dowód do rejestru

Tabela: stary URL → kod → docelowy, dla wszystkich adresów zwracających dziś 200.
Liczba wpisów `post_type=produkt` po operacji. Jeśli decyzja to „bez działania" — zrzut z GSC
pokazujący zero wyświetleń dla `/produkt/*` jako uzasadnienie.

## 9. Rollback

`.htaccess`: kopia z datą sprzed zmiany, upload FTP-em (cykl zapis/kasowanie zweryfikowany 19.08).
Sieroty: `wp post untrash <ID>`.

## 10. Rozliczenie

Zakres **R**, 1–2 h. DZIENNIK M3.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **natychmiast** | trzy adresy przez `curl`, brak pętli |
| **+7 dni** | GSC: czy `/produkt/*` przestały zbierać wyświetlenia, czy docelowe je przejęły |
| **+30 dni** | czy w GSC nie przybyło nowych duplikatów spod innej starej bazy |
