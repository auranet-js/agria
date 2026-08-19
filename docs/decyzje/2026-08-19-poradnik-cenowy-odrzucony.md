# Poradnik cenowy odrzucony — cena wchodzi do huba, nie na nowy URL

> Data: 2026-08-19 · Decyzja Janka po analizie danych · Dotyczy: **T-010**, grupa D i E rozpiski
> `docs/operations/CEN_LISTA_URL_2026-08-13.md`

## Decyzja

**Nie tworzymy strony `/ile-kosztuje-wapnowanie-hektara/`.** Treść cenową, którą miała nieść,
dokładamy jako sekcję **„Ile kosztuje wapnowanie" do istniejącego huba `/wapnowanie-gleby/`**.
Link kontekstowy z huba do poradnika (grupa E) staje się bezprzedmiotowy.

## Dlaczego — trzy pomiary

**1. Planowana fraza nie ma wolumenu.** DataForSEO, Polska, PL, 19.08:

| Fraza | Wolumen/mies. | CPC |
|---|---|---|
| `wapno granulowane cena` | 480 | 0,28 |
| `ile kosztuje tona wapna` | 110 | 0,78 |
| `wapno nawozowe cena` | 90 | 0,14 |
| **`ile kosztuje wapnowanie hektara`** | **brak danych** | — |
| **`koszt wapnowania 1 ha`** | **brak danych** | — |
| **`wapnowanie gleby koszt`** | **brak danych** | — |

Przy okazji: rozpiska z 13.08 podawała dla „ile kosztuje tona wapna" CPC **5,32 USD** jako
„najwyższy w projekcie". Dziś DataForSEO zwraca **0,78 USD**. Ta liczba się zestarzała i nie
powinna być podstawą decyzji.

**2. Hub już rankuje na te intencje, i to wysoko.** GSC, 19.05–18.08:

| Fraza | Strona | Pozycja |
|---|---|---|
| ile kosztuje tona wapna | `/wapnowanie-gleby/` | **2,0** |
| cena wapna na pole | `/wapnowanie-gleby/` | **2,0** |
| cena wapna nawozowego | `/wapnowanie-gleby/` | **2,5** |
| cena wapna za tonę | `/wapnowanie-gleby/` | **3,0** |
| kreda granulowana cena | `/wapnowanie-gleby/` | 2,0 |
| ile kosztuje worek wapna | `/wapnowanie-gleby/` | 4,0 |

**3. Hub na te pytania nie odpowiadał.** Przed zmianą: **zero wystąpień** słów „zł", „cena",
„koszt" w całej treści. Google wysyłał tam ludzi z zapytaniem cenowym na drugiej pozycji,
a strona nie miała dla nich odpowiedzi.

## Ryzyko, którego unikamy

Nowy URL o tej samej intencji co hub to dokładnie mechanizm opisany w ADR
`2026-08-11-podzial-rol-ads-seo.md` i potwierdzony **tego samego dnia** w diagnozie
`docs/audits/T-026-diagnoza-indeksacji-2026-08-19.md`: Google nie pobiera drugiej strony
odpowiadającej na to samo pytanie. Cztery lipcowe poradniki mają z tego powodu status
„URL is unknown" mimo 41 dni w sitemapie i linkowania z zaindeksowanego huba.

Scenariusze dla nowego poradnika były dwa, oba złe: albo nie zostałby zaindeksowany (najbardziej
prawdopodobny), albo odebrałby hubowi pozycje 2–3 na frazy, które hub już obsługuje.

## Co zrobiono zamiast

Sekcja **„Ile kosztuje wapnowanie"** na `/wapnowanie-gleby/` (ID 2074), wstawiona między
„Jakie wapno AGRIA dla jakiej gleby" a „Kiedy wapnować glebę?". Zawiera widełki dla trzech
typów wapna z warunkiem dostawy, **przeliczenie na hektar** (materiał przy dawce 3 t/ha
węglanowego i 2 t/ha tlenkowego) oraz odesłanie do kart produktowych po ceny szczegółowe.

Zero nowych URL-i, zero ryzyka kanibalizacji, efekt natychmiastowy — strona jest już
zaindeksowana i crawlowana (ostatni crawl 15.08).

## Czego ta decyzja nie przesądza

Nie zamyka drogi do treści cenowych na innych stronach. Zamyka **jedną konkretną stronę
pod frazę bez wolumenu**. Gdyby „ile kosztuje wapnowanie hektara" zaczęło generować realne
zapytania, wracamy do tematu — ale wtedy z danymi, nie z założeniem.
