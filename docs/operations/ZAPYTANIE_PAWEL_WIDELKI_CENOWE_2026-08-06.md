# Zapytanie do Pawła — widełki cenowe za tonę

> Data: 2026-08-06. Podstawa: `docs/seo/ANALIZA_CENY_NA_STRONIE_2026-08-06.md`.
> **Adresat: Janek.** Materiał do rozmowy telefonicznej z Pawłem + tabela do przekazania po rozmowie.
> Zakres pytania zawężony decyzją Janka (06.08): **wyłącznie widełki tonowe**, bez cen za opakowania detaliczne.

---

## 1. Rekomendacja — chcemy

**Tak.** Klaster cenowy to ~1 320 wyszukiwań miesięcznie przy zerowej obecności AGRII, a SERP dla tych fraz składa się wyłącznie ze stron podających cenę. Bez widełek nie da się tam wejść żadną treścią.

Ryzyko odwrotne — że cena ściągnie detalistów — **nie występuje przy cenie za tonę**. Cena tonowa odsiewa hobbystę skuteczniej niż jej brak: „od 210 zł/t przy dostawie całopojazdowej" zniechęca szukającego worka 25 kg, podczas gdy brak ceny go nie odstrasza, tylko kieruje do telefonu, który ktoś w AGRII musi odebrać.

---

## 2. Jak to ugryźć w rozmowie

Paweł może nie chcieć podać cen — to naturalna ostrożność, nie upór. Trzy rzeczy, które zdejmują opór, w tej kolejności:

**1. Zacząć od faktu, nie od prośby.** Ceny wapna AGRII **już są w internecie** — wystawiają je pośrednicy pod marką Agrobielik:

| Ogłoszenie na OLX | Cena | Lokalizacja |
|---|---|---|
| Wapno tlenkowe palone AGROBIELIK 70 | 210 zł | Kielce |
| Wapno tlenkowe AGROBIELIK 60 odm. 03 | 249 zł/t luz · 319 zł/t big-bag | Barcin |

To nie jest pytanie, czy cena Agrobielika ma być publiczna. Ona jest publiczna. Pytanie brzmi, czy klient znajduje ją u AGRII, czy u pośrednika.

**2. Nazwać, co to konkretnie kosztuje.** Samo „wapno granulowane olx" i „wapno nawozowe olx" to **360 wyszukiwań miesięcznie** — ludzie celowo szukają wapna na OLX, bo tam cena jest od ręki. Do tego 480 na „wapno granulowane cena". Ten ruch dziś w całości omija agria.pl.

**3. Powiedzieć wprost, że to widełki „od", nie cennik.** Trzy zdania, które warto powiedzieć dosłownie:

> - Podajemy **„od X zł/t netto"** — punkt wejścia, nie cena ostateczna.
> - Przy każdej pozycji piszemy, że **cena zależy od tonażu, odległości i formy dostawy** — negocjacje zostają po stronie handlowca.
> - **Żadnych cen za worki.** Cena za tonę to filtr — odsiewa działkowca, zostawia gospodarstwo.

**4. Zostawić furtkę.** W tabeli jest kolumna „nie podawać". Paweł może wyłączyć dowolną pozycję bez tłumaczenia się — łatwiej wtedy wypełnić resztę. Nawet 5–6 wypełnionych wierszy wystarczy do startu.

---

## 2a. Format ceny — doprecyzowanie Janka (06.08), obowiązujące

**Cena nigdy nie występuje sama — zawsze z przypiętym warunkiem dostawy. Dwa punkty odniesienia na grupę:**

```
Wapno węglanowe granulowane
Luz, dostawa całopojazdowa (24 t) — od X zł/t netto
Big-bag, od 1 tony                — od Y zł/t netto
Mniejsze ilości                   — wycena indywidualna

Ceny orientacyjne, netto, loco magazyn. Nie stanowią oferty handlowej
w rozumieniu Kodeksu cywilnego — warunki ustalamy indywidualnie.
```

**Dlaczego dwie kwoty, nie jedna.** Samo „od 210 zł/t" bez warunku jest nieinformacyjne: jeśli to cena przy pełnym pojeździe, a typowe zamówienie to 5–10 t, każdy pytający dostanie wyższą i pierwsza rozmowa startuje od rozczarowania. Drugi wiersz to zdejmuje, a przy okazji **sam pracuje handlowo** — klient widzi, ile zyskuje na pełnym pojeździe, zanim ktokolwiek z nim porozmawia.

**To rozwiązuje konflikt z STR-02.** Paweł zdjął formy dostawy z 19 kart, bo „taki zapis nas ogranicza" — obawa dotyczyła deklaracji minimum zamówienia. Tutaj minimum nie ma: nie piszemy „minimum 24 t", tylko „przy 24 t cena wynosi od X". **Cena przejmuje rolę filtra, którą wcześniej pełnił zapis o MOQ — działa tak samo, a niczego nie zamyka.** Drobny klient nadal może zadzwonić i kupić. W mailu trzeba to powiedzieć wprost, żeby Paweł nie odbił się odruchowo.

