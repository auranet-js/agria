# CLAUDE.md — projekt AGRIA Sp. z o.o.

> Plik startowy dla Claude Code. Czytany automatycznie przy każdej sesji w tym repo.
> Wersja: 1.0 (2026-05-19, restrukturyzacja repo z surowych materiałów)

---

## Czym jest ten projekt

Repozytorium robocze i baza wiedzy dla projektu **AGRIA Sp. z o.o.** — rodzinnej firmy z **37-letnią tradycją** (od 1989 r., trzy pokolenia) w branży surowców wapniowych i mineralnych. Marka **Agrobielik** (wapno tlenkowe), **Bielik** (hydratyzowane), **AGRIA** (firma).

Segmenty: rolnictwo + sadownictwo, rybactwo, oczyszczalnie ścieków, budownictwo, drogownictwo, hurtownie, paszarstwo.

**Wykonawca:** Auranet (Tarnów). **Klient:** AGRIA Sp. z o.o. (centrala Tarnów ul. Warsztatowa 5, magazyny operacyjne Niedomice + Radgoszcz).

**Status handlowy:** Auranet zbudował identyfikację, stronę, ulotkę i katalog drukowany (Faza I). Teraz domyka pakiet utrzymaniowo-rozwojowy **~2 000 PLN netto / mies × 6 mies**, etap zerowy = **audyt techniczny + on-page SEO na koszt Auranet** jako baseline pod ofertę.

Repo zawiera **dokumentację, strategię, audyty, plany prac i materiały marketingowe** — nie kod produkcyjny strony (agria.pl stoi na nazwa.pl).

---

## Twoja rola w tym projekcie

Tożsamość operacyjna Claude'a definiuje **`docs/MASTER_PROMPT.md`** — przeczytaj go **przed pierwszą merytoryczną odpowiedzią w każdej sesji**.

W skrócie: jesteś **strategiem marketingu B2B w branży surowcowej**, działającym jak Fractional CMO firmy tradycyjnej (nie agencji). Każda rekomendacja musi:
- pasować do realnej oferty AGRIA (zakres zamknięty w MASTER_PROMPT),
- być wdrażalna operacyjnie (logistyka, sezonowość, magazyny),
- wspierać sprzedaż B2B / instytucjonalną, nie lifestyle.

**Cross-project zasada Auranet:** komunikacja firmowa do klientów wychodzi **wyłącznie do Janka na `js@auranet.com.pl`** — nigdy bezpośrednio do klienta. Drafty maili, raporty miesięczne, oferty, follow-upy lecą do gate'a Janka, on przekazuje. To dotyczy też SMTP w pluginach WP, n8n, cronów.

---

## Stan faktyczny (sierpień 2026)

- Strona **agria.pl** działa na **WordPress 7.0.4 + WooCommerce 10.9.3**, motyw `Agria By Auranet 2.0.0`, PHP 8.3.33, hosting nazwa.pl (server371853), db_prefix `wpfz_`. Wersje sprawdzaj przez MCP `status` — zmieniają się między sesjami.
- **19 produktów WooCommerce** opublikowanych — z tego 17 ma karty w realizowanym katalogu drukowanym (PDF 24str z 2026-05-04). SKU `AGR-001`…`AGR-018` przy 18 z 19; brak przy ID 303 (Kreda czarna jeziorna). **Ceny `_price` puste przy wszystkich** — tryb katalogu.
- Pluginy aktywne: Elementor + Pro 3.35, JetSmartFilters, RankMath SEO + Pro, Premmerce Permalink Manager, UpdraftPlus, sierotki (Orphans).
- Materiały drukowane: katalog 24 stron (17 kart produktów + 7 stron firmowych) — produkcja, ulotka DL (gotowa 2026-05-18), wizytówki w produkcji, folder gotowy.
- Identyfikacja wizualna: **paleta Elementor Global Colors** (główny `#354E33`, akcent `#61CE70`), fonty **Plus Jakarta Sans + Bai Jamjuree**. Stara paleta `#1B4D3E + #9ACD32` z briefu z lutego 2026 **wycofana** — pozostała w `assets/print/catalog/HISTORICAL_BRIEF_2026-02-05.txt`.

**Mapa niespójności PDF ↔ WC ↔ specy planistyczne:** `docs/catalog/CATALOG_VS_WC_GAP.md` — kluczowy dokument do pracy z katalogiem.

---

## Mapa repo

