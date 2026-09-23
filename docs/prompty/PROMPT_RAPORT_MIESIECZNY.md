# Prompt: raport miesięczny AGRIA — dowolny miesiąc

> **Jak używać:** w nowej sesji `cd ~/projekty/agria && claude` (także zdalnie) wklej jedną linię:
>
> `Przeczytaj docs/prompty/PROMPT_RAPORT_MIESIECZNY.md i zrób raport za <miesiąc RRRR>, stan na <DD.MM>.`
>
> Przykład: `… raport za wrzesień 2026, stan na 30.09.`
> Zastępuje `docs/raporty/PROMPT_RAPORT_M2_2026-07.md` (pisany pod lipiec, bez Ads, OLX i rozliczenia).
> **Wzorzec treści i tonu:** ostatni mail z raportem, który faktycznie poszedł do klienta (§1 pkt 4) —
> nie draft z repo, bo Janek poprawia maile przed wysyłką (sierpień: setup OLX 1 800 → 1 500 zł).

Poniżej `MIESIĄC` = miesiąc raportu, `STAN` = dzień, na który liczymy, `Mx` = numer miesiąca współpracy
(M1 = czerwiec 2026, więc wrzesień = M4, październik = M5).

---

## 0. Zasady nadrzędne

- **Wszystko idzie wyłącznie do Janka** (`~/bin/send-to-jan`, `js@auranet.com.pl`). Nigdy do klienta,
  nawet jeśli adresy Kasjana i Pawła są w kontekście. Janek wysyła sam ze swojej skrzynki.
- **„Zrobione” wyprowadzasz z commitów i z produkcji, nie z planu.** Każda liczba ma źródło: API, commit
  albo odczyt z serwera. Bez źródła — nie ma jej w raporcie.
- **Raport dotyczy tylko AGRII.** Faktura jest zbiorcza na ASEO (memory `project_agria_fakturowanie_przez_aseo`),
  ale w raporcie i w kosztach liczymy wyłącznie AGRIĘ.
- Sesja może być uruchomiona zdalnie, gdy Janek jest poza biurem — **nie zadawaj mu serii pytań.**
  Czego nie da się ustalić z repo, API i skrzynki, oznacz w drafcie `[DO POTWIERDZENIA: …]` i jedź dalej.

## 1. Wczytaj stan faktyczny

1. `CLAUDE.md` projektu i `~/.claude/projects/-home-host476470-projekty-agria/memory/MEMORY.md`. Obowiązkowo
   przeczytaj: `feedback_agria_no_self_criticism_built_site`, `feedback_agria_offer_mail_structure`,
   `feedback_agria_bez_zargonu_loco`, `feedback_agria_auranet_decyduje`, `feedback_agria_pawel_relacja_telefoniczna`,
   `feedback_gsc_ctr_z_poziomu_strony`, `project_agria_fakturowanie_przez_aseo`, `project_agria_dwie_warstwy_cen`.
2. `docs/REJESTR_ZOBOWIAZAN.md` — **DZIENNIK `Mx`** (co dostarczone, zakres R/P/W, godziny) i KOLEJKA.
3. Poprzedni raport: `docs/raporty/<RRRR-MM poprzedni>.md` i `…-mail.md` — czym się pochwaliliśmy
   i **co obiecaliśmy na MIESIĄC w sekcji „Plan na …”.**
4. Ostatni **wysłany** mail z raportem: `python3 ~/bin/claude-mail-fetch.py list | grep -i agria` →
   najnowszy „Podsumowanie prac …” → `fetch <id>`, czytaj `/tmp/claude-mails/<id>/body.txt`.
   Stamtąd bierzesz strukturę, ton, obietnice na MIESIĄC i **koszty zapowiedziane na MIESIĄC**.
5. Strona postępu dla klienta: `docs/raporty/postep-prac.html` (link AGRIA dostała w mailu:
   `https://auratest.pl/ag-postep-7f3c9d21e8b4a6f5/`).
6. `git log --since=<1. dzień MIESIĄCA> --until=<STAN +1> --pretty=format:'%ad %h %s' --date=short`
   i **skonfrontuj z dziennikiem** (zasada 5 rejestru). Commit bez wiersza w dzienniku albo wiersz
   bez commita — dopisz albo wyjaśnij, zanim cokolwiek policzysz.

## 2. Dane z API — świeży pull, nie liczby z notatek

Zapisz surowe odpowiedzi do `data/raport-<RRRR-MM>/`.

| Źródło | Jak | Uwagi |
|---|---|---|
| **GSC** | `scripts/gsc_pull.py` — przestaw `MONTHS` na MIESIĄC, poprzedni i ten sam miesiąc rok temu, **jeden przebieg** | Property URL-prefix `https://agria.pl/`. Dane kończą się ~3 dni przed dniem pulla — **napisz w raporcie, do którego dnia są**. CTR i kliknięcia licz **z poziomu strony**, nie z sumy zapytań (próg prywatności ukrywa większość). Frazy w TOP3/TOP10 tak jak w raporcie sierpniowym |
| **GSC indeks** | `scripts/gsc_inspect.py` na adresach zmienionych w MIESIĄCU | werdykt + data crawla |
| **GA4** | Data API, property `538301430`: sesje, sesje organiczne, zdarzenia `phone_click`, `form_submit`, `whatsapp_click` | porównaj z poprzednim miesiącem tym samym zapytaniem |
| **Google Ads** | API v25, CID `674-207-1446` (`scripts/google/_lib.py`, wzorce w `data/kontrole/*odczyt-ads*.md`): kliknięcia, koszt, konwersje per kampania, `search_term_view` | **cykl budżetu to 15.–15., nie miesiąc kalendarzowy** — wydatek podaj za MIESIĄC i osobno stan cyklu |
| **OLX** | `python3 scripts/olx/statystyki.py` + historia `data/olx/statystyki.json`, stan pakietu z `data/olx/monitor-log.json` | statystyki są kumulatywne — przyrost MIESIĄCA = różnica pomiarów z granic miesiąca |
| **Wizytówka Google** | `scripts/gbp_dump.py` / Performance API: połączenia, trasy, wejścia na stronę | Tarnów i Niedomice osobno |

