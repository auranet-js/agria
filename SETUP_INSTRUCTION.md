# Instrukcja: wgranie zawartości i `/init` w Claude Code

> Krok po kroku — od klonowania repo do gotowej sesji Claude Code z pełnym kontekstem AGRIA.

---

## Krok 0 — Stan początkowy

Sklonowałeś już repo:

```bash
[host476470@elara projekty]$ git clone git@github.com:auranet-js/agria.git
[host476470@elara projekty]$ cd agria
```

Repo jest stare i nieaktualne. W tej operacji **wyczyścimy je i wgramy świeżą zawartość** z archiwum przygotowanego w tym wątku.

---

## Krok 1 — Wyczyść stare repo (zostaw .git)

Na lokalnym kompie (Windows) lub na zdalnym `host476470@elara`:

```bash
cd agria
# usuń wszystko OPRÓCZ folderu .git
find . -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
ls -la
# powinno zostać tylko .git/
```

⚠️ **Uwaga:** jeżeli w starym repo jest coś, co chcesz zachować (np. README z historią), zrób kopię gdzie indziej przed czyszczeniem.

Alternatywnie — bez czyszczenia, świadomie zachowując historię:

```bash
git checkout -b feature/repo-restructure-2026-05
# tu wgrasz pliki i nadpiszesz starsze
```

---

## Krok 2 — Wgraj zawartość z archiwum

Pobierz archiwum `agria-repo-content.zip` (lub `.tar.gz`) z tego wątku i rozpakuj **do folderu `agria/`**.

### Wariant A — z `.zip` (Windows / cross-platform)

```bash
# w folderze agria/
unzip -o /sciezka/do/agria-repo-content.zip
```

### Wariant B — z `.tar.gz` (Linux / WSL)

```bash
cd agria
tar xzf /sciezka/do/agria-repo-content.tar.gz
```

### Sprawdź strukturę

```bash
tree -L 3
# lub:
find . -type f ! -path './.git/*' | sort
```

Powinieneś zobaczyć:

```
agria/
├── .gitignore
├── CLAUDE.md
├── README.md
├── TREE.md
├── assets/
│   ├── AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx
│   ├── KATALOG_AGRIA_24STR_KOMPLET.txt
│   └── agria-logo.png
└── docs/
    ├── MASTER_PROMPT.md
    ├── PROJECT_STATE.md
    ├── brand/IDENTITY.md
    ├── catalog/{5 plików .md}
    ├── offers/AURANET_2000PLN_MONTHLY.md
    ├── operations/WORKING_AGREEMENT.md
    ├── seo/{2 pliki .md}
    ├── strategy/{2 pliki .md}
    └── technical/{2 pliki .md}
```

---

## Krok 3 — Commit i push

```bash
cd agria
git add -A
git status   # zweryfikuj co idzie do commita
git commit -m "feat: pełna restrukturyzacja repo — baza wiedzy AGRIA + CLAUDE.md pod Claude Code"
git push origin main
# lub jeśli zrobiłeś feature branch:
# git push origin feature/repo-restructure-2026-05
```

---

## Krok 4 — Uruchom Claude Code w folderze

```bash
cd agria
claude
```

W sesji wykonaj `/init`:

```
/init
```

Claude Code automatycznie:
1. Wykryje plik `CLAUDE.md` w roocie.
2. Wczyta go do kontekstu sesji.
3. `CLAUDE.md` poinstruuje Claude'a, żeby od razu przeczytał:
   - `docs/MASTER_PROMPT.md` (tożsamość roli)
   - `docs/PROJECT_STATE.md` (bieżący stan)

---

## Krok 5 — Pierwszy prompt do Claude Code po `/init`

Wklej dokładnie ten prompt jako pierwszą wiadomość:

```
Załaduj kontekst projektu AGRIA.

1. Przeczytaj kolejno:
   - CLAUDE.md
   - docs/MASTER_PROMPT.md (Twoja tożsamość w tym projekcie)
   - docs/PROJECT_STATE.md (gdzie jesteśmy, co dalej)
   - docs/offers/AURANET_2000PLN_MONTHLY.md (bieżący priorytet handlowy)
   - docs/seo/SEO_AUDIT_PLAN.md (najbliższe zadanie operacyjne)

2. Wywołaj MCP `Agria.pl:status` żeby zweryfikować, czy strona produkcyjna żyje i które wersje są aktualne. Porównaj z PROJECT_STATE.md i zgłoś rozbieżności.

3. Wywołaj MCP `Agria.pl:wc_products_list` (limit: 100) i porównaj z `docs/catalog/PRODUCTS_INVENTORY.md`. Zgłoś różnice (nowe / usunięte / przemianowane produkty).

4. Po wczytaniu kontekstu, podaj mi:
   - krótkie streszczenie stanu projektu (max 10 zdań),
   - 3 najpilniejsze rzeczy do zrobienia w najbliższym tygodniu,
   - 3 otwarte pytania, na które potrzebujesz ode mnie odpowiedzi przed rozpoczęciem pracy nad audytem SEO.

Nie pisz wstępnie nic „witam", od razu wykonaj kroki 1-4 i daj zwięzły output.
```

---

## Krok 6 — Co dalej

Po udanym `/init` i pierwszym prompcie Claude powinien być gotowy do:

- prowadzenia audytu SEO (etap zerowy),
- generowania treści (artykuły, opisy produktów, schema),
- pracy z MCP Agria.pl,
- przygotowywania ofert i raportów,
- generowania JSX dla katalogu drukowanego.

---

## Troubleshooting

### Claude Code nie wczytuje CLAUDE.md
- Upewnij się, że `CLAUDE.md` jest w **roocie repo**, nie w `docs/`.
- W Claude Code: `/context` powinien pokazać CLAUDE.md jako wczytany plik.
- Jeżeli nie — sprawdź `~/.claude/settings.json` czy `autoLoadProjectClaude` jest `true` (domyślnie tak jest).

### MCP `Agria.pl` nie działa w Claude Code
- Sprawdź czy MCP serwer `Agria.pl` jest skonfigurowany w `~/.claude.json` lub konfiguracji projektowej.
- Jeżeli MCP klienta Claude (web) różni się od MCP Claude Code — może wymagać osobnej rejestracji.
- W ostateczności: w Claude Code użyj `/mcp` żeby zobaczyć aktywne MCP serwery.

### Stare repo było pełne czegoś ważnego
- `git log --all --oneline` — zobacz historię.
- `git checkout <commit> -- <plik>` — przywróć konkretny plik z konkretnego commita.
- Wszystko zostaje w `.git/`, nic nie zostało utracone (chyba że force-pushowałeś).

### Konflikt branchy przy push
- Jeżeli `git push` daje błąd "rejected — non-fast-forward":
  - `git pull --rebase origin main` (jeśli ufasz historii)
  - lub `git push --force-with-lease` (jeśli świadomie nadpisujesz)

---

## Dalsze wątki w Claude Code

Każdy duży temat = osobna sesja `claude` w terminalu, ale **wszystkie w tym samym folderze repo**. Claude za każdym razem wczyta CLAUDE.md.

Sugerowana kolejność pierwszych sesji:

1. **Sesja: Audyt SEO** — Claude wykonuje audyt zgodnie z `docs/seo/SEO_AUDIT_PLAN.md`, zapisuje wyniki do `docs/seo/SEO_AUDIT_RESULTS.md`.
2. **Sesja: Oferta dla klienta** — doszlifowanie `docs/offers/AURANET_2000PLN_MONTHLY.md` + przygotowanie wersji prezentacyjnej (PDF / slides).
3. **Sesja: Katalog drukowany** — generowanie 17 JSX dla pozostałych kart.
4. **Sesja: Content calendar Q3 2026** — plan 6 artykułów na lipiec-wrzesień.
5. **Sesja: Wdrożenie analityki** — GA4 + GSC + GTM + Looker Studio dashboard.