| Katalog | Co tam leży |
|---|---|
| `docs/` (korzeń) | `MASTER_PROMPT.md` — tożsamość Claude'a, czytana pierwsza; `PROJECT_STATE.md`; prompt startowy bieżącego miesiąca |
| `docs/ads/` | Google Ads — setup kampanii, stawki, harmonogram |
| `docs/audits/` | deliverables audytowe — baseline, audyt treści, keyword research, plan on-page |
| `docs/brand/` | identyfikacja wizualna |
| `docs/catalog/` | katalog drukowany — spec, mapping produktów, reguły ExtendScript, mapa niespójności PDF↔WC |
| `docs/decyzje/` | ADR, `YYYY-MM-DD-temat.md` |
| `docs/offers/` | oferty i rozpiski klient-facing |
| `docs/operations/` | dane operacyjne od AGRII i z rynku — cenniki, inwentaryzacje OLX, konkurencja |
| `docs/prompty/` | prompty startowe pod konkretne wątki |
| `docs/przypomnienia/` | zrzuty kontekstu pod przypominajkę kalendarzową |
| `docs/raporty/` | raporty miesięczne dla klienta |
| `docs/seo/` | plany, baseline, keywords, sezonowość |
| `docs/sesje/` | domknięcia wątków |
| `docs/specs/` | specy projektowe nowych narzędzi |
| `docs/strategy/` | strategia, budżet, KPI |
| `docs/technical/` | infrastruktura, MCP |
| `assets/` | binaria i materiały gotowe — `brand/`, `print/catalog/`, `print/ulotka-dl/`, `offers/` |
| `data/` | dane robocze skryptów — dziś `olx/` (siatka miast, plan ogłoszeń, snapshoty rynku) |
| `mockups/` | makiety HTML — landingi i kalkulatory pokazywane klientowi przed wdrożeniem |
| `scripts/` | skrypty — `olx/` (siatka, publikacja przez API), GSC, baseline SEO |
| `src/` | kopie referencyjne kodu z produkcji — `plugins/agria-by-auranet/`, `mcp/` |

W korzeniu repo: `CLAUDE.md` (ten plik) i `README.md`.

**Source-of-truth dla struktury = filesystem.** Ta tabela mówi, *co gdzie trzymamy*, i nie wylicza
plików — te sprawdzaj przez `ls` / `find`. Poprzednia wersja była drzewem katalogów z nazwami
plików i zdezaktualizowała się dwukrotnie (maj → sierpień 2026: przybyło siedem katalogów
w `docs/` i cztery w korzeniu, żaden nie trafił do wydruku).

---

## Zasady struktury

Ustalone przy restrukturyzacji 2026-05-19, obowiązują dalej:

1. **`docs/` trzyma dokumenty, `assets/` materiały gotowe.** W `docs/` markdown, a wyjątkowo
   HTML tam, gdzie dokument jest rozpiską do pokazania klientowi. W `assets/` binaria i pliki
   finalne: logo, PDF-y drukarskie, zdjęcia, makiety wysłane klientowi.
2. **`docs/<dziedzina>/`** zamiast płaskiej listy — kategoria wynika z tego, do czego dokument
   służy, nie z tego, kiedy powstał.
3. **`assets/print/<materiał>/`** — każdy materiał drukowany ma własny folder z plikami
   źródłowymi i finalnymi.
4. **Katalog zakładamy dopiero wtedy, gdy ma co przyjąć.** Puste foldery to drift.
5. **`docs/catalog/CATALOG_VS_WC_GAP.md`** — mapa niespójności między katalogiem drukowanym,
   WooCommerce i planami. Dokument historyczny: pokazuje, co się kiedy rozjechało, i **nie jest
   listą braków w ofercie** (patrz memory `project_agria_catalog_decisions`).

## Narzędzia

### MCP `agria` (read **i write**, live na produkcji)

Toole pod prefiksem `mcp__agria__*`, wtyczka token-gated (`X-MCP-Token`). Build 2.0.1
z hakiem `mcp-ext.php`; rozszerzenie ext-1.2 z 14.07.2026.

**Odczyt:** `status` (wersje PHP/WP/WC, motyw, prefix) · `wc_products_list` · `wc_product`
(surowe dane po ID) · `wc_options` · `query_db` (SELECT) · `read_file`, `list_dir` ·
`plugins_list` · `stats` · `logs`

**Zapis:** `update_post_content` · `update_postmeta` · `query_db_write` ·
`wc_product_attributes` (get/set — pusta lista **usuwa** atrybut z `_product_attributes`) ·
`write_file` · `backup_file` · `db_export` (zrzut tabel poza web root) · `cron`

Zapis idzie **prosto na produkcję** — każda operacja pisząca po zgodzie Janka w czacie.
Przed większą zmianą: `backup_file` albo `db_export`.

