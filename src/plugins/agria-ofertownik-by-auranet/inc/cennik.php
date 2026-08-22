<?php
/**
 * Cennik: budowa siatki pozycji z osi i zasiew cenami z cennika Pawla z 07.08.2026.
 *
 * Zasiew powiela te sama cene dla KAZDEGO zakladu, z ktorego dany produkt jedzie — swiadomie.
 * Cennik Pawla nie ma podzialu na zaklady, a ceny per kopalnia sie roznia; poprawianie gotowej
 * tabeli to robota na godzine, wypelnianie pustej na kilka dni (spec §4.1a).
 */

defined( 'ABSPATH' ) || exit;

/**
 * Cennik startowy: SKU => [ klucz formy => cena zl/t ].
 *
 * Zrodlo: docs/operations/CENNIK_PAWEL_2026-08-07.md (mail Pawla 07.08.2026 12:49), przelozony
 * na tone. Ceny netto, za towar, bez transportu.
 *
 * Ceny opakowan przychodza od AGRII ZA SZTUKE i tutaj sa juz przeliczone na tone — Agrobielik 70
 * w worku 20 kg to 11,50 zl/szt, czyli 575 zl/t. Roznica wobec 220 zl/t luzem jest dwuipolkrotna
 * i to jest wlasciwy powod, dla ktorego cennik musi miec os formy.
 *
 * Cztery karty bez ceny (AGR-004, AGR-007, AGR-012 i Kreda czarna bez SKU) zostaja puste —
 * pozycja powstaje, cena jest nullem, ekran wyceny mowi wprost „brak ceny".
 */
function agria_of_cennik_startowy(): array {
	return [
		'AGR-001' => [ 'luz' => 220, 'big-bag-1000' => 400, 'worek-20' => 575, 'worek-40' => 475 ],
		'AGR-002' => [ 'luz' => 750, 'big-bag-1000' => 850 ], // frakcja 0–3; 2–8 mm ma wlasne ceny, patrz nizej
		'AGR-003' => [ 'big-bag-1000' => 790 ],
		'AGR-005' => [ 'luz' => 120 ],
		'AGR-006' => [ 'luz' => 57 ],
		'AGR-008' => [ 'big-bag-1000' => 350, 'worek-25' => 380 ],
		'AGR-009' => [ 'luz' => 50 ],
		'AGR-010' => [ 'luz' => 36 ],
		'AGR-011' => [ 'big-bag-1000' => 370, 'worek-25' => 410 ],
		'AGR-013' => [ 'big-bag-1000' => 410, 'worek-25' => 490 ],
		'AGR-014' => [ 'luz' => 125 ],
		'AGR-015' => [ 'luz' => 190, 'worek-30' => 610 ],
		'AGR-016' => [ 'worek-30' => 645 ],
		'AGR-017' => [ 'luz' => 950, 'big-bag-1000' => 1200 ],
		'AGR-018' => [ 'luz' => 945, 'worek-25' => 1220 ],
	];
}

/**
 * Agrobielik 90 (AGR-002) ma na jednej karcie WooCommerce cztery ceny, bo cennik rozbija go
 * na frakcje 0–3 mm i 2–8 mm. To jedyny produkt, ktory potrzebuje trzeciej osi.
 */
function agria_of_frakcje_startowe(): array {
	return [
		'AGR-002' => [
			'0-3 mm' => [ 'luz' => 750, 'big-bag-1000' => 850 ],
			'2-8 mm' => [ 'luz' => 850, 'big-bag-1000' => 940 ],
		],
	];
}

/**
 * Buduje siatke pozycji cennika dla wszystkich produktow: zaklad x forma (x frakcja).
 * Nie zapisuje niczego — zwraca to, co powinno byc w tabeli.
 */
function agria_of_zbuduj_siatke(): array {
	$startowy = agria_of_cennik_startowy();
	$frakcje  = agria_of_frakcje_startowe();
	$siatka   = [];

	foreach ( agria_of_produkty() as $produkt ) {
		$sku      = get_post_meta( $produkt->ID, '_sku', true );
		$zaklady  = agria_of_zaklady_produktu( $produkt->ID );
		$formy    = agria_of_formy_produktu( $produkt->ID );

		if ( ! $zaklady || ! $formy ) {
			continue;
		}

		$warianty_frakcji = isset( $frakcje[ $sku ] ) ? array_keys( $frakcje[ $sku ] ) : [ '' ];

		foreach ( $zaklady as $z ) {
			foreach ( $formy as $f ) {
				foreach ( $warianty_frakcji as $frakcja ) {
					$cena_zl = $frakcja !== ''
						? ( $frakcje[ $sku ][ $frakcja ][ $f['klucz'] ] ?? null )
						: ( $startowy[ $sku ][ $f['klucz'] ] ?? null );

					$siatka[] = [
						'produkt_id'     => $produkt->ID,
						'produkt'        => $produkt->post_title,
						'sku'            => $sku,
						'zaklad_term_id' => $z['term_id'],
						'zaklad'         => $z['nazwa'],
						'forma_term_id'  => $f['term_id'],
						'forma'          => $f['nazwa'],
						'forma_klucz'    => $f['klucz'],
						'frakcja'        => $frakcja,
						'cena'           => agria_of_na_grosze( $cena_zl ),
					];
				}
			}
		}
	}
	return $siatka;
}

