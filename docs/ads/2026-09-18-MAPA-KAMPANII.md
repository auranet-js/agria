# Mapa kont a Google Ads — AGRIA, stan na 18.09.2026

> **Konto:** 674-207-1446 (direct, nie pod MCC) · **odczyt:** API v25, 18.09
> **Okres metryk:** 14.08–17.09 (5 tygodni emisji) · **wydatek łączny: 1 558,75 zł**
> Wszystko poniżej to **stan zastany**, nie projekt. Projekt zmian: `2026-09-18-PROJEKT-PRZEBUDOWY-KAMPANII.md`

## Widok z góry

```
KONTO 674-207-1446  ·  MANUAL_CPC (eCPC wyłączone)  ·  sieć partnerska i display WYŁĄCZONE
│
├── AGRIA - Rolnictwo          60 zł/dz   1 214,20 zł   ENABLED / SERVING
│   │  geo: 2 promienie 150 km (50.135,20.850 · 50.217,21.017), PRESENCE
│   │       minus 8 miast: Kraków, Nowy Sącz, Tarnów, Rzeszów, Kielce, Bielsko-Biała, Częstochowa, Katowice
│   │  harmonogram: niedziela, poniedziałek, wtorek — 6:00–22:00
│   │  wykluczenia kampanii: 127 (frazowe)
│   │
│   ├── Wapno granulowane      11 fraz   463,79 zł  →  /wapno-granulowane/   [noindex]
│   ├── Wapno nawozowe         25 fraz   292,48 zł  →  /wapno-nawozowe/      [noindex]
│   └── Wapno magnezowe i kreda 14 fraz  230,58 zł  →  /wapno-nawozowe/      [noindex]
│       (każda z grup ma 6 wykluczeń paszowych: drób, kury, kurnik, kur niosek, pastewna, paszowa)
│
├── AGRIA - Paszarstwo          9 zł/dz     260,36 zł   ENABLED / SERVING
│   │  geo: CAŁA POLSKA · harmonogram: 7 dni 6:00–22:00 · wykluczenia: 23
│   └── Kreda pastewna         13 fraz   260,36 zł  →  /paszarstwo/kreda-pastewna/  [w indeksie]
│
└── AGRIA - Marka               5 zł/dz      84,19 zł   ENABLED / SERVING
    │  geo: CAŁA POLSKA · harmonogram: 7 dni 6:00–22:00 · wykluczenia: BRAK
    └── Brand                   8 fraz    84,19 zł  →  /  (ścieżka wyświetlana /oferta/)
```

## Liczby zbiorcze

| | 14.08–17.09 |
|---|---|
| wydatek | 1 558,75 zł |
| kliknięcia | 906 · CTR 11,3% · CPC 1,72 zł |
| konwersje | **5**, wszystkie `phone_click` → **311,75 zł za konwersję** |
| mobile | **90% kosztu** (1 408 zł) · desktop 143 zł · tablet 7 zł |
| frazy aktywne | 71 pozytywnych w 5 grupach |
| wykluczenia | 150 frazowych na poziomie kampanii + 18 na poziomie grup |
| jakość strony docelowej | **`poniżej średniej` na 40 z 50 ocenionych fraz** |

## Dni tygodnia

| dzień | wyśw. | klik. | koszt | CPC | kto emituje |
|---|---|---|---|---|---|
| niedziela | 1 852 | 219 | **398,92 zł** | 1,82 zł | wszystkie trzy |
| poniedziałek | 1 872 | 215 | **386,02 zł** | 1,80 zł | wszystkie trzy |
| wtorek | 1 658 | 186 | 331,83 zł | 1,78 zł | wszystkie trzy |
| środa | 928 | 82 | 123,82 zł | **1,51 zł** | Paszarstwo + Marka |
| czwartek | 485 | 56 | 84,33 zł | **1,51 zł** | Paszarstwo + Marka |
| piątek | 771 | 73 | 118,66 zł | 1,63 zł | Paszarstwo + Marka |
| sobota | 757 | 75 | 115,17 zł | 1,54 zł | Paszarstwo + Marka |

## Godziny (wrzesień, 749,17 zł)

Emisja 6:00–22:00. W godzinach pracy biura **8:00–16:00 schodzi 495,13 zł (66,1%)**, poza nimi 254,04 zł.
Szczyty: 10:00 (107,46 zł), 12:00 (73,85), 15:00 (67,77). Ostatnia godzina 21:00–22:00: 15,02 zł.

## Skąd klikają (obecność fizyczna, nie zainteresowanie)

