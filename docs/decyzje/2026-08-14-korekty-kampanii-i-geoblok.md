# ADR 2026-08-14 — korekty kampanii po pierwszym dniu emisji + geoblok

**Status:** wykonane 14.08.2026 · zweryfikowane na koncie i na produkcji
**Konto Ads:** 674-207-1446 · **Poprzedni ADR:** `2026-08-13-uruchomienie-kampanii-ads.md`
**Koryguje:** decyzję „24/7 bez day-partingu" z ADR 13.08

---

## Punkt wyjścia — kampanie ruszyły 14.08, nie 13.08

13.08 kampanie zebrały **zero wyświetleń**. Pierwsza emisja padła **14.08 o 14:00**.
Dorobek pierwszych trzech godzin:

| | 14.08, 14:00–17:00 |
|---|---|
| Wyświetlenia | 158 |
| Kliknięcia | 12 |
| Koszt | 24,26 zł z 40 zł budżetu |
| Śr. CPC | ~2,00 zł |
| Konwersje | 0 |

Kampania **Marka: zero wyświetleń** — brandu nikt nie wyszukał.

Tempo ~8 zł/h oznacza, że 40 zł starcza na ok. 5 godzin emisji. Przy starcie o 8:00
reklamy gasłyby ok. 13:00 — czyli znikamy, zanim rolnik wróci z pola.

---

## Decyzje

### 1. Harmonogram 6:00–22:00, siedem dni — korekta ADR 13.08

ADR 13.08 zapisał „24/7 bez day-partingu" bez uzasadnienia. Audyt portfolio pokazał,
że **AGRIA była jedynym kontem klienckim bez harmonogramu**:

| Konto | Harmonogram |
|---|---|
| Victorini | 7–22 pn–sob, 9–22 niedziela |
| PrimaAuto | brand 6–23, tematyczne 8–21 / 7–22 |
| ASEO | 6–22 codziennie |
| PMP fibertech | 7–16, tylko pn–pt |
| Rzeczoznawca | 8–16, tylko pn–pt |
| AGRIA (do 14.08) | **brak** |

Przyjęty wzorzec **ASEO (6–22 codziennie)** — najbliższy profil: B2B surowcowy
z aktywnym weekendem. **Weekendów nie wyłączamy** — niedziela jest u AGRII
najmocniejszym dniem (patrz memory `project_agria_ads_sezonowosc`).

Budżetu **nie podnosimy** (decyzja Janka) — harmonogram ma rozłożyć te same 40 zł
na godziny, w których jest ruch, zamiast palić je w nocy, gdy nikt nie odbierze telefonu.

### 2. Stawka „Wapno nawozowe" 2,50 → 2,00 zł

Najwyższa stawka na koncie stała przy najsłabszym CTR w kampanii (5,3% wobec 37–40%
w grupie granulowanej). Druga dźwignia przy zamrożonym budżecie: te same pieniądze,
ok. 25% więcej kliknięć.

Stan po zmianie: granulowane 2,00 · nawozowe 2,00 · magnezowe 1,00 · brand 0,50.

### 3. Wykluczenia 38 → 59

**Fala 1 — odmiany ogrodowe (10).** Wykluczenia w dopasowaniu do wyrażenia nie odmieniają
przez przypadki, więc `ogród` i `ogrodowy` z ADR 13.08 **nie łapały** tego, co realnie weszło:
`wapno ogrodowe`, `wapno ogrodowe cena`, `ile wapna do ogrodu`, `wapno na ogródek`, `wapno na mech`.
Dodane: `ogrodowe`, `ogrodowa`, `ogrodowych`, `ogrodu`, `ogródek`, `ogródka`, `ogrodniczy`,
`ogrodnicze`, `mech`, `mchu`.

**Fala 2 — zapytania o dawkowanie (11).** Weszły `ile wapna sypkiego na ha`, `ile wapna
granulowanego na hektar`, `wapno magnezowe granulowane ile na hektar`, `ile wapna tlenkowego
na hektar`. To łamie **podział ról z ADR 11.08** (poradnikowe i decyzyjne → SEO organiczne)
i jest podwójnie nieopłacalne, bo na tych frazach **już stoimy w organiku**:

| Fraza | Pozycja organiczna | Wyświetleń/mies. (GSC) |
|---|---|---|
| ile wapna granulowanego na hektar | 7,8 | 892 |
| ile wapna na hektar | 8,8 | 1 005 |

Dodane: `na hektar`, `na ha`, `ile wapna`, `dawka`, `dawkowanie`, `jak wapnowac`,
`jak wapnować`, `kiedy wapnowac`, `kiedy wapnować`, `ile kg`, `co to jest`.

