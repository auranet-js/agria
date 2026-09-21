# Sesja 2026-09-21 — przegląd kolejki, zaległe zgłoszenia GSC, opis kategorii Oczyszczalnie (T-093)

> **Zakres:** R (treść, indeksacja) · **Stan produkcji na koniec sesji:** opis termu 767 wdrożony,
> pięć adresów z crawlem 21.09 · **Do commita:** `docs/REJESTR_ZOBOWIAZAN.md`, `data/T-093/`,
> `docs/przypomnienia/2026-10-05-kontrola-T-093.md`, ten plik

---

## 1. Co zostało zrobione

**Zgłoszenie czterech kart v2 w GSC** — zaległość z 19.09. #311 Agrobielik 90, #318 węglanowe z Mg
odm. 04, #302 Dolomit, #320 wapno palone mielone. Przed operacją wszystkie cztery miały crawl
**09.09**, czyli sprzed wdrożenia v2 z 14.09 — Google znał adresy, nie znał treści.

**T-093 — opis kategorii `/wapno-do-oczyszczalni/`** (term 767): 976 B → **8 732 B**, 1 → 7 × H2
i 4 × H3, 2 → 8 linków wewnętrznych, render strony 4 983 → **11 311 znaków**. Zapis przez
`$wpdb->update` (`wp eval-file` po SSH), backup `db_export` + poprzedni opis 1:1 w repo.
Przebieg i uzasadnienie treści: `data/T-093/wdrozenie-2026-09-21.md`.

**Weryfikacja indeksacji po zgłoszeniach** — pięć adresów (kategoria + cztery karty) ma crawl
**2026-09-21**, wszystkie `PASS`. Ręczne zgłoszenie panelowe zadziałało w ciągu godziny.

---

## 2. Siedem ustaleń z tej sesji

1. **Ręczne zgłoszenie w GSC działa i jest szybkie** — pięć adresów pobranych tego samego dnia.
   Potwierdzenie mechanizmu z 09.09. Indexing API nadal nie jest do tego potrzebne.
2. **Poradnik `/higienizacja-osadow-sciekowych-wapnem/` żyje** — 157 wyświetleń i 2 kliknięcia
   (21.08–17.09) wobec zapisu „zero wyświetleń, nigdy nie pobrany" w rejestrze. Sprostowane.
   Cztery frazy ma wspólne z kategorią i na każdej stoi niżej → materiał do D1.
3. **`wapno do szamba` to druga fraza tej kategorii** — 55 wyświetleń, poz. 10,3, zero kliknięć,
   70 wyszukań miesięcznie w planerze. Strona nie miała o tym ani zdania.
4. **Bielik jest jedynym produktem tej kategorii w workach 25 kg** — i jedynym, który nadaje się
   do ręcznej pracy przy zbiorniku (gaszony fabrycznie). Wapno palone reaguje z wodą gwałtownie.
5. **Rozstrzygnięcie Kazimierza (21.09, dwa kroki):** wapno wchodzi **wyłącznie do zbiornika
   opróżnionego z osadu** — do odkażenia i wybielenia ścian. Do zbiornika w pracy nie, jeśli
   stosowane są biopreparaty; tak samo do pracującej oczyszczalni biologicznej. Przy okazji wymienił
   zastosowania **spoza tej kategorii: kurniki, obory, kompostowniki, odkażanie gleby**.
6. **Kanał workowy to sklepy i hurtownie** (decyzja Janka 21.09) — palety, nie pojedyncze worki
   (zapis Pawła 07.08). Cena workowa Bielika **1 220 zł/t** opublikowana pierwszy raz, wyłącznie
   jako przeliczenie na tonę.
7. **Szablon renderuje opis kategorii nad listingiem.** Po zmianie do kafelków jest ~9 150 znaków
   tekstu (przed: 2 806; `/paszarstwo/`: 6 633). Droga do kart się nie wydłużyła, bo tabela z linkami
   do czterech produktów stoi po 771 znakach opisu — ale to jest granica, przy której warto zadać
   pytanie o szablon (patrz §4).

---

## 3. Co jest otwarte — w kolejności ważności

### P1. Dwie pozycje treściowe po terminie (obie z 20.09)

- **T-085 „kategoria `/wapno-hydratyzowane/`"** — `wapno hydratyzowane` 2 400/mies. (III 3 600),
  kategoria zaindeksowana, ale stoi na **31,3**. Druga połowa zobowiązania z maila do Kasjana z 06.08.
  ⚠️ Inny odbiorca niż rolnik — budowlanka. Wzorzec: T-092, T-078, T-093; zaczyna się od baseline'u
  GSC dla adresu, bo to on ustawia oś treści (przy T-093 odkrył całą intencję szambową).
- **T-074 „spoke ziemniaki"** — `wapno pod ziemniaki` 50/mies., **szczyt IX–X 110**, czyli okno
  zamyka się w ciągu dwóch tygodni. Wchodzi od zmianowania i przedplonu; parch i dawka pogłówna
  są już w terminarzu `/jak-stosowac-wapno-nawozowe/` — linkować, nie powtarzać.

### P2. Terminy tego tygodnia

- **23.09 (wt)** — publikacja na wizytówce Google, teksty w `docs/gbp/2026-09-08-blok0-publikacje-i-opinie.md`.
  ⚠️ Post z 16.09 przepadł, publikacji nie da się datować wstecz — nie nadrabiać dwoma naraz.
- **26.09** — kontrola T-078 `/paszarstwo/` na frazach formowych, baseline
  `data/T-078/baseline-gsc-2026-09-08.json` (462 wyświetlenia, zero kliknięć).
