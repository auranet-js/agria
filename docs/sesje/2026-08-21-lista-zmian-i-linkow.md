# Sesja 2026-08-21 — pełna lista dotkniętych adresów i zasobów

> Wszystko, co zmieniło stan produkcji w tym wątku. Sprawdzone `curl` po zmianie
> (wszystkie **HTTP 200**, TTFB 0,27–0,47 s) oraz obejrzane przez Puppeteer na emulacji
> iPhone'a 390×844 DPR 2 i przez Chrome MCP na desktopie 1464×812.

## A. Adresy edytowane bezpośrednio — 7

| URL | Co zmienione | Zadanie |
|---|---|---|
| https://agria.pl/wapnowanie-gleby/ | `rank_math_title`, `rank_math_description` | T-053 |
| `https://agria.pl/ile-wapna-granulowanego-na-ha/` | `rank_math_title` (61 → 55 zn.), `rank_math_description` | T-053 |
| `https://agria.pl/jak-stosowac-wapno-nawozowe/` | meta, `focus_keyword`, **`post_title`**, **treść: terminarz IUNG** (tabela terminów, grupy upraw, ziemniaki/parch, lucerna, podział dawki) | T-053 + T-055 |
| `https://agria.pl/kalkulator-wapnowania/` | `rank_math_title` (usunięte dublowanie frazy z hubem), `rank_math_description` | T-053 |
| `https://agria.pl/wapno-granulowane/` | blok kontaktowy w hero, kotwica `#oddzwonimy`, formularz, końcowe CTA; **kolumna tekstu 852 px** (było 1440); **siatka 3 produktów** | T-059, T-063, T-064 |
| `https://agria.pl/wapno-nawozowe/` | jw.; **kolumna tekstu 852 px**; **siatka 14 produktów** | T-059, T-063, T-064 |
| `https://agria.pl/wapno-do-stabilizacji-gruntow/` | **kolumna tekstu 852 px**; **siatka 1 produktu** | T-063, T-064 |

## B. Adresy, którym zmienił się render przez naprawę szablonu (H1) — 11

Nie edytowane pojedynczo. Zmiana w widgecie nagłówka szablonu Elementora „Agria Single Post” (ID 2171)
i w widgecie hero strony głównej (ID 321). **Przed: zero H1. Po: dokładnie jeden H1 z tytułem.**

| URL | H1 po zmianie |
|---|---|
| `https://agria.pl/` | NAWOZY WAPNIOWE I SUROWCE PRZEMYSŁOWE |
| `https://agria.pl/wapnowanie-gleby/` | Wapnowanie gleby – kiedy, ile i jakie wapno stosować |
| `https://agria.pl/ile-wapna-granulowanego-na-ha/` | Ile wapna granulowanego na hektar? Dawki i stosowanie |
| `https://agria.pl/jak-stosowac-wapno-nawozowe/` | Kiedy wapnować pole? Terminy, technika i błędy |
| `https://agria.pl/wapno-nawozowe-na-trawnik/` | Wapno nawozowe na trawnik – kiedy, ile i jakie stosować |
| `https://agria.pl/higienizacja-osadow-sciekowych-wapnem/` | Higienizacja i stabilizacja osadów ściekowych wapnem |
| `https://agria.pl/czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/` | Czy wapnować czy nie wapnować stawy karpiowe? |
| `https://agria.pl/wykwity-na-murze/` | Wykwity – jak powstają i skąd się biorą na murze? |
| `https://agria.pl/cement-czym-jest-jak-powstaje-i-jakie-sa-jego-klasy/` | Cement – czym jest, jak powstaje i jakie są jego klasy? |
| `https://agria.pl/jak-murowac-klinkier/` | Jak murować z cegły klinkierowej – zasady bez wykwitów |
| `https://agria.pl/tynki-rodzaje-kategorie/` | Tynki – rodzaje, kategorie i zasady wykonania |

## C. Adresy z nowym paskiem kontaktu na telefonie — 24

Moduł `modules/call-bar/` renderuje pasek wyłącznie przy `pointer:coarse` i szerokości ≤1024 px.
Treść tych stron nietknięta.

**19 kart produktów**

https://agria.pl/kreda-malarska/kreda-malarska/
https://agria.pl/paszarstwo/kreda-pastewna/
https://agria.pl/wapno-do-oczyszczalni/wapno-palone-mielone/
https://agria.pl/wapno-hydratyzowane/bielik/
https://agria.pl/wapno-nawozowe-rolnictwo/agrobielik-70/
https://agria.pl/wapno-nawozowe-rolnictwo/agrobielik-90/
https://agria.pl/wapno-nawozowe-rolnictwo/dolomit/
https://agria.pl/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/
https://agria.pl/wapno-nawozowe-rolnictwo/kreda-nawozowa-granulowana/
https://agria.pl/wapno-nawozowe-rolnictwo/kreda-nawozowa-sypka/
https://agria.pl/wapno-nawozowe-rolnictwo/mieszanka-tlenkowo-weglanowa/
https://agria.pl/wapno-nawozowe-rolnictwo/oxyfertil-90/
https://agria.pl/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/
https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-granulowane/
https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/
https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-04/
https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-05/
https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/
https://agria.pl/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/

**5 kategorii** (te, które faktycznie odpowiadają treścią)

https://agria.pl/wapno-nawozowe-rolnictwo/
https://agria.pl/paszarstwo/
https://agria.pl/wapno-do-oczyszczalni/
https://agria.pl/wapno-hydratyzowane/
https://agria.pl/kreda-malarska/

