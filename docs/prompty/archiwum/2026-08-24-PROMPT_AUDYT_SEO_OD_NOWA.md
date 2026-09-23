# Prompt wątku: audyt SEO agria.pl od nowa — kategorie, produkty, indeksacja, plan treści VIII–X

> **Data zlecenia:** 2026-08-24, Janek. **Powód:** plan treści i architektura adresów rozjechały się
> przez trzy miesiące decyzji podejmowanych w kilku wątkach. Dokumenty przeczą sobie nawzajem,
> przekierowania były zakładane i zdejmowane w obie strony, część zadań dublowała robotę już wykonaną.
> **Zadanie: sprawdzić wszystko od zera, na stanie faktycznym, i ułożyć jeden spójny plan.**

---

## 0. Zasada nadrzędna — nie ufaj dokumentom, w tym temu

**Każde zdanie w `docs/` traktuj jako hipotezę do sprawdzenia, nie jako fakt.** Dotyczy to również
tego promptu: liczby i listy poniżej mają Ci powiedzieć, **gdzie patrzeć**, a nie zwolnić z patrzenia.
Trzy razy w sierpniu dokument mówił co innego niż produkcja — i za każdym razem produkcja miała rację.

**Twierdzenie bez pomiaru nie wchodzi do raportu.** Każdy wiersz wyniku ma mieć obok siebie dowód:
wykonane zapytanie, kod odpowiedzi HTTP, ID rekordu, zrzut z API. Jeśli czegoś nie zmierzyłeś,
piszesz „niezmierzone", nie „prawdopodobnie".

---

## 1. Trzy pułapki metodyczne, na które ktoś już wszedł — nie wchodź drugi raz

**1. CTR i kliknięcia w GSC licz z wymiaru `page`, nigdy przez sumowanie wierszy `query`.**
Próg prywatności ukrywa większość danych. Zmierzone 24.08 na `/wapnowanie-gleby/`, 90 dni:
poziom strony **20 670 wyświetleń / 115 kliknięć / CTR 0,56%**, suma zapytań **6 854 / 17 / 0,25%** —
pod progiem schowało się 67% wyświetleń i 85% kliknięć. Na zaniżonej liczbie powstało niepotrzebne
zadanie. Wymiar `query` służy do struktury intencji, nie do sum.

**2. Brak trafień w źródle strony nie znaczy „nie ma".** Consent Mode, `url_passthrough`
i `ads_data_redaction` **są** wdrożone — ale w kontenerze GTM (tag „Consent Default Denied",
wyzwalacz `2147479572`), a nie w HTML. `grep` po źródle dał zero i na tej podstawie powstał
niepotrzebny moduł, wycofany tego samego dnia. **Zanim uznasz coś za brakujące, sprawdź wszystkie
warstwy, w których to może mieszkać.**

**3. Zanim zgłosisz zadanie, sprawdź dziennik, nie tylko kolejkę.** `docs/REJESTR_ZOBOWIAZAN.md` ma
dwie części. Zadanie T-069 dublowało T-053, zamknięty trzy dni wcześniej — wystarczyło otworzyć
dziennik M3.

**Do tego pułapki techniczne projektu** (`CLAUDE.md` §4, memory `project_agria_render_caching`):
sitemapa Rank Matha cache'uje się **w plikach** `uploads/rank-math/*.xml` (kasować przez FTP) ·
`query_db_write` **nie rusza `post_modified`**, więc sitemapa poda starą datę · strony 307/310/320
renderują się z `_elementor_data`, nie z `post_content` · parametry produktu żyją w **czterech
warstwach** naraz · CDN nazwa.pl bywa włączony, weryfikuj z cache-bustem.

---

## 2. Narzędzia — wszystko, czym możesz mierzyć

| Do czego | Jak |
|---|---|
| Baza i pliki produkcji | MCP `mcp__agria__*` — `query_db`, `query_db_write`, `read_file`, `write_file`, `backup_file`, `db_export` |
| Powłoka, WP-CLI | `ssh agria-prod`, WP-CLI `/usr/local/sbin/wp --path=/home/server371853/ftp/agria.pl`. **Dawaj zbiorczo, z `timeout` na każdej komendzie** — pojedyncze wywołania potrafią wisieć |
| `.htaccess`, pliki poza sandboxem MCP | FTP: `curl --netrc-file ~/secrets/agria/netrc ftp://ftp.server371853.nazwa.pl/agria.pl/...` |
| Indeksacja, pozycje, CTR | `scripts/gsc_inspect.py` (URL Inspection), `scripts/gsc_pull.py`, bezpośrednio Search Analytics API przez `scripts/google/_lib.py` |
| Wolumeny, sezonowość, SERP, konkurencja | DataForSEO **przez curl**, sekrety `~/secrets/dataforseo/`. Saldo sprawdź przed serią (`/v3/appendix/user_data`) |
| Kampanie, konwersje | `bash scripts/google/ads_call.sh <PATH> POST <plik.json>` |
| Ruch i zdarzenia | GA4 Data API przez `scripts/google/_lib.py`, property `538301430` |
| Wydajność | PSI v5 z tokenem OAuth (`~/bin/google-access-token`) |
| Render oczami klienta | Chrome MCP. **Uwaga: lokalny Chrome blokuje `googletagmanager.com`** — brak GTM w przeglądarce to bloker, nie usterka strony |
| Zgłoszenia do indeksu | **wyłącznie** `~/bin/index-submit`, wspólna pula 200/dobę na wszystkie projekty |

