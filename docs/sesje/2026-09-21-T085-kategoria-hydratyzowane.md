# Sesja 2026-09-21 (druga) — T-085, czyli kiedy 2 400 wyszukań nic nie znaczy

> **Zakres:** R (treść, pomiar) · **Stan produkcji na koniec sesji:** opis termu 768 wdrożony, adres
> zgłoszony w GSC · **Do commita:** `docs/REJESTR_ZOBOWIAZAN.md`, `data/T-085/`, ten plik

---

## 1. Co zostało zrobione

**T-085 — opis kategorii `/wapno-hydratyzowane/`** (term 768): 468 B → **2 407 B**, 1 → 3 × H2,
2 → 5 linków, render strony 4 395 → **5 967 znaków**. Zapis `$wpdb->update` przez `wp eval-file` po SSH,
MD5 w bazie zgodny co do znaku z plikiem. Backup:
`~/agria-backups/T-085/przed-T085-term-taxonomy-20260921-171304.sql`. Zgłoszone w GSC tego samego dnia.

**Zakres zadania zmieniony w trakcie, za zgodą Janka.** Rejestr mówił „rozbuduj opis pod frazę
`wapno hydratyzowane` 2 400/mies., bo adres stoi na 31,3". Trzy pomiary pokazały, że tego wolumenu
nie da się obsłużyć — szczegóły niżej. Napisana i odrzucona wersja pełna 5 788 B leży
w `data/T-085/opis-768-v2.html`; wdrożona jest przycięta wersja segmentowa.

