# OLX — baseline pomiarowy i zasoby do wystawienia ogłoszeń

> Data: 2026-08-07, wieczór. Uzupełnia `OLX_INWENTARYZACJA_2026-08-07.md` (dostęp i stan konta)
> oraz `OLX_KONKURENCJA_2026-08-07.md` (rynek, wraz z korektą §3a).
> Cel: mieć na czym oprzeć prognozę zapytań, zanim cokolwiek wystawimy.

---

## 1. Baseline — zrobiony 07.08 o 17:52

`data/olx/snapshots/2026-08-07-1752.json`, narzędzie `scripts/olx/olx-snapshot`.

Stan wyjściowy AGRII: **19 ogłoszeń, 7 273 wyświetlenia, 209 odsłon telefonu, 1 wątek wiadomości.**

Snapshot **wyłącza prywatne ogłoszenie Pawła** (mieszkanie, kategoria 15) — ma 627 wyświetleń i 10 odsłon telefonu i zawyżyłoby każdy wskaźnik AGRII o ~8%. Liczby całościowe konta zostają w polu `totals_incl_private`.

Kolejny snapshot: **14.08**, potem co tydzień. `olx-snapshot --diff-last` liczy przyrost, tempo dobowe i przelicznik na ogłoszenie/miesiąc.

## 2. Dlaczego bez tego prognoza byłaby zmyślona

Partner API zwraca statystyki **kumulatywne od utworzenia ogłoszenia**, a ogłoszenia AGRII pochodzą z trzech różnych roczników. Po znormalizowaniu przez wiek:

| Utworzone | Ogłoszeń | Wyświetleń łącznie | wyśw./mies. na ogłoszenie | Odsłon tel. |
|---|---|---|---|---|
| 2023-08 (Tarnów × 2) | 2 | 2 969 | 41,6 | 55 |
| 2024-07 (Piotrków Tryb., „Do stawu") | 1 | 2 514 | 99,5 | 94 |
| 2025-07 (16 geo-duplikatów) | 16 | 1 790 | 8,6 | 60 |

**Ten przelicznik jest dolnym oszacowaniem, nie wskaźnikiem.** Dzielimy przez pełny wiek ogłoszenia, a ogłoszenia nie były cały czas aktywne — 17 z nich wygasło 18.07 i wcześniej też żyły tylko w oknach opłaconego pakietu. Rzeczywiste tempo w czasie ekspozycji jest wyższe, o nieznaną wielkość. Stąd rozstrzyga dopiero pomiar przyrostowy.

**Osobno: „intencja w tytule" tłumaczy mniej, niż zakładaliśmy.** Ogłoszenie „Do stawu" istnieje w dwóch egzemplarzach:

| Miasto | Utworzone | wyśw./mies. | Odsłon tel. |
|---|---|---|---|
| Piotrków Trybunalski | 2024-07 | 99,5 | 94 |
| Przemyśl | 2025-07 | 8,7 | 3 |

Ten sam tytuł, ta sama oferta, te same zdjęcia — **różnica 11×**. Więc na wynik pracuje coś jeszcze niż sam tytuł: staż ogłoszenia, ciągłość ekspozycji albo miasto. Nie wiemy które i **nie zgadujemy** — pomiar przyrostowy na jednorodnej partii to rozstrzygnie. Do tego czasu tytuł pod intencję traktujemy jako dobrą praktykę popartą jednym przypadkiem, nie jako pewnik z mnożnikiem.

## 3. Zasoby — czym dysponujemy bez dokupywania czegokolwiek

### Zdjęcia — kit jest gotowy i lepszy, niż zakładał prompt

Ogłoszenia mają po 8 zdjęć i to **komplet grafik brandowych zrobionych przez Auranet**: zdjęcia poglądowe frakcji z podpisami (Agrobielik 70 0–2, Agrobielik 90 0–3 i 2–8, Oxyfertil 90 3–8, węglanowe sypkie z/bez magnezu, węglanowe granulowane z/bez magnezu, kreda sypka i granulowana), plus realne zdjęcia palet z workami i big-bagów w magazynie, plus grafika otwierająca „WAPNA NAWOZOWE". Każda z logo Agria, hasłem „Stabilne parametry. Pewne dostawy. Od 1989 r." i **QR-kodem do kalkulatora wapnowania**.

Zdjęcia żyją na CDN OLX i ich URL-e wracają z API — **można je podpiąć pod nowe ogłoszenia bez ponownego uploadu**.

Czego w kicie nie ma: ujęć pod konkretne zastosowanie (staw, sad, oczyszczalnia) oraz grafik dla dolomitu, kredy pastewnej, kredy malarskiej, hydratyzowanego i palonego mielonego. Karty produktowe na stronie mają po 1–2 zdjęcia własne — na 8 slotów OLX to za mało.

### Parametry — wyciągane z produkcji, nie przepisywane

`scripts/olx/extract_specs.py` → `data/olx/product-specs.json`. Czyta **render** kart produktowych z agria.pl (nie bazę — parametry żyją w czterech warstwach i tylko render pokazuje to, co widzi klient), wyciąga tabelę „Specyfikacja techniczna", lead i zdjęcia. Komplet: 19 kart, 10–16 parametrów każda.

### QR na zdjęciach to jedyna działająca droga OLX → strona

W całej kategorii **5 ogłoszeń na 1 204 ma adres WWW w opisie**, a numery telefonu w opisie (19 na 1 204) sprzedawcy rozbijają gwiazdkami — tak samo robi obecny opis AGRII (`6*6*4*3*9*3*0*6*2`). To wygląda na obchodzenie filtra, nie na dozwoloną praktykę. **Regulamin trzeba przeczytać, zanim cokolwiek wpiszemy w opis** — Centrum Pomocy OLX jest za logowaniem, więc idzie to razem z sesją w panelu.

Konsekwencja dla pomiaru: link tekstowy odpada, **UTM wchodzi w QR-kod na grafikach**. Dziś QR prowadzi do `agria.pl/kalkulator-wapnowania/` bez parametrów, czyli ruch z OLX ląduje w GA4 jako bezpośredni i jest nie do odróżnienia.

## 4. Partner API — co działa, czego nie ma

| Endpoint | Stan |
|---|---|
| `GET /partner/adverts` | działa, zwraca też URL-e zdjęć i `auto_extend_enabled` |
| `GET /partner/adverts/{id}/statistics` | `advert_views`, `phone_views`, `users_observing` — kumulatywnie |
| `GET /partner/categories/{id}/attributes` | atrybuty kat. 4368: `state`, `bdo`, `delivery`; limit **8 zdjęć** |
| `GET /partner/threads` | działa — **1 wątek, 6 wiadomości, zero nieprzeczytanych** |
| `GET /partner/cities` \| `/regions` | 53 247 miast z lat/lon, 16 województw |
| pakiety / płatności / limity | **nie istnieją w API** — stan pakietu tylko z panelu |

**Wiadomości OLX to w tej kategorii kanał marginalny** — 1 wątek wobec 209 odsłon telefonu. Kontakt idzie telefonem i tak trzeba to mierzyć.

## 5. Cennik OLX — odczytany z panelu konta AGRII (07.08, wieczór)

### Co AGRIA kupowała

Panel → Pakiety: **pięć pakietów „Mega • 20 ogłoszeń"** w kategorii *Rolnictwo >> Produkty rolne, Giełda zwierząt, Pozostałe, Ryneczek, Nawozy…*, wygasłych **06.08.2025, 18.09.2025, 14.12.2025, 29.03.2026 i 18.07.2026**. Stan konta dziś: **0 zł, 0 punktów, pakiet zerowy.**

To domyka pytanie z inwentaryzacji: **17 ogłoszeń wygasło 18.07 z końcem 30-dniowej emisji ostatniego Megapakietu 20.** Pakiet jest ważny 30 dni od zakupu, każde ogłoszenie z pakietu — 30 dni.

I daje drugą, ważniejszą rzecz: **AGRIA kupowała pakiety pięć razy w ciągu trzynastu miesięcy, nieregularnie.** Ogłoszenia były więc na antenie mniej więcej **150 dni z 395** — mniej niż 40% czasu. Dlatego przelicznik „wyświetlenia ÷ wiek ogłoszenia" z §2 zaniża tempo o czynnik rzędu **2,5×**. To nie jest kanał, który „słabo działał" — to kanał włączany co jakiś czas.

### Cennik pakietów (brutto, płatność online, stan 07.08.2026)

| Liczba ogłoszeń | Start (Nawozy) | Premium (Nawozy) | Megapakiet |
|---|---|---|---|
| 5 | 53,99 | 65,99 | 95,99 |
| 10 | 95,99 | 119,99 | 179,99 |
| 20 | 179,99 | **227,99** | **335,99** ← *to kupowała AGRIA* |
| 50 | — | 443,99 | 719,99 |
| 100 | — | 719,99 | 1 319,99 |
| 200 | — | 1 199,99 | 2 399,99 |

Różnica między nimi: **Megapakiet pozwala wystawiać wymiennie w podkategoriach** (Nawozy, Produkty rolne, Worki, Zbiorniki, Środki ochrony roślin, Pozostałe rolnicze…), pakiety Start/Premium są przypisane do jednej. Premium dodaje 90 dni statystyk, jedno odświeżenie w 7. dniu emisji, wyróżnianie na stronie firmowej, banner i **link do zewnętrznej strony WWW**. Start ma WebApi i link do WWW, bez odświeżenia.

**Koszt jednostkowy to jest właśnie miejsce, gdzie AGRIA traci pieniądze:**

| Wariant | zł/ogłoszenie/30 dni |
|---|---|
| Megapakiet 20 (stan obecny) | **16,80** |
| Premium Nawozy 20 | 11,40 |
| Premium Nawozy 50 | 8,88 |
| Premium Nawozy 100 | 7,20 |
| Premium Nawozy 200 | **6,00** |

Za **te same 336 zł**, które AGRIA płaciła za 20 ogłoszeń w Megapakiecie, Pakiet Premium w kategorii Nawozy daje **około 40**. Warunek: wszystko musi mieścić się w Nawozach — a dziś jedno ogłoszenie (to aktywne, 1 272 wyświetlenia) siedzi w **Rolnictwo → Pozostałe**, nie w Nawozach. Do przeniesienia.

### Cennik promowania (ceny dynamiczne, odczytane na żywym ogłoszeniu 858802418)

| Usługa | Cena |
|---|---|
| Mini — wyróżnienie 3 dni | 13,08 zł |
| Midi — wyróżnienie 7 dni + odświeżenie 3× | 37,75 zł |
| **Maxi — wyróżnienie 30 dni + odświeżenie 9× + strona główna 7 dni** | **104,89 zł** |
| Wyróżnienie 7 dni (pojedynczo) | 15,73 zł |
| Odświeżenie 7× | 52,05 zł |
| Strona główna 7 dni | 62,44 zł |

OLX nie ma cennika promowań — to **ceny dynamiczne**, zmienne wraz z popytem, widoczne dopiero przy zakupie. Powyższe to zdjęcie z 07.08 dla jednego ogłoszenia; przy planowaniu trzeba je traktować jako rząd wielkości, nie stawkę.

### To rozstrzyga pytanie Pawła liczbowo

„30 ogłoszeń czy 10 + promowanie" — przy budżecie ~330 zł/mies.:

| Wariant | Co za to jest |
|---|---|
| 10 ogłoszeń + promowanie | Premium 10 (119,99) + 2× Maxi (209,78) = **329,77 zł → 10 ogłoszeń, 2 promowane** |
| wolumen | Premium 50 = **443,99 zł → 50 ogłoszeń** — albo Premium 20 (227,99) → **20 ogłoszeń i 100 zł zostaje** |

Jedno promowanie Maxi kosztuje tyle, co **dziewięć ogłoszeń** w Pakiecie Premium 100. Do tego dane rynkowe: dwaj najwięksi gracze w kategorii mają odpowiednio **zero** i 24 promowania przy 191 i 161 ogłoszeniach. **Wolumen, nie promowanie** — i to nie jest już opinia, tylko arytmetyka.

## 6. Regulamin — cztery rzeczy, które trzeba zmienić w treści

Regulamin Serwisu OLX.pl, pkt 4 „Zasady publikacji Ogłoszeń":

1. **Geo-multiplikacja jest wprost dozwolona.** *„Ten sam Przedmiot może być w danym czasie objęty więcej niż jednym Ogłoszeniem w kategoriach płatnych i limitowanych (…), pod warunkiem, że opublikowane Ogłoszenia różnią się lokalizacją, w tym dzielnicą oraz są dodane w ramach jednego Konta"*. Nawozy to kategoria płatna — model liderów jest legalny i możemy go powtórzyć bez ryzyka.

2. **Numer telefonu w treści jest zabroniony.** *„w treści Ogłoszenia nie można wskazywać danych kontaktowych, dane takie mogą zostać podane wyłącznie we wskazanych w tym celu polach formularza"*. Wszystkie obecne opisy AGRII kończą się `6*6*4*3*9*3*0*6*2` — rozbicie gwiazdkami to obchodzenie filtra, nie zgodność. **Wypada z nowych treści.** Telefon i tak jest w polu kontaktowym i to on generuje te 209 odsłon.

3. **Jedno ogłoszenie = jeden przedmiot.** Obecny opis wymienia w jednym ogłoszeniu wapno tlenkowe 70 i 90, węglanowe, węglanowo-magnezowe, kredę **i „nawozy sztuczne"**. Łamie to regulamin, rozmywa dopasowanie do wyszukiwania — a „nawozy sztuczne" są dodatkowo **poza zakresem produktowym AGRII** (`docs/MASTER_PROMPT.md`). Rozbicie na produkty jest tu jednocześnie wymogiem formalnym i lepszym marketingiem.

4. **Adres WWW — droga jest, ale nie w opisie.** Zakaz z regulaminu dotyczy odnośników *„prowadzących Użytkowników do serwisów świadczących takie same lub podobne usługi jak Grupa OLX"*, czyli konkurencyjnych serwisów ogłoszeniowych; agria.pl nim nie jest. Sformułowanie jest jednak na tyle szerokie, że **nie warto tego testować w opisie**. Bezpieczna droga jest jawna: **„Link do zewnętrznej strony WWW" to funkcja pakietu** (Start i Premium) — link z UTM idzie na **Stronę firmową OLX**.

   Zastrzeżenie do QR-kodu na grafikach: regulamin mówi wprost, że *„Treść Ogłoszenia stanowią również dodane w ramach niego zdjęcia oraz tytuł"* — więc QR formalnie jest treścią ogłoszenia. Chodzi tam od roku bez interwencji OLX, ale to jest tolerancja, nie zgoda. Zostawiamy, dokładając UTM, i nie budujemy na nim jedynej ścieżki pomiaru.
