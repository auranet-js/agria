# 2026-05-27 — Akcept oferty stałej opieki SEO przez AGRIA

> ADR. Zamknięcie Fazy II (sprzedaż) → otwarcie Fazy III (realizacja M1).

---

## Status

Zaakceptowana 2026-05-27 (Paweł Bigos, AGRIA Sp. z o.o., po rozmowie wczorajszej z Kasjanem).

## Kontekst

2026-05-25 13:34 Janek wysłał do AGRIA (Paweł Bigos + Kasjan) ofertę stałej opieki SEO agria.pl — mail prosty dla zarządu + załącznik PDF ze szczegółowym planem M1-M6 (`docs/offers/agria-oferta-wyslana-2026-05-25.md` + `assets/offers/AGRIA-oferta-opieka-strona-2026-05-25.pdf`).

Model finansowy: **6 × 2 000 PLN netto / miesiąc**, faktura miesięczna VAT z 7-dniowym terminem, bez sumy całkowitej w komunikacji do klienta, M1 odrębny scope (fundamenty) bez premium cenowego — patrz `2026-05-19-pakiet-rozbicie-m1-m2do6.md` + `2026-05-19-korekta-ceny-m1-2000pln.md`.

## Decyzja klienta

**2026-05-27 10:39** (Paweł Bigos, mail Re: Agria.pl - oferta opieki nad stroną i pozycjonowania, forward Janka do `claude@auratest.pl` o 12:44 jako [18] w archiwum):

> Cześć,
> Po rozmowie wczorajszej z Kasjanem potwierdzamy że realizujemy przedstawiony plan opieki nad stroną agria.
> Jutro odezwę się do Ciebie jeszcze w sprawie poprawy kilku istotnych rzeczy na stronie.
> Pozdrawiam

**Interpretacja:**
- Pakiet 6-mies × 2 000 PLN netto zaakceptowany bez korekt.
- Decyzja kolektywna (Paweł operacyjnie, Kasjan budżetowo — model z `feedback_agria_offer_mail_structure` potwierdzony).
- Brak żądania zmian w scope / harmonogramie / formie umowy → wchodzimy w realizację wg `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md`.

## Konsekwencje

### Operacyjne natychmiast (2026-05-27 → 2026-05-31)

