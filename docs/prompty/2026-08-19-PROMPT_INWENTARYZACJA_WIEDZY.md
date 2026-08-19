# Prompt startowy — inwentaryzacja całego projektu AGRIA (19.08.2026)

> **Powód powstania:** 19.08 w wątku Ads dzień 5 model doradzał w sprawie cen i statusu
> dystrybutora Nordkalku, **nie mając pojęcia**, że jedno i drugie zostało ustalone
> i zapisane w tym repo dni wcześniej. Zapytał Janka o rzecz, którą Janek już mu podał.
>
> **To nie jest brak wiedzy w projekcie — to brak dostępu do niej na starcie sesji.**
> W `docs/` leżą **93 pliki .md**, w memory **30 wpisów**. Prompt startowy wątku Ads
> wskazywał pięć plików i model przeczytał dokładnie pięć. `CENNIK_PAWEL_2026-08-07.md`,
> `CEN_LISTA_URL_2026-08-13.md` i `docs/specs/2026-08-18-ofertownik-design.md` — czyli
> komplet wiedzy cenowej — nie zostały otwarte ani razu.
>
> Ten wątek ma to naprawić u źródła: zinwentaryzować, co projekt naprawdę wie, gdzie to
> leży, co jest nieaktualne, i **zbudować jeden punkt wejścia**, którego przeczytanie
> wystarcza, żeby nie doradzać na ślepo.

---

## Prompt do skopiowania

