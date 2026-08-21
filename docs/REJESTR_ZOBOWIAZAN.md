# Rejestr zadań — AGRIA

> **JEDNA I JEDYNA lista zadań projektu.** Niezależnie od tego, czy temat zgłosił Paweł, Kazimierz,
> Janek czy Claude — wchodzi tutaj i tylko tutaj.
>
> **Dwie części, dwa czytania.** Góra (`KOLEJKA`) odpowiada na „co robimy teraz i co nas blokuje".
> Dół (`DZIENNIK`) odpowiada na „co dostarczyliśmy w miesiącu X" — materiał do raportu miesięcznego.
>
> Git zapisuje to, co **napisaliśmy**. Ten plik zapisuje to, co **zlecone i jeszcze niezamknięte** —
> wymiar, którego commit z natury nie niesie, bo opisuje artefakt, nie stan obowiązku.
>
> Stan na **2026-08-21** (dopisane T-052…T-059; T-039 wchłonięte przez T-058; T-052 i T-053 domknięte). Bazowa weryfikacja **19.08**: MCP `query_db`, `curl` na produkcji,
> GSC URL Inspection API, Google Ads API, PSI/CrUX — nie z dokumentów.
> Numeracja `T-NNN` od 19.08.2026, mapowanie starych ID na końcu pliku
> (ADR `docs/decyzje/2026-08-19-numeracja-T-NNN-i-przebudowa-rejestru.md`).

## Jak to działa

**Zasady zapisu:**

1. **Nowy temat = nowy wiersz od razu**, w momencie zgłoszenia. Nie „zapamiętam".
2. **Zawsze źródło i data zgłoszenia** — `[P]` Paweł · `[K]` Kazimierz · `[J]` Janek · `[A]` Auranet-Claude.
3. **Commit zamykający pozycję zmienia jej wiersz w tym samym commicie** i wpisuje hash do „Dowodu".
   **Wiersz bez dowodu nie ma prawa mieć ✅.**
4. **Godziny wpisuj przy domknięciu, do dziennika.** AGRIA jest na ryczałcie — klient godzin nie widzi,
   my ich potrzebujemy, żeby wiedzieć, czy pakiet się spina. `5 h*` = wartość nieodtworzona wstecz,
   znacznik, nie pomiar.
5. **Przed raportem miesięcznym skonfrontuj dziennik z `git log --since=… --until=…`.** Ręczna lista
   zawsze się rozjeżdża — to jest powód, dla którego ten plik powstał.
6. **Numer zadania wchodzi w nazwy plików** — prompt, audyt, raport i mail dostają prefiks `T-NNN`.

**Status:** 🔴 na nas, nic nie blokuje · 🟡 czeka na AGRIĘ · 🔵 zakres do rozstrzygnięcia ·
⚪ robi AGRIA · ✅ zamknięte i zweryfikowane · ⛔ unieważnione, nie wykonywać

**Zakres:** **R** ryczałt 2 000 netto/mies (M1–M6, akcept 27.05) · **P** poza ryczałtem, osobna
pozycja handlowa · **W** własne Auranet, nie fakturujemy · **K** koszt albo robota po stronie AGRII

---

# KOLEJKA

## 🔴 Teraz — 8 pozycji, nic ich nie blokuje

