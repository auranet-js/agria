<?php
/**
 * Osie cennika: zaklady wysylkowe i formy dostawy — czytane z taksonomii `pa_agria-*`.
 *
 * Atrybuty sa brudne po buggy imporcie (rozbijanie wartosci po przecinkach). Stan zmierzony 22.08.2026:
 * 17 termow lokalizacji, z tego 3 to puste duplikaty; 22 termy form, z tego 7 bez zadnego przypisania.
 * Prawdziwy dlug to slowo „Luz" w SIEDMIU zapisach (Luz, Luz 24 t, Luz (24 t), Luz 14–16 t,
 * Luz 24–26 t, Luz 25–27 t, Luz (25–27 t)) z 11 przypisaniami do zywych kart.
 *
 * Ofertownik normalizuje to W LOCIE i dlatego NIE CZEKA na sprzatanie taksonomii.
 * Sprzatanie zostaje osobnym zadaniem — bo te same smieci widzi dzis rolnik na kartach produktow —
 * ale nie jest juz warunkiem wstepnym cennika.
 */

defined( 'ABSPATH' ) || exit;

const AGRIA_OF_TAX_ZAKLAD = 'pa_agria-lokalizacja';
const AGRIA_OF_TAX_FORMA  = 'pa_agria-forma-dostawy';

/**
 * Rozklada nazwe termu formy na rodzaj i gramature.
 *
 * „Luz 24 t" to nie jest forma dostawy — to forma zlepiona z ladownoscia auta. Ladownosc nalezy
 * do ustawien transportu (i bywa inna), wiec tutaj ja odrzucamy zamiast wozic dalej.
 *
 * @return array{rodzaj:string, kg:?int, klucz:string}|null  null = term smieciowy, do pominiecia
 */
function agria_of_rozbierz_forme( string $nazwa ): ?array {
	$n = trim( preg_replace( '/\s+/u', ' ', $nazwa ) );

	// Smieci po imporcie: „1- 0", „4", „4- 0", „8" — same cyfry i myslniki, zero tresci.
	if ( $n === '' || preg_match( '/^[\d\s\-–]+$/u', $n ) ) {
		return null;
	}

	$male = mb_strtolower( $n, 'UTF-8' );

	if ( str_starts_with( $male, 'luz' ) ) {
		// Ladownosc z nazwy ignorujemy swiadomie — patrz komentarz wyzej.
		return [ 'rodzaj' => 'luz', 'kg' => null, 'klucz' => 'luz' ];
	}

	if ( str_contains( $male, 'big-bag' ) || str_contains( $male, 'big bag' ) ) {
		$kg = preg_match( '/(\d+)\s*kg/u', $male, $m ) ? (int) $m[1] : null;
		return [ 'rodzaj' => 'big-bag', 'kg' => $kg, 'klucz' => $kg ? "big-bag-{$kg}" : 'big-bag' ];
	}

	if ( str_starts_with( $male, 'worek' ) ) {
		$kg = preg_match( '/(\d+)\s*kg/u', $male, $m ) ? (int) $m[1] : null;
		return [ 'rodzaj' => 'worek', 'kg' => $kg, 'klucz' => $kg ? "worek-{$kg}" : 'worek' ];
	}

	return null;
}

/**
 * Nazwa zakladu bez kodu pocztowego, do porownan i do wyswietlenia.
 * „26-060 Checiny (26-060)" i „Checiny (26-060)" to ten sam zaklad zapisany dwa razy.
 */
function agria_of_nazwa_zakladu( string $nazwa ): string {
	$n = preg_replace( '/\(\s*\d{2}-\d{3}\s*\)/u', '', $nazwa );      // nawias z kodem
	$n = preg_replace( '/^\s*\d{2}-\d{3}\s+/u', '', (string) $n );    // kod na poczatku
	return trim( preg_replace( '/\s+/u', ' ', (string) $n ) );
}

function agria_of_kod_zakladu( string $nazwa ): ?string {
	return preg_match( '/(\d{2}-\d{3})/u', $nazwa, $m ) ? $m[1] : null;
}

/** Zaklady przypisane do produktu. Puste duplikaty odpadaja same — nie maja przypisan. */
function agria_of_zaklady_produktu( int $produkt_id ): array {
	$termy = wp_get_post_terms( $produkt_id, AGRIA_OF_TAX_ZAKLAD );
	if ( is_wp_error( $termy ) ) {
		return [];
	}
	$out = [];
	foreach ( $termy as $t ) {
		$out[ $t->term_id ] = [
			'term_id' => $t->term_id,
			'nazwa'   => agria_of_nazwa_zakladu( $t->name ),
			'kod'     => agria_of_kod_zakladu( $t->name ),
			'surowa'  => $t->name,
		];
	}
	return $out;
}

/**
 * Formy przypisane do produktu, znormalizowane i ODDUPLIKOWANE.
 *
 * Agrobielik 70 ma dzis cztery termy formy, z ktorych dwa to ten sam luz zapisany inaczej.
 * Bez tego kroku cennik miakby dwie pozycje na to samo i handlowiec zobaczylby „brak ceny"
 * przy jednej z nich.
 */
function agria_of_formy_produktu( int $produkt_id ): array {
	$termy = wp_get_post_terms( $produkt_id, AGRIA_OF_TAX_FORMA );
	if ( is_wp_error( $termy ) ) {
		return [];
	}
	$out = [];
	foreach ( $termy as $t ) {
		$f = agria_of_rozbierz_forme( $t->name );
		if ( ! $f ) {
			continue;
		}
		// Pierwszy term wygrywa; kolejne zapisy tej samej formy dokladaja sie tylko jako slad.
		if ( isset( $out[ $f['klucz'] ] ) ) {
			$out[ $f['klucz'] ]['termy'][] = $t->term_id;
			$out[ $f['klucz'] ]['surowe'][] = $t->name;
			continue;
		}
		$out[ $f['klucz'] ] = [
			'klucz'   => $f['klucz'],
			'rodzaj'  => $f['rodzaj'],
			'kg'      => $f['kg'],
			'term_id' => $t->term_id,
			'termy'   => [ $t->term_id ],
			'surowe'  => [ $t->name ],
			'nazwa'   => $f['rodzaj'] === 'luz' ? 'Luz' : ucfirst( $f['rodzaj'] ) . ( $f['kg'] ? " {$f['kg']} kg" : '' ),
		];
	}
	return $out;
}

/** Produkty, ktore ofertownik obsluguje — wszystkie opublikowane karty WooCommerce. */
function agria_of_produkty(): array {
	return get_posts( [
		'post_type'      => 'product',
		'post_status'    => 'publish',
		'posts_per_page' => -1,
		'orderby'        => 'title',
		'order'          => 'ASC',
	] );
}
