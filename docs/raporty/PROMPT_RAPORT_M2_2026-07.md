# Prompt: raport miesięczny AGRIA (lipiec 2026 / M2) — do Kasjana i Pawła

> **Jak używać:** wklej całość jako pierwszą wiadomość w nowym wątku `cd ~/projekty/agria && claude`.
> Wzorzec metodyczny: raport ASEO za lipiec 2026 (`~/projekty/aseosystem/seo-queue/raporty/2026-07.md`
> + mail `2026-07-mail-short.md`) — ta sama analiza, ten sam styl, **inny kontekst klienta i inne pułapki**.
> Kasjan jest właścicielem obu firm (ASEO Recykling System i AGRIA), więc raporty czyta ta sama osoba —
> spójność stylu jest celowa. **Nie kopiuj treści ASEO** — kopiuj metodę.

---

## 0. Zanim cokolwiek napiszesz — wczytaj stan faktyczny

Nie pisz raportu z pamięci ani z planów. Kolejno:

1. **Memory projektu:** `~/.claude/projects/-home-host476470-projekty-agria/memory/MEMORY.md` i wskazane w nim wpisy.
   Obowiązkowo: `feedback_agria_no_self_criticism_built_site`, `feedback_agria_offer_mail_structure`,
   `feedback_agria_pawel_relacja_telefoniczna`, `project_agria_offer_status`, `project_agria_gbp`,
   `project_agria_render_caching`, `project_agria_nav_debt_m4`.
2. **Repo:** `docs/raporty/REALIZACJA_M2_2026-07.md`, `docs/raporty/DOWODY_M2_2026-07.md`,
   `docs/raporty/2026-06.md` + `2026-06-mail.md` (co obiecaliśmy miesiąc temu i jakim językiem),
   `docs/PROJECT_STATE.md`, `docs/przypomnienia/`.
3. **Commity:** `git log --since=2026-06-25 --until=2026-08-04 --pretty=format:'%ad %h %s' --date=short`
   — to jest twarda lista tego, co realnie zrobione w lipcu. Raport ma się z nią zgadzać.
4. **Ustalenia mailowe:** `python3 ~/bin/claude-mail-fetch.py list | grep -i agria` → `fetch <id>`.
   Sprawdź, co ostatnio poszło do klienta i w jakim tonie (akcept oferty przez Pawła, ustalenia zakresu M2/M3).

**Zasada nadrzędna:** „co zrobione" wyprowadzasz z commitów i weryfikacji live, nie z planu. Jeśli plan mówi
„zrobione", a live/GSC mówi inaczej — w raporcie ląduje wersja z live.

---

## 1. Dane z API (świeży pull, nie liczby z notatek)

### GSC — miesiące kalendarzowe, jeden pull
Property AGRII to **URL-prefix `https://agria.pl/`, NIE `sc-domain:`** (memory `project_agria_analytics_stack`).
Skrypt do adaptacji: `~/projekty/aseosystem/seo-queue/gsc_pull.py` (OAuth z `~/secrets/google/tokens.json`,
refresh tokenem, scope webmasters) — skopiuj do `~/projekty/agria/scripts/` i zmień `SITE` + listę fraz.

Pobierz **maj / czerwiec / lipiec jako pełne miesiące kalendarzowe w jednym przebiegu** — GSC dojrzewa dane
~30 dni, więc liczby czerwca z raportu czerwcowego będą dziś inne. Porównywalność wymaga jednego pulla.
Metryki: kliknięcia, wyświetlenia, CTR, pozycja średnia, **liczba fraz z widocznością, frazy w TOP3, w TOP10**
(liczone z `dimensions:["query"]`, `rowLimit: 25000`), rozbicie na kraje, TOP strony, TOP zapytania,
wszystkie zapytania z klikami.

Dla fraz kluczowych AGRII (wapno nawozowe, wapno rolnicze, kreda, wapno do stabilizacji gruntów, nazwy
produktów — **weź je z `docs/seo/`, nie zgaduj**) zrób `query × page` — to wykrywa kanibalizację.

### Indeksacja
Historia projektu to zaległy re-crawl po kwietniowym noindex (`project_agria_indexation_diagnosis`).
Sprawdź URL Inspection API dla kluczowych URL (LP stabilizacja gruntów, 4 poradniki, kategorie, produkty):
ile faktycznie w indeksie, kiedy ostatni crawl. **To jest główny dowód postępu M1/M2** — ważniejszy niż pozycje.

### GA4
Property `538301430` (`G-KVFMR3NZDH`), GTM `GTM-TDC85TQN`. Ruch organiczny lipiec vs czerwiec, key events.
Uwaga: lokalny Chrome ma bloker maskujący GTM — weryfikuj przez API, nie przez przeglądarkę.

