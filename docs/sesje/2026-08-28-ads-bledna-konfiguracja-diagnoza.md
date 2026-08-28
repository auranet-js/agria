# Ads — „Błędna konfiguracja" przy konwersjach: diagnoza

**28.08.2026.** Odpowiedź na zgłoszenie Janka z przypomnienia
`docs/przypomnienia/2026-08-28-gads-cele-bledna-konfiguracja.md`.
Wyłącznie odczyty — nic nie zapisano do konta klienta.

---

## Werdykt

**Ostrzeżenie nie oznacza błędu wdrożenia. Oznacza brak danych.**

Google podaje to wprost w szczegółach akcji `phone_click` (panel Ads, zakładka stanu):

> **Stan działania powodującego konwersję: Błędna konfiguracja**
> „W ciągu ostatnich 7 dni nie zarejestrowano żadnych konwersji. Podejmij działania,
> aby przywrócić pomiar konwersji."
>
> *Conversion issue* → **Conversion has never received data**
> „Your conversion has never received a tag ping or attribution data."

Dowód rozstrzygający — korelacja 5 na 5. Etykietę „Aktywne" ma **dokładnie ta jedna
akcja, która dostała dane**; wszystkie z zerem mają „Błędną konfigurację":

| Akcja | Stan śledzenia | Wszystkie konw. |
|---|---|---|
| `agria.pl (web) form_submit` | **Aktywne** | **2,00** |
| `agria.pl (web) generate_lead` | Błędna konfiguracja | 0,00 |
| `agria.pl (web) phone_click` | Błędna konfiguracja | 0,00 |
| `Połączenia z reklam (30s+)` | Błędna konfiguracja | 0,00 |
| `agria.pl (web) file_download` | Błędna konfiguracja | 0,00 |

Wdrożenie jest sprawne — potwierdzone trzema niezależnymi pomiarami:

1. **GTM** — 10 tagów, triggery poprawne: `Click - Telefon` = linkClick / Click URL
   startsWith `tel:`; analogicznie `mailto:` i `wa.me`; `Form Submit` = formSubmission.
2. **Strona** — linki `tel:` obecne na stronie głównej, `/kontakt/` i kartach produktów
   (sprawdzone User-Agentem mobilnym).
3. **Ścieżka GA4 → Ads przepuszcza 1:1** — GA4 zanotował **2** `form_submit` z `google / cpc`,
   Ads zaimportował **dokładnie 2**.

---

## Korekta założenia z T-087

W T-087 zapisano: *„zero konwersji jest arytmetycznie zgodne z utratą atrybucji przy
odmowie zgody"*. **Pomiar tego nie potwierdza.** Dla `form_submit` atrybucja przechodzi
bez ubytku (2 w GA4 z Ads → 2 w Ads). Zero konwersji głównych bierze się stąd, że
**zdarzenia oznaczone jako główne realnie nie występują w ruchu z Ads** — nie stąd,
że giną po drodze.

### Zdarzenia GA4 wg źródła, 30.07–28.08

| Zdarzenie | (direct) | **google / cpc** | inne |
|---|---|---|---|
| `form_submit` | 7 | **2** | — |
| `form_start` | 5 | 2 | 1 (chatgpt.com) |
| `email_click` | — | **2** | — |
| `whatsapp_click` | — | **1** | 1 (google/organic) |
| `phone_click` | 1 | **0** | — |
| `generate_lead` | — | **0** | 1 (chatgpt.com) |

---

## Realny błąd konfiguracji — inny niż zgłoszony

Mapowanie akcji na cele jest rozjechane. **Jedyna akcja, która zbiera dane, nie liczy się
jako konwersja.**

| Akcja | Cel | Rola | W celach konta |
|---|---|---|---|
| `form_submit` — **2 konwersje z Ads** | „Inna" | **dodatkowa** | **Nie** |
| `generate_lead` — 0 z Ads, 1 zdarzenie/mies. | „Przesłanie formularza kontaktowego" | główna | Tak |
| `phone_click` — 0 z Ads, 1 zdarzenie/mies. | „Połączenie telefoniczne" | główna | Tak |

Skutek: kampanie raportują **0 konwersji** przy 234 kliknięciach i 458 zł wydanych
(13–28.08), mimo **dwóch realnych zgłoszeń formularzowych z Ads**. Licytacja nie dostaje
żadnego sygnału. Cel „Inna" ma **0 głównych działań** — Google sam podpowiada w panelu:
*„podziel działania powodujące konwersję z kategorii Inne na bardziej szczegółowe cele"*.

**Założenie „formularz jest już pokryty przez `generate_lead`" nie działa w praktyce.**
`generate_lead` odpala trigger `Form Success - Elementor` typu **elementVisibility** —
przez 30 dni strzelił **raz**, i to z chatgpt.com. `form_submit` (formSubmission) w tym
samym czasie: **9 razy**. Obawa o podwójne liczenie była słuszna teoretycznie, ale
mierzący tag nie mierzy, a mierzący jest pomocniczy — **formularz nie jest dziś liczony
jako konwersja w ogóle**.

