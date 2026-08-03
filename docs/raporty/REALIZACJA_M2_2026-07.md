# Realizacja M2 (lipiec 2026) — plan vs wykonane

> Baza pod raport miesięczny do AGRII. Plan źródłowy: `docs/strategy/STRATEGIA_AGRIA_6MIES_2026.md` §6 M2.
> Stan na 2026-07-15.

---

## Plan M2 (z oferty) — status

| # | Zaplanowane | Status | Uwaga |
|---|---|---|---|
| 1 | **4 artykuły eksperckie o wapnowaniu** (ile wapna na ha, jak wapnować, tlenkowe vs węglanowe, pH gleby) | ✅ **4/4** | Klaster „wapnowanie" domknięty (hub `/wapnowanie-gleby/` + 3 spoke). Hub-and-spoke, schema FAQ/HowTo, zgłoszone do indeksacji. Już rankują: „ile wapna na hektar" #14, kalkulator #20. |
| 2 | **Wzmocnienie techniczne** (szybkość, struktura adresów, bezpieczeństwo) | ◐ **częściowo** | Struktura adresów ✅ (rdzeń URL/taksonomii + 19×301). Sitemapa ✅ (patrz wartość dodana). **Zaległe → M3:** szybkość mobilna (CWV, LCP 5 s), nagłówki bezpieczeństwa (.htaccess). |
| 3 | **Wizytówka Google (Tarnów)** — optymalizacja + publikacje | ✗ **niezrobione** | GBP read-only po incydencie 2026-05-13. Do uruchomienia — wymaga decyzji o dostępie/koncie. Przenieść do M3. |
| 4 | **Raport miesięczny** | ⏳ koniec lipca | Ten dokument = baza. |

**Werdykt:** rdzeń merytoryczny M2 (content + struktura URL) dowieziony. Trzy pozycje utrzymaniowe (GBP, CWV mobilne, nagłówki bezpieczeństwa) przechodzą na M3 — z nadwyżką pokryte wartością dodaną poniżej.

---

## Wartość dodana (poza planem M2)

Rzeczy niezaplanowane na lipiec, a wykonane — część to zadania z późniejszych miesięcy dostarczone wcześniej, część to naprawy krytyczne wykryte przy pracy.

### Dostarczone z wyprzedzeniem (z planu M5 / M3)
- **Landing „Wapno do stabilizacji gruntów"** (`/wapno-do-stabilizacji-gruntow/`) — **plan M5 (październik), dostarczone w lipcu.** Fraza „stabilizacja gruntu" 720/mies., najwyższy CPC w projekcie ($2,13). Parametry z karty Nordkalk (CL 90-Q, R5). Pierwszy landing komercyjny w historii projektu.
- **Dopracowanie kart produktów rolniczych** — plan M3, wykonane w lipcu i głębiej niż zakładano (patrz parametry).

### Naprawy krytyczne (niezaplanowane, wykryte przy pracy)
- **Sitemapa** — serwowała Google 19 nieaktualnych URL-i (301-ki po migracji, cache RankMath w plikach). Naprawione + kategorie produktowe po raz pierwszy w sitemapie. **Bez tego treści M2 indeksowałyby się przez przekierowania w szczycie sezonu.**
- **H1 na całej witrynie** — nie było **ani jednego** H1 na 19 kartach i 5 kategoriach (nazwa produktu siedziała w H2). Dodane. Bazowy sygnał on-page, którego brakowało.
- **Meta na 7 stronach statycznych** (było: tylko strona główna). Kalkulator rankuje #20 — teraz z tagami.

### Parametry produktów — pełna naprawa (19 produktów)
Doprowadzone do zgodności z kartami producentów/AGRII (publicznymi na `/do-pobrania/`). Odkryto, że parametry żyły w **4 niezależnych warstwach** (atrybuty WC, tabela w treści, Elementor, meta SEO) — naprawione wszystkie:
- pH usunięte jako parametr (wartości poza skalą: „>16", „>17");
- bug importu (przecinek dziesiętny rozbijał wartości) — naprawiony;
- **klasy normowe CL 90-S / CL 90-Q + wapno czynne** dodane (309, 320) — język przetargów oczyszczalni, czego konkurencja nie ma;
- Agrobielik 90 / Oxyfertil 90 na 90% CaO (karta + atest OSChR).

### Analiza strategiczna
- **Rozpiska intencji wolumenowej** + **backlog sezonowy** (bloki A–F) — analiza SERP, konkurencji (Biovita: 109 fraz przy słabszym profilu linków niż AGRIA), sezonowości. Fundament pod landingi sierpniowe.

### Infrastruktura
- Rozszerzenie MCP (`db_export`, `wc_product_attributes`) — umożliwia bezpieczną pracę na parametrach i backupy.

---

## Domknięcie lipca — sesja 2026-07-30

### Wyniki M2 (GSC, dane rzeczywiste)

| Okres | Klik | Wyśw | CTR | Śr. poz. |
|---|---|---|---|---|
| czerwiec (1–30.06) | 63 | 2 821 | 2,23% | 13,9 |
| **lipiec (1–29.07)** | **200** | **8 721** | 2,29% | **8,9** |
| — 1–15.07 (przed fixami) | 81 | 3 214 | 2,52% | 10,9 |
| — 16–29.07 (po fixach) | 119 | 5 507 | 2,16% | **7,8** |

