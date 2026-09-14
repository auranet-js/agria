# PROMPT — T-136 „modernizacja treści kart”: domknięcie pilota i pozostałe karty wzorem v2

> **Projekt:** `agria` · **Rejestr:** T-136 · **Stan zweryfikowany:** 14.09.2026 (produkcja, render, GSC — dowody w §1)
> **Poprzedni prompt:** `docs/prompty/2026-09-11-PROMPT_MODERNIZACJA_KART_PILOT.md` — jego §1 (decyzje) i §6 (czego nie robisz) **obowiązują dalej**.
> **Przeczytaj na starcie:** `CLAUDE.md`, `docs/produkty/_WNIOSKI.md` (§2.1, §4.4, §5, decyzje `[J 11.09]`),
> **wzór v2:** `docs/produkty/pilot/oxyfertil-90-tresc.md` i `weglanowe-odmiana-04-tresc.md`, wiersz T-136 w `docs/REJESTR_ZOBOWIAZAN.md`.
> Memory: `feedback_agria_edycja_link_akcept_gsc`, `feedback_agria_zero_cen_w_title`, `feedback_agria_params_from_datasheets`,
> `feedback_agria_nazwy_producent_nie_marka`, `feedback_agria_prefer_mcp_curl_allowlisted` (SSH pierwszy), `project_agria_render_caching`.

---

## 0. Gdzie jesteśmy

Pilot na trzech kartach wszedł na produkcję 11.09 (v1), a dwie z nich tego samego wieczoru dostały wersję v2 —
**v2 jest wzorem dla pozostałych kart**. Zostaje: akcept #315 v2, #307 v2, 14 kart, potem D1 (kategorie).
Reklamy stoją do końca modernizacji kart (D2, `[J 11.09]`), więc tempo tego wątku przekłada się wprost na powrót Ads.

## 1. Stan kart pilota — zweryfikowany 14.09

| karta | na produkcji | schemat | Google | akcept |
|---|---|---|---|---|
| **#312 Oxyfertil 90** | **v2** — `post_content` = `data/produkty/pilot/wdrozenie-v2/oxyfertil-90-post_content.html` (md5 zgodne) | `Product` z nazwą WC + `FAQPage` 7 pytań | crawl **14.09 01:09**, PASS, bez błędów (tylko ostrzeżenia) | ✅ `[J 11.09]`, zgłoszone w GSC 11.09 |
| **#315 węglanowe odm. 04** | **v2** — `…/wdrozenie-v2/weglanowe-odmiana-04-post_content.html` (md5 zgodne), wgrane 11.09 ok. 19:10 | `Product` + `FAQPage` 9 pytań; ID 315 **jest** w `AGRIA_KARTY_SCHEMA_V2` | crawl **12.09 04:42** (po zmianie), PASS | ⏳ **brak zapisanego akceptu** — pierwszy krok wątku |
| **#307 kreda pastewna** | **v1** — `data/produkty/pilot/wdrozenie/kreda-pastewna-post_content.html` (md5 zgodne) | `Product` bez `FAQPage`, nazwa w schemacie = tytuł SEO | crawl 11.09, PASS | v1 ✅; **v2 nie zaczęte** |

Odczyt: SSH `wp post get` + md5 wobec plików, render `curl` z cache-bustem (typy JSON-LD, H2), GSC URL Inspection API.
Błąd „Opisy produktów: 1 nieprawidłowy element” z 11.09 **zniknął** — dziś same ostrzeżenia (`aggregateRating`, `review`, GTIN,
`shippingDetails`, `hasMerchantReturnPolicy`, `validFrom`); tych pól nie uzupełniamy, bo wymagałyby danych, których AGRIA nie ma.
**Kontrola pilota: 09.10** — GSC 28 dni wobec `data/produkty/pilot/gsc-karty-28d-2026-09-11.json` (#312 15/313, #315 12/1 212, #307 2/203).

## 2. Start wątku — najpierw to, w tej kolejności

1. **Link do #315 v2 do akceptu** (`https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/`). Po akcepcie wpis `[J data]`
   w T-136. Zgłoszenia w GSC nie powtarzaj — Google pobrał wersję v2 12.09.
2. **Quiz (`AskUserQuestion`, maks. 3 pytania, rekomendacja pierwsza):**
   - **#307 v2:** czy Kazimierz odpowiedział na pytanie o dawki i frakcje per gatunek (treść pytania: `kreda-pastewna-tresc.md` na końcu)?
     Warianty: odpowiedział (Janek podaje) · jeszcze nie — robimy v2 z jedną dawką z karty · wstrzymać #307. Przy tym **T-135**
     (zdjęcie worka 30 kg jako główne — propozycja Kazimierza): tak / nie / po odpowiedzi.
   - **Kolejność 14 kart:** wg ruchu i zapytań (`_WNIOSKI.md` §2.1) · **najpierw dwie granulowane #314 i #317** (T-117 —
     `wapno granulowane` X 8 100, karty mają 849 i 399 wyświetleń przy 0–2 kliknięciach, szczyt za 2–3 tygodnie).
     Przy tym: **czy T-116 i T-117 wchodzą do T-136** (te same karty, te same pola — rekomendacja: tak, jeden wiersz mniej).
   - **Tryb:** karta po karcie (wdrożenie → link → akcept → GSC, rekomendacja) · najpierw pliki MD kilku kart do przeczytania, potem seria.
