<?php
/**
 * Plugin Name: AGRIA Ofertownik by Auranet
 * Description: Wycena zamowienia z transportem z wlasciwego zakladu — narzedzie wewnetrzne dzialu handlowego.
 * Version:     0.7.0
 * Author:      Auranet
 * Text Domain: agria-ofertownik
 * Requires PHP: 8.0
 *
 * Wtyczka celowo ODDZIELNA od `agria-by-auranet` — patrz docs/specs/2026-08-18-ofertownik-design.md §2.
 * Nadpisanie tamtej wtyczki kasuje geoblok bez sladu; kazde wgranie jej to okazja do tego.
 * Ofertownik obok redukuje liczbe takich okazji do zera i daje sie wylaczyc jednym klikiem.
 *
 * CENY NIE TRAFIAJA DO POL WOOCOMMERCE. Zmierzone 22.08.2026: `_price` wycieka publicznie
 * przez Store API i przez JSON-LD Rank Matha. ADR docs/decyzje/2026-08-22-audyt-wycieku-cen-werdykt.md.
 */

defined( 'ABSPATH' ) || exit;

define( 'AGRIA_OF_VERSION', '0.7.0' );
define( 'AGRIA_OF_DIR', plugin_dir_path( __FILE__ ) );
define( 'AGRIA_OF_URL', plugin_dir_url( __FILE__ ) );

// Uprawnienie do ofertownika. Musi byc widoczne TAKZE na froncie — ekran /wycena/ nie jest w panelu.
define( 'AGRIA_OF_CAP', 'manage_woocommerce' );

require_once AGRIA_OF_DIR . 'inc/db.php';
require_once AGRIA_OF_DIR . 'inc/ustawienia.php';
require_once AGRIA_OF_DIR . 'inc/cennik.php';
require_once AGRIA_OF_DIR . 'inc/zaklady.php';
require_once AGRIA_OF_DIR . 'inc/odleglosci.php';
require_once AGRIA_OF_DIR . 'inc/wycena.php';
require_once AGRIA_OF_DIR . 'inc/koszyk.php';
require_once AGRIA_OF_DIR . 'inc/gus.php';
require_once AGRIA_OF_DIR . 'inc/ekran.php';
require_once AGRIA_OF_DIR . 'inc/oferty.php';
require_once AGRIA_OF_DIR . 'inc/pulpit.php';
if ( is_admin() ) {
	require_once AGRIA_OF_DIR . 'inc/admin.php';
	require_once AGRIA_OF_DIR . 'inc/panel-zaklady.php';
	require_once AGRIA_OF_DIR . 'inc/zestawienie.php';
}

/**
 * Bramka ekranu /wycena/.
 *
 * NIE uzywamy `auth_redirect()`. Ta funkcja waliduje ciasteczko `secure_auth`, ktore przy
 * wymuszonym SSL w panelu wydawane jest TYLKO dla `/wp-admin` — front go nie dostaje.
 * Skutek zmierzony 25.08.2026 na stagingu: handlowiec zalogowany w panelu („Witaj, testclaude")
 * byl odbijany z `/wycena/` na `wp-login.php?...&reauth=1` mimo waznej sesji.
 * `is_user_logged_in()` czyta ciasteczko `logged_in`, ktore obowiazuje na calej witrynie.
 *
 * @return bool true = wpuszczamy; false = przekierowanie juz wyslane, wywolujacy ma zakonczyc.
 */
function agria_of_wpuszczamy(): bool {
	if ( is_user_logged_in() && current_user_can( AGRIA_OF_CAP ) ) {
		return true;
	}
	if ( is_user_logged_in() ) {
		wp_die( 'To narzędzie jest dla działu handlowego AGRII. Twoje konto nie ma do niego dostępu.',
			'Brak dostępu', [ 'response' => 403 ] );
	}
	$wroc = ( is_ssl() ? 'https://' : 'http://' ) . ( $_SERVER['HTTP_HOST'] ?? '' ) . ( $_SERVER['REQUEST_URI'] ?? '/wycena/' );
	wp_safe_redirect( wp_login_url( $wroc ) );
	return false;
}

register_activation_hook( __FILE__, 'agria_of_aktywacja' );

function agria_of_aktywacja(): void {
	agria_of_db_utworz_tabele();
	agria_of_db_utworz_tabele_geo();
	agria_of_ustawienia_zasiej();
	add_option( 'agria_of_wersja_db', AGRIA_OF_VERSION );
}

/**
 * Migracja schematu przy podbiciu wersji — bez tego aktualizacja wtyczki przez wgranie plikow
 * (a tak wlasnie ja aktualizujemy) nie odpalilaby `register_activation_hook`.
 */
add_action( 'plugins_loaded', function (): void {
	if ( get_option( 'agria_of_wersja_db' ) !== AGRIA_OF_VERSION ) {
		agria_of_db_utworz_tabele();
		agria_of_db_utworz_tabele_geo();
		update_option( 'agria_of_wersja_db', AGRIA_OF_VERSION );
	}
}, 5 );
