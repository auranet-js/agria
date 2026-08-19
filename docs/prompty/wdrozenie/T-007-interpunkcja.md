# T-007 — korekta interpunkcji w tekstach

| | |
|---|---|
| **Linia / zakres** | Strona · **K** (robi AGRIA) |
| **Status** | ⚪ robi Paweł sam — czeka od 15.06 |
| **Szacunek** | po naszej stronie: 0 h, o ile Paweł nie poprosi o wykonanie |

---

## 1. Czego to dotyka

Teksty na stronie. Wykonawcą jest **Paweł**, samodzielnie w Elementorze.

## 2. Strefy kruche

1. **To jest jedyna pozycja w rejestrze, której nie wykonujemy.** Nie „pomagajmy" przy okazji
   innej edycji — dwie osoby edytujące tę samą treść w Elementorze to konflikt wersji bez historii.
2. **Wtyczka Orphans (sierotki) 3.4.4 działa na produkcji** i sama przenosi jednoliterowe spójniki
   do następnego wiersza. Jeśli Paweł zgłosi „coś się psuje z odstępami" — sprawdź ją, zanim
   uznasz to za jego błąd.
3. **Jeśli Paweł edytuje strony, których dotyka `T-008`/`T-009`/`T-010`, powstanie konflikt.**
   Przed edycją tych stron warto wiedzieć, czy właśnie ich nie poprawia — `post_modified` powie.
4. **Nie przepisuj treści przy okazji** poprawiania czegoś innego. Zmiana, o którą nikt nie prosił,
   jest w tym projekcie kosztem, nie wartością.

## 3. Stan

Otwarte od 15.06. Wykonawca: AGRIA.

## 4. Warunki wejścia

Brak — nie jest to nasze zadanie. Chyba że Paweł poprosi wprost, wtedy przekwalifikuj na **R**
i potraktuj jak normalną edycję treści.

## 5. Co robisz

1. Przy każdym przeglądzie kolejki sprawdź `post_modified` stron, których dotyczy:
   ```sql
   SELECT ID, post_title, post_modified FROM {prefix}posts
   WHERE post_type IN ('page','post','product') AND post_status='publish'
   ORDER BY post_modified DESC LIMIT 20
   ```
2. Jeśli widać ruch — Paweł pracuje, zostaw. Jeśli od 15.06 zero zmian — Janek przypomni telefonicznie.
3. Nie wysyłaj przypomnień mailem. Paweł jest obsługiwany telefonicznie.

## 6. Jak sprawdzasz / testujesz

`post_modified` i porównanie z datą zgłoszenia. Nic więcej.

## 7. Dowód do rejestru

Data, w której Paweł potwierdził wykonanie, albo decyzja o przejęciu zadania przez nas.

## 8. Rozliczenie

Zakres **K** — nie nasze godziny. W DZIENNIKU odnotowujemy datę domknięcia, nie czas.

## 9. Recheck

| Kiedy | Co |
|---|---|
| **przy każdym przeglądzie kolejki** | czy nadal wisi; 65+ dni na pozycji „robi klient" to sygnał, że trzeba ją albo przejąć, albo zamknąć jako nieaktualną |
