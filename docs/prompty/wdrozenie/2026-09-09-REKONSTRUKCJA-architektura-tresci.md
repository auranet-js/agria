# Rekonstrukcja: skąd się wzięła obecna architektura treści agria.pl

> **Projekt:** `agria` · **Typ:** wyjaśnienie, nie wdrożenie · **Zlecone:** Jan Schenk, 09.09.2026
> **Zakaz:** niczego nie zmieniasz na produkcji. To jest zadanie śledcze i pisemne.

---

## 0. Po co ten wątek

Janek przestał rozumieć, dlaczego strona wygląda tak, jak wygląda. Jego słowa, streszczone
bez łagodzenia:

> Na początku ustaliliśmy klasteryzację: robimy kategorie — wapno do rolnictwa, do budownictwa,
> do oczyszczalni i tak dalej. Każda kategoria ma listing produktów, filtry po lewej, treść nad
> listingiem i pod nim. Zbudowaliśmy landingi, które teoretycznie działają. **Potem nagle
> stwierdziłeś, że trzeba im coś dodać, że coś nie rankuje** — i dziś patrzę na makietę landingu
> „wapno granulowane" i nie wiem, co to za byt.
>
> **Co to w ogóle jest „wapno granulowane"?** Do czego jest? Jakie produkty się na nie składają?
> Nie mamy w ofercie „wapna granulowanego" — mamy wapno węglanowe granulowane, węglanowe
> z magnezem granulowane i kredę nawozową granulowaną. Trzy różne produkty z parametrami.
>
> **Mamy pełny katalog i każdy produkt ma swoją kartę.** Karty producentów leżą na `/do-pobrania/`
> — wystarczy je obejrzeć. Robiliśmy każdą kartę produktu pod SEO Twoim mechanizmem.
> A Ty budujesz obok landingi, z których nic nie wynika albo wynika coś słabego.
> `/wapno-do-stawu/` jeszcze rozumiem — to realna intencja. Ale reszta?
>
> Prawdopodobnie trzeba będzie zrobić wszystko od nowa, bo ja tego nie rozumiem. Przecież robimy
> SEO, a tu są bzdury totalne.

**Zadanie: odtworzyć historię punkt po punkcie, od założenia strony do dziś, i odpowiedzieć,
dlaczego dziś jest tak, jak jest.** Nie streszczenie stanu — **chronologia decyzji z datami
i źródłami**, plus jasne wskazanie, które z nich były uzgodnione z Jankiem, a które podjąłem sam.

---

## 1. Stan faktyczny na dziś — punkt wyjścia, zweryfikuj go, nie przepisuj

**Siedem kategorii produktowych** (`product_cat`, odczyt MCP 09.09):

| term | nazwa | slug | produktów |
|---|---|---|---|
| 764 | Wapno nawozowe | `wapno-nawozowe-rolnictwo` | **15** |
| 767 | Oczyszczalnie | `wapno-do-oczyszczalni` | 1 |
| 768 | Budownictwo | `wapno-hydratyzowane` | 1 |
| 770 | Paszarstwo | `paszarstwo` | 1 |
| 830 | Kreda malarska | `kreda-malarska` | 1 |
| 765 | Sadownictwo | `wapno-do-sadu` | **0** |
| 769 | Hurtownie | `wapno-nawozowe-hurt` | **0** |

**Dziewiętnaście kart produktów.** Wszystkie mają treść 5,3–7,4 tys. znaków, atrybuty `pa_*`,
producenta i (16 z 19) cenę w treści.

**Cztery landingi-strony, które NIE są kategoriami** — osobne wpisy `page`, treść w `post_content`:
`/wapno-nawozowe/` (2757), `/wapno-granulowane/` (2751), `/wapno-do-stawu/` (2796),
`/wapno-do-stabilizacji-gruntow/` (2745). Trzy pierwsze mają `noindex`.

**Pytanie osiowe:** po co istnieje warstwa landingów obok warstwy kategorii, skoro kategoria
`wapno-nawozowe-rolnictwo` ma listing 15 produktów, filtry i opis rozbudowany w T-092?

---

## 2. Pytania, na które ma odpowiedzieć ten wątek

Każda odpowiedź **z datą, źródłem i cytatem** — ADR, commit, wiersz rejestru, plik w `docs/`.
Gdzie źródła nie ma, napisz wprost „brak zapisu, decyzja niearchiwizowana".

1. **Jaka była pierwotna klasteryzacja** przy budowie strony? Kto ją ustalił, kiedy, gdzie zapisana?
   Ile kategorii miało być i jaka była logika podziału — po zastosowaniu, po produkcie, po odbiorcy?
2. **Skąd wzięły się dwie puste kategorie** (Sadownictwo, Hurtownie) i dlaczego są puste?
3. **Kiedy i dlaczego powstała warstwa landingów?** Który dokument to uzasadnia? Czy to była
   decyzja Janka, czy moja? Jeśli moja — na jakiej przesłance?
