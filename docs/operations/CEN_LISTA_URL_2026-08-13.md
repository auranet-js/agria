# Ceny na stronie — lista dotkniętych URL-i

> Data: 2026-08-13. Podstawa: `CENNIK_PAWEL_2026-08-07.md` (15 z 19 kart), mockup zaakceptowany przez Janka 13.08.
> URL-e pobrane z **produkcji** (`product-sitemap.xml`), nie z bazy — Premmerce Permalink Manager buduje ścieżkę per kategoria.
> Status indeksacji zgodny z ADR `2026-08-11-podzial-rol-ads-seo.md`.

---

## A. Poza indeksem — landingi Google Ads (2 URL)

Zgodnie z ADR landingi obsługują wyłącznie ruch płatny. **Nie trafiają do sitemapy, nie są linkowane wewnętrznie.**

| URL | Stan dziś | Co robimy |
|---|---|---|
| `https://agria.pl/wapno-granulowane/` | istnieje, **`post_content` = 0 bajtów** | pełna treść + sekcja „Wapno granulowane — cena" (3 produkty granulowane) |
| `https://agria.pl/wapno-nawozowe/` | **nie istnieje**, 301 na `/wapno-nawozowe-na-trawnik/` | utworzyć + pełna treść + sekcja cenowa |

**Do dołożenia na obu: `noindex, follow`.** Dziś `/wapno-granulowane/` ma `index, follow` i self-canonical, czyli poza indeksem jest wyłącznie dlatego, że Google go nie odkrył. Od startu kampanii adres staje się publiczny — izolacja „przez nieodkrycie" przestaje wystarczać.

---

## B. W indeksie — karty produktowe z ceną (15 URL)

**KOREKTA 19.08.2026 (ADR `docs/decyzje/2026-08-19-dwie-warstwy-cen.md`): NIE ustawiamy ceny
w WooCommerce.** Pierwotny zapis brzmiał „cena od w WC, odblokowuje `offers` w schema” — **jest
nieaktualny**. Cena wchodzi **wyłącznie jako treść** (H2 z frazą cenową + akapit), `_price` zostaje
puste, wariantów nie tworzymy. Schema `Product`/`offers` budujemy **ręcznie, odzwierciedlając treść**.
Ceny w strukturze produktu to osobna, **niejawna** warstwa pod ofertownik.
Kwoty w tabeli poniżej pozostają aktualne — zmienia się wyłącznie miejsce publikacji, i **tylko
w przeliczeniu na tonę** (ceny za sztukę worka nie idą na stronę).

