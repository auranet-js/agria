# Ofertownik AGRIA — projekt narzędzia

> Spec projektowy. Powstał 18.08.2026 z rozmowy Janek ↔ Claude, po tym jak rozpiska
> 200 ogłoszeń OLX (`agria-olx-ogloszenia-final-2026-08-17.html`) pokazała AGRII
> tabelę „miejscowość → zakład wysyłkowy → km → udział transportu w cenie" i wywołała
> pytanie: „a czy tak nie dałoby się wyceniać przy telefonie?".
>
> Status: **projekt do akceptu**. Nie plan wdrożenia, nie oferta. Kwoty i harmonogram
> powstaną osobno, po decyzji.

---

## 1. Problem

Klient dzwoni i pyta o cenę wapna. Handlowiec musi w trakcie rozmowy złożyć trzy rzeczy:
cenę towaru, koszt przewozu z **właściwego** zakładu (a ten jest inny dla każdego produktu)
i przeliczenie jednostek, w których klient myśli — hektary, worki, palety — na tony,
w których liczy się cena. Dziś robi to z głowy i na kartce.

Skutki, które z tego wynikają:

- **wycena trwa** — albo klient czeka przy telefonie, albo słyszy „oddzwonię";
- **cena bywa policzona z sufitu** — zwłaszcza transport, bo trzeba pamiętać, że kreda
  granulowana jedzie z Kornicy, a Agrobielik z Niedomic albo Sitkówki;
- **nikt nie widzi obrazu** — ile było wycen, z jakiego kanału (OLX / reklama / strona /
  polecenie), o ile schodzono z ceny, co z tego się zamknęło;
- **niedosprzedane auto** — transport płaci się za pojazd, nie za tonę, więc klient
  zamawiający 12 t płaci za przewóz tyle samo co przy 24 t, ale nikt mu tego nie mówi.

Narzędzie ma zamienić to w jeden ekran, który odpowiada w trakcie rozmowy.

**Użytkownik:** handlowiec AGRII przy telefonie. Kilku–kilkunastu wycen dziennie.
Nie sklep internetowy, nie samoobsługa dla rolnika — narzędzie wewnętrzne.

---

## 2. Gdzie to żyje

**Osobna wtyczka `agria-ofertownik-by-auranet`** na agria.pl — nie moduł w `agria-by-auranet`
(decyzja Janka 18.08.2026).

Narzędzie stoi na stronie AGRII, bo tam są produkty z parametrami i zdjęciami oraz konta
zespołu; osobna instancja wymagałaby przepisania tych 19 produktów i pilnowania, żeby się
nie rozjechały. Ale **własna wtyczka, nie moduł tamtej** — z trzech powodów:

- `security-geoblock.php` nosi w nagłówku ostrzeżenie, że reinstalacja albo nadpisanie
  `agria-by-auranet` kasuje blokadę bez śladu. Każde wgranie tamtej wtyczki jest okazją
  do zdjęcia geobloku po cichu; ofertownik obok redukuje liczbę takich okazji do zera;
- ofertownik można włączyć i wyłączyć jednym kliknięciem, nie ruszając niczego,
  co obsługuje stronę sprzedażową;
- rozwój i testy idą na żywym serwerze bez ryzyka dla działającej witryny.

**Praca i testy na produkcji są tu dopuszczalne** — zespół AGRII nie korzysta na co dzień
z panelu, a wtyczka nic nie renderuje dla odwiedzających. Warunek zostaje jeden i twardy:
dopóki nie dotyka danych sklepu. Wyjątek od tego warunku — konwersja produktów na wariantowe
— jest opisany w 7.3 i wymaga osobnej próby.

### 2a. Zależności od `agria-by-auranet`

Ofertownik korzysta z dwóch rzeczy tamtej wtyczki, ale **żadna nie jest wymagana do działania**:
`liming-calculator` (przeliczanie hektarów na tony) i CPT `agria_inquiry` (zapytania ze strony,
etap 3). Obie sprawdzane przed użyciem; gdy ich nie ma, odpowiednie pole po prostu się nie
pojawia. Wyłączenie jednej wtyczki nie może psuć drugiej.

