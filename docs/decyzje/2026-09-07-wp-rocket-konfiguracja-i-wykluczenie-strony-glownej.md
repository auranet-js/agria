# WP Rocket na agria.pl — konfiguracja, tryb bezpieczny i wykluczenie strony głównej z odraczania

> **Data:** 2026-09-07 · **Zakres:** ryczałt R · **Dotyczy:** T-131, T-130
> **Stan wejściowy:** Janek zainstalował WP Rocket 3.23.3.3 na produkcji, konfigurację robiło Auranet.
> **Prompt wątku:** `docs/prompty/wdrozenie/2026-09-08-WP-ROCKET.md`
> **Backup przed zmianami:** `~/agria-backups/przed-konfiguracja-wp-rocket-2026-09-07-20260907-170419.sql` (810 wierszy tabeli `wpfz_options`, poza web rootem)

---

## 1. Decyzja

Odraczanie JavaScriptu (`delay_js`) włączone w **trybie bezpiecznym** z jednym wykluczeniem
treściowym na tagi Google, oraz **wyłączone punktowo na stronie głównej** wpisem
`_rocket_exclude_delay_js = 1` w meta strony 321.

Konfiguracja docelowa:

```
delay_js = 1
delay_js_execution_safe_mode = 1
delay_js_exclusions = ["googletagmanager.com/gtm.js"]
defer_all_js = 1
lazyload = 1 · lazyload_iframes = 1 · lazyload_youtube = 1
minify_css = 1 · minify_js = 1 · minify_concatenate_js = 0
remove_unused_css = 0 · async_css = 0
cache_mobile = 1 · do_caching_mobile_files = 1 · cache_logged_user = 0
postmeta 321: _rocket_exclude_delay_js = 1
```

Trzy ostatnie linie bloku minifikacji i cache to stan zastany po instalacji — nie zmienialiśmy go,
odpowiada wzorcowi z victorini.

## 2. Dlaczego tryb bezpieczny zamiast listy wykluczeń z victorini

Tryb bezpieczny Rocketa wyklucza z odraczania jQuery, wzorzec `js-(before|after)` oraz **wszystko
spod `/wp-content/` i `/wp-includes/`** (`Settings::get_safe_mode_exclusions()`). Sprawdzone na
renderze agrii, co to realnie obejmuje:

| warstwa | jak wychodzi w HTML | los |
|---|---|---|
| Complianz — plik | `/wp-content/plugins/complianz-gdpr-premium/cookiebanner/js/complianz.min.js` | natychmiast (ścieżka) |
| Complianz — konfiguracja | inline `cmplz-cookiebanner-js-extra`, zawiera `/wp-content/` | natychmiast (treść) |
| Complianz — inicjalizacja | inline `cmplz-cookiebanner-js-after` | natychmiast (wzorzec `js-after`) |
| Elementor, Elementor Pro, WooCommerce, JetSmartFilters, motyw | pliki spod `/wp-content/` | natychmiast |
| GTM + `gtag('consent','default')` | **inline**, bez `/wp-content/` w treści | wykluczony ręcznie |
| **reCAPTCHA** | `https://www.google.com/recaptcha/api.js?render=…` | **odroczona** |
| **skrypt formularza AGRIA** | surowy inline `<script>`, bez `/wp-content/` w treści | **odroczony** |

Czyli tryb bezpieczny odracza dokładnie te dwie pozycje, o które chodziło w T-131, i chroni całą
resztę **bez przepisywania osiemnastopozycyjnej listy z victorini**. Warstwa zgód jest przy tym
załatwiona ustawieniem, zero kodu — zgodnie z `CLAUDE.md` §5 i memory
`feedback_agria_complianz_ustawieniami_zero_kodu`.

To nie jest wygodnictwo. Transient `rocket_check_key_errors` na produkcji mówi „Walidacja licencji
nie powiodła się", a konsekwencją techniczną jest to, że **dynamiczne listy wykluczeń z SaaS
Rocketa się nie pobiorą**. Nie ma na czym polegać poza tym, co wpiszemy sami — więc opieramy się
na liście wbudowanej w kod wtyczki, nie na pobieranej. (Sama licencja to temat Janka, nie doradzamy.)