### Google Ads
**Sprawdź, czy w ogóle są.** Strategia AGRII to „zerowy budżet link buildingu, przygotowanie pod future PPC"
(`project_seo_strategy_constraints`) — jeśli kampanii nie ma, **nie rób sekcji Ads i nie sugeruj jej klientowi
bez decyzji Janka**. Jeśli są: `~/projekty/aseosystem/scripts/google/ads_call.sh` jako wzorzec (podmień CID),
metryki: imp, kliki, koszt, IS, Abs Top IS, rank lost, budget lost, konwersje.

### Wydajność
PageSpeed Insights v5 (klucz `~/secrets/google/psi-crux-key.txt`) mobile dla strony głównej + jednej kategorii
+ jednej karty produktu: performance/a11y/BP/SEO, LCP, CLS, TBT + CrUX field data (może nie być — mały ruch).

### SERP live (opcjonalnie, ale mocne)
DataForSEO (`~/secrets/dataforseo/basic-auth-b64.txt`, saldo ~$35 — sprawdź przed serią,
endpoint `/v3/serp/google/organic/live/regular`, `location_code: 2616`, `language_code: "pl"`).
Pokazuje realny SERP, nie średnią GSC. **Sprawdź przy okazji, czy w wynikach nie stoi inna domena klienta** —
w ASEO okazało się, że druga strona tego samego właściciela zajmuje miejsce, o które walczyliśmy.
Kasjan ma więcej niż jedną firmę — zweryfikuj, zanim uznasz konkurenta za obcego.

---

## 2. Weryfikacja live (nie ufaj bazie)

- MCP AGRIA (token-gated, `mcp-ext` v1.2) — `query_db`, `read_file`, `update_post_content`, `db_export`.
  Preferuj MCP nad curl (`feedback_agria_prefer_mcp_curl_allowlisted`).
- **Parametry produktu żyją w 4 warstwach** (atrybuty `pa_*`, tabela w `post_content`, tabela w Elementorze,
  meta SEO) — weryfikuj **wyrenderowaną stronę**, nie bazę (`project_agria_render_caching`).
- CDN nazwa.pl cache'uje — cache-bust przy sprawdzaniu. Sitemapa RankMath siedzi w plikach
  `uploads/rank-math/*.xml`.
- Smoke test: strona główna, kategorie, LP stabilizacja gruntów, 4 poradniki, `/do-pobrania/`, sitemap, robots
  — status HTTP i czas odpowiedzi.

---

## 3. Raport pełny → `docs/raporty/2026-07.md`

Wzorzec struktury (z ASEO — dopasuj sekcje do tego, co w AGRII ma sens):

1. **Nagłówek metodyczny** — miara sukcesu, źródła danych z datą pulla, pliki powiązane.
2. **Co zrobione w lipcu** — z commitów, pogrupowane; osobno „w ramach M2", osobno „ponad zakres".
3. **Widoczność organiczna** — tabela maj/czerwiec/lipiec + interpretacja. Jeśli rosną wyświetlenia,
   a nie rosną kliki — powiedz to wprost i wyjaśnij dlaczego (nowe treści wchodzą na 2-3 stronę wyników).
4. **Indeksacja** — ile URL w indeksie, dynamika, dowód z URL Inspection.
5. **Pozycje fraz** — tabela baseline → teraz, z oceną. Regresy pokazuj razem z przyczyną i naprawą.
6. **Audyt techniczny** — tabela obszar / stan / uwagi (wydajność, sitemapa, schema, hreflang jeśli dotyczy,
   kanibalizacja, dług nawigacyjny).
7. **Ocena realizacji celów miesiąca** — tabela cel → wynik → zrealizowany/nie. **Nie chowaj niedowiezionych.**
8. **Plan na kolejny miesiąc** — priorytety z uzasadnieniem z danych, nie z życzeń.
9. **Koszty** — patrz niżej.

Raport pełny jest **wewnętrzny** (nasza historia + audyt). Może zawierać rzeczy, których klient nie zobaczy.

---

## 4. Mail do klienta → `docs/raporty/2026-07-mail.md`

**Odbiorcy: Kasjan (właściciel) i Paweł Bigos (operacyjnie).** Kasjan czyta też raporty ASEO — ten sam styl.

Reguły twarde (memory AGRIA — złamanie którejkolwiek = mail do wyrzucenia):

- **NIE krytykujemy stanu strony.** Auranet zbudował agria.pl, więc „brak / błąd / wolno / martwe linki" to
  krytyka własnej roboty. Framing rozwojowy: „uruchamiamy / wzmacniamy / optymalizujemy / dokładamy".
  Audyt techniczny zostaje w raporcie wewnętrznym, do klienta idzie „obszary rozwoju".
- **Prosto, dla zarządu.** Bez żargonu SEO, bez tabel KPI, bez frameworków klasyfikacji (A/B/C/D — Janek to
  raz odrzucił). Technikalia w załączniku, i to **PDF, nie `.md`**.
