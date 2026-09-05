# Czy rozbudowa kategorii kanibalizuje — i co realnie zyskujemy (T-092)

**Data:** 2026-09-04 · **Pytanie:** przed wdrożeniem T-092 sprawdzić, czy rozbudowa
`/wapno-nawozowe-rolnictwo/` nie pogłębi kanibalizacji ze stroną główną, i co konkretnie zyskujemy.
**Źródła:** GSC Search Analytics 05.06–01.09 (`dataState: final`), DataForSEO SERP live
(Polska i województwo małopolskie, desktop), render produkcyjny.

## 1. Zaskoczenie: organicznie nas na tej frazie nie ma wcale

SERP na żywo dla `wapno nawozowe`, 04.09:

| Zasięg | Pozycja agria.pl w wynikach organicznych |
|---|---|
| Polska (`location_code` 2616), TOP33 | **brak** |
| Małopolska (`location_code` 20852), TOP30 | **brak** |

Za to w Małopolsce SERP zawiera **12-pozycyjny pakiet lokalny**, a w nim wizytówka
**AGRIA Sp. z o.o. — Wapna Nawozowe na pozycji 16**. Konkurenci stoją wyżej z wizytówkami nazwanymi
wprost pod frazę: AGRO Diogra (6), Eko-Wap (7), Wamex (8), Agrokan (15).

**Konsekwencja dla pytania o kanibalizację:** dwa nasze adresy nie odbierają sobie miejsca w TOP10,
bo żaden go nie zajmuje. Pozycje z GSC (strona główna 6,5 · kategoria 11,0) są średnimi po zapytaniach,
lokalizacjach i urządzeniach — nie odpowiadają żadnemu SERP-owi, który da się dziś zobaczyć.

W SERP-ie krajowym jest też **AI Overview** — ta sama sytuacja, którą widać w kontroli CTR huba z 04.09.

## 2. Sygnał grupowy jednak potwierdza zasadę „jedna intencja, jeden adres"

Metoda z ADR 11.08 powtórzona na 90 dniach GSC. Pierwsze podejście dało wynik odwrotny do
oczekiwanego — bo liczyło frazy brandowe (gdzie mamy wiele URL-i i świetne pozycje) oraz „drugie URL-e"
z czterema wyświetleniami. Po odfiltrowaniu brandu i policzeniu tylko URL-i o istotnym udziale
(≥20% wyświetleń lidera):

| Realnie konkurujących URL-i | Fraz | Średnia pozycja | Wyświetlenia | CTR |
|---|---|---|---|---|
| 1 | 62 | **10,1** | 10 231 | 0,47% |
| 2 | 17 | **17,6** | 2 047 | 0,20% |
| 3+ | 10 | **22,5** | 1 090 | 0,37% |

Zależność jest wyraźna i zgodna z ADR: im więcej naszych adresów realnie walczy o jedną frazę,
tym niżej stoimy. **To argument, żeby nie mnożyć adresów — ale rozbudowa kategorii żadnego nowego
adresu nie tworzy.** Wzmacnia jeden z dwóch już istniejących.

## 3. Skąd bierze się dublowanie na tej frazie

Title strony głównej: **„Wapno nawozowe, hydratyzowane i palone – AGRIA Sp. z o.o."**, description
otwiera się słowami „AGRIA – wapno nawozowe tlenkowe i węglanowe…". Fraza `wapno nawozowe` stoi więc
na pierwszej pozycji w title dwóch różnych stron. W GSC widać tego skutek: 32 dni z danymi to sama
kategoria, 6 dni sama strona główna, 7 dni oba — a w ostatnim tygodniu sierpnia oba równolegle,
przy czym strona główna trzyma pozycję ok. 5, kategoria ok. 11.

Strona główna łapie łącznie **86 fraz przy pozycji ważonej 23,3** — głównie geograficzne
(`wapno kraków`, `wapno sosnowiec`, `wapno dolnośląskie`, `wapno ostrów wielkopolski`). Jest workiem
na wszystko, nie stroną o wapnie nawozowym.

## 4. Co realnie zyskujemy rozbudową kategorii

