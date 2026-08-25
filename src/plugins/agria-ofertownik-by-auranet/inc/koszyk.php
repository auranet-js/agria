<?php
/**
 * Wycena WIELOPOZYCYJNA — kilka produktow na jedno zamowienie.
 *
 * Rzecz, ktora ujawnia sie dopiero przy wielu pozycjach i ktorej wersja jednopozycyjna
 * nie mogla pokazac: **auto jedzie z JEDNEGO zakladu**. Klient biorący Agrobielika z Sitkowki
 * i krede z Celin dostaje DWA transporty, nie jeden — i dopiero widzac to rozbicie handlowiec
 * wie, ze warto namowic na produkt z tego samego zakladu albo dopelnic auto.
 *
 * Dlatego pozycje grupuja sie po zakladzie, a kazda grupa to osobne auto z wlasnym
 * doborem metody, wlasnymi kursami i wlasnym dopelnieniem.
 */

defined( 'ABSPATH' ) || exit;

/**
 * Wycenia komplet pozycji.
 *
 * @param array $pozycje  lista: produkt_id, forma_klucz, ilosc, jednostka, frakcja,
 *                        opcjonalnie zaklad_term_id, cena_reczna
 * @param int   $mie_id   miejscowosc dostawy
 * @param array $opcje    stan_transportu, km_reczne per zaklad, metoda per zaklad
 */
