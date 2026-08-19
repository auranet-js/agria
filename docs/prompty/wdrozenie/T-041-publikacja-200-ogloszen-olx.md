# T-041 — publikacja 200 ogłoszeń OLX

| | |
|---|---|
| **Linia / zakres** | OLX · **P** (nasza robota) + **K** (pakiet po stronie AGRII) |
| **Status** | 🟡 czeka na AGRIĘ od 18.08 — pakiet **Premium 200, 1 199,99 zł brutto** |
| **Szacunek** | 3–4 h publikacji + nadzór |

---

## 1. Czego to dotyka

Konto ogłoszeniowe AGRII na OLX (login `pawelxpb@gmail.com`), aplikacja Partner API „Agria.pl"
(client_id 203091). Ładunek 200 ogłoszeń, siatka 53 miejscowości, rejestr `data/olx/posted.json`.
Pośrednio: telefony Pawła i Kazimierza (kontakt w ogłoszeniach), ceny (muszą się zgadzać ze stroną),
widoczność wobec konkurencji, która siedzi na tym samym OLX-ie.

## 2. Strefy kruche

1. **Bez pakietu Premium publikacja się nie uda** — konto ma limit darmowych ogłoszeń.
   Wystawione dziś ogłoszenie ma status **`limited`** (sprawdzone 19.08 przez API), co jest
   dokładnie tym objawem. Nie próbuj „przepchnąć" części — kończy się śmieciem na koncie klienta.
2. **`post_adverts.py` nie wystawia dwa razy tego samego `external_id`** — to zabezpieczenie,
   nie przypadek. Nie obchodź go ręcznymi wywołaniami API.
3. **`auto_extend` zgasił konto 18.07**, będąc włączonym na 1 z 20 ogłoszeń. Przy 200 ogłoszeniach
   ta sama pomyłka jest 200× droższa. Decyzja o `--auto-extend` osobna, świadoma, po publikacji.
4. **Token wygasa po ~24 h** — przy publikacji 200 pozycji sesja może przekroczyć ważność.
   `olx-agria refresh` przed startem i przygotowanie na odświeżenie w trakcie.
5. **Publikuj etapami.** `--pilot 1` → sprawdzenie → `--pilot 10` → sprawdzenie → `--all`.
   Nigdy 200 jednym strzałem: jeśli w szablonie jest błąd, wychodzi 200 razy na koncie klienta.
6. **Treści muszą być po `T-042`** (poprawki Kazimierza). Publikacja treści sprzed poprawek
   oznacza 200 ogłoszeń do ręcznej korekty.
7. **Ceny w ogłoszeniach ↔ ceny na stronie (T-010)** — trzy kanały (strona, Ads, OLX) muszą mówić
   to samo. Rozjazd zauważy stały odbiorca, nie Google.

## 3. Stan zmierzony 19.08.2026

```
adverts-payload.json   200 pozycji        plan-ogloszen.json  200
product-specs.json      19                posted.json           1
siatka-miast.json       12                cities-all.json   53 247
API: 1 ogłoszenie żywe, status „limited", valid_to 2026-09-06
Token: odświeżony, ważny do 2026-08-20 15:04
```

## 4. Warunki wejścia

- [ ] **AGRIA kupiła pakiet Premium 200** (zakres K, 1 199,99 zł brutto) — potwierdzenie od Pawła.
- [ ] `T-042` zamknięty: treści po poprawkach Kazimierza.
- [ ] `olx-agria refresh` wykonany.
- [ ] Kopia `data/olx/posted.json` przed startem.

## 5. Co robisz

1. `~/bin/olx-agria refresh`; `python3 scripts/olx/post_adverts.py --status`.
2. `--dry-run` na całości: 200 pozycji, zero błędów walidacji.
3. `--pilot 1` → obejrzyj wystawione ogłoszenie na OLX (URL z API), pokaż Jankowi.
4. Po „ok": `--pilot 10` → ponowna kontrola, tym razem rozrzutu miejscowości i zdjęć.
5. Po „ok": `--all`. W trakcie monitoruj błędy; przy `invalid_token` — `refresh` i wznowienie
   (rejestr `posted.json` chroni przed duplikatami).
6. Dopiero po publikacji: decyzja o `--auto-extend`, osobno.

## 6. Jak sprawdzasz w trakcie

Po każdym etapie: `olx-agria api /partner/adverts` — liczba ogłoszeń i ich statusy.
Status inny niż aktywny na więcej niż kilku pozycjach = zatrzymaj się i diagnozuj.

## 7. Jak testujesz

```bash
~/bin/olx-agria api /partner/adverts | python3 -c "
import json,sys; d=json.load(sys.stdin)['data']
from collections import Counter; print(len(d), Counter(x['status'] for x in d))"
python3 scripts/olx/post_adverts.py --status     # rejestr lokalny = stan na koncie
```
Test merytoryczny: 5 losowych ogłoszeń otwartych w przeglądarce — zdjęcia, cena, telefon, miejscowość.

## 8. Dowód do rejestru

Liczba wystawionych ogłoszeń z API + rozkład statusów, 5 URL-i przykładowych, data zakupu pakietu
przez AGRIĘ, decyzja o `auto_extend`.

## 9. Rollback

Usunięcie ogłoszeń przez API (`DELETE /partner/adverts/{id}`) na podstawie `posted.json`.
Kosztuje pakiet — dlatego etapy pilotowe są obowiązkowe, a nie ostrożnościowe.

## 10. Rozliczenie

Nasza robota: **P** (OLX setup 1 800 + 300/mies.). Pakiet Premium: **K**, koszt AGRII —
w DZIENNIKU odnotuj datę zakupu, nie kwotę jako nasz przychód.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+24 h** | statusy wszystkich ogłoszeń — ile aktywnych, ile odrzuconych |
| **+7 dni** | wyświetlenia i kontakty z OLX (statystyki konta), pierwsze telefony do Pawła/Kazimierza |
| **+30 dni** | wygasanie ogłoszeń i decyzja o przedłużeniu; czy `auto_extend` nie zgasił konta |
| **przy każdej zmianie cen** | zgodność OLX ↔ strona ↔ Ads |