| ID | Zadanie | Linia | Zakr. | Dowód / kontekst |
|---|---|---|---|---|
| **T-027** | `/do-pobrania/` — zgłoszenie do reindeksacji | SEO | R | **Zgłoszone 19.08 15:16 UTC** przez `~/bin/index-submit` (1 URL, `OK`, zużycie 1/100; log `~/.claude/indexing-submit.log`). Strona zgłoszona **już po** T-008 i T-009. Stan przed: `BLOCKED_BY_META_TAG`, ostatni crawl 2026-04-12, live `index, follow`. **Dowodem domknięcia jest zmiana werdyktu GSC, nie zgłoszenie** — recheck 22.08 (+72 h) i 02.09 (+14 dni). **Wzmocnienie 19.08 18:14:** sitemapa RankMath podawała dla tej strony `lastmod 2026-06-29` mimo dzisiejszej edycji (cache plikowy `uploads/rank-math/*.xml`, 6 plików z 14.07 i 13.08). Cache usunięty przez FTP po kopii `agria-backups/rank-math-cache-2026-08-19-1814.tgz`; sitemapa odbudowana i podaje teraz `2026-08-19T15:14:25`. Kontrola po odbudowie: 6 sitemap odpowiada 200, koszyk i zamówienie **nadal poza** sitemapą (T-019 nietknięte), 16 kart produktowych z dzisiejszą datą |
| **T-026** | Indeksacja — sześć URL-i poza indeksem: **diagnoza gotowa, decyzja przed wykonaniem** | SEO | R | **Diagnoza 19.08: `docs/audits/T-026-diagnoza-indeksacji-2026-08-19.md`.** Przyczyna **nie jest techniczna** — wykluczone kolejno: sitemapa (pobrana 13.08, 0 błędów), odpowiedź dla Googlebota (200 + `index, follow` na wszystkich sześciu), `robots.txt`, `noindex` w sitemapie (zero stron), budżet crawlowy (strona główna crawlowana 18.08, kategoria 16.08, karta produktu 14.08). **Rozstrzygające:** `/wapnowanie-gleby/` i `/ile-wapna-granulowanego-na-ha/` powstały tego samego dnia — hub jest zaindeksowany i crawlowany 15.08, poradnik nigdy nie pobrany. **Dla każdego z sześciu adresów istnieje już inna strona AGRII rankująca na tę intencję** (hub na „ile wapna granulowanego na hektar" poz. 7,7 / 1 289 wyśw.; kategoria `/wapno-do-oczyszczalni/` na „higienizacja osadów ściekowych" 113 wyśw.; karta `/kreda-malarska/kreda-malarska/` poz. 8,9). Dwa adresy mają **zero popytu** na frazy tematyczne. **Nie zgłaszać czwarty raz do Indexing API.** Cztery scenariusze do decyzji Janka opisane w diagnozie |
| **T-039** | Korekty kampanii Marka: wykluczenia opakowaniowe, stawka Brand 0,50 → 3,00 zł, grupa „Producent" `[A]` | Ads | P | **Marka nie wydała ani grosza przez sześć dni emisji** (Ads API 19.08) — przy 0,50 zł nie wchodzimy do aukcji. **Wchłonięte przez T-058** — nie wykonywać osobno, korekty idą jedną operacją razem z przebudową struktury kampanii |
| **T-054** | Blok B — paszarstwo: karta #307, opis kategorii `/paszarstwo/`, poradnik o dawkowaniu kredy pastewnej | SEO | R | **8 940 wyszukań/mies., największy klaster w portfelu** (`kreda pastewna` 2 400, `kreda pastewna dla kur` 1 600, `wapno dla kur` 1 000, `kreda dla kur` 720). Produkt o najwyższym skoku marży w cenniku: 190 zł/t luz → 610 zł/t worki 30 kg. Plan: `docs/seo/T-052-AUDYT_FRAZ_I_PLAN_SEZON_2026-08-21.md` blok B. ⚠️ **Karta #307 opisuje kredę pastewną parametrami wapna tlenkowego** (reakcja egzotermiczna, pH >12 — węglan tego nie robi), zgłoszone w `FAKTY_KLIENTA` §9 i nierozstrzygnięte. Bez poprawnych parametrów nie publikujemy karty; poradnik i kategoria idą niezależnie |
| **T-055** | Blok C — pole i uprawa: poradnik „Jakie wapno na pole” + przebudowa `/jak-stosowac-wapno-nawozowe/` na terminarz | SEO | R | **1 890 + 1 400 wyszukań/mies., zerowe pokrycie.** `wapno na pole` 390, `jakie wapno na pole` 140, `czy można siać wapno na zboże` 90, `wapno pod ziemniaki` 100, `wapno na łąki` 100, `wapno pod rzepak` 20 (**sierpień 140**). Terminarz: `kiedy wapnować glebę` 320 (**październik 590**), `kiedy siać wapno granulowane` 420, `kiedy wapnować pole` 90 (**październik 260**). **Terminarz robimy przebudową istniejącego URL-a, nie nowym** — drugi adres na „kiedy wapnować” łamałby ADR 11.08. **Termin publikacji: 05.09**, żeby zdążyć na szczyt październikowy |
| **T-056** | Blok D — staw i rybactwo: kategoria `/wapno-do-stawow/` + 2 poradniki + powrót pozycji menu | SEO | R | **4 100 wyszukań/mies., zerowe pokrycie i pusta kategoria.** `kreda do stawu` 1 600, `wapno do stawu` 390, `kreda do stawu rybnego` 260, `wapno do stawu z rybami` 210. GSC 28 dni: **0 wyświetleń na czymkolwiek ze słowem „staw”**. SERP na „wapno do stawu”: **trzy z siedmiu wyników TOP7 to posty z Facebooka** — najsłabsza konkurencja w całym portfelu. Zobowiązanie wobec Kasjana z maila 06.08 („wrzesień — treści pod oczyszczalnie i rybactwo”). Spłaca też dług nawigacyjny z 30.07 |
| **T-057** | Blok E — gleba i odczyn: 2 poradniki + strona tonażowa na `/wapno-nawozowe-hurt/` | SEO | R | **6 320 wyszukań/mies.** `ph gleby` 1 000, `badanie gleby` 1 000, `zakwaszenie gleby` 390, `stacja chemiczno-rolnicza` 260, `analiza gleby` 260, `jak podnieść ph gleby` 210. **Ten klaster wypadł z audytu 19.05 przez filtr regexowy** — żadna z tych fraz nie zawiera słowa „wapno” ani „kreda”. To ta sama droga, którą Polcalc zbudował 95% widoczności. Strona tonażowa: `wapno granulowane big bag` 520 łącznie, `… cena za tonę` 490 |
| **T-058** | Ads — przebudowa kampanii: struktura segmentowa, grupa „Producent”, grupa „Kreda pastewna” | Ads | P | **Częściowo wykonane 21.08** (dowód w dzienniku): 26 wykluczeń obcych marek + stawka Brand 0,50 → 3,00 zł. **Zostaje:** grupa „Producent” (`wapno nordkalk` 210/mies. HIGH, `nordkalk` 880 — licytacja na cudzy znak jest dozwolona zawsze, **w treści reklamy nazwy nie używamy** dopóki T-040 nie potwierdzi statusu dystrybutora), grupa „Kreda pastewna” (wymaga zdjęcia `pastewna`/`kury`/`drób` z wykluczeń kampanii i przeniesienia ich na poziom pozostałych grup) oraz podział budżetu. **Decyzja Janka przed wykonaniem** — patrz „Do rozstrzygnięcia” |
| **T-059** | Landingi Ads — ścieżka kontaktu | Strona | R | **Wykonane 21.08, dowód w dzienniku.** Zostaje jedna rzecz: formularz „oddzwonimy” korzysta z istniejącego modułu `inquiry-form`, który wymaga wyboru produktu z 20 opcji — na landingu z ruchem „wapno granulowane cena” to zbędne tarcie. Lekki wariant (`mode="callback"`: imię, telefon, tonaż, lokalizacja) do dorobienia w module |

## 🟡 Czeka na AGRIĘ

| ID | Zadanie | Czeka od | Na co konkretnie |
|---|---|---|---|
| **T-040** | Teksty reklam z nazwą „Nordkalk" `[A]` | 19.08 | **status autoryzowanego dystrybutora.** Licytować na cudzy znak wolno zawsze, użyć w treści — tylko odsprzedawcy. W repo tej informacji nie ma (sprawdzone `grep` po `docs/` i memory) — **nie zgadywać** |
| **T-050** | Zdjęcia na wizytówkę GBP Tarnów `[A 20.08]` | 20.08 | **materiał od AGRII.** Profil ma 10 kadrów, wszystkie wgrane 02.07: tylko 2 zewnętrzne i 8 „dodatkowych". Brak wnętrza, produktu i transportu. Zastępników nie generujemy — to zdjęcia firmy na jej własnym profilu w Mapach. Reszta T-046 zrobiona 20.08 |
| **T-043** | Weryfikacja mockupu kalkulatora Mg przez Kazimierza | 18.08 | `mockups/agria-kalkulator-mg-test-2026-08-18.html` przekazany 18.08 |
| **T-047** | Odzysk profili GBP **Niedomice** i **Radgoszcz** | 15.07 | dostęp. Ścieżka: Request access z konta Auranet + weryfikacja własności (KRS 0000170666, NIP 8730006657). **W komunikacji do klienta przemilczeć multi-location**, dopóki brak dostępu |

## 📅 Zaplanowane — wrzesień (M4)

| ID | Zadanie | Linia | Zakr. | Uwagi |
|---|---|---|---|---|
| **T-044** | Wdrożenie modułu Mg w kalkulatorze na produkcję | Kalkulator | P ≈4 h | Po T-043. **4 kwestie otwarte** przed wdrożeniem — memory `project_agria_kalkulator_mg` |
| **T-031** | CWV mobile — LCP | SEO | R | **Odblokowane 19.08 — T-048 zamknięty, PSI mierzy.** Pomiar 19.08 17:03: **mobile LCP 7,3 s, score 0,69**; **desktop LCP 1,5 s, score 0,95** — problem jest wyłącznie mobilny. TBT 80 ms i CLS 0,002 są dobre, więc to ciężki zasób, nie JavaScript. CrUX „data not found" (za mały ruch). Proxy z Elary 19.08: główna **TTFB 1,27 s przy cache-miss, HTML 154 KB**; karta produktu TTFB 0,35 s |
| **T-030** | LocalBusiness ×2 (Niedomice, Radgoszcz) w schema | SEO | R | Front ma tylko `Organization`. Dane oddziałów mamy z T-003 |
| **T-045** | Ofertownik, etap zerowy: audyt wycieku cen → konwersja jednego produktu na wariantowy → sprzątanie atrybutów → cennik | Ofertownik | **W** | Niezaczęty, osobny wątek (rozdzielony od T-010 decyzją 19.08). Spec: `docs/specs/2026-08-18-ofertownik-design.md`. **Audyt wycieku cen to warunek bezpieczeństwa danych, nie porządki** — ceny wariantów WC są domyślnie widoczne na froncie, w REST API, w feedach i w schema Rank Matha, a ta warstwa ma pozostać **niejawna** |
| — | Menu: powrót pozycji Sadownictwo / Rybactwo / Hurtownie | Strona | R | Zdjęte 30.07 jako `draft`. Wracają **razem z treścią**, nie z landingami — memory `project_agria_nav_debt_m4`. Przypomnienie: `docs/przypomnienia/2026-09-01-menu-segmenty-m4.md` |

