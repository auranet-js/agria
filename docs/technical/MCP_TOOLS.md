# MCP Agria.pl — narzędzia dostępne dla Claude'a

> Lista narzędzi MCP serwera `Agria.pl` skonfigurowanych w środowisku Claude. Wszystkie read-only (na czas obecny).

---

## Dostęp i konfiguracja

MCP serwer: `Agria.pl` (zarejestrowany w `~/.claude.json` lub konfiguracji projektowej). Endpoint i klucz — w sesji operatora.

---

## Narzędzia

### `Agria.pl:status`
Zwraca: PHP version, WP version, WC version, server time, motyw, prefix DB.

**Użycie:** szybki health-check przed pracą.

```
Agria.pl:status  →  { php: "8.3.30", wp: "6.9.4", wc: "10.6.1", theme: "Agria By Auranet 2.0.0", ... }
```

### `Agria.pl:wc_products_list`
Lista wszystkich produktów WooCommerce.

**Parametry:**
- `limit` (int, default 50, max 200)
- `search` (string, filter po nazwie)
- `status` (string, default `publish`)

**Zwraca:** `{ count, products[] }` z `id`, `name`, `sku`, `status`, `modified`, `categories[]`.

### `Agria.pl:catalog_product`
Pełne dane produktu sparsowane pod format katalogu drukowanego.

**Parametry:** `product_id` (int) **LUB** `name` (string, exact/partial).

**Zwraca:** nazwa, krótki opis, długi opis, sekcje, tabela parametrów (15 wierszy: CaO, reaktywność, frakcja itp.), formy dostawy, kategorie.

**Użycie:** generowanie JSX dla każdej karty katalogu.

### `Agria.pl:wc_product`
Surowe dane WooCommerce po ID — meta, atrybuty, pricing, warianty.

### `Agria.pl:query_db`
SELECT na bazie WP (read-only).

**Użycie:** custom raporty, debugowanie metadanych, audyt SEO (np. ile produktów ma alty obrazów).

### `Agria.pl:read_file`
Czyta plik z `wp-content/` (plugins, themes, uploads, mu-plugins).

**Użycie:** weryfikacja konfiguracji motywu, debugging.

### `Agria.pl:list_dir`
Lista plików w katalogu wewnątrz `wp-content/`.

### `Agria.pl:plugins_list`
Lista wszystkich aktywnych wtyczek WP z wersjami.

**Użycie:** audyt bezpieczeństwa, weryfikacja konfliktów, planowanie update'ów.

### `Agria.pl:wc_options`
Czyta opcje WooCommerce z `wp_options`.

**Użycie:** sprawdzenie konfiguracji wysyłki, podatków, walut, checkoutu.

### `Agria.pl:stats`
Statystyki sklepu: produkty po statusie/typie, zamówienia po statusie, kategorie, ostatnie zamówienia, najlepsi klienci.

---

## Czego MCP nie umie (na dziś)

- ❌ Zapis do bazy (UPDATE / INSERT / DELETE)
- ❌ Modyfikacja plików (write)
- ❌ Uruchamianie WP-CLI z poziomu MCP

**Dla operacji zapisu:** Auranet używa WP-CLI po SSH lub pluginu (np. WP REST API + własny endpoint), poza MCP.

---

## Patterny użycia

### Audit produktów pod SEO

```
1. Agria.pl:wc_products_list (limit: 100)
2. Dla każdego produktu: Agria.pl:catalog_product (product_id)
3. Analiza: długość opisu, czy ma parametry, czy ma kategorie, czy ma SKU
4. Zapis findings do docs/seo/SEO_AUDIT_RESULTS.md
```

### Generacja JSX dla katalogu drukowanego

```
1. Lista 17 produktów z PRINT_CATALOG_SPEC.md
2. Dla każdego: Agria.pl:catalog_product (name)
3. Mapowanie do struktury PROD (jak w AGRIA_DUPLIKUJ_AGROBIELIK70_v3.jsx)
4. Wygenerowanie 17 plików .jsx do assets/jsx/
```

### Weryfikacja bezpieczeństwa

```
1. Agria.pl:plugins_list
2. Krzyżowo z bazą CVE (wpscan / wpvulndb)
3. Lista wtyczek do update'u w docs/technical/SECURITY_AUDIT.md
```
