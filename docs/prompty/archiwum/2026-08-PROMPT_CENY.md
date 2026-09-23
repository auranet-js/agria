# Prompt startowy — ceny na stronie (wątek CEN)

> Utworzony 2026-08-07 po odpowiedzi Pawła na zapytanie o widełki cenowe.
> Uruchamiać w `~/projekty/agria`. Czytaj najpierw: `docs/operations/CENNIK_PAWEL_2026-08-07.md`.

## Stan wejściowy

Paweł przysłał widełki „od X zł/t" dla **15 z 19 kart** (mail 07.08, [201]). Ceny są **netto, loco magazyn, bez transportu**. Zapytanie, na które odpowiadał: `docs/operations/ZAPYTANIE_PAWEL_WIDELKI_CENOWE_2026-08-06.md`. Uzasadnienie strategiczne: `docs/seo/ANALIZA_CENY_NA_STRONIE_2026-08-06.md` (klaster cenowy ~1 320 wyszukań/mies, zerowa obecność AGRII).

## Zablokowane do decyzji Janka

1. **Worki** — publikujemy przeliczenie na tonę (575 / 475 zł/t), czy pomijamy? Paweł podał ceny za sztukę, deklarując jednocześnie, że sprzedaży po worku nie prowadzą. Cena tonowa miała być filtrem odsiewającym detalistę.
2. **Agrobielik 90** — dwie frakcje z różnymi cenami, jedna karta w WC (311). Jedna cena „od 750" z tabelką frakcji, czy warianty?

## Zadania

| ID | Zadanie | Zależność |
|---|---|---|
| CEN-03 | Dopytać Pawła o 4 brakujące pozycje — **dolomit priorytetowo** (fraza 6 600/mies), tlenkowe z Mg (313), węglanowe odm. 05 (316), kreda czarna (303). Przy okazji potwierdzić dwie anomalie cenowe z §3 cennika | telefon Janka |
| CEN-04 | Sekcja „Ile kosztuje…" na landingach `/wapno-nawozowe/` i `/wapno-granulowane/` — widełki + klauzula o braku charakteru oferty + informacja, że cena nie obejmuje transportu. **Bez** dopisku „mniejsze ilości — wycena indywidualna" (Paweł prosił o usunięcie) | decyzja 1 |
| CEN-05 | Cena „od" w WooCommerce na kartach — odblokowuje `offers` w schema `Product`, dziś generowanej bez oferty | decyzja 1 |
| CEN-06 | Poradnik „Ile kosztuje wapnowanie hektara" — przeliczenie na ha; „ile kosztuje tona wapna" ma najwyższy CPC w projekcie (5,32 USD). Naturalnie spina się z kalkulatorem, który rankuje #6 | CEN-04 |
| CEN-07 | Frazy cenowe do Google Ads | CEN-04 |

## Ograniczenia

- Ceny na stronie, w Ads i na OLX **nie schodzą poniżej cen stałych odbiorców** (Paweł podniósł część stawek właśnie dlatego, np. Wialan).
- Edycja ceny musi zostać kilkuminutowa (pole w Elementorze + cena „od" w WC) — to było obiecane Pawłowi.
- Nie krytykujemy stanu strony w komunikacji do klienta (`feedback_agria_no_self_criticism_built_site`).