1. **Telefoniczne rozmowy Janek-Paweł** w sprawie ad-hoc poprawek + nauczenie Pawła self-edit przez Elementor — patrz `feedback_agria_pawel_relacja_telefoniczna`. **Nie piszemy draftu email do Pawła** (Janek 2026-05-27 odrzucił mój draft jako „kiepski" — sygnał że formalizacja jest nieadekwatna do relacji).
2. **Checklist dostępów do AGRIA** — wysyłka maila z listą wymagań T1 (patrz `M1_KICKOFF_2026-06.md` §„Checklist dostępów"): WP Admin, FTP/SFTP nazwa.pl, GBP Manager centrala, kontakt decyzyjny.
3. **Decyzja Janka — pre-payment vs post-payment M1.** Plan mówi „faktura M1" w T4 po końcowym akcepcie — to post-payment 30.06. Alternatywa: pre-payment 01.06 z terminem 7 dni. Sugestia: post-payment.
4. **Bez umowy pisemnej** — Janek 2026-05-27: „nie podpisujemy umowy, to są zaufani ludzi, opieramy to właśnie na akceptacji mailowej". Akcept Pawła z 10:39 = wystarczająca podstawa. Patrz `feedback_agria_no_written_contract_trust_based`.

### Operacyjne 2026-05-28+ — backlog ad-hoc Pawła

Paweł zapowiedział „Jutro odezwę się jeszcze w sprawie poprawy kilku istotnych rzeczy na stronie". To **backlog ad-hoc poza planem M1**. Framework triage (per pozycja):

| Klasa | Kryterium | Konsekwencja |
|---|---|---|
| **A. W M1** | mieści się w P0-P5 z audytu LUB w deliverable „plan on-page" / „audyt treści" | bez dodatkowej faktury |
| **B. Przesunięte do M2-M6** | mieści się w segmentowym scope tematycznym | wpada do harmonogramu, bez dodatku |
| **C. Osobne zlecenie** | rozbudowa funkcjonalna (kalkulator, nowa sekcja, formularz, integracja), reskin, copy poza SEO, grafika | wycena godzinowa osobno, akcept Janka per pozycja |
| **D. Po stronie klienta** | wymaga materiałów / decyzji od AGRIA przed implementacją | blokujemy do dostawy, nie liczymy |

Rejestr w `docs/operations/BACKLOG_TRIAGE.md` (tworzony po nadejściu listy).

### Dokumenty / memory zaktualizowane (tej sesji)

- `docs/PROJECT_STATE.md` — Faza II → III, oferta zaakceptowana
- Memory `project_agria_offer_status` — status ZAAKCEPTOWANA, timeline, oczekiwany backlog
- Memory `MEMORY.md` index — opis pozycji zaktualizowany
- Nowy `docs/operations/M1_KICKOFF_2026-06.md` — agenda kickoff, dostępy, harmonogram T1-T4

### Dokumenty / memory do utworzenia po triażu backlog (2026-05-28+)

- `docs/operations/BACKLOG_TRIAGE.md` — żywy rejestr klasyfikacji pozycji
- Ewentualne ADR per decyzja o zakresie M1 vs osobne zlecenie (jeśli klient pcha duże rzeczy do M1)

### Nie zmienia się

- Scope M1 (6 deliverables fundamentów) wg `MONTH_1_FOUNDATIONS_PLAN.md`.
- Scope M2-M6 (segmentowy rozkład tematyczny).
- Strategia bez budżetu LB (`2026-05-19-seo-bez-budzetu-linkbuilding.md`).
- Pre-M1 proof-of-value wykonany przez Auranet zostaje przy AGRIA bez fakturowania.
- Cena: 6 × 2 000 PLN, M1 bez premium.
- Reguły komunikacji do klienta przez gate Janka (`feedback_never_email_clients_directly`).

## Alternatywy odrzucone

Brak — akcept klienta nie zostawia pola do alternatyw negocjacyjnych. Otwarte decyzje (umowa pisemna, pre/post-payment) to konsekwencje, nie alternatywy decyzji o akcepcie.

## Otwarte do rozstrzygnięcia w T1 M1

1. Termin płatności M1 (decyzja Janka, propozycja: post-payment 30.06).
2. 4 pytania z `docs/catalog/CATALOG_VS_WC_GAP.md` (cement/kruszywo, Kreda czarna, Agrobielik 90, SKU) — slot z handlowcem w T1.
3. Dostępy FTP/SFTP nazwa.pl — konto Auranet czy klienta?

Zamknięte 2026-05-27:
- Format umowy → **bez umowy pisemnej**, opieramy się na akcepcie mailowym Pawła (`feedback_agria_no_written_contract_trust_based`)
- Obsługa backlog Pawła → telefon Janka + Elementor self-edit (`feedback_agria_pawel_relacja_telefoniczna`)

## Powiązane

- Mail źródłowy: `/tmp/claude-mails/18/body.txt` (forward Janka, oryginał Paweł 10:39)
- Memory: `project_agria_offer_status` (status), `feedback_agria_offer_mail_structure` (model Paweł+Kasjan), `feedback_never_email_clients_directly` (gate komunikacji), `feedback_no_made_up_pricing_without_approval` (triage backlog)
- Decyzje: `2026-05-19-pakiet-rozbicie-m1-m2do6.md`, `2026-05-19-korekta-ceny-m1-2000pln.md`
- Plany: `docs/offers/AURANET_2000PLN_MONTHLY.md`, `docs/offers/MONTH_1_FOUNDATIONS_PLAN.md`, `docs/operations/M1_KICKOFF_2026-06.md`
