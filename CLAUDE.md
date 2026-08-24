# CLAUDE.md — AGRIA (agria.pl)

> **Repo:** `agria` (GitHub: `auranet-js/agria`) | **Wersja:** 2.0 (2026-08-19)
> **Uzupełnia:** `~/.claude/CLAUDE.md` (globalny) + `~/projekty/CLAUDE.md` (cross-project)
>
> Ten plik trzyma **fakty operacyjne**: gdzie stoi produkcja, czym się do niej dostać, czego nie ruszać.
> **Nie trzyma stanu prac ani listy zadań** — od tego jest `docs/REJESTR_ZOBOWIAZAN.md`.

---

## 1. Co to za projekt

**AGRIA Sp. z o.o.** — firma rodzinna od 1989 r., surowce wapniowe i mineralne, sprzedaż hurtowa B2B.
Centrala Tarnów (Warsztatowa 5), magazyny Niedomice i Radgoszcz. **Auranet jest jej działem marketingu**
— stronę zbudowaliśmy my, prowadzimy ją na retainerze 2 000 netto/mies (+ Ads i OLX osobno).

Fakty o produktach, cenach, ludziach i ustaleniach handlowych: **`docs/FAKTY_KLIENTA.md`**.
Nie zgaduj i nie dopytuj Janka, zanim tam nie zajrzysz.

---

## 2. Środowisko

| Parametr | Wartość |
|---|---|
| Domena | `agria.pl` |
| Hosting | **nazwa.pl** — `server371853.nazwa.pl` (NIE Elara/Hostido) |
| Root WP | **`~/agria.pl`** = `/home/server371853/ftp/agria.pl` |
| WordPress / WooCommerce | 7.0.4 / 10.9.3 — **sprawdzaj przez MCP `status`**, zmienia się między sesjami |
| PHP | 8.3.33 |
| DB prefix | **`wpfz_`** (nigdy `wp_`) |
| Motyw | `Agria By Auranet` 2.0.0 |
| Builder | Elementor + Elementor Pro 3.35 |
| SEO | Rank Math + PRO |
| Inne wtyczki | JetSmartFilters, Premmerce Permalink Manager, UpdraftPlus, Orphans (sierotki) |
| CDN | nazwa.pl — **każda zmiana wymaga cache-bustu**, patrz §4 |

**Katalog domowy to już `ftp`** — `~` wskazuje na `/home/server371853/ftp`, więc ścieżki `~/ftp/...`
trafiają w próżnię.

### Cztery kanały dostępu

| Kanał | Do czego | Czego NIE zrobi |
|---|---|---|
| **SSH** `ssh agria-prod` | powłoka, **WP-CLI 2.4.0** (`/usr/local/sbin/wp`, wymaga `--path=~/agria.pl`), masowe operacje, migracje | — |
| **MCP `agria`** `mcp__agria__*` | szybki odczyt i zapis, `query_db`, `logs`, `db_export`, `wc_product_attributes` | WP-CLI |
| **FTP** (plain, nie SFTP) | root WP łącznie z **`.htaccess`** — przekierowania i nagłówki | WP-CLI, DB-write |
| **Chrome MCP** | front i panel oczami klienta — **weryfikacja renderu**, patrz §4 | — |

Sekrety: `~/secrets/agria/` (`ssh.env`, `ftp.txt`, `netrc`, `olx.txt`). Klucz SSH `claude-agria-elara`
(ed25519), odcięcie = usunięcie jednej linii w panelu nazwa.pl.

**Sesje SSH dawaj zbiorczo**, nie po jednym poleceniu — `ssh agria-prod 'bash -s' <<'EOF'` z `timeout N`
na każdej komendzie. Pojedyncze wywołania potrafią wisieć; skrypt zbiorczy z limitami przechodzi.

---

## 3. MCP `agria` — pełen zakres

Wtyczka token-gated (`X-MCP-Token`), build 2.0.1 + hak `mcp-ext.php`, rozszerzenie ext-1.2.

