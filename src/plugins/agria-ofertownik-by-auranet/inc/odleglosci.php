<?php
/**
 * Miejscowosci, wspolrzedne zakladow i odleglosci DROGOWE.
 *
 * Dwie rzeczy, ktore trzeba tu rozumiec, bo obie kosztuja pieniadze:
 *
 * 1. ODLEGLOSC MUSI BYC DROGOWA. Siatka policzona przy OLX (`scripts/olx/grid.py`) liczy po ortodromie
 *    i sama to deklaruje: „wystarczajaco dokladna dla decyzji o zasiegu dostawy". Do faktury nie jest.
 *    Zmierzone 22.08.2026 na trasie Sitkowka -> Mlawa: 255 km w linii prostej, **327 km droga** (+28%).
 *    Przy wannie liczonej w dwie strony ta roznica to **605 zl na jednym aucie**.
 *
 * 2. NIE MA ZEWNETRZNEJ ZALEZNOSCI, KTORA ZATRZYMUJE SPRZEDAZ. Gdy router nie odpowiada, liczymy
 *    ortodrome z narzutem i mowimy wprost, ze to szacunek. Handlowiec moze tez wpisac kilometry recznie.
 *    Awaria cudzej uslugi nie moze konczyc rozmowy z klientem.
 *
 * Podpowiadanie miejscowosci idzie z WLASNEJ tabeli (53 247 miejscowosci z danych OLX) — bez Google Places,
 * bez klucza API, bez billingu i bez sekretu na serwerze klienta.
 */

defined( 'ABSPATH' ) || exit;

/** Narzut na ortodrome, gdy nie znamy trasy. Zmierzony, nie przyjety — patrz naglowek. */
const AGRIA_OF_NARZUT_TRASY = 1.28;

function agria_of_db_utworz_tabele_geo(): void {
	global $wpdb;
	require_once ABSPATH . 'wp-admin/includes/upgrade.php';
	$collate = $wpdb->get_charset_collate();

	dbDelta( "CREATE TABLE " . agria_of_tabela( 'miejscowosci' ) . " (
		id BIGINT UNSIGNED NOT NULL,
		nazwa VARCHAR(120) NOT NULL,
		powiat VARCHAR(120) NOT NULL DEFAULT '',
		gmina VARCHAR(120) NOT NULL DEFAULT '',
		wojewodztwo VARCHAR(40) NOT NULL DEFAULT '',
		lat DECIMAL(9,5) NOT NULL,
		lon DECIMAL(9,5) NOT NULL,
		PRIMARY KEY (id),
		KEY nazwa (nazwa(32))
	) {$collate};" );

	dbDelta( "CREATE TABLE " . agria_of_tabela( 'trasy' ) . " (
		id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
		zaklad_term_id BIGINT UNSIGNED NOT NULL,
		miejscowosc_id BIGINT UNSIGNED NOT NULL,
		km INT UNSIGNED NOT NULL,
		zrodlo VARCHAR(20) NOT NULL DEFAULT 'osrm',
		policzono DATETIME NOT NULL,
		PRIMARY KEY (id),
		UNIQUE KEY para (zaklad_term_id, miejscowosc_id)
	) {$collate};" );
}

/** Jednorazowy zasiew miejscowosci z pliku w katalogu wtyczki. */
function agria_of_zasiej_miejscowosci(): int {
	global $wpdb;
	$tab  = agria_of_tabela( 'miejscowosci' );
	if ( (int) $wpdb->get_var( "SELECT COUNT(*) FROM {$tab}" ) > 50000 ) {
		return 0;
	}
	$plik = AGRIA_OF_DIR . 'dane/miejscowosci.csv.gz';
	if ( ! file_exists( $plik ) ) {
		return 0;
	}
	$fh = gzopen( $plik, 'rb' );
	fgetcsv( $fh ); // naglowek
	$n = 0;
	$paczka = [];
	while ( ( $r = fgetcsv( $fh ) ) !== false ) {
		$paczka[] = $wpdb->prepare( '(%d,%s,%s,%s,%s,%f,%f)', $r[0], $r[1], $r[2], $r[3], $r[4], $r[5], $r[6] );
		if ( count( $paczka ) >= 500 ) {
			$wpdb->query( "INSERT IGNORE INTO {$tab} (id,nazwa,powiat,gmina,wojewodztwo,lat,lon) VALUES " . implode( ',', $paczka ) );
			$n += count( $paczka );
			$paczka = [];
		}
	}
	if ( $paczka ) {
		$wpdb->query( "INSERT IGNORE INTO {$tab} (id,nazwa,powiat,gmina,wojewodztwo,lat,lon) VALUES " . implode( ',', $paczka ) );
		$n += count( $paczka );
	}
	gzclose( $fh );
	return $n;
}

