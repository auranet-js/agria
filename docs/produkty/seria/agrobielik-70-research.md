# Research — #310 Agrobielik 70 (T-136 seria)

> 14.09.2026 · pełny stan karty: [`../agrobielik-70.md`](../agrobielik-70.md) (§4–§8 — nie przepisuję)
> GSC 28 dni 2026-08-14 … 09-10: `data/produkty/seria/gsc-310-28d-2026-09-14.json` · 90 dni: `data/produkty/gsc/agrobielik-70.json` ·
> SERP mobile 10.09 z PAA: `data/produkty/dfs/serp-agrobielik-70-2026-09-10.json` · planer: `data/produkty/ads/agrobielik-70-planer.json` · **DataForSEO: 0 USD.**

## 0. Warstwa renderu — INNA niż w dotychczasowych kartach

`_elementor_edit_mode = builder`, `_elementor_data` 7 313 B → **render z Elementora** (`data-elementor-type="product-post" data-elementor-id="310"`;
#312 i #315 tego kontenera nie mają). Dowód: „Odczyn pH >12" jest tylko w `post_content` — w renderze 0 trafień (curl 14.09).
Oba pola mają poza tym tę samą treść (podobieństwo słów 0,996). **Edycja samego `post_content` nic by nie zmieniła.**
Wdrożenie: `post_content` jak w pozostałych kartach + zdjęcie `_elementor_edit_mode` → szablon produktu renderuje `post_content` jak dla #307
(ma `_elementor_data` bez znacznika builder). `_elementor_data` zostaje w bazie; cofnięcie = przywrócenie jednej wartości meta.

## 1. Frazy, które należą do tej karty

| fraza | wyszukań/mies. | GSC karty | przydział |
|---|---|---|---|
| agrobielik · agrobielik 70 · wapno agrobielik · …cena · …big bag · …20 / 40 kg | ≈ 20 łącznie | SERP: `agrobielik 70` **abs 1**, `agrobielik` abs 6 | **#310** |
| wapno tlenkowe cena · …cena za tonę · …big bag · …sypkie · …luzem · wapno tlenkowe 70 | 50 · 30 · 50 · 20 · 10 · 10 | hub / stary adres big-bag 33 wyśw. poz. 11,9 (301 → #310) | **#310** — podstawowe wapno tlenkowe sypkie w ofercie; do rewizji w D1 |
| wapno tlenkowe czy węglanowe · …a węglanowe · agrobielik 70 czy 90 | 10 · 10 · <10 | 0 | **#310** (FAQ) |
| wapno nawozowe tlenkowe | 50 | **#310 17 wyśw. poz. 10,7** (28 dni) · #312 poz. 10 | D1 (przypisane przy #312); H1 karty = nazwa WC i tak je niesie |
| **wapno tlenkowe** | **720** | hub, #313 | **D1** |
| nordkalk wapno · wapno nordkalk · nordkalk wapno sitkówka | 480 · 210 · 30 | 0 | D1 (5 produktów Nordkalku); producent i zakład w treści |
| wapno tlenkowe dawkowanie · ile na hektar · ile wapna tlenkowego na hektar | 40 · 20 · 20 | hub 87–105 wyśw. | **hub** — karta: 2–6 t/ha + link |
| wapno tlenkowe do stawu | 90 | hub 1 | **D4 / `/wapno-do-stawu/`** — karta: dawka stawowa z karty + link |

## 2. Co Google nagradza

`agrobielik 70`: #310 abs 1, dalej CARLOS (OLX, 210 zł/t z odbiorem w Sitkówce), producent, sklepy z workiem 25 kg. `wapno tlenkowe`: OLX, osadkowski,
sklepy z workiem 20 kg; AGRIA abs 22 (#313). **PAA:** „Kiedy stosować wapno tlenkowe?" · „Które wapno jest lepsze: węglanowe czy tlenkowe?" ·
„Jakie wapno na szybkie odkwaszenie gleby?" · „Ile wapna tlenkowego na 1 ha?" · „Co to jest wapno tlenkowe?" · „Ile kosztuje 1 tona wapna?"

## 3. Czego szuka kupujący

- **Zapytań ofertowych: 0.** Ads nie kierowały na kartę.
- **GSC karty, 28 dni:** 7 klik. / 160 wyśw. / CTR 4,38% / poz. 6,3 — próg prywatności ukrywa wszystkie kliknięcia.
- Kupujący pyta o: szybkość działania, termin, dawkę (pole i staw), tlenkowe czy węglanowe, cenę za tonę i big-bag.

## 4. Co z tego wynika dla treści (karta PDF, atest 46/25 jako dokument, `[C]`, `[F]`)

1. **Z karty PDF nieobecne na stronie:** „bez ryzyka wypalenia próchnicy na glebach średniociężkich" · „idealne przed zasiewami wiosennymi i jesiennymi" ·
   łąki · „Dostawy własną flotą z magazynów Niedomice i Sitkówka" · „Marka Agrobielik — od 1989 roku" · wiersz „Forma dostawy".
2. **Odmiana 02** — z atestu OSChR 46/25 (dokument na `/do-pobrania/`), dziś tylko w schemacie; atest i karta PDF — linki pod specyfikacją.
3. **Rozróżnienie z Bielikiem (#309)** — FAQ, bo „wapno bielik" trafia na kartę #310 (poz. 69).
4. **Porównanie** z Agrobielikiem 90 (0–3 mm) i mieszanką tlenkowo-węglanową (#308 — ta sama zawartość CaO, dawka i szybkość na kartach, inna cena), bez ocen.
5. **Cena:** od 220 zł/t luzem (bez tonażu); big-bag i worki 20/40 kg bez kwot (cennik: 400 zł/t BB, 11,50 i 19 zł/szt.).
6. **Usunąć (DescWriter):** plony +15–20% (×3), pH >12 (FAQ 3, 5), „odkaża dno stawu", „Dezynfekcja", mineralizacja mułu, rekultywacja,
   „gleby ciężkie", stawy 2–3 tygodnie, „35-letnie doświadczenie", title „70 70%".
