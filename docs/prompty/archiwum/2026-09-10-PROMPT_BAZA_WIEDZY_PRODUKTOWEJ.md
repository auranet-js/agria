# PROMPT — baza wiedzy o każdym produkcie AGRII

> **Projekt:** `agria` · **Zlecił:** Jan Schenk, 10.09.2026 · **Typ:** zadanie badawcze, **READ-ONLY wobec produkcji**
> **Wynik:** `docs/produkty/` — jeden plik MD na produkt + indeks + macierz fraz.
> **Kontekst poprzedniego wątku:** `docs/sesje/2026-09-10-rekonstrukcja-architektury-podsumowanie.md` — przeczytaj w całości,
> zanim zaczniesz. Tam jest stan faktyczny, słownik i lista decyzji otwartych.

---

## 0. Po co ten wątek — słowami Janka, bez łagodzenia

Przez pół roku pracowałeś na **frazach**, nie na **produktach**. Budowałeś landingi, przestawiałeś kategorie, liczyłeś
kanibalizację — a nigdy nie usiadłeś do tego, **co AGRIA sprzedaje**. Wszystko jest w kartach PDF z katalogu: jaki to produkt,
z jakiej kopalni, jaka frakcja, jakie zastosowanie, jaka dawka, z czym go porównać.

Janek: *„Dopóki nie zbudujesz konkretnej bazy wiedzy o każdym produkcie, w osobnym pliku MD dla każdego produktu —
i dopiero jak to zbudujesz, możesz sobie sprawdzić DataForSEO, Search Console, nawet Google Ads, ilość i koszt."*

Przykłady, o które chodzi:
- **Agrobielik 70** — chcemy rankować na `agrobielik 70`, na `agrobielik 70 zastosowanie`, na `ile agrobielik 70 na hektar`.
- **Oxyfertil 90** — na główną frazę produktu, na Oxyfertil + lokalizację kopalni/zakładu, na Oxyfertil + dawkowanie.
- **Producent / kopalnia jako fraza** — jeśli z jednego zakładu (np. Trzuskawica — do sprawdzenia na kartach) bierzemy dwa wapna,
  to mamy dwa produkty na frazy z nazwą tego zakładu.
- **Porównania** — z czym produkt porównać (inna frakcja, inna odmiana, tlenkowe vs węglanowe, granulat vs sypkie).

**Dopiero po zbudowaniu bazy** wracamy do decyzji o kategoriach, stronach grup produktów i reklamach (decyzje D1–D4 w podsumowaniu §3).
**W tym wątku żadnej z nich nie podejmujesz i nie proponujesz architektury.**

---

## 1. Zasady twarde

1. **Źródło prawdy o produkcie = karta AGRII z katalogu** (`agria-karta-produktu-*.pdf` na `/do-pobrania/`).
   Nazwa, zastosowania, parametry, frakcja, dawka, producent, zakład/kopalnia — **stamtąd**. Karty producentów, atesty OSChR
   i karty charakterystyki to źródła uzupełniające. **Rozumowanie nie jest źródłem.**
2. **Produktów i parametrów nie ruszasz.** Nic nie zapisujesz na produkcji — zero MCP write, zero WP-CLI, zero Elementora,
   zero zgłoszeń do indeksu. Tylko odczyt.
3. Gdy karta PDF i strona (render karty) mówią co innego — **zapisujesz rozbieżność w pliku produktu, nic nie poprawiasz**.
4. Każda liczba ma źródło i datę (plik, zapytanie API, okno GSC). Brak danych = „niezmierzone", nie zero.
5. **Słownik:** kategoria = strona z listą produktów; karta = strona jednego produktu; poradnik = artykuł.
   Nie używasz słów „landing" i „segment". „Zastosowanie" = to, do czego produkt służy według karty.
6. **Jeden krok na raz:** najpierw pilot na jednym produkcie (§5), pokazujesz Jankowi, czekasz na akcept szablonu,
   dopiero potem pozostałe 18.
7. Pytania do Janka tylko quizem (AskUserQuestion), z podpowiedziami i wariantem „nie wiem / pytamy klienta".
8. Do klienta nic nie wysyłasz.

---

## 2. Wejście — produkty i ich PDF-y (mapa zbudowana 10.09, zweryfikuj na starcie)

PDF-y: `https://agria.pl/wp-content/uploads/2026/06/<plik>` (karty AGRII), `/2026/08/` (atesty, karty charakterystyki Nordkalk 2025),
`/2026/03/` (starsze karty producenta). Pełna lista 31 PDF-ów: `curl -s https://agria.pl/do-pobrania/ | grep -o 'href="[^"]*\.pdf"'`.
Katalog drukowany w repo: `assets/print/catalog/Agria-katalog-2026-05-04-web.pdf`.

