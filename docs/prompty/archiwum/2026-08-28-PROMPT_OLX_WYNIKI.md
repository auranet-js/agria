# Prompt wątku: OLX — co kanał realnie dał w pierwszym miesiącu i czy odnawiamy pakiet

> **Data zlecenia:** 2026-08-28, Janek. **Powód:** kanał chodzi od 20.08, kosztuje 1 200 zł/mies
> po stronie klienta plus 300 zł prowadzenia, a decyzja o odnowieniu pakietu musi zapaść
> **przed 16.09** — czyli zanim skończy się pierwszy pełny cykl emisji. Do tej pory zbieraliśmy
> pomiary, nie wyciągaliśmy z nich wniosków.
>
> **Zadanie: policzyć wynik kanału, rozbić go na to, co pracuje i co nie, i wyjść z rekomendacją
> dla Pawła — odnawiamy, w jakiej skali, na jakiej podstawie.**

---

## 0. Zasada nadrzędna — liczby poniżej mówią, gdzie patrzeć, nie zwalniają z patrzenia

Każda liczba w tym prompcie jest z pomiaru z konkretną datą. Do raportu wchodzi **twój** odczyt,
zrobiony w tym wątku, nie przepisany stąd. Czego nie zmierzyłeś — piszesz „niezmierzone".

Ceny ofertownika nie wychodzą nigdzie: ani do raportu, ani do ogłoszeń, ani do maila.

---

## 1. Stan faktyczny na 28.08 — punkt startu

**Kanał żyje.** 200 ogłoszeń wystawionych 20.08 przez Partner API, wszystkie `active`,
`auto_extend` na 200/200, pakiet Premium 200 wyczerpany co do miejsca. 11 produktów, 53 miasta,
9 województw, ceny 36–790 zł/t. 200 ogłoszeń to **17 unikalnych kombinacji tytuł+opis** —
resztę robi geo-multiplikacja, dozwolona regulaminem w kategoriach płatnych.

**Pomiary, które już są** (`data/olx/statystyki.json`, kumulatywne od wystawienia):

| Kiedy | Ogłoszeń | Odsłony | Odsłony numeru | Obserwujący |
|---|---|---|---|---|
| 21.08 10:34 | 112 | 69 | 1 | 6 |
| 21.08 10:38 | 200 | 120 | 1 | 10 |
| 24.08 07:35 | 200 | 307 | 3 | 15 |
| 25.08 09:53 | 200 | 366 | **10** | 15 |

**Automatyzacja, która chodzi sama** (crontab, nie ruszać bez `~/bin/cron-install`):
- `monitor.py` — **codziennie 7:25**, kontrola statusów, `auto_extend` i zapasu pakietu →
  `data/olx/monitor-log.json`. Wpis z 28.08: 200 w rejestrze, 0 poza `active`, 0 bez `auto_extend`,
  **19 dni pakietu**.
- `statystyki.py --zapisz --telegram` — **poniedziałki 7:35**. Czyli **31.08 rano wpadnie świeży
  pomiar** — zacznij od sprawdzenia, czy się zapisał, i licz na nim, nie na tabeli powyżej.

**Koszt kanału:** pakiet Premium 200 = 1 199,99 zł brutto/mies po stronie AGRII (Megapakiet 200 to
2 199,99 za to samo — różnica tysiąca złotych siedzi w jednym kliknięciu w panelu), plus Auranet
1 800 setup jednorazowo + 300 zł netto/mies prowadzenia.

**Prognoza, którą sprzedaliśmy klientowi:** ostrożnie ~50, realnie ~150, optymistycznie ~230 odsłon
numeru miesięcznie. **To jest liczba do rozliczenia w tym wątku.** Punkt odniesienia: całe konto
OLX AGRII dało 209 telefonów przez cały swój cykl życia, a organik agria.pl 221 kliknięć w lipcu.

---

## 2. Termin, który jest ważniejszy niż cała reszta

**Pakiet wygasa 16.09, emisja ogłoszeń kończy się 19.09.** `auto_extend` przedłuża ogłoszenie
**tylko dopóki żyje pakiet** — jeśli AGRIA nie odnowi przed 16.09, **wszystkie 200 ogłoszeń zgasną
jednego dnia**. Precedens jest zmierzony: 18.07 ogłoszenie 858802418 odnowiło się o 08:43:52,
pakiet wygasł o 08:55, pozostałe 17 zgasło.

