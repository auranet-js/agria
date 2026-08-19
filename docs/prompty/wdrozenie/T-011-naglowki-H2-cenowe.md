# T-011 — nagłówki H2 z frazą cenową na kartach produktów

| | |
|---|---|
| **Linia / zakres** | Ceny · **R** |
| **Status** | 🔴 teraz — wykonywane **w tej samej edycji co T-010**, nie osobno |
| **Zgłosił** | Janek, 19.08.2026 |
| **Szacunek** | 0 h dodatkowych, jeśli idzie z T-010; ~3 h, jeśli ktoś rozdzieli |
| **Prompt pomocniczy** | `docs/prompty/2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md` (136 linii, wzorce zdań) |

---

## 1. Czego to dotyka

Wyłącznie **warstwa nagłówków** w treści tych samych 15 kart co T-010: `<h2>` w `post_content`
lub w widgecie Elementora. Pośrednio: struktura nagłówków całej karty (H1 → H2 → H3), którą
Google czyta jako mapę tematu, oraz frazy cenowe, na które karta ma zacząć rankować.

## 2. Strefy kruche

1. **Jeden H1 na stronę.** Karty produktowe mają H1 z nazwą produktu. Nowy blok cenowy musi być
   H2, nie H1 — dwa H1 psują strukturę i nic nie zyskują.
2. **Fraza w H2 musi być tą, której ludzie szukają**, nie tą, która ładnie brzmi. „Wapno granulowane
   cena" > „Ile kosztuje nasze wapno granulowane". Sprawdź wolumen w danych, które już mamy
   (`data/`, `docs/seo/`), nie zgaduj.
3. **H2 bez akapitu pod spodem to spam.** Nagłówek cenowy zawsze z treścią — widełki, warunek
   dostawy, dwa punkty odniesienia. Sam nagłówek Google potraktuje jako doorway.
4. **Kanibalizacja wewnątrz karty.** Jeśli karta ma już H2 typu „Cennik" albo „Zamówienia" —
   nie dokładaj drugiego cenowego, przepisz istniejący.
5. **Elementor przechowuje nagłówki jako osobne widgety** (`elType: widget`, `widgetType: heading`).
   Wstawienie H2 przez `post_content` na stronie renderującej z Elementora **nie da efektu** —
   sprawdź warstwę przed edycją.

## 3. Stan zmierzony 19.08.2026

```
0 z 19 kart ma dziś nagłówek zawierający słowo „cena"
0 z 19 kart ma cenę w treści w jakiejkolwiek formie
```

**Warstwa renderująca — sprawdzone 19.08:** `_elementor_data` mają wyłącznie trzy produkty —
**307** (`kreda-pastewna`), **310** (`agrobielik-70`), **320** (`wapno-palone-mielone`).
Na tych trzech nagłówek musi powstać jako **widget Elementora**, nie jako `<h2>` w `post_content`.
Pozostałe 16 produktów nie ma tej meta w ogóle i renderuje z `post_content`.

## 4. Warunki wejścia

- [ ] T-010 w toku lub gotowy — H2 bez treści cenowej nie ma sensu.
- [ ] Lista fraz cenowych per produkt ustalona (z danych, nie z głowy).

## 5. Co robisz

1. Dla każdej z 15 kart wybierz frazę cenową odpowiadającą produktowi
   (np. Agrobielik 90 → „agrobielik cena", wapno węglanowe granulowane → „wapno granulowane cena").
2. Ustal warstwę renderującą nagłówki tej karty (`post_content` czy `_elementor_data`).
3. Wstaw H2 razem z akapitem T-010 — **jedna operacja zapisu na kartę**, nie dwie.
4. Zweryfikuj strukturę nagłówków po zmianie: dokładnie jeden H1, H2 cenowy obecny.

## 6. Jak sprawdzasz w trakcie

Po każdej karcie:
```bash
curl -s "https://agria.pl<URL>" | grep -oP '<h[12][^>]*>[^<]{0,80}' | head -6
```
Ma pokazać jeden `<h1>` z nazwą produktu i `<h2>` z frazą cenową.

## 7. Jak testujesz po wdrożeniu

```bash
# H2 cenowy na wszystkich 15 kartach
URLS=$(sed -n 's/^| [0-9]* | `\([^`]*\)`.*/\1/p' docs/operations/CEN_LISTA_URL_2026-08-13.md)
for u in $URLS; do
  printf '%s → ' "$u"
  curl -s "https://agria.pl$u" | grep -oiP '<h2[^>]*>[^<]*cena[^<]*' | head -1 || echo BRAK
done
# Dokładnie jeden H1 na kartę
for u in $URLS; do printf '%s h1=%s\n' "$u" "$(curl -s https://agria.pl$u | grep -c '<h1')"; done
```
Render potwierdzasz przez Chrome MCP `get_page_text` — nagłówek musi być widoczny w tekście strony.

## 8. Dowód do rejestru

Liczba kart z H2 cenowym (dziś 0/19 → po wdrożeniu 15/19) + zrzut struktury nagłówków z jednej
karty + hash commitu.

## 9. Rollback

Ten sam `db_export` co T-010. Usunięcie H2 bez usunięcia akapitu jest gorsze niż zostawienie obu —
jeśli cofasz, cofasz cały blok.

## 10. Rozliczenie

Zakres **R**, rozliczany łącznie z T-010 jako jedna pozycja DZIENNIKA M3.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | struktura nagłówków na 3 kartach (Chrome MCP) |
| **+14 dni** | GSC: czy karty zaczęły zbierać wyświetlenia na frazach cenowych (`scripts/gsc_pull.py`) |
| **+30 dni** | pozycje na frazach cenowych vs baseline sprzed wdrożenia |
