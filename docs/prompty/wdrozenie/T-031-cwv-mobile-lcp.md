# T-031 — Core Web Vitals mobile: LCP

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 📅 wrzesień (M4) — **blokada z T-048 zdjęta 19.08**, pomiar jest |
| **Szacunek** | 4–6 h |

---

## 1. Czego to dotyka

Wydajność strony głównej i kart produktowych na urządzeniach mobilnych: obrazy, CSS/JS Elementora,
czas odpowiedzi serwera, czcionki. Pośrednio: Elementor Pro (generuje ciężki HTML), motyw
`Agria By Auranet`, CDN nazwa.pl, geoblok (działa na cache-miss, dokłada się do TTFB).

## 2. Strefy kruche

1. **LCP 7,4 s przy TBT 30 ms i CLS 0,002** to profil „ciężki zasób, lekki JavaScript".
   Optymalizacja JS nic tu nie da — szukaj obrazu albo bloku renderującego, nie skryptów.
2. **PSI raportuje `server-response-time: 10 ms`, a proxy z Elary zmierzyło TTFB 1,27 s
   przy cache-miss.** Sprzeczność jest pozorna: PSI trafił w cache. **Mierz oba stany** —
   inaczej zoptymalizujesz to, co i tak jest szybkie.
3. **CrUX zwraca „data not found"** — za mały ruch. Nie ma danych polowych, więc pracujesz
   na danych laboratoryjnych i musisz to jasno powiedzieć w raporcie. Nie udawaj, że masz field data.
4. **Elementor renderuje strony 307/310/320 z `_elementor_data`** — optymalizacja obrazów
   przez zmianę `post_content` ich nie dotknie.
5. **Nie instaluj wtyczki cache'ującej ani optymalizacyjnej bez zgody.** Na produkcji klienta,
   na której stoją Elementor Pro, JetSmartFilters i Complianz, wtyczka optymalizacyjna to
   najczęstsza przyczyna „strona nagle wygląda inaczej".
6. **`na-ls-cache-enabled: off`** — cache LiteSpeed nazwa.pl jest dziś wyłączony. Włączenie go
   może być najtańszą poprawą TTFB, ale to zmiana konfiguracji hostingu klienta — decyzja Janka.
7. **HTML strony głównej ma 154 KB** (pomiar 19.08). To dużo dla strony B2B i wskazuje na
   nadmiarowy markup Elementora, a nie na obrazy.

## 3. Stan zmierzony 19.08.2026 (PSI mobile, kwota wróciła)

```
performance score      0,70
LCP                    7,4 s          ← cel < 2,5 s
FCP                    2,7 s
TBT                    30 ms          (dobre)
CLS                    0,002          (bardzo dobre)
server-response-time   10 ms          (trafienie w cache)
runtimeError           None
Proxy z Elary 19.08:   TTFB 1,27 s przy cache-miss, HTML 154 KB
                       karta produktu TTFB 0,35 s
Ostatni pełny pomiar 03.08: LCP 7,4 s — bez zmian
```

## 4. Warunki wejścia

- [ ] `T-048` zamknięty dowodem (jest — pomiar z 19.08).
- [ ] Świeży pomiar PSI z dnia rozpoczęcia pracy (kwota dzienna PSI potrafi się wyczerpać —
      19.08 rano była wyczerpana, po południu wróciła; planuj pomiary, nie strzelaj seriami).

## 5. Co robisz

1. Pomiar bazowy: PSI mobile + desktop dla `/` i dwóch kart produktowych, zapis JSON do `tmp/`.
2. **Zidentyfikuj element LCP** — w audycie `largest-contentful-paint-element`. W pomiarze z 19.08
   ta sekcja była pusta, więc powtórz z pełnym zestawem kategorii, nie tylko `performance`.
3. Rozdziel TTFB: pomiar z cache i bez (`?cb=$(date +%s)`), oba z Elary i przez PSI.
4. Wypisz trzy najcięższe zasoby z `network-requests` i sprawdź, czy element LCP jest wśród nich.
5. Przygotuj listę zmian **uszeregowaną po stosunku zysku do ryzyka**, pokaż Jankowi.
   Typowo: format i wymiary obrazu LCP, `fetchpriority`, preload czcionki, ograniczenie
   nadmiarowego CSS Elementora.
6. Wdrażaj **po jednej zmianie**, mierząc po każdej. Trzy zmiany naraz i spadek LCP o 2 s
   nie mówią, która zadziałała.

## 6. Jak sprawdzasz w trakcie

Po każdej zmianie: PSI mobile na tym samym URL-u + wizualna kontrola strony przez Chrome MCP
(optymalizacja obrazu, która psuje układ, jest regresem, nie postępem).

## 7. Jak testujesz

```bash
KEY=$(cat ~/secrets/google/psi-crux-key.txt)
for u in https://agria.pl/ https://agria.pl/wapno-nawozowe-rolnictwo/agrobielik-70/; do
  curl -s "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1],safe=''))" "$u")&strategy=mobile&category=performance&key=$KEY" \
   | python3 -c "import json,sys;d=json.load(sys.stdin)['lighthouseResult'];print(d['requestedUrl'],d['categories']['performance']['score'],d['audits']['largest-contentful-paint']['displayValue'])"
done
```
Cel etapowy: LCP poniżej 4 s. Cel docelowy: poniżej 2,5 s. Jeśli po wyczerpaniu tanich zmian
LCP stoi, wnioskiem jest „potrzebna przebudowa szablonu / zmiana hostingu", a nie kolejne mikrooptymalizacje.

## 8. Dowód do rejestru

Tabela pomiarów przed/po dla każdej wdrożonej zmiany, z datą i URL-em. Bez tabeli nie ma domknięcia —
„przyspieszyliśmy stronę" bez liczb jest w tym projekcie nieprzyjmowane.

## 9. Rollback

`backup_file` przed każdą zmianą w motywie/wtyczce, `db_export` przed zmianami w `_elementor_data`.
Każda zmiana odwracalna osobno — to jest powód, dla którego idą pojedynczo.

## 10. Rozliczenie

Zakres **R**. Wrzesień (M4), 4–6 h. Jeśli wniosek będzie „potrzebna przebudowa szablonu" —
to osobna pozycja handlowa, nie ryczałt.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **po każdej zmianie** | PSI mobile, ten sam URL |
| **+30 dni** | CrUX — czy przy większym ruchu pojawiły się dane polowe |
| **+30 dni** | GSC raport Core Web Vitals — czy adresy wychodzą ze „słabych" |
| **przy każdej aktualizacji Elementora** | ponowny pomiar; Elementor potrafi cofnąć zysk jedną wersją |
