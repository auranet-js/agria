# T-085 „kategoria /wapno-hydratyzowane/" — przebieg i rozstrzygnięcie, 21.09.2026

> **Zadanie z rejestru:** rozbudowa opisu kategorii pod frazę `wapno hydratyzowane` (2 400/mies., III 3 600),
> bo adres stoi na poz. 31,3. Druga połowa zobowiązania z maila do Kasjana z 06.08.
> **Wynik:** zadanie **przedefiniowane w trakcie** na podstawie trzech pomiarów. Wdrożony opis segmentowy
> 2 407 B zamiast planowanych ~6 kB. Powód poniżej.

## 1. Co zmierzone, zanim cokolwiek napisano

### 1.1 Baseline GSC, 28 dni (21.08–17.09) — `baseline-gsc-2026-09-21.json`

| Adres | Klik | Wyśw | CTR | Poz |
|---|---|---|---|---|
| `/wapno-hydratyzowane/` (kategoria, term 768) | 2 | 122 | 1,64% | **30,0** |
| `/wapno-hydratyzowane/bielik/` (karta #309) | **10** | **584** | 1,71% | **7,3** |
| `/wapno-do-oczyszczalni/` (kontrola po T-093) | 12 | 458 | 2,62% | 9,1 |

Na samej frazie `wapno hydratyzowane` kategoria ma **38 wyświetleń i pozycję 39,6**. Karta nad progiem
na tej frazie nie wychodzi, ale na `wapno hydratyzowane bielik` stoi na **8,9**, a na `cl 90-s` na **9,3**
i na `cl 90` na **1,0**.

⚠️ Sumy zapytań nie zgadzają się z agregatem (karta: ok. 150 widocznych wobec 584) — **74% ukryte progiem
prywatności**. Liczby czytane z poziomu strony, nie z sumy zapytań (`feedback_gsc_ctr_z_poziomu_strony`).

**Intencja zapytań jest cenowa i opakowaniowa, nie budowlana:** `wapno bielik cena` (31 wyśw., poz. 5,1 —
jedyne kliknięcie karty), `wapno bielik 30 kg cena` (31), `wapno bielik 25 kg` (5), `wapno bielik 25 kg cena` (3).
Budowlanka nad progiem jest śladowa: `wapno do zaprawy` 2, `wapno tynkarskie` 1, `wapno budowlane bielik` 4.

### 1.2 SERP-y, mobile PL, `location_code 2616` — `serp-2026-09-21.json`

| Fraza | TOP10 | AGRIA |
|---|---|---|
| `wapno hydratyzowane` | Castorama, Leroy Merlin, Allegro, Ramex, Handlobud, Lhoist + poradniki | poza TOP20 |
| `wapno hydratyzowane cena` | blok produktowy na abs 1, Leroy, Ramex, Lubar, Ceneo, Allegro | poza TOP20 |
| `wapno budowlane` | AI Overview, Allegro, Castorama, PSB Mrówka, OBI, Bricoman | poza TOP20 |

„Ludzie pytają też" pod pierwszą frazą: *Czy nadaje się do ogrodu? Czy nadaje się do malowania?
Jak rozrabiać? Ile wapna na 10 litrów wody?* — **SERP detaliczny, worek 20–30 kg w markecie.**
Przy okazji wyjaśnione `wapno bielik 30 kg cena` z GSC: rynkowy worek to 20–30 kg, nasz 25.

### 1.3 Planer Ads — czy jest fraza zadaniowa „wapno do…" warta wzięcia — `planer-2026-09-21.json`

| Fraza | /mies. | Szczyt | Werdykt po SERP-ie (`serp-bielenie-2026-09-21.json`) |
|---|---|---|---|
| wapno do bielenia drzew | **1 900** | **III 9 900** | Castorama, Leroy, OBI, Bricomarché, Agrecol — **wiaderka 1–2 kg**, nie nasz towar |
| wapno do bielenia ścian | 320 | IX 480 | mieszany: obok marketów **fermo.pl „wapno super białe 7 kg"**, hodowlany.pl „malowanie kurnika i budynków inwentarskich", expondo „bielenie obory" — **jedyny realny trop** |
| wapno do bielenia | 210 | III 480 | jw. |
| wapno do kurnika | 170 | III 260 | jw. |
| wapno do kompostownika | 140 | IX 210 | — |
| mleko wapienne | 590 (konkurencja **LOW**) | IX 720 | Wikipedia, Lhoist, chemia laboratoryjna (roztwór 10%), drogownictwo — definicyjna, nie zakupowa |
| **wapno do uzdatniania wody** | **<10** | — | odpada mimo obecności w karcie producenta |
| wapno do obory | 20 | — | odpada |

## 2. Rozstrzygnięcie i jego powód

**Frazy ogólnej nie gonimy.** Masowy popyt na wapno hydratyzowane jest detaliczny — worek albo wiaderko
w markecie. Nasz popyt (składy, hurtownie, oczyszczalnie, firmy przerabiające osady) **nie siedzi
w wyszukiwarce, tylko w relacjach handlowych**, co potwierdza odpowiedź Kazimierza z 21.09.
Rozbudowa opisu do 6 kB powtórzyłaby T-092: lepsza widoczność, zero kliknięć, bo kliknięcia są na frazie,
której nie obsługujemy.

**Kanibalizacja jest naszego autorstwa** — `git log -S`: title karty „Wapno Bielik – wapno hydratyzowane,
luz i worek 25 kg" wstawiony **14.09 w T-136** (`e1596fa`), title i focus keyword kategorii
„Wapno hydratyzowane do budownictwa" / `wapno hydratyzowane` — w sierpniowym audycie (`8f2bfb3`).
Dwie nasze strony na jednej frazie, wygrywa karta.

**Slug `wapno-hydratyzowane` musi zostać** — Premmerce buduje adres produktu ze slugu kategorii,
więc zmiana slugu przeniosłaby kartę stojącą na 7,3. Nazwa kategorii, H1, title i meta **nietknięte**;
propozycja zmiany nazwy idzie do D1, bo rusza H1, okruszki i menu.

## 3. Odpowiedź Kazimierza (21.09) — podstawa treści

- **Kupują: składy, hurtownie, oczyszczalnie ścieków, firmy przerabiające osady.**
  Wykonawcy indywidualnemu na budowę **z zasady się nie dostarcza** — chcą długich terminów płatności,
  ryzyko wypłacalności zbyt duże; stali kontrahenci są pewni od lat. **To decyzja handlowa, nie luka.**
- **Certyfikaty idą z fakturą przy każdej dostawie.**
- **Uzdatnianie wody: dzieje się** (Bielik i „super białe" z Lhoista), ale **na jakiej podstawie odbiorcy
  to stosują — nie wie.** Dlatego na stronie idzie wyłącznie za kartą producenta, bez relacji.

Rozstrzygnięcia Janka z tej samej rozmowy: klasa i zastosowania **z karty charakterystyki producenta**;
**big-bag jest, skoro jest luz**; **minimum zamówienia nie ma** — „najpierw kontakt".

## 4. Co wdrożone

**Opis termu 768: 468 B → 2 407 B**, 1 → **3 × H2**, 2 → **5 linków**, dodana tabela dwuwierszowa
z linkami do karty Bielika i do wapna palonego mielonego. Render strony **4 395 → 5 967 znaków**.

Zmiany merytoryczne wobec stanu sprzed:
1. **Usunięte „luzem na plac budowy"** — obecny opis obiecywał dostawę wykonawcy, czyli to, czego nie robimy.
2. **Wprowadzona klasa CL 90-S** cytatem z karty charakterystyki (Nordkalk Wapno Sp. z o.o., wyd. 1.1
   z 26.03.2025) wraz z listą zidentyfikowanych zastosowań. To jedyna fraza klastra, na której karta
   stoi na poz. 1,0 — realnie nasza.
3. **Big-bag dopisany** obok luzu 14–16 t i worka 25 kg.
4. **Dokumenty jakościowe z fakturą przy każdej dostawie** — argument nieobecny dotąd nigdzie na stronie.
5. **Ceny za tonę** (945 luz / 1 220 worki 25 kg), **bez minimum zamówienia**.
6. **Dwa wyjścia poza kategorię** — karta Bielika i `/wapno-do-oczyszczalni/` — żeby strona z jednym
   produktem nie była ślepym zaułkiem.

**Czego świadomie nie ma:** dezynfekcji i właściwości biobójczych (reżim BPR 528/2012, produkt sprzedawany
jako nawozowy i budowlany), proporcji zaprawy (brak w kartach — nie wyprowadzamy z rozumowania),
uzdatniania wody jako osi treści (wolumen <10).

## 5. Dowód

| Co | Gdzie |
|---|---|
| Backup tabeli przed zmianą | `agria-prod:~/agria-backups/T-085/przed-T085-term-taxonomy-20260921-171304.sql` (40 951 B) |
| Opis 1:1, stan przed / po | `data/T-085/opis-768-przed.html` · `data/T-085/opis-768-v3-przyciety.html` |
| Wersja pełna 5 788 B (odrzucona) | `data/T-085/opis-768-v2.html` |
| Zapis | `$wpdb->update` przez `wp eval-file` po SSH — **MD5 w bazie zgodny co do znaku z plikiem** (`f8febe31cdbf1523d1fcdc327a24e9c5`, 2 407 B). `wp term update` i `wp_update_term` odpadają: kses zdejmuje tabele i nagłówki |
| Weryfikacja renderu | curl z cache-bustem: 5 967 znaków, `CL 90-S` obecne, `big-bag` obecne, `plac budowy` **nieobecne**, 5 linków wychodzi |
| Mockup przed/po do akceptu | `data/T-085/mockup-przed-po.html` → `https://auratest.pl/fe4f58fec53ctmp/agria-wapno-hydratyzowane-przed-po-2026-09-21.html` |
| Zgłoszenie w GSC | 21.09, panel, „**Przesłano prośbę o zindeksowanie**"; stan przed zgłoszeniem: „Adres URL znajduje się w Google", strona w indeksie |

## 6. Co zostaje otwarte

1. **Poradnik o bieleniu budynków inwentarskich** — ściany 320 + kurnik 170 + obora 20 ≈ **510/mies.,
   szczyt IX i III**, SERP niezabrany przez markety, odbiorcą jest rolnik, czyli publiczność reszty serwisu.
   Materiał na klaster rolniczy, **nie na kategorię produktową** — kończy się zakupem worka w składzie.
   Do założenia jako osobna pozycja.
2. **Nazwa kategorii „Budownictwo"** wobec faktu, że wykonawcom nie sprzedajemy — do D1, razem
   z `rank_math_primary_product_cat` na 19 kartach.
3. **„Wapno super białe" z Lhoista** — wymienione przez Kazimierza i obecne w SERP-ie konkurencji
   (fermo.pl, abs 4), nie ma go wśród naszych 19 kart. Nie wiem, czy AGRIA je sprzedaje.
4. **Trzy pytania bez odpowiedzi**: deklaracja właściwości użytkowych z CE dla CL 90-S; próg, od którego
   obowiązuje cena workowa; sześć pytań technicznych do Kazimierza z 08.09 plus T-108 (dolomit) — nadal wiszą.