3. Zgoda na zapis do produkcji dla serii kart (CLAUDE.md §5) — jedno „ok” na tryb z quizu, nie na każde polecenie.

## 3. Wzór v2 — co ma karta po modernizacji

Na podstawie #312 i #315 (zaakceptowanego #312). Plik `docs/produkty/<etap>/<slug>-tresc.md` ma te sekcje, bo czyta je
`scripts/karta_tresc_do_html.py`:

- **§1 frazy przypisane i hipoteza** — jedna fraza = jeden nasz adres (`_macierz-fraz.csv`, kolizje z hubem/kategorią/inną kartą
  zaznaczone); hipoteza „po zmianie karta X zyska Y na Z, kontrola <data +28 dni>”.
- **§1a mapa fraza → miejsce na karcie** (title / H1 / H2 / FAQ / lead / meta) — to jest rdzeń v2: każda fraza z popytem ma swoje miejsce.
- **§2 meta** — title **bez ceny** (krytyczne), różny od innych kart, bez podwójnych liczb; meta description (cena dozwolona
  pod warunkiem aktualizacji w 3 miejscach, `FAKTY_KLIENTA` §7); focus keyword.
- **§3 lead** → `post_excerpt`.
- **§4 treść** → `post_content`: H2 niosące frazy („<produkt> — zastosowanie i dawkowanie”, „— cena…”, porównanie „X czy Y?”);
  zastosowania i liczby **wyłącznie z karty PDF i dokumentów producenta**; producent i kopalnia/zakład, **bez marek producenta**;
  porównanie z produktami AGRII tego samego rodzaju (`_WNIOSKI.md` §4.4, fakty bez oceniania); **tabela „Specyfikacja techniczna”
  1:1 z karty PDF** łącznie z wierszem „Forma dostawy” (bez MOQ i „minimum”); sekcja ceny z `CENNIK_PAWEL_2026-08-07.md` + zdanie
  o transporcie („cena za towar, bez transportu” — zero żargonu); linki do karty PDF i atestu z `/do-pobrania/`;
  **FAQ 7–9 pytań** z PAA, GSC i zapytań ofertowych (H3 + odpowiedź — z nich powstaje `FAQPage`).
- Końcówkę od „Zapytaj o ofertę” skrypt przenosi 1:1 ze stanu przed zmianą; kotwice „Na skróty” zostają.
- Brak dawki / ceny w źródle = nie wymyślasz; pytanie do Janka quizem.

## 4. Cykl jednej karty

1. **Research** (1 strona, `<slug>-research.md`): frazy karty z macierzy, SERP mobile 3–5 fraz (`scripts/dfs_serp.py`, najpierw
   `data/produkty/dfs/`), PAA, GSC 90 dni (`scripts/gsc_baseline.py --dni 90`, próg prywatności — CTR licz z poziomu strony),
   zapytania ofertowe z tej karty (MCP `query_db`, odczyt). Plik produktu w `docs/produkty/` cytujesz linkiem, nie przepisujesz.
   **DataForSEO: limit 0,30 USD na cały etap 14 kart** (pilot kosztował 0,011 USD za trzy), saldo przed i po.
2. **Treść** `<slug>-tresc.md` wg §3.
3. **Stan przed:** zrzut `post_content`, `post_excerpt`, `rank_math_title`, `rank_math_description`, `rank_math_focus_keyword`
   do `data/produkty/<etap>/backup/przed-<data>.json` (format jak `data/produkty/pilot/backup/przed-wdrozeniem-2026-09-11.json`)
   + baseline GSC 28 dni do `data/produkty/<etap>/`. Przed większą serią `db_export` tabel postów i meta.