## 🔵 Do rozstrzygnięcia — zakres miękki

| ID | Zadanie | Co rozstrzygnąć |
|---|---|---|
| **T-033** | Zgody / pomiar GA4 | **Korekta stanu wiedzy:** Complianz Privacy Suite premium **7.5.7.2 jest aktywny** i leci na froncie (95 wystąpień `cmplz`). Memory `project_agria_ga4_consent_blocker` i backlog on-page twierdzą, że CMP nie ma — **to nieprawda**. GA4 mimo to nie mierzy (5 sesji organicznych vs 221 kliknięć GSC w lipcu). Problem jest w konfiguracji zgód, nie w braku bannera — **rediagnoza od zera** |
| **T-034** | Premmerce DOM-XSS | Zainstalowana **2.3.13**, podatna była 2.3.11. Changelogu nie da się sprawdzić publicznie — wtyczki nie ma w repozytorium wp.org. Do potwierdzenia u vendora albo z `readme.txt` na serwerze |

## ⛔ Unieważnione — nie wykonywać

| ID | Co | Czym unieważnione |
|---|---|---|
| **T-035** | Landingi organiczne `/wapno-palone/`, `/wapno-magnezowe/`, `/wapno-hydratyzowane/`, `/kreda-nawozowa/` | ADR `2026-08-11-podzial-rol-ads-seo.md` + memory `project_agria_architektura_kanalow`: **landingi wyłącznie jako cele Ads, poza indeksem**. Powód zmierzony: 6 URL-i na frazę „wapno bielik" → pozycja 15,3; frazy z jednym URL-em w TOP10. Organik idzie treścią |
| **T-036** | Landingi segmentowe `/wapno-do-stawow/`, `/wapno-do-sadu/`, hub Oczyszczalnie | jw. Menu wraca we wrześniu z treścią, nie z landingami |
| **T-037** | `/transport-i-dostawa/`, sekcja B2B, formularz z tonażem, formy dostawy z powrotem na karty | częściowo sprzeczne z T-002 (Paweł kazał zdjąć formy dostawy). Powrót wymaga jego zgody — bez niej nie ruszać |
| **T-038** | Plan hub-and-spoke per segment (HUB Rolnictwo / Rybactwo / Oczyszczalnie) | jw. **`CONTENT_AUDIT_2026-06-15.md` §3 nie ma o tym ani słowa** — to jest źródło powtarzających się propozycji „zróbmy huby" |
| **T-006** | Przebudowa sekcji „Dział sprzedaży" po odejściu P. Stanisława | **Zdjęte z kolejki decyzją Janka 20.08** `[J]`. Nie dopytywać Pawła o skład działu — pytanie wypada z listy. Otwarte osobno: zepsuty `href` telefonu Kazimierza (`http://+48 781 875 411`) — nie zgłoszone jako zadanie |
| **T-007** | Korekta interpunkcji w tekstach | **Wykonane przez Pawła samodzielnie** (potwierdzenie Janka 20.08 `[J]`). Robota po stronie AGRII, nie nasz deliverable — poza dziennikiem |

---

# DZIENNIK

Godziny z gwiazdką (`5 h*`) to **znacznik nieodtworzonej wartości**, nie pomiar — decyzja 19.08,
gdy dziennik powstawał wstecz. Od M4 wpisujemy realne.

## M1 — czerwiec 2026 · ryczałt 2 000 netto

| ID | Co dostarczone | Dowód | h |
|---|---|---|---|
| T-001 | Kalkulator przestał proponować kredę pastewną i malarską | wdrożone 18.06, `post__not_in [304,307]`, readback z serwera | 5 h* |
| T-002 | Formy dostawy zdjęte ze specyfikacji 19 kart + FAQ | wdrożone 29.06, commit `1cc6bd8`, 19/19 zweryfikowane | 5 h* |
| T-004 | Karty produktu i charakterystyki na `/do-pobrania/` | wdrożone 29.06, 22 pozycje w sekcji, live-zweryfikowane | 5 h* |
| T-005 | Zdjęcia produktów zgodne z katalogiem | wdrożone 29.06 | 5 h* |

## M2 — lipiec 2026 · ryczałt 2 000 netto

| ID | Co dostarczone | Dowód | h |
|---|---|---|---|
| T-003 | Telefony na mapie zgodne z oddziałami, numer `660` usunięty | wdrożone 01.07, commit `1dfe5c5`, zero wystąpień `660` na froncie | 5 h* |
| — | Rdzeń URL/taksonomii — Blok A | wdrożone 08.07 na produkcji i w DB | 5 h* |
| — | Raport miesięczny M2 dla AGRII | `docs/raporty/DOWODY_M2_2026-07.md` | 5 h* |

## M1–M2 — blok SEO on-page (daty per pozycja nieodtworzone)

Wszystkie **zweryfikowane na produkcji 19.08**, nie przepisane ze statusu w dokumencie —
sześć pozycji miało w papierach „niezrobione", a są zrobione.

