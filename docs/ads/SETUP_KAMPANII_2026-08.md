# Setup kampanii Google Ads — AGRIA, sierpień 2026

**Konto:** 674-207-1446 („AGRIA", direct, PLN, Europe/Warsaw, auto-tagging ON)
**Start:** 14.08.2026 · **Budżet:** 1 200 zł/mies. = 40 zł/dzień
**Podstawa:** plan wysłany klientowi 06.08 (`docs/offers/2026-08-PLAN_ADS_3MIES.md`) + ADR 11.08 (`docs/decyzje/2026-08-11-podzial-rol-ads-seo.md`)
**Status:** do akceptu Janka przed wysłaniem do API

---

## 0. Aktualizacja 13.08 — stan przed startem

| Element | Stan 11.08 | Stan 13.08 (zweryfikowany) |
|---|---|---|
| Rozliczenie na koncie Ads | ❌ blocker | ✅ konto `ENABLED`, API odpowiada |
| CMP / Consent Mode v2 | ❌ brak | ✅ Complianz włączony i skonfigurowany, `consent-mode: yes`, tryb zaawansowany. Test: po akceptacji wszystkie sygnały v2 (`ad_storage`, `ad_user_data`, `ad_personalization`) → `granted` |
| GTM | 1 kontener (Elementor) | ⚠️ **DWA kontenery** — Complianz wstrzykuje własny, snippety Elementora 2711/2712 nadal aktywne. Konwersje policzą się dwa razy. **Do wyłączenia przed startem** |
| Landing `/wapno-granulowane/` | „opublikowany 06.08" | ⛔ **PUSTY** — `post_content` ma 0 bajtów. Render: tytuł + breadcrumb, zero parametrów, zero CTA. Treść gotowa: `docs/seo/lp/wapno-granulowane.html` |
| Landing `/wapno-nawozowe/` | do publikacji | ⛔ nie istnieje, 301 na poradnik o trawniku. Treść gotowa: `docs/seo/lp/wapno-nawozowe.html` |
| Struktura kampanii | opis w tym dokumencie | ✅ wykonywalny builder `scripts/google/ads_build_campaigns.py` (`--dry-run` przechodzi, 20 operacji API, walidacja limitów OK) |

**Reklama na pustą stronę docelową to nie jest kwestia gorszego wyniku — to ryzyko odrzucenia reklam przez Google (polityka strony docelowej) i pewność wysokiego CPC.** Publikacja treści obu landingów jest warunkiem startu ważniejszym niż cokolwiek innego na tej liście.

### Trzy korekty merytoryczne wprowadzone do buildera

1. **Wykluczenia brandowe w kampanii Rolnictwo** (`agria`, `agrobielik`, `bielik`, `oxyfertil`, `ekograncali`) — bez nich kampania rolnicza przechwyci ruch brandowy po wyższym CPC i zafałszuje ocenę obu kampanii. W wersji z 11.08 tego nie było.
2. **Nagłówki zastosowaniowe** zamiast części nagłówków „producent / hurt" — wniosek z audytu OLX: to samo ogłoszenie z tytułem „Do stawu" zebrało 2 514 wyświetleń i 94 odsłony telefonu, wersje „Najtaniej!" po ~110 wyświetleń i ~3 telefony. Intencja w tytule bije komunikat cenowy.
3. **Harmonogram na rozszerzeniu połączeń** (pn–pt, godziny pracy) — `phone_click` liczy kliknięcie, nie rozmowę. Bez harmonogramu Smart Bidding po przełączeniu na Maksymalizację konwersji uczyłby się optymalizować pod telefony, których nikt nie odbiera. Kampania zostaje 24/7, przycisk „Zadzwoń" nie.
   ⚠️ **Godziny do potwierdzenia:** strona podaje 8:00–16:00 w trzech miejscach, Janek pamięta 7–15. Builder ma 8–16 za stroną.

## 1. Stan konta — co już zrobione

| Element | Status |
|---|---|
| Konto założone, widoczne dla API pod `js@auranet.com.pl` | ✅ |
| GA4 ↔ Ads zlinkowane (7 akcji konwersji zaimportowanych) | ✅ |
| `generate_lead` — ENABLED, **primary**, kategoria SUBMIT_LEAD_FORM | ✅ |
| `phone_click` — ENABLED, **primary** | ✅ |
| `form_submit`, `file_download` — ENABLED, pomocnicze | ✅ |
| `purchase`, `qualify_lead`, `close_convert_lead` — zostają HIDDEN (brak sprzedaży online) | ✅ |
| Helper `scripts/google/ads_call.sh` z CID | ✅ |
| **Rozliczenie na koncie** | ❌ **blocker Janka** |
| Landing `/wapno-nawozowe/` | ❌ do publikacji przed startem |

**Blocker:** zapytania o kampanie zwracają `CUSTOMER_NOT_ENABLED` — konto czeka na domknięcie płatności. Konwersje dało się skonfigurować mimo to, kampanii nie utworzymy.

**Znane ograniczenie:** `countingType` konwersji jest immutable dla akcji importowanych z GA4 (zostaje MANY_PER_CLICK zamiast ONE_PER_CLICK). Skutek: dwukrotne wysłanie formularza przez tego samego użytkownika policzy się jako dwie konwersje. Rozwiązanie — natywny tag konwersji Google Ads w GTM, do dołożenia razem z Complianz.

---

## 2. Struktura

Dwie kampanie, cztery grupy reklam. Podział budżetu 85/15 zgodnie z planem dla klienta.

```
Kampania „AGRIA — Rolnictwo"              34 zł/dzień
├── Wapno granulowane      → /wapno-granulowane/
├── Wapno nawozowe         → /wapno-nawozowe/
└── Wapno magnezowe i kreda→ /wapno-nawozowe/

Kampania „AGRIA — Marka"                   6 zł/dzień
└── Brand                  → /
```

### Ustawienia obu kampanii

| Parametr | Wartość | Dlaczego |
|---|---|---|
| Typ | Sieć wyszukiwania, **bez partnerów, bez display** | Kontrola jakości ruchu na starcie |
| Lokalizacja | Polska — **„obecność", nie „zainteresowanie"** | Bez tego płacimy za zagraniczne wyszukiwania o Polsce |
| Język | polski | |
| Harmonogram | **24/7, bez day-partingu** | Niedziela +42% na frazach transakcyjnych (GSC własne). Rolnik szuka po zejściu z pola |
| Strategia stawek | **Maksymalizacja kliknięć, limit CPC 2,00 zł** | Zero historii konwersji + pomiar zablokowany przez consent = Smart Bidding nie ma na czym się uczyć. Limit chroni przed przepałem |
| Urządzenia | bez modyfikatorów | Mobile to 70% wyświetleń wg GSC — nie ograniczamy |
| Rotacja reklam | optymalizacja | |

Po miesiącu i wdrożeniu CMP: przejście na „Maksymalizacja konwersji" albo tCPA, gdy uzbiera się ~30 konwersji.

---

## 3. Słowa kluczowe

Wszystkie w dopasowaniu **do wyrażenia** (phrase), głowy dodatkowo w **ścisłym** (exact). Bez dopasowania przybliżonego na start — przy 40 zł/dzień broad rozjeżdża budżet.

**Grupa „Wapno granulowane"** (fraza główna 9 900 wyszukań w sierpniu)
```
"wapno granulowane"          [wapno granulowane]
"wapno nawozowe granulowane" "wapno granulowane luzem"
"wapno granulowane big bag"  "granulat wapniowy"
"wapno węglanowe granulowane" "wapno tlenkowe granulowane"
"kreda granulowana"
```

**Grupa „Wapno nawozowe"**
```
"wapno nawozowe"             [wapno nawozowe]
"wapno rolnicze"             "wapno do gleby"
"wapno węglanowe"            "wapno tlenkowe"
"wapno nawozowe luzem"       "wapno pod orkę"
"wapno na pole"              "wapno do odkwaszania gleby"
```

**Grupa „Wapno magnezowe i kreda"**
```
"wapno magnezowe"            [wapno magnezowe]
"wapno z magnezem"           "wapno węglanowo-magnezowe"
"wapno magnezowe granulowane" "dolomit nawozowy"
"kreda nawozowa"
```

**Kampania „Marka"**
```
[agria]          "agria wapno"      "agria tarnów"
[agrobielik]     "agrobielik"       "bielik wapno"
"oxyfertil"      "ekograncali"
```

### Odstępstwo od promptu M3 — do Twojej decyzji

Prompt M3 przewidywał dołożenie long-tailu informacyjnego („ile wapna na hektar", „ile wapna na ha"). **Rekomenduję tego nie kupować.** Powody:

- Na te frazy mamy pozycje **7,9–9,0 organicznie** i realny ruch: 899 i 791 wyświetleń w ostatnich 28 dniach. Kupowalibyśmy to, co już dostajemy za darmo.
- „wapnowanie gleby" ma **najwyższy CPC w projekcie — 1,64 USD**, przy niskiej intencji zakupowej.
- Budżet 40 zł/dzień jest mały; każda złotówka wydana na frazę informacyjną to złotówka mniej na transakcyjną w szczycie sezonu.

Jeśli chcesz podwójnej obecności w SERP na te frazy — wracamy do tego we wrześniu, gdy będziemy znali realny CPC rdzenia.

---

## 4. Wykluczenia — to decyduje o rentowności

Odsiewamy hobbystę i budowlankę detaliczną, zostawiamy rolnika i instytucję. Lista na poziomie **kampanii** (obie).

```
trawnik · ogród · ogrodowy · działka · doniczka · kwiaty · rośliny doniczkowe
5 kg · 10 kg · basen · akwarium · bielenie drzew
budowlane · malarska · gaszone · do ścian · tynk · zaprawa
praca · oferty pracy · sprzedam · kupię · używane
olx · allegro · ceneo · leroy · castorama · obi · bricomarche
wikipedia · co to jest · wzór chemiczny · definicja
kury · drób · pastewna
```

Uzasadnienie trzech nieoczywistych pozycji:

- **`olx`, `allegro`, `ceneo`, `leroy`, `castorama`** — SERP z 11.08 pokazuje, że marketplace'y trzymają #1 na czterech z sześciu naszych fraz. Zapytania z ich nazwą to użytkownik, który już wybrał kanał; nie przepłacamy za przechwycenie.
- **`pastewna`, `kury`, `drób`** — kreda pastewna jest produktem AGRII, ale paszarstwo ma inny rytm sezonowy (popyt płaski cały rok) i w planie dla klienta zostało świadomie odłożone jako rotacja pozasezonowa. Nie mieszamy go z budżetem rolniczym w szczycie.
- **`/wapno-nawozowe-na-trawnik/`** — nasz własny poradnik uznany w backlogu za błąd kierunkowy. Reklamy nie kierujemy na niego nigdy.

---

## 5. Teksty reklam

Wszystkie zweryfikowane pod limity Google (nagłówek 30, opis 90). Zero przekroczeń.

### Grupa „Wapno granulowane" → `/wapno-granulowane/`

**Nagłówki:** Wapno granulowane luzem · Wapno granulowane – producent · Wapno nawozowe granulowane · Granulat wapniowy dla rolnika · Wapno granulowane od 1989 r. · Dostawa własną flotą 3–24 t · Luz, big-bag, worek 25 kg · Zapytaj o ofertę – podaj tonaż · Atesty i karty produktowe · Wapno granulowane Małopolska · Dwa magazyny, szybki załadunek · Wapno tlenkowe i węglanowe · 37 lat na rynku wapna · Wycena dla gospodarstw · Wapno granulowane hurt

**Opisy:**
1. Producent wapna od 1989 r. Granulat luzem, w big-bagach i workach. Zapytaj o ofertę.
2. Własna flota 3–24 t i dwa magazyny – dowozimy na termin, także przy większych tonażach.
3. Karty produktowe, atesty OSChR, klasy normowe. Wiesz dokładnie, co wjeżdża na pole.
4. Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą. Obsługa gospodarstw i hurtowni.

**Ścieżka:** `/wapno/granulowane`

### Grupa „Wapno nawozowe" → `/wapno-nawozowe/`

**Nagłówki:** Wapno nawozowe – producent · Wapno nawozowe luzem 24 t · Wapno węglanowe i tlenkowe · Wapno nawozowe dla rolnictwa · Odkwaszanie gleby – wapno · Zapytaj o ofertę – podaj tonaż · Wapno nawozowe od 1989 r. · Dostawa własną flotą · Atesty OSChR, karty techniczne · Big-bag 1000 kg lub luzem · Wapno nawozowe Małopolska · Agrobielik i Oxyfertil · Wycena dla gospodarstw · Rodzina, trzy pokolenia · Wapno nawozowe hurt

**Opisy:**
1. Wapno tlenkowe i węglanowe prosto od producenta. Luz, big-bag, worek. Zapytaj o ofertę.
2. Dobierzemy typ wapna do Twojej gleby i terminu zabiegu. Doradztwo w cenie dostawy.
3. Własna flota 3–24 t, dwa magazyny, terminy dopasowane do prac polowych.
4. Karty produktowe i atesty dostępne na stronie. Parametry zgodne z rozporządzeniem.

**Ścieżka:** `/wapno/nawozowe`

### Grupa „Wapno magnezowe i kreda" → `/wapno-nawozowe/`

**Nagłówki:** Wapno magnezowe granulowane · Wapno z magnezem – producent · Kreda nawozowa luzem · Dolomit i wapno magnezowe · Magnez i wapń w jednym zabiegu · Zapytaj o ofertę – podaj tonaż · Kreda nawozowa i pastewna · Dostawa własną flotą 3–24 t · Wapno magnezowe od 1989 r. · Atesty i karty produktowe · Big-bag 1000 kg lub luzem · Wapno magnezowe Małopolska · Wycena dla gospodarstw · 37 lat na rynku wapna · Kreda nawozowa hurt

**Opisy:**
1. Wapno magnezowe i kreda od producenta. Wapń i magnez w jednym zabiegu.
2. Luz 24 t, big-bag 1000 kg, worki. Dobór formy dostawy do wielkości gospodarstwa.
3. Karty produktowe z zawartością CaO i MgO. Atesty OSChR dla każdej partii.
4. Podaj tonaż i lokalizację – przygotujemy wycenę z dostawą własną flotą.

**Ścieżka:** `/wapno/magnezowe`

### Kampania „Marka" → `/`

**Nagłówki:** AGRIA – wapno nawozowe · AGRIA Sp. z o.o. Tarnów · Agrobielik – wapno tlenkowe · Bielik – wapno hydratyzowane · Oxyfertil w ofercie AGRIA · Producent od 1989 roku · Wapno i surowce wapniowe · Zapytaj o ofertę · Oficjalna strona AGRIA · EkoGranCali – granulat · Trzy pokolenia, 37 lat · Dwa magazyny w Małopolsce

**Opisy:**
1. Oficjalna strona AGRIA Sp. z o.o. Wapno nawozowe, budowlane i surowce wapniowe od 1989 r.
2. Agrobielik, Bielik, Oxyfertil, EkoGranCali – pełna oferta prosto od producenta.
3. Rodzinna firma z Tarnowa, trzy pokolenia w branży wapna. Własna flota i dwa magazyny.
4. Karty produktowe, atesty i kalkulator wapnowania dostępne na stronie.

**Ścieżka:** `/oferta`

### ⚠️ Do Twojego rozstrzygnięcia: formy dostawy w tekstach

Nagłówki i opisy używają sygnału logistycznego („luz 24 t", „big-bag 1000 kg", „własna flota 3–24 t"). **STR-02 z 29.06 zdjęła te informacje z 19 kart produktów** na prośbę Pawła — *„czasami nawet małe ilości możemy wysyłać, a taki zapis nas ogranicza"*.

W reklamach ten sygnał jest narzędziem odsiewu: odróżnia nas od sklepów detalicznych i przyciąga rolnika całopojazdowego. Sformułowania są **możliwościowe, nie wykluczające** („luz, big-bag, worek 25 kg" — trzy opcje, nie minimum zamówienia), więc nie cofają poprawki Pawła. Jeśli uznasz, że to jednak kolizja, wymieniam je na komunikaty o dostawie bez podawania form.

---

## 6. Rozszerzenia

**Objaśnienia:** Producent od 1989 roku · Własna flota 3–24 t · Dwa magazyny w Małopolsce · Atesty OSChR · Luz, big-bag, worki · Doradztwo w doborze wapna

**Linki do podstron:**

| Tytuł | Opis 1 | Opis 2 | URL |
|---|---|---|---|
| Kalkulator wapnowania | Policz dawkę na hektar | Bezpłatne narzędzie online | `/kalkulator-wapnowania/` |
| Karty produktowe | Parametry i atesty PDF | Wszystko do pobrania | `/do-pobrania/` |
| Wapnowanie gleby | Poradnik: kiedy i ile | Terminy i dawki wapna | `/wapnowanie-gleby/` |
| Kontakt | Zapytaj o ofertę | Telefon i formularz | `/kontakt/` |

**Rozszerzenie połączeń:** numer centrali Tarnów (wdrożony w STR-03), godziny biura.
**Rozszerzenie lokalizacji:** spięte z wizytówką Tarnów — wymaga połączenia konta Ads z profilem firmy.

Kalkulator jako link do podstrony to świadomy wybór: rankuje organicznie na pozycji 6,2 i jest naszym najmocniejszym narzędziem wciągającym rolnika w kontakt.

---

## 7. Czego ten setup nie rozwiązuje

**Pomiar konwersji nie zadziała bez CMP.** Consent Mode odmawia zgody dla PL, a na stronie nie ma banera — GA4 w lipcu zanotował 5 sesji organicznych przy 221 kliknięciach w GSC. Konwersje importowane z GA4 będą świecić zerem. Wdrożenie Complianz jest warunkiem tego, co obiecaliśmy klientowi w mailu: *„będzie dokładnie widać, ile kontaktów przyszło z reklamy"*.

**LCP mobile 7,4 s wpływa na koszt kliknięcia.** Ocena jakości strony docelowej to składowa Quality Score. Landing `/wapno-granulowane/` dziedziczy problem z obrazem hero. Do sprawdzenia przed startem — jeśli landing jest lekki, temat schodzi na dalszy plan.

---

## 8. Kolejność wykonania

| # | Zadanie | Kto | Termin |
|---|---|---|---|
| 1 | Domknięcie rozliczenia na koncie Ads | **Janek** | przed 13.08 |
| 2 | Publikacja `/wapno-nawozowe/` (poza indeksem, wg ADR) | Claude | 12.08 |
| 3 | Instalacja Complianz | **Janek** | 12–13.08 |
| 4 | Konfiguracja Complianz + Consent Mode + natywny tag konwersji Ads | Claude | po instalacji |
| 5 | Utworzenie kampanii przez API (ładunki gotowe) | Claude | 13.08 |
| 6 | Smoke test: podgląd reklam, linki docelowe, konwersja testowa, UTM | Claude | 14.08 |
| 7 | Start | — | **14.08** |