Prefiks funkcji i opcji: `agria_of_` — rozłączny z `agria_` tamtej wtyczki. Typy wpisów
zostają w rodzinie nazw (`agria_quote`, `agria_client`), bo to kwestia czytelności listy
w panelu, nie kolizji.

**Ekran pod `/wycena/`** — pełnoekranowy front za logowaniem, nie wp-admin. Handlowiec
trzyma to otwarte przez cały dzień; wp-admin ładuje się wolniej i ma pasek boczny,
który tu do niczego nie służy. Adres za logowaniem jest z definicji poza cache CDN
nazwa.pl, więc znany problem z podmianą treści go nie dotyczy.

**Izolacja od sklepu.** Moduł nie zmienia niczego, co widzi rolnik wchodzący z reklamy:
własny szablon, własne typy wpisów, zero ingerencji w koszyk, checkout i karty produktów.
Jedyny punkt styku to warianty produktów (rozdz. 4.1) — i on wymaga audytu z rozdz. 7.

---

## 3. Stan zastany (zweryfikowany 18.08.2026 przez MCP)

**Środowisko:** WP 7.0.4, WooCommerce 10.9.3, PHP 8.3.33, motyw `Agria By Auranet 2.0.0`,
wtyczka `agria-by-auranet v1.0.0`, prefix `wpfz_`, hosting nazwa.pl (server371853).

**Moduły wtyczki:** `catalog-mode`, `inquiry-form`, `liming-calculator`, `product-video`,
`scroll-to-top`, `seo-head`. Autoloader ładuje je z `modules/<nazwa>/<nazwa>.php`
na `plugins_loaded` priorytet 5.

Dwa z nich ofertownik wykorzystuje:

- **`liming-calculator`** — przelicza hektary i pH na dawkę. Klient mówi „12 ha gleby
  lekkiej", handlowiec dostaje tonaż bez liczenia. (Rozszerzenie o moduł magnezowy
  jest w testach u Kazimierza — `mockups/agria-kalkulator-mg-test-2026-08-18.html`.)
- **`inquiry-form`** — zapisuje zapytania ze strony jako CPT `agria_inquiry`
  (8 wpisów, ostatni 13.08.2026). Gotowe wejście leadów, do podpięcia w etapie 3.

**Konta:** `js` (administrator), `pb` — Paweł Bigos (administrator), `kn` — Kazimierz
Nowak (editor). Dochodzi rola `agria_handlowiec`.

**Produkty:** 19 sztuk, wszystkie proste (**zero wariantów w bazie**), SKU `AGR-001`…
`AGR-018` przy 18 z 19 — brak przy ID 303 (Kreda czarna jeziorna).
**Wszystkie mają `_price = NULL`** — tryb katalogu, żadnej ceny w bazie.

**Atrybuty — osie przyszłego cennika istnieją:**

| Taksonomia | Termów | Przypisań | Uwaga |
|---|---|---|---|
| `pa_agria-lokalizacja` | 17 | 37 | zakłady z kodami pocztowymi; produkty mają po kilka |
| `pa_agria-forma-dostawy` | 22 | 34 | Luz, Big-bag 500/600/1000 kg, Worek 10/20/25/30/40 kg |

**Atrybuty są brudne** — pozostałość po buggy imporcie (rozbijanie wartości po przecinkach):

- śmieciowe termy w formach dostawy: `1- 0`, `4`, `4- 0`, `8`;
- ten sam zakład pod trzema nazwami: `Góraźdzce (47-316)` vs `Gorażdże (47-316)`,
  `Chęciny (26-060)` vs `26-060 Chęciny (26-060)`, `Częstochowa ( 42-200 )` vs
  `Częstochowa (42-200)`;
- forma zlepiona z ładownością: `Luz 24 t`, `Luz 14–16 t`, `Luz (25–27 t)`;
- martwa rodzina taksonomii bez przypisań do produktów: `pa_lokalizacja`,
  `pa_forma-dostawy`, `pa_marka`, `pa_producent`, `pa_frakcja`, `pa_segment`.

**Dane transportowe policzone wcześniej przy OLX** i gotowe do przeniesienia:
`scripts/olx/grid.py` — współrzędne 14 zakładów wysyłkowych, liczenie odległości,
progi opłacalności. `data/olx/siatka-miast.json` — 53 miejscowości × zakład × km.

