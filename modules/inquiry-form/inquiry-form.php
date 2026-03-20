<?php
/**
 * Moduł: Inquiry Form v2 (Formularz zapytań i zamówień próbek)
 *
 * Shortcode: [agria_inquiry_form]
 *  - Na stronie produktu (WC / CPT): auto-fill nazwy + formy dostawy
 *  - Na osobnej stronie (/zamow/): dropdown ze wszystkimi produktami
 *  - AJAX submit, reCAPTCHA v3, email do handlowca + autoresponder do klienta
 *  - Zapis zgłoszeń jako CPT agria_inquiry (historia w adminie)
 *
 * Wrzuć do: wp-content/plugins/agria-by-auranet/modules/inquiry-form/inquiry-form.php
 * Dodaj 'inquiry-form' do tablicy $modules w agria-by-auranet.php
 */

defined( 'ABSPATH' ) || exit;

class Agria_Inquiry_Form {

    private static ?self $instance = null;
    private string $recaptcha_site_key;
    private string $recaptcha_secret_key;

    public static function instance(): self {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->recaptcha_site_key   = get_option( 'agria_recaptcha_site_key', '' );
        $this->recaptcha_secret_key = get_option( 'agria_recaptcha_secret_key', '' );

        add_action( 'init', [ $this, 'register_inquiry_cpt' ] );
        add_shortcode( 'agria_inquiry_form', [ $this, 'render_shortcode' ] );
        add_action( 'wp_ajax_agria_inquiry_submit',        [ $this, 'handle_submit' ] );
        add_action( 'wp_ajax_nopriv_agria_inquiry_submit', [ $this, 'handle_submit' ] );
        add_action( 'admin_init', [ $this, 'register_settings' ] );
        add_filter( 'manage_agria_inquiry_posts_columns',  [ $this, 'inquiry_columns' ] );
        add_action( 'manage_agria_inquiry_posts_custom_column', [ $this, 'inquiry_column_data' ], 10, 2 );
    }

    // ══════════════════════════════════════════════════════════════════════════
    // CPT: Zgłoszenia
    // ══════════════════════════════════════════════════════════════════════════

