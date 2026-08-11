# OLX jako prowadzony kanał sprzedaży — AGRIA, sierpień–październik 2026

> Odpowiedź na pytanie Pawła z 07.08: *„czy kupujemy dalej pakiet 30 ogłoszeń, czy lepiej wziąć mniejszy pakiet, np. 10, i skupić się na ich promowaniu"*.
> Podstawa: `docs/operations/OLX_INWENTARYZACJA_2026-08-07.md`, `OLX_KONKURENCJA_2026-08-07.md` (z korektą §3a), `OLX_BASELINE_2026-08-07.md`, `CENNIK_PAWEL_2026-08-07.md`.
> Okno czasowe zestrojone z planem Ads (`2026-08-PLAN_ADS_3MIES.md`) — jeden moment decyzji dla obu kanałów na koniec października.

---

## Część wewnętrzna — na czym stoi ten plan (NIE do klienta)

### Ustalenia z Jankiem (07.08)

| Rzecz | Decyzja |
|---|---|
| Kto wystawia | **My, przez Partner API.** Każdy zapis na koncie klienta po jego „ok" |
| Pakiet | **Premium 100 w kategorii Nawozy — 719,99 zł brutto/mies.** |
| Wycena Auranet | **Setup 1 800 zł netto jednorazowo + 300 zł netto/mies.** Zatwierdzone przez Janka 07.08 |
| Panel OLX | Odczytany 07.08 z zalogowanego konta AGRII |

### Dlaczego setup ciężki, a prowadzenie lekkie

Janek zakwestionował pierwotną propozycję miesięcznej stawki rzędu prowadzenia Ads (600–800 zł) pytaniem, czy kanał nie chodzi sam. **Miał rację i to jest sprawdzalne na koncie AGRII.**

`auto_extend` odnawia ogłoszenia automatycznie — ale **tylko dopóki żyje pakiet**. Widać to co do minuty: jedyne ogłoszenie z włączonym auto_extend (858802418) odnowiło się **18.07 o 08:43:52**, a pakiet wygasł **18.07 o 08:55**. Zdążyło wziąć ostatnią jednostkę. Pozostałe 17 zgasło. To samo ogłoszenie spróbuje odnowić się 17.08 i padnie, jeśli pakietu nie będzie.

Wniosek: przy opłaconym pakiecie i auto_extend na wszystkich ogłoszeniach **kanał nie wymaga cotygodniowej obsługi**. Realna praca to:

| Co | Kiedy |
|---|---|
| Odczyt pomiaru i korekta — zabić martwe tytuły, powielić działające | raz po 2–3 tygodniach, potem rzadziej |
| Rewizja sezonowa asortymentu i siatki miast | 2–3× w roku (listopad: wapno palone; grudzień–marzec: paszarstwo i budownictwo) |
| Aktualizacja cen po nowym cenniku Pawła | jedna komenda `--update`, minuty |

Stąd 300 zł/mies., nie 800. **Dzisiejszy czas jest zaszyty w setupie — bez osobnej pozycji „analiza" w mailu.**

Rewizja sezonowa nie wchodzi do tej wyceny — pojawi się jako osobna pozycja, gdy wypadnie (najbliższa: listopad).

### Co obejmuje setup 1 800 zł — rozpiska

| Blok | Zakres |
|---|---|
| Rozpoznanie kanału | Spięcie Partner API z kontem AGRII, inwentaryzacja 20 ogłoszeń i ich statystyk, ustalenie mechaniki pakietów i `auto_extend` z panelu, cennik pakietów i promowań, przegląd regulaminu pod kątem geo-multiplikacji, danych kontaktowych i linków |
| Analiza rynku | 2 486 ogłoszeń z dwóch podkategorii, 544 sprzedawców — profile liderów, rotacja, promowanie, struktura tytułów, ceny sprowadzone do porównywalnych (loco, za tonę) |
| Model doboru miejscowości | Wolumen wyszukiwań per województwo z DataForSEO, zakłady wysyłkowe per produkt z kart produktowych, koszt transportu jako udział w cenie tony → siatka liczona, nie zgadywana |
| Treści | 10 pozycji asortymentowych, tytuły pod intencję, opisy z parametrami zaciąganymi z kart produktowych, ceny z jednostką i klauzulą, dobór zdjęć per produkt z kitu brandowego |
| Narzędzia | Generator ogłoszeń i pipeline wystawiania przez API, rejestr chroniący przed dublowaniem, tryb aktualizacji treści i cen na wszystkich ogłoszeniach naraz |
| Pomiar | Baseline statystyk konta, cotygodniowy snapshot przyrostowy, monitoring konkurencji z diffem tydzień do tygodnia |

Stan na wieczór 07.08: **rozpoznanie, analiza rynku, model doboru miejscowości, treści, narzędzia i pomiar — zrobione.** Pilot wystawiony i zweryfikowany. Zostaje masówka po zakupie pakietu.

### Co obejmuje 300 zł/mies — rozpiska

