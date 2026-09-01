# Prompt: zaktualizowane podsumowanie sierpnia dla Kasjana i Pawła

> **Jak użyć:** wklej całość jako pierwszą wiadomość w nowym wątku `cd ~/projekty/agria && claude`.
> **Data powstania:** 2026-09-01. **Okno raportowania: pełny sierpień, 1–31.08.2026** — wynik „na wczoraj".
> **Odbiorcy końcowi:** Kasjan (`biuro@aseosystem.pl`, właściciel, decyduje o budżecie) + Paweł Bigos
> (`pawel.bigos@agria.pl`, operacyjnie). Wysyła **Janek sam**, z `js@auranet.com.pl`. Nigdy Claude.

---

## 0. Po co to robimy

Podsumowanie sierpnia **już istnieje** i jest zacommitowane (`27afffa`). Zadanie to **nie jest pisanie
od zera**, tylko:

1. **odświeżenie liczb na pełny miesiąc** — dotychczasowe stoją na oknie 1–29.08, bo GSC dojrzewa dane
   ~3 dni; 01.09 pełny sierpień jest już wiarygodny i **wynik wyjdzie wyższy**;
2. **rozpisanie korzyści w siedmiu materiach** (§3) — dziś raport jest mocny w SEO i słabszy w opisaniu
   tego, co powstało w grafice, treści i analityce, a to jest praca, za którą klient płaci;
3. domknięcie mailem, który Janek wysyła **1–2.09**.

**Zasada nadrzędna:** każde zdanie o efekcie ma mieć liczbę i źródło. Bez liczby to jest opinia,
a opinii nie fakturujemy. Jeśli czegoś nie da się zmierzyć — napisz, że nie da się, i nie udawaj.

---

## 1. Co już jest w repo — przeczytaj to najpierw

| Plik | Co zawiera |
|---|---|
| `docs/raporty/2026-08.md` | **raport pełny, wewnętrzny** — 8 sekcji, alokacja godzin, audyt techniczny, plan września |
| `docs/raporty/2026-08-mail.md` | **draft maila do klienta** — ten do aktualizacji i wysyłki |
| `docs/raporty/PODSUMOWANIE_M3_2026-08.md` | dowody + bilans handlowy + ustalenia z Kasjanem |
| `docs/raporty/2026-07-mail-WYSLANY.md` | **wzorzec językowy** — to poszło do klienta miesiąc temu |
| `docs/REJESTR_ZOBOWIAZAN.md` | dziennik M3 (co dostarczone, godziny, zakres R/P/W) + kolejka września |
| `docs/FAKTY_KLIENTA.md` §6 | ustalenia handlowe, w tym korekta OLX z 31.08 |

Memory projektu — **obowiązkowo przed pisaniem do klienta**: `feedback_agria_no_self_criticism_built_site`,
`feedback_agria_offer_mail_structure`, `feedback_agria_bez_zargonu_loco`, `project_agria_gbp`,
`feedback_gsc_ctr_z_poziomu_strony`, `feedback_agria_auranet_decyduje`.

---

## 2. Odśwież dane — pełny sierpień, pull 01.09

### GSC — okna pełnych miesięcy
Property to **URL-prefix `https://agria.pl/`**, nie `sc-domain:`. Wzorzec: `scripts/gsc_pull.py`
(OAuth z `~/secrets/google/tokens.json`, refresh token). Pobierz w jednym przebiegu:

| Okno | Po co |
|---|---|
| `2026-08-01`…`2026-08-31` | **wynik miesiąca** |
| `2026-07-01`…`2026-07-31` | poprzedni miesiąc |
| `2026-06-01`…`2026-06-30` | M1, pokazuje trend |
| `2026-08-01`…`2026-08-31` **2025** | **rok do roku — najmocniejszy argument, bo odporny na sezon** |

Metryki: kliknięcia, wyświetlenia, CTR, pozycja · liczba fraz z widocznością, **TOP3 i TOP10**
(`dimensions:["query"]`, `rowLimit: 25000`) · TOP strony (`dimensions:["page"]`) · zapytania z klikami.

