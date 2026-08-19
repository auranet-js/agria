# Ads AGRIA, dzień 5 — dlaczego nie widać leadów (18.08.2026)

**Konto:** 674-207-1446 · **Okres:** 14–18.08.2026 (pięć pełnych dni) · **Analiza:** 19.08.2026 rano · **Wszystkie liczby z Google Ads API v25,
GA4 Data API, GSC API, GTM API i DataForSEO — zapytania odtwarzalne przez `scripts/google/ads_call.sh`.**

---

## Odpowiedź w jednym zdaniu

Leadów nie ma i **nie miało prawa ich być**: przez pięć dni kupiliśmy 100 kliknięć, a numer
telefonu — jedyny mierzony kanał kontaktu — pokazał się w **32 z 682 wyświetleń reklamy (4,7%)**
i na landingu leży dopiero na **79% wysokości strony**. To nie jest problem doboru fraz.

---

## 0. Pytanie zerowe — co jest zmierzone, a co nie

### Działa

| Co | Dowód |
|---|---|
| Akcja konwersji „Połączenia z reklam (30s+)" istnieje i jest aktywna | `conversion_action` id `7720746866`, `AD_CALL` / `PHONE_CALL_LEAD`, `ENABLED`, `primaryForGoal: true` |
| Oba numery podpięte do tej akcji | assety `407759148260` (+48 664 393 062) i `407857774603` (+48 781 875 411), oba `USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION` → `conversionActions/7720746866`, oba `APPROVED` i `ENABLED` w `customer_asset` |
| Ruch płatny **dociera** do GA4 z atrybucją | GA4 14–18.08: `google / cpc` = **41 sesji, 33 zaangażowane (80%)**. To koryguje wcześniejsze założenie z memory `project_agria_ga4_consent_blocker`, że Ads będzie niemierzalne — `url_passthrough` w GTM działa |
| GTM ma poprawnie skonfigurowany pomiar kliknięcia w telefon | wersja live 5, tag „GA4 Event - Phone Click" nie wstrzymany, trigger id 14: `{{Click URL}} startsWith tel:`. Linki na landingu to `href="tel:+48664393062"` — pasują |

### Nie działa / nie mierzy

| Co | Dowód | Skutek |
|---|---|---|
| **Numer telefonu prawie się nie wyświetla** | `metrics.phone_impressions`: 14.08 – 0, 15.08 – 0, 16.08 – 0, 17.08 – 21, 18.08 – 11. Razem **32 przy 682 wyświetleniach reklamy** | Harmonogram assetów połączeń to **pn–pt 8:00–16:00**, a kampania chodzi **6:00–22:00 przez 7 dni**. W sobotę i niedzielę — czyli w dni, które GSC wskazuje jako najmocniejsze — reklama nie pokazuje numeru w ogóle |
| Zero połączeń przez numer przekierowania Google | `call_view` — **zero rekordów**; `metrics.phone_calls` = 0 we wszystkie dni | Nie ma czego liczyć jako konwersję |
| Zero konwersji jakiegokolwiek typu | zapytanie `campaign` + `segments.conversion_action_name` za 13–18.08 zwraca **zero wierszy** | — |
| Zero zdarzeń klikowych w GA4 | zdarzenia 14–18.08: `scroll` 336, `user_engagement` 133, `page_view` 113, `session_start` 91, `first_visit` 90, `form_start` **1**. **Brak `phone_click`, `email_click`, `whatsapp_click`, `outbound_link`, `form_submit`** | Tag GTM działa (336 zdarzeń `scroll` to też tag GTM), więc najprawdopodobniej **nikt nie kliknął**. Ale wszystkie triggery klikowe naraz na zerze to wzorzec wart jednego ręcznego testu w DebugView, zanim uznamy to za fakt |
| Około 59% płatnych kliknięć nie ma sesji w GA4 | 100 kliknięć w Ads vs 41 sesji `google / cpc` | Brak CMP → część pingów bez ciągłości sesji. Ads-owe liczby są pełne, GA4-owe są dolnym oszacowaniem |

