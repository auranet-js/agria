# T-030 — `LocalBusiness` ×2 (Niedomice, Radgoszcz) w danych strukturalnych

| | |
|---|---|
| **Linia / zakres** | SEO · **R** |
| **Status** | 📅 wrzesień (M4) |
| **Szacunek** | 2 h |

---

## 1. Czego to dotyka

Dane strukturalne JSON-LD na froncie — dziś generowane przez Rank Math. Docelowo dwa węzły
`LocalBusiness` dla magazynów w Niedomicach i Radgoszczy, obok istniejącego `Organization`.
Miejsce wdrożenia: `modules/seo-head/seo-head.php` (moduł już modyfikuje wyjście `<head>`)
albo ustawienia Rank Math.

## 2. Strefy kruche

1. **Rank Math ma `local_business_type: Organization`** i `knowledgegraph_type: company`.
   Zmiana tego ustawienia przepisze schema **całej witryny**, nie doda oddziałów.
   Oddziały dokładasz **własnym węzłem**, nie przełącznikiem w Rank Math.
2. **`LocalBusiness` bez zweryfikowanego profilu GBP to sygnał bez pokrycia.** Google zestawia
   schema z Business Profile; deklarowanie dwóch lokalizacji, których nie mamy w GBP (**T-047**),
   nie jest błędem technicznym, ale nie przyniesie efektu w Mapach. Wdrożenie ma sens jako
   przygotowanie gruntu — powiedz to wprost, nie obiecuj widoczności lokalnej.
3. **Dane oddziałów muszą być zgodne z GBP, wizytówką, stroną `/kontakt/` i OLX.**
   Rozjazd NAP jest gorszy niż brak danych. Źródło: `T-003` (telefony na mapie, wdrożone 01.07).
4. **Nie duplikuj `Organization`.** Jedna firma, dwa oddziały jako `LocalBusiness`
   z `parentOrganization`, nie trzy niezależne firmy.
5. **`geo` (współrzędne) tylko rzeczywiste** — zmyślone współrzędne magazynu to błąd, który
   ktoś zauważy dopiero, gdy kierowca pojedzie w pole.
6. **Walidacja obowiązkowa** — Rich Results Test i Schema Validator. Błąd składni JSON-LD
   potrafi unieważnić **całą** strukturę na stronie, łącznie z działającym dziś `Organization`.

## 3. Stan zmierzony 19.08.2026

```
front /: "@type" → Organization ×1, WebSite ×1, WebPage ×1, Article ×1, Person ×1, ImageObject ×3
LocalBusiness: brak
Rank Math: knowledgegraph_type=company, knowledgegraph_name=„AGRIA Sp. z o.o.",
           local_business_type=Organization
GBP: tylko Tarnów; Niedomice i Radgoszcz poza kontrolą (T-047)
```

## 4. Warunki wejścia

- [ ] Dane oddziałów potwierdzone (adresy, telefony, godziny) — pochodzą z `T-003`, zweryfikuj aktualność.
- [ ] `T-029` zamknięty — nie dokładaj węzłów do struktury, z której właśnie usuwasz `Person`.

## 5. Co robisz

1. Zbierz dane oddziałów z `/kontakt/` i `FAKTY_KLIENTA.md`, potwierdź u Janka.
2. Napisz węzły `LocalBusiness` z `parentOrganization` wskazującym `@id` istniejącego `Organization`.
3. `backup_file` na `seo-head.php`, wdrożenie filtrem `rank_math/json_ld`.
4. Walidacja: Rich Results Test + Schema Markup Validator na `/` i `/kontakt/`.
5. Kontrola, że `Organization`, `WebSite` i `Product` nie ucierpiały.

## 6. Jak sprawdzasz w trakcie

```bash
curl -s https://agria.pl/kontakt/ | grep -oP '"@type":"[A-Za-z]+"' | sort | uniq -c
```
Po zmianie: `LocalBusiness` ×2, `Organization` ×1, reszta bez zmian.

## 7. Jak testujesz

```bash
# 1. typy schema na kluczowych stronach
for u in / /kontakt/ /o-firmie/; do echo "$u"; curl -s https://agria.pl$u | grep -oP '"@type":"[A-Za-z]+"' | sort | uniq -c; done
# 2. poprawność JSON — wyciągnij bloki ld+json i sparsuj
curl -s https://agria.pl/kontakt/ | python3 -c "
import sys,re,json
for m in re.findall(r'<script type=\"application/ld\+json\"[^>]*>(.*?)</script>', sys.stdin.read(), re.S):
    json.loads(m); print('OK', len(m), 'B')"
# 3. Rich Results Test (ręcznie, przez przeglądarkę)
```

## 8. Dowód do rejestru

Zrzut typów schema przed/po, wynik walidatora (zero błędów), potwierdzenie, że `Organization`
i `Product` nadal parsują się poprawnie.

## 9. Rollback

`backup_file` modułu `seo-head.php` — przywrócenie jednym zapisem.

## 10. Rozliczenie

Zakres **R**, wrzesień (M4), ~2 h.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+1 h** | walidacja JSON-LD na trzech stronach |
| **+14 dni** | GSC → Ulepszenia: czy Google odczytał nowe encje bez błędów |
| **po T-047** | uzupełnienie o dane z odzyskanych profili GBP i sprawdzenie spójności NAP |
