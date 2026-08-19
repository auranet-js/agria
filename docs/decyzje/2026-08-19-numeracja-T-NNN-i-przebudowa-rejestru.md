# Numeracja T-NNN i przebudowa rejestru na kolejkę + dziennik

> ADR, 2026-08-19. Decyzja Janka po porównaniu struktury agrii z `primaauto` i `victorini`.

## Problem

Projekt nie odpowiadał na pytanie „co robimy teraz i co nas blokuje". Trzy przyczyny, wszystkie
potwierdzone porównaniem z dwoma projektami, gdzie to działa:

1. **Rejestr ułożony po liniach usługowych, nie po czasie.** Osiem sekcji tematycznych (Strona /
   Ceny / SEO / Ads / OLX / Kalkulator / Ofertownik / GBP) mówi, co jest w temacie X. Victorini
   układa kolejkę po horyzoncie: *najbliższe (M4, 20 h) / czeka na Mariusza (z datą „czeka od") /
   zaplanowane*. Prima tak samo, plus graf zależności.
2. **Numer zadania nie żył w nazwach plików.** `grep -roE '\bT-[0-9]+' docs/` dawał 4 trafienia
   w całym repo. U Victoriniego jeden task to zestaw plików o wspólnym prefiksie
   (`t148-*-prompt`, `t148-mail-do-mariusza`, `raporty/*-t148-*`) — cofnięcie się to `ls | grep t148`.
   Efekt u nas: audyty i prompty nie miały do czego przylgnąć.
3. **Brak dziennika dostaw.** Victorini trzyma `KOLEJKA` + `DZIENNIK` (co dostarczone w miesiącu,
   ile godzin, w pakiecie / dodatkowe / gratis) i konfrontuje dziennik z `git log` przed raportem.
   U nas raport miesięczny powstawał za każdym razem od zera.

## Decyzje

1. **Identyfikatory `T-NNN`, jeden ciąg dla całego projektu.** Prefiksy per linia usługowa
   (`STR-`, `CEN-`, `ADS-`, `OLX-`, `KAL-`, `OFE-`, `GBP-`, `P0-`, `P1-`, `A`, `B`, `C`, `D`, `E`,
   `DUP-`, `HUB-`) **znikają**. Powód: siedemnaście schematów naraz, część odziedziczona po audytach,
   nieczytelna dla człowieka. Linia usługowa zostaje jako **kolumna**, nie jako część nazwy.
   Świadomy koszt: odnośniki krzyżowe w `FAKTY_KLIENTA.md` trzeba podmienić ręcznie.
2. **Rejestr w dwóch częściach.** `KOLEJKA` (teraz / czeka na AGRIĘ / zaplanowane) odpowiada na
   „co robimy". `DZIENNIK` per miesiąc odpowiada na „co dostarczyliśmy" — materiał do raportu.
3. **Godziny w dzienniku, nie w komunikacji do klienta.** AGRIA jest na ryczałcie 2 000/mies, więc
   klient godzin nie widzi; my potrzebujemy ich, żeby wiedzieć, czy pakiet się spina. Tam, gdzie
   nie znamy liczby wstecz (M1-M3) — **wpisujemy 5** jako znacznik „nieodtworzone", nie jako pomiar.
4. **`PROJECT_STATE.md` zwijamy** do `docs/sesje/`. Był trzecim opisem tego samego stanu w innej
   kolejności i głównym źródłem rozjazdu.
5. **Numer zadania wchodzi w nazwy plików.** Każdy nowy prompt, audyt, raport i mail dostaje prefiks
   `T-NNN` w nazwie.

## Mapa przenumerowania

| Nowy | Stary | Co to jest | Stan 19.08 |
|---|---|---|---|
| T-001 | STR-01 | kalkulator bez kredy pastewnej i malarskiej | ✅ |
| T-002 | STR-02 | formy dostawy zdjęte z 19 kart i FAQ | ✅ |
| T-003 | STR-03 | telefony na mapie zgodne z oddziałami, 660 usunięty | ✅ |
| T-004 | STR-04 | karty i charakterystyki na `/do-pobrania/` | ✅ |
| T-005 | STR-05 | zdjęcia produktów zgodne z katalogiem | ✅ |
| T-006 | STR-06 | przebudowa sekcji „Dział sprzedaży" | 🟡 czeka na AGRIĘ, 65 dni |
| T-007 | STR-07 | korekta interpunkcji — robi Paweł | ⚪ |
| T-008 | STR-08 | 8 atestów i kart Nordkalku na `/do-pobrania/` | 🔴 teraz |
| T-009 | STR-09 | usunięcie sekcji „Certyfikaty" | 🔴 teraz, razem z T-008 |
| T-010 | CEN-01 | widełki „od X zł/t" w treści 15 kart + 2 landingi + poradnik | 🔴 **priorytet 1** |
| T-011 | CEN-02 | nagłówki H2 z frazą cenową | 🔴 teraz, z T-010 |
| T-012…T-025 | P0-2a, P1-1, P1-2, P1-4, P1-5, P1-6, A1, A3, B1, B2, B6, B7, C1, landingi Ads noindex | blok SEO zamknięty i zweryfikowany 19.08 | ✅ → dziennik |
| T-026 | P0-6 | sześć adresów poza indeksem Google | 🔴 teraz |
| T-027 | P0-6b | `/do-pobrania/` z kwietniowym werdyktem noindex | 🔴 teraz, po T-008/009 |
| T-028 | DUP-01 | 15 starych `post_type=produkt` równolegle do 19 WC | 🔴 teraz — znalezione 19.08 |
| T-029 | P1-7 | login admina `js` w schema na froncie | 🔴 teraz — bezpieczeństwo, 65 dni |
| T-030 | P0-2b | brak LocalBusiness dla Niedomic i Radgoszczy | 🔴 wrzesień |
| **T-048** | **GEO-01** | **geoblok odcina Lighthouse/PSI — nie da się mierzyć wydajności** | 🔴 **teraz** |
| T-031 | P0-4 | LCP mobile — niemierzalny, dopóki stoi T-048 | 🔴 wrzesień, **po T-048** |
| T-032 | P0-3 | 301 dla `/kategoria-produktu/*` | 🔵 teraz — odblokowane od 18.08 |
| T-033 | P1-9 | zgody i pomiar GA4 | 🔵 do rozstrzygnięcia |
| T-034 | P0-5 | Premmerce DOM-XSS | 🔵 do rozstrzygnięcia |
| T-035…T-038 | C4–C7, E1–E3, D1–D4, HUB-VI | landingi organiczne, segmentowe, transport/B2B, hub-and-spoke | ⛔ **nie wykonywać** |
| T-039 | ADS-01 | poprawki kampanii Marka (0 zł przez 6 dni) | 🔴 teraz |
| T-040 | ADS-02 | czy wolno pisać „Nordkalk" w reklamach | 🟡 czeka na AGRIĘ |
| T-041 | OLX-01 | publikacja 200 ogłoszeń | 🟡 czeka — Premium kupuje AGRIA |
| T-042 | OLX-02 | poprawki treści od Kazimierza (18.08) | 🔴 teraz |
| T-043 | KAL-01 | weryfikacja mockupu przez Kazimierza | 🟡 czeka na AGRIĘ |
| T-044 | KAL-02 | wdrożenie modułu magnezowego | 🔴 po T-043 |
| T-045 | OFE-01 | ofertownik, etap zerowy | 🔴 wrzesień |
| T-046 | GBP-01 | optymalizacja wizytówki Tarnów | 🔴 teraz — obiecane na piśmie w M2 |
| T-047 | GBP-02 | odzysk wizytówek Niedomice i Radgoszcz | 🟡 czeka na dostęp |

**Kolejka „teraz" po przejściu mapy — 13 pozycji:** T-008, T-009, T-010, T-011, T-026, T-027,
T-028, T-029, T-032, T-039, T-042, T-046, **T-048**.

**T-048 (dawne GEO-01) dopisane po pełnym odczycie rejestru** — wypadło z pierwszej wersji mapy.
Waży więcej, niż wygląda: geoblok wdrożony 14.08 (`src/plugins/agria-by-auranet/security-geoblock.php`)
przy odrzuceniu zwraca `Content-Type: text/plain`, a whitelist `$good_bots` nie zawiera
`Chrome-Lighthouse` — więc PSI dostaje `NOT_HTML` i **cała mierzalność wydajności stoi**.
Fix to jedna linia, ale na produkcji, więc czeka na zgodę. Kolejność wymuszona: T-048 → pomiar → T-031.

## Konsekwencje

- `FAKTY_KLIENTA.md` cytuje stare ID w §3, §6 i §8 (`CEN-01`, `ADS-02`, `STR-06`, `OFE-01`) —
  do podmiany przy przebudowie rejestru.
- Dokumenty historyczne (audyty z maja i czerwca, `CATALOG_VS_WC_GAP.md`) zachowują stare ID.
  To zapis stanu z tamtego dnia, nie żywy wskaźnik — nie przepisujemy.
- Wzorzec: `~/projekty/victorini/docs/REJESTR.md` i `~/projekty/primaauto/docs/QUEUE.md`.

Poprzedni krok tego samego porządkowania: usunięcie `docs/MASTER_PROMPT.md` (commit `2109a2f`).
