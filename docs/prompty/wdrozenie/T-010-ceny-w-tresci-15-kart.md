# T-010 — widełki „od X zł/t netto" w treści 15 kart + 2 landingi Ads + poradnik cenowy

| | |
|---|---|
| **Linia / zakres** | Ceny · **R** (ryczałt) |
| **Status** | 🔴 teraz, **priorytet 1** — 12 dni od cennika, 6 od akceptu mockupu |
| **Zgłosił** | Paweł, 07.08.2026 |
| **Szacunek** | 6–8 h (15 kart × ~20 min + 2 landingi + poradnik + schema) |
| **Idzie razem z** | `T-011` (nagłówki H2 cenowe) — ta sama robota na tych samych kartach, nie rozdzielaj |

---

## 1. Czego to dotyka

**Warstwy danych:** `post_content` 15 produktów WooCommerce · `_elementor_data` tych samych
produktów (jeśli karta renderuje z Elementora) · meta Rank Math (`rank_math_description`) ·
schema `Product`/`offers` budowana ręcznie · sitemapa (rośnie o 1 URL — poradnik).

**Systemy poza stroną:** Google Ads (kampania Rolnictwo kieruje na te URL-e — po zmianie treści
Quality Score i trafność strony docelowej się przeliczą) · OLX (ceny muszą być zgodne, konkurencja
czyta oba kanały) · GSC (re-crawl 15 kart).

**Pliki źródłowe:** `docs/operations/CENNIK_PAWEL_2026-08-07.md` (kwoty),
`docs/operations/CEN_LISTA_URL_2026-08-13.md` (mapowanie URL↔SKU↔cena),
`docs/decyzje/2026-08-19-dwie-warstwy-cen.md` (dlaczego bez `_price`).

## 2. Strefy kruche — co tu pęka

1. **`_price` musi zostać puste we wszystkich 19 produktach.** To nie jest zaniedbanie, tylko
   decyzja (ADR 19.08). Wpisanie ceny w WooCommerce uruchamia drugą, **niejawną** warstwę
   ofertownika i wypuszcza kwoty przez REST Store API — sprawdzone 19.08:
   `https://agria.pl/wp-json/wc/store/v1/products` jest **publiczne** i zwraca pole `prices`
   (dziś `"price":"0"`). Wpisujesz cenę w WC → w tej samej sekundzie widzi ją każdy, kto zna URL.
2. **Cztery karty bez ceny zostają nietknięte** — Dolomit (302), Kreda czarna (303), Tlenkowe
   z Mg (313), Węglanowe odm. 05 (316). Paweł ich nie wycenił. Nie improwizuj, nie licz średniej.
3. **Ceny workowe — decyzja Janka nierozstrzygnięta.** `FAKTY_KLIENTA.md` §7: publikować wyłącznie
   przeliczenia na tonę; Paweł napisał „nie będziemy prowadzić sprzedaży po worku". **Zapytaj Janka
   na starcie jednym zdaniem**, zanim napiszesz pierwszą kartę — nie po fakcie.