4. **Czym miało być `/wapno-granulowane/`** — kategorią, przekrojem przez produkty, celem Ads?
   Jakie trzy produkty pod nie podpięto i z których kategorii pochodzą?
5. **Dlaczego landingi mają `noindex`** i kiedy to ustawiono? Jeśli są poza indeksem, to czemu
   mają rozbudowaną treść SEO?
6. **Czy karty produktów były robione pod SEO** i jakim mechanizmem? Czy wykorzystano karty
   producentów z `/do-pobrania/` (17 PDF-ów)? Gdzie to udokumentowane?
7. **Co mówi ADR `2026-08-11`** o kanibalizacji i architekturze kanałów, a co ADR `2026-08-21`
   o hubie i spokach? Czy landingi są z nimi zgodne, czy im przeczą?
8. **Które decyzje architektoniczne podjąłem sam, bez akceptu Janka?** Wypisz je osobną listą.
   To jest najważniejsza część odpowiedzi.
9. **Co z tego wszystkiego realnie pracuje** — dane GSC per adres, 28 dni: kategorie kontra
   landingi kontra karty. Który poziom przynosi wyświetlenia i kliknięcia?
10. **Czy sensowniejsza jest architektura bez warstwy landingów** — kategoria z opisem plus karty
    produktów — i co kosztowałoby przejście na nią?

---

## 3. Gdzie szukać — nie zgaduj, otwórz

**ADR-y** (`docs/decyzje/`), w kolejności istotności dla tematu:
`2026-08-11-podzial-rol-ads-seo.md` · `2026-08-21-architektura-pole-hub-i-spoke.md` ·
`2026-08-21-nazwy-kategorii-bez-segmentow.md` · `2026-08-24-audyt-seo-od-nowa-rozstrzygniecia.md` ·
`2026-07-08-rdzen-url-taksonomia.md` · `2026-06-15-decyzje-katalogowe.md` ·
`2026-08-19-dwie-warstwy-cen.md` · `2026-08-21-terminarz-jako-hub-osi-kiedy.md`

**Strategia i rozpiski** (`docs/seo/`):
`ROZSTRZYGNIECIE_ARCHITEKTURY_2026-08-11.md` · `SEO_STRATEGIA_POD_WYNIK_2026-07-08.md` ·
`ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md` · `T-052-AUDYT_FRAZ_I_PLAN_SEZON_2026-08-21.md` ·
`LP_WAPNO_GRANULOWANE_2026-08-06.md` · `LP_WAPNO_NAWOZOWE_2026-08-06.md` ·
`LP_STABILIZACJA_GRUNTU_2026-06-15.md` · `KEYWORDS_BASELINE.md` · `lp/` · `baselines/`

**Katalog i produkty:** `docs/catalog/` · `docs/FAKTY_KLIENTA.md` §3 ·
`docs/operations/CENNIK_PAWEL_2026-08-07.md` · karty producentów na `https://agria.pl/do-pobrania/`

**Rejestr:** `docs/REJESTR_ZOBOWIAZAN.md` — sekcja „Unieważnione" mówi, czego już nie proponować;
dziennik M1–M4 mówi, co i kiedy dowieziono.

**Historia:** `git log --reverse --format="%ad %h %s" --date=short` — pierwszy commit **26.02.2026**.
Użyj `git log --follow` na plikach landingów i na module `plain-content-layout`.

**Memory projektu:** `~/.claude/projects/-home-host476470-projekty-agria/memory/` — zwłaszcza
`project_agria_architektura_kanalow`, `project_agria_catalog_decisions`,
`feedback_agria_landingi_wzorzec_nie_elementor`.

**AUDYTY — wszystkie, w kolejności powstania. To jest kręgosłup chronologii:**
`KEYWORD_RESEARCH_2026-05-19.md` (pierwszy KR, później **zastąpiony** przez T-052 — sprawdź czym
i dlaczego) · `ONPAGE_PLAN_2026-05-20.md` · `BASELINE_M1_2026-06.md` ·
`CONTENT_AUDIT_2026-06-15.md` · `INDEXATION_DIAGNOSIS_2026-06-15.md` ·
`KR_PRIORYTETYZACJA_2026-06-15.md` · `ONPAGE_BACKLOG_M2-M6_2026-06-15.md` ·
`SEO_AUDIT_RESULTS.md` · `T-026-diagnoza-indeksacji-2026-08-19.md` ·
`2026-08-24-AUDYT_SEO_OD_NOWA.md` · `2026-09-07-CRAWL_SCREAMING_FROG.md` ·
`2026-09-08-WERYFIKACJA-CRAWL.md`

