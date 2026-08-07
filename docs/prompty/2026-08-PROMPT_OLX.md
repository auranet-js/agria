# Prompt startowy — OLX (wątek OLX)

> Utworzony 2026-08-07 po spięciu API i inwentaryzacji konta.
> Czytaj najpierw: `docs/operations/OLX_INWENTARYZACJA_2026-08-07.md` + memory `reference_agria_olx_api`.

## Stan wejściowy

API spięte i działa (`~/bin/olx-agria api /partner/adverts`), scope `v2 read write`, refresh token jest. Konto AGRII: 20 ogłoszeń, **1 aktywne**, 17 wygasło 18.07 — czyli firma zniknęła z OLX w środku sezonu. Wszystkie ogłoszenia to jedna oferta powielona na 18 miast. Cykl życia: 7 273 wyświetlenia, 209 odsłon telefonu, z czego **45% kontaktów pochodzi z jednego ogłoszenia „Do stawu", które jest dziś wyłączone**.

Paweł pyta: *„kupujemy dalej pakiet 30 ogłoszeń, czy mniejszy pakiet, np. 10, i skupiamy się na promowaniu?"* — i prosi o spojrzenie fachowym okiem.

## Zadania

| ID | Zadanie |
|---|---|
| OLX-01 | Dociągnąć **aktualne ceny pakietów ogłoszeń i wyróżnień OLX w kategorii Nawozy (2026)** — bez tego rekomendacja to zgadywanie. Panel konta + cennik OLX dla firm |
| OLX-02 | Rekomendacja dla Pawła: liczba ogłoszeń vs promowanie vs **różnicowanie intencji w tytułach**. Teza do obronienia danymi: różnicę robi intencja („do stawu", „odkwaszanie gleby", „granulowane"), nie liczba slotów ani miasto |
| OLX-03 | Reaktywacja: włączyć `auto_extend` (dziś na 1 z 20), przywrócić najlepsze ogłoszenie („Do stawu", 94 telefony) |
| OLX-04 | Uspójnić ceny w ogłoszeniach z cennikiem z 07.08 — opis mówi „600 zł brutto/t" przy worku 40 kg, cennik daje 475 zł/t netto |
| OLX-05 | Ocenić, czy warto generować i rotować ogłoszenia z 19 kart WooCommerce przez API (scope `write` jest) — to zmienia odpowiedź na pytanie Pawła |
| OLX-06 | Zgłosić Pawłowi przez Janka: zmiana hasła (przyszło plaintextem) + 2FA |

## Ograniczenia

- Ceny na OLX nie mogą schodzić poniżej cen stałych odbiorców (np. Wialan) — konflikt kanałowy, patrz `CENNIK_PAWEL_2026-08-07.md` §5.
- Na koncie wisi **prywatne ogłoszenie Pawła** (mieszkanie, kat. 15). API ma do niego dostęp — nie ruszać.
- Stawy mają na OLX najwyższą skuteczność, mimo że w Google Ads segment ma zerowy wolumen (`project_agria_ads_sezonowosc`). Nie przenosić wniosków między kanałami.