**Liczby z okna 1–29.08 do przebicia (nie przepisuj ich, sprawdź):** 349 klik · 26 856 wyśw. · poz. 7,1 ·
507 fraz · TOP3 202 · TOP10 363. Rok wcześniej 1–29.08.2025: 224 klik · 8 926 wyśw. · poz. 16,3.

**Grupa kontrolna sezonowa** — poradniki, których nie tykaliśmy (`cement`, `tynki`, `wykwity`):
w oknie 1–29 miały **0 kliknięć w lipcu i 0 w sierpniu** przy wyświetleniach 62 → 84. Powtórz na pełnym
miesiącu — to jest dowód, że wzrost nie jest sezonem.

⚠️ **CTR licz z poziomu strony, nie z sumy zapytań** — próg prywatności GSC ukrywa większość kliknięć
na poziomie `query` (memory `feedback_gsc_ctr_z_poziomu_strony`).

### Google Ads
`bash scripts/google/ads_call.sh /googleAds:searchStream POST <plik.json>`, CID 674-207-1446, API v25
(wersja czytana z `~/secrets/google/ads-config.json`, **nie hardkoduj**).

```sql
SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros,
       metrics.conversions, metrics.all_conversions, metrics.average_cpc, metrics.ctr
FROM campaign WHERE segments.date BETWEEN '2026-08-13' AND '2026-08-31'
```
Do rozbicia konwersji dodaj `segments.conversion_action_name` i `segments.date` z filtrem
`metrics.all_conversions > 0`.

**Stan na 13–30.08:** 388 klik · 3 295 wyśw. · 689,76 zł · CTR 11,8% · CPC 1,78 zł · 3 zdarzenia
(2 × `form_submit` 25.08, 1 × `phone_click` 28.08). **Dolicz 31.08** — to niedziela po przestawieniu
na dni zakupowe, czyli dzień, który ma pokazać, czy zmiana z 28.08 działa.

### GA4
Property `538301430`, Data API `runReport`. Sierpień vs lipiec: `sessions`, `sessionDefaultChannelGroup`,
`eventCount` per `eventName`, `keyEvents`.
**Stan 1–30.08:** 357 sesji (organic 73, paid 118) wobec 148 w lipcu (organic 5).
⚠️ **GA4 widzi wycinek** — 73 sesje organiczne wobec 349 kliknięć w GSC. Do organiku używaj GSC;
GA4 służy do zdarzeń. **Nie mieszaj tych dwóch źródeł w jednej tabeli.**

### OLX
`data/olx/statystyki.json` (kumulatywne, licz różnice) + `data/olx/monitor-log.json`.
**Stan 31.08 07:35:** 200/200 `active` · 794 odsłony · **27 odsłon numeru** · 25 obserwujących ·
17 dni do wygaśnięcia pakietu. Jeśli monitor zebrał świeższy wpis — użyj go i **podaj godzinę pomiaru**.

### Indeksacja
`scripts/gsc_inspect.py` (URL Inspection). **Odczyt 31.08:** karty #306 i #308 weszły do indeksu
(crawl 28–29.08), `/wapno-do-stabilizacji-gruntow/` i `/jak-stosowac-wapno-nawozowe/` przeszły
z „nieznany" na „wykryta"; poza indeksem zostają #303, #311, #316, #318, `/wapno-do-stawu/`,
`/wapno-granulowane/`. Sprawdź, czy 01.09 doszło coś jeszcze.

---

## 3. Siedem materii — w każdej liczba i korzyść

To jest **sedno zadania**. Dla każdej materii odpowiedz na trzy pytania: **co powstało (liczba)**,
**co to daje klientowi (korzyść w jego języku)**, **skąd wiemy (dowód)**. Materie, w których dziś
raport jest najsłabszy, oznaczone ⚠️.

### 3.1 Rozwój i prace na stronie
Źródło: `git log --since=2026-08-01 --until=2026-09-01` (141 commitów) + dziennik M3 w rejestrze
+ zapytanie do bazy o `post_modified` w sierpniu (MCP `query_db`, prefix `wpfz_`).

