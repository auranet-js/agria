# Menu — powrót pozycji Sadownictwo / Rybactwo / Hurtownie

> Pozycja bez numeru w rejestrze. **Propozycja: nadać `T-049`** przy najbliższej aktualizacji rejestru — pozycja bez ID nie da się zacytować w commicie ani w raporcie.

| | |
|---|---|
| **Linia / zakres** | Strona · **R** |
| **Status** | 📅 wrzesień (M4) |
| **Przypomnienie** | `docs/przypomnienia/2026-09-01-menu-segmenty-m4.md` (kalendarz „Auranet Claude") |
| **Szacunek** | 1 h menu + czas na treść (osobno) |

---

## 1. Czego to dotyka

Menu główne WordPressa (trzy pozycje ustawione 30.07 jako `draft`) oraz strony docelowe,
na które te pozycje wskazują.

## 2. Strefy kruche

1. **Pozycje zdjęto, bo prowadziły na puste kategorie z przekierowaniem 301.** Przywrócenie
   ich bez treści odtwarza dokładnie ten sam błąd — menu wskazujące w pustkę jest gorsze
   niż jego brak.
2. **Wracają razem z treścią, nie razem z landingami.** To jest wprost zapisane w memory
   `project_agria_nav_debt_m4` i w rejestrze. Landingi segmentowe (`T-036`) są **unieważnione**
   ADR-em o kanibalizacji — nie wracaj do nich tylnymi drzwiami pod pretekstem „przecież menu
   musi gdzieś prowadzić".
3. **Kanibalizacja jest zmierzona, nie teoretyczna:** fraza „wapno bielik" z sześcioma URL-ami
   dawała pozycję 15,3, a frazy z jednym URL-em wchodziły do TOP10. Nowa strona segmentowa
   bez odrębnej intencji odbiera pozycje istniejącym.
4. **Trzy pozycje to trzy różne sytuacje.** Rybactwo i oczyszczalnie mają zerowy wolumen
   w Ads; sadownictwo i hurtownie to inna sprawa. Nie traktuj ich jako jednego pakietu —
   każda potrzebuje osobnej decyzji, czy treść w ogóle ma powstać.
5. **Menu jest w bazie jako `nav_menu_item`** — zmiana statusu z `draft` na `publish` to jedna
   operacja, natychmiast widoczna dla wszystkich. Nie „na próbę".

## 3. Stan

Trzy pozycje w statusie `draft` od 30.07. Do sprawdzenia w dniu wykonania:
```sql
SELECT ID, post_title, post_status, menu_order FROM {prefix}posts
WHERE post_type='nav_menu_item' ORDER BY menu_order
```

## 4. Warunki wejścia

- [ ] Treść docelowa istnieje i jest opublikowana — dla **każdej** przywracanej pozycji osobno.
- [ ] Potwierdzone (T-003 / pytanie 3 do Pawła), że dany segment jest realnym segmentem sprzedaży.
      Oferta handlowa nie wymienia budownictwa i drogownictwa, katalog tak — ta sama wątpliwość
      dotyczy części tych pozycji.

## 5. Co robisz

1. Dla każdej z trzech pozycji ustal, dokąd ma prowadzić i czy ta strona istnieje z treścią.
2. Pozycje bez treści **zostają w `draft`**. Przywracasz tylko te z pokryciem.
3. Zmiana statusu przez WP-CLI albo panel, jedna pozycja naraz.
4. Kontrola nawigacji przez Chrome MCP: menu na desktopie i na mobile.

## 6. Jak sprawdzasz w trakcie

```bash
curl -s https://agria.pl/ | grep -oP '(?<=href="https://agria.pl/)[^"]*(?=")' | sort -u
```
Każdy nowy link z menu przetestuj na kod HTTP — 301 albo 404 w menu głównym to regres.

## 7. Jak testujesz

```bash
for u in <nowe pozycje menu>; do printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' https://agria.pl$u)" "$u"; done
```
Wszystkie mają dać 200. Plus render menu na mobile przez Chrome MCP.

## 8. Dowód do rejestru

Lista przywróconych pozycji z kodami HTTP celów, zrzut menu z Chrome MCP, lista pozycji,
które świadomie **nie** wróciły, z powodem.

## 9. Rollback

Powrót statusu na `draft` — jedna operacja.

## 10. Rozliczenie

Zakres **R**, wrzesień (M4). Treść dla segmentów, jeśli powstanie, rozliczana osobno wg zakresu.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | wszystkie linki menu → 200, render mobile |
| **+30 dni** | GSC: czy nowe strony segmentowe nie odebrały pozycji istniejącym (test kanibalizacji — `scripts/seo_baseline.py`) |