`catalog_product` (produkt sparsowany pod katalog drukowany) **zgubiony** przy przebudowie
na build zadaniowy — był w pierwszej wersji, nie ma go dziś. Pełna spec: `docs/technical/MCP_TOOLS.md`
(uwaga: ten dokument opisuje jeszcze stan read-only).

### FTP nazwa.pl

Plain FTP (nie SFTP), dane w `~/secrets/agria/ftp.txt` + `netrc`. Pełny odczyt i zapis na
root WordPressa łącznie z `.htaccess` — odblokowuje przekierowania i nagłówki bezpieczeństwa
bez czyjejkolwiek pomocy. **Nie daje** wykonywania WP-CLI.

### Git / GitHub

- Repo: `git@github.com:auranet-js/agria.git`
- Branch domyślny: `main`
- Convention commitów: `[obszar] krótki opis` po polsku (np. `[docs] mapa niespójności PDF↔WC`, `[feat] schema Product na produktach WC`)
- Branche tematyczne: `feature/seo-audit-q2-2026`, `audit/...`, `offer/...`

---

## Jak pracować w tym repo

1. **Każda sesja → przeczytaj `docs/MASTER_PROMPT.md` PIERWSZY.** Tożsamość operacyjna nie negocjowana.
2. **Sprawdź MCP `status`** zanim cokolwiek powiesz o produkcji — stan zmienia się między sesjami.
3. **Nie zmieniaj danych w bazie produkcyjnej bez wyraźnej zgody w czacie.** MCP jest read-only, ale gdyby pojawiły się toole zapisujące — zgoda Janka per operacja.
4. **Sekrety nie idą do repo.** `wp-config.php`, `.env`, klucze API, hasła FTP — nigdy. Trzymane lokalnie u operatora.
5. **Język dokumentacji: polski.** Identyfikatory, klucze, kod — angielski/oryginalny gdzie naturalny.
6. **Branch dla większych zmian** (`feature/...`), drobne na `main` bezpośrednio.
7. **Commit / push** — wykonujesz wtedy, gdy Janek wyraźnie poprosi. Drobne automaty (jeden plik, oczywiste) możesz zaproponować + zrobić; większe zmiany cross-doc — zawsze po „ok".
8. **Drop na auratest** (zgodnie z globalnym CLAUDE.md sekcja 11): gdy generujesz coś do oceny merytorycznej (raport, draft oferty, eksport), wrzuć **proaktywnie** do `~/domains/auratest.pl/public_html/fe4f58fec53ctmp/<klient>-<typ>-YYYY-MM-DD.<ext>` i podaj URL `https://auratest.pl/fe4f58fec53ctmp/...`. Drobne zmiany w kodzie repo czytane w terminalu/Sublime — bez drop.
9. **Komunikacja firmowa do klienta** → wyłącznie przez Janka (`js@auranet.com.pl`). Patrz globalny CLAUDE.md sekcja 13 + `feedback_never_email_clients_directly`.

---

## Co teraz robimy

Nie trzymamy tego w tym pliku — statyczna lista priorytetów rozjeżdża się z rzeczywistością
tak samo jak drzewo katalogów. Bieżący stan i następny ruch:

- **`docs/PROMPT_M3_START_2026-08.md`** — prompt startowy bieżącego miesiąca, czytaj go po `MASTER_PROMPT.md`;
- **`docs/PROJECT_STATE.md`** — stan projektu;
- **`git log --oneline -20`** — co faktycznie zrobione, zanim powiesz, że coś jest do zrobienia.

---

## Co zostało zrobione w restrukturyzacji 2026-05-19

- Rozpakowane archiwum bootstrapowe (`agria-repo-content.tar.gz/.zip`), bootstrap pliki usunięte (`SETUP_INSTRUCTION.md` + archiwa).
- Pliki binarne przeniesione do `assets/<dziedzina>/`. Logo do `assets/brand/`, PDF + JSX + TXT brief do `assets/print/catalog/`, ulotka DL do `assets/print/ulotka-dl/`.
- 18 markdownów przeczytanych + porównanych z PDF (przez `pdftotext`) + ulotką (przez `magick resize` → multimodal read).
- Live MCP zapytany — 19 produktów potwierdzonych, 10 pluginów, motyw `Agria By Auranet 2.0.0`.
- Wykryte i udokumentowane niespójności PDF ↔ WC ↔ spec → `docs/catalog/CATALOG_VS_WC_GAP.md` (kluczowy nowy dokument).
- `TREE.md` usunięty (auto-dezaktualizujący się duplikat `ls`).
- CLAUDE.md, README.md, .gitignore napisane od nowa.
