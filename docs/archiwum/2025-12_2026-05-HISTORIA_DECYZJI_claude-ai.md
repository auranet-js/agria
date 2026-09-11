> **Źródło:** Google Drive `AGRIA/Archiwum/AGRIA_HISTORIA_DECYZJI.md` (+ ten sam tekst w `AGRIA_decisions_split.zip`), wgrane przez Janka 10.09.2026.
> Zestawienie z 28 wątków Claude.ai — źródło **wtórne**; linki do wątków działają tylko z konta Janka na claude.ai.
> Konwencja statusów w dokumencie: `DECYZJA` = ustalił Janek lub klient, `REKOMENDACJA` = propozycja Claude bez potwierdzenia.

# AGRIA — historia decyzji i ustaleń projektu (22.12.2025 – 19.05.2026)

> Dokument zbiorczy do zasilenia repo / Claude Code. Zebrany z 28 wątków projektu „Agria" w Claude.ai oraz ze skilli `agria-katalog` i `agria-katalog-indesign`.
> Data zestawienia: 10.09.2026. Stan faktyczny opisany na dzień ostatniego wątku (19.05.2026) — wszystko późniejsze trzeba zweryfikować przez MCP `Agria.pl`.

## 0. Konwencje dokumentu

- **Data** = dzień wątku, w którym zapadła decyzja (data ostatniej aktywności wątku).
- **Status:** ✅ wdrożone / zatwierdzone · 🟡 w toku / częściowo · ⏳ zaplanowane · ❌ odrzucone lub zastąpione · ⚠️ niespójność do wyjaśnienia.
- **Typ:** `DECYZJA` (ustalił Janek lub klient) · `WDROŻENIE` (zrobione technicznie) · `REKOMENDACJA` (propozycja Claude, bez potwierdzenia) · `FAKT` (dane firmowe / techniczne).
- Sekrety (klucze reCAPTCHA, Google Maps API, FTP, credentials n8n) **celowo pominięte** — są w historii czatów, nie przenosić do repo.
- Link do wątku źródłowego podany przy każdej sekcji; pełny indeks w sekcji 14.

---

## 1. Oś czasu (chronologicznie)

