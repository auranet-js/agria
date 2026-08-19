# Content audit + topic clusters + kalendarz M2–M6 — AGRIA

> **STATUS: CZĘŚCIOWO UNIEWAŻNIONY (2026-08-19).** Sekcja **§3 „Topic clusters (hub & spoke)”**
> — HUB Rolnictwo / Rybactwo / Oczyszczalnie — **jest nieaktualna i nie wolno jej realizować.**
> Zdjął ją ADR `docs/decyzje/2026-08-11-podzial-rol-ads-seo.md`: landingi i huby segmentowe istnieją
> wyłącznie jako cele Google Ads, poza indeksem, bo zmierzono kanibalizację (6 URL-i na frazę
> „wapno bielik” → pozycja 15,3). Reszta dokumentu — inwentarz treści i kalendarz — nadal ważna.
> Aktualny stan zobowiązań: `docs/REJESTR_ZOBOWIAZAN.md`.

> Deliverable M1 #4. Data: 2026-06-15. Źródła: live MCP Agria (inwentarz treści), `KEYWORD_RESEARCH_2026-05-19.md` (112 fraz / 8 klastrów), `ONPAGE_PLAN_2026-05-20.md`.

## ⚠️ KOREKTA (2026-06-15, po decyzji Janka)

**Oferta WC jest KOMPLETNA (19 produktów) — nie dodajemy produktów.** Drogownictwo JEST segmentem AGRIA, ale obsługiwanym **istniejącymi produktami**, nie nowym asortymentem:
- ❌ **NIE ścigamy `kruszywo` (9 900) / `kruszywo granitowe` / `kruszywo 0-31`** — to kruszywo łamane/granitowe na podbudowy, którego AGRIA NIE produkuje. ~95% volume klastra drogowego = poza asortymentem.
- ✅ **Addresowalne istniejącymi produktami:** `stabilizacja gruntu` (720/mies, CPC $2,13) → **Wapno palone mielone #320** + Bielik hydratyzowany #309. Akcja = **landing „Wapno do stabilizacji gruntów" + poradnik**, NIE nowy produkt.

Reszta: oferta = 19 produktów, Kreda czarna #303 zostaje, Agrobielik 90 #311 opisany poprawnie (bez zmian), SKU = konwencja PRODUCT_DATA_MAPPING. Realne segmenty content: rolnictwo, sadownictwo, rybactwo, oczyszczalnie, budownictwo (Bielik), paszarstwo + stabilizacja gruntów (drogownictwo).

---

## 1. Inwentarz treści (stan live)

**Produkty: 19** (publish) w 8 kategoriach:
| Kategoria (product_cat) | Produktów | Klaster KR | Volume/mies |
|---|---|---|---|
| Rolnictwo – wapno nawozowe | 17 | Rolnictwo | ~3 240 |
| Hurtownie | 13 | (przekrojowa) | — |
| Sadownictwo | 9 | Rolnictwo/Sad | (w rolnictwie) |
| Rybactwo – stawy | 5 | Rybactwo | ~240 |
| Oczyszczalnie | 4 | Oczyszczalnie | ~170 |
| Budownictwo | 1 | Budownictwo | ~3 670 |
| Paszarstwo (kreda pastewna) | 1 | Paszarstwo | ~150 |

**Blog: 6 wpisów** — wapnowanie gleby, stawy karpiowe, cement, jak murować klinkier, wykwity na murze, tynki. (+2 auto-draft)
**Strony: 11** — Home, Oferta, O firmie, Kontakt, Poradniki, Kalkulator wapnowania, Do pobrania, RODO, Wsparcie, Zamówienia, Cart.

## 2. Dopasowanie treści ↔ klastry (gdzie jest rozjazd)

| Klaster | Volume | Produkty | Wpisy blog | Diagnoza |
|---|---|---|---|---|
| **Drogownictwo** | **~14 040** | **0** | 0 | 🔴 Największe volume w całym researchu, ZERO pokrycia. Zależne od decyzji „kruszywo/cement do WC?" (`CATALOG_VS_WC_GAP`). |
| Budownictwo | ~3 670 | 1 | **4** | 🟠 Content przeinwestowany (4/6 wpisów) vs 1 produkt. Treść jest, nie ma czego sprzedać → ruch informacyjny bez konwersji. |
| Rolnictwo | ~3 240 | 17 | 1 | 🟢 Produkty pokryte, ale tylko 1 poradnik przy największej liczbie fraz informacyjnych. Niedobór contentu poradnikowego. |
| Rybactwo | ~240 | 5 | 1 | 🟢 OK, proporcjonalnie. |
| Oczyszczalnie | ~170 | 4 | 0 | 🟡 Niskie volume, wysoka wartość per lead, B2B przetargowy. Brak contentu informacyjnego + FAQ/AEO. |
| Paszarstwo | ~150 | 1 | 0 | 🟡 Cienko, niszowo. |

