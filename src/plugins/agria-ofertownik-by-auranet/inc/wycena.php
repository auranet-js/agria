<?php
/**
 * Logika wyceny — czysta kalkulacja, bez wyjscia na ekran.
 *
 * Cala wartosc narzedzia siedzi w tym pliku: zlozeniu ceny towaru z kosztem przewozu
 * z WLASCIWEGO zakladu. Ten sam adres dostawy ma inny koszt zaleznie od tego, skad towar wyjezdza —
 * Radom to 90 km z Sitkowki albo 250 km z Niedomic. Dlatego transport nie liczy sie strefami WooCommerce.
 */

defined( 'ABSPATH' ) || exit;

/**
 * Ile ton wazy zamowienie podane w jednostce klienta.
 *
 * Klient mowi „dziesiec workow" albo „trzy big-bagi", cena liczy sie na tony.
 *
 * @return array{tony:float, palet:?int}
 */
function agria_of_przelicz_ilosc( float $ile, string $jednostka, array $forma ): array {
	$paleta = agria_of_paleta();
	$klucz  = $forma['klucz'];

	if ( $jednostka === 'tona' ) {
		$tony = $ile;
	} elseif ( $jednostka === 'sztuka' && $forma['kg'] ) {
		$tony = $ile * $forma['kg'] / 1000;
	} else {
		$tony = $ile;
	}

	// Palety licza sie TYLKO dla form paletowych. Luz jedzie luzem i palety nie zna.
	$palet = null;
	if ( $forma['rodzaj'] !== 'luz' && isset( $paleta[ $klucz ] ) ) {
		$na_palecie = max( 1, (int) $paleta[ $klucz ]['sztuk'] );
		$sztuk      = $jednostka === 'sztuka' ? $ile : ( $forma['kg'] ? $tony * 1000 / $forma['kg'] : 0 );
		// Palety nie da sie wypelnic w polowie — zaokraglamy w gore, zawsze.
		$palet = (int) max( 1, ceil( $sztuk / $na_palecie ) );
	}

	return [ 'tony' => round( $tony, 3 ), 'palet' => $palet ];
}

/**
 * Koszt przewozu jedna metoda.
 *
 * @return array{metoda:string, nazwa:string, koszt:int, kursy:int, opis:string}|null
 */
function agria_of_koszt_metody( string $klucz, array $metoda, int $km, float $tony, ?int $palet ): ?array {
	if ( isset( $metoda['stawka_paleta'] ) ) {
		if ( ! $palet ) {
			return null; // kurier nie wozi luzu — nie ma czego postawic na palecie
		}
		return [
			'metoda' => $klucz,
			'nazwa'  => $metoda['nazwa'],
			'koszt'  => (int) $metoda['stawka_paleta'] * $palet,
			'kursy'  => 1,
			'opis'   => sprintf( '%d × %s zł za paletę', $palet, number_format( (float) agria_of_na_zlote( (int) $metoda['stawka_paleta'] ), 2, ',', ' ' ) ),
		];
	}

	if ( empty( $metoda['stawka_km'] ) || empty( $metoda['ladownosc_kg'] ) ) {
		return null;
	}
	$ladownosc_t = $metoda['ladownosc_kg'] / 1000;
	$kursy       = (int) max( 1, ceil( $tony / $ladownosc_t ) );
	$mnoznik     = ! empty( $metoda['oba_kierunki'] ) ? 2 : 1;
	$koszt       = (int) round( $km * (int) $metoda['stawka_km'] * $mnoznik * $kursy );

	return [
		'metoda' => $klucz,
		'nazwa'  => $metoda['nazwa'],
		'koszt'  => $koszt,
		'kursy'  => $kursy,
		'opis'   => sprintf( '%d km × %s zł%s%s', $km,
			number_format( (float) agria_of_na_zlote( (int) $metoda['stawka_km'] ), 2, ',', ' ' ),
			$mnoznik === 2 ? ' × 2 (w dwie strony)' : '',
			$kursy > 1 ? " × {$kursy} kursy" : '' ),
	];
}