| Data | Obszar | Zdarzenie / decyzja | Status |
|---|---|---|---|
| 2025-12-22 | Strategia | Strategia marketingowa v2.1 (3 fazy, 4 segmenty, budżet 53,3–71,3 tys. PLN/rok). DOCX nie wyszedł — dostarczono PDF (pandoc). | ✅ |
| 2026-01-15 | Brand | Stopka HTML v1 (Arial, kolor logo `#009140`, link RODO). | ✅ |
| 2026-01-20 | Brand | Stopki HTML v2 — tabela 460 px, style inline, logo `logo-podpis-email.png`, RODO → `https://agria.pl/rodo/`. Zestaw dla kilku osób. | ✅ |
| 2026-01-22 | Brand | Tagline: odrzucone hasła o tradycji/standardzie („AGRIA nie jest znanym brandem"). Kierunek: hasło mówi, co sprzedajemy i dla kogo. | ✅ |
| 2026-02-05 | PIM | PIM v1.0 wysłany klientowi do akceptacji (28 SKU / 19 produktów bazowych / 42 kolumny). Zdjęcia po stronie Auranet do 14.02. Koncepcja: każda strona katalogu = samodzielna ulotka. | ✅ |
| 2026-02-05 | Katalog | Plik `KATALOG_AGRIA_24STR_KOMPLET.txt` (v1.0, Montserrat, `#1B4D3E`/`#9ACD32`) — później zastąpiony. | ❌ zastąpiony |
| 2026-02-20 | Strona | Analiza PIM 2026-02-20. Debata WC vs CPT+ACF; plan URL; „budujemy od nowa, ma być lepiej niż było". Pierwszy generator InDesign (JSX) — bug podwójnego przeliczania mm. | 🟡 → zastąpione 27.02 |
| 2026-02-27 | Strona | **Finalnie WooCommerce w trybie katalogu.** Model: 1 PROD-ID = 1 produkt `simple`, warianty jako meta JSON `_agria_variants`. Atrybuty z prefiksem `agria-`. Wtyczka modułowa **Agria by Auranet** (moduł `catalog-mode`). Repo + GitHub Actions FTP deploy na `agria.auratest.pl`. | ✅ |
| 2026-03-13 | n8n / SEO | Adaptacja workflow DescWriter z LAGUZ na AGRIA (Gemini, tagi `content-write`→`content-done`, Rank Math). Kotwice H2, CTA „Zapytaj o ofertę, zamów próbkę", fix Rank Math focus keyword, podział opisu na sekcje meta + szablon Elementor z Dynamic Tags. | ✅ |
| 2026-03-20 | Formularz | Moduł `inquiry-form` (oferta/próbka), shortcode `[agria_inquiry_form]`, CPT zgłoszeń, autoresponder, reCAPTCHA v3. | ✅ |
| 2026-03-20 | Kalkulator | Moduł `liming-calculator`, shortcode `[agria_kalkulator_wapnowania]`, metodyka IUNG-PIB 2022, AJAX, pole areału, tekst SEO nad kalkulatorem. | ✅ |
| 2026-03-24 | Strona | Layout archiwum bloga (Elementor), mapa 3 lokalizacji (Google Maps JS w Custom HTML), typografia RWD, stopka mobile. | ✅ |
| 2026-03-27 | Strona | **Go-live:** przeniesienie z `agria.auratest.pl` na `agria.pl` (nazwa.pl). Nowe klucze reCAPTCHA (Elementor + wtyczka). Fix menu admina wtyczki (Agria → Ustawienia). | ✅ |
| 2026-04-07 | Katalog | Start makiety w InDesign. Paleta WWW, fonty PJS 600 + Bai Jamjuree 300. Szablon ręczny = karta Dolomitu (str. 1), kolejne karty przez JSX duplikujący stronę. Utworzony skill `agria-katalog`. | ✅ |
| 2026-04-08 | Katalog | Każdy produkt z WC = osobna karta (koniec kart zbiorczych). Zakaz wycinania pH z tabeli. Linki WP+frontend po każdej karcie. | ✅ |
| 2026-04-10 | Katalog | Nazwy 1:1 z WC (2 dopuszczalne normalizacje, >50 znaków → pytać klienta). `descHead` ≠ `sectionHead`. Zakaz `\ri`. Konwencja nazw plików JSX. | ✅ |
| 2026-04-13 | Katalog | 18 kart kompletnych + review IDML. Piktogramy segmentów (solid, siatka 48, `#0D9247`). Okładka zdefiniowana. | ✅ |
| 2026-04-15 | Katalog | Str. 2 (o firmie), str. 3 (segmenty/oferta), str. 22–24 (warunki, kontakt, tył). Review całości, poprawki krytyczne. Mail do **Kasjana (nowy właściciel AGRIA)** z projektem 24 str. do wydruku i uwag. | ✅ |
| 2026-05-04 | Katalog | Plik `Agria-katalog-2026-05-04-web.pdf` — wersja po korektach (skład produktów zmieniony vs 15.04, patrz sekcja 9.9). | ✅ |
| 2026-05-18 | Druk | Ulotka DL dwustronna gotowa (`AGRIA---Ulotka-DL-2026-05-18-2-front/back.jpg`). Wycena druku 200/500/1000 szt. z narzutem 30%. | ✅ |
| 2026-05-19 | Oferta / SEO | Zielone światło (wstępne) na retainer **2000 PLN netto/mies.** (12–15 h). Audyt SEO na koszt Auranet → oferta 6 mies. Przeniesienie projektu do Claude Code (repo `auranet-js/agria`). | 🟡 |

---

## 2. Strategia, marka, dane firmowe

Źródła: [f83131b3](https://claude.ai/chat/f83131b3-7cb2-4ade-88d5-4f17a65fcf0a) (2025-12-22), [5a4ece51](https://claude.ai/chat/5a4ece51-21b7-4e47-be0d-8ea699407f38) (2025-12-22), [b84ebb27](https://claude.ai/chat/b84ebb27-5a2c-4a38-8f8e-368a19cd967b) (2026-01-22), [d4edd311](https://claude.ai/chat/d4edd311-52f9-4f3a-976b-31a06e024f34) (2026-01-15), [52e1f212](https://claude.ai/chat/52e1f212-e45e-4907-8f16-f3d565706032) (2026-01-20), [f97f1795](https://claude.ai/chat/f97f1795-79ac-4338-bb2c-350ef4dddfcb) (2026-03-24), pliki projektu.

### 2.1 Strategia marketingowa (v2.1, 22.12.2025) — `DECYZJA` do zatwierdzenia przez Zarząd

- Cel 12 mies.: infrastruktura marketingowo‑sprzedażowa + rozpoznawalność Agria/Agrobielik ogólnopolsko.
- Trzy fazy: I — budowa (identyfikacja, strona, materiały), II — aktywacja (Google Ads, SEO, content), III — skalowanie (optymalizacja CPL, remarketing, FB/LinkedIn, targi Agrotech/Polagra).
- Segmenty strategiczne: **A** duże gospodarstwa 50+ ha (priorytet), **B** oczyszczalnie (priorytet), **C** rybactwo, **D** hurtownie/dystrybutorzy.
- Google Ads (plan): Rolnicy 1 500, Stawy 1 000, Oczyszczalnie 500 PLN/mies. = 3 000 PLN/mies.
- KPI rok 1: 2 000+ sesji/mies., 30+ leadów/mies., CPL < 150 PLN, 30+ fraz TOP 10, 5+ nowych oczyszczalni, +15–20% sprzedaży całopojazdowej.
- Budżet rok 1: 53 300–71 300 PLN (śr. 4,4–5,9 tys./mies.).
- Pozyskiwanie oczyszczalni: baza 40–50 (Wielkopolska → Łódzkie → Mazowieckie), pitch PDF 3–4 str., sekwencja telefon→mail→follow-up→wizyta, monitoring `baza.zamowien.gov.pl`, pierwsza dostawa referencyjna ze zniżką 20–30%.
- ⚠️ Dokument datowany „grudzień 2025", ale harmonogram w treści używa dat 2025 (Q1–Q4 2025). Realnie dotyczy 2026.
- ⚠️ Faza „budowy" wykonana innymi drogami niż w planie (np. katalog 24 str. zamiast testowego 4–6 str., brak dedykowanych landing pages do 19.05).
- Master prompt (plik projektu): zamknięty zakres produktowy, ton „Fractional CMO firmy tradycyjnej", zero lifestyle, decyzje GO/NO-GO, zawsze priorytet + pierwszy krok + ryzyko.

### 2.2 Tagline i hasła

| Data | Hasło / ustalenie | Użycie | Status |
|---|---|---|---|
| 2026-01-22 | Kierunek: hasło ma mówić „co sprzedajemy", nie „tradycja/standard" (klient nieznany rynkowi). | zasada | ✅ DECYZJA |
| 2026-01-22 | „Parametry, na których możesz polegać." (propozycja) | tył okładki w specyfikacji z 05.02, mockup str. 24 (15.04) | 🟡 |
| 2026-02-05 → 04-13 | „Surowce wapniowe i mineralne. Stabilne parametry. Pewne dostawy." | okładka katalogu | ✅ |
| 2026-04-15 | „Stabilne parametry. Pewne plony." (rekomendacja na tył okładki — rym z okładką) | tył okładki katalogu | ✅ w katalogu, ⚠️ review 15.04 wskazał niespójność „dostawy" vs „plony" — decyzja klienta |
| 2026-04-15 | Nagłówek str. 2: **„Wapno to nasza specjalność. Trzy pokolenia w branży."** Podpis: **„Zarząd AGRIA Sp. z o.o."** | katalog str. 2 | ✅ DECYZJA |

### 2.3 Identyfikacja wizualna

- Paleta obowiązująca (Elementor Global Colors na agria.pl; potwierdzona 07.04 dla katalogu): `#354E33` główny, `#61CE70` akcent, `#798D7A` drugorzędny, `#596A5A` tekst, `#F8FBF3` tło. CMYK w `design-spec.md`.
- Paleta z pliku 24STR (`#1B4D3E`, `#9ACD32`) — **wycofana** (07.04).
- Kolory logo/znaku: `#009140` (logo, stopki 15.01, CSS kalkulatora), `#0D9247` (piktogramy segmentów). ⚠️ dwa różne zielone „firmowe" — do ujednolicenia.
- Fonty: nagłówki **Plus Jakarta Sans SemiBold 600**, tekst **Bai Jamjuree Light 300** (web i druk). Montserrat — wycofany.
- Typografia RWD (24.03, Plus Jakarta Sans): H1 48/36/28 px, H2 36/28/24, H3 28/24/20, H4 22/20/18, body 17/16/15 (desktop/tablet/mobile); line-height nagłówki 1,2–1,3, body 1,6–1,7.
- Stopki mailowe: Arial 14/12 px, tabela 460 px, style inline, telefony i agria.pl klikalne, link RODO. Osoby w stopkach: Stanisław Latowski (Biuro Zarządu, Centrala Tarnów), Kazimierz Nowak (Kierownik Oddziału Radgoszcz) + inne.

### 2.4 Dane firmowe (`FAKT`)

- AGRIA Sp. z o.o., KRS 0000170666, NIP 8730006657, REGON 001405704, kapitał 58 250 zł, SR Kraków XII Wydz. Gosp.
- Centrala: Tarnów, 33-100. ⚠️ Adres: w wątku mapy (24.03) **ul. Warsztatowa 5**, w stopkach (15.01, 20.01) **ul. Warszawska 5** — zweryfikować u klienta.
- Oddział Radgoszcz: ul. Witosa 12, 33-207 Radgoszcz, tel./fax 14 641 43 01.
- Oddział Niedomice: ul. Fabryczna 17, 33-132 Niedomice, tel. 604 428 782.
- Telefony centrali: 14 621 88 21, 14 621 88 22, 14 621 79 02, 660 768 691; e-mail biuro@agria.pl.
- ⚠️ Numer „główny" niespójny między materiałami: katalog 24STR/strona 2 → 660 768 691; stopki kart katalogu → +48 14 621 88 21 (na str. 22–23 literówka „…88 210"); katalog web 05.2026 i ulotka → 604 428 782 wg analizy z 19.05. Ustalić jeden numer B2B.
- Właściciel: **Kasjan** (nowy właściciel, komunikacja na „Ty", krótkie maile — 15.04). Zmiana pokoleniowa w zarządzie (strategia).
- Od 1989 r. Marki: **Agrobielik** (wapno tlenkowe), **Bielik** (hydratyzowane).

### 2.5 Producenci i magazyny źródłowe (`FAKT`, z katalogu 05.2026 wg analizy 19.05)

- Producenci/dostawcy: Nordkalk (Sitkówka), Lhoist, Trzuskawica (Oxyfertil 90 wg kart), Industria / Świętokrzyska Grupa Przemysłowa (Jażwica, Laskowa, Winna), Celiny / Hochel Group, Grankal, KZK Kornica, Siarkopol (Dolomit, Tarnobrzeg), Kopalnia Drugnia (Pierzchnica), Cement Ożarów (CRH) i Kopalnia Morawica (logotypy).
- Magazyny wysyłkowe (poza 2 oddziałami): Niedomice, Sitkówka, Tarnów Opolski, Górażdże, Częstochowa, Draby, Celiny, Bukowa, Chęciny, Łagów, Kostomłoty Drugie, Pierzchnica, Kornica, Tarnobrzeg.
- ⚠️ Review 15.04: pole „Magazyn" na kartach sugeruje 12 oddziałów AGRIA — rekomendacja: etykieta „Źródło / lokalizacja producenta" albo dopisek na str. 2 o dostawach bezpośrednio z kopalń partnerskich.
- 🟡 Rekomendacja 19.05: sieć magazynów to USP (dowóz z najbliższego źródła) — do strategii i SEO lokalnego.

---

## 3. PIM i dane produktowe

Źródła: [51905cde](https://claude.ai/chat/51905cde-c1f1-4fb7-a150-77f18e8f3216) (2026-02-05), [92a69da9](https://claude.ai/chat/92a69da9-f6c3-4944-96a8-69b2c481e966) (2026-02-20), [156d7f51](https://claude.ai/chat/156d7f51-4b7a-4692-97ac-127381a913d2) (2026-02-27), [84232c51](https://claude.ai/chat/84232c51-3eb2-4885-b6ee-01cb07082f77) (2026-03-13).

- 2026-02-05 `DECYZJA`: PIM v1.0 (Excel) do akceptacji klienta; 1 wiersz = 1 SKU; ceny do użytku wewnętrznego (mogą służyć handlowcom); kolumny zdjęć/PDF = nazwy przyszłych plików. Po akceptacji — PIM online na Google Drive dla handlowców.
- 2026-02-20 `FAKT`: PIM `AGRIA_PIM_2026-02-20` (Google Sheets `1WY01OGv1Z9bZTfH-Sn9BoG4Ar27JAp2Q1nwqaf6TNsQ`), ok. 54–59 SKU, 15–17 produktów bazowych, 42 kolumny; 94% bez danych SEO, 100% bez zdjęć (stan 13.03).
- 2026-02-20 `DECYZJA`: ceny poza zakresem strony; warianty (forma dostawy × magazyn) tylko informacyjnie (tabela „dostępny w magazynach") i jako dane dla kalkulatorów/porównywarek.
- 2026-02-27 `WDROŻENIE`: poprawki danych przy imporcie v6: `egotermiczna`→`Egzotermiczna`, `Długodziałająca(bezpieczna)`→ze spacją, frakcje `0,1-04mm`→`0,1-0,4mm` itd., segmenty ujednolicone (`małe oczyszczalnie`/`Oczyszczalnie duże`→`Oczyszczalnie`, `stawy rybackie`→`Rybactwo`, `Budownictwo detaliczne`→`Budownictwo`), pole pH z błędną datą `2026-08-10` (31 SKU) pominięte, lokalizacje znormalizowane.
- 2026-03-13 `DECYZJA`: baza wiedzy dla n8n = PIM + dane produktów WC (bez osobnej bazy). Kategorie/obszary zastosowania są w danych WC.
- Stan WC 19.05.2026 (MCP): **19 produktów, ID 302–320**, wszystkie **bez SKU** ⚠️. Lista w sekcji 9.2.

---

## 4. Strona WWW — architektura i wdrożenie

Źródła: [92a69da9](https://claude.ai/chat/92a69da9-f6c3-4944-96a8-69b2c481e966), [156d7f51](https://claude.ai/chat/156d7f51-4b7a-4692-97ac-127381a913d2), [d7e4fdea](https://claude.ai/chat/d7e4fdea-5942-4086-b9f6-0e857143d166), [f97f1795](https://claude.ai/chat/f97f1795-79ac-4338-bb2c-350ef4dddfcb), [5cdd7cbe](https://claude.ai/chat/5cdd7cbe-3450-4501-a3b0-fbcd1fa319ab), [2c8129e9](https://claude.ai/chat/2c8129e9-5e02-4416-825d-08e0ccafc66b), [2655c1b1](https://claude.ai/chat/2655c1b1-84cc-4ade-a6bc-85b6952a2682), [5e4acf1c](https://claude.ai/chat/5e4acf1c-c4aa-45b6-8208-53af4c009f72), [0090ce6e](https://claude.ai/chat/0090ce6e-5c25-42be-a213-d5586db9f019).

### 4.1 Wybór platformy

| Data | Wariant | Status |
|---|---|---|
| 2026-02-20 | Rekomendacja Claude: WC catalog mode → po info „ceny nas nie obchodzą" zmiana na CPT `produkt` + ACF Pro + taksonomie (WC „NO-GO"). | ❌ zastąpione |
| 2026-02-20 | Janek: zna WooCommerce (projekt LAGUZ), wymaga, żeby kalkulatory i n8n działały bez problemu. | kontekst |
| 2026-02-27 | **WooCommerce w trybie katalogu + atrybuty globalne** (filtrowanie, tabele techniczne, kalkulatory, porównania). Bez ACF („nie korzystamy z ACF" — 20.03). | ✅ DECYZJA |

### 4.2 Model danych produktu w WC (27.02) — `WDROŻENIE`

- Opcja B: **1 PROD-ID = 1 produkt `simple`** (nie variable, bez wyboru wariantu przez klienta).
- Meta **`_agria_variants`** = JSON wszystkich SKU (`sku, nazwa_handlowa, forma_dostawy, typ_opakowania, waga_kg, lokalizacja, cena, jednostka, moq`) → tabela dostępności na stronie produktu / formularz.
- Meta `_agria_prod_id` (klucz idempotentności importu).
- Kategorie (płaskie): Rolnictwo, Sadownictwo, Rybactwo, Oczyszczalnie, Budownictwo, Hurtownie, Paszarstwo (Drogownictwo w planie, finalnie brak produktów).
- Atrybuty globalne z prefiksem **`agria-`** (kolizja nazw `marka`, `frakcja`, `segment` itd.): `agria-forma-dostawy, agria-lokalizacja, agria-producent, agria-marka, agria-cao, agria-mgo, agria-norma, agria-frakcja, agria-forma-fiz, agria-typ-reakcji, agria-szybkosc, agria-reaktywnosc, agria-dawkowanie, agria-czas, agria-zastosowanie, agria-efekt, agria-dod-zast, agria-segment`. Split po przecinku tylko: producent, marka, norma, segment, lokalizacja, forma-dostawy, cao, mgo.
- Na żywej bazie (20.03) CaO siedzi w **`pa_min-cao`** (termy „min. 70% CaO" itd.), segment w **`pa_agria-segment`**. ⚠️ `pa_min-cao` ≠ `agria-cao` z importu v6 — zweryfikować aktualne taksonomie w MCP.
- SEO (Rank Math) z pierwszego SKU: title, meta description, frazy.
- Import: skrypt PHP wywoływany przez przeglądarkę (FTP), czyszczenie produktów, meta, kategorii, atrybutów i transientów WC przed importem.

### 4.3 URL i struktura (patrz też sekcja 6)

- Stara strona: `/oferta/[segment]/[produkt]/` (np. `/oferta/rolnictwo/wapno-nawozowe-tlenkowe-palone-odmiany-01-02-i-03/`).
- 2026-02-20 `DECYZJA`: „budujemy wszystko od nowa, ma być lepiej niż było"; prefiks `/oferta/` odrzucony; segmenty realizowane landing page'ami z frazą w URL; 301 ze starych adresów (Rank Math Redirections lub .htaccess).
- Stan faktyczny (skill katalogu, kalkulator): karta produktu **`https://agria.pl/produkt/[slug]/`** (baza WC „produkt"). ⚠️ Plan mówił `/produkty/` — obowiązuje to, co na produkcji.
- ⏳ Redirecty 301 ze starych URL — brak potwierdzenia wdrożenia w czatach.

### 4.4 Wtyczka „Agria by Auranet" — `WDROŻENIE`

- Modułowa: `agria-by-auranet/agria-by-auranet.php` + `modules/[moduł]/[moduł].php`, lista modułów w `$modules`.
- Moduły: `catalog-mode` (27.02), `inquiry-form` (20.03), `liming-calculator` (20.03).
- `catalog-mode`: ukrywa ceny (listing, produkt, warianty JS), zamienia „Dodaj do koszyka" na **„Zapytaj o cenę"**, przekierowuje `/koszyk/` i `/zamowienie/` na stronę główną, blokuje rejestrację klientów, panel **WP Admin → Agria** (włącz/wyłącz, etykieta CTA, typ CTA: e-mail/telefon/link `/kontakt/`).
- 2026-03-27 fix: menu admina — dodane podmenu **Agria → Ustawienia** (wcześniej klik prowadził do CPT „Zgłoszenia"), w `render_admin_page()` dodane `do_settings_sections('agria-settings')` (sekcje e-mail formularza i reCAPTCHA).
- Repo wtyczki na GitHubie + **GitHub Actions** (`SamKirkland/FTP-Deploy-Action`) — push na `main` → deploy diff na `agria.auratest.pl` (`/public_html/wp-content/plugins/agria-by-auranet/`), sekrety `FTP_SERVER/FTP_USERNAME/FTP_PASSWORD`. ⚠️ Po go-live (27.03) nieustalone, czy deploy celuje w produkcję.
- Motyw produkcyjny: `Agria By Auranet 2.0.0` (child Hello Elementor) — stan 19.05.

### 4.5 Środowiska i go-live

- Test: `agria.auratest.pl` (hosting Auranet, WP-CLI na `host476470@elara`).
- 2026-03-27 `WDROŻENIE`: przeniesienie na **agria.pl** (nazwa.pl, `server371853`). Stan 19.05: WP 6.9.4, WC 10.6.1, PHP 8.3.30, prefiks DB `wpfz_`.
- reCAPTCHA v3: nowe klucze pod domenę agria.pl → Elementor (Ustawienia → Integracje) oraz ustawienia wtyczki (Agria → Ustawienia). Wartości kluczy — poza dokumentacją.

### 4.6 Elementy stron (24.03)

- **Formularze kontaktowe:** Elementor Pro Forms (+ reCAPTCHA v3 z integracji Elementora).
- **Mapa kontaktu:** Google Maps JS API w widgecie Custom HTML, 3 markery (Tarnów, Radgoszcz, Niedomice), **bez automatycznie otwartego popupu** (decyzja Janka), klucz API współdzielony z innymi projektami, ograniczenie referrerów do `agria.pl/*` i `www.agria.pl/*`.
- **Blog archive:** layout z mockupu (nagłówek „baza wiedzy", filtry kategorii branżowych, sidebar „Ostatnie wpisy" — widget Posts, 4 wpisy, obraz 110 px po lewej, tylko data, bez excerptu, wyklucz bieżący, separator border przez Custom CSS; „Popularne tagi"). Kolory z Global Colors.
- ⚠️ Kategorie bloga: plan 20.02 „Poradniki, Normy, Case studies" vs mockup 24.03 kategorie branżowe (Rolnictwo, Stawy i rybactwo, Oczyszczalnie…) — do ujednolicenia.
- **Stopka mobile:** kontener Flex → Column na mobile, Row+Wrap (2×2) na tablecie, logo max 100–120 px, bez własnego CSS.
- Kotwice na karcie produktu: `#opis`, `#specyfikacja-techniczna`, `#lokalizacje`, `#zamow`.

---

## 5. Automatyzacja treści — n8n DescWriter

Źródła: [84232c51](https://claude.ai/chat/84232c51-3eb2-4885-b6ee-01cb07082f77), [7ba83ef2](https://claude.ai/chat/7ba83ef2-8139-43b7-b887-39fbbd3554c4), [563bb57b](https://claude.ai/chat/563bb57b-3614-4f95-bdc4-44099abcd56b) (wszystkie 2026-03-13).

- `DECYZJA`: bazą jest workflow **LAGUZ „DESCWRITER ENHANCED"** (33 nody), przerabiany grupami nodów. Plik: `AGRIA - DESCWRITER_ENHACED_2026-03.json`.
- Model: **Gemini** (credentials jak w LAGUZ). Trigger: tagi WC **`content-write` → `content-done`**. SEO plugin: **Rank Math**. Credential WC w n8n: „Agria Woo".
- Brand guidelines = master prompt AGRIA; knowledge base = PIM + dane produktu z WC.
- Pipeline: Product Analysis → Insights → Intro → Benefits → Technical Specs (HTML) → FAQ → Final Assembly → HTML Sanitizer → Anchor Injector → Update WooCommerce → Generate SEO Meta → Update Rank Math → tag done.
- Poprawki wdrożone 13.03:
  - `Set Product Insights`: ekstrakcja JSON z konwersacyjnej odpowiedzi Gemini + fallback z danych produktu (nie wywala workflow).
  - `HTML Sanitizer`: usuwanie literału „n" po `</h2>` i `</table>`.
  - Nowy node **Anchor Injector** — `id` na H2: `opis`, `specyfikacja-techniczna`, `lokalizacje`, `zamow`.
  - CTA końcowe: **„Zapytaj o ofertę, zamów próbkę"**.
  - `Update WooCommerce Description`: description z Anchor Injector; `short_description` bez `<h2>` (sam akapit + „Kluczowe korzyści").
  - `Update Rank Math SEO`: bug — `rank_math_focus_keyword` brał wartość z `rank_math_title` → poprawione.
  - Prompt `Generate SEO Meta`: focus keyword **zgodny z nazwą produktu**.
- `DECYZJA` (13.03): opis dzielony na **5 sekcji w meta produktu**, szablon Elementor Theme Builder (single product) czyta je przez Dynamic Tag „post-custom-field" (Droga 1 — bez generowania `_elementor_data`). Sekcje: intro (kontener z `_element_id: opis`), benefits, specs, FAQ, CTA. ⚠️ Nazwy kluczy w czacie w dwóch wersjach: `_agria_section_intro…` (szablon) i `_agria_intro…` (node Save Product Sections) — sprawdzić w bazie (`query_db` na `wpfz_postmeta`).

---

## 6. SEO, struktura fraz i klastry

Źródła: [92a69da9](https://claude.ai/chat/92a69da9-f6c3-4944-96a8-69b2c481e966) (20.02), [563bb57b](https://claude.ai/chat/563bb57b-3614-4f95-bdc4-44099abcd56b) (13.03), [d531e970](https://claude.ai/chat/d531e970-ac71-4c4c-a95f-7bf778561ace) (20.03), [0090ce6e](https://claude.ai/chat/0090ce6e-5c25-42be-a213-d5586db9f019) (19.05), strategia.

### 6.1 Decyzje zapadłe

| Data | Ustalenie | Status |
|---|---|---|
| 2026-02-20 | Segment nie w URL produktu (produkt należy do wielu segmentów); segment = strona docelowa z frazą intencyjną. | ✅ DECYZJA |
| 2026-02-20 | Plan landingów: `/wapno-nawozowe/` (rolnicy), `/wapno-do-stawow/`, `/wapno-do-oczyszczalni/` + archiwum produktów + blog. Równolegle w strategii: `/dla-rolnikow`, `/dla-oczyszczalni`, `/dla-stawow`. | 🟡 wariant URL nie potwierdzony; landingów brak w stanie 19.05 |
| 2026-02-20 | Schema Product + breadcrumbs z Rank Math; frazy z PIM jako focus keyword. | 🟡 |
| 2026-03-13 | **Podział ról fraz:** karta produktu → fraza zgodna z nazwą produktu (np. „wapno palone mielone wysokoreaktywne"); **kategoria/landing → fraza intencyjna** (np. „wapno do oczyszczalni"). | ✅ DECYZJA |
| 2026-03-13 | Opisy produktów generowane przez n8n z kotwicami H2 i FAQ; meta Rank Math generowane w workflow. | ✅ |
| 2026-03-20 | Tekst SEO (~900 znaków, 3 akapity) nad kalkulatorem: frazy „kalkulator wapnowania gleby", „dawka wapna", „pH gleby", „CaO na hektar", „IUNG-PIB", „badanie gleby". | ✅ |
| 2026-05-19 | Audyt SEO (8 obszarów, ~20 h) na koszt Auranet jako baseline oferty. | ⏳ |

### 6.2 Frazy strategiczne (strategia + baseline 19.05)

- Rolnictwo: wapno nawozowe, wapno nawozowe Agrobielik, wapno nawozowe cena, wapno do gleby, odkwaszanie gleby, wapno tlenkowe, wapno węglanowe, jak wapnować glebę, ile wapna na hektar, pH gleby tabela.
- Oczyszczalnie: wapno do oczyszczalni, higienizacja osadów, stabilizacja osadów wapnem, wapno do osadów ściekowych, wapno hydratyzowane oczyszczalnia, PN-EN 459-1.
- Rybactwo: wapno do stawów, wapnowanie stawów rybnych, ile wapna do stawu, pH stawu rybnego, wapno do stawu cena, mineralizacja mułu stawowego.
- Hurt: hurtownia wapna nawozowego, wapno dla dystrybutorów.
- Budownictwo/drogi: wapno hydratyzowane budownictwo, stabilizacja gruntów wapnem, kruszywo drogowe.
- Lokalne: wapno Małopolska, wapno Tarnów, dostawa wapna Niedomice.
- Wykluczenia: wapno mleczne, mleko wapienne, wapno w organizmie, wapno gaszone (reakcja).
- Pozycje / wolumeny: **brak danych** (TBD po audycie).

### 6.3 Klastry tematyczne — stan

**Klastry nie zostały opracowane jako osobne zadanie w żadnym wątku.** Z decyzji wynika struktura hub-and-spoke (zapis porządkujący, nie nowa decyzja):

| Hub (strona docelowa, fraza intencyjna) | Karty produktów (frazy produktowe) | Artykuły wspierające (z planu content) |
|---|---|---|
| Wapno nawozowe / rolnictwo + sadownictwo | Agrobielik 70/90, Oxyfertil 90, tlenkowe z Mg, mieszanka, węglanowe (314–319), Dolomit, kredy nawozowe | Jak wapnować glebę; Tlenkowe vs węglanowe; Dawkowanie wg pH; ile wapna na hektar; kalkulator wapnowania |
| Wapno do stawów / rybactwo | Agrobielik 70/90, Oxyfertil 90, kredy nawozowe | Wapnowanie stawów — kiedy, ile, czym; pH stawu |
| Wapno do oczyszczalni | Wapno palone mielone wysokoreaktywne, Bielik, Agrobielik 90, Oxyfertil 90 | Wapno do oczyszczalni — normy; Higienizacja osadów |
| Budownictwo | Bielik, Kreda malarska | (plan mies. 6 oferty) |
| Paszarstwo | Kreda pastewna | brak |

- Oferta 19.05 przewiduje „linkowanie wewnętrzne — huby tematyczne" (m.in. hub „rybactwo" w lipcu) oraz 2 artykuły/mies.
- 🟡 Rekomendacja 19.05: rozbić treści ulotki DL (140 kg CaO/ha ubytku rocznie, tabela pH wg IUNG-PIB, segmenty) na artykuły/landingi — **bez decyzji** (Janek przerwał wątek).

---

## 7. Kalkulator wapnowania

Źródła: [d531e970](https://claude.ai/chat/d531e970-ac71-4c4c-a95f-7bf778561ace) (2026-03-20), [2655c1b1](https://claude.ai/chat/2655c1b1-84cc-4ade-a6bc-85b6952a2682) (2026-03-27).

- `DECYZJA`: MVP typu Nordkalk (użytek + gleba + pH → dawka CaO + produkty AGRIA); wersja rozszerzona typu K+S (uprawa, plon, ekologia) — nie teraz.
- Miejsce: **osobna strona**, shortcode w Elementorze: **`[agria_kalkulator_wapnowania]`**; moduł `liming-calculator` wtyczki.
- Metodyka: **IUNG-PIB, Jadczyszyn & Lipiński 2022** „Zasady ustalania dawek wapna w doradztwie nawozowym"; tabele hardcoded w PHP (grunty orne: 4 kategorie gleby, pH co 0,1, podział dawki cz. I/II; użytki zielone: pH × 4 przedziały C org.).
- Użytki zielone: **dropdown 4 przedziałów C** (<2,5 / 2,6–5,0 / 5,1–10,0 / >10%), tooltip „jeśli nie znasz — 2,6–5,0%".
- Zakres pH: b. lekka 3,8–5,0; lekka 3,8–5,5; średnia 3,9–6,0; ciężka 3,9–6,3; UZ 3,8–5,9.
- Wzór: `dawka_nawozu [t/ha] = dawka_CaO / (CaO% / 100)`.
- Produkty: dynamicznie z WC, segment `rolnictwo` (`pa_agria-segment`), CaO parsowane z termu `pa_min-cao` („min. 70% CaO" → 70); mapa awaryjna ID→CaO w kodzie (310:70, 311:80, 312:80, 313:55, 314–316:50, 317–319:40, 308:60, 302:30, 305–306:50 — wartości do weryfikacji z PIM).
- Wyniki: **tabela** (nazwa, CaO%, dawka t/ha, link), **wszystkie produkty z podziałem tlenkowe / węglanowe**, **podwójny wiersz per produkt** przy podziale dawki (cz. I / cz. II), sortowanie od najniższej dawki.
- Działanie: **AJAX** (`wp_ajax_agria_calc_liming` + nopriv, nonce), vanilla JS, bez bibliotek.
- Dodane po testach: pole **„Wielkość działki (ha)"** (domyślnie 1) → „Łącznie na X ha: Y t CaO" + kolumna „Łącznie na pole".
- CSS: kolor `#009140`. ⚠️ Niezgodny z paletą WWW (`#354E33`/`#61CE70`) — do przemyślenia.
- V2 (⏳): PDF z wynikiem, formularz zapytania z danymi z kalkulatora, eventy GA4, kalkulator dla stawów.
- 27.03: kalkulator nie zbiera danych osobowych — reCAPTCHA niepotrzebna, CTA prowadzi do formularza.

---

## 8. Formularz zapytań i próbek

Źródła: [f6cb3fbc](https://claude.ai/chat/f6cb3fbc-e7e5-40c8-8ff0-b73edd6af905) (2026-03-20), [5e4acf1c](https://claude.ai/chat/5e4acf1c-c4aa-45b6-8208-53af4c009f72) (2026-03-27).

- `DECYZJA`: formularz **zapytanie ofertowe + zamówienie próbki** (typ przełączany), dane z WP-CLI/WC (bez ACF), zgłoszenia **e-mailem do handlowca**, **autofill** bieżącego produktu na karcie.
- Moduł `inquiry-form`, shortcode **`[agria_inquiry_form]`** — na karcie produktu (sekcja `#zamow`) + osobna strona zamówienia.
- Pola: typ (oferta/próbka), produkt, forma dostawy, ilość, imię i nazwisko, firma, telefon, e-mail, miejscowość, wiadomość, zgoda RODO (zapis daty), URL źródłowy, IP.
- Zapis: CPT **`agria_inquiry`**, statusy: Nowe / Skontaktowano / Zamknięte; menu Agria → Zgłoszenia; mail do handlowca z linkiem do zgłoszenia.
- Autoresponder HTML do klienta (kontakt w 1 dzień roboczy, dane firmy).
- Antyspam: **reCAPTCHA v3** (próg 0,4, graceful fallback, badge ukryty z informacją w stopce) + honeypot.
- Ustawienia: e-mail odbiorcy + CC, klucze reCAPTCHA w Agria → Ustawienia (od 27.03).
- ✅ Janek potwierdził działanie 20.03.

---

## 9. Katalog drukowany

Źródła: [ee2b3f91](https://claude.ai/chat/ee2b3f91-bc65-445f-af90-6bc9e7da8170) (04-07), [9fd10ab6](https://claude.ai/chat/9fd10ab6-934f-474f-8605-81a82135d444) (04-08), [5274b3f8](https://claude.ai/chat/5274b3f8-a1f6-40d8-a401-c0cbc907d437) (04-10), [c3848a1d](https://claude.ai/chat/c3848a1d-f27c-475d-ba52-faa3361e7585) (04-13), [6f0a74f2](https://claude.ai/chat/6f0a74f2-7b6e-4215-87d9-e66a9d6b3fb6) (04-13), [d9adedbe](https://claude.ai/chat/d9adedbe-cb45-4cfe-bec5-5e65869bd539) (04-13), [c6b086f2](https://claude.ai/chat/c6b086f2-3150-4583-84d3-b0ea0f3bd571) (04-15), [101337bb](https://claude.ai/chat/101337bb-364c-40cd-9c28-f2c62a46f9f4) (04-15), [0090ce6e](https://claude.ai/chat/0090ce6e-5c25-42be-a213-d5586db9f019) (05-19), skill `agria-katalog`.

### 9.1 Ewolucja podejścia

| Data | Podejście | Status |
|---|---|---|
| 2026-02-05 | Spec 24 str. (txt): 18 kart, Montserrat, stare kolory | ❌ |
| 2026-02-20 | Generator InDesign „od zera" (JSX, rysowanie elementów) | ❌ |
| 2026-04-07 | Pełny layout, paleta WWW, PJS 600 + BJ 300. **Szablon ręczny = karta Dolomitu (str. 1)**, dokument `Agria-katalog-2026-04-03-OFERTA.indd`; każda karta = JSX duplikujący stronę 1 i podmieniający treści. Wzór: `AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx`. | ✅ |
| 2026-04-07 | Katalog zostaje w projekcie Agria (kontekst), powstaje skill `agria-katalog`. | ✅ |
| 2026-04-07/08 | Karty zbiorcze dla odmian (węglanowe bez Mg, z Mg, kredy) → **zmienione**: każdy produkt WC = osobna karta. | ✅ 04-08 |

### 9.2 Produkty w WC (stan 19.05.2026, MCP)

| ID | Produkt | W katalogu 15.04 |
|---|---|---|
| 302 | Dolomit | ✅ (szablon) |
| 303 | Kreda czarna (jeziorna) | ❌ decyzja klienta — pomijamy (⚠️ nadal w WC) |
| 304 | Kreda malarska | ✅ |
| 305 | Kreda nawozowa granulowana | ✅ |
| 306 | Kreda nawozowa sypka | ✅ |
| 307 | Kreda pastewna | ✅ |
| 308 | Mieszanka tlenkowo-węglanowa | ✅ |
| 309 | Wapno hydratyzowane Bielik | ✅ |
| 310 | Wapno nawozowe tlenkowe Agrobielik 70 | ✅ |
| 311 | Wapno nawozowe tlenkowe Agrobielik 90 | ✅ |
| 312 | Wapno nawozowe tlenkowe Oxyfertil 90 | ✅ |
| 313 | Wapno nawozowe tlenkowe zawierające magnez | ✅ (nazwa druk: „z magnezem") |
| 314 | Węglanowe bez Mg granulowane | ✅ |
| 315 | Węglanowe bez Mg — Odmiana 04 | ✅ |
| 316 | Węglanowe bez Mg — Odmiana 05 | ✅ |
| 317 | Węglanowe z Mg granulowane | ✅ |
| 318 | Węglanowe z Mg — Odmiana 04 | ✅ |
| 319 | Węglanowe z Mg — Odmiana 05 | ✅ |
| 320 | Wapno palone mielone wysokoreaktywne | ✅ |

### 9.3 Zasady treści kart (obowiązujące — skill `agria-katalog`)

1. Jeden produkt na raz: skrypt → test w InDesignie → feedback → następny.
2. Dane zawsze z MCP (`catalog_product`, `wc_product`), nie z głowy.
3. **Nazwy 1:1 z WC** (od 10.04; wcześniej 07–08.04 dopuszczano skróty >35 znaków). Dopuszczalne tylko: „zawierające magnez" → „z magnezem", „— Odmiana XX" → „- ODMIANA XX". Nazwa >50 znaków → pytać klienta. Referencja: „WAPNO NAWOZOWE WĘGLANOWE Z MAGNEZEM - GRANULOWANE" (49 zn., 3 linie, ramka rozciągana o 15 mm).
4. Zero szablonowych otwarć („Szybkie…"); każdy produkt inny kąt (tabela kątów w skillu).
5. **Nigdy nie wycinać pH** z tabeli; przy 16 parametrach wycina się „Dostępność: Cały rok".
6. `descHead` = cecha produktu; `sectionHead` = efekt / dla kogo (2 linie). Test: nie mogą być parafrazą.
7. Zakaz `"...\ri ..."` w `sectionHead` (renderuje „i" na początku drugiej linii).
8. Pliki: `AGRIA_karta_[ID]_[skrot].jsx`, bez `_v1/_v2`, iteracje przez edycję pliku.
9. Samokontrola całego obiektu `PROD` przed oddaniem.
10. Po karcie: linki edycja WP + frontend `https://agria.pl/produkt/[slug]/`.
11. Tabela: 15 wierszy; czyszczenie śmieci MCP (frakcje, pauzy, encje HTML), magazyny skracane do nazw.
12. JSX: duplikacja na koniec dokumentu (`AFTER, lastPage`), ramka nazwy wykrywana po exact „DOLOMIT".

### 9.4 Struktura 24 stron (wersja 15.04)

| Str. | Zawartość | Ustalenia |
|---|---|---|
| 1 | Okładka | Tło `#354E33`, zdjęcie pełnostronicowe (traktor, złota godzina), gradient, logo białe PG; „AGRIA / Surowce wapniowe i mineralne / Stabilne parametry. Pewne dostawy." + „www.agria.pl 2026" |
| 2 | O firmie | Nagłówek „Wapno to nasza specjalność. Trzy pokolenia w branży.", H2 „Witamy w AGRIA", 3 akapity (kim jesteśmy / jak pracujemy / dla kogo), CTA „Zapraszamy do rozmowy", podpis „Zarząd AGRIA Sp. z o.o.", zdjęcie ogólne z wapnem |
| 3 | Segmenty / oferta | 5 bloków: zdjęcie + nagłówek + slogan korzyści + tekst (Janek: „nie projektuj, tylko treści"); „Ochrona środowiska" → **„Oczyszczalnie ścieków"**; ostatecznie „nie kombinujemy" z łączeniem segmentów |
| 4–21 | 18 kart produktów | kolejność: Agrobielik 70, 90, Oxyfertil 90, tlenkowe z Mg, mieszanka, 314, 315, 316, 317, 318, 319, kreda granulowana, sypka, malarska, pastewna, Dolomit (19), Bielik (20), palone mielone (21) |
| 22 | Warunki handlowe | 4 boxy USP (35 lat / 2 oddziały / flota 3–24 t / dokumentacja), płatności i dostawa, zamówienia, logotypy producentów, CTA |
| 23 | Kontakt | oddziały, handlowcy, kontakt przetargowy |
| 24 | Tył okładki | tło ciemnozielone, mapa Polski z lokalizacjami, logo, slogan, www/tel/e-mail, pasek z danymi prawnymi |

### 9.5 Piktogramy segmentów (13.04)

- 8 piktogramów: rolnictwo, rybactwo, oczyszczalnie, budownictwo, drogownictwo, sadownictwo, paszarstwo, hurtownie; pliki `AGRIA_ikona_[segment].svg`.
- Rekomendacja/kierunek: **solid**, viewBox **48×48**, estetyka Phosphor Fill, `rx=1`, kolor `#0D9247`, rozmiar tagu 10–15 mm. Janek: „trochę mało rolnictwa, sprawdźmy inne wersje, może być solid".
- Użycie w 18 kartach (15.04): Rolnictwo 15, Hurtownie 12, Sadownictwo 9, Rybactwo 6, Oczyszczalnie 5, Budownictwo 2, Paszarstwo 1, Drogownictwo 0.
- ⚠️ Ryzyko druku: `#0D9247` jako kompozyt CMYK — sprawdzić na proofie.

### 9.6 Review i poprawki

- 13.04: review IDML kart 1–18 — poprawione `\ri` (Dolomit, Agrobielik 70, 90), duplikacje descHead/sectionHead (tlenkowe z Mg, węglanowe granulowane, Odm 05), literówki, podwójne spacje.
- 15.04 krytyczne (przed wysyłką): tekst Rybactwa wklejony w segment Oczyszczalnie (str. 3) → nowa treść; nagłówek tabeli „V" zamiast „PARAMETRY" (str. 16); telefon „+48 14 621 88 210" (str. 22–23).
- 15.04 wysokie: piktogramy — str. 5 i 6 Sadownictwo → Rybactwo; str. 17 dodać Rolnictwo; str. 20 Hurtownie → Oczyszczalnie. Dolomit (str. 19) — przepisane treści (descHead „Dolomit: długodziałające odkwaszanie z magnezem", sectionHead „Dwa składniki / jeden zabieg", producent Siarkopol, worki 10/25 kg, Tarnobrzeg). Literówka str. 14.
- 15.04 `DECYZJA`: drobiazgi typograficzne w tabeli Dolomitu (pauzy, spacje) — **odpuszczone**.
- Do v2.0: etykieta „Magazyn", brak wiersza „Dostępność" (str. 8, 14, 17, 21), niespójny tagline, brak kart cementu / kruszywa / wapna drogowego / Ekograncali Activ.

### 9.7 Wysyłka do klienta (15.04)

- Mail do Kasjana (krótki, na „Ty"): 24 strony = wielokrotność 4 (gotowe pod drukarnię po akceptacji); prośba o wydruk i przegląd; tabele i treści do weryfikacji (treści pisane przez Auranet, klient nie dostarczył własnych); brakujące produkty (m.in. cement) do dodania/wymiany; PDF 6 MB (jakość web), wersja do druku ~20 MB po zatwierdzeniu.

### 9.8 Specyfikacja druku (design-spec)

A4, spad 3 mm, safe 5 mm, marginesy 12/12/15/15, jednostronnie (`facingPages=false`), saddle stitch; okładka 250 g Munken Lynx Rough, środek 135 g Munken Pure Cream; CMYK (+opcj. Pantone 382 C), lakier UV selektywny; PDF/X-1a:2001, 300 dpi, fonty osadzone. Nakłady: proof 10 szt. (~500 PLN), 500 szt. (2 000–2 500), 1 000 szt. (3 500–4 500). ⏳ Proof/druk — brak potwierdzenia w czatach.

### 9.9 Wersja 2026-05-04 (web) — `FAKT` wg analizy z 19.05

- Plik `Agria-katalog-2026-05-04-web.pdf`: 23 strony, 17 kart (wg odczytu 19.05 — ⚠️ vs 24 str. z 15.04, zweryfikować).
- Zmiany składu vs 15.04: doszły **Agrobielik 90 frakcja 2–8 mm** (osobna karta), **Kreda nawozowa sypka Odmiana 06a** (Pierzchnica/Drugnia), **węglanowe z Mg Odm 05** (CaO 25–37%, MgO 8–20%); brak **Kredy malarskiej**.
- ⚠️ Karty Agrobielik 90 0–3 mm i 2–8 mm mają niemal identyczne teksty; bullet „2–4 dni" przy wariancie 7–14 dni.
- ⚠️ Produkty z katalogu nieobecne w WC: Agrobielik 90 2–8 mm, Kreda sypka 06a; w WC nieobecne w katalogu: Kreda malarska (304), Kreda czarna (303).

---

## 10. Pozostałe materiały drukowane

Źródło: [e5bb7dee](https://claude.ai/chat/e5bb7dee-4dd3-4ba6-a35e-269eb2487375) (2026-05-18), [0090ce6e](https://claude.ai/chat/0090ce6e-5c25-42be-a213-d5586db9f019).

- **Ulotka DL** (99×210, 6 stron w „C", kreda 170 g połysk, 4/4) — projekt gotowy 18.05 (front/back JPG). Treść: 140 kg CaO/ha rocznego ubytku, tabela pH wg IUNG-PIB, segmenty.
- Wycena dla klienta (18.05, narzut 30%, termin ~5 dni roboczych, netto): **200 szt. — 235 zł, 500 szt. — 316 zł, 1 000 szt. — 384 zł**. Projekt DTP osobno. ⚠️ Cena bazowa 1 000 szt. szacowana (brak w screenie cennika) — do potwierdzenia w konfiguratorze.
- Wizytówki — ⏳ planowane (19.05).

---

## 11. Oferta Auranet — retainer SEO/utrzymanie

Źródło: [0090ce6e](https://claude.ai/chat/0090ce6e-5c25-42be-a213-d5586db9f019) (2026-05-19).

- Wstępne zielone światło: **2 000 PLN netto/mies.**, 12–15 h pracy, horyzont **6 miesięcy** (czerwiec–listopad 2026).
- `DECYZJA`: **audyt techniczny + on-page na koszt Auranet** (baseline pod ofertę); analityka (GA4, GSC, GTM) Auranet wdraża wcześniej dla siebie, klient płaci za nią w ramach oferty później.
- Szkic zakresu (dokument roboczy, nie zaakceptowany przez klienta): technical SEO i utrzymanie 3–4 h, on-page 3–4 h, content 2 artykuły/mies. 4–5 h, analityka i raport 1–2 h, ad-hoc 1–2 h. Poza pakietem: Google Ads, sesja zdjęciowa, redesigny >5 h, linkbuilding płatny, druk, social media.
- Kamienie milowe (szkic): VI stabilizacja + schema + GBP; VII produkty + hub rybactwo; VIII oczyszczalnie + landing; IX evergreen + kategorie; X SEO lokalne + katalogi branżowe; XI budownictwo/drogownictwo + E-E-A-T + re-audyt.
- Cele 6 mies. (szkic): +50–100% sesji organicznych, +15–25 fraz TOP 10, +30–50% konwersji, CWV zielone.
- ⏳ Status: oferta do przygotowania i prezentacji; czekamy na potwierdzenie klienta.

---

## 12. Infrastruktura, dostępy, narzędzia (bez sekretów)

- Hosting produkcyjny: nazwa.pl, `server371853`; ścieżka WP: `/home/server371853/ftp/agria.pl`.
- Test/dev: `agria.auratest.pl`, SSH `host476470@elara` (WP-CLI).
- **MCP `Agria.pl`**: `https://agria.pl/mcp/mcp.php` (read-only). Narzędzia: `status`, `wc_products_list`, `catalog_product`, `wc_product`, `query_db`, `read_file`, `list_dir`, `plugins_list`, `wc_options`, `stats`. Troubleshooting: `wp-load.php not found` → poprawić `$WP_ROOT` w `mcp.php`.
- Repo projektowe (docs): `git@github.com:auranet-js/agria.git` — 19.05 `DECYZJA`: stare repo reużyte; Janek wrzuca wszystkie materiały luzem, Claude Code dostaje pełną swobodę struktury (pakiet z `CLAUDE.md` przygotowany w czacie jako alternatywa).
- Repo wtyczki `agria-by-auranet` — GitHub + Actions (sekcja 4.4).
- n8n: self-hosted, credential WC „Agria Woo".
- Google Cloud: klucz Maps JS współdzielony z innymi projektami (monitoring zużycia per API).
- Skille Claude: `agria-katalog` (aktualny), `agria-katalog-indesign` (starszy — reguła duplikacji `AFTER, srcPage` przestarzała).

---

## 13. Otwarte kwestie, niespójności, TODO

### 13.1 Niespójności do rozstrzygnięcia

1. Adres centrali: Warsztatowa 5 vs Warszawska 5.
2. Główny numer telefonu B2B (660 768 691 / 14 621 88 21 / 604 428 782).
3. Dwa zielone „firmowe" (`#009140` vs `#0D9247`) + kalkulator w `#009140` vs paleta WWW.
4. Tagline okładka („Pewne dostawy") vs tył („Pewne plony").
5. Taksonomie CaO: `pa_min-cao` vs `pa_agria-cao`.
6. Klucze meta sekcji opisu: `_agria_section_*` vs `_agria_*`.
7. URL produktów `/produkt/` (stan) vs plan `/produkty/`; landingi `/wapno-…/` vs `/dla-…/`.
8. Katalog 15.04 (24 str., 18 kart) vs web 04.05 (23 str., 17 kart wg odczytu).
9. Pole „Magazyn" na kartach vs „dwa magazyny" na str. 2.
10. Kreda czarna nadal w WC mimo wycięcia z katalogu.
11. Brak SKU na wszystkich 19 produktach WC.
12. Produkty tylko w katalogu (Agrobielik 90 2–8 mm, Kreda sypka 06a) i tylko w WC (Kreda malarska).
13. Trzuskawica: w strategii i kartach (Oxyfertil), w analizie 19.05 zasugerowano jej usunięcie z listy producentów — rozstrzygnąć faktami od klienta.

### 13.2 Niewykonane / niepotwierdzone

- Redirecty 301 ze starych URL `/oferta/…`.
- Landing pages segmentowe (rolnicy / stawy / oczyszczalnie).
- Karty i produkty WC: cement, kruszywo, wapno drogowe, Ekograncali Activ (drogownictwo bez produktów).
- Proof i druk katalogu; wersja print ~20 MB.
- Wizytówki.
- Audyt SEO, baseline fraz, GA4/GSC/GTM, oferta 2000 PLN.
- Kalkulator V2 (PDF, prefill formularza, GA4, stawy).
- Klastry tematyczne i kalendarz treści.
- Deploy wtyczki po go-live (czy Actions celuje w produkcję).
- Google Business Profile dla oddziałów.

---

## 14. Indeks wątków projektu

| Data | Wątek | Temat |
|---|---|---|
| 2025-12-22 | [f83131b3](https://claude.ai/chat/f83131b3-7cb2-4ade-88d5-4f17a65fcf0a) | Strategia marketingowa |
| 2025-12-22 | [5a4ece51](https://claude.ai/chat/5a4ece51-21b7-4e47-be0d-8ea699407f38) | Konwersja strategii MD → DOCX/PDF |
| 2026-01-15 | [d4edd311](https://claude.ai/chat/d4edd311-52f9-4f3a-976b-31a06e024f34) | Stopki HTML v1 |
| 2026-01-15 | [7c1aa7e4](https://claude.ai/chat/7c1aa7e4-1ef8-4641-9204-ebc66780f892) | (pusty) |
| 2026-01-20 | [52e1f212](https://claude.ai/chat/52e1f212-e45e-4907-8f16-f3d565706032) | Stopki HTML v2 |
| 2026-01-22 | [b84ebb27](https://claude.ai/chat/b84ebb27-5a2c-4a38-8f8e-368a19cd967b) | Tagline |
| 2026-02-05 | [51905cde](https://claude.ai/chat/51905cde-c1f1-4fb7-a150-77f18e8f3216) | PIM v1.0 do klienta |
| 2026-02-20 | [92a69da9](https://claude.ai/chat/92a69da9-f6c3-4944-96a8-69b2c481e966) | Architektura strony, URL, generator InDesign v1 |
| 2026-02-27 | [156d7f51](https://claude.ai/chat/156d7f51-4b7a-4692-97ac-127381a913d2) | WooCommerce, import PIM, wtyczka, deploy |
| 2026-03-13 | [84232c51](https://claude.ai/chat/84232c51-3eb2-4885-b6ee-01cb07082f77) | Adaptacja n8n LAGUZ → AGRIA |
| 2026-03-13 | [7ba83ef2](https://claude.ai/chat/7ba83ef2-8139-43b7-b887-39fbbd3554c4) | Kotwice, CTA, sanitizer |
| 2026-03-13 | [563bb57b](https://claude.ai/chat/563bb57b-3614-4f95-bdc4-44099abcd56b) | Rank Math, sekcje meta, szablon Elementor |
| 2026-03-20 | [f6cb3fbc](https://claude.ai/chat/f6cb3fbc-e7e5-40c8-8ff0-b73edd6af905) | Formularz zapytań/próbek |
| 2026-03-20 | [d531e970](https://claude.ai/chat/d531e970-ac71-4c4c-a95f-7bf778561ace) | Kalkulator wapnowania |
| 2026-03-24 | [d7e4fdea](https://claude.ai/chat/d7e4fdea-5942-4086-b9f6-0e857143d166) | Blog archive |
| 2026-03-24 | [f97f1795](https://claude.ai/chat/f97f1795-79ac-4338-bb2c-350ef4dddfcb) | Mapa lokalizacji |
| 2026-03-24 | [5cdd7cbe](https://claude.ai/chat/5cdd7cbe-3450-4501-a3b0-fbcd1fa319ab) | RWD: toggle, stopka, typografia |
| 2026-03-27 | [2c8129e9](https://claude.ai/chat/2c8129e9-5e02-4416-825d-08e0ccafc66b) | Go-live, reCAPTCHA |
| 2026-03-27 | [2655c1b1](https://claude.ai/chat/2655c1b1-84cc-4ade-a6bc-85b6952a2682) | Kalkulator + zamówienia (przypomnienie) |
| 2026-03-27 | [5e4acf1c](https://claude.ai/chat/5e4acf1c-c4aa-45b6-8208-53af4c009f72) | Klucze reCAPTCHA we wtyczce, menu admina |
| 2026-04-07 | [ee2b3f91](https://claude.ai/chat/ee2b3f91-bc65-445f-af90-6bc9e7da8170) | Makieta katalogu, szablon Dolomit, skill |
| 2026-04-08 | [9fd10ab6](https://claude.ai/chat/9fd10ab6-934f-474f-8605-81a82135d444) | Karty: mieszanka, węglanowe |
| 2026-04-10 | [5274b3f8](https://claude.ai/chat/5274b3f8-a1f6-40d8-a401-c0cbc907d437) | Karty 317–318, nowe zasady skilla |
| 2026-04-13 | [c3848a1d](https://claude.ai/chat/c3848a1d-f27c-475d-ba52-faa3361e7585) | Karty 319 → koniec, review |
| 2026-04-13 | [6f0a74f2](https://claude.ai/chat/6f0a74f2-7b6e-4215-87d9-e66a9d6b3fb6) | Piktogramy segmentów |
| 2026-04-13 | [d9adedbe](https://claude.ai/chat/d9adedbe-cb45-4cfe-bec5-5e65869bd539) | Okładka |
| 2026-04-15 | [c6b086f2](https://claude.ai/chat/c6b086f2-3150-4583-84d3-b0ea0f3bd571) | Str. 2, segmenty, str. 22–24 |
| 2026-04-15 | [101337bb](https://claude.ai/chat/101337bb-364c-40cd-9c28-f2c62a46f9f4) | Review katalogu, mail do Kasjana |
| 2026-05-18 | [e5bb7dee](https://claude.ai/chat/e5bb7dee-4dd3-4ba6-a35e-269eb2487375) | Wycena ulotki DL |
| 2026-05-19 | [0090ce6e](https://claude.ai/chat/0090ce6e-5c25-42be-a213-d5586db9f019) | Przeniesienie do Claude Code, audyt, oferta |
