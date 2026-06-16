# Backlog poprawek strony agria.pl

> Żywy backlog poprawek zgłaszanych przez klienta (Paweł Bigos, AGRIA).
> Paweł dosyła kolejne partie — dokument otwarty, dopisujemy na bieżąco.
> Wdrożenie: **SSH / WP-CLI** na nazwa.pl (MCP Agria = read-only, nie do zapisu).
> Status na: 2026-06-16. Źródło partii #1: mail Pawła z 2026-06-15 20:30 (fwd Janka, [73]).

---

## Legenda statusów

- 🟢 **GOTOWE DO WDROŻENIA** — zakres jasny, technicznie zlokalizowane, czeka tylko na realizację
- 🟡 **CZEKA NA MATERIAŁY** — bloker po stronie klienta (pliki, dane)
- 🔵 **WYMAGA KONCEPCJI / DANYCH** — zakres miękki, do ustalenia
- ⚪ **PO STRONIE KLIENTA** — robi Paweł, nie nasze zadanie
- ✅ **WDROŻONE**

**Decyzja Janka 2026-06-16:** na teraz tylko spisanie backlogu — **zero wdrożeń na produkcji** do osobnego startu (zbliża się urlop Janka).

---

## Partia #1 — mail Pawła 2026-06-15

### STR-01 · Kalkulator wapnowania — usunąć kredę pastewną i malarską 🟢
**Zgłoszenie:** „kalkulator wapnowania — usunąć z niego kredę pastewną i kredę malarską."
**Lokalizacja:** strona *Kalkulator wapnowania* (`/kalkulator-wapnowania/`, post ID 729) → widget shortcode `[agria_kalkulator_wapnowania]`. Logika produktów w custom kodzie (motyw `Agria By Auranet 2.0.0` lub dedykowany plugin — do namierzenia przy wdrożeniu: `grep` za `kreda` / `pastewna` / `malarska` w plikach motywu/pluginu po SSH).
**Do zrobienia:** usunąć dwie pozycje produktowe (kreda pastewna, kreda malarska) z listy produktów wapniowych dobieranych przez kalkulator. Uzasadnienie Pawła sensowne — kalkulator liczy dawkę CaO do odkwaszania pola, kreda pastewna (dodatek paszowy) i malarska tam nie pasują.
**Bloker:** brak (wdrożenie SSH).

### STR-02 · Formy dostawy z PIM — usunąć spod specyfikacji technicznej 🟢
**Zgłoszenie:** „usunąłbym też wszędzie spod specyfikacji technicznej formy dostawy z PIMu, które nanosiliśmy — czasami nawet małe ilości możemy wysyłać, a taki zapis nas ogranicza."
**Zakres (potwierdzony Janek 2026-06-16):** zdjąć sekcję form dostawy ze **wszystkich** kart produktów.
**Lokalizacja:** specyfikacja techniczna na kartach produktów (19 prod. WC). Mechanizm renderowania form dostawy (meta produktu / atrybut WC / template motywu) — do namierzenia przy wdrożeniu.
**Do zrobienia:** usunąć blok „formy dostawy" z wyświetlania specyfikacji. Uwaga: to cofnięcie zmiany, którą sami nanosiliśmy — sprawdzić czy usuwamy dane (meta) czy tylko ich render w template.
**Bloker:** brak (wdrożenie SSH).

### STR-03 · Mapa w Kontakcie — telefony zsynchronizować z oddziałami pod mapą 🟢🔵
**Zgłoszenie:** „nanieść na mapie w kontaktach telefony — takie same jak przy oddziałach (poniżej mapy)."
**Lokalizacja:** strona *Kontakt* (post ID 323), custom JS Google Maps (`agria-map`), tablica `var locations[]` z polami `phone` / `phoneFull` w infowindow markerów.
**Stan obecny na mapie:** Tarnów `14 621 88 21`, Radgoszcz `14 641 43 01`, Niedomice `604 428 782`.
**Problem:** rozjazd z numerami w kartach oddziałów pod mapą (na stronie widoczne też `660 76 86 91`, `664 393 062`). Paweł chce ujednolicić mapę do numerów spod mapy.
**Do zrobienia:** zaktualizować `phone`/`phoneFull` w `locations[]` tak, by zgadzały się z kartami oddziałów.
**Bloker — DANE:** potrzebny **właściwy numer per oddział** (zwł. siedziba Tarnów — centrala `14 621 88 21` czy komórka handlowca?). Ustalić z Pawłem przed edycją.