| WC ID | produkt | karta na stronie | karta AGRII (PDF) | źródła uzupełniające |
|---|---|---|---|---|
| 310 | Wapno nawozowe tlenkowe Agrobielik 70 | `/wapno-nawozowe-rolnictwo/agrobielik-70/` | `agria-karta-produktu-agrobielik-70.pdf` | atest OSChR odm. 02 (2025); Nordkalk `karta-produktu-wapno-nawozowe-odmiana-02.pdf`; KCh tlenek wapnia Nordkalk 2025 |
| 311 | Wapno nawozowe tlenkowe Agrobielik 90 | `/wapno-nawozowe-rolnictwo/agrobielik-90/` | **dwie:** `…agrobielik-90-0-3mm.pdf`, `…agrobielik-90-2-8mm.pdf` | atest OSChR odm. 01 (2025); Nordkalk `…odmiana-03.pdf`? — ustal, której odmiany dotyczy |
| 312 | Wapno nawozowe tlenkowe Oxyfertil 90 | `/wapno-nawozowe-rolnictwo/oxyfertil-90/` | `…oxyfertil-90.pdf` | — |
| 313 | Wapno nawozowe tlenkowe zawierające magnez | `/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/` | `…tlenkowe-z-magnezem.pdf` | — |
| 308 | Mieszanka tlenkowo-węglanowa | `/wapno-nawozowe-rolnictwo/mieszanka-tlenkowo-weglanowa/` | `…mieszanka-tlenkowo-weglanowa.pdf` | — |
| 314 | Wapno nawozowe węglanowe bez magnezu granulowane | `/wapno-nawozowe-rolnictwo/weglanowe-granulowane/` | `…weglanowe-granulowane.pdf` | — |
| 315 | Węglanowe bez magnezu — Odmiana 04 | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/` | `…weglanowe-odmiana-04.pdf` | KCh węglan wapnia Nordkalk 2025 |
| 316 | Węglanowe bez magnezu — Odmiana 05 | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` | **brak karty AGRII** | ⚠️ producent: render mówi Lhoist, `FAKTY_KLIENTA` §3 mówi Kopalnia Celiny |
| 317 | Węglanowe z magnezem granulowane | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/` | `…weglanowe-z-magnezem-granulowane.pdf` | — |
| 318 | Węglanowe z magnezem — Odmiana 04 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-04/` | `…weglanowe-z-magnezem-odmiana-04.pdf` | atest OSChR Jażwica 2026 |
| 319 | Węglanowe z magnezem — Odmiana 05 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-05/` | `…weglanowe-z-magnezem-odmiana-05.pdf` | atesty OSChR Laskowa 2026, Winna 2026 |
| 302 | Dolomit | `/wapno-nawozowe-rolnictwo/dolomit/` | `…dolomit.pdf` | — |
| 305 | Kreda nawozowa granulowana | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-granulowana/` | `…kreda-nawozowa-granulowana.pdf` | — |
| 306 | Kreda nawozowa sypka | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-sypka/` | `…kreda-nawozowa-sypka-odmiana-06a.pdf` | ⚠️ karta mówi „odmiana 06a" — sprawdź zgodność ze stroną |
| 307 | Kreda pastewna | `/paszarstwo/kreda-pastewna/` | `…kreda-pastewna.pdf` | ⚠️ „37% CaO" vs „37% Ca" — zgłoszone 21.08, rozstrzyga karta |
| 304 | Kreda malarska | `/kreda-malarska/kreda-malarska/` | **brak karty AGRII** (nie ma jej w katalogu 04.05) | — |
| 320 | Wapno palone mielone wysokoreaktywne | `/wapno-do-oczyszczalni/wapno-palone-mielone/` | `…wapno-palone-mielone-wysokoreaktywne.pdf` | KCh tlenek wapnia Nordkalk 2025 i Kujawy |
| 309 | Wapno hydratyzowane Bielik | `/wapno-hydratyzowane/bielik/` | `…wapno-hydratyzowane-bielik.pdf` | Nordkalk `karta-produktu-wapno-hydratyzowane.pdf`; KCh diwodorotlenek wapnia Nordkalk 2025 |
| 303 | Kreda czarna (jeziorna) | `/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/` | **brak karty AGRII** (wycięta z katalogu) | — |

**Na `/do-pobrania/` są też karty producenta produktów, których nie ma w WooCommerce:** `karta-produktu-wapno-palone-kruszone.pdf`,
`karta-produktu-wapno-palone-w-brylach.pdf`. Zapisz, co to za produkty i czy AGRIA je sprzedaje — **nie proponuj dodania do sklepu**
(zestaw produktów jest zamknięty), tylko odnotuj w indeksie.

**Pozostałe źródła w repo, z których korzystasz:**
- `docs/FAKTY_KLIENTA.md` §3–5 — producenci, ceny (cennik Pawła 07.08, ceny **za towar bez transportu**), logistyka, magazyny.
- `docs/operations/CENNIK_PAWEL_2026-08-07.md` — ceny; **na stronie tylko w treści, `_price` zostaje puste** (ADR `2026-08-19-dwie-warstwy-cen`).
- `data/olx/product-specs.json` — render tabel specyfikacji 19 kart z 20.08 (to jest stan strony, nie źródło prawdy).
- `data/olx/market/2026-08-28.json` + `docs/operations/OLX_KONKURENCJA_2026-08-07.md` — oferty konkurencji na OLX (nazwy, ceny, sprzedawcy).
- `data/seo/2026-09-09-serp-*.json` — SERP-y z 09.09 (część fraz już pobrana — nie płać drugi raz).
- `data/zrodla/` — IUNG-PIB 2021 i 2022 (dawki, terminy) z warstwą tekstową.
- `docs/archiwum/2025-12_2026-05-HISTORIA_DECYZJI_claude-ai.md` §9 — zasady kart katalogu (nazwy 1:1 z WC, kąty treści).

---

## 3. Co ustalasz dla każdego produktu — szablon pliku `docs/produkty/<slug>.md`

```markdown
# <nazwa 1:1 z karty AGRII> (WC #<ID>)

