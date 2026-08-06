# Ceny na agria.pl — analiza i rekomendacja

> Data: 2026-08-06. Powód: pytanie Janka, czy wprowadzenie cen pomogłoby, w kontekście obecności marki Agrobielik na OLX.
> Źródła: DataForSEO (search volume + SERP live, pull 06.08), OLX (weryfikacja ogłoszeń), audyt schema agria.pl.
> **Status: rekomendacja do decyzji.** Wymaga faktu handlowego od AGRII (widełki cenowe) — patrz §5.

---

## 1. Punkt wyjścia — dotychczasowe założenie

`ROZPISKA_INTENCJA_WOLUMENOWA_2026-07-14.md` §3 ustaliła: **zero ceny, zero koszyka**, CTA „zapytaj o ofertę — podaj tonaż". Uzasadnienie: segregację intencji robi landing, nie fraza — detalista odbija się sam, rolnik całopojazdowy zostaje. Dowód: Biovita stoi #1 na „wapno nawozowe" stroną bez ceny i bez koszyka.

**To założenie pozostaje słuszne dla fraz ogólnych.** Nie obejmuje natomiast osobnej warstwy zapytań, której wtedy nie policzyliśmy.

---

## 2. Czego nie widzieliśmy — klaster cenowy

| Fraza | Vol/mies. | CPC USD | Konkurencja |
|---|---|---|---|
| wapno granulowane cena | **480** | 0,73 | HIGH |
| wapno granulowane olx | **320** | 0,18 | MEDIUM |
| **ile kosztuje tona wapna** | 110 | **5,32** | — |
| wapno nawozowe cena | 90 | 0,66 | HIGH |
| wapno palone cena | 90 | 0,15 | HIGH |
| cena wapna nawozowego | 70 | 1,36 | HIGH |
| wapno rolnicze cena | 40 | 0,77 | HIGH |
| wapno nawozowe olx | 40 | 0,64 | HIGH |
| ile kosztuje wapno nawozowe | 40 | 0,80 | — |
| wapno nawozowe allegro | 20 | 0,02 | HIGH |
| wapno nawozowe cena za tonę | 10 | — | — |
| wapno nawozowe cennik | 10 | — | — |
| **Razem** | **~1 320** | | |

Dla skali: **cała witryna miała w lipcu 10 220 wyświetleń.** AGRIA ma dziś w tym klastrze zerową obecność.

Osobno warto zapamiętać **„ile kosztuje tona wapna" — CPC 5,32 USD**, najwyższe w całym projekcie (dla porównania: stabilizacja gruntu 2,65, wapnowanie gleby 1,64). Rynek płaci za to zapytanie najwięcej, bo to moment tuż przed zakupem.

---

## 3. Co mówi SERP — a mówi jednoznacznie

TOP20 dla **„wapno granulowane cena"** (480/mies., DataForSEO live 06.08):

| # | Domena | Typ |
|---|---|---|
| 1 | sklep.rolmat.pl | sklep z ceną |
| 2 | **olx.pl** | marketplace |
| 3 | sklep.agrosklad.com.pl | sklep z ceną |
| 4 | allegro.pl | marketplace |
| 5 | youtube.com | wideo |
| 6–9 | farma-malecki, poradnikogrodniczy, osadkowski, agrochem | sklepy + jeden poradnik |
| 10–20 | sprzedajemy, dlaroslin, agrozam, agrosimex, olx, agrolok, **ceneo**, zasiejpole, erli, wpolu | sklepy i porównywarki |

**Ani jednego katalogu B2B bez ceny w całej dwudziestce.** To nie jest kwestia jakości treści — Google dla tej frazy nagradza konkretny typ strony: ofertę z podaną ceną. Bez ceny na te frazy nie wchodzimy, choćbyśmy napisali najlepszy tekst w branży.

To jest dokładnie odwrotna sytuacja niż na frazie „wapno nawozowe", gdzie Biovita wygrywa stroną bez ceny. **Dwie różne intencje, dwa różne typy strony.**

---

## 4. OLX — weryfikacja

Sprawdzone na OLX: **marka Agrobielik jest tam obecna z cenami, ale wystawiają ją inne podmioty.**

| Ogłoszenie | Cena | Lokalizacja |
|---|---|---|
| Wapno tlenkowe palone AGROBIELIK 70 | 210 zł | Kielce |
| Wapno tlenkowe AGROBIELIK 60 odm. 03 | 249 zł/t luz · 319 zł/t big-bag | Barcin |
| Wapno nawozowe (Kujawit, Radkowit, Dewonit) | 35 zł | Barcin |
| wapno siarkowe, węglanowe, magnezowe — atesty | 35 zł | Gliwice |

