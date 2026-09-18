# Projekt przebudowy kampanii Google Ads — AGRIA

> **Data:** 2026-09-18 · **Konto:** 674-207-1446 · **Autor:** Auranet
> **Podstawa:** odczyt API v25 z 18.09 za okres **14.08–17.09** (pełne 5 tygodni emisji) + GA4 01–17.09
> **Budżet ramowy:** **1 200 zł netto/mies.** (zatwierdzony, ADR 2026-08-13) = **39,5 zł/dzień średnio**
> **Wykonanie: Janek, ręcznie na koncie.** Ten dokument jest projektem, nie zmianą.
>
> Zasada, z której wynika cały projekt: **przy 40 zł dziennie nie da się prowadzić pięciu grup
> na 82 frazach i jednocześnie mieć w którejkolwiek z nich wiarygodne dane.** Budżet musi stać
> tam, gdzie intencja jest najbliżej zamówienia, a reszta ma zniknąć albo czekać na swój sezon.

---

## 1. Stan dzisiejszy — zmierzony, nie z papierów

| | 14.08–17.09 |
|---|---|
| wydatek | **1 558,75 zł** (Rolnictwo 1 214,20 · Paszarstwo 260,36 · Marka 84,19) |
| kliknięcia | 906 · **CTR 11,3%** (mobile) |
| CPC średni | 1,72 zł |
| konwersje | **5** (3 w sierpniu, 2 we wrześniu) — wszystkie `phone_click` |
| **koszt konwersji** | **311,75 zł** |
| udział mobile | **90% kosztu** (1 408 zł z 1 558) |

Struktura: 3 kampanie, 5 grup, 82 frazy aktywne, wszystko **MANUAL_CPC** z wyłączonym eCPC,
sieć partnerska i display **wyłączone** (dobrze), geo **PRESENCE** (dobrze — płacimy za obecność,
nie za zainteresowanie).

**Reklamy nie są problemem.** CTR 11,3% przy siłach GOOD/AVERAGE, teksty niosą cenę za tonę,
tonaż i własną flotę. Zostają bez zmian treściowych — patrz §6.

---

## 2. Gdzie ucieka budżet — sześć pozycji, od największej

### W1. 84% kliknięć nie dociera do pomiaru — **~1 300 zł bez żadnej wiedzy**

**453 kliknięcia Ads we wrześniu wobec 74 sesji „Paid Search" w GA4 (16,3%).** Ten sam stosunek
zmierzono 07.09, więc to nie jest wypadek jednego tygodnia.

Sesje, które **docierają**, zachowują się dobrze: 49 z 66 zaangażowanych, średnio 126 s,
współczynnik odrzuceń 25,8%. Czyli ruch nie jest śmieciowy — coś odcina go po drodze.

Dwie hipotezy, **obie niezweryfikowane**, wykluczające się kosztowo:
- **(a) Ludzie odpadają przed załadowaniem.** 90% ruchu to mobile, a LCP strony głównej skacze
  **3,7 ↔ 7,6 s** (T-132). Jeśli tak — tracimy realnych klientów i każda złotówka w kampanii
  jest warta połowę.
- **(b) Nie mierzymy ich, ale dochodzą.** Consent denied bez CMP (memory `project_agria_ga4_consent_blocker`).
  Jeśli tak — kampania działa lepiej, niż widać, a problem jest sprawozdawczy.

⚠️ **Tego trzeba rozstrzygnąć przed skalowaniem czegokolwiek.** Pomiar rozstrzygający: licznik
żądań z parametrem `gclid` po stronie serwera wobec liczby kliknięć w Ads. Dostępu do logów
`/home/server371853/logs` nie mamy (katalog nieczytelny), więc licznik trzeba dołożyć w PHP
albo odczytać z beacona WP Rocket. **Robota na ok. godzinę, wartość: rozstrzyga, czy 1 300 zł
miesięcznie kupuje klientów, czy powietrze.**

### W2. Rolnictwo na trzech dniach przepłaca CPC