⚠️ **Tego terminu NIE MA w sekcji „Terminy najbliższe" rejestru** — sprawdzone 28.08. Siedzi
wyłącznie w memory i w akapicie podsumowania M3. Pierwsza rzecz do naprawienia: wiersz w rejestrze
z datą **10.09** (zapas na decyzję i przelew), nie 16.09.

To jest pytanie do Pawła **z wyprzedzeniem**, i musi do niego pójść z liczbą, nie z prośbą.

---

## 3. Co policzyć — siedem pytań, na które ma odpowiedzieć raport

1. **Ile kanał dał w pierwszym miesiącu.** Odsłony, odsłony numeru, obserwujący — przyrosty
   tygodniowe, nie wartości kumulatywne. Krzywa ma pokazać, czy ruch narasta, czy wysyca.
2. **Rozkład, nie średnia.** Które produkty, miasta i warianty tytułu zbierają odsłony i telefony,
   a które stoją na zerze. Przy 200 ogłoszeniach średnia niczego nie mówi — 25.08 dziesięć odsłon
   numeru na 200 ogłoszeń znaczy, że pracuje kilka sztuk, i trzeba wiedzieć które.
3. **Czy prognoza 50/150/230 się broni.** Pełny cykl emisji to 20.08–19.09; policz stan na dzień
   analizy i ekstrapoluj uczciwie, z zaznaczeniem, ile dni faktycznie zmierzono.
4. **Ile kosztuje jeden kontakt.** 1 199,99 + 300 podzielone przez odsłony numeru. Zestaw z Ads:
   13–23.08 to **215 kliknięć, 396,18 zł, zero konwersji**, a od 28.08 działa `AD_CALL` — pierwszy
   pomiar telefonów niezależny od warstwy zgód. Dwa kanały, ten sam okres, ta sama jednostka.
5. **Czy treść albo siatka wymaga korekty przed drugim cyklem.** Jeśli któryś produkt ma zerowy
   zwrot w 6 miastach, jego sloty są warte więcej pod innym produktem. Rewizja sezonowa jest
   **poza wyceną** — listopad, wapno palone i paszarstwo; nie wciągaj jej tutaj.
6. **Co robi konkurencja.** `scripts/olx/market_snapshot.py`, baseline 07.08: 2 486 ogłoszeń,
   544 sprzedawców w kat. 4368 + 765. Diff wobec baseline'u powie, czy rynek się zagęścił
   i czy liderzy zmienili strategię.
7. **Rekomendacja odnowienia.** Odnawiamy 200, schodzimy niżej, czy wchodzimy wyżej — z liczbą
   obok. Pamiętaj, że suwak pakietu ma progi 5/10/20/50/100/200 i **nic wyżej**; 400 to dwa zakupy
   o nieznanej sumowalności (niesprawdzone).

---

## 4. Pułapki pomiarowe — ktoś już na nie wszedł

**Statystyki są kumulatywne od wystawienia.** Przyrost liczysz z różnicy między pomiarami.
Nie nadpisuj historii w `statystyki.json` — każdy pomiar dopisujesz z datą.

**API gubi zapytania przy równoległości.** Przy 8 wątkach ginęło co trzecie — `statystyki.py` ma
z tego powodu trzy powtórki na ogłoszenie. Jeśli liczba ogłoszeń w odczycie jest mniejsza niż 200,
to najpewniej gubione zapytania, nie zgaszone ogłoszenia; potwierdź w `monitor-log.json`.

**Lista zbiorcza `GET /partner/adverts` oddaje statusy z opóźnieniem.** Wiarygodny jest odczyt
`GET /partner/adverts/{id}` per ogłoszenie. Statusy `new` i `disabled` tuż po zmianie są
**przejściowe** (moderacja przepuszcza w 2 min 14 s – 2 min 58 s); werdykt negatywny to `moderated`
albo `blocked`.