**Geoblok:** `security-geoblock.php` w trybie ENFORCE przepuszcza tylko Europę.
Bez znaczenia dla handlowca w Polsce; `/wp-admin` i `/wp-json` są jawnie wyłączone z blokady.

---

## 4. Model danych

### 4.1. Cennik — na wariantach WooCommerce

Wiersz cennika = **wariant produktu**, osie to istniejące atrybuty:
`pa_agria-lokalizacja` (z którego zakładu) × `pa_agria-forma-dostawy` (w czym).

Cena wariantu to **cena netto za tonę** danej formy z danego zakładu. Nie cena za worek —
wszystko liczy się na tony, bo tak wygląda handel i tak podane są ceny w ogłoszeniach.

Uzasadnienie wyboru: dochodzi kopalnia albo forma dostawy → dopisujesz term i wariant,
nikt nie rusza kodu. Własna tabela cennika wymagałaby własnego modelu relacji i własnego
panelu na to samo. **Oś zakładu potwierdzona 18.08.2026** — cena tony różni się w zależności od kopalni
i zakładu, więc obie osie zostają. Wariantów wyjdzie ok. 100–150; tworzone jednorazowo
skryptem z cennika, nie ręcznie. Liczba nie jest problemem operacyjnym, bo cała edycja
idzie przez jeden ekran cennika (niżej), a nie przez panel wariantów.

**Trzecia oś tam, gdzie jest potrzebna: frakcja.** Agrobielik 90 ma w cenniku cztery ceny
na jednej karcie WooCommerce — 0–3 mm po 750 zł/t luzem i 850 w big-bagu, 2–8 mm po 850 i 940.
Bez wariantów nie da się tego zapisać; z wariantami wystarczy dołożyć `pa_agria-frakcja`
jako oś dla tego jednego produktu. Przy okazji domyka to otwarte pytanie
z `docs/catalog/CATALOG_VS_WC_GAP.md`.

**Forma dostawy zmienia cenę tony, nie tylko opakowanie.** Agrobielik 70 luzem kosztuje
220 zł/t, ten sam produkt w worku 20 kg — 11,50 zł za sztukę, czyli 575 zł/t. Różnica
dwuipółkrotna. To jest właściwy powód, dla którego cennik musi mieć oś formy: nie chodzi
o wygodę, tylko o to, że bez niej cennika nie da się zapisać.

Ceny opakowań przychodzą od AGRII **za sztukę**, a w wariancie leżą przeliczone **na tonę**.
Ekran wyceny pokazuje obie liczby, bo klient przez telefon pyta „ile za worek".

**Podłoga cenowa.** Część cen została przez AGRIĘ podniesiona, żeby nie schodzić poniżej
poziomu stałych odbiorców. Wariant trzyma więc obok ceny także cenę minimalną; handlowiec
może zejść niżej, ale widzi, że schodzi poniżej podłogi. Nie blokada — ostrzeżenie.

**Edycja przez własny ekran, nie przez panel wariantów.** Jedna tabela wszystkich pozycji
z cenami do wpisania w miejscu, filtrowana po produkcie i zakładzie. Panel wariantów
WooCommerce przy stu pozycjach jest nie do przejścia.

### 4.1a. Skąd bierzemy cennik startowy

Nie z pytania do AGRII — z **`docs/operations/CENNIK_PAWEL_2026-08-07.md`**, czyli cennika,
który Paweł przysłał 7 sierpnia. Pokrywa 15 z 19 kart z podziałem na luz, big-bag i opakowania.

Cennik nie ma podziału na zakłady, a ceny per kopalnia się różnią (4.1). Na start
**powielamy tę samą cenę dla każdego zakładu, z którego dany produkt jedzie**, i AGRIA
różnicuje je potem w ekranie cennika — poprawianie gotowej tabeli jest robotą na godzinę,
wypełnianie pustej na kilka dni.

Bez ceny zostają cztery karty: AGR-004 (tlenkowe z magnezem), AGR-007 (węglanowe bez Mg
odm. 05), AGR-012 (Dolomit) i ID 303 (Kreda czarna jeziorna). Wariant powstaje, cena
zostaje pusta, a ekran wyceny mówi wprost „brak ceny — ustal z Pawłem". Dolomit wart jest
osobnej wzmianki przy rozmowie: fraza „dolomit" to 6 600 wyszukań miesięcznie, największy
wolumen w projekcie.

