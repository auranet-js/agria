# Plan wdrożeniowy — task po tasku

> **Co to jest:** dla każdej pozycji z `docs/REJESTR_ZOBOWIAZAN.md` osobny plik z promptem
> wykonawczym. Napisane **na stanie rzeczywistym** — każdy kanał dostępu przetestowany,
> każdy stan zmierzony na produkcji 2026-08-19 między 15:00 a 15:35, nie przepisany z dokumentów.
>
> **Czego tu nie ma:** wykonania. Ten katalog przygotowuje wdrożenie, nie realizuje go.
>
> **Jak używać:** `00-PROTOKOL-WSPOLNY.md` czytasz raz na starcie wątku, potem plik konkretnego taska.

---

## Kolejność wykonania

```
T-048 ──→ T-031                       dowód PSI już jest, T-031 odblokowany
T-008 ──┬─ T-009 ──→ T-027            jedna strona (ID 731), jedna wizyta, potem reindeksacja
        └─ ID 731, dwie warstwy treści
T-010 ──── T-011                      PRIORYTET 1, jedna edycja na tych samych kartach
T-029 · T-032 · T-028 · T-026 · T-039 · T-042 · T-046      niezależne, dowolna kolejność
```

## Wszystkie pozycje

### 🔴 Teraz — 13 pozycji

| Plik | Zadanie | Zakr. | Szac. |
|---|---|---|---|
| [`T-010`](T-010-ceny-w-tresci-15-kart.md) | widełki cenowe w treści 15 kart + 2 landingi + poradnik | R | 6–8 h |
| [`T-011`](T-011-naglowki-H2-cenowe.md) | nagłówki H2 z frazą cenową | R | z T-010 |
| [`T-008`](T-008-atesty-i-karty-nordkalk.md) | 8 atestów i kart Nordkalku na `/do-pobrania/` | R | 2–3 h |
| [`T-009`](T-009-usuniecie-sekcji-certyfikaty.md) | usunięcie sekcji „Certyfikaty" | R | 1 h |
| [`T-027`](T-027-reindeksacja-do-pobrania.md) | zgłoszenie `/do-pobrania/` do reindeksacji | R | 0,25 h |
| [`T-048`](T-048-geoblok-lighthouse.md) | geoblok vs Lighthouse — **dowód zdobyty 19.08** | R | 0,3 h |
| [`T-028`](T-028-duplikaty-produkt.md) | duplikaty pod starą bazą `/produkt/` + 15 sierot | R | 2 h |
| [`T-029`](T-029-login-admina-w-schema.md) | login `js` w schema, REST i enumeracji autora | R | 1,5 h |
| [`T-026`](T-026-szesc-url-poza-indeksem.md) | 6 URL-i poza indeksem — **zadanie diagnostyczne** | R | 2–3 h |
| [`T-032`](T-032-301-kategoria-produktu.md) | 301 dla `/kategoria-produktu/*` | R | 1 h |
| [`T-039`](T-039-korekty-kampanii-marka.md) | kampania Marka: stawka, wykluczenia, grupa „Producent" | P | 1,5 h |
| [`T-042`](T-042-poprawki-tresci-olx.md) | poprawki treści OLX od Kazimierza | P | 2 h |
| [`T-046`](T-046-gbp-tarnow.md) | optymalizacja profilu GBP Tarnów | R | 2–3 h |

### 🟡 Czeka na AGRIĘ — 6 pozycji

| Plik | Na co czeka |
|---|---|
| [`T-006`](T-006-dzial-sprzedazy.md) | skład działu sprzedaży (65 dni) — **ale naprawa `href` Kazimierza wykonalna dziś** |
| [`T-040`](T-040-nordkalk-w-reklamach.md) | status autoryzowanego dystrybutora Nordkalku |
| [`T-041`](T-041-publikacja-200-ogloszen-olx.md) | pakiet OLX Premium 200 (1 199,99 zł, zakres K) |
| [`T-043`](T-043-weryfikacja-kalkulatora-mg.md) | uwagi Kazimierza do mockupu kalkulatora |
| [`T-047`](T-047-odzysk-profili-gbp-oddzialy.md) | dostęp do profili GBP Niedomice i Radgoszcz |
| [`T-007`](T-007-interpunkcja.md) | robi Paweł sam — ⚪, nasza rola to pilnowanie terminu |

