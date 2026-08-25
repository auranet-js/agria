# ADR 2026-08-24 — rozstrzygnięcia po audycie SEO od nowa

> **Status:** przyjęte (decyzja Janka 24.08.2026)
> **Podstawa:** `docs/audits/2026-08-24-AUDYT_SEO_OD_NOWA.md`, pomiary z 24.08
> **Zastępuje w części:** `docs/seo/2026-08-21-sezonowosc-i-kolejnosc-M4.md` §2 i §4,
> sekcję treściową `docs/REJESTR_ZOBOWIAZAN.md` sprzed 24.08

---

## Kontekst

Plan treści na sezon powstawał w trzech wątkach (14.07, 21.08, 24.08) i rozjechał się
z produkcją w trzech miejscach naraz: kolejność opierała się na sezonowości odczytanej
z przyciętej serii, część zadań stała na stanie strony sprzed naprawy, a całość zakładała,
że nowa treść opublikowana z wyprzedzeniem 2–6 tygodni zdąży wejść do indeksu.

Audyt z 24.08 zmierzył wszystkie trzy założenia. Dwa się nie potwierdziły.

---

## Decyzja 1 — kolejność treści wynika z tego, czy adres jest crawlowany

**Ustalenie pomiarowe.** Od 09.07 opublikowaliśmy **dziesięć nowych adresów. Google nie pobrał
ani jednego** (GSC URL Inspection, 24.08). Dotyczy to również stron kompletnych i linkowanych:
`/jak-stosowac-wapno-nawozowe/` ma 13 455 znaków renderu i 16 linków wewnętrznych, a werdykt
to „Discovered — currently not indexed", crawl **nigdy**. W tym samym czasie adresy, które Google
zna, crawlowane są **codziennie** — `/oferta/` i `/wapno-do-sadu/` 24.08, `/`, hub i `/kontakt/`
23.08, dziesięć kart produktów 21–23.08.