| Czynność | Rytm |
|---|---|
| Snapshot statystyk własnych ogłoszeń + odczyt przyrostu | co tydzień, zautomatyzowane |
| **Monitoring konkurencji**: kto wszedł i wypadł, czy podmieniają tytuły, czy przestawiają miejscowości, ile odświeżają, czy zaczynają promować | co tydzień, zautomatyzowane, `market_snapshot.py --diff-last` |
| Wygaszenie ofert bez wyników, powielenie działających | raz w miesiącu |
| Aktualizacja cen po nowym cenniku | na żądanie, jedna komenda na wszystkie ogłoszenia |
| Przypomnienie o odnowieniu pakietu przed wygaśnięciem | co miesiąc |

### Monitoring konkurencji — co konkretnie mierzymy

Baseline zebrany 07.08: `data/olx/market/2026-08-07.json`, **2 486 ogłoszeń od 544 sprzedawców** z kategorii Nawozy i Pozostałe rolnicze. OLX nie udostępnia statystyk cudzych ogłoszeń, ale publiczne API oddaje `created_time` i `last_refresh_time`, więc mierzalne jest:

| Sprzedawca | Ogłoszeń | Unikalnych tytułów | Miast | Promowanych | Mediana wieku ogłoszenia |
|---|---|---|---|---|---|
| 699-712-071 | **510** | 55 | 361 | 0 | 240 dni |
| AGRO-KOTYNIA | 162 | 9 | 162 | 25 | **1 670 dni** |
| Ewelina | 103 | 7 | 101 | 0 | **0,3 dnia** |
| PPHU „Marcin" | 100 | 90 | 91 | 0 | **2 706 dni** |
| EMPRO | 99 | 44 | 96 | 0 | 931 dni |
| Wapna Świętokrzyskie | 39 | 39 | 36 | 14 | — |

Widać z tego dwie różne strategie: **utrzymywanie tych samych ogłoszeń latami** (AGRO-KOTYNIA 4,5 roku, PPHU Marcin 7,4 roku) wobec **kasowania i wystawiania od nowa** (Ewelina — 103 ogłoszenia o medianie wieku 0,3 dnia). Pierwsza buduje staż, druga daje świeżą datę kosztem jednostek pakietu. Nasze dane własne sugerują, że staż ma znaczenie (trzy najstarsze ogłoszenia AGRII odpowiadają za 71% kontaktów), więc idziemy pierwszą drogą.

**Czego świadomie nie twierdzimy:** 94% ogłoszeń w kategorii ma `last_refresh_time` młodszy niż 3 dni. Kuszące jest wywnioskowanie, że wszyscy codziennie płacą za odświeżanie — ale przy 544 sprzedawcach, w tym drobnych prywatnych, to nieprawdopodobne. Bardziej prawdopodobne, że pole odzwierciedla też odświeżenia po stronie OLX. **Nie budujemy na tym wniosków** — rozstrzygnie to dopiero różnica między snapshotami, pierwsza 14.08.

### Ile konkurenci mogą z tego mieć — ostrożnie

Podstawiając nasz zmierzony wskaźnik (22,4 wyświetlenia na ogłoszenie miesięcznie, CR 3,35% na telefon):

| Sprzedawca | Ogłoszeń | Szacowane wyświetlenia/mies. | Szacowane telefony/mies. | Koszt pakietu/mies. |
|---|---|---|---|---|
| 699-712-071 | 510 | ~11 400 | ~380 | ~3 600 zł (3 pakiety) |
| AGRO-KOTYNIA | 162 | ~3 600 | ~120 | ~1 200 zł |
| **AGRIA po zmianie** | **100** | **~2 240** | **~75** | **720 zł** |

**Ile z tych telefonów zamienia się w zamówienia — nie wiemy i nie udajemy, że wiemy.** To zależy od ceny, dostępności i transportu, czyli od rzeczy poza kanałem. Ale sam koszt kontaktu — rzędu 10 zł — mówi, dlaczego ci ludzie utrzymują setki ogłoszeń latami.

### Siatka miast — dlaczego wygląda tak, a nie inaczej

Pierwsza wersja siatki była dobrana ręcznie „pod stawy" i „pod rolnictwo". **To było zgadywanie i zostało wyrzucone.** Obecna (`scripts/olx/grid.py` → `data/olx/siatka-miast.json`) liczy się z trzech rzeczy:

1. **Popyt per województwo** — wolumen wyszukiwań 11 fraz w 16 województwach (DataForSEO, Google Ads, pull 07.08). Mazowieckie 3 010/mies., Śląskie 1 630, Małopolskie 1 450, na końcu Lubuskie 220 i Opolskie 250.
2. **Zasięg miejscowości** — liczba **różnych** sprzedawców wystawiających tam wapno. Liczba ogłoszeń nie nadaje się na tę miarę: Łomianki mają ich 24, ale prawie wszystkie od jednego geo-spamera. Po przejściu na liczbę sprzedawców na czoło wychodzą realne ośrodki rolnicze: Lublin 15, Siedlce 13, Mława 13, Grójec 12, Kalisz 11, Kielce 11, Łomża 11.
3. **Ekonomika transportu** — i to jest czynnik, który przesądza.

