# 2026-10-08 — treści października: staw, pH, menu i H1 kategorii

## Co zrobione (wszystko na produkcji, zweryfikowane renderem, zgłoszone w GSC)

| Zadanie | Wynik |
|---|---|
| T-071 „kreda do stawu” | **Bez nowego adresu** — kreda dopisana na `/wapno-do-stawu/` (3 × H2, tabela „ile kredy na ar i worki”, 3 FAQ z PAA), tytuł bez ceny, w ramce tylko „od 125 zł/t”, zdjęcie webp 2846 |
| T-070 „wpis o stawach karpiowych” | Wpis 2079: `rank_math_canonical_url` → `/wapno-do-stawu/` (0 wyświetleń w 90 dni, dublował stronę stawową), zdjęcie 2847 |
| T-080 „poradnik pH gleby” | **Nowy adres `/ph-gleby/`** `[J 08.10]`, wpis 2850, źródła wyłącznie IUNG-PIB + karty AGRII; hub 2074 skrócony do jednego akapitu z linkiem |
| Menu bez branż (domknięcie decyzji 21.08) | „Wapno i kreda do stawów”, „Wapno do oczyszczalni”, „Wapno budowlane”, „Kreda pastewna” (menu 811 i 818) |
| H1 kategorii | 767 → „Wapno do oczyszczalni”, 768 → „Wapno budowlane” (`$wpdb`, nie `wp term update`); 770 Paszarstwo zostaje do D1 |
| `/wapno-do-oczyszczalni/` | H2 „Wapnowanie osadów ściekowych — wapno palone czy hydratyzowane”, „oczyszczalni ścieków” w 3 miejscach treści, tytuł bez „(higienizacja)” |
| Kalendarz | 10 nieaktualnych przypomnień odhaczonych (✅ + Szałwia); kontrole **22.10** i **09.11** (staw + kategorie, osobno pH) |

## Wnioski (warte pamiętania)

- **Kanibalizację sprawdzaj w GSC przed pisaniem** (`scripts/gsc_fraza.py`): przy stawie i kredzie pastewnej istniejące strony już łapały frazy planowanych poradników — nowy adres byłby trzecim własnym URL-em.
- **Oczyszczalnie: Google sam podzielił role** po 21.09 — „higienizacja” → poradnik, „wapnowanie osadów” → kategoria (poz. 9,4). Nie ciągnąć kategorii w „higienizację”.
- **Na agria.pl obrazy tylko webp** (precedens 23.09) — JPG z 2844/2845 wgrany omyłkowo, nieużywany, do usunięcia na „ok” Janka.
- **Pełne czyszczenie cache WP Rocket** (menu jest na każdej stronie) — po nim sprawdzić 4 arkusze na stronie głównej (incydent 05.10); 08.10 trzy razy OK.
- **SSH na nazwa.pl zrywa połączenia** — ponawiać; `scp` z wieloma plikami potrafi przejść dopiero za którymś razem.

## Otwarte

- **T-077 „kreda pastewna”** — czeka na **Pawła** (pytania wysłane Jankowi na Telegram 08.10): skąd „1–2 kg / 100 kg paszy” w katalogu AGRII (producenci Lhoist Bukowa i Celiny dawek nie podają), dawki dla niosek / krów / świń, frakcja kury vs bydło. Konkurencja podaje 3–10% paszy — sprzeczne z naszą kartą, nie przepisywać. Razem z dawkami: zdanie o **odbiorze w Niedomicach i Radgoszczy, także pojedynczy worek 30 kg** (`[J 08.10]`: „jak ktoś przyjedzie, sprzedadzą”) i **ujednolicenie magazynów** (wszystkie cztery: Bukowa, Celiny, Niedomice, Radgoszcz — karta podaje dwa pierwsze, kategoria dwa ostatnie). Materiał: `data/T-077/`.
- Waga big-bagu kredy granulowanej: karta 500 kg vs cennik Pawła „od 1 t” — na stronie bez wagi.
- Linki z kart kredy granulowanej i sypkiej do `/wapno-do-stawu/` — propozycja bez decyzji.
- T-081 „badanie gleby” (31.10) — nieruszone; nie dublować sekcji „Jak sprawdzić pH” z `/ph-gleby/`.

## Prompt kontynuacyjny

```
Pracujemy w ~/projekty/agria. Przeczytaj docs/sesje/2026-10-08-tresci-pazdziernik-staw-ph-menu.md
i docs/przypomnienia/2026-10-07-recheck-olx-audyt.md.

1. NAJPILNIEJSZE — kontrola OLX po audycie (zaległa od 07.10): T-144 „przełożenie 29 martwych”,
   T-146 „8× Mg granul. → węgl. granul.”, 17 „do stawu” po zmianie tytułu. Pomiar statystyki.py + grupy,
   raport docs/raporty/2026-09-OLX_AUDYT.md jako punkt odniesienia. Pakiet wygasa 16.10 11:19, AGRIA
   decyduje do 10.10 — wynik z liczbami dla Pawła (przez Janka). Po wykonaniu odhacz event 07.10 w kalendarzu.
2. Zaległe kontrole SEO jednym odczytem (plik w data/kontrole/): T-078 /paszarstwo/ (26.09),
   przebudowa kampanii Marka (02.10), T-092 po 30 dniach (04.10), T-085 + T-093 (05.10).
   Odhacz ich eventy w kalendarzu.
3. Wizytówka Tarnów: posty 16/23/30.09 nie wyszły — 4 tematy na październik i powrót do wtorków.
Jeśli przyszła odpowiedź Pawła o kredzie pastewnej — T-077 według sekcji „Otwarte” w pliku sesji.
```
