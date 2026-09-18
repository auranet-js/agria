# Blok 2, domknięcie wrześniowego wdrożenia i decyzje — 18–30.09.2026

> **Projekt:** `agria` · **Zakres:** ryczałt R (Ads i OLX osobno, P)
> **Kolejność ustalona przez Janka 18.09:** **A → B → C**, Ads jako analiza bez dotykania konta.
> **Poprzedni blok:** blok 1 domknięty 14.09 — 19 kart v2 wdrożonych i zaakceptowanych, T-116 i T-117 zamknięte.
> **Protokół:** czytasz `00-PROTOKOL-WSPOLNY.md` **przed** tym plikiem. Zgoda Janka na każdy zapis, per operacja.
>
> **O czym jest ten wątek:** wrzesień dowiózł najwięcej treści w historii projektu i **ani jeden pomiar po nim
> jeszcze nie zapadł**. Blok 2 zaczyna się więc nie od pisania, tylko od dowiezienia tego, co napisane:
> zgłoszenia do indeksu, trzy kontrole, materiał pod decyzje. Treść wchodzi dopiero w §6, po D1.

---

## 0. Czego NIE zakładać

Zmierzone 18.09.2026, nie przypuszczane. Pierwsze trzy punkty przewracają zapisy, które stoją dziś w rejestrze.

1. ⚠️ **Kampanie Google Ads NIE są wstrzymane.** Rejestr i memory mówią „pauza przedłużona poza 14.09" —
   odczyt API 18.09 pokazuje **wszystkie trzy kampanie `ENABLED` / `SERVING`**: Rolnictwo (60 zł/dz),
   Paszarstwo (9 zł/dz), Marka (5 zł/dz). Emisja szła nieprzerwanie. **Zapis w rejestrze jest nieprawdziwy
   i wymaga sprostowania** (§8), a nie powtórzenia.
2. ⚠️ **Prognoza „wrzesień pójdzie na ~1 800 zł" się nie sprawdza.** Zmierzone: **01–17.09 to 749,17 zł**,
   453 kliknięcia, 4 377 wyświetleń, **2 konwersje**. Rytm: nd/pn/wt po ~70 zł, pozostałe dni 2–16 zł.
   Projekcja do 30.09 to **ok. 1 240 zł** wobec 1 200 zatwierdzonych — przekroczenie rzędu 3%, nie 50%.
   Harmonogram dowozi to, czego nie dowiózł limit dzienny. **T-109 zmienia przedmiot:** nie „kiedy wznowić",
   tylko „czy zostawiamy do końca sezonu".
3. ⚠️ **Profil GBP `Agria Niedomice` JEST na koncie** — `locations/11295576611408862023`, Fabryczna 17,
   `hasVoiceOfMerchant: true`, weryfikacja przeszła (Janek ją przechodził). **Radgoszcza nadal nie ma**,
   zero oczekujących zaproszeń. T-047 przechodzi z „czekamy na dostęp" na „do wypełnienia w połowie".
4. **Wszystkie 19 kart renderuje dziś z `post_content`** — 310 i 320 przełączone w T-136 (14.09). Stary zapis
   „karty 307 / 310 / 320 renderują z `_elementor_data`" jest **nieaktualny**; ich `_elementor_data` to martwe
   kopie, nie edytuj ich jako treści.
5. **Do indeksu wchodzi się wyłącznie ręcznym „Poproś o zindeksowanie" w panelu GSC.** Linkowanie nie wprowadza
   (dowód: 16 dni na czterech adresach Fazy 0, zero pobrań), Indexing API też nie (trzy zgłoszenia z T-094).
   Panel ma **własny limit dzienny** — 14.09 padł po jedenastu kartach. To nie jest pula 200/dobę z globalnego
   CLAUDE.md §10a i **nie wolno jej mylić z `~/bin/index-submit`**.
6. **`?cb=` nie jest narzędziem weryfikacji** po WP Rocket — rozgrzewka jednym żądaniem, pomiar na czystym
   adresie. Do porównania „z Rocketem / bez" służy `?nowprocket=1` i tak to opisujesz.
7. **WP-CLI `term update` przepuszcza opis przez `wp_filter_kses`** i wycina tabele oraz nagłówki. Opisy
   kategorii zapisujesz **przez MCP `query_db_write`**, po zapisie porównujesz **MD5 z plikiem źródłowym**.
