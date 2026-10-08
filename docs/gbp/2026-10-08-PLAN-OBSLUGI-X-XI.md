# Wizytówki Google AGRII — plan obsługi październik–listopad 2026

> **Data:** 2026-10-08 · **Stan:** przygotowane, **nic nie wysłane i nic nie zmienione** na żadnym profilu.
> Źródła: `scripts/gbp_dump.py` → `tmp/gbp-tarnow.json` (08.10), Business Profile Performance API
> (dzienne metryki 01.06–07.10, frazy VI–X), Business Information API (profil Niedomic, kategorie),
> DataForSEO Google Maps (5 zapytań, ok. $0,01). Zastępuje „Mechanikę” z `2026-10-08-pazdziernik-publikacje.md`.

---

## 1. Diagnoza w liczbach

### Tarnów — wyniki (Performance API)

| | VI | VII | VIII | IX |
|---|---|---|---|---|
| Wyświetlenia (wyszukiwarka + Mapy) | 433 | 543 | 760 | 745 |
| Kliknięcia „zadzwoń” | 6 | 12 | 14 | 11 |
| Prośby o trasę | 50 | 43 | 45 | 58 |
| Kliknięcia w stronę | 3 | 4 | 9 | **16** |
| Czat | 0 | 0 | 0 | 0 |

Dane dzienne sięgają **04.10** (październik niedojrzały, nie porównuję). Tygodnie od poniedziałku, wyświetlenia:
31.08 **176** · 07.09 **190** (post 08.09) · 14.09 **228** · 21.09 **144** · 28.09 **45** (niedojrzałe).
**Wpływu postów nie da się z tego wyczytać** — jeden post i trzy pominięte w czterech tygodniach to za mało;
spadek w ostatnim tygodniu jest artefaktem opóźnienia danych, nie skutkiem ciszy. Wniosek praktyczny: rytm
trzymamy dla świeżości profilu, a efekt mierzymy kliknięciami w stronę i telefonami po 8 tygodniach regularności.

Frazy (VI–X, suma): **wapno nawozowe 396**, **agria 316**, **wapno 221** — reszta pod progiem 15
(m.in. „nawozy tarnów”, „hurtownie nawozów małopolskie”, „wapno nawozowe gdzie kupić”, ale też
„saletra amonowa tarnów”, „biostymulatory nawozy”, „grupa azoty sprzedaż nawozów” — ruch spoza oferty).

### Tarnów — profil

- Kategorie: **Dostawca nawozów** + Hurtownia produktów rolnych, Dostawca środków chemicznych dla rolnictwa,
  Dostawca materiałów budowlanych. Godziny pn–pt 8–16, bez godzin świątecznych (1.11 i 11.11 przed nami).
- **Usługi: lista pusta** (`serviceItems` = brak). Kategoria „Dostawca nawozów” nie ma predefiniowanych usług,
  więc zostają usługi własne (free-form) — tu leży najtańszy brak do domknięcia.
- Atrybuty: 3 (dostawa, WhatsApp, link do kalkulatora — T-119). Obszar: 4 województwa (T-120).
- Opis: aktualny merytorycznie; wymienia „sadownictwo, gospodarstwa rybackie, hurtownie”, czyli branże, które
  21.08 zdjęliśmy z nawigacji — **do decyzji, nie zmieniam**.
- Telefon główny **14 621 88 21** — jest też na `/kontakt/`, więc to nie błąd NAP. Kliknięcia „zadzwoń”
  z wizytówki trafiają na stacjonarny, nie do Pawła — warto, żeby Janek o tym wiedział przy rozliczaniu telefonów.
- Zdjęcia: **10, wszystkie z 02.07**, 2 zewnętrzne + 8 „dodatkowych”. Brak wnętrza, produktu, załadunku, transportu (T-050).
- Opinie: **9, średnia 4,3, ostatnia 28.02.2025**, wszystkie z odpowiedzią. **Proces z T-122 nie ruszył** —
  od 08.09 nie przyszła ani jedna opinia.
- Posty: 5, ostatni **08.09**; 16/23/30.09 nie wyszły.