### 4.2. Zakłady wysyłkowe

Term taksonomii `pa_agria-lokalizacja` + współrzędne w meta termu. Nazwa i kod pocztowy
już tam są; współrzędne przenoszone z `scripts/olx/grid.py` (14 zakładów) i uzupełniane
dla brakujących przez geokodowanie kodu pocztowego.

### 4.3. Stawki transportu

Trzy wiersze w opcji wtyczki. Nie wysyłka WooCommerce — ta liczy według stref adresowych
i nie zna pojęcia „z którego zakładu towar wyjeżdża", a u AGRII cała stawka bierze się
właśnie stąd (ten sam Radom to 90 km z Sitkówki albo 250 km z Niedomic, zależnie od produktu).

| Metoda | Nalicza | Stawka netto | Ładowność | Wozi formy |
|---|---|---|---|---|
| Naczepa | za km, w jedną stronę | 5,50 zł | 24 t | Worek 25/30/40 kg, Big-bag 500/600/1000 kg |
| Beczka silosowa | za km, **z dwóch stron** | 4,80 zł | 24 t | Luz — sypkie, kruszone |
| Wanna | za km, **z dwóch stron** | 4,20 zł | 24 t | Luz — sypkie |
| Kurier paletowy | **za paletę** | 120 zł | — | Worek 25/30/40 kg, Big-bag 500/600/1000 kg |

Kurier ma jedną stawkę krajową i bierze paletę niezależnie od masy, także big-bag
1000 kg (ustalenie z 18.08.2026 — świadomie proste). Odstępstwa, jeśli się zdarzą,
handlowiec poprawia nadpisując kwotę w ofercie; nie ma dla nich reguł w kodzie.

Ładowność 24 t domyślnie dla każdej metody, edytowalna osobno per metoda.

**Paleta to jednostka miejsca na aucie, nie miary towaru.** Już dwa worki po 25 kg
albo jeden 40-kilogramowy zajmują całą paletę — nie da się jej wypełnić w połowie
i nie da się zamówić mniej. Big-bag zajmuje paletę tak samo jak te dwa worki.
Górna pojemność palety per forma dostawy (ile worków, jaka masa) — parametr do ustalenia.

**Uwaga do wcześniejszych wyliczeń:** siatka OLX (`grid.py`) liczyła 6 zł/km w jedną
stronę jako założenie. Realnie wanna to 4,2 × 2 = 8,4 zł/km, więc udziały transportu
w rozpisce OLX są dla towarów sypkich luzem zaniżone mniej więcej dwukrotnie
(kreda 57 zł/t na 200 km to nie 23%, tylko ~70% ceny towaru). Do skorygowania osobno —
poza zakresem tego dokumentu, ale konsekwencja dotyczy doboru miejscowości pod ogłoszenia.

### 4.4. Odległości — pamięć podręczna

Para `zakład ↔ miejscowość` liczona raz przez Google Routes API i zapamiętywana.
Nie dla oszczędności (kilkanaście wycen dziennie mieści się w darmowej puli Google Maps
Platform), tylko po to, żeby drugi telefon z tej samej gminy odpowiadał natychmiast.

Podpowiadanie miejscowości: Google Places, ograniczone do Polski.

Odległość **drogowa, nie w linii prostej** — trasa jest średnio 25–30% dłuższa,
a przy wannie liczonej w dwie strony pomyłka 30% na 200 km to około 500 zł na aucie.

### 4.5. Oferta — CPT `agria_quote`, zamrożona

Spójnie z istniejącym `agria_inquiry`, więc lista, wyszukiwarka i uprawnienia
przychodzą z WordPressa.

Oferta zapisuje **stan z chwili wystawienia**, nie referencje do cennika:

- pozycje: produkt, forma, zakład, ilość w tonach i w jednostce klienta;
- **cena proponowana** (z cennika) **obok ceny podanej** (po korekcie handlowca);
- transport: metoda, kilometry, stawka, liczba kursów, kwota — także proponowana i podana;
- kto wystawił, kiedy, dla kogo, z jakiego kanału przyszedł kontakt;
- status.

