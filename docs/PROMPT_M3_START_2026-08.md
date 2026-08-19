# Prompt: realizacja M3 (sierpień 2026) — Ads live do 15.08 + domknięcie SEO do 31.08

> **Jak używać:** wklej całość jako pierwszą wiadomość w nowym wątku `cd ~/projekty/agria && claude`.
> **Data wystawienia promptu:** 2026-08-06. **Twardy deadline kampanii: 14.08** (15.08 to sobota i święto).
> **Kontekst handlowy:** mail do klienta wysłany 06.08 (`docs/offers/2026-08-PLAN_ADS_3MIES.md`) — zadeklarowaliśmy start reklam „ok. 14 sierpnia". To jest zobowiązanie wobec klienta, nie plan życzeniowy.

---

## 0. Zanim cokolwiek zrobisz — wczytaj stan i ZWERYFIKUJ GO NA ŻYWO

1. **Memory projektu:** `~/.claude/projects/-home-host476470-projekty-agria/memory/MEMORY.md`, obowiązkowo `project_agria_start_here_m2`, `project_agria_ads_sezonowosc`, `project_agria_render_caching`, `project_agria_mcp_writebuild`, `feedback_agria_prefer_mcp_curl_allowlisted`, `feedback_agria_no_self_criticism_built_site`.
2. **Tożsamość:** ładuje się z memory `feedback_agria_auranet_decyduje` + `CLAUDE.md` §7. Auranet JEST działem marketingu AGRII. Decyzje marketingowe podejmujemy my, klienta pytamy wyłącznie o fakty produktowe. (`docs/MASTER_PROMPT.md` usunięty 19.08.2026 — dublował globalny CLAUDE.md i podawał nieaktualnych producentów.)
3. **Repo:** `docs/raporty/2026-07.md` (raport M2 — pełna diagnoza), `docs/offers/2026-08-PLAN_ADS_3MIES.md` (co obiecaliśmy klientowi), `docs/seo/BACKLOG_SEZON_2026-07-14.md` (bloki A–F), `docs/seo/ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md`.
4. **Commity:** `git log --since=2026-07-25 --pretty=format:'%ad %h %s' --date=short`.

**Zasada nadrzędna:** stan z dokumentów jest z 3 sierpnia. **Zanim zaplanujesz cokolwiek — przepuść listę z §1 przez weryfikację live.** Część rzeczy mogła się ruszyć sama (crawl), część mogła się zepsuć. W planie ląduje stan z live, nie z notatek.

---

## 1. Rewizja stanu — sprawdź to najpierw, jednym przebiegiem

Uruchom `scripts/gsc_inspect.py` i `scripts/gsc_pull.py`, dorzuć curl-e. Wypełnij tabelę faktami z **dzisiaj**:

