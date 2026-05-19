# AGRIA — repozytorium projektowe Auranet

> Baza wiedzy, strategii, audytów i materiałów marketingowych dla projektu **AGRIA Sp. z o.o.** (Tarnów, od 1989 r., 37 lat, surowce wapniowe i mineralne, marka Agrobielik / Bielik).

**Wykonawca:** Auranet. **Klient:** AGRIA Sp. z o.o. (centrala Tarnów ul. Warsztatowa 5; oddziały operacyjne Niedomice + Radgoszcz). **Strona produkcyjna:** [agria.pl](https://agria.pl) (nazwa.pl).

---

## Co tu jest

- `docs/` — cała dokumentacja (markdown): strategia, SEO, katalog, brand, technical, offers, operations, audits.
- `assets/` — pliki binarne: logo, PDF realizowanego katalogu drukowanego, ulotka DL (front/back), JSX dla InDesign, historyczny brief.
- `CLAUDE.md` — plik startowy dla Claude Code (czytany automatycznie).
- `.gitignore` — sekrety / backupy / edytory wykluczone z repo.

Pełna mapa repo — w `CLAUDE.md` sekcja „Mapa repo".

---

## Jak zacząć

### Klonowanie

```bash
git clone git@github.com:auranet-js/agria.git
cd agria
```

### Praca w Claude Code

```bash
claude
```

Claude przeczyta `CLAUDE.md` przy starcie → następnie zaczyna od `docs/MASTER_PROMPT.md` (tożsamość operacyjna) i `docs/PROJECT_STATE.md` (bieżący stan).

### Praca z dokumentacją bez Claude'a

Otwórz interesujące pliki w edytorze (Sublime, VS Code, Obsidian). Najważniejsze punkty wejścia:

| Co chcesz wiedzieć | Zacznij od |
|--------------------|------------|
| Strategia marketingowa | `docs/strategy/STRATEGY_2025_2026.md` |
| Budżet + KPI | `docs/strategy/BUDGET_KPI.md` |
| Plan audytu SEO | `docs/seo/SEO_AUDIT_PLAN.md` |
| Stan produktów w WC | `docs/catalog/PRODUCTS_INVENTORY.md` |
| ⚠️ Niespójności katalog↔WC↔spec | `docs/catalog/CATALOG_VS_WC_GAP.md` |
| Spec katalogu drukowanego | `docs/catalog/PRINT_CATALOG_SPEC.md` |
| Realizowany katalog (PDF) | `assets/print/catalog/Agria-katalog-2026-05-04-web.pdf` |
| Ulotka DL | `assets/print/ulotka-dl/*.jpg` |
| Identyfikacja wizualna | `docs/brand/IDENTITY.md` |
| Oferta dla klienta | `docs/offers/AURANET_2000PLN_MONTHLY.md` |
| Stack techniczny strony | `docs/technical/INFRASTRUCTURE.md` |
| Narzędzia MCP Agria.pl | `docs/technical/MCP_TOOLS.md` |

---

## Konwencje

- **Commit messages:** `[obszar] krótki opis` po polsku. Przykłady: `[docs] mapa niespójności PDF↔WC`, `[feat] schema Product na 19 produktach`, `[fix] literówki «węglanowe» w nazwach WC`.
- **Branche:** `feature/<temat>`, `audit/<temat>`, `offer/<temat>`. Drobne zmiany na `main`.
- **Język:** dokumentacja po polsku, identyfikatory / klucze / kod — oryginał.
- **Sekrety:** nigdy w repo (`.env`, hasła FTP, klucze API, `wp-config.php` z danymi prod).
- **Pliki binarne:** w `assets/`, nie w `docs/`. Pliki źródłowe DTP (`.indd`, `.ai`, `.psd`) gdy dojdą → `assets/print/<materiał>/source/`.

---

## Kontakt operacyjny

**Klient:**
- AGRIA Sp. z o.o.
- ul. Warsztatowa 5, 33-100 Tarnów
- KRS 0000170666 · NIP 8730006657 · REGON 001405704
- ☎ +48 14 621 88 21 (centrala) · +48 604 428 782 · +48 660 768 691
- ✉ biuro@agria.pl
- Oddział Niedomice: ul. Fabryczna 17, Paweł Bigos, +48 664 393 062, pawel.bigos@agria.pl
- Oddział Radgoszcz: ul. Witosa 12, Kazimierz Nowak, +48 781 875 411, kazimierz.nowak@agria.pl

**Wykonawca:**
- Auranet (Jan Schenk, Tarnów / Radgoszcz)
- js@auranet.com.pl
- [auranet.com.pl](https://auranet.com.pl)

---

## Status projektu

**Faza I (budowa)** — zamknięta: strona agria.pl uruchomiona, identyfikacja gotowa, katalog drukowany (17 kart) w produkcji, ulotka DL gotowa.

**Faza II (utrzymanie + SEO + content)** — w trakcie:
1. Audyt techniczny + on-page (etap zerowy, koszt Auranet) → baseline pod ofertę.
2. Oferta 6-miesięczna ~2 000 PLN netto/mies × 6 mies = 12 000 PLN netto pakiet.
3. Po akceptacji: comiesięczna realizacja (technical + on-page + 2 artykuły + analityka + raport).

Pełen stan: `docs/PROJECT_STATE.md`.