```
Wątek: inwentaryzacja projektu AGRIA — audyt stanu wiedzy, techniki, merytoryki
i harmonogramu. Sesja diagnostyczna, NIE wykonawcza: nic nie zmieniamy na produkcji,
nie ruszamy kampanii, nie piszemy treści.

Powód: 19.08 wyszło, że model prowadzący wątek Ads nie wiedział o cenach ustalonych
z Pawłem ani o relacji AGRIA–Nordkalk, mimo że jedno i drugie jest w repo. Ryzyko jest
konkretne: doradzamy klientowi wbrew ustaleniom, które sami zapisaliśmy, i pytamy go
o rzeczy, które już nam powiedział.

Punkt wyjścia: repo ma 93 pliki .md w docs/, 30 wpisów memory, 5 równoległych wątków
roboczych, 15 ADR-ów, 8 audytów, 9 raportów. Zakres pracy od maja do sierpnia 2026.


ZASADA NADRZĘDNA TEGO WĄTKU

Każde twierdzenie o stanie projektu z dowodem obok: ścieżka pliku i cytat, zapytanie
do bazy i wynik, URL i kod odpowiedzi, commit. Gdzie dowodu nie ma — pisz
„niezweryfikowane" i nie zgaduj. Ten wątek istnieje właśnie dlatego, że ktoś zgadywał.


1. ŹRÓDŁA WIEDZY — co gdzie leży i co z tego jest prawdą

Przejdź całe `docs/` (93 pliki) i całe memory (30 wpisów). Dla każdego dokumentu ustal:
- czego dotyczy jednym zdaniem,
- z kiedy pochodzi i czy opisuje stan aktualny, czy historyczny,
- czy jest źródłem prawdy, czy kopią/pochodną innego dokumentu,
- czy jest sprzeczny z którymkolwiek innym dokumentem albo z memory.

Wynik: `docs/INDEKS_WIEDZY.md` — tabela plik | dziedzina | data | status
(AKTUALNY / HISTORYCZNY / SPRZECZNY / DO USUNIĘCIA) | czego jest źródłem prawdy.

Szczególnie sprawdź te znane pola minowe:
- **Ceny.** `docs/operations/CENNIK_PAWEL_2026-08-07.md`,
  `docs/operations/CEN_LISTA_URL_2026-08-13.md`,
  `docs/operations/ZAPYTANIE_PAWEL_WIDELKI_CENOWE_2026-08-06.md`,
  `docs/seo/ANALIZA_CENY_NA_STRONIE_2026-08-06.md`, cennik startowy w
  `docs/specs/2026-08-18-ofertownik-design.md`, ceny w `docs/offers/OLX_TABELA_OGLOSZEN.md`
  i `docs/prompty/2026-08-PROMPT_CENY.md`, memory `project_agria_ceny_strategia`.
  **Siedem miejsc z cenami.** Który jest źródłem prawdy? Czy się zgadzają?
- **PROJECT_STATE.md** (24 KB) ma warstwy z maja, czerwca, lipca i sierpnia ułożone
  jedna na drugiej — sekcje „Co jest gotowe", „Co jest w toku", „Następne kroki"
  opisują stan sprzed trzech miesięcy, a świeży stan siedzi w nagłówku z 18.08.
  Rozstrzygnij, co z tym zrobić.
- **CATALOG_VS_WC_GAP.md** — memory ostrzega, że to mapa historyczna, a nie lista
  braków. Sprawdź, czy dokument sam to o sobie mówi wystarczająco wyraźnie.


2. MERYTORYKA — co wiemy o kliencie, a czego nie

Zbierz w jedno miejsce i zweryfikuj wobec dokumentów:

a) **Produkty.** 19 pozycji w WC. Dla każdej: producent surowca (Nordkalk / Trzuskawica /
   inny), parametry z karty, formy dostawy, cena od Pawła, czy ma kartę w katalogu
   drukowanym, czy jest w ogłoszeniach OLX, czy jest wykluczona z Ads i dlaczego.

b) **Relacja z producentami.** MASTER_PROMPT mówi: producent surowca to Nordkalk
   (Sitkówka) i Trzuskawica, AGRIA jest dostawcą. `CATALOG_VS_WC_GAP.md` przypisuje
   sześć kart do Nordkalku i zero do Trzuskawicy. **Czego NIE wiemy:** czy AGRIA jest
   autoryzowanym dystrybutorem Nordkalku. To rozstrzyga, czy wolno użyć nazwy „Nordkalk"
   w treści reklamy Google (licytować na cudzy znak wolno zawsze, użyć go w tekście —
   tylko odsprzedawcy). Sprawdź, czy odpowiedź jest gdzieś w repo albo w mailach
   (`~/bin/claude-mail-fetch.py`). Jeśli nie ma — trafia na listę pytań do Pawła,
   NIE zgadujemy.

c) **Ludzie i role.** Paweł, Kazimierz, Kasjan — kto za co odpowiada, kto co zatwierdza,
   który numer telefonu jest czyj i gdzie występuje. Sprawdź memory
   `feedback_agria_pawel_relacja_telefoniczna` i `feedback_agria_offer_mail_structure`.

d) **Ustalenia handlowe.** Kwota, okres, co obejmuje, co jest poza zakresem, czy jest
   rozjazd między tym, co potwierdził Kasjan, a tym, co poszło w mailu (memory
   `project_agria_ads_sezonowosc` sygnalizuje różnicę trzy vs cztery miesiące).


3. TECHNIKA — stan faktyczny, nie z dokumentacji

Sprawdzasz na żywo (SSH + WP-CLI, MCP, curl), nie przepisujesz z `INFRASTRUCTURE.md`:
- wersje WP / WC / PHP / motywu, lista wtyczek i która co robi,
- 19 produktów: status, SKU, ceny, atrybuty — pamiętaj o czterech warstwach parametrów
  (memory `project_agria_render_caching`) i weryfikuj RENDER, nie bazę,
- stary `post_type=produkt` (ID 67, 68, 69) opublikowany równolegle do `product`,
- demo-produkty motywu w indeksie (`/produkt/organic-pineapple/`) i 404-ki z ADR 14.08,
- duplikaty URL — Agrobielik 70 pod dwoma adresami, oba zbierają wyświetlenia w GSC,
- stan indeksacji wobec `INDEXATION_DIAGNOSIS_2026-06-15.md` i przypomnienia z 22.07,
- Core Web Vitals mobile (uwaga: PSI API ma dzienny limit — 19.08 był wyczerpany),
- geoblok, `.htaccess`, nagłówki bezpieczeństwa,
- analityka: GTM (wersja live 5), GA4, GSC, brak CMP i co z tego wynika,
- MCP: które toole żyją, czego brakuje (`catalog_product` zgubione).


4. KONKURENCI — co naprawdę o nich wiemy

W repo są: `docs/operations/OLX_KONKURENCJA_2026-08-07.md`,
`docs/prompty/2026-08-PROMPT_KONKURENCJA.md`, `scripts/seo_baseline.py`
(porównanie z polcalc.pl, biovita.com.pl, orcal.pl), snapshoty w `docs/seo/baselines/`.

Ustal: kogo uznajemy za konkurenta i dlaczego, jak stoimy wobec nich w organiku
(ostatni snapshot vs dziś), kto reklamuje się na naszych frazach, kto trzyma ceny
w internecie, a kto nie. Rozdziel wyraźnie **konkurentów** (Polcalc, Orcal, kopalnie)
od **producentów naszego surowca** (Nordkalk, Trzuskawica) i od **kanałów odsprzedaży**
(Allegro, Ceneo, OLX) — w wątku Ads to się zlało w jedno i doprowadziło do błędnej
rekomendacji.


5. TASKI I AUDYTY — co zrobione, co obiecane, co przepadło

a) Przejdź `git log` od pierwszego commita i zestaw z tym, co dokumenty deklarują
   jako zrobione. Szukaj rozjazdów w obie strony: zadeklarowane a niezrobione
   (`/wapno-granulowane/` miał „zero bajtów mimo zapisu, że opublikowany 06.08")
   i zrobione a nieudokumentowane.

b) Osiem audytów w `docs/audits/` (baseline M1, content, indeksacja, KR, KR
   priorytetyzacja, on-page plan, on-page backlog M2–M6, SEO audit results).
   Dla każdego: co zalecał, ile z tego wdrożono, co zostało otwarte.

c) `docs/operations/STRONA_BACKLOG_POPRAWKI.md`, `docs/seo/BACKLOG_SEZON_2026-07-14.md`,
   `docs/audits/ONPAGE_BACKLOG_M2-M6_2026-06-15.md` — trzy backlogi. Zderz je i powiedz,
   co z nich jest nadal żywe.

d) Raporty miesięczne M1 i M2 (`docs/raporty/`) — co obiecaliśmy klientowi na piśmie
   i czy to dowieźliśmy. `DOWODY_M2_2026-07.md` jest punktem odniesienia.

e) `docs/przypomnienia/` — trzy pliki, w tym `2026-09-01-menu-segmenty-m4.md`.
   Sprawdź kalendarz „Auranet Claude" i powiedz, co czeka.


6. CO SIĘ DZIEJE TERAZ I W NAJBLIŻSZYCH DNIACH

Pięć wątków wg `PROJECT_STATE.md` (Content/SEO M3, Ads, OLX, kalkulator Mg, ofertownik)
plus dwa otwarte 19.08: ceny i nagłówki cenowe na produktach
(`2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md`) oraz korekty kampanii Marka.

Dla każdego: gdzie stoi, na czym stoi (czeka na klienta / na nas / na dane), jaki jest
następny ruch i co go blokuje. Osobno wypisz, co ma termin — koniec sierpnia to koniec
M3, wrzesień to drugi impuls sezonu (wapnowanie pożniwne), rozliczenie budżetu Ads.


7. DELIVERABLE — punkt wejścia, nie kolejny dokument do zgubienia

To jest właściwy cel wątku. Na koniec mają powstać:

1. **`docs/INDEKS_WIEDZY.md`** — mapa źródeł prawdy (punkt 1).
2. **`docs/FAKTY_KLIENTA.md`** — jedno miejsce z faktami handlowymi i produktowymi:
   produkty, producenci, ceny, ludzie, ustalenia, relacje. Każdy fakt z datą i źródłem.
   To jest dokument, którego brak wywołał ten wątek.
3. **`docs/PYTANIA_DO_PAWLA.md`** — czego nie wiemy i musimy zapytać, bo to wiedza
   klienta, nie nasza. Status dystrybutora Nordkalku wchodzi tu jako pierwszy.
4. **Przepisany `docs/PROJECT_STATE.md`** — bez warstw archeologicznych, stan na dziś,
   historia do `docs/sesje/`.
5. **Poprawiony `CLAUDE.md`** — sekcja „Jak pracować w tym repo" ma dziś punkt
   „przeczytaj MASTER_PROMPT". Ma mieć obowiązkową listę wejściową, po której model
   nie zgaduje w sprawie cen i klienta.
6. **Lista rozjazdów i sprzeczności** znalezionych po drodze, z rekomendacją co z każdym.

Nie mnóż dokumentów ponad tę szóstkę. Jeśli coś da się dopisać do istniejącego pliku
zamiast tworzyć nowy — dopisz.


CZEGO W TYM WĄTKU NIE ROBIMY

Nie zmieniamy niczego na produkcji ani na koncie Ads. Nie piszemy treści. Nie wysyłamy
nic do klienta. Nie podejmujemy decyzji marketingowych — zbieramy podstawę, na której
będzie je można podjąć. Jedyne pliki, które powstają lub się zmieniają, to szóstka
z punktu 7.
```

---

## Dlaczego akurat teraz

Trzy rzeczy zbiegły się 18–19.08:

1. Ruszyły kampanie Ads z realnym budżetem — koszt złej rekomendacji przestał być teoretyczny.
2. Projekt urósł do pięciu równoległych wątków, a `PROJECT_STATE.md` przestał nadążać.
3. Wyszło na jaw, że model wchodzący w wątek po prompcie startowym czyta pięć plików
   z dziewięćdziesięciu trzech i nie ma jak się dowiedzieć, że pozostałe osiemdziesiąt
   osiem istnieje.

---

## Czego ten wątek NIE dotyka

- **Wykonania** czegokolwiek z tego, co znajdzie — poprawki idą do właściwych wątków.
- **Kampanii Ads** — `docs/sesje/2026-08-18-ads-dzien5-diagnoza.md`.
- **Cen i nagłówków na produktach** — `docs/prompty/2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md`.
- **OLX, kalkulatora Mg, ofertownika** — osobne wątki, `docs/PROJECT_STATE.md`.