| # | Co sprawdzić | Stan na 03.08 (do potwierdzenia lub obalenia) | Jak sprawdzić |
|---|---|---|---|
| 1 | 4 poradniki lipcowe + `/wapno-do-stabilizacji-gruntow/` | **„URL unknown to Google", `lastCrawl` pusty** mimo sitemapy, linkowania i 3× Indexing API | `scripts/gsc_inspect.py` |
| 2 | `/do-pobrania/` | GSC trzyma werdykt **„noindex" z crawlu 12.04**, live ma `index, follow` | URL Inspection + `curl` meta robots |
| 3 | Duplikat sitemapy | `wp-sitemap.xml` (natywna WP, 2025) zgłoszona obok RankMath | GSC Sitemaps API |
| 4 | Blok linkowania na kartach | **15 z 20** — brak m.in. na `/wapno-nawozowe-rolnictwo/agrobielik-70/` (flagowiec), `/kreda-malarska/kreda-malarska/`, `/wapno-do-oczyszczalni/wapno-palone-mielone/`, `/paszarstwo/kreda-pastewna/` | skan `product-sitemap.xml` + grep render |
| 5 | Kanibalizacja „wapno bielik" | **6 URL** na jedną frazę markową (210/mies.) | `gsc_pull.py` §6 |
| 6 | LCP mobile | **7,4 s** (home), 6,9 s (karta), 6,0 s (kategoria). Reszta PSI naprawiona (TBT 110 ms), SEO 100/100 | PSI v5, klucz `~/secrets/google/psi-crux-key.txt` |
| 7 | GA4 | ~60 ze 148 sesji to wejścia na **404 z demo motywu**; atrybucja martwa (5 sesji „organic" vs 221 klik GSC) — Consent Mode bez banera | GA4 Data API, wymiar `landingPage` + `sessionDefaultChannelGroup` |
| 8 | Element-cache Elementora | **wyłączony** (`elementor_element_cache_ttl = disable`) po incydencie 30.07 | `query_db` na `options` |
| 9 | Nagłówki bezpieczeństwa | 4 z 6 (jest HSTS, X-Frame, X-Content-Type, Referrer-Policy; brak CSP i Permissions-Policy) | `curl -I` |
| 10 | Menu | 3 pozycje (Sadownictwo/Rybactwo/Hurtownie) jako `draft` — **wracają dopiero we wrześniu z landingami**, nie ruszać | `project_agria_nav_debt_m4` |

**Jeśli punkt 1 nadal jest „URL unknown" — to jest najważniejsza rzecz w tym miesiącu.** Klientowi obiecaliśmy, że treści z lipca dociśniemy do wyników.

---

## 2. Ścieżka krytyczna — reklamy live do 14.08

Kolejność ma znaczenie: **landingi PRZED kampanią**. Reklama kierowana na stronę bez dopasowanej treści dostaje niższą ocenę jakości i płacimy więcej za kliknięcie.

### KROK A (6–9.08) — landingi produktowe. Bez tego nie ruszamy.

Dziś **nie ma ani jednej strony pod frazę o największym wolumenie**. To jest jednocześnie zadanie SEO z planu M3 i warunek sensownej kampanii — jedna robota, dwa efekty.

| Landing | Fraza główna | Wolumen (sierpień) | CPC |
|---|---|---|---|
| **wapno granulowane** | „wapno granulowane" | **9 900** (rok: 5 400 śr.) | 0,48 USD |
| **wapno nawozowe** | „wapno nawozowe" | 1 900 | 0,62 USD |

Wzorzec: `/wapno-do-stabilizacji-gruntow/` (LP z 14.07) + `docs/seo/BACKLOG_SEZON_2026-07-14.md` blok C. Każdy landing:
- exact-match H1 i title, self-canonical, `index, follow`,
- tabela parametrów z kart producentów (**wyłącznie z kart — `feedback_agria_params_from_datasheets`**), klasy normowe gdzie dotyczy,
- **sygnał logistyczny jako atut, nie bariera:** „dostępne: luz 24 t / big-bag 1000 kg / worek 25 kg", własna flota 3–24 t, dwa magazyny, terminy B2B — to jest narzędzie odsiewu hobbysty, patrz backlog §„Zasada przewodnia",
- CTA **„zapytaj o ofertę — podaj tonaż"**, zero ceny, zero koszyka,
- linkowanie z huba `/wapnowanie-gleby/`, z `/oferta/` i z kart produktów,
- JSON-LD, wpięcie do sitemapy, zgłoszenie przez `~/bin/index-submit`.

⚠️ **Sprzeczność do obejścia:** STR-02 (poprawka Pawła z 29.06) zdjęła formy dostawy z 19 kart, bo „zapis nas ogranicza". Na landingach wraca **jako możliwość, nie wymóg** — to nie jest cofnięcie poprawki Pawła. Jeśli masz wątpliwość, zapytaj Janka; nie pisz do klienta.

### KROK B (7–11.08) — konto i pomiar

1. **Założenie konta Google Ads — ręczna akcja Janka** (UI + karta płatnicza Janka, zgodnie z mailem do klienta: „budżet opłacam z góry i podpinam do swojej karty"). API nie założy konta bez MCC, a Auranet prowadzi konta jako direct (patrz `ads_call.sh` w aseosystem: *„direct account, NIE pod MCC"*). **Zgłoś to Jankowi jako pierwsze — to blocker, którego sam nie zdejmiesz.**
   Po założeniu: CID dopisz do `~/.claude/projects/-home-host476470-projekty/memory/reference_google_apis.md` i zrób helper `scripts/google/ads_call.sh` (wzorzec: `~/projekty/aseosystem/scripts/google/ads_call.sh`, podmień CID).
2. **Konwersje — zanim ruszy pierwsza reklama.** Bez nich kampania jest ślepa:
   - **telefon** — kliknięcie w `tel:` (numery per oddział wdrożone w STR-03, commit `1dfe5c5`),
   - **formularz** — `form_submit` (GA4 notuje 14/mies., w tym 12 z `/kontakt/`),
   - import konwersji z GA4 do Ads albo osobny tag w GTM (`GTM-TDC85TQN`, snippety Elementor Custom Code `Gtm-head` 2711 / `gtm-body` 2712 — **NIE GTM4WP**).
   - ⚠️ **Zweryfikuj przez GA4 Realtime API, nie przez przeglądarkę** — lokalny Chrome ma bloker maskujący GTM (`project_agria_analytics_stack`).
3. **Filtr ruchu 404** w GA4 — wejścia na `/produkt/fresh-avocado` i spółkę zawyżają dane o ~40%. Bez tego pomiar efektu kampanii będzie zaszumiony.

### KROK C (11–13.08) — budowa kampanii

**Dwie kampanie** (decyzja z maila do klienta, nie zmieniaj bez Janka):

**1. Rolnictwo (rdzeń budżetu).** Frazy phrase/exact: wapno granulowane, wapno nawozowe, wapno nawozowe granulowane, wapno magnezowe, kreda nawozowa, wapno węglanowe, wapno tlenkowe, wapno rolnicze, + long-tail „ile wapna na hektar / na ha" (mamy tam poz. 8,9 organicznie — reklama nad wynikiem organicznym to podwójna obecność w szczycie sezonu).

**Wykluczenia — to decyduje o rentowności.** Odsiewamy hobbystę, zostawiamy rolnika i instytucję:
`trawnik`, `ogród`, `działka`, `doniczka`, `5 kg`, `10 kg`, `kwiaty`, `basen`, `akwarium`, `budowlane`, `malarska`, `gaszone do ścian`, `praca`, `oferty pracy`, `sprzedam`, `olx`, `allegro`, `ceneo`, `używane`, `wikipedia`, `co to jest`, `wzór chemiczny`.
Uwaga: `/wapno-nawozowe-na-trawnik/` to nasz własny poradnik uznany w backlogu za błąd (F6) — **nie kierować na niego reklam**.

**2. Brandowa.** „agria", „agria wapno", „agrobielik", „bielik wapno", „oxyfertil", „ekograncali". Grosze za klik, obrona przed licytowaniem marki. Osobna kampania z małym budżetem — **nie mieszać z rolnictwem**, bo zaniży średni koszt konwersji i zafałszuje ocenę rdzenia.

**Ustawienia:**
- Budżet **40 zł/dzień** (1 200/mies.), podział ~85% rolnictwo / ~15% brand.
- **Harmonogram 24/7 — NIE wyłączać weekendów.** Dane własne GSC: frazy transakcyjne mają w niedzielę 19,6 wyśw./dzień vs 13,8 w poniedziałek (**+42%**). Rolnik szuka, gdy zszedł z pola (`project_agria_ads_sezonowosc`).
- Sieć wyszukiwania, **bez partnerów i bez display** na start.
- Lokalizacja: Polska. Rozszerzenia: lokalizacji (spięte z wizytówką Tarnów), połączeń, linków do podstron, objaśnień (własna flota, dwa magazyny, 37 lat, atesty).
- Prognoza kontrolna: **700–900 kliknięć/mies. przy koszcie 1,20–1,50 zł**. Jeśli po tygodniu realny CPC jest 2× wyższy — sprawdź ocenę jakości landingów, nie podnoś budżetu.

### KROK D (14.08) — start i smoke test
Kampanie ON. Sprawdź: wyświetlanie reklam (podgląd), poprawność linków docelowych, rejestrację konwersji testowej, brak 404 w URL-ach reklam, spójność UTM.

---

## 3. SEO do 31.08 — żeby sierpień też dał wynik, nie tylko lipiec

Cel Janka: **do końca miesiąca wynik z prac lipcowych ORAZ z części sierpniowych.**

**P0 — odblokowanie indeksacji (najpilniejsze, robić równolegle z landingami).**
- Blok linkowania na 5 brakujących kartach, **zaczynając od Agrobielika 70**.
- Linki **kontekstowe** (w treści, nie tylko blok) z `/wapnowanie-gleby/` i z kategorii do 4 poradników i obu landingów.
- `/do-pobrania/` — zgłosić do re-crawlu (4 miesiące bez wizyty Google, a to 17 kart produktów + atesty).
- Wyrejestrować `wp-sitemap.xml` z GSC.
- ⚠️ **Nie polegaj na Indexing API** — trzy zgłoszenia (09.07, 14.07, 30.07) nie wywołały crawlu. To API jest pod JobPosting/BroadcastEvent. Graj sygnałami: linkowanie wewnętrzne, świeżość sitemapy, ruch z Ads na te URL-e (kampania kierowana m.in. na nowe landingi sama generuje sygnał).
- Kontrola indeksacji: **20.08 i 28.08**.

**P1 — kanibalizacja „wapno bielik".** Sześć URL-i na jedną frazę markową. Wskaż jedną stronę docelową (rekomendacja: `/wapno-hydratyzowane/bielik/`), resztę podporządkuj linkowaniem wewnętrznym i meta. Robić **przed** startem kampanii brandowej, żeby reklama i organik nie biły się o ten sam ruch.

**P1 — LCP mobile.** 7,4 s to obraz hero: format (WebP/AVIF), rozmiar, `fetchpriority="high"`, preload, brak lazy-load na LCP. Mobile daje 7 135 z 10 220 wyświetleń przy CTR 1,7% vs 3,0% na desktopie — to najdroższa pojedyncza strata. **Wpływa też na koszt kliknięcia w Ads.**

**P2 — jeśli zostanie czas:** baner zgód (odblokowuje atrybucję źródeł), CSP + Permissions-Policy, decyzja o element-cache Elementora (`ttl=24` czy zostaje wyłączony).

**Czego NIE robić w sierpniu:** przywracania 3 pozycji menu (wraca we wrześniu z landingami segmentowymi), landingów oczyszczalni i stawów (to wrzesień), landingu zasięgu dostaw (nieuzgodniony z Pawłem).

---

## 4. Pomiar — co realnie zdąży do 31.08

Bądź uczciwy w ocenie, także wobec Janka:

| Źródło wyniku | Czy zdąży do 31.08 | Uwaga |
|---|---|---|
| **Google Ads** | ✅ natychmiast | Od 14.08 ruch i konwersje od pierwszego dnia. To będzie najmocniejsza liczba sierpnia |
| **Dojrzewanie prac lipcowych** | ✅ | Hub i kategorie już rosną; lipiec zamknął się na 221 klik / 10 220 wyśw. |
| **Indeksacja 5 stron** | ◐ realne przy naprawie do ~15.08 | Crawl 2–6 tyg.; przy wsparciu ruchem z Ads może przyspieszyć |
| **Landingi produktowe — pozycje** | ✗ nie w sierpniu | Nowe URL-e potrzebują 4–8 tyg. Ale **ruch z Ads na nie idzie od razu** |
| **LCP → CTR mobile** | ◐ | Poprawa techniczna natychmiast, przełożenie na CTR z opóźnieniem |

**Raport M3 przygotuj na 31.08–02.09** wzorem `docs/raporty/2026-07.md`: świeży pull GSC (pełne miesiące czerwiec/lipiec/sierpień w jednym przebiegu), URL Inspection, GA4, **plus po raz pierwszy sekcja Google Ads** (wyświetlenia, kliknięcia, koszt, konwersje, udział w wyświetleniach, koszt konwersji).

---

## 5. Narzędzia i pułapki

- **MCP agria** (token-gated, ext-1.2): `update_post_content`, `update_postmeta`, `query_db_write`, `db_export`, `wc_product_attributes`. Preferuj MCP nad curl (`feedback_agria_prefer_mcp_curl_allowlisted`). **Backup przed każdą serią zmian** (`db_export`, zapis poza web root).
- **FTP** (`~/secrets/agria/ftp.txt`) — `.htaccess`, nagłówki, pliki sitemapy.
- **Cache:** CDN nazwa.pl (cache-bust przy każdej weryfikacji), sitemapa RankMath żyje **w plikach** `uploads/rank-math/*.xml`, element-cache Elementora **wyłączony** — nie włączaj bez decyzji.
- **Parametry produktu żyją w 4 warstwach** — weryfikuj RENDER, nie bazę (`project_agria_render_caching`).
- **Indexing API — budżet dzienny wspólny dla wszystkich projektów.** Wyłącznie przez `~/bin/index-submit`, sprawdź `--status` przed serią.
- **DataForSEO** — saldo ~$33,7 (06.08). Endpointy użyte w analizie sezonowej: `keywords_data/google_ads/search_volume/live`, `.../ad_traffic_by_keywords/live`.

**Pułapki komunikacyjne (jeśli cokolwiek idzie do klienta):**
- **Nie krytykuj stanu strony** — Auranet ją zbudował. Framing rozwojowy.
- **Nie zadawaj klientowi pytań w mailu bez zgody Janka.** Decyzje marketingowe są nasze.
- **Budżet tylko miesięcznie**, nigdy suma wielomiesięczna. 1 200 zł to koszt do Google, nie przychód Auranet.
- **Nie planuj poza październik** — klient zaakceptował trzy miesiące, o kontynuacji rozmawiamy na wyniku.
- Mail wyłącznie przez `~/bin/send-to-jan` na `js@auranet.com.pl`. **Nigdy bezpośrednio do klienta.**

---

## 6. Definition of done

- [ ] Rewizja stanu z §1 wykonana na żywo, rozjazdy wobec notatek z 03.08 wypisane
- [ ] Landingi „wapno granulowane" i „wapno nawozowe" opublikowane, w sitemapie, zlinkowane
- [ ] Konto Google Ads założone (Janek) + helper `ads_call.sh` z CID
- [ ] Konwersje (telefon + formularz) skonfigurowane i **zweryfikowane przez API**
- [ ] Dwie kampanie live **najpóźniej 14.08**, 24/7, z wykluczeniami
- [ ] P0 indeksacyjne domknięte; kontrola 20.08 i 28.08
- [ ] Kanibalizacja „wapno bielik" rozstrzygnięta
- [ ] LCP mobile poprawione (cel: poniżej 4 s; docelowo 2,5 s)
- [ ] Commit + push po każdym większym etapie
- [ ] Memory zaktualizowane (CID Ads, stan indeksacji, wyniki kampanii)