| region | Rolnictwo | Paszarstwo | Marka |
|---|---|---|---|
| małopolskie | 264,01 zł (22%) | 27,36 zł | 33,42 zł (40%) |
| lubelskie | 203,85 zł (17%) | 16,68 zł | 5,93 zł |
| podkarpackie | 194,62 zł (16%) | 22,46 zł | 5,41 zł |
| mazowieckie | 107,56 zł (9%) | 26,06 zł | 2,97 zł |
| świętokrzyskie | 101,54 zł (8%) | — | 11,47 zł |
| śląskie | 99,47 zł (8%) | 27,16 zł | — |
| Warszawa | 56,79 zł (5%) | **40,53 zł (16%)** | 7,38 zł |
| łódzkie | 46,12 zł (4%) | — | — |
| wielkopolskie | — | 22,41 zł (9%) | 7,87 zł |
| dolnośląskie | — | 15,39 zł (6%) | 4,90 zł |

## Strony docelowe i ich koszt (01–17.09)

| kampania / grupa | strona | indeks | koszt |
|---|---|---|---|
| Rolnictwo / Wapno granulowane | `/wapno-granulowane/` | **noindex** | 225,92 zł |
| Rolnictwo / Wapno nawozowe | `/wapno-nawozowe/` | **noindex** | 161,19 zł |
| Rolnictwo / Wapno magnezowe i kreda | `/wapno-nawozowe/` | **noindex** | 156,50 zł |
| Paszarstwo / Kreda pastewna | `/paszarstwo/kreda-pastewna/` | w indeksie | 162,12 zł |
| Marka / Brand | `/` | w indeksie | 43,44 zł |

**543 zł z 749 zł (72%) prowadzi na dwie strony wyłączone z indeksu.**

---

# Frazy — komplet, per grupa

### AGRIA - Rolnictwo / Wapno granulowane — 11 fraz, 463.79 zł
| fraza | dopasowanie | wyśw. | klik. | koszt | QS | strona docelowa |
|---|---|---|---|---|---|---|
| wapno granulowane | frazowe | 470 | 62 | 120.63 zł | 7 | średnia |
| wapno granulowane cena | frazowe | 265 | 49 | 96.18 zł | 5 | poniżej |
| wapno granulowane | ścisłe | 441 | 41 | 80.70 zł | 7 | średnia |
| wapno nawozowe granulowane | frazowe | 227 | 30 | 59.14 zł | 5 | poniżej |
| kreda granulowana | frazowe | 191 | 22 | 43.27 zł | 4 | poniżej |
| wapno granulowane big bag | frazowe | 97 | 15 | 28.82 zł | 5 | poniżej |
| wapno węglanowe granulowane | frazowe | 88 | 8 | 15.45 zł | 3 | poniżej |
| granulat wapniowy | frazowe | 9 | 5 | 9.78 zł | — | — |
| wapno tlenkowe granulowane | frazowe | 48 | 4 | 7.87 zł | 3 | poniżej |
| wapno węglanowe cena za tonę | frazowe | 11 | 1 | 1.95 zł | 3 | średnia |
| wapno granulowane luzem | frazowe | 1 | 0 | 0.00 zł | 3 | poniżej |

### AGRIA - Rolnictwo / Wapno magnezowe i kreda — 14 fraz, 230.58 zł
| fraza | dopasowanie | wyśw. | klik. | koszt | QS | strona docelowa |
|---|---|---|---|---|---|---|
| kreda nawozowa | frazowe | 453 | 37 | 72.11 zł | 3 | poniżej |
| wapno z magnezem | frazowe | 185 | 25 | 47.06 zł | 3 | poniżej |
| wapno magnezowe | frazowe | 147 | 19 | 37.12 zł | 4 | poniżej |
| wapno magnezowe | ścisłe | 133 | 17 | 29.21 zł | 4 | poniżej |
| wapno magnezowe granulowane | frazowe | 103 | 12 | 23.54 zł | 3 | poniżej |
| wapno magnezowe granulowane big bag | frazowe | 6 | 4 | 7.95 zł | 6 | poniżej |
| wapno kredowe luzem | frazowe | 5 | 4 | 7.77 zł | 6 | poniżej |
| wapno magnezowe big bag | frazowe | 9 | 2 | 3.92 zł | 8 | średnia |
| kreda nawozowa luzem | frazowe | 1 | 1 | 1.90 zł | 7 | poniżej |
| wapno dolomitowe cena za tonę | frazowe | 2 | 0 | 0.00 zł | — | — |
| kreda nawozowa big bag | frazowe | 2 | 0 | 0.00 zł | 1 | poniżej |
| dolomit nawozowy | frazowe | 2 | 0 | 0.00 zł | — | — |
| wapno węglanowo-magnezowe | frazowe | 11 | 0 | 0.00 zł | 6 | średnia |
| wapno magnezowe luzem cena | frazowe | 2 | 0 | 0.00 zł | 8 | średnia |