**Punkt wyjścia dla pomiaru pozycji:** `scripts/seo_baseline.py` i `data/seo/baselines/`.

---

## 3. Reguły, których nie wolno złamać

Przeczytaj **całe** memory projektu (`~/.claude/projects/-home-host476470-projekty-agria/memory/`),
zanim cokolwiek zaproponujesz. Krytyczne dla tego zadania:

- **`project_agria_architektura_kanalow`** — landingi Ads są **poza indeksem** świadomie, bo
  kanibalizacja jest zmierzona („wapno bielik": 6 URL-i → pozycja 15,3). Polcalc, nie Biovita, jest
  właściwym komparatorem. **Czytaj sekcję „DLACZEGO", zanim zaproponujesz nowy landing.**
- **`project_agria_ceny_strategia`** i **`project_agria_dwie_warstwy_cen`** — widełki tonowe, nigdy
  cennik; ceny ofertownika nie wychodzą na front żadnym kanałem.
- **`feedback_agria_bez_zargonu_loco`** — odbiorcą jest rolnik. Zero żargonu.
- **`feedback_agria_params_from_datasheets`** — parametry wyłącznie z kart producentów i rozporządzeń.
- **`feedback_agria_landingi_wzorzec_nie_elementor`** — landing powstaje z powielenia działającej
  struktury, nie z surowego HTML w `post_content`.
- **`feedback_agria_complianz_ustawieniami_zero_kodu`** — warstwa zgód wyłącznie ustawieniami.
- **`feedback_agria_no_self_criticism_built_site`** — stronę zbudował Auranet. W materiałach dla
  klienta framing rozwojowy, nie wytykanie błędów.
- **Produkcja:** zgoda Janka **per operacja**, `db_export`/`backup_file` przed każdą większą zmianą.

---

## ETAP 1 — kategorie: która ma być landingiem, która nie ma prawa istnieć

**Stan zastany do weryfikacji** (odczyt z bazy 24.08, `product_cat`, 8 pozycji):

| term_id | Nazwa | Slug | Produktów | Opis (zn.) |
|---|---|---|---|---|
| 764 | Wapno nawozowe | `wapno-nawozowe-rolnictwo` | 15 | 779 |
| 767 | Oczyszczalnie | `wapno-do-oczyszczalni` | 1 | 724 |
| 768 | Budownictwo | `wapno-hydratyzowane` | 1 | 380 |
| 770 | Paszarstwo | `paszarstwo` | 1 | 447 |
| 830 | Kreda malarska | `kreda-malarska` | 1 | **0** |
| 765 | Sadownictwo | `wapno-do-sadu` | **0** | 571 |
| 766 | Wapno do stawów | **`rybactwo-kat-archiwum`** | **0** | 393 |
| 769 | Hurtownie | `wapno-nawozowe-hurt` | **0** | 404 |

**Dla każdej z ośmiu ustal i udokumentuj:**

1. **Co oddaje pod swoim adresem** — kod HTTP, cel przekierowania, `meta robots`, canonical.
   Sprawdź też adres wynikający ze slugu **i** adres historyczny, jeśli slug był zmieniany
   (przypadek 766: nazwa mówi „Wapno do stawów", slug mówi `rybactwo-kat-archiwum`, a landing
   o stawach żyje pod **osobnym** adresem `/wapno-do-stawu/` — rozstrzygnij, co jest czym).
2. **Czy jest w sitemapie**, z jakim `lastmod`, i czy `lastmod` odpowiada realnej edycji.
3. **Werdykt GSC** (URL Inspection) + data ostatniego crawlu.
4. **Wyświetlenia, kliknięcia, pozycja za 90 dni** — z wymiaru `page`, plus rozkład intencji
   z `page × query` (do struktury, nie do sum).
5. **Czy ma popyt** — wolumen fraz, na które celuje, z DataForSEO, z sezonowością miesięczną.
6. **Kto wygrywa SERP** na jej frazę główną i **jakim typem strony** (sklep, poradnik, kategoria,
   Facebook, OLX). To rozstrzyga, czy kategoria ma sens, czy potrzebny jest inny typ strony.
7. **Czy nie kanibalizuje** innej naszej strony na tę samą intencję — porównaj pozycje.

**Rozstrzygnij per kategoria:** zostaje jako kategoria · zostaje, ale jako landing z ręcznym
listingiem · przekierowanie (dokąd i dlaczego) · usunięcie. **Uwaga na pułapkę Premmerce:** adres
produktu budowany jest z kategorii o **najwyższym `term_id`** (`PermalinkListener.php:248`,
sortowanie `DESC`), więc dopisanie produktów do kategorii o wysokim ID **przenosi ich adresy**.
To jest udokumentowany powód, dla którego staw dostał landing zamiast kategorii —
ADR `2026-08-21-nazwy-kategorii-bez-segmentow.md`.

---

## ETAP 2 — produkty: 19 kart, każda osobno

**Dla każdego z 19 produktów** (`post_type=product`, `post_status=publish`):

1. Adres kanoniczny i **wszystkie** adresy, pod którymi karta odpowiada 200 (stara baza `/produkt/`
   powinna dawać 301 przez moduł `legacy-urls` — **sprawdź, czy naprawdę daje, dla każdego slugu**).
2. Werdykt GSC + data crawlu + czy w sitemapie.
3. Wyświetlenia, kliknięcia, pozycja (90 dni, poziom strony).
4. Czy ma `SKU`, cenę w treści (widełki, nie cennik), `_price` **musi być puste** — tryb katalogu.
5. Czy parametry na froncie zgadzają się z kartą producenta — **render, nie baza**, bo warstw są cztery.
6. Czy karta renderuje się z `post_content`, czy z `_elementor_data` (307, 310, 320 — z Elementora).

**Osobno zbadaj znane wątpliwości:** karta **#307 Kreda pastewna** opisana parametrami wapna
tlenkowego (egzotermia, pH >12 — węglan tego nie robi) · **#303 Kreda czarna** i #302, #313, #316
bez wyceny · adres `/kreda-malarska/kreda-malarska/` ze zdublowanym członem · demo-produkt motywu.

---

## ETAP 3 — przekierowania i zgłoszenia: pełna inwentaryzacja, bo robione były w obie strony

**Zbierz w jednym miejscu wszystkie reguły z trzech niezależnych warstw** i sprawdź każdą na żywo:

1. **`.htaccess`** — blok `# BEGIN AGRIA 301` (reguły z lipca i z 19.08, m.in. `/kategoria-produktu/*`,
   `/wapno-nawozowe-hurt/`, `/wapno-do-sadu/`, `/kreda-pastewna/`). Pobierz przez FTP, wypisz **każdą
   regułę z celem i kodem odpowiedzi zmierzonym na żywo**.
2. **Moduł `modules/legacy-urls/legacy-urls.php`** — dwie funkcje: stara baza `/produkt/` → adres
   kanoniczny WooCommerce, oraz mapa wycofanych wpisów (dziś: `/ile-wapna-granulowanego-na-ha/`
   → `/wapnowanie-gleby/`, scalone 24.08).
3. **Premmerce** — przekierowania wynikające z konfiguracji wtyczki, nie z naszego kodu.

**Dla każdego przekierowania odpowiedz:** dokąd prowadzi, ile skoków, czy nie ma pętli, czy cel
odpowiada 200, **czy stary adres nadal zbiera wyświetlenia** (jeśli tak — ile i na jakiej pozycji;
`/wapno-do-sadu/wapno-weglanowe-…-luz-2/` zbierał 23 wyświetlenia na pozycji 7,6 **mimo 301**).

**Znane usterki do potwierdzenia lub obalenia:** `/wapno-do-stawow/` oddaje **404, nie 301** na
`/wapno-do-stawu/` · wpis `/czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/` ma w GSC werdykt
„Excluded by `noindex`" z crawla **18.04**, choć na żywo `noindex` nie ma · `/do-pobrania/` ma
werdykt `BLOCKED_BY_META_TAG` z crawla **12.04** mimo poprawnego stanu i zgłoszenia z 19.08.

**Zgłoszenia do Indexing API:** wypisz z `~/.claude/indexing-submit.log`, co i kiedy zgłaszaliśmy,
i **co z tego wyszło** — zestaw z werdyktem GSC. Trzy zgłoszenia sześciu adresów nie zadziałały;
sprawdź, czy przyczyna była poprawnie zdiagnozowana (diagnoza: `docs/audits/T-026-diagnoza-*`),
i czy po scaleniu z 24.08 coś się zmieniło.

---

## ETAP 4 — treści, które istnieją: co z nich żyje

Wypisz **wszystkie** wpisy i strony (nie tylko te z rejestru): adres, data publikacji i realnej
edycji, długość, werdykt GSC, wyświetlenia/kliknięcia/pozycja za 90 dni, frazy z `page × query`.

Rozstrzygnij dla każdej: **pracuje · nie pracuje, ale ma popyt · nie ma popytu · dubluje inną naszą stronę.**
Kanibalizację sprawdzaj zawsze przez porównanie pozycji na tej samej frazie, nie przez podobieństwo tematu —
diagnoza z 19.08 pomyliła te dwie rzeczy i zaproponowała scalenie strony, która wcale nie dublowała huba
(hub trzyma oś ILE na pozycji 8,2, a oś KIEDY na 34,1 — to są dwie różne strony, nie jedna).

---

## ETAP 5 — plan treści VIII–X: skonfrontuj z rzeczywistością i ułóż od nowa

**Dokumenty, które się nawzajem podważają — przeczytaj wszystkie, ale rozstrzygaj pomiarem:**
`docs/seo/T-052-AUDYT_FRAZ_I_PLAN_SEZON_2026-08-21.md` (bloki A–F) ·
`docs/seo/2026-08-21-sezonowosc-i-kolejnosc-M4.md` (pomiar sezonowości, który obalił część terminów) ·
`docs/seo/ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md` (częściowo unieważniona) ·
ADR-y z 11.08, 21.08 (×3) · `docs/REJESTR_ZOBOWIAZAN.md` (kolejka **i dziennik**).

**Do ustalenia dla każdej pozycji planu:**

1. **Czy już istnieje** — na produkcji, nie w dokumencie. Część „zaplanowanych" jest zrobiona.
2. **Wolumen i sezonowość** z DataForSEO, miesiąc po miesiącu, minimum 12 miesięcy wstecz.
   Zmierzone rozbieżności, które trzeba potwierdzić: `wapno na łąki` szczytuje w **marcu**, nie
   we wrześniu · sadownictwo szczytuje w **marcu**, listopad to 40 wobec średniej 210 ·
   `kreda pastewna` ma rozkład **płaski** · `wapno granulowane` szczytuje w **październiku (8 100)**.
3. **Kto zajmuje TOP10** i jakim typem strony. Zmierzone: na „wapno do stawu" trzy z siedmiu
   wyników TOP7 to posty z Facebooka — potwierdź, czy nadal.
4. **Czy mamy czym to napisać.** Parametry i dawki **wyłącznie ze źródeł** — a `data/zrodla/`
   **nie istnieje** (sprawdzone 24.08), mimo że terminarz cytuje IUNG-PIB. To jest blokada
   dla wszystkiego, co uprawowe.
5. **Termin publikacji wyliczony z sezonu**, nie z kolejności w dokumencie: treść ma być żywa
   i zaindeksowana **przed** szczytem, z zapasem na crawl — a crawl na tej domenie bywa liczony
   w tygodniach.
6. **Jeden adres na intencję.** Zanim zaproponujesz nowy URL: czy istniejąca strona nie obsłuży
   tej frazy lepiej. Próg z ADR 21.08: **≥3 frazy i ≥100 wyszukań/mies.**, liczone z GSC.

---

## Czego oczekuję na wyjściu

**Jeden dokument** `docs/audits/2026-08-XX-AUDYT_SEO_OD_NOWA.md`, z sekcjami odpowiadającymi etapom,
w którym **każdy wiersz ma dowód**. Plus:

1. **Tabela kategorii** — 8 wierszy, decyzja i uzasadnienie per wiersz.
2. **Tabela produktów** — 19 wierszy, stan indeksacji i adresów.
3. **Tabela przekierowań** — wszystkie reguły z trzech warstw, zmierzone na żywo, z oceną „zostaje /
   do zmiany / do usunięcia".
4. **Tabela treści** — wszystko, co opublikowane, z werdyktem „pracuje / nie pracuje / dubluje".
5. **Plan VIII–X od nowa** — jeden adres = jeden wiersz, z frazą wiodącą, wolumenem, szczytem
   sezonowym, blokadą, terminem i uzasadnieniem kolejności.
6. **Lista rozbieżności** między dokumentami a produkcją, każda z rozstrzygnięciem. To jest
   materiał na sprostowania w rejestrze.
7. **Przepisana sekcja treściowa `docs/REJESTR_ZOBOWIAZAN.md`** — po akceptacji Janka, nie z automatu.

**Czego NIE robić:** nie zmieniaj niczego na produkcji w tym wątku bez osobnej zgody — to jest audyt,
nie wdrożenie. Nie proponuj landingów do indeksu wbrew ADR 11.08. Nie zgłaszaj nic do Indexing API.
Nie pisz treści — najpierw ma być ustalone, co i kiedy.

**Zacznij od przeczytania:** `CLAUDE.md`, całe memory projektu, `docs/REJESTR_ZOBOWIAZAN.md`
(**obie części**), `docs/FAKTY_KLIENTA.md`. Dopiero potem dotykaj danych.
