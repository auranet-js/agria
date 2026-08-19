# T-008 — 8 nowych atestów i kart charakterystyki Nordkalku na `/do-pobrania/`

| | |
|---|---|
| **Linia / zakres** | Strona · **R** |
| **Status** | 🔴 teraz — 12 dni od zgłoszenia |
| **Zgłosił** | Paweł, 07.08.2026, mail [201] |
| **Szacunek** | 2–3 h |
| **Idzie razem z** | `T-009` (usunięcie sekcji Certyfikaty) — **jedna wizyta na tej samej stronie**, potem `T-027` |

---

## 1. Czego to dotyka

Strona **ID 731** `/do-pobrania/` — `post_content` (36 782 B) **oraz** `_elementor_data` (14 478 B).
Katalog `wp-content/uploads/2026/08/` (upload PDF-ów przez FTP). Biblioteka mediów WP (jeśli
wgrywasz FTP-em, WP ich nie zna — linki muszą być bezpośrednie albo trzeba zarejestrować załączniki).

**Materiały:** 8 PDF-ów leży w `/tmp/claude-mails/201/` — **to `/tmp`, może zniknąć**:
```
Atest_Jażwica.pdf · Atest_Laskowa.pdf · Atest_Winna.pdf
ATEST_wapno_nawozowe_odm._01.pdf · 2025_-_ATEST_wapno_nawozowe_odm._02.pdf
Karta-charakterystyki-CaO_-Sitkowka-2025.pdf   (tlenek wapnia, KCH/1)
Karta-charakterystyki-CaOH2_Sitkowka.pdf       (diwodorotlenek wapnia, KCH/3)
Karta-charakterystyki-CaCO3_kreda-techniczna_ZS-2025.pdf (węglan wapnia, KCH/5)
```
Wszystkie Nordkalk Wapno Sp. z o.o., wydanie 1.1, aktualizacja 26.03.2025.

## 2. Strefy kruche

1. **Pierwszy krok to skopiowanie PDF-ów z `/tmp` do repo** (`assets/` albo `tmp/` projektu).
   Jeśli `/tmp/claude-mails/201/` zostanie wyczyszczone, materiał trzeba odzyskiwać z maila.
2. **Atesty to skany bez warstwy tekstowej** — mapowanie do produktów robisz **wizualnie**,
   otwierając plik, nie po nazwie. „Atest Jażwica" to nazwa kopalni, nie produktu.
3. **Nowe karty Nordkalku mogą zastępować obecne.** Sekcja „Karty charakterystyki" ma dziś
   4 pozycje (tlenek wapnia CL 90-Q, tlenek wapnia Zakład Kujawy, diwodorotlenek CL 90-S,
   wapno nawozowe odm. 03). Sprawdź daty wydań — jeśli nowa zastępuje starą, **stara schodzi**,
   nie dublujesz. Dwie karty tego samego związku z różnych lat to błąd merytoryczny, nie bogactwo.
4. **Treść żyje w dwóch warstwach.** Zweryfikowane 19.08: na ID 731 fraza „ertyfikat" występuje
   i w `post_content`, i w `_elementor_data`. Ta sama strona, dwa źródła. Edytujesz obie albo
   ustalasz, która renderuje — i wtedy druga zostaje jako martwy rozjazd, który wróci przy
   pierwszym otwarciu Elementora przez Pawła.
5. **Nazwy plików idą do URL-i publicznych.** Polskie znaki i spacje w `Atest_Jażwica.pdf`
   dadzą URL-encoded potwory. Przemianuj wg konwencji przed uploadem.
6. **`_elementor_element_cache`** — po zmianie wyczyść na `a:0:{}`. Na ID 731 tej meta dziś
   **nie ma** (sprawdzone 19.08), ale Elementor tworzy ją przy renderze.
7. **Parametry z kart producentów są źródłem prawdy** — jeśli przy okazji zauważysz rozjazd
   między kartą PDF a treścią na stronie, to osobne zgłoszenie, nie poprawka przy okazji.

## 3. Stan zmierzony 19.08.2026