/**
 * Metody dostepne dla danej formy, posortowane od najtanszej.
 *
 * Formy paletowe maja DWIE metody naraz — naczepe i kuriera — i rozstrzygamy je bez progu:
 * liczymy oba warianty i pokazujemy tanszy. Zero regul do zapamietania przez handlowca.
 * Punkt zrownania wypada przy `liczba palet = km / 21,8`, czyli przy 70 km naczepa przejmuje
 * od czwartej palety, a przy 250 km dopiero od dwunastej.
 */
function agria_of_metody_dla_formy( array $forma, int $km, float $tony, ?int $palet ): array {
	$out = [];
	foreach ( agria_of_transport() as $klucz => $metoda ) {
		if ( ! in_array( $forma['rodzaj'], (array) $metoda['formy'], true ) ) {
			continue;
		}
		$w = agria_of_koszt_metody( $klucz, $metoda, $km, $tony, $palet );
		if ( $w ) {
			$out[] = $w;
		}
	}
	usort( $out, fn( $a, $b ) => $a['koszt'] <=> $b['koszt'] );
	return $out;
}

/**
 * Pelna wycena.
 *
 * @param array $wejscie  produkt_id, miejscowosc_id, forma_klucz, ilosc, jednostka,
 *                        opcjonalnie: zaklad_term_id, frakcja, metoda, km (nadpisanie reczne)
 */