**W API nie ma endpointów płatności.** Stan pakietu czytasz z `GET /partner/users/me/packets`
(ten działa — wcześniejszy zapis „pakietów nie ma w API" był błędny), reszta wyłącznie z panelu.

**Nie wnioskuj z `last_refresh_time` konkurencji** — 94% poniżej 3 dni przy 544 sprzedawcach to nie
mogą być płatne bumpy. Rozstrzyga diff między snapshotami.

**Do korekty cenowej nie wracamy.** Wniosek „ceny AGRII 25–40% powyżej mediany OLX" był **błędny** —
pole „cena" na OLX nie ma jednostki, tylko 36 z 1 204 ogłoszeń podaje cenę tonową, a stara mediana
powstała m.in. z sześciu kopii jednego ogłoszenia. Po odfiltrowaniu do ofert porównywalnych AGRIA
jest w rynku wszędzie. Tania konkurencja to w dużej części **wapno nieatestowane** — nie ten sam
produkt, nie konkurujemy z tym ceną.

**Warianty ZASTOSOWANIA tego samego towaru (staw / gleba) celowo dzielą 22 miasta.** To nie jest
duplikat i nie „naprawiać" tego — decyzja Janka 17.08, po tym jak zostało to raz nadgorliwie wycięte.

---

## 5. Czego nie robić

- **Nie pisać do klienta.** Wszystko idzie do Janka na `js@auranet.com.pl` przez `~/bin/send-to-jan`.
- **Nie zmieniać ogłoszeń na produkcji** w tym wątku. To jest wątek analityczny; korekty treści
  albo siatki wychodzą z niego jako **propozycja z liczbą**, nie jako wykonana zmiana.
  `PUT /partner/adverts/{id}` podmienia **cały** zasób, nie łata pola — jedno niedomknięte pole
  kasuje numer telefonu z ogłoszenia, czyli kanał, który daje wszystkie kontakty.
- **Nie dotykać crontaba** inaczej niż przez `~/bin/cron-install`.
- **Zero żargonu w czymkolwiek, co zobaczy klient** — bez „loco", MOQ, franco, EXW. Odbiorcą jest
  rolnik. 228 wystąpień „loco magazyn" było już raz czyszczone.
- **Nie krytykować kanału jako pomysłu.** Jeśli liczby są słabe, opisujesz liczby i mówisz, co z nimi
  zrobić — framing rozwojowy, nie rozliczeniowy.

---

## 6. Czym się kończy wątek

1. **Raport** `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md` — wynik, rozkład, koszt kontaktu,
   zestawienie z Ads i organikiem, rekomendacja odnowienia z uzasadnieniem.
2. **Wiersz w rejestrze** `docs/REJESTR_ZOBOWIAZAN.md` — nowy `T-NNN` na decyzję o pakiecie
   z terminem **10.09** plus dopisek w „Terminy najbliższe" (dziś tego terminu tam nie ma).
3. **Krótki tekst dla Pawła** — do maila przez Janka, telefonicznie do niego i tak trafi szybciej.
   Jedna liczba, jedna rekomendacja, jeden termin. Bez tabel na dwie strony.
4. Jeśli coś okaże się warte zapamiętania na stałe — dopisek do memory `project_agria_olx_kanal`,
   nie do tego promptu.

---

## 7. Skąd czytać

| Co | Gdzie |
|---|---|
| Historia pomiarów | `data/olx/statystyki.json` · `data/olx/monitor-log.json` |
| Rejestr wystawionych ogłoszeń | `data/olx/posted.json` (id, SKU, miasto, tytuł) |
| Plan i siatka | `data/olx/plan-ogloszen.json` · `data/olx/siatka-miast.json` |
| Skrypty | `scripts/olx/` — `statystyki.py`, `monitor.py`, `market_snapshot.py`, `post_adverts.py` |
| Rynek, baseline | `docs/operations/OLX_BASELINE_2026-08-07.md` · `docs/operations/OLX_KONKURENCJA_2026-08-07.md` |
| Plan kanału i treść maila do klienta | `docs/offers/2026-08-PLAN_OLX.md` |
| Przebieg wdrożenia, gotchas | `docs/sesje/2026-08-17-olx-wdrozenie.md` |
| Sekrety | `~/secrets/olx/agria-app.env` · `~/secrets/agria/olx.txt`; token: `~/domains/auratest.pl/olx-private/agria-tokens.json` |
| Memory | `project_agria_olx_kanal` · `reference_agria_olx_api` |
