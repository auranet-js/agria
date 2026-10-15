# 2026-10-15 — rozliczenie Ads (T-109), przebudowa na jedną frazę tlenkową, kalendarz

Commit `8068077` na gałęzi `worktree-ads-tlenek` (do fast-forward na `main`). Kalendarz „Auranet Claude”:
zamknięte T-109 i trzy wrześniowe posty GBP (przeniesione do planu październikowego).

## Co zrobione

| Obszar | Wynik |
|---|---|
| T-109 „koniec cyklu Ads 15.09–15.10” | Cykl wyczerpany **12.10**: 1 136,23 zł, 691 klik., CPC 1,64 zł, **1 konwersja**, **0 połączeń z reklam** przy 515 wyświetleniach numeru. Janek wstrzymał 3 kampanie 12.10 12:17. Od 13.08 łącznie ok. 2 570 zł i 4 konwersje bez potwierdzonej sprzedaży. Dane surowe: `tmp/t109/` (głównej kopii) |
| Geo starych kampanii | Rolnictwo: 2 × 150 km, 8 miast wykluczonych. Paszarstwo i Marka: cała Polska — ok. 230 zł poza 4 województwami (małopolskie, śląskie, podkarpackie, świętokrzyskie), zero konwersji |
| Planer słów kluczowych | Tlenek hurtowy (bez budowlanych, worków, stawów) ok. **2 000 wyszukiwań/mies. w kraju ≈ 66/dz**; górny zakres stawki na górę strony 1,4–2,0 zł. Ograniczeniem jest popyt, nie budżet |
| Nowa kampania „AGRIA - Wapno tlenkowe” | **1 fraza** „wapno tlenkowe” (do wyrażenia), 80 km od Niedomic, 2,50 zł, 15 zł/dz, 7 dni 6–22, 34 wykluczenia, tylko numer Pawła, reklama na kartę Agrobielik 70. Utworzona **PAUSED**, sprawdzona odczytem z konta; reklama w weryfikacji Google. Skrypt `scripts/ads/tlenek-2026-10-15/build.py` |
| Wizytówka Tarnów | Odczyt API: ostatni post **08.09**, posty z 16/23/30.09 i 13.10 nie wyszły; opinii 9, ostatnia 28.02.2025 |

## Wnioski warte pamiętania

- **Rozproszenie zabiło wynik:** 40 zł/dz na 3 kampanie, 7 grup, ok. 50 fraz — nic nie stało stale na górze. Zasada od teraz: jedna fraza, pierwsza pozycja, obszar pod realny wolumen (memory `feedback_agria_ads_koncentracja_nie_rozproszenie`).
- **Bez pomiaru telefonów nie ma wyniku do pokazania.** AD_CALL = 0 przez cały cykl. Warunek startu: Paweł pyta dzwoniących, skąd znają AGRIĘ.
- **Kody województw `geoTargetConstants/208xx` sprawdzaj zapytaniem** — 6 z 7 podanych z pamięci było błędnych. Małopolskie 20852, podkarpackie 20856, świętokrzyskie 20858, śląskie 20859, lubelskie 20851, łódzkie 20850, opolskie 20854. Planer zaokrągla małe frazy do 10, więc sumy województw są zawyżone.
- Performance Max odrzucony — przy kilku konwersjach na miesiąc nie ma na czym się uczyć.

## Otwarte

- **Start kampanii tlenkowej:** kolejna faktura albo aktywacja przyznanej promocji Google **oraz** decyzja Pawła, czy ceny na stronie i w reklamach idą za OLX (granulaty 250/260 zł/t; tlenek 220 zł/t tej zmiany nie dotyczy). Przy starcie: Wapno tlenkowe + Marka (5 zł/dz) włączone, Rolnictwo i Paszarstwo zostają wstrzymane.
- T-161 i T-162 (stare Rolnictwo) — kandydaci do „Unieważnione”.
- Numer **604 428 782** w rozszerzeniach połączeń — nieprzypisany do nikogo, do wyjaśnienia.
- Wizytówka: akcept planu październikowego, zaległy post, eventy wtorkowe.