### Konkurencja w Mapach (DataForSEO, punkt: Tarnów)

| Zapytanie | Wynik |
|---|---|
| „wapno nawozowe” | **AGRIA 1.**, Wamex (Wola Rzędzińska) 2. — tylko dwa wyniki |
| „wapno” (Tarnów) | **AGRIA 1.**, Wamex 2. |
| „nawozy” (Tarnów) | WIALAN 1. (**427 opinii**), Planta 2. (**83**), **AGRIA 3. (9)** |
| „wapno” (Niedomice) | **Agria Niedomice 1.** (5,0 · 8 opinii) |

Na swojej frazie AGRIA nie ma z kim przegrać. Na szerszym „nawozy” przegrywa liczbą opinii, nie trafnością —
9 wobec 83 i 427. **Wamex** ma **pięć pinezek** w powiecie (Zgłobice, Wola Rzędzińska, Ładna, Szynwałd,
Stare Żukowice) — to model, który AGRIA mogłaby mieć z trzema magazynami.

### Oddziały — tu jest najwięcej do zrobienia

- **Niedomice** (`locations/11295576611408862023`, na naszym koncie od 18.09): **8 opinii, średnia 5,0, ani jednej
  odpowiedzi**, w tym świeża z **20.08.2026**. Kategoria **„Zakład chemiczny”**,
  **brak WWW**, opis jednozdaniowy („Magazyn i centrum dystrybucji w Niedomicach”), 6 zdjęć, 0 postów.
  Mimo to pierwsza w Mapach na „wapno” przy magazynie.
- **Radgoszcz**: profil **istnieje w Mapach jako „Agria | Sklep”, Witosa 12, 33-207 Radgoszcz, 5,0 · 7 opinii,
  NIEPRZEJĘTY** (`is_claimed: false`, cid 12711310256069240814). Nie trzeba czekać na zaproszenie ani prosić
  właściciela — profil nie ma właściciela, można go **przejąć** z poziomu Map. Na koncie dziś go nie ma.

**Razem:** AGRIA ma w Mapach **24 opinie** (9 + 8 + 7), a zarządza odpowiedziami tylko na 9.

---

## 2. Działania w kolejności

### T-165 „odpowiedzi na 8 opinii Niedomic” — my, po akcepcie Janka
Najtańsza rzecz z największym efektem: 8 publicznych opinii bez słowa od firmy, w tym jedna z sierpnia.
`scripts/gbp_odpowiedz.py` ma zaszytą lokalizację Tarnowa — trzeba dodać parametr `--lokalizacja`
(zmiana w repo, nie na profilu). Odpowiedzi krótkie, każda inna, bez szablonu:

| Data | Ocena / treść | Proponowana odpowiedź |
|---|---|---|
| 20.08.2026 | 5, bez treści | Dziękujemy za ocenę. Zapraszamy po kolejny transport — magazyn w Niedomicach czynny pn–pt 8–16. |
| 28.02.2025 | 5, „Polecam bardzo” | Dziękujemy, miło nam to czytać. |
| 28.02.2025 | 5, „szeroki asortyment, fachowe doradztwo” | Dziękujemy. Doradztwo w doborze wapna do gleby to dla nas część sprzedaży, nie dodatek — zapraszamy ponownie. |
| 22.02.2025 | 5, „Mega mili i profesjonalni pracownicy!” | Dziękujemy w imieniu całego zespołu z Niedomic. |
| 02.08.2024 | 5, „Najlepsza firma… (szczególnie pan Paweł)” | Dziękujemy — przekazaliśmy panu Pawłowi. Cieszymy się, że rada się sprawdziła. |
| 06.02.2024 | 5, „Polecam” | Dziękujemy za polecenie. |
| 24.01.2022 | 5, bez treści | Dziękujemy za ocenę. |
| 23.01.2022 | 5, „Polecam” | Dziękujemy i zapraszamy ponownie. |

⚠️ Opinia z 02.08.2024 przytacza fragment o radzie Pawła — pełną treść przeczytać przed wysyłką (zrzut ucina).
Kontrola: zrzut opinii Niedomic po wysyłce — 8/8 z `reviewReply`.

