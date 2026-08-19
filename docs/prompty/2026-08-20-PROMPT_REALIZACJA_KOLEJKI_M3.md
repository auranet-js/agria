# Prompt startowy — realizacja kolejki M3

> Wątek wykonawczy. Cel: zamknąć jak najwięcej z trzynastu pozycji „teraz" **do 31.08**.
> Utworzony 19.08.2026 po przebudowie rejestru (commity `a909f11`, `fcd8a16`).

## Lista wejściowa — czytasz w tej kolejności, zanim cokolwiek zrobisz

1. **`CLAUDE.md`** — środowisko, cztery kanały dostępu, **§4 Strefy kruche**, §5 czego nie wolno.
2. **`docs/REJESTR_ZOBOWIAZAN.md`** — kolejka i dziennik. To jest lista, którą realizujesz.
3. **`docs/FAKTY_KLIENTA.md`** — otwierasz, gdy zadanie dotyka oferty, cen, ludzi albo ustaleń.

Nie ma trzeciego pliku ze stanem i nie ma master promptu — rozebrane 19.08. Reguły komunikacji
ładują się z memory (`feedback_agria_*`), nie czytasz ich z dokumentu.

## Zasada domykania — obowiązuje przy każdej pozycji

**Commit zamykający pozycję zmienia jej wiersz w rejestrze w tym samym commicie** i wpisuje dowód
(hash, URL po zmianie, wynik `curl`/MCP). **Wiersz bez dowodu nie ma prawa mieć ✅.** Zamknięta
pozycja przenosi się z `KOLEJKA` do `DZIENNIK M3` razem z godzinami.

Bez dowodu piszesz „niezweryfikowane" — nie „zrobione".

## Kolejność wykonania i dlaczego taka

```
T-048 (retest PSI) ──→ T-031 (LCP) ...........  wrzesień, tylko jeśli PSI ruszy
T-008 ──┬──→ T-009 ──→ T-027 (reindeksacja)     jedna strona, jedna wizyta, potem zgłoszenie
        └── ID 731, _elementor_data
T-010 ──→ T-011                                  PRIORYTET 1, jedna robota na tych samych kartach
T-028, T-029, T-026, T-032, T-039, T-042, T-046  niezależne, można w dowolnej kolejności
```

### 1. T-010 + T-011 — ceny na stronie. **Priorytet 1.**

Zlecenie kompletne i zaakceptowane, wisi od 07.08. Wszystko gotowe: ceny w
`docs/operations/CENNIK_PAWEL_2026-08-07.md`, rozpiska per URL w `CEN_LISTA_URL_2026-08-13.md`,
mockup zaakceptowany przez Janka 13.08, prompt wykonawczy w
`docs/prompty/2026-08-19-PROMPT_SEO_CENY_NA_STRONACH.md`.

