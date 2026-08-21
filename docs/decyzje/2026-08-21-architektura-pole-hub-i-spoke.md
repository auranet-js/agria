# ADR 2026-08-21 — architektura klastra „pole": hub, terminarz i trzy uprawy

**Status:** przyjęta 2026-08-21 · **Dotyczy:** T-055 · **Uzupełnia** ADR `2026-08-11-podzial-rol-ads-seo.md`
**Dane:** DataForSEO `keyword_suggestions` (2 080 unikalnych fraz z seedów wapno/wapnowanie/kreda, pull 21.08),
`google_ads/search_volume` z sezonowością 12 mies. · **Kontekst:** `docs/seo/T-052-AUDYT_FRAZ_I_PLAN_SEZON_2026-08-21.md`

---

## Problem

Plan T-055 przewidywał jeden poradnik „Jakie wapno na pole". Uwaga Janka z 21.08: taka strona
**wyczerpuje frazę i blokuje uprawy** — jeśli hub odpowie na „jakie wapno pod ziemniaki" własnym
nagłówkiem, to on zacznie na tę frazę rankować, a późniejsza dedykowana strona będzie walczyć
z własnym serwisem. Dokładnie ten mechanizm zmierzyliśmy 11.08: sześć naszych URL-i na „wapno bielik"
dało najlepszą pozycję 15,3, a każda fraza z jednym adresem stoi w TOP10.

Odwrotny błąd jest równie realny: rozbicie wszystkiego na uprawy tworzy strony bez popytu.

## Dane, które rozstrzygają

| Klaster | Fraz z wolumenem ≥10 | Razem/mies. | Główna fraza |
|---|---|---|---|
| **pole — ogólne** | 15 | **980** | `wapno na pole` 390 (HIGH) |
| **kiedy / termin** | — | **~1 110** | `kiedy wapnować glebę` 320 (**październik 590**) |
| łąki i pastwiska | 7 | **210** | `wapno na łąki` 50 + `jakie wapno na łąki` 50 |
| ziemniaki | 6 | **170** | `wapno pod ziemniaki` 50 + `jakie wapno pod ziemniaki` 50 |
| zboża ozime | 7 | **170** | `czy można siać wapno na zboże` 90 (**LOW**) |
| **rzepak** | **1** | **20** (sierpień 140) | `wapno pod rzepak` |
| **kukurydza** | **0** | **0** | — |
| buraki | 0 | 0 | — |

Osobno w klastrze ogólnym: `wapno budowlane na pole` 70 + `wapno budowlane na pole dawka` 20 = **90** —
pytanie, czy wapno hydratyzowane nadaje się na pole. AGRIA ma oba produkty, więc odpowiedź jest nasza.

Klaster „przed siewem / po zimie" to w 80% trawnik i działka (hobby, świadomie odsiewany).
Po odjęciu zostaje `wapno granulowane przed siewem` 50 + `wapnowanie przed siewem` 20 = **70**.

## Decyzja

**Trzy poziomy, każdy na rozłączny zestaw fraz. Oś podziału to pytanie, nie temat.**

| Poziom | URL | Oś | Frazy | Wolumen |
|---|---|---|---|---|
| **Terminarz** | `/jak-stosowac-wapno-nawozowe/` (przebudowa, nie nowy adres) | **KIEDY** | `kiedy wapnować glebę` 320, `kiedy siać wapno granulowane` 420, `wapnowanie gleby kiedy` 280, `kiedy wapnować pole` 90, `wapnowanie przed siewem` 70 | ~1 110 |
| **Hub** | `/jakie-wapno-na-pole/` (nowy) | **JAKIE — rodzaj wapna × typ gleby** | `wapno na pole` 390, `jakie wapno na pole` 140, `wapno budowlane na pole` 90, `kreda na pole` 50, `wapno sypkie/granulowane na pole` 60, `wapno na pole luzem` 40, `gdzie kupić wapno na pole` 30 | ~980 |
| **Spoke** | `/wapno-na-laki-i-pastwiska/` | **uprawa** | 7 fraz | 210 |
| **Spoke** | `/wapno-pod-zboza-ozime/` | **uprawa + termin siewu** | 7 fraz, w tym rzepak ozimy | 190 |
| **Spoke** | `/wapno-pod-ziemniaki/` | **uprawa** | 6 fraz | 170 |

