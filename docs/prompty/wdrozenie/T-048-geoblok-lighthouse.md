# T-048 — geoblok odcinał Lighthouse/PSI: kod poprawiony, dowód do dopięcia

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 🔴 teraz — **kod wdrożony 19.08 13:14, pomiar wykonany 19.08 15:02, zostało wpisanie dowodu** |
| **Odblokowuje** | `T-031` (CWV mobile — LCP) |
| **Szacunek** | 20 min |

---

## 1. Czego to dotyka

Plik `wp-content/plugins/agria-by-auranet/security-geoblock.php` na produkcji (kopia referencyjna
w `src/plugins/agria-by-auranet/`, commit `34cd965`). Pośrednio: **każdy pomiar wydajności**
(PSI, Lighthouse, CrUX), weryfikacja landingów przez AdsBota, dostępność strony dla botów AI.

## 2. Strefy kruche

1. **Geoblok jest w trybie ENFORCE** (`$enforce = true`) — realny 403 dla ruchu spoza Europy.
   Każda zmiana w liście `$good_bots` natychmiast wpływa na to, kto widzi stronę.
2. **`AdsBot-Google` musi zostać na liście.** Bez dostępu do landingów Google **odrzuca reklamy** —
   przy żywej kampanii to natychmiastowy koszt.
3. **Fail-open**: brak bazy GeoLite2, błąd czytnika albo nieznany kraj → przepuszcza. To znaczy,
   że test „nie dostałem 403" **nie dowodzi**, że reguła bota zadziałała — mógł zadziałać fail-open.
   Dowodem jest pełny wynik Lighthouse bez `runtimeError`.
4. **Baza GeoLite2 należy do Complianz** (`uploads/complianz/maxmind/GeoLite2-Country.mmdb`).
   Odinstalowanie albo przekonfigurowanie Complianz (**patrz T-033**) może wyjąć bazę spod geobloku.
   Te dwa taski trzeba czytać razem.
5. **Zasięg tylko na cache-miss.** Strony z edge cache CDN nie docierają do PHP — geoblok się
   tam nie odpala. Nie zakładaj, że blok jest szczelny.
6. **Kill-switch**: `define('AGRIA_GEOBLOCK_OFF', true)` w `wp-config.php`. `wp-config.php` jest
   **zablokowany dla MCP `write_file`** — edycja tylko przez FTP lub SSH.

## 3. Stan zmierzony 19.08.2026

Kod na produkcji (`grep` na żywym pliku) zawiera w `$good_bots`:
`Chrome-Lighthouse`, `Google-PageSpeed`, `GoogleOther` — obok `Googlebot`, `AdsBot-Google`,
`Storebot-Google`, `Google-InspectionTool`, botów Bing/DDG/Apple/Yandex i klasy LLM
(GPTBot, ClaudeBot, PerplexityBot). Backup: `security-geoblock.php.bak-2026-08-19`.

**Pomiar PSI z 19.08 15:02 (kwota już wróciła):**
```
performance score:        0,70
LCP (mobile):             7,4 s
FCP:                      2,7 s
TBT:                      30 ms
CLS:                      0,002
server-response-time:     10 ms
runtimeError:             None        ← Lighthouse wyrenderował stronę, 403 nie było
finalUrl:                 https://agria.pl/
userAgent:                HeadlessChrome/151
```

To jest dowód, którego brakowało 19.08 rano. **Task jest gotowy do zamknięcia** — zostało wpisanie
tego wyniku do wiersza rejestru i przeniesienie pozycji do DZIENNIKA M3.

## 4. Warunki wejścia

- [ ] Powtórzyć pomiar w dniu domykania (wynik powyżej jest z 19.08 — jeśli domykasz później,
      zrób świeży, bo dowód ma być z dnia zamknięcia).

## 5. Co robisz

```bash
# 1. świeży pomiar
KEY=$(cat ~/secrets/google/psi-crux-key.txt)
curl -s "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2Fagria.pl%2F&strategy=mobile&category=performance&key=$KEY" -o tmp/psi-$(date +%F).json
python3 -c "import json;d=json.load(open('tmp/psi-$(date +%F).json'));lr=d['lighthouseResult'];print('score',lr['categories']['performance']['score'],'runtimeError',lr.get('runtimeError'));print({k:lr['audits'][k]['displayValue'] for k in ['largest-contentful-paint','first-contentful-paint','total-blocking-time','cumulative-layout-shift']})"
# 2. kontrola, że good_bots stoi na produkcji
ssh agria-prod "grep -n 'Chrome-Lighthouse\|AdsBot-Google' \$HOME/agria.pl/wp-content/plugins/agria-by-auranet/security-geoblock.php"
# 3. kontrola, że zwykły ruch europejski nadal przechodzi
curl -sI https://agria.pl/ | head -1
```

## 6. Jak testujesz

Trzy odpowiedzi muszą paść naraz: `runtimeError: None`, wynik score liczbowy (nie `null`),
`AdsBot-Google` obecny w pliku. Jeśli którakolwiek nie — nie zamykasz.

## 7. Dowód do rejestru

Wklejasz blok z sekcji 3 (score, LCP, `runtimeError: None`, `fetchTime`) + numer commitu `34cd965`
+ nazwę backupu. Potem: wiersz z KOLEJKI → DZIENNIK M3, `T-031` traci blokadę.

## 8. Rollback

Backup `security-geoblock.php.bak-2026-08-19` przez SSH. Awaryjnie — kill-switch w `wp-config.php`
(FTP, nie MCP).

## 9. Rozliczenie

Zakres **R**. W DZIENNIKU M3 geoblok już figuruje jako dostarczony 14.08 ze znacznikiem
„skutek uboczny: T-048" — domknięcie T-048 dopisuje do tego wiersza dowód pomiaru, nie tworzy
nowej pozycji rozliczeniowej.

## 10. Recheck

| Kiedy | Co |
|---|---|
| **+7 dni** | PSI ponownie — czy geoblok nie wrócił do blokowania po aktualizacji wtyczki/Complianz |
| **+7 dni** | Ads: czy żadna reklama nie ma statusu odrzucenia z powodu strony docelowej |
| **przy każdej zmianie Complianz** | sprawdzić, czy `GeoLite2-Country.mmdb` nadal jest na miejscu (T-033) |