**Świadomie NIE wykluczone:** `ile kosztuje wapno nawozowe` (intencja cenowa, nie dawkowa)
oraz marki konkurencji z ceną — `wapno orcal cena`, `orcal granulowany cena`,
`wapno morawica cena`. Kto szuka konkretnej marki z ceną, szuka dostawcy.

### 4. „producent" → „od producenta" w tekstach

Producentem surowca są **Nordkalk i Trzuskawica**, AGRIA jest dostawcą — sam „producent"
sugerowałby produkcję własną i kłócił się z pozycjonowaniem z ADR 13.08. Forma
**„od producenta"** jest prawdziwa i mocniejsza handlowo („bez pośredników").
Decyzja Janka 14.08.

| Grupa | Było | Jest |
|---|---|---|
| Wapno granulowane | Wapno granulowane – producent | Granulowane od producenta |
| Wapno nawozowe | Wapno nawozowe – producent | Wapno nawozowe od producenta |
| Wapno magnezowe i kreda | Wapno z magnezem – producent | Wapno z magnezem od producenta |
| Brand | Producent od 1989 roku | Wapno prosto od producenta |

Objaśnienie `Producent od 1989 roku` → `Wapno od producenta`. Nagłówki
`Prosto od producenta wapna` zostały bez zmian — były już w dobrej formie.

⚠️ Wymiana tekstów nastąpiła 14.08 ok. 15:40, czyli **w trakcie** pierwszego dnia emisji.
CTR 7,5% z 14.08 pochodzi z **poprzednich** tekstów (z opakowaniami w nagłówkach)
i nie jest oceną nowego pozycjonowania.

### 5. `phone_click` → działanie dodatkowe (secondary)

`phone_click` liczy **kliknięcie w numer**, `Połączenia z reklam (30s+)` liczy **rozmowę**.
Przy dwóch działaniach głównych jeden kontakt telefoniczny liczy się dwa razy. Dodatkowo
`phone_click` idzie przez GA4, więc ginie przy odmowie zgody — AD_CALL Google mierzy
po swojej stronie, poza consentem.

Przy MANUAL_CPC zmiana jest dziś wyłącznie porządkowa (nie ma automatu licytacji).
Zadziała przy planowanym przejściu na Maks. konwersji — bez niej Smart Bidding goniłby
tańszy, słabszy sygnał zamiast odebranych rozmów.

Wzorzec portfolio — konta mające obie konwersje naraz:

| Konto | GA4 `phone_click` | Konwersja z połączeń |
|---|---|---|
| Victorini | secondary | PRIMARY |
| PMP fibertech | secondary | — |
| ASEO | PRIMARY | PRIMARY (liczy podwójnie) |
| PrimaAuto | PRIMARY | PRIMARY (liczy podwójnie) |

Wykonane ręcznie w panelu przez Janka — Google Ads API `/conversionActions:mutate`
blokuje w tej sesji klasyfikator uprawnień Claude Code.

### 6. Geoblok — ruch spoza Europy odcięty

**Powód (GA4, 01–14.08):** 82 ze 123 sesji z **Singapuru (67%)**, zaangażowanie **0,0%**,
Polska — **4 sesje**. Sygnatura bota: rozdzielczość **1280x1200 + English** = 84 sesje
(ta sama także z Arabii Saudyjskiej, USA, Bangladeszu, Pakistanu, RPA, Ukrainy);
drugi wzorzec `800x600` = 10 sesji.

**Te same boty generują 404-ki:** „Page Not Found" miało 30 odsłon, tyle samo co strona
główna. Chodzą po nieistniejącej mapie — demo-produkty motywu (`fresh-green-peas`,
`naga-pepper-2`, `organic-broklen`, `pure-honey`, `/product-category/apple|food|vegetable`),
stare adresy DuoCMS (`/pl/produkt/15-…`, `/zapytanie-ofertowe-nr1-2019/`), stare wpisy
(`/jak-murowac-z-cegly-klinkierowej/`, `/wykwity-jak-powstaja/`), `/rolnictwo`, `/oferta/inne/`.
Sitemapa jest czysta (20 produktów, bez demo) — to nie nasz błąd, to bot z archiwalną listą URL.

**Rozwiązanie:** `wp-content/plugins/agria-by-auranet/security-geoblock.php`, ładowany
przez `require_once` w nagłówku `agria-by-auranet.php` przed autoloaderem modułów.
Kopia referencyjna: `src/plugins/agria-by-auranet/security-geoblock.php`.

