<?php
/**
 * Moduł: pasek kontaktu na telefonie (T-059)
 *
 * Powód: 14–20.08 kampania Google Ads kupiła 147 kliknięć przy zerze konwersji.
 * Numer telefonu — jedyny mierzony kanał leada — pokazywał się na 62 z 1 023
 * wyświetleń reklamy, a na stronie docelowej pierwszy link `tel:` to była ikonka
 * słuchawki na 29% wysokości dokumentu. Ten pasek daje numer pod kciukiem przez
 * cały czas przewijania, na urządzeniach dotykowych.
 *
 * Zakres: wyłącznie strony docelowe reklam, karty produktów i kategorie.
 * Nie dotyka reszty serwisu ani panelu.
 *
 * @package Agria_By_Auranet
 */

defined( 'ABSPATH' ) || exit;

const AGRIA_CALLBAR_TEL      = '+48664393062';
const AGRIA_CALLBAR_TEL_TEXT = '664 393 062';

/**
 * Czy pasek ma się pokazać na tym widoku.
 */
function agria_callbar_enabled(): bool {
	if ( is_admin() || is_feed() || is_404() || is_search() ) {
		return false;
	}

	/** Strony docelowe kampanii Ads. */
	$landing_ids = [ 2751, 2757, 2796 ];

	if ( is_page( $landing_ids ) ) {
		return true;
	}

	if ( function_exists( 'is_product' ) && is_product() ) {
		return true;
	}

	if ( function_exists( 'is_product_category' ) && is_product_category() ) {
		return true;
	}

	return false;
}

/**
 * Pasek renderujemy w stopce dokumentu; CSS trzyma go poza układem strony,
 * więc nie rusza CLS ani szerokości kontenerów.
 */
function agria_callbar_render(): void {
	if ( ! agria_callbar_enabled() ) {
		return;
	}

	$tel  = AGRIA_CALLBAR_TEL;
	$text = AGRIA_CALLBAR_TEL_TEXT;
	?>
<style id="agria-callbar-css">
.agria-callbar{display:none}
@media (max-width:1024px) and (pointer:coarse){
	.agria-callbar{
		display:flex;position:fixed;left:0;right:0;bottom:0;z-index:9990;
		box-shadow:0 -2px 10px rgba(0,0,0,.18);font-family:inherit
	}
	.agria-callbar a{
		flex:1;display:flex;align-items:center;justify-content:center;gap:.4em;
		padding:14px 8px;font-size:16px;font-weight:700;line-height:1.1;
		text-decoration:none;letter-spacing:.01em
	}
	.agria-callbar .agria-callbar-tel{background:#1f5c2e;color:#fff}
	.agria-callbar .agria-callbar-form{background:#e8f0e6;color:#1f5c2e;flex:0 0 42%}
	body{padding-bottom:56px}
}
@media print{.agria-callbar{display:none}}
</style>
<div class="agria-callbar" role="complementary" aria-label="Szybki kontakt">
	<a class="agria-callbar-tel" href="tel:<?php echo esc_attr( $tel ); ?>" data-agria-callbar="tel">Zadzwoń <?php echo esc_html( $text ); ?></a>
	<a class="agria-callbar-form" href="#oddzwonimy" data-agria-callbar="form">Oddzwonimy</a>
</div>
	<?php
}
add_action( 'wp_footer', 'agria_callbar_render', 20 );
