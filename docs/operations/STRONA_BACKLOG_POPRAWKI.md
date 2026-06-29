# Backlog poprawek strony agria.pl

> Żywy backlog poprawek zgłaszanych przez klienta (Paweł Bigos, AGRIA).
> Paweł dosyła kolejne partie — dokument otwarty, dopisujemy na bieżąco.
> Wdrożenie: **SSH / WP-CLI** na nazwa.pl (MCP Agria = read-only, nie do zapisu).
> Status na: 2026-06-29. Źródło partii #1: mail Pawła z 2026-06-15 20:30 (fwd Janka, [73]).

---

## Legenda statusów

- 🟢 **GOTOWE DO WDROŻENIA** — zakres jasny, technicznie zlokalizowane, czeka tylko na realizację
- 🟡 **CZEKA NA MATERIAŁY** — bloker po stronie klienta (pliki, dane)
- 🔵 **WYMAGA KONCEPCJI / DANYCH** — zakres miękki, do ustalenia
- ⚪ **PO STRONIE KLIENTA** — robi Paweł, nie nasze zadanie
- ✅ **WDROŻONE**

**Decyzja Janka 2026-06-16:** na teraz tylko spisanie backlogu — **zero wdrożeń na produkcji** do osobnego startu (zbliża się urlop Janka).

---

## Partia #1 — mail Pawła 2026-06-15

