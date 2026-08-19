<?php
/**
 * Modul: stare adresy produktow -> 301 na adres kanoniczny (T-028, 2026-08-19)
 *
 * PROBLEM: kazdy z 19 produktow odpowiada HTTP 200 pod **dwoma** adresami — pod
 * wlasciwa sciezka z kategoria (np. /wapno-nawozowe-rolnictwo/agrobielik-70/)
 * oraz pod stara baza /produkt/agrobielik-70/. Sprawdzone 19.08: 19 na 19 slugow
 * odpowiada 200 pod stara baza, kazdy z canonicalem wskazujacym adres wlasciwy.
 *
 * Canonical dziala — GSC za 90 dni nie pokazuje dla /produkt/* ani jednego
 * wyswietlenia poza demo-produktem motywu, ktory i tak jest juz 404. To znaczy,
 * ze nie odzyskujemy tu ruchu, tylko przestajemy wydawac budzet crawlowy na
 * drugi komplet adresow. Ma to znaczenie, bo cztery strony poradnikowe z lipca
 * nadal czekaja na pierwsze pobranie przez Google (T-026).
 *
 * DLACZEGO PHP, A NIE .htaccess: adres docelowy zalezy od kategorii produktu
 * i jest inny dla kazdej pozycji — w .htaccess wymagaloby to 19 recznych regul,
 * ktore trzeba pamietac przy kazdym nowym produkcie i przy kazdej zmianie
 * kategorii. Hook czyta adres kanoniczny z WooCommerce, wiec nie da sie
 * rozjechac z rzeczywistoscia.
 *
 * ZAKRES: wylacznie zadania GET pod stara baza, wylacznie dla istniejacych
 * produktow. Nieistniejacy slug nadal daje 404 — nie zamieniamy 404 na 301
 * prowadzace do 404. Panel, REST i AJAX sa nietkniete.
 */

defined( 'ABSPATH' ) || exit;

if ( ! function_exists( 'agria_redirect_legacy_product_base' ) ) {
	/**
	 * Przekierowuje /produkt/<slug>/ na adres kanoniczny produktu.
	 */
	function agria_redirect_legacy_product_base(): void {
		if ( is_admin() || wp_doing_ajax() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
			return;
		}
		if ( ! is_singular( 'product' ) ) {
			return;
		}
		// GET i HEAD. Sam GET nie wystarcza: czesc crawlerow i narzedzi monitorujacych
		// odpytuje HEAD-em i przy samym GET dostawalaby 200 pod starym adresem,
		// czyli dokladnie to, co ten modul ma wyeliminowac (sprawdzone 19.08).
		if ( ! in_array( $_SERVER['REQUEST_METHOD'] ?? 'GET', array( 'GET', 'HEAD' ), true ) ) {
			return;
		}

		$uri = wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH );
		if ( ! is_string( $uri ) || strpos( $uri, '/produkt/' ) !== 0 ) {
			return;
		}

		$kanoniczny = get_permalink( get_queried_object_id() );
		if ( ! $kanoniczny ) {
			return;
		}

		// Zabezpieczenie przed petla: jesli adres kanoniczny sam siedzi pod stara
		// baza (czyli Premmerce zmienil konfiguracje), nie przekierowujemy.
		$sciezka_kan = wp_parse_url( $kanoniczny, PHP_URL_PATH );
		if ( ! is_string( $sciezka_kan ) || $sciezka_kan === $uri || strpos( $sciezka_kan, '/produkt/' ) === 0 ) {
			return;
		}

		wp_safe_redirect( $kanoniczny, 301, 'Agria legacy product base' );
		exit;
	}
	add_action( 'template_redirect', 'agria_redirect_legacy_product_base', 1 );
}
