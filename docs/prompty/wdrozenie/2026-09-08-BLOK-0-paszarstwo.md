# Blok 0, wątek treści — opis kategorii `/paszarstwo/` (T-078)

> **Termin:** 12.09.2026 · **Projekt:** `agria` · **Zakres:** ryczałt R
> **Kontekst:** `docs/PLAN_WRZESIEN_2026.md` §3 · wzorzec wykonania: `data/T-092/wdrozenie-2026-09-04.md`
>
> Osobny wątek, bo to pisanie, nie konfiguracja — inny tryb pracy niż dwa pozostałe wątki bloku 0.

---

## 1. Po co, w liczbach z 07.09

| | wartość |
|---|---|
| `kreda pastewna` (DFS) | **2 400/mies**, rozkład **płaski** (IX–XI 1 900, szczyt V 2 900) |
| `kreda pastewna dla kur` | 1 600 · `kreda dla kur` 720 (**XI 1 000**) · `wapno dla kur niosek` 210 |
| klaster „kreda" w GSC (01.08–03.09) | **463 wyświetlenia, 0 kliknięć**, pozycja ważona **10,0** |
| kategoria `/paszarstwo/` | 123 wyświetlenia, 3 kliknięcia, poz. **12,5**, **421 słów**, tytuł **43 znaki** |
| karta `/paszarstwo/kreda-pastewna/` | 205 wyświetleń, **1 kliknięcie**, poz. 8,6, tytuł **22 znaki** |
| stary adres `/kreda-pastewna/` (301) | **253 wyświetlenia, poz. 11,0** — więcej niż kategoria i karta razem |

**Rozkład płaski ma konsekwencję:** ten klaster nie ma okna sezonowego, którego można nie zdążyć.
Robimy go teraz, bo jest duży i pusty, a nie dlatego, że ucieka.

⚠️ **Celem jest CTR, nie nowa widoczność.** 463 wyświetlenia przy pozycji 10,0 i zerze kliknięć
znaczy, że jesteśmy widoczni i nieklikani — dokładnie ta sama choroba, co w całym serwisie
(32 047 wyświetleń → 410 kliknięć, CTR 1,28%).

## 2. Co robimy

**Rozbudowa opisu taksonomii kategorii `/paszarstwo/`** — dokładnie tak, jak T-092 zrobił
z `/wapno-nawozowe-rolnictwo/` 04.09 (958 → ~5 700 znaków, 1 → 7 nagłówków H2, 3 → 5 linków
wewnętrznych, render 5 650 → 10 425 znaków).

Oś treści: **czym się różni kreda pastewna od nawozowej, komu i ile podawać.** Odbiorcą jest
hodowca — nioski, bydło, trzoda — nie rolnik od wapnowania pola. Inny język, inne jednostki
(procent w mieszance paszowej, nie tony na hektar).

Do wykorzystania: karty producentów z `/do-pobrania/`, karta #307 Kreda pastewna
(parametry zweryfikowane 24.08 we wszystkich czterech warstwach — **T-079 unieważnione, nie ma
tam błędu**), oraz cena `od 190 zł/t netto` z warunkiem dostawy.

**Poprawić też tytuł kategorii i karty** — 43 i **22 znaki** to za mało, żeby cokolwiek obiecać
w SERP-ie. ⚠️ Ale nie opieraj się na tezie, że sama długość tytułu robi CTR — crawl 07.09 to
**odrzucił** (tytuły <45 znaków: CTR 1,01%, ≥45 znaków: 1,16%, różnica w szumie). **Zacznij od
obejrzenia SERP-u** dla `kreda pastewna` i `kreda pastewna dla kur` — kto tam jest, co obiecuje
w tytule, czy jest featured snippet lub AI Overview. Dla huba taki pomiar wyjaśnił wszystko.

## 3. Trzy pułapki zmierzone przy T-092 — nie powtarzaj ich

1. **WP-CLI `term update` bez `--user` przepuszcza opis przez `wp_filter_kses`** i wycina tabele
   oraz nagłówki. Zapis szedł ostatecznie przez MCP `query_db_write`, który filtrów WP nie uruchamia.
2. **Kontener przewijania z T-044 tu nie działa** — render zjada `style` z `<div>` i zostawia go
   na `<table>`. Zostaje czyste `<table>` z motywowym `width:100%`.
3. **`lastmod` w sitemapie dla archiwum bierze się z produktów, nie z opisu** — po zmianie opisu
   data się nie ruszy, mimo wyczyszczenia cache Rank Matha. Nie traktuj tego jako błędu.

## 4. Czego nie robisz

- **Nie zakładasz nowych adresów.** Poradnik o kredzie (T-077) to osobna pozycja z terminem 30.09,
  a nowe adresy są warunkowane kontrolą indeksacji 15.09.
- **Nie ruszasz H1 ani struktury listingu produktów** — T-092 też ich nie ruszał.
- **Nie zmieniasz ceny** ani nie dodajesz drugiej kwoty; obowiązuje „jedna kwota `od X zł/t netto`
  na kartę, zawsze ze swoim warunkiem" (`FAKTY_KLIENTA.md`, decyzja Janka 19.08).

## 5. Zrobione =

Backup przed (`db_export`), render zweryfikowany **przeglądarką i `curl` z cache-bustem** — nie
odczytem z bazy, baseline GSC zapisany do `data/T-078/` przed wdrożeniem, cache Elementora
i sitemapy wyczyszczone, wiersz T-078 w rejestrze zamknięty w tym samym commicie z dowodem.
**Kontrola 14-dniowa** wpisana w terminarz na **26.09**, mierzona na frazach formowych klastra,
nie na frazie głównej.
