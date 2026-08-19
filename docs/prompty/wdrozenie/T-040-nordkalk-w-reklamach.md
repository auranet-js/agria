# T-040 — teksty reklam z nazwą „Nordkalk"

| | |
|---|---|
| **Linia / zakres** | Ads · **P** |
| **Status** | 🟡 czeka na AGRIĘ od 19.08 |
| **Blokuje** | grupę „Producent" w `T-039` |
| **Szacunek** | 1 h po odpowiedzi |

---

## 1. Czego to dotyka

Treści reklam Google Ads (nagłówki, opisy) w kampanii Marka. Pośrednio: ryzyko prawne
z tytułu użycia cudzego znaku towarowego oraz relacja AGRIA–Nordkalk.

## 2. Strefy kruche

1. **Licytować na cudzy znak towarowy w Google Ads wolno zawsze. Użyć nazwy w treści reklamy —
   tylko odsprzedawcy.** To jest cała różnica i cała blokada.
2. **Odpowiedzi nie ma nigdzie w repo ani w memory** — sprawdzone 19.08 `grep`-em po `docs/`
   i katalogu memory. **Nie zgaduj.** To, że AGRIA sprzedaje produkty Nordkalku (Agrobielik, Bielik),
   nie przesądza o statusie autoryzowanego dystrybutora.
3. **Marki `Agrobielik` i `Bielik` to produkty Nordkalku, AGRIA jest dystrybutorem, nie producentem.**
   Nazwy produktowe w reklamach są używane dziś i to jest inna sytuacja niż nazwa firmy-producenta.
   Nie rozszerzaj blokady na nazwy produktów.
4. **Zgłoszenie od Nordkalku do Google kończy się wstrzymaniem reklam**, nie negocjacją.
   Koszt błędu jest natychmiastowy.
5. Odpowiedź od Pawła ma paść **telefonicznie do Janka**, nie mailem z tabelą.

## 3. Stan

Pytanie zadane 19.08, otwarte. Grupa „Producent" w T-039 czeka.

## 4. Warunki wejścia

- [ ] Paweł potwierdził status: autoryzowany dystrybutor Nordkalku — tak/nie.
- [ ] Jeśli tak: czy jest dokument (umowa, certyfikat dystrybutora), na który można się powołać
      w razie zgłoszenia do Google.

## 5. Co robisz

**Jeśli TAK:** przygotuj 3 warianty tekstów z nazwą producenta, pokaż Jankowi, wdroż jako grupę
„Producent" w kampanii Marka (razem z T-039). Zapisz w `FAKTY_KLIENTA.md`, że status jest
potwierdzony i skąd to wiemy — żeby pytanie nie wróciło za trzy miesiące.

**Jeśli NIE:** grupa „Producent" idzie bez nazwy producenta — licytujemy na frazy markowe,
w treści mówimy o produktach (Agrobielik, Bielik) i o roli dystrybutora. Wpisz rozstrzygnięcie
do `FAKTY_KLIENTA.md` i zamknij wiersz jako rozstrzygnięty, nie jako niewykonany.

## 6. Jak sprawdzasz

Po wdrożeniu tekstów: status reklam w Ads API — `POLICY_APPROVED` vs `DISAPPROVED`
z powodem `TRADEMARK_IN_AD_TEXT`.

## 7. Jak testujesz

```bash
bash scripts/google/ads_call.sh /googleAds:searchStream POST tmp/q-ads-status.json
# ad_group_ad.policy_summary.approval_status dla nowych reklam
```

## 8. Dowód do rejestru

Odpowiedź Pawła (data, forma), status zatwierdzenia reklam z API, wpis w `FAKTY_KLIENTA.md`.

## 9. Rollback

Wstrzymanie reklam z nazwą producenta (`status: PAUSED`) — natychmiastowe, bez czekania.

## 10. Rozliczenie

Zakres **P**, ~1 h. Rozstrzygnięcie „nie" też jest domknięciem.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+48 h po wdrożeniu** | status zatwierdzenia reklam |
| **+30 dni** | czy nie wpłynęło zgłoszenie znaku towarowego (widoczne jako `DISAPPROVED` w koncie) |
