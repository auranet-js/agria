<?php
/**
 * Ustawienia transportu — wartosci STARTOWE, nie ustalenia z klientem.
 *
 * Cennik Pawla z 07.08.2026 dotyczy wylacznie towaru, loco magazyn — stawek przewozu w nim nie ma.
 * Liczby ponizej pochodza z notatki telefonicznej 18.08 i AGRIA nadpisuje je w module ustawien (§4.7).
 * Nie wolno ich nigdzie przedstawiac jako „danych od klienta".
 */

defined( 'ABSPATH' ) || exit;

const AGRIA_OF_OPCJA_TRANSPORT = 'agria_of_transport';
const AGRIA_OF_OPCJA_PALETA    = 'agria_of_paleta';

/**
 * `oba_kierunki` — czy kurs liczy sie w dwie strony. Beczka i wanna wracaja puste i AGRIA
 * placi za powrot; naczepa nie. Przy 200 km to roznica rzedu tysiaca zlotych na aucie,
 * wiec to nie jest szczegol konfiguracyjny.
 */
function agria_of_transport_domyslne(): array {
	return [
		'naczepa' => [
			'nazwa'        => 'Naczepa',
			'stawka_km'    => 550,   // grosze
			'oba_kierunki' => false,
			'ladownosc_kg' => 24000,
			'formy'        => [ 'worek', 'big-bag' ],
		],
		'beczka' => [
			'nazwa'        => 'Beczka silosowa',
			'stawka_km'    => 480,
			'oba_kierunki' => true,
			'ladownosc_kg' => 24000,
			'formy'        => [ 'luz' ],
		],
		'wanna' => [
			'nazwa'        => 'Wanna',
			'stawka_km'    => 420,
			'oba_kierunki' => true,
			'ladownosc_kg' => 24000,
			'formy'        => [ 'luz' ],
		],
		'kurier' => [
			'nazwa'        => 'Kurier paletowy',
			'stawka_paleta'=> 12000, // grosze za palete, stawka krajowa niezalezna od masy
			'oba_kierunki' => false,
			'ladownosc_kg' => null,
			'formy'        => [ 'worek', 'big-bag' ],
		],
	];
}

/**
 * Pojemnosc palety per forma dostawy.
 *
 * Do 22.08.2026 bylo to jedyne pytanie wymieniane wprost w rozpisce jako blokujace uruchomienie.
 * Decyzja Janka: to pole w ustawieniach, nie pytanie do Pawla — klient wpisze wlasna wartosc.
 * Ponizsze liczby sa NASZYM oszacowaniem z gramatur i typowej palety 1000 kg; oznaczone jako
 * `szacunek`, zeby ekran mogl to powiedziec wprost zamiast udawac pewnosc.
 */
function agria_of_paleta_domyslne(): array {
	return [
		'worek-10'   => [ 'sztuk' => 100, 'masa_kg' => 1000, 'szacunek' => true ],
		'worek-20'   => [ 'sztuk' => 50,  'masa_kg' => 1000, 'szacunek' => true ],
		'worek-25'   => [ 'sztuk' => 40,  'masa_kg' => 1000, 'szacunek' => true ],
		'worek-30'   => [ 'sztuk' => 33,  'masa_kg' => 990,  'szacunek' => true ],
		'worek-40'   => [ 'sztuk' => 25,  'masa_kg' => 1000, 'szacunek' => true ],
		'big-bag-500'  => [ 'sztuk' => 2, 'masa_kg' => 1000, 'szacunek' => true ],
		'big-bag-600'  => [ 'sztuk' => 1, 'masa_kg' => 600,  'szacunek' => true ],
		'big-bag-1000' => [ 'sztuk' => 1, 'masa_kg' => 1000, 'szacunek' => true ],
	];
}

function agria_of_ustawienia_zasiej(): void {
	add_option( AGRIA_OF_OPCJA_TRANSPORT, agria_of_transport_domyslne() );
	add_option( AGRIA_OF_OPCJA_PALETA, agria_of_paleta_domyslne() );
}

function agria_of_transport(): array {
	$z = get_option( AGRIA_OF_OPCJA_TRANSPORT );
	return is_array( $z ) && $z ? $z : agria_of_transport_domyslne();
}

function agria_of_paleta(): array {
	$z = get_option( AGRIA_OF_OPCJA_PALETA );
	return is_array( $z ) && $z ? $z : agria_of_paleta_domyslne();
}

/**
 * Czy nowa wartosc rozni sie od starej o rzad wielkosci.
 *
 * Wymog z §4.7: klient prowadzi cennik sam, a wpisane 57 zamiast 570 daje wycene dziesieciokrotnie
 * za tania i nikt sie nie zorientuje az do faktury. To ostrzezenie, nie blokada — tak samo
 * jak przy podlodze cenowej.
 */
function agria_of_skok_o_rzad( ?int $bylo, ?int $jest ): bool {
	if ( ! $bylo || ! $jest ) {
		return false;
	}
	$iloraz = max( $bylo, $jest ) / min( $bylo, $jest );
	return $iloraz >= 5;
}