Powód zamrożenia: otwarcie oferty sprzed dwóch miesięcy nie może pociągnąć aktualnego
cennika i przeliczyć sumy — dokument przestałby zgadzać się z tym, co klient usłyszał.
Przycisk „przywróć proponowaną" wraca do ceny z chwili wystawienia, nie do dzisiejszej.

**Efekt uboczny wart tyle co reszta:** skoro cena proponowana leży w bazie obok podanej,
różnica jest mierzalna. Widać, o ile schodzi się poniżej cennika — który handlowiec,
na którym produkcie, przy którym kanale, w którym momencie sezonu. Zero dodatkowej pracy
przy formularzu.

### 4.6. Klient — CPT `agria_client`

**Nie** użytkownik WordPressa / klient WooCommerce. Powód konkretny: WordPress wymaga
unikalnego loginu i unikalnego adresu e-mail, a rolnik dzwoniący z komórki maila często
nie poda — dwóch takich klientów to konflikt, obejściem byłyby sztuczne adresy typu
`509xxxxxxx@brak.local`. To zaśmieca tabelę użytkowników, miesza klientów z kontami
zespołu i grozi wysyłką na fikcyjny adres. CPT nie ma tych ograniczeń: identyfikatorem
jest telefon albo NIP, e-mail opcjonalny.

Tworzony automatycznie przy pierwszej ofercie, dopasowywany po numerze telefonu i NIP.

---

## 5. Logika wyceny

### 5.1. Przebieg

1. **Miejscowość** — pole z podpowiedziami Google, ograniczone do Polski.
2. **Produkt** — lista 19 pozycji z wyszukiwarką.
3. **Ilość** — w tonach, hektarach (przez `liming-calculator`), big-bagach albo workach;
   przeliczana na tony po gramaturze z formy dostawy.
4. **Wynik natychmiast** — cena towaru, koszt transportu z rozbiciem na kilometry
   i stawkę, cena za tonę z dostawą, suma.

Każdą liczbę handlowiec może nadpisać, bo negocjuje. Przy każdej nadpisanej — powrót
do proponowanej jednym kliknięciem.

### 5.2. Dobór zakładu

Spośród zakładów, które mają dany produkt w danej formie (czyli mają wariant z ceną),
wybierany jest ten o najkrótszej trasie do klienta. Handlowiec widzi wybór i może go
zmienić — decyduje też dostępność towaru, której narzędzie nie zna.

### 5.3. Dobór pojazdu i koszt przewozu

Metoda wynika z formy towaru. Luz jedzie wanną albo beczką silosową — kurier odpada,
bo nie ma czego postawić na palecie. Formy paletowe mają natomiast **dwie metody naraz**:
naczepę i kuriera.

Rozstrzygamy je bez progu — narzędzie liczy oba warianty i pokazuje tańszy. Zero reguł
do zapamiętania przez handlowca, zero konfiguracji do utrzymania. Punkt zrównania wypada
przy `liczba palet = km / 21,8`, czyli przy 70 km naczepa przejmuje od czwartej palety,
a przy 250 km dopiero od dwunastej. Kurier obsługuje więc dokładnie to, co ma obsługiwać:
drobne zamówienia i pojedyncze palety w dalsze rejony.

Handlowiec widzi wybraną metodę i może ją przełączyć — o dostępności auta wie więcej
niż narzędzie.

```
kursy       = ceil(tony / ładowność metody)
koszt auta  = km × stawka × (2 jeśli metoda liczona z dwóch stron) × kursy
koszt/tonę  = koszt auta / faktyczny załadunek
```

### 5.4. Dopełnienie auta

Transport płaci się za pojazd, nie za tonę. Przy niepełnym ładunku narzędzie pokazuje,
ile brakuje i jak zmieni się cena za tonę po dopełnieniu — np. *„do pełnego auta brakuje
12 t; przy 24 t transport spada z 68 na 34 zł/t"*.

To jedyny element całości, który sam z siebie podnosi średnią wartość zamówienia.

### 5.5. Próg dolny

**Jednostką najmniejszą jest paleta. Ofertownik nie wycenia niczego mniejszego** —
rozstrzygnięcie z 18.08.2026, bez wyjątków i bez komunikatów specjalnych.

