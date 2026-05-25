# ONPAGE_PLAN — agria.pl: priorytetyzacja KR → URL + plan on-page

> **Sesja 2026-05-20 (Wątek 5). Koszt po stronie Auranet (pre-M1 proof-of-value / dopełnienie w M1).**
> Dwa deliverables M1 w jednym dokumencie:
> - **Część A** = deliverable M1 #3 — priorytetyzacja keyword research → URL agria.pl
> - **Część B** = deliverable M1 #5 — plan on-page poprawek per produkt/kategoria (obszar 2 audytu)
>
> **Dane wejściowe:** `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` (112 fraz, 8 klastrów), live MCP `Agria.pl` (19 produktów + 7 kategorii + 11 stron + 6 postów, stan 2026-05-20 20:04 UTC), meta RankMath z `wpfz_postmeta`/`wpfz_termmeta`.
> **Stan live potwierdzony:** WP 6.9.4, WC 10.6.1, PHP 8.3.30, motyw `Agria By Auranet 2.0.0`, prefix `wpfz_`.
> **MCP read-only** — żadnych zmian w bazie. Wszystkie rekomendacje do wdrożenia przez WP Admin / WP-CLI po dostępach (T1 M1).

---

## Executive summary (dla zarządu klienta)

**Dobra wiadomość on-page:** RankMath jest skonfigurowany dla **całej oferty** — wszystkie 19 produktów i 7 kategorii ma własny title, meta description i frazę kluczową. To nie jest pole zaorane od zera, tylko **strona do dostrojenia**.

**Trzy systemowe problemy do naprawy:**

1. **Strony statyczne nie mają meta SEO.** Oferta, O firmie, Kontakt, Kalkulator wapnowania, Do pobrania, Poradniki — wszystkie renderują się z domyślnego szablonu RankMath, bez własnego title i opisu. Najboleśniejszy przypadek: **Kalkulator wapnowania** mógłby rankować na frazę „ile wapna granulowanego na ha" (**590 wyszukiwań/mies**), a dziś nie ma nawet tytułu pod tę intencję.

2. **Najwyższy-wolumenowy klaster (drogownictwo, ~14 000 wyszuk./mies) nie ma żadnej strony** — bo kruszywo / cement / wapno drogowe **nie są w sklepie** (czeka decyzja klienta z `CATALOG_VS_WC_GAP.md` §1). To nie błąd on-page, to **decyzja biznesowa blokująca duży potencjał**.

3. **Literówki bez polskich znaków w nazwach 8 produktów** (`weglanowe`, `zawierajace`) wchodzą wprost do H1 i tytułu strony — Google rankuje słabiej na poprawną pisownię, której szuka 99% użytkowników.

