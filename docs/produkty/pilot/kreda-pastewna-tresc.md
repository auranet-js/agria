# Treść — #307 Kreda pastewna (T-136, v2 14.09; v1 zaakceptowane `[J 11.09]`)

> 11.09.2026 (v1) · **14.09.2026 (v2 — wzór #312/#315)** · research: [`kreda-pastewna-research.md`](kreda-pastewna-research.md) · baza: [`../kreda-pastewna.md`](../kreda-pastewna.md)
> Źródła treści: **[K]** karta AGRII PDF (`/wp-content/uploads/2026/06/agria-karta-produktu-kreda-pastewna.pdf`) · **[LB]** karta Lhoist Bukowa „Kreda Pastewna 0-0,3mm" (IV 2026) ·
> **[CEL]** karta Kopalni Wapienia „Celiny" F13 (29.04.2026) · **[FOT]** worek 30 kg · **[C]** `CENNIK_PAWEL_2026-08-07.md` · **[F]** `FAKTY_KLIENTA.md` §5 ·
> **[KN]** Kazimierz Nowak, WhatsApp 09.09 i 11.09 (przekazane przez Janka 14.09). Nic spoza tych źródeł.
> Nazwa WC, adres, kategoria, `_price` — bez zmian. Warstwa renderu: **`post_content`** (ustalone 11.09, research §0) + `post_excerpt` jako lead.
>
> **Decyzje Janka 11.09 (quiz):** wiersze „Odczyn pH >12" i „Typ reakcji: Egzotermiczna" z karty PDF **nie wchodzą** do tabeli `[J 11.09]` ·
> gatunki: nioski i bydło mleczne w H2, lead i FAQ, jedna dawka z karty `[J 11.09]`.
> **Decyzje 14.09:** zawartość wapnia jako **„Ca min. 37%"** w leadzie, FAQ i tabeli `[J 14.09]` — karta PDF ma „min. 37% CaO", Kazimierz 11.09:
> „zapis zawartości wapnia w kredzie 37%CaO zamiast 37%Ca" to błąd karty; „Ca min. 37%" podają [LB], [FOT], a [CEL] „Ca min. 389 g/kg" ·
> dawki per gatunek — **odpowiedź klienta [KN] 09.09: nie ma ich**, dawka zależy od zbóż w mieszance i wapnia w pozostałych składnikach paszy; karta podaje dawkę ogólną.

## 1. Frazy przypisane i hipoteza

**Frazy karty** (wszystkie paszowe — w serwisie nie ma drugiego produktu paszowego): `kreda pastewna` 2 400 · `kreda pastewna dla kur` 1 600 ·
`kreda dla kur` 720 · `wapno dla kur niosek` 210 · `kreda pastewna dla bydła` 210 · `kreda pastewna dla kur niosek` 110 · `kreda paszowa` 90 ·
`…dla kur dawkowanie` 90 · `kreda dla bydła` 70 · `…dla bydła dawkowanie` 70 · `ile kredy pastewnej dla kur` 50 · `kreda pastewna cena` 40 ·
`kreda pastewna dawkowanie` 30 · `gruboziarnista` 30 · `drobnoziarnista` 30 · `co to jest kreda pastewna` 20 · `cena za tonę` 20 · `ile kosztuje` 20 · `30 kg`, `luzem` <10.
Kolizje: kategoria `/paszarstwo/` (listuje tylko #307) i stary `/kreda-pastewna/` z 301 na kategorię — poza zakresem karty.

**Hipoteza:** po zmianie #307 zacznie zbierać wyświetlenia na frazach drobiowych — dziś 0 wierszy w GSC na `kreda pastewna dla kur` i `kreda dla kur` —
co najmniej 100 wyświetleń w 28 dniach, i wyprzedzi `/paszarstwo/` na frazach o bydle (dziś kategoria 20 wyśw., karta 7), bo gatunki, dawka, frakcje
i producenci trafiają do title, nagłówków i FAQ, a `FAQPage` odpowiada na PAA. Reklamy stoją (D2), więc wynik jest czysto organiczny. **Kontrola: dzień wdrożenia v2 + 28 dni.**

## 1a. Mapa: fraza → miejsce na karcie

| fraza (wyszukań/mies.) | gdzie pracuje |
|---|---|
| `kreda pastewna` 2 400 · `co to jest kreda pastewna` 20 · PAA „Jaki jest skład kredy pastewnej?" | title, H1 (nazwa WC), lead, FAQ „Co to jest kreda pastewna i jaki ma skład?" |
| `kreda pastewna dla kur` 1 600 · `kreda dla kur` 720 · `wapno dla kur niosek` 210 · `…dla kur niosek` 110 · PAA „Czy kury powinny jeść kredę?" | title, H2 „Kreda pastewna dla kur niosek i bydła mlecznego", lead, meta, FAQ „Co daje kreda pastewna kurom nioskom i bydłu?" |
| `kreda pastewna dla bydła` 210 · `kreda dla bydła` 70 · PAA „Co daje kreda pastewna dla bydła?" | title, ten sam H2, ten sam FAQ |
| `…dawkowanie` 30 · `…dla kur dawkowanie` 90 · `…dla bydła dawkowanie` 70 · `ile kredy pastewnej dla kur` 50 (GSC poz. 6,6) · PAA „Ile kredy pastewnej dla kur na 100 kg?", „Jaka dawka kredy pastewnej dla bydła?" | H2 „Kreda pastewna — dawkowanie: ile na 100 kg paszy", FAQ „Ile kredy pastewnej na 100 kg paszy dla kur i bydła?", meta |
| PAA „Jak podawać kredę pastewną?" · „Jak stosować kredę pastewną dla kur?" | FAQ „Jak podawać kredę pastewną?" |
| `gruboziarnista` 30 · `drobnoziarnista` 30 | H2 „Kreda pastewna drobnoziarnista i gruboziarnista — dwie kopalnie, cztery frakcje", tabela frakcji, FAQ „…drobnoziarnista czy gruboziarnista?" |
| `kreda paszowa` 90 · PAA „Czy kreda pastewna to to samo co wapno?" · „Co jest lepsze wapno czy kreda?" | FAQ „Czy kreda pastewna to to samo co wapno?" |
| producent i dokumenty (na bydło nr 1 w SERP: big-bag z nazwą kopalni) | sekcja kopalń (numery weterynaryjne), FAQ „Kto produkuje…" |
| `kreda pastewna cena` 40 · `cena za tonę` 20 · `ile kosztuje` 20 · `30 kg`, `luzem` <10 | H2 „Kreda pastewna — cena za tonę, worek 30 kg i luz", FAQ „Ile kosztuje tona…", lead, meta |

**Schemat:** `Product` (nazwa produktu) + `offers` (bez zmian) + **`FAQPage` z 8 pytań**.

## 2. Meta

| pole | dziś | nowe |
|---|---|---|
| title (57 zn.) | Kreda pastewna dla kur niosek i bydła, worek 30 kg \| AGRIA | *bez zmian* |
| meta description (152 zn.) | Kreda pastewna — materiał paszowy, źródło wapnia dla niosek i bydła mlecznego. Frakcje od 0–0,3 do 1–3 mm, dawka 1–2 kg/100 kg paszy. Worek 30 kg i luz. | **Kreda pastewna Ca min. 37% dla kur niosek i bydła mlecznego. Frakcje 0–0,3 do 1–3 mm, dawka 1–2 kg na 100 kg paszy. Worek 30 kg, luz od 190 zł/t.** |
| focus keyword | kreda pastewna | *bez zmian* |

## 3. Lead (`post_excerpt`)

> Kreda pastewna to materiał paszowy — naturalny węglan wapnia do mieszanek paszowych, premiksów i mieszanek mineralnych. Zawiera min. 37% wapnia (Ca).
> Wapń buduje kości, zęby i skorupy jaj, dlatego kreda jest ważna w żywieniu kur niosek i bydła mlecznego. Ma cztery frakcje — od drobnoziarnistej
> 0–0,3 mm po gruboziarnistą 1–3 mm — i dawkowanie 1–2 kg na 100 kg paszy. Dostarczamy ją z dwóch kopalni — Lhoist Bukowa i Kopalni Wapienia „Celiny" —
> w workach 30 kg i luzem.
>
> **Cena: od 190 zł/t netto przy dostawie całosamochodowej 24 t — za towar, bez transportu. Dostępna także w workach 30 kg.**

## 4. Treść (`post_content`)

### H2 Kreda pastewna dla kur niosek i bydła mlecznego

Kreda pastewna uzupełnia wapń w dietach zwierzęcych. Wapń jest budulcem kośćca, zębów i skorup jajowych — dlatego ma kluczowe znaczenie
w żywieniu **kur niosek** i **bydła mlecznego**. Kreda działa też jako bufor kwasicy żołądkowej: neutralizuje nadmiar kwasów, wspomaga trawienie
i stabilizuje przewód pokarmowy przy wysokoenergetycznych dawkach.

### H2 Kreda pastewna — dawkowanie: ile na 100 kg paszy

Karta produktu podaje **1–2 kg kredy na 100 kg paszy**. To dawka ogólna, bez podziału na gatunki: ile kredy dodać do konkretnej mieszanki,
zależy od zbóż w recepturze i od tego, ile wapnia wnoszą pozostałe składniki paszy.

Kredę podaje się jako składnik paszy — w mieszankach paszowych, premiksach i mieszankach mineralnych. Frakcję dobiera się do miksera
i grupy zwierząt (niżej).

### H2 Kreda pastewna drobnoziarnista i gruboziarnista — dwie kopalnie, cztery frakcje

Kreda pastewna jest dostępna równolegle z dwóch kopalni — z magazynów w Bukowej i w Celinach. Podwójne źródło dostaw jest ważne dla
wytwórni pasz i hodowli wielkotowarowych, które nie mogą pozwolić sobie na przerwę w produkcji mieszanek. Frakcję — od pyliście drobnej
po 1–3 mm — dobiera się do miksera i grupy zwierząt.

| frakcja | producent | magazyn |
|---|---|---|
| 0–0,3 mm (drobnoziarnista) | Lhoist Bukowa | Bukowa |
| 0,1–0,4 mm | Kopalnia Wapienia „Celiny" | Celiny |
| 0,4–0,8 mm | Kopalnia Wapienia „Celiny" | Celiny |
| 1–3 mm (gruboziarnista) | Kopalnia Wapienia „Celiny" | Celiny |

Worek 30 kg to kreda z Lhoist Bukowa. Oba zakłady mają zakładowe numery weterynaryjne: **Lhoist Bukowa — PL2613013p**,
**Kopalnia Wapienia „Celiny" — PL26043170p** (z certyfikatem GMP+). Odbiorcy dostają pełną dokumentację zgodności z normami paszowymi.

### H2 Kreda pastewna — specyfikacja techniczna

Tabela 1:1 z karty PDF **bez wierszy „Odczyn pH >12" i „Typ reakcji: Egzotermiczna"** `[J 11.09]`, zawartość wapnia jako „Ca min. 37%" `[J 14.09]`. Wiersz „Forma dostawy" wraca `[J 11.09]`.

| Parametr | Wartość |
|---|---|
| Zawartość wapnia | Ca min. 37% |
| Forma fizyczna | Sypkie |
| Frakcja | 0–0,3 / 0,1–0,4 / 0,4–0,8 / 1–3 mm |
| Kategoria paszowa | Suplement mineralny |
| Zastosowanie | Uzupełnienie Ca w dietach zwierzęcych |
| Funkcja biologiczna | Bufor kwasicy, źródło wapnia dla kości |
| Efekt zastosowania | Neutralizacja kwasów, wsparcie trawienia |
| Dawkowanie | 1–2 kg / 100 kg paszy |
| Segment | Paszarstwo, hurtownie, rolnictwo |
| **Forma dostawy** | **Luz (24 t), worek 30 kg** |
| Magazyn | Bukowa (29-105), Celiny (26-020) |
| Producent | Celiny (Hochel Group), Lhoist |
| Dostępność | Cały rok |

Pod tabelą: **[Pobierz kartę produktu Kreda pastewna (PDF)](/wp-content/uploads/2026/06/agria-karta-produktu-kreda-pastewna.pdf)**

### H2 Kreda pastewna — cena za tonę, worek 30 kg i luz

**Kreda pastewna** kosztuje **od 190 zł/t netto** przy dostawie całosamochodowej 24 t. Produkt jest dostępny także w workach 30 kg, w sprzedaży hurtowej.

Podane kwoty dotyczą samego towaru, bez transportu. Ceny orientacyjne, netto, nie stanowią oferty handlowej w rozumieniu Kodeksu cywilnego.

Dowozimy własnym transportem, samochodami od 3 do 24 t, z magazynu w Bukowej albo w Celinach. Koszt dostawy pod Twój adres podamy w wycenie.

### H2 Najczęściej zadawane pytania

**H3 Co to jest kreda pastewna i jaki ma skład?**
To materiał paszowy — naturalny węglan wapnia, dodawany do mieszanek paszowych, premiksów i mieszanek mineralnych jako źródło wapnia.
Kreda AGRII zawiera min. 37% wapnia (Ca) i jest sypka, w czterech frakcjach od 0–0,3 do 1–3 mm.

**H3 Co daje kreda pastewna kurom nioskom i bydłu?**
Wapń — budulec kośćca, zębów i skorup jajowych, dlatego kreda jest ważna w żywieniu kur niosek i bydła mlecznego. Działa też jako bufor
kwasicy: neutralizuje nadmiar kwasów i wspiera trawienie.

**H3 Ile kredy pastewnej na 100 kg paszy dla kur i bydła?**
Karta produktu podaje 1–2 kg kredy na 100 kg paszy, bez podziału na gatunki. Ile dokładnie dodać, zależy od zbóż w recepturze i od wapnia
w pozostałych składnikach paszy — udział kredy dobiera się do konkretnej mieszanki.

**H3 Jak podawać kredę pastewną?**
Jako składnik paszy — w mieszankach paszowych, premiksach i mieszankach mineralnych, w dawce 1–2 kg na 100 kg paszy. Frakcję dobiera się
do miksera i grupy zwierząt.

**H3 Kreda pastewna drobnoziarnista czy gruboziarnista — którą wybrać?**
Frakcję dobiera się do miksera i grupy zwierząt. Drobnoziarnista 0–0,3 mm pochodzi z Lhoist Bukowa, frakcje 0,1–0,4 i 0,4–0,8 mm oraz gruboziarnista
1–3 mm — z Kopalni Wapienia „Celiny". Powiedz handlowcowi, dla jakiego stada i do jakiej paszy potrzebujesz kredy, a wskażemy frakcję i magazyn.

**H3 Czy kreda pastewna to to samo co wapno?**
Nie. Kreda pastewna, nazywana też paszową, jest materiałem paszowym — w katalogu materiałów paszowych figuruje jako węglan wapnia, a zakłady,
które ją produkują, mają numery weterynaryjne. Wapno nawozowe i kreda nawozowa to nawozy do odkwaszania gleby — w ofercie AGRII to osobne produkty.

**H3 Kto produkuje kredę pastewną i jakie są dokumenty?**
Kredę pastewną AGRII produkują Lhoist Bukowa (nr weterynaryjny PL2613013p) i Kopalnia Wapienia „Celiny" (nr weterynaryjny PL26043170p,
certyfikat GMP+). Karta produktu jest do pobrania pod specyfikacją; odbiorcy dostają pełną dokumentację zgodności z normami paszowymi.

**H3 Ile kosztuje tona kredy pastewnej i czy jest w workach 30 kg?**
Od 190 zł/t netto luzem, przy dostawie całosamochodowej 24 t — to cena za towar, bez transportu. Kredę kupisz też w workach 30 kg.
Dowozimy własnym transportem; napisz, ile potrzebujesz i dokąd, a koszt dostawy podamy w wycenie.

### H2 Zapytaj o ofertę, zamów próbkę — *bez zmian*
Skontaktuj się z naszym zespołem handlowym, aby uzyskać indywidualną wycenę, zamówić próbkę produktu lub omówić warunki dostawy.
Agria — 37 lat doświadczenia na rynku nawozów wapniowych.

## 5. Schemat

- `FAQPage` — 8 pytań z sekcji FAQ, 1:1 (mechanizm jak w pliku #312 §5; ID 307 dopisane do `AGRIA_KARTY_SCHEMA_V2`).
- `Product` / `offers` — bez zmian (190 PLN, `TNE`); nazwa w schemacie = nazwa WC.

## 6. Decyzje przy akcepcie

1. ~~Wiersz „Forma dostawy"~~ — **rozstrzygnięte `[J 11.09]`: wraca 1:1 z karty PDF**, bez SKU, MOQ i słowa „minimum" (Paweł ograniczał minimum, nie formy dostawy).
2. ~~Cena worka 30 kg~~ — **rozstrzygnięte `[J 11.09]`: podajemy cenę luzu (190 zł/t), worek 30 kg jako możliwość zakupu, bez kwoty** (reguła 19.08 zostaje).
3. **„Materiał paszowy" w prozie a „Suplement mineralny" w tabeli.** Tabela zostaje 1:1 z karty PDF. W prozie używam określenia producentów, które jest też na worku.
4. **T-135** (zdjęcie worka 30 kg jako główne) pasuje do tej treści — decyzja poza plikiem treści. Wątpliwość z numerem wyjaśniona 14.09:
   `PL21K274` to numer referencyjny karty Lhoist Bukowa (nagłówek „Nr ref. PL21K274, Kwiecień 2026"), nie numer weterynaryjny.
5. ~~„37% CaO"~~ — **rozstrzygnięte `[J 14.09]`: „Ca min. 37%"** (błąd karty PDF potwierdzony przez klienta 11.09). ⚠️ Karta PDF na `/do-pobrania/`
   dalej ma „min. 37% CaO" — do wymiany, gdy Kazimierz z Pawłem przyślą poprawioną kartę (zapowiedź [KN] 11.09).
6. ~~Dawki i frakcje per gatunek~~ — **odpowiedź klienta [KN] 09.09**: dawka zależy od mieszanki zbóż i zawartości wapnia w składnikach paszy,
   karta podaje ją ogólnie; frakcji do gatunków nie przypisujemy.

## 7. Pytanie do klienta — zamknięte 14.09

Pytanie z 11.09 (frakcje i dawki per gatunek) — odpowiedź w §6 pkt 6. Nowe pytania nie wychodzą; poprawioną kartę PDF klient przyśle sam.

## 8. Co znika w stosunku do dzisiejszej karty (v1)

„min. 37% CaO" (lead, FAQ, tabela, meta) → „Ca min. 37%" · FAQ „Ile kredy pastewnej dodać…" z odesłaniem do handlowca po dawkę → dawka ogólna z wyjaśnieniem, od czego zależy ·
dochodzą: H2 o dawkowaniu, H2 z frazami drobno- i gruboziarnista, FAQ o składzie, o tym, co daje kurom i bydłu, i o podawaniu; cena w meta.
Względem karty sprzed 11.09 — lista w historii pliku (v1): „atest do każdej partii", „pH powyżej 12", „35-letnie doświadczenie" i reszta twierdzeń DescWritera.