- **Budżet TYLKO miesięcznie** — 2 000 zł netto/mies. **NIGDY suma roczna ani wielomiesięczna.**
  Nie zmyślaj żadnych innych stawek bez akceptu Janka.
- Forma **„ty/Wy"**, bez dopytywania o formę. Bez stopki — dokleja ją Outlook Janka.
- **Przemilcz multi-location GBP** (oddziały Niedomice/Radgoszcz — brak dostępu, `project_agria_gbp`).
- Długość ~30-40 linii: wprowadzenie (1-2 zdania) → zrobione (5-7 punktów hi-level) → wyniki (kilka liczb,
  po ludzku) → plan na kolejny miesiąc → koszty. Bez PDF-a z raportem, jeśli klient go nie oczekuje.
- Uczciwość: jeśli coś nie wyszło, jedno zdanie z przyczyną i tym, co z tym zrobiliśmy. Lepiej niż przemilczenie.

**Wzorzec językowy** — zerknij, jak brzmi mail ASEO za lipiec
(`~/projekty/aseosystem/seo-queue/raporty/2026-07-mail-short.md`) i mail AGRII za czerwiec
(`docs/raporty/2026-06-mail.md`). Ten sam rejestr: konkret, korzyść, zero ozdobników.

---

## 5. Akcept i wysyłka

1. **Pokaż Jankowi pełną treść maila INLINE w czacie** (nie sam link — chce czytać w jednym widoku).
2. Pliki wystaw na `https://auratest.pl/fe4f58fec53ctmp/agria-raport-lipiec-YYYY-MM-DD.md`
   i podaj klikalne linki **w czacie**.
3. Zapytaj Janka o rzeczy, które są jego decyzją, **zanim** napiszesz mail — nie po. Typowo: czy dana pozycja
   jest w cenie M2 czy poza, jak ująć niedowieziony punkt, czy zapowiadać coś, co nie jest jeszcze uzgodnione
   z klientem.
4. Wysyłka **wyłącznie** `~/bin/send-to-jan -s "[draft do AGRII] <temat>" -B <czysta-treść.md>`.
   **Bez załączników** (`feedback_aseo_mail_do_janka_bez_zalacznikow`) — Janek forwarduje ten mail dalej,
   a raport wewnętrzny zawiera rzeczy nie dla klienta. Jeśli klient ma dostać PDF — powiedz to Jankowi,
   niech zdecyduje.
5. **NIGDY bezpośrednio do klienta.** Wszystko na `js@auranet.com.pl`, Janek przekazuje.
6. Po akcepcie: commit raportu i maila do repo + push.
7. Zapisz memory: nowy „START TUTAJ" dla projektu (wyniki, koszty, plan kolejnego miesiąca, co otwarte),
   zaktualizuj `MEMORY.md` i oznacz poprzedni start-here jako superseded.

---

## 6. Pułapki specyficzne dla AGRII

| Pułapka | Co zrobić |
|---|---|
| Krytyka strony, którą sami zbudowaliśmy | Framing rozwojowy w kliencie, audyt tylko wewnętrznie |
| Podanie sumy rocznej budżetu | Tylko 2 000 zł netto/mies., nigdy 12 × cokolwiek |
| Wymyślona stawka / widełki | Zero cen bez akceptu Janka |
| Weryfikacja parametrów produktu w bazie | Weryfikuj render — parametry żyją w 4 warstwach |
| Stary render mimo poprawnej bazy | CDN nazwa.pl + `_elementor_element_cache` + pliki sitemapy RankMath |
| Multi-location GBP w mailu | Przemilcz do czasu dostępu do oddziałów |
| Dług nawigacyjny (3 pozycje menu) | Wraca we wrześniu **z landingami** (M4), nie wcześniej — nie obiecuj wcześniej |
| Formalizacja komunikacji z Pawłem | Paweł = telefon Janka, nie mail-driven. Bez agencyjnych frameworków |
| Propozycja umowy / klauzul | AGRIA działa na akcepcie mailowym, nie proponuj umów |
| Sekcja Google Ads „bo w ASEO była" | Najpierw sprawdź, czy kampanie istnieją |

---

## 7. Definition of done

- [ ] `docs/raporty/2026-07.md` — pełny, na świeżych danych z API, z oceną realizacji celów (także niedowiezionych)
- [ ] `docs/raporty/2026-07-mail.md` — mail ~30-40 linii, framing rozwojowy, budżet miesięczny, pokazany Jankowi inline
- [ ] Oba pliki wystawione na auratest, linki podane w czacie
- [ ] Wysłane przez `send-to-jan`, bez załączników, tylko na `js@auranet.com.pl`
- [ ] Commit + push w `~/projekty/agria`
- [ ] Memory zaktualizowane (nowy start-here + `MEMORY.md`)