### Czego świadomie NIE budujemy jako osobnych adresów

- **`/wapno-pod-rzepak/`** — jedna fraza w planerze, 20/mies. Rzepak ozimy sieje się w sierpniu,
  w tym samym oknie agrotechnicznym co zboża ozime; wchodzi jako **sekcja w spoke'u ozimin**,
  z własnym H2 i własną odpowiedzią, ale bez własnego adresu.
- **`/wapno-pod-kukurydze/`, `/wapno-pod-buraki/`** i pozostałe uprawy — patrz następna sekcja.
  Nie znaczy „nie pokrywamy". Znaczy „pokrywamy inaczej".
- **Osobnej strony „przed siewem" ani „po zimie"** — 70/mies., to sekcje terminarza.

## Pełne pokrycie upraw — poprawka po uwadze Janka (21.08)

**Zarzut:** „w Polsce uprawia się wiele rzeczy i ktoś o to w końcu zapyta". Słuszny, a moje pierwsze
sprawdzenie było wadliwe tym samym błędem, za który skrytykowałem audyt z maja: pytałem wyłącznie
o frazy **zawierające słowo „wapno"**. Uprawa bywa pytana od strony gleby.

**Sprawdzenie drugie (21.08):** 260 kombinacji uprawa × pH / odczyn / wymagania glebowe, 42 gatunki
uprawiane w Polsce. Wynik: **7 fraz z wolumenem ≥10, razem 290/mies.**, i to głównie hobby
(`jakie ph dla trawy` 210, truskawka, borówka). W planerze Google tego ogona faktycznie nie widać.

**Ale planer nie jest instrumentem do mierzenia ogona.** Zaokrągla do zera wszystko poniżej progu.
Search Console widzi zapytania przy **jednym** wyświetleniu — i widzi je już dziś:

| Zapytanie (GSC, 90 dni) | Wyśw. | Pozycja |
|---|---|---|
| ile wapna na hektar łąki | 25 | 7,2 |
| ile wapna granulowanego na hektar łąki | 22 | 10,9 |
| **wapnowanie po kukurydzy** | **6** | **64,2** |
| jakie wapno pod jeczmien ozimy | 2 | **2,0** |
| jakie wapno pod pszenice ozimą | 1 | **2,0** |
| jakie nawożenie pod rzepak | 1 | **2,0** |
| jakie wapno pod rzepak | 1 | **3,0** |
| wapnowanie pod rzepak | 1 | **4,0** |
| jęczmień ozimy sandra wymagania glebowe | 1 | 3,0 |

**To jest dowód, że Janek ma rację, i to mocniejszy niż planer.** Na zapytaniach uprawowych stoimy
już dziś na pozycjach **2–4** — treścią, która o uprawach nie mówi ani słowa. Nikt inny na nie
nie odpowiada. Kukurydza, którą planer wycenił na zero, ma realne zapytanie i naszą pozycję **64**,
bo akurat na nie nie mamy nic.

### Decyzja: pokrywamy każdą uprawę, ale dwoma narzędziami, nie czterdziestoma adresami

| Narzędzie | Co obejmuje | Dlaczego tak |
|---|---|---|
| **Tabela uprawowa w hubie** `/jakie-wapno-na-pole/` | wszystkie uprawy polowe w Polsce: optymalny odczyn, orientacyjna dawka, zalecany typ wapna, termin względem siewu | Google dopasowuje **fragmenty i tabele** do zapytań długiego ogona. Jedna mocna strona wygrywa ogon lepiej niż czterdzieści cienkich, a cienkie strony bez popytu to obciążenie indeksu, nie aktywo |
| **Selektor uprawy w kalkulatorze** `/kalkulator-wapnowania/` | ta sama lista upraw jako pole wyboru — dawka liczona z uwzględnieniem wymagań gatunku | Kalkulator rankuje na 5,8 i jest naszym najmocniejszym narzędziem. Odpowiedź funkcjonalna, nie tylko tekstowa — tego nie ma żaden konkurent |

Do tego **FAQ z jednym pytaniem na uprawę** w hubie (schema `FAQPage`), po jednym zdaniu odpowiedzi
— to jest format, który Google i odpowiedzi AI cytują fragmentami.