**Sprzedajemy na tony loco magazyn, więc o zasięgu decyduje stosunek kosztu przewozu do ceny towaru.** Przy zestawie 24 t i stawce rzędu 6 zł/km wychodzi około **0,25 zł za tonę na kilometr** (*założenie do potwierdzenia u Pawła — on kwotuje transport indywidualnie, więc zna realną stawkę*). Przyjmując, że transport nie powinien przekraczać połowy ceny towaru:

| Produkt | zł/t | Sensowny zasięg |
|---|---|---|
| Węglanowe z Mg odm. 05 | 36 | **72 km** |
| Węglanowe odm. 04 | 57 | **114 km** |
| Kreda nawozowa sypka | 125 | 250 km |
| Kreda pastewna | 190 | 380 km |
| Agrobielik 70 luz | 220 | 440 km |
| Węglanowe granulowane | 350 | 700 km |
| Agrobielik 90 / Oxyfertil 90 | 750–790 | cała Polska |
| Wapno palone mielone | 950 | cała Polska |

**Odpowiedź na pytanie „czy sprzedawanie tego do Gdańska ma sens": zależy od produktu.** Gdańsk to ~500 km od Niedomic. Dla wapna węglanowego po 57 zł/t transport wyniósłby ~125 zł na tonie — ponad dwukrotność ceny towaru. Bez sensu. Dla Agrobielika 90 po 750 zł/t to ~17% ceny — jak najbardziej. Dlatego **każdy produkt ma własną siatkę miast**, a nie jedną wspólną.

Dochodzi rzecz, która wyszła dopiero przy tej analizie: **wysyłka nie idzie z Niedomic.** Karty produktowe wskazują różne zakłady per produkt — kreda nawozowa granulowana z Kornicy (08-205, pod Siedlcami), węglanowe odm. 04 z Góraźdżec i Tarnowa Opolskiego, kreda sypka z Pierzchnicy, kreda pastewna z Bukowej i Celin. Kreda granulowana ma więc do Siedlec 38 km, a nie 250.

Efekt: **100 ogłoszeń w 33 miejscowościach, 8 województwach, maksymalnie 4 ogłoszenia na miasto.** Węższy zasięg geograficzny niż u liderów — ale to nie jest zaniedbanie, tylko konsekwencja tego, że sprzedajemy towar masowy loco. Model oznacza cztery ogłoszenia, w których transport zjada ponad 40% ceny (Dębica, Płock, Płońsk, Zwoleń) — do przejrzenia przy pierwszej korekcie.

### Skąd Premium 100, a nie Megapakiet

AGRIA kupowała **Megapakiet 20 za 335,99 zł** — pięć razy w trzynaście miesięcy, nieregularnie. Megapakiet daje wymienność podkategorii rolniczych; sprawdziłem, czy jej potrzebujemy:

| Podkategoria | Ogłoszeń | Wapniarskich | Kto |
|---|---|---|---|
| **Nawozy** | 1 204 | **709** | cała czołówka: AGRO-KOTYNIA 161, DAREK 70, Agro-Siew 58, Wapna Świętokrzyskie 39, Tadeusz 39 |
| Produkty rolne | 1 272 | 2 | — |
| Worki | 1 085 | 1 | — |
| Pozostałe rolnicze | 1 254 | 95 | **92 to 699-712-071** — hurtownia zaopatrzenia (folia, dezynfekanty), nie konkurent wapniarski. Jego wapniarska część to kreda stawowa |

Rynek jest w Nawozach. Wapno palone mielone dla oczyszczalni i hydratyzowane dla budownictwa leżą w zupełnie innym drzewie kategorii — **Megapakiet i tak by ich nie objął**. Płacenie za wymienność, której nie wykorzystamy, to 108 zł na każdych 20 ogłoszeniach.

Koszt jednostkowy: Megapakiet 20 = **16,80 zł/ogłoszenie**, Premium Nawozy 100 = **7,20 zł**.

### Odpowiedź na „30 ogłoszeń czy 10 + promowanie" — liczbowo

Ceny promowania (dynamiczne, odczyt 07.08 na ogłoszeniu 858802418): Mini 13,08 · Midi 37,75 · **Maxi 104,89 zł**.

Przy budżecie ~330 zł/mies.: 10 ogłoszeń + 2 promowania Maxi = 329,77 zł, albo 20 ogłoszeń bez promowania i 100 zł reszty. Jedno promowanie Maxi kosztuje tyle, co **dziewięć ogłoszeń** w Premium 100.

Do tego rynek: 699-712-071 ma **zero** promowanych przy 191 ogłoszeniach, AGRO-KOTYNIA 24 przy 161. **Wolumen, nie promowanie.** Promowanie zostawiamy jako narzędzie punktowe na ogłoszenia, które same dowiodą skuteczności — nie na start.

### Prognoza — jak jest policzona

