<?php
/**
 * Plugin Name:       Agria by Auranet
 * Plugin URI:        https://auranet.pl
 * Description:       Modular plugin for Agria website. Catalog mode, custom templates, product features and more.
 * Version:           1.1.0
 * Author:            Auranet
 * Author URI:        https://auranet.pl
 * Text Domain:       agria-auranet
 * Domain Path:       /languages
 * Requires at least: 6.0
 * Requires PHP:      8.0
 * WC requires at least: 7.0
 */

defined( 'ABSPATH' ) || exit;

// ── Stałe ────────────────────────────────────────────────────────────────────

define( 'AGRIA_VERSION',     '1.1.0' );
define( 'AGRIA_PLUGIN_FILE', __FILE__ );
define( 'AGRIA_PLUGIN_DIR',  plugin_dir_path( __FILE__ ) );
define( 'AGRIA_PLUGIN_URL',  plugin_dir_url( __FILE__ ) );
define( 'AGRIA_MODULES_DIR', AGRIA_PLUGIN_DIR . 'modules/' );

// ── Blok geograficzny ────────────────────────────────────────────────────────
// Ładowany od razu, nie przez autoloader modułów — ma odciąć ruch zanim
// WordPress zacznie cokolwiek renderować. Szczegóły w nagłówku pliku.

require_once AGRIA_PLUGIN_DIR . 'security-geoblock.php';

// ── Ekspozycja kont uzytkownikow ─────────────────────────────────────────────
// Blokada anonimowego odczytu /wp-json/wp/v2/users (T-029). Ladowana wczesnie,
// bo filtr rest_pre_dispatch musi stac przed obsluga zadania REST.

require_once AGRIA_PLUGIN_DIR . 'security-user-enum.php';

// ── Autoloader modułów ───────────────────────────────────────────────────────

/**
 * Ładuje wszystkie aktywne moduły z katalogu /modules/.
 * Każdy moduł to podkatalog z plikiem o tej samej nazwie co katalog.
 * Przykład: modules/catalog-mode/catalog-mode.php
 */
function agria_load_modules(): void {
    $modules = [
        'catalog-mode',
        'product-video',
        'scroll-to-top',
        'seo-head',
        'legacy-urls',
        // Kolejne moduły dodawaj tutaj:
        'liming-calculator',
        'inquiry-form',
        'call-bar',
        'plain-content-layout',
        // 'product-table',
        // 'calculators',
    ];

    foreach ( $modules as $module ) {
        $file = AGRIA_MODULES_DIR . $module . '/' . $module . '.php';
        if ( file_exists( $file ) ) {
            require_once $file;
        } else {
            if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
                error_log( "[Agria] Moduł nie znaleziony: $file" );
            }
        }
    }
}

add_action( 'plugins_loaded', 'agria_load_modules', 5 );

// ── Aktywacja / Deaktywacja ──────────────────────────────────────────────────

register_activation_hook( __FILE__, 'agria_plugin_activate' );
function agria_plugin_activate(): void {
    // Ustaw domyślne opcje przy pierwszej aktywacji
    if ( false === get_option( 'agria_catalog_mode_enabled' ) ) {
        add_option( 'agria_catalog_mode_enabled', '1' );
    }
    flush_rewrite_rules();
}

register_deactivation_hook( __FILE__, 'agria_plugin_deactivate' );
function agria_plugin_deactivate(): void {
    flush_rewrite_rules();
}
