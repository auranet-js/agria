# Prompt startowy — Google Ads AGRIA, dzień 5: gdzie są leady (18.08.2026)

> Poprzedni wątek: `docs/decyzje/2026-08-14-korekty-kampanii-i-geoblok.md` (commit `bf75788`).
> Wcześniejszy prompt: `docs/prompty/2026-08-15-PROMPT_ADS_DZIEN2.md`.
> **Uwaga: po 14.08 nie ma w repo żadnego zapisu o kampaniach.** Jeśli między 15 a 17.08
> coś zmieniano na koncie, wyjdzie to dopiero z API — nie zakładaj, że stan odpowiada ADR-owi.

---

## Prompt do skopiowania

```
Wątek: Google Ads AGRIA — dzień 5. Pytanie Janka brzmi wprost: nie widać żadnych
leadów przy niemałym budżecie. Trzeba rozstrzygnąć dlaczego i co z tym zrobić.

Przeczytaj najpierw:
- docs/decyzje/2026-08-13-uruchomienie-kampanii-ads.md (struktura konta)
- docs/decyzje/2026-08-14-korekty-kampanii-i-geoblok.md (korekty po pierwszym dniu)
- docs/decyzje/2026-08-11-podzial-rol-ads-seo.md (dokąd wolno kierować reklamy)
- memory: project_agria_ads_kampanie_zywe, project_agria_ads_sezonowosc,
  project_agria_ga4_consent_blocker, project_agria_architektura_kanalow

Stan wyjściowy: konto 674-207-1446, dwie kampanie MANUAL_CPC (Rolnictwo 34 zł/dz,
Marka 6 zł/dz). Pierwsza emisja 14.08 o 14:00. Po 14.08 brak zapisów w repo —
zweryfikuj stan konta na żywo, nie z dokumentów.

Narzędzie: scripts/google/ads_call.sh (helper, wzorzec z pmpfibertech).


PYTANIE ZEROWE — rozstrzygnij je przed całą resztą

Czy leadów NIE MA, czy ich NIE WIDAĆ. To nie to samo i cała dalsza analiza zależy
od odpowiedzi.

Konwersje mierzymy z połączeń telefonicznych, a memory project_agria_ga4_consent_blocker
mówi, że pomiar jest zepsuty: w lipcu GA4 pokazał 5 sesji organicznych przy 221
kliknięciach z GSC, bo Consent Mode odmawia zgody wobec braku banera. Jeśli to samo
dotyczy konwersji Ads, „zero leadów" jest artefaktem pomiaru, a nie faktem o rynku —
i wtedy optymalizowanie kampanii pod ten wskaźnik jest gonieniem własnego ogona.

Sprawdź konkretnie:
- czy akcja konwersji w Ads w ogóle rejestruje cokolwiek (status, ostatnia konwersja,
  czy tag zbiera dane),
- czy kliknięcia w numer telefonu docierają do GA4 (Realtime, nie raport dzienny —
  raporty chodzą 4-6 h za rzeczywistością),
- czy rotacja dwóch numerów (Paweł, Kazimierz) działa i czy da się w ogóle
  przypisać połączenie do kampanii.

Powiedz wprost, co jest zmierzone, a co niemierzalne. Jeśli pomiar nie działa —
to jest zadanie numer jeden, przed jakąkolwiek optymalizacją stawek.


1. BILANS PIĘCIU DNI

Zestaw 14-18.08 dzień po dniu: wyświetlenia, kliknięcia, CTR, śr. CPC, koszt,
konwersje — osobno dla obu kampanii i dla każdej grupy reklam.

Odpowiedz na trzy rzeczy:
- ile realnie wydaliśmy wobec 40 zł/dz i czy budżet się wyczerpuje, czy zostaje,
- o której godzinie gaśnie emisja (po korekcie harmonogramu z 14.08),
- czy kampania Marka nadal ma zero wyświetleń.


2. NA CO REALNIE PŁACIMY — search terms za cały okres

Wyciągnij search_term_view i podziel zapytania na trzy koszyki, z kosztem każdego:

a) ZAKUPOWE - kto chce kupić tonaż („wapno nawozowe cena", „wapno granulowane
   big bag", „wapno luzem transport")
b) EDUKACYJNE - kto się uczy, a nie kupuje („kiedy wapnować", „dawkowanie wapna
   na hektar", „jakie wapno pod rzepak"). Hipoteza Janka: możliwe, że płacimy
   głównie za ten koszyk i dlatego nikt nie dzwoni.
c) CUDZE MARKI I KOPALNIE - zapytania o konkretnego producenta lub zakład
   („wapno sitkówka", „nordkalk", „polcalc", „wapniak kornicki").

Przy koszyku (c) postaw pytanie handlowe, nie techniczne: ktoś szukający wapna
z konkretnej kopalni zwykle wie, czego chce i skąd to bierze. Czy chcemy za to
płacić? Policz, ile nas to kosztowało przez pięć dni, i daj rekomendację —
wykluczyć czy zostawić. To decyzja marketingowa, więc podejmujemy ją my
(patrz MASTER_PROMPT, „Kto podejmuje decyzje marketingowe").


3. HIPOTEZA JANKA — własne nazwy produktowe zamiast generycznego „wapna"

Do sprawdzenia: czy nie lepiej celować w „Agrobielik 70" i „Agrobielik 90"
niż konkurować o drogie, ogólne „wapno nawozowe".

Zweryfikuj to danymi, nie opinią:
- jaki jest miesięczny wolumen wyszukiwań dla „agrobielik", „agrobielik 70",
  „agrobielik 90", „bielik wapno" (DataForSEO przez curl, sekrety
  w ~/secrets/dataforseo/ - saldo bywa niskie, sprawdź przed serią zapytań),
- co pokazuje kampania Marka: jeśli po pięciu dniach nadal ma zero wyświetleń,
  to znaczy, że tej marki nikt nie wyszukuje, i hipoteza upada — powiedz to wprost,
- czy w search terms pojawiły się w ogóle jakiekolwiek zapytania markowe.

Jeśli wolumen jest zerowy, zaproponuj co innego zamiast tego: np. frazy
z tonażem i logistyką, które odsiewają hobbystę („wapno 24 tony", „wapno
całopojazdowo", „wapno big bag 1000 kg").


4. GDZIE LĄDUJE RUCH

Sprawdź, czy reklamy kierują na /wapno-granulowane/ i /wapno-nawozowe/ i czy te
strony są sprawne (200, treść się renderuje, numer telefonu widoczny nad zgięciem,
LCP na mobile). Landingi są celami Ads i stoją poza indeksem — tak ma być, patrz
ADR 2026-08-11. NIE proponuj nowych landingów organicznych ani wpuszczania tych
do indeksu; kanibalizacja jest zmierzona.


5. REKOMENDACJA

Zamknij jednym akapitem: czy kampania ma sens w obecnej formie, co zmieniamy
w tym tygodniu i czego świadomie nie ruszamy. Jeśli wniosek brzmi „za wcześnie
na ocenę", powiedz to zamiast dorabiać optymalizacje do pięciu dni danych —
ale wtedy podaj, ile dni i ilu kliknięć potrzeba, żeby ocena miała sens.

Zasada obowiązująca w całym wątku: każde twierdzenie o stanie konta z dowodem
obok (wykonane zapytanie i jego wynik). Bez dowodu pisz „niezweryfikowane".
```

---

## Czego ten wątek NIE dotyka

- **Ofertownik** — osobny wątek, projekt własny Auranet (`docs/specs/2026-08-18-ofertownik-design.md`).
- **OLX** — czeka na pakiet po stronie AGRII, plus poprawki treści z 18.08.
- **Kalkulator Mg** — u Kazimierza do weryfikacji.
- **Nowe landingi organiczne** — zablokowane ADR-em o kanibalizacji.

Stan wszystkich wątków: `docs/PROJECT_STATE.md`, sekcja z 18.08.
