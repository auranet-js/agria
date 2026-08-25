# Fakty o kliencie — AGRIA Sp. z o.o.

> **Po co ten plik.** Jedno miejsce z faktami handlowymi i produktowymi, których model nie ma prawa
> zgadywać ani dopytywać u Janka, bo już je dostał. Powstał 19.08.2026 po incydencie, w którym wątek
> Ads doradzał w sprawie cen, nie wiedząc, że cennik przyszedł dwanaście dni wcześniej i leży w repo.
>
> **Każdy fakt ma źródło i datę.** Czego nie ma źródła — jest w sekcji „Czego nie wiemy", nie w tabelach.
> Wymiar „co zlecone i niezrobione" trzyma `docs/REJESTR_ZOBOWIAZAN.md`, nie ten plik.
>
> **Zasada aktualizacji:** gdy klient przyśle dane (mail, telefon, plik), fakt ląduje tutaj w tym samym
> commicie co dokument źródłowy. Plik bez wpisu = wiedza, której następna sesja nie zobaczy.

---

## 1. Firma

| Fakt | Wartość | Źródło |
|---|---|---|
| Nazwa | AGRIA Sp. z o.o. | KRS |
| KRS / NIP | 0000170666 / 8730006657 | raport M2, ścieżka odzysku GBP |
| Od kiedy | **1989 r.** — 37 lat, trzy pokolenia, firma rodzinna | katalog drukowany 2026-05 (str. firmowe) |
| Centrala | Tarnów, ul. Warsztatowa 5 | katalog drukowany 2026-05, stopka agria.pl |
| Magazyny własne | **Niedomice** (33-132), **Radgoszcz** | jw. |
| Branża | surowce wapniowe i mineralne, sprzedaż **hurtowa i detaliczna** | oferta handlowa AGRII |
| Marki | **Agrobielik** (wapno tlenkowe), **Bielik** (hydratyzowane) — **to marki Nordkalku, nie AGRII** | SERP 19.08: `agrobielik` → osadkowski.pl, nordkalk-wapno.pl, agrotrzcina.pl, agria.pl (poz. 4), allegro, ceneo, olx |
| Segmenty deklarowane w ofercie handlowej | rolnicy i sadownicy, gospodarstwa rybackie, oczyszczalnie, hurtownie | oferta handlowa AGRII |
| Segmenty dodane w katalogu marketingowym | budownictwo, drogownictwo, paszarstwo, cement, kruszywa | katalog 2026-05 |

**Rozjazd do rozstrzygnięcia:** oferta handlowa AGRII **nie wymienia** budownictwa, drogownictwa,
paszarstwa ani kruszyw — katalog marketingowy je dodaje. Wpływa na zakres treści i kafle na `/oferta/`.
Pytanie do Pawła, patrz §7.

**Czego AGRIA nie sprzedaje:** kruszyw łamanych i granitowych na podbudowy (~95% wolumenu klastra
drogowego). Decyzja Janka 15.06 — memory `project_agria_catalog_decisions`. Drogownictwo obsługiwane
**istniejącym** produktem: wapno palone mielone #320 do stabilizacji gruntów.

---

## 2. Ludzie i role

| Osoba | Rola | Jak się z nim pracuje | Źródło |
|---|---|---|---|
| **Paweł Bigos** | **syn właściciela.** Główny kontakt operacyjny, akceptuje zmiany na stronie, przysyła cenniki i materiały | **telefon Janka, nie mail.** Nie pisać draftów z frameworkami klasyfikacji (A/B/C/D) — agencyjna formalizacja jest nieadekwatna. Tel. **664 393 062** | memory `feedback_agria_pawel_relacja_telefoniczna`; numery z maila 01.07; rola — ustalenie Janka 22.08 |
| **Bogdan** | **prezes zarządu.** Nazwisko nieustalone | — | ustalenie Janka 22.08 |
| **Kazimierz Nowak** | **specjalista ds. nawozów.** Strona merytoryczna — dane do kalkulatora, treści ogłoszeń OLX | mail + telefon. Tel. **781 875 411** (Radgoszcz) | mail 18.08 (kalkulator, poprawki OLX); rola — ustalenie Janka 22.08 |
| **Kasjan** | decyzja o budżecie — to z nim Paweł konsultował akcept oferty | nie kontaktujemy się bezpośrednio | akcept oferty 27.05 |
| **P. Stanisław** | odszedł z działu sprzedaży; miał kontakt do starego operatora wizytówek Google | — | T-006, diagnoza GBP 01.07 |
| Joanna, Małgorzata | Biuro Sprzedaży — **rola niepotwierdzona**, poza działem handlowym | — | T-006 |