**Fallback:** jeśli poda tylko jedną kwotę na grupę — publikujemy sam wiersz całopojazdowy plus „mniejsze ilości: wycena indywidualna". Działa, tylko słabiej filtruje.

**Zabezpieczenia obiecane Pawłowi — do dotrzymania przy wdrożeniu:** adnotacja o braku charakteru oferty handlowej z zaproszeniem do kontaktu oraz edycja ceny w kilka minut (pole w Elementorze + cena „od" w WooCommerce, bez przebudowy strony).

---

## 3. Tabela do wypełnienia

Formy dostawy uzupełnione z kart produktowych AGRII — do wpisania zostają **wyłącznie liczby**.

### Wapno tlenkowe (palone)

| Produkt | CaO | Formy tonażowe | **od zł/t — luz 24 t** | **od zł/t — big-bag od 1 t** | nie podawać |
|---|---|---|---|---|---|
| Agrobielik 70 | min. 70% | luz 24–26 t · big-bag 1000 kg | | | ☐ |
| Agrobielik 90 | min. 90% | luz 24 t · big-bag 1000 kg | | | ☐ |
| Oxyfertil 90 | min. 90% | big-bag 1000 kg | — | | ☐ |
| Tlenkowe z magnezem | 70% CaO + 25% MgO | big-bag 1000 kg | — | | ☐ |
| Mieszanka tlenkowo-węglanowa | min. 70% | luz 24 t | | — | ☐ |

### Wapno węglanowe sypkie

| Produkt | CaO / MgO | Formy tonażowe | **od zł/t — luz** | **od zł/t — big-bag** | nie podawać |
|---|---|---|---|---|---|
| Węglanowe odmiana 04 | min. 50% CaO | luz 25–27 t · big-bag 1000 kg | | | ☐ |
| Węglanowe odmiana 05 | min. 50% CaO | *do potwierdzenia* | | | ☐ |
| Węglanowe z Mg odmiana 04 | min. 41% CaO + 8% MgO | luz 25–27 t | | — | ☐ |
| Węglanowe z Mg odmiana 05 | 25–37% CaO + 8–20% MgO | luz | | — | ☐ |

### Wapno granulowane — *priorytet, największy wolumen wyszukiwań*

| Produkt | CaO / MgO | Formy tonażowe | **od zł/t — big-bag** | nie podawać |
|---|---|---|---|---|
| Węglanowe granulowane | min. 50% CaO | big-bag 500 / 600 kg | | ☐ |
| Węglanowe z Mg granulowane | min. 31% CaO + 16% MgO | big-bag 600 kg | | ☐ |
| Kreda nawozowa granulowana | min. 50% CaO | big-bag 500 kg | | ☐ |

### Pozostałe

| Produkt | CaO | Formy tonażowe | **od zł/t — luz** | **od zł/t — big-bag** | nie podawać |
|---|---|---|---|---|---|
| Kreda nawozowa sypka | min. 50% | luz 24 t | | — | ☐ |
| Kreda pastewna | min. 37% | luz 24 t | | — | ☐ |
| Wapno hydratyzowane Bielik | min. 90% | luz 14–16 t | | — | ☐ |
| Wapno palone mielone wysokoreaktywne | min. 90% | luz 24 t · big-bag 1000 kg | | | ☐ |
| Kreda czarna jeziorna | — | big-bag 600 kg | — | | ☐ |
| Dolomit | CaO+MgO min. 45% | *tylko worki 10 / 25 kg* | — | — | nie dotyczy |
| Kreda malarska | — | *tylko worki* | — | — | nie dotyczy |

### Dwa pytania uzupełniające

1. **Czy podane widełki są loco magazyn, czy z transportem?** (Jeśli loco — dopiszemy „cena bez transportu, wyceniamy indywidualnie wg odległości".)
2. **Czy AGRIA ma własne konto na OLX?** Jeśli nie — to osobny temat do rozważenia, bo pośrednicy sprzedają tam pod marką Agrobielik.

---

## 4. Co robimy z odpowiedzią

| Gdzie | Co dokładnie |
|---|---|
| Landingi `/wapno-nawozowe/`, `/wapno-granulowane/` | sekcja „Ile kosztuje wapno" z widełkami + zastrzeżenie o tonażu i transporcie |
| Nowy poradnik „Ile kosztuje wapnowanie hektara" | przeliczenie widełek na hektar; fraza „ile kosztuje tona wapna" ma najwyższy CPC w projekcie (5,32 USD) |
| Karty produktów | cena „od" w WooCommerce — odblokowuje `offers` w schema `Product`, dziś generowanej bez oferty |
| Google Ads | dopiero po wdrożeniu sekcji dokładamy frazy cenowe do kampanii |

**Bez odpowiedzi nie wpisujemy żadnych kwot.** Liczby z OLX to ceny pośredników, nie AGRII — służą wyłącznie jako argument w rozmowie.