### STR-01 · Kalkulator wapnowania — usunąć kredę pastewną i malarską ✅
**Zgłoszenie:** „kalkulator wapnowania — usunąć z niego kredę pastewną i kredę malarską."
**Lokalizacja:** plugin `agria-by-auranet` → `modules/liming-calculator/includes/class-product-matcher.php`, metoda `query_agriculture_products()`. Kalkulator NIE ma listy na sztywno — ciąga produkty z segmentu `pa_agria-segment` (rolnictwo/sadownictwo) mające `pa_min-cao > 0`. Kreda malarska (#304) i pastewna (#307) mają przypisany segment `rolnictwo` + CaO (53/37), stąd wpadały.
**WDROŻONE 2026-06-18 (Claude, FTP):** dodane `'post__not_in' => [ 304, 307 ]` w WP_Query kalkulatora — chirurgiczne wykluczenie, dotyka TYLKO kalkulatora (listingi kategorii bez zmian). `php -l` OK, readback z serwera identyczny. Backup: `~/backups/agria/2026-06-18/class-product-matcher.php.bak`.

### STR-02 · Formy dostawy z PIM — usunąć spod specyfikacji technicznej ✅
**Zgłoszenie:** „usunąłbym też wszędzie spod specyfikacji technicznej formy dostawy z PIMu, które nanosiliśmy — czasami nawet małe ilości możemy wysyłać, a taki zapis nas ogranicza."
**Zakres (potwierdzony Janek 2026-06-16 + 2026-06-29):** zdjąć formy dostawy ze **wszystkich** kart + wyczyścić FAQ z konkretnych form/MOQ (zostawić dawkowanie).
**Stan faktyczny (odkryty 2026-06-29):** „formy dostawy" to NIE atrybut/template, lecz **zahardkodowany HTML w `post_content`** każdego produktu — (a) wiersz „Forma dostawy" w tabeli specyfikacji, (b) osobna sekcja „Dostępne formy dostawy" (SKU/opakowanie/waga/MOQ), (c) odpowiedzi FAQ o formach/opakowaniach/MOQ.
**WDROŻONE 2026-06-29 (Claude, MCP write):**
- Dobudowany zapis do MCP przez `mcp-ext.php` (mechanizm rozszerzeń) + wdrożony właściwy build `mcp.php` v2.0.1 przez FTP (stary nie miał hooka). Nowe narzędzia: `update_post_content`, `query_db_write` (guardy: tylko UPDATE/INSERT, WHERE wymagane). Backup żywego mcp.php + treści 19 produktów w scratchpad.
- 19/19: usunięty wiersz „Forma dostawy" + sekcja „Dostępne formy dostawy" (#313 sekcji nie miał). FAQ: odpowiedź o formie zastąpiona ogólnym, elastycznym przekazem („różne formy, od mniejszych ilości po całopojazdowe, cały rok, własna logistyka, kontakt z handlowcem"); usunięta klauzula „od 3 do 24 ton". Dawkowanie nietknięte.
- Weryfikacja na produkcji: 0 wierszy/sekcji/klauzul, tagi tabel zbalansowane, każdy zapis match=True (readback).
- **Poza zakresem (zostaje):** wzmianki o formach w treści wstępnej/bulletach (np. „elastyczne formy dostawy (big-bag, worki, luz)") — to copy marketingowe, nie PIM ani FAQ.

### STR-03 · Mapa w Kontakcie — telefony zsynchronizować z oddziałami pod mapą 🟢🔵
**Zgłoszenie:** „nanieść na mapie w kontaktach telefony — takie same jak przy oddziałach (poniżej mapy)."
**Lokalizacja:** strona *Kontakt* (post ID 323), custom JS Google Maps (`agria-map`), tablica `var locations[]` z polami `phone` / `phoneFull` w infowindow markerów.
**Stan obecny na mapie:** Tarnów `14 621 88 21`, Radgoszcz `14 641 43 01`, Niedomice `604 428 782`.
**Problem:** rozjazd z numerami w kartach oddziałów pod mapą (na stronie widoczne też `660 76 86 91`, `664 393 062`). Paweł chce ujednolicić mapę do numerów spod mapy.
**Do zrobienia:** zaktualizować `phone`/`phoneFull` w `locations[]` tak, by zgadzały się z kartami oddziałów.
**Bloker — DANE:** potrzebny **właściwy numer per oddział** (zwł. siedziba Tarnów — centrala `14 621 88 21` czy komórka handlowca?). Ustalić z Pawłem przed edycją.

### STR-04 · Sekcja „do pobrania" — karty produktu + karty charakterystyki 🟡🔵
**Zgłoszenie (2026-06-15):** „do pobrania — nanieść wszystkie nowe karty produktu oraz karty charakterystyki."
**Doprecyzowanie (2026-06-29):** Paweł wrzucił na Google Drive pojedyncze PDF-y stron katalogu (`\AGRIA\Katalog\Pojedyncze\Agria-katalog-2026-05-13`). Zadanie: zmienić im nazwy, dodać sekcję w „do pobrania" i wstawić w „Karty produktu" na https://agria.pl/do-pobrania/. **Przeanalizować wszystkie obecne pliki przed zmianą** — część „kart produktu" to pliki dostawców, niektóre to faktycznie karty charakterystyki.

**ANALIZA OBECNEGO STANU `/do-pobrania/` (strona ID 731, Elementor, 4 sekcje = icon-list; wykonana 2026-06-29):**
- **Karty produktu (6 poz.):** 5 to prawdziwe karty produktu Trzuskawica/Kujawy (palone w bryłach, palone kruszone, hydratyzowane CL 90-S, nawozowe odm. 02, odm. 03 — potwierdzone `pdftotext`). **Poz. 2 BŁĘDNA:** tekst „Wapno budowlane CL 90-Q (palone mielone)", ale link → `karta-charakterystyki-diwodorotlenek-wapnia-cl-90-s.pdf` = **karta CHARAKTERYSTYKI złego produktu** (hydratyzowane CL 90-S, nie palone mielone), w dodatku PDF bez warstwy tekstowej (skan). Ten sam plik już poprawnie siedzi w sekcji obok. Czyli: brak prawdziwej karty produktu dla „palone mielone", a wstawiono zły plik.
- **Karty charakterystyki (4 poz.):** tlenek wapnia CL 90-Q, tlenek wapnia Kujawy (oba MSDS Trzuskawica, OK), diwodorotlenek CL 90-S (skan, OK), wapno nawozowe odm. 03 (skan).
- **Certyfikaty (5 poz.):** poz. 1 i 2 mają RÓŻNY opis, ale TEN SAM link (`ertyfikat-zgodnosci-we-cem-ii-b-v-32-5-r-ozarow.pdf`) — duplikat linku do naprawy. Literówki w nazwach plików („ertyfikat" bez „c").
- **Atesty i opinie (1 poz.):** atest OSChR wapno nawozowe odm. 01.

**WDROŻONE 2026-06-29 (Claude):**
- Dostęp do Drive przez **Google Drive API (OAuth `~/secrets/google/tokens.json`, scope `drive.readonly`)** — NIE connector claude.ai (ten w Claude Code nieautoryzowany). 17 PDF-ów pobrane z folderu (Drive id `15KU4uyOdi5GAONCm8x62t9liB6F9DJsv`).
- Przemianowane wg `agria-karta-produktu-<produkt>.pdf`, wgrane FTP do `wp-content/uploads/2026/06/`. Każdy zmapowany do produktu (Agrobielik 70/90 0-3 i 2-8mm/Oxyfertil 90/tlenkowe z Mg/mieszanka/węglanowe ×6/kredy ×3/dolomit/hydratyzowane Bielik/palone mielone).
- Strona 731 (`_elementor_data`, przez nowe `update_postmeta`): 17 kart AGRIA dodanych do **jednej istniejącej listy „Karty produktu"** (bez osobnego nagłówka — pierwotnie dodałem pod-blok „linia AGRIA", Janek odrzucił, scalone do jednej listy = 5 dostawcy + 17 AGRIA = 22 poz.); usunięta błędna poz. (palone mielone → link do karty charakterystyki diwodorotlenku). Wyczyszczony `_elementor_element_cache` (inaczej maskował zmiany).
- Live-zweryfikowane: 22 karty w sekcji Karty produktu, brak nagłówka „linia AGRIA"; diwodorotlenek tylko w „Karty charakterystyki".
**Pozostaje (poza zakresem zgłoszenia, do decyzji):** duplikat linku w „Certyfikaty" (poz.1=2); ew. uzupełnienie brakujących kart (303 kreda czarna, 304 kreda malarska, 316 węglanowe odm.05 — brak w katalogu); odświeżenie meta SEO/og strony (auto-RankMath).
**Uwaga infra:** CDN nazwa.pl — przy weryfikacji zawsze cache-bust; element-cache Elementora czyścić po każdej zmianie `_elementor_data`/`post_content` na stronach budowanych w Elementorze (produkty 310, 320 mają treść w widgecie text-editor, NIE w post_content).

### STR-05 · Zdjęcia produktów — ujednolicić wg katalogu ✅
**Zgłoszenie:** „zmienić zdjęcia produktów — obecnie są pomieszane. Zdjęcia powinny być takie, jak dawaliśmy do katalogu produktów, materiały będziesz miał na whatsappie."
**WDROŻONE 2026-06-29:** zdjęcia produktów podmienione na zgodne z katalogiem drukowanym. Zamknięte po stronie Auranet.

### STR-06 · Sekcja „Dział sprzedaży" — przebudowa po odejściu P. Stanisława 🔵
**Zgłoszenie:** „zastanowiłbym się, czy nie zmienić sekcji Dział sprzedaży — jakoś inaczej ją ułożyć albo coś dodać, bo po usunięciu P. Stanisława mam wrażenie, że czegoś tam brakuje."
**Do zrobienia:** propozycja nowego układu sekcji Dział sprzedaży (strona Kontakt) — uzupełnić tak, by nie sprawiała wrażenia niekompletnej.
**Bloker — DANE + KONCEPCJA:** aktualny skład działu (kto został, imiona/role/telefony/segmenty obsługi). Po zebraniu danych — przygotujemy 1 propozycję układu do akceptu (bez agencyjnych frameworków — ustalenie z Pawłem telefonicznie / przez Janka).

### STR-07 · Tekst strony — korekta interpunkcji ⚪
**Zgłoszenie:** „tekst poprawiłem, ale i tak muszę go jeszcze sprawdzić pod kątem interpunkcji itp."
**Status:** robi Paweł sam. Czekamy aż przekaże finalny tekst — wtedy ewentualnie naniesiemy.

---

## Wątki poboczne (nie-stronowe, do śledzenia)

- **Wizytówka Google (GBP):** Paweł nie kojarzy maila o wizytówce — zadzwoni do P. Stanisława, dopyta czy to kontakt poprzedniego operatora. Jeśli nie — odzysk przez pomoc Google. *Nasza rola:* wsparcie przy odzysku dostępu, gdy Paweł da znać.

---

## Czego potrzebujemy od Pawła (zbiorczo — bloker-dane)

1. Karty produktu + karty charakterystyki (PDF) — STR-04
2. Właściwe telefony per oddział (zwł. siedziba Tarnów) — STR-03
3. Aktualny skład działu sprzedaży po P. Stanisławie — STR-06

---

## Następny krok (po starcie wdrożeń)

Kolejność wg gotowości: **STR-01 ✅ → STR-05 ✅ → STR-02** (odblokowane, czysto techniczne, SSH/WP-CLI) → **STR-03** (po dosłaniu numerów) → STR-04 (po materiałach) → STR-06 (po danych) → STR-07 (po finalnym tekście Pawła).
Przed edycją plików produkcyjnych: `mysqldump` + backup plików do `~/backups/agria/<data>/` (reguła globalna).
