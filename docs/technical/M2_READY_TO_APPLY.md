# Pakiet gotowy-do-wdrożenia — T-178 (techniczne P0) + T-013 (SKU)

> Data: 2026-06-15. Przygotowane SOLO (MCP agria read-only). Wszystko poniżej wymaga **zapisu na produkcji** — WP Admin / FTP nazwa.pl / WP-CLI. Stan zweryfikowany live przez MCP.
>
> **Zasada:** nic z tego nie wykonano — to artefakty do wklejenia, gdy będzie dostęp. Każda pozycja ma jawną blokadę.

---

## 1. Schema — usunięcie „My Blog" (P0-2)

**Stan live (zweryfikowany):** „My Blog" siedzi w 3 miejscach:
- `rank-math-options-titles` → `knowledgegraph_name = "My Blog"`
- `rank-math-options-titles` → `website_name = "My Blog"`
- `woocommerce_pos_store_name = "My Blog"` (wtyczka WC POS)

`knowledgegraph_type` = `company` (dobrze — schema Organization).

### Do wdrożenia (WP Admin → RankMath → Titles & Meta → Local SEO / Global Meta)

| Pole | Wartość docelowa |
|---|---|
| Knowledge Graph Type | Company *(już ustawione)* |
| Knowledge Graph Name | `AGRIA Sp. z o.o.` |
| Website Name | `AGRIA` |
| Website Alternate Name | `AGRIA Sp. z o.o.` |

WC POS store name (WP Admin → POS settings lub `wp option update woocommerce_pos_store_name "AGRIA Sp. z o.o."`).

### ⚠️ Blokada — dane firmowe od AGRIA (do pełnego Organization/LocalBusiness)

Do kompletnej schemy potrzebne (P0-2 w `ONPAGE_BACKLOG_M2-M6`):
- **NIP, REGON** (do `Organization` + faktur) — pozyskać od AGRIA lub z GUS BIR (mam dostęp, `~/secrets/gus/`).
- **Adres centrali** — wg kontekstu projektu: ul. Warsztatowa 5, 33-100 Tarnów — **do potwierdzenia**.
- **Telefon główny, godziny otwarcia** — do potwierdzenia (P2-3 w backlogu).
- Logo (URL) — RankMath pobiera z ustawień; sprawdzić czy ustawione.

**Minimalny fix bez czekania na dane:** sama zmiana Knowledge Graph Name + Website Name z „My Blog" na „AGRIA" / „AGRIA Sp. z o.o." — usuwa zawstydzający placeholder w schemie. LocalBusiness ×2 (Niedomice + Radgoszcz) — po danych.

---

## 2. Meta-opis strony — „cement i kruszywo" (NOWE, do decyzji)

**Stan live:** `blogdescription` = „Wapno nawozowe, cement i kruszywo dla rolnictwa, rybactwa, budownictwa. Stabilne dostawy od 1989r."

**Problem:** wg decyzji katalogowej 2026-06-15 AGRIA **nie sprzedaje cementu ani kruszywa** (oferta = 19 produktów). Opis strony (używany m.in. w schemie/tytułach) reklamuje produkty spoza oferty.

**Propozycja:** `Wapno nawozowe, hydratyzowane i palone dla rolnictwa, rybactwa, oczyszczalni i budownictwa. Stabilne dostawy od 1989 r.`

**⚠️ Decyzja Janka** — czy zmieniamy (i czy ten wariant). Zapis: WP Admin → Ustawienia → Ogólne (lub `wp option update blogdescription "..."`).

---

## 3. .htaccess — przekierowania 301 `/kategoria-produktu/*` (P0-3)

**Cel:** stare URL-e kategorii produktów (`/kategoria-produktu/<slug>/`) → aktualne (Premmerce zmienił strukturę). Odzysk link juice.

### ⚠️ Blokada podwójna
1. **Dostęp FTP/SFTP nazwa.pl** — brak.
2. **Inwentarz mapowań** — trzeba potwierdzić aktualne URL-e każdej kategorii (np. `/kategoria-produktu/rolnictwo-wapno-nawozowe/` → `/wapno-nawozowe-rolnictwo/`?). Do zrobienia: lista 8 kategorii stare→nowe przed bulk.

### Wzorzec reguły (do uzupełnienia mapowań, test na 10 URL przed wdrożeniem)
```apache
# AGRIA — 301 legacy product-category → nowe URL (Premmerce). Wstawić PRZED regułami WP.
<IfModule mod_rewrite.c>
RewriteEngine On
# Przykład per kategoria (uzupełnić realnymi slugami po inwentaryzacji):
RewriteRule ^kategoria-produktu/rolnictwo(.*)$ /wapno-nawozowe-rolnictwo/ [R=301,L]
RewriteRule ^kategoria-produktu/oczyszczalnie(.*)$ /oczyszczalnie/ [R=301,L]
# ... pozostałe kategorie
# Fallback (jeśli 1:1 mapowanie slugów): zdjęcie prefiksu
# RewriteRule ^kategoria-produktu/(.+)$ /$1 [R=301,L]
</IfModule>
```
**Uwaga:** fallback „zdjęcie prefiksu" tylko jeśli slug kategorii się nie zmienił — inaczej 301 prowadzi do 404. Stąd wymóg inwentaryzacji.

---

## 4. .htaccess — nagłówki bezpieczeństwa (P1-1)

