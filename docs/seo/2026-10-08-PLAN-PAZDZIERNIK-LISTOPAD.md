# SEO AGRII — plan październik–listopad 2026 (wątek SEO)

> **Data:** 2026-10-08 · **Status:** propozycja do akceptu Janka, nic nie wdrożone.
> **Numery:** T-157…T-162 (T-149…T-156 zarezerwowane dla wątku OLX). Wiersze do rejestru — na końcu, rejestr nietknięty.
> **Dane:** GSC 07.09–04.10 (28 dni, dojrzałe), poziom strony i zapytanie × strona —
> zrzut roboczy w scratchpadzie sesji, liczby przepisane niżej. Ads: odczyt API 08.09–07.10 (30 dni).
> Wejście: `data/kontrole/2026-10-08-kontrole-zalegle-seo.md`, `docs/produkty/_WNIOSKI.md`, rejestr (Faza 2, Unieważnione).

---

## Diagnoza w pięciu zdaniach

1. **Opisy kategorii działają na widoczność** (/paszarstwo/ ×23, rolnictwo +157% przy tle +70%), **nie na kliknięcia**:
   serwis ma 1,27% CTR, a kategoria rolnicza 0,61% przy 2 619 wyświetleniach.
2. **Największe pojedyncze luki to frazy rodzajowe, na których nie istniejemy:** `wapno magnezowe` 1 900/mies. → **40 wyświetleń**
   w 28 dni, `wapno palone` 2 400 (X–XI **3 600**) → **54 wyświetlenia rozsiane po 5 adresach**, `wapno tlenkowe` 720 → 35.
3. **Kanibalizacja to w praktyce brak wskazania zwycięzcy**, nie nadmiar treści: na `wapno węglanowe` karta odm. 04 (414 wyśw., poz. 10,2)
   konkuruje z granulowaną (103, poz. 20,6), a żaden poradnik nie linkuje do niej kotwicą „wapno węglanowe”.
4. **Hub `/wapnowanie-gleby/` (16 787 wyśw., CTR 0,69%) zostawiamy** — tytuł i opis przepisał T-053 (21.08), T-069 unieważnione;
   powtórka byłaby trzecim podejściem do tej samej rzeczy bez nowej hipotezy.
5. **Ads Rolnictwo ma inny problem niż Marka:** traci **48% wyświetleń przez budżet** (ranking tylko 14%), a **79% wydatku**
   (641 z 808 zł) idzie na frazy z oceną strony docelowej „poniżej średniej” — 416 kliknięć, **1 konwersja**.

---

## Zmiany w kolejności priorytetu

### 1. T-157 „tytuł i opis kategorii Wapno nawozowe” — **gotowe do wdrożenia**

**URL:** `/wapno-nawozowe-rolnictwo/` · pola `rank_math_title`, `rank_math_description` (H1 „Wapno nawozowe” bez zmian — nazwa kategorii to D1).

| | dziś | proponowane |
|---|---|---|
| tytuł w Google | `Wapno nawozowe do rolnictwa \| AGRIA` | **`Wapno nawozowe rolnicze — tlenkowe, węglanowe, kreda \| AGRIA`** (59 zn.) |
| opis | „Wapno nawozowe do odkwaszania gleb lekkich i ciężkich. Tlenkowe CaO 70-90%, węglanowe granulowane, kreda. Luzem 24t. Skontaktuj się z nami.” | **„15 produktów: wapno tlenkowe 70–90% CaO, węglanowe sypkie i granulowane, z magnezem i bez, kreda nawozowa. Luz 24 t, big-bag, worek 25 kg, własny transport.”** |

**Dlaczego:** 2 619 wyświetleń / 16 kliknięć (**0,61%**) w 28 dni; `wapno nawozowe` (1 300/mies.) 1 163 wyśw. na poz. 9,2 → **2 kliknięcia**;
`wapno rolnicze` 261 wyśw., poz. 7,0 → 3 kliknięcia — „rolnicze” nie ma dziś ani w tytule, ani w opisie. Obecny opis kończy się
pustym wezwaniem, nie mówi, co jest na liście. Bez ceny (memory: zero kwot w tytułach). Liczby z listingu (15 produktów) i z kart.
**Kontrola:** GSC 14 i 28 dni po wdrożeniu, CTR **z poziomu strony** wobec tła serwisu, plus CTR frazy `wapno nawozowe`.

### 2. T-158 „wapno palone przed szczytem X–XI” — **gotowe do wdrożenia, z jedną decyzją o T-084**

