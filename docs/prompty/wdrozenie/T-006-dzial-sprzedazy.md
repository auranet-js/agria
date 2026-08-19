# T-006 — przebudowa sekcji „Dział sprzedaży" po odejściu P. Stanisława

| | |
|---|---|
| **Linia / zakres** | Strona · **R** |
| **Status** | 🟡 czeka na AGRIĘ — **65 dni** |
| **Zgłosił** | Paweł, 15.06.2026 |
| **Szacunek** | 1,5 h po otrzymaniu danych |

---

## 1. Czego to dotyka

Sekcja kontaktowa na `/kontakt/` i wszędzie, gdzie powielony jest skład działu (stopka, `/o-firmie/`,
karty produktów z „zapytaj o ofertę"). Dane osobowe pracowników — imiona, role, telefony, segmenty.
Pośrednio: schema `Organization`/`ContactPoint`, spójność NAP z GBP (T-046) i z OLX.

## 2. Strefy kruche

1. **Blokada jest po stronie klienta i jest twarda** — nie znamy aktualnego składu działu.
   **Nie zgaduj, nie przepisuj ze starej wersji, nie usuwaj samego P. Stanisława „na wszelki wypadek"**:
   telefon może być przekierowany, a puste miejsce w dziale wygląda gorzej niż nieaktualne nazwisko.
2. **Numery telefonów to dane, które gdzieś już żyją** — GBP (`14 621 88 21`), OLX, Ads
   (rotacja dwóch numerów: Paweł 664 393 062, Kazimierz 781 875 411). Zmiana na stronie musi być
   spójna ze wszystkimi.
3. **Zepsuty `href` Kazimierza: `http://+48 781 875 411`.** To da się naprawić **niezależnie
   od blokady** — nie wymaga wiedzy o składzie działu, tylko poprawnego `tel:`. Zrób to od razu
   jako osobny mikro-zapis, nie czekaj 65 dni na resztę.
4. **Dane osobowe** — telefony pracowników publikowane na stronie to decyzja pracodawcy, nie nasza.
   Publikujemy dokładnie to, co Paweł poda, ani jednej kolumny więcej.
5. **Forma pytania: telefon Janka, nie mail z tabelą.** Paweł jest obsługiwany telefonicznie;
   mail z frameworkiem klasyfikacji został raz odrzucony jako agencyjny.

## 3. Stan zmierzony

Do sprawdzenia w dniu wykonania: które strony zawierają skład działu, w której warstwie
(`post_content` / `_elementor_data`), gdzie dokładnie siedzi zepsuty `href`.
```bash
curl -s https://agria.pl/kontakt/ | grep -oP 'href="tel:[^"]*|href="http://\+48[^"]*'
```

## 4. Warunki wejścia

- [ ] **Paweł podał: imiona, role, telefony, obsługiwane segmenty.** To jest jedyna blokada.
- [ ] Ustalone, czy telefon P. Stanisława jest przekierowany (jeśli tak, numer zostaje, opis się zmienia).

## 5. Co robisz

**Teraz, bez czekania:** napraw `href` Kazimierza na `tel:+48781875411` — jeden zapis, jedna weryfikacja.

**Po otrzymaniu danych:**
1. Zinwentaryzuj wszystkie miejsca ze składem działu (`grep` po `post_content` i `_elementor_data`).
2. Pokaż Jankowi listę miejsc i proponowaną treść.
3. Zapis warstwa po warstwie, z `expect_old_len`.
4. Sprawdź spójność z GBP i OLX.

## 6. Jak sprawdzasz w trakcie

Każdy numer telefonu na stronie musi być klikalny i prowadzić do właściwego numeru:
```bash
curl -s https://agria.pl/kontakt/ | grep -oP '(?<=href="tel:)[^"]*'
```

## 7. Jak testujesz

Wszystkie strony ze składem działu przez Chrome MCP — nazwiska, role, telefony zgodne z tym,
co podał Paweł. Zero wystąpień nazwiska osoby, która odeszła (chyba że Paweł zdecydował inaczej).

## 8. Dowód do rejestru

Lista poprawionych URL-i, zrzut `tel:` po zmianie, potwierdzenie Pawła (przez Janka), hash commitu.

## 9. Rollback

`db_export` sprzed zmiany.

## 10. Rozliczenie

Zakres **R**. Naprawa `href` — mikro-pozycja, wpisz osobno w DZIENNIK, bo jest wykonalna dziś
i nie powinna czekać na resztę.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h po naprawie href** | `curl` na `/kontakt/` |
| **co 14 dni, dopóki blokada trwa** | przypomnienie Jankowi przy rozmowie z Pawłem — 65 dni to za długo |
| **+7 dni po wdrożeniu składu** | spójność telefonów: strona ↔ GBP ↔ OLX ↔ Ads |