Harmonogram Rolnictwa to dziś **niedziela, poniedziałek, wtorek 6:00–22:00** przy 60 zł/dz.
Google dopuszcza dwukrotność dziennego budżetu, więc w dniu emisji schodzi **105–121 zł**.

| dni | CPC |
|---|---|
| nd / pn / wt (chodzi Rolnictwo) | **1,78–1,82 zł** |
| śr / czw / pt / sob (bez Rolnictwa) | **1,51–1,63 zł** |

Różnica ~15%. Przy 1 200 zł to **ok. 180 zł miesięcznie = ok. 100 kliknięć**, które dziś oddajemy
za nadganianie w trzech dniach. ⚠️ Zastrzeżenie: te dni różnią się też składem kampanii, więc
15% to górna granica efektu, nie pewnik — ale kierunek jest jednoznaczny.

### W3. Paszarstwo strzela po całej Polsce — **~104 zł z 260 zł poza obszarem dostawy**

Kampania ma geo ustawione na **cały kraj** (`geoTargetConstants/2616`). Wydatek:

| region | koszt | w zasięgu dostawy? |
|---|---|---|
| Warszawa | 40,53 zł | nie |
| mazowieckie | 26,06 zł | częściowo (Radom tak) |
| wielkopolskie | 22,41 zł | nie |
| dolnośląskie | 15,39 zł | nie |
| małopolskie + podkarpackie + śląskie + lubelskie | 93,66 zł | tak |

Kreda pastewna jedzie w workach 30 kg, big-bagach i luzem **własną flotą z dwóch magazynów
w Małopolsce**. Dostawa worków pod Poznań nie ma ekonomii. ⚠️ **Do potwierdzenia u Janka** —
patrz pytanie P2 w §8.

### W4. Kupujemy frazę, na której organik stoi na pozycji 2,0

**`wapno na pole`: 62,80 zł, 32 kliknięcia, QS 4, zero konwersji.** Hub `/wapnowanie-gleby/`
rankuje na tę frazę organicznie na **pozycji 2,0** (audyt 24.08, potwierdzone ADR-em).
Płacimy za ruch, który i tak mamy.

To samo dotyczy `kreda nawozowa` (72,11 zł, QS 3) — po T-092 kategoria wyszła na **pozycję 10,76**
z 22,96 i wciąż rośnie. Tu jeszcze nie jesteśmy w TOP3, więc fraza zostaje, ale w dopasowaniu
ścisłym i pod obserwacją.

### W5. Marka kupuje cudze intencje

**`agria` (dopasowanie szerokie): 31,21 zł, 37% budżetu kampanii Marka.** „Agria" to również
szwedzka marka maszyn i ubezpieczyciel zwierząt — te zapytania nie należą do nas.
Wartościowa część kampanii to nazwy produktowe: `agrobielik`, `bielik wapno`, `oxyfertil`,
`wapno bielik`, `agria wapno`, `agria tarnów` — razem 53 zł i to one mają sens.

### W6. Marki konkurencji w ogonie

124 hasła z jednym kliknięciem kosztowały **230,82 zł (22% wydatku)**. Ogon jest w większości
trafny (ceny, tonaże, big-bagi), ale siedzą w nim nazwy konkurentów, których lista wykluczeń
z 21.08 nie objęła: **morawica, orcal, agros wap, wapniak kornicki, siewierz, nordkalk, supermag,
unicalc, dolokorn, agromit, promyk, „wapna świętokrzyskie"** — ok. 20 zł w pięć tygodni,
ale rosnące wraz z zasięgiem dopasowań frazowych.

---

## 3. Projekt — trzy kampanie, osiem grup, 1 200 zł

### Podział budżetu

