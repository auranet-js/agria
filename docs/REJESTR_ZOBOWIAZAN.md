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
> Stan na **2026-08-19**. Weryfikacja tego dnia: MCP `query_db`, `curl` na produkcji,
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

## 🔴 Teraz — 7 pozycji, nic ich nie blokuje

| ID | Zadanie | Linia | Zakr. | Dowód / kontekst |
|---|---|---|---|---|
| **T-010** | **Widełki „od X zł/t netto"** — pozostały **landingi Ads (2), poradnik cenowy, link z huba** `[P 07.08]` | Ceny | R | **Karty zrobione 19.08 15:35 — 15/19 ma cenę w treści** (było 0/19), `_price` nadal puste w 19/19, Store API zwraca wyłącznie `"price":"0"`. Zasada cenowa ustalona 19.08: **cena wiodąca = najtańsza dostępna forma hurtowa** (luz tam, gdzie jest; big-bag przy granulatach; worki przy kredzie malarskiej, która luzem nie występuje), worki wyłącznie **w zł/t, nigdy w zł/szt.** Cztery karty bez wyceny Pawła nietknięte (Dolomit, Kreda czarna, Tlenkowe z Mg, Węglanowe odm. 05). Rozpiska: `docs/operations/CEN_LISTA_URL_2026-08-13.md`. **Do zrobienia: `/wapno-granulowane/` i `/wapno-nawozowe/` (treść + `noindex, follow`), poradnik `/ile-kosztuje-wapnowanie-hektara/`, link kontekstowy z `/wapnowanie-gleby/`** |
| **T-027** | `/do-pobrania/` — zgłoszenie do reindeksacji | SEO | R | **Zgłoszone 19.08 15:16 UTC** przez `~/bin/index-submit` (1 URL, `OK`, zużycie 1/100; log `~/.claude/indexing-submit.log`). Strona zgłoszona **już po** T-008 i T-009. Stan przed: `BLOCKED_BY_META_TAG`, ostatni crawl 2026-04-12, live `index, follow`. **Dowodem domknięcia jest zmiana werdyktu GSC, nie zgłoszenie** — recheck 22.08 (+72 h) i 02.09 (+14 dni) |
| **T-028** | **15 opublikowanych `post_type=produkt` (ID 60–74)** równolegle do 19 produktów WC `[A 19.08]` | SEO | R | **Znalezione 19.08, nieujęte w żadnym dokumencie.** `/produkt/agrobielik-70/` i `/produkt/dolomit/` → HTTP 200. Wcześniejsza notatka mówiła o trzech (67, 68, 69) — jest piętnaście. Agrobielik 70 pod dwoma adresami, oba zbierają wyświetlenia w GSC |
| **T-026** | Indeksacja — sześć URL-i poza indeksem | SEO | R | GSC 19.08. **„Google nieznany" (4):** `/ile-wapna-granulowanego-na-ha/`, `/jak-stosowac-wapno-nawozowe/`, `/higienizacja-osadow-sciekowych-wapnem/`, `/kreda-malarska/`. **„Wykryta, niezindeksowana" (2):** `/wapno-nawozowe-na-trawnik/`, `/wapno-do-stabilizacji-gruntow/`. Mimo 3× Indexing API. Reszta portfela zdrowa — 11 URL-i PASS ze świeżym crawlem |
| **T-039** | Korekty kampanii Marka: wykluczenia opakowaniowe, stawka Brand 0,50 → 3,00 zł, grupa „Producent" `[A]` | Ads | P | **Marka nie wydała ani grosza przez sześć dni emisji** (Ads API 19.08) — przy 0,50 zł nie wchodzimy do aukcji. Rekomendacja czeka na „działaj", punkt decyzyjny 7–10 dni |
| **T-042** | Poprawki treści ogłoszeń ustalone z Kazimierzem `[K mail 18.08]` | OLX | P | Na nas, przed publikacją |
| **T-046** | Optymalizacja profilu GBP **Tarnów** (opis, kategorie, zdjęcia, publikacje) | GBP | R | Profil dostępny od 15.07, optymalizacja **obiecana klientowi na piśmie** w raporcie M2 jako zadanie sierpnia. Brak śladu wykonania. **Do końca M3 zostało 12 dni** |

## 🟡 Czeka na AGRIĘ

