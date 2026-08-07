# OLX — spięcie API i inwentaryzacja konta AGRII

> Data: 2026-08-07. Konto ogłoszeniowe przekazane przez Pawła (mail [201]).
> Pytanie od klienta do odpowiedzi: *„czy kupujemy dalej pakiet 30 ogłoszeń, czy lepiej wziąć mniejszy pakiet, np. 10, i skupić się na ich promowaniu"*.

---

## 1. Dostęp — stan gotowy

Aplikacja **„Agria.pl"** w `developer.olx.pl` żyje na koncie Janka (`js@auranet.com.pl`), `client_id 203091`, scope `v2 read write`. Konto ogłoszeniowe AGRII podpięte pod nią 07.08.2026 przez OAuth2 `authorization_code` — **przeglądarka musi być w tym momencie zalogowana na konto AGRII**, inaczej token wychodzi na konto Janka.

| Element | Gdzie |
|---|---|
| Callback OAuth (deploy) | `~/domains/auratest.pl/public_html/olx/agria-callback.php` |
| Źródła (repo) | `scripts/olx/agria-callback.php`, `scripts/olx/olx-agria` |
| Helper CLI | `~/bin/olx-agria` — `url` / `status` / `refresh` / `api <ścieżka>` |
| Sekrety + tokeny | `~/domains/auratest.pl/olx-private/` (700, HTTP 404 z zewnątrz) |
| Login/hasło konta AGRII | `~/secrets/agria/olx.txt` |

**Gotcha, która kosztowała jedno podejście:** PHP na auratest.pl ma `open_basedir` ograniczony do katalogu domeny — **nie przeczyta niczego z `~/secrets/`**. Stąd sekrety OLX leżą w `olx-private/` wewnątrz domeny, a w `~/secrets/olx/README.txt` został tylko wskaźnik. Kod autoryzacyjny OLX żyje 60 s, więc wymiana na tokeny musi lecieć w samym callbacku.

Konto: id `43762401`, `pawelxpb@gmail.com`, firmowe (`is_business: true`), założone 2016-06-21.

---

## 2. Stan konta — 20 ogłoszeń

| Status | Ile | Uwaga |
|---|---|---|
| `active` | 1 | ważne do 17.08, jedyne z włączonym `auto_extend` |
| `limited` | 2 | w tym **najlepsze ogłoszenie na koncie** |
| `outdated` | 17 | wszystkie wygasły **18.07.2026** |

**AGRIA zniknęła z OLX trzy tygodnie temu, w środku sezonu.** Wygaśnięcie 17 ogłoszeń tego samego dnia wygląda na koniec opłaconego pakietu.

Wszystkie ogłoszenia o wapnie to **jedna oferta powielona na 18 miast** (lat 49,6–51,8: Małopolska, Świętokrzyskie, Śląsk, Łódzkie), cena wszędzie **400 zł** (jedno 440), po 8 zdjęć, kategoria `4368 Nawozy` (18 szt.) i `765 Pozostałe` (1 szt.). Pakiet szedł więc w zasięg geograficzny **jednego** produktu, nie w różne produkty.

Na koncie wisi też prywatne ogłoszenie Pawła (mieszkanie, kat. 15). API ma do niego dostęp — **nie ruszamy**.

---

## 3. Statystyki — twarde dane z API

| | wyświetlenia | odsłony telefonu |
|---|---|---|
| Top 3 ogłoszenia | 5 483 (75%) | 149 (71%) |
| Pozostałe 16 geo-duplikatów | 1 790 | 60 |
| **Razem (cykl życia)** | **7 273** | **209** (CR 2,9%) |

Ranking:

| wyśw. | tel. | status | ogłoszenie |
|---|---|---|---|
| 2 514 | **94** | `limited` | **„Do stawu, wapno nawozowe tlenkowe, palone 70%/90%…"** |
| 1 697 | 28 | `outdated` | „Wapno nawozowe węglanowe, tlenkowe, sypkie granulowane" |
| 1 272 | 27 | `active` | „Wapno nawozowe tlenkowe CaO 70%, odkwaszanie" |
| ~110 śr. | ~3 śr. | `outdated` | 16 × geo-duplikat „Wapno tlenkowe CaO 70%/90% • Luzem / BigBag • Najtaniej!" |

**Jedno ogłoszenie („Do stawu") odpowiada za 45% wszystkich kontaktów telefonicznych z całego konta — i dziś jest wyłączone.**

Dla skali: 209 odsłon telefonu z OLX wobec **221 kliknięć z całego organiku w lipcu** (GSC). To nie jest kanał poboczny.

---

## 4. Wnioski wstępne (przed rekomendacją dla klienta)

> **Korekta 07.08 wieczorem** — punkt 2 poniżej został obalony przez dane rynkowe, patrz `OLX_KONKURENCJA_2026-08-07.md` §2. Geo-multiplikacja **jest** modelem tej kategorii; AGRIA prowadziła ją w 1/8 skali lidera i na jednym produkcie. Punkt 1 się broni.

1. **Intencja w tytule robi różnicę.** „Do stawu" bije kopie „Najtaniej!" o rząd wielkości przy tej samej ofercie i tych samych zdjęciach.
2. ~~**Geo-multiplikacja ma słabą stopę zwrotu** — ~110 wyświetleń i 3 telefony na duplikat.~~ → liderzy rynku robią dokładnie to samo, tylko na 9–26 różnych ofertach × 120–161 miast.
3. **Stawy działają na OLX, choć w Google Ads mają zerowy wolumen** (patrz memory `project_agria_ads_sezonowosc`). Kanały nie są wymienne — segment martwy w płatnym wyszukiwaniu potrafi być najmocniejszy na marketplace.
4. `auto_extend` jest włączony na **jednym** z 20 ogłoszeń — reszta wygasa cicho.
5. **Rozjazd cenowy:** opis aktywnego ogłoszenia mówi „600 zł brutto/t" przy worku 40 kg, a cennik z 07.08 daje 19 zł/szt = 475 zł/t netto. Do uspójnienia razem z wdrożeniem cen na stronie.

**Czego brakuje do rekomendacji:** aktualnych cen pakietów ogłoszeń i wyróżnień OLX w kategorii Nawozy (2026). Bez tego liczby w rekomendacji byłyby zgadywaniem.

---

## 5. Bezpieczeństwo

- Hasło do konta AGRII przyszło mailem plaintextem — **do zmiany + 2FA** (zgłosić Pawłowi przez Janka).
- Konto jest prywatno-firmowe (prywatny Gmail Pawła, prywatne ogłoszenie mieszkania). Docelowo warto rozważyć konto firmowe na adres AGRII — ale to decyzja klienta, nie nasza.