4. **Żargon = zakaz twardy.** „loco", MOQ, franco, EXW, HDS. Cennik źródłowy jest napisany w tym
   języku („netto, loco magazyn"), na stronie to brzmi **„cena za towar, bez transportu"**.
5. **Bez progu ilościowego.** Nie „minimum 24 t", tylko „przy 24 t cena wynosi od X" — Paweł zdjął
   formy dostawy z kart właśnie dlatego, że „zapis nas ogranicza" (T-002). Nie wracaj tylnymi drzwiami.
6. **Dwie warstwy treści.** Zanim napiszesz do `post_content`, sprawdź per produkt, czy karta
   renderuje z `_elementor_data`. Na ID 731 słowo „ertyfikat" siedzi w obu warstwach naraz —
   ten sam wzorzec może być na kartach.
7. **Landing `/wapno-granulowane/` ma dziś `index, follow` i `post_content` = 0 bajtów.** Wypełnienie
   treścią bez jednoczesnego `noindex` wpuszcza go do indeksu i uruchamia kanibalizację, którą
   ADR 11.08 zmierzył na frazie „wapno bielik" (6 URL-i → pozycja 15,3).

## 3. Stan zmierzony 19.08.2026

```
MCP query_db:      19 produktów WC, 19 z pustym _price, 0 ze słowem „cena" w treści
REST Store API:    publiczne, prices.price = "0" dla wszystkich (wektor wycieku po wpisaniu cen)
Ads API 14 dni:    Rolnictwo 199,62 zł / 100 klików / 682 wyśw. / 0 konwersji
15 URL-i docelowych: wszystkie HTTP 200 (sprawdzone pojedynczo 19.08)
/wapno-granulowane/: istnieje, post_content 0 B, index+follow
/wapno-nawozowe/:    nie istnieje, 301 na /wapno-nawozowe-na-trawnik/
```

**Które karty renderują z Elementora — sprawdzone, nie zgadywane.** Z 19 produktów `_elementor_data`
mają **tylko trzy**:

| ID | slug | `post_content` | `_elementor_data` | w zakresie T-010 |
|---|---|---|---|---|
| **307** | `kreda-pastewna` | 5 254 B | **7 549 B** | tak (`/paszarstwo/kreda-pastewna/`) |
| **310** | `agrobielik-70` | 6 718 B | **6 884 B** | tak |
| **320** | `wapno-palone-mielone` | 6 348 B | **6 558 B** | tak |

Pozostałych **16 produktów nie ma `_elementor_data` w ogóle** — renderują z `post_content`,
więc zwykły zapis wystarczy. **Trzy powyższe wymagają edycji warstwy Elementora**; zapis samego
`post_content` na nich nic nie zmieni na froncie. To dokładnie te trzy ID, o których mówi
`CLAUDE.md` §4 pkt 2.

Koszt zwłoki jest policzony: 33 % wydatku kampanii to zapytania cenowe lądujące na stronach bez ceny.

## 4. Warunki wejścia

- [ ] Janek rozstrzygnął pytanie o worki (tylko zł/t, czy także zł/szt.).
- [ ] Potwierdzone, że ceny są **bez transportu** — cennik mówi to wprost (potwierdzenie Janka 07.08,
      „cena jak ktoś przyjedzie"); kwestia z rozpiski 13.08 jest tym zamknięta.
- [ ] `db_export` tabel `posts` + `postmeta` zrobiony i przeniesiony poza web root.

## 5. Co robisz — krok po kroku

1. Zapytaj Janka o worki (jedno zdanie) i o zgodę na zapis pierwszej karty jako wzorca.
2. `db_export(['posts','postmeta'], label='przed-T-010')`, przenieś plik `.sql` przez SSH poza
   `wp-content/`, skasuj oryginał.
3. Dla **jednej** karty (Agrobielik 70, `/wapno-nawozowe-rolnictwo/agrobielik-70/`, AGR-001, 220 zł/t):
   ustal, z której warstwy renderuje treść — `query_db` na `post_content LIKE` i `_elementor_data LIKE`
   dla frazy z widocznego akapitu.
4. Napisz blok cenowy: `<h2>` z frazą cenową (to jest **T-011**, ta sama edycja) + akapit
   z widełkami, warunkiem dostawy i dwoma punktami odniesienia + klauzula prawna.
5. Pokaż Jankowi treść bloku **przed** zapisem. Po „ok" — zapis z `expect_old_len`.
6. Weryfikuj render przez Chrome MCP (nie przez bazę), potem `curl` na kod HTTP i obecność frazy.
7. Powtórz dla pozostałych 14 kart wg tabeli B w `CEN_LISTA_URL_2026-08-13.md`.
8. Landingi: `/wapno-granulowane/` — treść **z gotowego wzorca działającej strony** (obejrzyj przez
   Chrome MCP i powiel strukturę, nie pisz surowego HTML-a do `post_content`) + `noindex, follow`.
   `/wapno-nawozowe/` — utworzyć analogicznie.
9. Poradnik `/ile-kosztuje-wapnowanie-hektara/` — nowy wpis, wchodzi do sitemapy i linkowania.
10. Link kontekstowy z huba `/wapnowanie-gleby/` do poradnika. **Bez cen na hubie.**
11. Schema `Product`/`offers` — ręcznie, odzwierciedlając treść, nie z bazy.

## 6. Jak sprawdzasz w trakcie

- Po każdej karcie: `expect_old_len` musi się zgodzić (`match: true`) — jeśli nie, ktoś edytował
  równolegle, zatrzymaj się.
- Po każdej karcie: `curl -s <URL> | grep -c "zł/t"` ≥ 1.
- Co pięć kart: `query_db` liczące, ile produktów ma `_price` niepuste — **musi być 0**.

## 7. Jak testujesz po wdrożeniu

```bash
# 1. Treść jest na wszystkich 15 kartach
for u in $(sed -n 's/^| [0-9]* | `\([^`]*\)`.*/\1/p' docs/operations/CEN_LISTA_URL_2026-08-13.md); do
  printf '%s → ' "$u"; curl -s "https://agria.pl$u" | grep -o 'zł/t' | head -1
done
# 2. _price nadal puste w 19/19  (MCP query_db)
SELECT COUNT(*) FROM {prefix}postmeta WHERE meta_key='_price' AND meta_value <> ''
# 3. Store API nie ujawnia kwot
curl -s "https://agria.pl/wp-json/wc/store/v1/products?per_page=20" | grep -o '"price":"[^"]*"' | sort -u
# 4. Landingi poza indeksem
for u in /wapno-granulowane/ /wapno-nawozowe/; do curl -s "https://agria.pl$u" | grep -o 'content="noindex[^"]*"'; done
# 5. Render, nie baza
Chrome MCP: navigate + get_page_text na 3 losowych kartach — H2 i akapit muszą być widoczne
```

## 8. Dowód do rejestru

Wklejasz: liczbę kart ze słowem „cena" w treści (dziś 0/19, po wdrożeniu 15/19), wynik zapytania
o `_price` (musi zostać `0`), wynik `grep noindex` z obu landingów, URL poradnika z `page-sitemap.xml`,
hash commitu z aktualizacją rejestru.

## 9. Rollback

`db_export` z kroku 2 → przywrócenie `post_content`/`postmeta` per ID przez `query_db_write` UPDATE
(nie import całej tabeli). Landingi: `noindex` zostaje, treść wraca do stanu 0 B.
Poradnik: `wp post delete <ID>` przez SSH + usunięcie z sitemapy (RankMath przebuduje sam,
pliki `uploads/rank-math/*.xml` skasować FTP-em).

## 10. Rozliczenie

Zakres **R**. Do DZIENNIKA M3 jako jedna pozycja razem z T-011 (rozdzielanie godzin między nie
jest sztuczne — to jedna edycja). Godziny realne, nie gwiazdka.

## 11. Recheck

| Kiedy | Co i czym |
|---|---|
| **+1 h** | render 15 kart przez Chrome MCP — czy Elementor nie nadpisał; `_price` nadal puste |
| **+24 h** | Ads: czy CTR i śr. CPC kampanii Rolnictwo drgnęły (`ads_call.sh`, porównaj z 199,62 zł / 100 klików) |
| **+72 h** | GSC URL Inspection na 3 kartach — czy Google zaciągnął nową treść |
| **+7 dni** | pozycje na frazach cenowych („wapno granulowane cena", „agrobielik cena") — `scripts/seo_baseline.py` |
| **+14 dni** | czy Paweł czegoś nie poprawił ręcznie w Elementorze — porównanie `post_modified` |