Szczyt `wapno palone` to **październik–listopad (3 600/mies.)** — jedyny duży klaster, który szczytuje teraz, a nie w sierpniu
(memory `project_agria_sezon_sierpniowy`). Dziś: 54 wyświetlenia, 0 kliknięć, 5 adresów; najlepiej karta #320 (12 wyśw., poz. 10,7).
`_WNIOSKI.md` przypisuje frazę do #320 (+ #310, #311 jako tlenkowe palone).

- **Zwycięzca: karta `/wapno-do-oczyszczalni/wapno-palone-mielone/` (#320).** Tytuł w Google:
  `Wapno palone mielone do higienizacji osadów ściekowych | AGRIA` → **`Wapno palone mielone wysokoreaktywne, big-bag i luz | AGRIA`** (59 zn.).
  Fraza rodzajowa na początku, zastosowanie zostaje w opisie (opis bez zmian — **nie dopisujemy stabilizacji**, bo żadna karta PDF
  jej nie podaje, D3).
- **Agrobielik 70 i 90** (`/wapno-nawozowe-rolnictwo/agrobielik-70/`, `…/agrobielik-90/`) — słowo „palone” występuje na nich **0 razy**,
  choć to wapno tlenkowe palone (tak opisują je dystrybutorzy i stary serwis AGRII, `/oferta/rolnictwo/wapno-nawozowe-tlenkowe-palone-…`).
  W pierwszym akapicie: „wapno nawozowe tlenkowe (palone)”. Treść opisowa, nie parametr — dozwolone wg reguły kart z 10.09.
- **Decyzja Janka:** T-084 „treść pod wapno palone na `/wapno-do-stabilizacji-gruntow/`” celuje w stronę, którą D3 zostawia bez
  rozstrzygnięcia, a Google woli kartę #320. Propozycja: T-084 zamknąć jako wchłonięte przez T-158.
**Kontrola:** 28 dni (szczyt trwa do końca XI): wyświetlenia klastra „palon” i liczba adresów na `wapno palone`.

### 3. T-159 „hub prowadzi do karty wapna magnezowego” — **gotowe do wdrożenia**

`wapno magnezowe` **1 900/mies. (najwięcej po granulowanym)**, `wapno magnezowe granulowane` 880 — a karta
`/wapno-nawozowe-rolnictwo/weglanowe-magnez-granulowane/` stoi na **poz. 14,4** (239 wyśw., 1 klik.). Hub `/wapnowanie-gleby/`
już łapie frazy dawkowe o magnezie na poz. 5–8: `ile wapna magnezowego na hektar` 136, `wapno magnezowe granulowane ile na hektar` 122,
`wapno magnezowe ile na hektar` 102 (razem 360 wyśw., 0 kliknięć), a do karty linkuje raz, kotwicą „wapno węglanowe z magnezem granulowane”.

**Zmiana na hubie** (sekcja „Wapń i magnez – duet krytyczny”), nowe H3:
> **Ile wapna magnezowego na hektar**
> Wapno magnezowe granulowane stosuje się w dawce **1–6 t/ha** (karta produktu) — dawkę dla swojego pola, z uwzględnieniem
> zawartości magnezu w glebie, policzysz w kalkulatorze wapnowania. [wapno magnezowe granulowane →]

Dawka z karty (`docs/produkty/weglanowe-magnez-granulowane.md`: 1–6 t/ha), bez rozbijania po pH — karta tego nie podaje.
Na karcie nic nie dopisujemy: FAQ „Ile wapna magnezowego granulowanego dać na hektar?” już jest.
**Kontrola:** 28 dni — pozycja karty na `wapno magnezowe granulowane` (dziś 14,4) i kliknięcia huba na trzech frazach dawkowych.

### 4. T-160 „kotwice fraz rodzajowych do zwycięzców” — **gotowe do wdrożenia, nie zależy od D1**

Kotwice w trzech poradnikach o największym ruchu: `/wapnowanie-gleby/` (16 787 wyśw.), `/jak-stosowac-wapno-nawozowe/` (5 687), `/ph-gleby/`.
Zmieniamy tekst istniejących linków albo dopisujemy jeden w zdaniu, które już mówi o produkcie — bez nowych sekcji.

| fraza (popyt) | dziś w GSC | zwycięzca | co |
|---|---|---|---|
| `wapno węglanowe` (1 000) | odm. 04 414/poz. 10,2 · granul. 103/20,6 · Mg granul. 10/48,2 | **`…/weglanowe-odmiana-04/`** | kotwica „wapno węglanowe” → odm. 04 w hubie i w `/jak-stosowac/`; przy granulowanym zawsze „wapno węglanowe **granulowane**” |
| `wapno tlenkowe` (720) | tlenkowe z Mg 17/25,8 · mieszanka 7/21,6 · Agrobielik 70 3/**6,0** | **`…/agrobielik-70/`** | kotwica „wapno tlenkowe” → Agrobielik 70 (dziś linki mają kotwicę nazwy produktu) |
| `kreda nawozowa` (1 000) | granulowana 120/11,1 · sypka 15/20,9 · 5 innych po 1–9 | **`…/kreda-nawozowa-granulowana/`** | kotwica „kreda nawozowa” → granulowana; sypka trzyma `kreda nawozowa sypka` (58 wyśw., **poz. 3,1**; karta: CTR 4,30%) |
| `wapno nawozowe` (1 300) | kategoria 1 163/9,2 · **strona główna 194/6,2** | **kategoria** | zostawiamy do D1 — strona główna to układ Elementora, ruszamy ją raz, razem z D1 |

**Kontrola:** 28 dni — liczba własnych adresów na frazę i pozycja zwycięzcy (dziś wyżej).

### 5. T-161 „Ads Rolnictwo: wstrzymanie 12 fraz z wynikiem jakości ≤ 3” — **decyzja Janka (D2 otwarte), nie wykonuję**

13 fraz z QS 1–3 w 30 dni: **227,67 zł, 116 kliknięć, 1 konwersja** — ta jedna na `kreda nawozowa` (52,77 zł), więc ją zostawiamy.
Pozostałe 12: **174,90 zł, 89 kliknięć, 0 konwersji**, m.in. `wapno z magnezem` 54,88 zł (QS 3), `wapno magnezowe granulowane` 31,43 (3),
`wapno cena za tonę` 29,45 (2), `wapno big bag` 19,87 (2), `wapno tlenkowe` 17,68 (3).
Kampania traci 48% wyświetleń przez budżet — wstrzymanie nie zmniejsza wydatku, tylko przesuwa ok. **175 zł/mies.** na frazy z QS 5–8.
**Kontrola:** 14 dni — CPC kampanii i udział w wyświetleniach (dziś IS 37,6%, utrata przez budżet 48,0%).

### 6. T-162 „Ads Rolnictwo: grupa Wapno granulowane na karty” — **decyzja Janka (D2 otwarte), nie wykonuję**

Grupa „Wapno granulowane”: **326,75 zł, 169 kliknięć, 0 konwersji** w 30 dni, cel `/wapno-granulowane/` (noindex, ocena strony
„poniżej średniej” na trzech wariantach `wapno granulowane`, łącznie 236 zł). Wzorzec z Marki: osobne grupy z reklamą dopasowaną do strony.
Propozycja: dwie grupy → karty `…/weglanowe-granulowane/` i `…/weglanowe-magnez-granulowane/`.
**Uczciwie o oczekiwaniach:** w Marce przeniesienie na kartę **nie podniosło** oceny strony docelowej (`bielik wapno` QS 3 → 3),
zysk przyszedł z dopasowania reklamy (IS 46 → 73%, CTR 4,6 → 11,5%). Tu spodziewamy się CTR i udziału, nie oceny strony.
Pilot na jednej grupie, reszta Rolnictwa bez zmian do odczytu.
**Kontrola:** 14 dni — CTR i CPC grupy, ocena strony docelowej, konwersje (dziś 0).

---

## Bez nowego numeru — do istniejących pozycji

- **T-077 „kreda pastewna” (czeka na Pawła):** `kreda pastewna dla kur` (1 600/mies.) → karta #307 ma **1 164 wyśw. na poz. 9,6, 5 kliknięć** —
  największa pojedyncza fraza portfela tuż za pierwszą stroną. Kategoria `/paszarstwo/` trzyma już frazy dawkowe (poz. 3,5–4,6),
  więc proponuję T-077 **bez nowego adresu** (jak T-071): sekcja „Kreda pastewna dla kur niosek — ile i jak podawać” na karcie #307,
  dawki z odpowiedzi Pawła. Tytuł karty zostaje (`…dla kur niosek i bydła…` już zawiera frazę).
- **T-081 „badanie gleby” (31.10):** zakres = pobieranie próbek i odczyt wyniku ze stacji; **nie powtarzać** sekcji „Jak sprawdzić pH” z `/ph-gleby/` (08.10).
- **T-083 „wapno do sadu” (30.11):** to nowy adres — wymaga `[J]` wg reguły architektury z 10.09. Flaga, nie propozycja.
- **Kontrole już w kalendarzu:** 22.10 (staw + kategorie po 08.10) i 09.11 (pH) — T-157…T-160 mierzymy osobno, żeby się nie mieszały.

## Sprawdzone, nie robimy

- **Hub `/wapnowanie-gleby/` — tytuł i opis:** T-053 (21.08) zrobił, T-069 unieważnione. 0,69% przy poz. 5,8 to prawdopodobnie
  przegląd AI / wyróżniony fragment na „ile wapna na hektar” — **niezweryfikowane**, jeden odczyt SERP (DataForSEO, saldo do sprawdzenia) rozstrzygnie.
- **Linki z kalkulatora do kart:** wynik kalkulatora już linkuje produkty (`calculator.js`, `agria-calc__product-link`).
- **`higienizacja osadów ściekowych`** (30/mies., poz. 19,4) i **`cl 90-s`** (0 wyświetleń) — za mały popyt, żeby ruszać treść.
- **Trawnik** (`jakie wapno na trawnik` 140 wyśw., 0 klik.) — nie ten odbiorca (B2B, cały samochód).

## Fakty do D1 (bez rekomendacji)

- `wapno magnezowe` 1 900 i `wapno palone` 2 400 nie mają w serwisie adresu, który Google uznaje za odpowiedź (40 i 54 wyśw.).
- `wapno granulowane` 4 400/mies., a karta #314 ma na tej frazie **31 wyśw. na poz. 2,2** — liczby się nie spinają; przed D1 jeden odczyt SERP.
- Na `wapno nawozowe` strona główna (poz. 6,2) stoi wyżej niż kategoria (9,2).
- **Okno na zmiany adresów (301) to XII–II** — najniższy ruch w roku; D1 z przekierowaniami najtaniej wdrożyć wtedy.

Zauważone obok, nie ruszam: w stopce wszystkich stron literówka „Wyślj wiadomość”.

---

## Wiersze do rejestru (propozycja)

| ID | Zadanie | Zakr. | Kontekst |
|---|---|---|---|
| **T-157** | Tytuł i opis kategorii „Wapno nawozowe” pod `wapno nawozowe` / `wapno rolnicze` | R | 2 619 wyśw., CTR 0,61%; plan `docs/seo/2026-10-08-PLAN-PAZDZIERNIK-LISTOPAD.md` §1 |
| **T-158** | Wapno palone przed szczytem X–XI: tytuł #320 + „palone” na Agrobieliku 70/90 | R | 2 400 (X–XI 3 600) → 54 wyśw.; wchłania T-084 po akcepcie |
| **T-159** | Hub → karta wapna magnezowego granulowanego (H3 dawka 1–6 t/ha) | R | karta poz. 14,4; hub 360 wyśw. na frazach dawkowych Mg |
| **T-160** | Kotwice fraz rodzajowych do zwycięzców (węglanowe, tlenkowe, kreda nawozowa) | R | 3 poradniki, bez nowych sekcji |
| **T-161** | Ads Rolnictwo: wstrzymanie 12 fraz QS ≤ 3 | P | 174,90 zł / 89 klik. / 0 konw. w 30 dni — decyzja Janka |
| **T-162** | Ads Rolnictwo: pilot grupy „Wapno granulowane” na karty #314 / #317 | P | 326,75 zł / 169 klik. / 0 konw. — decyzja Janka |

## Kolejność wdrożenia

13–14.10: T-157, T-158, T-159, T-160 jednym wejściem przez SSH (backup do `~/agria-backups/T-157-160/`), weryfikacja renderem
z cache-bustem, link do akceptu, po akcepcie „Poproś o zindeksowanie” w GSC (Chrome MCP). T-161/T-162 — po decyzji Janka.
Kontrole: **28.10** (14 dni) i **11.11** (28 dni).

---

## Prompt kontynuacyjny

```
Pracujemy w ~/projekty/agria — wątek SEO. Przeczytaj docs/seo/2026-10-08-PLAN-PAZDZIERNIK-LISTOPAD.md
i data/kontrole/2026-10-08-kontrole-zalegle-seo.md.

1. Zapytaj mnie quizem o: akcept T-157…T-160 (teksty z planu), zamknięcie T-084 na rzecz T-158,
   decyzję o T-161 i T-162 (Ads Rolnictwo).
2. Po akcepcie: dopisz T-157…T-162 do docs/REJESTR_ZOBOWIAZAN.md, wdroż T-157…T-160 przez SSH
   (backup → zmiana → render z cache-bustem → link do akceptu → zgłoszenie w GSC przez Chrome MCP).
   Tytuł w Google = rank_math_title, bez kwot. Treść kart tylko opisowa, parametry z kart.
3. Załóż w kalendarzu „Auranet Claude” kontrole 28.10 i 11.11 (T-157…T-160) z baseline'em z planu.
4. Jeśli Paweł odpowiedział w sprawie kredy pastewnej — T-077 bez nowego adresu, sekcja na karcie #307.
```
