# T-026 — dlaczego sześć adresów nie wchodzi do indeksu

> Diagnoza z 19.08.2026. Wszystkie liczby z GSC URL Inspection API i Search Analytics API,
> zakres 19.05–18.08.2026. **Zadanie było diagnostyczne — to jest jego produkt, nie zmiana na stronie.**

## Wniosek

**Dla każdego z sześciu adresów istnieje już inna strona agria.pl, którą Google zaindeksował
i która rankuje na tę samą intencję.** Google nie pobiera drugiej strony o tym samym pytaniu —
i dlatego cztery z nich mają status „URL is unknown", mimo że siedzą w sitemapie od 41 dni
i są linkowane z zaindeksowanego huba.

To ten sam mechanizm, który ADR `2026-08-11-podzial-rol-ads-seo.md` zmierzył na landingach
(„wapno bielik": sześć adresów na jedną frazę → pozycja 15,3). Różnica jest taka, że tam
kanibalizacja obniżała pozycje, a tutaj **blokuje samo pobranie**.

## Co zostało wykluczone — po kolei, z dowodem

| Hipoteza | Sprawdzenie | Wynik |
|---|---|---|
| Sitemapa niezgłoszona albo z błędami | GSC Sitemaps API | `sitemap_index.xml` pobrana **13.08**, 48 URL-i, **0 błędów, 0 ostrzeżeń** |
| Serwer odrzuca Googlebota | `curl -A "Googlebot"` na wszystkich sześciu | **200** dla każdego, pełna treść (104–160 KB) |
| `noindex` na stronie | nagłówek `robots` przez Googlebota | `index, follow` na wszystkich sześciu |
| `robots.txt` blokuje | odczyt pliku | blokuje wyłącznie `wc-logs`, `woocommerce_uploads`, `add-to-cart`, `wp-admin` |
| Strony z `noindex` w sitemapie | skan wszystkich pięciu sitemap, każdy URL osobno | **zero** stron z `noindex` |
| Wyczerpany budżet crawlowy | `lastCrawlTime` dla stron różnych typów | Google crawluje **na bieżąco**: strona główna **18.08**, kategoria **16.08**, karta produktu **14.08**, hub **15.08** |
| Geoblok (wdrożony 14.08) | jw. — crawle po 14.08 są świeże | nie blokuje; problem trwa od lipca, geoblok jest młodszy |

**Rozstrzygające porównanie:** `/wapnowanie-gleby/` i `/ile-wapna-granulowanego-na-ha/` powstały
**tego samego dnia** (lastmod 2026-07-09), leżą w tej samej sitemapie, mają tę samą strukturę.
Hub jest **zaindeksowany i crawlowany 15.08**. Poradnik — **nigdy nie pobrany**.
Różnicy nie da się wytłumaczyć techniką.

## Sześć adresów, sześć konkurentów wewnętrznych

| Adres poza indeksem | Status GSC | Kto już rankuje na tę intencję | Dowód |
|---|---|---|---|
| `/ile-wapna-granulowanego-na-ha/` | unknown | **`/wapnowanie-gleby/`** | „ile wapna granulowanego na hektar" poz. **7,7**, 1 289 wyśw.; „ile wapna granulowanego na ha" poz. 9,8 |
| `/jak-stosowac-wapno-nawozowe/` | unknown | **`/wapnowanie-gleby/`** | „stosowanie wapna" poz. 13,3; „kreda nawozowa kiedy stosować"; „nawozy wapniowe kiedy stosować" — komplet fraz na hubie |
| `/higienizacja-osadow-sciekowych-wapnem/` | unknown | **`/wapno-do-oczyszczalni/`** (kategoria) | „higienizacja osadów ściekowych" **113 wyśw.** poz. 17,8; „wapnowanie osadów ściekowych" 94 wyśw.; „urządzenie do higienizacji…" 47 wyśw. |
| `/wapno-nawozowe-na-trawnik/` | unknown | — | **zero wyświetleń** na jakąkolwiek frazę z „trawnik" w całym serwisie. Nie ma konkurenta, bo nie ma popytu |
| `/kreda-malarska/` (kategoria) | Discovered | **`/kreda-malarska/kreda-malarska/`** (karta produktu) | „kreda malarska" poz. **8,9**, 53 wyśw. — karta wygrywa z kategorią |
| `/wapno-do-stabilizacji-gruntow/` | Discovered | — | **zero wyświetleń** na frazy z „stabiliz". Landing T-024, sezonowo poza popytem |

## Co z tego wynika — do decyzji, nie do wykonania

Trzy różne sytuacje, trzy różne odpowiedzi. **Żadna nie jest „zgłoś do Indexing API czwarty raz"** —
trzy zgłoszenia już były i nie zadziałały, bo problem nie leży po stronie odkrycia.

1. **Pokrycie intencji z hubem** (`ile-wapna-granulowanego-na-ha`, `jak-stosowac-wapno-nawozowe`).
   Hub rankuje i zbiera wyświetlenia. Poradniki dublują jego temat. Do rozważenia: scalenie
   wartościowych fragmentów do huba i 301, albo przepisanie pod intencję, której hub nie obsługuje.
   **Zostawienie jak jest oznacza dwie strony konkurujące o jedno pytanie** — dokładnie to,
   czego zakazuje ADR z 11.08.
2. **Pokrycie z kategorią** (`higienizacja-osadow-sciekowych-wapnem`). Kategoria `/wapno-do-oczyszczalni/`
   ma realny wolumen (113 + 94 + 47 wyświetleń) i słabe pozycje (14–18). Treść poradnika jest
   materiałem, który mógłby te pozycje podnieść — **wewnątrz kategorii**, nie obok niej.
3. **Brak popytu** (`wapno-nawozowe-na-trawnik`, `wapno-do-stabilizacji-gruntow`). Zero wyświetleń
   na frazy tematyczne. Indeksacja niczego tu nie zmieni. Naturalne miejsce to cel kampanii Ads
   (poza indeksem, zgodnie z ADR) albo pozycja „Unieważnione".
4. **Kategoria kontra karta** (`kreda-malarska`). Karta produktu wygrywa z kategorią na tę samą frazę.
   Wiąże się z długiem `/kreda-malarska/kreda-malarska/` (zdublowany człon w ścieżce), świadomie
   odłożonym przy T-010. Do rozstrzygnięcia razem z nim.

## Zauważone przy okazji, poza zakresem

- **Sitemapa RankMath podaje nieaktualne `lastmod`.** `/do-pobrania/` ma w niej `2026-06-29`,
  choć strona była zmieniana **19.08** (T-008/T-009). Pliki `uploads/rank-math/*.xml` są cache'owane
  i nie odświeżyły się po edycji. To osłabia zgłoszenie reindeksacji z T-027 — Google widzi w sitemapie
  datę sprzed dwóch miesięcy.
- **Dwie sitemapy naraz w GSC**: `sitemap_index.xml` (RankMath, zgłoszona 19.05) i `wp-sitemap.xml`
  (natywna WordPressa, zgłoszona 30.04.2025). Obie pobierane, obie z 48 URL-ami. Duplikat do sprzątnięcia.
- `/czy-wapnowac-czy-nie-wapnowac-stawy-karpiowe/` ma w GSC werdykt „Excluded by `noindex`"
  z crawla **18.04**, ale na żywo `noindex` nie ma. Zaległy werdykt, jak przy `/do-pobrania/`.
