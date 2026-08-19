# T-043 — weryfikacja mockupu kalkulatora z modułem Mg przez Kazimierza

| | |
|---|---|
| **Linia / zakres** | Kalkulator · **P** |
| **Status** | 🟡 czeka na AGRIĘ od 18.08 |
| **Blokuje** | `T-044` (wdrożenie do pluginu) |
| **Szacunek** | 0,5 h po odpowiedzi (zebranie uwag), wdrożenie osobno |

---

## 1. Czego to dotyka

Mockup `mockups/agria-kalkulator-mg-test-2026-08-18.html` (commit `c4547d2`), wystawiony pod
`https://auratest.pl/fe4f58fec53ctmp/agria-kalkulator-mg-test-2026-08-18.html`.
Docelowo: moduł `agria-by-auranet/modules/liming-calculator/` na produkcji.

## 2. Strefy kruche

1. **To jest merytoryka rolnicza, nie UX.** Kazimierz weryfikuje **liczby**: dawki, granice ocen,
   przeliczniki. Uwaga typu „ładniej by wyglądało" nie jest tym, na co czekamy.
2. **Cztery kwestie są otwarte i żadna nie może zniknąć po cichu przy wdrożeniu:**
   - **%CaO wapna tlenkowego magnezowego (#313)** — WC deklaruje „min. 70 % CaO" obok 25 % MgO.
     Jeśli 70 % to suma CaO+MgO, dawka rośnie z 6,86 do ~10,7 t/ha. Do rozstrzygnięcia z kartą producenta.
   - **Rozjazd Dolomitu** — produkcyjny `extract_cao_percent` bierze pierwszą liczbę ze sluga
     `cao-mgo-min-45-w-tym-mgo-min-15` → **45 %**, choć realne CaO = 45 − 15 = **30 %**.
     Mockup liczy w tabeli Mg z 30, w tabeli CaO z 45 (wierność produkcji). Przy wdrożeniu
     trzeba zdecydować, czy poprawiamy matcher — a to dotyka wszystkich wyników, nie tylko Mg.
   - **Blokada max w polu Mg** = przycinanie wartości. Alternatywa (dopuścić realny wynik
     + komunikat „bardzo wysoka") zaproponowana, **Janek nie rozstrzygnął**.
   - **Ostrzeżenie przy dawkach powyżej progu jednorazowej aplikacji** (4 t lekkie / 5 t ciężkie)
     — dziś tylko disclaimer.
3. **Parametry produktów wyłącznie z kart producentów** (Nordkalk, Lhoist) i rozporządzeń.
   17 kart leży publicznie na `/do-pobrania/` — klient ściąga ten sam plik, więc rozjazd wyjdzie.
4. **Nie zmieniaj domyślnego celu nawożenia.** Default = górna granica „wysokiej"; próba zmiany
   na minimum została raz wycofana na żądanie Janka. To decyzja, nie niedopatrzenie.
5. **Kalkulator nie proponuje kredy pastewnej ani malarskiej** (`post__not_in [304,307]`, T-001).
   To zostaje.

## 3. Stan

Mockup u Kazimierza od 18.08. Brak odpowiedzi na 19.08.

## 4. Warunki wejścia

- [ ] Kazimierz odesłał uwagi (albo potwierdził, że liczby się zgadzają).

## 5. Co robisz

1. Poproś Janka o ponaglenie, jeśli minęło ponad 7 dni — to blokuje T-044 i wrzesień.
2. Po otrzymaniu uwag: spisz je jako listę zmian z podziałem na „liczby" i „interfejs".
3. Zestaw je z czterema otwartymi kwestiami — część uwag może je rozstrzygnąć.
4. Przedstaw Jankowi: co zmieniamy w mockupie przed wdrożeniem, co idzie od razu do pluginu.
5. Zaktualizuj mockup, wystaw ponownie na auratest, poproś o potwierdzenie.

## 6. Jak sprawdzasz

Każda uwaga Kazimierza ma trafić do listy z jednoznacznym statusem: przyjęta / odrzucona
z uzasadnieniem / do rozstrzygnięcia przez Janka. Żadna nie może zostać bez adresu.

## 7. Jak testujesz

Kontrolne przeliczenie trzech przypadków ręcznie (gleba lekka / średnia / ciężka), porównanie
z wynikiem mockupu. Dawki muszą być realne — 16–19 t/ha dolomitu było objawem błędu w poprzedniej
wersji logiki i tak samo poznasz następny.

## 8. Dowód do rejestru

Lista uwag Kazimierza ze statusami, zaktualizowany mockup z URL-em, potwierdzenie akceptu.

## 9. Rollback

Mockup jest w gicie, wdrożenia jeszcze nie ma — ryzyko zerowe.

## 10. Rozliczenie

Zakres **P** (kalkulator poza ryczałtem). Zebranie uwag ~0,5 h, korekta mockupu wg zakresu.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+7 dni od przekazania** | ponaglenie przez Janka, jeśli cisza |
| **przy T-044** | cztery otwarte kwestie muszą mieć rozstrzygnięcie **przed** pierwszą linią kodu |
