# T-047 — odzysk profili GBP: Niedomice i Radgoszcz

| | |
|---|---|
| **Linia / zakres** | GBP · **R** |
| **Status** | 🟡 czeka na AGRIĘ od 15.07 |
| **Blokuje** | pełne `T-030` (LocalBusiness ×2) i multi-location w komunikacji |
| **Szacunek** | 1 h zgłoszenia + tygodnie oczekiwania na Google |

---

## 1. Czego to dotyka

Dwa profile firmowe w Google, których **nie mamy na koncie** — potwierdzone 19.08:
lista lokalizacji konta `accounts/111497772731899556217` zawiera osiem pozycji (AGRIA Tarnów,
Prima-Auto, Victorini, Laguz, ASEO ×2, PlakatyDlaFirm, Auranet) i **żadnego oddziału AGRII**.

## 2. Strefy kruche

1. **Request access uruchamia procedurę, w której obecny właściciel dostaje mail** i ma czas
   na reakcję. Jeśli profil jest pod prywatnym kontem byłego pracownika, sprawa może stanąć.
   To jest powód, dla którego trwa od 15.07.
2. **Weryfikacja własności wymaga danych rejestrowych** — KRS 0000170666, NIP 8730006657.
   Te dane idą do Google, więc muszą być dokładne.
3. **Nie twórz nowych profili „bo szybciej".** Duplikat lokalizacji w Google to kara widoczności
   dla obu wpisów i bałagan, którego nie da się szybko posprzątać.
4. **W komunikacji do klienta multi-location pozostaje przemilczane**, dopóki dostępu nie ma —
   nie obiecujemy rozwoju wizytówek Niedomic i Radgoszczy, nie wpisujemy ich do raportów
   jako „w toku".
5. **Konto Auranet, z którego idzie request, jest typu PERSONAL i UNVERIFIED** — to może być
   dodatkowa przeszkoda w procedurze. Sprawdź, zanim zaczniesz, czy Google nie wymaga
   konta firmowego.

## 3. Stan zmierzony 19.08.2026

```
GBP API, lokalizacje na koncie: 8 — w tym AGRIA Tarnów (locations/11686460679773422640)
Niedomice: BRAK        Radgoszcz: BRAK
```

## 4. Warunki wejścia

- [ ] Ustalone, czy profile w ogóle istnieją w Google (wyszukanie w Mapach po adresie oddziału).
- [ ] Janek zdecydował, z którego konta idzie request.

## 5. Co robisz

1. Sprawdź w Mapach, czy profile istnieją i jaki mają stan (zweryfikowany / niezweryfikowany /
   „zgłoś jako właściciel").
2. Jeśli istnieją: Request access z konta wskazanego przez Janka, z danymi KRS/NIP.
3. Jeśli nie istnieją: to nie jest „odzysk", tylko utworzenie — **osobna decyzja Janka**,
   bo wiąże się z weryfikacją pocztową i obsługą dwóch dodatkowych profili na stałe.
4. Zapisz datę zgłoszenia i termin, po którym Google odpowiada (zwykle 3–7 dni na reakcję
   właściciela, potem decyzja).

## 6. Jak sprawdzasz

Ponowne `accounts/.../locations` po każdej zmianie statusu — pojawienie się lokalizacji
na liście jest jedynym twardym dowodem.

## 7. Jak testujesz

```bash
# lista lokalizacji konta — oddziały mają się pojawić
python3 - <<'PY'   # patrz wzorzec w 00-PROTOKOL-WSPOLNY §4
PY
```

## 8. Dowód do rejestru

Data zgłoszenia, odpowiedź Google, `locations/<id>` obu oddziałów po odzyskaniu.

## 9. Rollback

Nie dotyczy — nic nie zmieniamy, tylko wnioskujemy o dostęp.

## 10. Rozliczenie

Zakres **R**. Godziny minimalne, czas oczekiwania nie jest naszą robotą.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+7 dni od zgłoszenia** | status wniosku |
| **co 14 dni** | dopóki brak odpowiedzi — przypomnienie przy rozmowie Janka z Pawłem |
| **po odzyskaniu** | odblokowuje pełne `T-030` i temat multi-location w komunikacji |
