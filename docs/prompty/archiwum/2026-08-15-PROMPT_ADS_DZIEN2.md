# Prompt startowy — Ads dzień 2 + weryfikacja geobloku (15.08.2026)

> Kontynuacja wątku z 14.08. Pełny zapis decyzji: `docs/decyzje/2026-08-14-korekty-kampanii-i-geoblok.md`
> (commit `bf75788`). Poprzedni ADR: `2026-08-13-uruchomienie-kampanii-ads.md`.

---

## Prompt do skopiowania

```
Wątek: Google Ads AGRIA — dzień 2 po korektach + weryfikacja geobloku.

Przeczytaj docs/decyzje/2026-08-14-korekty-kampanii-i-geoblok.md — tam jest
komplet wczorajszych zmian, sprostowań i gotchas.

Kampanie realnie ruszyły 14.08 o 14:00 (nie 13.08, jak zapisano wcześniej).
Wczoraj między 14:00 a 17:00: 158 wyświetleń, 12 kliknięć, 24,26 zł, zero konwersji.
Po tych trzech godzinach wprowadziliśmy komplet korekt — dziś pierwszy pełny dzień,
na którym w ogóle da się je ocenić.

Sprawdź i zestaw:

1. Google Ads (API, helper scripts/google/ads_call.sh, CID 674-207-1446):
   - search_term_view za pełną dobę — czy wykluczenia domknęły ogrodowe i dawkowe,
     co nowego weszło, czy dalej płacimy głównie za zapytania cenowe
   - rozkład godzinowy wydatku — czy harmonogram 6-22 dociągnął budżet do popołudnia,
     czy nadal gaśnie przed południem (to przesądza, czy wracamy do stawek)
   - CTR nowych tekstów "od producenta" wobec wczorajszych 7,5% ze starych
   - czy kampania Marka nadal ma zero wyświetleń

2. GA4 (property 538301430) — najważniejszy test dnia:
   - czy Singapur zniknął po geobloku (wczoraj 82 ze 123 sesji, 67%, zaangażowanie 0,0%)
   - czy "Page Not Found" spadło z 30 odsłon (tyle samo co strona główna)
   - czy pojawił się wreszcie ruch google/cpc na landingach
   UWAGA: raporty dzienne GA4 chodzą 4-6 h za rzeczywistością — sprawdzaj też Realtime,
   zanim uznasz, że czegoś nie ma.

3. Jeśli geoblok zadziałał — to pierwszy dzień, w którym dane GA4 nadają się do oceny
   kampanii. Powiedz wprost, co z nich wynika, a co nadal jest niemierzalne.

Otwarte, świadomie niezrobione:
- godziny pracy 8-16 czy 7-15 — czeka na potwierdzenie u Pawła, przesądza o harmonogramie
  połączeń i oknie emisji
- objaśnienia strukturalne: AGRIA zero, PrimaAuto 45 (do zrobienia z danych, które mamy)
- wizytówka Google niepodpięta do Ads
- zero grafik na koncie (kit z OLX odpada w całości)

POZA tym wątkiem, nie wchodź w to bez polecenia: ceny na kartach produktów
i podmiana certyfikatów. Cennik jest kompletny w docs/operations/CEN_LISTA_URL_2026-08-13.md,
ale to osobny temat.
```

---

## Stan na koniec 14.08 — ściąga

**Konto Ads 674-207-1446**

| Element | Stan |
|---|---|
| Kampanie | Rolnictwo 34 zł/dz · Marka 6 zł/dz, obie ENABLED, MANUAL_CPC |
| Harmonogram | 6:00–22:00, 7 dni, obie kampanie (wdrożone 14.08) |
| Stawki | granulowane 2,00 · nawozowe 2,00 · magnezowe 1,00 · brand 0,50 |
| Wykluczenia | 59 na kampanii Rolnictwo |
| Reklamy | 4 RSA, wszystkie z „od producenta", wymienione 14.08 ok. 15:40 |
| Konwersje główne | `generate_lead`, `Połączenia z reklam (30s+)` |
| Konwersje dodatkowe | `phone_click`, `form_submit`, `file_download` |

**Strona**

| Element | Stan |
|---|---|
| Geoblok | `agria-by-auranet/security-geoblock.php`, ENFORCE, fail-open |
| Kill-switch | `define('AGRIA_GEOBLOCK_OFF', true)` w `wp-config.php` |
| Landingi | `/wapno-granulowane/`, `/wapno-nawozowe/` — `noindex, follow`, numer Pawła |
| Consent | Complianz opt-in, Consent Mode v2, `url_passthrough` w GTM (wersja live 5) |
| GTM | GTM-TDC85TQN, 10 tagów, workspace bez niezapisanych zmian |

**Czego się spodziewać po geobloku:** GA4 powinno pokazać ruch polski zamiast 67%
Singapuru, a 404-ki spaść do pojedynczych — to był ten sam bot. Jeśli tak się **nie**
stanie, sprawdź, czy ruch nie idzie z cache edge CDN nazwa.pl (blok działa tylko
na żądaniach docierających do PHP).

**Gotchas, które kosztowały czas 14.08:**
- wykluczenia PHRASE nie odmieniają przez przypadki (`ogród` ≠ `ogrodowe`, `ogrodu`, `ogródek`)
- grep po statycznym HTML nie wykrywa tagów GTM — sprawdzaj `versions:live` w API
- MCP `write_file` nie tworzy katalogów
- `/conversionActions:mutate` blokuje klasyfikator uprawnień — robić w panelu
- dane godzinowe GA4 opóźnione ~4–6 h
