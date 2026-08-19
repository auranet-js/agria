# Rejestr zobowiązań — AGRIA

> **Do czego to służy.** Git i dokumenty w `docs/` zapisują to, co **napisaliśmy**. Ten plik zapisuje
> to, co **zlecone i jeszcze niezamknięte** — jedyny wymiar, którego commit z natury nie niesie,
> bo commit opisuje wytworzony artefakt, a nie stan obowiązku.
>
> **Czytany obowiązkowo na starcie każdej sesji w tym repo** (patrz `CLAUDE.md` → „Jak pracować w tym repo").
> Zanim zaproponujesz cokolwiek nowego, sprawdź, czy nie stoi tu coś zleconego i niezrobionego.
>
> Stan na: **2026-08-19**. Weryfikacja: MCP `query_db`, `curl` na produkcji, GSC URL Inspection API,
> Google Ads API, PSI/CrUX — tego dnia, nie z dokumentów.

---

## Jak czytać

**Status:**

| Status | Znaczenie |
|---|---|
| ✅ **ZAMKNIĘTE** | wykonane i zweryfikowane na produkcji — kolumna „Dowód" mówi czym |
| 🔴 **OTWARTE — na nas** | zlecone, zaakceptowane, niewykonane; nic nie blokuje poza naszą kolejnością |
| 🟡 **OTWARTE — blokada** | czeka na dane, decyzję albo płatność po stronie AGRII |
| 🔵 **OTWARTE — do rozstrzygnięcia** | zakres miękki albo sprzeczny z późniejszą decyzją |
| ⚪ **PO STRONIE KLIENTA** | robi AGRIA, nie nasze zadanie — śledzimy, nie wykonujemy |
| ⛔ **UNIEWAŻNIONE** | późniejsza decyzja zdjęła to z zakresu — zostaje dla historii, **nie wykonywać** |

**Zakres (rozliczenie):**

| Znacznik | Znaczenie |
|---|---|
| **R** | ryczałt — mieści się w 2 000 zł netto/mies (umowa M1–M6, akcept 27.05.2026) |
| **P** | poza ryczałtem — osobna pozycja handlowa, kwota podana tam, gdzie udokumentowana |
| **W** | własne Auranet — nie fakturujemy AGRII na tym etapie |
| **K** | po stronie AGRII — ich koszt albo ich robota |

**Reguła aktualizacji:** commit, który zamyka pozycję, zmienia tu wiersz w tym samym commicie
i wpisuje swój hash do kolumny „Dowód". Wiersz bez dowodu nie ma prawa mieć statusu ✅.

---

## Linie usługowe — skrót

| # | Linia | Otwarte | Najstarsze otwarte | Zakres | Na kim |
|---|---|---|---|---|---|
| 1 | Strona — backlog Pawła (STR) | 4 | 15.06.2026 (STR-06) | R | Auranet / AGRIA |
| 2 | **Ceny i nagłówki cenowe** | 2 | 07.08.2026 | R | **Auranet** |
| 3 | SEO on-page i content (M1–M6) | 8 | 19.05.2026 (P0-4) | R | Auranet |
| 4 | Google Ads | 2 | 19.08.2026 | P — media 1 200 zł/mies | Auranet / AGRIA |
| 5 | OLX | 2 | 18.08.2026 | P — 1 800 setup + 300/mies | AGRIA / Auranet |
| 6 | Kalkulator wapnowania (moduł Mg) | 2 | 18.08.2026 | P — ≈4 h | Kazimierz → Auranet |
| 7 | Ofertownik | 1 | 18.08.2026 | W | Auranet |
| 8 | Wizytówki Google (GBP) | 2 | 15.07.2026 | R | Auranet / AGRIA |

**Razem otwartych: 23.** Z tego na nas bez żadnej blokady: **13**.

---

## 1. Strona — backlog poprawek Pawła

Źródło: `docs/operations/STRONA_BACKLOG_POPRAWKI.md`. Partia #1 — mail Pawła 15.06, partia #2 — mail 07.08.
Cała linia w ryczałcie (**R**).

| ID | Co zlecone | Zlecił / kiedy | Status | Dowód / blokada |
|---|---|---|---|---|
| STR-01 | Kalkulator bez kredy pastewnej i malarskiej | Paweł 15.06 | ✅ | wdrożone 18.06, `post__not_in [304,307]`, readback z serwera |
| STR-02 | Formy dostawy zdjęte ze specyfikacji 19 kart + FAQ | Paweł 15.06 | ✅ | wdrożone 29.06, commit `1cc6bd8`, 19/19 zweryfikowane |
| STR-03 | Telefony na mapie zgodne z oddziałami, `660` usunięty | Paweł 15.06 | ✅ | wdrożone 01.07, commit `1dfe5c5`, zero wystąpień `660` na froncie |
| STR-04 | Karty produktu i charakterystyki na `/do-pobrania/` | Paweł 15.06 | ✅ | wdrożone 29.06, 22 pozycje w sekcji, live-zweryfikowane |
| STR-05 | Zdjęcia produktów zgodne z katalogiem | Paweł 15.06 | ✅ | wdrożone 29.06 |
| STR-06 | Przebudowa sekcji „Dział sprzedaży" po odejściu P. Stanisława | Paweł 15.06 | 🟡 | **65 dni**. Blokada: aktualny skład działu (imiona, role, telefony) — pytanie do Pawła. Przy okazji: zepsuty `href` Kazimierza (`http://+48 781 875 411`) |
| STR-07 | Korekta interpunkcji w tekstach | Paweł 15.06 | ⚪ | robi Paweł, czekamy na finalny tekst |
| STR-08 | 8 nowych atestów + karty charakterystyki Nordkalk na `/do-pobrania/` | Paweł 07.08 | 🔴 | **12 dni**. Sprawdzone 19.08: strona ma **0 wystąpień „Sitkówka"** — nowych kart Nordkalku nie ma. Materiały w mailu [201] |
| STR-09 | Usunięcie całej sekcji „Certyfikaty" z `/do-pobrania/` | Paweł 07.08 | 🔴 | **12 dni**. Sprawdzone 19.08: **7 wystąpień „certyfikat"** — sekcja stoi, razem z duplikatem linku i literówkami „ertyfikat" |

**Uwaga:** STR-08 i STR-09 to jedna wizyta na tej samej stronie (ID 731, `_elementor_data`) — robi się je razem.
Do tego dochodzi P0-6b: `/do-pobrania/` trzeba zgłosić do ponownego crawlu, bo Google trzyma na niej werdykt z kwietnia (niżej).

---

## 2. Ceny i nagłówki cenowe na stronie — zakres **R**

**To jest pozycja, przez którą powstał ten rejestr.** Zlecenie kompletne, zaakceptowane dwustronnie,
rozpisane co do URL-a — i niewykonane.

| ID | Co zlecone | Zlecił / kiedy | Status | Dowód / blokada |
|---|---|---|---|---|
| CEN-01 | Widełki „od X zł/t netto" **w treści** 15 kart (H2 + akapit) + 2 landingi Ads + poradnik cenowy + link z huba | Paweł przysłał cennik 07.08; **mockup zaakceptowany przez Janka 13.08** | 🔴 | **12 dni od cennika, 6 od akceptu.** MCP 19.08: `19 produktów / 19 bez _price / 0 ze słowem „cena" w treści`. Rozpiska: `docs/operations/CEN_LISTA_URL_2026-08-13.md`, ceny: `CENNIK_PAWEL_2026-08-07.md` |
| CEN-02 | Nagłówki H2 z frazą cenową na kartach („wapno granulowane cena", „wapno nawozowe cena", „agrobielik cena") | Janek, ustnie, potwierdzone 19.08 | 🔴 | Sprawdzone 19.08: **0 z 19 kart** ma nagłówek cenowy. Prompt wykonawczy: `docs/prompty/2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md` |

**Koszt tego, że stoi — zmierzony, nie szacowany.** Kampania Rolnictwo wydała **199,62 zł w sześć dni**
(Ads API, 19.08) przy zerowej liczbie konwersji, a z diagnozy dnia 5 wynika, że **33% tego wydatku**
to zapytania cenowe (`wapno granulowane cena`, `ile kosztuje tona wapna granulowanego`,
`wapno nawozowe cena za tonę`) lądujące na stronach bez ceny. Klaster cenowy w organiku:
~1 320 wyszukiwań/mies., zerowa obecność AGRII.

**Ograniczenia twarde przy wykonaniu** (memory `project_agria_ceny_strategia`, `feedback_agria_bez_zargonu_loco`):
cena nigdy sama — zawsze z warunkiem dostawy, dwa punkty odniesienia na grupę; nigdy pełny cennik
i nigdy ceny za worek jako komunikat główny; nigdy progu ilościowego; zero żargonu („loco" zakazane);
adnotacja „ceny orientacyjne, nie stanowią oferty w rozumieniu KC"; pole edytowalne, żeby Paweł
zmieniał je w minuty.

**Sposób wykonania — rozstrzygnięty 19.08** (ADR `docs/decyzje/2026-08-19-dwie-warstwy-cen.md`,
memory `project_agria_dwie_warstwy_cen`):

- cena idzie **wyłącznie w treść** — `<h2>` z frazą cenową + akapit z widełkami i warunkiem dostawy;
- **`_price` w WooCommerce zostaje puste**, wariantów ani atrybutów cenowych nie tworzymy;
- **schema `Product`/`offers` budujemy ręcznie z treści**, nie z bazy. Karta emituje dziś `Product`
  z 18 `PropertyValue` i zerem `offers` (sprawdzone 19.08) — miejsce jest puste;
- **wyłącznie przeliczenia na tonę.** Ceny za sztukę worka nie idą na stronę (decyzja Janka 19.08,
  wobec zdania Pawła z 07.08: na ten moment nie będzie sprzedaży po worku);
- **OFE-01 nie jest warunkiem wstępnym** — powiązanie odpadło, bo CEN-01 nie dotyka struktury
  produktu. Ofertownik idzie osobnym wątkiem.

---

## 3. SEO on-page i content (M1–M6) — zakres **R**

Źródła: `docs/audits/ONPAGE_BACKLOG_M2-M6_2026-06-15.md`, `docs/seo/BACKLOG_SEZON_2026-07-14.md`,
`docs/audits/SEO_AUDIT_RESULTS.md`. **Kolumna „Dowód" to weryfikacja z 19.08, nie przepisany status
z dokumentu** — sześć pozycji miało w papierach „niezrobione", a są zrobione.

### Zamknięte (zweryfikowane 19.08)

| ID | Zadanie | Dowód z produkcji |
|---|---|---|
| P0-2a | Schema Organization zamiast „My Blog" | front: `"@type":"Organization"`, `"name":"AGRIA Sp. z o.o."` |
| P1-1 | Nagłówki bezpieczeństwa | `curl -I`: HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy (4 z 6 — brak CSP i Permissions-Policy) |
| P1-2 | Title strony głównej skrócony | 56 znaków, `rank_math_title` na ID 321 |
| P1-4 | `product_cat` w sitemapie | `product_cat-sitemap.xml` obecny w indeksie sitemap |
| P1-5 | SKU dla produktów | 18 z 19 ma `AGR-0xx`; #303 świadomie bez (decyzja katalogowa) |
| P1-6 | Literówki w nazwach produktów | `post_title`: „węglanowe", „zawierające" — poprawne w 19/19 |
| A1 | Sitemapa RankMath po migracji URL | `product-sitemap.xml` z aktualnymi adresami |
| A3 | `/cart/` poza sitemapą | `page-sitemap.xml`: 11 URL-i, `/cart/` nieobecny |
| B1 | Meta title + description na stronach statycznych | 6 z 6 (oferta, o-firmie, poradniki, kalkulator, do-pobrania, kontakt) |
| B2 | Bielik #309 on-page | `Wapno hydratyzowane Bielik CL 90-S \| CaO+MgO 90%` — parametry normowe z karty Nordkalk |
| B6 | pH wapna palonego („>16" było fizycznie niemożliwe) | render karty: `pH >12` |
| B7 | „35 lat" → „37 lat" | 0 wystąpień „35 lat" na `/`, `/o-firmie/`, `/oferta/` |
| C1 | Landing `/wapno-do-stabilizacji-gruntow/` | ID 2745, HTTP 200, w sitemapie |
| — | Landingi Ads poza indeksem | `/wapno-granulowane/`, `/wapno-nawozowe/`: HTTP 200, `noindex, follow` |
| — | Demo-produkt motywu z indeksu | `/produkt/organic-pineapple/` → HTTP 404 |

### Otwarte

| ID | Zadanie | Status | Dowód / blokada |
|---|---|---|---|
| **GEO-01** | **Geoblok odcina Lighthouse/PSI — nie da się mierzyć CWV** | 🔴 | **Znalezione 19.08.** PSI zwraca `NOT_HTML — served as MIME type text/plain`; geoblok (`security-geoblock.php`, wdrożony 14.08) przy odrzuceniu robi dokładnie `header('Content-Type: text/plain')` + `exit('Forbidden')`. Whitelist `$good_bots` ma Googlebota, AdsBota i Google-InspectionTool, **nie ma `Chrome-Lighthouse`** — a PSI fetchuje z USA. Fix: dopisać `Chrome-Lighthouse`, `Google-PageSpeed`, `GoogleOther` do listy. **Jedna linia, ale to zmiana na produkcji — czeka na zgodę** |
| P0-4 | **CWV mobile — LCP** | 🔴 | **Niemierzalne dziś obiema drogami:** PSI blokuje GEO-01, CrUX zwraca „data not found" (za mały ruch, żeby origin trafił do zbioru). Proxy z Elary 19.08: strona główna **TTFB 1,27 s przy cache-miss, HTML 154 KB**; karta produktu TTFB 0,35 s. Ostatni pełny pomiar 03.08: LCP 7,4 s. **Kolejność: GEO-01 → pomiar → dopiero optymalizacja** |
| P0-6 | **Indeksacja — sześć URL-i poza indeksem** | 🔴 | GSC URL Inspection 19.08. **„Adres URL jest Google nieznany" (4):** `/ile-wapna-granulowanego-na-ha/`, `/jak-stosowac-wapno-nawozowe/`, `/higienizacja-osadow-sciekowych-wapnem/`, `/kreda-malarska/`. **„Wykryta, niezindeksowana" (2):** `/wapno-nawozowe-na-trawnik/`, `/wapno-do-stabilizacji-gruntow/`. Mimo 3× Indexing API. Reszta portfela zdrowa — 11 URL-i PASS ze świeżym crawlem (09–18.08), hub `/wapnowanie-gleby/` crawl 15.08 |
| P0-6b | `/do-pobrania/` — werdykt z kwietnia | 🔴 | GSC 19.08: „Strona wykluczona za pomocą tagu **noindex**", `BLOCKED_BY_META_TAG`, **ostatni crawl 2026-04-12**. Live ma `index, follow` — Google po prostu nie wrócił. Zgłosić do reindeksacji razem ze STR-08/09 |
| P1-7 | **Login admina `js` eksponowany w schema** | 🔴 | Sprawdzone 19.08: front zwraca `"@type":"Person"`, `"name":"js"` ×2. Zgłoszone w audycie 15.06, otwarte **65 dni** |
| P0-2b | LocalBusiness ×2 (Niedomice, Radgoszcz) w schema | 🔴 | Front ma tylko `Organization`. Dane oddziałów mamy z STR-03 |
| DUP-01 | **15 opublikowanych `post_type=produkt` (ID 60–74)** równolegle do 19 produktów WC | 🔴 | **Znalezione 19.08, nieujęte w żadnym dokumencie.** `/produkt/agrobielik-70/` i `/produkt/dolomit/` → HTTP 200. Wcześniejsza notatka mówiła o trzech (67, 68, 69) — jest piętnaście. Do tego Agrobielik 70 pod dwoma adresami w WC, oba zbierają wyświetlenia w GSC |
| P0-3 | 301 dla `/kategoria-produktu/*` | 🔵 | Niezweryfikowane. Odblokowane od 18.08 (SSH + `.htaccess`) |
| P1-9 | Zgody / pomiar GA4 | 🔵 | **Korekta stanu wiedzy:** Complianz Privacy Suite premium **7.5.7.2 jest aktywny** i leci na froncie (95 wystąpień `cmplz`). Memory `project_agria_ga4_consent_blocker` i backlog on-page twierdzą, że CMP nie ma — **to nieprawda**. GA4 mimo to nie mierzy (5 sesji organicznych vs 221 kliknięć GSC w lipcu). Problem jest w konfiguracji zgód, nie w braku bannera — rediagnoza od zera |
| P0-5 | Premmerce DOM-XSS | 🔵 | Zainstalowana **2.3.13**, podatna była 2.3.11. Changelogu nie da się sprawdzić publicznie — wtyczki nie ma w repozytorium wp.org (`premmerce-permalink-manager` → „Plugin not found"). Do potwierdzenia u vendora albo z pliku `readme.txt` na serwerze |

### Unieważnione — nie wykonywać

| ID | Co | Czym unieważnione |
|---|---|---|
| C4–C7 | Landingi organiczne `/wapno-palone/`, `/wapno-magnezowe/`, `/wapno-hydratyzowane/`, `/kreda-nawozowa/` | ADR `2026-08-11-podzial-rol-ads-seo.md` + memory `project_agria_architektura_kanalow`: **landingi wyłącznie jako cele Ads, poza indeksem**. Powód zmierzony: 6 URL-i na frazę „wapno bielik" → pozycja 15,3; frazy z jednym URL-em w TOP10. Organik idzie treścią |
| E1–E3 | Landingi segmentowe `/wapno-do-stawow/`, `/wapno-do-sadu/`, hub Oczyszczalnie | jw. Menu (Sadownictwo/Rybactwo/Hurtownie) zdjęte 30.07 jako `draft`, wraca we wrześniu **razem z treścią**, nie z landingami — memory `project_agria_nav_debt_m4` |
| D1–D4 | `/transport-i-dostawa/`, sekcja B2B, formularz z tonażem, formy dostawy z powrotem na karty | częściowo sprzeczne ze STR-02 (Paweł kazał zdjąć formy dostawy). D4 wymaga jego zgody (F1) — bez niej nie ruszać |
| HUB-VI | Plan hub-and-spoke per segment z `CONTENT_AUDIT_2026-06-15.md` §3 (HUB Rolnictwo / Rybactwo / Oczyszczalnie) | jw. **Dokument nie ma o tym ani słowa** — to jest źródło powtarzających się propozycji „zróbmy huby". Oznaczony nagłówkiem statusu 19.08 |

---

## 4. Google Ads — zakres **P** (media 1 200 zł/mies)

Zobowiązanie: **3 miesiące kampanii**. ADR `2026-08-13-uruchomienie-kampanii-ads.md`. Konto 674-207-1446.

**Stan konta na żywo (Ads API, 19.08, ostatnie 14 dni):**

| Kampania | Status | Budżet | Wyświetlenia | Kliknięcia | Koszt | Konwersje |
|---|---|---|---|---|---|---|
| AGRIA - Rolnictwo | ENABLED | 34 zł/dz | 682 | 100 | **199,62 zł** | 0 |
| AGRIA - Marka | ENABLED | 6 zł/dz | **0** | **0** | **0,00 zł** | 0 |

| ID | Co | Status | Dowód / blokada |
|---|---|---|---|
| ADS-01 | Korekty na kampanii Marka: wykluczenia opakowaniowe, stawka Brand 0,50 → 3,00 zł, nowa grupa „Producent" | 🔴 | **Potwierdzone liczbami 19.08: Marka nie wydała ani grosza przez sześć dni emisji** — przy stawce 0,50 zł nie wchodzimy do aukcji. Rekomendacja czeka na „działaj", punkt decyzyjny 7–10 dni |
| ADS-02 | Teksty reklam z nazwą „Nordkalk" | 🟡 | **Blokada: status autoryzowanego dystrybutora.** Licytować na cudzy znak wolno zawsze, użyć w treści — tylko odsprzedawcy. **W repo tej informacji nie ma** (sprawdzone `grep` po `docs/` i memory) — pytanie do Pawła, nie zgadywać |
| — | Wiarygodność konwersji z połączeń | — | Zero konwersji przy 100 kliknięciach może być artefaktem pomiaru — zależy od P1-9. Nie optymalizować pod ten wskaźnik przed rediagnozą zgód |

**Rozjazd do rozstrzygnięcia:** memory `project_agria_ads_sezonowosc` sygnalizuje różnicę **trzy vs cztery miesiące**
kampanii między tym, co potwierdził Kasjan, a tym, co poszło w mailu. Do sprawdzenia przed rozliczeniem budżetu.

---

## 5. OLX — zakres **P** (1 800 zł netto setup + 300 zł/mies)

200 ogłoszeń, 12 pozycji asortymentowych, 53 miejscowości, 9 województw, publikacja przez Partner API.

| ID | Co | Status | Dowód / blokada |
|---|---|---|---|
| OLX-01 | Publikacja 200 ogłoszeń | 🟡 | Treści, siatka miast i spięcie z API gotowe. **Blokada: pakiet Premium 200 kupuje AGRIA** (1 199,99 zł brutto — zakres **K**) |
| OLX-02 | Naniesienie poprawek treści ustalonych z Kazimierzem mailowo 18.08 | 🔴 | Na nas, przed publikacją |

---

## 6. Kalkulator wapnowania — moduł magnezowy — zakres **P** (≈4 h)

| ID | Co | Status | Dowód / blokada |
|---|---|---|---|
| KAL-01 | Weryfikacja mockupu przez Kazimierza | 🟡 | `mockups/agria-kalkulator-mg-test-2026-08-18.html` przekazany 18.08 |
| KAL-02 | Wdrożenie modułu Mg na produkcję | 🔴 | Po weryfikacji. **4 kwestie otwarte** przed wdrożeniem — memory `project_agria_kalkulator_mg` |

---

## 7. Ofertownik — zakres **W** (własne Auranet)

**Nie jest pozycją billable dla AGRII na tym etapie** (decyzja Janka 18.08: najpierw budujemy, potem sprzedajemy).
Rozpiska klient-facing istnieje, ale **bez kwot** i nie idzie do klienta przed zbudowaniem.

| ID | Co | Status | Dowód / blokada |
|---|---|---|---|
| OFE-01 | Etap zerowy: audyt wycieku cen → konwersja jednego produktu na wariantowy → sprzątanie atrybutów → cennik | 🔴 | Niezaczęty, **osobny wątek** (rozdzielone od CEN-01 decyzją 19.08). Spec: `docs/specs/2026-08-18-ofertownik-design.md`. **Audyt wycieku cen to warunek bezpieczeństwa danych, nie porządki:** ceny wariantów WooCommerce są domyślnie widoczne na froncie, w REST API, w feedach i w schema Rank Matha, a ta warstwa ma pozostać **niejawna** |

---

## 8. Wizytówki Google (GBP) — zakres **R**

| ID | Co | Status | Dowód / blokada |
|---|---|---|---|
| GBP-01 | Optymalizacja profilu **Tarnów** (opis, kategorie, zdjęcia, publikacje) | 🔴 | Profil dostępny od 15.07, optymalizacja **obiecana klientowi na piśmie** w raporcie M2 jako zadanie sierpnia. Brak śladu wykonania. Do końca M3 zostało 12 dni |
| GBP-02 | Odzysk profili **Niedomice** i **Radgoszcz** | 🟡 | Dostępu nadal brak. Ścieżka: Request access z konta Auranet + weryfikacja własności firmy (KRS 0000170666, NIP 8730006657). **W komunikacji do klienta przemilczeć multi-location** dopóki brak dostępu |

---

## Terminy najbliższe

| Kiedy | Co |
|---|---|
| **31.08** | Koniec M3. Raport miesięczny dla AGRII — punkt odniesienia `docs/raporty/DOWODY_M2_2026-07.md` |
| **31.08** | Rozliczenie pierwszego miesiąca budżetu Ads (wydane 199,62 zł z 1 200 zł na 19.08) |
| **01.09** | Przypomnienie kalendarzowe: menu — segmenty M4 (`docs/przypomnienia/2026-09-01-menu-segmenty-m4.md`) |
| **wrzesień** | Drugi impuls sezonu — wapnowanie pożniwne. Szczyty: `wapno granulowane` 14 800/mies. w sierpniu, `wapno palone` 9 900 w październiku |

---

## Pytania do Pawła — wiedza klienta, nie nasza

Każde blokuje konkretną pozycję rejestru. Rozwinięcie: `docs/FAKTY_KLIENTA.md` → sekcja „Czego nie wiemy".

1. **Czy AGRIA jest autoryzowanym dystrybutorem Nordkalku?** → blokuje ADS-02.
2. **Aktualny skład działu sprzedaży** (imiona, role, telefony, segmenty) → blokuje STR-06, 65 dni.
3. **Czy budownictwo i drogownictwo to realne segmenty?** Oferta handlowa AGRII ich nie wymienia, katalog marketingowy tak.
4. Zgoda na przywrócenie form dostawy jako atutu, nie MOQ → warunek D4.
5. Błędy w katalogu drukowanym do erraty: pH >16 przy wapnie palonym, kreda pastewna opisana parametrami wapna tlenkowego, „35 lat" zamiast 37.
6. Pozycja „Wapno hydratyzowane Bielik, worki 25 kg — 1245/SZT" w ofercie handlowej — niemal na pewno literówka (12,45).

---

## Czego ten rejestr nie zastępuje

- **`docs/FAKTY_KLIENTA.md`** — co wiemy o kliencie (produkty, producenci, ceny, ludzie, ustalenia). Rejestr mówi *co wisi*, FAKTY *jak jest*.
- **`docs/PROJECT_STATE.md`** — stan wątków i kontekst „dlaczego tak".
- **ADR w `docs/decyzje/`** — decyzje z uzasadnieniem. Rejestr cytuje je w kolumnie „unieważnione czym", nie powiela.
- **Git** — historia wykonania. Rejestr dokłada wymiar obowiązku, nie kopiuje commitów.
