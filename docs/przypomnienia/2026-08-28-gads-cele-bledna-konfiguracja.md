# Google Ads — „Błędna konfiguracja" przy konwersjach telefon i formularz

**Zgłoszone przez Janka 28.08.2026.** Panel Ads pokazuje ostrzeżenie **„Błędna konfiguracja"**
przy akcjach konwersji dotyczących **telefonu** i **formularza**. Do zdiagnozowania i naprawy.

> **Ten plik jest promptem startowym dla nowego wątku.** Poniżej jest wszystko, co zmierzone
> 28.08 — nie zaczynaj od zera i nie powtarzaj tych odczytów, chyba że weryfikujesz zmianę.

---

## Dostęp

| Co | Jak |
|---|---|
| Google Ads | konto **674-207-1446** (CID `6742071446`), direct, NIE pod MCC |
| Helper Ads | `bash scripts/google/ads_call.sh <PATH> <METHOD> [JSON_FILE]` — wersja API z `~/secrets/google/ads-config.json` |
| GA4 | property **538301430**, strumień `G-KVFMR3NZDH`; Data API + Admin API przez `scripts/google/_lib.py` (`from _lib import api`) |
| GTM | konto `6356149706`, kontener **252883347** (`GTM-TDC85TQN`), workspace **4** |

Wzorzec wywołania GAQL:
```bash
echo '{"query":"SELECT ... FROM conversion_action"}' > /tmp/q.json
bash scripts/google/ads_call.sh /googleAds:searchStream POST /tmp/q.json
```

---

## Stan zmierzony 28.08 — punkt wyjścia

### Akcje konwersji na koncie (8)

| Nazwa | Typ | Status | Główna |
|---|---|---|---|
| `agria.pl (web) phone_click` | `GOOGLE_ANALYTICS_4_CUSTOM` | ENABLED | **TAK** |
| `agria.pl (web) form_submit` | `GOOGLE_ANALYTICS_4_CUSTOM` | ENABLED | nie |
| `agria.pl (web) generate_lead` | `GOOGLE_ANALYTICS_4_GENERATE_LEAD` | ENABLED | **TAK** |
| `agria.pl (web) file_download` | `GOOGLE_ANALYTICS_4_CUSTOM` | ENABLED | nie |
| `Połączenia z reklam (30s+)` | `AD_CALL` | ENABLED | **TAK** |
| `agria.pl (web) purchase` | `GOOGLE_ANALYTICS_4_PURCHASE` | **HIDDEN** | nie |
| `agria.pl (web) qualify_lead` | `GOOGLE_ANALYTICS_4_QUALIFY_LEAD` | **HIDDEN** | nie |
| `agria.pl (web) close_convert_lead` | `GOOGLE_ANALYTICS_4_CLOSE_CONVERT_LEAD` | **HIDDEN** | nie |

### Ile faktycznie zarejestrowano

- **Ads, 13–28.08:** `form_submit` **2 konwersje**. Wszystko inne — **zero**, w tym `phone_click`,
  który od 24.08 jest konwersją **główną**.
- **GA4, 13–28.08 (cały ruch, nie tylko Ads):** `phone_click` **1**, `generate_lead` **1**,
  `form_submit` **3**, `form_start` 4, `email_click` 2, `whatsapp_click` 2, `file_download` brak.
  Dla skali: `page_view` 376, `session_start` 285.
- **GA4, 30 dni:** **395 aktywnych użytkowników**, 413 sesji.

### Co po stronie tagów jest sprawne (sprawdzone, nie zakładaj że zepsute)

- GTM: wersja live **v5 z 10 tagami**, w tym `GA4 Event - Phone Click`, `Email Click`,
  `Generate Lead`, `WhatsApp Click`. Workspace 4 **zsynchronizowany 28.08** (T-088) — 10 tagów,
  zero konfliktów. Publikować można bezpiecznie.
- Tag `phone_click` **strzela** — GA4 zarejestrowało zdarzenie. Nie jest to więc martwy tag,
  tylko rzadkie zjawisko.