### T-166 „profil Niedomic — kategoria, WWW, opis” — my, po akcepcie Janka
Zrzut przed zmianą (`gbp_dump.py` z lokalizacją Niedomic). Zmiany:
- kategoria główna **Zakład chemiczny → Dostawca nawozów** (jak Tarnów), dodatkowa: Hurtownia produktów rolnych;
- WWW: `https://agria.pl/` (z UTM `?utm_source=google&utm_medium=organic&utm_campaign=gbp-niedomice`, żeby GA4 odróżniło oddział);
- opis (propozycja, ok. 450 znaków): *„Magazyn AGRII w Niedomicach — wapno nawozowe tlenkowe, węglanowe i węglanowo-magnezowe,
  kreda nawozowa i pastewna. Wydajemy towar luzem i w big-bagach, organizujemy transport całosamochodowy
  na gospodarstwa w Małopolsce i na Podkarpaciu. Doradzamy dobór wapna do odczynu i kategorii gleby —
  dawkę można policzyć w kalkulatorze na agria.pl. AGRIA działa od 1989 roku, centrala w Tarnowie.”*
  (bez marek producentów i bez cen — zgodnie z `feedback_agria_nazwy_producent_nie_marka`);
- atrybuty jak Tarnów (dostawa, WhatsApp 664 393 062 — to numer Niedomic, link do kalkulatora).
Kontrola: zrzut „po” + Mapy na „wapno” przy Niedomicach (dziś 1. miejsce — nie może spaść).
⚠️ **Reguła z memory „przemilczeć multi-location w komunikacji do klienta” przestała pasować do Niedomic** (dostęp
od 18.09) — do decyzji Janka, czy wpisujemy oddział do raportu.

### T-167 „przejęcie profilu Radgoszcz” — AGRIA przez Janka (weryfikacja wymaga ich telefonu/obecności)
Profil „Agria | Sklep”, Witosa 12, nieprzejęty. Ścieżka: Mapy → profil → „Zarządzaj tym profilem / Jesteś właścicielem?”
z konta, które ma Tarnów i Niedomice → weryfikacja (telefon na numer z profilu, SMS albo nagranie wideo miejsca —
Google wybiera metodę). **Wideo musi nagrać ktoś na miejscu w Radgoszczy** (Kazimierz, 781 875 411) — szyld, magazyn,
dowód prowadzenia działalności. Do potwierdzenia przy okazji: czy adres Witosa 12 jest aktualny
(`FAKTY_KLIENTA.md` podaje tylko miejscowość). Po przejęciu: ten sam pakiet co T-166.
Kontrola: lokalizacja widoczna na koncie (`accounts/…/locations`), `hasVoiceOfMerchant: true`.

### T-168 „usługi na wizytówce Tarnów” — my, po akcepcie Janka
Lista pusta. Propozycja 7 usług własnych (nazwa + 1 zdanie + bez cen): Wapno nawozowe tlenkowe ·
Wapno nawozowe węglanowe · Wapno węglanowo-magnezowe · Kreda nawozowa (granulowana i sypka) · Kreda pastewna ·
Wapno hydratyzowane · Transport całosamochodowy na gospodarstwo. Opisy z kart produktów
(`docs/produkty/`), zapis przez `gbp_patch.py` z maską `serviceItems` — skrypt trzeba rozszerzyć o struktury
(dziś wysyła tylko stringi, znane z T-120). Ten sam zestaw idzie potem do Niedomic.
Kontrola: zrzut „po”, render w Mapach (zakładka „Usługi”).

