# Inventory produktów AGRIA — WooCommerce

> Stan z MCP `Agria.pl:wc_products_list` na dzień **2026-05-19**.
> Do aktualizacji co kwartał lub przy znaczących zmianach w katalogu.

---

## Podsumowanie

| Liczba | Co |
|--------|----|
| **19** | produktów opublikowanych |
| **0** | wszystkie produkty mają SKU = `null` ⚠️ |
| **7** | kategorii używanych: Rolnictwo - wapno nawozowe, Sadownictwo, Rybactwo - wapno do stawów, Oczyszczalnie, Budownictwo, Hurtownie, Paszarstwo |

**Issue P1 dla audytu:** brak SKU na wszystkich produktach. Do uzupełnienia (zgodnie z konwencją katalogu drukowanego: AGR-001, AGR-002 itp.).

---

## Pełna lista (19 produktów)

| ID | Nazwa | Kategorie | Modyfikacja |
|----|-------|-----------|-------------|
| 302 | Dolomit | Rolnictwo, Hurtownie | 2026-03-25 |
| 303 | Kreda czarna(jeziorna) z kwasami humusowymi i węglem organicznym | Rolnictwo, Sadownictwo, Hurtownie | 2026-03-25 |
| 304 | Kreda malarska | Rolnictwo, Hurtownie | 2026-03-24 |
| 305 | Kreda nawozowa granulowana | Rolnictwo, Rybactwo, Hurtownie | 2026-03-25 |
| 306 | Kreda nawozowa sypka | Rolnictwo, Rybactwo, Hurtownie | 2026-03-24 |
| 307 | Kreda pastewna | Rolnictwo, Hurtownie, Paszarstwo | 2026-03-24 |
| 308 | Mieszanka tlenkowo-węglanowa | Rolnictwo, Sadownictwo | 2026-03-23 |
| 309 | Wapno hydratyzowane Bielik | Oczyszczalnie, Budownictwo | 2026-03-23 |
| 310 | Wapno nawozowe tlenkowe Agrobielik 70 | Rolnictwo, Sadownictwo, Rybactwo, Hurtownie | 2026-03-23 |
| 311 | Wapno nawozowe tlenkowe Agrobielik 90 | Rolnictwo, Rybactwo, Oczyszczalnie, Hurtownie | 2026-03-24 |
| 312 | Wapno nawozowe tlenkowe Oxyfertil 90 | Rolnictwo, Rybactwo, Oczyszczalnie, Hurtownie | 2026-03-25 |
| 313 | Wapno nawozowe tlenkowe zawierające magnez | Rolnictwo, Hurtownie | 2026-03-24 |
| 314 | Wapno nawozowe weglanowe bez magnezu granulowane | Rolnictwo, Sadownictwo, Hurtownie | 2026-03-24 |
| 315 | Wapno nawozowe weglanowe bez magnezu — Odmiana 04 | Rolnictwo, Sadownictwo, Hurtownie | 2026-03-25 |
| 316 | Wapno nawozowe weglanowe bez magnezu — Odmiana 05 | Rolnictwo, Sadownictwo | 2026-03-25 |
| 317 | Wapno nawozowe weglanowe zawierajace magnez granulowane | Rolnictwo, Sadownictwo, Hurtownie | 2026-03-13 |
| 318 | Wapno nawozowe weglanowe zawierajace magnez — Odmiana 04 | Rolnictwo, Sadownictwo | 2026-03-24 |
| 319 | Wapno nawozowe weglanowe zawierajace magnez — Odmiana 05 | Rolnictwo, Sadownictwo | 2026-03-13 |
| 320 | Wapno palone mielone wysokoreaktywne | Oczyszczalnie | 2026-03-23 |

---

## Mapowanie kategorii → segmenty (ze strategii)

| Kategoria WC | Segment strategiczny |
|--------------|----------------------|
| Rolnictwo - wapno nawozowe | A (duże gospodarstwa) |
| Sadownictwo | A (rolnictwo) |
| Rybactwo - wapno do stawów | C (rybactwo) |
| Oczyszczalnie | B (oczyszczalnie) |
| Budownictwo | E (budownictwo) |
| Paszarstwo | A (rolnictwo paszarstwo) |
| Hurtownie | D (dystrybutorzy) |

**Uwaga:** brakuje produktów / kategorii dla **Drogownictwa** (Segment F) — w katalogu drukowanym są (kruszywo, wapno palone drogowe), ale nie ma ich w WooCommerce. Decyzja do uzgodnienia z klientem: dodać do WC czy zostawić tylko w druku?

---

## Niespójności / TODO

1. **Brak SKU** na wszystkich 19 produktach.
2. **Drogownictwo** (kruszywo + wapno palone drogowe) — nie ma w WC, jest w katalogu drukowanym.
3. **Agrobielik 90 frakcja 2–8 mm** — jest w katalogu drukowanym jako AGR-002F, w WC tylko zwykły Agrobielik 90 (id 311). Decyzja: wariant produktu czy osobny SKU?
4. **Kreda czarna (jeziorna)** — wciąż w WC (id 303), choć została wycięta z katalogu drukowanego.
5. **Cement** — w katalogu drukowanym (AGR-019), nie ma w WC.
6. **Nazwy produktów** — niektóre mają literówki / brak polskich znaków („weglanowe" zamiast „węglanowe"). Do poprawy w SEO o-page.
7. **Oxyfertil 90** (id 312) — produkt jest, ale nie ma go w katalogu drukowanym. Decyzja: dodać do katalogu w kolejnej iteracji?

---

## Pobranie świeżych danych

```bash
# Przez MCP w Claude Code:
# Agria.pl:wc_products_list (limit: 100)
# Agria.pl:catalog_product (name lub product_id)
```

Aktualizacja tego pliku: ręcznie po każdym znaczącym przeglądzie. Można też zautomatyzować skryptem (n8n / GitHub Action) co kwartał.