## 3. Dlaczego tagi Google NIE są odraczane

Decyzja Janka 07.09, zgodna z victorini. Powód mocniejszy, niż zakładał prompt: ten sam inline,
który ładuje `gtm.js`, niesie **`gtag('consent','default', …)`**. Odroczenie przesunęłoby domyślne
Consent Mode za pierwszą interakcję, podczas gdy Complianz odpala swoje kategorie wcześniej.
Skrypt ma już atrybut `data-category="functional"`, czyli **jednego bramkarza** — dokładanie
drugiego w postaci Rocketa to ryzyko, którego przy czterech zdarzeniach konwersji kwartalnie
(T-110) i tak byśmy nie zmierzyli.

Koszt decyzji: **313 KB** zostaje na stronie. Zweryfikowane po wdrożeniu, że kolejność w `dataLayer`
jest poprawna: `default_consent` → `cmplz_event_*` → `gtm.js`.

## 4. Dlaczego strona główna jest wykluczona z odraczania

**To jest ustalenie tej sesji, nie było go w planie.** Po włączeniu odraczania strona główna
straciła LCP: **3,7 → 8,0 s**, wynik 0,83 → 0,64, mimo że transfer spadł 930 → 812 KB.

Wykluczenie przyczyn po kolei, każda osobnym pomiarem PSI mobile:

| co sprawdzone | wynik | wniosek |
|---|---|---|
| CDN nazwa.pl podaje stary render? | `x-cdn-nazwa.pl-policyused: cdn=disabled`, `na-ls-cache-enabled: off`, `last-modified` po purge | nie, pomiar świeży |
| `?nowprocket=1` (Rocket ominięty) w tej samej chwili | **3,3 s / 0,84** | regres jest realny, nie szum |
| `defer_all_js = 0` | 7,3 s wobec 7,7 s | **bez wpływu** |
| `lazyload = 0` | 8,2 s | **bez wpływu** |
| `delay_js = 0` | **3,8 s / 0,84** | **przyczyna** |

Mechanizm siedzi w markupie: tło hero strony głównej jest przypisane do
**`.elementor-motion-effects-layer`** — warstwy, którą **tworzy JavaScript Elementora**, nie HTML.
Odraczanie wstrzymuje ją do pierwszej interakcji użytkownika, a LCP jest mierzone wcześniej.
Dotyczy to więc także **prawdziwych użytkowników i danych polowych CrUX**, nie tylko laboratorium PSI.

Wykluczenie strony głównej nic nie kosztuje, bo **strona główna nie ma formularza ani reCAPTCHY** —
sprawdzone w HTML. Odraczanie nie miało tam czego zdejmować.

Zasięg wzorca w serwisie (próbka 12 adresów): motion-effects występuje na stronie głównej,
`/poradniki/` (7 warstw) i na kartach produktów. **Karty mają jedno i drugie naraz** — parallaks
i reCAPTCHĘ — i tam bilans wychodzi jednoznacznie na korzyść odraczania (patrz §5), więc
wykluczamy wyłącznie stronę główną.

## 5. Pomiary

PSI mobile. Kolumna „przed" dla strony głównej i `/wapno-nawozowe/` to stan z 07.09 sprzed
instalacji Rocketa; dla karty produktu — pomiar z tej sesji przy wyłączonym odraczaniu, bo
07.09 karty nie mierzyliśmy.

| adres | przed | po |
|---|---|---|
| `/` | LCP 3,7 s · 0,83 · 930 KB | LCP **3,7 s** · 0,84 · **811 819 B** |
| `/wapno-nawozowe/` | LCP 5,7 s · 0,60 · **3 373 379 B** | LCP **4,8 s** · **0,77** · **1 137 401 B** |
| `/wapno-nawozowe-rolnictwo/agrobielik-90/` | LCP 11,8 s · 0,57 · **2 575 678 B** | LCP **6,2 s** · **0,73** · **1 374 856 B** |
| TTFB z cache, mobile | 1,40 s | **0,033 s** |