/** Podpowiedzi miejscowosci — prefiks wazniejszy niz trafienie w srodku nazwy. */
function agria_of_szukaj_miejscowosci( string $fraza, int $limit = 12 ): array {
	global $wpdb;
	$fraza = trim( $fraza );
	if ( mb_strlen( $fraza ) < 2 ) {
		return [];
	}
	$tab = agria_of_tabela( 'miejscowosci' );
	return $wpdb->get_results( $wpdb->prepare(
		"SELECT id, nazwa, powiat, wojewodztwo, lat, lon,
		        CASE WHEN nazwa LIKE %s THEN 0 ELSE 1 END AS waga
		 FROM {$tab}
		 WHERE nazwa LIKE %s
		 ORDER BY waga, CHAR_LENGTH(nazwa), nazwa
		 LIMIT %d",
		$wpdb->esc_like( $fraza ) . '%',
		'%' . $wpdb->esc_like( $fraza ) . '%',
		$limit
	), ARRAY_A );
}

function agria_of_miejscowosc( int $id ): ?array {
	global $wpdb;
	$w = $wpdb->get_row( $wpdb->prepare( 'SELECT * FROM ' . agria_of_tabela( 'miejscowosci' ) . ' WHERE id=%d', $id ), ARRAY_A );
	return $w ?: null;
}

/**
 * Wspolrzedne zakladu z meta termu.
 *
 * Zasiew dopasowuje nazwe zakladu do bazy miejscowosci — dokladniej niz wartosci wpisane recznie
 * w `grid.py`, gdzie wspolrzedne byly zaokraglone do trzech miejsc (czyli do ~100 m) i wskazywaly
 * srodek gminy, nie punkt zaladunku.
 */
function agria_of_wspolrzedne_zakladu( int $term_id ): ?array {
	$lat = get_term_meta( $term_id, 'agria_of_lat', true );
	$lon = get_term_meta( $term_id, 'agria_of_lon', true );
	return ( $lat && $lon ) ? [ 'lat' => (float) $lat, 'lon' => (float) $lon ] : null;
}

function agria_of_zasiej_wspolrzedne_zakladow(): array {
	global $wpdb;
	$tab    = agria_of_tabela( 'miejscowosci' );
	$wynik  = [];
	$termy  = get_terms( [ 'taxonomy' => AGRIA_OF_TAX_ZAKLAD, 'hide_empty' => true ] );

	foreach ( $termy as $t ) {
		if ( agria_of_wspolrzedne_zakladu( $t->term_id ) ) {
			$wynik[ $t->name ] = 'juz bylo';
			continue;
		}
		$nazwa = agria_of_nazwa_zakladu( $t->name );
		$m = $wpdb->get_row( $wpdb->prepare(
			"SELECT * FROM {$tab} WHERE nazwa=%s ORDER BY CHAR_LENGTH(nazwa) LIMIT 1", $nazwa
		), ARRAY_A );
		if ( ! $m ) {
			$m = $wpdb->get_row( $wpdb->prepare(
				"SELECT * FROM {$tab} WHERE nazwa LIKE %s ORDER BY CHAR_LENGTH(nazwa) LIMIT 1",
				$wpdb->esc_like( $nazwa ) . '%'
			), ARRAY_A );
		}
		if ( $m ) {
			update_term_meta( $t->term_id, 'agria_of_lat', $m['lat'] );
			update_term_meta( $t->term_id, 'agria_of_lon', $m['lon'] );
			$wynik[ $t->name ] = "{$m['nazwa']} ({$m['wojewodztwo']}) {$m['lat']}, {$m['lon']}";
		} else {
			$wynik[ $t->name ] = 'NIE DOPASOWANO — wpisz recznie';
		}
	}
	return $wynik;
}

