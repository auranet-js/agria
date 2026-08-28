# Recheck OLX — trzy dni po przełożeniu 68 ogłoszeń (T-106)

> **Termin:** poniedziałek 31.08.2026 · **Założone:** 28.08.2026 · **Projekt:** `agria`
> **Commit wykonania:** `161f041` · **Poprzedni kontekst:** `docs/raporty/2026-09-OLX_WYNIKI_CYKL_1.md`
>
> **Po co ten recheck:** moderacja OLX wydaje werdykt **po fakcie i po cichu**, a 28.08 zmieniliśmy
> 68 z 200 ogłoszeń — 60 zmieniło miejscowość, 8 zmieniło miejscowość i produkt. Kontrola zaraz po
> serii pokazała czysto, ale trzy dni to pierwszy termin, w którym cisza naprawdę coś znaczy.
> Drugi powód: pomiar pozycji z 28.08 poszedł **przed pełnym przeindeksowaniem** i wymaga powtórzenia.

---

## 1. Co się stało 28.08 — w skrócie

**68 ogłoszeń przeniesionych z pasa 200–375 km do pasa 2–98 km od magazynów** w Niedomicach
i Radgoszczy. Siatka **53 → 60 miejscowości**. Podstawa: 21 z 22 kontaktów pierwszego cyklu
przyszło z promienia do 200 km, a 68 ogłoszeń stojących dalej dało razem **jeden**.

| Seria | Ile | Co się zmieniło | Ryzyko |
|---|---:|---|---|
| **A** | 60 | samo `location.city_id` | niskie — jedno pole, ładunek z `putable()` |
| **B** | 8 | miejscowość **i produkt** (sloty kredy pastewnej) | wyższe — pełna podmiana treści + **nowy `external_id`** |

Kreda pastewna zeszła z 12 pozycji do 4: rynek paszowy siedzi w kategoriach 765 i 761, a pakiet
obejmuje **wyłącznie 4368**, więc przeniesienia kategorii nie da się zrobić.

**Z 19 miast wycofaliśmy się całkowicie** (Warszawa, Wrocław, Poznań, Łódź, Kalisz, Siedlce, Mława,
Radzyń Podlaski, Płock, Płońsk, Konin, Kępno, Ostrów Wlkp., Ciechanów, Ostrołęka, Sokołów Podlaski,
Łowicz, Legnica, Izbicko).

