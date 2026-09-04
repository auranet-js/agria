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
        require_once $dir . 'class-mg-data.php';
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
        $mg_groups       = Agria_Mg_Data::get_groups();
        $mg_ranges       = Agria_Mg_Data::get_target_ranges();

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

        $dose_data  = null;
        $soil_group = ''; // grupa mechaniczna gleby do oceny magnezu

        if ( $usage_type === 'grunty_orne' ) {
            $soil_category = sanitize_text_field( $_POST['soil_category'] ?? '' );
            $allowed_cats  = array_keys( Agria_IUNG_Data::get_soil_categories() );

            if ( ! in_array( $soil_category, $allowed_cats, true ) ) {
                wp_send_json_error( 'Nieprawidłowa kategoria gleby.' );
            }

            $dose_data  = Agria_IUNG_Data::lookup_arable( $soil_category, $ph );
            $soil_group = $soil_category; // ścieżka orna bierze grupę z kroku 2

        } elseif ( $usage_type === 'uzytki_zielone' ) {
            $carbon_content = sanitize_text_field( $_POST['carbon_content'] ?? '' );
            $allowed_carbon = array_keys( Agria_IUNG_Data::get_carbon_classes() );

            if ( ! in_array( $carbon_content, $allowed_carbon, true ) ) {
                wp_send_json_error( 'Nieprawidłowa klasa zawartości C.' );
            }

            $dose_data = Agria_IUNG_Data::lookup_grassland( $ph, $carbon_content );

            // Użytki zielone — grupa gleby z osobnego pola (krok 3c)
            $mg_soil = sanitize_text_field( $_POST['mg_soil_group'] ?? '' );
            if ( isset( Agria_Mg_Data::THRESHOLDS[ $mg_soil ] ) ) {
                $soil_group = $mg_soil;
            }

        } else {
            wp_send_json_error( 'Nieprawidłowy typ użytku.' );
        }

        if ( null === $dose_data ) {
            wp_send_json_error( 'Brak danych dla podanych parametrów. Sprawdź wartość pH.' );
        }

        [ $cao_total, $cao_part1, $cao_part2 ] = $dose_data;

        // --- Magnez (pole nieobowiązkowe) ---
        $mg_raw      = str_replace( ',', '.', sanitize_text_field( $_POST['mg_value'] ?? '' ) );
        $mg_declared = ( '' !== $mg_raw && is_numeric( $mg_raw ) && (float) $mg_raw >= 0 );

        $mg          = null;
        $mg_products = [];
        $cao_topup   = null;

        if ( $mg_declared ) {
            if ( '' === $soil_group ) {
                // Użytki zielone bez wskazanej grupy — pokazujemy prośbę o krok 3c
                $mg = [ 'no_group' => true ];
            } else {
                $mg_value  = (float) $mg_raw;
                $range     = Agria_Mg_Data::target_range( $soil_group );

                // Blokada: zbadana zawartość przycinana do maksimum dla tej gleby
                if ( $mg_value > $range['max'] ) {
                    $mg_value = $range['max'];
                }

                $target_raw = str_replace( ',', '.', sanitize_text_field( $_POST['mg_target'] ?? '' ) );
                $target     = ( '' !== $target_raw && is_numeric( $target_raw ) ) ? (float) $target_raw : null;

                $mg = Agria_Mg_Data::assess( $soil_group, $mg_value, $target );

                if ( $mg && $mg['needs'] ) {
                    $mg_products = Agria_Product_Matcher::get_mg_products( $mg['dose_mgo'], (float) $cao_total );
                    $cao_topup   = Agria_Product_Matcher::get_cao_topup();
                }
            }
        }

        // Tabela magnezowa zastępuje klasyczny dobór wg CaO — jak w prototypie
        $mg_table_shown = ! empty( $mg_products );

        $products = [];
        if ( $cao_total > 0 && ! $mg_table_shown ) {
            $products = Agria_Product_Matcher::get_products( $cao_total, $cao_part1, $cao_part2, $mg_declared );
        }

        wp_send_json_success( [
            'cao_dose'    => $cao_total,
            'part_1'      => $cao_part1,
            'part_2'      => $cao_part2,
            'products'    => $products,
            'mg'          => $mg,
            'mg_products' => $mg_products,
            'cao_topup'   => $cao_topup,
            'source'      => 'IUNG-PIB Puławy, Jadczyszyn 2021',
        ] );
    }
}

// Init
Agria_Liming_Calculator::instance();
