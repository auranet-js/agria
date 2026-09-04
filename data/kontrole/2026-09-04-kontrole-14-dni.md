# Punkt kontrolny 04.09.2026 — dwie kontrole 14-dniowe

## A. T-053 — CTR huba `/wapnowanie-gleby/` po zmianie meta

**Data pomiaru:** 2026-09-04 · **Zmiana meta:** 21.08.2026 · **Źródło:** GSC Search Analytics API
(`dataState: final`) + URL Inspection API. CTR liczony **z poziomu strony** (filtr `page`), nie z sumy
zapytań — memory `feedback_gsc_ctr_z_poziomu_strony`.

### Warunki pomiaru

- **Dane GSC dojrzały do 01.09** — okna „14 dni" (do 03.09) i „13 dni" (do 02.09) zwracają identyczne
  liczby co 12 dni do 01.09. Porównanie robione więc na **równych oknach 12-dniowych**, nie na
  nominalnych 14 dniach.
- **Meta żyje na produkcji** (curl z cache-bustem 04.09):
  `<title>Ile wapna na hektar? Tabela dawek i kalkulator | AGRIA</title>` + description z tabelą dawek.
- **Google widział nową wersję** — URL Inspection 04.09: `PASS`, „Strona przesłana i zindeksowana",
  `lastCrawlTime 2026-09-01T00:42:54Z`, canonical zgodny. Strona jest crawlowana na bieżąco,
  więc nowa meta była w indeksie przez praktycznie całe okno pomiarowe.

### Wynik — strona

| Okno | Wyświetlenia | Kliknięcia | CTR | Pozycja |
|---|---|---|---|---|
| przed, 09–20.08 (12 dni) | 8 918 | **49** | 0,55% (±0,15 pp) | 6,16 |
| po, 21.08–01.09 (12 dni) | 8 086 | **49** | 0,61% (±0,17 pp) | 5,48 |

Różnica CTR: **+0,057 pp**, przedział ufności 95%: **−0,17 … +0,28 pp** — obejmuje zero.

### Tło — cały serwis, te same okna

| Okno | Wyświetlenia | Kliknięcia | CTR | Pozycja |
|---|---|---|---|---|
| przed | 11 879 | 141 | 1,19% | 6,91 |
| po | 11 953 | 141 | 1,18% | 6,99 |

Serwis stoi w miejscu, więc ruch huba (−9,3% wyświetleń) to zjawisko lokalne, nie trend całości.

### Werdykt

**Brak mierzalnego efektu.** Liczba kliknięć jest identyczna (49 → 49), a wzrost CTR mieści się
w szumie. Co więcej, w tym samym oknie **pozycja poprawiła się o 0,68** (6,16 → 5,48) — sama ta
poprawa powinna podnieść CTR niezależnie od treści meta. Skoro przy lepszej pozycji liczba kliknięć
nie drgnęła, hipoteza „przepisany title i description odblokują kliknięcia" **nie potwierdza się**.

### Obserwacja poza zakresem zadania

**CTR 0,61% przy pozycji 5,5 jest anomalnie niski** — dla tej pozycji typowy zakres to kilka procent.
Ta sama anomalia widoczna jest w rozbiciu na frazy: `ile wapna na hektar` 402 wyświetlenia i 2
kliknięcia przy pozycji 5,2, `ile wapna granulowanego na hektar` 444 / 3 przy 6,5. To wygląda na
zapytania, w których odpowiedź zapada w samym SERP (AI Overview / featured snippet), a nie na problem
z brzmieniem meta. **Nie weryfikowane** — wymagałoby odczytu SERP dla klastra dawkowego.
Zgłoszone, nie wykonane.

---

## B. Nazwy kategorii bez członu segmentowego `[J 21.08]` — pozycja na `wapno nawozowe`

Druga kontrola zaplanowana na ten sam dzień (dziennik M3). Zmiana z 21.08: `wpfz_terms.name` 764
„Rolnictwo - wapno nawozowe" → **„Wapno nawozowe"**, czyli H1 kategorii dopasowany do frazy.
Dowodem miała być pozycja w GSC po 14 dniach. Te same równe okna 12-dniowe co w sekcji A.

### Strona `/wapno-nawozowe-rolnictwo/`

| Okno | Wyświetlenia | Kliknięcia | CTR | Pozycja |
|---|---|---|---|---|
| przed, 09–20.08 | 392 | 3 | 0,77% | 8,37 |
| po, 21.08–01.09 | 421 | 2 | 0,48% | 9,11 |

### Fraza `wapno nawozowe` na tym adresie

| Okno | Wyświetlenia | Kliknięcia | Pozycja |
|---|---|---|---|
| przed, 09–20.08 | 19 | 0 | 10,37 |
| po, 21.08–01.09 | **114** | 0 | **11,23** |

### Werdykt

**Dopasowanie H1 do frazy nie przesunęło strony do TOP10** — pozycja stoi na drugiej stronie wyników
i nawet lekko się cofnęła (10,37 → 11,23). Wyświetlenia na frazę wzrosły sześciokrotnie (19 → 114),
ale to najpewniej **sezon**, nie efekt zmiany: `wapno nawozowe` ma szczyt VIII–X (1 900 wobec średniej
1 300), a większy wolumen z natury ciągnie średnią pozycję w dół, bo dokłada zapytania z dalszych
miejsc. ⚠️ Okno „przed" ma tylko **19 wyświetleń** — pozycja z takiej próbki jest chwiejna i sama
w sobie nie unosi wniosku o kierunku zmiany.

**Zero kliknięć w obu oknach.** Wniosek operacyjny: sama nazwa nie wystarczy, adres potrzebuje treści —
i to jest dokładnie **T-092** (opis kategorii, termin 05.09), następna pozycja w kolejce.
Kontrola nie zmienia planu, potwierdza go.