**Odczyt:** `status` · `wc_products_list` · `wc_product` · `wc_options` · `query_db` (SELECT) ·
`read_file` · `list_dir` · `plugins_list` · `stats` · `logs`
**Zapis:** `update_post_content` · `update_postmeta` · `query_db_write` · `wc_product_attributes`
(get/set — **pusta lista usuwa** atrybut z `_product_attributes`) · `write_file` · `backup_file` ·
`db_export` (zrzut tabel poza web root) · `cron`

`catalog_product` **zgubiony** przy przebudowie na build zadaniowy — nie ma go dziś.
Spec: `docs/technical/MCP_TOOLS.md` (opisuje jeszcze stan read-only).

---

## 4. Strefy kruche — nie ruszaj bez diagnozy

1. **Parametry produktu żyją w czterech warstwach naraz**: atrybuty `pa_*` (często niewidoczne na froncie),
   tabela w `post_content`, tabela w `_elementor_data`, meta SEO. Zmiana w jednej nie przechodzi
   na pozostałe. **Weryfikuj RENDER przez Chrome MCP, nie bazę.**
2. **Elementor cache** — `_elementor_element_cache` trzyma stary HTML. Czyść na `a:0:{}`.
   Strony **307 / 310 / 320 renderują z `_elementor_data`, NIE z `post_content`** — edycja treści
   posta nic tam nie zmienia.
3. **Sitemapa RankMath cache'uje się w PLIKACH** `uploads/rank-math/*.xml` — nie w bazie.
   Usuwanie przez FTP.
4. **CDN nazwa.pl** — po każdej zmianie cache-bust, inaczej weryfikujesz stan sprzed godziny.
5. **`_price` puste we wszystkich 19 produktach to DECYZJA, nie brak.** Tryb katalogu. Ceny mają
   **dwie niezależne warstwy** (treść SEO vs ofertownik) — `docs/FAKTY_KLIENTA.md` §7 i ADR
   `docs/decyzje/2026-08-19-dwie-warstwy-cen.md`. **Nie ustawiaj `_price` ani wariantów pod publikację.**
6. **Warstwa zgód mieszka w trzech miejscach naraz**: panel Complianza, szablon, którego wtyczka
   realnie używa (`templates/statistics/` — przy integracji przez GTM to `google-tag-manager-consent-mode.js`),
   i **kontener GTM**. `url_passthrough` oraz `ads_data_redaction` siedzą **w kontenerze**, więc
   **nie widać ich w źródle strony** — zero trafień w HTML nie znaczy „nie ma". Sprawdzaj kontener
   przez API, zanim uznasz coś za brakujące.
7. **Landingi buduj z gotowego wzorca** — obejrzyj działającą stronę przez Chrome MCP i powiel strukturę.
   Surowy HTML w `post_content` renderuje się bez layoutu (`/wapno-granulowane/` stał pusty tydzień
   z reklamami wycelowanymi na niego).

---

## 5. Czego NIE wolno bez pytania

- **Pisać do produkcji** — MCP idzie prosto na żywą stronę. Zgoda Janka **per operacja**,
  `backup_file` albo `db_export` przed większą zmianą.
- Ustawiać cen w WooCommerce (`_price`, warianty) — patrz §4 pkt 5.
- Zgłaszać URL-e do **Google Indexing API** inaczej niż przez `~/bin/index-submit` (wspólna pula 200/dobę
  na wszystkie projekty, globalny CLAUDE.md §10a).
- Modyfikować `.htaccess` — pokaż diff, czekaj na „ok".
- **Dokładać kod do warstwy zgód.** Complianz, Consent Mode, baner i sygnały (`url_passthrough`,
  `ads_data_redaction`, `wait_for_update`) zmieniamy **wyłącznie ustawieniami** — panelem wtyczki
  albo kontenerem GTM. Gdy ustawienia nie potrafią, **wracasz z pytaniem**, nie piszesz modułu.
  Zasada z T-062; incydent 24.08 opisany w memory `feedback_agria_complianz_ustawieniami_zero_kodu`.
