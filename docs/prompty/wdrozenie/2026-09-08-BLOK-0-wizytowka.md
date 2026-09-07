# Blok 0, wątek wizytówki — Google Business Profile Tarnów

> **Kiedy:** 08–12.09.2026 · **Projekt:** `agria` · **Zakres:** ryczałt R
> **Obejmuje:** T-119 · T-120 · T-121 · T-122
> **Kontekst:** `docs/PLAN_WRZESIEN_2026.md` §4 · memory `project_agria_gbp`
>
> **Osobny wątek od produkcji WP, i to celowo: GBP nie ma cofnięcia zmiany.** `patch` nadpisuje pole
> i tyle — jedynym rollbackiem jest zrzut zrobiony wcześniej (`scripts/gbp_dump.py`).

---

## Dlaczego ten wątek ma pierwszeństwo przed niejedną robotą na stronie

Pomiar GBP Performance **01.06–05.09 (97 dni)**:

| metryka | wynik |
|---|---|
| wyświetlenia | **1 810**, w tym mobile search 1 353 (**75%**) |
| **kliknięcia „zadzwoń"** | **31** |
| prośby o trasę | **138** |
| kliknięcia w stronę | 15 |

**Kampania Google Ads za 1 158 zł dała w tym samym czasie jedno kliknięcie typu CALLS.**
Wizytówka za zero złotych dała trzydzieści jeden. To jest dziś najskuteczniejszy kanał kontaktowy
w całym projekcie i jednocześnie najbardziej zaniedbany.

⚠️ **Czego ten wątek NIE zrobi:** nie zbuduje ruchu z fraz lokalnych. Pomiar DFS 07.09:
`wapno tarnów`, `wapno nawozowe niedomice`, `wapno radgoszcz`, `wapno nawozowe w pobliżu` —
**wszystkie poniżej progu**; jedyne `nawozy tarnów` ma **10/mies**. Wartość leży w Mapach i w panelu
wiedzy, nie w SEO lokalnym. Nie obiecuj klientowi wzrostu z fraz miejskich.

---

## 0. Przed pierwszą zmianą

```
python3 scripts/gbp_dump.py tmp/gbp-tarnow-przed-blok0-$(date +%F).json
```

Zrzut obejmuje lokalizację, media, opinie i publikacje. **Bez niego nie zaczynaj** — to jedyny rollback.
Konto `accounts/111497772731899556217`, lokalizacja `locations/11686460679773422640`.
Zapis przez `scripts/gbp_patch.py` (istnieje, sprawdź jego `updateMask`, zanim wywołasz).

## 1. T-119 — atrybuty, dziś **zero ustawionych**

Odczyt 07.09: `attributes` zwraca pustą listę, choć kategoria „Dostawca nawozów" udostępnia komplet.
**Zakres rozstrzygnięty przez Janka 07.09: `has_delivery`, WhatsApp i link do kalkulatora.**
Reszty nie ustawiamy — atrybut niezgodny ze stanem jest gorszy niż jego brak:

| atrybut | dlaczego |
|---|---|
| `has_delivery` — **Dostawa** | AGRIA wozi własnym transportem całosamochodowym; to wprost odpowiada temu, jak firma działa |
| `url_whatsapp` | WhatsApp jest na stronie i w GA4 widać kliknięcia; na wizytówce nie istnieje |
| ~~`url_facebook`, `url_youtube`~~ | ❌ **NIE ustawiamy** — decyzja Janka 07.09 |
| `url_appointment` | ✅ **`/kalkulator-wapnowania/`** — decyzja Janka 07.09; to najlepiej klikana strona w serwisie (CTR 5,3%) |
| `has_onsite_parking`, `pay_*` | **poza zakresem tego wątku** — nie ustawiaj bez potwierdzenia stanu faktycznego |

⚠️ Atrybuty dostępności (wózki, pętla indukcyjna) **zostaw puste**, dopóki nikt nie potwierdzi stanu
faktycznego. To nie jest miejsce na optymistyczne założenia.