**Wniosek strategiczny:** blog ciągnie w stronę budownictwa (gdzie 1 produkt), a niedoinwestowane są: (a) **drogownictwo** — ogromne volume, decyzja katalogowa, (b) **rolnictwo** — rdzeń oferty, brak poradników pod frazy informacyjne ściągające rolników.

## 3. Topic clusters (hub & spoke)

Architektura pod pozycjonowanie informacyjne → produktowe:

**HUB Rolnictwo** (`/poradniki/` + LP rolnicy) → spokes:
- „ile wapna na hektar" · „jak wapnować glebę" · „pH gleby — tabela i odczyt" · „odkwaszanie gleby" · „wapno tlenkowe vs węglanowe" → linkują do kategorii Rolnictwo + Agrobielik 70/90.

**HUB Rybactwo** (LP stawy) → „ile wapna do stawu" · „pH stawu rybnego" · „wapnowanie stawów — kiedy" → produkty stawowe. *(1 wpis już jest)*

**HUB Oczyszczalnie** (LP oczyszczalnie) → „higienizacja osadów wapnem" · „stabilizacja osadów — PN-EN 459-1" · FAQ/AEO → Wapno palone mielone + Bielik.

**HUB Budownictwo** (istniejące 4 wpisy) → dopiąć do produktu Bielik hydratyzowane + rozważyć poszerzenie oferty budowlanej (inaczej content nie konwertuje).

**HUB Drogownictwo** (warunkowy — po decyzji katalogowej) → „stabilizacja gruntów wapnem" · „kruszywo wapienne — zastosowanie" · „mączka/m/kruszywo cena" → nowa kategoria/produkty.

## 4. Kalendarz content M2–M6 (20 tematów, 4/mies)

> Priorytet wg volume × dopasowanie do oferty. Sezonowość rolnictwa: marzec–kwiecień + wrzesień–październik.

**M2 (lipiec) — Rolnictwo rdzeń:** 1) Ile wapna na hektar — kalkulator i tabela 2) Jak wapnować glebę krok po kroku 3) Wapno tlenkowe vs węglanowe — co wybrać 4) pH gleby — jak odczytać i poprawić

**M3 (sierpień) — Rolnictwo + Sad:** 5) Odkwaszanie gleby — kiedy i czym 6) Wapnowanie sadu — terminy 7) Magnez w wapnie — kiedy potrzebny 8) Wapno granulowane vs sypkie

**M4 (wrzesień) — Oczyszczalnie + Rybactwo (sezon jesienny):** 9) Higienizacja osadów wapnem 10) Stabilizacja osadów — PN-EN 459-1 11) Ile wapna do stawu 12) pH stawu rybnego

**M5 (październik) — Drogownictwo/Budownictwo (warunkowo):** 13) Stabilizacja gruntów wapnem 14) Kruszywo wapienne — zastosowania 15) Wapno hydratyzowane w budownictwie 16) Mleko wapienne — zastosowanie

**M6 (listopad) — Long-tail + AEO:** 17) Czy wapno palone jest szkodliwe — bezpieczeństwo 18) Wapno do kurnika/hodowli 19) Wapnowanie a plon — case 20) FAQ surowce wapniowe (AEO pod AI Overviews)

## 5. Wejścia do innych deliverables

- **#5 plan on-page:** produkty rolnictwo — title/H1 pod realne zapytania (np. „wapno nawozowe tlenkowe odmiana…"); kategorie jako LP per segment.
- **Decyzja katalogowa (handlowiec):** drogownictwo (14k volume) czeka na „kruszywo/cement do WC?" — bez tego największy klaster zostaje nieobsłużony.
- **Kreda czarna jeziorna** (produkt #303, status „wycięta"/publish?) — do rozstrzygnięcia, wpływa na inwentarz.