## 3. Plan kontra wykonanie — rdzeń raportu

Zrób tabelę na ekran i do `PODSUMOWANIE_Mx_<RRRR-MM>.md`:

1. **W zakresie** — każdy punkt z „Planu na MIESIĄC” z ostatniego wysłanego maila: zrobione / częściowo / nie,
   z dowodem (commit, adres, pomiar). Niezrobione wprost, z powodem.
2. **Ponad zakres** — pozycje z dziennika, których w planie nie było.
3. **Godziny (tylko do wewnątrz):** suma zmierzonych w ryczałcie (R) i poza nim (P), plus lista pozycji
   bez godzin. Stawki godzinowej **nie liczymy w żadnym dokumencie dla klienta**.
4. **Koszty MIESIĄCA** — ze zapowiedzi w ostatnim mailu (dla września: 2 000 opieka + 1 200 budżet Ads +
   600 prowadzenie + 300 obsługa OLX = **4 100 zł netto**). Wszystko spoza tej listy, co mogłoby wejść
   na fakturę → `[DO POTWIERDZENIA]`, nie dopisuj sam.

## 4. Pliki wynikowe

1. **`docs/raporty/<RRRR-MM>.md`** — raport pełny, wewnętrzny: dane, dowody, korekty poprzednich liczb.
2. **`docs/raporty/<RRRR-MM>-mail.md`** — mail do Kasjana i Pawła w strukturze ostatniego wysłanego:
   wyniki z Google → zrobione na stronie → reklamy → OLX → (uczciwie o jednej rzeczy, jeśli coś nie wyszło)
   → plan na następny miesiąc → koszty MIESIĄCA i następnego. Prosto, dla zarządu; zero żargonu
   (`loco`, `CTR`, `LCP`, `indeksacja`, „kanibalizacja”), zero krytyki strony (zbudował ją Auranet),
   tryb oznajmujący. Budżet tylko miesięcznie, nigdy suma za okres.
3. **Strona postępu** — dopisz MIESIĄC do `docs/raporty/postep-prac.html` (grupy jak we wrześniu,
   godziny tak, bez stawek), przestaw kolejkę i „Czekamy na AGRIĘ”, zmień „Stan na”.
   Wdrożenie: `cp docs/raporty/postep-prac.html ~/domains/auratest.pl/public_html/ag-postep-7f3c9d21e8b4a6f5/index.html`
   i sprawdź curl-em, że w stronie jest **zero** „wewnętrzny” i „zł/h”.
   ⚠️ **Nie używaj `docs/postep/build_postep.py --deploy` do tej strony** — to wersja wewnętrzna,
   ma własny adres (incydent 04–23.09: nadpisała stronę klienta).
4. **Rejestr** — wiersz „Raport Mx” w dzienniku, nagłówek „Stan na”, zamknięte pozycje z dowodem.

## 5. Oddanie Jankowi

1. Treść maila **w czacie**, w całości (Do / Temat / treść), plus lista `[DO POTWIERDZENIA]`.
2. Ten sam mail do Janka: `~/bin/send-to-jan -s "AGRIA — raport <miesiąc> (draft do akceptu)" -B docs/raporty/<RRRR-MM>-mail.md`
   — w pierwszej linii body: link do strony postępu i lista punktów do potwierdzenia.
3. `git commit` + `git push` plików raportu (`[docs] raport Mx <miesiąc> …`).
4. **Nie wysyłasz niczego do klienta** i nie wystawiasz faktury. Proformę przygotowujesz tylko na wyraźne
   „wystaw fakturę” (globalny CLAUDE.md §10, memory `reference_fakturownia_api` — faktura zbiorcza ASEO).

## 6. Pułapki

- **GSC z opóźnieniem** — raport zrobiony 1–2 dnia miesiąca ma dane bez ostatnich 2–3 dni. Napisz to w mailu
  jednym zdaniem (jak w sierpniu), nie ukrywaj.
- **Liczby poprzedniego miesiąca się zmieniają** — GSC dojrzewa ~30 dni. Porównanie tylko z tego samego pulla.
- **Sezon** — szczyt rolniczy to sierpień, nie październik (memory `project_agria_sezon_sierpniowy`).
  Spadek wrzesień → październik to nie jest problem do tłumaczenia, tylko sezon; wypisuj serie z etykietami rok-miesiąc.
- **Ceny** — w mailu ceny orientacyjne z treści kart, nigdy ceny ofertownika.
- **Ads** — konwersja główna to połączenie, `form_submit` jest pomocnicza (T-110). Nie sumuj ich jako „zapytań” bez podziału.

## 7. Definition of done

- [ ] tabela plan vs wykonanie z dowodem przy każdym punkcie
- [ ] liczby z API zapisane w `data/raport-<RRRR-MM>/`, z datą pulla
- [ ] raport pełny, mail, podsumowanie w `docs/raporty/`
- [ ] strona postępu zaktualizowana i sprawdzona (zero „wewnętrzny”, zero „zł/h”)
- [ ] mail w czacie + draft wysłany do Janka przez `send-to-jan`
- [ ] commit + push