function agria_of_ortodroma( float $lat1, float $lon1, float $lat2, float $lon2 ): float {
	$r = 6371.0;
	[ $la1, $lo1, $la2, $lo2 ] = array_map( 'deg2rad', [ $lat1, $lon1, $lat2, $lon2 ] );
	$a = sin( ( $la2 - $la1 ) / 2 ) ** 2 + cos( $la1 ) * cos( $la2 ) * sin( ( $lo2 - $lo1 ) / 2 ) ** 2;
	return $r * 2 * asin( sqrt( $a ) );
}

/**
 * Odleglosc drogowa zaklad -> miejscowosc, w kilometrach.
 *
 * Para liczy sie RAZ i zostaje w tabeli — drugi telefon z tej samej gminy odpowiada natychmiast.
 * Nie chodzi o oszczednosc zapytan, tylko o to, zeby ekran nie kazal czekac w trakcie rozmowy.
 *
 * @return array{km:int, zrodlo:string, pewne:bool}
 */
function agria_of_odleglosc( int $zaklad_term_id, int $miejscowosc_id ): array {
	global $wpdb;
	$tab = agria_of_tabela( 'trasy' );

	$z = $wpdb->get_row( $wpdb->prepare(
		"SELECT km, zrodlo FROM {$tab} WHERE zaklad_term_id=%d AND miejscowosc_id=%d",
		$zaklad_term_id, $miejscowosc_id
	), ARRAY_A );
	if ( $z ) {
		return [ 'km' => (int) $z['km'], 'zrodlo' => $z['zrodlo'], 'pewne' => $z['zrodlo'] === 'osrm' ];
	}

	$zak = agria_of_wspolrzedne_zakladu( $zaklad_term_id );
	$mie = agria_of_miejscowosc( $miejscowosc_id );
	if ( ! $zak || ! $mie ) {
		return [ 'km' => 0, 'zrodlo' => 'brak', 'pewne' => false ];
	}

	$km     = null;
	$zrodlo = 'szacunek';

	$url = sprintf(
		'https://router.project-osrm.org/route/v1/driving/%F,%F;%F,%F?overview=false',
		$zak['lon'], $zak['lat'], (float) $mie['lon'], (float) $mie['lat']
	);
	$odp = wp_remote_get( $url, [ 'timeout' => 8, 'headers' => [ 'User-Agent' => 'agria-ofertownik/0.1 (auranet.com.pl)' ] ] );
	if ( ! is_wp_error( $odp ) && wp_remote_retrieve_response_code( $odp ) === 200 ) {
		$dane = json_decode( wp_remote_retrieve_body( $odp ), true );
		if ( ( $dane['code'] ?? '' ) === 'Ok' && isset( $dane['routes'][0]['distance'] ) ) {
			$km     = (int) round( $dane['routes'][0]['distance'] / 1000 );
			$zrodlo = 'osrm';
		}
	}

	if ( $km === null ) {
		// Router milczy — liczymy sami i MOWIMY, ze to szacunek. Sprzedaz idzie dalej.
		$km = (int) round( agria_of_ortodroma( $zak['lat'], $zak['lon'], (float) $mie['lat'], (float) $mie['lon'] ) * AGRIA_OF_NARZUT_TRASY );
	}

	$wpdb->replace( $tab, [
		'zaklad_term_id' => $zaklad_term_id,
		'miejscowosc_id' => $miejscowosc_id,
		'km'             => $km,
		'zrodlo'         => $zrodlo,
		'policzono'      => current_time( 'mysql' ),
	] );

	return [ 'km' => $km, 'zrodlo' => $zrodlo, 'pewne' => $zrodlo === 'osrm' ];
}