| # | URL | SKU | Cena „od" |
|---|---|---|---|
| 1 | `/wapno-nawozowe-rolnictwo/agrobielik-70/` | AGR-001 | 220 zł/t (luz 24 t) |
| 2 | `/wapno-nawozowe-rolnictwo/agrobielik-90/` | AGR-002 | 750 zł/t (frakcja 0–3 mm; 2–8 mm od 850) |
| 3 | `/wapno-nawozowe-rolnictwo/oxyfertil-90/` | AGR-003 | 790 zł/t (big-bag) |
| 4 | `/wapno-nawozowe-rolnictwo/mieszanka-tlenkowo-weglanowa/` | AGR-005 | 120 zł/t |
| 5 | `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-04/` | AGR-006 | 57 zł/t |
| 6 | `/wapno-nawozowe-rolnictwo/weglanowe-granulowane/` | AGR-008 | 350 zł/t (big-bag) · worki 25 kg od 380 zł/t |
| 7 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-04/` | AGR-009 | 50 zł/t |
| 8 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-odmiana-05/` | AGR-010 | 36 zł/t |
| 9 | `/wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/` | AGR-011 | 370 zł/t (big-bag) · worki 25 kg od 410 zł/t |
| 10 | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-granulowana/` | AGR-013 | 410 zł/t (big-bag) · worki 25 kg od 490 zł/t |
| 11 | `/wapno-nawozowe-rolnictwo/kreda-nawozowa-sypka/` | AGR-014 | 125 zł/t |
| 12 | `/paszarstwo/kreda-pastewna/` | AGR-015 | 190 zł/t (luz) · worki 30 kg od 610 zł/t |
| 13 | `/kreda-malarska/kreda-malarska/` | AGR-016 | 645 zł/t (worki 30 kg) |
| 14 | `/wapno-do-oczyszczalni/wapno-palone-mielone/` | AGR-017 | 950 zł/t (luz) · big-bag od 1 200 zł/t |
| 15 | `/wapno-hydratyzowane/bielik/` | AGR-018 | 945 zł/t (luz) · worki 25 kg od 1 220 zł/t |

**Jednostki: worki podajemy w zł/t, tak jak podał Paweł.** Ceny za sztukę są w mailu wyłącznie dla Agrobielika 70 (11,50 zł za worek 20 kg, 19,00 zł za 40 kg). Paweł napisał wprost: *„na ten moment nie będziemy prowadzić sprzedaży po worku"* — przeliczanie worków na zł/szt byłoby wbrew jego deklaracji.

**Anomalie cenowe — sprawdzone 13.08, temat zamknięty.** Weryfikacja na OLX: węglanowe z Mg odm. 05 (36 zł/t) wobec kopalni Józefka 45 zł/t, węglanowe bez Mg odm. 04 (57) wobec kopalni Lipa 63, kreda (125) wobec Kornicy/OMYA 100–120. **Magnezowe jest tańsze od zwykłego węglanowego także u konkurencji** — odmiana 05 ma niższą zawartość CaO (25–37%) niż odmiana 04 (min. 50%), więc płaci się za wapń, nie za magnez. Ceny AGRII są rynkowe, nie ma czego prostować.

⚠️ **Otwarte: czy cena obejmuje dostawę.** Paweł pisze przy każdej pozycji luzem „Luz, **dostawa całopojazdowa** (24 t) — od X zł/t netto". Nasza notatka zapisała to jako „loco magazyn, bez transportu". Jeśli cena jednak zawiera dostawę, planowane zdanie „Cena nie zawiera kosztów transportu" zaniża atrakcyjność oferty. **Blokuje publikację cen** — do rozstrzygnięcia w rozmowie 14.08.

---

## C. W indeksie — karty BEZ ceny, czekają na Pawła (4 URL)

Nie dotykamy do czasu rozmowy. Zostają jak są.

| URL | SKU | Dlaczego brak |
|---|---|---|
| `/wapno-nawozowe-rolnictwo/dolomit/` | AGR-012 | **PRIORYTET — fraza „dolomit" 6 600 wyszukań/mies., największa w projekcie.** Hipoteza: Paweł pominął celowo, bo słabo się sprzedaje |
| `/wapno-nawozowe-rolnictwo/wapno-tlenkowe-magnez/` | AGR-004 | pominięte bez komentarza |
| `/wapno-nawozowe-rolnictwo/weglanowe-odmiana-05/` | AGR-007 | pominięte, odm. 04 wyceniona |
| `/wapno-nawozowe-rolnictwo/kreda-czarna-jeziorna/` | brak SKU | status niejednoznaczny od dawna — opublikowana w WC, wycięta z katalogu drukowanego |

---

## D. W indeksie — nowa strona (1 URL)

| URL | Stan | Co |
|---|---|---|
| `https://agria.pl/ile-kosztuje-wapnowanie-hektara/` | **nie istnieje** | poradnik z przeliczeniem widełek na hektar. Fraza „ile kosztuje tona wapna" ma **najwyższy CPC w projekcie — 5,32 USD**. Wchodzi do sitemapy i do linkowania wewnętrznego (odwrotnie niż landingi) |

---

## E. W indeksie — zmiana pośrednia (1 URL)

| URL | Co się zmienia |
|---|---|
| `https://agria.pl/wapnowanie-gleby/` | **bez cen.** Dostaje wyłącznie link kontekstowy do poradnika cenowego z sekcji D. Hub rankuje na „ile wapna na hektar" (poz. 8,8 · 1 005 wyśw.) — to intencja dawki, nie ceny, i nie mieszamy jej cennikiem |

---

## Podsumowanie liczbowe

| Grupa | URL | W indeksie |
|---|---|---|
| A. Landingi Ads | 2 | **nie** (do dołożenia `noindex`) |
| B. Karty z ceną | 15 | tak |
| C. Karty bez ceny — nie ruszamy | 4 | tak |
| D. Nowy poradnik cenowy | 1 | tak (nowy wpis w sitemapie) |
| E. Hub — tylko link | 1 | tak |
| **Dotknięte łącznie** | **19** | 17 w indeksie, 2 poza |

## Skutki uboczne do przewidzenia

- **Re-crawl 15 kart.** Zmiana ceny to zmiana treści — Google odwiedzi je ponownie. To pożądane, bo przy okazji podchwyci `offers` w schema.
- **Sitemapa rośnie o 1 URL** (poradnik cenowy). Landingi do niej **nie** wchodzą.
- **Spójność trójkanałowa.** Ceny na stronie, w Google Ads i na OLX muszą być zgodne i nie mogą schodzić poniżej cen stałych odbiorców — Paweł podniósł część stawek właśnie dlatego (np. Wialan).
- **Zauważone przy okazji, poza zakresem:** `/kreda-malarska/kreda-malarska/` ma zdublowany człon w ścieżce. Nie ruszam przy tej operacji — zmiana URL-a zaindeksowanej karty wymaga przekierowania i osobnej decyzji.
