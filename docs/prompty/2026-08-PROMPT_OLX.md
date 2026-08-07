# Prompt startowy — OLX jako kanał sprzedaży AGRII (operacja zamknięta w czasie)

> Wersja 2, 2026-08-07 (v1 była szkicem zadań; ta wersja obejmuje całą operację).
> Uruchamiać w `~/projekty/agria`. **Nie przechodzimy do kolejnych wątków, dopóki ten nie zostanie domknięty.**

---

## 1. Co ma powstać

**Jeden dokument decyzyjny dla AGRII** (Paweł + Kasjan), który odpowiada na pytanie „30 ogłoszeń czy 10 + promowanie" i przy okazji zamienia OLX z porzuconego konta w prowadzony kanał:

- **prognoza** — ile zapytań miesięcznie przy jakim nakładzie, policzona na własnych danych, nie na wróżeniu;
- **budżet miesięczny** — koszt po stronie AGRII (pakiet OLX + ewentualne wyróżnienia) **osobno** od kosztu obsługi po stronie Auranet;
- **harmonogram zamknięty w czasie** — start, kamienie milowe, moment oceny wyników, koniec etapu;
- **zakres prac Auranet** — co dokładnie robimy, w czym to jest wycenione (osobna pozycja czy w ramach 2 000/mies).

Do tego, po stronie technicznej: **operacja wystawienia ogłoszeń faktycznie wykonana**, nie tylko opisana.

---

## 2. Stan wiedzy — przeczytaj najpierw

| Dokument | Co tam jest |
|---|---|
| `docs/operations/OLX_INWENTARYZACJA_2026-08-07.md` | dostęp do API, stan konta AGRII, statystyki własnych ogłoszeń |
| `docs/operations/OLX_KONKURENCJA_2026-08-07.md` | 1 166 ogłoszeń rynku, profile liderów, ceny wg jednostki, nisze |
| `docs/operations/CENNIK_PAWEL_2026-08-07.md` | ceny AGRII z 07.08 + ograniczenie kanałowe (stali odbiorcy) |
| memory `reference_agria_olx_api` | jak działa dostęp, gdzie sekrety |