```
Chrome MCP /do-pobrania/:  22 karty produktów + 4 karty charakterystyki + 5 certyfikatów + 1 atest OSChR
grep „Sitkówka" na froncie: 0 wystąpień  →  nowych kart Nordkalku NIE MA
ID 731: post_content 36 782 B, _elementor_data 14 478 B, brak _elementor_element_cache
GSC: ostatni crawl 2026-04-12, werdykt BLOCKED_BY_META_TAG (live ma index, follow)
```

## 4. Warunki wejścia

- [ ] PDF-y skopiowane z `/tmp/claude-mails/201/` do repo.
- [ ] Ustalone mapowanie atest → produkt (wizualnie, z otwartych plików).
- [ ] Ustalone, które stare karty charakterystyki schodzą.
- [ ] `db_export(['posts','postmeta'])` przed edycją ID 731.

## 5. Co robisz

1. `cp -a /tmp/claude-mails/201/*.pdf <repo>/tmp/T-008/` — zabezpieczenie materiału.
2. Otwórz każdy atest, spisz: kopalnia, produkt, data ważności. Zapisz mapowanie w `tmp/T-008/mapowanie.md`.
3. Przemianuj wg konwencji: `atest-<produkt>-<rok>.pdf`, `karta-charakterystyki-<zwiazek>-<rok>.pdf`
   — bez polskich znaków, bez spacji, małe litery.
4. Upload FTP do `agria.pl/wp-content/uploads/2026/08/`, weryfikacja HTTP 200 na każdym URL-u.
5. Ustal warstwę renderującą listę na ID 731 (`post_content` czy `_elementor_data`).
6. Pokaż Jankowi listę pozycji do dodania i do zdjęcia. Po „ok" — zapis z `expect_old_len`.
7. Wyczyść `_elementor_element_cache` (jeśli istnieje) i cache CDN, jeśli `na-ls-cache-enabled` wróci na `on`.
8. **Dopiero po T-009** przechodzisz do T-027 (zgłoszenie do reindeksacji).

## 6. Jak sprawdzasz w trakcie

```bash
# każdy wgrany PDF odpowiada
for f in <lista nowych plików>; do
  printf '%s → %s\n' "$f" "$(curl -s -o /dev/null -w '%{http_code}' "https://agria.pl/wp-content/uploads/2026/08/$f")"
done
```

## 7. Jak testujesz po wdrożeniu

```bash
# 1. karty Nordkalku są na stronie
curl -s https://agria.pl/do-pobrania/ | grep -c -i 'sitkowka\|sitkówka'      # oczekiwane ≥ 3
# 2. żaden link nie prowadzi w pustkę
curl -s https://agria.pl/do-pobrania/ | grep -oP '(?<=href=")[^"]*\.pdf' | sort -u | \
  while read u; do printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' "$u")" "$u"; done | grep -v '^200'
# 3. render, nie baza
Chrome MCP: navigate /do-pobrania/ + get_page_text → policz pozycje w sekcjach
```

## 8. Dowód do rejestru

Liczba wystąpień „Sitkówka" na froncie (dziś 0 → po wdrożeniu ≥3), lista URL-i PDF z kodami 200,
zrzut listy pozycji z `get_page_text`, hash commitu.

## 9. Rollback

`db_export` sprzed edycji → UPDATE `post_content`/`_elementor_data` na ID 731.
PDF-y: usunięcie przez FTP (`-Q "-DELE …"`), sprawdzone 19.08 że działa.

## 10. Rozliczenie

Zakres **R**. Do DZIENNIKA M3 razem z T-009 jako jedna wizyta na stronie 731 — godziny wspólne.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | render `/do-pobrania/` przez Chrome MCP; wszystkie linki PDF → 200 |
| **+72 h** | GSC URL Inspection na `/do-pobrania/` — czy werdykt ruszył z `BLOCKED_BY_META_TAG` (to już zakres T-027) |
| **+7 dni** | czy Elementor nie odtworzył starej listy (porównaj `post_modified`) |
| **+30 dni** | czy Paweł nie przysłał kolejnej partii — wtedy nowy wiersz w rejestrze, nie doklejanie do tego |