## Prompt kontynuacyjny

```
Pracujemy w ~/projekty/agria — październik (M5), stan na 15.10.2026.

0. Najpierw: git pull, potem dołącz gałąź z 15.10:
   git merge --ff-only origin/worktree-ads-tlenek && git push
   Potem git log --oneline -10 i „sprawdź kalendarz”.

Przeczytaj: docs/sesje/2026-10-15-ads-przebudowa-tlenek.md, wiersz T-109 w docs/REJESTR_ZOBOWIAZAN.md,
docs/sesje/2026-10-08-olx-cykl3-seo-gbp.md (sekcja „Otwarte”),
docs/decyzje/2026-10-08-olx-tlenek-wysylka-z-magazynow.md,
memory feedback_agria_ads_koncentracja_nie_rozproszenie.md.

Stan, którego nie odtwarzaj od nowa:
- ADS: wszystkie kampanie WSTRZYMANE od 12.10. Kampania „AGRIA - Wapno tlenkowe” gotowa i wstrzymana
  (1 fraza, 80 km od Niedomic, 2,50 zł, numer Pawła, reklama na Agrobielik 70). START dopiero gdy:
  (a) kolejna faktura albo aktywacja przyznanej promocji Google, ORAZ (b) decyzja Pawła o cenach
  na stronie i w reklamach. Przy starcie: Wapno tlenkowe + Marka (5 zł/dz) włączone, Rolnictwo
  i Paszarstwo wstrzymane; sprawdź moderację reklamy. T-161/T-162 — zaproponuj przeniesienie
  do „Unieważnione”, nie rób sam.
- CENY: OLX granulaty węglanowe 250/260 zł/t (Paweł 13.10), strona i ofertownik 350/370 — zostają
  do decyzji Pawła po teście. Tlenek (220 zł/t) tej zmiany nie dotyczy.
- WIZYTÓWKA Tarnów: ostatni post 08.09. Plan docs/gbp/2026-10-08-pazdziernik-publikacje.md czeka
  na mój akcept. Po akcepcie: zaległy post + eventy wtorkowe. Niedomice/Radgoszcz — sprawdź git log
  (commit 6921005), co z T-165…T-170 już zrobione.

Kolejność pracy w październiku (pytaj o „ok” przed każdym zapisem na produkcji i koncie klienta):
1. Kalendarz: 20.10 kontrola moderacji OLX (T-149/T-155/T-156/T-163), 22.10 kontrole 14-dniowe
   T-071 „kreda do stawu” i T-080 „poradnik pH gleby”, 30.10 kontrola OLX 22 dni.
2. SEO T-157…T-160 z docs/seo/2026-10-08-PLAN-PAZDZIERNIK-LISTOPAD.md — każda zmiana z backupem,
   linkiem do akceptu i zgłoszeniem w GSC.
3. Wizytówki — akcept postów październikowych, potem T-165 (odpowiedzi na opinie Niedomic).
4. OLX T-164 „promocja tlenku” — rekonesans jest (commit 096f46b); kupno tylko z portfela OLX
   (08.10: 0 zł) — sprawdź saldo, nic nie kupuj bez „ok”.
5. 31.10: T-107 „podsumowanie 3 miesięcy Ads” — wydatek, brak wyniku, przebudowa, warunek pomiaru
   telefonów (Paweł pyta „skąd nas znacie”).
6. Początek listopada: raport M5 wg docs/prompty/PROMPT_RAPORT_MIESIECZNY.md.

Czeka na Pawła (nie zgaduj): T-077 dawka kredy pastewnej; decyzja o cenach; liczba telefonów
i zamówień z OLX i Google od połowy września.
```