| ID | Zadanie | Czeka od | Na co konkretnie |
|---|---|---|---|
| **T-006** | Przebudowa sekcji „Dział sprzedaży" po odejściu P. Stanisława `[P 15.06]` | **65 dni** | aktualny skład działu — imiona, role, telefony, segmenty. Przy okazji: zepsuty `href` Kazimierza (`http://+48 781 875 411`) |
| **T-040** | Teksty reklam z nazwą „Nordkalk" `[A]` | 19.08 | **status autoryzowanego dystrybutora.** Licytować na cudzy znak wolno zawsze, użyć w treści — tylko odsprzedawcy. W repo tej informacji nie ma (sprawdzone `grep` po `docs/` i memory) — **nie zgadywać** |
| **T-041** | Publikacja 200 ogłoszeń OLX | 18.08 | **pakiet Premium 200 kupuje AGRIA** (1 199,99 zł brutto, zakres **K**). Treści, siatka 53 miejscowości i spięcie z Partner API gotowe |
| **T-043** | Weryfikacja mockupu kalkulatora Mg przez Kazimierza | 18.08 | `mockups/agria-kalkulator-mg-test-2026-08-18.html` przekazany 18.08 |
| **T-047** | Odzysk profili GBP **Niedomice** i **Radgoszcz** | 15.07 | dostęp. Ścieżka: Request access z konta Auranet + weryfikacja własności (KRS 0000170666, NIP 8730006657). **W komunikacji do klienta przemilczeć multi-location**, dopóki brak dostępu |
| **T-007** | Korekta interpunkcji w tekstach `[P 15.06]` | 15.06 | finalny tekst — ⚪ robi Paweł sam |

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
| **T-010 (część: 15 kart)** + **T-011** — widełki cenowe i nagłówki H2 z frazą cenową | Wdrożone 19.08 15:35. **15/15 kart ma na froncie `<h2>` z frazą cenową i akapit z widełkami** (weryfikacja `curl` per URL). `_price` puste w **19/19**, Store API `"price":"0"` — warstwa ofertownika nietknięta. Schema bez `Offer`. Jeden `<h1>` na kartę. Cztery karty bez wyceny nietknięte (0 wystąpień „zł/t netto", HTTP 200). Trzy karty renderujące z Elementora (307, 310, 320) zmienione **w obu warstwach**. Render potwierdzony Chrome MCP na `/wapno-nawozowe-rolnictwo/agrobielik-70/`: blok stoi między specyfikacją a FAQ. Backup: `agria-backups/przed-T-010-20260819-153153.sql` | R | 3 h |
| **T-029** — login administratora przestał wyciekać (3 kanały) | Wdrożone 19.08 17:39. Audyt 15.06 wskazywał schema; zmierzone 19.08 kanały były **trzy**. **(1) Schema:** `display_name`/`user_nicename` użytkownika 1 → „AGRIA Sp. z o.o." / `agria`; **login `js` niezmieniony** (to pole logowania). Front: **0 wystąpień `"name":"js"`** na `/`, `/o-firmie/`, `/kontakt/`, `/do-pobrania/`, `/wapnowanie-gleby/` (było na każdej). **(2) Enumeracja:** Rank Math `disable_author_archives=on` → `/?author=1` i `/?author=2` dają **301 na stronę główną** (było 301 na `/author/js/`). **(3) REST:** nowy moduł `security-user-enum.php` (filtr `rest_pre_dispatch`) → `/wp-json/wp/v2/users` i `/users/1` zwracają **401** dla anonima. Role sprawdzone przez `rest_do_request`: administrator 200, redaktor 200, anonim 401 — pierwsza wersja filtra odcinała redaktora (403), warunek poprawiony z `list_users` na `edit_posts`. `/wp-json/`, `/wp/v2/posts`, Store API i wszystkie strony nadal 200. Backupy: `agria-by-auranet.php.bak-20260819-173923`, opcje Rank Math w `agria-backups/rankmath-titles-przed-T029.json` | R | 1,5 h |
| **T-032** — 301 dla starej bazy `/kategoria-produktu/*` | Wdrożone 19.08 17:45 przez FTP. **Sześć reguł jawnych** w bloku `# BEGIN AGRIA 301` — po jednej na kategorię z `product_cat-sitemap.xml` plus sam prefiks. Reguła generyczna świadomie odrzucona: zamieniałaby natychmiastowe 404 nieistniejących adresów na 301 prowadzące do 404. Wynik: **5/5 kategorii → 301 na czysty URL**, czyste URL-e nadal 200, `/kategoria-produktu/` → `/oferta/`, `/kategoria-produktu/nieistnieje/` → **404** (bez zmian), pętli brak (2 skoki). **Reguły z lipca nietknięte** (`/wapno-nawozowe-hurt/`, `/wapno-do-sadu/`, `/kreda-pastewna/`, przekierowania produktowe — sprawdzone). Panel 302, `wp-login` 200, `/wp-json/` 200, Store API 200, `wp-cron` 200, siedem kluczowych stron 200, trzy sitemapy 200. **Kontekst:** GSC za 90 dni pokazuje dla `/kategoria-produktu/*` **zero wyświetleń** — canonical działał, więc 301 zamyka furtkę na przyszłość, nie odzyskuje ruchu. Kopia: `agria-backups/htaccess-przed-T032-*.txt`, snapshot w repo `src/htaccess/` | R | 1 h |

**Stan na 19.08 wieczorem: z trzynastu pozycji „teraz" zamkniętych jest pięć** (T-048, T-008,
T-009, T-011 i główna część T-010 — 15 kart z ceną). W kolejce zostaje dziewięć, w tym T-027
czekające wyłącznie na werdykt Google. **Do końca M3 dwanaście dni.**

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
2. **Aktualny skład działu sprzedaży** (imiona, role, telefony, segmenty) → blokuje **T-006**, 65 dni.
3. **Czy budownictwo i drogownictwo to realne segmenty?** Oferta handlowa ich nie wymienia, katalog tak.
4. Zgoda na przywrócenie form dostawy jako atutu, nie MOQ → warunek części **T-037**.
5. Ceny dla czterech brakujących kart — Dolomit (302), Kreda czarna (303), Tlenkowe z Mg (313),
   Węglanowe odm. 05 (316). **Dolomit priorytetowo: 6 600 wyszukań/mies.** → rozszerza **T-010**.
6. Błędy w katalogu drukowanym do erraty: pH >16 przy wapnie palonym, kreda pastewna opisana
   parametrami wapna tlenkowego, „35 lat" zamiast 37.
7. Pozycja „Wapno hydratyzowane Bielik, worki 25 kg — 1245/SZT" — niemal na pewno literówka (12,45).

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
