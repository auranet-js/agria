# Weryfikacja po bloku 0 — crawl kontrolny 08.09.2026

**Po co:** domknięcie bloku 0 wymagało powtórnego crawlu, żeby sprawdzić, czy to, co znalazł
Screaming Frog 07.09, faktycznie zniknęło. Zamiast czekać na eksport z maszyny Janka, serwis
przeskanowany własnym narzędziem — **`scripts/crawl_kontrolny.py`**, 67 adresów, każdy pobrany
dwa razy (rozgrzewka cache Rocketa, pomiar na drugim żądaniu).

**Dane:** `data/kontrole/2026-09-08-crawl-kontrolny.json`
**Punkt odniesienia:** `docs/audits/2026-09-07-CRAWL_SCREAMING_FROG.md`

⚠️ To **nie jest** pełny zamiennik Screaming Froga — nie liczy linków wychodzących, głębokości
kliknięć, anchorów ani obrazów bez `alt`. Sprawdza dokładnie te rzeczy, które crawl 07.09 zgłosił
jako do naprawy, plus stałe wskaźniki higieny. Przy 62 adresach to wystarcza i kosztuje minutę.

---

## 1. Trzy adresy 404 z 07.09 — wszystkie rozwiązane

| adres | 07.09 | 08.09 |
|---|---|---|
| `/polityka-prywatnosci/` | **404** | **301 → `/rodo/`** |
| `/rolnictwo` | **404** | **301 → `/wapno-nawozowe-rolnictwo/`** |
| `/kontakt/pawel.bigos@agria.pl` | **404** | **404 — i tak ma być** |

Trzeci wymaga wyjaśnienia, bo status się nie zmienił. Przyczyną nie był brak strony, tylko
**adres e-mail wstawiony jako link względny zamiast `mailto:`** na stronie kontaktu. Sprawdzone
w renderze `/kontakt/`: wszystkie cztery adresy są dziś poprawne —
`mailto:biuro@`, `mailto:bogdan.bigos@`, `mailto:kazimierz.nowak@`, `mailto:pawel.bigos@`.
Nic już tam nie prowadzi, więc 404 na adresie, do którego nikt nie linkuje, jest właściwym
zachowaniem serwera, a nie usterką.

**Poza tym zero 404 na wszystkich 62 adresach.** Rozkład: 52 × 200 bez przekierowania,
14 przekierowań (znane historyczne kategorie, `/cart/`, warianty bez slasha).

## 2. Schema `offers` — 16 z 19, i to się zgadza

Crawl 07.09: **19 kart z błędem walidacji** „Either 'schema.org/review', 'schema.org/aggregateRating'
or 'schema.org/offers' is required".

Dziś: **19 kart wykrytych jako `Product`, 16 ma `offers`.** Bez `offers` zostają trzy:

| karta | ID | cena w treści |
|---|---|---|
| `/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/` | 303 | **brak** |
| `/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/` | 313 | **brak** |
| `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` | 316 | **brak** |

To są dokładnie te trzy karty, które nie mają ceny w treści — a `offers` budujemy **ręcznie
z treści, nigdy z `_price`** (ADR `2026-08-19-dwie-warstwy-cen.md`). Brak `offers` jest tam więc
**zgodny z projektem**, nie niedoróbką. Gdy karta dostanie cenę, `offers` wejdzie razem z nią.

## 3. Duplikat tytułu — NIE naprawiony, zostaje otwarty

| tytuł | adresy |
|---|---|
| „Wapno nawozowe węglanowe zawierające magnez \| AGRIA" | `/weglanowe-magnez-granulowane/` · `/weglanowe-magnez-odmiana-04/` |

Dwie karty konkurują tym samym tytułem — stan niezmieniony od 07.09. Nie było to osobną pozycją
w bloku 0, więc nie zostało naprawione; wchodzi do **T-116** (tytuły i opisy kart), gdzie i tak
zaczynamy od SERP-ów.

## 4. Brak meta description — 5 adresów, trzy warte reakcji

| adres | uwaga |
|---|---|
| `/category/poradniki/` | **T-099**, znane i otwarte — do tego jedyny **pusty H1** w serwisie |
| `/rodo/` | zgłoszone 07.09, wciąż bez opisu; przejmuje też ruch z `/polityka-prywatnosci/` |
| `/polityka-plikow-cookies-eu/` | strona generowana przez Complianz |
| `/oswiadczenie-o-ochronie-prywatnosci-eu/` | jw. |
| `/polityka-prywatnosci/` | to ten sam dokument co `/rodo/` (301), nie osobna pozycja |

`/kreda-malarska/` — zgłoszona 07.09 jako bez opisu — **ma dziś meta description**, T-096 potwierdzone.

## 5. Rzeczy potwierdzone jako działające zgodnie z decyzjami

- **`noindex` na `/wapno-granulowane/` i `/wapno-nawozowe/`** — to jedyne dwa `noindex` w serwisie
  i **tak ma być**: landingi są celami Ads poza indeksem (ADR `2026-08-11`, zmierzona kanibalizacja).
- **`/oferta` i `/kontakt` bez slasha oddają 301** na wersje ze slashem — bez duplikatu.
- **66 z 66 stron wyszło z cache WP Rocket** — cache działa na całym serwisie po wczorajszej
  konfiguracji.

## 6. Tytuły prawdopodobnie ucinane w SERP

Oszacowanie szerokości (próg 561 px), nie pomiar: 4 adresy, z czego dwa to strony prawne Complianza,
a `/wapno-granulowane/` jest `noindex`, więc realnie zostaje jedna karta —
`/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-05/` (~595 px, 64 znaki). Wchodzi do T-116.

⚠️ Przypomnienie z crawlu 07.09: **teza „krótszy tytuł = lepszy CTR" została odrzucona pomiarem**
(<45 znaków: 1,01%, ≥45 znaków: 1,16%, różnica w szumie). Skracamy tam, gdzie tytuł się nie mieści,
a nie po to, żeby podnieść CTR.

## 7. Dwa błędy w moim własnym narzędziu, znalezione i poprawione

1. **Wartość po `--json` była brana za plik źródłowy** — pierwsze uruchomienie padło na
   `FileNotFoundError`.
2. **Porównanie adresu końcowego robiło `rstrip("/")`**, przez co 301 z `/oferta` na `/oferta/`
   był niewidoczny, a oba adresy trafiały na listę duplikatów tytułu. Po poprawce porównanie jest
   dokładne, a duplikaty liczone wyłącznie na adresach bez przekierowania — inaczej raport
   pokazywałby sześć duplikatów zamiast jednego prawdziwego.

## 8. Co z tego zostaje otwarte

| co | gdzie |
|---|---|
| duplikat tytułu na dwóch kartach magnezowych | **T-116** |
| `/category/poradniki/` — pusty H1 i brak opisu | **T-099** |
| `/rodo/` bez meta description | drobne, do T-116 albo osobno |
| strony prawne Complianza bez opisu | do rozstrzygnięcia, czy w ogóle mają być w indeksie |

**Blok 0 uznaję za domknięty** — wszystko, co miał naprawić, jest naprawione i sprawdzone
na żywym serwisie, a to, co zostaje, należy do innych pozycji rejestru.
