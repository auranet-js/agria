# Wizytówka Tarnów — publikacje na październik (powrót do wtorków)

> **Data:** 2026-10-08 · **Do akceptu Janka przed publikacją.** Nic nie poszło na profil.
> Stan zmierzony 08.10 (`scripts/gbp_dump.py` → `tmp/gbp-tarnow.json`): **5 publikacji**, ostatnia **08.09**
> („Wrzesień i październik to ostatnie sensowne okno”). Posty zaplanowane na 16, 23 i 30.09 **nie wyszły**.
> Opinie: 9, ostatnia **28.02.2025**.

Rytm bez zmian: jedna publikacja we wtorek, każda na konkretny adres (`docs/gbp/2026-09-08-blok0-publikacje-i-opinie.md`).

| Wtorek | Temat | Adres | Skąd |
|---|---|---|---|
| **13.10** | Tlenkowe czy węglanowe — na czym polega różnica | `/wapno-nawozowe-rolnictwo/` | wrześniowy post 3, gotowy |
| **20.10** | Staw spuszczony — kreda czy wapno tlenkowe | `/wapno-do-stawu/` | nowy, treść strony z 08.10 |
| **27.10** | pH gleby — tester czy laboratorium | `/ph-gleby/` | nowy, poradnik z 08.10 |
| **03.11** | Kalkulator liczy teraz także magnez | `/kalkulator-wapnowania/` | wrześniowy post 2, gotowy |

**Wstrzymany: wrześniowy post 4 „Kreda pastewna to nie to samo co nawozowa”.** Podaje „1–2 kg na 100 kg paszy”,
a to jest dokładnie liczba, o którą pytamy Pawła w T-077 „kreda pastewna” (producenci jej nie podają).
Wraca po jego odpowiedzi, z poprawioną dawką.

Kolejność: rdzeń rolniczy na szczyt października, staw w sezonie odłowów (X–XI), pH jako wejście
do kalkulatora, kalkulator na koniec — domyka ścieżkę „sprawdź pH → policz dawkę”.

---

**13.10 · Tlenkowe czy węglanowe — na czym polega różnica** → `https://agria.pl/wapno-nawozowe-rolnictwo/`

> Tlenkowe (palone) reaguje od razu i podnosi pH w 2–4 tygodnie — sprawdza się na glebach średnich
> i ciężkich, ale na lekkich trzeba je dawkować ostrożnie. Węglanowe działa stopniowo, nie wypala materii
> organicznej, więc jest bezpieczne na glebach lekkich i w uprawach ekologicznych.

Zdjęcie: `2026/03/agria-product-bg-1.jpg` (JPG, jest).

---

**20.10 · Staw spuszczony? Kreda i wapno mają różne zadania** → `https://agria.pl/wapno-do-stawu/`

> Kreda utrzymuje odczyn wody i pracuje przy rybach przez cały sezon — działa wolno, więc nie podnosi pH
> skokowo. Wapno tlenkowe odkaża dno i rozkłada muł, ale sypie się je dopiero na spuszczony staw, bez wody:
> przy rybach podnosi odczyn gwałtownie. Kreda granulowana w workach 25 kg i big-bagach, sypka luzem
> całym samochodem. Sprawdź, ile kredy na ar.

Zdjęcie: zdjęcie stawu ze strony (`webp`, załącznik 2847) — **wymaga konwersji do JPG** (patrz niżej).

---

**27.10 · pH gleby — tester czy laboratorium** → `https://agria.pl/ph-gleby/`

> Tester daje wynik orientacyjny: powie, czy pole jest kwaśne, ale nie powie, ile wapna wysiać. Do dawki
> potrzebny jest pomiar laboratoryjny w roztworze KCl — i kategoria gleby, bo ciężka gleba przy tym samym
> pH wymaga wapnowania wcześniej niż lekka. Przy pH 5,5 w glebie zaczyna pojawiać się toksyczny glin.
> Skala odczynu i tabela potrzeb wapnowania w poradniku.

Źródło liczb: poradnik `/ph-gleby/` (IUNG-PIB 2021, 2022). Zdjęcie: obraz wyróżniający wpisu 2850 (`webp`) —
**wymaga konwersji do JPG**.

---

**03.11 · Kalkulator liczy teraz także magnez** → `https://agria.pl/kalkulator-wapnowania/`

> Na glebach lekkich niedobór wapnia i magnezu prawie zawsze idzie w parze. Kalkulator wapnowania
> dobiera teraz dawkę z uwzględnieniem magnezu — podajesz odczyn, kategorię gleby i areał, dostajesz
> dawkę na hektar i liczbę ton. Za darmo, bez rejestracji.

Moduł Mg sprawdzony w renderze 08.10 (pole „zawartość magnezu (Mg) w glebie — pole nieobowiązkowe”).
Zdjęcie: `2026/09/gbp-wapnowanie-efekty-przed-po.jpg` (JPG, jest).

---

## Zdjęcia

GBP przyjmuje tylko JPG/PNG. Dla 20.10 i 27.10 trzeba po stronie serwera skonwertować webp → JPG
(GD `imagecreatefromwebp`, precedens `2026/09/gbp-wapnowanie-efekty-przed-po.jpg`). To zapis do
`uploads` na produkcji — **tylko na „ok”**. Pliki JPG nie są podpinane do żadnej strony (na stronie
zostaje webp, zgodnie z regułą z 23.09).

## Mechanika

Wsady w `tmp/gbp-posty/2026-10-*.json`, publikacja `scripts/gbp_post.py <plik> --wyslij` w dniu wpisu,
zrzut `gbp_dump.py` przed każdą. Kalendarz „Auranet Claude”: cztery wtorkowe eventy 9:00; ten z 03.11
z dopiskiem „przygotuj listopad”.