**Korekta doboru w 2 z 8 slotów serii B** (decyzja Janka 28.08, po pytaniu „co trenduje w okolicy"):
Sandomierz dostał **Oxyfertil 90**, Dąbrowa Tarnowska **węglanowe odm. 04** — zamiast kredy
granulowanej. Podstawa: dwa niezależne pomiary regionalne zgodnie wskazały te produkty.
**Bochnia świadomie została** przy kredzie granulowanej, bo tam sygnały są sprzeczne.

---

## 2. Punkty odniesienia — z czym porównywać

**Zwrot własny w pierścieniu ≤200 km (28.08, 7,88 dnia emisji):**

| Produkt | Kontaktów na ogłoszenie |
|---|---:|
| Oxyfertil 90 | 0,50 (próba 6 ogłoszeń — mała) |
| Węglanowe odm. 04 | 0,36 (14 ogłoszeń, 5 kontaktów — największa próba) |
| Kreda granulowana | 0,22 |
| Agrobielik 70 (gleba) | 0,15 |
| Agrobielik 90 | 0,12 |
| **Kreda pastewna** | **0,00** (2 odsłony na 4 ogłoszenia) |

**Pierścienie odległości (cała siatka, 28.08):** 0–60 km **0,065** · 60–120 km **0,270** ·
120–200 km 0,141 · 200–300 km 0,017 · >300 km 0,000.

**Podaż konkurencji, MŁP+PDK+ŚWK (snapshot 28.08, kat. 4368):** granulowane **94** oferty ·
z magnezem 64 · kreda i węglanowe sypkie **28** · tlenkowe **27** · pastewna **1**.

**Statystyki całości 28.08 15:01:** 200 ogłoszeń, **634 odsłony, 22 odsłony numeru**, 21 obserwujących.

---

## 3. Co zrobić — po kolei

```bash
cd ~/projekty/agria && git pull

# (1) czy wszystkie żyją — 3 dni to pierwszy termin, w którym cisza moderacji coś znaczy
python3 scripts/olx/post_adverts.py --check          # oczekiwane: 200 w rejestrze, wszystkie active

# (2) czy 68 przełożonych stoi tam, gdzie ma — odczyt PER OGŁOSZENIE, nie lista zbiorcza
python3 scripts/olx/przeloz.py --sprawdz             # oczekiwane: "zgodnych z projektem: 68/68"

# (3) POWTÓRZYĆ pomiar pozycji — ten z 28.08 poszedł przed przeindeksowaniem
python3 scripts/olx/pozycje.py
#     zapisuje pod pozycje-YYYY-MM-DD.json; porównaj z pozycje-2026-08-28-po-przelozeniu.json
#     UWAGA: baseline SPRZED przekładki to pozycje-2026-08-28.json — NIE nadpisz go

# (4) pierwszy odczyt zwrotu po zmianie
python3 scripts/olx/statystyki.py

# (5) pakiet — ile zostało do 16.09
~/bin/olx-agria api /partner/users/me/packets
```

**Konkretne miejsca do obejrzenia okiem (Chrome MCP), jeśli coś w (1)–(2) zgrzyta:** Sandomierz
(Oxyfertil 90 — produkt zmieniony, ID 1092690465), Radgoszcz (węglanowe odm. 04, ID 1092698373),
Żabno (Agrobielik 90, ID 1092694731).

---

## 4. Na co patrzeć w liczbach

1. **Czy pierścień 0–60 km ruszył.** Rósł z 31 do 73 pozycji, a miał najgorszy wynik z bliskich
   (0,065). To jest **główna niewiadoma całej operacji** — nowe miejscowości blisko magazynów mają
   zarazem **najgęstszą konkurencję w siatce**: Połaniec 245, Żabno i Lisia Góra po 242, Radgoszcz
   i Dąbrowa Tarnowska 241 ogłoszeń w promieniu 50 km.
2. **Czy górskie pracują.** Najrzadsze rynki i najlepsze pozycje od pierwszego dnia: Lubień
   (101 ofert, pozycja 10), Mszana Dolna (110, poz. 10), Grybów (114, poz. 18). Jeśli kontakty mają
   skądkolwiek przyjść szybko, to stamtąd.
3. **Czy zamienniki biją kredę pastewną.** Osiem slotów, które dawały zero — teraz węglanowe odm. 04
   ×4, Agrobielik 70 gleba ×2, Oxyfertil 90 ×1, kreda granulowana ×1.
4. **Trzy dni to za mało na wnioski o skuteczności.** Ten recheck sprawdza, czy **mechanizm działa**
   — nie czy decyzja była słuszna. Na to jest kontrola **11.09**.

---

## 5. Pułapki — ktoś już na nie wszedł

- **Nie przeliczaj `przelozenie.py`.** Przydział jest zachłanny i liczy od stanu rejestru: 28.08
  przeliczenie po pilocie na 3 sztukach **przetasowało 56 z 65 pozycji**. Skrypt ma teraz twardy
  guard, który to blokuje; `--mimo-serii` przełamuje go **tylko świadomie**.
- **`adverts-payload.json` musi iść razem z każdym `PUT`-em.** Inaczej pierwszy
  `post_adverts.py --update` **cofnie wszystkie miasta** do stanu sprzed przekładki.
- **Klucze `external_id` serii A są historyczne** — niosą `city_id` sprzed przekładki. Prawda
  o miejscu i produkcie siedzi w **jawnych polach** `posted.json`: `city`, `city_id`, `wariant`.
  Nie wyprowadzaj wiedzy z nazwy klucza. Seria B ma klucze nowe, ze starym w `poprzedni_external_id`.
- **`PUT` podmienia CAŁY zasób.** Ładunek zawsze przez `putable()` z odpowiedzi `GET` — jedno
  pominięte pole kasuje numer telefonu, czyli kanał dający wszystkie kontakty.
- **Nie klikaj „Wyświetl numer" na własnym ogłoszeniu.** To generuje zdarzenie `phone_view`
  i fałszuje jedyną metryką kontaktu, jaką mamy.
- **Lista zbiorcza `GET /partner/adverts` oddaje statusy z opóźnieniem** — wiarygodny jest odczyt
  `GET /partner/adverts/{id}` per ogłoszenie.
- **Nie dotykaj crontaba** inaczej niż przez `~/bin/cron-install` (`monitor.py` 7:25 codziennie,
  `statystyki.py` poniedziałki 7:35 — w dniu rechecku zdąży już pójść sam).

---

## 6. Czym się kończy

- Wpis w **DZIENNIKU** `docs/REJESTR_ZOBOWIAZAN.md` z wynikiem trzech odczytów.
- Jeśli coś wypadło ze statusu `active` — **wycofanie z backupu**
  `data/backups/T-106-olx-przed-2026-08-28.json` (68 pełnych stanów sprzed).
- Czysty pomiar pozycji jako punkt odniesienia dla **kontroli 11.09**.
- Event oznaczony `✅` w kalendarzu „Auranet Claude".

---

## 7. Termin nadrzędny, ważniejszy niż ten recheck

**Pakiet wygasa 16.09, decyzja o odnowieniu do 10.09 (T-105).** Bez odnowienia **wszystkie 200
ogłoszeń gasną jednego dnia** — `auto_extend` żyje tylko dopóki żyje pakiet (precedens 18.07).
Rekomendacja Auranet: **odnawiamy 200, bez zmiany progu**. Pytanie do Pawła idzie **telefonem**,
z liczbą: koszt kontaktu 12–15 zł netto wobec 103 zł w Ads w tym samym oknie.

**Sekrety:** `~/secrets/olx/`, token `~/domains/auratest.pl/olx-private/agria-tokens.json`.
**Memory:** `project_agria_olx_kanal` · `reference_agria_olx_api`.
