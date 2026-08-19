# T-042 — poprawki treści ogłoszeń OLX ustalone z Kazimierzem

| | |
|---|---|
| **Linia / zakres** | OLX · **P** |
| **Status** | 🔴 teraz, na nas — ale **z luką dokumentacyjną, patrz §4** |
| **Zgłosił** | Kazimierz, mail 18.08.2026 |
| **Szacunek** | 2 h po odzyskaniu treści ustaleń |

---

## 1. Czego to dotyka

Ładunek ogłoszeń `data/olx/adverts-payload.json` (**200 pozycji**), plan `data/olx/plan-ogloszen.json`
(200), specyfikacje `data/olx/product-specs.json` (19), skrypty `scripts/olx/build_adverts.py`
i `post_adverts.py`. Pośrednio: jedno ogłoszenie **już wystawione** (`data/olx/posted.json`,
advert_id 1089946612, Zator, ważne do 06.09) — jeśli poprawki dotyczą też jego, idzie `--update`.

## 2. Strefy kruche

1. **To jest konto klienta.** `post_adverts.py` domyślnie nic nie wysyła — tryb trzeba podać
   świadomie. Nie uruchamiaj `--all` przy okazji poprawiania treści.
2. **Token OLX wygasa po ~24 h.** Zmierzone 19.08: `access_token: WYGASŁ (-1668 min)`,
   `olx-agria refresh` odnowił do 20.08 15:04. **Refresh jest pierwszym krokiem każdej sesji OLX**,
   inaczej dostaniesz `invalid_token: Expired token` i stracisz czas na diagnozę nie tam, gdzie trzeba.
3. **`auto_extend` już raz zgasił konto** (18.07, włączony na 1 z 20 ogłoszeń). Nie dotykaj go
   przy okazji poprawek treści.
4. **Ceny na OLX muszą być zgodne z cenami na stronie** (T-010) i nie mogą schodzić poniżej cen
   stałych odbiorców. To warunek handlowy Pawła, nie preferencja redakcyjna.
5. **Zero żargonu** także tutaj — odbiorcą OLX jest rolnik. „loco", MOQ, franco: zakaz.
6. **Nie publikujesz masowo** — publikacja 200 ogłoszeń to `T-041` i czeka na pakiet Premium
   po stronie AGRII. Ten task kończy się gotową treścią, nie wysyłką.

## 3. Stan zmierzony 19.08.2026

```
olx-agria status  → access_token WYGASŁ, refresh_token jest
olx-agria refresh → ważny do 2026-08-20 15:04:25
olx-agria api /partner/adverts → 200; 1 ogłoszenie, id 1089946612, status „limited",
   „Wapno do stawu — tlenkowe palone 70% CaO, atest, od 220 zł/t", valid_to 2026-09-06
data/olx/: adverts-payload.json 200 poz. · plan-ogloszen.json 200 · product-specs.json 19 · posted.json 1
```

## 4. Luka do zamknięcia zanim ruszysz

**Treści ustaleń Kazimierza z 18.08 nie ma ani w repo, ani w skrzynce `claude@auratest.pl`.**
Sprawdzone 19.08: `grep` po `docs/` i `data/` zwraca wyłącznie wzmianki („poprawki treści z 18.08"),
a `claude-mail-fetch.py list` kończy się na mailu [260] z 19.08, przy czym ostatnie maile OLX to
[248] i [250] z **11.08**.

**Pierwszy krok tego taska to poproszenie Janka o przesłanie maila Kazimierza na `claude@auratest.pl`.**
Bez tego nie wiadomo, co poprawiać — a zgadywanie treści ustaleń z klientem jest gorsze niż zwłoka.

## 5. Co robisz

1. Poproś Janka o forward maila [K 18.08] na `claude@auratest.pl`.
2. `python3 ~/bin/claude-mail-fetch.py fetch <id>` → treść do `/tmp/claude-mails/<id>/`,
   **od razu skopiuj do `tmp/T-042/`** (`/tmp` bywa czyszczone).
3. Spisz ustalenia jako listę zmian: co, gdzie w ładunku, dlaczego.
4. `olx-agria refresh` — token.
5. Nanieś zmiany w `data/olx/product-specs.json` i przegeneruj ładunek `build_adverts.py`.
6. `post_adverts.py --dry-run` — podgląd, zero ruchu do OLX.
7. Pokaż Jankowi 3 przykładowe ogłoszenia po zmianie (tekst, nie diff JSON-a).
8. Dla **już wystawionego** ogłoszenia: `post_adverts.py --update` (tylko ono, po zgodzie).

## 6. Jak sprawdzasz w trakcie

`--dry-run` po każdej większej zmianie w generatorze. Liczba pozycji w ładunku ma zostać 200 —
jeśli spadła, generator coś odrzucił po cichu.

## 7. Jak testujesz

```bash
~/bin/olx-agria refresh
~/bin/olx-agria api /partner/adverts | python3 -m json.tool | head -40   # treść wystawionego po --update
python3 scripts/olx/post_adverts.py --status                              # rejestr lokalny
```
Test merytoryczny: Kazimierz czyta trzy ogłoszenia i potwierdza. **Jego akcept jest warunkiem
domknięcia** — to jego ustalenia.

## 8. Dowód do rejestru

Ścieżka do maila w `tmp/T-042/`, lista naniesionych zmian, wynik `--dry-run` z liczbą pozycji,
treść wystawionego ogłoszenia po `--update` z API, potwierdzenie Kazimierza (przez Janka).

## 9. Rollback

`data/olx/` jest w gicie — `git checkout` na plikach ładunku. Wystawione ogłoszenie: ponowny
`--update` ze starą treścią (OLX nie ma historii wersji, więc trzymaj kopię starego payloadu).

## 10. Rozliczenie

Zakres **P** (OLX poza ryczałtem: setup 1 800 + 300/mies.). DZIENNIK M3, linia OLX.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+24 h** | czy ogłoszenie po `--update` renderuje się na OLX poprawnie (URL z API) |
| **przed T-041** | ponowny `--dry-run` — publikacja masowa musi iść na treści po poprawkach, nie sprzed |
| **06.09** | `valid_to` wystawionego ogłoszenia — decyzja o przedłużeniu |
| **+30 dni** | czy ceny w ogłoszeniach nadal zgodne z cenami na stronie (T-010) |