Osobno: **osiem z dziewiętnastu kart produktów jest poza indeksem** (6 × „URL unknown",
2 × „Discovered"), wszystkie w sitemapie od 15.07 lub 19.08.

**Decyzja.** Kolejność zadań treściowych ustala się wg trzech kryteriów w tej hierarchii:

1. **czy adres jest już crawlowany** — rozbudowa strony zaindeksowanej dociera do Google
   następnego dnia, nowy adres może nie dotrzeć wcale;
2. wolumen razy brak pokrycia, zmierzony w GSC wymiarem `page × query`;
3. odległość do szczytu sezonowego.

**Konsekwencja operacyjna.** Do 31.08 nie publikujemy nowych adresów. Wrzesień idzie na treść
w obrębie stron już zaindeksowanych. Nowe adresy wchodzą dopiero po **kontroli 15.09** —
jeśli żaden adres z Fazy 0 nie zostanie pobrany, wracamy z pytaniem, a nie z kolejnym artykułem.

**Czego ta decyzja NIE mówi.** Nie mówi, że linkowanie naprawia indeksację. Terminarz ma 16 linków
i nie został pobrany — linkowanie jest warunkiem koniecznym, nie wystarczającym. Faza 0 jest
uzasadniona tym, że to jedyna część problemu, która zależy od nas.

---

## Decyzja 2 — sezonowość liczona z pełnych dwunastu miesięcy, z etykietami

**Ustalenie pomiarowe.** Szczytem roku dla całej rodziny „pole / dawka / granulat" jest **sierpień**:
`wapno granulowane` VIII 9 900 wobec X 8 100 · `wapno węglanowe` VIII 2 400 · `ile wapna na hektar`
VIII 1 900 · `badanie gleby` VIII 1 900 (na równi z marcem) · `jakie wapno na pole` VIII 480.
Szczyt X–XI mają wyłącznie `wapno palone` (3 600), `kiedy wapnować glebę` (590) i `kiedy wapnować
pole` (260).

**Przyczyna błędu.** `docs/seo/2026-08-21-sezonowosc-i-kolejnosc-M4.md` §2 zbudował tabelę
„szczytują TERAZ" z kolumnami **IX / X / XI** i nie pokazał sierpnia — miesiąca, w którym powstawał.
Trzy liczby przepisane stamtąd do rejestru są nieprawdziwe:

| Zapis | Pomiar 24.08 |
|---|---|
| `wapno granulowane` „szczytuje w październiku na 8 100" | szczyt **VIII 9 900**, X to szczyt wtórny |
| `wapnowanie drzew owocowych kiedy` „XI to 40 wobec średniej 210" | **XI to 260**; wartość 40 to **czerwiec** — ostatni element serii wzięty za listopad |
| `wapno na łąki` „szczyt marcowy (III 70)" | 30–70 przez cały rok; III 70, ale tyle samo VIII, IX i XI — **szum, nie sezon** |

**Decyzja.** Serie sezonowe wypisujemy **zawsze z etykietami rok-miesiąc i zawsze za pełne
dwanaście miesięcy, łącznie z miesiącem bieżącym**. Zakaz cytowania wycinka okna w uzasadnieniu
terminu. Przy zapytaniach do DataForSEO nie mieszamy liczby pojedynczej i mnogiej w jednym batchu
(planer grupuje warianty i zeruje pozostałe — pułapka z T-056).

---

## Decyzja 3 — trzy pozycje unieważnione

**T-073 — hub `/jakie-wapno-na-pole/`: nie budujemy.**
`/wapnowanie-gleby/` rankuje na `wapno na pole` na **pozycji 2,0** (i na `ile kosztuje wapno na pole`
również 2,0). Nowy adres byłby drugim naszym URL-em na intencję, na której jesteśmy w TOP3 — czyli
wprost tym, czego zakazuje ADR `2026-08-11-podzial-rol-ads-seo.md`, potwierdzony w audycie
na sześciu frazach. Fraza `jakie wapno na pole` stoi na hubie na 30,7, co jest **problemem treści
huba, nie brakiem adresu**. Zamiast huba: sekcja „Jakie wapno na pole" **wewnątrz `/wapnowanie-gleby/`**.
Dodatkowo szczyt tej frazy to sierpień (480), więc termin 10.09 i tak trafiał po nim.

**T-075 — spoke „łąki i pastwiska": zdejmujemy z planu.**
`wapno na łąki` to 30–70 wyszukań miesięcznie przez cały rok. Termin 15.12 wypadał w dołku (30).
To nie jest klaster.

**T-079 — karta produktu #307 „Kreda pastewna": traci przedmiot.**
Zarzut („karta opisuje kredę pastewną parametrami wapna tlenkowego — egzotermia, pH >12") jest
**nieprawdziwy na stronie**. Sprawdzone 24.08 we wszystkich czterech warstwach — render, `post_content`,
`_elementor_data`, atrybuty `pa_*`, meta Rank Math: **zero wystąpień „egzoterm", zero „pH >12"**,
specyfikacja podaje `min. 37% CaO` i dawkowanie `1–2 kg / 100 kg paszy`. Naprawione **15.07**
przy naprawie parametrów w czterech warstwach. Wadliwy opis został **w katalogu drukowanym**
(`FAKTY_KLIENTA` §8 pkt 7) — to errata po stronie klienta, nie nasze zadanie.
Karta ma cenę, jest zaindeksowana (132 wyśw., poz. 8,4) i nie blokuje T-077.

---

## Decyzja 4 — dwie pozycje przesunięte poza okno

**T-082 — strona tonażowa na `/wapno-nawozowe-hurt/`: VII 2027.**
Klaster tonażowy szczytuje w **sierpniu** (`wapno granulowane big bag cena` VIII 590 wobec średniej
260, `wapno granulowane cena za tonę` VIII 320), więc publikacja 05.10 trafiała w opadające zbocze.
Dodatkowo wolumen w rejestrze był zawyżony: zapis mówił „`wapno … cena za tonę` **490 łącznie**",
a pomiar osobno po jednej frazie daje `wapno cena za tonę` 50 + `wapno granulowane cena za tonę` 90
+ `wapno na pole cena za tonę` 10 = **150**. Sama nazwa kategorii (`wapno nawozowe hurt`, `wapno hurt`)
zwraca z planera `null`.

**T-076 — spoke „zboża ozime i rzepak": VII 2027.**
Blokada `T-067` (brak źródeł IUNG w repo — `data/zrodla/` nie istnieje, potwierdzone 24.08).
Okno VIII–IX mija. Hub już rankuje na `jakie wapno pod rzepak` i `czy można siać wapno na zboże`.

---

## Decyzja 5 — blok F realizujemy na istniejącej kategorii

Zobowiązanie z maila do Kasjana z 06.08 („październik — stabilizacja gruntów i budownictwo")
zostaje w mocy, ale **budownictwo idzie jako przepisanie kategorii `/wapno-hydratyzowane/`**,
nie jako nowy landing ani rozbudowa poza nią. Kategoria jest zaindeksowana i crawlowana 21.08,
a stoi na **pozycji 31,3** przy wolumenie 2 400/mies. — to jest praca na istniejącym adresie,
zgodna z Decyzją 1.

Stabilizacja gruntów: **najpierw linki** (strona jest sierotą — zero linków wewnętrznych,
werdykt „URL unknown"), treść dopiero po niej.

---

## Konsekwencje dla rejestru

`docs/REJESTR_ZOBOWIAZAN.md` — sekcja treściowa przepisana w tym samym commicie:
kolejność wg Decyzji 1, T-073 / T-075 / T-079 do „Unieważnione", T-082 i T-076 poza okno,
jedenaście nowych pozycji z audytu (T-089…T-099).

**Kontrola 15.09** wpisana do „Terminów najbliższych" jako warunek wejścia w nowe adresy.