8. **Nie zeruj `_elementor_element_cache` przez `a:0:{}`** — Elementor czyta to jako poprawny pusty render
   i wygasza treść na produkcji (incydent 30.07). Po zmianie: `wp elementor flush-css` + `wp cache flush`.
9. **Parametry wyłącznie z kart producentów** (Nordkalk, Lhoist) i rozporządzeń — nigdy z rozumowania.
   Nazwa producenta i kopalni TAK, marka producenta NIE (memory `feedback_agria_nazwy_producent_nie_marka`).
10. **Zmiany na produkcji idą przez SSH** (`ssh agria-prod` na początku polecenia, bez `cd`/pętli/`timeout`
    przed), MCP zapasowo. Backupy do `~/agria-backups/<zadanie>/`, nie `.bak` obok pliku w web root.
11. **CTR liczysz z poziomu strony, nie z sumy zapytań** — próg prywatności GSC ukrył kiedyś 85% kliknięć
    i na zaniżonej liczbie powstało niepotrzebne zadanie.
12. **Nic nie idzie do klienta.** Wszystko przez Janka na `js@auranet.com.pl`, kanał `~/bin/send-to-jan`.

---

# A. Domknięcie wrześniowego wdrożenia

## 1. Zgłoszenie czterech kart v2 w GSC — **zaległe z 15.09, robisz pierwsze**

19 kart v2 wdrożono 14.09. Po jedenastu zgłoszeniach panel odbił resztę komunikatem „Przekroczono limit".
Czekają cztery:

| ID | Karta | Stan |
|---|---|---|
| **#311** | Agrobielik 90 | wdrożona i zaakceptowana 14.09, „URL unknown to Google" w pomiarze 24.08 |
| **#318** | węglanowe z magnezem, odmiana 04 | jw. |
| **#302** | Dolomit | jw., werdykt „Discovered — not indexed" |
| **#320** | wapno palone mielone | jw., render przełączony na `post_content` w T-136 |

**Metoda:** Chrome MCP, panel GSC, URL Inspection → „Poproś o zindeksowanie". Po każdym zgłoszeniu zrzut
ekranu albo odczyt komunikatu — **„wysłałem" bez potwierdzenia z panelu nie liczy się jako zrobione**.
Jeśli limit padnie wcześniej, zapisujesz, które weszły, a które zostają na jutro, i mówisz to wprost.

**Zrobione, gdy:** cztery adresy mają potwierdzenie z panelu albo wpis „odbite limitem, termin: <data>".

## 2. Kontrola indeksacji — Faza 0 plus 19 kart v2

Dwa pytania w jednym przebiegu, bo jedno narzędzie: `scripts/gsc_inspect.py` (URL Inspection API).

**(a) Faza 0 — kontrola przesunięta z 15.09.** Cztery adresy zgłoszone ręcznie 09.09:
`/wapno-do-stawu/`, `/wapno-do-stabilizacji-gruntow/`, `/jak-stosowac-wapno-nawozowe/`,
`/wapno-nawozowe-na-trawnik/` plus `/higienizacja-osadow-sciekowych-wapnem/`.
**Pytanie: czy weszły do indeksu i czy się w nim utrzymały** — interesuje `lastCrawlTime` i werdykt,
nie pozycje. To warunek wejścia w Fazę 2.

**(b) 19 kart v2 — pierwszy pomiar po wdrożeniu.** Czy Google pobrał nową treść i z jaką datą.
Karty zgłaszane 14.09 powinny mieć crawl 14–15.09; jeśli któraś go nie ma mimo zgłoszenia, to jest
nowy fakt i wraca do Janka jako pytanie, nie jako kolejne zgłoszenie.

**Zapis:** `data/kontrole/2026-09-18-indeksacja-karty-i-faza-0.md` — tabela adres / werdykt / lastCrawlTime /
zgłoszony ręcznie kiedy. Bez rekomendacji w tym pliku, same fakty.

**Zrobione, gdy:** plik istnieje, 24 adresy mają werdykt, a wniosek „Faza 2 otwarta / zamknięta" jest
napisany jednym zdaniem i pokazany Jankowi.

## 3. Kontrola T-092 „opis kategorii /wapno-nawozowe-rolnictwo/" — 14 dni

Wdrożone 04.09, kontrola należy się **18.09, czyli dziś**.

**Źródło: GSC**, nie DataForSEO (nowe treści widać tam z opóźnieniem). Baseline:
`data/T-092/baseline-gsc-2026-09-04.json`.

