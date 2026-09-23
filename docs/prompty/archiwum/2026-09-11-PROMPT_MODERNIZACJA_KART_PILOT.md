# PROMPT — modernizacja treści kart produktów: research → pilot na 3 kartach → D1

> **Projekt:** `agria` · **Zlecił:** Jan Schenk, 11.09.2026 · **Rejestr:** T-136
> **Podstawa:** baza wiedzy produktowej (T-134, commity `3bd6f8b`, `b1dc7a6`) — `docs/produkty/`:
> 19 plików produktów, `README.md` (indeks), `_macierz-fraz.csv` (581 fraz), `_WNIOSKI.md` (fakty do D1–D4 + decyzje Janka 11.09).
> **Przeczytaj na starcie:** `CLAUDE.md`, `docs/produkty/_WNIOSKI.md` w całości, pliki trzech kart pilota, memory
> `feedback_agria_params_from_datasheets`, `feedback_agria_nazwy_producent_nie_marka`, `feedback_agria_architektura_wokol_kart`,
> `project_agria_render_caching`, `feedback_agria_landingi_wzorzec_nie_elementor`.

---

## 0. Po co ten wątek

Baza wiedzy pokazała, że **żadna z 19 kart na stronie nie jest w pełni zgodna ze swoją kartą PDF** — widoczna tabela i treść
to tekst n8n DescWriter z 13.03 z dopisanymi zastosowaniami i liczbami bez źródła. Jednocześnie **6 z 11 zapytań ofertowych
przyszło z kart** (zero z kategorii, huba i poradników), a na frazy producentów i kopalń serwis ma **0 wyświetleń**.

Kolejność ustalona przez Janka 11.09: **research → pilot na trzech kartach → akcept → pozostałe karty → decyzja D1 (kategorie)**.
Kategorii, adresów i reklam w tym wątku nie ruszasz, dopóki pilot nie zostanie zaakceptowany.

## 1. Decyzje, które obowiązują (nie wracaj do nich)