**Nie awans na `wapno nawozowe` — tam sufit stawia co innego.** SERP na tę frazę zajmują rozbudowane
kategorie sklepowe (agrosklad 1–2, biovita 3–4, dlaroslin 10) i teksty poradnikowe (industria.eu ×2,
nawozy.eu, tagro, doradcatechmot). Nasza kategoria ma dziś **958 znaków** — nie ma czym konkurować,
a rozbudowa jest warunkiem wejścia do gry, nie gwarancją wyniku.

**Realny, bliższy zysk leży na frazach formowych**, gdzie już mamy wyświetlenia, ale rozstrzeliwują
je karty produktów walczące ze sobą:

| Fraza | Wyświetlenia | Ile naszych URL-i | Pozycje |
|---|---|---|---|
| `wapno nawozowe węglanowe` | 150 | 3 karty | 19,9 · 28,3 · 25,9 |
| `wapno nawozowe tlenkowe` | 141 | 3 URL-e | 13,4 · 17,7 · 11,5 |
| `wapno węglanowe` | 818 | 5 URL-i | 9,8 · 35,3 · 41,3 |
| `wapno węglanowe granulowane` | 122 | 3 URL-e | 22,8 · 34,4 · 2,1 |

To jest dokładnie profil z wiersza „3+ URL-e → pozycja 22,5". Kategoria z osobnymi sekcjami
o formach tlenkowej i węglanowej jest naturalnym kandydatem, żeby te frazy **skonsolidować pod jednym
adresem** — czyli rozbudowa działa tu przeciw kanibalizacji, nie na jej rzecz.

## 5. Warunki, żeby nie pogłębić rozproszenia

1. **Sekcje o dawce i terminie zostają krótkie i linkują dalej.** Hub `/wapnowanie-gleby/` trzyma
   `ile wapna na hektar` na pozycji 7,7 z 1 961 wyświetleniami, terminarz obsługuje oś „kiedy”.
   Projekt treści to spełnia — obie sekcje to po jednym akapicie z linkiem.
2. **Nie powstaje żaden nowy adres.** Wariant „zróbmy landing `/wapno-nawozowe/`” jest unieważniony
   (T-035) i nic się w tej sprawie nie zmienia.
3. **Do rozstrzygnięcia osobno, poza T-092:** przestawić title strony głównej tak, żeby nie otwierał
   się frazą `wapno nawozowe`. To jest właściwy ruch antykanibalizacyjny — dziś dwie strony celują
   w jedną frazę, a ta słabsza treściowo (kategoria) ma być tą docelową.
4. **Drugi wątek poza T-092: pakiet lokalny.** Na tę frazę w Małopolsce Google pokazuje mapę,
   a my jesteśmy w niej szesnaści, za konkurentami, których wizytówki nazwane są wprost pod frazę.
   Wiąże się z pozycjami GBP (T-046, T-047, T-050).

## 6. Zgodność z wcześniejszymi decyzjami — przegląd 04.09

**Potwierdzone (rozbudowa jest wprost tym, co ustalono):**

- **ADR `2026-08-11-podzial-rol-ads-seo.md`**: „Kategoria `/wapno-nawozowe-rolnictwo/` = **jedyna** strona
  organiczna na «wapno nawozowe»". Rozbudowa realizuje ten zapis, nie odchodzi od niego.
- **Audyt 24.08 §5**: term 764 „**zostaje jako kategoria, do wzmocnienia treścią**".
- **Memory `nowe_adresy_nie_wchodza_do_indeksu`**: 0 z 10 nowych adresów pobranych przez Google od 09.07.
  Rozbudowa adresu crawlowanego 21.08 to jedyny kanał z dowodem, że dociera w dniach.
- **Ceny**: memory `ceny_strategia` — „zero ceny obowiązuje nadal dla fraz ogólnych". Opis bez kwot,
  z odesłaniem do kart, gdzie kwoty są (15 z 19).
- **Timing**: pełna seria 12-miesięczna z etykietami (nie ucięta — memory `sezon_sierpniowy`):
  `wapno nawozowe` 2025-08 **1 900** · 2025-09 **1 900** · 2025-10 **1 900**, dołek 2025-12 = 590.
  Wrzesień jest w szczycie, publikacja 05.09 trafia w okno.