**Dział handlowy to trzy osoby: Bogdan, Paweł i Kazimierz** (ustalenie Janka 22.08.2026).
Ta trójka — i nikt poza nią — jest użytkownikiem ofertownika. Wcześniejszy zapis „Bogdan, Joanna,
Małgorzata — skład niepotwierdzony" figurował tu jako blokada od 65 dni; **jest zdjęta**.
Nie dopytujemy Pawła o skład — patrz T-006 w rejestrze, decyzja Janka 20.08.

**Numery na stronie:** Tarnów `604 428 782`, Niedomice `664 393 062` (Paweł), Radgoszcz `781 875 411` (Kazimierz).
Numer `660 768 691` **usunięty całkowicie** (osoba na L4) — mail Pawła 01.07.
W Google Ads rotują dwa numery: Paweł i Kazimierz.

---

## 3. Produkty — 19 kart WooCommerce

Producent z taksonomii `pa_agria-producent` (MCP, 19.08). Ceny netto **za towar, bez transportu**
(odbiór własny) z `CENNIK_PAWEL_2026-08-07.md` — mail Pawła 07.08 12:49.

| ID | SKU | Produkt | Producent | Luz 24 t | Big-bag | Opakowania |
|---|---|---|---|---|---|---|
| 310 | AGR-001 | Agrobielik 70 (tlenkowe) | **Nordkalk** | 220 | 400 | 20 kg 11,50/szt · 40 kg 19,00/szt |
| 311 | AGR-002 | Agrobielik 90 (tlenkowe) | **Nordkalk** | 750 (0–3 mm) · 850 (2–8 mm) | 850 · 940 | — |
| 312 | AGR-003 | Oxyfertil 90 (tlenkowe) | **Lhoist** | — | 790 | — |
| 313 | AGR-004 | Tlenkowe zawierające magnez | **Lhoist** | brak ceny | brak ceny | — |
| 308 | AGR-005 | Mieszanka tlenkowo-węglanowa | **Nordkalk** | 120 | — | — |
| 315 | AGR-006 | Węglanowe bez Mg — odm. 04 | Celiny (Hochel) + Lhoist | 57 | — | — |
| 316 | AGR-007 | Węglanowe bez Mg — odm. 05 | Kopalnia Celiny | brak ceny | — | — |
| 314 | AGR-008 | Węglanowe bez Mg granulowane | Celiny (Hochel) + Grankal + Lhoist | — | 350 | 25 kg → 380 zł/t |
| 318 | AGR-009 | Węglanowe z Mg — odm. 04 | Kopalnia Jażwica (Industria) | 50 | — | — |
| 319 | AGR-010 | Węglanowe z Mg — odm. 05 | Kopalnia Laskowa + Winna (Industria) | 36 | — | — |
| 317 | AGR-011 | Węglanowe z Mg granulowane | **Grankal** | — | 370 | 25 kg → 410 zł/t |
| 302 | AGR-012 | Dolomit | **Siarkopol** | **od 260** (0,1–0,4 i 0,4–0,8 mm) · **280** (1–3 mm) | ⚠️ forma niepodana | — |
| 305 | AGR-013 | Kreda nawozowa granulowana | KZK Kornica | — | 410 | 25 kg → 490 zł/t |
| 306 | AGR-014 | Kreda nawozowa sypka | Kopalnia Drugnia | 125 | — | — |
| 307 | AGR-015 | Kreda pastewna | Celiny (Hochel) + Lhoist | 190 | — | 30 kg → 610 zł/t |
| 304 | AGR-016 | Kreda malarska | **Lhoist** | — | — | 30 kg → 645 zł/t |
| 320 | AGR-017 | Wapno palone mielone wysokoreaktywne | **Nordkalk** | 950 | 1 200 | — |
| 309 | AGR-018 | Wapno hydratyzowane Bielik | **Nordkalk** | 945 | — | 25 kg → 1 220 zł/t |
| 303 | — | Kreda czarna jeziorna | **Grankal** | brak ceny | brak ceny | — |

