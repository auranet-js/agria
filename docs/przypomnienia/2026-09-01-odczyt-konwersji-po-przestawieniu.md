# Odczyt konwersji — 2 dni po przestawieniu kampanii na wieś

**Kiedy:** wtorek 01.09.2026 rano · **Projekt:** agria · **Konto Ads:** 674-207-1446 (CID 6742071446)
**Helper:** `bash scripts/google/ads_call.sh /googleAds:searchStream POST <plik.json>`

## Co się zmieniło 28.08 (to jest mierzone)

| | przed | po |
|---|---|---|
| zasięg | 8 województw → promień 100 km | **promień 150 km** × 2 (Niedomice, Radgoszcz) |
| dni emisji | 7 dni | **niedziela · poniedziałek · wtorek** 6:00–22:00 |
| budżet Rolnictwa | 26 zł/dz | **60 zł/dz** (13 dni × 60 ≈ 780 zł/mies, jak dotąd) |
| wykluczenia | brak | **8 miast**: Kraków, Katowice, Częstochowa, Bielsko-Biała, Kielce, Rzeszów, Tarnów, Nowy Sącz |
| frazy | 36 (16 transakcyjnych) | **44 (24 transakcyjne)** |
| rozszerzenia połączeń | tylko na koncie (5% wyświetleń) | **na wszystkich 3 kampaniach** (T-102, 28.08) |

Stan sprzed: `data/backups/T-104-rolnictwo-kryteria-przed-2026-08-28.json`

## Dane do odczytu (okres 30.08–01.09)

1. **Konwersje wg akcji** — `segments.conversion_action_name`, `metrics.all_conversions` z `campaign`.
   Interesują trzy: **`Połączenia z reklam (30s+)` (AD_CALL)** — pierwszy pomiar telefoniczny niezależny
   od zgód na stronie, działa od 28.08; **`phone_click`** (GA4, główna od 24.08); **`form_submit`**.
2. **Wolumen w dniu emisji** — czy 60 zł faktycznie schodzi. Przed zmianą Rolnictwo wydawało 27,64 zł/dz
   przy budżecie 26 i traciło **90% wyświetleń przez budżet**.
3. **Udział w wyświetleniach** — czy ruszył. ⚠️ Google raportuje wartości poniżej 10% jako `0.0999`
   („< 10%"), więc „10,0%" w odczycie **nie jest pomiarem, tylko progiem**.
4. **Search terms** — czy po wykluczeniu miast profil zapytań się zwiejszczył (mniej `trawnik`, `bielenie`).
5. **Rozkład geo** — `geographic_view` z `geographic_view.location_type`; sprawdzić, czy wykluczenia miast
   faktycznie odcięły ruch miejski.

## Progi i jak to czytać

- **Ambicja Janka: 1–2 sprzedaże dziennie przy 60 zł.** Przy CPC ~1,90 zł to ~30 kliknięć w dniu emisji,
  czyli konwersja 3–7%. Dla B2B surowcowego z kontaktem telefonicznym — ambitne, ale nie absurdalne.
- ⚠️ **Mierzymy telefony i formularze, nie sprzedaż.** Sprzedaż zna wyłącznie AGRIA. Żeby zamknąć dowód
  „to działa", potrzebne jest potwierdzenie od **Pawła (664 393 062)** albo **Kazimierza (781 875 411)**,
  ile z tych telefonów zamieniło się w zamówienie. Bez tego mamy leady, nie wynik sprzedażowy.
- **Dwa dni to za mało na wniosek o skuteczności.** Wystarczy natomiast, by zobaczyć: czy budżet schodzi,
  czy AD_CALL w ogóle rejestruje, czy ruch nie zniknął po wykluczeniach.
- **Nisza sama nie wypełni 60 zł** — oś transakcyjna przy 150 km i 3 dniach to ~283 wyszukania/mies,
  czyli ~1,3 kliknięcia w dniu emisji. Resztę zjedzą frazy szersze i tak ma być.

## Decyzje czekające na te dane

- **Rzeszów** — wykluczony wbrew pomiarowi (48% intencji rolniczej wobec 32% Krakowa). Pierwszy kandydat
  do przywrócenia, jeśli Rolnictwo będzie głodować.
- **Wniosek o większy budżet do Kasjana** — Janek złoży go, jeśli zobaczy, że mechanizm działa. Materiał:
  telefony + potwierdzenie sprzedaży od AGRII.
- Rozliczenie sierpnia: z 1 200 zł wykorzystane 539,57 zł do 28.08; przy 3 dniach emisji sierpień zamknie
  się ~660 zł. Wrzesień to pierwszy pełny miesiąc w nowym układzie.

## Kontekst w repo

`docs/REJESTR_ZOBOWIAZAN.md` — dziennik M3, wpisy z 28.08 (T-088, T-102, T-102b, geo, przestawienie).
Sezonowość: **sierpień jest szczytem roku**, nie październik (`project_agria_sezon_sierpniowy`).
