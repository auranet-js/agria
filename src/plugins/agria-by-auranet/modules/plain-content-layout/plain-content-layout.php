<?php
/**
 * Moduł: kolumna tekstu na stronach z surową treścią (T-063)
 *
 * Problem: strony, których treść siedzi w `post_content` i które nie mają własnego
 * układu Elementora, renderują się przez widget `theme-post-content` w szablonie
 * „Agria Single Page". Kontener tego widgetu jest pełnej szerokości (`e-con-full`,
 * bez ograniczenia), więc akapity ciągnęły się od krawędzi do krawędzi okna —
 * na 1440 px linia tekstu miała 1440 px, na telefonie dotykała obu boków bez marginesu.
 * Zmierzone 21.08: akapit 0–1440 px na `/wapno-nawozowe/` wobec 114–878 px
 * na zwykłym wpisie.
 *
 * Dotyczy trzech stron, wszystkie zbudowane z surowego HTML-a:
 * `/wapno-granulowane/`, `/wapno-nawozowe/` (cele reklam) i
 * `/wapno-do-stabilizacji-gruntow/` (indeksowana).
 *
 * Rozwiązanie: klasa `agria-plain` na `<body>` tych stron + ograniczenie szerokości
 * kolumny. Świadomie NIE ruszamy kontenera w szablonie — używa go każda strona,
 * także te z własnym układem Elementora i sekcjami na pełną szerokość.
 *
 * Cztery pułapki, każda złapana pomiarem, nie na oko:
 *  1. Widget renderuje się BEZ `.elementor-widget-container` — treść jest
 *     bezpośrednim dzieckiem `.elementor-widget-theme-post-content`.
 *  2. `max-width` bez `!important` przegrywa z regułą Elementora na `.elementor-element`.
 *  3. Widget jest elementem flex z domyślnym `min-width:auto`, więc nie zwęża się
 *     poniżej najszerszej zawartości.
 *  4. Nawet z `min-width:0` szerokość minimalna **tabel** rozpychała kontener:
 *     dokument miał 465 px przy ekranie 390 px. Dopiero `table-layout:fixed`
 *     na wąskich ekranach zdejmuje to napięcie — komórki zawijają tekst zamiast
 *     wymuszać szerokość. Na desktopie zostaje układ automatyczny, bo tam jest miejsce.
 *
 * To jest łatka na błąd konstrukcyjny z 06.08 i 14.08. Docelowo landingi mają zostać
 * przebudowane na wzorcu, który już działa (kolumna z szablonu wpisu) — T-063.
 *
 * @package Agria_By_Auranet
 */

defined( 'ABSPATH' ) || exit;

/** Strony z treścią w `post_content` i bez własnego układu Elementora. */
const AGRIA_PLAIN_PAGES = [ 2745, 2751, 2757, 2796 ];

/**
 * Znacznik na <body>, żeby CSS nie dotykał reszty serwisu.
 */
function agria_plain_body_class( array $classes ): array {
	if ( is_page( AGRIA_PLAIN_PAGES ) ) {
		$classes[] = 'agria-plain';
	}
	return $classes;
}
add_filter( 'body_class', 'agria_plain_body_class' );

/**
 * Kolumna tekstu o czytelnej długości wiersza.
 *
 * 900 px na desktopie daje ok. 90–100 znaków w wierszu przy obecnym stopniu pisma —
 * zbliżone do kolumny wpisu (764 px przy węższym kroju). Marginesy boczne odklejają
 * tekst od krawędzi ekranu telefonu.
 */
function agria_plain_styles(): void {
	if ( ! is_page( AGRIA_PLAIN_PAGES ) ) {
		return;
	}
	?>
<style id="agria-plain-layout-css">
.agria-plain .elementor-widget-theme-post-content{
	max-width:900px !important;
	min-width:0;
	margin-left:auto;margin-right:auto;padding-left:24px;padding-right:24px;box-sizing:border-box
}
.agria-plain .elementor-widget-theme-post-content > *{max-width:100%}
.agria-plain .elementor-widget-theme-post-content figure.wp-block-table{
	display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch
}
.agria-plain .elementor-widget-theme-post-content table{width:100%}
.agria-plain .elementor-widget-theme-post-content img{max-width:100%;height:auto}
@media (max-width:900px){
	/* Szerokość minimalna tabel rozpychała kontener i dawała poziomy przelew.
	   Stała siatka kolumn zdejmuje to napięcie — komórki zawijają tekst. */
	.agria-plain .elementor-widget-theme-post-content table{table-layout:fixed;word-break:break-word}
}
@media (max-width:480px){
	.agria-plain .elementor-widget-theme-post-content{padding-left:16px;padding-right:16px}
	.agria-plain .elementor-widget-theme-post-content td,
	.agria-plain .elementor-widget-theme-post-content th{padding:6px 8px;font-size:14px}
}
</style>
	<?php
}
add_action( 'wp_head', 'agria_plain_styles', 20 );
