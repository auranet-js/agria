# Prompt startowy — T-041, publikacja 199 ogłoszeń OLX (20.08.2026)

> Poprzedni etap: **T-049 domknięty 20.08** (commity `1bc2928`, `6157c49`) — warstwa zdjęć,
> tytuły i opisy. Ogłoszenie pilotowe **1089946612 jest `active` i widoczne publicznie**
> po poprawce pod pkt 4.4.c Regulaminu. **Akcept na uruchomienie mam od Janka 20.08.**
>
> Wszystkie liczby poniżej zmierzone **20.08**: Partner API, `json.load` na payloadzie,
> `curl` na 56 adresach zdjęć. Nie przepisane z dokumentów.

---

## Prompt do skopiowania

```
Wątek: AGRIA, T-041 — publikacja 199 ogłoszeń OLX z gotowego payloadu.
Treści, zdjęcia i spięcie z Partner API są zrobione i zaakceptowane. To jest wątek
wyłącznie wykonawczy: wystawić, dopilnować moderacji i auto_extend, zebrać dowód.

Przeczytaj najpierw:
- docs/REJESTR_ZOBOWIAZAN.md (T-041, T-049 w dzienniku M3)
- scripts/olx/post_adverts.py (tryby, rejestr posted.json, pułapka auto_extend)
- scripts/olx/build_adverts.py (co jest wymuszone kodem, czego nie wolno cofnąć)
- docs/prompty/2026-08-20-PROMPT_T-041_ZDJECIA.md (poprzedni etap, dla kontekstu)
- memory: project_agria_olx_kanal, reference_agria_olx_api

STAN ZMIERZONY 20.08 — punkt wyjścia, nie zakładaj innego:

Payload `data/olx/adverts-payload.json`: 200 ogłoszeń, 11 kart, 53 miejscowości.
Tytuły 118–138 znaków (limit 150). Opisy 3 518–4 479 znaków (limit 9 000).
Zdjęć na ogłoszenie: 7 w 186 pozycjach, 6 w 14 (kreda nawozowa granulowana — brak zdjęcia
studyjnego, bo karta ID 305 ma na produkcji podpięte zdjęcie innego produktu).
56 unikalnych adresów zdjęć, wszystkie odpowiadają HTTP 200, wszystkie z /agria-olx/v2/.
Miniatur 12 — po jednej na siatkę, wariantów „-kontekst" i „-pryzma" z pierwszego podejścia
w payloadzie NIE MA (sprawdzone: 0 wystąpień).

Ogłoszenie pilotowe 1089946612 na koncie zgadza się z payloadem co do znaku: ten sam tytuł
(123 zn.), ten sam opis (3 849 zn.), 7 zdjęć, status `active`. To jest wersja, która przeszła
moderację — payload i produkcja nie rozjeżdżają się.

Rejestr `data/olx/posted.json`: JEDNA pozycja — pilot 1089946612 (Zator).
Do wystawienia zostaje 199. post_adverts.py nigdy nie wystawi drugi raz tego samego
external_id, więc pilot sam wypadnie z kolejki.

Pakiet: „Pakiet 200 ogłoszeń premium", kategoria Rolnictwo–Nawozy, aktywny do
16.09.2026 12:11, zużyte 1 z 200. Odczyt: GET /partner/users/me/packets.
UWAGA: OLX_BASELINE_2026-08-07.md twierdzi, że pakietów nie ma w API — to nieprawda,
endpoint działa. Popraw tamten wiersz przy okazji.

CO ZROBIĆ, w tej kolejności:

1. TOKEN. `olx-agria refresh` przed startem. Token żyje 24 h i 20.08 padł w środku
   operacji — PUT zwrócił 401 invalid_token w połowie zadania.

2. TRZY FAZY, NIE „PARTIAMI NA OKO".
   Kluczowy pomiar 20.08: **200 ogłoszeń to tylko 17 wariantów treści**. Unikalnych tytułów
   jest 12, unikalnych zestawów zdjęć 12, unikalnych kombinacji tytuł+opis 17 (te dodatkowe
   pięć to akapit o naborze łódzkim doklejony na 12 ogłoszeniach z region_id 7). Największa
   grupa to 30 ogłoszeń o IDENTYCZNEJ treści, różniących się wyłącznie miastem.
   Moderator ocenia treść, nie liczbę — ma do oceny siedemnaście rzeczy, nie dwieście.

   FAZA 1 — po jednym ogłoszeniu na każdy z 17 wariantów, każde z innego miasta.
   To pokrywa 100 % przestrzeni ryzyka. Odpytuj statusy co minutę — POMIAR Z 20.08:
   po poprawce ogłoszenie przeszło z `new` na `active` w NIECAŁE 20 SEKUND. Wcześniejsza
   próba, ta odrzucona, siedziała w `new` dłużej i werdykt `moderated` przyszedł po kilku
   minutach. Czyli: kwadrans odpytywania wystarcza, godzina to marnowanie czasu.
   Nie ma trybu „wystaw wybrane warianty" — dopisz go albo wyfiltruj payload do listy
   external_id i podaj ją skryptowi.

   FAZA 2 — dopiero po potwierdzeniu, że 17 przeszło: reszta (182) partiami po 20–30,
   z krótkimi przerwami na odczyt statusów (nie na przeczekanie moderacji — ta jest szybka). Pozostałe ogłoszenia to permutacje treści, którą OLX już zaakceptował.
   Nikt nie musi przy tym siedzieć: `posted.json` zapisuje się po KAŻDYM ogłoszeniu,
   więc przerwanie w połowie niczego nie psuje — kolejne uruchomienie dokłada resztę.
   Rozważ crona na Elarze zamiast trzymania sesji.

   FAZA 3 — kontrola: rozkład statusów, auto_extend na wszystkich, zgodność posted.json z API.

   Status po POST to `new` — moderacja idzie PO nim, nie przed. `active` = przeszło,
   `moderated` = negatywny werdykt, `blocked`/`disabled` = gorzej.
   Podział robimy PRODUKTAMI, nie obszarami: treść niesie produkt, obszar zmienia tylko city_id.

2a. BEZPIECZNIK — DOPISZ GO, ZANIM RUSZYSZ FAZĘ 2.
   `post_adverts.py` przerywa serię tylko wtedy, gdy PIERWSZE ogłoszenie zwróci błąd HTTP.
   A moderacja przychodzi później i po cichu: POST kończy się sukcesem, status `new`,
   i dopiero po chwili robi się `moderated`. Przy 182 ogłoszeniach oznacza to, że możemy
   wypchnąć całość, zanim zobaczymy pierwszy negatywny werdykt.
   Dopisz: co N ogłoszeń odczyt GET /partner/adverts i STOP, jeśli pojawi się choć jeden
   status `moderated`, `blocked` albo `disabled`. Regulamin pkt 13.11 grozi zawieszeniem
   konta przy powtarzających się naruszeniach — jedno wstrzymane ogłoszenie już mieliśmy 20.08.

2b. LIMITY API — NIEZNANE, więc nie strzelaj seriami bez przerw.
   W OpenAPI nie ma udokumentowanego budżetu zapytań: jest kod 429 „too many requests"
   i pojedyncza wzmianka „throttling cost: 5" przy DELETE, bez podanego okna czasowego.
   Nie zakładaj, że limitu nie ma — po prostu nie wiemy, gdzie jest.

2c. NIE MA STANU „PRZYGOTOWANE, NIEOPUBLIKOWANE".
   Statusy to `new`, `active`, `limited`, `moderated`, `blocked`, `removed_by_user`,
   `outdated`, `unconfirmed`, `unpaid`. POST od razu wchodzi w moderację. Można wystawić
   i natychmiast `deactivate`, ale to i tak zużywa miejsce z pakietu i przechodzi moderację,
   więc nic nie daje.

3. AUTO_EXTEND. `post_adverts.py` ustawia go osobnym PUT-em zaraz po POST, bo PUT w tym
   API podmienia CAŁY zasób — wysłanie samego {"auto_extend_enabled": true} kończy się
   błędem walidacji, a flaga zostaje na false. Po całości sprawdź `--auto-extend`
   i policz, ile ogłoszeń faktycznie ma flagę.

4. DOWÓD DO REJESTRU. Liczba wystawionych, rozkład statusów, liczba z auto_extend,
   zrzut `posted.json`, kilka URL-i publicznych do sprawdzenia okiem.

5. POWIADOMIENIE NA TELEGRAM. Janek nie siedzi przy tym i wraca po ~2 h. Po fazie 1
   i po fazie 2 wyślij mu krótką wiadomość: ile wystawione, rozkład statusów, czy coś
   poszło do wstrzymanych. Sekrety: `~/secrets/telegram/bot-token.txt` i `chat-id.txt`,
   endpoint `https://api.telegram.org/bot<TOKEN>/sendMessage`.
   Jeśli bezpiecznik z 2a przerwie serię — napisz OD RAZU, nie czekaj na koniec fazy.