---

## Czemu `phone_click` nie strzela z Ads

**88,4% kliknięć to mobile** (268 z 303, 13–28.08). Mimo to zero kliknięć `tel:`
z ruchu płatnego. Użytkownik mobilny dzwoni raczej **prosto z reklamy** niż przechodzi
na stronę i klika numer.

Wniosek dla celu biznesowego („telefony jako twarda liczba pod rozmowę o budżecie"):
**nośnikiem jest `AD_CALL`, nie `phone_click`.** Rozszerzenia połączeń spięto z kampaniami
28.08 (T-102) — 6 powiązań, oba numery × 3 kampanie. Dane zaczną spływać od tej daty
i „Błędna konfiguracja" przy tej akcji zniknie sama.

---

## Co odpada z hipotez

- **Enhanced conversions** (hipoteza 5) — `enhanced_conversions_for_leads_enabled`
  i `accepted_customer_data_terms` **nieustawione**. Nie są źródłem ostrzeżenia.
  (Punkt (2) z T-087 nadal otwarty — warunki do zaakceptowania w panelu, API tego nie zrobi.)
- **Cele konta i kampanii** (hipoteza 4) — spójne. Wszystkie 3 kampanie mają te same
  4 cele biddable: `DEFAULT~WEBSITE`, `PHONE_CALL_LEAD~WEBSITE`, `PHONE_CALL_LEAD~CALL_FROM_ADS`,
  `SUBMIT_LEAD_FORM~WEBSITE`.
- **Ustawienia akcji** (hipoteza 3) — poprawne. Okna 90 dni (30 dla `AD_CALL`), atrybucja
  data-driven, liczenie „Każda" dla GA4 / „Jedna" dla `AD_CALL`.
- **Zgody** — nie badane i nie ruszane, zgodnie z prośbą Janka. Pomiar `form_submit`
  1:1 pokazuje, że ścieżka przepuszcza to, co GA4 widzi.

---

## Rekomendacje — do decyzji Janka

Każda to zapis do konta klienta, więc czekają na zgodę per operacja.

1. **`form_submit` → kategoria `SUBMIT_LEAD_FORM`, działanie główne**
   (`include_in_conversions_metric` → true). Odblokowuje kolumnę „Konwersje" i karmi
   licytację. **Wymaga świadomego cofnięcia decyzji z T-087** — uzasadnienie wyżej.
2. **`generate_lead` → dodatkowa** przy okazji punktu 1 (chroni przed podwójnym liczeniem,
   gdyby trigger Elementora kiedyś ruszył). Osobno: sprawdzić, czemu `Form Success -
   Elementor` (elementVisibility) praktycznie nie strzela.
3. **Zaimportować `email_click` i `whatsapp_click`** jako akcje konwersji — 3 kontakty
   z Ads w 30 dniach, dziś niewidoczne. To domyka punkt (3) z T-087.
4. **`purchase`, `qualify_lead`, `close_convert_lead`** — ukryć na stałe albo usunąć.
   Na tej stronie nie wystąpią (tryb katalogu, `_price` puste świadomie —
   ADR `2026-08-19-dwie-warstwy-cen.md`). Dziś wiszą jako `HIDDEN`.
5. **`AD_CALL` zostawić bez zmian** — dane od 28.08, ostrzeżenie zniknie samo.
6. **`file_download`** — zostawić jako dodatkową; zero pobrań z Ads w 30 dniach,
   ale `/do-pobrania/` jest realnym zasobem i warto go obserwować.

**Bilans po naprawie punktów 1 i 3:** zamiast dzisiejszych 0 konwersji Ads pokazałby
**5 kontaktów z ruchu płatnego** w 30 dniach (2 formularze + 2 maile + 1 WhatsApp) —
przy 458 zł wydanych daje to policzalny koszt kontaktu do rozmowy z Kasjanem o budżecie.

---

## Jak zmierzone

```bash
# Ads — ustawienia i statystyki akcji
bash scripts/google/ads_call.sh /googleAds:searchStream POST q.json
#   FROM conversion_action / FROM customer_conversion_goal / FROM campaign_conversion_goal
#   FROM campaign + segments.conversion_action_name + segments.device

# GA4 — zdarzenia wg źródła, kluczowe zdarzenia, link do Ads
python3 -c "from _lib import api; ..."   # runReport + keyEvents + googleAdsLinks

# GTM — tagi i triggery
GET /tagmanager/v2/accounts/6356149706/containers/252883347/workspaces/4/{tags,triggers}

# Panel Ads — treść ostrzeżenia (Chrome MCP, odczyt)
https://ads.google.com/aw/conversions  →  konto 674-207-1446  →  akcja phone_click
```