**Skorygowane w wyniku tego przeglądu:**

1. **Nazwa „Nordkalk" wypada z treści.** T-040 czeka na potwierdzenie statusu autoryzowanego
   dystrybutora („użyć w treści — tylko odsprzedawcy, **nie zgadywać**"). Na produkcji nazwa występuje
   dziś wyłącznie jako **wartość atrybutu „Producent"** w tabeli parametrów karty — to fakt o towarze,
   nie deklaracja relacji handlowej. Projekt zawierał zdanie „Agrobielik to marka Nordkalku, którego
   wapna dystrybuujemy" — usunięte, zastąpione odesłaniem do karty produktu.
2. **Zmiana miary powodzenia.** Proponowałem `wapno nawozowe tlenkowe` i `wapno nawozowe węglanowe` —
   pomiar wolumenu (DataForSEO, 04.09) pokazuje, że to frazy śladowe: **50 i 40 wyszukań/mies.**
   Właściwe frazy formowe to te **bez słowa „nawozowe"**: `wapno węglanowe` **1 000**,
   `kreda nawozowa` **1 000**, `wapno tlenkowe` **720**. Na `wapno węglanowe` mamy dziś 818 wyświetleń
   rozbitych na **pięć** URL-i (9,8 · 35,3 · 41,3 · …) — to jest właściwy cel konsolidacji.
3. **Czym mierzyć.** DataForSEO pokazuje wyniki dla nowych treści z opóźnieniem, więc postęp po
   wdrożeniu czytamy **z GSC** (pozycja i wyświetlenia per fraza × URL), a DFS służy do obrazu
   konkurencji i wolumenu, nie do oceny naszego ruchu.

**Zauważone przy okazji, poza zakresem T-092:**

- Wniosek „nie ma nas w TOP30" **nie jest nowym odkryciem** — memory `architektura_kanalow` notuje
  z 11.08: „poza TOP20 na wszystkich 6 frazach head, **local_pack ×12 na «wapno nawozowe»**".
  Dzisiejszy pomiar to potwierdza i uszczegóławia: jesteśmy **szesnaści w pakiecie lokalnym**.
- **Liczba „3 996 znaków i 3 × H2" pochodzi z audytu 24.08** (§5 i harmonogram Fazy 1), stamtąd weszła
  do rejestru. Realnie 958 znaków. **Ten sam typ zawyżenia dotyczy `/paszarstwo/`** — audyt podaje
  „3 083 znaki", a `term_taxonomy.description` ma **465 bajtów**. T-078 (termin 12.09) stoi więc
  na tej samej zawyżonej liczbie.
- **Strona główna celuje title w tę samą frazę wbrew ADR 11.08** — „Wapno nawozowe, hydratyzowane
  i palone – AGRIA Sp. z o.o.". Skoro kategoria ma być jedyną stroną organiczną na tę frazę,
  to jest odstępstwo do rozstrzygnięcia.
- **`wapno magnezowe` to największy klaster w portfelu**: 1 900/mies., szczyt 2025-08 **4 400**,
  wrzesień 2 900, październik 3 600 — więcej niż `wapno nawozowe`. Temat jest zaparkowany (T-060),
  a moduł magnezowy kalkulatora wszedł na produkcję 04.09. Do decyzji Janka, nie ruszam.

## Werdykt

**Rozbudowę wykonać.** Nie tworzy nowego adresu, więc nie dokłada kanibalizacji; naprawia stronę,
która jest właściwym typem dla tej intencji, a treściowo jest pusta. Zysku nie należy jednak
obiecywać na frazie `wapno nawozowe` — tam jesteśmy poza TOP30 i sam tekst tego nie odwróci.
Miarą powodzenia są **frazy formowe** (`wapno nawozowe tlenkowe`, `wapno nawozowe węglanowe`)
i to, czy kategoria zacznie je przejmować od kart. Kontrola za 14 dni od wdrożenia,
na tych frazach, nie na frazie głównej.