### AGRIA - Rolnictwo / Wapno nawozowe — 25 fraz, 292.48 zł
| fraza | dopasowanie | wyśw. | klik. | koszt | QS | strona docelowa |
|---|---|---|---|---|---|---|
| wapno na pole | frazowe | 179 | 32 | 62.80 zł | 4 | poniżej |
| wapno nawozowe | ścisłe | 164 | 27 | 52.13 zł | 5 | poniżej |
| wapno tlenkowe | frazowe | 138 | 17 | 33.38 zł | 1 | poniżej |
| wapno nawozowe luzem | frazowe | 47 | 14 | 26.23 zł | 7 | poniżej |
| wapno nawozowe cena za tonę | frazowe | 40 | 12 | 23.07 zł | 6 | poniżej |
| wapno big bag | frazowe | 76 | 12 | 22.52 zł | 2 | poniżej |
| wapno cena za tonę | frazowe | 58 | 9 | 17.33 zł | 2 | poniżej |
| wapno luzem | frazowe | 29 | 7 | 13.78 zł | 5 | poniżej |
| wapno na pole | ścisłe | 29 | 6 | 11.71 zł | 4 | poniżej |
| cena wapna na pole | frazowe | 19 | 5 | 9.70 zł | 3 | poniżej |
| cena wapna za tonę | frazowe | 16 | 4 | 7.92 zł | — | — |
| wapno nawozowe big bag | frazowe | 22 | 2 | 3.99 zł | 5 | poniżej |
| wapno rolnicze cena za tonę | frazowe | 4 | 2 | 3.94 zł | — | — |
| wapno na pole cena | frazowe | 13 | 1 | 1.99 zł | 6 | poniżej |
| wapno na pole luzem | frazowe | 5 | 1 | 1.99 zł | 7 | poniżej |
| wapno rolnicze | frazowe | 0 | 0 | 0.00 zł | — | — |
| wapno pod rzepak | frazowe | 13 | 0 | 0.00 zł | — | — |
| wapno do gleby | frazowe | 0 | 0 | 0.00 zł | — | — |
| wapno tlenkowe luzem | frazowe | 1 | 0 | 0.00 zł | 4 | średnia |
| wapno nawozowe | frazowe | 0 | 0 | 0.00 zł | — | — |
| wapno do odkwaszania gleby | frazowe | 0 | 0 | 0.00 zł | — | — |
| wapno węglanowe | frazowe | 0 | 0 | 0.00 zł | — | — |
| wapno sypkie na pole | frazowe | 2 | 0 | 0.00 zł | 3 | poniżej |
| wapno pod orkę | frazowe | 0 | 0 | 0.00 zł | — | — |
| wapno rolnicze luzem | frazowe | 1 | 0 | 0.00 zł | — | — |

### AGRIA - Paszarstwo / Kreda pastewna — 13 fraz, 260.36 zł
| fraza | dopasowanie | wyśw. | klik. | koszt | QS | strona docelowa |
|---|---|---|---|---|---|---|
| kreda pastewna dla kur | frazowe | 1240 | 95 | 112.49 zł | 4 | poniżej |
| kreda pastewna | ścisłe | 736 | 48 | 56.50 zł | 3 | poniżej |
| kreda pastewna | frazowe | 596 | 29 | 33.15 zł | 3 | poniżej |
| kreda dla kur niosek | frazowe | 114 | 10 | 11.92 zł | 3 | poniżej |
| kreda pastewna dla kur niosek | frazowe | 91 | 10 | 11.85 zł | 4 | poniżej |
| kreda paszowa | frazowe | 134 | 9 | 10.68 zł | 3 | poniżej |
| kreda pastewna cena | frazowe | 45 | 8 | 9.53 zł | 4 | poniżej |
| kreda pastewna dla bydła | frazowe | 65 | 6 | 7.09 zł | 4 | poniżej |
| wapno dla kur niosek | frazowe | 76 | 5 | 5.96 zł | 3 | poniżej |
| kreda pastewna gruboziarnista | frazowe | 19 | 1 | 1.18 zł | 4 | poniżej |
| wapno pastewne | frazowe | 18 | 0 | 0.00 zł | 2 | poniżej |
| węglan wapnia dla drobiu | frazowe | 0 | 0 | 0.00 zł | — | — |
| kreda pastewna dawkowanie | frazowe | 0 | 0 | 0.00 zł | — | — |