Powód jest logistyczny, nie cenowy: kurierzy detaliczni przyjmują przesyłki do 31 kg,
a wapno w worku papierowym i tak nie nadaje się do obiegu paczkowego — pyli i rwie się.
Nawet jeden worek jedzie więc na palecie. Skoro nie ma tańszej drogi, nie ma czego
wyceniać poniżej palety: kto bierze jeden worek, nie potrzebuje oferty.

Praktycznie: liczba palet zaokrągla się w górę, bo palety nie da się wypełnić w połowie.
Dwa worki po 25 kg to już cała paleta — nie ma więc realnego przypadku „poniżej palety",
jest tylko zamówienie tak małe, że nie warte oferty.

Samo małe zamówienie przestaje być problemem cenowym z chwilą wejścia kuriera (5.3):
jedna paleta to 120 zł przewozu, a nie 825 zł za podstawienie naczepy.

### 5.6. Trzy stany transportu

| Stan | Kwota | Co znaczy dla magazynu |
|---|---|---|
| Wyliczony | wg 5.3 | auto do zaplanowania, kwota na fakturze |
| **Gratis (0 zł)** | 0 | **auto do zaplanowania**, koszt wzięty na siebie jako ustępstwo w negocjacji |
| **Odbiór własny** | 0 | **auta nie planujemy**, klient przyjeżdża sam — do uzgodnienia termin i rampa |

Rozróżnienie ma znaczenie operacyjne, nie cenowe: obie opcje dają zero na wycenie
i przeciwną informację dla magazynu. Oba stany zapisywane w ofercie jawnie.

---

## 6. Ekran

Jeden widok, bez przeładowań. Kalkulacja po stronie przeglądarki — wynik pojawia się
w trakcie mówienia, nie po odesłaniu formularza. Serwer robi tylko to, czego przeglądarka
nie umie: pyta Google o trasę (raz na parę), zapisuje ofertę, pobiera dane z GUS.

Wzorzec wizualny: `mockups/agria-kalkulator-mg-test-2026-08-18.html` — ten sam typ
jednoplikowego, samowystarczalnego widoku, do którego AGRIA ma już zaufanie.

Po zapisie: PDF oferty do wysłania albo odczytania.

---

## 7. Etap zerowy — dwie rzeczy przed pierwszą ceną

### 7.1. Audyt wycieku cen

Dziś wszystkie produkty mają `_price = NULL`, więc problem jest hipotetyczny. Po wpisaniu
cen w warianty cena netto per kopalnia staje się daną w bazie, po którą sięga nie tylko
ekran ofertownika: REST API WooCommerce, `wc_get_product`, JetSmartFilters, dane
strukturalne, sitemapa produktowa. Tryb katalogu ukrywa **przycisk kupna** — to nie to
samo co ukrycie ceny wszystkimi kanałami.

Do przejścia przed wpisaniem pierwszej liczby: moduł `catalog-mode` i wszystkie drogi
wyjścia ceny na zewnątrz. Konkurencja AGRII siedzi z nimi na tym samym OLX-ie.

Jeśli audyt wykaże, że szczelne ukrycie jest niepewne — plan awaryjny: cena wariantu
zostaje pusta, a właściwa cena idzie w meta wariantu pod własnym kluczem, niewidocznym
dla WooCommerce. Model danych i ekran edycji pozostają bez zmian.

### 7.2. Sprzątanie atrybutów

Atrybuty w obecnym stanie nie nadają się na osie cennika (rozdz. 3). Do zrobienia:
usunięcie śmieciowych termów, scalenie duplikatów zakładów, rozdzielenie formy dostawy
od ładowności, usunięcie martwych taksonomii, uzupełnienie SKU przy ID 303.

Przy cenniku na wariantach każdy duplikat to osobna cena do wpisania i osobne miejsce,
w którym handlowiec zobaczy „brak ceny". Sprzątanie ma zresztą wartość niezależną
od ofertownika — te same śmieciowe wartości widzi dziś rolnik na kartach produktów.

### 7.3. Próba konwersji na jednym produkcie