**Liczby, od których startujesz:**
- Konto AGRII: 20 ogłoszeń, 1 aktywne, 17 wygasło 18.07. Cykl życia: 7 273 wyświetlenia, **209 odsłon telefonu**, CR 2,9%.
- Najlepsze ogłoszenie („Do stawu") — 2 514 wyświetleń, **94 telefony = 45% kontaktów z całego konta**, dziś wyłączone.
- Liderzy rynku: 191 / 161 / 93 / 70 / 58 ogłoszeń, model = 9–26 ofert × 44–161 miast, **prawie bez promowania**.
- Ceny: węglanowe AGRII o ~40% powyżej mediany OLX, kreda o ~25%; granulowane i tlenkowe w rynku. **Tlenkowe to na OLX pustka — 3 ogłoszenia z ceną tonową w całej kategorii.**

---

## 3. Bloki zadań

### Blok A — koszty po stronie klienta (bez tego nie ma budżetu)

- Cennik pakietów ogłoszeń OLX dla firm w kategorii Nawozy (2026) — ile ogłoszeń, za ile, na jaki okres.
- Koszt wyróżnień: „odświeżanie", „wyróżnienie", „na górze". Ile realnie kosztuje utrzymanie ogłoszenia przez 30 dni.
- Czy konto AGRII ma resztki pakietu (17 ogłoszeń wygasło jednego dnia — sprawdź w panelu, czy to koniec pakietu, czy koniec 30-dniowej ważności).
- Źródło: panel OLX na zalogowanym koncie (Chrome, konto AGRII loguje Janek) + publiczny cennik OLX dla firm.

### Blok B — asortyment i intencje

Rozstrzygnij, **które z 19 produktów w ogóle idą na OLX**, na podstawie §4 i §5 analizy konkurencji:
- kandydaci mocni: tlenkowe (Agrobielik 70/90, Oxyfertil), zastosowania stawowe, palone mielone;
- kandydaci słabi: węglanowe i kreda sypka — przegrywają ceną z kopalniami, chyba że komunikat oprzemy na czymś innym niż cena (atesty, ciągłość dostaw, jedno złoże);
- dolomit — sprawdź osobno, bo fraza ma 6 600 wyszukań/mies w Google, ale na OLX może być inaczej.

Dla każdego wybranego produktu: **tytuł pod intencję**, nie pod cenę. Wzorzec, który zadziałał na tym koncie: „Do stawu…" (94 telefony) wobec „…Najtaniej!" (~3 telefony na sztukę).

Ustal siatkę miast — ile ogłoszeń na produkt i gdzie. Punkt odniesienia: AGRO-KOTYNIA 9 ofert × 161 miast, 699-712-071 26 ofert × 120 miast. Uwzględnij realny zasięg dostaw AGRII (magazyny Niedomice i Radgoszcz) — powielanie na całą Polskę ma sens tylko przy dostawie całopojazdowej.

### Blok C — treść i materiały

- **Opisy ogłoszeń** z kart produktowych: parametry są już zweryfikowane z kartami producentów i atestami (naprawa z 15.07). Nie wymyślaj parametrów — bierz z produkcji przez MCP.
- **Zdjęcia** — są na stronie w `wp-content/uploads`, po 8 na ogłoszenie jak dotąd. Sprawdź, które karty mają komplet, i czy da się je wysłać przez API (OLX wymaga URL-i albo uploadu — sprawdź w dokumentacji Partner API).
- **Ceny w ogłoszeniach** — z `CENNIK_PAWEL_2026-08-07.md`, spójne z tym, co pójdzie na stronę. Uwaga: opis obecnego aktywnego ogłoszenia mówi „600 zł brutto/t" przy worku 40 kg, cennik daje 475 zł/t netto — do uspójnienia.
- **Czego Auranet dokłada** — jeśli brakuje zdjęć produktowych albo grafik pod konkretne zastosowanie (staw, sad, oczyszczalnia), zaproponuj co przygotujemy i ile to zajmie.

### Blok D — automatyzacja przez API

Scope `write` jest, więc do rozstrzygnięcia i wykonania:
- wystawianie ogłoszeń z danych produktowych (`POST /partner/adverts`) — zbuduj i przetestuj na jednym ogłoszeniu przed masówką;
- `auto_extend` na wszystkich (dziś na 1 z 20 — stąd ciche wygaśnięcie konta);
- rotacja i odświeżanie: co i jak często, żeby nie przepalać pakietu;
- **pomiar**: snapshot `advert_views` / `phone_views` per ogłoszenie w regularnym odstępie. Bez tego prognoza zostanie prognozą.

**Uwaga:** statystyki z API są kumulatywne od utworzenia ogłoszenia (część ogłoszeń pochodzi z 2023 r.), więc **nie da się z nich wprost policzyć wskaźnika miesięcznego**. Pierwszy pomiar przyrostowy zrób od razu na starcie — snapshot dziś, kolejny po tygodniu. Dopiero to daje uczciwą prognozę.

### Blok E — połączenie ze stroną

- Linkowanie: czy i gdzie na agria.pl wspominamy o ofercie na OLX (i odwrotnie — link ze strony w ogłoszeniach OLX, jeśli regulamin pozwala; **sprawdź regulamin, nie zakładaj**).
- **Pomiar w GA4**: ruch z OLX musi być rozpoznawalny (UTM w linkach z ogłoszeń). Pamiętaj o stanie GA4 — atrybucja jest dziś zaburzona, w TOP-15 landingów siedzi 9 pozycji demo motywu zwracających 404 (`REWIZJA_STANU_2026-08-06.md` §7). Zanim zaczniesz mierzyć OLX, upewnij się, że mierzysz cokolwiek.
- Telefon: 209 odsłon numeru to kontakty, których **nie widać w żadnej analityce**. Zaproponuj, jak je policzyć (osobny numer? call tracking? jeśli to za duże, powiedz wprost, że mierzymy proxy).

---

## 4. Prognoza — jak ją policzyć uczciwie

Punkt wyjścia: **209 odsłon telefonu przy CR 2,9%** z 20 ogłoszeń o nierównej jakości, z czego 45% z jednego trafionego. Model buduj po kolei:

1. ile wyświetleń daje jedno ogłoszenie w miesiącu (**zmierz przyrostowo**, nie zgaduj z danych kumulatywnych),
2. × liczba ogłoszeń w pakiecie,
3. × CR na telefon (własny punkt odniesienia: 2,9%, dla trafionej intencji 3,7%),
4. → zapytania miesięcznie, w widełkach pesymistyczny / realny / optymistyczny.

Powiedz wprost, czego prognoza nie obejmuje: sezonowości (sierpień–październik to szczyt dla rolnictwa), tego, ile zapytań zamieni się w zamówienia (to zależy od ceny i dostępności, nie od kanału), i tego, że ceny węglanowych są powyżej rynku.

**Nie obiecuj zamówień.** Wzorzec framingu jest w `docs/offers/2026-08-PLAN_ADS_3MIES.md` („za co bierzemy odpowiedzialność, a czego nie obiecujemy").

---

## 5. Budżet i harmonogram

Rozdziel trzy rzeczy, których klient nie może pomylić:

| Pozycja | Kto płaci | Charakter |
|---|---|---|
| Pakiet ogłoszeń OLX | AGRIA, bezpośrednio OLX | miesięcznie |
| Wyróżnienia / odświeżanie | AGRIA, bezpośrednio OLX | miesięcznie, opcjonalne |
| Przygotowanie i prowadzenie | Auranet | do ustalenia z Jankiem — osobna pozycja czy w ramach 2 000/mies |

Harmonogram wpisz w sezon: **sierpień–październik to szczyt dla rolnictwa**, listopad domyka wapno palone. Zaproponuj konkretne daty startu, moment oceny wyników i jasny koniec etapu, po którym jest decyzja „kontynuujemy / zwijamy" — analogicznie do planu Ads na 3 miesiące.

---

## 6. Decyzje, które musisz zebrać (nie zgaduj)

**Janek:**
- czy prowadzenie OLX to osobna pozycja w wycenie, czy mieści się w 2 000/mies (patrz `feedback_no_made_up_pricing_without_approval` — **żadnych kwot bez akceptu**);
- czy wystawiamy ogłoszenia w imieniu klienta z naszego API, czy przekazujemy Pawłowi gotowe treści do wklejenia.

**Paweł (przez Janka, telefonicznie — `feedback_agria_pawel_relacja_telefoniczna`):**
- czy węglanowe i kreda w ogóle mają iść na OLX, skoro są 25–40% powyżej mediany rynku;
- zmiana hasła do konta (przyszło mailem plaintextem) + 2FA;
- czy konto ma zostać na prywatnym Gmailu Pawła (wisi tam jego prywatne ogłoszenie mieszkania — **API ma do niego dostęp, nie ruszamy**).

---

## 7. Reguły komunikacji do klienta

- Dokument dla zarządu prosty, technikalia w załączniku; **budżet wyłącznie miesięcznie, nigdy suma całkowita** (`feedback_agria_offer_mail_structure`).
- Bez krytyki obecnego stanu — Auranet zbudował tę stronę (`feedback_agria_no_self_criticism_built_site`). To dotyczy też OLX: konto zaniedbał klient, ale piszemy „reaktywujemy kanał", nie „konto było martwe".
- Mail wyłącznie do Janka na `js@auranet.com.pl`, nigdy do klienta.
- Bez emoji, bez agencyjnych frameworków klasyfikacji.

---

## 8. Definicja „zrobione"

1. Znany koszt pakietu i wyróżnień → budżet miesięczny policzony.
2. Wybrany asortyment + tytuły pod intencję + siatka miast.
3. Ogłoszenia wystawione przez API (pilot → masówka), `auto_extend` włączony wszędzie.
4. Pomiar działa: snapshot statystyk + UTM w linkach, wiadomo, co i jak liczymy.
5. Dokument dla AGRII gotowy: prognoza w widełkach, budżet rozdzielony na trzy pozycje, harmonogram z datą oceny wyników, zakres prac Auranet.
6. Wszystko zacommitowane i wypchnięte; wnioski, które przeżyją wątek → memory.