| kampania | dziennie | miesięcznie | udział | dlaczego tyle |
|---|---|---|---|---|
| **K1 Wapno rolnicze** | **24 zł** | 720 zł | 60% | rdzeń oferty, szczyt sezonu X, jedyne frazy z realnym tonażem |
| **K2 Kreda pastewna** | **10 zł** | 300 zł | 25% | najtańszy ruch na koncie (CPC 1,19 zł) i popyt płaski cały rok |
| **K3 Marka** | **2 zł** | 60 zł | 5% | obrona nazw własnych, nie pozyskanie |
| **rezerwa** | — | **120 zł** | 10% | szczyt października (`wapno magnezowe` X 3 600, `granulowane` X 8 100) |

**Razem 1 200 zł.** Rezerwa nie leży bezczynnie — wchodzi do K1 na dwa tygodnie szczytu
albo zostaje niewydana, jeśli W1 nie zostanie rozstrzygnięte.

### K1 — „AGRIA — Wapno rolnicze" (24 zł/dz)

**Geo:** bez zmian — dwa promienie 150 km (50.135/20.850 i 50.217/21.017), `PRESENCE`,
wykluczone miasta: Kraków, Nowy Sącz, Tarnów, Rzeszów, Kielce, Bielsko-Biała, Częstochowa, Katowice.
⚠️ **Nie zawężać promienia.** Dane OLX pokazały, że pierścień 60–120 km daje **0,270 kontaktu
na ogłoszenie wobec 0,065 w pierścieniu 0–60 km** — dalej od magazynu jest mniej konkurencji,
nie mniej klientów.

**Harmonogram:** **wszystkie siedem dni, 6:00–21:00** (dziś: trzy dni 6:00–22:00).
Powód w W2. Godzina 22 wypada — w oknie 21:00–22:00 zeszło 15,02 zł przy 12 kliknięciach
i zerowej szansie na odebrany telefon.

**Grupy — trzy, po intencji, nie po produkcie:**

| grupa | frazy (dopasowanie) | dlaczego |
|---|---|---|
| **G1 Cena i tonaż** | `[wapno nawozowe cena]` · `[wapno granulowane cena]` · `[cena wapna za tonę]` · `[wapno nawozowe cena za tonę]` · `[ile kosztuje wapno nawozowe]` · `[wapno big bag cena]` · `[wapno granulowane big bag cena]` · `[wapno luzem cena]` · `"wapno cena za tonę"` | **32,4% dotychczasowego wydatku i najwyższa intencja transakcyjna.** Kto pyta o cenę za tonę, kupuje tonami |
| **G2 Granulowane** | `[wapno granulowane]` · `[wapno nawozowe granulowane]` · `[wapno granulowane luzem]` · `"wapno granulowane big bag"` · `[kreda granulowana]` | **jedyna grupa z QS 7 i oceną strony docelowej `AVERAGE`** — reszta konta ma `BELOW_AVERAGE`. Tu Google nas nie karze |
| **G3 Magnezowe i tlenkowe** | `[wapno magnezowe]` · `[wapno z magnezem]` · `[wapno magnezowe granulowane]` · `[wapno tlenkowe]` · `[wapno węglanowe z magnezem]` | **szczyt październikowy: `wapno magnezowe` X 3 600, `wapno tlenkowe` X 1 000.** Dziś organik stoi na 43,6 i 20,4 — Ads jest tu jedyną drogą do widoczności w sezonie |

