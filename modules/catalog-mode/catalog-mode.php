<?php
/**
 * Moduł: Catalog Mode
 *
 * Zamienia WooCommerce w tryb katalogu:
 *  - Ukrywa ceny na listingach i stronach produktu
 *  - Usuwa przyciski "Dodaj do koszyka" i "Kup teraz"
 *  - Wyłącza koszyk, checkout i zamówienia
 *  - Wyłącza rejestrację (tylko dla klientów)
 *  - Przekierowuje /koszyk/ i /zamowienie/ → strona główna
 *  - Dodaje przycisk CTA "Zapytaj o cenę" z mailto lub formularzem
 *  - Ustawienia w WP Admin → Agria → Tryb katalogu
 */

defined( 'ABSPATH' ) || exit;

class Agria_Catalog_Mode {

    private static ?self $instance = null;
    private bool $enabled;
    private string $cta_type;      // 'mailto' | 'form' | 'phone'
    private string $cta_email;
    private string $cta_phone;
    private string $cta_label;

    public static function instance(): self {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->enabled   = (bool) get_option( 'agria_catalog_mode_enabled', '1' );
        $this->cta_type  = get_option( 'agria_catalog_cta_type', 'mailto' );
        $this->cta_email = get_option( 'agria_catalog_cta_email', get_option( 'admin_email' ) );
        $this->cta_phone = get_option( 'agria_catalog_cta_phone', '' );
        $this->cta_label = get_option( 'agria_catalog_cta_label', 'Zapytaj o cenę' );

        $this->init_hooks();
    }

    // ── Hooks ────────────────────────────────────────────────────────────────

    private function init_hooks(): void {

        // Panel admina — ustawienia
        add_action( 'admin_menu',    [ $this, 'register_admin_menu' ] );
        add_action( 'admin_init',    [ $this, 'register_settings' ] );
        add_action( 'admin_notices', [ $this, 'admin_notice_active' ] );

        if ( ! $this->enabled ) {
            return;
        }

        // ── Ceny ─────────────────────────────────────────────────────────────
        add_filter( 'woocommerce_get_price_html',               '__return_empty_string' );
        add_filter( 'woocommerce_variable_price_html',          '__return_empty_string' );
        add_filter( 'woocommerce_variable_sale_price_html',     '__return_empty_string' );
        add_filter( 'woocommerce_sale_price_html',              '__return_empty_string' );
        add_filter( 'woocommerce_price_html',                   '__return_empty_string' );
        add_filter( 'woocommerce_empty_price_html',             '__return_empty_string' );
        add_filter( 'woocommerce_free_price_html',              '__return_empty_string' );

        // ── Koszyk — wyłącz całkowicie ─────────────────────────────────────
        add_filter( 'woocommerce_is_purchasable',               '__return_false' );
        add_filter( 'woocommerce_add_to_cart_validation',       '__return_false' );

        // ── Przyciski ─────────────────────────────────────────────────────
        // Usuń domyślny przycisk na listingu
        remove_action( 'woocommerce_after_shop_loop_item', 'woocommerce_template_loop_add_to_cart' );
        // Usuń domyślny przycisk na stronie produktu
        remove_action( 'woocommerce_single_product_summary', 'woocommerce_template_single_add_to_cart', 30 );

        // Dodaj CTA na listing
        add_action( 'woocommerce_after_shop_loop_item', [ $this, 'render_cta_loop' ], 10 );
        // Dodaj CTA na stronę produktu
        add_action( 'woocommerce_single_product_summary', [ $this, 'render_cta_single' ], 30 );

        // ── Koszyk, checkout, moje konto → przekierowania ─────────────────
        add_action( 'template_redirect', [ $this, 'redirect_restricted_pages' ] );

        // ── Usuń elementy koszyka z menu i widgetów ───────────────────────
        add_filter( 'woocommerce_widget_cart_item_visible',     '__return_false' );
        add_filter( 'woocommerce_add_to_cart_fragments',        '__return_empty_array' );

        // ── Ukryj status/meta zakupowe w e-mailach i panelu ───────────────
        add_filter( 'woocommerce_order_button_html',            '__return_empty_string' );

        // ── CSS — usuń style koszyka ───────────────────────────────────────
        add_action( 'wp_enqueue_scripts', [ $this, 'enqueue_catalog_styles' ] );

        // ── Wyłącz rejestrację klientów (zostaw admina) ───────────────────
        add_filter( 'woocommerce_process_registration_errors', [ $this, 'block_customer_registration' ] );

        // ── Ukryj zmienną cenę przy wyborze wariantu (JS) ─────────────────
        add_filter( 'woocommerce_available_variation', [ $this, 'clean_variation_data' ] );
    }

    // ── CTA Buttons ──────────────────────────────────────────────────────────

