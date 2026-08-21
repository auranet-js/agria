# ADR 2026-08-21 — terminarz jako hub osi KIEDY i roczna mapa wpisów uprawowych

**Status:** przyjęta 2026-08-21 `[J]` · **Dotyczy:** T-055, T-066
**Uzupełnia** ADR `2026-08-21-architektura-pole-hub-i-spoke.md` — nie zastępuje go.

---

## Problem

Przy podejściu do spoke'a ozimin (T-055, termin 05.09) wyszła kolizja, której ADR z rana tego
samego dnia nie przewidywał: **terminarz `/jak-stosowac-wapno-nawozowe/`, przebudowany 21.08,
odpowiada już na komplet fraz przypisanych do spoke'a.**

Ma sekcję „Kiedy wapnować pod konkretne uprawy" z podziałem IUNG-PIB na trzy grupy reakcji
i trzema nagłówkami H3: „Zboża ozime i rzepak", „Ziemniaki — jedyny wyjątek od reguły",
„Lucerna i koniczyna".

Frazy planowanego spoke'a ozimin są w komplecie pytaniami o **termin**, nie o uprawę:

| Fraza | Wol./mies. | O co realnie pyta |
|---|---|---|
| `czy można siać wapno na zboże` | 90 | dopuszczalność w terminie |
| `kiedy siać wapno pod zboża ozime` | 30 | termin |
| `wapnowanie przed siewem pszenicy ozimej` | 10 | termin |
| `kiedy wapnowanie pola pod pszenicę` | 10 | termin |

Czyli spoke ozimin **nie był rozłączny z terminarzem — był jego podzbiorem**. Zbudowanie go
uruchomiłoby mechanizm zmierzony 11.08 na „wapno bielik": sześć własnych URL-i na jedną intencję
i najlepsza pozycja 15,3, przy czym terminarz ma przewagę startu, bo jest zaindeksowany.

## Decyzja

**Terminarz jest drugim hubem serwisu — hubem osi KIEDY.** Nie jest to konflikt z hubem
`/jakie-wapno-na-pole/`, bo osie są rozłączne: tamten odpowiada **czym wapnować**, ten **kiedy**.

Serwis ma więc dwa huby i z każdego rozchodzą się strony szczegółowe:

| Hub | Oś | Rozchodzi się na |
|---|---|---|
| `/jakie-wapno-na-pole/` (do zbudowania, 10.09) | **JAKIE** — rodzaj wapna × typ gleby | dobór formy, tabela uprawowa, kalkulator |
| `/jak-stosowac-wapno-nawozowe/` (istnieje) | **KIEDY** — termin i okno agrotechniczne | wpisy uprawowe wg **przedplonu**, patrz mapa niżej |

### Oś stron szczegółowych to PRZEDPLON, nie termin

Strona uprawowa nie powtarza terminarza. Odpowiada na inne pytanie: nie „kiedy wolno",
tylko **„czy przy moim przedplonie mam jak zdążyć"**. Materiał, którego terminarz nie zawiera
i zawierać nie powinien:

- tabela **przedplon → data zbioru → ile tygodni okna → jaka forma wapna** (rzepak po jęczmieniu
  ozimym, pszenica po rzepaku, pszenica po pszenicy, pszenica po kukurydzy na ziarno — gdzie okna
  praktycznie nie ma);
- kolizja z nawożeniem startowym: rzepak dostaje azot przedsiewnie, a wapno wymaga 2–4 tygodni
  odstępu od nawozów azotowych — przy oknie czterotygodniowym to się arytmetycznie nie spina;
- zagadnienia gatunkowe wiążące się z odczynem (np. bor przy rzepaku, parch przy ziemniaku —
  ten ostatni już opisany w terminarzu i **nie do powtórzenia**).

Ta oś skaluje się na rok: każda uprawa ma inny przedplon i inne okno, więc kolejne wpisy
nie powielają się nawzajem.

### Reguła kurczenia sekcji

Sekcja uprawowa w terminarzu **kurczy się do dwóch–trzech zdań plus link dopiero w momencie,
gdy jej strona szczegółowa istnieje**. Dopóki strony nie ma, sekcja zostaje pełna — pełna sekcja
jest lepsza niż link donikąd. Kurczenie wchodzi **w tym samym wdrożeniu** co publikacja strony,
nie później.

