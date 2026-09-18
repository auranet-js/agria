# Przebudowa kampanii „AGRIA - Marka" — pakiet wykonawczy

> **Data przygotowania:** 2026-09-18 · **Kampania:** 24131649588 · **Grupa Brand:** 198590178225
> **Stan przed zmianą:** `tmp/ads-marka-2026-09-18-PRZED-kryteria.json` i `…-PRZED-reklamy.json`
> **Podstawa:** odczyt Ads API 14.08–17.09, GSC 90 dni, DataForSEO 18.09 (koszt 0,11 USD)

## Dlaczego ta kampania pierwsza

Najmniejsza (84,19 zł w pięć tygodni), najprostsza (jedna grupa, osiem fraz) i jedyna **bez
ani jednego wykluczenia**. Przy tym zawiera najlepszą i najgorszą frazę całego konta, co daje
czysty dowód na regułę, którą chcemy zastosować wszędzie: **strona docelowa ma odpowiadać zapytaniu.**

| fraza | wyśw. | klik. | CTR | CPC | QS | strona docelowa |
|---|---|---|---|---|---|---|
| agria wapno | 40 | 15 | **37,5%** | **0,90 zł** | **10** | powyżej średniej |
| agria tarnów | 68 | 12 | 17,6% | 1,21 zł | **10** | powyżej średniej |
| agria (ścisłe) | 165 | 18 | 10,9% | 1,73 zł | 8 | powyżej średniej |
| oxyfertil | 107 | 6 | 5,6% | 1,45 zł | 5 | średnia |
| bielik wapno | 197 | 9 | 4,6% | 1,48 zł | 3 | **poniżej** |
| agrobielik ×2 | 21 | 2 | — | 1,47 zł | **1** | **poniżej** |
| ekograncali | 0 | 0 | — | — | — | — |

Wszystkie prowadzą na `https://agria.pl/`. Dla pytania o firmę to właściwa odpowiedź (QS 8–10),
dla pytania o produkt — nie (QS 1–3).

Kampania traci **48,6% wyświetleń przez ranking** i tylko 6,9% przez budżet. Budżet 5 zł/dz
nie jest ograniczeniem i **nie zmieniamy go**.

## Co mówi pomiar DataForSEO o nazwie „agria" w polskim Google

| kontekst | wolumen/mies. |
|---|---|
| **ziemniaki odmiany Agria** (ziemniaki agria 210, agria ziemniaki 90, gdzie kupić 40, opinie 20, sadzeniaki, cena) | **~390** |
| **maszyny Agria-Werke** (traktorek 70, glebogryzarka 90, modele 400/1600/2100/2400/4800, kosiarka listwowa 30, części 60) | **~370** |
| Agria Grecja (wioska na Pelionie) | 70 |
| Agria insurance, ditianon, crema agria | ~20 |
| **nasze: agria niedomice** | **50** |
| **nasze: agria tarnów** | 20 |
| nasze: agria wapno | 10 |

**Ziemniaki są groźniejsze od maszyn** — to ta sama publiczność (rolnik), więc kontekst sam ich nie odsieje.

⚠️ **„agria [miasto]" nie jest problemem.** Sprawdzone: Kraków, Warszawa, Poznań, Wrocław, Katowice,
Lublin, Rzeszów, Kielce, Gdańsk, Łódź — **zero wolumenu**. Jedyne miasta z ruchem to nasze.
Zamiast blokować, **dodajemy `agria niedomice`** (50/mies., większy wolumen niż Tarnów, brak w kampanii).

## Kolejność wykonania

```bash
cd ~/projekty/agria
D=scripts/ads/brand-2026-09-18

# 1. Wykluczenia (26 pozycji) — kampania nie ma dziś żadnych
bash scripts/google/ads_call.sh /campaignCriteria:mutate POST $D/01-wykluczenia.json

# 2. Pauzy martwych i produktowych fraz + dodanie „agria niedomice"
bash scripts/google/ads_call.sh /adGroupCriteria:mutate POST $D/02-pauzy-i-nowa-fraza.json

# 3. Dwie nowe grupy — ZAPISZ ZWRÓCONE ID
bash scripts/google/ads_call.sh /adGroups:mutate POST $D/03-nowe-grupy.json

# 4. Podmień ID_GRUPY_BIELIK i ID_GRUPY_OXY w plikach 04 i 05, potem:
bash scripts/google/ads_call.sh /adGroupCriteria:mutate POST $D/04-frazy-nowych-grup.json
bash scripts/google/ads_call.sh /adGroupAds:mutate POST $D/05-reklamy.json
```

Kroki 1 i 2 są niezależne od 3–5 i można je wykonać same.

## Co się zmienia

| | przed | po |
|---|---|---|
| wykluczenia kampanii | **0** | 26 |
| grupy | 1 (Brand) | 3 (Brand, Bielik, Oxyfertil) |
| frazy aktywne | 8 | 4 w Brand + 5 w nowych grupach |
| frazy martwe | agrobielik ×2, ekograncali | wstrzymane |
| strony docelowe | wszystko na `/` | `/` dla firmowych, karty #309 i #312 dla produktowych |
| budżet | 5 zł/dz | **bez zmian** |
| stawki | 1,50 zł | bez zmian; oxyfertil 1,20 zł (organik na poz. 4,8) |

## Weryfikacja po wykonaniu

```bash
# frazy i statusy
bash scripts/google/ads_call.sh /googleAds:searchStream POST <(echo '{"query":"SELECT ad_group.name, ad_group_criterion.keyword.text, ad_group_criterion.status FROM ad_group_criterion WHERE campaign.name = \"AGRIA - Marka\" AND ad_group_criterion.type = \"KEYWORD\""}')

# reklamy i strony docelowe
bash scripts/google/ads_call.sh /googleAds:searchStream POST <(echo '{"query":"SELECT ad_group.name, ad_group_ad.ad.final_urls, ad_group_ad.status FROM ad_group_ad WHERE campaign.name = \"AGRIA - Marka\""}')
```

Oczekiwane: 3 grupy, 9 fraz (4 aktywne w Brand + 5 w nowych), 3 reklamy `ENABLED`, dwie
prowadzące na karty.

## Rollback

Nic nie jest usuwane — wszystkie zmiany to `PAUSED` albo `create`. Cofnięcie:
- wykluczenia → usunąć przez `campaignCriteria:mutate` z operacją `remove`
- pauzy → `status: ENABLED` na tych samych `criterionId` (lista w pliku 02)
- nowe grupy → `status: PAUSED` albo `REMOVED`
Stan wyjściowy w `tmp/ads-marka-2026-09-18-PRZED-*.json`.

## Czego pomiar po zmianie ma dotyczyć

**Nie konwersji** — przy 84 zł na pięć tygodni ta kampania nigdy nie da statystyki konwersyjnej.
Mierzymy dwie rzeczy, obie po **14 dniach**:

1. **Wynik jakości `bielik wapno`**: dziś 3, strona docelowa `poniżej średniej`. Jeśli przeniesienie
   na kartę #309 nie ruszy oceny w dwa tygodnie, to znaczy, że problem nie leży w trafności strony —
   i to jest wynik ważny dla decyzji o pozostałych kampaniach.
2. **Udział w wyświetleniach kampanii**: dziś 44,5%, utrata przez ranking 48,6%. Jeśli wzrost QS
   przełoży się na udział bez podnoszenia stawki, ta sama dźwignia zadziała w Rolnictwie.

⚠️ **Świadomie nie zmieniamy stawek razem ze stronami docelowymi.** Dwie zmienne naraz = brak wniosku.