**Wniosek:** mierzalne są koszt, kliknięcia i zachowanie na stronie. Niemierzalne są telefony —
bo telefonu praktycznie nie było widać. „Zero leadów" to na dziś **fakt o naszej ekspozycji,
nie o rynku**.

---

## 1. Bilans pięciu dni

| Dzień | Wyśw. | Klik. | CTR | Śr. CPC | Koszt | Konw. |
|---|---|---|---|---|---|---|
| 14.08 pt | 184 | 18 | 9,8% | 2,14 zł | 38,45 zł | 0 |
| 15.08 sob | 99 | 19 | 19,2% | 1,97 zł | 37,41 zł | 0 |
| 16.08 niedz | 137 | 21 | 15,3% | 1,96 zł | 41,16 zł | 0 |
| 17.08 pon | 142 | 21 | 14,8% | 1,97 zł | 41,47 zł | 0 |
| 18.08 wt | 120 | 21 | 17,5% | 1,96 zł | 41,13 zł | 0 |
| **Razem** | **682** | **100** | **14,7%** | **2,00 zł** | **199,62 zł** | **0** |

Kampania **AGRIA - Marka: zero wyświetleń przez pięć dni, zero wydatku.**

Grupy reklam (14–18.08):

| Grupa | Wyśw. | Klik. | CTR | Koszt | Stawka |
|---|---|---|---|---|---|
| Wapno nawozowe | 446 | 66 | 14,8% | 133,32 zł | 2,00 zł |
| Wapno granulowane | 198 | 33 | 16,7% | 64,78 zł | 2,00 zł |
| Wapno magnezowe i kreda | 38 | 1 | 2,6% | 1,52 zł | 1,00 zł |

### Ile realnie wydajemy wobec 40 zł/dz

Średnio **39,92 zł dziennie** — budżet wyczerpuje się codziennie. Ale rozkłada się źle:
**Rolnictwo (budżet 34 zł) wydaje 37,41–41,47 zł**, czyli chodzi na nadwyżce, którą Google dopuszcza
w ramach miesięcznego limitu, a **Marka (6 zł) nie wydaje nic**. Miesięczny sufit Rolnictwa
to 34 × 30,4 = **1 034 zł**, a nie 1 200 zł z planu — **166 zł budżetu klienta miesięcznie
nie ma jak się wydać**.

### O której gaśnie emisja

| Dzień | Ostatnia godzina z wyświetleniami |
|---|---|
| 15.08 sob | 21:00 |
| 16.08 niedz | 20:00 |
| 17.08 pon | **15:00** |
| 18.08 wt | 20:00 |

W poniedziałek reklama zniknęła o 15:00 — siedem godzin okna 6–22 bez emisji, w tym całe
popołudnie i wieczór. Harmonogram 6–22 z ADR 14.08 stoi poprawnie (potwierdzone w `campaign_criterion`,
7 dni × 6–22 na obu kampaniach), ale **budżet nie dociąga do jego końca**.

### Ile rynku bierzemy

`search_impression_share` dla Rolnictwa: **~10%**, z czego **>90% utracone przez budżet**
i tylko 2,7% przez ranking. Bierzemy jedną dziesiątą sierpniowego popytu, a wąskim gardłem
są pieniądze, nie jakość kampanii.

Dla Marki odwrotnie: **0% utracone przez budżet, >90% przez ranking** — aukcje na te frazy
istnieją, ale przy stawce 0,50 zł nie wchodzimy do nich w ogóle.

---

## 2. Na co realnie płacimy — search terms

Raport `search_term_view` pokrywa **69 z 100 kliknięć i 137,24 z 199,62 zł** (69%) — reszta
jest ukryta progiem prywatności Google. 223 unikalne zapytania.