Reguła 2 z ADR porannego („hub nie dostaje ani jednego H2 z nazwą uprawy") obowiązuje odtąd
oba huby, z powyższym zastrzeżeniem o kolejności.

## Roczna mapa wpisów rozchodzących się z terminarza

Kolumna „Popyt" podaje wyłącznie wartości **zmierzone** — planer z audytu T-052 albo GSC
za 90 dni. Puste pole znaczy „niezmierzone", nie „zero"; przed wejściem w temat trzeba zmierzyć,
bo planer zaokrągla ogon do zera (dowód: kukurydza wyceniona na 0, a w GSC ma realne zapytanie).

| Okno sezonowe | Temat | Popyt zmierzony | Stan |
|---|---|---|---|
| VIII–IX | **Zboża ozime i rzepak — okno między żniwami a siewem** | 190/mies.; GSC: `jakie wapno pod pszenice ozimą` poz. **2,0**, `jakie wapno pod jeczmien ozimy` poz. **2,0**, `jakie wapno pod rzepak` poz. **3,0**, `wapnowanie pod rzepak` poz. **4,0** | oś przestawiona na przedplon, priorytet obniżony — patrz „Konsekwencje" |
| IX–X | **Łąki i pastwiska** | 210/mies.; GSC: `ile wapna na hektar łąki` 25 wyśw. poz. **7,2**, `ile wapna granulowanego na hektar łąki` 22 wyśw. poz. **10,9** | w planie T-055, termin 15.09 |
| IX–X | **Ziemniaki** | 170/mies. | w planie T-055, termin 20.09. **Uwaga: parch i wapnowanie pogłówne w redliny już opisane w terminarzu** — strona musi wejść od strony przedplonu i zmianowania |
| X–XI | **Kukurydza jako przedplon i jako uprawa** | planer **0**; GSC: `wapnowanie po kukurydzy` 6 wyśw., nasza pozycja **64,2** | pierwszy kandydat awansu z tabeli — zapytanie istnieje, odpowiedzi nie mamy |
| XI–III | **Sadownictwo** | 470/mies., 9 fraz | osobna pozycja **T-065**, szczyt XI i III |
| I–II | **Badanie gleby i odczyn przed sezonem** | 6 320/mies. (`ph gleby` 1 000, `badanie gleby` 1 000, `zakwaszenie gleby` 390, `stacja chemiczno-rolnicza` 260) | osobna pozycja **T-057** — klaster wypadł z audytu majowego przez filtr regexowy |
| III–IV | **Wapnowanie wiosenne i przedsiewne** | 70/mies. po odsianiu trawnika i działki | poniżej progu URL-a — **sekcja terminarza, nie osobny adres** |
| III–V | Buraki | planer **0** | do zmierzenia w GSC przed decyzją |
| V–VI | Użytki zielone po pierwszym pokosie | — | do zmierzenia |
| VII–VIII | Wapnowanie pożniwne — szczyt operacyjny | `kiedy wapnować glebę` 320 (**X: 590**), `kiedy siać wapno granulowane` 420 | **rdzeń terminarza, zostaje w nim** |

**Próg wejścia bez zmian:** ≥3 frazy i ≥100 wyszukań/mies. łącznie, liczone z GSC.
Przegląd kwartalny: `query × page` filtrowane po nazwach upraw.

## Konsekwencje

1. **`/wapno-pod-zboza-ozime/` nie powstaje jako powtórka terminarza.** Jeżeli powstanie,
   to na osi przedplonowej, a sekcja w terminarzu kurczy się w tym samym wdrożeniu.
2. **Kolejność wrześniowa zmieniona.** Ozime schodzą za staw. Proporcja rozstrzygająca:
   ozime 190/mies. przy pokryciu, które już mamy, wobec stawu **4 100/mies. przy pokryciu zerowym**
   (0 wyświetleń w GSC na czymkolwiek ze słowem „staw", trzy z siedmiu wyników TOP7 to posty
   z Facebooka). Hub `/jakie-wapno-na-pole/` zostaje na 10.09 — tam kolizji nie ma.
3. **Dług źródłowy do spłacenia przed pisaniem stron uprawowych.** Terminarz cytuje IUNG-PIB,
   ale **w repo nie ma ani jednego pliku źródłowego** — `grep` po „IUNG" trafia wyłącznie
   w dokumentację projektu. Tabela przedplonów, bor przy rzepaku i zimowanie ozimin wymagają
   źródła, a reguła projektu mówi wprost: parametry z dokumentów producentów i instytutów,
   nigdy z rozumowania. Do zdobycia: *Poradnik wapnowania gleb gruntów ornych* (IUNG-PIB,
   Puławy 2021) i *Zasady ustalania dawek wapna w doradztwie nawozowym* (Jadczyszyn, Lipiński,
   IUNG-PIB 2022, ISBN 978-83-7562-385-7) — do `data/zrodla/`, z wyciągiem numerów tabel.

## Co ta decyzja unieważnia

| Ustalenie | Nowy status |
|---|---|
| T-055: spoke `/wapno-pod-zboza-ozime/` na frazach terminowych, termin 05.09 | **zastąpione** — oś na przedplon, priorytet za stawem |
| Kolejność z ADR porannego: ozime 05.09 → hub 10.09 → łąki 15.09 → ziemniaki 20.09 | **zmieniona** — staw → hub 10.09 → łąki 15.09 → ziemniaki 20.09 → ozime po zdobyciu źródeł |
| Terminarz jako „strona docelowa jednej intencji" | **zastąpione** — terminarz jest hubem osi KIEDY |
