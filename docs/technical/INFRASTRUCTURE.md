# Infrastruktura techniczna agria.pl

> Stan z MCP `Agria.pl:status` na 2026-05-19.

---

## Stack

| Warstwa | Wartość |
|---------|---------|
| Hosting | nazwa.pl, serwer `server371853.nazwa.pl` |
| PHP | 8.3.30 |
| WordPress | 6.9.4 |
| WooCommerce | 10.6.1 |
| Motyw | `Agria By Auranet 2.0.0` (własny, dziecko Hello Elementor) |
| Page builder | Elementor Pro |
| Baza | MySQL/MariaDB, prefix `wpfz_` |

---

## Domena

- Główna: **agria.pl** (HTTPS, certyfikat Let's Encrypt — do potwierdzenia)
- Aliasy: do sprawdzenia (np. `www.agria.pl` redirect na bez www lub odwrotnie)

---

## Dostępy (placeholdery — uzupełnia operator lokalnie, NIE w repo!)

⚠️ **Sekrety nie idą do repo.** Operator trzyma je w 1Password / własnym vaulcie.

| Co | Status | Gdzie trzymane |
|----|--------|----------------|
| WordPress admin (rola Administrator) | wymagane | 1Password Auranet |
| FTP / SFTP nazwa.pl | wymagane | 1Password Auranet |
| phpMyAdmin / SSH | nice-to-have | 1Password Auranet |
| Google Search Console | wymagane | konto Google Auranet |
| Google Analytics 4 | wymagane | konto Google Auranet |
| Google Tag Manager | wymagane | konto Google Auranet |
| Google Business Profile (Niedomice + Radgoszcz) | wymagane | konto Google Auranet |
| Google Ads | opcjonalne | po akceptacji budżetu |
| MCP `Agria.pl` | działa | klucz w konfiguracji MCP klienta Claude |

---

## Backup

| Warstwa | Częstotliwość | Lokalizacja | Status |
|---------|---------------|-------------|--------|
| WP + DB | tygodniowo | nazwa.pl (auto?) | do weryfikacji |
| Off-site (Auranet) | tygodniowo | Auranet S3 / lokalne | do skonfigurowania |
| Backup przed update | przed każdym update WP/WC/pluginów | lokalnie + S3 | procedura w toku |

---

## Cache i wydajność

- **Cache pluginu:** do sprawdzenia (WP Super Cache / W3 Total Cache / LiteSpeed Cache?)
- **CDN:** brak / Cloudflare? — do weryfikacji
- **Object cache (Redis/Memcached):** prawdopodobnie brak na nazwa.pl
- **Image optimization:** do weryfikacji (Smush / ShortPixel / WebP plugin?)

**Plan:** w pierwszym miesiącu po podpisaniu umowy 2000 PLN — weryfikacja i optymalizacja.

---

## Bezpieczeństwo

- Wtyczka security: do sprawdzenia (Wordfence / Solid Security / Sucuri?)
- Login URL: czy jest zmieniony (nie `/wp-admin/`)?
- 2FA na kontach admin: do wdrożenia
- Limit prób logowania: do wdrożenia
- Backup-na-żądanie przed każdym update'em: standard Auranet

---

## Issue list (z audytu / wstępnego przeglądu)

⏳ Do uzupełnienia po audycie.

---

## Procedura update'u

1. **Snapshot pełny** (WP + DB) przed update'em → S3.
2. **Update na staging** (jeśli istnieje) lub local Docker.
3. **Test** kluczowych flow: strona główna, produkt, kategoria, formularz, koszyk (jeśli aktywny), checkout.
4. **Update na produkcji** w oknie niskiego ruchu (np. wtorek 22:00).
5. **Smoke test** po update'cie.
6. **Rollback gotowy** w razie problemu (snapshot z punktu 1).