Zmierzone: **27 stron i kart dotkniętych w sierpniu.** Trzy nowe strony ofertowe (`/wapno-granulowane/`
7 792 znaki, `/wapno-nawozowe/` 8 993, `/wapno-do-stawu/` 7 139), przepisany terminarz (22 524),
hub scalony z poradnikiem dawkowym (21 794), 15 kart z warstwą cenową, `/do-pobrania/` (35 519),
strona główna z listingiem poradników. Plus: H1 na wpisach i `/oferta/`, układ trzech stron
z surową treścią, listingi produktów na landingach, 301 dla dwóch starych baz adresów,
login administratora przestał wyciekać trzema kanałami.

Korzyść do nazwania: **strona przestała być katalogiem, a zaczęła odpowiadać na pytania zakupowe.**

### 3.2 SEO i widoczność
Źródło: §2 tego promptu. Najmocniejsze liczby: rok do roku, fraz w TOP3, udział huba i kalkulatora
(44% ruchu w oknie 1–29), frazy nowe („ile wapna granulowanego na hektar", „wapno granulowane cena",
„ile wapna żeby podnieść pH o 1"). Dołóż grupę kontrolną jako dowód, że to nie sezon.

Korzyść: **ten sam ruch przychodzi dziś z pozycji 7, nie 16 — czyli z miejsca, z którego się kupuje.**

### 3.3 Setup i uruchomienie Google Ads
Źródło: dziennik M3 + `docs/offers/2026-08-PLAN_ADS_3MIES.md`.
Co powstało: konto od zera, spięcie z pomiarem, **trzy kampanie**, 44 frazy aktywne (w tym 24 transakcyjne),
teksty reklam, wykluczenia, geoblok bezpieczeństwa, rozszerzenia połączeń (6 powiązań: 2 numery × 3 kampanie),
dwa landingi docelowe z paskiem telefonu.
**To 8–10 h zadeklarowane klientowi jako wykonane bez dopłaty** — i tak ma zostać opisane.

⚠️ Korzyść do nazwania mocniej niż dziś: **kampania od pierwszego dnia mierzy telefon i formularz**,
więc rozmowa po trzech miesiącach będzie o liczbach, nie o wrażeniach.

### 3.4 Uruchomienie sprzedaży na OLX — statystyki
Źródło: `docs/offers/2026-08-PLAN_OLX.md`, dziennik M3, `data/olx/`.
Co powstało: **200 ogłoszeń w 60 miejscowościach**, 11 produktów, spięcie z Partner API, monitoring dzienny,
rejestr publikacji zgodny z API co do wpisu, `auto_extend` na 200/200.
Wynik: 794 odsłony, 27 odsłon numeru, 25 obserwujących w 11 dni; zero wygaszeń, zero odrzutów moderacji.
**Koszt kontaktu 9–12 zł w pierwszym cyklu** (sam pakiet; obsługa rusza we wrześniu) wobec **230 zł
za zdarzenie kontaktowe w Ads** — to jest liczba, która broni kanału.

⚠️ **Pakiet wygasa 16.09** — w mailu **wzmianka bez proszenia o decyzję** (ustalenie Janka 31.08):
„pakiet opłacony do połowy września, wrócimy do tego przed terminem". Decyzja idzie telefonem Janka
do Pawła, nie mailem.

### 3.5 Analityka ⚠️
Materia dziś najsłabiej opisana, a zjadła realny czas. Co powstało: Consent Mode zaawansowany,
baner zgód przestał zasłaniać ścieżkę kontaktu, `phone_click` przestawiony na konwersję główną,
synchronizacja workspace GTM (opublikowana wersja rozjeżdżała się z roboczą od 13.08), rediagnoza GA4
od zera, geoblok.
**Dowód skuteczności:** sesje organiczne w GA4 **5 → 73**, czyli pomiar zaczął w ogóle widzieć ruch,
którego wcześniej nie rejestrował.

Korzyść: **przestajemy zgadywać, skąd przychodzi zapytanie.** Bez tego budżet reklamowy wydaje się w ciemno.

### 3.6 Opracowanie grafik i treści ⚠️
Materia dziś w raporcie prawie nieobecna, a to była duża robota. Co powstało:
- **56 unikalnych zdjęć produktowych** rozłożonych na 7 slotów dla 11 kart (186 ogłoszeń po 7 zdjęć, 14 po 6),
  wszystkie zweryfikowane HTTP 200;
- **12 kadrów miniatur wygenerowanych przez Gemini** (`scripts/olx/miniatury.py`) — próbka towaru
  na gradiencie marki, zastosowanie u góry, pasek z korzyścią przy próbce;
- **przebudowa miniatur po pomiarze na realnym telefonie:** kadr listy mobilnej OLX to 150×183 px
  przy plikach poziomych 1500×1050 — widoczne było **środkowe 57% szerokości**, więc ucinało hasło
  z obu stron i logo. Zmierzone Puppeteerem na żywym OLX, poprawione generatorem;
- **11 kart informacyjnych z kodem QR** do kalkulatora (UTM per karta) + 17 kart katalogowych do druku;
- treści ogłoszeń: tytuły, leady, opisy per produkt i miasto.

Korzyść: **ogłoszenie wygrywa albo przegrywa w miniaturze na liście — tam zapada decyzja o kliknięciu.**

### 3.7 Tuning — czyli praca po starcie ⚠️
Najtrudniejsza do pokazania, bo nie zostawia „nowego bytu", a jest najbardziej ekspercka. Co zrobione:
- **Ads:** wyłączone 4 frazy szerokie zjadające **54% wydatku** (rozbiór 201 zapytań: 92 to marki
  konkurencji i lokalne kopalnie, a realnie naszych — cenowych i hurtowych — było **24 z 201, czyli 12%**);
  dodane 16 fraz intencyjnych; geo z 8 województw na dwa promienie wokół magazynów; emisja przestawiona
  na niedzielę–wtorek (niedziela ma zmierzony 2. CTR tygodnia); budżet 26 → 60 zł/dz przy trzech dniach.
  **Efekt zmierzony: udział marek i poradników w wydatku spadł z ~49% do 9,7%.**
- **OLX:** przełożenie **68 ogłoszeń** bliżej magazynów (pas 200–375 km → 2–98 km) po pomiarze,
  że pierścień 60–120 km dawał **0,270 kontaktu na ogłoszenie wobec 0,065** w pierścieniu bliskim.
  68/68, zero odrzutów, pakiet nietknięty.
- **Wykryty i usunięty 24-godzinny przestój emisji** 27.08 (puste saldo; Google nie alertuje —
  wykryte odczytem API).

Korzyść: **budżet przestał płacić za cudze marki i za obszary, do których nie dowozicie.**

---

## 4. Ceny — zgodne, nie ruszać

| Pozycja | Netto |
|---|---|
| Opieka nad stroną i pozycjonowanie | **2 000 zł** |
| Budżet reklamowy Google (idzie w całości do Google) | **1 200 zł** |
| Prowadzenie kampanii | **600 zł** |
| Jednorazowe uruchomienie kanału OLX | **1 800 zł** |
| **Razem sierpień** | **5 600 zł netto** |

- **Obsługi OLX (300 zł/mies.) w sierpniu NIE liczymy** — pokrywa ją setup; wchodzi od września.
  Decyzja Janka 31.08.
- Pakiet OLX Premium 200 (1 199,99 brutto) **kupuje AGRIA** — nie jest na naszej fakturze.
- Setup kampanii Google — **bez dopłaty, w ramach opieki**, tak zadeklarowane w mailu z 06.08.
- **Budżet komunikuj wyłącznie miesięcznie.** Nigdy sumy wielomiesięcznej.
- **Nie wymyślaj żadnych innych stawek** bez akceptu Janka.

Wewnętrznie (nie do klienta): ryczałt 2 000 zł przy **39,6 zmierzonych godzinach** ≈ 50 zł/h, z czego
**~20 h (ok. 1 000 zł) poszło w setup reklam i pomiar**, ~28 h w SEO, treść i technikę. Poza ryczałtem
28,0 h. Siedem pozycji dziennika ma znacznik `5 h*` — wartość nieodtworzona, więc realny nakład wyższy.

---

## 4a. Wrzesień — plan i koszty

**Wrzesień jest tańszy od sierpnia i to trzeba w mailu powiedzieć wprost** — znika jednorazowy setup OLX
(1 800 zł), dochodzi stała obsługa kanału (300 zł).

### Nasza faktura — wrzesień 2026

| Pozycja | Netto |
|---|---|
| Opieka nad stroną i pozycjonowanie | **2 000 zł** |
| Budżet reklamowy Google (idzie w całości do Google) | **1 200 zł** |
| Prowadzenie kampanii | **600 zł** |
| Obsługa kanału OLX | **300 zł** |
| **Razem wrzesień** | **4 100 zł netto** |

### Po stronie AGRII, poza naszą fakturą

| Pozycja | Kwota |
|---|---|
| Pakiet OLX Premium 200 na kolejny cykl | **1 199,99 zł brutto** |

⚠️ **Pakiet wygasa 16.09**, emisja formalnie do 19.09. `auto_extend` przedłuża ogłoszenia **tylko dopóki
żyje pakiet** — bez odnowienia **wszystkie 200 ogłoszeń gasną jednego dnia** (precedens 18.07: 17 ogłoszeń
zgasło razem z pakietem, w środku sezonu). **Decyzja musi zapaść do 10.09.**

**W mailu: wzmianka bez proszenia o decyzję** (ustalenie Janka 31.08) — „pakiet opłacony do połowy września,
wrócimy do tego przed terminem". Rozmowę o odnowieniu prowadzi Janek telefonicznie z Pawłem, z liczbą
w ręku: koszt kontaktu 9–12 zł wobec 230 zł za zdarzenie kontaktowe w Ads. Rekomendacja: odnawiamy 200.

### Co robimy we wrześniu — do maila, po ludzku

Źródło: `docs/REJESTR_ZOBOWIAZAN.md`, sekcja „Faza 1" i „Wrzesień". **Sprawdź rejestr przed pisaniem** —
terminy mogły się przesunąć.

| Termin | Co | Dlaczego akurat to |
|---|---|---|
| 05.09 | Opis kategorii `wapno nawozowe dla rolnictwa` (T-092) | Jedyny nasz adres rankujący na `wapno nawozowe` (1 300/mies., w sezonie 1 900) |
| 12.09 | Opis kategorii `paszarstwo` (T-078) | `kreda pastewna` 2 400/mies., popyt płaski cały rok |
| 20.09 | Spoke ziemniaki (T-074) · `wapno hydratyzowane` (T-085) · `wapno do oczyszczalni` (T-093) | Hydratyzowane i oczyszczalnie to **zobowiązanie z maila do Kasjana z 06.08** |
| wrzesień | Szybkość strony na telefonach (T-031) | Przesunięte z sierpnia — powiedzieć wprost |
| wrzesień | Kalkulator z modułem magnezowym na produkcję (T-044, ≈4 h) | Kazimierz przetestował i zaakceptował wersję roboczą 28.08 |
| wrzesień | Dane oddziałów w wynikach lokalnych (T-030) · lżejszy formularz na landingach (T-059) | — |
| **11.09** | Kontrola: czy 68 przełożonych ogłoszeń OLX zaczęło pracować | Pierścień 60–120 km dawał 0,270 kontaktu/ogłoszenie wobec 0,065 blisko |
| **15.09** | Kontrola: czy Google pobrał adresy odblokowane w sierpniu | Warunek wejścia w kolejną fazę treści |

⚠️ **Wrzesień jest przeładowany** — obietnice z 06.08 + prace przesunięte z sierpnia + Faza 1 treści
+ prowadzenie dwóch kanałów płatnych. **Do klienta idzie plan realny, nie życzeniowy** — jeśli coś ma
wypaść, decyduje Janek przed wysyłką maila, a nie klient po fakcie.

⚠️ **Zobowiązanie na koniec października:** w mailu z 06.08 zapowiedzieliśmy podsumowanie trzech miesięcy
reklam — ile zapytań, z jakich haseł, jakim kosztem — na podstawie którego klient decyduje o kontynuacji.
**Tej pozycji nie ma dziś w rejestrze.** Dopisz ją przy okazji tego wątku.


---

## 5. Mail do klienta — co zmienić względem draftu

Draft: `docs/raporty/2026-08-mail.md`. Zachowaj jego strukturę i ton, zaktualizuj liczby na pełny
sierpień i **dociągnij materie 3.5–3.7**, które dziś są w nim ledwie wzmiankowane.

Reguły twarde (złamanie = mail do wyrzucenia):
- **Nie krytykujemy stanu strony** — zbudował ją Auranet. Framing rozwojowy: „uruchamiamy / wzmacniamy /
  optymalizujemy", nigdy „brak / błąd / wolno".
- **Zero żargonu.** Odbiorcą jest zarząd i rolnik, nie specjalista. Zamiast „loco magazyn" → „cena za towar,
  bez transportu". Bez „CTR", „impresji", „konwersji" — pisz „wyświetlenia", „kliknięcia", „zapytania".
- **Przemilcz oddziały w Mapach** (Niedomice, Radgoszcz — brak dostępu do profili).
- Forma **„ty/Wy"**, bez stopki (dokleja Outlook), bez załącznika.
- **Uczciwie o szybkości mobile** — zapowiedziana na sierpień, nie zdążyliśmy, wchodzi we wrzesień.
  Jedno zdanie z przyczyną, bez samobiczowania.
- **Nowe wpisy poradnikowe:** nie pisz, że „nie było treści" — to nieprawda (§3.1). Napisz, że setup
  reklam zajął około połowy sierpniowego czasu w opiece, dlatego wpisy poradnikowe wracają we wrześniu.
- **Nie mieszaj OLX do rozliczenia opieki** — to osobna pozycja i osobna faktura.
- **Podaj koszt września (4 100 zł netto) obok sierpniowego** i powiedz wprost, że wrzesień jest tańszy,
  bo uruchomienie OLX było jednorazowe. Klient nie ma się tego domyślać z różnicy dwóch liczb.

---

## 6. Pułapki specyficzne

| Pułapka | Co zrobić |
|---|---|
| Przepisanie liczb z okna 1–29 jako „sierpień" | Przelicz na 1–31, wyjdzie wyżej |
| CTR z sumy zapytań | Licz z poziomu strony — próg prywatności ukrywa większość kliknięć |
| „CTR spadł" jako regres | Wyświetlenia urosły 3×, bo hub wszedł na frazy o wolumenie tysięcy z pozycji 6–8. Kliknięcia rosną szybciej niż kiedykolwiek |
| GA4 jako źródło o organiku | GA4 widzi wycinek. Organik = GSC, zdarzenia = GA4 |
| „Zero konwersji z Ads" | Do 24.08 telefony **nie były liczone** — to brak pomiaru, nie brak telefonów |
| Suma godzin z rejestru liczona automatem | Kolumna zawiera wpisy tekstowe („z T-008") — automat czyta je jako liczby. Sprawdzaj ręcznie |
| Weryfikacja treści w bazie | Parametry i treść żyją w 4 warstwach — weryfikuj **render**, z cache-bustem (CDN nazwa.pl) |
| Propozycja umowy albo klauzul | AGRIA działa na akcepcie mailowym. Nie proponować |
| Prośba o decyzję w sprawie pakietu OLX | Tylko wzmianka. Decyzja idzie telefonem Janka do Pawła |

---

## 7. Definition of done

- [ ] Liczby odświeżone na **1–31.08** ze wszystkich czterech źródeł (GSC, Ads, GA4, OLX) + indeksacja
- [ ] `docs/raporty/2026-08.md` zaktualizowany — pełny miesiąc, siedem materii z §3
- [ ] `docs/raporty/2026-08-mail.md` zaktualizowany — liczby, materie 3.5–3.7, ceny **5 600 netto
      za sierpień i 4 100 netto za wrzesień**, plan września z §4a, wzmianka o pakiecie OLX
- [ ] **Treść maila pokazana Jankowi INLINE w czacie** (nie sam link — chce czytać w jednym widoku)
- [ ] Pliki wystawione na `https://auratest.pl/fe4f58fec53ctmp/` z klikalnymi linkami w czacie
- [ ] Rejestr: wiersz 31.08 uzupełniony o finalne liczby, dziennik M3 domknięty
- [ ] Commit + push
- [ ] **Nic nie idzie do klienta** — wysyła Janek, 1–2.09
