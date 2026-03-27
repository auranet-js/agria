<?php
/**
 * AGRIA Liming Calculator — Bootstrap
 *
 * Shortcode: [agria_kalkulator_wapnowania]
 * AJAX:      agria_calc_liming
 */

defined( 'ABSPATH' ) || exit;

class Agria_Liming_Calculator {

    private static ?self $instance = null;

    public static function instance(): self {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->load_includes();

        add_shortcode( 'agria_kalkulator_wapnowania', [ $this, 'render_shortcode' ] );
        add_action( 'wp_ajax_agria_calc_liming',        [ $this, 'ajax_calculate' ] );
        add_action( 'wp_ajax_nopriv_agria_calc_liming', [ $this, 'ajax_calculate' ] );
    }

    private function load_includes(): void {
        $dir = __DIR__ . '/includes/';
        require_once $dir . 'class-iung-data.php';
        require_once $dir . 'class-product-matcher.php';
    }

    /**
     * Shortcode [agria_kalkulator_wapnowania]
     */
    public function render_shortcode( $atts ): string {
        $this->enqueue_assets();

        // Dane dla template
        $soil_categories = Agria_IUNG_Data::get_soil_categories();
        $carbon_classes  = Agria_IUNG_Data::get_carbon_classes();

        // Zakresy pH per kategoria (do JS)
        $ph_ranges = [];
        foreach ( array_keys( $soil_categories ) as $cat ) {
            $ph_ranges[ $cat ] = Agria_IUNG_Data::get_ph_range_arable( $cat );
        }
        $ph_grassland = Agria_IUNG_Data::get_ph_range_grassland();

        ob_start();
        include __DIR__ . '/templates/calculator-form.php';
        return ob_get_clean();
    }

    /**
     * Enqueue CSS + JS
     */
    private function enqueue_assets(): void {
        $base_url = AGRIA_PLUGIN_URL . 'modules/liming-calculator/assets/';
        $version  = AGRIA_VERSION;

        wp_enqueue_style(
            'agria-liming-calc',
            $base_url . 'calculator.css',
            [],
            $version
        );

        wp_enqueue_script(
            'agria-liming-calc',
            $base_url . 'calculator.js',
            [],
            $version,
            true // footer
        );
    }

    /**
     * AJAX handler — obliczenie dawki + produkty
     */
    public function ajax_calculate(): void {
        check_ajax_referer( 'agria_calc_nonce', 'nonce' );

        $usage_type = sanitize_text_field( $_POST['usage_type'] ?? '' );
        $ph         = sanitize_text_field( $_POST['ph'] ?? '' );

        if ( ! $usage_type || ! $ph ) {
            wp_send_json_error( 'Brak wymaganych parametrów.' );
        }

        // Walidacja pH (format: X.X)
        if ( ! preg_match( '/^\d\.\d$/', $ph ) ) {
            wp_send_json_error( 'Nieprawidłowy format pH.' );
        }

        $dose_data = null;

        if ( $usage_type === 'grunty_orne' ) {
            $soil_category = sanitize_text_field( $_POST['soil_category'] ?? '' );
            $allowed_cats  = array_keys( Agria_IUNG_Data::get_soil_categories() );

            if ( ! in_array( $soil_category, $allowed_cats, true ) ) {
                wp_send_json_error( 'Nieprawidłowa kategoria gleby.' );
            }

            $dose_data = Agria_IUNG_Data::lookup_arable( $soil_category, $ph );

        } elseif ( $usage_type === 'uzytki_zielone' ) {
            $carbon_content = sanitize_text_field( $_POST['carbon_content'] ?? '' );
            $allowed_carbon = array_keys( Agria_IUNG_Data::get_carbon_classes() );

            if ( ! in_array( $carbon_content, $allowed_carbon, true ) ) {
                wp_send_json_error( 'Nieprawidłowa klasa zawartości C.' );
            }

            $dose_data = Agria_IUNG_Data::lookup_grassland( $ph, $carbon_content );

        } else {
            wp_send_json_error( 'Nieprawidłowy typ użytku.' );
        }

        if ( null === $dose_data ) {
            wp_send_json_error( 'Brak danych dla podanych parametrów. Sprawdź wartość pH.' );
        }

        [ $cao_total, $cao_part1, $cao_part2 ] = $dose_data;

        // Produkty (tylko jeśli dawka > 0)
        $products = [];
        if ( $cao_total > 0 ) {
            $products = Agria_Product_Matcher::get_products( $cao_total, $cao_part1, $cao_part2 );
        }

        wp_send_json_success( [
            'cao_dose' => $cao_total,
            'part_1'   => $cao_part1,
            'part_2'   => $cao_part2,
            'products' => $products,
            'source'   => 'IUNG-PIB Puławy, Jadczyszyn 2021',
        ] );
    }
}

// Init
Agria_Liming_Calculator::instance();