### Reguła awansu — kiedy uprawa dostaje własny adres

Uprawa **wychodzi z tabeli i dostaje własny URL**, gdy spełni próg z sekcji „Decyzja":
**≥3 frazy i ≥100 wyszukań/mies. łącznie** — liczone **z GSC, nie z planera**, bo tylko GSC
widzi ogon. Przegląd **kwartalny**: `query × page` filtrowane po nazwach upraw.

Dziś próg spełniają trzy: łąki i pastwiska, zboża ozime, ziemniaki. One dostają spoke'y od razu.
Reszta czeka w tabeli i awansuje, gdy zapytania to uzasadnią. Kukurydza jest pierwszym kandydatem
do obserwacji — ma zapytanie i naszą pozycję 64.

### Ograniczenie źródłowe, do domknięcia przed publikacją tabeli

Optymalny odczyn i dawka per gatunek **nie mogą pochodzić z mojego rozumowania** — obowiązuje reguła
projektu, że parametry bierzemy z kart producentów i dokumentów branżowych. Dla wymagań glebowych
upraw źródłem są **tabele IUNG-PIB i rozporządzenia**, nie karta produktu. Do rozstrzygnięcia:
czy zaciągamy je z publikacji IUNG z podaniem źródła w treści, czy weryfikuje je Kazimierz.
**Tabela nie idzie na produkcję bez tego rozstrzygnięcia.**

### Trzy reguły, które to utrzymają

1. **Próg URL-a: klaster musi mieć ≥3 frazy i ≥100 wyszukań/mies. łącznie.** Poniżej — sekcja
   w stronie istniejącej. To jest kryterium liczbowe, nie wyczucie.
2. **Hub nie dostaje ani jednego H2 z nazwą uprawy.** Uprawy pojawiają się w nim wyłącznie jako
   zdanie z linkiem. Nagłówek „Wapno pod ziemniaki" w hubie oznacza, że hub wygra tę frazę
   i spoke nigdy nie wejdzie.
3. **Spoke nie odpowiada na „jakie wapno na pole" ogólnie** — otwiera odpowiedzią uprawową
   (dawka, termin, forma) i odsyła do huba po dobór typu wapna.

Kontrola po publikacji: GSC `query × page`. Jeśli hub notuje się na frazie uprawowej wyżej niż
jej spoke, nagłówki huba są za szerokie — do korekty w tym samym tygodniu.

## Kolejność, wymuszona sezonem

Wszystko, co ma pracować w październiku, musi być opublikowane **do 20 września**.

| Termin | Co | Dlaczego wtedy |
|---|---|---|
| **21–22.08** | Terminarz (przebudowa) | `title` został już 21.08 przestawiony na „Kiedy wapnować pole?" (T-053) — treść musi za nim nadążyć, inaczej tytuł obiecuje coś, czego w środku nie ma |
| do **05.09** | Spoke: zboża ozime + rzepak | siew ozimin wrzesień–październik, `wapno pod rzepak` szczytuje w sierpniu |
| do **10.09** | Hub `/jakie-wapno-na-pole/` | najwyższy wolumen klastra, potrzebuje najdłuższego rozbiegu |
| do **15.09** | Spoke: łąki i pastwiska | wapnowanie użytków zielonych jesienią |
| do **20.09** | Spoke: ziemniaki | `wapno pod ziemniaki` szczytuje wrzesień–październik (110) |

## Co ta decyzja unieważnia

| Ustalenie | Nowy status |
|---|---|
| T-055 „poradnik «Jakie wapno na pole»" jako jedna strona | **zastąpione** hubem + trzema spoke'ami z twardym progiem |
| Sugestia z rozmowy, żeby robić stronę per uprawa (kukurydza, buraki, rzepak) | **odrzucone dla trzech upraw** — brak wolumenu; rzepak jako sekcja |
| „Hub-and-spoke" z T-038 (unieważnione 11.08) | **bez zmian — to co innego.** T-038 dotyczyło hubów **segmentowych** (Rolnictwo / Rybactwo / Oczyszczalnie) nieopartych na pomiarze. Tutaj podział wynika z rozłącznych fraz i ma próg liczbowy |
