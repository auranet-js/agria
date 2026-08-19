# ADR 2026-08-19 — dwie niezależne warstwy cen: treść SEO vs ofertownik

**Status:** obowiązująca · decyzja Janka 19.08.2026
**Dotyczy:** CEN-01, CEN-02, OFE-01 w `docs/REJESTR_ZOBOWIAZAN.md`
**Koryguje:** `docs/operations/CEN_LISTA_URL_2026-08-13.md` §B, memory `project_agria_ceny_strategia`

---

## Decyzja

**Ceny w projekcie AGRIA żyją w dwóch warstwach, które nigdy się nie stykają.**

| | Warstwa **A — treść SEO** | Warstwa **B — ofertownik** |
|---|---|---|
| Po co | żeby rankować na frazy cenowe (`wapno granulowane cena` i pokrewne, klaster ~1 320/mies.) | żeby handlowiec wycenił zamówienie z transportem |
| Gdzie siedzi | **wyłącznie w treści strony** — nagłówek H2 + akapit | warianty WooCommerce, cennik wtyczki `agria-ofertownik-by-auranet` |
| Widoczność | publiczna, to jest cały sens | **nigdzie nie ujawniana** — wewnętrzna |
| Skąd wartości | cennik Pawła 07.08, przeliczony na tonę | cennik Pawła + różnicowanie per zakład, robione przez AGRIĘ |
| Kto właścicielem | AGRIA (usługa w ryczałcie) | **Auranet — projekt własny, nie billable** |

**To nie są te same ceny i nigdy nie były.** Warstwa A to komunikat marketingowy („od 220 zł/t
przy dostawie całopojazdowej"). Warstwa B to dane operacyjne, które w ofertowniku zostaną
rozbite per zakład wysyłkowy i obłożone kosztem transportu — ta sama tona z Sitkówki i z Niedomic
ma inną cenę końcową.

---

## Co z tego wynika — twarde reguły wykonania

### Warstwa A (CEN-01 / CEN-02) — teraz

1. **NIE ustawiamy `_price` w WooCommerce.** Karty zostają w trybie katalogu, `_price` puste
   w 19/19 tak jak dziś.
2. **NIE tworzymy wariantów** ani atrybutów cenowych pod publikację treści.
3. Cena wchodzi **wyłącznie jako treść**: `<h2>` z frazą cenową (np. „Wapno granulowane — cena")
   plus akapit z widełkami, warunkiem dostawy i klauzulą prawną.
4. **Schema `Product` / `offers` budujemy ręcznie, odzwierciedlając treść** — nie generujemy jej
   z `_price`, wariantów ani atrybutów. Dziś karta emituje `Product` z 18 `PropertyValue`
   i **zerem `offers`** (sprawdzone na `/wapno-nawozowe-rolnictwo/agrobielik-70/`, 19.08) —
   miejsce jest puste i trzeba je wypełnić świadomie, wartością zgodną z tym, co widzi człowiek.
5. Ceny **wyłącznie przeliczone na tonę.** Ceny za sztukę worka nie idą na stronę — Paweł napisał
   07.08 „na ten moment nie będziemy prowadzić sprzedaży po worku", a „11,50 zł za worek 20 kg"
   działa odwrotnie niż filtr, który miała pełnić cena tonowa. Decyzja Janka 19.08.

### Warstwa B (OFE-01) — osobno

6. **Ofertownik prowadzimy jako osobny wątek**, nie jako warunek wstępny CEN-01. Wcześniejsze
   powiązanie („audyt wycieku cen przed wpisaniem cen") **odpada**, bo CEN-01 nie dotyka już
   struktury produktu.
7. **Ceny warstwy B nie mogą wyciec.** To nabiera wagi właśnie dlatego, że mają zamieszkać
   w wariantach WooCommerce, a WooCommerce domyślnie je pokazuje — na froncie, w REST API,
   w feedach, w schema generowanej przez Rank Math. Audyt wycieku cen z etapu zerowego
   ofertownika przestaje być porządkami, a staje się **warunkiem bezpieczeństwa danych klienta**.
8. Ofertownik pozostaje **projektem własnym Auranet** — nie fakturujemy go AGRII na tym etapie
   (decyzja Janka 18.08). Tym bardziej ceny w nim zaszyte nie są materiałem do publikacji.

---

## Dlaczego to zapisujemy jako ADR

Ta decyzja jest dokładnie tego typu, który w tym projekcie ginął: rozstrzygnięcie zapada
w rozmowie, wykonanie idzie do innego wątku, a dokument z rozpiską mówi co innego.
`CEN_LISTA_URL_2026-08-13.md` §B mówi wprost „Cena »od« w WooCommerce. Odblokowuje `offers`
w schema `Product`" — czyli **odwrotnie niż ta decyzja**. Bez ADR-a i wpisu w memory następna
sesja otworzyłaby rozpiskę i wpisała ceny do bazy.

Powiązane: memory `project_agria_dwie_warstwy_cen`, `docs/FAKTY_KLIENTA.md` §7,
`docs/prompty/2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md`.
