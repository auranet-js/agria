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
| Wycena Auranet | **Setup 1 500 zł netto jednorazowo + 300 zł netto/mies.** Zatwierdzone przez Janka 07.08 |
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

Stąd 300 zł/mies., nie 800. Setup 1 500 zł pokrywa research z 07.08 (panel, 1 204 ogłoszenia rynku, regulamin, korekty cenowe), 100 gotowych ogłoszeń z parametrami i zdjęciami, pipeline API oraz uruchomiony pomiar. **Dzisiejszy czas jest zaszyty w setupie — bez osobnej pozycji „analiza" w mailu.**

Rewizja sezonowa nie wchodzi do tej wyceny — pojawi się jako osobna pozycja, gdy wypadnie (najbliższa: listopad).

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

## Treść maila

Cześć Kasjan, Paweł,

Paweł pytał, czy kupować dalej pakiet 30 ogłoszeń, czy wziąć mniejszy i skupić się na promowaniu. Sprawdziliśmy to na danych — Waszych i rynkowych — i odpowiedź jest jednoznaczna, więc zaczynam od niej.

**Wolumen, nie promowanie. I taniej niż dotychczas za ogłoszenie.**

Dotychczas kupowaliście Megapakiet na 20 ogłoszeń za 336 zł. W kategorii Nawozy jest pakiet, w którym **100 ogłoszeń kosztuje 720 zł** — czyli 7,20 zł za ogłoszenie zamiast 16,80 zł. Pięć razy więcej ogłoszeń za dwukrotnie wyższą kwotę.

Promowanie wypada blado w porównaniu: jedno wyróżnienie na 30 dni kosztuje 105 zł, czyli tyle, co dziewięć ogłoszeń. Rynek to potwierdza — dwaj najwięksi sprzedawcy w tej kategorii mają odpowiednio **zero i 24 promowania przy 191 i 161 ogłoszeniach**. Wygrywają liczbą ofert i tym, w ilu miejscowościach są widoczni, a nie wyróżnieniami.

**Koszty:**

| Pozycja | Kto płaci | Kwota |
|---|---|---|
| Pakiet 100 ogłoszeń OLX | AGRIA, bezpośrednio do OLX | **720 zł brutto miesięcznie** |
| Wyróżnienia i promowania | — | **0 zł** — świadomie nie wchodzimy |
| Uruchomienie kanału | Auranet | **1 500 zł netto, jednorazowo** |
| Prowadzenie | Auranet | **300 zł netto miesięcznie** |

**720 zł to nie jest nasze wynagrodzenie** — te pieniądze idą w całości do OLX za publikację ogłoszeń, tak samo jak budżet reklamowy idzie do Google. Uwaga: pakiet jest ważny 30 dni, więc to opłata cykliczna, nie jednorazowa.

**Dlaczego uruchomienie kosztuje więcej niż prowadzenie.** Bo tak to naprawdę wygląda. Uruchomienie to sto ogłoszeń z parametrami wziętymi z Waszych kart produktowych, dobór miejscowości pod każdy produkt, przegląd całej kategorii na OLX, sprawdzenie regulaminu i zbudowanie narzędzia, które wystawia i mierzy to automatycznie. Potem **kanał w dużej mierze chodzi sam** — ogłoszenia odnawiają się automatycznie, dopóki pakiet jest opłacony. Prowadzenie to odczyt danych, wygaszenie ofert, które nie działają, powielenie tych, które łapią, i podmiana cen, gdy się zmienią. Nie ma powodu, żeby brać za to tyle, co za prowadzenie kampanii reklamowych.

**Co pokazały Wasze własne dane.**

Konto ma dziś jedno aktywne ogłoszenie — 17 wygasło 18 lipca razem z końcem opłaconego pakietu. Przez cały czas działania te ogłoszenia zebrały **7 273 wyświetlenia i 209 odsłon numeru telefonu**. Dla porównania: cały ruch z Google na agria.pl dał w lipcu 221 kliknięć. **To nie jest kanał poboczny.**

Dwie rzeczy z tych danych warto wiedzieć:

**Pierwsza — tytuł decyduje.** Ogłoszenie zatytułowane „Do stawu…" zebrało 94 odsłony telefonu, czyli **45% wszystkich kontaktów z całego konta**. Ta sama oferta, te same zdjęcia, ale tytuł mówiący, do czego to służy, zamiast „Najtaniej!". Dlatego nowe ogłoszenia budujemy pod konkretne zastosowanie: do stawu, na odkwaszanie gleb ciężkich, pod rzepak, do paszy.

**Druga — ogłoszenia gasły po cichu.** Automatyczne przedłużanie było włączone na jednym ogłoszeniu z dwudziestu. To jedno przedłużyło się 18 lipca o 8:43, kwadrans przed wygaśnięciem pakietu — i dlatego jako jedyne żyje do dziś. Pozostałych siedemnaście zgasło tego samego ranka. Przy nowych ogłoszeniach automatyczne przedłużanie ustawiamy od razu na wszystkich.