### T-169 „karta opinii z QR na WZ” — AGRIA przez Janka (dopływ opinii)
T-122 dało link i dwa zdania SMS; nic nie przyszło, bo prośba wymaga pamiętania. Karta wkładana do WZ/faktury
działa bez pamiętania. **Gotowe pliki:**
- `docs/gbp/2026-10-08-opinie/karta-opinii-A4-4szt.html` — 4 karty na A4, do druku i cięcia;
- `docs/gbp/2026-10-08-opinie/qr-opinia-tarnow.svg` / `.png` — sam kod (np. na pieczątkę, druk WZ).
QR prowadzi do okna opinii **Tarnowa** (`newReviewUri`). ⚠️ **Kod nie zdekodowany maszynowo** (brak dekodera
na serwerze) — Janek sprawdza telefonem przed drukiem.
⚠️ Reguła 08.09 „opinie wyłącznie na Tarnów” — przy 8 + 7 opiniach na oddziałach do ponownej decyzji:
klient odbierający w Niedomicach zna Niedomice, nie Tarnów.
Kontrola: liczba opinii Tarnowa co 2 tygodnie (dziś 9); cel z T-122 — kilka miesięcznie.

### T-170 „posty X–XI + godziny świąteczne” — my, wtorkami
**Październik** (wsady gotowe, `gbp_post.py` przechodzi walidację bez `--wyslij`):
| Wtorek | Wsad | Zdjęcie |
|---|---|---|
| 13.10 | `tmp/gbp-posty/2026-10-13-tlenkowe-czy-weglanowe.json` | `2026/03/ofirmie2.jpg` (JPG ✓) — zmienione z `agria-product-bg-1.jpg`, bo to samo zdjęcie ma ostatni post z 08.09 |
| 20.10 | `tmp/gbp-posty/2026-10-20-staw-kreda-czy-wapno.json` | ⚠️ `2026/10/kreda-do-stawu-staw-karpiowy-jesienia.jpg` **nie istnieje** — konwersja z `.webp` po „ok” |
| 27.10 | `tmp/gbp-posty/2026-10-27-ph-gleby-tester-czy-laboratorium.json` | ⚠️ `2026/10/ph-gleby-pomiar-odczynu-w-polu.jpg` **nie istnieje** — konwersja z `.webp` po „ok” |
| 03.11 | `tmp/gbp-posty/2026-11-03-kalkulator-magnez.json` | `2026/09/gbp-wapnowanie-efekty-przed-po.jpg` (JPG ✓) |

Wsady 20.10 i 27.10 mają pole `_UWAGA` — usunąć przed `--wyslij`.

**Listopad — tematy:**
| Wtorek | Temat | Adres | Warunek |
|---|---|---|---|
| 10.11 | Kreda pastewna to nie to samo co nawozowa | `/paszarstwo/` | **tylko po odpowiedzi Pawła (T-077)** — dawka z wrześniowego tekstu jest pod znakiem zapytania |
| 17.11 | Wapno pod ziemniaki — kiedy, żeby nie było parcha | `/wapno-pod-ziemniaki/` | treść z poradnika T-074 |
| 24.11 | Wapnowanie osadów w oczyszczalni — palone czy hydratyzowane | `/wapno-do-oczyszczalni/` | rynek całoroczny, nie sezonowy |
| 01.12 | Atesty i karty produktów do pobrania | `/do-pobrania/` | bez nowych liczb — 17 kart jest na stronie |
(Zapas na 10.11, jeśli T-077 nie ruszy: wapno granulowane — szczyt sierpniowy minął, ale frazy X są wysokie.)

**Godziny świąteczne** (`specialHours`, oba profile): **1.11 (niedziela) — bez zmian**, **11.11 (środa) — zamknięte**.
Grudzień osobno: **24.12 (czwartek) — zamknięte**, od 2025 Wigilia jest ustawowo wolna; do potwierdzenia u AGRII, czy 2.11 i 31.12 pracują normalnie. Zapis listopadowy do 06.11, grudniowy do 15.12.
Kontrola: zrzut publikacji w każdy wtorek, metryki tygodniowe po 8 tygodniach (od 13.10 do 08.12).

