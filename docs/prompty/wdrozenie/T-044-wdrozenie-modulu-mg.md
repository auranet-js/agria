# T-044 — wdrożenie modułu Mg w kalkulatorze na produkcję

| | |
|---|---|
| **Linia / zakres** | Kalkulator · **P**, ≈4 h |
| **Status** | 📅 wrzesień (M4) — **po `T-043`** |
| **Szacunek** | 4 h + testy |

---

## 1. Czego to dotyka

Moduł `agria-by-auranet/modules/liming-calculator/` na produkcji: szablon (nowe pola kroku 3b–3d),
klasyfikacja w PHP, endpoint AJAX, matcher produktów (`extract_cao_percent`, dobór po `pa_agria-mgo`).
Pośrednio: **wszystkie wyniki kalkulatora**, także te bez magnezu — jeśli ruszysz matcher.

## 2. Strefy kruche

1. **Kalkulator jest narzędziem, na którym rolnik opiera decyzję o dawce.** Błąd w przeliczniku
   nie daje 500, tylko złą liczbę, której nikt nie zauważy do żniw. Testy liczbowe są ważniejsze
   niż testy interfejsu.
2. **Cztery kwestie z `T-043` muszą być rozstrzygnięte przed pierwszą linią kodu:**
   %CaO produktu #313 · rozjazd Dolomitu (45 vs 30) · przycinanie wartości Mg vs komunikat ·
   ostrzeżenie o progu jednorazowej dawki. Wdrażanie „z tymczasowym założeniem" oznacza,
   że założenie zostanie na produkcji na rok.
3. **Zmiana `extract_cao_percent` dotyka wszystkich produktów**, nie tylko dolomitu. Jeśli
   poprawiasz — przelicz **cały** zestaw 15 produktów przed i po, i porównaj.
4. **`post__not_in [304,307]`** — kalkulator nie proponuje kredy pastewnej ani malarskiej (T-001,
   wdrożone 18.06). Ta reguła zostaje; nowy kod nie może jej obejść inną ścieżką doboru.
5. **Default celu nawożenia = górna granica „wysokiej".** Nie zmieniaj — decyzja Janka, raz już
   wycofano próbę zmiany na minimum.
6. **Dobór jest dwuetapowy (Mg-first)**: dawkę nawozu magnezowego ustala niedobór Mg (sort po %MgO
   malejąco), brakujące CaO dopokrywa wapno bez magnezu. Poprzednie `max(wg Mg, wg CaO)` dawało
   nierealne 16–19 t/ha dolomitu — jeśli w testach zobaczysz takie liczby, wróciłeś do starej logiki.
7. **Parametry wyłącznie z kart producentów.** 17 kart leży publicznie na `/do-pobrania/` —
   klient ściąga ten sam PDF, więc każdy rozjazd wyjdzie na jaw.
8. **Wdrożenie idzie przez MCP `write_file`** (auto-backup `.bak-*`) albo FTP. Po każdym zapisie
   sprawdź `mcp__agria__logs` — błąd składni PHP w module kalkulatora zdejmuje stronę kalkulatora,
   a przy złym miejscu — całą witrynę.

## 3. Stan

Mockup gotowy (`mockups/agria-kalkulator-mg-test-2026-08-18.html`, commit `c4547d2`), u Kazimierza
od 18.08. Produkcyjny moduł bez modułu Mg.

## 4. Warunki wejścia

- [ ] `T-043` zamknięty: uwagi Kazimierza naniesione i zaakceptowane.
- [ ] Cztery otwarte kwestie rozstrzygnięte przez Janka, na piśmie w rejestrze albo ADR-ze.
- [ ] `backup_file` na wszystkich plikach modułu.
- [ ] Zestaw przypadków testowych przygotowany **przed** kodowaniem (wejście → oczekiwana dawka).

## 5. Co robisz

1. Zbuduj tabelę przypadków testowych: 3 typy gleby × (z Mg / bez Mg) × 2 poziomy niedoboru
   = 12 przypadków z ręcznie policzoną oczekiwaną dawką. **To jest test regresji** — bez niego
   nie masz jak stwierdzić, że nie zepsułeś istniejących wyników.
2. Uruchom te przypadki na **obecnej** produkcji (ścieżka bez Mg) i zapisz wyniki jako baseline.
3. Przenieś logikę z mockupu do modułu: pole kroku 3b, klasyfikacja, dobór Mg-first, matcher.
4. Zapis przez MCP (auto-backup), sprawdzenie `logs` po każdym pliku.
5. Przejdź 12 przypadków ponownie. Ścieżka bez Mg **musi dać identyczne wyniki co baseline**.
6. Kontrola renderu przez Chrome MCP — na produkcji, nie w mockupie.

## 6. Jak sprawdzasz w trakcie

Po każdym zapisie pliku: `mcp__agria__logs(lines=30)` i `curl -s -o /dev/null -w '%{http_code}'`
na `/kalkulator-wapnowania/`. Białe okno = wracasz z backupu, nie debugujesz na żywej stronie.

## 7. Jak testujesz

```bash
curl -s -o /dev/null -w 'kalkulator %{http_code}\n' https://agria.pl/kalkulator-wapnowania/
```
Plus 12 przypadków przez interfejs (Chrome MCP), plus porównanie ze ścieżką baseline.
Test akceptacyjny: Kazimierz przechodzi trzy własne przypadki na produkcji i potwierdza.

## 8. Dowód do rejestru

Tabela 12 przypadków: wejście, oczekiwane, baseline, po wdrożeniu. Potwierdzenie Kazimierza.
Nazwy plików backupu. Hash commitu z kopią modułu w `src/`.

## 9. Rollback

`.bak-*` z auto-backupu MCP, przywrócenie przez `write_file` z zawartością backupu
albo `cp` przez SSH. Rollback ma być przetestowany **przed** wdrożeniem, nie w trakcie awarii.

## 10. Rozliczenie

Zakres **P** ≈4 h. Wrzesień (M4). Jeśli poprawka matchera rozrośnie się na wszystkie produkty —
zgłoś Jankowi rozszerzenie zakresu, zanim ją zaczniesz.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | 12 przypadków + logi PHP |
| **+24 h** | logi pod kątem błędów AJAX z realnego ruchu |
| **+7 dni** | czy Kazimierz albo Paweł nie zgłosili dziwnych wyników |
| **+30 dni** | przelicz 3 przypadki ponownie — czy aktualizacja WP/WC nie zmieniła zachowania matchera |