**Korekta wobec pierwszej wersji tej listy:** `/wapno-do-stawow/`, `/wapno-do-sadu/`
i `/wapno-nawozowe-hurt/` **nie należą tutaj** — te trzy puste kategorie odpowiadają **301**
(przekierowanie z lipca na `/oferta/`), więc pasek się na nich nie renderuje. Sprawdzone `curl` 21.08.
To są dokładnie te trzy kategorie, które T-056 i T-057 mają wypełnić treścią i produktami.

**2 landingi** — wymienione w sekcji A.

**Świadomie BEZ paska:** strona główna, https://agria.pl/wapnowanie-gleby/, https://agria.pl/kontakt/,
https://agria.pl/poradniki/ i pozostałe strony statyczne — zweryfikowane, że pasek się tam nie pojawia.

## D. Pliki i rekordy na produkcji

| Zasób | Zmiana | Kopia |
|---|---|---|
| `wp-content/plugins/agria-by-auranet/modules/call-bar/call-bar.php` | **nowy plik** | snapshot w repo `src/plugins/…` |
| `wp-content/plugins/agria-by-auranet/agria-by-auranet.php` | rejestracja modułu `call-bar` | `.bak-20260821-123401` |
| `wpfz_postmeta` `_elementor_data` post 2171 | `"header_size":"h1"` w widgecie `12b047b2` | `data/backups/T-061-…md` |
| `wpfz_postmeta` `_elementor_data` post 321 | `"header_size":"h1"` w widgecie `1c03dac` | jw. |
| `wpfz_postmeta` `rank_math_*` posty 729, 2074, 2741, 2743 | nowe title/description | `data/backups/T-052-blokA-…md` |
| `wpfz_posts` 2743, 2751, 2757 | `post_content`, `post_title` | `~/agria-backups/post-275*-przed-T059-20260821.html` |

## E. Google Ads, konto 674-207-1446

| Zasób | Zmiana |
|---|---|
| Kampania **AGRIA - Rolnictwo** | +26 wykluczeń obcych marek (85 łącznie), −3 przeniesione na poziom grup, budżet **34 → 26 zł/dz** |
| Kampania **AGRIA - Marka** | stawka grupy Brand **0,50 → 3,00 zł**, budżet **6 → 5 zł/dz** |
| Kampania **AGRIA - Paszarstwo** | **nowa**, 9 zł/dz, grupa „Kreda pastewna” 1,20 zł, 13 fraz, 23 wykluczenia, RSA → `/paszarstwo/kreda-pastewna/` |
| Grupy Rolnictwa (×3) | +18 wykluczeń (`pastewna`, `kury`, `drób`, `kur niosek`, `kurnik`, `paszowa`) |
| Assety połączeń 664 i 781 | harmonogram pn–pt 8–16 **+ sobota 8–14** |

## F. Co widać oczami klienta — pomiary

**Telefon (iPhone 390×844), landing `/wapno-nawozowe/`:**

| Element | Pozycja | Nad zgięciem |
|---|---|---|
| H1 „WAPNO NAWOZOWE” | — | tak |
| Cena „od 36 / od 220 zł/t netto” | y 464 | **tak** |
| „Zadzwoń: 664 393 062” | y 529 | **tak** |
| Pasek przyklejony | y 798–844, `fixed` | **tak** |
| Formularz „oddzwonimy” | y 5718 (75%) | nie |

Dokument 7 656 px, 1 152 słowa, ładowanie 1,9 s. Tabele nie wychodzą poza ekran
(`scrollWidth` 390 = `clientWidth` 390; najszersza tabela 388 px).

**Desktop (Chrome MCP, 1464×812):** blok kontaktowy renderuje się bezpośrednio pod wstępem,
tabela terminarza z podpisem źródłowym IUNG mieści się w kolumnie treści, H1 na stronie głównej
i na landingach obecne.

## G. Znalezione przy oglądaniu, do rozstrzygnięcia

1. **Baner zgód zasłania całą ścieżkę kontaktu na telefonie.** Pomiar na `/wapno-nawozowe/`
   dla wejścia pierwszy raz (czyli dla każdego kliknięcia z reklamy): baner zajmuje
   **450 z 844 px = 53% ekranu**, zakrywa **i** przycisk „Zadzwoń” w hero (y 529–563),
   **i** pasek przyklejony (y 798–844). Do czasu kliknięcia „Akceptuj” nie widać ani numeru,
   ani ceny. → zgłoszone jako **T-062**.
2. **`/wapno-nawozowe/` — cena „od 36 zł/t”** to najniższa pozycja cennika (węglanowe z magnezem
   odm. 05), oznaczona w `CENNIK_PAWEL_2026-08-07.md` jako możliwa literówka. Teraz stoi nad zgięciem
   na stronie docelowej reklam. Do potwierdzenia u Pawła.
3. **Karta kredy pastewnej podaje „minimum 37% CaO”** — rynek i karty producentów podają
   **37% Ca**, nie CaO (węglan wapnia to ok. 40% Ca / 56% CaO). To ta sama pozycja, którą
   `FAKTY_KLIENTA` §9 zgłasza jako opis kredy parametrami wapna tlenkowego. Karta jest od dziś
   stroną docelową reklam → blokada publikacji w **T-054** obowiązuje.
4. **`/oferta/` nadal bez H1** — zgłoszone jako T-061 w kolejce.