Największy zysk jest na kartach produktów — **11,8 → 6,2 s i −1,2 MB**, razy dziewiętnaście kart.
Regres na 62 adresach (`data/seo/audyt-2026-08-24/urls.txt`): 50×200, 11×301, 1×302, **zero 404**;
wszystkie przekierowania to znane historyczne kategorie i `/cart/`.

Weryfikacja zrobiona **na wersji z cache**, nie na podglądzie zalogowanego — atrybut
`type="rocketlazyloadscript"` dostały wyłącznie reCAPTCHA i inline formularza, w tej kolejności,
a na stronie głównej nie ma go wcale. Baner zgód wstaje bez interakcji, sprawdzone po wyczyszczeniu
ciasteczek `cmplz_*` w przeglądarce.

## 6. Konsekwencje i pułapki na przyszłość

1. **`?cb=` przestało być narzędziem weryfikacji.** Omija cache Rocketa i zwraca wersję, której
   użytkownik nie dostaje. Każdy pomiar: rozgrzewka jednym żądaniem na adres, potem pomiar na
   czystym adresie. Do świadomego porównania „z Rocketem / bez Rocketa" służy `?nowprocket=1` —
   i wynik trzeba wtedy opisywać jako stan bez Rocketa, nie jako doświadczenie użytkownika.
2. **Nowa strona z parallaksem w hero odziedziczy ten sam problem.** Zanim taka strona pójdzie
   pod reklamy, sprawdź LCP; jeśli spada, albo zdejmij efekt ruchu z hero, albo dodaj
   `_rocket_exclude_delay_js` — ale tylko gdy na stronie nie ma formularza.
3. **`defer_all_js` zmierzone jako neutralne** na obu adresach (7,3 wobec 7,7 s). Zostawione
   włączone dla zgodności z victorini, ale nie jest pozycją, która cokolwiek dowozi — przy
   przyszłej diagnozie można je wyłączyć bez straty.
4. **Beacon Rocketa nie ma wpisu dla strony głównej.** Tabela `wpfz_wpr_above_the_fold` ma wpisy
   dla `/wapno-nawozowe/` i `/wapno-granulowane/`, brak dla `/`. Bez nich lazyload działa tam bez
   wiedzy o obrazach nad zgięciem — patrz T-132.
5. **Nonce formularza w cache'owanym HTML jest bezpieczny.** `purge_cron_interval` to 10 godzin,
   a nonce WordPressa żyje 24 godziny, więc „Token wygasł" nie wyskoczy. Gdyby ktoś kiedyś wydłużył
   czas życia cache powyżej doby — wyskoczy.
6. **Osobne pliki cache dla telefonów nie bronią przed powrotem wideo hero.** Sprawdzone: HTML
   mobilny i desktopowy jest bajt w bajt identyczny (186 060 B), a wideo wygasza Elementor po
   stronie przeglądarki wedle szerokości okna, nie po User-Agencie. Plik to dziś **2 408 832 B**,
   nie 22 MB — podmieniony 07.09 w `e719836`. Obie opcje są włączone i zostają, ale teza
   „bez nich 22-megabajtowe wideo wróci tylnymi drzwiami" była błędna.

## 7. Czego ta decyzja nie obejmuje

- ~~Test wysyłką formularza przez wylogowaną przeglądarkę~~ — **wykonany 07.09 o 17:39:48**, zgłoszenie z `/zamowienia/` przeszło (rekord `agria_inquiry` 2816, potem do kosza). Serwer odrzuca wysyłkę z pustym lub nieważnym tokenem i nie tworzy wpisu, więc powstanie rekordu **dowodzi, że odroczona reCAPTCHA zdążyła wydać token**. T-131 zamknięte. ⚠️ reCAPTCHA v3 jest niewidoczna, a plakietkę ukrywa CSS wtyczki — dowodem jest rekord, nie widok strony.
- **Obrazy 1 445 422 B w 18 plikach** na landingu — osobna pozycja, świadomie nie mieszana
  do tego wdrożenia.
- **Licencja WP Rocket** — temat Janka, nie doradzamy.
