# Prompt startowy — następny wątek AGRIA: „leć pod wynik"

> Wklej/uruchom to na początku następnej sesji `claude` w `~/projekty/agria`.
> Cel wątku: robić **treść pod wynik** (widoczność w Google), nie technikę. Dowód = ruch pozycji w GSC.

---

## Kontekst (przeczytaj najpierw)

1. `docs/MASTER_PROMPT.md` — tożsamość i zakres (Fractional CMO branży surowcowej; ton: fakty/parametry/zastosowania; zero lifestyle; NIE dodawaj produktów spoza oferty).
2. `docs/seo/SEO_STRATEGIA_POD_WYNIK_2026-07-08.md` — **analiza SERP + konkurencja + strategia**. To jest baza tej roboty.
3. `docs/audits/KEYWORD_RESEARCH_2026-05-19.md` + `KR_PRIORYTETYZACJA_2026-06-15.md` + `CONTENT_AUDIT_2026-06-15.md` — frazy i mapowanie.
4. Stan techniczny/rdzeń URL: `docs/PROJECT_STATE.md` + `docs/decyzje/2026-07-08-rdzen-url-taksonomia.md` (fundament zrobiony — NIE wracaj do techniki bez potrzeby).

## Zasady (twarde)

- **Content-facing framing:** AGRIA to buduje, nie krytykujemy stanu strony (memory `feedback_agria_no_self_criticism_built_site`). Rozwojowo, nie „brak/błąd".
- **Komunikacja do klienta wyłącznie do Janka** (`js@auranet.com.pl`) — nigdy do klienta.
- **Zapis na produkcję:** MCP `mcp__agria__*` (query_db_write/update_postmeta/update_post_content) + FTP (`~/secrets/agria/netrc`) na .htaccess/theme/plugin. Zapisy w RankMath (serializowane opcje) = jednorazowy skrypt PHP przez FTP, uruchom RAZ i SKASUJ.
- **Produkcyjny .htaccess / motyw / plugin: pokaż diff, czekaj na „ok".**
- **Sprawdzaj MCP `status` na starcie.** CDN nazwa.pl → cache-bust przy weryfikacji; czyść `_elementor_element_cache` po zmianie stron Elementora.
- **Indexing API tylko przez `~/bin/index-submit`** (budżet ad-hoc 100/dobę, pokaż zużycie).
- **DataForSEO przez curl** (`~/secrets/dataforseo/basic-auth-b64.txt`); SERP live/advanced = 1 fraza/zapytanie. Saldo ~$42.8.

## Kolejność robót (ROI malejąco)

### KROK 1 — Przebudowa `/wapnowanie-gleby/` (dowód konceptu, najszybszy zysk)
Cel: „ile wapna na hektar" / „ile wapna na ha" (720/mc) z **poz. 14 → strona 1**.
Do zrobienia (z diagnozy WebFetch):
- **Quick-answer na górze** z konkretnymi liczbami (np. „2–6 t/ha CaO zależnie od typu gleby i pH") PRZED teorią.
- **Sekcja FAQ** (jak szybko działa wapnowanie / czy przewapnowanie szkodzi / jak czytać pH z badania gleby / kiedy stosować) + **schema FAQPage** (RankMath).
- **schema HowTo** dla procedury doboru dawki (pH→typ gleby→dawka).
- **Tabela dawek spięta z produktami AGRIA** (Agrobielik 70/90, węglanowe, dolomit) — CaO/reaktywność/frakcja/dawka, z linkami do kart produktów (nowe URL-e `/wapno-nawozowe-rolnictwo/...`).
- Sezonowość (wiosna/jesień), interpretacja badania gleby, ew. infografika decyzyjna.
- Zachowaj ton MASTER_PROMPT. Draft do akceptu Janka PRZED publikacją.
- Po publikacji: `index-submit` tego URL, zanotuj datę → pomiar GSC za 4–8 tyg.

### KROK 2 — Content jesienny rolnictwo (sezon IX–XI, ~6 tyg. wyprzedzenia)
2–3 poradniki long-tail informacyjne pod frazy z KR (kiedy stosować / ile na ha / typy wapna / wapno a magnez), zoptymalizowane pod PAA + AI Overview. Draft → akcept → publikacja → index-submit.

### KROK 3 — Oczyszczalnie / higienizacja osadów (B2B, wysoka wartość, winnable)
Landing „higienizacja osadów ściekowych wapnem" (palone mielone + Bielik, parametry, pH>12, dokumentacja przetargowa) + schema. Konkurencja słaba (wapno-info 15 fraz). Frazy: higienizacja osadów, neutralizator ścieków.

### KROK 4 — On-page stron pieniężnych
Bielik (`/wapno-hydratyzowane/bielik/`) pod „wapno hydratyzowane" (2400, long-tail+brand), Dolomit (`/wapno-nawozowe-rolnictwo/dolomit/`, 6600), kategoria Rolnictwo pod „wapno nawozowe" (1300): title/H1/opis + schema Product/BreadcrumbList.

### KROK 5 — GBP Tarnów (local_pack) + GEO structured.

## Do domknięcia niezależnie (nie blokuje treści)
- **Regresja nawigacji/filtra po rdzeniu URL** (Model A): puste archiwa Rybactwo/Sadownictwo/Hurtownie → 301 na /oferta/; filtr „Zastosowanie" na archiwum kategorii wygasza segmenty spoza archiwum. Decyzja Janka A/B (patrz koniec `PROJECT_STATE.md`): A = przepiąć menu+filtr na `/oferta/?pa_agria-segment=…`; B = płaskie URL-e produktów + wielokrotny `product_cat`. **Nie ruszać bez decyzji.**
- Reszta bloku A: nagłówki bezpieczeństwa (.htaccess, gotowe, czeka na „ok"), `product_cat` do sitemapy, P1-7 login „js" w schemie (moduł `seo-head`), widoczna treść „cement/kruszywo" (excerpt 321 + /oferta/ intro).

## Definicja „zrobione" dla tego wątku
Min. 1 strona przebudowana/opublikowana pod konkretną frazę z popytem, zgłoszona do indeksacji, z zapisaną datą i frazą-celem do pomiaru GSC. Wynik = obserwowalny ruch pozycji, nie „zrobione technicznie".