### AGRIA - Marka / Brand — 8 fraz, 84.19 zł
| fraza | dopasowanie | wyśw. | klik. | koszt | QS | strona docelowa |
|---|---|---|---|---|---|---|
| agria | ścisłe | 165 | 18 | 31.21 zł | 8 | powyżej |
| agria tarnów | frazowe | 68 | 12 | 14.55 zł | 10 | powyżej |
| agria wapno | frazowe | 40 | 15 | 13.48 zł | 10 | powyżej |
| bielik wapno | frazowe | 197 | 9 | 13.30 zł | 3 | poniżej |
| oxyfertil | frazowe | 107 | 6 | 8.70 zł | 5 | średnia |
| agrobielik | frazowe | 12 | 1 | 1.48 zł | 1 | poniżej |
| agrobielik | ścisłe | 9 | 1 | 1.47 zł | 1 | poniżej |
| ekograncali | frazowe | 0 | 0 | 0.00 zł | — | — |


---

# Wykluczenia — stan zastany

## AGRIA - Rolnictwo (127, wszystkie frazowe)

**Marki konkurencji (43):** active calc · agrocalc · agrodol · agrolok · agros wap · agrowap · antigram ·
asmar · atrigran · biovita · calpol · complexor · dewonit · dobromir · dolokorn · fast cal · florovit ·
gold mag · grankal · humicalc · inovit · jurak · jurapol · józefka · kalkkreide · kornica · kornicki ·
koszelowska · koszelowski · kujawit · magnesia calc · morawica · morawicy · omya · orcal · osadkowski ·
polcalc · promyk · radkowice · radkowit · standard cal · suplagran · unicalc · wap mag · wapmag ·
wapnovit · waprol

**Detal i marketplace:** 5/10/20/25 kg · worek · worki · w workach · cena za worek · paczka · sklep ·
sklep internetowy · kup online · wysyłka kurierem · castorama · leroy · obi · działka · doniczka ·
ogród (9 odmian) · kwiaty · pomidory · maliny · warzywa · trawnik · rośliny doniczkowe

**Zastosowania spoza oferty:** bielenie · bielenie drzew · budowlane · murarskie · tynk · zaprawa ·
gaszone · do ścian · malarska · akwarium · basen · mech · mchu

**Intencje informacyjne:** co daje · co to jest · czy warto · dawka · dawkowanie · ile kg · ile wapna ·
jak stosować · jak wapnować (2 formy) · jakie wapno · kalkulator · kiedy stosować · kiedy wapnować (2 formy) ·
na czym polega · na ha · na hektar · najlepsze wapno · norma · opinie · po co · przed czy po · rodzaje wapna · forum

**Własne, żeby nie kanibalizować:** agria · bielik · ekograncali

## AGRIA - Paszarstwo (23, frazowe)

1/2/5 kg · akwarium · allegro · ceneo · chomik · dla ludzi · do jedzenia · do picia · empik · jadalna ·
kreda do tablicy · kreda krawiecka · kreda malarska · kreda szkolna · olx · papug · przepis · recenzje ·
sklep internetowy · ślimak · ślimaki

## AGRIA - Marka

**Brak wykluczeń.**

---

# Co mapa pokazuje

**1. Wykluczenia działają — i to trzeba odnotować.** 127 pozycji w Rolnictwie zatrzymało marki konkurencji:
ostatnie przecieki `agros wap`, `wapniak kornicki`, `dolokorn`, `agromit`, `wapna świętokrzyskie`, `supermag`
to **22–31.08**, potem cisza. Przez ostatnie trzy tygodnie przeszły tylko dwie marki spoza listy:
**`nordkalk`** (06.09 i 14.09, 3,94 zł) i **`wapniak jurajski`** (26.08 i 13.09, 3,95 zł).
Łączny koszt luki: **ok. 8 zł miesięcznie** — do dopisania, ale to nie jest pozycja oszczędnościowa.
⚠️ `nordkalk` wykluczamy ostrożnie: AGRIA jest autoryzowanym dystrybutorem, więc blokujemy zapytania
o kontakt do producenta, nie o produkty.

**2. Kampania Marka nie ma ani jednego wykluczenia** — jedyna bez nich.

**3. Struktura grup nie odpowiada strukturze stron.** Trzy grupy Rolnictwa prowadzą na dwie strony,
z czego jedna obsługuje dwie różne intencje (`/wapno-nawozowe/` dla grup „Wapno nawozowe"
i „Wapno magnezowe i kreda"). Stąd `poniżej średniej` na obu.

**4. Rolnictwo emituje w trzy dni, a wykluczenia paszowe ma na poziomie grup** — czyli architektura
zakłada rozdział rolnictwo/pasza, ale geo tego rozdziału nie utrzymuje: Paszarstwo strzela po całym kraju.

**5. Najlepsze i najgorsze frazy konta leżą w tej samej grupie.** Brand: `agria wapno` CTR 37,5%,
CPC 0,90 zł, QS 10 — i `agrobielik` QS 1 przy 21 wyświetleniach na pięć tygodni. Ta sama strona docelowa,
ta sama reklama. Różnica: dla pytania o firmę strona główna jest właściwą odpowiedzią, dla pytania
o produkt — nie jest.