**Pokrycie cenowe: 16 z 19** (od 24.08). Bez ceny zostają trzy: **303** Kreda czarna, **313** Tlenkowe z Mg,
**316** Węglanowe odm. 05.

**Dolomit — ceny otrzymane 2026-08-24** (przekazane przez Janka): **od 260 zł/t netto** dla frakcji
0,1–0,4 mm i 0,4–0,8 mm, **280 zł/t netto** dla frakcji 1–3 mm.
⚠️ **Do dopytania przed wpisaniem na kartę: której formy dostawy dotyczą te kwoty** (luz 24 t,
big-bag, worki). Reguła z 19.08 wymaga, żeby cena wiodąca **zawsze** niosła swój warunek dostawy —
samo „od 260 zł/t" czyta się tak, jakby dotyczyło worka. Bez tej informacji karty nie uzupełniamy.

⚠️ **Korekta wobec wcześniejszego zapisu „Dolomit boli najbardziej — 6 600 wyszukań/mies.".**
Wolumen jest prawdziwy (pomiar 24.08: 6 600/mies., szczyt III 9 900), ale **nie jest adresowalny kartą
produktu**. SERP na „dolomit" (DataForSEO, PL/pl, 24.08): Wikipedia #1 (minerał), dalej treść ogrodnicza
(target.com.pl, dlaroslin.pl), kruszywo Holcim, sklepy detaliczne z paczkami 10–25 kg, YouTube
i **suplement diety w tabletkach**. Intencja jest rozszczepiona. Adresowalna jest wąska część klastra:
`dolomit nawóz`, `wapno dolomitowe`. Karta #302 ma dodatkowo werdykt GSC **„Discovered — currently
not indexed"** i **zero wyświetleń w 90 dniach** — cena sama tego nie odblokuje.

**Anomalie cenowe do potwierdzenia** (mogą być poprawne — różne złoża i przemiał): węglanowe z Mg odm. 05
(36 zł/t) taniej niż odm. 04 z magnezem (50) i bez magnezu (57); kreda nawozowa sypka (125) ponad
dwukrotnie drożej od węglanowego bez magnezu (57), a chemicznie oba to węglan wapnia.

**Stan na stronie (zweryfikowany renderem per URL, 24.08): 15 z 19 kart ma na froncie kwotę
`zł/t netto`** — wdrożone 19.08 w ramach T-010/T-011. Bez kwoty zostają cztery: 302 Dolomit
(ceny są od 24.08, czekają na formę dostawy), 303 Kreda czarna, 313 Tlenkowe z Mg, 316 Węglanowe odm. 05.

**`_price` w WooCommerce jest puste w 19/19 i takie ma zostać** — tryb katalogu, ADR
`docs/decyzje/2026-08-19-dwie-warstwy-cen.md`. Store API zwraca `"price":"0"`, schema `Product`
emituje **zero `offers`** (zmierzone 24.08 na wszystkich 19 kartach — pozycja T-097 w rejestrze).
Patrz `REJESTR_ZOBOWIAZAN.md` → T-010, T-097.

---

## 4. Producenci i relacja

**W bazie jest dziesięciu producentów, nie dwóch.** Wcześniejszy `MASTER_PROMPT.md` (usunięty 19.08.2026)
wymieniał „Nordkalk (Sitkówka) i Trzuskawica" i był czytany pierwszy w każdej sesji — **Trzuskawicy nie ma
w danych produktowych ani razu**, a Lhoist, którego tamten plik nie wymieniał, ma najwięcej pozycji.
Ta tabela jest jedynym źródłem.

