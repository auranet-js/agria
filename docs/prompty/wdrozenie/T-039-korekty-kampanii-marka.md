# T-039 — korekty kampanii „AGRIA – Marka": stawka, wykluczenia, grupa „Producent"

| | |
|---|---|
| **Linia / zakres** | Ads · **P** (poza ryczałtem) |
| **Status** | 🔴 teraz — rekomendacja czeka na „działaj" |
| **Konto** | 674-207-1446 (CID `6742071446`), direct, nie pod MCC |
| **Szacunek** | 1–1,5 h |

---

## 1. Czego to dotyka

Kampania **AGRIA – Marka** w Google Ads: budżet dzienny, stawka MANUAL_CPC grupy Brand,
wykluczenia słów kluczowych, nowa grupa reklam „Producent". Pośrednio: kampania **Rolnictwo**
(dzielą pulę intencji — wykluczenia w jednej przesuwają ruch do drugiej) i budżet miesięczny
1 200 zł, z którego na 19.08 wydano 199,62 zł.

## 2. Strefy kruche

1. **To są pieniądze klienta, wydawane w czasie rzeczywistym.** Zmiana stawki z 0,50 na 3,00 zł
   to sześciokrotność. Przy budżecie dziennym 6 zł kampania może wyczerpać dzień na dwóch klikach.
   **Sprawdź budżet dzienny razem ze stawką**, nie osobno.
2. **Nazwa „Nordkalk" w treści reklam jest zablokowana** — to `T-040`, czeka na potwierdzenie
   statusu dystrybutora. Grupa „Producent" **nie może** zawierać nazwy producenta w tekstach,
   dopóki tamto nie wróci. Licytowanie na frazę marki jest dozwolone zawsze — używanie jej
   w treści tylko odsprzedawcy.
3. **Wykluczenia opakowaniowe** („worek", „25 kg", „paleta", „sklep") mają odsiać detalistę.
   Pozycjonowanie jest twarde: **dostawca całosamochodowy, nie sklep z workami**.
   Za szerokie wykluczenie utnie też zapytania big-bagowe, które są realną sprzedażą.
4. **Konwersje z połączeń** działają na rotacji dwóch numerów (Paweł, Kazimierz). Nie rusz
   konfiguracji numerów przy okazji zmiany stawek — to osobna warstwa.
5. **GA4 nie mierzy kompletnie** (patrz `T-033`): sierpień 1–19 to 49 sesji Paid Search wobec
   100 kliknięć w Ads. **Nie oceniaj skutku zmiany po GA4** — bierz dane z Ads API.
6. **API v25, składnia z pułapkami**: brak `start_date` w niektórych mutacjach, zasób ≠ powiązanie.
   Wersję czytaj z `~/secrets/google/ads-config.json`, nie hardkoduj.
7. **Punkt decyzyjny to 7–10 dni**, nie 2. Zmiana stawki oceniana po dwóch dniach to szum.

## 3. Stan zmierzony 19.08.2026 (Ads API, ostatnie 14 dni)

```
AGRIA - Rolnictwo   ENABLED   budżet 34,00 zł/dz   koszt 199,62 zł   100 klików   682 wyśw.   0 konw.
AGRIA - Marka       ENABLED   budżet  6,00 zł/dz   koszt   0,00 zł     0 klików     0 wyśw.   0 konw.
```

**Marka nie wydała ani grosza przez sześć dni emisji i nie zanotowała ani jednego wyświetlenia.**
Przy stawce 0,50 zł nie wchodzimy do aukcji w ogóle — to nie jest „słaby wynik", to brak udziału.

## 4. Warunki wejścia

- [ ] Janek powiedział „działaj" — to zmiana wydatku, nie optymalizacja techniczna.
- [ ] Zrzut stanu kampanii przed zmianą do `tmp/ads-przed-T-039-<data>.json`.
- [ ] Rozstrzygnięte, czy grupa „Producent" startuje bez nazwy Nordkalk (T-040 otwarte).

## 5. Co robisz

1. Zrzut stanu:
   ```bash
   bash scripts/google/ads_call.sh /googleAds:searchStream POST tmp/q-stan.json > tmp/ads-przed-T-039-$(date +%F).json
   ```
   (zapytanie o `campaign`, `ad_group`, `ad_group_criterion`, `campaign_budget`, metryki 14 dni)
2. Pokaż Jankowi tabelę: co jest teraz, co proponujesz, ile to kosztuje dziennie w najgorszym razie.
3. Podnieś stawkę Brand 0,50 → 3,00 zł (`/adGroupCriteria:mutate` albo `/adGroups:mutate`
   zależnie od poziomu, sprawdź gdzie dziś siedzi `cpc_bid_micros`).
4. Zweryfikuj budżet dzienny kampanii Marka — przy CPC 3 zł budżet 6 zł to dwa kliknięcia.
   Jeśli podnosisz, powiedz o tym wprost i wskaż, skąd bierzesz pieniądze w ramach 1 200 zł.
5. Dodaj wykluczenia opakowaniowe jako `NEGATIVE` na poziomie kampanii — **lista pokazana Jankowi
   przed dodaniem**, z komentarzem przy każdym, co odsiewa.
6. Utwórz grupę „Producent" z frazami markowymi, **bez nazwy producenta w treściach reklam**.
7. Readback: te same zapytania co w kroku 1, porównanie przed/po.

## 6. Jak sprawdzasz w trakcie

Po każdej mutacji odczyt zasobu, którego dotyczyła — API v25 potrafi zwrócić sukces i nie zmienić
tego, co myślisz, że zmieniłeś (zasób ≠ powiązanie).

## 7. Jak testujesz

```bash
# +48 h: czy kampania w ogóle weszła do aukcji
bash scripts/google/ads_call.sh /googleAds:searchStream POST tmp/q-14d.json | \
  python3 -c "…"   # oczekiwane: wyświetlenia Marka > 0
```
Sukces krótkoterminowy = **wyświetlenia przestały być zerem**. Sukces właściwy oceniasz po 7–10 dniach:
CTR, śr. CPC, koszt/konwersja, i czy wykluczenia nie zdusiły wolumenu Rolnictwa.

## 8. Dowód do rejestru

Tabela przed/po z Ads API (budżet, stawka, wyświetlenia, klik, koszt), lista dodanych wykluczeń,
ID nowej grupy reklam. Po 7 dniach — druga tabela z wynikiem.

## 9. Rollback

Zrzut z kroku 1 zawiera stare wartości; przywrócenie to ta sama mutacja z odwrotnymi liczbami.
Wykluczenia usuwa się `remove` na `adGroupCriterion`/`campaignCriterion`.

## 10. Rozliczenie

Zakres **P** — Ads jest poza ryczałtem. Godziny do DZIENNIKA M3 z adnotacją „Ads",
media 1 200 zł/mies. rozliczane osobno; na 19.08 wydane 199,62 zł.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+48 h** | wyświetlenia i koszt kampanii Marka — czy weszła do aukcji |
| **+7 dni** | punkt decyzyjny stawek: CTR, śr. CPC, pozycja; czy Rolnictwo nie straciło wolumenu |
| **+10 dni** | decyzja: zostawiamy, podnosimy, czy gasimy Markę i przenosimy budżet |
| **31.08** | rozliczenie miesięczne budżetu Ads — pozycja w raporcie M3 |