- Połączenie GA4 ↔ Ads istnieje, `adsPersonalizationEnabled: true`.
- Rozszerzenia połączeń spięte z kampaniami 28.08 (T-102) — **6 powiązań, oba numery × 3 kampanie**,
  wszystkie ENABLED. `AD_CALL` zacznie zbierać dane dopiero od 28.08, wcześniej asset wisiał
  wyłącznie na koncie (102 wyświetlenia na 1 895, zero kliknięć `CALLS`).

---

## Hipotezy do sprawdzenia — w tej kolejności

1. **Brak danych, nie błąd wdrożenia.** Google oznacza akcje bez konwersji w ostatnich ~30 dniach.
   Przy 1 zdarzeniu `phone_click` i 3 `form_submit` na 16 dni to najbardziej prawdopodobna przyczyna.
   Sprawdź, czy ostrzeżenie dotyczy tych akcji, czy raczej `HIDDEN`-owych (`purchase`, `qualify_lead`,
   `close_convert_lead`), które nigdy nie wystąpią na tej stronie — te warto **usunąć albo ukryć na stałe**.
2. **Podwójne liczenie / konflikt akcji.** `generate_lead` (typ GA4 GENERATE_LEAD) i `form_submit`
   (GA4 CUSTOM) mogą mierzyć to samo zdarzenie. Obie są aktywne, `generate_lead` jest główna.
   Sprawdź definicje zdarzeń w GA4 i czy nie liczą tego samego wysłania formularza.
3. **Ustawienia akcji:** okno konwersji, model atrybucji, `counting_type` (ONE_PER_CLICK vs EVERY),
   `primary_for_goal`. Odczyt: `SELECT conversion_action.name, conversion_action.counting_type,
   conversion_action.click_through_lookback_window_days, conversion_action.attribution_model_settings,
   conversion_action.primary_for_goal FROM conversion_action`.
4. **Cele konwersji na poziomie konta** (`customer_conversion_goal` / `campaign_conversion_goal`) —
   czy kampanie używają celu „Kontakty" i czy właściwe akcje są do niego przypisane.
5. **Enhanced conversions** — jeśli włączone bez poprawnego przekazywania danych, Google to zgłasza.

---

## Ograniczenia — czytaj przed działaniem

- ⛔ **NIE ruszaj Complianz ani warstwy zgód.** Zasada projektu: zgody zmieniamy **wyłącznie
  ustawieniami**, nigdy kodem, a w tym wątku najlepiej nie dotykaj ich w ogóle (wyraźna prośba
  Janka 28.08). Jeśli diagnoza prowadzi do zgód — **wróć z pytaniem, nie działaj**.
- ⛔ **Google Signals jest wyłączone** (świadomie, konfiguracja pre-M1). Dlatego GA4 nie ma
  demografii. Nie włączaj go przy okazji.
- ⚠️ **Zapis do konta klienta wymaga zgody Janka per operacja.** Backup stanu przed zmianą do
  `data/backups/` (katalog jest w `.gitignore`).
- ⚠️ **Listy remarketingowe są puste i to normalne** — próg dla sieci wyszukiwania to 1 000
  użytkowników/30 dni, mamy 395. Nie próbuj tego „naprawiać".

---

## Kontekst kampanii (stan po 28.08)

Rolnictwo: promień **150 km** × 2 (Niedomice, Radgoszcz), emisja **niedziela / poniedziałek / wtorek**
6:00–22:00, budżet **60 zł/dz**, 8 miast wykluczonych, 44 frazy (24 transakcyjne).
Paszarstwo 9 zł/dz, Marka 5 zł/dz — bez zmian, 7 dni.

**Cel biznesowy Janka:** dowieźć telefony jako twardą liczbę, żeby wystąpić do klienta (Kasjan)
o większy budżet. Dlatego poprawność pomiaru konwersji telefonicznych jest teraz **priorytetem
wyższym niż optymalizacja kampanii**.

⚠️ Pamiętaj przy wnioskach: **mierzymy telefony i formularze, nie sprzedaż.** Sprzedaż zna wyłącznie
AGRIA (Paweł 664 393 062, Kazimierz 781 875 411).

**Powiązane:** `docs/REJESTR_ZOBOWIAZAN.md` (dziennik M3, wpisy z 28.08: T-088, T-102, T-102b),
`docs/przypomnienia/2026-09-01-odczyt-konwersji-po-przestawieniu.md`, commit `f0a8770`.