**Wycięte z K1:** `wapno na pole` (oba dopasowania, W4) · `wapno nawozowe` w dopasowaniu frazowym
(zostaje `[wapno nawozowe cena]` w G1 — samo „wapno nawozowe" to 48,17 zł na intencję informacyjną) ·
`wapno tlenkowe` w PHRASE (QS **1**, 33,38 zł — zostaje wersja ścisła w G3).

**Przejście z PHRASE na EXACT** na frazach rdzeniowych. To zawęzi wolumen — świadomie:
przy 24 zł/dz lepiej wygrywać 60% aukcji na frazach kupujących niż 15% na wszystkich.

### K2 — „AGRIA — Kreda pastewna" (10 zł/dz)

**Geo: zmiana z całej Polski na pięć województw** — małopolskie, podkarpackie, świętokrzyskie,
lubelskie, śląskie. To pokrywa się z obszarem obsługi wizytówki Google i z zasięgiem własnej floty.
Oszczędność ok. 40% dotychczasowego wydatku kampanii (W3).

**Harmonogram:** siedem dni 6:00–21:00 (dziś 6:00–22:00 — jedyna zmiana to ostatnia godzina).

| grupa | frazy | dlaczego |
|---|---|---|
| **G1 Kreda pastewna** | `[kreda pastewna]` · `[kreda pastewna cena]` · `[kreda paszowa]` · `[kreda pastewna hurt]` | rdzeń, 2 400/mies., popyt płaski przez cały rok |
| **G2 Drób** | `[kreda pastewna dla kur]` · `[kreda pastewna dla kur niosek]` · `[kreda dla kur]` · `[wapno dla kur niosek]` | **najtańszy ruch na koncie: CPC 1,19 zł przy 1 366 wyświetleniach.** Tu budżet pracuje najefektywniej |
| **G3 Bydło i trzoda** | `[kreda pastewna dla bydła]` · `[kreda pastewna dla trzody]` · `[węglan wapnia dla bydła]` | fermy = większy tonaż jednorazowy niż drób przydomowy |

⚠️ **Zastrzeżenie merytoryczne:** frazy z grupy G2 prowadzą w dużej części do zapytań o worek
dla kilku kur przydomowych, a my sprzedajemy tonami. Wysoki CTR i zero konwersji przy 260 zł
w pięć tygodni to może być właśnie to. **Rozstrzygnięcie: reklama musi mówić o tonażu w pierwszym
nagłówku** (już mówi) **i landing musi mieć próg minimalny widoczny nad zgięciem** — inaczej
kupujemy hobbystów. To zadanie po stronie treści, nie kampanii.

### K3 — „AGRIA — Marka" (2 zł/dz)

**Wycinamy `agria` w dopasowaniu szerokim.** Zostają: `[agria wapno]` · `[agria tarnów]` ·
`[agrobielik]` · `[bielik wapno]` · `[wapno bielik]` · `[oxyfertil]` · `[ekograncali]`.
**Geo: cała Polska** — nazwy własne broni się wszędzie, a koszt jest znikomy.
**Harmonogram:** bez zmian, siedem dni.

### Wykluczenia wspólne (lista negatywna na poziomie konta)

**Marki konkurencji do dopisania:** morawica · orcal · agros wap · wapniak kornicki · siewierz ·
nordkalk · supermag · unicalc · dolokorn · agromit · promyk · wapna świętokrzyskie · polcalc ·
kredomix · wapnopol.
⚠️ **`nordkalk` z zastrzeżeniem:** AGRIA jest autoryzowanym dystrybutorem Nordkalku (potwierdzenie
Janka 07.09), więc wykluczenie dotyczy **wyłącznie** zapytań o kontakt do producenta
(`nordkalk kontakt`, `nordkalk praca`, `nordkalk cennik`), nie o produkty.

**Intencje spoza oferty:** praca · wikipedia · forum · opinie · allegro · olx · castorama ·
leroy merlin · obi · praktiker · bielenie · dezynfekcja · zaprawa · tynk · wapno gaszone do budowy.

---

## 4. Czego świadomie NIE zmieniamy

| co | dlaczego |
|---|---|
| **MANUAL_CPC** | przy 5 konwersjach na 5 tygodni automat nie ma się czego uczyć. Wrócimy do tego przy 15–20 konwersjach miesięcznie, nie wcześniej |
| **Teksty reklam** | CTR 11,3% jest ponad dwukrotnością średniej branżowej. Problem leży za kliknięciem, nie przed |
| **Promienie 150 km** | dane OLX mówią, że dalej = lepiej (4× więcej kontaktów w pierścieniu 60–120 km) |
| **Wykluczenia ośmiu miast** | „dostawca całosamochodowy, nie sklep z workami" — to pozycjonowanie, nie oszczędność |
| **Sieć partnerska i display** | już wyłączone, i dobrze |
| **Strony docelowe** | to jest decyzja **D2**, nie kosmetyka — patrz §8 |

---

## 5. Czego ten projekt NIE naprawia

**Nie naprawia kosztu konwersji.** 311,75 zł za telefon zostanie 311,75 zł, jeśli 84% kliknięć
nadal będzie znikać między reklamą a stroną (W1). Przebudowa struktury kupuje **ok. 15% więcej
kliknięć za te same pieniądze** i zdejmuje ~100 zł miesięcznie z wydatku poza obszarem dostawy —
to jest realny, ale wtórny zysk.

**Kolejność ważności jest odwrotna do kolejności łatwości:**
1. rozstrzygnąć W1 (gdzie znikają kliknięcia),
2. rozstrzygnąć D2 (dokąd prowadzimy),
3. dopiero potem przebudować strukturę.

Jeśli mamy zrobić jedną rzecz w tym tygodniu — to pierwszą, nie trzecią.

---

## 6. Kolejność wdrożenia (wykonanie: Janek)

| # | krok | ryzyko | odwracalne? |
|---|---|---|---|
| 1 | Wykluczenia: marki konkurencji + intencje spoza oferty | zerowe | tak |
| 2 | K3 Marka: usunąć `agria` szerokie, dodać nazwy produktowe ścisłe | zerowe | tak |
| 3 | K2 Paszarstwo: geo z całej Polski na pięć województw | niskie | tak |
| 4 | K1 Rolnictwo: harmonogram 3 dni → 7 dni, budżet 60 → 24 zł/dz | **średnie** — zmienia rytm licytacji, efekt widać po 7–10 dniach | tak |
| 5 | K1: przebudowa grup (G1/G2/G3), wycięcie `wapno na pole` | **średnie** — reset historii na nowych grupach | nie w pełni |
| 6 | Rezerwa 120 zł do K1 na szczyt października | — | tak |

**Kroki 1–3 można zrobić od razu** — nic nie psują i nie resetują historii.
**Krok 4 rozdziela od kroku 5 co najmniej siedem dni**, inaczej nie da się powiedzieć, co zadziałało.
**Krok 5 przed 1.10**, żeby nowe grupy zdążyły zebrać dane przed szczytem.

---

## 7. Co mierzymy i kiedy

| termin | pomiar | próg sukcesu |
|---|---|---|
| **+7 dni po kroku 4** | CPC średni, udział w wyświetleniach, wydatek dzienny | CPC poniżej **1,65 zł**, wydatek równy 24 ±5 zł/dz |
| **+14 dni po kroku 5** | koszt per grupa, QS, ocena strony docelowej | G1 i G2 bez `BELOW_AVERAGE` na frazach rdzeniowych |
| **31.10 (T-107)** | trzy miesiące kampanii dla klienta | materiał do decyzji o kontynuacji |

⚠️ **Nie mierzymy konwersji tygodniowo.** Przy pięciu zdarzeniach na pięć tygodni każdy tygodniowy
odczyt jest szumem. Konwersje ocenia się na oknie miesięcznym, i to ostrożnie.

---

## 8. Pytania, które muszą paść przed wdrożeniem

**P1 — strony docelowe (to jest D2).** Dziś 543 zł z 749 zł (72%) prowadzi na dwa landingi Ads
`/wapno-granulowane/` i `/wapno-nawozowe/`, a nie na karty produktów przepisane w T-136.
Czy K1 ma zostać na landingach, czy przejść na karty v2? Karty mają świeższą treść i parametry
z kart producenta; landingi mają listing z cenami i są budowane pod kontakt. **Nikt tego nie mierzył.**

**P2 — zasięg sprzedaży kredy pastewnej.** Czy worki 30 kg i big-bagi jadą poza Małopolskę
i sąsiednie województwa? Od tego zależy, czy zawężenie geo w K2 oszczędza 100 zł, czy odcina klientów.

**P3 — co robimy z rezerwą 120 zł**, jeśli W1 nie zostanie rozstrzygnięte do końca września.