**Mierzysz frazy formowe o realnym wolumenie, nie frazę główną:** `wapno węglanowe` (1 000/mies., przed
zmianą 627 wyświetleń na **5 URL-i**, pozycja ważona 15,3), `kreda nawozowa` (1 000, 30 wyświetleń, 24,2),
`wapno tlenkowe` (720, 40 wyświetleń, 20,2), `kreda nawozowa sypka` (kategoria już na 8,2).

**Dwa pytania:** czy kategoria wchodzi na te frazy i **czy spada liczba konkurujących własnych URL-i**
(to drugie jest ważniejsze — kanibalizacja była mierzona i opisana w `data/seo/2026-09-04-kanibalizacja-wapno-nawozowe.md`).

⚠️ **Okna równe albo nie ma pomiaru.** Dane GSC dojrzewają ~3 dni, więc „14 dni po" to realnie 14 dni do
ostatniego dojrzałego, a porównujesz z tyloma samymi dniami przed. Przy T-053 ta różnica decydowała o werdykcie.

**Zapis:** `data/kontrole/2026-09-18-kontrola-T-092.md`. Werdykt w trzech stanach: **zadziałało /
nie zadziałało / za wcześnie na wniosek** — ten trzeci jest dopuszczalny i lepszy od naciągania.

## 4. Ads — materiał pod decyzję, **zero zmian na koncie**

Konto obsługujesz **wyłącznie w odczycie**. Wstrzymania, wznowienia i zmiany budżetu robi Janek sam.

**(a) Sprostowanie stanu.** Odczyt `campaign.status`, `serving_status`, budżety, koszt dzienny 01–30.09,
konwersje per kampania i per typ. Ustal, **od kiedy dokładnie kampanie chodzą nieprzerwanie** i skąd wziął
się zapis o pauzie — to wchodzi do rejestru jako sprostowanie, nie jako przypis.

**(b) T-113 „jakość strony docelowej poniżej średniej na 34 z 37 fraz".** To jedyna realna dźwignia kosztowa
przy MANUAL_CPC z wyłączonym eCPC i **właśnie przestała być zablokowana**, bo 19 kart dostało nową treść.
Odczyt `ad_group_criterion.quality_info.creative_quality_score`, `post_click_quality_score`,
`search_predicted_ctr` per fraza, z datą pomiaru. **Porównaj ze stanem z 07.09** (`data/kontrole/2026-09-07-odczyt-ads-7-dni.md`)
— pytanie brzmi, czy przepisane karty ruszyły ocenę strony docelowej.
⚠️ Google odświeża te oceny z opóźnieniem; jeśli od zmiany minęło za mało czasu, **mówisz to i wyznaczasz
termin powtórki**, zamiast interpretować stary wynik.

**(c) T-110 „konwersja główna stoi na kanale o masie 4 zdarzeń kwartalnie"** i **T-111 „58,6% budżetu wychodzi
przy zamkniętym biurze"** — odśwież obie liczby na danych wrześniowych. Przy 2 konwersjach na 749 zł
(**375 zł za konwersję**) pytanie o to, co w ogóle liczymy jako konwersję, jest ważniejsze niż stawki.

**Zapis:** `data/kontrole/2026-09-18-odczyt-ads.md`. Na końcu **jedna tabela decyzyjna dla Janka**:
opcja / co daje / co kosztuje / czego nie wiemy. Bez rekomendacji wielowariantowej — jedna rekomendacja,
reszta jako odrzucone z powodem.

---

# B. Decyzje D1–D4 — quizem, na faktach

Warunek postawiony przez Janka 10.09 jest spełniony: baza wiedzy produktowej gotowa 11.09
(`docs/produkty/` — 19 plików, `_macierz-fraz.csv` z 581 frazami, `_WNIOSKI.md`), pilot i komplet kart
wdrożone i zaakceptowane 14.09.

**Otwierasz `docs/produkty/_WNIOSKI.md` §5 i pytasz z faktów, nie z pamięci i nie z audytów sprzed sierpnia.**

| | Decyzja | Co odblokowuje |
|---|---|---|
| **D1** | podział kategorii + adresy produktów przy wielu kategoriach | układ października: gdzie mają wisieć poradniki T-071, T-080, T-081 |
| **D2** | cel reklam | co robimy z kampaniami, które chodzą dalej (§4) |
| **D3** | stabilizacja gruntów — **zaindeksowana, nie odpublikowujemy** | domknięcie zaszłości, decyzja właściwie zapadła |
| **D4** | staw i „kreda do stawu" | T-071 i T-070, oba z terminem 10.10 |

