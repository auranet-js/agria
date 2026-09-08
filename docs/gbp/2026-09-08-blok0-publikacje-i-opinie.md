# Wizytówka Tarnów — rytm publikacji i uruchomienie opinii (T-121, T-122)

> **Data:** 2026-09-08 · **Blok 0** · **Zakres:** ryczałt R
> **Do akceptu Janka przed publikacją.** Nic z tego nie poszło jeszcze na profil.
> Stan wejściowy: cztery publikacje z 20.08 (wszystkie `LIVE`, CTA `LEARN_MORE`), najnowsza opinia z lutego 2025.

---

## T-121 — rytm publikacji

**Proponowany rytm: jedna publikacja tygodniowo, we wtorek.**

Wtorek, bo kampania emituje się w niedzielę, poniedziałek i wtorek — post wchodzi w ten sam rytm,
w którym i tak kupujemy uwagę. Google pokazuje publikacje najmocniej przez pierwszy tydzień, więc
tygodniowa kadencja utrzymuje profil „żywy" bez produkowania treści na siłę.

Każdy post prowadzi **na konkretny adres**, nigdy na stronę główną — tak jak cztery istniejące.

### Cztery pierwsze tematy

Trzy pierwsze pracują na szczyt wrzesień–październik, czwarty otwiera klaster paszowy, który ma
2 400 wyszukań miesięcznie i zero kliknięć.

---

**1 · 09.09 — Wrzesień i październik to ostatnie sensowne okno**
→ `https://agria.pl/jak-stosowac-wapno-nawozowe/`

> Wapno tlenkowe podnosi odczyn w 2–4 tygodnie, węglanowe pracuje 3–6 miesięcy. Jeśli efekt ma być
> widoczny na wiosnę, wysiew powinien się odbyć jesienią — na puste pole, kiedy można na nie wjechać
> bez ryzyka dla uprawy. Sprawdź, które wapno pasuje do Twojej gleby i kiedy je wysiać.

---

**2 · 16.09 — Kalkulator liczy teraz także magnez**
→ `https://agria.pl/kalkulator-wapnowania/`

> Na glebach lekkich niedobór wapnia i magnezu prawie zawsze idzie w parze. Kalkulator wapnowania
> dobiera teraz dawkę z uwzględnieniem magnezu — podajesz odczyn, kategorię gleby i areał, dostajesz
> dawkę na hektar i liczbę ton. Za darmo, bez rejestracji.

*Uzasadnienie: moduł magnezowy wszedł 04.09, czyli po sierpniowym poście o kalkulatorze —
to realnie nowa treść, nie powtórka.*

---

**3 · 23.09 — Tlenkowe czy węglanowe: na czym polega różnica**
→ `https://agria.pl/wapno-nawozowe-rolnictwo/`

> Tlenkowe (palone) reaguje od razu i podnosi pH w 2–4 tygodnie — sprawdza się na glebach średnich
> i ciężkich, ale na lekkich trzeba je dawkować ostrożnie. Węglanowe działa stopniowo, nie wypala
> materii organicznej, więc jest bezpieczne na glebach lekkich i w uprawach ekologicznych.

*Uzasadnienie: opis tej kategorii rozbudowaliśmy 04.09 z 958 do ~5 700 znaków — post kieruje ruch
na świeżo wzmocnioną stronę.*

---

**4 · 30.09 — Kreda pastewna to nie to samo co nawozowa**
→ `https://agria.pl/paszarstwo/`

> Kreda pastewna trafia do mieszanki paszowej, nie na pole — inne rozdrobnienie, inne wymagania
> czystości, inne dawkowanie. Stosuje się ją u niosek, bydła i trzody jako źródło wapnia.
> Zobacz parametry i atesty.

*Uzasadnienie: klaster „kreda" ma 463 wyświetlenia i zero kliknięć przy pozycji 10,0.
⚠️ Ten post wchodzi **po** wdrożeniu rozbudowanego opisu kategorii (T-078), nie przed.*

---

## Zdjęcia — przypisane 08.09

GBP przyjmuje wyłącznie **JPG i PNG**; uploady agria.pl są serwowane jako `.jpg.webp`, których nie
weźmie. Konwersja po stronie serwera (GD, `imagecreatefromwebp` → `imagejpeg`, jakość 88) — decyzja
Janka 08.09: „to są zdjęcia w znacznej części ze stocka lub generowane, możesz konwertować".

| post | zdjęcie | co przedstawia |
|---|---|---|
| 09.09 okno jesienne | `2026/03/agria-product-bg-1.jpg` | tło produktowe (użyte) |
| 16.09 kalkulator + magnez | `2026/09/gbp-wapnowanie-efekty-przed-po.jpg` | **przekonwertowane** — zdjęcie lotnicze, rozsiewacz, pole w połowie gołe i w połowie zielone |
| 23.09 tlenkowe czy węglanowe | `2026/03/agria-product-bg-1.jpg` | tło produktowe, powtórka |
| 30.09 kreda pastewna | `2026/03/ofirmie1.jpg` | **budynek AGRII z logo na elewacji** — jedyne autentyczne zdjęcie firmy w całej puli |

Gotowe pliki wsadowe: `tmp/gbp-posty/2026-09-*.json`, publikacja przez `scripts/gbp_post.py <plik> --wyslij`.

⚠️ **`2026/03/pobieranie-probek-glebowych.jpg` świadomie NIE użyte.** Tematycznie pasowałoby
do kalkulatora najlepiej ze wszystkich, ale ma w prawym górnym rogu **cudzy znak wodny** (zielone
logo, kadr wygląda na klatkę z filmu). Na stronie leży od marca; na wizytówce firmy to inna
ekspozycja. **Zauważone obok, nie ruszam** — do decyzji, czy zdejmować je też ze strony.

