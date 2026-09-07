# Blok 0, wątek główny — porządek na produkcji przed wznowieniem kampanii

> **Kiedy:** 08–12.09.2026 · **Projekt:** `agria` · **Zakres:** ryczałt R
> **Obejmuje:** T-127 · T-097 · T-096 · T-128 · T-113 (w częściach T-031, T-063, T-059)
> **Kontekst:** `docs/PLAN_WRZESIEN_2026.md` §5–§7 · `docs/audits/2026-09-07-CRAWL_SCREAMING_FROG.md`
> · `data/kontrole/2026-09-07-odczyt-ads-7-dni.md`
>
> **Dlaczego teraz i razem:** kampanie stoją do 14.09 (budżet cyklu wyczerpany 07.09 na 1 152,54 zł
> z 1 200), więc to jedyne okno, w którym robota na stronie nie kosztuje budżetu mediowego.
> Wszystkie te pozycje dotykają tej samej warstwy — jeden backup, jedna sesja, jedna weryfikacja.

---

## 0. Zanim cokolwiek ruszysz

1. **Backup bazy** przez MCP `db_export` (zrzut ląduje poza web rootem) — nazwa
   `przed-blok0-2026-09-XX`. Przy edycji plików dodatkowo `backup_file` na każdym dotykanym pliku.
2. **Przeczytaj `docs/FAKTY_KLIENTA.md` §7** i ADR `docs/decyzje/2026-08-19-dwie-warstwy-cen.md`
   **zanim** dotkniesz czegokolwiek związanego z ceną. To jest strefa, w której łatwo zrobić szkodę.
3. **Zgoda Janka per operacja zapisu na produkcji.** MCP pisze prosto na żywą stronę.

---

## 1. T-127 — trzy adresy 404 (zacznij od tego, jest najprostsze)

Znalezione crawlem Screaming Frog 07.09:

| adres | co jest | co ma być |
|---|---|---|
| `/polityka-prywatnosci/` | **404** | strona istnieje albo 301 na właściwy adres — **jest wymagana prawnie** i linkowana z serwisu |
| `/rolnictwo` | **404** | 301 na `/wapno-nawozowe-rolnictwo/` (sprawdź, czy nie ma już reguły na wariant ze slashem) |
| `/kontakt/pawel.bigos@agria.pl` | **404** | na stronie kontaktu adres e-mail wstawiono jako link **względny** zamiast `mailto:` — popraw źródło linku, nie dokładaj przekierowania |

**Najpierw ustal, czy `/polityka-prywatnosci/` kiedykolwiek istniała** (`query_db` po `post_name`,
`wp_posts`), czy to tylko martwy link. Complianz zwykle wskazuje własną stronę polityki — sprawdź,
na jaki adres kieruje baner, i **doprowadź do jednego adresu**, nie dwóch.

⚠️ Reguły `.htaccess` **tylko przez FTP, z kopią i po pokazaniu diffa Jankowi** (CLAUDE.md §5).

**Zrobione =** wszystkie trzy adresy oddają 200 albo 301 jednym skokiem, sprawdzone `curl` z cache-bustem,
plus regres na zestawie 62 adresów jak przy T-072 — zero nowych 404.

## 2. T-097 — `offers` w schemacie 19 kart produktowych

**Stan zmierzony crawlem:** 19 z 19 kart ma ten sam błąd walidacji Google Product Snippet:
`Either 'schema.org/review', 'schema.org/aggregateRating' or 'schema.org/offers' is required`.

**Reguła nadrzędna — ADR `2026-08-19-dwie-warstwy-cen.md`:**
`offers` budujemy **ręcznie z kwoty widocznej w treści strony**. **Nigdy** z `_price`, nigdy z wariantów
WooCommerce, nigdy z ofertownika. `_price` zostaje puste w 19/19 — to decyzja, nie brak.

- **15 kart ma kwotę `zł/t netto` na froncie** — dla nich `offers` powstaje z tej kwoty,
  z `priceCurrency: PLN`, `availability: InStock`, `priceValidUntil` i `url` karty.
- **4 karty nie mają kwoty** (302 Dolomit, 303 Kreda czarna, 313 Tlenkowe z Mg, 316 Węglanowe odm. 05).
  Dla nich **nie wymyślaj ceny** — użyj `AggregateOffer` bez `price` albo zostaw kartę bez `offers`
  i zapisz to jako świadomy wyjątek. Cena Dolomitu czeka na odpowiedź Pawła (T-100).

⚠️ **Kwota w treści musi się zgadzać z kwotą w schemacie co do złotówki.** Rozjazd to gorszy stan
niż brak `offers` — Google traktuje to jako wprowadzanie w błąd.

⚠️ **Sprawdź, gdzie schema powstaje** (Rank Math czy motyw), zanim zaczniesz — dopisywanie drugiego
bloku `Product` obok istniejącego zrobi duplikat, nie naprawę.

**Zrobione =** ponowna walidacja (Rich Results Test albo powtórny crawl SF z włączoną walidacją
schema) pokazuje **0 błędów** na kartach z ceną, a karty bez ceny są opisane w rejestrze jako wyjątek.

## 3. T-096 — `/kreda-malarska/` bez meta

