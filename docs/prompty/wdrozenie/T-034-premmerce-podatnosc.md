# T-034 — Premmerce Permalink Manager: podatność DOM-XSS

| | |
|---|---|
| **Linia / zakres** | Bezpieczeństwo · **R** |
| **Status** | 🔵 do rozstrzygnięcia — **w dużej mierze już rozstrzygnięte, patrz §3** |
| **Szacunek** | 1 h |

---

## 1. Czego to dotyka

Wtyczka `woo-permalink-manager` (Premmerce Permalink Manager for WooCommerce) **2.3.13**,
odpowiedzialna za całą strukturę URL-i produktów i kategorii. Pośrednio: `T-028` i `T-032`
(stare bazy URL), bo to ona buduje ścieżki.

## 2. Strefy kruche

1. **Ta wtyczka trzyma strukturę URL całego sklepu.** Deaktywacja albo podmiana = wszystkie
   adresy produktów zmieniają się w jednej chwili, a mamy je zaindeksowane i wpięte w kampanie Ads.
   **Nigdy nie deaktywuj „na próbę".**
2. **Wtyczki nie ma w repozytorium wp.org** (jest przez Freemius), więc aktualizacja idzie inną
   ścieżką niż zwykłe wtyczki. Sprawdź, czy licencja jest aktywna, zanim zaplanujesz update.
3. **Aktualizacja tej wtyczki to operacja wysokiego ryzyka** — zrób ją na kopii albo w oknie
   niskiego ruchu, z gotowym rollbackiem i z listą URL-i do sprawdzenia po.
4. **Rejestr mówi „DOM-XSS", changelog mówi „Local file inclusion".** To mogą być dwie różne
   podatności. Zanim uznasz sprawę za zamkniętą, ustal, o której mowa.

## 3. Stan zmierzony 19.08.2026

Rejestr zakładał, że „changelogu nie da się sprawdzić publicznie". **Da się — leży na serwerze:**
`wp-content/plugins/woo-permalink-manager/readme.txt`, sekcja `== Changelog ==`:

```
= 2.3.13 (12th May 2026) =
  * Security: Freemius SDK updated to 2.13.1
  * Fix: Updated WordPress tested up to version
= 2.3.11 (21st February 2024) =
  * Security: Local file inclusion vulnerability fix (Thanks to Rafie Muhammad - Patchstack)
= 2.3.10 … 2.3.7 …
```

Wniosek: **2.3.11 to wersja z poprawką**, nie wersja podatna. Zainstalowana **2.3.13 jest nowsza**,
zawiera ten fix plus aktualizację Freemius SDK do 2.13.1 (Freemius miał własne CVE — ta pozycja
też jest domknięta).

**Zostaje do sprawdzenia jedno:** czy „DOM-XSS" z zapisu w rejestrze to ta sama sprawa co LFI
z changelogu, czy osobna podatność, która nie ma wpisu w changelogu.

## 4. Warunki wejścia

Brak — to weryfikacja, nie zmiana.

## 5. Co robisz

1. Ustal źródło zapisu „DOM-XSS" w naszych dokumentach — audyt z czerwca, `grep` po `docs/audits/`.
   Jeśli źródłem był wpis Patchstack/WPScan, sprawdź numer CVE i wersję naprawioną.
2. Zestaw z changelogiem z serwera (sekcja 3).
3. Jeśli to ta sama podatność → zamknij wiersz z dowodem: cytat z changelogu + wersja zainstalowana.
4. Jeśli osobna i niezałatana → sprawdź, czy vendor wydał nowszą wersję; ustal ścieżkę
   aktualizacji przez Freemius; **zaplanuj ją jako osobną operację**, nie zrób od ręki.
5. Przy okazji sprawdź pozostałe wtyczki pod kątem wersji z podatnościami — bez instalowania
   niczego, sam przegląd:
   ```
   Elementor 3.35.9 · Elementor Pro 3.35.1 · WooCommerce 10.9.3 · Rank Math 1.0.264.1
   Rank Math PRO 3.0.107 · JetSmartFilters 3.7.5 · Complianz premium 7.5.7.2
   UpdraftPlus 1.26.2 · Orphans 3.4.4
   ```

## 6. Jak sprawdzasz

Numer CVE + wersja naprawiona wg vendora zestawione z wersją na produkcji. Bez CVE
albo bez wersji naprawionej — nie masz rozstrzygnięcia, masz przypuszczenie.

## 7. Jak testujesz

Jeśli dojdzie do aktualizacji:
```bash
# przed
ssh agria-prod "wp --path=\$HOME/agria.pl plugin list --format=csv" > tmp/plugins-przed.csv
curl -s https://agria.pl/product-sitemap.xml | grep -oP '(?<=<loc>)[^<]+' > tmp/urls-przed.txt
# po aktualizacji — te same URL-e muszą odpowiadać 200
while read u; do printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' "$u")" "$u"; done < tmp/urls-przed.txt | grep -v '^200'
```
Pusty wynik = struktura URL nietknięta.

## 8. Dowód do rejestru

Cytat z changelogu z serwera + wersja zainstalowana + numer CVE, jeśli ustalony.
Jeśli rozstrzygnięcie brzmi „nie dotyczy naszej wersji" — to jest domknięcie z dowodem, nie odpuszczenie.

## 9. Rollback

Przy aktualizacji: kopia katalogu wtyczki przez SSH przed operacją, plus `tmp/urls-przed.txt`
jako lista kontrolna.

## 10. Rozliczenie

Zakres **R**, ~1 h. Weryfikacja bez zmiany też idzie do dziennika — to jest praca,
która zdejmuje pozycję z listy ryzyk.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+30 dni** | przegląd wersji wtyczek pod kątem nowych CVE |
| **przy każdej aktualizacji Premmerce** | pełna lista URL-i produktów przed i po |