### STR-04 · Sekcja „do pobrania" — karty produktu + karty charakterystyki 🟡
**Zgłoszenie:** „do pobrania — nanieść wszystkie nowe karty produktu oraz karty charakterystyki. (...) jutro dowiem się, czy producent zgadza się na przerobienie kart i dodanie naszego logo. Materiały jutro podeślę, mam je na kompie w Niedomicach."
**Do zrobienia:** wgrać nowe PDF (karty produktu + karty charakterystyki/MSDS) i podpiąć do sekcji „do pobrania" na kartach produktów.
**Bloker — MATERIAŁY:** PDF-y od Pawła (Niedomice, ~2026-06-16). Plus otwarta kwestia: zgoda producenta na kartę z logo AGRIA.

### STR-05 · Zdjęcia produktów — ujednolicić wg katalogu 🟡
**Zgłoszenie:** „zmienić zdjęcia produktów — obecnie są pomieszane. Zdjęcia powinny być takie, jak dawaliśmy do katalogu produktów, materiały będziesz miał na whatsappie."
**Do zrobienia:** podmienić zdjęcia główne/galerię produktów na te z katalogu drukowanego (mapowanie produkt → zdjęcie).
**Bloker — MATERIAŁY:** zestaw zdjęć z WhatsApp + mapowanie do konkretnych produktów. Warto wymóc nazewnictwo plików = nazwa produktu, żeby uniknąć kolejnego „pomieszania".

### STR-06 · Sekcja „Dział sprzedaży" — przebudowa po odejściu P. Stanisława 🔵
**Zgłoszenie:** „zastanowiłbym się, czy nie zmienić sekcji Dział sprzedaży — jakoś inaczej ją ułożyć albo coś dodać, bo po usunięciu P. Stanisława mam wrażenie, że czegoś tam brakuje."
**Do zrobienia:** propozycja nowego układu sekcji Dział sprzedaży (strona Kontakt) — uzupełnić tak, by nie sprawiała wrażenia niekompletnej.
**Bloker — DANE + KONCEPCJA:** aktualny skład działu (kto został, imiona/role/telefony/segmenty obsługi). Po zebraniu danych — przygotujemy 1 propozycję układu do akceptu (bez agencyjnych frameworków — ustalenie z Pawłem telefonicznie / przez Janka).

### STR-07 · Tekst strony — korekta interpunkcji ⚪
**Zgłoszenie:** „tekst poprawiłem, ale i tak muszę go jeszcze sprawdzić pod kątem interpunkcji itp."
**Status:** robi Paweł sam. Czekamy aż przekaże finalny tekst — wtedy ewentualnie naniesiemy.

---

## Wątki poboczne (nie-stronowe, do śledzenia)

- **Wizytówka Google (GBP):** Paweł nie kojarzy maila o wizytówce — zadzwoni do P. Stanisława, dopyta czy to kontakt poprzedniego operatora. Jeśli nie — odzysk przez pomoc Google. *Nasza rola:* wsparcie przy odzysku dostępu, gdy Paweł da znać.

---

## Czego potrzebujemy od Pawła (zbiorczo — bloker-dane)

1. Karty produktu + karty charakterystyki (PDF) — STR-04
2. Zdjęcia produktów wg katalogu + mapowanie do produktów — STR-05
3. Właściwe telefony per oddział (zwł. siedziba Tarnów) — STR-03
4. Aktualny skład działu sprzedaży po P. Stanisławie — STR-06

---

## Następny krok (po starcie wdrożeń)

Kolejność wg gotowości: **STR-01 → STR-02** (oba odblokowane, czysto techniczne, SSH/WP-CLI) → **STR-03** (po dosłaniu numerów) → STR-04/05 (po materiałach) → STR-06 (po danych) → STR-07 (po finalnym tekście Pawła).
Przed edycją plików produkcyjnych: `mysqldump` + backup plików do `~/backups/agria/<data>/` (reguła globalna).