> Karta AGRII: <plik PDF> · karta na stronie: <URL> · kategoria dziś: <nazwa> · stan na <data>

## 1. Tożsamość (z karty PDF — cytaty, nie parafrazy)
- nazwa handlowa / techniczna / marka / odmiana wg rozporządzenia
- producent · **zakład / kopalnia** (lokalizacja) · magazyny wysyłkowe
- rodzaj: tlenkowe / węglanowe / kreda / dolomit / hydratyzowane / palone; z magnezem czy bez
- forma fizyczna i **frakcja** · formy dostawy wg karty

## 2. Parametry (tabela 1:1 z karty PDF, nic nie przeliczasz)

## 3. Zastosowania (z karty) — do czego, na jakie gleby / uprawy / obiekty, kiedy (termin), dawka

## 4. Z czym go porównać
- produkty AGRII tego samego rodzaju (inna frakcja, odmiana, z Mg / bez) — różnice wyłącznie z kart
- odpowiedniki konkurencji, które realnie widać w SERP i na OLX (nazwa, sprzedawca, cena jeśli publiczna)

## 5. Frazy — popyt
| fraza | typ (nazwa / nazwa+zastosowanie / nazwa+dawka / nazwa+cena / kopalnia / rodzaj ogólny / porównanie) | wyszukań/mies. (DFS) | CPC (Ads) | źródło, data |

## 6. Stan dziś na stronie (render, nie baza)
- title, H1, lista H2, liczba znaków treści, FAQ, cena w treści, `offers` w schemacie, zdjęcie, listing w kategorii
- indeks (URL Inspection), GSC 90 dni: wyświetlenia, kliknięcia, CTR, pozycja + **zapytania, na które karta się pokazuje**
- zapytania ofertowe z tej karty (CPT `agria_inquiry`, `_source_url`) · kliknięcia z Ads na tę kartę (jeśli były)
- **rozbieżności karta PDF ↔ strona** (parametr po parametrze)

## 7. Konkurencja w wynikach — kto stoi na 3–5 głównych frazach produktu (SERP mobile PL), gdzie jesteśmy

## 8. Luki — czego brakuje (treść, frazy bez pokrycia, porównania, zastosowania z karty nieobecne na stronie)