| Producent | Ile produktów | Uwaga |
|---|---|---|
| **Lhoist** | 6 | najliczniejszy, nieobecny w usuniętym MASTER_PROMPT |
| **Nordkalk** | 5 | marki Agrobielik i Bielik, zakład Sitkówka; karty produktowe CL 90-S / CL 90-Q |
| **Grankal** | 3 | |
| Celiny (Hochel Group) | 3 | osobno istnieje term „Kopalnia Celiny” (1) — duplikat do sprzątnięcia |
| Siarkopol, KZK Kornica, Kopalnia Drugnia, Jażwica (Industria), Laskowa, Winna (Industria) | po 1 | |
| **Trzuskawica** | **0** | wymieniana w usuniętym MASTER_PROMPT, brak w danych. Karty dostawcy na `/do-pobrania/` są Trzuskawica/Kujawy — to materiały, nie przypisanie produktu |

**AGRIA jest dostawcą, nie producentem surowca.** Agrobielik i Bielik to produkty Nordkalku sprzedawane
przez wielu dystrybutorów — AGRIA jest jednym z nich (SERP 19.08).

**Dług danych:** taksonomia producentów ma duplikaty termów — „Kopalnia Jażwica” vs „Kopalnia Jażwica (Industria)”,
„Kopalnia Winna” vs „Kopalnia Winna (Industria)”, „Kopalnia Celiny” vs „Celiny (Hochel Group)”. Analogicznie
lokalizacje: „Chęciny (26-060)” vs „26-060 Chęciny (26-060)”, „Góraźdzce” vs „Gorażdże”, „Częstochowa” ×2.
To jest robota z etapu zerowego ofertownika (T-045), nie osobne zadanie.

**Parametry produktowe bierzemy wyłącznie z kart producentów** (Nordkalk, Lhoist…) i rozporządzeń,
nigdy z rozumowania — memory `feedback_agria_params_from_datasheets`. 17 kart jest publicznie
na `/do-pobrania/`; klient ściąga ten sam PDF, co my.

---

## 5. Logistyka i transport

| Fakt | Wartość | Źródło |
|---|---|---|
| Flota własna | 3 t / 5 t / 12 t / 24 t + kurier | katalog, oferta handlowa |
| Zakłady wysyłkowe | 14 lokalizacji w taksonomii `pa_agria-lokalizacja`; najwięcej produktów: **Niedomice (10)**, **Sitkówka (5)**, Bukowa (4) | MCP 19.08 |
| Naczepa | 5,50 zł/km, w jedną stronę, 24 t — worki i big-bagi | spec ofertownika 18.08 |
| Beczka silosowa | 4,80 zł/km, **liczone w dwie strony**, 24 t — luz sypki i kruszony | jw. |
| Wanna | 4,20 zł/km, **liczone w dwie strony**, 24 t — luz sypki | jw. |
| Kurier paletowy | **120 zł za paletę**, stawka krajowa niezależna od masy | ustalenie 18.08 |
| Paleta | jednostka miejsca, nie masy — dwa worki 25 kg albo jeden 40 kg zajmują całą paletę, tak samo big-bag 1000 kg | jw. |
| Terminy | dostawa 2–5 dni, pilne 24–48 h; płatności B2B 14/30/60 dni | katalog |
| Rozładunek | HDS / wywrotka | katalog |

**Konsekwencja, o której łatwo zapomnieć:** ten sam adres dostawy ma inny koszt zależnie od zakładu,
z którego towar wyjeżdża (Radom to 90 km z Sitkówki albo 250 km z Niedomic). Dlatego transport
nie liczy się strefami WooCommerce.

---

## 6. Ustalenia handlowe