    public function render_cta_loop(): void {
        global $product;
        echo $this->get_cta_html( $product, 'loop' );
    }

    public function render_cta_single(): void {
        global $product;
        echo $this->get_cta_html( $product, 'single' );
    }

    private function get_cta_html( $product, string $context ): string {
        if ( ! $product ) return '';

        $label    = esc_html( $this->cta_label );
        $name     = esc_html( $product->get_name() );
        $sku      = esc_html( $product->get_sku() );
        $css_class = 'agria-cta-btn agria-cta-' . $context;

        if ( $this->cta_type === 'mailto' && $this->cta_email ) {
            $subject = rawurlencode( 'Zapytanie o produkt: ' . $name . ( $sku ? " ($sku)" : '' ) );
            $href    = 'mailto:' . antispambot( $this->cta_email ) . '?subject=' . $subject;
            return sprintf(
                '<a href="%s" class="%s">%s</a>',
                esc_attr( $href ),
                esc_attr( $css_class ),
                $label
            );
        }

        if ( $this->cta_type === 'phone' && $this->cta_phone ) {
            $phone = preg_replace( '/\s+/', '', $this->cta_phone );
            return sprintf(
                '<a href="tel:%s" class="%s">%s</a>',
                esc_attr( $phone ),
                esc_attr( $css_class ),
                $label
            );
        }

        // Fallback — link do strony kontakt
        $contact_url = get_permalink( get_page_by_path( 'kontakt' ) ) ?: home_url( '/kontakt/' );
        $url = add_query_arg( [
            'produkt' => urlencode( $name ),
            'sku'     => urlencode( $sku ),
        ], $contact_url );

        return sprintf(
            '<a href="%s" class="%s">%s</a>',
            esc_url( $url ),
            esc_attr( $css_class ),
            $label
        );
    }

    // ── Przekierowania ───────────────────────────────────────────────────────

    public function redirect_restricted_pages(): void {
        if ( is_admin() ) return;

        $restricted = [
            is_cart(),
            is_checkout(),
            is_account_page() && ! is_user_logged_in(),
        ];

        if ( in_array( true, $restricted, true ) ) {
            wp_safe_redirect( home_url( '/' ) );
            exit;
        }
    }

    // ── Warianty — usuń dane cenowe z AJAX response ───────────────────────

    public function clean_variation_data( array $data ): array {
        $data['price_html']           = '';
        $data['display_price']        = '';
        $data['display_regular_price']= '';
        return $data;
    }

    // ── CSS ──────────────────────────────────────────────────────────────────

    public function enqueue_catalog_styles(): void {
        wp_add_inline_style( 'woocommerce-general', $this->get_catalog_css() );

        // Inline style dla przycisku CTA
        wp_add_inline_style( 'woocommerce-general', $this->get_cta_css() );
    }

    private function get_catalog_css(): string {
        return '
            /* Agria Catalog Mode — ukryj elementy zakupowe */
            .cart-contents,
            .woocommerce-cart-form,
            .woocommerce-checkout,
            .widget_shopping_cart,
            .woocommerce-mini-cart,
            .cart-widget,
            .add_to_cart_button,
            .single_add_to_cart_button,
            .wc-proceed-to-checkout,
            .woocommerce-variation-price,
            .price del,
            .price ins,
            .woocommerce ul.products li.product .price,
            .woocommerce div.product p.price,
            .woocommerce div.product span.price {
                display: none !important;
            }
        ';
    }

    private function get_cta_css(): string {
        return '
            /* Agria CTA Button */
            .agria-cta-btn {
                display: inline-block;
                background-color: #2d7a2d;
                color: #ffffff !important;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: 600;
                text-decoration: none;
                text-align: center;
                transition: background-color 0.2s ease;
                margin-top: 8px;
                width: 100%;
                box-sizing: border-box;
            }
            .agria-cta-btn:hover {
                background-color: #1f5c1f;
                color: #ffffff !important;
            }
            .agria-cta-single {
                margin-top: 15px;
                margin-bottom: 15px;
                display: block;
                max-width: 300px;
            }
        ';
    }

    // ── Blokada rejestracji klientów ─────────────────────────────────────────

    public function block_customer_registration( \WP_Error $errors ): \WP_Error {
        if ( ! current_user_can( 'manage_options' ) ) {
            $errors->add( 'registration_disabled', __( 'Rejestracja jest wyłączona.', 'agria-auranet' ) );
        }
        return $errors;
    }

    // ── Panel administracyjny ─────────────────────────────────────────────────

    public function register_admin_menu(): void {
        add_menu_page(
            'Agria',
            'Agria',
            'manage_options',
            'agria-settings',
            [ $this, 'render_admin_page' ],
            'dashicons-admin-generic',
            58
        );
    }