### 📅 Wrzesień (M4) — 5 pozycji

| Plik | Zakr. |
|---|---|
| [`T-031`](T-031-cwv-mobile-lcp.md) — CWV mobile, LCP | R |
| [`T-030`](T-030-localbusiness-oddzialy.md) — LocalBusiness ×2 | R |
| [`T-044`](T-044-wdrozenie-modulu-mg.md) — moduł Mg w kalkulatorze | P ≈4 h |
| [`T-045`](T-045-ofertownik-etap-zerowy.md) — ofertownik, etap zerowy | W |
| [`MENU`](MENU-segmenty-m4.md) — powrót pozycji menu | R |

### 🔵 Do rozstrzygnięcia — 2 pozycje

| Plik | Co rozstrzygnąć |
|---|---|
| [`T-033`](T-033-zgody-i-pomiar-ga4.md) | dlaczego GA4 łapie ~49 % kliknięć Ads — **rediagnoza od zera** |
| [`T-034`](T-034-premmerce-podatnosc.md) | podatność Premmerce — **changelog znaleziony, sprawa niemal zamknięta** |

---

## Co się zmienia w obrazie kolejki po tych testach

Osiem ustaleń z 19.08, które przesuwają pracę. **Rejestru nie zmieniałem** — to jest lista
do przejrzenia i zatwierdzenia przed wdrożeniem.

1. **`T-048` ma dowód.** Kwota PSI wróciła; pomiar o 15:02 przeszedł: score 0,70, LCP 7,4 s,
   `runtimeError: None`. Task jest gotowy do zamknięcia i **odblokowuje `T-031`**.
   To najtańsze domknięcie w całej kolejce.
2. **`T-034` jest praktycznie rozstrzygnięty.** Rejestr mówi „changelogu nie da się sprawdzić
   publicznie" — leży na serwerze w `readme.txt`. Wynika z niego, że **2.3.11 to wersja z poprawką
   LFI**, a zainstalowana 2.3.13 jest nowsza. Zostaje jedno pytanie: czy „DOM-XSS" z naszych
   notatek to ta sama sprawa.
3. **`T-028` opisany jest inaczej, niż jest.** HTTP 200 pod `/produkt/*` **nie pochodzi**
   od piętnastu wpisów `post_type=produkt` (ID 60–74) — CPT `produkt` nie jest dziś zarejestrowany
   w WordPressie. To stara baza URL serwująca produkty WooCommerce, z canonicalem na właściwy adres.
   Dowód: `/produkt/wapno-palone-wysokoreaktywne/` → **404**. Priorytet spada, diagnoza się zmienia.
4. **`T-029` ma szerszy zakres, niż zapisano.** Poza schema login wycieka przez
   `/wp-json/wp/v2/users` (publicznie, z `is_super_admin: true`) i przez `?author=1`.
   Naprawa samej schema zostawia dwa otwarte kanały.
5. **`T-026` ma odwrócone przypisanie dwóch URL-i.** Zmierzone: `/kreda-malarska/` jest „Discovered",
   `/wapno-nawozowe-na-trawnik/` jest „unknown" — rejestr ma to na krzyż. Dodatkowo cztery poradniki
   **są** w sitemapie i **są** linkowane z huba, a Google ich nie pobrał ani razu. To przesuwa
   diagnozę w stronę duplikacji treści wobec huba, nie techniki.
6. **`T-033` startuje z fałszywej przesłanki i to już drugi raz.** Memory mówi „5 sesji organicznych
   w lipcu"; GA4 za 1–19.08 pokazuje 21 organicznych, 49 Paid Search, 107 Direct. Consent Mode v2
   jest wdrożony poprawnie. Pomiar działa **niekompletnie**, a nie „nie działa".