**Przy każdym audycie odpowiedz na trzy rzeczy:** co stwierdził, co z niego wykonano,
i **czy jego wnioski zostały później obalone** — bo część została (teza o długości tytułu,
liczba kart poza indeksem, „0/38 zaindeksowanych", zawyżone liczby znaków w audycie 24.08).
Audyt, którego wnioski upadły, a na którym oparto decyzje, jest osobno wart odnotowania.

**Raporty miesięczne do klienta** (`docs/raporty/`): `2026-06.md`, `2026-07.md`, `2026-08.md`,
`PODSUMOWANIE_M3_2026-08.md`, `DOWODY_M2_2026-07.md` plus wersje mailowe. **Porównaj, co
raportowaliśmy klientowi, z tym, co realnie stało na stronie** — rozjazd między jednym a drugim
jest częścią odpowiedzi.

**Strategia** (`docs/strategy/`): `STRATEGIA_AGRIA_6MIES_2026.md`, `STRATEGY_2025_2026.md`,
`BUDGET_KPI.md` — czy obecna architektura realizuje to, co tam zapisano.

**Sesje** (`docs/sesje/`): `2026-08-19-stan-przed-przebudowa-rejestru.md`,
`2026-08-21-lista-zmian-i-linkow.md`, `2026-08-21-podsumowanie.md` — tam jest zapisane moje
rozumowanie z dni, w których powstawały landingi.

**Postęp:** `docs/postep/` (`build_postep.py`, `dane/`) — szereg czasowy, jeśli ciągnięty.

---

## 3b. Klasteryzacja i powstawanie treści — osobna oś rekonstrukcji

To jest część, o którą Janek dopytał wprost. Odtwórz **dla każdego tekstu na stronie**:

| co ustalić | gdzie szukać |
|---|---|
| **jak wyglądała pierwotna klasteryzacja fraz** i ile razy się zmieniała | `KEYWORD_RESEARCH_2026-05-19` → `KR_PRIORYTETYZACJA_2026-06-15` → `ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14` → `T-052-AUDYT_FRAZ_2026-08-21` |
| **kiedy klaster przestał być listą fraz, a stał się listą adresów** | `ROZSTRZYGNIECIE_ARCHITEKTURY_2026-08-11`, ADR `2026-08-21-architektura-pole-hub-i-spoke` |
| **każdy tekst: data, na jakiej podstawie, jaki wynik** | dziennik w rejestrze + `data/T-NNN/` (baseline i wdrożenia) |
| **czy treść pisano pod frazę z pomiarem, czy pod rozpiskę** | porównaj rozpiski z `data/T-092/`, `data/T-078/` |
| **karty produktów — czy i jakim mechanizmem robione pod SEO** | `docs/catalog/`, dziennik M1–M2 „blok SEO on-page", commity `[content]` |

**Osobno wypisz teksty, które powstały i nie przyniosły nic** — z liczbami z GSC.
T-053 (meta huba) jest przykładem zmierzonym i zamkniętym; sprawdź, czy są inne.

**Pomiar świeży, do wykorzystania bez powtarzania:**
`data/seo/2026-09-09-serp-i-indeksacja-przed-T116.md` — SERP-y, stan indeksu 19 kart, GSC 28 dni.

---

## 4. Czego w tej odpowiedzi NIE robisz

- **Nie usprawiedliwiasz.** Jeśli decyzja była moja i nie ma dla niej uzasadnienia w danych —
  piszesz to wprost, bez tłumaczenia kontekstem.
- **Nie upiększasz chronologii.** Jeśli coś powstało „bo tak wyszło" — tak to nazywasz.
- **Nie proponujesz przebudowy w tym wątku.** Najpierw wyjaśnienie, decyzja co dalej należy do Janka.
- **Nie ruszasz produkcji.** Zero zapisów, zero MCP write, zero Elementora.
- **Nie powołujesz się na pamięć.** Każde twierdzenie ma źródło albo etykietę „brak zapisu".

---

## 5. Zrobione =

Dokument `docs/audits/2026-09-XX-REKONSTRUKCJA-ARCHITEKTURY.md` zawierający:

1. **Chronologię** od 26.02.2026 do dziś — data, decyzja, źródło, kto zdecydował.
2. **Mapę warstw**: kategorie → landingi → karty produktów, z odpowiedzią, co się z czym dubluje.
2b. **Oś klasteryzacji** — jak lista fraz zmieniała się w czasie i w którym momencie zaczęła
    generować adresy; które frazy dostały własny URL i na jakiej podstawie.
2c. **Oś treści** — każdy tekst opublikowany na stronie: data, źródło merytoryczne, fraza docelowa,
    wynik w GSC. Osobno: teksty bez efektu.
2d. **Oś audytów** — co stwierdzał każdy z dwunastu audytów, co z niego wykonano i **które jego
    wnioski zostały później obalone pomiarem**.
3. **Listę decyzji podjętych beze mnie** — osobno, bez wtapiania w narrację.
4. **Tabelę wyników GSC** per warstwa: kategorie, landingi, karty — wyświetlenia, kliknięcia, pozycja.
5. **Odpowiedź na dziesięć pytań z §2**, każda z dowodem.
6. **Jedno zdanie na końcu**: czy obecna architektura ma uzasadnienie w danych, czy nie.

Dokument wystawiony na `https://auratest.pl/fe4f58fec53ctmp/` i pokazany Jankowi linkiem.
Treść **inline w czacie** też — Janek ma to przeczytać w jednym widoku, nie klikać.