- Wysyłać cokolwiek do klienta. **Wszystko przez Janka na `js@auranet.com.pl`**, kanał `~/bin/send-to-jan`.
- Publikować cen ofertownika w jakiejkolwiek formie (front, REST, feed, schema).

---

## 6. Kolejka zadań

**Jedna i jedyna lista: [`docs/REJESTR_ZOBOWIAZAN.md`](docs/REJESTR_ZOBOWIAZAN.md).**
Nie prowadź listy tutaj i nie wyprowadzaj statusu z `git log` — commit opisuje **wytworzony artefakt**,
nie stan obowiązku. Rozpiska do wykonania commituje się identycznie jak wykonanie.

W rejestrze: **KOLEJKA** (teraz / czeka na AGRIĘ / zaplanowane) + **DZIENNIK** miesięczny pod raport.
Numeracja `T-NNN`. Sekcja **„Unieważnione"** mówi, czego NIE proponować.
**Commit zamykający pozycję aktualizuje jej wiersz w tym samym commicie.**

---

## 7. Brand i komunikacja — skrót

- **Marki:** `Agrobielik` (wapno tlenkowe), `Bielik` (hydratyzowane), `AGRIA` (firma).
  Agrobielik i Bielik to **produkty Nordkalku**, AGRIA jest dystrybutorem — nie producentem.
- **Głos:** fakty, parametry, zastosowania. B2B surowcowe, zero lifestyle'u i marketingowej nowomowy.
- **Zero żargonu** — odbiorcą jest rolnik, nie spedytor. Zamiast „loco magazyn" → „cena za towar,
  bez transportu". Dotyczy też MOQ, franco, EXW, HDS.
- **Nie krytykujemy stanu strony** w komunikacji do klienta — zbudował ją Auranet.
  Framing rozwojowy: „uruchamiamy / wzmacniamy / optymalizujemy".
- **Auranet decyduje** o kampaniach, treściach i priorytetach; klient o budżecie i faktach handlowych.
  Maile w trybie oznajmującym, opt-out zamiast opt-in.
- **Parametry produktów wyłącznie z kart producentów** (Nordkalk, Lhoist) i rozporządzeń — nigdy
  z rozumowania. 17 kart leży publicznie na `/do-pobrania/`.
- **Landingi tylko jako cele Ads, poza indeksem** — kanibalizacja zmierzona (ADR 2026-08-11).
  Organik idzie treścią.

Reszta reguł ładuje się z memory (`feedback_agria_*`) — nie duplikuj ich tutaj.

---

## 8. Kontakty

| Kto | Rola | Jak |
|---|---|---|
| **Paweł Bigos** | główny kontakt operacyjny, akceptuje zmiany | **telefon Janka**, nie mail — 664 393 062 |
| **Kazimierz Nowak** | merytoryka: kalkulator, treści OLX | mail + telefon — 781 875 411 |
| **Kasjan** | decyzja o budżecie | **nie kontaktujemy się bezpośrednio** |
| Auranet (Janek) | prowadzenie projektu | js@auranet.com.pl |

---

## 9. Konwencja commitów i struktura

Format `[obszar] krótki opis` po polsku. Obszary: `docs`, `feat`, `fix`, `content`, `seo`, `ads`,
`olx`, `chore`. Branch domyślny `main`, większe zmiany na `feature/...`.

| Katalog | Co tam |
|---|---|
| `docs/` | dokumentacja — `REJESTR_ZOBOWIAZAN.md`, `FAKTY_KLIENTA.md` w korzeniu, reszta w `docs/<dziedzina>/` |
| `assets/` | binaria i materiały gotowe — brand, druk, oferty |
| `src/` | kopie referencyjne kodu z produkcji (`plugins/`, `mcp/`) — **snapshoty, nie źródło prawdy** |
| `scripts/`, `data/`, `mockups/` | skrypty, dane robocze, makiety HTML |

**Source of truth dla kodu = serwer**, nie `src/`. Przed pracą sprawdź aktualność przez MCP `read_file`.
**Source of truth dla struktury = filesystem** — powyższa tabela mówi, co gdzie trzymamy, nie wylicza plików.
