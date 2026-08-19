# T-046 — optymalizacja profilu Google Business Profile: Tarnów

| | |
|---|---|
| **Linia / zakres** | GBP · **R** |
| **Status** | 🔴 teraz — **obiecane klientowi na piśmie** w raporcie M2 jako zadanie sierpnia |
| **Profil** | `locations/11686460679773422640`, konto `accounts/111497772731899556217` |
| **Szacunek** | 2–3 h |

---

## 1. Czego to dotyka

Profil firmy w Google Maps i w wynikach lokalnych: opis, kategorie, zdjęcia, publikacje (posty),
odpowiedzi na opinie, adres strony. Pośrednio: ruch lokalny, sygnały NAP (nazwa/adres/telefon),
spójność z `LocalBusiness` w schema (**patrz `T-030`** — dane oddziałów).

## 2. Strefy kruche

1. **Zmiany w GBP nie mają undo.** API nie wersjonuje profilu. **Zrzut stanu do `tmp/` przed
   każdą zmianą** jest jedynym rollbackiem.
2. **Google weryfikuje zmiany ręcznie i potrafi zawiesić profil.** Zmiana nazwy, kategorii głównej
   albo adresu to najczęstsze powody. Nazwa jest dziś przeładowana słowami kluczowymi
   („AGRIA Sp. z o.o. - Wapno nawozowe, hydratyzowane, dolomit") — **nie prostuj jej bez decyzji
   Janka**: skrócenie do samej nazwy prawnej jest zgodne z wytycznymi, ale kosztuje widoczność
   na frazy, a zmiana nazwy jest właśnie tym, co uruchamia weryfikację.
3. **Oddziałów Niedomice i Radgoszcz na koncie NIE MA** (sprawdzone 19.08 — lista lokalizacji
   zawiera osiem pozycji, żadna z nich to oddział AGRII). To `T-047`. **W komunikacji do klienta
   temat multi-location przemilczeć.**
4. **Konto jest typu PERSONAL i `UNVERIFIED`** — to konto Jana Schenka, nie organizacja.
   Nie próbuj migrować profilu ani zmieniać właściciela.
5. **`websiteUri` to dziś `http://www.agria.pl/`** — HTTP i `www`, podczas gdy strona stoi
   na `https://agria.pl/`. Drobiazg, ale to jest realne przekierowanie na starcie dla każdego
   kliknięcia z Map.
6. **Opis już istnieje i jest merytoryczny** — nie przepisuj go dla samego przepisania.
   Uzupełnij, jeśli czegoś brakuje.
7. **Odpowiedzi na opinie są publiczne i sygnowane firmą.** Draft każdej odpowiedzi idzie do Janka,
   nie publikujesz od ręki. Zero marketingowej nowomowy, ton zgodny z resztą komunikacji AGRII.

## 3. Stan zmierzony 19.08.2026 (GBP API)

```
title:        AGRIA Sp. z o.o. - Wapno nawozowe, hydratyzowane, dolomit
kategoria gł.: Dostawca nawozów
kategorie dod.: Hurtownia produktów rolnych · Dostawca środków chemicznych dla rolnictwa
                · Dostawca materiałów budowlanych
websiteUri:   http://www.agria.pl/            ← HTTP + www
telefon:      14 621 88 21
opis:         jest, merytoryczny (rodzinna firma z Tarnowa, od 1989, surowce wapniowe, B2B)
godziny:      pon–?, 8:00–16:00
openInfo:     OPEN, hasVoiceOfMerchant: true
ZDJĘCIA:      10
PUBLIKACJE:   0        ← główna luka
OPINIE:       9, średnia 4,3
```

## 4. Warunki wejścia

- [ ] Zrzut pełnego stanu profilu + media + opinie do `tmp/gbp-tarnow-<data>.json`.
- [ ] Zgoda Janka na zakres zmian (co dokładnie idzie do Google).

## 5. Co robisz

1. Zrzut stanu (`locations/…?readMask=…`, `/media`, `/reviews`) do `tmp/`.
2. **`websiteUri` → `https://agria.pl/`** — najtańsza zmiana o realnym skutku.
3. **Publikacje** — to jest właściwa treść tego taska. Zaproponuj Jankowi 4 posty na resztę M3
   i wrzesień: sezon wapnowania pożniwnego, dostępność produktów, atesty na stronie
   (spina się z T-008), kalkulator wapnowania. **Bez cen**, dopóki T-010 nie jest na stronie.
4. **Zdjęcia** — sprawdź, co jest w tych 10 pozycjach. Jeśli brakuje: siedziba, magazyn, transport,
   produkt w big-bagu — zgłoś Jankowi zapotrzebowanie, nie generuj zastępników.
5. **Opinie** — 9 opinii, sprawdź, ile ma odpowiedzi. Drafty odpowiedzi na te bez → do Janka.
6. Kategorie: przejrzyj, czy któraś nie jest martwa. **Nie dodawaj na zapas** — kategorie
   rozmywają dopasowanie.

## 6. Jak sprawdzasz w trakcie

Po każdej zmianie odczyt tego samego pola z API — GBP potrafi przyjąć żądanie i nie zastosować
zmiany (moderacja). Pole musi wrócić zmienione, inaczej czekasz, a nie powtarzasz.

## 7. Jak testujesz

```bash
# stan po zmianach — te same wywołania co w §3
# publikacje: localPosts musi zwrócić N > 0 z 'state': 'LIVE'
# websiteUri: https://agria.pl/
```
Test zewnętrzny: profil otwarty przez Chrome MCP w Mapach — czy posty są widoczne publicznie
(moderacja Google potrafi je trzymać w kolejce).

## 8. Dowód do rejestru

Zrzut przed/po dla zmienionych pól, ID i stan opublikowanych postów, liczba odpowiedzi na opinie,
zrzut ekranu profilu z Chrome MCP.

## 9. Rollback

Zrzut z kroku 1. Posty można usunąć (`localPosts.delete`), zmiany pól przywraca się kolejnym
`patch`-em — ale każda taka operacja to kolejny cykl moderacji, więc lepiej nie strzelać na próbę.

## 10. Rozliczenie

Zakres **R**. DZIENNIK M3, linia GBP. To pozycja **obiecana klientowi na piśmie** — jeśli
do 31.08 nie będzie zrobiona, musi trafić do raportu M3 jako jawnie przesunięta, nie przemilczana.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+24 h** | czy Google zatwierdził zmiany (`readMask` na zmienionych polach) |
| **+7 dni** | czy posty są `LIVE` i czy profil nie dostał ostrzeżenia |
| **+30 dni** | statystyki profilu: wyświetlenia, kliknięcia w telefon, trasy — porównanie z okresem sprzed |
| **przy T-047** | gdy oddziały wrócą pod kontrolę, spójność NAP między trzema profilami i schema |
