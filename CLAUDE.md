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

## Stan faktyczny (maj 2026)

- Strona **agria.pl** działa na **WordPress 6.9.4 + WooCommerce 10.6.1**, motyw `Agria By Auranet 2.0.0`, PHP 8.3.30, hosting nazwa.pl (server371853), db_prefix `wpfz_`.
- **19 produktów WooCommerce** opublikowanych — z tego 17 ma karty w realizowanym katalogu drukowanym (PDF 24str z 2026-05-04). **Wszystkie produkty mają `sku = null`** ⚠️.
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
| `assets/` | binaria i materiały gotowe — `brand/`, `print/catalog/`, `print/ulotka-dl/`, `offers/`, `mockups/` |
| `data/` | dane robocze skryptów — dziś `olx/` (siatka miast, plan ogłoszeń, snapshoty rynku) |
| `mockups/` | makiety HTML do testów u klienta |
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

### MCP `Agria.pl` (read-only, live na produkcji)

W Claude Code toole pod prefixem `mcp__claude_ai_Agria_pl__*`:

- `status` — wersje PHP/WP/WC, motyw, prefix DB
- `wc_products_list` — lista produktów (id, name, sku, status, categories, modified)
- `wc_product` — surowe dane produktu po ID (meta, atrybuty, pricing, warianty)
- `catalog_product` — produkt sparsowany pod format katalogu drukowanego (15 parametrów, formy dostawy)
- `wc_options` — opcje WooCommerce (waluta, magazyn, podatki)
- `query_db` — SELECT (read-only) na bazie WP
- `read_file`, `list_dir` — pliki w `wp-content/`
- `plugins_list` — aktywne wtyczki + wersje
- `stats` — statystyki sklepu

**Brak** zapisu — żadnego UPDATE/INSERT/DELETE z poziomu MCP. Operacje pisania = WP-CLI po SSH lub REST API.

W Claude.ai web te same toole nazywają się `Agria.pl:status` itd. — funkcjonalnie identyczne. Pełna spec: `docs/technical/MCP_TOOLS.md`.

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

## Bieżące priorytety (maj–czerwiec 2026)

1. **Audyt techniczny + on-page agria.pl** — `docs/seo/SEO_AUDIT_PLAN.md`, deliverable do `docs/audits/SEO_AUDIT_RESULTS.md` (utworzyć po wykonaniu).
2. **Domknięcie oferty 6-mies** — `docs/offers/AURANET_2000PLN_MONTHLY.md`, prezentacja zarządowi AGRIA.
3. **Generacja JSX dla pozostałych 16 kart katalogu** (PDF już ma 17 — wzorzec Agrobielik 70 w `assets/print/catalog/jsx/agrobielik-70.jsx`).
4. **Wdrożenie analityki** — GA4 + GSC + GTM (placeholder pod konto Auranet, do przekazania klientowi).
5. **Rozstrzygnięcie decyzji z `CATALOG_VS_WC_GAP.md`** — cement/kruszywo/drogowe (czy do WC?), Kreda czarna jeziorna (publish vs decyzja „wycięta"), warianty Agrobielika 90, SKU dla 19 produktów.

---

## Co zostało zrobione w restrukturyzacji 2026-05-19

- Rozpakowane archiwum bootstrapowe (`agria-repo-content.tar.gz/.zip`), bootstrap pliki usunięte (`SETUP_INSTRUCTION.md` + archiwa).
- Pliki binarne przeniesione do `assets/<dziedzina>/`. Logo do `assets/brand/`, PDF + JSX + TXT brief do `assets/print/catalog/`, ulotka DL do `assets/print/ulotka-dl/`.
- 18 markdownów przeczytanych + porównanych z PDF (przez `pdftotext`) + ulotką (przez `magick resize` → multimodal read).
- Live MCP zapytany — 19 produktów potwierdzonych, 10 pluginów, motyw `Agria By Auranet 2.0.0`.
- Wykryte i udokumentowane niespójności PDF ↔ WC ↔ spec → `docs/catalog/CATALOG_VS_WC_GAP.md` (kluczowy nowy dokument).
- `TREE.md` usunięty (auto-dezaktualizujący się duplikat `ls`).
- CLAUDE.md, README.md, .gitignore napisane od nowa.