## 9. Pytania do Janka / klienta (tylko to, czego karty nie rozstrzygają)
```

---

## 4. Skąd bierzesz dane i ile to kosztuje

| co | narzędzie | uwaga |
|---|---|---|
| treść PDF | `pdftotext -layout`, `pypdf` (oba są na Elarze) | PDF-y pobierz do `data/produkty/pdf/`, tekst obok (`.txt`) — nie do `tmp/` |
| render karty | `curl` z pominięciem cache, **nie `?cb=`** (WP Rocket); rozgrzewka jednym żądaniem, potem odczyt | wzorzec: `scripts/olx/extract_specs.py` |
| indeks | `python3 scripts/gsc_inspect.py <ścieżki>` | — |
| GSC per karta | `python3 scripts/gsc_baseline.py --dni 90 --out data/produkty/gsc/<slug>.json <ścieżka>` | zapytania filtrem `page`; CTR licz z poziomu strony, nie z sumy zapytań |
| popyt i pomysły na frazy | DataForSEO przez curl (`~/secrets/dataforseo/`): `keywords_data/google_ads/search_volume/live`, `dataforseo_labs/google/keyword_suggestions/live`, `location_code 2616`, `language_code pl` | **sprawdź saldo przed startem** (`GET /v3/appendix/user_data`) i podaj koszt po zakończeniu; nie mieszaj liczby pojedynczej i mnogiej w jednym batchu |
| CPC i wolumen z Ads | Google Ads API przez `scripts/google/ads_call.sh` — `:generateKeywordHistoricalMetrics` / `:generateKeywordIdeas` (pierwsze użycie tych metod — sprawdź na jednej frazie) oraz `search_term_view` (co realnie wpisali ludzie, którzy kliknęli nasze reklamy) | koszt zerowy |
| SERP | `scripts/dfs_serp.py` (mobile) — najpierw sprawdź `data/seo/2026-09-09-serp-*.json` | ok. 3–5 fraz na produkt |
| zapytania ofertowe | MCP `query_db` na `wpfz_posts` (`post_type='agria_inquiry'`) + `wpfz_postmeta` (`_source_url`, `_product_name`) | tylko odczyt |
| OLX | `data/olx/market/2026-08-28.json` | bez nowych zapytań do API OLX |

Frazy do zbadania **na każdy produkt** (minimum): nazwa produktu i marka; nazwa + zastosowanie; nazwa + dawkowanie / „ile na hektar";
nazwa + cena; nazwa + producent / kopalnia / lokalizacja zakładu; rodzaj ogólny (np. „wapno węglanowe granulowane"); frazy
porównawcze (np. „agrobielik 70 czy 90", „wapno tlenkowe czy węglanowe"). Wolumen zero z planera to „poniżej progu" — sprawdź
w GSC, czy zapytanie mimo to się pojawia.

---

## 5. Kolejność pracy

1. **Start:** przeczytaj podsumowanie poprzedniego wątku, `CLAUDE.md` projektu, memory `feedback_agria_params_from_datasheets`
   i `feedback_agria_architektura_wokol_kart`. Zweryfikuj mapę z §2 (lista PDF-ów, adresy kart).
2. **Pobierz wszystkie PDF-y** do `data/produkty/pdf/` i wyciągnij tekst. Zapisz w `docs/produkty/README.md`, który PDF
   jest czyj, i listę PDF-ów bez produktu w WC.
3. **PILOT — Agrobielik 70 (#310).** Wypełnij cały szablon z §3, łącznie z frazami, GSC, Ads, SERP i konkurencją.
   **Pokaż plik Jankowi (link na auratest + treść w czacie) i czekaj na akcept szablonu.** Nie ruszaj kolejnych produktów przed akceptem.
4. Po akcepcie — pozostałe 18 produktów, w kolejności: najpierw te z wyświetleniami bez kliknięć i te, z których przyszły zapytania
   (Oxyfertil 90, Bielik, wapno palone mielone, kreda granulowana, węglanowe odm. 04, #314, #317), potem reszta.
5. **Macierz fraz:** `docs/produkty/_macierz-fraz.csv` — produkt · fraza · typ · wolumen · CPC · nasz URL w GSC · pozycja · wyświetlenia.
6. **Indeks:** `docs/produkty/README.md` — tabela 19 produktów: rodzaj, producent/zakład, frakcja, główne zastosowania, kategoria dziś,
   stan karty (dobrze / luki / rozbieżności), główne frazy z popytem, pozycja dziś, zapytania ofertowe.
7. **Zestawienie dla Janka na koniec** (osobny plik `docs/produkty/_WNIOSKI.md`): które produkty są dobrze zrobione, które mają luki,
   jakie są rozbieżności z kartami, gdzie jest popyt bez pokrycia, jakie grupy produktów wynikają z kart (rodzaj, zakład, zastosowanie) —
   **jako fakty do decyzji D1–D4, bez rekomendacji architektury**. Pytania, które zostały — quizem.

---

## 6. Czego NIE robisz

- Nie zmieniasz niczego na stronie ani w bazie. Nie zgłaszasz adresów do Google.
- Nie proponujesz nowych stron, kategorii, przekierowań ani zmian w reklamach.
- Nie poprawiasz parametrów ani nazw — rozbieżności tylko zapisujesz.
- Nie wyciągasz parametrów „z wiedzy" o wapnie. Czego nie ma w karcie — zapisujesz jako brak.
- Nie aktualizujesz rejestru zadań poza jednym wierszem „baza wiedzy produktowej — w toku / zrobione".

## 7. Zrobione =

- `docs/produkty/<slug>.md` × 19 według szablonu, każde twierdzenie ze źródłem;
- `docs/produkty/README.md` (indeks + mapa PDF), `docs/produkty/_macierz-fraz.csv`, `docs/produkty/_WNIOSKI.md`;
- surowe dane w `data/produkty/` (PDF + txt, JSON z GSC / DFS / Ads);
- koszt DataForSEO podany w podsumowaniu;
- pliki wystawione na `https://auratest.pl/fe4f58fec53ctmp/` i pokazane Jankowi linkiem, wnioski także w treści czatu.