function agria_of_wycen_koszyk( array $pozycje, int $mie_id, array $opcje = [] ): array {
	$wynik = [ 'pozycje' => [], 'grupy' => [], 'blad' => null ];

	foreach ( $pozycje as $klucz => $p ) {
		$produkt_id = (int) ( $p['produkt_id'] ?? 0 );
		$ilosc      = (float) str_replace( ',', '.', (string) ( $p['ilosc'] ?? 0 ) );
		if ( ! $produkt_id || $ilosc <= 0 ) {
			continue;
		}

		$formy = agria_of_formy_produktu( $produkt_id );
		$forma = $formy[ $p['forma_klucz'] ?? '' ] ?? ( $formy ? reset( $formy ) : null );
		if ( ! $forma ) {
			continue;
		}

		$ile     = agria_of_przelicz_ilosc( $ilosc, (string) ( $p['jednostka'] ?? 'tona' ), $forma );
		$frakcja = (string) ( $p['frakcja'] ?? '' );

		// Zaklad: wybrany recznie albo najblizszy z cena.
		$kandydaci = [];
		foreach ( agria_of_zaklady_produktu( $produkt_id ) as $z ) {
			$c   = agria_of_cena( $produkt_id, $z['term_id'], $forma['term_id'], $frakcja );
			$odl = $mie_id ? agria_of_odleglosc( $z['term_id'], $mie_id ) : [ 'km' => 0, 'zrodlo' => 'brak', 'pewne' => false ];
			$kandydaci[] = [
				'term_id'  => $z['term_id'],
				'nazwa'    => $z['nazwa'],
				'km'       => $odl['km'],
				'pewne'    => $odl['pewne'],
				'cena'     => $c && $c['cena'] !== null ? (int) $c['cena'] : null,
				'cena_min' => $c && $c['cena_min'] !== null ? (int) $c['cena_min'] : null,
			];
		}
		if ( ! $kandydaci ) {
			continue;
		}
		usort( $kandydaci, function ( $a, $b ) {
			if ( ( $a['cena'] === null ) !== ( $b['cena'] === null ) ) {
				return $a['cena'] === null ? 1 : -1;
			}
			return $a['km'] <=> $b['km'];
		} );

		$zaklad = $kandydaci[0];
		if ( ! empty( $p['zaklad_term_id'] ) ) {
			foreach ( $kandydaci as $k ) {
				if ( $k['term_id'] === (int) $p['zaklad_term_id'] ) {
					$zaklad = $k;
					break;
				}
			}
		}

		$cena = isset( $p['cena_reczna'] ) && $p['cena_reczna'] !== ''
			? (int) agria_of_na_grosze( $p['cena_reczna'] )
			: $zaklad['cena'];

		$wynik['pozycje'][ $klucz ] = [
			'klucz'            => $klucz,
			'produkt_id'       => $produkt_id,
			'produkt'          => agria_of_tytul_produktu( $produkt_id ),
			'sku'              => get_post_meta( $produkt_id, '_sku', true ),
			'forma'            => $forma,
			'formy'            => array_values( array_map( fn( $f ) => [ 'klucz' => $f['klucz'], 'nazwa' => $f['nazwa'] ], $formy ) ),
			'ilosc'            => $ilosc,
			'jednostka'        => (string) ( $p['jednostka'] ?? 'tona' ),
			'frakcja'          => $frakcja,
			'tony'             => $ile['tony'],
			'palet'            => $ile['palet'],
			'zaklad'           => $zaklad,
			'zaklady'          => $kandydaci,
			'cena'             => $cena,
			'cena_proponowana' => $zaklad['cena'],
			'cena_min'         => $zaklad['cena_min'],
			'ponizej_podlogi'  => $zaklad['cena_min'] !== null && $cena !== null && $cena < $zaklad['cena_min'],
			'wartosc'          => $cena !== null ? (int) round( $cena * $ile['tony'] ) : 0,
			'brak_ceny'        => $cena === null,
		];
	}

	if ( ! $wynik['pozycje'] ) {
		return $wynik + [ 'towar' => 0, 'transport' => 0, 'razem' => 0, 'tony' => 0 ];
	}

	// --- grupowanie po zakladzie: jedna grupa = jedno auto ---------------------
	$grupy = [];
	foreach ( $wynik['pozycje'] as $p ) {
		$z = $p['zaklad']['term_id'];
		if ( ! isset( $grupy[ $z ] ) ) {
			$grupy[ $z ] = [
				'zaklad_term_id' => $z,
				'zaklad'         => $p['zaklad']['nazwa'],
				'km'             => $p['zaklad']['km'],
				'km_pewne'       => $p['zaklad']['pewne'],
				'tony'           => 0,
				'palet'          => 0,
				'pozycje'        => [],
				'rodzaje'        => [],
			];
		}
		$grupy[ $z ]['tony']     += $p['tony'];
		$grupy[ $z ]['palet']    += (int) $p['palet'];
		$grupy[ $z ]['pozycje'][] = $p['klucz'];
		$grupy[ $z ]['rodzaje'][ $p['forma']['rodzaj'] ] = true;
	}

	$stan = (string) ( $opcje['stan_transportu'] ?? 'wyliczony' );

	foreach ( $grupy as $z => &$g ) {
		$g['tony']  = round( $g['tony'], 3 );
		$g['palet'] = $g['palet'] ?: null;

		// Km moze nadpisac handlowiec — awaria routera nie moze zatrzymac wyceny.
		if ( isset( $opcje['km'][ $z ] ) && $opcje['km'][ $z ] !== '' ) {
			$g['km']       = (int) $opcje['km'][ $z ];
			$g['km_pewne'] = true;
			$g['km_reczne'] = true;
		}

		// Luz i palety w jednym aucie to dwa rozne pojazdy — liczymy po rodzaju,
		// ktory w tej grupie dominuje tonazem, i mowimy o tym wprost.
		$rodzaj = isset( $g['rodzaje']['luz'] ) ? 'luz' : array_key_first( $g['rodzaje'] );
		$g['mieszana'] = count( $g['rodzaje'] ) > 1;

		$metody = agria_of_metody_dla_formy(
			[ 'rodzaj' => $rodzaj, 'klucz' => $rodzaj ],
			(int) $g['km'], $g['tony'], $g['palet']
		);
		$metoda = $metody[0] ?? null;
		if ( ! empty( $opcje['metoda'][ $z ] ) ) {
			foreach ( $metody as $m ) {
				if ( $m['metoda'] === $opcje['metoda'][ $z ] ) {
					$metoda = $m;
					break;
				}
			}
		}

		$koszt = $metoda ? $metoda['koszt'] : 0;
		if ( in_array( $stan, [ 'gratis', 'odbior' ], true ) ) {
			$koszt = 0;
		}
		if ( isset( $opcje['transport'][ $z ] ) && $opcje['transport'][ $z ] !== '' ) {
			$koszt = (int) agria_of_na_grosze( $opcje['transport'][ $z ] );
		}

		$g['metoda']  = $metoda;
		$g['metody']  = $metody;
		$g['koszt']   = $koszt;
		$g['za_tone'] = $g['tony'] > 0 ? (int) round( $koszt / $g['tony'] ) : 0;

		// Dopelnienie auta — liczone per auto, bo per auto sie placi.
		$g['dopelnienie'] = null;
		$t = agria_of_transport();
		if ( $metoda && ! empty( $t[ $metoda['metoda'] ]['ladownosc_kg'] ) && $koszt > 0 ) {
			$ladownosc = $t[ $metoda['metoda'] ]['ladownosc_kg'] / 1000;
			$pelne     = $ladownosc * $metoda['kursy'];
			$g['ladownosc'] = $ladownosc;
			$g['wypelnienie'] = min( 1, $g['tony'] / max( $pelne, 0.001 ) );
			if ( $g['tony'] < $pelne - 0.01 ) {
				$pelny = agria_of_koszt_metody( $metoda['metoda'], $t[ $metoda['metoda'] ], (int) $g['km'], $pelne, $g['palet'] );
				$g['dopelnienie'] = [
					'brakuje' => round( $pelne - $g['tony'], 2 ),
					'pelne'   => round( $pelne, 2 ),
					'teraz'   => $g['za_tone'],
					'potem'   => (int) round( ( $pelny['koszt'] ?? $koszt ) / $pelne ),
				];
			}
		}
	}
	unset( $g );

	$towar     = array_sum( array_column( $wynik['pozycje'], 'wartosc' ) );
	$transport = array_sum( array_column( $grupy, 'koszt' ) );
	$tony      = round( array_sum( array_column( $wynik['pozycje'], 'tony' ) ), 3 );

	$wynik['grupy']     = array_values( $grupy );
	$wynik['towar']     = $towar;
	$wynik['transport'] = $transport;
	$wynik['razem']     = $towar + $transport;
	$wynik['tony']      = $tony;
	$wynik['za_tone']   = $tony > 0 ? (int) round( ( $towar + $transport ) / $tony ) : 0;
	$wynik['stan_transportu'] = $stan;
	$wynik['bez_ceny']  = count( array_filter( $wynik['pozycje'], fn( $p ) => $p['brak_ceny'] ) );

	return $wynik;
}