7. **`T-042` nie ma treści ustaleń.** Maila Kazimierza z 18.08 nie ma ani w repo, ani na
   `claude@auratest.pl` (ostatnie maile OLX: [248] i [250] z 11.08). Pierwszym krokiem musi być
   prośba do Janka o forward.
8. **`T-045` ma potwierdzony wektor wycieku.** `wc/store/v1/products` odpowiada publicznie
   i zwraca pole `prices`. Dziś zera. Pierwsza cena wariantu = pierwszy wyciek.
   To podnosi wagę audytu z „porządki" do „warunek".

9. **Tylko trzy karty produktowe renderują z Elementora.** Z 19 produktów `_elementor_data`
   mają **307** (kreda pastewna), **310** (agrobielik-70), **320** (wapno palone mielone) —
   i wszystkie trzy są w zakresie `T-010`. Pozostałe 16 nie ma tej meta w ogóle. To zamienia
   ogólne ostrzeżenie z `CLAUDE.md` §4 w konkretną listę trzech ID do innego trybu edycji.
   Wszystkie 15 URL-i docelowych T-010 odpowiada dziś HTTP 200.

Do tego dwie drobne obserwacje: profil GBP Tarnów ma **`websiteUri: http://www.agria.pl/`**
(HTTP i `www`, zamiast `https://agria.pl/`) i **zero publikacji** przy 10 zdjęciach i 9 opiniach;
`na-ls-cache-enabled: off` na produkcji, czyli cache LiteSpeed nazwa.pl jest dziś wyłączony —
warto sprawdzać ten nagłówek, zanim uzna się cache-bust za zbędny albo za winowajcę.

---

## Testy kanałów — komplet wyników

Pełna tabela z komendami: `00-PROTOKOL-WSPOLNY.md` §4. Skrót:

**Działa i zweryfikowane zapisem:** MCP (`write_file`, `query_db_write`, `update_postmeta`,
`backup_file`) · SSH + WP-CLI 2.4.0 · FTP (pełny cykl upload → HTTP 200 → DELE → 404) ·
Chrome MCP · GSC URL Inspection · **PSI (kwota wróciła)** · Google Ads API v25 · GBP API ·
Indexing API przez `index-submit` (0/100 zużyte) · OLX Partner API **po `refresh`**.

**Pułapki zmierzone, nie z dokumentacji:**
- `update_postmeta` **nie tworzy** nowej meta — zwraca `postmeta not found`.
- `query_db_write` blokuje `DELETE`; blokada łapie też słowo `REPLACE` w zwykłym `SELECT`-cie.
- Token OLX wygasa po ~24 h — `olx-agria refresh` jest krokiem obowiązkowym.
- Treść ID 731 żyje **równolegle** w `post_content` i `_elementor_data`.

Wszystkie artefakty testowe posprzątane: plik testowy w katalogu wtyczki usunięty,
meta `_agria_mcp_writetest` skasowana przez WP-CLI, backup testowy `seo-head.php.bak-*` usunięty,
plik `_ftp-write-test.txt` skasowany z rootu WP (potwierdzone HTTP 404).

---

## Zanim ruszy wdrożenie — do decyzji Janka

1. **Worki w T-010** — publikujemy tylko przeliczenia na tonę, czy także ceny za sztukę?
   Rekomendacja z `FAKTY_KLIENTA.md` §7: tylko tona.
2. **Zamknąć T-048** dowodem z 19.08 (albo świeżym pomiarem z dnia domykania).
3. **T-034** — czy zamykamy na podstawie changelogu, czy szukamy jeszcze źródła zapisu „DOM-XSS".
4. **T-028** — czy po korekcie diagnozy pozycja zostaje w „teraz", czy schodzi niżej.
5. **T-042** — forward maila Kazimierza na `claude@auratest.pl`.
6. **Menu M4** — nadać numer `T-049`, żeby dało się cytować w commitach.