Statystyki Partner API są kumulatywne od utworzenia ogłoszenia, więc wskaźnika miesięcznego nie da się z nich odczytać wprost. Liczę na **jednorodnej kohorcie**: 16 geo-duplikatów utworzonych 07–21.07.2025, wygasłych 18.07.2026, o znanej historii pakietów (5 pakietów × 30 dni = **150 dni ekspozycji z 395**).

Kohorta zebrała **1 790 wyświetleń i 60 odsłon telefonu**, CR 3,35%.

| Założenie o ekspozycji | wyśw./ogłoszenie/mies. |
|---|---|
| ogłoszenia żyły cały czas od utworzenia (dolna granica) | **8,6** |
| ogłoszenia żyły tylko w oknach pakietu (realne) | **22,4** |

Stąd trzy scenariusze dla 100 ogłoszeń przy ciągłym pakiecie i włączonym auto_extend:

| Scenariusz | Założenie | Wyświetleń/mies. | CR | **Odsłon telefonu/mies.** | Koszt pakietu na kontakt |
|---|---|---|---|---|---|
| Pesymistyczny | dolna granica tempa, CR jak średnia konta (2,9%) | ~860 | 2,9% | **~25** | 29 zł |
| Realny | tempo z okien pakietu, CR kohorty (3,35%) | ~2 240 | 3,35% | **~75** | 10 zł |
| Optymistyczny | tytuły pod intencję i rozbicie na produkty podnoszą CR do 3,7% (poziom trafionego „Do stawu"), tempo +40% | ~3 100 | 3,7% | **~115** | 6 zł |

Punkt odniesienia: **całe dotychczasowe konto dało 209 odsłon telefonu przez cały cykl życia** — a w lipcu cały organik agria.pl dał 221 kliknięć w GSC.

**Czego prognoza NIE obejmuje** (do powiedzenia klientowi wprost):
- sezonowości — sierpień–październik to szczyt dla rolnictwa, więc pierwsze miesiące będą powyżej średniej rocznej;
- tego, ile zapytań zamieni się w zamówienia — to zależy od ceny, dostępności i transportu, nie od kanału;
- tego, że trzy najlepsze ogłoszenia na koncie są z 2023 i 2024 roku, a ich przewaga może wynikać ze stażu, którego nowe ogłoszenia na starcie nie mają.

### Korekty do wcześniejszych dokumentów

Dwa wnioski z `OLX_KONKURENCJA_2026-08-07.md` nie wytrzymały weryfikacji i zostały poprawione w §3a tamtego dokumentu:

1. **„Ceny AGRII 25–40% powyżej mediany OLX"** — nieprawda. Pole „cena" na OLX nie ma jednostki; tylko 36 z 1 204 ogłoszeń podaje cenę tonową. Po odfiltrowaniu do porównywalnych ofert loco: węglanowe AGRII **57 zł/t** vs Morawica **57,40**, kreda **125** vs jedyna porównywalna **185**, tlenkowe **220** vs Harabin **210**. AGRIA jest w rynku wszędzie. Stara mediana powstała m.in. z sześciu kopii jednego ogłoszenia.
2. **„Tlenkowe to na OLX pustka — 3 ogłoszenia"** — jest ich 65, z czego 39 to jeden sprzedawca (Wapna Świętokrzyskie).

**Skutek dla planu:** nie wycinamy węglanowych ani kredy z powodu ceny. Zostaje realny temat: konkurenci sprzedają obok atestowanego wapna także **nieatestowane odsypy z wagi po 78 zł/t** (Harabin, obok 210 zł/t za atestowane). To jest ta „tania konkurencja z OLX", której obawia się Paweł — i to nie jest ten sam produkt.

### Cztery rzeczy regulaminowe, które zmieniamy w treści

Regulamin OLX pkt 4:

1. **Geo-multiplikacja jest wprost dozwolona** w kategoriach płatnych, przy różnych lokalizacjach i jednym koncie. Model liderów jest legalny.
2. **Numer telefonu w treści jest zabroniony** — dane kontaktowe wyłącznie w polach formularza. Dotychczasowe opisy kończyły się `6*6*4*3*9*3*0*6*2`; rozbicie gwiazdkami to obchodzenie filtra, nie zgodność. Wypada.
3. **Jedno ogłoszenie = jeden przedmiot.** Dotychczasowy opis wymieniał pięć grup produktów **plus „nawozy sztuczne"** — te są poza zakresem produktowym AGRII (`docs/MASTER_PROMPT.md`).
4. **Adres WWW** — zakaz dotyczy odnośników do konkurencyjnych serwisów ogłoszeniowych, ale sformułowanie jest szerokie. Bezpieczna droga jest jawna: **„Link do zewnętrznej strony WWW" to funkcja pakietu**, więc link z UTM idzie na Stronę firmową OLX, nie w opis.

### Stan wykonania na 07.08 wieczorem

- **Baseline pomiarowy zrobiony** — `data/olx/snapshots/2026-08-07-1752.json`, 19 ogłoszeń / 7 273 wyświetlenia / 209 telefonów, bez prywatnego ogłoszenia Pawła. Kolejny snapshot **14.08**.
- **100 ogłoszeń gotowych do wystawienia** — `data/olx/adverts-payload.json`: 10 produktów × 6–14 miast, 56 miast, każde zweryfikowane co do województwa. Parametry z renderu kart agria.pl, zdjęcia z kitu brandowego już na CDN OLX.
- **Pilot wystawiony i zweryfikowany** — ogłoszenie 1089946612 („Wapno do stawu", Zator), status `limited` (czeka na jednostkę pakietu). Wykrył dwa błędy, oba naprawione: brak telefonu w kontakcie i to, że PUT w tym API podmienia cały zasób, więc `auto_extend` ustawiany łatką cicho nie wchodził — **dokładnie ten mechanizm zgasił konto 18.07**.
- **Pipeline gotowy** — `scripts/olx/post_adverts.py` z trybami `--dry-run / --pilot / --all / --update / --auto-extend`, rejestr chroni przed dublowaniem.

### FLAGA — pomiar nie działa i dotyczy to też Ads

Sprawdziłem, zanim zacząłem mierzyć OLX. **GA4 nie zbiera danych z agria.pl.**

Lipiec: 148 sesji, z tego **5 organicznych** — przy 221 kliknięciach w GSC. Ostatnie 90 dni: 187 direct, 8 google/organic. `/kalkulator-wapnowania/` — cel QR-kodu z ogłoszeń — **5 odsłon w 90 dni**. Sesji ze źródłem „olx" — zero w dwunastu miesiącach.

Przyczyna: kontener GTM jest wpięty i opublikowany, tag GA4 odpala się na All Pages, wszystko skonfigurowane poprawnie. Ale tag „Consent Default Denied" ustawia `analytics_storage: denied` dla regionu EEA/PL, a **na stronie nie ma niczego, co kiedykolwiek wywoła `gtag('consent','update', granted)`** — nie ma banera zgody ani CMP. Zgoda zostaje odmówiona na zawsze, GA4 chodzi w trybie bezcookie'owych pingów.

**To nie jest problem OLX-owy.** Konsekwencje szersze:
- **Kampanie Ads startują w połowie sierpnia**, a w wysłanym planie napisaliśmy: *„Oba są mierzone, więc będzie dokładnie widać, ile kontaktów przyszło z reklamy, z jakiego hasła i jakim kosztem"*. Przy `ad_storage: denied` i braku GCLID w cookie **śledzenie konwersji Ads nie zadziała**. 1 200 zł/mies. budżetu reklamowego poszłoby bez pomiaru zwrotu.
- Wdrożenie CMP jest jednocześnie **wymogiem RODO**, więc to nie jest wybór „mierzyć czy nie", tylko „mieć zgodę i mierzyć" albo „nie mieć i nie mierzyć".

**Do decyzji Janka:** czy CMP wchodzi do planu jako osobna pozycja przed startem Ads, i czy ten temat w ogóle pojawia się w mailu o OLX, czy idzie osobno. Do czasu rozstrzygnięcia **głównym miernikiem OLX zostają statystyki OLX** (`advert_views`, `phone_views` mierzone przyrostowo), a GA4 jest pomocniczy — i tak trzeba to klientowi napisać, zamiast obiecywać pomiar, którego nie ma.

### Jak mierzymy ten kanał

| Miernik | Skąd | Uwaga |
|---|---|---|
| `advert_views`, `phone_views` per ogłoszenie | Partner API, `scripts/olx/olx-snapshot`, przyrostowo co tydzień | **Miernik główny.** Niezależny od stanu analityki na stronie |
| Wiadomości OLX | `/partner/threads` | Marginalne: 1 wątek wobec 209 telefonów. Monitorujemy, nie liczymy na to |
| Ruch OLX → agria.pl | UTM na linku Strony firmowej | **Pomocniczy** i zaniżony, dopóki nie ma CMP (patrz FLAGA) |

Link do ustawienia w panelu po zakupie pakietu (funkcja pakietu Premium „Link do zewnętrznej strony WWW"):

```
https://agria.pl/?utm_source=olx&utm_medium=marketplace&utm_campaign=olx-nawozy-2026-08
```

**QR-kod na grafikach zostaje bez UTM w tej rundzie.** Prowadzi do `/kalkulator-wapnowania/` (5 odsłon w 90 dni), ale zmiana adresu w kodzie oznacza przerobienie ośmiu grafik, a plików źródłowych nie ma w repo — istnieją tylko jako obrazy na CDN OLX. Do zrobienia przy najbliższej rewizji grafik, razem z ujęciami pod zastosowanie (staw, sad, oczyszczalnia), których w kicie brakuje.

### Ryzyka do pilnowania

- **Sierpień jest przeciążony** — plan Ads już to odnotowuje (setup Ads + landingi M3 + P0 indeksacyjne + CWV). OLX dokłada wystawienie 100 ogłoszeń. Samo wystawienie jest zautomatyzowane, ale rotacja i reakcja na dane to praca cotygodniowa.
- **Konto jest prywatno-firmowe** — prywatny Gmail Pawła, prywatne ogłoszenie mieszkania na tym samym koncie, hasło przyszło mailem plaintextem. Do rozmowy: zmiana hasła + 2FA. Docelowo konto na adres firmowy AGRII, ale to decyzja klienta.
- **Trzy najlepsze ogłoszenia (Piotrków, Tarnów ×2) mają staż** — 2023 i 2024 rok. Nie kasujemy ich, tylko aktualizujemy treść przez `--update`; nowe 100 wchodzi obok.

---

## Treść maila (v2 — pod akcept, 07.08 wieczorem)

Cześć Kasjan, Paweł,

Paweł pytał, czy kupować dalej pakiet ogłoszeń na OLX i czy nie lepiej wziąć mniejszy, a skupić się na promowaniu. Zamiast odpowiadać z głowy, rozebraliśmy tę kategorię na czynniki pierwsze — przejrzeliśmy blisko dwa i pół tysiąca ogłoszeń od pięciuset czterdziestu sprzedawców, zestawiliśmy to z Waszymi własnymi wynikami z trzech lat, sprawdziliśmy cennik OLX i regulamin, i policzyliśmy, dokąd w ogóle opłaca się wozić towar. Poniżej wynik i gotowy plan.

**Zacznę od tego, co Paweł przeczuwał: tak, na tym da się zarabiać.**

Największy sprzedawca w tej kategorii trzyma **510 ogłoszeń w 361 miejscowościach**. Kolejny — 162 ogłoszenia. Trzeci i czwarty po sto. To nie są przypadkowe wystawki: część z tych ogłoszeń wisi tam **od siedmiu lat**. Nikt nie utrzymuje setki ofert przez siedem lat dla sportu.

Podstawiając wskaźniki zmierzone na Waszym własnym koncie, sprzedawca ze 162 ogłoszeniami zbiera rzędu **120 telefonów miesięcznie**, płacąc OLX około 1 200 zł. To jakieś dziesięć złotych za kontakt z zainteresowanym. Ile z tego zamienia w zamówienia — tego nie wiemy i nie będę zgadywał. Ale koszt pozyskania kontaktu na tym poziomie tłumaczy, dlaczego oni tam siedzą.

**Ale nie wygrywają promowaniem — i to jest ważne, bo kosztowałoby Was najwięcej.**

Sprawdziliśmy to wprost: dwaj najwięksi gracze mają odpowiednio **zero i 24 wyróżnienia przy 510 i 162 ogłoszeniach**. Wyróżnienie jednego ogłoszenia na 30 dni kosztuje 105 zł — tyle, co dziewięć zwykłych ogłoszeń. Rynek wybiera liczbę ofert i liczbę miejscowości, nie wyróżnienia. My też.

**Wasze własne dane mówią to samo, tylko dobitniej.**

Konto ma dziś jedno aktywne ogłoszenie — siedemnaście wygasło 18 lipca razem z końcem opłaconego pakietu, w środku sezonu. Przez cały czas działania te ogłoszenia zebrały **7 273 wyświetlenia i 209 odsłon numeru telefonu**. Dla porównania: cały ruch z Google na agria.pl dał w lipcu 221 kliknięć. To nie jest kanał poboczny — to drugi kanał tej samej wielkości co wyszukiwarka.

Dwie rzeczy wyszły z tych danych, które od razu wykorzystujemy:

**Tytuł decyduje o wszystkim.** Ogłoszenie zatytułowane „Do stawu…" zebrało 94 odsłony telefonu — **45% wszystkich kontaktów z całego konta**. Ta sama oferta, te same zdjęcia, ale tytuł mówiący, do czego to służy, zamiast „Najtaniej!". Nowe ogłoszenia budujemy więc pod konkretne zastosowanie.

**Ogłoszenia gasły po cichu.** Automatyczne przedłużanie było włączone na jednym ogłoszeniu z dwudziestu. To jedno przedłużyło się 18 lipca o 8:43, kwadrans przed wygaśnięciem pakietu — i tylko dlatego żyje do dziś. Pozostałych siedemnaście padło tego samego ranka i nikt tego nie zauważył. Przy nowych ustawiamy przedłużanie od razu na wszystkich i pilnujemy terminu pakietu.

**Podpięliśmy się bezpośrednio do systemu OLX i to jest rzecz, która zmienia sposób prowadzenia tego kanału.**

OLX udostępnia firmom bezpośredni dostęp do danych i do zarządzania ogłoszeniami — poza panelem, którego używa się ręcznie. Uruchomiliśmy go na Waszym koncie i spięliśmy z naszymi narzędziami analitycznymi. Co to daje w praktyce:

**Widzimy wynik każdego ogłoszenia osobno, tydzień po tygodniu.** Panel OLX pokazuje liczby narastająco od dnia założenia ogłoszenia — z oferty wystawionej w 2023 roku nie da się wyczytać, ile zrobiła w zeszłym miesiącu. My pobieramy stan co tydzień i liczymy różnicę, więc widać przyrost, a nie sumę z trzech lat. Bez tego prognoza w tym mailu byłaby zgadywaniem, a nie rachunkiem.

**Sto ogłoszeń wystawiamy i zmieniamy jedną operacją.** Gdy Paweł przyśle nowy cennik, ceny podmieniają się we wszystkich ogłoszeniach w kilka minut — zamiast stu poprawek ręcznie w panelu. Tak samo z tytułami, opisami i zdjęciami.

**Automatycznego przedłużania pilnuje system, nie czyjaś pamięć.** To właśnie ono zawiodło 18 lipca.

**Widzimy, co robi konkurencja — co tydzień.** Pobieramy całą kategorię i porównujemy z poprzednim tygodniem: kto doszedł, kto zniknął, kto podmienił tytuły, kto przestawił miejscowości, kto zaczął płacić za wyróżnienia. To pierwszy raz, gdy tę kategorię da się obserwować systematycznie, a nie przez zaglądanie na OLX od czasu do czasu.

I to ten dostęp pokazał rzeczy, o których z panelu nie było jak się dowiedzieć: że jedno ogłoszenie odpowiada za 45% wszystkich kontaktów, że automatyczne przedłużanie działało na jednym z dwudziestu, i że pakiet wygasł kwadrans po tym, jak jedyne chronione ogłoszenie zdążyło się odnowić.

**Co jest gotowe.**

Nie przysyłam Wam koncepcji do przedyskutowania, tylko plan, który czeka na uruchomienie. **Sto ogłoszeń jest przygotowanych** — dziesięć produktów, każdy z własnym opisem, parametrami zaciągniętymi wprost z Waszych kart produktowych i cenami z cennika, który Paweł przysłał 7 sierpnia. Pierwsze ogłoszenie już wisi na koncie jako sprawdzian, że wszystko przechodzi poprawnie.

Ogłoszenia podają cenę **z jednostką i informacją, że jest netto loco magazyn**. To wygląda na drobiazg, a jest przewagą: na blisko dwa i pół tysiąca ogłoszeń w tej kategorii tylko trzydzieści sześć podaje cenę za tonę. Reszta wpisuje gołą liczbę, często zaniżoną, żeby wypaść wyżej przy sortowaniu po cenie. Uczciwa cena z jednostką odróżnia Waszą ofertę od tych, które wyglądają tanio tylko na liście.

**Przy okazji sprawdziliśmy obawę o tanią konkurencję i wygląda ona inaczej, niż się wydaje.** Wasze ceny są w rynku w każdej porównywalnej pozycji: wapno węglanowe 57 zł/t przy 57,40 zł/t z kopalni Morawica, kreda 125 zł/t przy 185 zł/t u konkurencji, wapno tlenkowe 220 zł/t przy 210 zł/t u najbliższego dostawcy. Te naprawdę tanie oferty to w dużej części **wapno nieatestowane** — odsypy z wagi po 78 zł za tonę, sprzedawane obok atestowanego po 210 zł przez tego samego sprzedawcę. To nie jest ten sam produkt. Nie ma sensu z tym konkurować ceną; ma sens pokazywać atest, co robimy w każdym opisie.

**Gdzie wystawiamy — i dlaczego nie wszędzie.**

Dotychczas była to jedna oferta powielona na 18 miast. Teraz każdy produkt ma własne ogłoszenie i **własną listę miejscowości**, policzoną, a nie dobraną na oko. Braliśmy pod uwagę, ile razy w danym województwie ludzie szukają Waszych produktów w Google, ilu różnych sprzedawców wapna jest już w danym mieście, i — najważniejsze — **ile kosztuje tam dowieźć tonę w stosunku do jej ceny**.

Ten ostatni czynnik przesądza o wszystkim. Sprzedajecie loco magazyn, a przewóz zestawu 24 t kosztuje mniej więcej 25 groszy za tonę na każdy kilometr. Dla wapna węglanowego po 57 zł za tonę oznacza to, że po stu kilometrach transport dorównuje cenie towaru — więc ogłoszenie tego produktu w Gdańsku byłoby ogłoszeniem, z którego nikt nie kupi. Dla Agrobielika 90 po 750 zł za tonę ten sam Gdańsk to kilkanaście procent ceny, czyli normalna transakcja.

Dlatego **każdy produkt ma inny zasięg**: węglanowe luzem trzymamy w promieniu około stu kilometrów od zakładu, kredę sypką do dwustu pięćdziesięciu, a wapno tlenkowe 90 i palone mielone możemy wozić przez całą Polskę. Razem wychodzi sto ogłoszeń w trzydziestu trzech miejscowościach.

Dwie rzeczy do sprawdzenia po Waszej stronie. Po pierwsze: jeśli realna stawka za transport jest inna niż te 25 groszy za tonokilometr, dajcie znać — przeliczymy siatkę, bo to ona wyznacza całą geografię. Po drugie, przydatne odkrycie: **część produktów nie jedzie z Niedomic**. Kreda nawozowa granulowana wysyłana jest z Kornicy pod Siedlcami, więc na Mazowszu i Podlasiu jest w dostawie znacznie tańsza, niż wynikałoby z odległości od Tarnowa. To poszerza zasięg, o którym pewnie nie myśleliście w tych kategoriach.

**Ile to może dać.**

Policzyliśmy na Waszych danych, na grupie szesnastu ogłoszeń o znanej historii publikacji. Przy stu ogłoszeniach i pakiecie utrzymywanym bez przerw:

- ostrożnie: **około 25 telefonów miesięcznie**,
- realnie: **około 75**,
- optymistycznie, jeśli tytuły pod zastosowanie zadziałają tak jak „Do stawu": **około 115**.

Przy koszcie kanału 1 020 zł miesięcznie wychodzi **od 9 do 41 zł za jeden telefon od zainteresowanego**.

**Koszty — całość, żeby był pełny obraz.**

| Pozycja | Miesięcznie | Do kogo trafia |
|---|---|---|
| Opieka nad stroną i pozycjonowanie | 2 000 zł netto | Auranet |
| Budżet reklamowy Google | 1 200 zł netto | Google |
| Prowadzenie kampanii Google Ads | 600 zł netto | Auranet |
| **Pakiet 100 ogłoszeń OLX** | **720 zł brutto** | **OLX** |
| **Prowadzenie OLX** | **300 zł netto** | **Auranet** |

Trzy pierwsze pozycje to ustalone wcześniej 3 800 zł. **OLX dokłada 720 zł do OLX i 300 zł do nas.** Do tego **jednorazowo 1 800 zł netto za uruchomienie kanału** — sto ogłoszeń, analiza rynku, model doboru miejscowości i narzędzia, które to wystawiają i mierzą. Część tej pracy jest już wykonana; fakturujemy ją raz i nie wraca.

Z tych kwot **1 200 zł idzie do Google, a 720 zł do OLX** — to nie jest nasze wynagrodzenie, tylko opłata za wyświetlanie. Jedna uwaga do pakietu OLX: jest ważny 30 dni, więc to opłata cykliczna. Pilnujemy terminu i przypominamy przed wygaśnięciem, żeby nie powtórzyła się sytuacja z 18 lipca.

**Dlaczego uruchomienie kosztuje więcej niż prowadzenie.** Bo tak to naprawdę wygląda. Ciężka praca jest na starcie — sto ogłoszeń, przegląd kategorii, model geografii, narzędzia. Potem **kanał w dużej mierze chodzi sam**: ogłoszenia odnawiają się automatycznie, dopóki pakiet jest opłacony. Prowadzenie to odczyt danych, wygaszenie ofert bez wyników, powielenie tych, które łapią, podmiana cen gdy się zmienią, i cotygodniowy podgląd, co robi konkurencja. Nie ma powodu brać za to tyle, co za prowadzenie kampanii reklamowych.

**Harmonogram — te same trzy miesiące co reklamy.**

- **po Waszej akceptacji** — zakup pakietu i wystawienie stu ogłoszeń, to kwestia jednego dnia,
- **koniec sierpnia** — pierwszy pomiar i korekta tytułów oraz miejscowości na podstawie danych,
- **wrzesień i październik** — prowadzenie, rotacja ofert, obserwacja konkurencji,
- **koniec października** — podsumowanie razem z reklamami: ile zapytań, z których produktów i miejscowości, jakim kosztem. Na tej podstawie decydujecie, czy idziemy dalej i w jakiej skali.

Nic nie przedłuża się samo. Sierpień, wrzesień i październik to szczyt sezonu dla rolnictwa, a listopad domyka wapno palone — dlatego zależy nam, żeby ruszyć w tym tygodniu, a nie od września. Każdy tydzień zwłoki to tydzień szczytu, którego się nie odrobi.

Na później jedna rzecz: zestaw produktów i miejscowości jest dobrany pod sezon rolniczy. W okolicach listopada wypada go przestawić — wapno palone wchodzi w swój szczyt, a zimą sensowniejsze są kreda pastewna i wapno hydratyzowane pod budownictwo. Wrócimy do tego przy podsumowaniu października.

**Za co bierzemy odpowiedzialność, a czego nie obiecujemy.** Odpowiadamy za to, że ogłoszenia będą poprawnie zbudowane, zgodne z regulaminem OLX, oparte na Waszych realnych parametrach i cenach, że nie będą gasnąć po cichu i że co tydzień będziemy wiedzieć, które działają, a które nie. Nie obiecujemy konkretnej liczby zamówień — na to wpływa cena, dostępność, transport i sezon, a te rzeczy są poza kanałem. Obiecujemy natomiast, że pod koniec października będziecie mieli twarde liczby do decyzji, a nie wrażenia.

Jeszcze jedno, drobne, ale warte zrobienia: konto OLX działa na prywatnym adresie Gmail, a hasło przyszło do nas zwykłym mailem. Warto je zmienić i włączyć logowanie dwuskładnikowe.

Dajcie akcept, a kupujemy pakiet i ogłoszenia idą na antenę tego samego dnia.

Pozdrawiam,
Janek
