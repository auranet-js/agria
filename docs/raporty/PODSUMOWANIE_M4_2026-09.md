# Podsumowanie M4 — wrzesień 2026 (wewnętrzne)

> Stan na 05.10.2026. Plan = sekcja „Plan na wrzesień” z maila wysłanego 01.09 (skrzynka `claude@auratest.pl`, ID 292).
> Dowody: dziennik M4 w `docs/REJESTR_ZOBOWIAZAN.md`, commity, dane w `data/raport-2026-09/` (pull 05.10).

## 1. Plan kontra wykonanie

| # | Plan na wrzesień (mail 01.09) | Stan | Dowód |
|---|---|---|---|
| 1 | Treści pod oczyszczalnie i wapno hydratyzowane | **zrobione** | T-093 21.09 (`4c2378d`, opis 976 B → 8 732 B), T-085 21.09 (`09987db`), kategoria Oczyszczalnie 1 → 4 produkty 14.09 (`180d34d`) |
| 2 | Opisy kategorii: wapno nawozowe dla rolnictwa i paszarstwo | **zrobione** | T-092 05.09 (`049563a`), `/paszarstwo/` 08.09 (`383b7d7`). GSC: `/paszarstwo/` 2 → **27** wejść, poz. 13,0 → **5,8** |
| 3 | Poradnik „wapno pod ziemniaki” | **zrobione** | T-074 23.09 (`6c3f47e`), wpis 2837. W tydzień: **18 wejść, 639 wyśw., poz. 3,6** |
| 4 | Szybkość strony na telefonach | **zrobione** | Blok 0 + WP Rocket 07.09 (`04e1a31`, `e719836`, `4e49aed`): strona główna LCP mobile 7,4 → 3,7 s, karta Agrobielik 90 11,8 → 6,2 s, TTFB z cache 1,40 → 0,03 s |
| 5 | Kalkulator z magnezem na stronę | **zrobione** | T-044 04.09 (`8e6c744`, 555 testów). Odbiór Kazimierza na produkcji potwierdzony przez Janka 05.10 |
| 6 | Dane obu magazynów w wynikach lokalnych Google | **częściowo** | Niedomice odzyskane 18.09 (T-047, `hasVoiceOfMerchant: true`), nieuzupełnione; Radgoszcz bez dostępu; `LocalBusiness` ×2 (T-030) niezrobione |
| 7 | Reklamy z korektami na danych | **zrobione** | Odczyt 07.09, mapa konta i przebudowa „Marka” + harmonogram Rolnictwa 18.09 (`e1340b0`), budżet Rolnictwa 28 zł/dz (Janek) — odczyt API 05.10: Rolnictwo 28 · Paszarstwo 9 · Marka 5 zł/dz |

## 2. Ponad plan

- **T-136 — wszystkie 19 kart produktów napisane od nowa** (11–14.09, 19 commitów `[content] T-136`), poprzedzone bazą wiedzy produktowej T-134 (`3bd6f8b`). Efekt GSC: karty **77 → 196 wejść** (×2,5), wyświetlenia 4 417 → 11 396. Kontrola 18.09: 24/24 adresów w indeksie.
- Blok 0 (07.09): 404, `offers` w schemacie 16 kart, formularz callback na landingach, telefon w formularzu.
- Crawl kontrolny własnym narzędziem (08.09), rekonstrukcja architektury (10.09, `cf45060`).
- Wizytówka Tarnów: atrybuty, obszar obsługi, pierwszy post 08.09. ⚠️ **Rytm wtorkowy nie wyszedł** — API 05.10: we wrześniu tylko 1 post (08.09), posty 16/23/30.09 nie opublikowane. Na stronie postępu poprawione „cotygodniowe wpisy”.
- OLX: T-137…T-140 (11.09), odczyt 14.09, audyt 23.09 + T-142…T-146.
- T-141 rozkład zapytań, T-110 korekta konwersji (18.09).
- **T-147 katalog PDF po słoweńsku** (24.09, `4107c58`) — poza ryczałtem, 4 h.

## 3. Godziny (tylko do wewnątrz)

| Zakres | Zmierzone | Pozycji z godzinami | Pozycji bez godzin |
|---|---|---|---|
| R (ryczałt) | **24,5 h** | 12 | 17 (Blok 0, 12 kart T-136, kategoria Oczyszczalnie, T-074, ilustracje, strona postępu) |
| P (poza ryczałtem) | **28 h** | 13 | 0 |
| **Razem** | **52,5 h** | | |

P = Ads (prowadzenie 600), OLX (obsługa 300), T-044 kalkulator Mg (3 h), T-147 katalog SL (4 h).

Commity bez wiersza w dzienniku (wszystkie z kart T-136 zgrupowanych w dzienniku po produkcie): #312, #315 (pilot 11.09), #320, #302, #318 (14.09) — mają commity, brak osobnych wierszy. Nie wpływa na rozliczenie (R, bez godzin).

## 4. Koszty września

Zapowiedziane w mailu 01.09:

| Pozycja | Netto | Linia na fakturze ASEO |
|---|---|---|
| Opieka nad stroną i pozycjonowanie | 2 000 zł | Prace techniczne przy stronie WWW |
| Budżet reklamowy Google | 1 200 zł | Google ADS — Budżet reklamowy |
| Prowadzenie kampanii | 600 zł | Google ADS — Obsługa kampanii reklamowej |
| Stała obsługa OLX | 300 zł | Prace techniczne przy stronie WWW |
| Katalog produktowy w wersji słoweńskiej (T-147) | 500 zł | Prace techniczne przy stronie WWW |
| **Razem AGRIA** | **4 600 zł** | |

Z maila ASEO z 05.10 (ID 329): ASEO 2 500 SEO + 400 obsługa Ads + 500 budżet Ads. **Wkład AGRII w fakturę zbiorczą: prace techniczne 2 800 · obsługa Ads 600 · budżet Ads 1 200 = 4 600 zł netto.** Fakturę zbiorczą Janek liczy w projekcie ASEO.

`[DO POTWIERDZENIA]`:
- ✅ T-147 katalog słoweński: **500 zł netto na wrzesień** (decyzja Janka 06.10). Wrzucenie na stronę (T-148) w ryczałcie.
- Budżet Ads: wydane IX **1 298,02 zł** (> 1 200), sierpniowa nadwyżka 390,42 zł pokryła różnicę. Saldo na koncie po 30.09 ≈ 1 200 × 2 − (809,58 + 1 298,02) = **292,40 zł** — zakładając, że oba miesiące zostały zasilone pełnym 1 200 zł.

## 5. Ryzyka i terminy października

- **Pakiet OLX wygasa ~16.10** (monitor 05.10: `dni_pakietu` 11). Przedłuża Paweł. Kontrola 07.10, decyzja przed 10.10.
- **T-130 film hero na mobile — przegląd 07.10.**
- T-077 poradnik kreda pastewna (termin 30.09) — **niezrobiony**, przechodzi na październik.
- Ads: od 15.09 **0 konwersji** na 492 kliknięcia; we wrześniu 2 × `phone_click`, koszt ~649 zł/konw. 72% wydatku na landingi `noindex` (mapa 18.09). Decyzja D2 o stronach docelowych otwarta.
- T-107 podsumowanie 3 miesięcy Ads — termin 31.10 (zobowiązanie z 06.08).
