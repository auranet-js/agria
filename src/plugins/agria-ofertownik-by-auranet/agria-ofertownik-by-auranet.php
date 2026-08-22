<?php
/**
 * Plugin Name: AGRIA Ofertownik by Auranet
 * Description: Wycena zamowienia z transportem z wlasciwego zakladu — narzedzie wewnetrzne dzialu handlowego.
 * Version:     0.1.0
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

define( 'AGRIA_OF_VERSION', '0.1.0' );
define( 'AGRIA_OF_DIR', plugin_dir_path( __FILE__ ) );
define( 'AGRIA_OF_URL', plugin_dir_url( __FILE__ ) );

require_once AGRIA_OF_DIR . 'inc/db.php';
require_once AGRIA_OF_DIR . 'inc/ustawienia.php';
require_once AGRIA_OF_DIR . 'inc/cennik.php';
require_once AGRIA_OF_DIR . 'inc/zaklady.php';
if ( is_admin() ) {
	require_once AGRIA_OF_DIR . 'inc/admin.php';
}

register_activation_hook( __FILE__, 'agria_of_aktywacja' );

function agria_of_aktywacja(): void {
	agria_of_db_utworz_tabele();
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
		update_option( 'agria_of_wersja_db', AGRIA_OF_VERSION );
	}
}, 5 );
