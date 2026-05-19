# 2026-05-19 — Korekta ceny M1: 2000 PLN, nie widełki 3500-5000

> ADR. Korekta decyzji `2026-05-19-pakiet-rozbicie-m1-m2do6.md` w części dotyczącej kwoty M1.

---

## Status

Zaakceptowana 2026-05-19 wieczorem (Janek po przeczytaniu quizu sesji z trzema pytaniami zawierającymi widełki 3500-5000).

## Kontekst

W sesji 2026-05-19 powstały dwa dokumenty:
- `docs/offers/AURANET_2000PLN_MONTHLY.md` v2.0 — rewrite oferty z monolitu 6×2000 PLN na rozbicie M1 + M2-M6
- `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — szczegółowy plan M1

W obu wpisana została **cena M1 = 3500-5000 PLN netto, stawka 175-200 PLN/h, 20-25h pracy**. Te liczby wzięły się z mojej (Claude'a) interpretacji memory `project_first_month_foundations_offer.md`, które mówiło o „większym budżecie jednorazowym wstępnie zaakceptowanym budżetowo".

**Memory nie zawierało konkretnej kwoty.** Widełki 3500-5000 wymyśliłem bez wyraźnego akceptu Janka.

## Decyzja

**Cena M1 = 2000 PLN netto, jak każdy inny miesiąc pakietu.**

Pakiet 6-miesięczny dla AGRIA:
- M1 (czerwiec 2026) — **2000 PLN netto** (fundamenty: strategia + analityka + KR + content audit + plan on-page + baseline)
- M2-M6 (lipiec-listopad 2026) — **5 × 2000 PLN netto = 10 000 PLN** (rozwój)
- **Razem: 6 × 2000 PLN = 12 000 PLN netto**

Brak rozróżnienia kwotowego między M1 a kolejnymi miesiącami. M1 zachowuje **odrębny scope** (fundamenty), ale nie odrębną cenę.

## Dlaczego

1. **Memory mówiło o briefie, nie kwocie.** „Wstępnie zaakceptowany budżetowo" znaczy „klient akceptuje rząd wielkości pakietu", nie „klient zgadza się na premium za M1".
2. **Widełki w dokumencie klient-facing są nieprofesjonalne.** Klient czyta „od 3500 do 5000" jako brak pewności i punkt wyjściowy do negocjacji w dół. Albo konkretna cena, albo placeholder.
3. **Brzytwa: jeśli klient akceptuje 2000 PLN/mies przez 6 mies bez problemu, ale waha się przy premium za M1, ryzyko utraty kontraktu rośnie.** Lepiej 12 000 PLN z gładkim startem niż 13 500-15 000 PLN z negocjacją od M1.
4. **Pre-M1 proof-of-value robiony przez Auranet „na koszt Auranet" jest właśnie po to**, żeby M1 nie wymagał premium. Audyt baseline (Wątek 1, ~6h), keyword research baseline (Wątek 2.5, ~4h + $0.15 DataForSEO), analityka GA4+GTM+GSC pre-M1 (Wątek 3, ~5h), fix indeksacji (Wątek 4, ~3-4h) — łącznie ~18-20h pracy proof-of-value przed startem M1. To zostaje przy AGRIA jako bonus, nie jest fakturowane.
5. **M1 w 2000 PLN to ~10-12h pracy** — wystarczy na dopełnienie tego, co nie zostało zrobione w pre-M1: strategia 6-mies (PDF klientowi), content audit + topic clusters, plan on-page rozbity per miesiąc, Looker Studio dashboard, baseline metryk, raport startowy M1.

## Konsekwencje

### Dokumenty do korekty (w tej sesji)
- `docs/offers/AURANET_2000PLN_MONTHLY.md` — zmiana wszystkich wystąpień widełek 3500-5000 → 2000 PLN, total 12 000 PLN. Tabela struktury pakietu uproszczona (6 × 2000). Sekcja „Wersja do klienta — szkic" zaktualizowana. Changelog v2.0 → v2.1.
- `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md` — cena = 2000 PLN, godziny ~10-12h zamiast 20-25h. Rozkład deliverables proporcjonalnie zmniejszony, z wyraźnym zaznaczeniem co zostało zrobione w pre-M1 jako proof-of-value (nie liczone w M1).
- `docs/PROJECT_STATE.md` — sync z tą decyzją + Wątki 3 i 4.

### Memory do aktualizacji
- `project_first_month_foundations_offer.md` — opis M1 z „większy budżet" → „2000 PLN, standardowa kwota miesięczna".
- Nowy feedback memory `feedback_no_made_up_pricing_without_approval.md` — reguła systemowa zabezpieczająca przed powtórzeniem: nie zmyślam cen bez akceptu Janka.

### Decyzje uchylone
- Kwoty z `2026-05-19-pakiet-rozbicie-m1-m2do6.md` (jeśli były) — zastąpione tą decyzją. Sama logika rozbicia M1 / M2-M6 (scope) zostaje.

### Nie zmieniają się
- Scope M1 (6 deliverables fundamentów).
- Scope M2-M6 (utrzymanie, on-page, content 4 art/mies, narzędzia, raportowanie, ad-hoc).
- Strategia bez budżetu LB (`2026-05-19-seo-bez-budzetu-linkbuilding.md`).
- Pre-M1 proof-of-value wykonany przez Auranet zostaje „na koszt Auranet".
- Format umowy (ramowa 6-mies, klauzula wypowiedzenia 30-dniowa od końca M1).

## Alternatywy odrzucone

| Wariant | Dlaczego nie |
|---|---|
| Widełki 3500-5000 w ofercie | Nieprofesjonalne, sygnał słabej pewności co do wyceny, pole do negocjacji w dół |
| M1 = 5000 PLN (sufit) | Ryzyko utraty kontraktu na pierwszym etapie — klient odbije się od kwoty premium |
| M1 = 3500 PLN (dół) | Niedoszacowanie pracy + sygnał „tani onboarding"; jeśli ma być 2000, to lepiej 2000 (równe) niż 3500 (dziwna kwota) |
| Pakiet 5×2000 + M1 free | Wartość M1 niedoceniona, klient traktuje fundamenty jako koszt sprzedaży Auranet, nie jako produkt |

## Lekcja

Memory typu „budżet wstępnie zaakceptowany" **nie jest mandatem do zmyślenia konkretnej liczby**. Konkretna kwota = wymaga konkretnego akceptu Janka w czacie.

Patrz: `feedback_no_made_up_pricing_without_approval.md`.
