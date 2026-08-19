# T-027 — zgłoszenie `/do-pobrania/` do reindeksacji

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 🔴 teraz, ale **po T-008 i T-009** — zgłaszasz stronę już poprawioną |
| **Szacunek** | 15 min + czekanie |

---

## 1. Czego to dotyka

Google Search Console (URL Inspection + Indexing API) dla `https://agria.pl/do-pobrania/`.
**Wspólna pula Indexing API: 200 zgłoszeń/dobę na wszystkie projekty Auranet**, budżet ad-hoc 100.

## 2. Strefy kruche

1. **Nigdy surowym `curl`-em do `indexing.googleapis.com`.** Hook `~/bin/indexing-guard-hook.py`
   to zablokuje, i słusznie — jeden batch bez kontroli zjada pulę PrimaAuto (incydent Desal 29.05).
   Wyłącznie `~/bin/index-submit`.
2. **Zgłoszenie strony przed poprawką jest gorsze niż brak zgłoszenia** — Google odświeży werdykt
   na starej treści i wróci nieprędko. Dlatego kolejność T-008 → T-009 → T-027 jest twarda.
3. **Indexing API oficjalnie obsługuje `JobPosting` i `BroadcastEvent`.** Dla zwykłych stron działa
   jako sygnał re-crawl, ale nie jest gwarancją — jeśli po 14 dniach nic, przyczyna leży gdzie
   indziej (patrz T-026, gdzie 3 strzały nie pomogły).
4. **Nie strzelaj drugi raz w tę samą stronę w krótkim odstępie.** To nie przyspiesza, a zużywa pulę.
5. **`BLOCKED_BY_META_TAG` z 12 kwietnia to zaległy werdykt, nie aktywny noindex** — live ma
   `index, follow`. Zweryfikuj to `curl`-em **przed** zgłoszeniem; jeśli na żywo jednak jest noindex,
   zgłoszenie nie ma sensu i szukasz źródła.

## 3. Stan zmierzony 19.08.2026

```
GSC URL Inspection /do-pobrania/:
  verdict:        NEUTRAL
  coverageState:  Excluded by 'noindex' tag
  indexingState:  BLOCKED_BY_META_TAG
  robotsTxtState: ALLOWED
  pageFetchState: SUCCESSFUL
  lastCrawlTime:  2026-04-12T17:58:58Z      ← 129 dni temu
  googleCanonical: https://agria.pl/do-pobrania/
index-submit --status: 0 / 100 zużyte dziś, --dry-run przechodzi
```

## 4. Warunki wejścia

- [ ] T-008 zamknięty (karty Nordkalku na stronie).
- [ ] T-009 zamknięty (sekcja Certyfikaty usunięta).
- [ ] `curl -s https://agria.pl/do-pobrania/ | grep -o 'content="index[^"]*"'` potwierdza `index, follow`.
- [ ] `index-submit --status` pokazuje wolny budżet.

## 5. Co robisz

```bash
# 1. potwierdź, że live nie ma noindex
curl -s https://agria.pl/do-pobrania/ | grep -oP '(?<=name="robots" content=")[^"]*'
# 2. pokaż Jankowi stan budżetu
~/bin/index-submit --status
# 3. dry-run
~/bin/index-submit --project agria --type URL_UPDATED --url https://agria.pl/do-pobrania/ --dry-run
# 4. po „ok" — realne zgłoszenie
~/bin/index-submit --project agria --type URL_UPDATED --url https://agria.pl/do-pobrania/
```

## 6. Jak sprawdzasz w trakcie

`~/bin/index-submit --status` po zgłoszeniu — licznik ma wzrosnąć o 1.
Log: `~/.claude/indexing-submit.log`.

## 7. Jak testujesz

GSC URL Inspection po **72 h** i po **14 dniach** — porównanie `lastCrawlTime` i `coverageState`
z wartościami z sekcji 3. Sukces = crawl z datą po wdrożeniu **i** `coverageState` inne niż
„Excluded by 'noindex'".

## 8. Dowód do rejestru

Wpis z `~/.claude/indexing-submit.log` (data, URL, projekt) + werdykt GSC z rechecku +72 h
z widocznym nowym `lastCrawlTime`. **Samo zgłoszenie nie jest dowodem zamknięcia** — dowodem
jest zmiana werdyktu. Do tego czasu wiersz zostaje 🔴 z adnotacją „zgłoszone <data>, czekam".

## 9. Rollback

Nie ma. Zgłoszenia nie da się cofnąć — dlatego kolejność po T-008/T-009 jest warunkiem, nie preferencją.

## 10. Rozliczenie

Zakres **R**, ~0,25 h. Do DZIENNIKA M3 dopiero po potwierdzeniu crawla.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+72 h** | URL Inspection — czy `lastCrawlTime` się zmienił |
| **+14 dni** | URL Inspection — czy `coverageState` = zaindeksowana |
| **+30 dni** | GSC Search Analytics: czy `/do-pobrania/` zbiera wyświetlenia (17 kart PDF to ruch na frazy typu „karta charakterystyki wapno") |