| ID | Co dostarczone | Dowód z produkcji 19.08 |
|---|---|---|
| T-012 | Schema Organization zamiast „My Blog" | `"@type":"Organization"`, `"name":"AGRIA Sp. z o.o."` |
| T-013 | Nagłówki bezpieczeństwa | `curl -I`: HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy (4 z 6 — brak CSP i Permissions-Policy) |
| T-014 | Title strony głównej skrócony | 56 znaków, `rank_math_title` na ID 321 |
| T-015 | `product_cat` w sitemapie | `product_cat-sitemap.xml` obecny w indeksie |
| T-016 | SKU dla produktów | 18 z 19 ma `AGR-0xx`; #303 świadomie bez (decyzja katalogowa) |
| T-017 | Literówki w nazwach produktów | `post_title`: „węglanowe", „zawierające" — poprawne w 19/19 |
| T-018 | Sitemapa RankMath po migracji URL | `product-sitemap.xml` z aktualnymi adresami |
| T-019 | `/cart/` poza sitemapą | `page-sitemap.xml`: 11 URL-i, `/cart/` nieobecny |
| T-020 | Meta title + description na stronach statycznych | 6 z 6 (oferta, o-firmie, poradniki, kalkulator, do-pobrania, kontakt) |
| T-021 | Bielik #309 on-page | `Wapno hydratyzowane Bielik CL 90-S \| CaO+MgO 90%` — parametry normowe z karty Nordkalk |
| T-022 | pH wapna palonego („>16" było fizycznie niemożliwe) | render karty: `pH >12` |
| T-023 | „35 lat" → „37 lat" | 0 wystąpień „35 lat" na `/`, `/o-firmie/`, `/oferta/` |
| T-024 | Landing `/wapno-do-stabilizacji-gruntow/` | ID 2745, HTTP 200, w sitemapie |
| T-025 | Landingi Ads poza indeksem | `/wapno-granulowane/`, `/wapno-nawozowe/`: HTTP 200, `noindex, follow` |
| — | Demo-produkt motywu zdjęty z indeksu | `/produkt/organic-pineapple/` → HTTP 404 |

**Razem M1–M2: 14 pozycji SEO + 7 z tabel miesięcznych.**

## M3 — sierpień 2026 (w toku, do 31.08) · ryczałt 2 000 netto + Ads 1 200 media + OLX

| Co dostarczone | Dowód | Zakr. | h |
|---|---|---|---|
| Uruchomienie kampanii Google Ads, konto 674-207-1446 | ADR `2026-08-13-uruchomienie-kampanii-ads.md`, kampanie żywe od 13.08 | P | 5 h* |
| Geoblok bezpieczeństwa | `src/plugins/agria-by-auranet/security-geoblock.php`, wdrożony 14.08. **T-048 domknięty 19.08:** boty pomiarowe dopisane do `$good_bots` (commit `34cd965`, backup `security-geoblock.php.bak-2026-08-19`), PSI 19.08 17:03 przechodzi — mobile score 0,69 / LCP 7,3 s, desktop 0,95 / LCP 1,5 s, `runtimeError: None`, `finalUrl: https://agria.pl/`. `AdsBot-Google` na liście (linia 64) — reklamy mają dostęp do landingów. Zwykły ruch: HTTP 200. Pomiary: `tmp/psi-T048-2026-08-19-1703.json` | R | 5 h* + 0,3 h |
| OLX: treści, siatka 53 miejscowości, spięcie z Partner API | `data/olx/`, `scripts/olx/` — czeka wyłącznie na pakiet Premium po stronie AGRII | P | 5 h* |
| Mockup kalkulatora z modułem Mg | `mockups/agria-kalkulator-mg-test-2026-08-18.html`, przekazany Kazimierzowi 18.08 | P | 5 h* |
| Dostęp SSH do produkcji + WP-CLI | klucz `claude-agria-elara` wgrany 18.08, `~/secrets/agria/ssh.env` | R | 5 h* |
| ADR dwie warstwy cen | `docs/decyzje/2026-08-19-dwie-warstwy-cen.md` | R | 5 h* |
| Spec ofertownika | `docs/specs/2026-08-18-ofertownik-design.md` | W | 5 h* |
| Porządek dokumentacji: `FAKTY_KLIENTA.md`, rejestr, rozbiórka `MASTER_PROMPT`, `CLAUDE.md` na wzorcu Primy/Victorini | commity `2109a2f`, `33fddef`, `a0b07b4` | R | 5 h* |
| **T-008** — 8 atestów i kart charakterystyki Nordkalku na `/do-pobrania/` | Wdrożone 19.08 15:14. 8 PDF-ów wgranych FTP-em do `uploads/2026/08/`, **wszystkie HTTP 200**. Strona ID 731 zmieniona w **obu warstwach**: `_elementor_data` 14 478 → 13 138 B, `post_content` 36 782 → 35 599 B. Render (Chrome MCP): **22 karty produktu · 4 karty charakterystyki · 5 atestów**, 31 linków PDF, wszystkie 200. „Nordkalk" na froncie: 6 wystąpień (było 0). Backup: `agria-backups/przed-T-008-T-009-20260819-151022.sql` (17 tys. wierszy) | R | 2,5 h |
| **T-009** — usunięcie sekcji „Certyfikaty" z `/do-pobrania/` | Wdrożone 19.08 15:14, jedną edycją z T-008. Front: **0 wystąpień „ertyfikat"** (było 7), 0 wystąpień „CEM/Dyckerhoff/ISO 9001". Sekcja zniknęła z nagłówkiem, bez pustej ramki. Znikł przy okazji duplikat linku (poz. 1 = poz. 2) i literówki w nazwach plików. **Atest OSChR i 4 karty charakterystyki nietknięte.** Strona: HTTP 200, 0,34 s; `/`, `/oferta/`, `/kontakt/`, `/kalkulator-wapnowania/` → 200 | R | z T-008 |
| **T-010 (część: 15 kart)** + **T-011** — widełki cenowe i nagłówki H2 z frazą cenową | Wdrożone 19.08 15:35. **15/15 kart ma na froncie `<h2>` z frazą cenową i akapit z widełkami** (weryfikacja `curl` per URL). `_price` puste w **19/19**, Store API `"price":"0"` — warstwa ofertownika nietknięta. Schema bez `Offer`. Jeden `<h1>` na kartę. Cztery karty bez wyceny nietknięte (0 wystąpień „zł/t netto", HTTP 200). Trzy karty renderujące z Elementora (307, 310, 320) zmienione **w obu warstwach**. Render potwierdzony Chrome MCP na `/wapno-nawozowe-rolnictwo/agrobielik-70/`: blok stoi między specyfikacją a FAQ. **Korekta redakcyjna 19.08 wieczorem:** pierwsza wersja podawała dwie kwoty obok siebie, co przy Agrobieliku 70 dawało skok +82 %, a przy kredzie pastewnej +221 % — druga liczba odstraszała zamiast informować. Wszystkie 15 kart przepisane na **jedną kwotę z warunkiem** plus formy bez cen; zweryfikowane: 0 kart z więcej niż jedną ceną na froncie. Backup: `agria-backups/przed-T-010-20260819-153153.sql` | R | 3 h |
| **T-010 (domknięcie)** — ceny na 2 landingach Ads + sekcja cenowa na hubie | Wdrożone 19.08 18:15. **Stan zastany inny niż w rozpisce z 13.08:** oba landingi już istniały z pełną treścią i `noindex, follow` (rozpiska mówiła: `/wapno-granulowane/` 0 bajtów i `index`, `/wapno-nawozowe/` nie istnieje). Brakowało im wyłącznie ceny. **Uzasadnienie pilności z Ads API:** kampania Rolnictwo wydała **199,62 zł na 100 kliknięć kierowanych właśnie na te dwie strony** (66+1 na `/wapno-nawozowe/`, 33 na `/wapno-granulowane/`), przy zerze konwersji. **Poradnik `/ile-kosztuje-wapnowanie-hektara/` ODRZUCONY** — ADR `docs/decyzje/2026-08-19-poradnik-cenowy-odrzucony.md`: fraza ma **zerowy wolumen** (DataForSEO), a hub `/wapnowanie-gleby/` już rankuje na „ile kosztuje tona wapna" (**poz. 2,0**), „cena wapna na pole" (2,0), „cena wapna nawozowego" (2,5). **Zamiast poradnika: sekcja „Ile kosztuje wapnowanie" na hubie** — który rankował na pytania cenowe i miał **zero wystąpień** słów „zł", „cena", „koszt". Teraz widełki trzech typów wapna + przeliczenie na hektar. Weryfikacja: trzy strony 200, landingi nadal `noindex` i poza sitemapą, hub `index, follow`, sekcja w strukturze między doborem wapna a terminem wapnowania (Chrome MCP). Backup: `agria-backups/przed-T-010b-landingi-hub-20260819-181253.sql` | R | 1,5 h |
| **T-029** — login administratora przestał wyciekać (3 kanały) | Wdrożone 19.08 17:39. Audyt 15.06 wskazywał schema; zmierzone 19.08 kanały były **trzy**. **(1) Schema:** `display_name`/`user_nicename` użytkownika 1 → „AGRIA Sp. z o.o." / `agria`; **login `js` niezmieniony** (to pole logowania). Front: **0 wystąpień `"name":"js"`** na `/`, `/o-firmie/`, `/kontakt/`, `/do-pobrania/`, `/wapnowanie-gleby/` (było na każdej). **(2) Enumeracja:** Rank Math `disable_author_archives=on` → `/?author=1` i `/?author=2` dają **301 na stronę główną** (było 301 na `/author/js/`). **(3) REST:** nowy moduł `security-user-enum.php` (filtr `rest_pre_dispatch`) → `/wp-json/wp/v2/users` i `/users/1` zwracają **401** dla anonima. Role sprawdzone przez `rest_do_request`: administrator 200, redaktor 200, anonim 401 — pierwsza wersja filtra odcinała redaktora (403), warunek poprawiony z `list_users` na `edit_posts`. `/wp-json/`, `/wp/v2/posts`, Store API i wszystkie strony nadal 200. Backupy: `agria-by-auranet.php.bak-20260819-173923`, opcje Rank Math w `agria-backups/rankmath-titles-przed-T029.json` | R | 1,5 h |
| **T-032** — 301 dla starej bazy `/kategoria-produktu/*` | Wdrożone 19.08 17:45 przez FTP. **Sześć reguł jawnych** w bloku `# BEGIN AGRIA 301` — po jednej na kategorię z `product_cat-sitemap.xml` plus sam prefiks. Reguła generyczna świadomie odrzucona: zamieniałaby natychmiastowe 404 nieistniejących adresów na 301 prowadzące do 404. Wynik: **5/5 kategorii → 301 na czysty URL**, czyste URL-e nadal 200, `/kategoria-produktu/` → `/oferta/`, `/kategoria-produktu/nieistnieje/` → **404** (bez zmian), pętli brak (2 skoki). **Reguły z lipca nietknięte** (`/wapno-nawozowe-hurt/`, `/wapno-do-sadu/`, `/kreda-pastewna/`, przekierowania produktowe — sprawdzone). Panel 302, `wp-login` 200, `/wp-json/` 200, Store API 200, `wp-cron` 200, siedem kluczowych stron 200, trzy sitemapy 200. **Kontekst:** GSC za 90 dni pokazuje dla `/kategoria-produktu/*` **zero wyświetleń** — canonical działał, więc 301 zamyka furtkę na przyszłość, nie odzyskuje ruchu. Kopia: `agria-backups/htaccess-przed-T032-*.txt`, snapshot w repo `src/htaccess/` | R | 1 h |
| **T-028** — duplikaty pod starą bazą `/produkt/` + 15 osieroconych wpisów | Wdrożone 19.08 18:00. **Diagnoza wyjściowa w rejestrze była błędna:** HTTP 200 pod `/produkt/*` nie pochodziło od wpisów `post_type=produkt` — ten CPT **nie jest zarejestrowany w WordPressie** (`wp post-type list`). To była stara baza URL serwująca produkty WooCommerce. Zmierzone: **19 z 19 produktów** odpowiadało 200 pod obiema bazami. **Rozwiązanie: moduł `modules/legacy-urls/`** — hook `template_redirect` czyta adres kanoniczny z WooCommerce i robi 301. Wybrany zamiast 19 ręcznych reguł w `.htaccess`, bo adres docelowy zależy od kategorii i rozjechałby się przy pierwszej zmianie. Wynik: **19/19 → 301** na adres właściwy, adresy właściwe 200, `/produkt/nieistnieje/` → 404, brak pętli. Pierwsza wersja obsługiwała tylko GET — przy HEAD stary adres nadal dawał 200; warunek rozszerzony o HEAD i przetestowany. **Sieroty ID 60–74:** zero linków w treści, w Elementorze i w menu (sprawdzone `query_db`); `wp post delete` odmówił kosza (typ niezarejestrowany, wymagał `--force`), więc **status zmieniony na `draft`** — odwracalne, zamiast trwałego kasowania. **Kontekst:** GSC za 90 dni pokazuje pod `/produkt/*` wyłącznie demo-produkt motywu (`organic-pineapple`, 7 wyświetleń, już 404). Realne produkty nie zbierały tam ruchu — zysk to budżet crawlowy, nie pozycje | R | 2 h |

| **T-046** — optymalizacja profilu GBP Tarnów | Wdrożone 20.08. Zrzut przed/po: `tmp/gbp-tarnow-2026-08-20.json` i `-PO.json` (GBP nie wersjonuje profilu, zrzut to jedyny rollback). **`websiteUri`: `http://www.agria.pl/` → `https://agria.pl/`** — było HTTP i `www`, czyli przekierowanie na starcie każdego kliknięcia z Map. **Publikacje: 0 → 4, wszystkie `LIVE`** — po żniwach, kalkulator dawki, atesty na `/do-pobrania/` (spina się z T-008), oferta z własnym transportem; bez cen, cztery adresy docelowe sprawdzone (200). **Opinie bez odpowiedzi: 6 → 0**, każda odpowiedź nawiązuje do treści opinii. **Naprawiony błąd z 22.07: pod opinią 5★ „Polecam" wisiały nasze przeprosiny za niezgodność dostawy** — ten sam tekst wklejono wtedy pod opinię 1★ i pod piątkę. Podmienione na podziękowanie, potwierdzone odczytem zwrotnym. Nowe skrypty: `scripts/gbp_dump.py`, `scripts/gbp_odpowiedz.py`, `scripts/gbp_patch.py` — domyślnie nic nie wysyłają, wymagają `--wyslij`. **Wiedza operacyjna: GBP przez kilkadziesiąt sekund po zapisie oddaje jeszcze STARĄ wartość** — pierwszy odczyt zwrotny pokazał stary tekst mimo `PUT` bez błędu; skrypty czytają w pętli. **Nietknięte świadomie:** nazwa (przeładowana słowami kluczowymi, ale zmiana nazwy uruchamia ręczną weryfikację Google i grozi zawieszeniem profilu) oraz kategorie. **Zostaje: zdjęcia** — 10 kadrów, wszystkie wgrane 02.07, tylko 2 zewnętrzne i 8 „dodatkowych"; brak wnętrza, produktu i transportu. Zapotrzebowanie do Pawła, zastępników nie generujemy | R | 2 h |
| **T-051** — miniatury OLX nieczytelne na telefonie | Wykonane 21.08. **Diagnoza:** kadr miniatury na liście mobilnej to **150×183 px, proporcja 0,82** przy `object-fit: cover`, a pliki były poziome 1500×1050 (1,43) — widać było **środkowe 57% szerokości**, więc na wszystkich 12 wzorach ucinało hasło z obu stron, początek paska korzyści i logo („apno na gleby ciężk", „2–4 TYGODNIE", „Ag"). Karta ogłoszenia była bez strat — problem dotyczył wyłącznie miejsca, w którym zapada decyzja o kliknięciu. Zmierzone przez Puppeteer na realnym OLX (`scripts/olx/zrzut_mobile.mjs`); Chrome MCP nie emuluje telefonu, a przy desktopowym UA OLX podmienia viewport na 887 px. **Rozwiązanie:** nowy generator `scripts/olx/miniatury_v3.py` — treść w kwadracie ze środka (blok 820 px), hasło mówi **tylko, do czego** służy towar (nazwa produktu stoi w tytule ogłoszenia tuż obok), pasek korzyści w `#D3FF23` i małe logo pod spodem, wszystko wyśrodkowane. Tła wygenerowane od nowa — jasne i nasycone zamiast brązowo-szarych. **24 pliki: dwa warianty na siatkę do rotacji** (inne tło, inna korzyść, to samo hasło); w payloadzie idą naprzemiennie — 101×A, 99×B. **Podmiana:** `PUT` na 200 ogłoszeniach przez `--update` z bezpiecznikiem; test na jednym potwierdził, że edycja **nie zjada miejsca z pakietu** (`left: 0` bez zmian) i status wraca na `active`. **Poprawka merytoryczna przy okazji:** generator miniatur był **piątą warstwą, którą T-042 pominął** — nadal mówił „na gleby ciężkie" zamiast „średnie i ciężkie". Zdjęte też twierdzenie „wzrost plonów do 20%" — brak źródła w kartach producentów. **Monitoring:** `scripts/olx/monitor.py` (cron 7:25 codziennie — alarm na Telegram przy ogłoszeniu poza `active`, zgaszonym `auto_extend` albo pakiecie kończącym się w ciągu 7 dni) i `scripts/olx/statystyki.py` (cron 7:35 w poniedziałki). Koszt obrazów: 24 × $0,134 ≈ **3,2 USD** | P | 4 h |
| **T-041** — publikacja 200 ogłoszeń OLX | Wykonane 20.08, 17:23–18:01. **200 z 200 ogłoszeń `active`, zero odrzutów moderacji, `auto_extend` na 200/200** — zweryfikowane odczytem `GET /partner/adverts/{id}` **per ogłoszenie**, nie z listy zbiorczej (lista oddaje statusy z opóźnieniem). Pakiet Premium 200 wyczerpany (`left: 0`), emisja do 19.09, pakiet ważny do 16.09. Rozkład: 11 produktów (AGR-001 52 · AGR-002 25 · AGR-008 20 · AGR-011 18 · AGR-014 16 · AGR-006 16 · AGR-013 14 · AGR-015 12 · AGR-009 12 · AGR-010 8 · AGR-003 7), **53 miasta**, ceny 36–790 zł/t zgodne z planem, zdjęć 7 w 186 ogłoszeniach i 6 w 14. `data/olx/posted.json` zgadza się z payloadem i z API **co do jednego wpisu** (0 różnic w obie strony). **Trzy fazy:** 17 wariantów treści → potwierdzenie → 183 w 12 partiach po produktach, przerwa 2 s między ogłoszeniami (budżet zapytań OLX nieudokumentowany). **Dwie rzeczy zmierzone przy okazji, obie były błędnymi założeniami w dokumentach:** (1) **siedem dużych miast wymaga `district_id`** — POST bez tego pola zwraca `HTTP 400 · district_id: niepoprawna wartość`, dotyczyło 29 ogłoszeń (Warszawa, Kraków, Łódź, Wrocław, Poznań, Katowice, Częstochowa); uzupełnione dzielnicami centralnymi w payloadzie **i** w generatorze (stała `DISTRICTS` w `build_adverts.py`, żeby regeneracja nie cofnęła); (2) **statusy `new` i `disabled` tuż po POST są przejściowe** — aktywacja przychodzi **2 min 14 s – 2 min 58 s** po wystawieniu, a nie „w niecałe 20 sekund" jak mówił prompt. **Bezpiecznik moderacyjny dopisany do `post_adverts.py`** (tryb `--ids`, `--check`, `--guard N`): odczyt statusów co N ogłoszeń **i na koniec każdej partii**, STOP przy `moderated`/`blocked` natychmiast, przy `disabled` dopiero po 5 minutach utrzymania, powiadomienie na Telegram. **Pierwsze dwie wersje bezpiecznika przerwały serię fałszywym alarmem** (brały stan przejściowy za odrzut) — stąd karencja. Powiadomienia do Janka: po fazie 1 i po całości, plus dwa sprostowania. **Luka w tym dowodzie, wyszła 21.08:** weryfikacja poszła wyłącznie przez API (statusy, `auto_extend`, zgodność rejestru) i **ani razu nie objęła wyglądu ogłoszenia na telefonie** — miniatury na liście mobilnej są przycięte w połowie hasła, patrz **T-051** | P | 3 h |
| **T-049** — warstwa zdjęć, tytuły i opisy OLX przed emisją | Wdrożone 20.08, commity `1bc2928` i `6157c49`. **Zdjęcia:** komplet 7 slotów dla 11 kart, 56 unikalnych adresów, wszystkie HTTP 200; 186 ogłoszeń po 7 zdjęć, 14 po 6 (kreda granulowana — karta ID 305 ma na produkcji podpięte zdjęcie innego produktu). Nowe skrypty: `miniatury.py` (12 kadrów przez Gemini `gemini-3-pro-image`, próbka towaru na gradiencie marki, u góry zastosowanie, przy próbce pasek z korzyścią), `karta_info.py` (11 kart z kodem QR do kalkulatora, UTM z `utm_content` per karta), `karty_katalogowe.py` (17 kart z katalogu druku bez QR i bez stopki z adresem), `market_photos.py` (próbka 1 105 ogłoszeń rynku). `zdjecia.py`: plansze 750×1205 zamiast 435×700, łatka po QR przepisana na lustrzane odbicie. **Treść:** tytuły 123–141 zn. (było 108–147), opisy 3 518–4 479 (było 1 145–1 545), doszły sekcje transport / rozsiew / kalkulator / dofinansowanie (+ akapit o naborze łódzkim na 12 ogłoszeniach) / pozostała oferta / dlaczego AGRIA / CTA. Walidacja reguł OLX z OpenAPI przechodzi na 200 ogłoszeniach. **Moderacja:** ogłoszenie 1089946612 wstrzymane (pkt 4.4.c, 4.4.h, 4.4.i, 13.1.d — odczytane w przeglądarce, Centrum Pomocy jest za JavaScriptem). Poprawka: usunięcie słowa „netto" z linii cenowej i klauzuli „nie stanowią oferty handlowej" (4.4.c wymaga ceny końcowej) plus zdjęcie worków z tytułów (inna jednostka niż tona; big-bagi zostają). **Po poprawce status `active`, ogłoszenie widoczne publicznie.** Koszt generowania obrazów: 51 sztuk × $0,134 ≈ **6,80 USD** | P | 6 h |
| **T-042** — poprawki mockupu ogłoszeń OLX po uwagach Kazimierza | Wdrożone 20.08. Zakres doprecyzowany przez Janka: chodziło o mockup ogłoszeń, nie o teksty na stronie. **Jedna korekta merytoryczna:** tytuł ogłoszenia AGR-001 (Agrobielik 70) mówił „do odkwaszania gleb **ciężkich**", podczas gdy lead, `intencja` i pole `Zastosowanie funkcjonalne` w specyfikacji od początku mówiły „gleb **średnich i ciężkich**" — tytuł był węższy od produktu i odcinał gleby średnie. Poprawione w **czterech warstwach**: `scripts/olx/plan.py` (źródło generatora, żeby regeneracja nie cofnęła zmiany), `data/olx/plan-ogloszen.json` i `data/olx/adverts-payload.json` (30 rekordów każdy, oba przechodzą `json.load`), `docs/offers/OLX_TABELA_OGLOSZEN.md` (30 wierszy tabeli). Kontrola: **0 wystąpień starej frazy w całym repo**. **Reszta korekt Kazimierza zaakceptowana bez zmian** — treści idą w tej postaci do T-041 | P | 0,5 h |

| **T-052** — audyt fraz od nowa, plan treści na sezon | Wykonane 21.08. `docs/seo/T-052-AUDYT_FRAZ_I_PLAN_SEZON_2026-08-21.md`. **Zastępuje `docs/audits/KEYWORD_RESEARCH_2026-05-19.md`.** Trzy błędy poprzedniego audytu udokumentowane liczbami: **(1)** filtr regexowy (`wapn|kreda|tlenkow|…`, metodyka pkt 4) wyciął klaster glebowy — `ph gleby` 1 000, `badanie gleby` 1 000, `zakwaszenie gleby` 390, `odczyn gleby` 260, `analiza gleby` 260, `stacja chemiczno-rolnicza` 260, `jak podnieść ph gleby` 210, `próbki gleby` 170, razem **~3 640/mies. skasowane mechanicznie**, bo żadna z tych fraz nie zawiera słowa „wapno” ani „kreda”; to dokładnie ten klaster, na którym Polcalc ma 95% widoczności; **(2)** seedy nie pokrywały oferty — paszarstwo zmierzone w audycie na 150/mies. wobec **8 940** (×60), rybactwo 240 wobec **4 100** (×17), a klastry „pole/uprawa” (1 890), „termin zabiegu” (1 400) i „tonaż/luz/big-bag” (2 210) nie istniały w ogóle; **(3)** 82% zmierzonego wolumenu to drogownictwo (14 040 — AGRIA nie sprzedaje kruszyw) i budownictwo DIY (3 670 — segment wykluczony w Ads 13.08); na tej podstawie w raporcie czerwcowym wskazaliśmy klientowi wapno hydratyzowane jako największy potencjał. **Nowa mapa: 28 720 wyszukań/mies. realnego popytu, z czego 14 330 w klastrach o zerowym pokryciu.** Źródła: DataForSEO `keyword_suggestions` (2 080 unikalnych fraz z seedów wapno/wapnowanie/kreda), `google_ads/search_volume` (99 fraz hipotez z sezonowością 12 mies.), 8 SERP-ów `live/regular`, GSC 24.07–20.08, koszt ≈ 0,42 USD. **Korekta ADR 11.08:** reguła „jeden URL na intencję” zostaje dla fraz, na których już rankujemy; dla fraz z zerowym pokryciem nie ma zastosowania — nie ma czego kanibalizować | R | 3 h |
| **T-053** — Blok A: CTR klastra dawkowego | Wdrożone 21.08, zweryfikowane na żywym froncie z cache-bustem. **Baseline:** `/wapnowanie-gleby/` 14 227 wyświetleń → **69 kliknięć (CTR 0,49%)** przy pozycji 6,7; fraza „ile wapna na hektar” 1 219 wyświetleń → **1 kliknięcie**. Zmienione `rank_math_title` i `rank_math_description` na czterech adresach: **2074** `/wapnowanie-gleby/` → „Ile wapna na hektar? Tabela dawek i kalkulator”; **2741** `/ile-wapna-granulowanego-na-ha/` → tytuł skrócony 61 → 55 zn. (wychodził poza ucięcie w SERP); **2743** `/jak-stosowac-wapno-nawozowe/` → **przestawiony na intencję „kiedy wapnować pole”** (szczyt październikowy 590 + 260; `rank_math_focus_keyword` zmieniony) — świadomie zamiast tworzenia drugiego URL-a na tę frazę; **729** `/kalkulator-wapnowania/` → usunięte „ile wapna na hektar” z tytułu, bo dublowało hub na tej samej frazie. Wszystkie tytuły ≤57 zn., opisy ≤157 zn. Readback z produkcji: **4/4 nowe tytuły i opisy renderują się na froncie**. Backup wartości sprzed zmiany: `data/backups/T-052-blokA-meta-przed-2026-08-21.md`. **Dowodem domknięcia jest CTR w GSC po 14 dniach, nie sam zapis** — kontrola 04.09 | R | 1 h |

| **T-059** — ścieżka kontaktu na landingach Ads | Wdrożone 21.08, zweryfikowane na żywym froncie. **Stan przed:** pierwszy link `tel:` na obu landingach to ikonka słuchawki na **29–30% wysokości dokumentu**, numer jako tekst dopiero na **60%**, cena na **57%**; `phone_impressions` 14–20.08 to **62 przy 1 023 wyświetleniach reklamy**, `form_start` 1, `form_submit` 0. **Wdrożone cztery elementy:** (1) **blok kontaktowy w hero** obu landingów — cena „od …/t netto” plus przycisk „Zadzwoń: 664 393 062” i godziny pracy, wstawiony w miejsce dawnego linku tekstowego „Zapytaj o ofertę — podaj tonaż”; render potwierdzony **bezpośrednio pod H1, przed pierwszym H2**; (2) **nowy moduł `modules/call-bar/`** — pasek przyklejony do dołu ekranu z numerem i przyciskiem „Oddzwonimy”, wyłącznie na urządzeniach dotykowych (`max-width:1024px` + `pointer:coarse`), na landingach, kartach produktów i kategoriach; poza układem strony, `body{padding-bottom}` chroni przed zasłonięciem stopki, `@media print` go chowa; (3) **kotwica `#oddzwonimy`** i **formularz kontaktowy** na dole obu landingów (istniejący, przetestowany moduł `inquiry-form`, shortcode z własnym tytułem) — kampania chodzi 6–22 przez 7 dni, a telefon jest odbierany pn–pt 8–16, więc poza tym oknem musi być co kliknąć; (4) końcowe CTA przestawione z linku do `/kontakt/` na numer telefonu. **Weryfikacja:** obie strony 200, kotwica, formularz, blok hero i pasek obecne w renderze, **zero surowych shortcode’ów**; pasek pokazuje się na landingach, karcie `agrobielik-70` i kategorii, a **nie pokazuje** na `/wapnowanie-gleby/`, `/kontakt/` i stronie głównej — zgodnie z zakresem. Backupy: `~/agria-backups/post-2751-przed-T059-20260821.html`, `post-2757-…`, `agria-by-auranet.php.bak-20260821-123401`. Snapshot w repo: `src/plugins/agria-by-auranet/modules/call-bar/` | R | 2 h |
| **T-058 (część)** — Ads: wykluczenia obcych marek i stawka Brand | Wdrożone 21.08 przez Ads API v25. **26 wykluczeń** (dopasowanie do wyrażenia) na kampanii Rolnictwo: polcalc, orcal, morawica, morawicy, siewierz, unicalc, promyk, atrigran, radkowit, kujawit, jurak, dobromir, inovit, omya, dewonit, agrodol, agrolok, humicalc, complexor, magnesia calc, józefka, koszelowska, działoszyn, osadkowski, biovita, florovit. Razem na kampanii **85 wykluczeń** (było 59). **Dwie korekty wobec rekomendacji z 18.08:** (a) tamta lista zawierała `grankal`, `kornica`, `kornicki` i `drugnia` — to **producenci, od których AGRIA kupuje towar** (`FAKTY_KLIENTA` §4: Grankal 3 produkty, KZK Kornica 1, Kopalnia Drugnia 1); wykluczenie ich odcięłoby zapytania o własny asortyment, więc na listę nie weszły; (b) tamta rekomendacja szacowała stratę na **125 zł/mies. i zalecała zostawić „marka + cena”** — przeliczenie search terms z 14–20.08 daje **34 zł/mies.** na czyste zapytania katalogowe i **81 zł/mies.** na „marka + cena”. Wykluczyliśmy jedno i drugie: przy **90% udziału w wyświetleniach traconym przez budżet** na zapytaniach bezmarkowych każda złotówka wydana na cudzą markę to złotówka odjęta od `wapno granulowane cena`, gdzie jesteśmy naturalną odpowiedzią. Odzysk ≈ **115 zł/mies. ≈ 10% budżetu**. **Stawka grupy Brand 0,50 → 3,00 zł** — kampania Marka traciła >90% wyświetleń przez ranking przy 0% przez budżet, czyli przy 0,50 zł nie wchodziła do aukcji; 6 zł/dz (≈166 zł/mies. budżetu klienta) nie miało jak się wydać. Readback z API potwierdza obie zmiany | P | 1 h |

**Stan na 21.08: zamkniętych trzynaście pozycji** — dziewięć z pierwotnej listy „teraz" (T-048, T-008, T-009,
T-011, główna część T-010 — 15 kart z ceną — T-042, T-049, T-046 i T-041) plus **T-051**, **T-052**, **T-053** i **T-059**,
zgłoszone i domknięte tego samego dnia. W kolejce zostaje osiem: T-026 i T-027 (czeka wyłącznie na werdykt
Google), cztery bloki treści **T-054…T-057** oraz **T-058** (Ads, część wykonana 21.08). **Kanał OLX ruszył 20.08** — 200 ogłoszeń w emisji do 19.09; pakiet wygasa
16.09, więc **decyzja o odnowieniu pakietu musi zapaść przed 16.09**, inaczej `auto_extend` nie ma czego przedłużyć
i całość zgaśnie jednego dnia (tak zgasło 17 ogłoszeń 18.07). **T-006 i T-007 zdjęte z listy 20.08** (decyzja Janka /
wykonane przez Pawła). **Do końca M3 jedenaście dni.**

---

## Terminy najbliższe

| Kiedy | Co |
|---|---|
| **31.08** | Koniec M3. Raport miesięczny dla AGRII — punkt odniesienia `docs/raporty/DOWODY_M2_2026-07.md` |
| **31.08** | Rozliczenie pierwszego miesiąca budżetu Ads (wydane 199,62 zł z 1 200 zł na 19.08) |
| **01.09** | Przypomnienie kalendarzowe: menu — segmenty M4 |
| **wrzesień** | Drugi impuls sezonu — wapnowanie pożniwne. Szczyty: `wapno granulowane` 14 800/mies. w sierpniu, `wapno palone` 9 900 w październiku |

## Pytania do Pawła — wiedza klienta, nie nasza

Każde blokuje konkretną pozycję. Rozwinięcie: `docs/FAKTY_KLIENTA.md` → „Czego nie wiemy".
**Forma: telefon Janka, nie mail z tabelą** — memory `feedback_agria_pawel_relacja_telefoniczna`.

1. **Czy AGRIA jest autoryzowanym dystrybutorem Nordkalku?** → blokuje **T-040**.
2. **Czy budownictwo i drogownictwo to realne segmenty?** Oferta handlowa ich nie wymienia, katalog tak.
3. Zgoda na przywrócenie form dostawy jako atutu, nie MOQ → warunek części **T-037**.
4. Ceny dla czterech brakujących kart — Dolomit (302), Kreda czarna (303), Tlenkowe z Mg (313),
   Węglanowe odm. 05 (316). **Dolomit priorytetowo: 6 600 wyszukań/mies.** → rozszerza **T-010**.
5. Błędy w katalogu drukowanym do erraty: pH >16 przy wapnie palonym, kreda pastewna opisana
   parametrami wapna tlenkowego, „35 lat" zamiast 37.
6. Pozycja „Wapno hydratyzowane Bielik, worki 25 kg — 1245/SZT" — niemal na pewno literówka (12,45).

---

## Mapowanie starych ID → `T-NNN`

Dokumenty historyczne (audyty z maja i czerwca, `CATALOG_VS_WC_GAP.md`) zachowują stare oznaczenia —
to zapis stanu z tamtego dnia, nie żywy wskaźnik, nie przepisujemy ich.

`STR-01…09` → `T-001…T-009` · `CEN-01` → `T-010` · `CEN-02` → `T-011` ·
`P0-2a` → `T-012` · `P1-1` → `T-013` · `P1-2` → `T-014` · `P1-4` → `T-015` · `P1-5` → `T-016` ·
`P1-6` → `T-017` · `A1` → `T-018` · `A3` → `T-019` · `B1` → `T-020` · `B2` → `T-021` · `B6` → `T-022` ·
`B7` → `T-023` · `C1` → `T-024` · landingi Ads noindex → `T-025` ·
`P0-6` → `T-026` · `P0-6b` → `T-027` · `DUP-01` → `T-028` · `P1-7` → `T-029` · `P0-2b` → `T-030` ·
`P0-4` → `T-031` · `P0-3` → `T-032` · `P1-9` → `T-033` · `P0-5` → `T-034` ·
`C4–C7` → `T-035` · `E1–E3` → `T-036` · `D1–D4` → `T-037` · `HUB-VI` → `T-038` ·
`ADS-01` → `T-039` · `ADS-02` → `T-040` · `OLX-01` → `T-041` · `OLX-02` → `T-042` ·
`KAL-01` → `T-043` · `KAL-02` → `T-044` · `OFE-01` → `T-045` · `GBP-01` → `T-046` · `GBP-02` → `T-047` ·
`GEO-01` → `T-048`

## Czego ten rejestr nie zastępuje

- **`docs/FAKTY_KLIENTA.md`** — co wiemy o kliencie (produkty, producenci, ceny, ludzie, ustalenia).
  Rejestr mówi *co wisi*, FAKTY *jak jest*.
- **ADR w `docs/decyzje/`** — decyzje z uzasadnieniem. Rejestr je cytuje, nie powiela.
- **Git** — historia wykonania. Rejestr dokłada wymiar obowiązku, nie kopiuje commitów.