| decyzja | źródło |
|---|---|
| Źródło prawdy = karta AGRII PDF. **Tabela parametrów 1:1 z karty PDF**, nic nie przeliczasz, nie „poprawiasz" | memory, `[J 10.09]` |
| Treść opisowa, H2, FAQ, title, meta, cena w treści — **wolno zmieniać** | memory `feedback_agria_params_from_datasheets` |
| Twierdzenia spoza karty PDF (plony +15–30%, pH >12 tam, gdzie karta go nie ma, stawy/rekultywacja, ARiMR, 35/37 lat) = DescWriter, **usuwamy** | `[J 10.09]` |
| **Producent i kopalnia/zakład w treści — tak; marki producenta — nie** (Dewonit, Wapniak Kornicki, Grankal HumiPlus, Calcifertil, Bukowiak, Opolwiak, „Oxyfertil Ca 90") | `[J 11.09]` |
| Nordkalk wolno wymieniać — AGRIA jest autoryzowanym dystrybutorem | T-040, `[J 07.09]` |
| Rozbieżności karty PDF z atestami / dokumentami producentów — **bez zgłaszania**, parametry zostają (m.in. #307 „37% CaO", pH >12, egzotermia) | `[J 11.09]` |
| #303 i #316 zostają tak, jak są | `[J 11.09]` |
| **Reklamy stoją do końca pilota** (D2). Wstrzymanie na koncie robi Janek sam — **nie ruszasz Ads** | `[J 11.09]` |
| Zero nowych adresów, kategorii, landingów. Nazwy produktów z WC bez zmian | memory `feedback_agria_architektura_wokol_kart` |
| `_price` puste, ceny ofertownika nigdzie | ADR `2026-08-19-dwie-warstwy-cen` |

## 2. Etap 1 — research (tylko dla trzech kart pilota)

Karty: **#312 Oxyfertil 90** (38 klik. / 575 wyśw. w 90 dniach, 2 zapytania — najlepsza karta), **#315 Węglanowe bez Mg odm. 04**
(17 / 1 652 — widoczność bez kliknięć, 1 zapytanie), **#307 Kreda pastewna** (3 / 234, 149 klik. z Ads, popyt na drób ≈ 2 780/mies.
bez pokrycia). Trzy różne sytuacje — trzy miary.

Research ma odpowiedzieć na trzy pytania **na kartę**, nie więcej:
1. **Które frazy należą do tej karty** — z `_macierz-fraz.csv`: fraza → jeden nasz adres. Wypisz frazy, na które dziś pokazuje się
   inny nasz adres (hub, kategoria, inna karta), i zaznacz kolizje. Pomiar 04.09: fraza z 1 adresem śr. poz. 10,1, z 3+ adresami 22,5.
2. **Co Google nagradza na głównych frazach karty** — SERP mobile (`scripts/dfs_serp.py`, najpierw sprawdź `data/produkty/dfs/`
   i `data/seo/`), 3–5 fraz na kartę: typ stron w top 5, elementy, które mają (cena, producent, zakład, dokumenty, frakcje, FAQ),
   pytania PAA. **Limit DataForSEO na cały etap: 0,30 USD**, saldo przed i po.
3. **Czego szuka kupujący** — PAA, zapytania GSC karty (`scripts/gsc_baseline.py --dni 90`, pamiętaj o progu prywatności),
   treść zapytań ofertowych z tej karty (MCP `query_db`, tylko odczyt), Ads `search_term_view` dla #307.

Wynik: `docs/produkty/pilot/<slug>-research.md` — jedna strona na kartę. **Nie osobny audyt** — to, co już jest w pliku produktu,
cytujesz linkiem, nie przepisujesz.

## 3. Etap 2 — pilot: nowa treść trzech kart

Dla każdej karty jeden plik `docs/produkty/pilot/<slug>-tresc.md`:
- **frazy przypisane** do karty (z etapu 1) i hipoteza w jednym zdaniu: „po zmianie karta X zyska Y na frazach Z, kontrola <data +28 dni>";
- title (bez podwójnych liczb, różny od innych kart), meta description, lead;
- H2 i treść — **zastosowania i liczby wyłącznie z karty PDF i dokumentów producenta**; producent i zakład/kopalnia; porównanie
  z produktami AGRII tego samego rodzaju (`_WNIOSKI.md` §4.4 — fakty z kart i cennik, bez oceniania);
- **tabela „Specyfikacja techniczna" 1:1 z karty PDF** (dziś odbiega na każdej karcie — wraca do karty, łącznie z wierszem „Forma dostawy");
- cena w treści zgodnie z cennikiem (tylko pozycje z `CENNIK_PAWEL_2026-08-07.md`, np. worek #307 610 zł/t), zdanie o transporcie;
- FAQ z prawdziwych pytań (PAA, GSC, zapytania ofertowe) + `FAQPage` w schemacie;
- linki do karty PDF (i atestu, jeśli jest na `/do-pobrania/`);
- #307: gatunki (drób, bydło) **tylko w zakresie, który mówią karta i dokumenty producenta** — dawek per gatunek nie ma w żadnym źródle,
  więc ich nie wymyślasz (pytanie do Janka quizem).

**Pokaż Jankowi trzy pliki (link auratest + treść w czacie) i czekaj na akcept.** Dopiero po akcepcie wdrożenie.

### Wdrożenie (po akcepcie, zgoda Janka per operacja)
- backup (`db_export` / `backup_file`) przed zmianą;
- ⚠️ **warstwa renderu — sprawdź przed edycją, nie zakładaj.** Odczyt MCP 11.09: #312 i #315 mają tylko `post_content`;
  #307 ma `_elementor_data` (7 951 B) **bez** `_elementor_edit_mode = builder` (który mają #310 i #320); `CLAUDE.md` §4 pkt 2 wymienia
  307 wśród kart renderowanych z `_elementor_data`. Zanim przepiszesz treść, ustal warstwę: znajdź fragment tekstu, który jest tylko
  w jednym z dwóch pól, i sprawdź, czy widać go w renderze;
- po zmianie `wp elementor flush-css` + `wp cache flush` + cache-bust CDN; **weryfikacja renderem** (`scripts/produkty_render.py`
  i Chrome MCP), nie bazą;
- ręczne „Poproś o zindeksowanie" w GSC robi Janek (działa w minuty); Indexing API tylko przez `~/bin/index-submit`;
- baseline GSC 28 dni przed zmianą zapisany w `data/produkty/pilot/`; data kontroli w rejestrze.

## 4. Etap 3 — po akcepcie pilota

1. Pozostałe 16 kart według zaakceptowanego wzoru, w kolejności z `_WNIOSKI.md` §2.1 (najpierw te z ruchem lub zapytaniami).
2. **D1 — kategorie** quizem na faktach z `_WNIOSKI.md` §5 i wynikach pilota. Dopiero tu klasteryzacja SERP (porównanie wyników
   dla fraz rodzajowych: wapno granulowane, węglanowe, tlenkowe, magnezowe, nawozowe, kreda nawozowa) — z limitem DataForSEO
   ustalonym z Jankiem przed startem. D1 zmienia adresy (Premmerce) — żadnej zmiany bez zapisanego `[J]`.

## 5. Zauważone wcześniej, do decyzji Janka (nie rób bez polecenia)

- Stare adresy `/oferta/<segment>/<produkt>/` zwracają 404 (ok. 5 600 wyświetleń w 2026) — przekierowania 301 w `.htaccess` (diff → „ok").
- `/kreda-pastewna/` przekierowuje na kategorię `/paszarstwo/`, nie na kartę; Google pokazuje stary adres na `kreda pastewna` (poz. 21,7).
- Nowy adres #320 ma 0 wyświetleń, ruch idzie na stary `…-luz-24t/` (301) — ręczne zgłoszenie w GSC.
- `FAKTY_KLIENTA` §3 i T-094 mają nieaktualne zapisy (offers, indeks) — korekta przy okazji.
- T-135 (zdjęcie worka 30 kg jako główne na #307, propozycja Kazimierza) — pasuje do pilota #307; decyzja Janka.

## 6. Czego NIE robisz

- Nie zmieniasz parametrów, nazw produktów, adresów, kategorii, `_price`. Nie ruszasz Google Ads.
- Nie wysyłasz nic do klienta (tylko przez Janka, `~/bin/send-to-jan`).
- Nie robisz nowego audytu całego serwisu — research dotyczy trzech kart.
- Nie proponujesz architektury przed akceptem pilota.

## 7. Zrobione (etap 1 + 2) =

- `docs/produkty/pilot/<slug>-research.md` ×3 i `<slug>-tresc.md` ×3, wystawione na auratest i pokazane w czacie;
- akcept Janka zapisany `[J data]` w rejestrze (T-136);
- po wdrożeniu: render zgodny z plikiem treści (dowód: `produkty_render.py` przed/po), baseline i data kontroli w rejestrze;
- koszt DataForSEO podany.
