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

### Ścieżka zakupu — zweryfikowana na żywo w panelu (11.08)

Panel → Pakiety → **Kup pakiet ogłoszeń** → kategoria **Rolnictwo** → z listy podkategorii **Nawozy**
→ ekran „Kup pakiet" z suwakiem liczby ogłoszeń i trzema wariantami. To nie jest teoria z Centrum
Pomocy, tylko przeklikana ścieżka na koncie AGRII (bez finalizacji zakupu).

Co pokazuje ekran przy **200 ogłoszeniach**:

| Wariant | Cena | Za ogłoszenie | Uwagi |
|---|---|---|---|
| Start | **niedostępny** | — | „Pakiet dostępny dla: 5, 10, 20 ogłoszeń" |
| **Premium** | **1 199,99 zł** | **6,00 zł** | 1× odświeżenie każdego ogłoszenia, 90 dni statystyk, logo i baner, ulepszona ministrona |
| Mega | 2 199,99 zł | 11,00 zł | 2× odświeżenie, poza tym to samo |

**Maksimum w jednym zakupie to 200 ogłoszeń** — suwak ma progi 5 / 10 / 20 / 50 / 100 / 200 i nic
wyżej. Wejście na 400 wymagałoby dwóch zakupów i **nadal nie wiemy, czy się sumują** — tego nie da
się sprawdzić inaczej niż kupując.

Korekta wobec Centrum Pomocy: podawało tam Megapakiet 200 za 2 399,99 zł, a w panelu jest
**2 199,99 zł**. Cena Premium 200 zgadza się co do grosza.

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

## 7. Pomiar po stronie strony — znaleziona przyczyna martwej analityki

Prompt kazał sprawdzić, czy w ogóle cokolwiek mierzymy, zanim zaczniemy mierzyć OLX. Sprawdziłem — **nie mierzymy**, i wiadomo dlaczego.

### Skala rozjazdu

| Okres | GA4 | GSC |
|---|---|---|
| lipiec 2026 | 148 sesji, z tego **5 z Organic Search** | **221 kliknięć** |
| 90 dni (10.05–07.08) | 206 sesji: 187 direct, 8 google/organic, 1 ecosia, 1 brave | — |

**Osiem sesji organicznych w trzy miesiące** wobec 221 kliknięć w samym lipcu. To nie jest przesunięta atrybucja — to brak pomiaru.

Przy okazji: `/kalkulator-wapnowania/`, czyli cel QR-kodu z ogłoszeń OLX, ma **5 odsłon w 90 dni**. Sesji ze źródłem zawierającym „olx" — **zero w dwunastu miesiącach**.

### Przyczyna

Kontener GTM-TDC85TQN jest wpięty na każdej stronie i **opublikowany** (wersja 4), tag „GA4 – Google Tag" odpala się na All Pages, wszystkie 9 tagów aktywne. Konfiguracja jest poprawna. Problem jest jedno piętro wyżej — w tagu „Consent Default Denied", który odpala się na Consent Initialization:

```js
gtag('consent', 'default', {
  'ad_storage': 'denied', 'ad_user_data': 'denied',
  'ad_personalization': 'denied', 'analytics_storage': 'denied',
  'wait_for_update': 500, 'region': ['EEA','PL']
});
```

To jest poprawne domyślne ustawienie Consent Mode v2. Brakuje drugiej połowy: **na agria.pl nie ma żadnego mechanizmu, który kiedykolwiek wywoła `gtag('consent','update', … granted)`.** W renderze nie ma banera zgody ani żadnego CMP — z wtyczek widoczne są wyłącznie Elementor, Elementor Pro i WooCommerce (GTM jest wpięty przez Elementor Custom Code, świadomie bez GTM4WP/Complianz).

Efekt: dla każdego odwiedzającego z Polski `analytics_storage` zostaje `denied` **na zawsze**. GA4 działa w trybie bezcookie'owych pingów — nie ma identyfikatora użytkownika, nie ma ciągłości sesji, nie ma na czym oprzeć atrybucji źródła. Stąd 90% „Direct" i stąd garść sesji zamiast setek.

### Co to znaczy dla OLX

**UTM-y w linkach zrobimy i mają sens** — parametry z adresu trafiają do pingu niezależnie od cookies, więc ruch z OLX będzie rozpoznawalny co do źródła. Ale będzie **mocno zaniżony ilościowo**, dopóki zgoda nie zacznie być udzielana.

Dlatego **głównym miernikiem kanału OLX zostają statystyki OLX** — `advert_views` i `phone_views` z Partner API, mierzone przyrostowo (§1). GA4 jest miernikiem pomocniczym i tak trzeba go opisać klientowi, zamiast obiecywać pomiar, którego dziś nie ma.

### To jest zadanie poza OLX

Wdrożenie CMP dotyczy całego projektu, nie tego wątku — bez niego nie mierzymy ani SEO, ani Ads, ani OLX. Jest to jednocześnie wymóg prawny (RODO/EAA), więc nie jest to wybór między „mierzyć" a „nie mierzyć", tylko między „mieć zgodę i mierzyć" a „nie mieć i nie mierzyć". **Do wpisania jako osobna pozycja w planie M3/M4** — tutaj tylko odnotowane, bo bez tego liczby w dokumencie dla AGRII byłyby obietnicą bez pokrycia.