| Ustalenie | Treść | Data / źródło |
|---|---|---|
| Umowa | **6 × 2 000 zł netto/mies**, opieka SEO/content/on-page | akcept Pawła (po konsultacji z Kasjanem) **27.05.2026** |
| Forma | **bez umowy pisemnej** — akcept mailowy. Nie proponować umów ani klauzul | decyzja Janka 27.05, memory `feedback_agria_no_written_contract_trust_based` |
| Komunikacja budżetu | **tylko miesięcznie** (2 000/mies). **Nigdy suma całkowita** — 12 000 to zakaz | memory `feedback_agria_offer_mail_structure` |
| Google Ads | osobna pozycja, media **1 200 zł/mies**, kampanie żywe od 13.08, plan na 3 miesiące | ADR 13.08 |
| OLX | osobna pozycja: **1 800 zł netto setup + 300 zł/mies**; pakiet Premium 200 (1 199,99 brutto) **kupuje AGRIA** | wycena 07.08, mail 11.08 |
| Kalkulator Mg | **≈4 h** do rozliczenia | ustalenie 18.08, rejestr T-043/T-044 |
| Ofertownik | **projekt własny Auranet**, nie billable na tym etapie — najpierw budujemy, potem sprzedajemy | decyzja Janka 18.08 |
| Poza zakresem ryczałtu | social media, sesje zdjęciowe, Google Ads | `AURANET_2000PLN_MONTHLY.md` |

**Rozjazd do rozstrzygnięcia:** memory `project_agria_ads_sezonowosc` sygnalizuje różnicę **trzy vs cztery
miesiące** kampanii Ads między tym, co potwierdził Kasjan, a tym, co poszło w mailu. Do sprawdzenia
przed rozliczeniem budżetu.

---

## 7. Ustalenia komunikacyjne — co wolno, czego nie

- **DWIE NIEZALEŻNE WARSTWY CEN — nigdy ich nie mieszaj** (decyzja Janka 19.08,
  ADR `docs/decyzje/2026-08-19-dwie-warstwy-cen.md`):
  **(A) treść SEO** — cena wyłącznie w `<h2>` i akapicie, po to, żeby rankować na frazy cenowe.
  `_price` w WooCommerce zostaje **puste**, wariantów ani atrybutów cenowych nie tworzymy,
  a schema `Product`/`offers` budujemy **ręcznie z treści**, nie z bazy.
  **(B) ofertownik** — ceny w wariantach WooCommerce i w cenniku wtyczki, różnicowane per zakład,
  obłożone transportem. **Nigdzie nie ujawniane, dane wewnętrzne.** Ofertownik jest projektem
  własnym Auranet, więc tym bardziej nie jest to materiał do publikacji.
  To nie są te same kwoty w tym samym miejscu i nigdy nie były.
- **Ceny na stronie: JEDNA kwota „od X zł/t netto” na kartę** — najtańsza dostępna forma hurtowa,
  **zawsze ze swoim warunkiem** („od 220 zł/t netto przy dostawie całosamochodowej 24 t”).
  Pozostałe formy wymieniamy **bez kwot**: „dostępny także w big-bagach od 1 tony oraz w workach
  20 kg i 40 kg, w sprzedaży hurtowej”. **Decyzja Janka 19.08** — zastępuje regułę „dwa punkty
  odniesienia” z 06.08.
  **Powód:** druga kwota podnosiła próg wejścia zamiast go obniżać. Zmierzone na 15 kartach:
  Agrobielik 70 dawał skok 220 → 400 zł/t (**+82 %**), kreda pastewna 190 → 610 (**+221 %**).
  Słowo „od” niesie całą informację o widełkach, a pytanie o cenę big-bagu trafia tam, gdzie ma
  trafiać — do handlowca. Warunek przy cenie wiodącej jest obowiązkowy: samo „od 220 zł/t”
  czyta się tak, jakby dotyczyło worka.
- **Nigdy pełny cennik** i nigdy cena za sztukę — wyłącznie przeliczenia na tonę.
- **Ceny za worki — decyzja otwarta.** Paweł podał ceny workowe i w tym samym mailu napisał:
  *„na ten moment nie będziemy prowadzić sprzedaży po worku”*. Cała zgoda na publikację cen opierała się
  na tym, że cena tonowa odsiewa detalistę, a „11,50 zł za worek” robi odwrotnie. **Rekomendacja: publikować
  wyłącznie przeliczenia na tonę.** Bez decyzji Janka nie ruszamy części workowej T-010.
