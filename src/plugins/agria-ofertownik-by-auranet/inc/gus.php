<?php
/**
 * Dane platnika z rejestru REGON (GUS BIR1.1).
 *
 * Handlowiec wpisuje NIP, reszta danych do faktury zaciaga sie sama. Rolnik przez telefon
 * i tak nie podyktuje poprawnie nazwy spolki ani adresu, a blad w tych polach wraca
 * jako korekta faktury.
 *
 * Uwaga na sesje: GUS wydaje `sid` wazny okolo godziny bez aktywnosci i NIE lubi
 * logowania przy kazdym zapytaniu. Trzymamy go w transiencie i logujemy sie ponownie
 * dopiero, gdy przestanie dzialac.
 */

defined( 'ABSPATH' ) || exit;

const AGRIA_OF_GUS_URL     = 'https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc';
const AGRIA_OF_GUS_OPCJA   = 'agria_of_gus_klucz';
const AGRIA_OF_GUS_SESJA   = 'agria_of_gus_sid';

function agria_of_gus_klucz(): string {
	return (string) get_option( AGRIA_OF_GUS_OPCJA, '' );
}

function agria_of_gus_zapytaj( string $akcja, string $cialo, string $sid = '' ) {
	$naglowki = [
		'Content-Type' => 'application/soap+xml; charset=utf-8',
	];
	if ( $sid ) {
		$naglowki['sid'] = $sid;
	}
	// Uwaga na przestrzenie nazw: operacje siedza w `PUBL`, ale PARAMETRY WYSZUKIWANIA
	// w `PUBL/2014/07/DataContract`. Zapytanie z <ns:Nip> zamiast <dat:Nip> przechodzi
	// bez bledu HTTP i zwraca PUSTY wynik — czyli wyglada dokladnie jak „nie ma takiej firmy".
	$koperta = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'
		. ' xmlns:ns="http://CIS/BIR/PUBL/2014/07"'
		. ' xmlns:dat="http://CIS/BIR/PUBL/2014/07/DataContract">'
		. '<soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">'
		. '<wsa:To>' . AGRIA_OF_GUS_URL . '</wsa:To>'
		. '<wsa:Action>http://CIS/BIR/PUBL/2014/07/IUslugaBIRzewnPubl/' . $akcja . '</wsa:Action>'
		. '</soap:Header><soap:Body>' . $cialo . '</soap:Body></soap:Envelope>';

	$odp = wp_remote_post( AGRIA_OF_GUS_URL, [
		'timeout' => 12,
		'headers' => $naglowki,
		'body'    => $koperta,
	] );
	if ( is_wp_error( $odp ) ) {
		return $odp;
	}
	return wp_remote_retrieve_body( $odp );
}

function agria_of_gus_sid( bool $odswiez = false ): string {
	if ( ! $odswiez ) {
		$sid = get_transient( AGRIA_OF_GUS_SESJA );
		if ( $sid ) {
			return (string) $sid;
		}
	}
	$klucz = agria_of_gus_klucz();
	if ( ! $klucz ) {
		return '';
	}
	$body = agria_of_gus_zapytaj( 'Zaloguj', '<ns:Zaloguj><ns:pKluczUzytkownika>' . esc_html( $klucz ) . '</ns:pKluczUzytkownika></ns:Zaloguj>' );
	if ( is_wp_error( $body ) || ! preg_match( '#<ZalogujResult>([^<]+)</ZalogujResult>#', (string) $body, $m ) ) {
		return '';
	}
	$sid = trim( $m[1] );
	if ( $sid ) {
		set_transient( AGRIA_OF_GUS_SESJA, $sid, 45 * MINUTE_IN_SECONDS );
	}
	return $sid;
}

/**
 * Dane firmy po NIP.
 *
 * @return array{nazwa:string,ulica:string,kod:string,miejscowosc:string,regon:string,adres:string}|null
 */
function agria_of_gus_po_nip( string $nip ): ?array {
	$nip = preg_replace( '/\D+/', '', $nip );
	if ( strlen( $nip ) !== 10 ) {
		return null;
	}
	$cache = get_transient( 'agria_of_gus_' . $nip );
	if ( is_array( $cache ) ) {
		return $cache;
	}

	$szukaj = function ( string $sid ) use ( $nip ) {
		return agria_of_gus_zapytaj( 'DaneSzukajPodmioty',
			'<ns:DaneSzukajPodmioty><ns:pParametryWyszukiwania><dat:Nip>' . $nip . '</dat:Nip></ns:pParametryWyszukiwania></ns:DaneSzukajPodmioty>',
			$sid );
	};

	$sid  = agria_of_gus_sid();
	$body = $sid ? $szukaj( $sid ) : '';
	// Wygasla sesja oddaje pusty wynik zamiast bledu — logujemy sie raz jeszcze, zanim odpuscimy.
	if ( ! $sid || is_wp_error( $body ) || ! str_contains( (string) $body, '<Nazwa>' ) ) {
		$sid = agria_of_gus_sid( true );
		if ( ! $sid ) {
			return null;
		}
		$body = $szukaj( $sid );
	}
	if ( is_wp_error( $body ) ) {
		return null;
	}

	$xml = html_entity_decode( (string) $body, ENT_QUOTES | ENT_XML1, 'UTF-8' );
	$pole = function ( string $nazwa ) use ( $xml ): string {
		return preg_match( "#<{$nazwa}>([^<]*)</{$nazwa}>#u", $xml, $m ) ? trim( $m[1] ) : '';
	};

	$nazwa = $pole( 'Nazwa' );
	if ( ! $nazwa ) {
		return null;
	}

	$ulica = trim( $pole( 'Ulica' ) . ' ' . $pole( 'NrNieruchomosci' )
		. ( $pole( 'NrLokalu' ) ? '/' . $pole( 'NrLokalu' ) : '' ) );

	$dane = [
		'nazwa'       => $nazwa,
		'ulica'       => $ulica,
		'kod'         => $pole( 'KodPocztowy' ),
		'miejscowosc' => $pole( 'Miejscowosc' ),
		'regon'       => $pole( 'Regon' ),
		'nip'         => $nip,
	];
	$dane['adres'] = trim( sprintf( '%s, %s %s', $ulica, $dane['kod'], $dane['miejscowosc'] ), ', ' );

	set_transient( 'agria_of_gus_' . $nip, $dane, WEEK_IN_SECONDS );
	return $dane;
}

add_action( 'wp_ajax_agria_of_gus', function (): void {
	check_ajax_referer( 'agria_of' );
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_send_json_error( [], 403 );
	}
	if ( ! agria_of_gus_klucz() ) {
		wp_send_json_error( [ 'blad' => 'Brak klucza GUS — uzupełnij w Ofertownik → Transport.' ] );
	}
	$dane = agria_of_gus_po_nip( sanitize_text_field( $_GET['nip'] ?? '' ) );
	if ( ! $dane ) {
		wp_send_json_error( [ 'blad' => 'Nie znaleziono firmy o tym NIP.' ] );
	}
	wp_send_json_success( $dane );
} );