Klik ×3,2, wyświetlenia ×3,1, średnia pozycja w górę o 5 miejsc. Druga połowa miesiąca mocniejsza od pierwszej.

Najmocniejsze strony: `/wapnowanie-gleby/` 4 908 wyśw / 29 klik / poz. 7,8 (fraza „ile wapna na hektar" **8,7 z baseline 14** — cel „strona 1" osiągnięty przed terminem kontroli 06.08); `/kalkulator-wapnowania/` poz. **6,5** / 17 klik (był #20 bez tagów — potwierdza wartość meta z 08.07); karty na nowych URL-ach rankują (`oxyfertil-90` poz. 5,6 / 12 klik, `weglanowe-odmiana-04` poz. 5,1).

### Recheck indeksacji (zaległy z 22.07) — wykonany

**Kluczowe ustalenie: 5 z 6 nowych stron lipcowych nie było zaindeksowanych.** `lastCrawl = None`, zero wyświetleń, trzy tygodnie po publikacji i po zgłoszeniu do Indexing API (09. i 14.07). Trzy w stanie „wykryta, obecnie niezindeksowana", dwie „Google nieznany". Weryfikacja wykluczyła blokadę techniczną: HTTP 200, `index, follow`, self-canonical, JSON-LD, obecność w sitemapie, TTFB 0,3–0,9 s. Przyczyna leżała w sygnałach crawl:

- **globalne menu i stopka linkowały do trzech martwych kategorii** (`wapno-do-sadu`, `wapno-do-stawow`, `wapno-nawozowe-hurt` — 0 produktów po migracji 08.07, objęte 301 → `/oferta/`). 18 linków na 301-ki z każdej strony witryny, w szczycie sezonu;
- **oba landingi były sierotami** — `/wapno-do-stabilizacji-gruntow/` bez linku z `/oferta/`, z kategorii oczyszczalni i z karty #320; TODO z C1 nie było domknięte.

### Wykonane 30.07

| Zakres | Stan |
|---|---|
| **Linkowanie wewnętrzne** — blok „Poradniki techniczne" / „Zastosowania i poradniki" na **15 kartach** produktowych → 4 poradniki + 2 landingi B2B | ✅ zweryfikowane w renderze |
| **Re-submit 5 URL** do Indexing API (budżet 5/100) | ✅ 5 OK, 0 ERR |
| **„35 lat" → „37 lat"** — 19 kart, strona główna, `/o-firmie/`, szablon Elementor, alt obrazka | ✅ zero wystąpień w całej witrynie |
| **Literówki w H2 kart** („weglanowe", „zawierajace" — H1 były poprawne od 15.07, H2 nie) — 4 karty | ✅ zweryfikowane w renderze |
| **SKU `AGR-001…AGR-018`** dla 18 produktów (mapa z `M2_READY_TO_APPLY.md` §6) | ✅ widoczne w WC API i **w schema `Product.sku`** |
| Backup bazy przed zmianami (`posts`, `postmeta`, `terms`, `options`) | ✅ 59 MB, `agria-backups/`, poza web root |

### Pomiar wydajności (baseline pod M3)

PSI mobile strona główna: perf **48 → 67**, TBT **790 → 100 ms**, Speed Index 6,2 → 4,7 s. **LCP nadal 7,2 s** (obraz hero) — zostaje rdzeniem zadania CWV w M3. TTFB 0,28–0,41 s.

### Incydent (zamknięty tego samego dnia)

Przy czyszczeniu cache Elementora wartość `a:0:{}` w `_elementor_element_cache` została odczytana przez Elementora jako poprawny **pusty** render, nie jako brak cache. Wyzerowanie cache szablonów wygasiło treść na wszystkich stronach, postach i 2 kartach (HTML 125 → 72 KB). Wykryte własnym skanem, naprawione tego samego dnia przez wyłączenie element-cache (`elementor_element_cache_ttl = disable`). Weryfikacja po naprawie: 19/19 kart i 21/21 stron z pełną treścią, TTFB bez pogorszenia. Okno ekspozycji ~15 min. Wniosek zapisany w memory projektu.

---

## Do domknięcia (przechodzi dalej)
- **GBP Tarnów** → M3 (decyzja o dostępie).
- **CWV mobilne** → M3 (LCP 7,2 s, obraz hero). **Nagłówki bezpieczeństwa** — przygotowane, czekają na wgranie `.htaccess`.
- **Element-cache Elementora** — świadoma decyzja: przywrócić `ttl=24` razem z pracami CWV w M3 czy zostawić wyłączony.
- **Menu + stopka: 3 pozycje na martwe kategorie** — decyzja o celu (usunąć do M4, gdy powstaną landingi segmentowe, czy przepiąć teraz).
- **SKU #303** (Kreda czarna jeziorna) — potwierdzić numer `AGR-019`.
- **Karty od AGRII** dla 3 produktów bez źródła (303, 304, 316) + odmiana 305.
- **Erraty do katalogu** przy dodruku.
- **307** — jedno zdanie prozy w Elementorze (pH>12 na kredzie pastewnej) do ręcznej poprawki.
