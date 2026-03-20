<?php
/**
 * Moduł: Product Video
 *
 * Dodaje pole URL filmu do:
 *  - Kategorii produktów (term meta: category_video_url)
 *  - Produktów (post meta: _product_video_url)
 *
 * Shortcody:
 *  [product_category_video] — zwraca URL filmu z bieżącej kategorii (do użycia na archive)
 *  [product_video]          — zwraca URL filmu z bieżącego produktu (do użycia na single product)
 *
 * Użycie w Elementor:
 *  - Wstaw widget Video / HTML
 *  - Jako src/href podaj shortcode, np. [product_video]
 *  - Lub użyj Dynamic Tag → Shortcode
 */

defined( 'ABSPATH' ) || exit;

class Agria_Product_Video {

    private static ?self $instance = null;

    public static function instance(): self {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        // ── Kategorie ────────────────────────────────────────────────────
        add_action( 'product_cat_add_form_fields',  [ $this, 'add_category_field' ] );
        add_action( 'product_cat_edit_form_fields',  [ $this, 'edit_category_field' ] );
        add_action( 'created_product_cat',           [ $this, 'save_category_field' ] );
        add_action( 'edited_product_cat',            [ $this, 'save_category_field' ] );

        // ── Produkty ─────────────────────────────────────────────────────
        add_action( 'woocommerce_product_options_general_product_data', [ $this, 'add_product_field' ] );
        add_action( 'woocommerce_process_product_meta',                 [ $this, 'save_product_field' ] );

        // ── Shortcody ────────────────────────────────────────────────────
        add_shortcode( 'product_category_video', [ $this, 'shortcode_category_video' ] );
        add_shortcode( 'product_video',          [ $this, 'shortcode_product_video' ] );
    }

    // ── Kategorie — formularze ───────────────────────────────────────────────

    public function add_category_field(): void {
        ?>
        <div class="form-field">
            <label for="category_video_url"><?php esc_html_e( 'URL filmu kategorii', 'agria-auranet' ); ?></label>
            <input type="url" name="category_video_url" id="category_video_url" value="" placeholder="https://...">
            <p class="description"><?php esc_html_e( 'Link do filmu (mp4, YouTube, Vimeo)', 'agria-auranet' ); ?></p>
        </div>
        <?php
    }

    public function edit_category_field( \WP_Term $term ): void {
        $video_url = get_term_meta( $term->term_id, 'category_video_url', true );
        ?>
        <tr class="form-field">
            <th scope="row">
                <label for="category_video_url"><?php esc_html_e( 'URL filmu kategorii', 'agria-auranet' ); ?></label>
            </th>
            <td>
                <input type="url" name="category_video_url" id="category_video_url"
                       value="<?php echo esc_attr( $video_url ); ?>" style="width:100%;" placeholder="https://...">
                <p class="description"><?php esc_html_e( 'Link do filmu (mp4, YouTube, Vimeo)', 'agria-auranet' ); ?></p>
            </td>
        </tr>
        <?php
    }

    public function save_category_field( int $term_id ): void {
        if ( isset( $_POST['category_video_url'] ) ) {
            update_term_meta( $term_id, 'category_video_url', esc_url_raw( wp_unslash( $_POST['category_video_url'] ) ) );
        }
    }

    // ── Produkty — pole w zakładce Ogólne ────────────────────────────────────

    public function add_product_field(): void {
        woocommerce_wp_text_input( [
            'id'          => '_product_video_url',
            'label'       => __( 'URL filmu produktu', 'agria-auranet' ),
            'placeholder' => 'https://...',
            'desc_tip'    => true,
            'description' => __( 'Link do filmu (mp4, YouTube, Vimeo). Nadpisuje film z kategorii.', 'agria-auranet' ),
        ] );
    }

    public function save_product_field( int $post_id ): void {
        if ( isset( $_POST['_product_video_url'] ) ) {
            update_post_meta( $post_id, '_product_video_url', esc_url_raw( wp_unslash( $_POST['_product_video_url'] ) ) );
        }
    }

    // ── Shortcody ────────────────────────────────────────────────────────────

    /**
     * [product_category_video]
     * Zwraca URL filmu przypisanego do bieżącej kategorii produktu.
     * Działa tylko na stronach archiwum kategorii (is_product_category).
     */
    public function shortcode_category_video(): string {
        if ( ! is_product_category() ) {
            return '';
        }

        $term = get_queried_object();
        if ( ! $term || is_wp_error( $term ) ) {
            return '';
        }

        $url = get_term_meta( $term->term_id, 'category_video_url', true );
        return $url ? esc_url( $url ) : '';
    }

    /**
     * [product_video]
     * Zwraca URL filmu przypisanego do bieżącego produktu.
     * Działa na single product i w loopie produktowym.
     */
    public function shortcode_product_video(): string {
        global $product;

        if ( ! $product || ! is_a( $product, 'WC_Product' ) ) {
            global $post;
            if ( $post && $post->post_type === 'product' ) {
                $product = wc_get_product( $post->ID );
            }
        }

        if ( ! $product || ! is_a( $product, 'WC_Product' ) ) {
            return '';
        }

        $url = get_post_meta( $product->get_id(), '_product_video_url', true );
        return $url ? esc_url( $url ) : '';
    }
}

Agria_Product_Video::instance();