- **30.09** — T-077 „poradnik o kredzie pastewnej" + przygotowanie czterech tematów GBP na październik.

### P3. Niezamknięte z poprzedniej sesji

- **„Gdzie znikają kliknięcia Ads"** — 453 kliknięcia wobec 74 sesji Paid Search w GA4. Do 15.10
  (koniec cyklu budżetowego) to jest największa niewiadoma projektu. Pomiar: licznik żądań z `gclid`
  po stronie serwera, ok. godziny roboty.
- **D1–D4** — baza wiedzy gotowa od 11.09. Dzisiejsza sesja dołożyła dwa wsady: kanibalizacja
  kategoria ↔ poradnik na czterech frazach osadowych oraz **H1 kategorii = nazwa WC**
  („Oczyszczalnie" to jedno generyczne słowo, title niesie całą frazę). Zmiana nazwy kategorii rusza
  H1, okruszki, etykietę w stopce i listing „Kategorie" — dlatego idzie w jednym przebiegu przez D1,
  nie ad hoc. ⚠️ Przed jakąkolwiek propozycją sprawdzić `rank_math_primary_product_cat` na 19 kartach,
  bo Premmerce bierze kategorię o najwyższym `term_id`, a primary to nadpisuje.
- **T-113 „jakość strony docelowej poniżej średniej"** — 72% wydatku Ads prowadzi na dwa landingi
  `noindex`, których T-136 nie dotknął. Pierwszy sygnał: kontrola Marki **02.10**.

---

## 4. Zauważone obok, nieruszone

1. **Zastosowania spoza kategorii z rozmowy z Kazimierzem** — kurniki, obory, kompostowniki,
   odkażanie gleby. Należą raczej do paszarstwa i rolnictwa niż do oczyszczalni. Przed jakąkolwiek
   treścią: wolumen fraz z planera, bo to może być temat wielkości `wapno do szamba` albo zero.
2. **Opis kategorii wypycha listing produktów w dół** — czy część treści wypiąć pod listing
   (`woocommerce_after_main_content`) albo rozbić na dwa pola. Dotyczy wszystkich kategorii naraz,
   więc osobne zadanie na szablonie, nie przy okazji treści.
3. **Etykieta w menu głównym** „Oczyszczalnie - Higienizacja osadów" ma zwykły myślnik zamiast
   półpauzy. Kosmetyka, jedna edycja. Anchor merytorycznie zostaje — niesie frazę `higienizacja osadów`
   na każdej stronie serwisu i jest lepszy niż sama nazwa kategorii.

---

## 5. Czego nie zakładać w następnej sesji

1. **Nie pisz, że poradnik higienizacyjny ma zero wyświetleń** — ma 157 i 2 kliknięcia.
2. **Nie licz, że karty i kategoria czekają na crawl** — pięć adresów pobranych 21.09.
3. **Nie zapisuj opisu termu przez `wp term update` ani `wp_update_term`** — kses zdejmuje tabele
   i nagłówki. Jedyna droga: `$wpdb->update` (skrypt przez `wp eval-file`) albo MCP `query_db_write`.
4. **Nie owijaj tabeli w `<div style="overflow-x:auto">`** — render zjada `style` z diva i zostawia
   go na tabeli. Czysty `<table>`, maksymalnie pięć kolumn ze względu na telefon.
5. **Nie obiecuj kliknięć po opisie kategorii.** Trzy kontrole tego typu (T-053, T-092) dały poprawę
   pozycji bez poprawy CTR. Wzorzec jest powtarzalny na widoczności, nie na CTR.
6. **Nie pisz na stronie o „środku dezynfekcyjnym grzybo- i bakteriobójczym"**, choć tak to nazwał
   Kazimierz — produkty biobójcze mają własny reżim rejestracyjny (BPR 528/2012), a wapno AGRII jest
   sprzedawane jako nawozowe i budowlane. Opisujemy mechanizm, nie deklarujemy właściwości produktu.
7. **SSH do agrii potrafi odbić timeoutem albo błędem DNS bazy** i zadziałać przy powtórce minutę
   później. Polecenie musi **zaczynać się** od `ssh agria-prod` lub `scp`, bez `cd &&` i bez pipe'a
   przed nim, inaczej nie łapie reguły z allowlisty.

---

## 6. Prompt do nowego wątku

```
Kontynuujemy AGRIĘ. Przeczytaj docs/sesje/2026-09-21-T093-i-zgloszenia-gsc.md (ta sesja)
i docs/REJESTR_ZOBOWIAZAN.md (sekcja KOLEJKA + Terminy najbliższe).

Stan: T-093 zamknięte 21.09, cztery karty v2 i kategoria mają crawl 21.09. Zaległe z 20.09
zostają dwie pozycje treściowe: T-085 „kategoria /wapno-hydratyzowane/" i T-074 „spoke ziemniaki".
W tym tygodniu twarde terminy: 23.09 publikacja na wizytówce, 26.09 kontrola T-078 /paszarstwo/,
30.09 T-077 poradnik o kredzie pastewnej plus cztery tematy GBP na październik.

Zacznij od T-085. Kolejność jak przy T-093: baseline GSC dla adresu (scripts/gsc_baseline.py,
--dni 28, do data/T-085/) → SERP-y, jeśli baseline czegoś nie rozstrzyga → treść do akceptu
z linkiem na auratest → po „ok" zapis przez $wpdb->update → weryfikacja renderem z cache-bustem
→ zgłoszenie w GSC → wiersz w rejestrze i dzienniku M4 w tym samym commicie.

Pokaż plan przed wykonaniem i czekaj na „działaj".
```