4. **HTML:** `python3 scripts/karta_tresc_do_html.py <ID> <tresc.md> <backup.json> <katalog_wyjścia>`.
5. **Warstwa renderu — sprawdź, nie zakładaj** (`_elementor_data` bez `_elementor_edit_mode` = render z `post_content`, jak #307;
   z `builder` — jak #310 i #320 — edycja `post_content` nic nie zmieni). Fragment tekstu tylko w jednym polu → czy jest w renderze.
6. **Wdrożenie przez SSH** (polecenie zaczyna się od `ssh agria-prod` / `scp`, bez pętli i `cd` przed nim):
   `scp` plików do `~/agria-backups/t136-<etap>/` → `wp eval-file wdroz-karta.php <id> <slug> <długość_obecnej_treści>`
   (guard długości, kopia „przed” obok — wzór `data/produkty/pilot/wdrozenie-v2/wdroz-karta.php`) → meta przez `wp post meta update`
   → **dopisz ID do `AGRIA_KARTY_SCHEMA_V2`** w `wp-content/plugins/agria-by-auranet/modules/seo-head/seo-head.php`
   (kopia pliku do `~/agria-backups/`, `php -l`) → `wp cache flush` + `rocket_clean_post` + cache-bust CDN.
7. **Weryfikacja renderem:** `scripts/produkty_render.py <slug> <ścieżka>` przed/po + `curl` z `?cb=`: title, H2, tabela 1:1 z PDF,
   `FAQPage` z liczbą pytań = liczba H3 w FAQ, `Product.name` = nazwa WC, stare twierdzenia DescWritera 0 trafień; telefon 390 px.
8. **Link do karty w czacie → akcept → zgłoszenie w GSC przez Chrome MCP** („Poproś o zindeksowanie”, potwierdzenie komunikatem).
9. **Rejestr w tym samym commicie:** wiersz T-136 (karta, `[J data]` akceptu, data kontroli +28 dni), wpis w dzienniku M4.

## 5. Kolejka 14 kart (#303 i #316 zostają bez zmian — `[J 11.09]`)

Wg `_WNIOSKI.md` §2.1 (klik / wyśw. 90 dni, zapytania): #309 Bielik 16/621, 2 · #319 węglanowe z Mg odm. 05 13/573, 1 ·
#310 Agrobielik 70 11/237 · #304 kreda malarska 6/284 (brak karty PDF — tylko to, co potwierdzone) · #305 kreda granulowana 5/363, 1 ·
#313 tlenkowe z Mg 2/420 (brak ceny) · **#314 węglanowe granulowane 2/849** · #306 kreda sypka 2/82 · **#317 węglanowe z Mg granulowane
0/399** (title identyczny z #318) · #308 mieszanka 0/2 · #311 Agrobielik 90 · #318 węglanowe z Mg odm. 04 · #302 dolomit
(karta PDF i sekcja ceny opisują dwa różne towary — do quizu) · #320 wapno palone mielone (**render z `_elementor_data`**, ruch
na starym adresie `…-luz-24t/`).
Rozbieżności kart PDF z atestami (#311, #318, #319, #320) — **bez zgłaszania**, tabela z karty PDF.

## 6. Po kartach

**D1 — kategorie** quizem na faktach z `_WNIOSKI.md` §5 i wynikach kontroli 09.10. Dopiero wtedy klasteryzacja SERP fraz rodzajowych,
z limitem DataForSEO ustalonym z Jankiem. Zmiana adresów (Premmerce) = 301 + ponowne zgłoszenia w GSC, tylko z zapisanym `[J]`.

## 7. Czego NIE robisz

- Parametrów, nazw produktów WC, adresów, kategorii, `_price` — nie ruszasz. Cen ofertownika nigdzie.
- **Google Ads nie ruszasz** — wstrzymanie robi Janek. (14.09 odczyt API: wszystkie trzy kampanie nadal ENABLED i emitują —
  jeśli dalej tak jest, powiedz to Jankowi jednym zdaniem, nie zmieniaj.)
- Nie wysyłasz nic do klienta. Pytania do Kazimierza/Pawła idą przez Janka, najpierw quizem do niego.
- Nie budujesz landingów, hubów ani nowych stron; nie robisz audytu całego serwisu.
- Nie skanujesz roadmapy przy okazji — przyległe rzeczy jedną linią „Zauważone obok, nie ruszam”.

## 8. Zrobione =

- #315 v2 z zapisanym akceptem; #307 v2 wdrożone albo świadomie wstrzymane decyzją Janka;
- każda z 14 kart: research + treść w repo, render zgodny z plikiem (dowód przed/po), ID w `AGRIA_KARTY_SCHEMA_V2`, akcept `[J]`,
  zgłoszenie w GSC, baseline i data kontroli w rejestrze;
- koszt DataForSEO podany; commit per karta lub per seria, rejestr w tym samym commicie.
