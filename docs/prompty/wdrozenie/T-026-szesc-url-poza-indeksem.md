# T-026 — sześć URL-i poza indeksem mimo trzech zgłoszeń do Indexing API

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 🔴 teraz — **zadanie diagnostyczne, nie wykonawcze** |
| **Szacunek** | 2–3 h diagnozy, działanie zależne od wyniku |

---

## 1. Czego to dotyka

Sześć adresów treściowych + całą hipotezę o tym, dlaczego treść z lipca nie wchodzi do indeksu.
Pośrednio: geoblok (od 14.08), sitemapy RankMath, linkowanie wewnętrzne z huba `/wapnowanie-gleby/`,
budżet crawlowy witryny.

## 2. Strefy kruche

1. **Nie strzelaj czwarty raz do Indexing API.** Trzy zgłoszenia nie pomogły — czwarte tym bardziej
   nie pomoże, a zabierze z puli, którą dzielą wszystkie projekty. **Najpierw przyczyna, potem
   ewentualne zgłoszenie.**
2. **Rejestr ma przypisanie odwrotne niż stan faktyczny.** Zmierzone 19.08:
   `/kreda-malarska/` jest „Discovered", nie „unknown"; `/wapno-nawozowe-na-trawnik/` jest „unknown",
   nie „Discovered". Popraw to w rejestrze przy okazji — inaczej diagnoza rusza z błędnego założenia.
3. **„URL is unknown to Google" przy stronie, która jest w sitemapie i jest linkowana z huba,
   to sygnał sprzeczny.** Zweryfikowane 19.08: cztery z tych adresów **są** w `post-sitemap.xml`
   i **są** linkowane z `/wapnowanie-gleby/`. To zawęża pole do: budżet crawlowy, jakość/duplikacja
   treści, albo blokada po stronie serwera przy crawlu z adresów Google.
4. **Geoblok jest podejrzanym, ale niedowiedzionym.** Wdrożony 14.08, a problem trwa od lipca —
   więc nie jest przyczyną pierwotną. Może jednak **przedłużać** stan. Sprawdź `curl -A "Googlebot"`
   **z adresu spoza Europy**, jeśli masz jak; z Elary tego nie udowodnisz, bo jesteśmy w PL i wpadamy
   w regułę geograficzną, nie w regułę bota.
5. **`/kreda-malarska/` nie jest w żadnej sitemapie** (sprawdzone 19.08 — brak w `post-` i `page-sitemap`;
   występuje jako **kategoria** w `product_cat-sitemap.xml`). To osobna przyczyna niż pozostałe pięć.
6. **Nie dopisuj do sitemapy ręcznie** — RankMath generuje pliki, a jego cache siedzi
   w `uploads/rank-math/*.xml`. Zmiana idzie przez ustawienia typu zawartości, nie przez plik.

## 3. Stan zmierzony 19.08.2026 (GSC URL Inspection)

| URL | coverageState | w sitemapie | linkowany z huba |
|---|---|---|---|
| `/ile-wapna-granulowanego-na-ha/` | URL is unknown to Google | `post-sitemap` ✅ | ✅ |
| `/jak-stosowac-wapno-nawozowe/` | URL is unknown to Google | `post-sitemap` ✅ | ✅ |
| `/higienizacja-osadow-sciekowych-wapnem/` | URL is unknown to Google | `post-sitemap` ✅ | ✅ |
| `/wapno-nawozowe-na-trawnik/` | URL is unknown to Google | `post-sitemap` ✅ | ✅ |
| `/kreda-malarska/` | Discovered – currently not indexed | ❌ **brak** | ❌ |
| `/wapno-do-stabilizacji-gruntow/` | Discovered – currently not indexed | `page-sitemap` ✅ | ❌ |

Wszystkie: `lastCrawlTime: None`, `pageFetchState: UNSPECIFIED` — **Google ich nigdy nie pobrał**.
Reszta portfela: 11 URL-i PASS ze świeżym crawlem.

## 4. Warunki wejścia

Brak — to diagnoza, zaczyna się od odczytu.

## 5. Co robisz — kolejność hipotez od najtańszej

1. **Sitemapa faktycznie zgłoszona?** GSC Sitemaps API: kiedy Google ostatnio pobrał
   `sitemap_index.xml`, ile URL-i odczytał, ile błędów.
2. **Odpowiedź serwera dla Googlebota:**
   ```bash
   for u in /ile-wapna-granulowanego-na-ha/ /jak-stosowac-wapno-nawozowe/; do
     curl -s -o /dev/null -w "%{http_code} $u\n" -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "https://agria.pl$u"
   done
   ```
3. **Test renderowania w GSC** (Live Test przez URL Inspection API z `inspectionUrl` + `LIVE`) —
   czy Google widzi treść, czy pustą stronę.
4. **Duplikacja treści** — czy te poradniki nie powielają huba `/wapnowanie-gleby/`, który rankuje
   („ile wapna na hektar", pozycja 8,8, 1 005 wyświetleń). Google może je pomijać jako redundantne.
   To jest **najbardziej prawdopodobna hipoteza dla czterech poradników** i zgadza się z ADR-em
   o kanibalizacji z 11.08.
5. **`/kreda-malarska/`** — osobno: brak w sitemapie treściowej. Ustal, czy to strona, czy tylko
   kategoria produktowa, i czy w ogóle ma istnieć jako oddzielny URL.
6. **Dopiero po rozpoznaniu przyczyny** proponujesz działanie Jankowi. Możliwe wyniki:
   scalenie treści, przepisanie pod inną intencję, wzmocnienie linkowania, albo świadome
   odpuszczenie i przeniesienie do „Unieważnione".

## 6. Jak sprawdzasz w trakcie

Każda hipoteza kończy się liczbą albo werdyktem, nie wrażeniem. Zapisujesz je w `tmp/T-026-diagnoza.md`
w formie: hipoteza → komenda → wynik → wniosek.

## 7. Jak testujesz — po ewentualnym działaniu

```bash
python3 scripts/gsc_inspect.py           # werdykty dla wszystkich sześciu
# sukces = coverageState inne niż „unknown"/„Discovered" i lastCrawlTime niepuste
```

## 8. Dowód do rejestru

**Dla tego taska dowodem jest diagnoza, nie zmiana.** Wklejasz: tabelę hipotez z wynikami,
wskazaną przyczynę, decyzję Janka co dalej. Jeśli decyzja to „odpuszczamy" — wiersz idzie do
„Unieważnione" z uzasadnieniem, i to jest domknięcie.

## 9. Rollback

Zależny od podjętego działania. Diagnoza sama w sobie nic nie zmienia.

## 10. Rozliczenie

Zakres **R**, 2–3 h diagnozy. DZIENNIK M3 z adnotacją, czy skończyło się działaniem.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+14 dni** | `gsc_inspect.py` — czy którykolwiek werdykt drgnął bez naszej ingerencji |
| **+30 dni** | jeśli było działanie: pełny recheck sześciu URL-i |
| **przy każdej nowej treści** | sprawdzić po 14 dniach, czy nowy URL nie wpada w ten sam stan — to jest test, czy przyczynę faktycznie usunęliśmy |
