<?php
/**
 * GeoIP blok krajow — Auranet 2026-08-14
 *
 * KOPIA REFERENCYJNA. Plik zywy: wp-content/plugins/agria-by-auranet/security-geoblock.php
 * na produkcji (nazwa.pl, server371853). Ladowany przez `require_once` w naglowku
 * agria-by-auranet.php, PRZED autoloaderem modulow — ma odciac ruch, zanim WordPress
 * zacznie cokolwiek renderowac.
 *
 * ⚠️ Reinstalacja lub nadpisanie wtyczki KASUJE blokade bez sladu (objaw: Singapur
 * wraca do GA4). Po kazdej aktualizacji wtyczki sprawdz, czy plik i `require_once` sa.
 *
 * Wpuszcza Europe (EU/EEA + UK + CH + UA) oraz zaufane boty/LLM; reszte -> 403.
 * Wzorzec przeniesiony z victorini2025/inc/security-geoblock.php (2026-07-02)
 * i aseo-security-geoblock.php (2026-08-11) — oba na nazwa.pl, oba zweryfikowane.
 *
 * POWOD (dane GA4, 01-14.08.2026): 82 ze 123 sesji z Singapuru (67%), zaangazowanie
 * 0,0%, sygnatura 1280x1200/English. Polska — 4 sesje. Te same boty generuja 30 odslon
 * bledu 404 (demo-produkty motywu, stare adresy DuoCMS). GA4 nie nadaje sie do oceny
 * kampanii Google Ads, dopoki ten ruch nie zniknie.
 *
 * Baza: wp-content/uploads/complianz/maxmind/GeoLite2-Country.mmdb — utrzymywana
 * i odswiezana przez Complianz (8,6 MB, stan 13.08). Nie dublujemy wlasnej kopii.
 * Czytnik: natywne rozszerzenie PHP `maxminddb` — potwierdzone na serwerze 14.08
 * (PHP 8.3.33, testy 8.8.8.8->US, 188.146.0.1->PL, 203.116.1.1->SG).
 *
 * TRYB: ENFORCE — realny 403 dla ruchu spoza Europy.
 * Kill-switch awaryjny: define('AGRIA_GEOBLOCK_OFF', true) w wp-config.php.
 * Powrot do obserwacji: $enforce = false (wtedy tylko log, zero blokad).
 * FAIL-OPEN: brak bazy / blad czytnika / nieznany kraj -> przepuszcza.
 *
 * ZASIEG: dziala na ruchu docierajacym do PHP (dynamika + cache-miss). Strony
 * serwowane z cache edge CDN nazwa.pl NIE docieraja do origin, wiec tam blok sie
 * nie odpala (tak samo jak .htaccess). Pelne odciecie = tylko edge (Cloudflare).
 */

defined( 'ABSPATH' ) || exit;

if ( defined( 'AGRIA_GEOBLOCK_OFF' ) && AGRIA_GEOBLOCK_OFF ) {
	return;
}

if ( ! function_exists( 'agria_geoblock' ) ) {
	/**
	 * Blokuje zadania spoza Europy zanim WordPress wyrenderuje strone.
	 */
	function agria_geoblock(): void {
		// ── PRZELACZNIK EGZEKUCJI ── false = dry-run (log), true = realny 403
		$enforce = true;

		if ( php_sapi_name() === 'cli' ) {
			return;
		}
		if ( defined( 'DOING_CRON' ) && DOING_CRON ) {
			return;
		}

		// Sciezki zawsze przepuszczane (panel, REST, cron, nasz MCP).
		$uri = $_SERVER['REQUEST_URI'] ?? '';
		if ( preg_match( '#(/wp-admin|/wp-login\.php|/wp-json|/wp-cron\.php|/mcp/)#i', $uri ) ) {
			return;
		}

		// Zaufane boty / LLM — zawsze wpuszczaj (SEO, AI visibility, weryfikacja reklam).
		// AdsBot-Google MUSI tu byc: bez dostepu do landingow Google odrzuca reklamy.
		$ua        = $_SERVER['HTTP_USER_AGENT'] ?? '';
		$good_bots = array(
			'Googlebot', 'Storebot-Google', 'Google-InspectionTool', 'Google-Extended',
			'AdsBot-Google', 'AdsBot-Google-Mobile', 'Google-Safety', 'Mediapartners-Google',
			'bingbot', 'BingPreview', 'Slurp', 'DuckDuckBot', 'Applebot', 'YandexBot',
			'facebookexternalhit', 'facebookcatalog', 'LinkedInBot', 'Twitterbot',
			'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-Web', 'anthropic-ai',
			'PerplexityBot', 'Amazonbot', 'meta-externalagent',
		);
		foreach ( $good_bots as $bot ) {
			if ( '' !== $ua && stripos( $ua, $bot ) !== false ) {
				return;
			}
		}

		// IP klienta (REMOTE_ADDR — niespoofowalny; zweryfikowane 14.08, ze to realny klient).
		$ip = $_SERVER['REMOTE_ADDR'] ?? '';
		if ( '' === $ip ) {
			return;
		}
		// Prywatne / zarezerwowane -> przepuszczaj.
		if ( ! filter_var( $ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE ) ) {
			return;
		}

		$db = WP_CONTENT_DIR . '/uploads/complianz/maxmind/GeoLite2-Country.mmdb';
		if ( ! is_readable( $db ) || ! class_exists( 'MaxMind\\Db\\Reader' ) ) {
			return; // fail-open
		}

		static $europa = array(
			'PL', 'DE', 'CZ', 'SK', 'AT', 'NL', 'BE', 'FR', 'LU', 'DK', 'SE', 'NO', 'FI', 'IE', 'GB', 'CH',
			'IT', 'ES', 'PT', 'HU', 'RO', 'BG', 'HR', 'SI', 'LT', 'LV', 'EE', 'GR', 'CY', 'MT', 'IS', 'LI', 'UA',
		);

		try {
			$reader = new MaxMind\Db\Reader( $db );
			$rec    = $reader->get( $ip );
			$reader->close();
		} catch ( Throwable $e ) {
			return; // fail-open
		}

		$cc = $rec['country']['iso_code'] ?? '';
		if ( '' === $cc ) {
			return; // nieznany kraj -> nie blokuj
		}
		if ( in_array( $cc, $europa, true ) ) {
			return; // Europa -> OK
		}

		if ( ! $enforce ) {
			error_log( "[Agria geoblock] DRY-RUN: zablokowalbym $ip ($cc) na $uri" );
			return;
		}

		// ── spoza Europy -> 403 ──
		if ( ! headers_sent() ) {
			http_response_code( 403 );
			header( 'Content-Type: text/plain; charset=utf-8' );
			header( 'Cache-Control: no-store, no-cache, must-revalidate, max-age=0' );
		}
		exit( 'Forbidden' );
	}
}

agria_geoblock();
