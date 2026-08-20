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
Tytuły 123–141 znaków (limit 150). Opisy 3 518–4 479 znaków (limit 9 000).
Zdjęć na ogłoszenie: 7 w 186 pozycjach, 6 w 14 (kreda nawozowa granulowana — brak zdjęcia
studyjnego, bo karta ID 305 ma na produkcji podpięte zdjęcie innego produktu).
56 unikalnych adresów zdjęć, wszystkie odpowiadają HTTP 200.

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

2. PARTIAMI, NIE NARAZ. Regulamin pkt 13.11 grozi zawieszeniem konta przy powtarzających
   się naruszeniach, a moderację przeszedł dotąd JEDEN tytuł i JEDEN opis. Wystaw
   kilkanaście pozycji z RÓŻNYCH kart produktowych (`--pilot N`), odczekaj na werdykt,
   dopiero potem resztę. Status po POST to `new` — moderacja idzie po nim, nie przed.
   Sprawdzaj GET /partner/adverts i licz statusy; `active` = przeszło, `moderated` =
   negatywny werdykt, `blocked`/`disabled` = gorzej.

3. AUTO_EXTEND. `post_adverts.py` ustawia go osobnym PUT-em zaraz po POST, bo PUT w tym
   API podmienia CAŁY zasób — wysłanie samego {"auto_extend_enabled": true} kończy się
   błędem walidacji, a flaga zostaje na false. Po całości sprawdź `--auto-extend`
   i policz, ile ogłoszeń faktycznie ma flagę.

4. DOWÓD DO REJESTRU. Liczba wystawionych, rozkład statusów, liczba z auto_extend,
   zrzut `posted.json`, kilka URL-i publicznych do sprawdzenia okiem.

CZEGO NIE WOLNO COFNĄĆ — to są poprawki po odrzuceniu przez moderację 20.08:
- Zero słowa „netto" i „brutto" w opisie. Pkt 4.4.c wymaga ceny końcowej.
- Zero klauzuli „ceny orientacyjne, nie stanowią oferty handlowej". Ten sam punkt.
- Zero worków w tytułach i w linii cenowej — worek to inna jednostka niż tona, więc
  cena za tonę ich nie obejmuje. Big-bagi ZOSTAJĄ, bo są sprzedawane na tony.
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
