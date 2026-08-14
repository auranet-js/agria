# ADR 2026-08-13 — uruchomienie kampanii Google Ads

**Status:** wykonane 13.08.2026 · kampanie ENABLED i serwują
**Konto:** 674-207-1446 (AGRIA, direct, PLN, Europe/Warsaw)
**Poprzednie ustalenia:** `docs/ads/SETUP_KAMPANII_2026-08.md` (plan z 11.08), `2026-08-11-podzial-rol-ads-seo.md` (role kanałów)
**Odtworzenie:** `scripts/google/ads_build_campaigns.py` (struktura), `scripts/google/ads_teksty_dostawca.py` (teksty i wykluczenia)

---

## Co stoi na koncie

| Kampania | Budżet | Strategia | Grupy |
|---|---|---|---|
| AGRIA - Rolnictwo | 34 zł/dz | MANUAL_CPC | Wapno granulowane (2,00 zł) · Wapno nawozowe (2,50) · Wapno magnezowe i kreda (1,00) |
| AGRIA - Marka | 6 zł/dz | MANUAL_CPC | Brand (0,50 zł) |

Sieć wyszukiwania bez partnerów i bez display. Polska w trybie **obecność** (nie „obecność lub zainteresowanie"). Język polski. 24/7 bez day-partingu. 34 słowa kluczowe w dopasowaniu do wyrażenia i ścisłym, zero przybliżonego. 38 wykluczeń na kampanii rolniczej plus lista współdzielona na koncie.

---

## Decyzje i ich uzasadnienie

### 1. MANUAL_CPC zamiast Maksymalizacji kliknięć

Plan z 11.08 przewidywał Maks. kliknięć. **Zmienione po audycie portfolio Auranet:** Victorini, PrimaAuto, ASEO, PMP Fibertech i Rzeczoznawca — wszystkie stoją na MANUAL_CPC. Maks. kliknięć nie używa nikt.

Powód merytoryczny: ta strategia optymalizuje pod liczbę kliknięć w budżecie, czyli szuka najtańszych. Najtańsze kliknięcia w naszej kategorii to długi ogon i zapytania przypadkowe — dokładnie ruch, który odsiewamy.

**Maksymalizacja konwersji odrzucona na teraz**, mimo że kusi. Google zaleca ~30 konwersji w 30 dniach jako minimum; mamy zero. Algorytm zgadywałby na pustej próbce. Wracamy do tematu po miesiącu, gdy konwersje z połączeń nazbierają dane.

**Ważne rozróżnienie, które padło w dyskusji:** Smart Bidding nie buduje modelu „kim jest ten reklamodawca". Uczy się korelacji sygnał→konwersja na konkretnym koncie. Kontekstu „jesteśmy dostawcą, nie sklepem" Google uczy się z **treści landingu, słów kluczowych i wykluczeń**, niezależnie od strategii stawek.

Stawki wyliczone z CPC DataForSEO (granulowane 0,48 USD, nawozowe 0,62, magnezowe 0,16), nie ustawione ryczałtem.

### 2. Konwersja z połączeń + dwa numery w rotacji

Utworzona akcja **„Połączenia z reklam (30s+)"** — typ `AD_CALL`, kategoria `PHONE_CALL_LEAD`, primary, próg 30 sekund, ONE_PER_CLICK.

Numery: **664 393 062 (Paweł)** i **781 875 411 (Kazimierz)**, oba jako zasoby konta, harmonogram pn–pt 8:00–16:00, oba z podpiętą powyższą konwersją.

**Dlaczego rotacja, a nie przypisanie per kampania:** decyzja Janka — Google ma sam dobierać numer. Warunek, bez którego to nie działa: Google nie wie, czy ktoś odebrał telefon, dopóki połączenie nie idzie przez **numer przekierowania Google**. Dopiero wtedy nieodebrane połączenie nie liczy się jako konwersja i algorytm zaczyna preferować numer, który realnie odbiera. Stąd kolejność: najpierw konwersja z połączeń, potem rotacja.

To zamyka problem opisany przy godzinach pracy: `phone_click` liczy kliknięcie w numer, `PHONE_CALL_LEAD` liczy rozmowę.

Stary numer **604 428 782** zdjęty z reklam. Na stronie schodzi na `/kontakt/` (decyzja Janka), header i stopka dostają numer Pawła.

### 3. Pozycjonowanie: dostawca całosamochodowy, nie sklep

**Decyzja Janka 13.08:** AGRIA ma być czytana jako dostawca surowca z dostawami w całej Polsce, nie sklep online z workami wapna.

Skutki w tekstach — z nagłówków wypadły opakowania (`Luz, big-bag, worek 25 kg`, `Wapno granulowane hurt`), weszły skala i zasięg: `Dostawy całosamochodowe`, `Dostawy w całej Polsce`, `Własna flota – cała Polska`, `Dostawca wapna od 1989 r.`. Opis wiodący: *„Dostawca wapna nawozowego od 1989 r. Dostawy całosamochodowe w całej Polsce."*

Objaśnienie `Luz, big-bag, worki` → **`Dostawy całosamochodowe`**.

**Nigdzie nie ma progu ilościowego.** Komunikujemy skalę, nie minimum zamówienia — zgodnie z prośbą Pawła przy STR-02 („czasami nawet małe ilości możemy wysyłać, a taki zapis nas ogranicza"). Ta sama logika co przy cenach: skala odsiewa hobbystę sama z siebie, bez zamykania drzwi.

### 4. Wykluczenia — 38, w tym trzy własne produkty

Dołożone przeciw detalowi: `worek`, `worki`, `w workach`, `25 kg`, `20 kg`, `10 kg`, `sklep`, `sklep internetowy`, `kup online`, `wysyłka kurierem`, `paczka`, `cena za worek`.

**Wykluczone świadomie trzy produkty z oferty:**

| Wykluczenie | Produkt | Powód |
|---|---|---|
| `pastewna` | kreda pastewna (190 zł/t) | popyt płaski cały rok — rotacja pozasezonowa, nie temat na sierpniowy szczyt |
| `gaszone` | wapno hydratyzowane Bielik (945 zł/t) | budowlanka detaliczna |
| `malarska` | kreda malarska (645 zł/t) | jw. |

Do odzyskania w każdej chwili — zdjąć wykluczenie i dołożyć słowa. Ceny od Pawła są.

**Błąd wychwycony przez Janka:** `gdzie kupić` zostało wykluczone i **usunięte tego samego dnia**. To fraza zakupowa, nie detaliczna — pytający „gdzie kupić wapno nawozowe" szuka dostawcy, czyli jest naszym klientem.

`sklep` zostawiony mimo dyskusyjności: odsiewa detalistę, ale przy dopasowaniu do wyrażenia złapie też „sklep rolniczy hurt".

### 5. Landingi opublikowane poza indeksem

`/wapno-granulowane/` (post 2751) dostał treść — do 13.08 miał **zero bajtów** mimo zapisu w dokumentacji, że jest „opublikowany 06.08". `/wapno-nawozowe/` (post 2757) utworzony od zera; wcześniej adres zwracał 301 na poradnik o trawniku, czyli stronę wykluczaną słowem `trawnik`.

Oba: **`noindex, follow`** — domknięcie luki z ADR 11.08, gdzie izolacja opierała się wyłącznie na tym, że Google nie odkrył adresów. Od startu kampanii adresy stają się publiczne, więc brak dyrektywy przestał wystarczać.

Duplikat GTM usunięty (snippety Elementora 2711 i 2712 → `draft`), na stronie jest jeden kontener.

---

## Gotchas Google Ads API v25 — do zapamiętania

| Problem | Rozwiązanie |
|---|---|
| `campaign.start_date` **nie istnieje** w v25 | Google usunęło pole. Kampania startuje w momencie utworzenia; datę kontroluje się statusem |
| `containsEuPoliticalAdvertising` wymagane | Od 2025, rozporządzenie UE. Wartość: `DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING` |
| `updateMask: "manual_cpc"` odrzucone | Maska musi wskazywać subpole: `manual_cpc.enhanced_cpc_enabled` |
| **Zasób ≠ powiązanie** | `assets:mutate` tworzy zasób, ale bez `customerAssets:mutate` on **nigdzie się nie wyświetla**. Sitelinki i objaśnienia wisiały niepodpięte — wykryte i naprawione 13.08 |
| RSA są niezmienialne | Zmiana tekstów = utworzenie nowej reklamy i usunięcie starej |

---

## Otwarte

1. **Godziny w harmonogramie połączeń** — ustawione 8–16 za stroną, Janek pamięta 7–15. Niepotwierdzone u Pawła.
2. **Numery na stronie** — header, stopka i landingi nadal ze starymi numerami.
3. **Wizytówka Google** — połączenie z Ads niewykonane. Portfolio ma: PrimaAuto 6 lokalizacji, Victorini 1, AGRIA zero.
4. **Grafiki** — AGRIA ma zero zasobów graficznych (Victorini 546, PrimaAuto 86). Kit z OLX **odpada w całości** — Google odrzuca obrazy z tekstem, logo i QR-kodem, a wszystkie grafiki z OLX mają wszystkie trzy.
5. **Objaśnienia strukturalne** — PrimaAuto ma 45, AGRIA zero.
