# PROJECT_STATE.md — Stan projektu AGRIA

> Ostatnia aktualizacja: maj 2026. Plik aktualizowany przy istotnych zmianach. Czytany przez Claude'a na początku każdej sesji.

---

## Status ogólny

**Faza projektu:** przejście z FAZY I (budowa infrastruktury) do FAZY II (aktywacja + sprzedaż usług marketingowych).

**Auranet jako wykonawca:** zbudował stronę, identyfikację, katalog. Teraz domyka monetyzację współpracy — pakiet utrzymaniowo-rozwojowy ~2000 PLN netto / mies. (12–15 h pracy).

---

## Co jest gotowe ✅

### Infrastruktura strony
- **agria.pl** — uruchomione, WP 6.9.4, WC 10.6.1, motyw `Agria By Auranet 2.0.0`, PHP 8.3.30
- Hosting nazwa.pl (serwer371853)
- MCP `Agria.pl` skonfigurowany i działający — read-only dostęp do bazy, plików, WC

### Identyfikacja
- Logo (refresh) — gotowe
- Kolory firmowe ustalone:
  - Główny ciemnozielony `#354E33`
  - Akcent jasnozielony `#61CE70`
  - Drugorzędny `#798D7A`
  - Tekst `#596A5A`
- Typografia: Plus Jakarta Sans (nagłówki) + Bai Jamjuree (tekst)
- Ulotka A6 — gotowa, w produkcji
- Wizytówki — w przygotowaniu

### Katalog produktowy (druk)
- Spec 24-stronicowy gotowy (`docs/catalog/PRINT_CATALOG_SPEC.md`)
- Wzorzec JSX dla InDesign przygotowany na bazie Agrobielik 70 (`assets/AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx`)
- **Do zrobienia:** 17 pozostałych kart produktów (duplikacja + podmiana danych z MCP)

### WooCommerce
- 19 produktów opublikowanych
- Kategorie: Rolnictwo, Sadownictwo, Rybactwo, Oczyszczalnie, Budownictwo, Hurtownie, Paszarstwo
- Stan: patrz `docs/catalog/PRODUCTS_INVENTORY.md`

---

## Co jest w toku 🟡

### Pakiet on-page SEO + utrzymanie (2000 PLN/mies × 6 mies)
**Status:** zielone światło wstępne od klienta, czekamy na finalne potwierdzenie po przedstawieniu oferty.

**Kolejność działań:**
1. ⏳ Audyt techniczny + on-page SEO (na koszt Auranet, baseline pod ofertę) — `docs/seo/SEO_AUDIT_PLAN.md`
2. ⏳ Wdrożenie analityki (GA4, GSC, GTM) — na razie pod konto Auranet
3. ⏳ Przygotowanie oferty 6-miesięcznej (czerwiec–listopad 2026) — `docs/offers/AURANET_2000PLN_MONTHLY.md`
4. ⏳ Prezentacja oferty klientowi
5. ⏳ Po akceptacji: rozpoczęcie planu miesięcznego

### Katalog 24-str
- 1/18 kart produktów gotowa (Agrobielik 70)
- Pozostałe 17 — generowanie z MCP `Agria.pl:catalog_product`

---

## Co jest zablokowane / czeka 🔴

- **Google Ads** — czeka na akceptację oferty miesięcznej i zatwierdzenie budżetu 3000 PLN/mies przez zarząd AGRIA
- **Baza oczyszczalni (Segment B)** — przygotowanie po stronie klienta (handlowiec B2B)
- **Sesja zdjęciowa** dla katalogu i strony — niezakontraktowane

---

## Decyzje, ustalenia, kompromisy

| Data       | Decyzja                                                                  | Status |
|------------|--------------------------------------------------------------------------|--------|
| Q1 2026    | Stack: WordPress + WooCommerce + Elementor (motyw autorski Auranet)     | ✅     |
| Q1 2026    | Paleta kolorów: zielenie zgodne z Elementor Global Colors                | ✅     |
| Q1 2026    | Z katalogu drukowanego wycinamy „Kredę czarną (jeziorną)"               | ✅     |
| Q1 2026    | Katalog: 24 strony A4 zszywane, oprawa saddle stitch                     | ✅     |
| Q2 2026    | Audyt SEO na koszt Auranet, oferta 2000 PLN/mies, 6-miesięczne ramy     | 🟡     |
| Q2 2026    | Format umowy: faktura miesięczna VAT, ramowa umowa na 6 mies            | ⏳     |

---

## Otwarte pytania do klienta

1. Czy AGRIA ma ustawione **konto Google Ads** + dostęp do **Google Search Console**? (potrzebne do oferty)
2. **Dostępy FTP/SFTP** do nazwa.pl — czy mamy je na własnym koncie Auranet, czy na koncie klienta?
3. **Zakres umowy 2000 PLN** — czy obejmuje też prowadzenie social media, czy tylko on-page + content + analityka?
4. **Sesja zdjęciowa katalogu** — kto finansuje (1500–2500 PLN)?
5. **CRM** — Google Sheets na start wystarczy, czy klient chce coś poważniejszego (HubSpot Free, Pipedrive)?

---

## Następne kroki (operacyjnie)

### Tydzień bieżący
- [ ] Wykonać audyt techniczny strony agria.pl (Lighthouse, PageSpeed, Screaming Frog, Ahrefs/Senuto)
- [ ] Spisać findings do `docs/seo/SEO_AUDIT_RESULTS.md` (utworzyć po wykonaniu audytu)
- [ ] Wdrożyć GA4 + GSC + GTM (placeholder pod konto Auranet, do przekazania klientowi)

### Najbliższe 2 tygodnie
- [ ] Doszlifować ofertę `docs/offers/AURANET_2000PLN_MONTHLY.md`
- [ ] Prezentacja oferty klientowi
- [ ] Generacja JSX dla 17 pozostałych kart katalogu (skrypt batchowy)

### Czerwiec 2026 (po akceptacji oferty)
- [ ] Plan prac miesięcznych — czerwiec / lipiec / sierpień
- [ ] Wystawienie pierwszej faktury 2000 PLN
- [ ] Start miesięcznego raportowania (KPI z GA4 + GSC)