| Koszyk | Wyśw. | Klik. | Koszt | % kosztu |
|---|---|---|---|---|
| **Ogólne produktowe** (wapno granulowane, wapno nawozowe, wapno na pole…) | 201 | 27 | 53,53 zł | **39,0%** |
| **(a) Zakupowe** — cena, tona, luz, big bag, sprzedaż | 78 | 23 | 44,87 zł | **32,7%** |
| **(c2) Obce marki i kopalnie** | 96 | 10 | 20,76 zł | **15,1%** |
| **(b) Edukacyjne** | 23 | 4 | 8,24 zł | **6,0%** |
| **(c1) Nordkalk** (nasz surowiec, nie „cudza marka") | 14 | 4 | 7,88 zł | 5,7% |
| **(d) Detal / ogród** | 33 | 1 | 1,96 zł | 1,4% |

### Hipoteza „płacimy głównie za koszyk edukacyjny" — nieprawdziwa

Edukacja to **6,0% kosztu, 8,24 zł przez pięć dni**, i to po korekcie wykluczeń z 14.08.
Realnie 72% pieniędzy idzie na zapytania zakupowe i ogólnoproduktowe. Trzy zapytania
edukacyjne, które weszły (`jakie wapno na zakwaszoną glebę`, `ile wapna sypkiego na ha`,
`co daje wapnowanie pola`), są warte 8 zł — nie tłumaczą braku telefonów.

**Za to 33% kosztu to wprost zapytania cenowe** — `wapno granulowane cena` (15,64 zł, 8 klików,
najdroższe zapytanie okresu), `cena wapna granulowanego`, `ile kosztuje tona wapna granulowanego`,
`wapno nawozowe cena za tonę`. **A na obu landingach nie ma ani jednej ceny.** To jest punkt 2
z listy otwartych ADR 14.08, nadal otwarty, i dziś kosztuje najwięcej.

### Koszyk (c) — decyzja handlowa

Rozdzielam go na dwa, bo **Nordkalk to producent naszego surowca, a nie konkurent**
(MASTER_PROMPT: Nordkalk/Sitkówka, Trzuskawica). `wapno nordkalk luzem cena` i
`wapno węglanowe nordkalk` (7,88 zł) to zapytania o **nasz towar** — zostają.

Obce marki i kopalnie kosztowały **20,76 zł przez pięć dni ≈ 125 zł miesięcznie ≈ 10% budżetu**:

| Zapytanie | Klik. | Koszt |
|---|---|---|
| wapno granulowane polcalc 500kg cena | 3 | 5,84 zł |
| wapno morawica cena | 1 | 2,50 zł |
| wapno orcal cena | 1 | 2,49 zł |
| orcal granulowany cena | 1 | 2,00 zł |
| wapno siewierz cena | 1 | 2,00 zł |
| unicalc | 1 | 1,99 zł |
| wapno promyk | 1 | 1,98 zł |
| complexor turbo cena | 1 | 1,96 zł |

**Rekomendacja: wykluczamy same nazwy, zostawiamy „marka + cena".** Kto wpisuje `unicalc`
albo `wapno promyk`, ma dostawcę i szuka jego karty produktu — płacimy za cudzy katalog.
Kto wpisuje `wapno orcal cena` albo `wapno morawica cena`, **porównuje ofertę** — to jest
zmiana dostawcy, czyli nasz klient. Ta sama logika, którą przyjęliśmy 14.08.

Do wykluczenia (dopasowanie do wyrażenia): `unicalc`, `promyk`, `atrigran`, `radkowit`,
`kujawit`, `jurak`, `dobromir`, `inovit`, `kornicki`, `kornica`, `omya`, `grankal`, `dewonit`,
`agrodol`, `agrolok`, `humicalc`, `complexor`, `magnesia calc`, `józefka`, `koszelowskie`,
`drugnia`, `działoszyn`. Przy 90% udziału traconego przez budżet każda złotówka wydana na
zapytanie kogoś, kto już ma dostawcę, to złotówka odjęta od `wapno granulowane cena`.

---

## 3. Hipoteza o nazwach własnych — upada w wersji „Agrobielik", ale wskazuje na Nordkalk

**Korekta wobec pierwszej wersji tego dokumentu:** Agrobielik **nie jest marką własną AGRII**, tylko **produktem Nordkalku** sprzedawanym przez wielu dystrybutorów. SERP na `agrobielik` (DataForSEO, 19.08): 1. osadkowski.pl, 2. nordkalk-wapno.pl, 3. agrotrzcina.pl, **4. agria.pl**, 5. allegro.pl, 7. ceneo.pl, 8. olx.pl, 9. greenpunkt.pl. Produkt jest znany — myliłem się co do tego, czyj jest.

### Wolumen (DataForSEO, Polska, pl)

| Fraza | Wyszukań/mies. | Konkurencja |
|---|---|---|
| wapno nawozowe | **1 300** | HIGH |
| wapno granulowane cena | 480 | HIGH |
| wapno nawozowe granulowane | 390 | HIGH |
| wapno granulowane big bag | 260 | HIGH |
| **wapno bielik** | **210** | LOW |
| bielik wapno | 20 | LOW |
| **agrobielik** | **10** | LOW |
| agria wapno | 10 | LOW |
| **agrobielik 70 / agrobielik 90 / agrobielik cena** | **poniżej progu pomiaru** | — |

### Search Console (agria.pl, 90 dni: 19.05–17.08)

- **`agrobielik`: 0 wyświetleń w wymiarze zapytań.** ⚠️ **To NIE jest dowód zerowego popytu** — GSC anonimizuje zapytania wpisywane przez bardzo małą liczbę użytkowników, a przy 10 wyszukaniach miesięcznie brand mieści się poniżej progu raportowania. Natomiast **strony Agrobielika zbierają ruch**: `/wapno-nawozowe-hurt/wapno-agrobielik-70-big-bag-1000kg/` 168 wyświetleń (poz. 8,7) i `/wapno-nawozowe-rolnictwo/agrobielik-70/` 106 wyświetleń (poz. 7,4) — ale z fraz ogólnych, nie z nazwy własnej.
- `bielik` — 167 wyświetleń, ale rozkład zabija pomysł: `wapno hydratyzowane bielik` (84),
  `wapno bielik` (52), `wapno bielik 30 kg cena` (11), `wapno bielik 25 kg`, `wapno bielik castorama`.
  **To jest popyt na wapno budowlane w workach 25–30 kg, z Castoramy** — dokładnie segment,
  który świadomie wykluczyliśmy (`gaszone`, `worek`, `25 kg`). Wchodzenie w „wapno bielik"
  łamie pozycjonowanie „dostawca całosamochodowy, nie sklep".
- `oxyfertil` — 110 wyświetleń, pozycja 4,6–5,7. **To jedyna nasza nazwa produktowa z realnym
  popytem** — i już ją mamy organicznie w TOP6, bez płacenia.
- `agria` — 819 wyświetleń, ale `agria` samo w sobie to pozycja 4,3 (mieszanka: odmiana ziemniaka,
  maszyny rolnicze, klub piłkarski Agria Osijek). To, co nasze — `agria tarnów` (pozycja 1,4)
  i `agria niedomice` (2,0) — **trzymamy organicznie na pierwszym miejscu**.

### Co mówi kampania Marka

Zero wyświetleń przez pięć dni, **>90% udziału utracone przez ranking przy 0% utraconym
przez budżet**. Aukcje istnieją (bo `agria` to słowo wieloznaczne), ale stawka 0,50 zł nie
wystarcza, żeby w nie wejść. W search terms nie pojawiło się **ani jedno** zapytanie markowe.

**Wniosek: hipoteza upada w wersji „Agrobielik zamiast generyku”, ale nie w wersji „marka”.**
Sam `agrobielik` ma 10 wyszukań miesięcznie — to nigdy nie zastąpi generyku (1 300 + 480 + 390 + 260).
Ale marka, którą warto kupować, to **Nordkalk**, nie Agrobielik:

| Fraza | Wyszukań/mies. | Konkurencja |
|---|---|---|
| nordkalk | **880** | LOW |
| **wapno nordkalk** | **210** | **HIGH** |
| oxyfertil | 30 | LOW |
| wapno trzuskawica | 30 | LOW |
| standard cal | 20 | LOW |
| wapno agrobielik | 10 | MEDIUM |
| agrobielik | 10 | LOW |

`wapno nordkalk` przy konkurencji HIGH to fraza handlowa, dwadzieścia razy pojemniejsza od Agrobielika — i **mamy do niej tytuł**, bo Nordkalk jest producentem surowca, który AGRIA sprzedaje. Kampania Rolnictwo już na niej konwertuje (`wapno nordkalk luzem cena` — 2 kliknięcia, `wapno węglanowe nordkalk` — 2 kliknięcia).

**Do potwierdzenia u Pawła (fakt handlowy, nie nasza decyzja):** czy AGRIA jest autoryzowanym dystrybutorem Nordkalku. Sama licytacja na cudzy znak towarowy jest w Google Ads dozwolona zawsze, ale **użycie nazwy „Nordkalk” w treści reklamy** wymaga statusu odsprzedawcy.

### Wariant zastępczy „frazy z tonażem i logistyką" — też nie ma wolumenu

Sprawdzone: `wapno 24 tony`, `wapno całopojazdowo`, `wapno big bag 1000 kg`, `wapno luzem transport`,
`wapno nawozowe dostawa`, `wapno z dowozem`, `dostawca wapna nawozowego`, `wapno nawozowe hurt`,
`wapno nawozowe tona`, `wapno granulowane luzem` — **wszystkie poniżej progu pomiaru DataForSEO.**
Jedyne, co żyje: `wapno luzem` 40/mies. i `wapno nawozowe luzem` 40/mies.

To jest istotne rozstrzygnięcie metodyczne: **hobbysty nie da się odsiać doborem słów kluczowych,
bo słowa kluczowe „dla dużych" nie mają wolumenu.** Filtr musi siedzieć w treści reklamy
i landingu — skala, tonaż, dostawa całosamochodowa, widełki cenowe za tonę — czyli dokładnie
tam, gdzie go umieściliśmy 13.08. Zostawiamy jak jest.

---

## 4. Gdzie ląduje ruch

Reklamy kierują na `/wapno-granulowane/` (grupa granulowana) i `/wapno-nawozowe/`
(grupy nawozowa **i** magnezowa). Wszystkie reklamy `APPROVED`.

| Sprawdzone | Wynik |
|---|---|
| Kod odpowiedzi | **200** obie |
| TTFB (mobile UA) | 0,29 s i 0,42 s |
| Treść renderuje się | tak — H1, sekcje, opisy produktów, CTA |
| `robots` | `noindex, follow` — **zgodnie z ADR 11.08, tak ma być** |
| GA4 potwierdza ruch | `/wapno-nawozowe/` 32 odsłony, `/wapno-granulowane/` 19 odsłon (14–18.08) |
| **Numer telefonu nad zgięciem** | **NIE** |
| **Cena / widełki** | **NIE** |
| LCP mobile | **niezweryfikowane** — dzienny limit PageSpeed Insights API wyczerpany |

### Numer telefonu na landingu — to jest główny problem

Rozkład linków `tel:` w dokumencie:

- **5,5% dokumentu** — pasek górny, ale to **ikonka słuchawki w widgecie „social icons",
  bez numeru jako tekstu**. Nad zgięciem na telefonie widać godziny „Poniedziałek–Piątek 08.00–16:00",
  adres, e-mail i dwie ikonki.
- **52,9%** — CTA w sekcji hero: „Zapytaj o ofertę — podaj tonaż" → prowadzi do `/kontakt/`
  (formularz, nie telefon).
- **59,3%** — pierwszy raz numer **jako czytelny tekst**: „Zapytaj o ofertę · tel. +48 664 393 062",
  na końcu treści merytorycznej, tuż przed stopką.
- reszta — stopka.

Czyli: użytkownik, który przyszedł z reklamy z zapytaniem `wapno granulowane cena`, dostaje
stronę bez ceny i bez widocznego numeru, a przycisk, który widzi, prowadzi do formularza.
GA4 to potwierdza: **`form_start` = 1, `form_submit` = 0** przez pięć dni.

---

## 5. Rekomendacja

**Kampania ma sens i nie jest źle zbudowana — CTR 14,7% przy 90% udziału traconym wyłącznie
przez budżet oznacza, że kupujemy właściwy ruch i jest go dziesięć razy więcej, niż nas stać.
Zero leadów po pięciu dniach nie jest sygnałem o rynku, tylko o tym, że ścieżka kontaktu jest
zamknięta: numer telefonu widać na 4,7% wyświetleń reklamy i dopiero na 79% wysokości landingu,
a strona, na którą kierujemy 33% kliknięć o cenę, ceny nie podaje.** Dlatego w tym tygodniu
robimy trzy rzeczy po stronie strony i dwie po stronie konta, a stawek i słów kluczowych
świadomie nie ruszamy — przy CPC 1,96 zł wobec stawki 2,00 zł jesteśmy na suficie licytacji,
więc taniej będzie dopiero wtedy, gdy Wyniki Jakości (dziś 1–6, na `wapno węglanowe`
i `wapno tlenkowe` po 1) podniesie lepsze dopasowanie landingu, a nie zmiana stawki.

### Robimy w tym tygodniu

| # | Co | Dlaczego |
|---|---|---|
| 1 | **Numer telefonu jako przycisk „Zadzwoń 664 393 062" w hero obu landingów** + pasek sticky na mobile | Jedyny mierzony kanał leada dziś jest schowany za ikonką. To najtańsza zmiana o największym efekcie |
| 2 | **Widełki cenowe „od X zł/t" na obu landingach** (zgodnie z ustaleniem z 06.08 — widełki tonowe, nie cennik i nie worki) | 33% kosztu to zapytania cenowe, które odbijają się od strony bez ceny. Cennik jest gotowy: `docs/operations/CEN_LISTA_URL_2026-08-13.md` |
| 3 | **Formularz „oddzwonimy" pod CTA, z polem tonaż + lokalizacja** | Kampania chodzi 6–22 przez 7 dni, telefon odbierany jest pn–pt 8–16. Poza tym oknem — a to obejmuje niedzielę, najmocniejszy dzień wg GSC — musi być co kliknąć. Assetu połączeń **nie** rozszerzamy na weekend: nieodebrany telefon jest gorszy niż brak telefonu, bo uczy algorytm, że numer nie odbiera |
| 4 | **Podnosimy stawkę w grupie Brand z 0,50 na 3,00 zł i dokładamy grupę „Producent” (`wapno nordkalk`, `nordkalk wapno nawozowe`, `wapno trzuskawica`, `standard cal`) po 2,50 zł.** Markę wyłączamy dopiero wtedy, gdy po 7–10 dniach nadal nie wyda złotówki | Marka traci **>90% wyświetleń przez ranking przy 0% przez budżet** — aukcje istnieją, przy 0,50 zł do nich nie wchodzimy. Test jest ograniczony budżetem 6 zł/dz, więc kosztuje najwyżej kilkadziesiąt złotych miesięcznie i odpowiada danymi z konta, a nie szacunkiem planera. Prawdziwy wolumen siedzi nie w `agrobielik` (10/mies.), tylko w `wapno nordkalk` (**210/mies., HIGH**) i `nordkalk` (880/mies.) — marce producenta, którego wapno faktycznie sprzedajemy, i na której już konwertujemy (`wapno nordkalk luzem cena` → 2 kliknięcia) |
| 5 | **22 wykluczenia obcych marek i kopalń** (bez „marka + cena") | 20,76 zł przez pięć dni ≈ 125 zł/mies. na zapytania o cudzy katalog, przy budżecie, który i tak nie starcza |

### Czego świadomie nie ruszamy

Stawek (jesteśmy na suficie licytacji — najpierw Wynik Jakości), zestawu słów kluczowych
(dopasowanie jest dobre: 72% kosztu na zapytaniach zakupowych i produktowych), harmonogramu
6–22 przez 7 dni, tekstów reklam „od producenta" (mają za sobą 4 dni, za mało na ocenę),
statusu `noindex` landingów (ADR 11.08 — kanibalizacja jest zmierzona), geobloku.

### Kiedy ocena kampanii będzie miała sens

**Nie teraz.** Przy oczekiwanej dla B2B surowcowego konwersji 1–3% z 100 kliknięć spodziewana
liczba leadów to 1–3, a zero mieści się w szumie. Żeby odróżnić „kampania nie działa" od
„mieliśmy pecha", potrzeba **300–500 kliknięć**, czyli przy obecnym tempie ~20 klików/dzień
**15–25 dni od naprawy ścieżki kontaktu**. Realny termin oceny: **około 10 września**,
i to pod warunkiem, że punkty 1–3 wejdą w tym tygodniu — bo liczyć konwersje z okresu,
w którym numeru nie było widać, nie ma sensu.

### Do decyzji klienta (nie naszej)

Przy 90% udziału w wyświetleniach traconym przez budżet, w miesiącu, który jest szczytem roku
(`wapno granulowane` 9 900 wyszukań w sierpniu wg DataForSEO), 40 zł/dzień kupuje jedną dziesiątą
rynku. To jest argument za podniesieniem budżetu **na wrzesień–październik** (drugi impuls
wapnowania pożniwnego), do przedstawienia dopiero po naprawie ścieżki kontaktu — nie wcześniej,
bo dosypywanie pieniędzy do lejka bez wyjścia to powiększanie strat.

---

## Sprostowanie do ADR 13.08

`change_event` na koncie nie zawiera **żadnego** zdarzenia przed **14.08.2026 13:49:20**.
Budżety, obie kampanie, grupy, słowa kluczowe i reklamy zostały utworzone **14.08 między
13:49 a 13:52**, pierwsze wyświetlenie o 14:00. ADR 13.08 opisuje więc plan i wykonaną pracę,
ale **kampanie na koncie powstały 14.08**, nie 13.08. To wyjaśnia „zero wyświetleń 13.08"
z ADR 14.08 — nie było czego wyświetlać.

Drugie ustalenie: **między 14.08 17:16 a 18.08 nikt nic na koncie nie zmieniał** (186 zdarzeń
w historii zmian, wszystkie z 14.08). Stan konta odpowiada ADR-owi z 14.08.

---

## Aneks 19.08 — ceny na kartach produktów: nie ma ich nigdzie

Sprawdzone po pytaniu Janka, czy widełki cenowe z decyzji 06.08 zostały wdrożone.
**Nie zostały — ani w bazie, ani w renderze.**

| Sprawdzenie | Wynik |
|---|---|
| `_price` przy 19 opublikowanych produktach | **NULL przy wszystkich 19** |
| słowo „cena" w `post_content` produktu | **0 z 19** |
| `<h2>` zawierający „cena" | **0 z 19** |
| render `/agrobielik-70/`, `/weglanowe-granulowane/`, `/oxyfertil-90/` | jedyne wystąpienie rdzenia „cen" to zwrot **„indywidualną wycenę"** w sekcji kontaktowej |
| landingi Ads `/wapno-granulowane/`, `/wapno-nawozowe/` | zero cen, zero widełek |

Nagłówki kart produktów to dziś: H1 z nazwą, „Specyfikacja techniczna",
„Najczęściej zadawane pytania", „Zapytaj o ofertę, zamów próbkę". **Żadnego nagłówka
cenowego.** Wolumen, który przez to zostawiamy: `wapno granulowane cena` 480/mies.,
`wapno nawozowe cena za tonę` 140, `wapno magnezowe cena` 90, `wapno na pole cena` 50,
`wapno tlenkowe cena` 50, `kreda nawozowa cena` 50.

Wątek prowadzony osobno: `docs/prompty/2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md`.

### Zauważone obok, nie ruszam

- **Agrobielik 70 ma dwa adresy**, oba zbierają wyświetlenia w GSC (90 dni):
  `/wapno-nawozowe-hurt/wapno-agrobielik-70-big-bag-1000kg/` (168 wyśw., poz. 8,7)
  i `/wapno-nawozowe-rolnictwo/agrobielik-70/` (106 wyśw., poz. 7,4).
- **Stary typ wpisu `produkt` nadal opublikowany** — ID 67, 68, 69 (Agrobielik 70,
  Agrobielik 90, Agrobielik 90 frakcja 2-8 mm) równolegle do `product` ID 310, 311.
- **Demo-produkt motywu w indeksie** — `/produkt/organic-pineapple/`, 7 wyświetleń
  na pozycji 5,0 w 90 dni.