function agria_of_wycen( array $wejscie ): array {
	$produkt_id = (int) ( $wejscie['produkt_id'] ?? 0 );
	$mie_id     = (int) ( $wejscie['miejscowosc_id'] ?? 0 );
	$blad       = null;

	$formy = agria_of_formy_produktu( $produkt_id );
	$forma = $formy[ $wejscie['forma_klucz'] ?? '' ] ?? null;
	if ( ! $forma ) {
		return [ 'blad' => 'Nie znam tej formy dostawy dla wybranego produktu.' ];
	}

	$ilosc = agria_of_przelicz_ilosc(
		(float) ( $wejscie['ilosc'] ?? 0 ),
		(string) ( $wejscie['jednostka'] ?? 'tona' ),
		$forma
	);
	if ( $ilosc['tony'] <= 0 ) {
		return [ 'blad' => 'Podaj ilość.' ];
	}

	// --- dobor zakladu -------------------------------------------------------
	// Sposrod zakladow, ktore maja ten produkt w tej formie, bierzemy najblizszy trasa.
	// Handlowiec widzi wybor i moze go zmienic — o dostepnosci towaru wie wiecej niz narzedzie.
	$kandydaci = [];
	foreach ( agria_of_zaklady_produktu( $produkt_id ) as $z ) {
		$cena = agria_of_cena( $produkt_id, $z['term_id'], $forma['term_id'], (string) ( $wejscie['frakcja'] ?? '' ) );
		$odl  = $mie_id ? agria_of_odleglosc( $z['term_id'], $mie_id ) : [ 'km' => 0, 'zrodlo' => 'brak', 'pewne' => false ];
		$kandydaci[] = [
			'term_id' => $z['term_id'],
			'nazwa'   => $z['nazwa'],
			'km'      => $odl['km'],
			'zrodlo'  => $odl['zrodlo'],
			'pewne'   => $odl['pewne'],
			'cena'    => $cena && $cena['cena'] !== null ? (int) $cena['cena'] : null,
			'cena_min'=> $cena && $cena['cena_min'] !== null ? (int) $cena['cena_min'] : null,
		];
	}
	if ( ! $kandydaci ) {
		return [ 'blad' => 'Ten produkt nie ma przypisanego żadnego zakładu wysyłkowego.' ];
	}

	// Zaklady bez ceny ida na koniec — nie chcemy wybrac najblizszego, ktorego nie umiemy wycenic.
	usort( $kandydaci, function ( $a, $b ) {
		if ( ( $a['cena'] === null ) !== ( $b['cena'] === null ) ) {
			return $a['cena'] === null ? 1 : -1;
		}
		return $a['km'] <=> $b['km'];
	} );

	$wybrany = $kandydaci[0];
	if ( ! empty( $wejscie['zaklad_term_id'] ) ) {
		foreach ( $kandydaci as $k ) {
			if ( $k['term_id'] === (int) $wejscie['zaklad_term_id'] ) {
				$wybrany = $k;
				break;
			}
		}
	}

	$km = isset( $wejscie['km'] ) && $wejscie['km'] !== '' ? (int) $wejscie['km'] : (int) $wybrany['km'];
	$km_reczne = isset( $wejscie['km'] ) && $wejscie['km'] !== '';

	// --- transport -----------------------------------------------------------
	$metody = agria_of_metody_dla_formy( $forma, $km, $ilosc['tony'], $ilosc['palet'] );
	$metoda = $metody[0] ?? null;
	if ( ! empty( $wejscie['metoda'] ) ) {
		foreach ( $metody as $m ) {
			if ( $m['metoda'] === $wejscie['metoda'] ) {
				$metoda = $m;
				break;
			}
		}
	}

	$stan_transportu = (string) ( $wejscie['stan_transportu'] ?? 'wyliczony' );
	$koszt_transportu = $metoda ? $metoda['koszt'] : 0;
	if ( in_array( $stan_transportu, [ 'gratis', 'odbior' ], true ) ) {
		$koszt_transportu = 0;
	}
	if ( isset( $wejscie['transport_reczny'] ) && $wejscie['transport_reczny'] !== '' ) {
		$koszt_transportu = (int) agria_of_na_grosze( $wejscie['transport_reczny'] );
	}

	// --- towar ---------------------------------------------------------------
	$cena_t = isset( $wejscie['cena_reczna'] ) && $wejscie['cena_reczna'] !== ''
		? (int) agria_of_na_grosze( $wejscie['cena_reczna'] )
		: $wybrany['cena'];

	if ( $cena_t === null ) {
		$blad = 'Brak ceny — ustal z Pawłem.';
	}

	$wartosc_towaru = $cena_t !== null ? (int) round( $cena_t * $ilosc['tony'] ) : 0;
	$razem          = $wartosc_towaru + $koszt_transportu;

	// --- dopelnienie auta ----------------------------------------------------
	// Przewoz placi sie za pojazd, nie za tone. To jedyny element calosci, ktory sam z siebie
	// podnosi wartosc zamowienia — handlowiec dostaje gotowy argument zamiast liczyc go w pamieci.
	$dopelnienie = null;
	if ( $metoda && ! empty( agria_of_transport()[ $metoda['metoda'] ]['ladownosc_kg'] ) && $koszt_transportu > 0 ) {
		$ladownosc_t = agria_of_transport()[ $metoda['metoda'] ]['ladownosc_kg'] / 1000;
		$pelne       = $ladownosc_t * $metoda['kursy'];
		if ( $ilosc['tony'] < $pelne - 0.01 ) {
			$brakuje       = $pelne - $ilosc['tony'];
			$transport_pel = agria_of_koszt_metody( $metoda['metoda'], agria_of_transport()[ $metoda['metoda'] ], $km, $pelne, $ilosc['palet'] );
			$dopelnienie = [
				'brakuje_t'      => round( $brakuje, 2 ),
				'pelne_t'        => round( $pelne, 2 ),
				'teraz_za_tone'  => (int) round( $koszt_transportu / $ilosc['tony'] ),
				'potem_za_tone'  => (int) round( ( $transport_pel['koszt'] ?? $koszt_transportu ) / $pelne ),
			];
		}
	}

	$ponizej_podlogi = $wybrany['cena_min'] !== null && $cena_t !== null && $cena_t < $wybrany['cena_min'];

	return [
		'blad'             => $blad,
		'forma'            => $forma,
		'tony'             => $ilosc['tony'],
		'palet'            => $ilosc['palet'],
		'zaklad'           => $wybrany,
		'zaklady'          => $kandydaci,
		'km'               => $km,
		'km_reczne'        => $km_reczne,
		'km_pewne'         => $km_reczne ? true : $wybrany['pewne'],
		'metoda'           => $metoda,
		'metody'           => $metody,
		'stan_transportu'  => $stan_transportu,
		'cena_t'           => $cena_t,
		'cena_proponowana' => $wybrany['cena'],
		'cena_min'         => $wybrany['cena_min'],
		'ponizej_podlogi'  => $ponizej_podlogi,
		'wartosc_towaru'   => $wartosc_towaru,
		'transport'        => $koszt_transportu,
		'za_tone_z_dostawa'=> $ilosc['tony'] > 0 ? (int) round( $razem / $ilosc['tony'] ) : 0,
		'razem'            => $razem,
		'dopelnienie'      => $dopelnienie,
	];
}
