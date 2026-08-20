# Prompt startowy — T-041 OLX, warstwa zdjęć przed emisją (20.08.2026)

> Poprzedni etap: **T-042 domknięty 20.08** (commit `288d979`) — korekta tytułu AGR-001
> („gleb ciężkich" → „gleb średnich i ciężkich") w czterech warstwach. **Treści ogłoszeń
> zaakceptowane przez Janka 20.08** w wersji z tą poprawką; punkt odniesienia:
> `https://auratest.pl/fe4f58fec53ctmp/agria-olx-ogloszenia-final-2026-08-17.html`
> (wygenerowany 17.08, więc pokazuje tytuł SPRZED korekty — treść merytoryczna aktualna).
>
> Wszystkie liczby poniżej zmierzone **20.08**: `curl` na 27 URL-i, `identify`, API OLX,
> `json.load` na payloadzie. Nie przepisane z dokumentów.

---

## Prompt do skopiowania

```
Wątek: AGRIA, T-041 — przygotowanie warstwy ZDJĘĆ do emisji 200 ogłoszeń na OLX.
Treści są zaakceptowane i zamknięte, publikacja czeka wyłącznie na pakiet Premium 200
po stronie AGRII. Zanim ruszy emisja, trzeba domknąć zdjęcia: co mamy, co dostaniemy
od klienta, co trzeba dorobić lub wygenerować — z oglądem tego, jak robi to konkurencja.

Przeczytaj najpierw:
- docs/REJESTR_ZOBOWIAZAN.md (T-041, T-042, sekcja „Czeka na AGRIĘ")
- docs/offers/2026-08-PLAN_OLX.md
- scripts/olx/zdjecia.py (dlaczego plansze są cięte i skąd zniknął kod QR)
- scripts/olx/build_adverts.py (słowniki FOTO i GALERIE — tam siedzi dobór zdjęć)
- memory: project_agria_olx_kanal, reference_agria_olx_api,
  feedback_agria_bez_zargonu_loco, feedback_agria_params_from_datasheets

STAN ZMIERZONY 20.08 — punkt wyjścia, nie zakładaj innego:

Payload `data/olx/adverts-payload.json`: 200 ogłoszeń, 11 kart produktowych,
53 miejscowości. Zdjęć na ogłoszenie: 5 (w 123 ogłoszeniach), 6 (w 52), 7 (w 25).
27 unikalnych URL-i, WSZYSTKIE odpowiadają HTTP 200 (sprawdzone 20.08).

Trzy źródła zdjęć, każde z innym problemem:

1. Plansze Auranetu, cięte na połówki — `https://auratest.pl/agria-olx/agria-*.jpg`,
   10 sztuk w użyciu. WSZYSTKIE mają 435×700 px. To jest najsłabszy punkt całego
   zestawu: pierwsze zdjęcie decyduje o kliknięciu z listy, a 435 px szerokości to
   miniatura, nie zdjęcie. Konkurencja wystawia kadry rzędu 3000×4000.
2. Trzy kadry z CDN OLX (hero „WAPNA NAWOZOWE" z ciągnikiem, palety worków,
   big-bagi w magazynie), 1000×700 — pochodzą ze STARYCH ogłoszeń AGRII.
   Sprawdź, czy przetrwają wygaśnięcie tamtych ogłoszeń; jeśli nie, trzeba mieć
   własne kopie pod własnym URL-em.
3. Trzynaście zdjęć z kart produktowych agria.pl (format .webp, 170–510 KB).
   Do zweryfikowania, czy Partner API przyjmuje webp — jeśli nie, konwersja.

Luka jawna: kreda pastewna NIE MA własnej planszy. Jej ogłoszenia otwiera ogólny
kadr „hero", a nie produkt (build_adverts.py, zbiór BEZ_PLANSZY).

CO ZROBIĆ, w tej kolejności:

1. KONKURENCJA — najpierw fakty, potem opinie.
   Snapshot `data/olx/market/2026-08-07.json` (2 486 ofert kategorii 4368, z tego
   782 o wapnie/kredzie) NIE zawiera zdjęć — pola photo/image są puste, zero wystąpień.
   Ale publiczne API je zwraca; zweryfikowane 20.08:
     https://www.olx.pl/api/v1/offers/?offset=0&limit=50&category_id=4368&query=wapno
   pole `photos[]` → `link` (CDN, wzorzec `image;s={width}x{height}`) + width/height.
   Zbierz próbkę wapno/kreda i policz: mediana liczby zdjęć na ogłoszenie, typowe
   wymiary i orientacja, udział zdjęć realnych (hałda, big-bag, rozsiewacz) wobec
   plansz z tekstem i cennikiem. Potem OBEJRZYJ kilkanaście czołowych — liczby nie
   powiedzą, czy kategoria wygląda na fotografię z podwórka czy na grafikę handlową.
   Punkt odniesienia po wolumenie: AGRO-KOTYNIA (162 ogłoszenia), „699-712-071" (103),
   DAREK (70), Agro-Siew (58), Tadeusz (40), Wapna Świętokrzyskie (38).

