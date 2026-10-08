# 2026-10-08 — OLX cykl 3, zaległe kontrole SEO, plany trzech wątków

Commit `f41d851` (push na `main`). Kalendarz „Auranet Claude”: kontrole OLX **20.10**, **30.10**, **09.11**.

## Co zrobione

| Obszar | Wynik |
|---|---|
| Kontrola OLX po audycie | 23.09 → 08.10: **2,52 odsłony numeru/dobę** (wcześniej 1,60), koszt ~**17 zł** (było 27). `docs/raporty/2026-10-08-OLX_KONTROLA_PO_AUDYCIE.md` |
| Rozmowa Janka z Pawłem | pakiet **przedłużony**, z OLX **2 zamówienia na całe samochody tlenku**, na ogłoszeniach tylko numer Pawła (odsłona ≠ telefon), najwięcej telefonów o tlenek, małe ilości tylko z Niedomic/Radgoszczy. ADR `docs/decyzje/2026-10-08-olx-tlenek-wysylka-z-magazynow.md`, `docs/FAKTY_KLIENTA.md` §5–6 (w tym Wielan) |
| OLX na koncie | T-149 (11 przełożonych) · T-150/T-152 (77 tytułów i opisów, 5 × „kreda do stawu”) · T-151+T-155 (15 → Agrobielik 70) · T-156 (14 w pas rolniczy) · T-163 (72 × sekcja „SKĄD ODBIERZESZ I JAK DOWOZIMY”). **40 ogłoszeń zmienionych mocno**, tlenek 74 → 89. Wszystko zweryfikowane: active + telefon + miasto |
| Ranking gmin rolniczych | GUS BDL (ewidencja 2014), mapa `docs/rynek/2026-10-08-mapa-intensywnosc.html` (auratest), dane `data/rynek/2026-10-08-gminy-grunty-orne.json` |
| Kontrole SEO | T-078, Marka, T-092, T-085, T-093 — `data/kontrole/2026-10-08-kontrole-zalegle-seo.md`, eventy odhaczone |
| Plany wątków | SEO `docs/seo/2026-10-08-PLAN-PAZDZIERNIK-LISTOPAD.md` (T-157…T-162) · wizytówki `docs/gbp/2026-10-08-PLAN-OBSLUGI-X-XI.md` (T-165…T-170) · OLX `docs/olx/2026-10-08-PLAN-CYKL-3.md` |

## Wnioski warte pamiętania

- **Odsłony numeru z API ≠ telefony.** Tlenek ma najmniej odsłon na ogłoszenie (0,32–0,34), a u Pawła najwięcej telefonów i oba zamówienia. Liczbę telefonów i zamówień bierzemy od Pawła.
- **OLX szukają ludzie z miast, nie ze wsi:** ogłoszenia w gminach rolniczych miały 0,36 odsłony numeru/ogł., poza nimi 0,54. T-156 to test, nie pewniak.
- **Tlenek wokół magazynów jest nasycony** (28 ogłoszeń Agrobielika w 70 km) — nowych nie stawiać bliżej niż 20 km od istniejącego.
- Statusy `disabled` po PUT są przejściowe (2–3 min) — zawsze kontrola po kilku minutach, nie panika.
- **Zamiana produktu** szła przez kontrolę uprawnień dopiero po zgodzie Janka; skrypty: `scripts/olx/zamiana_cykl3.py`, `tresc_cykl3.py --wsad <plik>` (znacznik per seria w `posted.json`).
- Dane GUS dla gmin bez filtra `year` zwracają ewidencję 2014; filtr roku psuje zapytanie.

## Otwarte

**OLX**
- **T-164 „promocja tlenku”** — prośba Pawła: opcje płatnej promocji OLX, ceny, 3–5 ogłoszeń Agrobielika 70, budżet do akceptu Janka. Uwaga: ADR 07.08 („wolumen zamiast promowania”) — to wąski test.
- T-153 „zgodność opisów z regulaminem” — odłożone (POZOSTAŁA OFERTA 200/200, „od X zł/t”).

**SEO** — do „ok” Janka, każda zmiana z linkiem do akceptu i zgłoszeniem w GSC:
- T-157 „tytuł i opis kategorii Wapno nawozowe”, T-158 „wapno palone przed szczytem X–XI”, T-159 „hub → karta wapna magnezowego”, T-160 „kotwice fraz rodzajowych”.
- Ads Rolnictwo: T-161 „wstrzymanie 12 fraz QS ≤3”, T-162 „grupa Wapno granulowane na karty” — decyzje osobno.
- Pytanie: zamknąć T-084 na rzecz T-158?

**Wizytówki**
- Posty: 13.10 / 20.10 / 27.10 / 03.11 (`docs/gbp/2026-10-08-pazdziernik-publikacje.md`, wsady `tmp/gbp-posty/2026-10-*.json`) — **akcept tekstów + „ok” na konwersję 2 zdjęć webp → JPG** w uploads; eventy wtorkowe po akcepcie.
- T-165 „odpowiedzi na 8 opinii Niedomic”, T-166 „profil Niedomic”, T-167 „przejęcie Radgoszczy” (potwierdzone z Pawłem), T-168 „usługi Tarnów”, T-169 „karta opinii z QR” (zeskanować QR przed drukiem), T-170.
- Decyzje Janka: reguły „opinie tylko Tarnów” i „przemilczeć oddziały” (powstały bez dostępu), telefon główny Tarnów = stacjonarny, opis profilu z branżami zdjętymi z menu.

**Czeka na Pawła:** T-077 „kreda pastewna” (dawki — Paweł szuka i konsultuje z Kasjanem); post GBP o kredzie pastewnej wstrzymany do tego czasu.

**Zauważone obok:** literówka „Wyślj wiadomość” w stopce strony; JPG z 2844/2845 nieużywany (do usunięcia na „ok”).

## Prompt kontynuacyjny

```
Pracujemy w ~/projekty/agria. Przeczytaj docs/sesje/2026-10-08-olx-cykl3-seo-gbp.md
i docs/decyzje/2026-10-08-olx-tlenek-wysylka-z-magazynow.md.

Trzy linie usług, każda osobno — zacznij od tej, którą wskażę; bez wskazania: OLX.
1. OLX — T-164 „promocja tlenku”: sprawdź opcje płatnej promocji na OLX (Partner API / cennik),
   ceny, zaproponuj 3–5 ogłoszeń Agrobielika 70 (dane: data/olx/statystyki.json, posted.json)
   i budżet; nic nie kupuj bez mojego „ok”. Jeśli jest po 20.10 — najpierw event kontrolny z kalendarza.
2. SEO — T-157…T-160 z docs/seo/2026-10-08-PLAN-PAZDZIERNIK-LISTOPAD.md: po kolei, każda zmiana
   z backupem, linkiem do akceptu i zgłoszeniem w GSC (memory feedback_agria_edycja_link_akcept_gsc).
   T-161/T-162 (Ads) tylko jako decyzja do mnie.
3. Wizytówki — docs/gbp/2026-10-08-PLAN-OBSLUGI-X-XI.md: najpierw akcept postów październikowych
   i konwersja 2 zdjęć do JPG, eventy wtorkowe; potem T-165 (odpowiedzi Niedomice) do akceptu.
Jeśli Paweł odpowiedział o kredzie pastewnej — T-077 wg sekcji „Otwarte” w
docs/sesje/2026-10-08-tresci-pazdziernik-staw-ph-menu.md.
Na start: sprawdź kalendarz „Auranet Claude” dla agria (dziś + zaległe).
```