Nie znalazłem ogłoszenia z Tarnowa ani wystawionego przez AGRIĘ. **Do potwierdzenia u Pawła, czy AGRIA ma tam własne konto.**

Wniosek jest mocniejszy niż samo pytanie: **cena produktów AGRII jest już publiczna — tyle że publikują ją pośrednicy i to oni zbierają na tym zapytania.** Argument „nie pokazujemy cen, bo B2B" chroni więc informację, która tajemnicą nie jest. Chroni wyłącznie *naszą* cenę, przy jednoczesnym oddaniu ruchu.

Osobno: **„wapno granulowane olx" ma 320 wyszukiwań miesięcznie.** Ludzie celowo szukają wapna na OLX, bo tam znajdują cenę od ręki.

---

## 5. Rekomendacja — rozdzielić warstwy, podać widełki za tonę

**Nie cennik detaliczny. Widełki „od X zł/t netto" w osobnej warstwie treści.**

| Warstwa | Cena | Uzasadnienie |
|---|---|---|
| Landingi ogólne (`/wapno-nawozowe/`, `/wapno-granulowane/`) | **bez ceny**, CTA „podaj tonaż" | Bez zmian. Tu Biovita wygrywa bez ceny, a brak ceny odsiewa intencję detaliczną. |
| **Nowa sekcja „Ile kosztuje wapno" na landingach** | **widełki od X zł/t** | Przechwytuje klaster cenowy bez przekształcania landingu w sklep. |
| Poradnik „Ile kosztuje wapnowanie hektara" | widełki + kalkulacja na ha | Fraza „ile kosztuje tona wapna" ma CPC 5,32 — najwyższy w projekcie. Naturalne rozwinięcie kalkulatora, który już rankuje. |
| Karty produktów | cena „od" w WooCommerce | **Odblokowuje `offers` w schema `Product`** — dziś RankMath wypuszcza `Product` bez oferty, czyli wydmuszkę. Cena w SERP podnosi CTR. |

**Dlaczego akurat widełki za tonę, a nie cennik:**

1. **Cena za tonę sama odsiewa hobbystę** — działkowiec szukający worka 25 kg odbija się od „od 210 zł/t przy dostawie całopojazdowej" skuteczniej niż od braku ceny. Brak ceny go nie odstrasza, tylko zmusza do telefonu, który ktoś musi odebrać.
2. **Widełki zachowują elastyczność negocjacyjną** — „od" nie jest zobowiązaniem, jest punktem wejścia. Rabaty per tonaż i kontrakt roczny zostają w rękach handlowca.
3. **Cena wapna i tak zależy od transportu** — to trzeba w treści powiedzieć wprost („cena zależy od odległości i formy dostawy"), co jest jednocześnie uczciwe i uzasadnia widełki.
4. **Ads bez ceny są droższe** — użytkownik klika reklamę na frazę cenową, nie znajduje ceny, wraca do wyników. Przy budżecie 1 200 zł/mies. to realna strata, a jakość strony docelowej wpływa na koszt kliknięcia.

**Czego nie robimy:** koszyka, cen za opakowania detaliczne, cennika sztywnego w PDF, konkurowania ceną z Allegro i Ceneo. Wchodzimy w klaster cenowy jako **dostawca całopojazdowy z widełkami**, nie jako sklep.

---

## 6. Co potrzebne od AGRII (fakt handlowy, nie decyzja marketingowa)

Jedno pytanie do Pawła: **jakie widełki „od … zł/t netto" możemy podać** dla głównych grup — tlenkowe, węglanowe sypkie, granulowane, kreda — przy dostawie całopojazdowej, i czy cena ma być podana z transportem czy loco magazyn.

Dodatkowo warto potwierdzić: **czy AGRIA ma własne konto na OLX.** Jeśli nie — to osobny temat, bo pośrednicy sprzedają tam pod marką Agrobielik i przechwytują 360 wyszukiwań miesięcznie („wapno granulowane olx" + „wapno nawozowe olx").

Do czasu odpowiedzi **nie wpisujemy żadnych kwot** — liczby z OLX w §4 są cenami pośredników, nie AGRII, i nie wolno ich użyć jako naszych.

---

## 7. Wpływ na plan M3

Rekomendacja **nie opóźnia** startu kampanii 14.08:

- landingi publikujemy bez cen zgodnie z planem — sekcja cenowa to dopisanie jednego bloku, gdy przyjdą widełki,
- kampania rolnicza rusza na frazach ogólnych; **frazy cenowe dokładamy dopiero po wprowadzeniu sekcji** (reklama na „wapno granulowane cena" kierowana na stronę bez ceny = przepalony budżet),
- cena na kartach produktów i naprawa schema `Product` — po decyzji, poza ścieżką krytyczną Ads.