CZEGO NIE WOLNO COFNĄĆ — to są poprawki po odrzuceniu przez moderację 20.08:
- Zero słowa „netto" i „brutto" w opisie. Pkt 4.4.c wymaga ceny końcowej.
- Zero klauzuli „ceny orientacyjne, nie stanowią oferty handlowej". Ten sam punkt.
- Zero worków w TYTUŁACH i w LINII CENOWEJ — worek to inna jednostka niż tona, więc cena
  za tonę ich nie obejmuje (sprawdzone: 0/200 w obu miejscach). Big-bagi ZOSTAJĄ, są w 136
  tytułach, bo sprzedaje się je na tony. Worki występują wyłącznie w sekcji TRANSPORT
  („Big-bagi i worki na paletach") — to zdanie Janka i ma tam zostać.
- Zero numeru telefonu i e-maila w tytule i opisie. Kontakt tylko w polach formularza.
- Zero kodów QR na zdjęciach produktowych. Kod jest wyłącznie na osobnej karcie
  z kalkulatorem, z UTM w utm_content.

CZEGO NIE RUSZAĆ:
- Zdjęć na profilu GBP i w ogłoszeniach — zestaw jest zaakceptowany.
- Cen. Pole `price` bierze wartość z planu i tak zostaje.
- Nazwy profilu GBP i kategorii.

ZROBIONE = 200 ogłoszeń na koncie, przewaga statusów `active`, auto_extend na wszystkich,
`posted.json` zgodny z API, wiersz T-041 w rejestrze zamknięty z dowodem.
```

## Czego ten wątek NIE dotyka

- **Zdjęć na wizytówce GBP** — 10 kadrów, wszystkie z 02.07, brak wnętrza, produktu
  i transportu. To pytanie do Pawła, osobna pozycja.
- **Treści ogłoszeń** — zaakceptowane, przeszły moderację w tej postaci.
- **T-039 (Ads)** i **T-026 (indeksacja)** — osobne wątki, czekają na decyzje.