Warto przy tym wiedzieć, że przedłużanie działa **tylko dopóki pakiet jest opłacony**. To ogłoszenie, które przetrwało, spróbuje odnowić się 17 sierpnia i też padnie, jeśli pakietu nie będzie. Dlatego pakiet trzeba odnawiać co miesiąc — pilnujemy tego my i przypominamy przed terminem.

**Co uruchamiamy:**

**100 ogłoszeń: dziesięć produktów rozstawionych w 56 miejscowościach.** Dotychczas była to jedna oferta powielona na 18 miast — teraz każdy produkt dostaje własne ogłoszenie z własnymi parametrami, a miejscowości dobieramy pod segment: wapno do stawów w rejonach stawowych, kreda pastewna w rejonach drobiarskich, wapno na odkwaszanie w rejonach o intensywnej produkcji roślinnej.

Ogłoszenia dostają parametry prosto z kart produktowych ze strony — zawartość CaO, reaktywność, frakcję, dawkowanie, producenta — plus cenę **z jednostką i informacją, że jest netto loco magazyn**. To brzmi drobiazgowo, ale jest istotne: w tej kategorii większość ogłoszeń podaje w polu ceny liczbę bez jednostki, często zaniżoną, żeby wypaść wyżej przy sortowaniu po cenie. Na 1 204 ogłoszenia tylko 36 podaje cenę za tonę. Uczciwa cena z jednostką odróżnia ofertę od tych, które wyglądają tanio tylko na liście.

**Przy okazji sprawdziliśmy obawę o tanią konkurencję.** Wasze ceny są w rynku w każdej porównywalnej pozycji — wapno węglanowe 57 zł/t przy 57,40 zł/t z kopalni Morawica, kreda 125 zł/t przy 185 zł/t u konkurencji, wapno tlenkowe 220 zł/t przy 210 zł/t u najbliższego dostawcy. Tanie oferty, które widać na OLX, to w dużej części **wapno nieatestowane** — odsypy z wagi po 78 zł za tonę, sprzedawane obok atestowanego po 210 zł przez tego samego sprzedawcę. To nie jest ten sam produkt i nie ma sensu z tym konkurować ceną. Ma sens pokazywać atest.

**Ile zapytań to może dać.**

Policzyliśmy to na Waszych danych, nie na wróżeniu — na grupie 16 ogłoszeń o znanej historii publikacji. Przy 100 ogłoszeniach i pakiecie utrzymywanym bez przerw:

- ostrożnie: **około 25 telefonów miesięcznie**,
- realnie: **około 75**,
- optymistycznie, jeśli tytuły pod zastosowanie zadziałają tak jak „Do stawu": **około 115**.

Licząc wszystko, co kanał kosztuje miesięcznie — pakiet i prowadzenie razem, czyli 1 020 zł — wychodzi **od 9 do 41 zł za jeden telefon od zainteresowanego**.

**Za co bierzemy odpowiedzialność, a czego nie obiecujemy.** Odpowiadamy za to, że ogłoszenia będą poprawnie zbudowane, zgodne z regulaminem OLX, oparte na Waszych realnych parametrach i cenach, że nie będą gasnąć po cichu i że co tydzień będziemy wiedzieć, które działają, a które nie. Nie obiecujemy konkretnej liczby zamówień — na to wpływa cena, dostępność, transport i sezon, a te rzeczy są poza kanałem. Obiecujemy natomiast, że pod koniec października będziecie mieli twarde liczby do decyzji.

**Harmonogram — te same trzy miesiące co reklamy.**

- **połowa sierpnia** — zakup pakietu i wystawienie stu ogłoszeń,
- **koniec sierpnia** — pierwszy pomiar i korekta tytułów oraz miejscowości na podstawie danych,
- **wrzesień i październik** — prowadzenie, rotacja ofert, reagowanie na to, co się sprawdza,
- **koniec października** — podsumowanie razem z reklamami: ile zapytań, z których produktów i miejscowości, jakim kosztem. Na tej podstawie decydujecie, czy idziemy dalej i w jakiej skali.

Nic nie przedłuża się samo. Sierpień–październik to szczyt sezonu dla rolnictwa, więc to jest właściwy moment, żeby to sprawdzić — a listopad domyka jeszcze wapno palone.

Jedna rzecz na później: zestaw produktów i miejscowości jest dobrany pod sezon rolniczy. W okolicach listopada wypada go przestawić — wapno palone wchodzi w swój szczyt, a zimą sensowniejsze są kreda pastewna i wapno hydratyzowane pod budownictwo. Wrócimy do tego, gdy będziemy podsumowywać październik.

**Dwie rzeczy do Was.**

Konto OLX działa na prywatnym adresie Gmail, a hasło przyszło do nas zwykłym mailem. Warto je zmienić i włączyć logowanie dwuskładnikowe.

I druga: ceny w ogłoszeniach ustawiamy zgodnie z cennikiem, który Paweł przysłał 7 sierpnia. Jeśli coś się w nim zmieni, dajcie znać — poprawimy we wszystkich ogłoszeniach naraz.

Jeśli nie macie uwag, kupujemy pakiet i ruszamy.

Pozdrawiam,
Janek