**Forma:** `AskUserQuestion`, 2–4 warianty na pytanie, wariant z rekomendacją pierwszy, opcja „nie wiem /
pytamy klienta" zawsze obecna. Podpowiedzi budujesz z tego, co realnie widzisz w danych — nie z powietrza.
**Przy każdym wariancie jedno zdanie, co daje albo co blokuje**, inaczej Janek nie ma na czym oprzeć decyzji.

⚠️ **Pułapka D1:** Premmerce bierze kategorię o najwyższym `term_id`, ale `rank_math_primary_product_cat`
to nadpisuje — **druga kategoria może zmienić adres produktu**. Zanim zaproponujesz cokolwiek w D1,
sprawdź primary category na wszystkich 19 kartach (memory `project_agria_premmerce_kategoria_adres`).

**Zapis decyzji:** `[J <data>]` przy każdej, ADR w `docs/decyzje/2026-09-<dd>-D1-D4-architektura.md`.
Słownik: **kategoria / karta / poradnik** — bez „landing" i „segment".

**Zrobione, gdy:** cztery decyzje mają zapis `[J]`, ADR jest w repo, a wiersze rejestru dotknięte przez
D1 są przepisane w tym samym commicie.

---

# C. Treść z terminem

**Wchodzi dopiero po D1** — bo D1 rozstrzyga, pod jakimi kategoriami te strony mają wisieć.
Jeśli D1 przeciąga się poza 20.09, **wracasz z pytaniem**, a nie piszesz treści „na wszelki wypadek".

## 5. T-085 „kategoria /wapno-hydratyzowane/ — przepisanie pod frazę" — termin 20.09

`wapno hydratyzowane` **2 400/mies.** (III 3 600), kategoria zaindeksowana, crawl 21.08, stoi na **31,3**.
Rozstrzygnięte ADR-em 24.08: **rozbudowa kategorii, nie nowy adres.**
To druga połowa zobowiązania z maila do Kasjana z 06.08 — pierwsza (T-084) czeka.

⚠️ **Inny odbiorca i inny język niż rolnik** — budowlanka, nie pole. Zero żargonu mimo to:
„cena za towar, bez transportu", nie „loco magazyn".

**Wzorzec wykonania: T-092 i T-078.** Zaczynasz od **wyciągnięcia zapytań GSC dla tego adresu z 28 dni** —
przy kredzie pastewnej ten krok pokazał, że klaster pyta o dawkowanie, nie o produkt, i przestawił całą oś
treści. Baseline przed zmianą do `data/T-085/`.

## 6. T-093 „/wapno-do-oczyszczalni/ — wchłonięcie merytoryki poradnika" — termin 20.09

Najlepszy CTR kategorii w serwisie: **3,97%**, 806 wyświetleń, 32 kliknięcia, pozycja 9,5, crawl 22.08.
Zbiera **całą** intencję osadową, podczas gdy poradnik `/higienizacja-osadow-sciekowych-wapnem/` ma zero
wyświetleń i nigdy nie był pobrany. **Poradnik zostaje osobnym adresem** (decyzja Janka 24.08), merytoryka
pracuje w kategorii. Listing kategorii ma od 14.09 cztery produkty zamiast jednego — treść ma to odzwierciedlać.

## 7. T-074 „spoke ziemniaki" — termin 20.09

`wapno pod ziemniaki` 50/mies. (**IX–X 110**) — jedyny spoke uprawowy z potwierdzonym szczytem jesiennym.
⚠️ Wchodzi **od zmianowania i przedplonu**; parch i dawka pogłówna w redliny są już w terminarzu
`/jak-stosowac-wapno-nawozowe/` — nie powtarzaj ich, linkuj.

---

# D. Poza kolejnością — rzeczy z własnym terminem

## 8. GBP Niedomice — profil odzyskany, do wypełnienia

Stan zmierzony 18.09 wobec Tarnowa:

| | Tarnów | Niedomice |
|---|---|---|
| kategoria główna | Dostawca nawozów | **Zakład chemiczny** ❌ |
| kategorie dodatkowe | 4 | **brak** |
| WWW | `https://agria.pl/` | **brak** ❌ |
| obszar obsługi | 4 województwa | **brak** |
| opis | pełny, z produktami | jedno zdanie |
| telefon | 14 621 88 21 | 664 393 062 (Paweł) |
| publikacje | rytm tygodniowy | **zero** |