**Pytanie do klienta zamknięte** — Kazimierz odpowiedział 21.09 na pięć pytań wysłanych Telegramem
przez Janka. Pytanie nr 2 z listy do Pawła („czy budownictwo to realny segment") wykreślone z rejestru.

---

## 2. Siedem ustaleń z tej sesji

1. **Karta bije kategorię pięciokrotnie.** Baseline GSC 28 dni: `/wapno-hydratyzowane/bielik/`
   **584 wyśw. / 10 klik. / poz. 7,3**, kategoria **122 / 2 / 30,0**. Na samej frazie
   `wapno hydratyzowane` kategoria stoi na **39,6**.
2. **SERP na tę frazę jest detaliczny i to jest powód, dla którego odpuszczamy.** Castorama, Leroy
   Merlin, Allegro, OBI, Bricoman, Ceneo, PSB Mrówka — worek 20–30 kg w markecie. AGRIA poza TOP20
   na `wapno hydratyzowane`, `wapno hydratyzowane cena` i `wapno budowlane`. „Ludzie pytają też":
   *czy nadaje się do ogrodu / do malowania / ile wapna na 10 litrów wody*.
3. **Nie ma frazy zadaniowej „wapno do…", którą dałoby się tu podstawić** — sprawdzone na wprost
   zadane pytanie Janka. `wapno do bielenia drzew` 1 900 (III **9 900**) to wiaderka 1–2 kg
   w marketach; `wapno do uzdatniania wody` **<10** mimo obecności w karcie producenta;
   `mleko wapienne` 590 przy konkurencji LOW jest definicyjne (Wikipedia, chemia laboratoryjna).
4. **Kanibalizacja kategoria ↔ karta jest naszego autorstwa** (`git log -S`): title karty wstawiony
   **14.09 w T-136** (`e1596fa`), title i focus keyword kategorii — w audycie sierpniowym (`8f2bfb3`).
   Przy przepisywaniu karty nie sprawdziłem, co stoi po drugiej stronie na tej samej frazie.
   To samo przeoczenie co przy `wapno nawozowe`.
5. **Slug `wapno-hydratyzowane` jest nietykalny** — Premmerce buduje adres produktu ze slugu kategorii,
   więc zmiana slugu przeniosłaby kartę stojącą na 7,3. Nazwę, H1 i title można ruszać, adres nie.
6. **Kazimierz (21.09): kupują składy, hurtownie, oczyszczalnie ścieków i firmy przerabiające osady.**
   Wykonawcy indywidualnemu na budowę **z zasady się nie dostarcza** — chcą długich terminów płatności,
   ryzyko wypłacalności zbyt duże. To decyzja handlowa, nie luka. Certyfikaty idą z fakturą przy każdej
   dostawie. Uzdatnianie wody: dzieje się (Bielik i „super białe" z Lhoista), ale podstawy stosowania
   nie zna.
7. **Popyt AGRII nie siedzi w wyszukiwarce, tylko w relacjach handlowych.** To jest wniosek ogólny,
   nie dotyczy wyłącznie tej kategorii — przy każdym kolejnym „fraza ma X wyszukań" trzeba najpierw
   sprawdzić, czy SERP jest B2B, czy marketowy.

---

## 3. Co jest otwarte — w kolejności ważności

### P1. Jedna zaległa pozycja treściowa

- **T-074 „spoke ziemniaki"** — `wapno pod ziemniaki` 50/mies., **szczyt IX–X 110**, termin minął 20.09,
  okno zamyka się w ciągu dwóch tygodni. Wchodzi od zmianowania i przedplonu; parch i dawka pogłówna
  są już w terminarzu `/jak-stosowac-wapno-nawozowe/` — linkować, nie powtarzać. Wzorzec wykonania:
  T-092, T-078, T-093, T-085 — **zaczyna się od baseline'u GSC**, a od tej sesji także
  **od SERP-u**, zanim powstanie jakakolwiek treść.

### P2. Terminy tego tygodnia

- **23.09 (wt)** — publikacja na wizytówce Google, teksty w `docs/gbp/2026-09-08-blok0-publikacje-i-opinie.md`.
  ⚠️ Publikacji nie da się datować wstecz; post z 16.09 przepadł — nie nadrabiać dwoma naraz.
- **26.09** — kontrola T-078 `/paszarstwo/` na frazach formowych, baseline
  `data/T-078/baseline-gsc-2026-09-08.json` (462 wyświetlenia, zero kliknięć).
- **30.09** — T-077 „poradnik o kredzie pastewnej" + przygotowanie czterech tematów GBP na październik.

### P3. Do założenia i do rozstrzygnięcia

- **Poradnik o bieleniu budynków inwentarskich** — ściany 320 + kurnik 170 + obora 20 ≈ **510/mies.,
  szczyt IX i III**, SERP **niezabrany przez markety** (fermo.pl „wapno super białe 7 kg", hodowlany.pl
  „malowanie kurnika i budynków inwentarskich", expondo „bielenie obory"). Odbiorcą jest rolnik, czyli
  publiczność reszty serwisu. **Materiał na klaster rolniczy, nie na kategorię produktową.** Nie ma
  jeszcze numeru T-NNN.
- **Nazwa kategorii „Budownictwo"** wobec tego, komu realnie sprzedajemy — do D1, razem z `rank_math_primary_product_cat`
  na 19 kartach (⚠️ #309 nie ma tego pola, więc Premmerce bierze kategorię o wyższym `term_id` = 768).
- **„Wapno super białe" z Lhoista** — wymienione przez Kazimierza, obecne w SERP-ie konkurencji,
  nie ma go wśród naszych 19 kart. Nie wiadomo, czy AGRIA je sprzedaje.
- **Trzy pytania bez odpowiedzi**: deklaracja właściwości użytkowych z CE dla CL 90-S · próg, od którego
  obowiązuje cena workowa 1 220 zł/t · **sześć pytań technicznych do Kazimierza z 08.09 plus T-108
  (dolomit) — wiszą od trzynastu dni**.
- **„Gdzie znikają kliknięcia Ads"** — 453 kliknięcia wobec 74 sesji Paid Search w GA4. Do 15.10 to
  największa niewiadoma projektu. Pomiar: licznik żądań z `gclid` po stronie serwera, ok. godziny roboty.
- **T-113 „jakość strony docelowej poniżej średniej"** — 72% wydatku Ads prowadzi na dwa landingi
  `noindex`. Pierwszy sygnał: kontrola Marki **02.10**.

---

## 4. Zauważone obok, nieruszone

1. **Puste kategorie** — „Sadownictwo" (765) i „Hurtownie" (769) mają **zero produktów**, opisy 602 i 420 B.
   Janek 21.09: „nie obchodzą mnie puste kategorie, z jakiegoś powodu są puste". Nie proponować.
2. **`wapno bielik 30 kg cena` — 31 wyświetleń na opakowanie, którego nie sprzedajemy.** Rynkowy worek
   to 20–30 kg, nasz 25. Nie wiadomo, czy rynek myli produkty, czy gdzieś jest wersja 30 kg.
3. **Rozjazd terminu T-085 w rejestrze** — KOLEJKA mówiła 20.09, lista pytań do Pawła 20.10. Wiersz
   zamknięty na dacie z KOLEJKI, rozjazd nie prostowany osobno.

---

## 5. Czego nie zakładać w następnej sesji

1. **Nie proponuj rozbudowy `/wapno-hydratyzowane/` pod frazę ogólną.** Zmierzone i rozstrzygnięte
   21.09: SERP detaliczny, popyt niesprzedawalny. Dowód w `data/T-085/serp-2026-09-21.json`.
2. **Nie zmieniaj slugu kategorii 768** — przeniesie adres karty #309 stojącej na 7,3.
3. **Nie pisz, że kategoria „Budownictwo" obsługuje wykonawców.** Nie dostarczamy im z zasady.
4. **Nie zapisuj opisu termu przez `wp term update` ani `wp_update_term`** — kses zdejmuje tabele
   i nagłówki. Jedyna droga: `$wpdb->update` przez `wp eval-file` albo MCP `query_db_write`.
5. **Nie owijaj tabeli w `<div style="overflow-x:auto">`** — render zjada `style` z diva. Czysty
   `<table>`, maksymalnie pięć kolumn ze względu na telefon.
6. **Nie przyjmuj wolumenu z planera za dowód szansy.** Od 21.09 kolejność jest twarda:
   **baseline GSC → SERP → dopiero treść.** W tej sesji sam wolumen wskazałby frazę, która jest
   w całości marketowa.
7. **Nie pisz o właściwościach biobójczych ani dezynfekcji** — produkty biobójcze mają własny reżim
   rejestracyjny (BPR 528/2012), a wapno AGRII jest sprzedawane jako nawozowe i budowlane.
8. **SSH do agrii potrafi odbić timeoutem** i zadziałać przy powtórce. Polecenie musi **zaczynać się**
   od `ssh agria-prod` lub `scp`, bez `cd &&` i bez pipe'a przed nim.
9. **Notatka i pytania do Janka idą Telegramem** (`~/secrets/telegram/`), krótko — tak poszły pytania
   do Kazimierza 21.09. Maile do klienta: nigdy bezpośrednio, tylko `~/bin/send-to-jan`.

---

## 6. Prompt do nowego wątku

```
Kontynuujemy AGRIĘ. Przeczytaj docs/sesje/2026-09-21-T085-kategoria-hydratyzowane.md (ta sesja)
i docs/REJESTR_ZOBOWIAZAN.md (sekcja KOLEJKA + Terminy najbliższe).

Stan: T-093 i T-085 zamknięte 21.09, oba adresy zgłoszone w GSC. T-085 zamknięte w zakresie
ZMIENIONYM — frazy `wapno hydratyzowane` świadomie nie gonimy, bo SERP jest detaliczny
(Castorama, Leroy, Allegro); nie wracaj do pomysłu rozbudowy tej kategorii.

Zaległa jest jedna pozycja treściowa: T-074 „spoke ziemniaki" (`wapno pod ziemniaki` 50/mies.,
szczyt IX-X 110, okno zamyka się w dwa tygodnie). W tym tygodniu twarde terminy: 23.09 publikacja
na wizytówce, 26.09 kontrola T-078 /paszarstwo/, 30.09 T-077 poradnik o kredzie pastewnej plus
cztery tematy GBP na październik. Kontrole 05.10: T-085 i T-093.

Zacznij od T-074. Kolejność od tej sesji jest twarda: baseline GSC dla adresu
(scripts/gsc_baseline.py --dni 28, do data/T-074/) → SERP mobile PL (scripts/dfs_serp.py,
location_code 2616) → dopiero treść do akceptu z linkiem na auratest → po „ok" zapis przez
$wpdb->update → weryfikacja renderem z cache-bustem → zgłoszenie w GSC przez Chrome MCP →
wiersz w rejestrze i dzienniku M4 w tym samym commicie.

Jeśli SERP pokaże, że fraza jest marketowa jak przy T-085 — wróć z tym, zanim cokolwiek napiszesz.

Pokaż plan przed wykonaniem i czekaj na „działaj".
```