## 2. T-120 — obszar obsługi (`serviceArea`), dziś puste

Firma dowozi w promieniu ~150 km z magazynów w Niedomicach i Radgoszczy — to samo, co ustawiliśmy
jako zasięg kampanii 28.08. Pole `serviceArea` jest dokładnie na to.

⚠️ **Nie zamieniaj wizytówki na „firmę bez adresu"** (`business_type: CUSTOMER_LOCATION_ONLY`) —
AGRIA ma realną siedzibę pod Warsztatową 5 i ta pinezka daje 138 próśb o trasę. Chodzi o **dodanie**
obszaru obsługi obok adresu, nie o zastąpienie adresu.

## 3. T-121 — publikacje, cisza od 20.08

Cztery ostatnie posty są z 20.08, wszystkie z CTA `LEARN_MORE`. Materiał na kolejne **już istnieje**
i nie trzeba go pisać od zera: kalkulator wapnowania (w tym nowy moduł magnezowy z 04.09),
komplet atestów i kart na `/do-pobrania/`, terminarz „kiedy wapnować", świeży opis kategorii
`/wapno-nawozowe-rolnictwo/` z 04.09, widełki cenowe `zł/t netto`.

Ustal **rytm tygodniowy** i pierwsze cztery tematy do akceptu Janka. Post ma prowadzić na konkretny
adres, nie na stronę główną. Pisz jak do rolnika — reguła „zero żargonu" obowiązuje (memory
`feedback_agria_bez_zargonu_loco`).

## 4. T-122 — opinie, najnowsza z **lutego 2025**

Dziewięć opinii, średnia **4,30**, wszystkie z odpowiedzią — obsługa jest w porządku, brakuje dopływu.
Dziewiętnaście miesięcy bez nowej opinii to sygnał dla Map i dla człowieka, który ją czyta.

**To nie jest zadanie techniczne, tylko proces po stronie AGRII.** Przygotuj:
- krótki link do wystawienia opinii (skrócony URL z profilu),
- dwa zdania, które Paweł albo Kazimierz mogą wysłać stałemu odbiorcy po dostawie,
- propozycję momentu w cyklu sprzedaży, w którym prośba ma sens.

Całość **do Janka**, on przekazuje. Nie kontaktujemy się z odbiorcami AGRII.

⚠️ Jedna opinia jest **jednogwiazdkowa z 2021** i ma już odpowiedź — nie ruszaj jej, nie odpisuj
drugi raz. Świeże opinie rozwodnią ją same.

⚠️ **Prośby o opinię kierujemy wyłącznie na wizytówkę Tarnów**, także po odzyskaniu oddziałów
(T-047 i T-124) — rozproszenie opinii między trzy pinezki to jedyne realne ryzyko tej architektury.

---

## 5. Czego w tym wątku nie robisz

- **Nie ruszasz oddziałów** — Niedomice i Radgoszcz nie są jeszcze pod naszym zarządem (T-047,
  czeka od 15.07). Architektura trzech wizytówek (T-124) to blok 3, po odzysku dostępu.
- **Nie wgrywasz zdjęć zastępczych.** Profil ma 10 kadrów z 02.07, żadnego produktu ani transportu,
  ale to są zdjęcia firmy na jej własnym profilu — materiał musi przyjść od AGRII (T-050).
- **Nie zmieniasz numeru telefonu ani godzin** — to T-123, blok 3, do rozstrzygnięcia razem
  z architekturą oddziałów. Dziś na wizytówce jest stacjonarny `14 621 88 21`, a w Ads rotujemy
  komórki Pawła i Kazimierza; **to jest świadoma niespójność do omówienia, nie błąd do naprawienia
  po cichu**.

## 6. Zrobione =

Zrzut „po" (`gbp_dump.py`) pokazuje ustawione atrybuty i obszar obsługi, pierwsza publikacja jest
opublikowana i widoczna na żywym profilu, a materiał do zbierania opinii leży u Janka do przekazania.
Wiersze T-119…T-122 w rejestrze zaktualizowane w tym samym commicie, z dowodem.