    public function register_inquiry_cpt(): void {
        register_post_type( 'agria_inquiry', [
            'labels' => [
                'name'               => 'Zgłoszenia',
                'singular_name'      => 'Zgłoszenie',
                'menu_name'          => 'Zgłoszenia',
                'all_items'          => 'Wszystkie zgłoszenia',
                'search_items'       => 'Szukaj zgłoszeń',
                'not_found'          => 'Brak zgłoszeń',
                'not_found_in_trash' => 'Brak zgłoszeń w koszu',
            ],
            'public'              => false,
            'show_ui'             => true,
            'show_in_menu'        => 'agria-settings',
            'supports'            => [ 'title' ],
            'capability_type'     => 'post',
            'map_meta_cap'        => true,
            'exclude_from_search' => true,
            'publicly_queryable'  => false,
            'has_archive'         => false,
        ] );

        register_post_status( 'inquiry_new', [
            'label'                     => 'Nowe',
            'public'                    => false,
            'show_in_admin_all_list'    => true,
            'show_in_admin_status_list' => true,
            'label_count'               => _n_noop( 'Nowe <span class="count">(%s)</span>', 'Nowe <span class="count">(%s)</span>' ),
        ] );
        register_post_status( 'inquiry_contacted', [
            'label'                     => 'Skontaktowano',
            'public'                    => false,
            'show_in_admin_all_list'    => true,
            'show_in_admin_status_list' => true,
            'label_count'               => _n_noop( 'Skontaktowano <span class="count">(%s)</span>', 'Skontaktowano <span class="count">(%s)</span>' ),
        ] );
        register_post_status( 'inquiry_closed', [
            'label'                     => 'Zamknięte',
            'public'                    => false,
            'show_in_admin_all_list'    => true,
            'show_in_admin_status_list' => true,
            'label_count'               => _n_noop( 'Zamknięte <span class="count">(%s)</span>', 'Zamknięte <span class="count">(%s)</span>' ),
        ] );
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Kolumny admina
    // ══════════════════════════════════════════════════════════════════════════

    public function inquiry_columns( array $columns ): array {
        return [
            'cb'          => $columns['cb'],
            'title'       => 'Zgłoszenie',
            'inq_type'    => 'Typ',
            'inq_product' => 'Produkt',
            'inq_contact' => 'Kontakt',
            'inq_phone'   => 'Telefon',
            'inq_status'  => 'Status',
            'date'        => 'Data',
        ];
    }

    public function inquiry_column_data( string $column, int $post_id ): void {
        $meta = fn( $k ) => get_post_meta( $post_id, $k, true );
        switch ( $column ) {
            case 'inq_type':
                echo $meta( '_inquiry_type' ) === 'probka' ? '📦 Próbka' : '📋 Oferta';
                break;
            case 'inq_product':
                echo esc_html( $meta( '_product_name' ) );
                break;
            case 'inq_contact':
                echo esc_html( $meta( '_full_name' ) );
                $c = $meta( '_company' );
                if ( $c ) echo '<br><small>' . esc_html( $c ) . '</small>';
                break;
            case 'inq_phone':
                $ph = $meta( '_phone' );
                echo '<a href="tel:' . esc_attr( $ph ) . '">' . esc_html( $ph ) . '</a>';
                break;
            case 'inq_status':
                $s = get_post_status( $post_id );
                $map = [
                    'inquiry_new'       => '<span style="color:#e67e22;font-weight:600;">● Nowe</span>',
                    'inquiry_contacted' => '<span style="color:#2d7a2d;font-weight:600;">● Skontaktowano</span>',
                    'inquiry_closed'    => '<span style="color:#888;">● Zamknięte</span>',
                    'publish'           => '<span style="color:#e67e22;font-weight:600;">● Nowe</span>',
                ];
                echo $map[ $s ] ?? esc_html( $s );
                break;
        }
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Ustawienia
    // ══════════════════════════════════════════════════════════════════════════

    public function register_settings(): void {
        register_setting( 'agria_catalog_mode', 'agria_inquiry_email',      [ 'type' => 'string', 'default' => '' ] );
        register_setting( 'agria_catalog_mode', 'agria_inquiry_cc_email',   [ 'type' => 'string', 'default' => '' ] );
        register_setting( 'agria_catalog_mode', 'agria_recaptcha_site_key', [ 'type' => 'string', 'default' => '' ] );
        register_setting( 'agria_catalog_mode', 'agria_recaptcha_secret_key',[ 'type' => 'string', 'default' => '' ] );

        // ── Sekcja: Formularz ──
        add_settings_section( 'agria_inquiry_section', 'Formularz zapytań',
            function() { echo '<p>Konfiguracja formularza zamówień i próbek.</p>'; },
            'agria-settings'
        );

        add_settings_field( 'agria_inquiry_email', 'E-mail odbiorcy', function() {
            $val = get_option( 'agria_inquiry_email', '' );
            $fb  = get_option( 'agria_catalog_cta_email', get_option( 'admin_email' ) );
            printf( '<input type="email" name="agria_inquiry_email" value="%s" class="regular-text" placeholder="%s"><p class="description">Domyślnie: %s</p>',
                esc_attr( $val ), esc_attr( $fb ), esc_html( $fb ) );
        }, 'agria-settings', 'agria_inquiry_section' );

        add_settings_field( 'agria_inquiry_cc_email', 'CC (kopia)', function() {
            printf( '<input type="email" name="agria_inquiry_cc_email" value="%s" class="regular-text" placeholder="opcjonalnie">',
                esc_attr( get_option( 'agria_inquiry_cc_email', '' ) ) );
        }, 'agria-settings', 'agria_inquiry_section' );

        // ── Sekcja: reCAPTCHA ──
        add_settings_section( 'agria_recaptcha_section', 'reCAPTCHA v3',
            function() { echo '<p>Zabezpieczenie formularzy. <a href="https://www.google.com/recaptcha/admin" target="_blank">Zarządzaj kluczami →</a></p>'; },
            'agria-settings'
        );

        add_settings_field( 'agria_recaptcha_site_key', 'Klucz witryny (Site Key)', function() {
            printf( '<input type="text" name="agria_recaptcha_site_key" value="%s" class="regular-text">',
                esc_attr( get_option( 'agria_recaptcha_site_key', '' ) ) );
        }, 'agria-settings', 'agria_recaptcha_section' );

        add_settings_field( 'agria_recaptcha_secret_key', 'Tajny klucz (Secret Key)', function() {
            printf( '<input type="text" name="agria_recaptcha_secret_key" value="%s" class="regular-text">',
                esc_attr( get_option( 'agria_recaptcha_secret_key', '' ) ) );
        }, 'agria-settings', 'agria_recaptcha_section' );
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Kontekst produktu
    // ══════════════════════════════════════════════════════════════════════════

    private function get_product_context(): array {
        global $post, $product;
        $ctx = [ 'name' => '', 'id' => 0, 'type' => '', 'url' => '', 'forms' => [], 'is_product' => false ];

        if ( function_exists( 'is_product' ) && is_product() ) {
            if ( ! $product && $post ) $product = wc_get_product( $post->ID );
            if ( $product && is_a( $product, 'WC_Product' ) ) {
                $ctx = array_merge( $ctx, [
                    'name' => $product->get_name(), 'id' => $product->get_id(),
                    'type' => 'product', 'url' => get_permalink( $product->get_id() ),
                    'is_product' => true, 'forms' => $this->get_wc_product_forms( $product->get_id() ),
                ] );
            }
            return $ctx;
        }

        if ( $post && $post->post_type === 'produkt' && is_singular( 'produkt' ) ) {
            $ctx = array_merge( $ctx, [
                'name' => get_the_title( $post->ID ), 'id' => $post->ID,
                'type' => 'produkt', 'url' => get_permalink( $post->ID ),
                'is_product' => true, 'forms' => $this->get_cpt_product_forms( $post->ID ),
            ] );
            return $ctx;
        }

        if ( ! empty( $_GET['produkt'] ) ) {
            $ctx['name'] = sanitize_text_field( wp_unslash( $_GET['produkt'] ) );
        }
        return $ctx;
    }

    private function get_wc_product_forms( int $pid ): array {
        $raw = get_post_meta( $pid, '_agria_variants', true );
        if ( ! $raw ) return [];
        $variants = is_string( $raw ) ? json_decode( $raw, true ) : $raw;
        if ( ! is_array( $variants ) ) return [];
        $forms = [];
        foreach ( $variants as $v ) { if ( ! empty( $v['forma'] ) ) $forms[] = $v['forma']; }
        return array_values( array_unique( $forms ) );
    }

    private function get_cpt_product_forms( int $pid ): array {
        $count = (int) get_post_meta( $pid, 'dostepnosc', true );
        if ( $count < 1 ) return [];
        $forms = [];
        for ( $i = 0; $i < $count; $i++ ) {
            $f = get_post_meta( $pid, "dostepnosc_{$i}_forma_dostawy_wariant", true );
            if ( $f ) $forms[] = ucfirst( $f );
        }
        return array_values( array_unique( $forms ) );
    }

    private function get_all_products_data(): array {
        $products = [];
        if ( function_exists( 'wc_get_products' ) ) {
            $wc = get_posts( [ 'post_type' => 'product', 'post_status' => 'publish', 'numberposts' => -1, 'orderby' => 'title', 'order' => 'ASC' ] );
            foreach ( $wc as $p ) {
                $products[ $p->ID ] = [ 'title' => $p->post_title, 'forms' => $this->get_wc_product_forms( $p->ID ) ];
            }
        }
        $wc_titles = array_column( $products, 'title' );
        $cpt = get_posts( [ 'post_type' => 'produkt', 'post_status' => 'publish', 'numberposts' => -1, 'orderby' => 'title', 'order' => 'ASC' ] );
        foreach ( $cpt as $p ) {
            if ( in_array( $p->post_title, $wc_titles, true ) ) continue;
            $products[ $p->ID ] = [ 'title' => $p->post_title, 'forms' => $this->get_cpt_product_forms( $p->ID ) ];
        }
        return $products;
    }

    // ══════════════════════════════════════════════════════════════════════════
    // reCAPTCHA v3
    // ══════════════════════════════════════════════════════════════════════════

    private function has_recaptcha(): bool {
        return ! empty( $this->recaptcha_site_key ) && ! empty( $this->recaptcha_secret_key );
    }

    private function verify_recaptcha( string $token ): bool {
        if ( ! $this->has_recaptcha() ) return true;

        $resp = wp_remote_post( 'https://www.google.com/recaptcha/api/siteverify', [
            'body' => [
                'secret'   => $this->recaptcha_secret_key,
                'response' => $token,
                'remoteip' => $_SERVER['REMOTE_ADDR'] ?? '',
            ],
            'timeout' => 10,
        ] );

        if ( is_wp_error( $resp ) ) {
            if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) error_log( '[Agria reCAPTCHA] ' . $resp->get_error_message() );
            return true; // nie blokuj przy problemie z Google
        }

        $body = json_decode( wp_remote_retrieve_body( $resp ), true );
        if ( empty( $body['success'] ) ) return false;

        $score = (float) ( $body['score'] ?? 0 );
        if ( $score < 0.4 ) {
            if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) error_log( "[Agria reCAPTCHA] Low score: $score" );
            return false;
        }
        return true;
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Shortcode render
    // ══════════════════════════════════════════════════════════════════════════

    public function render_shortcode( $atts ): string {
        $atts = shortcode_atts( [
            'title'  => 'Zapytaj o ofertę lub zamów próbkę',
            'submit' => 'Wyślij zapytanie',
        ], $atts, 'agria_inquiry_form' );

        $ctx     = $this->get_product_context();
        $all     = $ctx['is_product'] ? [] : $this->get_all_products_data();
        $form_id = 'agria-inquiry-' . wp_rand( 1000, 9999 );
        $nonce   = wp_create_nonce( 'agria_inquiry_nonce' );
        $has_rc  = $this->has_recaptcha();

        ob_start();
        ?>
        <?php if ( $has_rc ) : ?>
        <script src="https://www.google.com/recaptcha/api.js?render=<?php echo esc_attr( $this->recaptcha_site_key ); ?>" async defer></script>
        <?php endif; ?>

        <div class="agria-inquiry-wrap" id="<?php echo esc_attr( $form_id ); ?>">
            <h3 class="agria-inquiry-title"><?php echo esc_html( $atts['title'] ); ?></h3>

            <form class="agria-inquiry-form" novalidate>
                <input type="hidden" name="action" value="agria_inquiry_submit">
                <input type="hidden" name="_nonce" value="<?php echo esc_attr( $nonce ); ?>">
                <input type="hidden" name="source_url" value="<?php echo esc_url( $ctx['url'] ?: get_permalink() ); ?>">
                <input type="hidden" name="recaptcha_token" value="">
                <div style="position:absolute;left:-9999px;" aria-hidden="true">
                    <input type="text" name="agria_website" tabindex="-1" autocomplete="off" value="">
                </div>

                <!-- Typ zapytania -->
                <div class="agria-field agria-field-radio">
                    <label class="agria-label">Typ zapytania <span class="agria-req">*</span></label>
                    <div class="agria-radio-group">
                        <label class="agria-radio-item agria-radio-active">
                            <input type="radio" name="inquiry_type" value="oferta" checked>
                            <span class="agria-radio-label">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                                Zapytaj o ofertę
                            </span>
                        </label>
                        <label class="agria-radio-item">
                            <input type="radio" name="inquiry_type" value="probka">
                            <span class="agria-radio-label">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
                                Zamów próbkę
                            </span>
                        </label>
                    </div>
                </div>

                <!-- Produkt -->
                <?php if ( $ctx['is_product'] ) : ?>
                    <input type="hidden" name="product_name" value="<?php echo esc_attr( $ctx['name'] ); ?>">
                    <input type="hidden" name="product_id" value="<?php echo esc_attr( $ctx['id'] ); ?>">
                    <div class="agria-field">
                        <label class="agria-label">Produkt</label>
                        <div class="agria-product-badge">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2d7a2d" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                            <?php echo esc_html( $ctx['name'] ); ?>
                        </div>
                    </div>
                <?php elseif ( $ctx['name'] ) : ?>
                    <input type="hidden" name="product_id" value="">
                    <div class="agria-field">
                        <label class="agria-label">Produkt <span class="agria-req">*</span></label>
                        <input type="text" name="product_name" value="<?php echo esc_attr( $ctx['name'] ); ?>" class="agria-input" required>
                    </div>
                <?php else : ?>
                    <div class="agria-field">
                        <label class="agria-label">Produkt <span class="agria-req">*</span></label>
                        <select name="product_name" class="agria-input agria-product-select" required>
                            <option value="">— Wybierz produkt —</option>
                            <?php foreach ( $all as $pid => $pdata ) : ?>
                                <option value="<?php echo esc_attr( $pdata['title'] ); ?>"
                                        data-forms="<?php echo esc_attr( wp_json_encode( $pdata['forms'] ) ); ?>">
                                    <?php echo esc_html( $pdata['title'] ); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>
                <?php endif; ?>

                <!-- Forma dostawy -->
                <div class="agria-field">
                    <label class="agria-label">Preferowana forma dostawy</label>
                    <select name="delivery_form" class="agria-input agria-delivery-select">
                        <option value="">— Wybierz formę —</option>
                        <?php
                        $forms = $ctx['is_product'] ? $ctx['forms'] : [];
                        if ( empty( $forms ) ) $forms = [ 'Big-bag', 'Worki', 'Luz', 'Inna' ];
                        foreach ( $forms as $f ) :
                        ?>
                            <option value="<?php echo esc_attr( $f ); ?>"><?php echo esc_html( $f ); ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>

                <!-- Ilość -->
                <div class="agria-field">
                    <label class="agria-label">Ilość orientacyjna</label>
                    <input type="text" name="quantity" class="agria-input" placeholder="np. 24t, 5 big-bagów, 100 worków 25 kg">
                </div>

                <hr class="agria-separator">

                <!-- Dane kontaktowe -->
                <div class="agria-grid">
                    <div class="agria-field">
                        <label class="agria-label">Imię i nazwisko <span class="agria-req">*</span></label>
                        <input type="text" name="full_name" class="agria-input" required>
                    </div>
                    <div class="agria-field">
                        <label class="agria-label">Firma / Gospodarstwo</label>
                        <input type="text" name="company" class="agria-input">
                    </div>
                    <div class="agria-field">
                        <label class="agria-label">Telefon <span class="agria-req">*</span></label>
                        <input type="tel" name="phone" class="agria-input" required placeholder="+48">
                    </div>
                    <div class="agria-field">
                        <label class="agria-label">E-mail <span class="agria-req">*</span></label>
                        <input type="email" name="email" class="agria-input" required>
                    </div>
                </div>

                <div class="agria-field">
                    <label class="agria-label">Miejscowość / Kod pocztowy</label>
                    <input type="text" name="location" class="agria-input" placeholder="np. Tarnów 33-100">
                </div>

                <div class="agria-field">
                    <label class="agria-label">Dodatkowe uwagi</label>
                    <textarea name="message" class="agria-input agria-textarea" rows="3" placeholder="Termin dostawy, szczególne wymagania, pytania..."></textarea>
                </div>

                <!-- RODO -->
                <div class="agria-field agria-field-checkbox">
                    <label class="agria-checkbox-label">
                        <input type="checkbox" name="rodo_consent" value="1" required>
                        <span>Wyrażam zgodę na przetwarzanie moich danych osobowych w celu obsługi zapytania.
                        <a href="/polityka-prywatnosci/" target="_blank" rel="noopener">Polityka prywatności</a>.</span>
                    </label>
                </div>

                <!-- Submit -->
                <div class="agria-field">
                    <button type="submit" class="agria-submit-btn">
                        <span class="agria-btn-text"><?php echo esc_html( $atts['submit'] ); ?></span>
                        <span class="agria-btn-loading" style="display:none;">
                            <svg width="20" height="20" viewBox="0 0 24 24" class="agria-spinner"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" stroke-dasharray="31.4" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" dur="0.8s" from="0 12 12" to="360 12 12" repeatCount="indefinite"/></circle></svg>
                            Wysyłanie...
                        </span>
                    </button>
                </div>

                <?php if ( $has_rc ) : ?>
                <div class="agria-recaptcha-info">
                    Formularz chroniony przez reCAPTCHA Google.
                    <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Prywatność</a> &middot;
                    <a href="https://policies.google.com/terms" target="_blank" rel="noopener">Warunki</a>
                </div>
                <?php endif; ?>

                <!-- Komunikaty -->
                <div class="agria-msg agria-msg-success" style="display:none;" role="alert">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d7a2d" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                    <div>
                        <strong>Dziękujemy! Otrzymaliśmy Twoje zapytanie.</strong><br>
                        Nasz handlowiec skontaktuje się z Tobą w ciągu 1 dnia roboczego.<br>
                        <small>Potwierdzenie wysłaliśmy na podany adres e-mail.</small>
                    </div>
                </div>
                <div class="agria-msg agria-msg-error" style="display:none;" role="alert">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#c0392b" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
                    <div><strong>Błąd wysyłania.</strong> Spróbuj ponownie lub zadzwoń: <a href="tel:+48605335559">+48 605 335 559</a></div>
                </div>
                <div class="agria-msg agria-msg-captcha" style="display:none;" role="alert">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#e67e22" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                    <div><strong>Weryfikacja nie powiodła się.</strong> Odśwież stronę i spróbuj ponownie.</div>
                </div>
            </form>
        </div>

        <style>
        .agria-inquiry-wrap{max-width:640px;margin:0 auto;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
        .agria-inquiry-title{font-size:22px;font-weight:700;color:#1a1a1a;margin:0 0 24px;padding-bottom:12px;border-bottom:3px solid #2d7a2d}
        .agria-field{margin-bottom:16px}.agria-label{display:block;font-size:13px;font-weight:600;color:#333;margin-bottom:5px}
        .agria-req{color:#c0392b}
        .agria-input{width:100%;padding:10px 12px;border:1px solid #ccc;border-radius:4px;font-size:14px;color:#333;background:#fff;transition:border-color .2s;box-sizing:border-box}
        .agria-input:focus{outline:none;border-color:#2d7a2d;box-shadow:0 0 0 2px rgba(45,122,45,.15)}
        .agria-textarea{resize:vertical;min-height:70px}select.agria-input{cursor:pointer}
        .agria-radio-group{display:flex;gap:10px}.agria-radio-item{flex:1;cursor:pointer}.agria-radio-item input{display:none}
        .agria-radio-label{display:flex;align-items:center;gap:8px;padding:12px 16px;border:2px solid #ddd;border-radius:6px;font-size:14px;font-weight:500;color:#555;transition:all .2s;justify-content:center}
        .agria-radio-item input:checked+.agria-radio-label{border-color:#2d7a2d;background:#f0f9f0;color:#2d7a2d}
        .agria-radio-item:hover .agria-radio-label{border-color:#2d7a2d}
        .agria-product-badge{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;background:#f0f9f0;border:1px solid #c8e6c8;border-radius:6px;font-size:14px;font-weight:600;color:#2d7a2d}
        .agria-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 16px}
        .agria-separator{border:none;border-top:1px solid #e5e5e5;margin:20px 0}
        .agria-field-checkbox{margin-top:8px}
        .agria-checkbox-label{display:flex;align-items:flex-start;gap:8px;font-size:12px;color:#666;cursor:pointer;line-height:1.4}
        .agria-checkbox-label input{margin-top:2px;accent-color:#2d7a2d}.agria-checkbox-label a{color:#2d7a2d}
        .agria-submit-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;width:100%;padding:14px 24px;background:#2d7a2d;color:#fff;border:none;border-radius:6px;font-size:16px;font-weight:600;cursor:pointer;transition:background .2s;margin-top:8px}
        .agria-submit-btn:hover{background:#1f5c1f}.agria-submit-btn:disabled{background:#999;cursor:not-allowed}
        .agria-spinner{animation:agria-spin .8s linear infinite}@keyframes agria-spin{to{transform:rotate(360deg)}}
        .agria-msg{display:flex;align-items:flex-start;gap:10px;padding:14px 16px;border-radius:6px;margin-top:16px;font-size:14px;line-height:1.5}
        .agria-msg svg{flex-shrink:0;margin-top:2px}
        .agria-msg-success{background:#f0f9f0;border:1px solid #c8e6c8;color:#2d7a2d}
        .agria-msg-error{background:#fdf0f0;border:1px solid #f5c6c6;color:#c0392b}.agria-msg-error a{color:#c0392b;font-weight:600}
        .agria-msg-captcha{background:#fef9f0;border:1px solid #f5e6c6;color:#b7791f}
        .agria-recaptcha-info{font-size:11px;color:#999;text-align:center;margin-top:8px}.agria-recaptcha-info a{color:#999}
        @media(max-width:600px){.agria-grid{grid-template-columns:1fr}.agria-radio-group{flex-direction:column}.agria-inquiry-title{font-size:18px}}
        .grecaptcha-badge{visibility:hidden !important}
        </style>

        <script>
        (function(){
            var wrap=document.getElementById('<?php echo esc_js( $form_id ); ?>');
            if(!wrap)return;
            var form=wrap.querySelector('.agria-inquiry-form'),btn=wrap.querySelector('.agria-submit-btn'),
                btnTxt=wrap.querySelector('.agria-btn-text'),btnLoad=wrap.querySelector('.agria-btn-loading'),
                msgOk=wrap.querySelector('.agria-msg-success'),msgErr=wrap.querySelector('.agria-msg-error'),
                msgCap=wrap.querySelector('.agria-msg-captcha'),
                hasRC=<?php echo $has_rc ? 'true' : 'false'; ?>,rcKey='<?php echo esc_js( $this->recaptcha_site_key ); ?>';

            form.querySelectorAll('.agria-radio-item input').forEach(function(r){
                r.addEventListener('change',function(){
                    form.querySelectorAll('.agria-radio-item').forEach(function(i){i.classList.remove('agria-radio-active')});
                    if(this.checked)this.closest('.agria-radio-item').classList.add('agria-radio-active');
                });
            });

            var pSel=form.querySelector('.agria-product-select'),dSel=form.querySelector('.agria-delivery-select');
            if(pSel&&dSel){
                pSel.addEventListener('change',function(){
                    var opt=this.options[this.selectedIndex],fj=opt.getAttribute('data-forms'),fs=[];
                    try{fs=JSON.parse(fj||'[]')}catch(e){}
                    dSel.innerHTML='<option value="">— Wybierz formę —</option>';
                    (fs.length?fs:['Big-bag','Worki','Luz','Inna']).forEach(function(f){
                        var o=document.createElement('option');o.value=f;o.textContent=f;dSel.appendChild(o);
                    });
                });
            }

            form.addEventListener('submit',function(e){
                e.preventDefault();
                msgOk.style.display='none';msgErr.style.display='none';msgCap.style.display='none';
                var valid=true;
                form.querySelectorAll('[required]').forEach(function(el){
                    if(!el.value.trim()&&el.type!=='checkbox'){valid=false;el.style.borderColor='#c0392b'}
                    else if(el.type==='checkbox'&&!el.checked){valid=false}
                    else{el.style.borderColor=''}
                });
                if(!valid)return;
                btn.disabled=true;btnTxt.style.display='none';btnLoad.style.display='inline-flex';

                function doSubmit(token){
                    form.querySelector('[name="recaptcha_token"]').value=token||'';
                    fetch('<?php echo esc_url( admin_url( 'admin-ajax.php' ) ); ?>',{
                        method:'POST',body:new FormData(form),credentials:'same-origin'
                    }).then(function(r){return r.json()}).then(function(data){
                        btn.disabled=false;btnTxt.style.display='';btnLoad.style.display='none';
                        if(data.success){msgOk.style.display='flex';form.reset();msgOk.scrollIntoView({behavior:'smooth',block:'center'})}
                        else if(data.data&&data.data.captcha){msgCap.style.display='flex'}
                        else{msgErr.style.display='flex'}
                    }).catch(function(){
                        btn.disabled=false;btnTxt.style.display='';btnLoad.style.display='none';msgErr.style.display='flex';
                    });
                }

                if(hasRC&&typeof grecaptcha!=='undefined'){
                    grecaptcha.ready(function(){grecaptcha.execute(rcKey,{action:'agria_inquiry'}).then(doSubmit)});
                }else{doSubmit('')}
            });
        })();
        </script>
        <?php
        return ob_get_clean();
    }

    // ══════════════════════════════════════════════════════════════════════════
    // AJAX handler
    // ══════════════════════════════════════════════════════════════════════════

    public function handle_submit(): void {
        if ( ! wp_verify_nonce( $_POST['_nonce'] ?? '', 'agria_inquiry_nonce' ) ) {
            wp_send_json_error( [ 'message' => 'Token wygasł. Odśwież stronę.' ] );
        }
        if ( ! empty( $_POST['agria_website'] ) ) { wp_send_json_success(); }

        // reCAPTCHA v3
        if ( $this->has_recaptcha() ) {
            $rc_token = sanitize_text_field( $_POST['recaptcha_token'] ?? '' );
            if ( empty( $rc_token ) || ! $this->verify_recaptcha( $rc_token ) ) {
                wp_send_json_error( [ 'message' => 'Weryfikacja reCAPTCHA nie powiodła się.', 'captcha' => true ] );
            }
        }

        $d = [
            'inquiry_type'  => sanitize_text_field( $_POST['inquiry_type'] ?? 'oferta' ),
            'product_name'  => sanitize_text_field( $_POST['product_name'] ?? '' ),
            'product_id'    => absint( $_POST['product_id'] ?? 0 ),
            'delivery_form' => sanitize_text_field( $_POST['delivery_form'] ?? '' ),
            'quantity'      => sanitize_text_field( $_POST['quantity'] ?? '' ),
            'full_name'     => sanitize_text_field( $_POST['full_name'] ?? '' ),
            'company'       => sanitize_text_field( $_POST['company'] ?? '' ),
            'phone'         => sanitize_text_field( $_POST['phone'] ?? '' ),
            'email'         => sanitize_email( $_POST['email'] ?? '' ),
            'location'      => sanitize_text_field( $_POST['location'] ?? '' ),
            'message'       => sanitize_textarea_field( $_POST['message'] ?? '' ),
            'source_url'    => esc_url_raw( $_POST['source_url'] ?? '' ),
            'rodo_consent'  => ! empty( $_POST['rodo_consent'] ),
        ];

        if ( empty( $d['full_name'] ) || empty( $d['phone'] ) || empty( $d['email'] ) || empty( $d['product_name'] ) ) {
            wp_send_json_error( [ 'message' => 'Wypełnij wymagane pola.' ] );
        }
        if ( ! is_email( $d['email'] ) ) {
            wp_send_json_error( [ 'message' => 'Podaj prawidłowy adres e-mail.' ] );
        }
        if ( ! $d['rodo_consent'] ) {
            wp_send_json_error( [ 'message' => 'Wymagana jest zgoda RODO.' ] );
        }

        $inquiry_id  = $this->save_inquiry( $d );
        $sent_handler = $this->send_handler_email( $d, $inquiry_id );
        $this->send_client_email( $d );

        $sent_handler
            ? wp_send_json_success( [ 'message' => 'Wysłano.', 'inquiry_id' => $inquiry_id ] )
            : wp_send_json_error( [ 'message' => 'Nie udało się wysłać wiadomości.' ] );
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Zapis zgłoszenia (CPT)
    // ══════════════════════════════════════════════════════════════════════════

    private function save_inquiry( array $d ): int {
        $type_label = $d['inquiry_type'] === 'probka' ? 'Próbka' : 'Oferta';
        return (int) wp_insert_post( [
            'post_type'   => 'agria_inquiry',
            'post_title'  => sprintf( '%s — %s — %s', $type_label, $d['product_name'], $d['full_name'] ),
            'post_status' => 'inquiry_new',
            'meta_input'  => [
                '_inquiry_type'  => $d['inquiry_type'],
                '_product_name'  => $d['product_name'],
                '_product_id'    => $d['product_id'],
                '_delivery_form' => $d['delivery_form'],
                '_quantity'      => $d['quantity'],
                '_full_name'     => $d['full_name'],
                '_company'       => $d['company'],
                '_phone'         => $d['phone'],
                '_email'         => $d['email'],
                '_location'      => $d['location'],
                '_message'       => $d['message'],
                '_source_url'    => $d['source_url'],
                '_rodo_consent'  => $d['rodo_consent'] ? 'yes' : 'no',
                '_rodo_date'     => current_time( 'mysql' ),
                '_ip_address'    => $_SERVER['REMOTE_ADDR'] ?? '',
            ],
        ] );
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Email do handlowca
    // ══════════════════════════════════════════════════════════════════════════

    private function send_handler_email( array $d, int $inquiry_id ): bool {
        $to = get_option( 'agria_inquiry_email', '' );
        if ( ! $to ) $to = get_option( 'agria_catalog_cta_email', get_option( 'admin_email' ) );

        $type_label = $d['inquiry_type'] === 'probka' ? 'Zamówienie próbki' : 'Zapytanie ofertowe';
        $subject    = sprintf( '[Agria] %s — %s', $type_label, $d['product_name'] );
        $date       = wp_date( 'Y-m-d H:i' );
        $admin_url  = admin_url( 'post.php?post=' . $inquiry_id . '&action=edit' );

        $fields = [
            'Typ zapytania'   => $type_label,
            'Produkt'         => $d['product_name'],
            'Forma dostawy'   => $d['delivery_form'] ?: '—',
            'Ilość'           => $d['quantity'] ?: '—',
            ''                => '',
            'Imię i nazwisko' => $d['full_name'],
            'Firma'           => $d['company'] ?: '—',
            'Telefon'         => $d['phone'],
            'E-mail'          => $d['email'],
            'Miejscowość'     => $d['location'] ?: '—',
        ];
        $rows = '';
        foreach ( $fields as $lbl => $val ) {
            if ( $lbl === '' ) { $rows .= '<tr><td colspan="2" style="border-bottom:1px solid #e5e5e5;padding:8px 0;"></td></tr>'; continue; }
            $rows .= '<tr><td style="padding:8px 12px;font-weight:600;color:#555;white-space:nowrap;vertical-align:top;">'.esc_html($lbl).'</td><td style="padding:8px 12px;color:#1a1a1a;">'.esc_html($val).'</td></tr>';
        }
        if ( $d['message'] ) {
            $rows .= '<tr><td style="padding:8px 12px;font-weight:600;color:#555;vertical-align:top;">Uwagi</td><td style="padding:8px 12px;color:#1a1a1a;white-space:pre-wrap;">'.esc_html($d['message']).'</td></tr>';
        }

        $source = $d['source_url'] ? '<a href="'.esc_url($d['source_url']).'" style="color:#2d7a2d;">'.esc_html($d['source_url']).'</a>' : '—';

        $body = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head>
        <body style="margin:0;padding:0;font-family:Arial,sans-serif;background:#f5f5f5;">
        <div style="max-width:600px;margin:20px auto;background:#fff;border:1px solid #ddd;border-radius:8px;overflow:hidden;">
            <div style="background:#2d7a2d;padding:20px 24px;">
                <h1 style="margin:0;color:#fff;font-size:18px;font-weight:700;">'.esc_html($type_label).'</h1>
                <p style="margin:6px 0 0;color:rgba(255,255,255,.8);font-size:13px;">'.esc_html($d['product_name']).' &middot; '.esc_html($date).'</p>
            </div>
            <table style="width:100%;border-collapse:collapse;font-size:14px;margin:16px 0;">'.$rows.'</table>
            <div style="padding:16px 24px;text-align:center;">
                <a href="'.esc_url($admin_url).'" style="display:inline-block;padding:10px 24px;background:#2d7a2d;color:#fff;text-decoration:none;border-radius:4px;font-weight:600;font-size:14px;">Otwórz zgłoszenie #'.(int)$inquiry_id.' w panelu</a>
            </div>
            <div style="padding:12px 24px;background:#f9f9f9;border-top:1px solid #e5e5e5;font-size:12px;color:#888;">
                Wysłano z: '.$source.'<br>Zgoda RODO: Tak &middot; '.esc_html($date).' &middot; IP: '.esc_html($_SERVER['REMOTE_ADDR']??'').'
            </div>
        </div></body></html>';

        $headers = [
            'Content-Type: text/html; charset=UTF-8',
            'From: Agria Formularz <wordpress@' . parse_url( home_url(), PHP_URL_HOST ) . '>',
        ];
        if ( $d['email'] ) $headers[] = 'Reply-To: ' . $d['full_name'] . ' <' . $d['email'] . '>';
        $cc = get_option( 'agria_inquiry_cc_email', '' );
        if ( $cc && is_email( $cc ) ) $headers[] = 'Cc: ' . $cc;

        return wp_mail( $to, $subject, $body, $headers );
    }

    // ══════════════════════════════════════════════════════════════════════════
    // Email do klienta (autoresponder)
    // ══════════════════════════════════════════════════════════════════════════

    private function send_client_email( array $d ): bool {
        if ( empty( $d['email'] ) || ! is_email( $d['email'] ) ) return false;

        $type_label = $d['inquiry_type'] === 'probka' ? 'zamówienie próbki' : 'zapytanie ofertowe';
        $subject    = 'Potwierdzenie — ' . $d['product_name'] . ' | Agria';
        $date       = wp_date( 'j F Y, H:i' );
        $site_url   = home_url();

        $summary = [
            'Produkt'        => $d['product_name'],
            'Forma dostawy'  => $d['delivery_form'] ?: '—',
            'Ilość'          => $d['quantity'] ?: '—',
        ];
        $srows = '';
        foreach ( $summary as $lbl => $val ) {
            $srows .= '<tr><td style="padding:6px 0;color:#888;font-size:13px;">'.esc_html($lbl).'</td><td style="padding:6px 0 6px 12px;color:#333;font-size:13px;font-weight:600;">'.esc_html($val).'</td></tr>';
        }
        if ( $d['message'] ) {
            $srows .= '<tr><td style="padding:6px 0;color:#888;font-size:13px;">Uwagi</td><td style="padding:6px 0 6px 12px;color:#333;font-size:13px;">'.esc_html($d['message']).'</td></tr>';
        }

        $body = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head>
        <body style="margin:0;padding:0;font-family:Arial,sans-serif;background:#f5f5f5;">
        <div style="max-width:560px;margin:20px auto;background:#fff;border:1px solid #e0e0e0;border-radius:8px;overflow:hidden;">
            <div style="background:#2d7a2d;padding:24px 28px;text-align:center;">
                <h1 style="margin:0;color:#fff;font-size:20px;font-weight:700;">Dziękujemy za '.esc_html($type_label).'!</h1>
            </div>
            <div style="padding:28px;">
                <p style="margin:0 0 16px;font-size:15px;color:#333;line-height:1.6;">
                    '.esc_html($d['full_name']).', dziękujemy za przesłanie zapytania dotyczącego produktu <strong>'.esc_html($d['product_name']).'</strong>.
                </p>
                <p style="margin:0 0 20px;font-size:15px;color:#333;line-height:1.6;">
                    Nasz zespół handlowy zapozna się z Twoim zgłoszeniem i <strong>skontaktuje się w ciągu 1 dnia roboczego</strong> telefonicznie lub mailowo.
                </p>
                <div style="background:#f9f9f9;border:1px solid #e5e5e5;border-radius:6px;padding:16px 20px;margin-bottom:24px;">
                    <p style="margin:0 0 10px;font-size:12px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:.5px;">Podsumowanie zapytania</p>
                    <table style="width:100%;border-collapse:collapse;">'.$srows.'</table>
                    <p style="margin:10px 0 0;font-size:11px;color:#aaa;">Wysłano: '.esc_html($date).'</p>
                </div>
                <p style="margin:0 0 8px;font-size:14px;color:#333;">W razie pytań możesz się z nami skontaktować:</p>
                <p style="margin:0 0 4px;font-size:14px;color:#333;">📞 <a href="tel:+48605335559" style="color:#2d7a2d;text-decoration:none;font-weight:600;">+48 605 335 559</a></p>
                <p style="margin:0;font-size:14px;color:#333;">✉️ <a href="mailto:biuro@agria.pl" style="color:#2d7a2d;text-decoration:none;">biuro@agria.pl</a></p>
            </div>
            <div style="padding:16px 28px;background:#f5f5f5;border-top:1px solid #e5e5e5;text-align:center;">
                <p style="margin:0 0 4px;font-size:12px;color:#888;"><strong>Agria Sp. z o.o.</strong> — 35 lat doświadczenia na rynku nawozów wapniowych</p>
                <p style="margin:0;font-size:11px;color:#aaa;"><a href="'.esc_url($site_url).'" style="color:#2d7a2d;text-decoration:none;">www.agria.pl</a></p>
            </div>
        </div></body></html>';

        return wp_mail( $d['email'], $subject, $body, [
            'Content-Type: text/html; charset=UTF-8',
            'From: Agria Sp. z o.o. <wordpress@' . parse_url( home_url(), PHP_URL_HOST ) . '>',
        ] );
    }
}

Agria_Inquiry_Form::instance();