/**
 * Zapisuje siatke do tabeli. Pozycje juz istniejace zostaja NIETKNIETE — zasiew nie nadpisuje
 * tego, co AGRIA zdazyla zmienic. Dokladane sa wylacznie brakujace kombinacje.
 *
 * @return array{dodane:int, pominiete:int}
 */
function agria_of_zasiej_cennik(): array {
	global $wpdb;
	$tab   = agria_of_tabela( 'ceny' );
	$teraz = current_time( 'mysql' );
	$dodane = 0;
	$pominiete = 0;

	foreach ( agria_of_zbuduj_siatke() as $p ) {
		$istnieje = $wpdb->get_var( $wpdb->prepare(
			"SELECT id FROM {$tab} WHERE produkt_id=%d AND zaklad_term_id=%d AND forma_term_id=%d AND frakcja=%s",
			$p['produkt_id'], $p['zaklad_term_id'], $p['forma_term_id'], $p['frakcja']
		) );
		if ( $istnieje ) {
			$pominiete++;
			continue;
		}
		$wpdb->insert( $tab, [
			'produkt_id'     => $p['produkt_id'],
			'zaklad_term_id' => $p['zaklad_term_id'],
			'forma_term_id'  => $p['forma_term_id'],
			'frakcja'        => $p['frakcja'],
			'cena'           => $p['cena'],
			'cena_min'       => null,
			'jednostka'      => 'tona',
			'zmienil'        => null,
			'zmieniono'      => $teraz,
		] );
		$dodane++;
	}
	return [ 'dodane' => $dodane, 'pominiete' => $pominiete ];
}

/** Cena pozycji — null gdy brak. Zwraca grosze. */
function agria_of_cena( int $produkt_id, int $zaklad_term_id, int $forma_term_id, string $frakcja = '' ): ?array {
	global $wpdb;
	$tab = agria_of_tabela( 'ceny' );
	$w = $wpdb->get_row( $wpdb->prepare(
		"SELECT * FROM {$tab} WHERE produkt_id=%d AND zaklad_term_id=%d AND forma_term_id=%d AND frakcja=%s",
		$produkt_id, $zaklad_term_id, $forma_term_id, $frakcja
	), ARRAY_A );
	return $w ?: null;
}

/**
 * Zmiana ceny z zapisem historii i wykryciem skoku o rzad wielkosci.
 *
 * @return array{ok:bool, ostrzezenie:?string}
 */
function agria_of_ustaw_cene( int $id, string $pole, ?int $grosze, int $user_id ): array {
	global $wpdb;
	if ( ! in_array( $pole, [ 'cena', 'cena_min' ], true ) ) {
		return [ 'ok' => false, 'ostrzezenie' => 'nieznane pole' ];
	}
	$tab = agria_of_tabela( 'ceny' );
	$bylo = $wpdb->get_var( $wpdb->prepare( "SELECT {$pole} FROM {$tab} WHERE id=%d", $id ) );
	$bylo = $bylo === null ? null : (int) $bylo;

	$wpdb->update( $tab,
		[ $pole => $grosze, 'zmienil' => $user_id, 'zmieniono' => current_time( 'mysql' ) ],
		[ 'id' => $id ]
	);
	$wpdb->insert( agria_of_tabela( 'historia' ), [
		'cena_id'   => $id,
		'pole'      => $pole,
		'bylo'      => $bylo,
		'jest'      => $grosze,
		'zmienil'   => $user_id,
		'zmieniono' => current_time( 'mysql' ),
	] );

	return [
		'ok' => true,
		'ostrzezenie' => agria_of_skok_o_rzad( $bylo, $grosze )
			? sprintf( 'Zmiana o rzad wielkosci: %s zl -> %s zl. Sprawdz, czy to nie pomylka.',
				number_format( (float) agria_of_na_zlote( $bylo ), 2, ',', ' ' ),
				number_format( (float) agria_of_na_zlote( $grosze ), 2, ',', ' ' ) )
			: null,
	];
}