**Twarde ograniczenia — złamanie któregokolwiek psuje robotę:**
- cena idzie **wyłącznie w treść** — `<h2>` z frazą cenową + akapit z widełkami i warunkiem dostawy;
- **`_price` zostaje puste**, wariantów ani atrybutów cenowych **nie tworzysz** (ADR dwie warstwy cen);
- schema `Product`/`offers` budujesz **ręcznie z treści**, nie z bazy;
- **wyłącznie przeliczenia na tonę** — ceny za worek nie idą na stronę (decyzja Janka 19.08);
- cena nigdy sama — zawsze z warunkiem dostawy, dwa punkty odniesienia na grupę;
- **zero żargonu**: „loco", MOQ, franco, EXW, HDS — zakazane. „Cena za towar, bez transportu";
- bez progu ilościowego („minimum 24 t") — zamiast tego „przy 24 t cena wynosi od X";
- klauzula „ceny orientacyjne, netto, nie stanowią oferty w rozumieniu KC" zostaje;
- pole edytowalne, żeby Paweł zmieniał je w minuty.

**Dowód domknięcia:** MCP `query_db` pokazuje słowo „cena" w treści 15 kart (dziś 0/19), render
przez Chrome MCP potwierdza H2 i akapit, `_price` nadal puste w 19/19.

### 2. T-008 + T-009 + T-027 — `/do-pobrania/`, jedna wizyta

Strona ID 731, treść w `_elementor_data` (nie `post_content` — patrz `CLAUDE.md` §4 pkt 2).
T-008: dołożyć 8 atestów i karty Nordkalku (materiały w mailu [201]). T-009: usunąć całą sekcję
„Certyfikaty" razem z duplikatem linku i literówkami „ertyfikat". Dopiero po obu — T-027:
zgłoszenie do reindeksacji przez `~/bin/index-submit` (**nigdy surowym curlem**, wspólna pula 200/dobę).

Google trzyma na tej stronie werdykt `BLOCKED_BY_META_TAG` z **12 kwietnia**, choć live ma
`index, follow` — po prostu nie wrócił.

**Dowód:** `curl` pokazuje 0 wystąpień „certyfikat" i obecność „Sitkówka"; `index-submit --status`
z wpisem; GSC URL Inspection po kilku dniach.

### 3. T-048 — retest PSI (pierwsza rzecz rano)

Kod na produkcji ma już `Chrome-Lighthouse`, `Google-PageSpeed`, `GoogleOther` w `$good_bots`.
19.08 PSI odbił się o `Quota exceeded … Queries per day` na projekcie GCP `583797351490`.
Powtórz pomiar, wpisz wynik do wiersza. Jeśli przechodzi — `T-031` (LCP mobile) staje się mierzalny;
ostatni znany pomiar to LCP 7,4 s z 03.08.

### 4. Reszta — niezależne, bierz wg tego, na co jest czas

| ID | Co | Uwaga wykonawcza |
|---|---|---|
| **T-029** | login admina `js` w schema na froncie | bezpieczeństwo, otwarte 65 dni, `"@type":"Person"` ×2 |
| **T-028** | 15 starych `post_type=produkt` (ID 60–74) obok 19 produktów WC | Agrobielik 70 pod dwoma adresami, oba zbierają wyświetlenia w GSC — rozstrzygnąć 301 czy trash |
| **T-026** | 6 URL-i poza indeksem | 4× „Google nieznany", 2× „wykryta, niezindeksowana", mimo 3× Indexing API — **nie strzelaj czwarty raz**, znajdź przyczynę |
| **T-032** | 301 dla `/kategoria-produktu/*` | odblokowane od 18.08 (SSH + `.htaccess`), diff przed wgraniem |
| **T-039** | kampania Marka: stawka 0,50 → 3,00 zł, wykluczenia, grupa „Producent" | **0 zł wydane przez 6 dni** — przy 0,50 nie wchodzimy do aukcji |
| **T-042** | poprawki treści ogłoszeń OLX od Kazimierza (mail 18.08) | przed publikacją, która i tak czeka na pakiet AGRII |
| **T-046** | optymalizacja GBP Tarnów | **obiecane klientowi na piśmie** w raporcie M2 jako zadanie sierpnia. Oddziałów NIE ruszamy — brak dostępu |

## Czego w tym wątku NIE robisz

- **Nie proponujesz landingów organicznych ani hubów segmentowych** — `T-035`…`T-038`, unieważnione
  ADR-em 2026-08-11 na zmierzonej kanibalizacji („wapno bielik": 6 URL-i → pozycja 15,3).
- Nie ustawiasz `_price` ani wariantów WooCommerce (patrz wyżej).
- Nie piszesz do produkcji bez zgody w czacie i bez `backup_file` / `db_export` przy większej zmianie.
- Nie wysyłasz niczego do klienta — wszystko przez Janka na `js@auranet.com.pl`.
- Nie pytasz Pawła o rzeczy z naszej kompetencji. Lista tego, o co **wolno** zapytać, jest w rejestrze
  („Pytania do Pawła") i w `FAKTY_KLIENTA.md` §8. Forma: telefon Janka, nie mail z tabelą.

## Kontekst terminowy

**31.08 kończy M3.** Raport miesięczny dla AGRII — wzorzec `docs/raporty/DOWODY_M2_2026-07.md`,
materiał zbierasz z sekcji `DZIENNIK` rejestru, nie od zera. Tego samego dnia rozliczenie pierwszego
miesiąca budżetu Ads (na 19.08 wydane 199,62 zł z 1 200 zł).