Dwie pozycje są pilne, reszta może poczekać: **kategoria** (decyduje, na jakie zapytania profil w ogóle
wchodzi do pakietu lokalnego — dziś stawia magazyn wapna poza klastrem nawozowym) i **brak linku do agria.pl**.

⚠️ **GBP nie ma cofnięcia zmiany.** Przed każdą operacją `scripts/gbp_dump.py` do `tmp/`, zgoda Janka
per pole. Numer telefonu **nie do ruszania bez ustalenia z Pawłem** — edycje numeru przechodzą moderację
i potrafią nie wejść (precedens z 01.09 na Tarnowie).
**Radgoszcz zostaje otwarty w T-047** — nie ma go na koncie, zero oczekujących zaproszeń.

## 9. Wizytówka Tarnów — publikacje 23.09 i 30.09

Rytm wtorkowy z T-121. Teksty gotowe: `docs/gbp/2026-09-08-blok0-publikacje-i-opinie.md`.
**Post z 16.09 przepadł** — publikacji nie da się datować wstecz, nie próbuj nadrabiać dwoma naraz.
**30.09 = koniec zapasu tematów**, tego dnia przygotowujesz kolejne cztery na październik.
Zdjęcie tylko JPG lub PNG (uploady agria.pl są `.jpg.webp` — nie przejdą).

## 10. Kontrola T-078 „opis kategorii /paszarstwo/" — 26.09

Na **frazach formowych** klastra (`kreda pastewna dawkowanie`, `… dla bydła dawkowanie`,
`ile kredy pastewnej dla kur na 100 kg`), nie na frazie głównej. Baseline `data/T-078/baseline-gsc-2026-09-08.json`:
**462 wyświetlenia i zero kliknięć**, więc **każde kliknięcie jest zmianą jakościową**.

---

## 11. Rejestr — co ten blok ma sprostować

Trzy wiersze mówią dziś nieprawdę i **commit zamykający którąkolwiek pozycję ma je poprawić w tym samym commicie**:

1. **T-109 / nagłówek rejestru** — „pauza przedłużona poza 14.09", „wrzesień idzie na ~1 800 zł".
   Kampanie chodzą nieprzerwanie, wrzesień idzie na ~1 240 zł. Sprostowanie z liczbami i datą odczytu.
2. **T-105 „odnowienie pakietu OLX Premium 200"** — **zamknięte**. Monitor `data/olx/monitor-log.json`:
   16.09 `dni_pakietu: 0`, 17.09 **29**, 200/200 `active`, zero braków. Paweł przedłużył, nic nie zgasło.
3. **T-047 „odzysk profili GBP"** — Niedomice odzyskane i zweryfikowane, zostaje Radgoszcz.
   Pozycja przechodzi z 🟡 „czeka na AGRIĘ" na 🔴 w części Niedomic.

Plus `CLAUDE.md` §4 pkt 2 — zapis o kartach renderujących z `_elementor_data` jest już poprawiony (14.09),
sprawdź tylko, czy prompt T-136 i memory nie ciągną starej wersji.

---

## 12. Definicja „zrobione" dla całego bloku

| Pozycja | Zrobione, gdy |
|---|---|
| §1 zgłoszenia GSC | cztery karty mają potwierdzenie z panelu albo zapisany powód odbicia |
| §2 kontrola indeksacji | `data/kontrole/2026-09-18-indeksacja-karty-i-faza-0.md` z 24 werdyktami + zdanie o Fazie 2 |
| §3 kontrola T-092 | `data/kontrole/2026-09-18-kontrola-T-092.md`, okna równe, werdykt w trzech stanach |
| §4 Ads | `data/kontrole/2026-09-18-odczyt-ads.md` + tabela decyzyjna, **zero zmian na koncie** |
| §B D1–D4 | cztery zapisy `[J]`, ADR w `docs/decyzje/`, wiersze rejestru przepisane |
| §5–7 treść | render zweryfikowany po cache-buście, baseline GSC przed zmianą, wiersz rejestru z dowodem |
| §8 GBP Niedomice | zrzut przed, zgoda per pole, odczyt po zmianie potwierdzający zapis |
| §11 rejestr | trzy sprostowania w repo |

**Słowa „zrobione / działa / sprawdzone" używasz wyłącznie z dowodem obok** — wykonana komenda i jej wynik,
URL po zmianie, diff, zrzut. Bez dowodu piszesz „niezweryfikowane" i weryfikujesz przed raportem.