⚠️ **Pula się kończy.** Po 30.09 zostają tylko powtórki i materiały budowlane (cement, klinkier,
tynki, wykwity) — nietrafione dla rolnictwa. Na październik potrzebny materiał od AGRII (**T-050**)
albo świadoma decyzja o generowaniu, spójna z tym, że część obecnych zdjęć i tak jest generowana.

---

## Pytania techniczne do Kazimierza — sześć, wysłane 08.09

Decyzja Janka 08.09: skoro i tak piszemy do Kazimierza, dopytujemy o wszystko, czego nie wiemy
technicznie — „chłop się na tym zna". Lista przeszła przez gate: sprawdzone w `FAKTY_KLIENTA.md`,
że **big-bag** (przy kredzie pastewnej jest tam myślnik — nie ma go) i **worek 30 kg** są już
udokumentowane, więc o nie nie pytamy.

Wysłane do Janka `send-to-jan`, temat „AGRIA — pytania techniczne do Kazimierza (pełna lista…)".

| # | pytanie | co odblokowuje |
|---|---|---|
| 1 | **Dawkowanie a gatunek** — jeden przedział 1–2 kg/100 kg dla wszystkich, a pytają osobno o bydło i nioski | rozbicie sekcji dawkowania na konkrety |
| 2 | **Frakcja a gatunek** — cztery frakcje bez przypisania; konkurencja pisze „gruba dla niosek" | rozbicie sekcji frakcji |
| 3 | **CaO 37% — jak podawać hodowcy** — to ok. 26% Ca i ok. 66% CaCO₃, a typowa kreda paszowa bywa opisywana jako 95%+ CaCO₃; próg z najsłabszego źródła czy realny parametr? | jedna liczba w tabeli czy dwie |
| 4 | **Dwa źródła — Celiny (Hochel) i Lhoist** — czy parametry i frakcje się różnią | czy jedna specyfikacja na kategorię jest uczciwa |
| 5 | **Dokumentacja paszowa** — rejestr podmiotów paszowych, numer weterynaryjny, deklaracja materiału paszowego | treść i argument, których dziś nie mamy w ogóle |
| 6 | **Produkcja ekologiczna** — czy dopuszczona i czy jest papier | jw. |

**Osobno w tym samym mailu: T-108** — dolomit ma „CaO + MgO min 45%, w tym MgO min 15%", czyli
czystego CaO jest 30%, a kalkulator bierze pierwszą liczbę (45) i zaniża dawkę. Pytanie: dobór
po czystym CaO 30% czy po sumie 45%. Kazimierz robił z nami moduł magnezowy, więc to jego działka.

⚠️ **Frakcja wróciła na listę.** Pierwotnie Janek rozstrzygnął ją w quizie („zostajemy bez
mapowania"), ale skoro i tak pytamy Kazimierza, wraca jako pytanie — jeśli potwierdzi podział,
dopisujemy. Do tego czasu opis kategorii zostaje bez zmian.

---

## T-122 — uruchomienie opinii

Dziewięć opinii, średnia **4,30**, wszystkie z odpowiedzią. Obsługa jest w porządku — brakuje
wyłącznie dopływu. Ostatnia opinia ma dziewiętnaście miesięcy.

**To nie jest zadanie techniczne. To proces po stronie AGRII** — my przygotowujemy narzędzie,
prośby wysyła Paweł albo Kazimierz.

### Link do wystawienia opinii

```
https://search.google.com/local/writereview?placeid=ChIJvzPwdbyEPUcRGlMk2nXMFLI
```

Prowadzi wprost do okna wystawiania opinii dla wizytówki Tarnów, bez szukania w Mapach.

### Dwa zdania do wysłania odbiorcy

Do wklejenia w SMS albo wiadomość — bez nagłówka, bez podpisu firmowego, bo to ma brzmieć
jak wiadomość od handlowca, którego klient zna:

> Dzień dobry, dotarło wszystko w porządku? Jeśli tak, będę wdzięczny za krótką opinię w Google —
> zajmuje minutę i bardzo nam pomaga: [link]

### Kiedy pytać

**Dzień po dostawie, nie w dniu dostawy.** W dniu dostawy klient rozładowuje i sprawdza towar —
prośba o opinię trafia w najgorszy moment. Dzień później wie już, że wszystko się zgadza.

Najlepszy moment w cyklu to **druga i kolejna dostawa do tego samego odbiorcy** — stały klient
odpisuje chętniej niż nowy, a jego opinia brzmi wiarygodniej, bo może napisać o powtarzalności.

**Realistycznie:** przy jednej prośbie dziennie i typowej skuteczności rzędu 10–20% to kilka opinii
miesięcznie. Nie potrzeba więcej — potrzeba regularności, żeby najnowsza opinia nie miała znowu
dziewiętnastu miesięcy.

### Czego nie robimy

- **Nie kontaktujemy się z odbiorcami AGRII.** Materiał idzie do Janka, on przekazuje.
- **Nie ruszamy opinii jednogwiazdkowej z 2021** — ma już odpowiedź, drugi raz nie odpisujemy.
  Świeże opinie rozwodnią ją same: przy dziewięciu opiniach jedna gwiazdka waży dużo, przy
  dwudziestu przestaje.
- **Prośby kierujemy wyłącznie na wizytówkę Tarnów**, także po odzyskaniu oddziałów (T-047, T-124).
  Rozproszenie opinii między trzy pinezki to jedyne realne ryzyko architektury trzech wizytówek.