2. CO MAMY I CO BĘDZIEMY MIEĆ.
   Zinwentaryzuj własne materiały: `assets/print/` (katalog 2026, ulotka DL),
   zdjęcia z kart produktowych, plansze źródłowe w `~/domains/auratest.pl/public_html/
   agria-olx/.plansze`. Osobno wypisz, czego fizycznie nie ma i czego nie da się
   dorobić bez klienta — zdjęcia magazynów Niedomice i Radgoszcz, załadunku, big-bagów
   na placu. To idzie do Janka jako pytanie do Pawła TELEFONEM, nie mailem z tabelą.

3. CO WYGENEROWAĆ i GDZIE PRZEBIEGA GRANICA.
   Rozstrzygnij z Jankiem, zanim cokolwiek wygenerujesz: ogłoszenie sprzedażowe ma
   pokazywać rzeczywisty towar. Grafika produktowa, plansza z parametrami, wizualizacja
   frakcji, przekrój dawkowania — tak. Fotorealistyczne „zdjęcie" magazynu albo dostawy
   AGRII, której nie było — nie, bo to wprowadza kupującego w błąd i jest zaczepne
   regulaminowo. Zaproponuj podział materiału na te dwie kategorie i pokaż go do decyzji.
   Narzędzia: Freepik API (`~/secrets/freepik/api-key.txt`, Mystic) i Gemini/nanobanana,
   jeśli rozszerzenie jest w tej sesji dostępne — sprawdź, nie zakładaj.

4. WYMOGI TECHNICZNE OLX. Ustal z dokumentacji Partner API: maksymalna liczba zdjęć
   na ogłoszenie, dopuszczalne formaty, minimalne wymiary, czy OLX zaciąga plik z URL-a
   raz i trzyma u siebie (od tego zależy, czy nasze adresy na auratest.pl muszą żyć
   tylko w chwili publikacji, czy stale). Dziś wysyłamy zdjęcia jako listę URL-i —
   `scripts/olx/post_adverts.py`, pole `images`.

TWARDE OGRANICZENIA, nie do negocjacji:
- Zero kodów QR i zero adresów WWW na zdjęciach. Regulamin OLX traktuje zdjęcia jako
  treść ogłoszenia, więc kod prowadzący na zewnątrz jest tam odnośnikiem. Plansze były
  już z tego powodu retuszowane — nie cofaj tego.
- Zero numeru telefonu na zdjęciu i w opisie. Kontakt wyłącznie w polach formularza.
- Jedno ogłoszenie = jeden produkt. Kadr z dwoma produktami obok siebie był powodem,
  dla którego plansze w ogóle tniemy.
- Parametry na grafikach wyłącznie z kart producentów (Nordkalk, Lhoist) i z kart
  produktowych agria.pl. Zero liczb z rozumowania.
- Język bez żargonu: „cena za towar, bez transportu", nigdy „loco magazyn".

NARZĘDZIA NA MIEJSCU: ImageMagick (`convert`, `identify`) jest. Pillow NIE MA —
nie pisz kodu na PIL. Skrypty warstwy zdjęć: `scripts/olx/zdjecia.py` (cięcie plansz,
zamalowanie plakietki QR), `scripts/olx/build_adverts.py` (słowniki FOTO i GALERIE).
Po zmianie zdjęć payload trzeba przebudować build_adverts.py i zwalidować `json.load`.

ZROBIONE = każda z 11 kart produktowych ma komplet zdjęć spełniających wymogi OLX,
pierwszy kadr pokazuje TEN produkt, kreda pastewna ma własny materiał, zero QR,
payload przebudowany i zwalidowany, zestaw wystawiony Jankowi do akceptu jako tabela
HTML na auratest.pl. Publikacja NIE rusza — czeka na pakiet Premium po stronie AGRII.
```

## Czego ten wątek NIE dotyka

- **Treści ogłoszeń** — zaakceptowane 20.08, zamknięte jako T-042. Nie otwieraj ich
  ponownie „przy okazji"; ewentualna zmiana wymaga osobnej decyzji Janka.
- **Publikacji** — T-041 czeka na pakiet Premium 200 (1 199,99 zł brutto), który kupuje
  AGRIA. Do tego czasu żadnego `post_adverts.py` w trybie wysyłki.
- **Siatki miast** — 53 miejscowości ustalone, `scripts/olx/grid.py`.
- **Pozostałych pozycji kolejki M3** (T-046 GBP, T-039 Ads, T-026 indeksacja) — osobne wątki.