**Co dostajemy z mapowania fraz:** z 112 fraz baseline **44 jest realnie wdrażalnych pod ofertę AGRIA** i wybranych jako priorytetowe pod content M2–M6 (reszta to zapytania detaliczne „castorama/leroy/allegro", marki konkurencji i frazy poza zakresem — świadomie pominięte, lista na końcu Części A).

**Priorytet, pierwszy krok, ryzyko:**
- **Priorytet:** uzupełnić meta stron + naprawić literówki w nazwach produktów (P0 → M2).
- **Pierwszy krok jutro:** ustawić title + opis na `/kalkulator-wapnowania/` pod „ile wapna na ha" — to jedyne narzędzie na stronie z szansą na 590 wyszuk./mies leżące odłogiem.
- **Ryzyko braku działania:** strona dalej rankuje przypadkowo, najwyższy-wolumenowy klaster (drogownictwo) zostaje niewidoczny, a kalkulator — najmocniejszy magnes contentowy — marnuje swój potencjał.

---

# CZĘŚĆ A — Priorytetyzacja KR → URL (deliverable M1 #3)

## A1. Inwentarz URL agria.pl (stan live 2026-05-20)

### Strony segmentowe = kategorie produktowe (7) — główne landing pages SEO

| Kategoria (term_id) | URL | Fraza RankMath (focus) | Produktów | Title RankMath | Stan meta |
|---|---|---|---:|---|---|
| Rolnictwo (764) | `/wapno-nawozowe-rolnictwo/` | wapno nawozowe | 17 | Wapno nawozowe do rolnictwa \| AGRIA | ✅ komplet |
| Hurtownie (769) | `/wapno-nawozowe-hurt/` | wapno nawozowe hurt | 13 | Wapno nawozowe hurt \| AGRIA dla hurtowni | ✅ komplet |
| Sadownictwo (765) | `/wapno-do-sadu/` | wapno do sadu | 9 | Wapno do sadu owocowego \| AGRIA (węglanowe granulowane) | ✅ komplet |
| Rybactwo (766) | `/wapno-do-stawow/` | wapno do stawów | 5 | Wapno do stawów rybnych \| AGRIA (odmiany 01,02) | ✅ komplet |
| Oczyszczalnie (767) | `/wapno-do-oczyszczalni/` | wapno do oczyszczalni | 4 | Wapno do oczyszczalni ścieków \| AGRIA (higienizacja) | ✅ komplet |
| Budownictwo (768) | `/wapno-hydratyzowane/` | wapno hydratyzowane | 1 | Wapno hydratyzowane do budownictwa \| AGRIA | ✅ komplet |
| Paszarstwo (770) | `/kreda-pastewna/` | kreda pastewna | 1 | Kreda pastewna do żywienia zwierząt \| AGRIA | ✅ komplet |

**Wniosek:** każdy z 5 segmentów MASTER_PROMPT (+ hurt + paszarstwo) ma dedykowaną kategorię z opisem SEO i frazą. To fundament — nie budujemy landing pages od zera, optymalizujemy istniejące.

### Strony statyczne (7 merytorycznych + 4 utility)

| Strona (ID) | URL | Focus RankMath | Title RankMath | Stan meta |
|---|---|---|---|---|
| Strona główna (321) | `/` | wapno nawozowe | — (szablon) | ⚠️ tylko focus, brak custom title/desc |
| Oferta (79) | `/oferta/` | — | — | ❌ pusta |
| O firmie (325) | `/o-firmie/` | — | — | ❌ pusta |
| Kontakt (323) | `/kontakt/` | — | — | ❌ pusta |
| **Kalkulator wapnowania (729)** | `/kalkulator-wapnowania/` | — | — | ❌ pusta (najboleśniejsza luka) |
| Poradniki / blog hub (727) | `/poradniki/` | — | — | ❌ pusta |
| Do pobrania (731) | `/do-pobrania/` | — | — | ❌ pusta |
| RODO (733) | `/rodo/` | — | — | utility (noindex OK) |
| Wsparcie (1660) | `/wsparcie/` | — | — | utility |
| Zamówienia (1920) | `/zamowienia/` | — | — | utility (noindex) |
| Cart (80) | `/cart/` | — | — | utility (noindex) |

### Produkty (19) — patrz pełna mapa w Części B (B3)

URL produktu = `/{kategoria}/{slug}/` (przepisywany przez Premmerce). **Uwaga:** prefix kategorii wybiera Premmerce, bo `rank_math_primary_product_cat` jest `null` dla wszystkich 19 — patrz finding B5-1 (Dolomit ląduje pod `/wapno-nawozowe-hurt/`, nie pod rolnictwem).

### Blog (6 postów, hub `/poradniki/`)

| Post (ID) | Tytuł | Segment | Data |
|---|---|---|---|
| 2079 | Czy wapnować czy nie wapnować stawy karpiowe? | rybactwo | 2026-03-12 |
| 2074 | Wapnowanie gleby – kiedy, ile i jakie wapno stosować | rolnictwo | 2026-02-23 |
| 2090 | Wykwity – jak powstają i skąd się biorą na murze? | budownictwo | 2026-01-23 |
| 2082 | Cement – czym jest, jak powstaje i jakie są jego klasy? | budownictwo | 2025-12-23 |
| 2084 | Jak murować z cegły klinkierowej – zasady bez wykwitów | budownictwo | 2025-05-23 |
| 2092 | Tynki – rodzaje, kategorie i zasady wykonania | budownictwo | 2025-04-23 |

**Rozkład blogu jest skrzywiony:** 4 z 6 postów to budownictwo, a budownictwo ma **najmniej produktów (1)**. Rolnictwo — najwięcej produktów (17) i najwięcej wolumenu fraz informacyjnych — ma **tylko 1 post**. To gap do nadgonienia w content M2–M6 (zgodne z `SEO_AUDIT_RESULTS.md` P2-8).

---

## A2. Pokrycie klastrów KR przez istniejące URL

| Klaster KR | Vol/mies (top) | Landing (kategoria) | Pokrycie produktem | Pokrycie blogiem | Ocena |
|---|---:|---|---|---|---|
| Rolnictwo | ~3 240 | ✅ /wapno-nawozowe-rolnictwo/ | ✅ 11 produktów wapno/kreda nawozowa | ⚠️ 1 post (#2074) | **Dobre, content cienki** |
| Budownictwo | ~3 670 | ✅ /wapno-hydratyzowane/ | ✅ #309 Bielik | ✅ 4 posty | **Dobre** |
| Drogownictwo | ~14 040 | ❌ brak | ❌ brak (kruszywo/cement poza WC) | ❌ brak | **BLOCKED — decyzja klienta** |
| Rybactwo | ~240 | ✅ /wapno-do-stawow/ | ✅ #310/#311/#312 + kredy | ✅ 1 post (#2079) | **Dobre na swój wolumen** |
| Oczyszczalnie | ~170 | ✅ /wapno-do-oczyszczalni/ | ✅ #320 + #309/#311/#312 | ❌ brak | **Landing OK, content gap (AEO)** |
| Paszarstwo | ~150 | ✅ /kreda-pastewna/ | ✅ #307 | ❌ brak | **Landing OK, content gap** |
| Sadownictwo | (w rolnictwie) | ✅ /wapno-do-sadu/ | ✅ 9 produktów | ❌ brak | **Dobre, content gap** |
| Marka/ogólne | ~10 | ✅ / + /o-firmie/ | n/d | n/d | **OK** |

**Kluczowy wniosek strategiczny:** 7 z 8 klastrów ma landing page. **Jedyny niepokryty klaster — drogownictwo — to zarazem najwyższy wolumen (~14 000/mies).** Odblokowanie zależy od decyzji klienta „czy kruszywo wapienne / cement / wapno drogowe wchodzą do oferty online" (`CATALOG_VS_WC_GAP.md` §1). **Bez tej decyzji 65% całego zmapowanego wolumenu fraz zostaje poza zasięgiem.**

---

## A3. Mapowanie fraz priorytetowych → URL (44 frazy)

Legenda statusu:
- **JEST** — istnieje URL celujący w intencję, wystarczy on-page (title/H1/treść).
- **CZĘŚCIOWO** — URL istnieje, ale intencja pokryta słabo (np. brak sekcji/treści odpowiadającej na zapytanie).
- **GAP** — brak URL pod tę intencję, potrzebny nowy content (blog/FAQ/sekcja).
- **BLOCKED** — wymaga decyzji produktowej klienta zanim powstanie URL.

Legenda priorytetu (content/on-page roadmap):
- 🟢 **P0 → M2** | 🟡 **P1 → M3–M4** | 🔵 **P2 → M5–M6**

### Rolnictwo (12 fraz priorytetowych)

| Fraza | Vol | Intent | URL docelowy | Status | Prio |
|---|---:|---|---|---|---|
| wapno nawozowe | 1300 | info | `/wapno-nawozowe-rolnictwo/` (+ `/`) | JEST | 🟢 |
| ile wapna granulowanego na ha | 590 | info | `/kalkulator-wapnowania/` + nowy poradnik | CZĘŚCIOWO | 🟢 |
| wapno nawozowe granulowane | 390 | trans | `/wapno-nawozowe-rolnictwo/` + #314/#305 | CZĘŚCIOWO | 🟢 |
| wapno nawozowe cena za tonę | 140 | info | poradnik „cennik/od czego zależy cena wapna" | GAP | 🟡 |
| wapno nawozowe cena | 90 | info | poradnik cennikowy + `/kontakt/` (zapytanie) | GAP | 🟡 |
| wapno nawozowe z magnezem | 70 | trans | #313 + #317/#318/#319 | JEST | 🟢 |
| dolomit wapno nawozowe | 70 | trans | `/.../dolomit-worek-25kg/` (#302) | JEST | 🟢 |
| wapno nawozowe tlenkowe | 50 | info | #310/#311 + kategoria | JEST | 🟢 |
| kiedy stosować wapno nawozowe | 50 | info | blog #2074 | JEST | 🟡 |
| wapno nawozowe luzem | 50 | info | warianty „-luz" (#306/#308/#315…) | CZĘŚCIOWO | 🔵 |
| ile kosztuje wapno nawozowe | 40 | info | poradnik cennikowy (jw.) | GAP | 🟡 |
| wapno nawozowe węglanowe | 30 | info | #314/#315/#316 + kategoria | JEST | 🟡 |

### Budownictwo (8 fraz)

| Fraza | Vol | Intent | URL docelowy | Status | Prio |
|---|---:|---|---|---|---|
| wapno hydratyzowane | 2400 | trans | `/wapno-hydratyzowane/` + #309 | JEST | 🟢 |
| wapno hydratyzowane zastosowanie | 140 | trans | sekcja na kategorii + poradnik | CZĘŚCIOWO | 🟢 |
| wapno hydratyzowane cena | 140 | trans | kategoria + poradnik cennikowy | CZĘŚCIOWO | 🟡 |
| czy wapno hydratyzowane jest szkodliwe | 70 | info | poradnik FAQ/BHP | GAP | 🟡 |
| wapno hydratyzowane bielik | 50 | trans | #309 (focus dokładny) | JEST | 🟢 |
| wapno hydratyzowane karta charakterystyki | 20 | info | `/do-pobrania/` | CZĘŚCIOWO | 🟡 |
| wapno palone a hydratyzowane | 20 | info | poradnik porównawczy | GAP | 🔵 |
| co to jest wapno hydratyzowane | 20 | info | poradnik + sekcja kategorii | GAP | 🔵 |

### Drogownictwo (6 fraz — w zakresie AGRIA, reszta poza) — **BLOCKED**

| Fraza | Vol | Intent | URL docelowy | Status | Prio |
|---|---:|---|---|---|---|
| stabilizacja gruntu | 720 | info | nowa landing „wapno do stabilizacji gruntu" | BLOCKED | 🟡 |
| kruszywo wapienne | 260 | info | nowa landing „kruszywo wapienne" | BLOCKED | 🟡 |
| kruszywo drogowe 0-31 5 cena | 110 | info | landing + cennik | BLOCKED | 🔵 |
| kruszywo dolomitowe 0-31 5 | 50 | trans | landing kruszywo dolomitowe | BLOCKED | 🔵 |
| kruszywo drogowe 0-31 5 | 50 | trans | landing kruszywo drogowe | BLOCKED | 🔵 |
| wapno palone mielone (uziarnienie drogowe) | — | trans | #320 / nowa sekcja drogowa | BLOCKED | 🔵 |

> **Uwaga zakres:** „kruszywo" (9900) i „kruszywo granitowe" (720) są **poza ofertą AGRIA** — AGRIA dostarcza kruszywo wapienne/dolomitowe, nie granit. W priorytetach tylko frazy wapienne/dolomitowe + stabilizacja gruntu wapnem. Cała sekcja czeka na decyzję §1 z `CATALOG_VS_WC_GAP.md`.

### Rybactwo (5 fraz)

| Fraza | Vol | Intent | URL docelowy | Status | Prio |
|---|---:|---|---|---|---|
| wapnowanie stawu wapnem budowlanym | 70 | info | `/wapno-do-stawow/` + blog #2079 | JEST | 🟡 |
| wapno hydratyzowane do stawu | 50 | trans | `/wapno-do-stawow/` + #309 | CZĘŚCIOWO | 🟡 |
| wapnowanie zarybionego stawu | 40 | info | blog #2079 (rozszerzyć) | JEST | 🔵 |
| wapno tlenkowo/magnezowe do stawu | 20 | trans | #310/#311 + kategoria | CZĘŚCIOWO | 🔵 |
| wapno tlenkowe dawkowanie staw | 10 | info | blog #2079 + kalkulator | JEST | 🔵 |

### Oczyszczalnie (3 frazy — niski wolumen, wysoka wartość B2B, AEO)

| Fraza | Vol | Intent | URL docelowy | Status | Prio |
|---|---:|---|---|---|---|
| neutralizator(y) ścieków | 140 | trans/comm | `/wapno-do-oczyszczalni/` + #320 | CZĘŚCIOWO | 🟡 |
| higienizacja osadów ściekowych | 30 | info | poradnik AEO „jak higienizować osady wapnem" + #320 | CZĘŚCIOWO | 🟡 |

### Paszarstwo / sadownictwo (4 frazy)

| Fraza | Vol | Intent | URL docelowy | Status | Prio |
|---|---:|---|---|---|---|
| jakie wapno do kurnika | 110 | info | poradnik (Bielik dezynfekcja) + #309 | GAP | 🔵 |
| wapno hydratyzowane do kurnika | 40 | trans | poradnik + #309 | GAP | 🔵 |
| kreda pastewna (focus) | — | trans | `/kreda-pastewna/` + #307 | JEST | 🟡 |
| wapno do sadu (focus) | — | trans | `/wapno-do-sadu/` | JEST | 🟡 |

**Podsumowanie priorytetów (44 frazy):**
- 🟢 **P0 → M2:** 12 fraz (głównie quick-winy z istniejącym URL: wapno hydratyzowane, wapno nawozowe, granulowane, tlenkowe, z magnezem, dolomit, Bielik + kalkulator pod „ile na ha").
- 🟡 **P1 → M3–M4:** 16 fraz (content cennikowy, FAQ, rozszerzenia kategorii, oczyszczalnie AEO, rybactwo, drogownictwo po decyzji).
- 🔵 **P2 → M5–M6:** 16 fraz (long-tail porównawcze, kurnik, drogownictwo szczegółowe, rozszerzenia blogu).

## A4. Frazy świadomie pominięte (nie wchodzą do priorytetów)

| Grupa | Przykłady | Powód pominięcia |
|---|---|---|
| Detaliczne / sieci marketów | castorama, leroy merlin, obi, bricomarche, mrówka, allegro | SERP zdominowany przez sieci; intencja zakupu detalicznego, nie B2B |
| Marki konkurencji | florovit, polcalc, morawica, kujawit, orcal, atrigran, supermag | Zapytania brandowe — odrębna strategia „X vs Agrobielik" (gap analysis, nie core content) |
| Konsumenckie / lifestyle | wapno na trawnik, do bielenia drzew/ścian, w ogrodzie | Poza pozycjonowaniem B2B surowcowym (MASTER_PROMPT) |
| Poza ofertą | kruszywo granitowe (720), kruszywo 8 16 / 2-8 (granit) | AGRIA = kruszywo wapienne/dolomitowe, nie granit |
| Suplementy/medyczne | (już odfiltrowane w KR baseline) | Poza zakresem |

> **Frazy markowe konkurencji** nie są martwe — to materiał na osobny deliverable „treści porównawcze" (`X vs Agrobielik`) w M4–M6, gdy domena nabierze autorytetu. Dziś nie warto na nie celować przy zerowym budżecie link buildingu.

---

# CZĘŚĆ B — Plan on-page per produkt/kategoria (deliverable M1 #5)

> Obszar 2 z `docs/seo/SEO_AUDIT_PLAN.md`: title, meta description, H1, struktura nagłówków, slug.
> Na produktach WC **H1 = nazwa produktu (`post_title`)** — naprawa nazwy naprawia jednocześnie H1 i wyświetlany nagłówek. Meta title (RankMath) jest osobny od nazwy.

## B1. Stan ogólny on-page (co już działa)

| Element | Stan | Komentarz |
|---|---|---|
| Meta title — produkty | ✅ 19/19 ustawione | dobre, kilka do dostrojenia (case, „70 70%", literówki) |
| Meta description — produkty | ✅ 19/19 ustawione | 2 thin („35 lat doświadczenia" placeholder: #307, #319) |
| Focus keyword — produkty | ✅ 19/19 | 8 zawiera literówkę (`weglanowe`) — odzwierciedla nazwę |
| Meta — kategorie | ✅ 7/7 komplet | bardzo dobre, frazy trafione |
| Meta — strony statyczne | ❌ 0/7 custom | **główny gap on-page** |
| Schema Product | ✅ 19 PropertyValue | bez `sku` (P1-5) i bez `offers` (tryb katalogu) |

## B2. Plan on-page — KATEGORIE (7 stron segmentowych)

Kategorie są w dobrym stanie — meta trafione we frazy z KR. Drobne dostrojenia:

| Kategoria | Title / focus dziś | Rekomendacja | Prio |
|---|---|---|---|
| Rolnictwo (764) | „Wapno nawozowe do rolnictwa \| AGRIA" / `wapno nawozowe` | OK. H2 w opisie „Odkwaś glebę…" — dodać wzmiankę „granulowane" (390 vol) w treści | 🟢 |
| Hurtownie (769) | „Wapno nawozowe hurt…" / `wapno nawozowe hurt` | OK — fraza trafiona | 🔵 |
| Sadownictwo (765) | „Wapno do sadu owocowego…" / `wapno do sadu` | OK | 🔵 |
| Rybactwo (766) | „Wapno do stawów rybnych…" / `wapno do stawów` | Dodać sekcję „wapnowanie stawu wapnem budowlanym/hydratyzowanym" (frazy 70+50) | 🟡 |
| Oczyszczalnie (767) | „Wapno do oczyszczalni ścieków…" / `wapno do oczyszczalni` | Dodać blok FAQ pod „neutralizator ścieków" + „higienizacja osadów" (AEO/schema FAQ) | 🟡 |
| Budownictwo (768) | „Wapno hydratyzowane do budownictwa…" / `wapno hydratyzowane` | **Najważniejsza kategoria po wolumenie (2400).** Rozbudować treść: zastosowanie, cena, BHP („czy szkodliwe") | 🟢 |
| Paszarstwo (770) | „Kreda pastewna do żywienia zwierząt…" / `kreda pastewna` | OK; rozważyć poradnik „jakie wapno do kurnika" (110) podlinkowany | 🔵 |

**Finding B2-1 (P1):** opisy kategorii to jeden akapit + lista — dla frazy „wapno hydratyzowane" (2400 vol, intencja transakcyjna z elementem informacyjnym) konkurencja ma rozbudowane strony filarowe. Budownictwo i Rolnictwo zasługują na **content filarowy** (hub) w M2–M3, nie tylko opis kategorii.

## B3. Plan on-page — PRODUKTY (19)

### B3a. Produkty priorytetowe (mapowane na frazy P0/P1) — rekomendacje szczegółowe

**#310 Wapno nawozowe tlenkowe Agrobielik 70** — `/.../wapno-agrobielik-70-big-bag-1000kg/`
- Title dziś: `Wapno nawozowe tlenkowe Agrobielik 70 70% CaO | AGRIA` (53 zn., „70 70%" zgrzyta)
- **Title rec:** `Agrobielik 70 — wapno nawozowe tlenkowe 70% CaO | AGRIA` (53 zn.)
- H1 (nazwa): OK
- Frazy: `wapno nawozowe tlenkowe agrobielik 70`, `wapno nawozowe tlenkowe` (50) — JEST. Prio 🟢

**#311 Wapno nawozowe tlenkowe Agrobielik 90** — `/.../wapno-agrobielik-90-big-bag-1000kg/`
- Title dziś: `wapno nawozowe tlenkowe agrobielik 90 80% CaO | AGRIA` (**mała litera na początku**)
- **Title rec:** `Agrobielik 90 — wapno nawozowe tlenkowe 80% CaO | AGRIA`
- **Decyzja klienta:** wariant frakcji 2–8 mm (PDF ma osobną kartę, WC ma tylko #311) — `CATALOG_VS_WC_GAP.md` §2. Do rozstrzygnięcia czy `variable product` czy osobny SKU. Prio 🟡 (po decyzji)

**#309 Wapno hydratyzowane Bielik** — `/wapno-hydratyzowane/wapno-hydratyzowane-bielik-luz/`
- Title dziś: `wapno hydratyzowane bielik min. 72% CaO | AGRIA` (**mała litera**)
- **Title rec:** `Wapno hydratyzowane Bielik 72% CaO | AGRIA` (42 zn.)
- **Najcenniejszy produkt po wolumenie** (fraza kategorii 2400 + „bielik" 50). Rozbudować opis o zastosowanie budowlane + oczyszczalnie. Prio 🟢

**#302 Dolomit** — obecnie `/wapno-nawozowe-hurt/dolomit-worek-25kg/`
- Title dziś: `Dolomit | Nawóz wapniowo-magnezowy AGRIA` (40 zn.) — OK
- **Finding (B5-1):** produkt rolniczy ląduje pod URL **hurtowni**, bo brak primary category. Ustawić primary = Rolnictwo → URL `/wapno-nawozowe-rolnictwo/dolomit-worek-25kg/`. **Wymaga 301 ze starego URL.** Prio 🟡
- Fraza `dolomit wapno nawozowe` (70) — JEST

**#305 Kreda nawozowa granulowana** — `/.../kreda-nawozowa-granulowana-big-bag-500kg/`
- Title: `Kreda nawozowa granulowana 50% CaO | AGRIA` — OK. Fraza `wapno nawozowe granulowane` (390) wspiera. Prio 🟢

**#320 Wapno palone mielone wysokoreaktywne** — `/wapno-do-oczyszczalni/...`
- Title: `Wapno palone mielone wysokoreaktywne | AGRIA` — OK
- Dodać w opisie frazy „neutralizator ścieków", „higienizacja osadów" + blok FAQ (AEO). Prio 🟡

**#308 Mieszanka tlenkowo-węglanowa** — title OK, focus dokładny. Prio 🔵
**#312 Oxyfertil 90** — title OK (57 zn., borderline). Prio 🔵
**#313 Wapno nawozowe tlenkowe zawierające magnez** — title OK (z polskimi znakami!), fraza `wapno nawozowe z magnezem` (70). Prio 🟢

### B3b. Produkty z literówkami w nazwie (8) — naprawa H1 + title (P0 → M2)

**Nazwa produktu = H1.** Literówki bez polskich znaków wchodzą do H1 i osłabiają ranking. `CATALOG_VS_WC_GAP.md` §9.

| ID | Nazwa dziś (H1) | Nazwa rec (H1) |
|---|---|---|
| 314 | Wapno nawozowe **weglanowe** bez magnezu granulowane | Wapno nawozowe **węglanowe** bez magnezu granulowane |
| 315 | Wapno nawozowe **weglanowe** bez magnezu — Odmiana 04 | Wapno nawozowe **węglanowe** bez magnezu — Odmiana 04 |
| 316 | Wapno nawozowe **weglanowe** bez magnezu — Odmiana 05 | Wapno nawozowe **węglanowe** bez magnezu — Odmiana 05 |
| 317 | Wapno nawozowe **weglanowe zawierajace** magnez granulowane | Wapno nawozowe **węglanowe zawierające** magnez granulowane |
| 318 | Wapno nawozowe **weglanowe zawierajace** magnez — Odmiana 04 | Wapno nawozowe **węglanowe zawierające** magnez — Odmiana 04 |
| 319 | Wapno nawozowe **weglanowe zawierajace** magnez — Odmiana 05 | Wapno nawozowe **węglanowe zawierające** magnez — Odmiana 05 |

> Po zmianie nazwy: zsynchronizować focus keyword (np. #314 `wapno nawozowe weglanowe bez magnezu` → `węglanowe`) i meta title (część już ma poprawną pisownię — np. #318 title ma „węglanowe zawierające", a nazwa nie — **niespójność do ujednolicenia**). **Slug NIE zmieniać** (bez polskich znaków jest OK SEO-wise i zmiana = 301 bez korzyści).

### B3c. Produkty z thin/placeholder meta (2) — przepisanie (P1 → M3)

| ID | Problem | Rekomendacja |
|---|---|---|
| 307 Kreda pastewna | desc = „Kreda pastewna — zapytaj o ofertę. Agria, **35 lat** doświadczenia." (placeholder + zła liczba lat) | Przepisać pod paszarstwo: żwacz, wapń, TMR; **„37 lat"** (2026−1989) |
| 319 Wapno węglanowe zaw. magnez Odm. 05 | desc placeholder „…35 lat doświadczenia" | Przepisać jak #318 (parametry CaO/MgO, gleby lekkie) |

> **„35 lat" → „37 lat"** to globalna niespójność (`CATALOG_VS_WC_GAP.md` §4) — ulotka DL ma poprawnie 37, docs i meta mają relikt. Sprawdzić wszystkie meta/treści przy okazji.

### B3d. Produkty zależne od decyzji klienta (flaga, nie ruszamy autonomicznie)

| Produkt | Decyzja blokująca (`CATALOG_VS_WC_GAP.md`) |
|---|---|
| #303 Kreda czarna jeziorna | §1 — decyzja Q1 „wycinamy" vs publish w WC + w ulotce DL. Czekamy: zostawić indexable / `noindex` / poprawić. **Slug 73 zn.** do skrócenia tylko jeśli zostaje (z 301). |
| #304 Kreda malarska | §1 — nigdy nie planowana do katalogu, ale publish w WC. Indexable? |
| #311 Agrobielik 90 wariant 2–8 mm | §2 — `variable product` vs osobny SKU |
| Cement / kruszywo / wapno drogowe | §1 — w ogóle wejście do WC (odblokowuje cały klaster drogownictwo) |

## B4. Plan on-page — STRONY STATYCZNE (główny gap)

Wszystkie renderują się z domyślnego szablonu RankMath. Propozycje meta:

| Strona | Title rec | Meta description rec | Focus | Prio |
|---|---|---|---|---|
| `/` (321) | `Wapno nawozowe i budowlane od 1989 r. \| AGRIA Sp. z o.o.` (~56 zn.) | Producent i dystrybutor wapna nawozowego, hydratyzowanego i kredy od 1989 r. Dostawy luzem, big-bag, worki. 37 lat, trzy pokolenia. Zapytaj o ofertę. | wapno nawozowe | 🟢 |
| `/kalkulator-wapnowania/` (729) | `Kalkulator wapnowania — ile wapna na ha \| AGRIA` | Oblicz dawkę wapna nawozowego na hektar wg pH i typu gleby. Darmowy kalkulator wapnowania AGRIA dla rolników i sadowników. | ile wapna na ha | 🟢 |
| `/oferta/` (79) | `Oferta — wapno nawozowe, hydratyzowane, kreda \| AGRIA` | Pełna oferta AGRIA: wapno tlenkowe, węglanowe, hydratyzowane, kreda nawozowa i pastewna. 5 segmentów, dostawy własną flotą. | wapno nawozowe oferta | 🟢 |
| `/o-firmie/` (325) | `O firmie AGRIA — 37 lat w surowcach wapniowych \| AGRIA` | AGRIA Sp. z o.o. — rodzinna firma od 1989 r., trzy pokolenia. Surowce wapniowe i mineralne dla rolnictwa, budownictwa, ochrony środowiska. | agria | 🟡 |
| `/do-pobrania/` (731) | `Karty charakterystyki i atesty \| AGRIA` | Karty charakterystyki, atesty PZH, deklaracje zgodności PN-EN dla wapna i kredy AGRIA. Pobierz dokumenty techniczne. | karta charakterystyki wapno | 🟡 |
| `/poradniki/` (727) | `Poradniki — wapnowanie, wapno budowlane, stawy \| AGRIA` | Praktyczne poradniki AGRIA: kiedy i ile wapnować, wapno do stawów, zaprawy i tynki. Wiedza techniczna od ekspertów od 1989 r. | wapnowanie poradnik | 🟡 |
| `/kontakt/` (323) | `Kontakt — Tarnów, Niedomice, Radgoszcz \| AGRIA` | Skontaktuj się z AGRIA: centrala Tarnów + oddziały Niedomice i Radgoszcz. Doradztwo i wyceny wapna nawozowego i budowlanego. | kontakt agria | 🔵 |

> `/rodo/`, `/wsparcie/`, `/zamowienia/`, `/cart/` — utility, ustawić `noindex` (RankMath), nie marnować budżetu meta.

## B5. Findings on-page systemowe

**B5-1 (P1) — brak primary category na 19 produktach.** `rank_math_primary_product_cat = null` dla wszystkich → Premmerce wybiera prefix URL wg własnej logiki (najwyższy term_id). Skutek: Dolomit (rolniczy) pod `/wapno-nawozowe-hurt/`, Kreda pastewna pod `/kreda-pastewna/` (paszarstwo) zamiast rolnictwa. **Rekomendacja:** ustawić primary per produkt zgodnie z głównym segmentem; **każda zmiana prefixu = 301** (łączyć z planem 301 z `SEO_AUDIT_RESULTS.md` P0-3). Prio 🟡 → M3.

**B5-2 (P1) — niespójność nazwa produktu ↔ meta title.** Część produktów ma poprawną pisownię w meta title, a literówkę w nazwie (#318: title „węglanowe zawierające", nazwa „weglanowe zawierajace"). Ujednolicić przy naprawie B3b.

**B5-3 (P2) — slugi z sufiksem opakowania.** `-big-bag-1000kg`, `-luz`, `-luz-2` w slugach (#316/#319 mają auto-dedup `-luz-2`). SEO-neutralne, ale `-2` brzydkie. Zmiana = 301 bez realnej korzyści → **nie ruszać** poza #303 (Kreda czarna, 73 zn.) jeśli klient zdecyduje, że zostaje.

**B5-4 (z audytu, P1-5) — sku = null na 19/19.** Schema Product bez `sku` → mniejsza eligibility rich snippet + brak ID dla feedów. Wdrożenie zależy od decyzji o numeracji `AGR-XXX` (`CATALOG_VS_WC_GAP.md` §1/§8 — spec vs mapping rozjeżdżają się). Prio 🟡 po decyzji.

## B6. Backlog on-page — rozbicie per miesiąc

### P0 → M2 (lipiec) — quick wins, niskie ryzyko
- [ ] Meta dla `/` , `/kalkulator-wapnowania/`, `/oferta/` (B4) — **kalkulator pod „ile wapna na ha" 590 vol = priorytet #1**
- [ ] Naprawa literówek w 8 nazwach produktów = H1 (#314–319) + sync focus keyword (B3b)
- [ ] Title case fix #303, #311, #309 (mała litera na początku) (B3a)
- [ ] „35 lat" → „37 lat" w meta #307, #319 + globalnie (B3c)
- [ ] Title #310 „70 70%" → poprawny (B3a)
- [ ] Rozbudowa treści kategorii Budownictwo + Rolnictwo pod frazy 2400/1300 (B2)

### P1 → M3–M4 (sierpień–wrzesień) — content + struktura
- [ ] Meta `/o-firmie/`, `/do-pobrania/`, `/poradniki/` (B4)
- [ ] Przepisanie thin meta #307, #319 (B3c)
- [ ] Ustawienie primary category 19 produktów + 301 (B5-1)
- [ ] Sync nazwa↔title (B5-2)
- [ ] Sekcja FAQ + schema na `/wapno-do-oczyszczalni/` (oczyszczalnie AEO)
- [ ] Sekcja „wapnowanie stawu" na `/wapno-do-stawow/` (rybactwo)
- [ ] Content cennikowy (frazy „cena/cena za tonę" rolnictwo + budownictwo)
- [ ] Wdrożenie SKU po decyzji klienta (B5-4)

### P2 → M5–M6 (październik–listopad) — long-tail + skala
- [ ] Poradniki long-tail: „czy wapno hydratyzowane szkodliwe", „wapno palone a hydratyzowane", „jakie wapno do kurnika"
- [ ] Landing drogownictwo (kruszywo wapienne + stabilizacja gruntu) — **po decyzji §1**
- [ ] Treści porównawcze „X vs Agrobielik" (marki konkurencji)
- [ ] Decyzje produktowe domknięte: Kreda czarna #303 (slug/index), Agrobielik 90 wariant
- [ ] Meta `/kontakt/`, noindex stron utility

---

## Zależności od decyzji klienta (do potwierdzenia w T1 M1)

| # | Decyzja | Co odblokowuje | Źródło |
|---|---|---|---|
| 1 | Cement / kruszywo / wapno drogowe do WC? | **Cały klaster drogownictwo ~14 000 vol** (najwyższy potencjał) | CATALOG_VS_WC_GAP §1 |
| 2 | Kreda czarna jeziorna #303 — zostaje/wycięta/noindex? | Slug 73 zn., status indexacji | §1 |
| 3 | Agrobielik 90 wariant 2–8 mm — variable vs osobny SKU? | Schema, URL, linkowanie | §2 |
| 4 | Numeracja SKU `AGR-XXX` finalna? | Bulk SKU 19 produktów, schema | §1/§8 |

**Praktyka (z audytu):** żadnej z tych rekomendacji nie wykonujemy autonomicznie — flagujemy w prezentacji oferty jako „wykonamy po decyzji klienta".

---

## Następne kroki

1. **Drop do klienta przez Janka** (`js@auranet.com.pl`) — nigdy bezpośrednio do AGRIA.
2. **T2 M1:** przełożyć Część A na Google Sheets (priorytetyzacja KR) + Część B na backlog Trello/Sheets (zgodnie z `MONTH_1_FOUNDATIONS_PLAN.md` deliverables #3 i #5).
3. **Decyzje produktowe** (4 pytania) — slot z handlowcem AGRIA w T1.
4. **Pierwszy konkretny krok wdrożeniowy:** meta `/kalkulator-wapnowania/` pod „ile wapna na ha" (590 vol leżące odłogiem).

---
_Wygenerowano 2026-05-20 (Wątek 5) na podstawie KEYWORD_RESEARCH_2026-05-19 + live MCP Agria.pl. MCP read-only — zero zmian w produkcji._