    public function register_settings(): void {
        register_setting( 'agria_catalog_mode', 'agria_catalog_mode_enabled',  [ 'type' => 'boolean', 'default' => 1 ] );
        register_setting( 'agria_catalog_mode', 'agria_catalog_cta_type',      [ 'type' => 'string',  'default' => 'mailto' ] );
        register_setting( 'agria_catalog_mode', 'agria_catalog_cta_email',     [ 'type' => 'string',  'default' => get_option( 'admin_email' ) ] );
        register_setting( 'agria_catalog_mode', 'agria_catalog_cta_phone',     [ 'type' => 'string',  'default' => '' ] );
        register_setting( 'agria_catalog_mode', 'agria_catalog_cta_label',     [ 'type' => 'string',  'default' => 'Zapytaj o cenę' ] );
    }

    public function admin_notice_active(): void {
        if ( $this->enabled ) {
            echo '<div class="notice notice-info"><p>';
            echo '<strong>Agria:</strong> WooCommerce działa w trybie katalogu. Ceny i koszyk są ukryte.';
            echo ' <a href="' . esc_url( admin_url( 'admin.php?page=agria-settings' ) ) . '">Ustawienia →</a>';
            echo '</p></div>';
        }
    }

    public function render_admin_page(): void {
        if ( ! current_user_can( 'manage_options' ) ) return;
        ?>
        <div class="wrap">
            <h1>Agria <small style="font-size:13px; color:#666;">by Auranet v<?php echo AGRIA_VERSION; ?></small></h1>

            <h2 class="nav-tab-wrapper">
                <a class="nav-tab nav-tab-active">Tryb katalogu</a>
            </h2>

            <form method="post" action="options.php" style="max-width:600px; margin-top:20px;">
                <?php settings_fields( 'agria_catalog_mode' ); ?>

                <table class="form-table" role="presentation">

                    <tr>
                        <th scope="row">Tryb katalogu</th>
                        <td>
                            <label>
                                <input type="checkbox" name="agria_catalog_mode_enabled" value="1"
                                    <?php checked( get_option( 'agria_catalog_mode_enabled' ), '1' ); ?>>
                                Włącz tryb katalogu (ukrywa ceny, koszyk, checkout)
                            </label>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Etykieta przycisku CTA</th>
                        <td>
                            <input type="text" name="agria_catalog_cta_label"
                                value="<?php echo esc_attr( get_option( 'agria_catalog_cta_label', 'Zapytaj o cenę' ) ); ?>"
                                class="regular-text">
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Typ CTA</th>
                        <td>
                            <?php $cta_type = get_option( 'agria_catalog_cta_type', 'mailto' ); ?>
                            <label style="display:block; margin-bottom:6px;">
                                <input type="radio" name="agria_catalog_cta_type" value="mailto"
                                    <?php checked( $cta_type, 'mailto' ); ?>>
                                E-mail (mailto:)
                            </label>
                            <label style="display:block; margin-bottom:6px;">
                                <input type="radio" name="agria_catalog_cta_type" value="phone"
                                    <?php checked( $cta_type, 'phone' ); ?>>
                                Telefon (tel:)
                            </label>
                            <label style="display:block;">
                                <input type="radio" name="agria_catalog_cta_type" value="contact"
                                    <?php checked( $cta_type, 'contact' ); ?>>
                                Link do strony /kontakt/ (z parametrami produktu)
                            </label>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Adres e-mail</th>
                        <td>
                            <input type="email" name="agria_catalog_cta_email"
                                value="<?php echo esc_attr( get_option( 'agria_catalog_cta_email', get_option( 'admin_email' ) ) ); ?>"
                                class="regular-text">
                            <p class="description">Używany gdy typ CTA = E-mail</p>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Numer telefonu</th>
                        <td>
                            <input type="text" name="agria_catalog_cta_phone"
                                value="<?php echo esc_attr( get_option( 'agria_catalog_cta_phone', '' ) ); ?>"
                                class="regular-text"
                                placeholder="+48 123 456 789">
                            <p class="description">Używany gdy typ CTA = Telefon</p>
                        </td>
                    </tr>

                </table>

                <?php submit_button( 'Zapisz ustawienia' ); ?>
            </form>

            <hr>
            <h3>Aktywne moduły</h3>
            <table class="widefat" style="max-width:600px;">
                <thead><tr><th>Moduł</th><th>Status</th></tr></thead>
                <tbody>
                    <tr>
                        <td>Tryb katalogu</td>
                        <td><?php echo get_option( 'agria_catalog_mode_enabled' ) ? '<span style="color:green">✓ Aktywny</span>' : '<span style="color:#888">— Wyłączony</span>'; ?></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <?php
    }
}

// Inicjalizuj moduł
Agria_Catalog_Mode::instance();
