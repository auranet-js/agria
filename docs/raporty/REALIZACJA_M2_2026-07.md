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

## Do domknięcia (przechodzi dalej)
- **GBP Tarnów** → M3 (decyzja o dostępie).
- **CWV mobilne + nagłówki bezpieczeństwa** → M3.
- **Karty od AGRII** dla 3 produktów bez źródła (303, 304, 316) + odmiana 305.
- **Erraty do katalogu** przy dodruku.
- **307** — jedno zdanie prozy w Elementorze (pH>12 na kredzie pastewnej) do ręcznej poprawki.
