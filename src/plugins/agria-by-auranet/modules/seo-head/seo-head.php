<?php
/**
 * Moduł: SEO / <head> cleanup
 * Drobne, niezależne od motywu poprawki wyjścia w <head> (meta, schema).
 *
 * @package Agria
 */

defined( 'ABSPATH' ) || exit;

/**
 * Hello Elementor wypuszcza <meta name="description"> z post_excerpt strony
 * (funkcja hello_elementor_add_description_meta_tag), co DUPLIKUJE meta description
 * generowaną przez RankMath. Dwie meta description = błąd SEO.
 * RankMath jest jedynym źródłem meta description — wyłączamy wersję Hello jego
 * własnym, dokumentowanym filtrem.
 */
add_filter( 'hello_elementor_description_meta_tag', '__return_false' );

/*
 * ─────────────────────────────────────────────────────────────────────────────
 * offers w schema Product — z kwoty widocznej w tresci (T-097, 2026-09-07)
 * ─────────────────────────────────────────────────────────────────────────────
 *
 * PROBLEM: 19 z 19 kart produktowych oblewa walidacje Google Product Snippet
 * z komunikatem "Either schema.org/review, schema.org/aggregateRating or
 * schema.org/offers is required" (crawl Screaming Frog 07.09). Rank Math buduje
 * wezel Product z 18 wlasciwosciami i zerem offers, bo WooCommerce ma puste
 * _price — i ma je miec.
 *
 * DLACZEGO NIE Z BAZY: ADR docs/decyzje/2026-08-19-dwie-warstwy-cen.md rozdziela
 * dwie warstwy cen, ktore nigdy sie nie stykaja. Warstwa A (tresc SEO) jest
 * publiczna, warstwa B (ofertownik — warianty WooCommerce, cennik wtyczki) jest
 * wewnetrzna i nie moze wyciec przez front, REST, feed ani schema. Gdyby offers
 * powstawalo z _price albo z wariantow, publikacja ofertownika automatycznie
 * ujawnilaby ceny warstwy B. Dlatego kwota czytana jest z post_content.
 *
 * DLACZEGO PARSOWANIE, A NIE TABLICA KWOT: Google traktuje rozjazd miedzy cena
 * widoczna dla czlowieka a cena w schemacie jako wprowadzanie w blad. Tablica
 * 16 kwot w kodzie rozjezdza sie z trescia przy pierwszej zmianie cennika,
 * o ktorej nikt nie pamieta. Czytanie z tresci sprawia, ze zgodnosc jest
 * wlasnoscia konstrukcji, a nie czyimas dyscyplina.
 *
 * ZAKRES: karta bez kwoty w tresci nie dostaje offers. Na 07.09 sa to trzy
 * pozycje — #303 Kreda czarna, #313 Tlenkowe z Mg, #316 Weglanowe bez Mg
 * odmiana 05. To swiadomy wyjatek, nie brak: ceny dla nich nie wymyslamy.
 */

if ( ! function_exists( 'agria_cena_z_tresci' ) ) {
	/**
	 * Wyciaga wiodaca kwote "od X zl/t netto" z tresci karty.
	 *
	 * Bierze PIERWSZE trafienie, bo tak jest zbudowana tresc: kwota wiodaca to
	 * najtansza dostepna forma hurtowa (docs/FAKTY_KLIENTA.md §7), a ewentualna
	 * druga kwota — jak 280 zl/t dla frakcji 1-3 mm dolomitu — stoi po niej.
	 * Separator tysiecy dopuszczony (spacja zwykla i nielamiaca), bo tresc
	 * przechodzi przez wtyczke od sierotek.
	 *
	 * @param string $tresc post_content karty.
	 * @return int|null Kwota w zlotych albo null, gdy karta ceny nie podaje.
	 */
	function agria_cena_z_tresci( string $tresc ): ?int {
		$wzor = '/od\s+([0-9]{1,3}(?:(?:\x{00A0}|&nbsp;|\s)[0-9]{3})*)\s*z[łl]\s*\/\s*t\s+netto/u';
		if ( ! preg_match( $wzor, $tresc, $trafienie ) ) {
			return null;
		}
		$kwota = (int) preg_replace( '/\D/', '', $trafienie[1] );

		return $kwota > 0 ? $kwota : null;
	}
}

if ( ! function_exists( 'agria_dodaj_offers_do_produktu' ) ) {
	/**
	 * Dokłada offers do wezla Product w grafie Rank Matha.
	 *
	 * Wchodzi w istniejacy wezel zamiast emitowac wlasny blok Product — drugi
	 * blok obok istniejacego bylby duplikatem, nie naprawa. Klucz wezla w grafie
	 * bywa rozny miedzy wersjami Rank Matha, wiec szukamy po @type.
	 *
	 * @param array $data  Graf JSON-LD Rank Matha.
	 * @return array
	 */
	function agria_dodaj_offers_do_produktu( $data ) {
		if ( ! is_array( $data ) || ! is_singular( 'product' ) ) {
			return $data;
		}

		$post = get_queried_object();
		if ( ! $post instanceof WP_Post ) {
			return $data;
		}

		$cena = agria_cena_z_tresci( (string) $post->post_content );
		if ( null === $cena ) {
			return $data;
		}

		foreach ( $data as $klucz => $wezel ) {
			if ( ! is_array( $wezel ) || isset( $wezel['offers'] ) ) {
				continue;
			}
			$typ = $wezel['@type'] ?? '';
			if ( ! in_array( 'Product', (array) $typ, true ) ) {
				continue;
			}

			$data[ $klucz ]['offers'] = array(
				'@type'              => 'Offer',
				'url'                => get_permalink( $post ),
				'price'              => (string) $cena,
				'priceCurrency'      => 'PLN',
				'availability'       => 'https://schema.org/InStock',
				// Rok do przodu, liczony przy renderze — data zaszyta na sztywno
				// zaczyna klamac w dniu, w ktorym mija.
				'priceValidUntil'    => gmdate( 'Y-m-d', strtotime( '+1 year' ) ),
				// Cena jest za TONE, nie za sztuke. Bez tego schemat sugeruje,
				// ze 645 zl kosztuje jedno opakowanie. TNE = tona metryczna
				// w UN/CEFACT, kodzie ktorego uzywa schema.org.
				//
				// valueAddedTaxIncluded jako URL, nie jako PHP-owe false: Rank
				// Math rzutuje wartosci grafu na tekst, wiec false wychodzilo
				// pustym stringiem — a pusty string nie jest wartoscia Boolean
				// (zmierzone na karcie #302, 07.09).
				'priceSpecification' => array(
					'@type'                 => 'UnitPriceSpecification',
					'price'                 => (string) $cena,
					'priceCurrency'         => 'PLN',
					'unitCode'              => 'TNE',
					'valueAddedTaxIncluded' => 'https://schema.org/False',
				),
				'seller'             => array(
					'@type' => 'Organization',
					'name'  => 'AGRIA Sp. z o.o.',
					'url'   => home_url( '/' ),
				),
			);
		}

		return $data;
	}
	add_filter( 'rank_math/json_ld', 'agria_dodaj_offers_do_produktu', 99, 1 );
}