Cennik na wariantach wymaga zmiany typu produktu z prostego na wariantowy. **To zmiana
w danych sklepu, nie w naszej wtyczce** — osobna wtyczka przed nią nie chroni. WooCommerce
renderuje produkt wariantowy inaczej niż prosty: zamiast opisu pojawiają się listy wyboru
atrybutów. Możliwe, że w trybie katalogu nie zmieni to niczego widocznego; możliwe też,
że rolnik zobaczy na karcie Agrobielika rozwijaną listę kopalni.

Dlatego: konwersja **jednego** produktu, obejrzenie jego karty na żywo, decyzja. Dopiero
potem pozostałe osiemnaście. Jeśli karta się rozjedzie, do wyboru: ukrycie selektorów
filtrem w module `catalog-mode`, albo powrót do cennika we własnej tabeli — model cen
(zakład × forma × frakcja) i ekran edycji pozostają wtedy bez zmian, zmienia się wyłącznie
miejsce zapisu.

---

## 8. Etapy

**Etap 1 — wycena.** Sprzątnięte atrybuty, warianty z cenami, ekran edycji cennika,
zakłady ze współrzędnymi, stawki transportu, Google Places i Routes, ekran wyceny,
zapis oferty, PDF. Po tym etapie handlowiec przestaje liczyć na kartce.

**Etap 2 — obraz sprzedaży.** GUS po NIP, karta klienta z historią, źródło kontaktu,
statystyka kanałów i rabatów (rozdz. 4.5). Po tym etapie Paweł widzi, który kanał sprzedaje.

**Etap 3 — domknięcie obiegu.** Wycena wielu pozycji na jedno auto z optymalizacją
załadunku, przycisk „wyceń" prosto przy zapytaniu z `agria_inquiry`, wysyłka oferty
do klienta.

---

## 9. Założenia i pozycje otwarte

**Przyjęte, do potwierdzenia u Pawła:**

- ładowność 24 t dla każdej z trzech metod liczonych za kilometr (edytowalna osobno);
- naczepa 5,50 zł/km w jedną stronę; beczka 4,80 i wanna 4,20 z dwóch stron;
- „palety 25, 40" z notatki telefonicznej to gramatury worków (25 i 40 kg) układanych
  na palecie — zgodnie z wartościami `Worek 25 kg` i `Worek 40 kg` w atrybutach.
  **Ile worków wchodzi na paletę i ile ton ona waży — nieustalone.**

**Rozstrzygnięte 18.08.2026 (było otwarte):**

- **cena tony różni się w zależności od kopalni i zakładu** — obie osie zostają
  w cenniku, ok. 150 wariantów, edycja przez jeden ekran zbiorczy;
- **poniżej palety nie ofertujemy w ogóle** — patrz 5.5; paleta jest najmniejszą
  jednostką miejsca na aucie, więc próg jest fizyczny, nie umowny;
- **przewóz małych ilości** — rozwiązany kurierem paletowym po 120 zł za paletę,
  wybieranym automatycznie tam, gdzie wychodzi taniej od naczepy (4.3, 5.3).

**Otwarte, niepilne:**

- kto aktualizuje cennik — Paweł przez ekran edycji czy Auranet przy zmianach;
- czy klient dostaje wycenę na piśmie, czy handlowiec podaje cenę wyłącznie ustnie,
  a zapis służy tylko AGRII.

---

## 10. Czego świadomie nie robimy

- **Wysyłki WooCommerce jako silnika transportu** — strefy adresowe nie znają pojęcia
  „skąd towar jedzie", a własna metoda wysyłki żyje w koszyku, którego ofertownik
  nie używa. Trzy stawki nie potrzebują tej infrastruktury.
- **Klientów jako użytkowników WordPressa** — patrz 4.6.
- **Gotowego CRM-u** — cała wartość siedzi w liczeniu transportu z właściwego zakładu,
  czego żaden CRM nie umie; trzeba by to napisać tak czy inaczej, dokładając abonament
  za funkcje, których kilku handlowców nie użyje.
- **Samoobsługi dla rolnika** — narzędzie wewnętrzne. Kalkulator na stronie dla klienta
  to `liming-calculator`, osobna rzecz o innym celu.
- **Stanów magazynowych i rezerwacji** — narzędzie nie wie, co leży na hałdzie,
  i nie udaje, że wie. Dostępność potwierdza handlowiec.