Term 830 jako **jedyny z ośmiu** nie ma ani `rank_math_title`, ani `rank_math_description`, opis
taksonomii ma **0 znaków**, front oddaje domyślny tytuł WordPressa. Potwierdzone crawlem 07.09
(strona w zestawie „bez meta description" razem z `/rodo/` i `/category/poradniki/`).

⚠️ Uwaga na kontekst: **karta** `/kreda-malarska/kreda-malarska/` ma 164 wyświetlenia i pozycję 6,7,
a **kategoria** `/kreda-malarska/` — zero. Nie buduj kategorii kosztem karty; ustal, który adres ma
zbierać tę frazę, i drugi podporządkuj.

**Zrobione =** termmeta uzupełnione, render potwierdza tytuł i opis, encja `&#8211;` w treści naprawiona.

## 4. T-128 — 1,7 MB obrazów bez ani jednego użycia

Pięć plików z zerowym `IMG Inlinks` w crawlu: kreda pastewna frakcje 0.4–0.8 (479 KB), 0.1–0.4 (427 KB),
1–3 (402 KB) oraz Agrobielik 90 0–3 (265 KB) i 2–8 (166 KB).

**Nie kasuj od razu.** Najpierw sprawdź, czy któraś karta produktowa **nie ma zdjęcia produktu** —
wtedy te pliki są materiałem, nie śmieciem. Dopiero to, co zostanie bez zastosowania, usuwaj,
z kopią do `~/backups/agria/`.

## 5. T-113 — jakość strony docelowej (części T-031, T-063, T-059)

**Dlaczego to jedna robota, a nie trzy:** Google ocenia `post_click_quality_score` jako
**„poniżej średniej" na 34 z 37 fraz**, a przy MANUAL_CPC ta ocena **mnoży stawkę w rankingu
i wyznacza faktyczny CPC**. Trzy poniższe pozycje są składowymi tej samej oceny.

### 5a. T-031 — LCP mobile 7,4 s przy 90,5% ruchu mobilnego

PSI mobile: score 68, **LCP 7,4 s**, desktop 1,5 s, TBT 110 ms, CLS 0 — czyli **sieć i zasoby**,
nie JavaScript. Transfer 1 478 KB na 97 zapytań.

⚠️ **Rozbieżność do wyjaśnienia na starcie:** rejestr mówi o hero **686 KB**, a w crawlu SF największy
obraz to 479 KB i jest nieużywany. **Hero prawdopodobnie ładuje się przez CSS jako `background-image`**,
dlatego SF go nie policzył jako `<img>`. Zacznij od ustalenia, co dokładnie jest elementem LCP
(PSI/Lighthouse poda to wprost), zanim zaczniesz optymalizować cokolwiek.

### 5b. T-063 — trzy landingi to nadal surowy HTML w `post_content`

Moduł `plain-content-layout` z 21.08 jest łatką na objaw. Docelowo: wzorzec działającej strony
obejrzany przez **Chrome MCP** i powielony (memory `feedback_agria_landingi_wzorzec_nie_elementor`).

### 5c. T-059 — lekki formularz „zostaw numer, oddzwonimy"

Dzisiejszy `inquiry-form` wymaga wyboru produktu z **dwudziestu opcji**. Tymczasem formularz jest
**jedynym realnie działającym kanałem kontaktu**: w trzy miesiące **37 rozpoczęć → 32 wysłania (86%)**,
przy 3 kliknięciach w telefon i 2 w WhatsApp. Wariant `mode="callback"` — imię, telefon, zgoda —
na landingach ruchu płatnego, gdzie intencja brzmi „cena za tonę", nie „dobierz mi produkt".

⚠️ **58,6% budżetu wychodzi, gdy biuro jest zamknięte** (pn–pt 8–16), a po przejściu na niedziele —
61,3%. Ten formularz jest w tych godzinach jedyną ścieżką, więc jego widoczność na mobile jest
ważniejsza niż jego kompletność.

---

## 6. Czego w tym wątku NIE robisz

- **T-112 (cena „od 36 zł/t")** — zablokowane pytaniem do Pawła: czy 36 zł/t jest prawdziwe i jakiej
  formy dostawy dotyczy. `FAKTY_KLIENTA.md` §3 trzyma tę kwotę w sekcji „anomalie do potwierdzenia".
  **Nie zgaduj i nie podmieniaj na własną liczbę.**
- **Nie ustawiaj `_price` ani wariantów WooCommerce** — tryb katalogu jest decyzją.
- **Nie dokładaj kodu do warstwy zgód** (Complianz, Consent Mode) — wyłącznie ustawieniami.
- Nie ruszaj konta Google Ads — to osobny wątek po 14.09.
- Nie zgłaszaj URL-i do Indexing API inaczej niż przez `~/bin/index-submit`.

## 7. Weryfikacja całości — zanim napiszesz „zrobione"

1. **Render, nie baza.** Parametry i treść żyją w czterech warstwach naraz; sprawdzasz to, co widzi
   użytkownik, przez `curl` z cache-bustem i przez Chrome MCP.
2. **Cache po każdej zmianie:** `_elementor_element_cache` → `a:0:{}`, CDN nazwa.pl cache-bust,
   sitemapa Rank Matha to **pliki** `uploads/rank-math/*.xml` — usuwane przez FTP.
3. **Regres na 62 adresach** — kody odpowiedzi przed i po, wzorem T-072. Zero nowych 404,
   zero stron podejrzanie małych, po jednym H1.
4. **Powtórny crawl SF na koniec** — najprostszy dowód, że wszystkie cztery pozycje zeszły z listy.
   Poproś Janka o eksport, tak jak 07.09.
5. **Rejestr:** każdy wiersz T-NNN aktualizowany **w tym samym commicie**, co zmiana. Wiersz bez dowodu
   nie ma prawa mieć ✅.
