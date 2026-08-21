# Sesja 2026-08-21 — podsumowanie

> Wątek zaczął się od zarzutu: „nie rankujemy, audyt zrobiony źle, Ads zabiera pieniądze i nie
> przynosi konwersji, nic nie jest przygotowane na sezon". Skończył się na osiemnastu domkniętych
> pozycjach, trzech błędach konstrukcyjnych znalezionych po drodze i nowym planie na sezon.
> Pełna lista dotkniętych adresów: `2026-08-21-lista-zmian-i-linkow.md`.

## 1. Co się okazało prawdą, a co nie

**Zarzut o audyt — potwierdzony, z trzema mechanizmami.** Keyword research z 19.05 miał filtr
regexowy wymagający słowa `wapn|kreda|…`, który skasował **cały klaster glebowy** (`ph gleby` 1 000,
`badanie gleby` 1 000, `zakwaszenie gleby` 390 i dalej — ~3 640/mies.). Seedy nie pokrywały oferty:
paszarstwo policzone na 150/mies. wobec **8 940**, rybactwo 240 wobec **4 100**. A 82% zmierzonego
wolumenu opisywało drogownictwo i budownictwo DIY — rynki, na których AGRIA nie gra.

**„Od 9 lipca nie opublikowaliśmy żadnej treści" — moje własne zdanie, nieprawdziwe.** Prawdą jest
węższe: od 9 lipca nie powstał ani jeden **nowy artykuł**. Po tej dacie weszło ~20 adresów
(landing stabilizacji, parametry produktów, ceny na 15 kartach, strony prawne, `/do-pobrania/`).

**Zarzut o Ads — potwierdzony, ale nie w tym miejscu, gdzie szukałem.** Dobór fraz był dobry
(72% kosztu na zapytaniach zakupowych). Zawiodła ścieżka kontaktu i to, że **żadna z pięciu
rekomendacji z 18.08 nie została wykonana**, bo zapisałem je w pliku sesyjnym zamiast w rejestrze.

## 2. Co zostało zrobione

| Obszar | Rzecz |
|---|---|
| **Audyt** | Nowa mapa fraz: **28 720 wyszukań/mies.** realnego popytu, z czego **14 330 w klastrach o zerowym pokryciu**. Źródła: 2 080 fraz z `keyword_suggestions`, 359 fraz hipotez z sezonowością, 12 SERP-ów, GSC 90 dni |
| **SEO on-page** | CTR klastra dawkowego: nowe title/description na 4 adresach (baseline 14 227 wyśw. → 69 klik) |
| **Treść** | Terminarz wapnowania przebudowany ze źródłami IUNG-PIB (tabela terminów, grupy reakcji upraw, parch przy ziemniakach, podział dawki 3/4 + 1/4) |
| **Konwersja** | Ścieżka kontaktu na landingach: cena i numer nad zgięciem, pasek przyklejony na telefonie, kotwica i formularz „oddzwonimy" |
| **Ads** | 26 wykluczeń obcych marek, stawka Brand 0,50 → 3,00, **nowa kampania Paszarstwo** (kreda pastewna 2 400/mies., CPC 2–4× niższy), budżet 34/6 → **26/5/9**, sobota na rozszerzeniu połączeń |
| **Naprawy** | H1 na 10 wpisach i stronie głównej, układ trzech landingów, listingi produktów na trzech landingach |

## 3. Trzy błędy konstrukcyjne znalezione po drodze

1. **Żaden wpis blogowy nie miał H1** — szablon Elementora nie ustawiał `header_size`, tytuł szedł
   jako `h2`. Dotyczyło też strony z 14 227 wyświetleniami. Gdyby nie wyszło, pięć nowych artykułów
   z planu sezonowego trafiłoby do tego samego szablonu.
2. **Trzy landingi renderowały tekst na całą szerokość okna** (1440 px, na telefonie bez marginesu) —
   surowy HTML w `post_content` bez układu Elementora. **Zgłosił Janek**, nie wyszło mi to
   w sprawdzeniu godzinę wcześniej, bo sprawdzałem listę własnych kryteriów zamiast tego,
   czy strona wygląda poprawnie.
3. **Zero linków do kart produktów na landingach** — nazwy stały w tabelach jako goły tekst.
   **Zgłosił Janek.** Naprawione widgetem Elementora z ręcznym wyborem, wg jego wskazania.

## 4. Decyzje zapisane jako ADR

- `2026-08-21-architektura-pole-hub-i-spoke.md` — trzy poziomy na rozłącznych frazach, **próg URL-a
  ≥3 frazy i ≥100 wyszukań/mies. liczone z GSC**, hub bez nagłówków uprawowych, pełne pokrycie upraw
  tabelą i kalkulatorem zamiast czterdziestoma adresami.
- **Korekta ADR 11.08:** reguła „jeden URL na intencję" obowiązuje dla fraz, na których już rankujemy;
  tam, gdzie mamy zero URL-i, nie ma czego kanibalizować.

## 5. Co zostaje otwarte — 12 pozycji

**Pilne, bo idą pieniądze:** T-062 (baner zgód zasłania 53% ekranu telefonu i całą ścieżkę kontaktu
przy pierwszym wejściu — czyli przy każdym kliknięciu z reklamy), T-058 (grupa „Producent",
rewizja grupy magnezowej, ocena kampanii po 7 dniach — **28.08**).

**Sezon, twarde terminy:** T-055 spoke ozimin **do 05.09** i hub **do 10.09**, T-056 staw **do 20.09**,
T-057 gleba **do 20.09**, T-054 paszarstwo. Wszystko, co ma pracować w październiku, musi być
opublikowane do 20.09.

**Puste kategorie segmentowe** — `/wapno-do-stawow/`, `/wapno-do-sadu/`, `/wapno-nawozowe-hurt/`
oddają dziś 301 na `/oferta/`. Odbudowa: T-056, T-065, T-057. Zdjęcie 301 zawsze **razem z treścią
i produktami**, nigdy przed.

**Dług:** T-063 (przebudowa landingów na wzorcu, dziś stoją na łatce CSS), T-061 (`/oferta/` bez H1),
T-026/T-027 (indeksacja), T-060 (magnez i fosfor, zaparkowane).

## 6. Dwie rzeczy do potwierdzenia u Pawła

Obie stoją teraz na stronach docelowych reklam:

1. **Cena „od 36 zł/t"** na `/wapno-nawozowe/` — najniższa pozycja cennika (węglanowe z magnezem
   odm. 05), oznaczona w `CENNIK_PAWEL_2026-08-07.md` jako możliwa literówka.
2. **Karta kredy pastewnej podaje „minimum 37% CaO"** — rynek i karty producentów podają **37% Ca**.
   Węglan wapnia to ok. 40% Ca / 56% CaO, więc to nie jest to samo. Karta jest od dziś stroną
   docelową reklam; blokada publikacji w T-054 obowiązuje.