Wzorzec z **victorini2025/inc/security-geoblock.php** (02.07) i **aseo-security-geoblock.php**
(11.08). Baza: `GeoLite2-Country.mmdb`, którą **Complianz już trzyma i odświeża sam**
(8,6 MB, stan 13.08) — nie dublujemy własnej kopii. Czytnik: natywne rozszerzenie
`maxminddb`, potwierdzone na serwerze (PHP 8.3.33).

Weryfikacja 14.08:

| Test | Wynik |
|---|---|
| Singapur `203.116.1.1` | Forbidden |
| USA `8.8.8.8` | Forbidden |
| Polska `188.146.0.1` | przepuszczony |
| AdsBot-Google → landing | 200 |
| Googlebot → strona główna | 200 |
| Strona główna / landingi / kontakt | 200 |

Kill-switch: `define('AGRIA_GEOBLOCK_OFF', true)` w `wp-config.php`.
Fail-open: brak bazy, błąd czytnika lub nieznany kraj → przepuszcza, nigdy nie blokuje.

---

## Sprostowania wobec wcześniejszych ustaleń

**`url_passthrough` — nie brakuje go, jest od dawna.** Kontener GTM-TDC85TQN ma
`url_passthrough: true` i `ads_data_redaction: true` w tagu „Consent Default Denied",
opublikowane w wersji live 5, zero niezapisanych zmian. Wcześniejszy wniosek o braku
wziął się z grepowania **statycznego HTML** — tagi GTM wstrzykuje dopiero `gtm.js`,
więc w źródle strony ich nie widać. Victorini ma ten sam kod w snippecie w HTML, stąd
różnica w wyniku greppa. Efekt identyczny.

**Geoblok w ASEO działa** — nie jest martwy, jak zapisano w pierwszej analizie tej sesji.
Martwa jest wyłącznie reguła GeoIP w samym `.htaccess` (bo `mod_geoip` na nazwa.pl nie
istnieje) — i właśnie dlatego powstała wersja PHP jako mu-plugin. To ona jest wzorcem.

---

## Gotchas dołożone do listy z ADR 13.08

| Problem | Rozwiązanie |
|---|---|
| Wykluczenia PHRASE nie odmieniają przez przypadki | Wypisać formy osobno: `ogród` NIE łapie `ogrodowe`/`ogrodu`/`ogródek` |
| Grep po HTML nie wykrywa tagów GTM | Sprawdzać `versions:live` w API GTM, nie źródło strony |
| MCP `write_file` nie tworzy katalogów | Plik w korzeniu wtyczki + `require_once`, zamiast `modules/<nazwa>/` |
| Dane godzinowe GA4 opóźnione ~4-6 h | Raport dzienny kończył się na 10:00, gdy ruch szedł o 14:00. Realtime pokazuje od razu |
| `/conversionActions:mutate` blokowany | Klasyfikator uprawnień Claude Code — robić w panelu |

---

## Otwarte

1. **Godziny pracy — 8–16 czy 7–15.** Harmonogram połączeń stoi na 8–16, Janek pamięta 7–15.
   Fakt handlowy, wymaga potwierdzenia u Pawła. Przesądza też o oknie emisji.
2. **Ceny na kartach produktów.** Cennik jest kompletny (`docs/operations/CEN_LISTA_URL_2026-08-13.md`,
   15 pozycji), ale strony go nie mają — a **wszystkie płatne kliknięcia pierwszego dnia
   to zapytania cenowe** (`wapno granulowane cena`, `cena wapna granulowanego`,
   `wapno nawozowe cena za tonę`, `wapno orcal cena`, `orcal granulowany cena`,
   `wapno morawica cena`). Płacimy za ruch, który odbija się od strony bez cen.
3. **Objaśnienia strukturalne** — AGRIA zero, PrimaAuto 45. Do zrobienia z danych, które są.
4. **Wizytówka Google** — niepodpięta do Ads.
5. **Grafiki** — zero zasobów; kit z OLX odpada w całości (tekst, logo i QR na wszystkich).
6. **Certyfikaty na stronach produktów** — zgłoszone przez Janka 14.08, poza tym wątkiem.

---

## Do sprawdzenia jutro (15.08)

- Search terms za pełną dobę — czy wykluczenia domknęły ogrodowe i dawkowe, jak wypadają
  nowe teksty „od producenta" na CTR.
- GA4 — czy Singapur zniknął i czy „Page Not Found" spadło z 30 odsłon. Dopiero wtedy
  dane nadają się do oceny kampanii.
- Czy harmonogram 6–22 zmienił rozkład wydatku (czy budżet dociąga do popołudnia).