### T-050 „zdjęcia od AGRII” (istniejące, wznowić) — AGRIA przez Janka
Konkretna lista ujęć, telefonem, w poziomie, w dzień:
1. Wjazd i szyld w Tarnowie (Warsztatowa 5) — to zdjęcie widzi każdy, kto prosi o trasę (58 próśb we wrześniu).
2. Plac w Niedomicach z pryzmą wapna luzem.
3. Big-bagi na placu — z bliska, widać opakowanie.
4. Załadunek ładowarką na ciężarówkę.
5. Ciężarówka z towarem na wyjeździe (bez tablic rejestracyjnych na zdjęciu albo do zamazania).
6. Worki 25/30 kg na palecie.
7. Biuro / ludzie przy pracy — 1 zdjęcie zespołu, jeśli zgodzą się na wizerunek.
8. Radgoszcz — szyld i magazyn (od razu do T-167).
Nie generujemy zastępników — to zdjęcia firmy na jej własnym profilu.

---

## 3. Kto i kiedy

| Zadanie | Kto | Blokada | Termin |
|---|---|---|---|
| T-165 odpowiedzi Niedomice | my | akcept treści | ten tydzień |
| T-166 profil Niedomic | my | akcept + decyzja „multi-location w raporcie” | ten tydzień |
| T-170 post 13.10 | my | akcept tekstów, „ok” na 2 konwersje JPG | 13.10 |
| T-168 usługi Tarnów | my | akcept listy, rozszerzenie `gbp_patch.py` | do 20.10 |
| T-169 karta z QR | AGRIA (druk) | Janek sprawdza QR, przekazuje Pawłowi | do 20.10 |
| T-167 Radgoszcz | AGRIA (Kazimierz na miejscu) + Janek | weryfikacja Google | do 31.10 |
| T-050 zdjęcia | AGRIA | lista ujęć do Pawła | do 31.10 |
| godziny 11.11 | my | potwierdzenie AGRII | do 06.11 |

## 4. Proponowane wiersze do REJESTRU (nie wpisane)

```
| **T-165** | Odpowiedzi na 8 opinii Niedomic (zero odpowiedzi, 5,0) `[A 08.10]` | R | Treści w docs/gbp/2026-10-08-PLAN-OBSLUGI-X-XI.md §2; gbp_odpowiedz.py dostaje --lokalizacja |
| **T-166** | Profil Niedomic: kategoria „Zakład chemiczny” → Dostawca nawozów, WWW, opis, atrybuty `[A 08.10]` | R | j.w.; zrzut przed i po |
| **T-167** | Przejęcie profilu Radgoszcz („Agria | Sklep”, Witosa 12, 5,0 · 7 opinii, nieprzejęty) `[A 08.10]` | R | weryfikacja przez AGRIĘ na miejscu; zastępuje część Radgoszcza w T-047 |
| **T-168** | Usługi na wizytówce Tarnów — lista pusta, 7 usług własnych `[A 08.10]` | R | wymaga struktur w gbp_patch.py |
| **T-169** | Karta opinii z QR do WZ (dopływ opinii — T-122 nie ruszyło) `[A 08.10]` | R | docs/gbp/2026-10-08-opinie/ |
| **T-170** | Posty wtorkowe X–XI (8) + godziny świąteczne 11.11 `[A 08.10]` | R | wsady tmp/gbp-posty/2026-10-*, 2026-11-03 |
```

---

## Prompt kontynuacyjny

```
Pracujemy w ~/projekty/agria — wątek WIZYTÓWKI GOOGLE. Przeczytaj
docs/gbp/2026-10-08-PLAN-OBSLUGI-X-XI.md i memory project_agria_gbp_rytm_publikacji.

Stan 08.10: nic nie wysłane. Gotowe: odpowiedzi na 8 opinii Niedomic (T-165), pakiet profilu
Niedomic (T-166), 4 wsady postów X (T-170, tmp/gbp-posty/), karta z QR (T-169).
Kolejność: (1) akcept Janka per pozycja, (2) gbp_odpowiedz.py --lokalizacja + wysyłka T-165,
(3) zrzut + T-166, (4) konwersja 2 webp→JPG po „ok” i post 13.10 we wtorek,
(5) rozszerzenie gbp_patch.py o serviceItems → T-168.
Każda zmiana: gbp_dump.py przed, zrzut po, wpis w REJESTRZE w tym samym commicie.
Nic do klienta bezpośrednio — materiał dla AGRII (karta, lista zdjęć, Radgoszcz) przez Janka.
```