Gotowe do wklejenia (FTP, sekcja `.htaccess` w public_html). Blokada: dostęp FTP.

```apache
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
  # HSTS — włączyć dopiero gdy pewne, że całość serwowana po HTTPS (nazwa.pl ma cert):
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
</IfModule>
```
**Uwaga HSTS:** włączyć świadomie (po HSTS przeglądarka wymusza HTTPS na rok). Reszta nagłówków bezpieczna od razu.

---

## 5. Premmerce Permalink Manager DOM-XSS (P0-5)

**Stan:** podatność DOM-XSS we wcześniejszej wersji (audyt 19.05). To podatność **client-side** — serwerowy WAF łapie ją słabo.

**Działanie:**
1. **Sprawdzić aktualną wersję wtyczki** (WP Admin → Wtyczki) i czy wyszedł patch 2.3.12+ — jeśli tak: **aktualizacja = najczystszy fix** (priorytet).
2. Jeśli brak patcha: monitoring release'ów vendora + ewentualnie reguła Cloudflare/WAF na podejrzane parametry w URL. Bez Cloudflare przed nazwa.pl — ograniczone pole.

**Blokada:** WP Admin (sprawdzenie wersji + update) + ew. Cloudflare.

---

## 6. SKU bulk dla 19 produktów (T-013)

**Konwencja:** `PRODUCT_DATA_MAPPING.md` (AGR-001…). Zmapowane do realnych ID live (zweryfikowane MCP).

| ID | Produkt | SKU |
|---|---|---|
| 310 | Wapno nawozowe tlenkowe Agrobielik 70 | `AGR-001` |
| 311 | Wapno nawozowe tlenkowe Agrobielik 90 | `AGR-002` |
| 312 | Wapno nawozowe tlenkowe Oxyfertil 90 | `AGR-003` |
| 313 | Wapno nawozowe tlenkowe zawierające magnez | `AGR-004` |
| 308 | Mieszanka tlenkowo-węglanowa | `AGR-005` |
| 315 | Wapno nawozowe węglanowe bez magnezu — Odmiana 04 | `AGR-006` |
| 316 | Wapno nawozowe węglanowe bez magnezu — Odmiana 05 | `AGR-007` |
| 314 | Wapno nawozowe węglanowe bez magnezu granulowane | `AGR-008` |
| 318 | Wapno nawozowe węglanowe zawierające magnez — Odmiana 04 | `AGR-009` |
| 319 | Wapno nawozowe węglanowe zawierające magnez — Odmiana 05 | `AGR-010` |
| 317 | Wapno nawozowe węglanowe zawierające magnez granulowane | `AGR-011` |
| 302 | Dolomit | `AGR-012` |
| 305 | Kreda nawozowa granulowana | `AGR-013` |
| 306 | Kreda nawozowa sypka | `AGR-014` |
| 307 | Kreda pastewna | `AGR-015` |
| 304 | Kreda malarska | `AGR-016` |
| 320 | Wapno palone mielone wysokoreaktywne | `AGR-017` |
| 309 | Wapno hydratyzowane Bielik | `AGR-018` |
| 303 | Kreda czarna (jeziorna) z kwasami humusowymi | `AGR-019` ⚠️ |

**⚠️ #303 = decyzja:** w mappingu Kreda czarna była „usunięta", ale decyzja 2026-06-15 ją przywróciła. Proponuję `AGR-019` (numer wolny — pozycje cement/kruszywo/wapno drogowe z mappingu **anulowane**, nie dodajemy). Potwierdź numer.

### Skrypt WP-CLI (gotowy, po SSH/WP-CLI na nazwa.pl)
```bash
# AGRIA — bulk SKU. wp wc product update synchronizuje też lookup table WC.
declare -A SKU=(
  [310]=AGR-001 [311]=AGR-002 [312]=AGR-003 [313]=AGR-004 [308]=AGR-005
  [315]=AGR-006 [316]=AGR-007 [314]=AGR-008 [318]=AGR-009 [319]=AGR-010
  [317]=AGR-011 [302]=AGR-012 [305]=AGR-013 [306]=AGR-014 [307]=AGR-015
  [304]=AGR-016 [320]=AGR-017 [309]=AGR-018 [303]=AGR-019
)
for id in "${!SKU[@]}"; do
  wp wc product update "$id" --sku="${SKU[$id]}" --user=<ADMIN_LOGIN>
done
# Weryfikacja:
wp wc product list --fields=id,name,sku --user=<ADMIN_LOGIN>
```
**Blokada:** dostęp SSH/WP-CLI nazwa.pl (lub przez WP Admin ręcznie per produkt — 19 szt).

---

## Podsumowanie blokad (co odblokuje co)

| Potrzebne od Ciebie / AGRIA | Odblokowuje |
|---|---|
| **WP Admin** (RankMath, Wtyczki, Ustawienia) | §1 schema, §2 meta-opis, §5 wersja Premmerce |
| **FTP/SFTP nazwa.pl** | §3 301, §4 nagłówki bezpieczeństwa |
| **SSH/WP-CLI nazwa.pl** | §6 SKU bulk (albo ręcznie w WP Admin) |
| **Dane firmowe AGRIA** (NIP, REGON, adres, godziny) | pełna schema Organization/LocalBusiness §1 |
| **Inwentarz URL kategorii** (stare→nowe) | §3 mapowania 301 |
| **Decyzje Janka:** meta-opis (§2), SKU #303 (§6) | wdrożenie §2, §6 |
