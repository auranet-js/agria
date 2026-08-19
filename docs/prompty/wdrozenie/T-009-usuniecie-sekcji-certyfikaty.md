# T-009 — usunięcie sekcji „Certyfikaty" z `/do-pobrania/`

| | |
|---|---|
| **Linia / zakres** | Strona · **R** |
| **Status** | 🔴 teraz — 12 dni |
| **Zgłosił** | Paweł, 07.08.2026: *„proszę również usunąć wszystkie certyfikaty — na ten moment nie są potrzebne, a część z nich jest już nieaktualna"* |
| **Szacunek** | 1 h (przy okazji T-008) |

---

## 1. Czego to dotyka

Ta sama strona **ID 731**, te same dwie warstwy (`post_content` + `_elementor_data`).
Znika **cała sekcja razem z nagłówkiem** — nie zostawiasz pustej listy ani osieroconego H2.

**Pozycje do usunięcia (stan 19.08, odczyt przez Chrome MCP):**
```
Certyfikat Zgodności WE – Cement portlandzki CEM I 32,5 R (Ożarów)
Certyfikat Zgodności WE – Cement popiołowy CEM II/B-V 32,5 R (Ożarów)
Certyfikat Zgodności WE – Cement popiołowy CEM II/A-V 42,5 R (Ożarów)
Certyfikat Zgodności WE – Cement wieloskładnikowy CEM II/B-M (V-LL) 32,5 R (Dyckerhoff)
Certyfikat ISO 9001:2000 – Kopalnia Wapienia Morawica
```

## 2. Strefy kruche

1. **„Atest OSChR – Wapno nawozowe (odmiana 01)" NIE jest certyfikatem** i **zostaje**.
   Leży w liście tuż pod certyfikatami — łatwo go zmieść razem z nimi. To atest, dowód
   parametrów produktu, na którym opieramy deklarację „Agrobielik 90 = 90 % CaO".
2. **Cztery karty charakterystyki też zostają.** Usuwasz sekcję „Certyfikaty", nie wszystko,
   co nie jest kartą produktu.
3. **Literówki „ertyfikat"** — w treści są uszkodzone wystąpienia (brakująca pierwsza litera).
   `grep -c 'certyfikat'` je **przegapi**. Licz po `ertyfikat`.
4. **Duplikat linku** — pozycja 1 i 2 wskazują ten sam plik. Usunięcie sekcji zamyka to przy okazji;
   nie rób z tego osobnego zadania.
5. **Dwie warstwy.** Zweryfikowane 19.08: `ertyfikat` występuje **i** w `post_content`, **i**
   w `_elementor_data`. Usunięcie z jednej zostawia treść w drugiej — i ona wróci.
6. **PDF-y certyfikatów w `uploads/` zostają na dysku.** Usuwasz odnośniki ze strony, nie pliki —
   ich adresy mogą być gdzieś zalinkowane. Kasowanie plików to osobna decyzja Pawła.

## 3. Stan zmierzony 19.08.2026

```
front /do-pobrania/: 7 wystąpień „certyfikat"  (sekcja stoi)
post_content ID 731: zawiera „ertyfikat"       → TAK
_elementor_data ID 731: zawiera „ertyfikat"    → TAK
```

## 4. Warunki wejścia

- [ ] `db_export` zrobiony (wspólny z T-008).
- [ ] Zgoda Janka na zapis do ID 731.

## 5. Co robisz

1. Wypisz dokładnie, co znika i co zostaje — pokaż Jankowi listę, nie opis.
2. Usuń sekcję z warstwy renderującej **i** z drugiej warstwy, w jednej operacji na warstwę,
   z `expect_old_len`.
3. Sprawdź, że nagłówek sekcji też zniknął (nie została pusta ramka Elementora).
4. Wyczyść cache Elementora, jeśli meta się pojawiła.

## 6. Jak sprawdzasz w trakcie

```bash
curl -s https://agria.pl/do-pobrania/ | grep -c 'ertyfikat'    # cel: 0
curl -s https://agria.pl/do-pobrania/ | grep -c 'Atest OSChR'  # cel: 1 — nie zmieciony
```

## 7. Jak testujesz po wdrożeniu

```bash
# 1. sekcji nie ma w żadnej postaci
curl -s https://agria.pl/do-pobrania/ | grep -i -c 'ertyfikat\|CEM I\|Dyckerhoff\|ISO 9001'   # 0
# 2. atest i karty charakterystyki nietknięte
curl -s https://agria.pl/do-pobrania/ | grep -c 'Karta charakterystyki'   # ≥ 4
curl -s https://agria.pl/do-pobrania/ | grep -c 'Atest OSChR'             # 1
# 3. baza czysta w obu warstwach (MCP query_db)
SELECT (post_content LIKE '%ertyfikat%') , (SELECT meta_value LIKE '%ertyfikat%' FROM {prefix}postmeta WHERE post_id=731 AND meta_key='_elementor_data') FROM {prefix}posts WHERE ID=731
# 4. render bez pustej ramki — Chrome MCP get_page_text
```

## 8. Dowód do rejestru

`grep -c 'ertyfikat'` → 0 (dziś 7), `grep -c 'Atest OSChR'` → 1, wynik zapytania o obie warstwy
(dwa zera), zrzut listy z Chrome MCP, hash commitu.

## 9. Rollback

Ten sam `db_export` co T-008. Rollback przywraca sekcję razem z literówkami — jeśli cofasz,
zgłaszasz Jankowi, że wracają.

## 10. Rozliczenie

Zakres **R**, godziny wspólne z T-008 (jedna wizyta, jedna edycja strony).

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | front: 0 wystąpień „ertyfikat", atest na miejscu |
| **+7 dni** | czy Elementor nie odtworzył sekcji z drugiej warstwy |
| **+30 dni** | czy Paweł nie poprosił o powrót jakiegoś certyfikatu — wtedy nowy wiersz |
