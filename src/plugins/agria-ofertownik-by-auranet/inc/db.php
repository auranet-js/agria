<?php
/**
 * Schemat bazy ofertownika.
 *
 * Cennik siedzi we WLASNEJ tabeli, nie w wariantach WooCommerce — decyzja z ADR 22.08.2026,
 * podjeta po zmierzeniu, ze `_price` wychodzi publicznie przez Store API i przez schema Rank Matha.
 * Osie zostaja te same, co przewidywala specyfikacja: produkt x zaklad x forma x frakcja.
 */

defined( 'ABSPATH' ) || exit;

function agria_of_tabela( string $nazwa ): string {
	global $wpdb;
	return $wpdb->prefix . 'agria_of_' . $nazwa;
}

function agria_of_db_utworz_tabele(): void {
	global $wpdb;
	require_once ABSPATH . 'wp-admin/includes/upgrade.php';

	$collate = $wpdb->get_charset_collate();
	$ceny    = agria_of_tabela( 'ceny' );
	$historia = agria_of_tabela( 'historia' );

	// `cena` i `cena_min` w GROSZACH — liczby calkowite. Ceny wapna schodza do 36 zl/t,
	// a przy mnozeniu przez tonaz i dzieleniu przez ladownosc float potrafi zgubic grosz
	// w miejscu, ktore potem trafia na fakture.
	dbDelta( "CREATE TABLE {$ceny} (
		id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
		produkt_id BIGINT UNSIGNED NOT NULL,
		zaklad_term_id BIGINT UNSIGNED NOT NULL,
		forma_term_id BIGINT UNSIGNED NOT NULL,
		frakcja VARCHAR(40) NOT NULL DEFAULT '',
		cena INT UNSIGNED NULL,
		cena_min INT UNSIGNED NULL,
		jednostka VARCHAR(10) NOT NULL DEFAULT 'tona',
		zmienil BIGINT UNSIGNED NULL,
		zmieniono DATETIME NULL,
		PRIMARY KEY (id),
		UNIQUE KEY pozycja (produkt_id, zaklad_term_id, forma_term_id, frakcja),
		KEY produkt (produkt_id)
	) {$collate};" );

	// Historia zmian cen — wymog z §4.7 specyfikacji: skoro cennik prowadzi klient,
	// pomylka o rzad wielkosci musi byc widoczna i odwracalna.
	dbDelta( "CREATE TABLE {$historia} (
		id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
		cena_id BIGINT UNSIGNED NOT NULL,
		pole VARCHAR(20) NOT NULL,
		bylo INT UNSIGNED NULL,
		jest INT UNSIGNED NULL,
		zmienil BIGINT UNSIGNED NULL,
		zmieniono DATETIME NOT NULL,
		PRIMARY KEY (id),
		KEY cena (cena_id),
		KEY czas (zmieniono)
	) {$collate};" );
}

/** Zlotowki (tekst z formularza albo float) na grosze. Null zostaje nullem — brak ceny to nie zero. */
function agria_of_na_grosze( $zl ): ?int {
	if ( $zl === null || $zl === '' ) {
		return null;
	}
	$zl = str_replace( [ ' ', ' ', ',' ], [ '', '', '.' ], (string) $zl );
	if ( ! is_numeric( $zl ) ) {
		return null;
	}
	return (int) round( ( (float) $zl ) * 100 );
}

function agria_of_na_zlote( ?int $grosze ): ?float {
	return $grosze === null ? null : round( $grosze / 100, 2 );
}
