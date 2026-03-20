<?php
/**
 * Moduł: Scroll to Top
 *
 * Dodaje przycisk "Przewiń do góry" w prawym dolnym rogu strony.
 * Pojawia się po przewinięciu 300px. Zero zależności JS.
 *
 * Kolory: używa zmiennych CSS Elementora (Global Colors):
 *  - --e-global-color-primary   → tło przycisku
 *  - --e-global-color-secondary → tło na hover
 * Automatycznie dopasowuje się do palety każdego motywu Elementor.
 */

defined( 'ABSPATH' ) || exit;

class Agria_Scroll_To_Top {

    private static ?self $instance = null;

    public static function instance(): self {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        add_action( 'wp_footer', [ $this, 'render' ] );
    }

    public function render(): void {
        ?>
        <button id="agria-scroll-top" aria-label="<?php esc_attr_e( 'Przewiń do góry', 'agria-auranet' ); ?>">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 19V5M12 5L5 12M12 5L19 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </button>

        <style>
            #agria-scroll-top {
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 50px;
                height: 50px;
                background-color: var(--e-global-color-primary, #6ec1e4);
                color: #fff;
                border: none;
                border-radius: 50%;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
                z-index: 9999;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }
            #agria-scroll-top.visible {
                opacity: 1;
                visibility: visible;
            }
            #agria-scroll-top:hover {
                background-color: var(--e-global-color-secondary, #54595f);
                transform: translateY(-3px);
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
            }
            #agria-scroll-top:active {
                transform: translateY(-1px);
            }
            @media (max-width: 768px) {
                #agria-scroll-top {
                    bottom: 20px;
                    right: 20px;
                    width: 45px;
                    height: 45px;
                }
            }
        </style>

        <script>
            (function() {
                var btn = document.getElementById('agria-scroll-top');
                if (!btn) return;
                window.addEventListener('scroll', function() {
                    btn.classList.toggle('visible', window.pageYOffset > 300);
                });
                btn.addEventListener('click', function() {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                });
            })();
        </script>
        <?php
    }
}

Agria_Scroll_To_Top::instance();