- **Zero żargonu.** Odbiorcą jest rolnik, nie spedytor. Zamiast „loco magazyn" → **„cena za towar, bez transportu"**.
  Dotyczy też MOQ, franco, EXW, HDS. Memory `feedback_agria_bez_zargonu_loco`.
- **Bez progu ilościowego.** Paweł zdjął formy dostawy z kart, bo „zapis nas ogranicza" (T-002).
  Nie piszemy „minimum 24 t", tylko „przy 24 t cena wynosi od X".
- **Klauzula prawna zostaje:** „ceny orientacyjne, netto, nie stanowią oferty handlowej w rozumieniu
  Kodeksu cywilnego". Dopisek „mniejsze ilości — wycena indywidualna" Paweł kazał usunąć (ceny obejmują już 0,5–1 t).
- **Nie krytykujemy stanu strony w komunikacji do klienta** — Auranet ją zbudował, więc to krytyka własnej
  roboty. Framing rozwojowy: „uruchamiamy / wzmacniamy / optymalizujemy". Memory `feedback_agria_no_self_criticism_built_site`.
- **W komunikacji przemilczeć multi-location GBP**, dopóki nie mamy dostępu do profili oddziałów.
- **Nic nie idzie do klienta bezpośrednio.** Wszystko przez Janka na `js@auranet.com.pl`.

---

## 8. Czego nie wiemy — pytania do Pawła

Kolejność wg tego, co blokują. Pozycje rejestru w nawiasach.

1. **Czy AGRIA jest autoryzowanym dystrybutorem Nordkalku?** *(blokuje T-040)*
   Licytować na cudzy znak towarowy wolno w Google Ads zawsze; **użyć nazwy „Nordkalk" w treści reklamy
   wolno tylko odsprzedawcy.** Sprawdzone 19.08: odpowiedzi nie ma nigdzie w repo ani w memory. Nie zgadywać.
2. ~~**Aktualny skład działu sprzedaży**~~ — **pytanie wypada z listy.** Dwiema decyzjami:
   T-006 zdjęte z kolejki 20.08 („nie dopytywać Pawła o skład działu"), a 22.08 Janek podał skład
   działu handlowego — Bogdan, Paweł, Kazimierz (§2). Role Joanny i Małgorzaty pozostają nieznane,
   ale nic od nich nie zależy.
3. **Czy budownictwo i drogownictwo to realne segmenty sprzedaży?** *(wpływa na zakres treści i `/oferta/`)*
4. **Ceny dla trzech brakujących kart** — Kreda czarna (303), Tlenkowe z Mg (313), Węglanowe odm. 05 (316).
   ~~Dolomit (302)~~ — **ceny przyszły 24.08** (§3). *(rozszerza T-010)*
4a. **Której formy dostawy dotyczą ceny Dolomitu** (od 260 zł/t dla 0,1–0,4 i 0,4–0,8 mm, 280 zł/t dla 1–3 mm) —
   luz 24 t, big-bag czy worki? **Bez tej odpowiedzi kwota nie wchodzi na kartę**, bo cena wiodąca musi
   nieść swój warunek dostawy. *(blokuje uzupełnienie T-010 o kartę #302)*
5. **Potwierdzenie anomalii cenowych** — odm. 05 taniej niż odm. 04; kreda sypka drożej niż węglanowe.
6. **Zgoda na przywrócenie form dostawy jako atutu**, nie jako MOQ.
7. **Errata do katalogu drukowanego:** pH >16 przy wapnie palonym (skala kończy się na 14),
   kreda pastewna opisana parametrami wapna tlenkowego (reakcja egzotermiczna, pH >12 — węglan tego nie robi),
   „35 lat na rynku" zamiast 37.
8. **Literówka w ofercie handlowej:** „Wapno hydratyzowane Bielik, worki 25 kg — 1245/SZT" — niemal
   na pewno 12,45.
9. **Czy AGRIA ma konto na OLX** i czy Agrobielik wystawiany tam przez pośredników im przeszkadza.

**Uwaga o formie:** to są pytania na telefon Janka, nie na maila z tabelą. Paweł pracuje telefonicznie —
memory `feedback_agria_pawel_relacja_telefoniczna`.
