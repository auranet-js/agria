<?php
/**
 * Oferty i klienci — CPT `agria_quote` i `agria_client`.
 *
 * OFERTA JEST ZAMROZONA. Zapisuje stan z chwili wystawienia, nie odwolania do cennika.
 * Otwarcie oferty sprzed dwoch miesiecy nie moze pociagnac aktualnych cen i przeliczyc sumy —
 * dokument przestalby zgadzac sie z tym, co klient uslyszal przez telefon.
 *
 * Efekt uboczny wart tyle co reszta: skoro cena proponowana lezy w bazie OBOK podanej, roznica
 * jest mierzalna. Widac, o ile schodzi sie ponizej cennika — kto, na czym i przy ktorym kanale.
 * Zero dodatkowej pracy przy formularzu.
 *
 * Klient jako CPT, NIE jako uzytkownik WordPressa: WP wymaga unikalnego loginu i adresu e-mail,
 * a rolnik dzwoniacy z komorki maila czesto nie poda. Dwoch takich klientow to konflikt, a obejsciem
 * bylyby sztuczne adresy typu `509xxxxxxx@brak.local` — smiecace tabela uzytkownikow i grozace
 * wysylka na fikcyjny adres.
 */

defined( 'ABSPATH' ) || exit;

const AGRIA_OF_CPT_OFERTA = 'agria_quote';
const AGRIA_OF_CPT_KLIENT = 'agria_client';

add_action( 'init', function (): void {
	$wspolne = [
		'public'              => false,
		'show_ui'             => true,
		'show_in_menu'        => 'agria-of-cennik',
		'exclude_from_search' => true,
		'publicly_queryable'  => false,
		'show_in_rest'        => false, // nie wystawiamy tego zadnym API — patrz ADR 22.08
		'capability_type'     => 'post',
		'map_meta_cap'        => true,
		'supports'            => [ 'title', 'author' ],
	];
	register_post_type( AGRIA_OF_CPT_OFERTA, $wspolne + [
		'labels' => [ 'name' => 'Oferty', 'singular_name' => 'Oferta', 'menu_name' => 'Oferty' ],
	] );
	register_post_type( AGRIA_OF_CPT_KLIENT, $wspolne + [
		'labels' => [ 'name' => 'Klienci', 'singular_name' => 'Klient', 'menu_name' => 'Klienci' ],
	] );
} );

/** Skad przyszedl kontakt — po to, zeby dalo sie w koncu powiedziec, ktory kanal sprzedaje. */
function agria_of_kanaly(): array {
	return [
		'olx'       => 'OLX',
		'ads'       => 'Reklama Google',
		'strona'    => 'Strona / formularz',
		'polecenie' => 'Polecenie',
		'staly'     => 'Stały klient',
		'inne'      => 'Inne',
	];
}

function agria_of_statusy(): array {
	return [
		'nowa'      => 'Wystawiona',
		'czeka'     => 'Klient się zastanawia',
		'zamowione' => 'Zamówione',
		'przepadla' => 'Przepadła',
	];
}

/**
 * Znajduje klienta po telefonie albo NIP, zaklada gdy go nie ma.
 * Telefon normalizujemy do samych cyfr — „664 393 062" i „+48664393062" to ten sam czlowiek.
 */
function agria_of_klient( array $dane ): int {
	$tel = preg_replace( '/\D+/', '', (string) ( $dane['telefon'] ?? '' ) );
	$tel = $tel ? substr( $tel, -9 ) : '';
	$nip = preg_replace( '/\D+/', '', (string) ( $dane['nip'] ?? '' ) );

	$istniejacy = 0;
	foreach ( [ [ 'agria_of_telefon', $tel ], [ 'agria_of_nip', $nip ] ] as [ $klucz, $wartosc ] ) {
		if ( ! $wartosc ) {
			continue;
		}
		$znalezione = get_posts( [
			'post_type'      => AGRIA_OF_CPT_KLIENT,
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'meta_key'       => $klucz,
			'meta_value'     => $wartosc,
			'fields'         => 'ids',
		] );
		if ( $znalezione ) {
			$istniejacy = (int) $znalezione[0];
			break;
		}
	}

	$nazwa = trim( (string) ( $dane['nazwa'] ?? '' ) ) ?: ( $tel ?: 'Klient bez danych' );

	if ( $istniejacy ) {
		// Dane uzupelniamy, nie nadpisujemy pustym — drugi telefon czesto dokłada NIP albo nazwe.
		foreach ( [ 'agria_of_telefon' => $tel, 'agria_of_nip' => $nip ] as $k => $v ) {
			if ( $v && ! get_post_meta( $istniejacy, $k, true ) ) {
				update_post_meta( $istniejacy, $k, $v );
			}
		}
		return $istniejacy;
	}

	$id = wp_insert_post( [
		'post_type'   => AGRIA_OF_CPT_KLIENT,
		'post_status' => 'publish',
		'post_title'  => $nazwa,
	] );
	if ( is_wp_error( $id ) ) {
		return 0;
	}
	update_post_meta( $id, 'agria_of_telefon', $tel );
	update_post_meta( $id, 'agria_of_nip', $nip );
	update_post_meta( $id, 'agria_of_miejscowosc', sanitize_text_field( $dane['miejscowosc'] ?? '' ) );
	return (int) $id;
}

/**
 * Zapisuje oferte jako stan zamrozony.
 *
 * @param array $wejscie  to samo, co poszlo do `agria_of_wycen`, plus dane klienta i kanal
 * @param array $w        wynik `agria_of_wycen`
 */
function agria_of_zapisz_oferte( array $wejscie, array $w ): int {
	$produkt   = agria_of_tytul_produktu( (int) $wejscie['produkt_id'] );
	$mie       = agria_of_miejscowosc( (int) ( $wejscie['miejscowosc_id'] ?? 0 ) );
	$klient_id = agria_of_klient( [
		'nazwa'       => $wejscie['klient_nazwa'] ?? '',
		'telefon'     => $wejscie['klient_telefon'] ?? '',
		'nip'         => $wejscie['klient_nip'] ?? '',
		'miejscowosc' => $mie['nazwa'] ?? '',
	] );

	$tytul = sprintf( '%s — %s, %s t%s',
		$mie['nazwa'] ?? '?',
		$produkt,
		$w['tony'],
		! empty( $wejscie['klient_nazwa'] ) ? ' · ' . sanitize_text_field( $wejscie['klient_nazwa'] ) : ''
	);

	$id = wp_insert_post( [
		'post_type'   => AGRIA_OF_CPT_OFERTA,
		'post_status' => 'publish',
		'post_title'  => $tytul,
		'post_author' => get_current_user_id(),
	] );
	if ( is_wp_error( $id ) ) {
		return 0;
	}

	// Stan zamrozony: wszystko, co potrzebne do odtworzenia rozmowy, w wartosciach — nie w referencjach.
	$zapis = [
		'klient_id'        => $klient_id,
		'kanal'            => sanitize_text_field( $wejscie['kanal'] ?? 'inne' ),
		'status'           => 'nowa',
		'produkt_id'       => (int) $wejscie['produkt_id'],
		'produkt'          => $produkt,
		'sku'              => get_post_meta( (int) $wejscie['produkt_id'], '_sku', true ),
		'miejscowosc'      => $mie['nazwa'] ?? '',
		'miejscowosc_id'   => (int) ( $wejscie['miejscowosc_id'] ?? 0 ),
		'wojewodztwo'      => $mie['wojewodztwo'] ?? '',
		'forma'            => $w['forma']['nazwa'],
		'forma_klucz'      => $w['forma']['klucz'],
		'frakcja'          => (string) ( $wejscie['frakcja'] ?? '' ),
		'tony'             => $w['tony'],
		'palet'            => $w['palet'],
		'jednostka'        => sanitize_text_field( $wejscie['jednostka'] ?? 'tona' ),
		'ilosc_podana'     => (float) ( $wejscie['ilosc'] ?? 0 ),
		'zaklad'           => $w['zaklad']['nazwa'],
		'zaklad_term_id'   => $w['zaklad']['term_id'],
		'km'               => $w['km'],
		'km_pewne'         => $w['km_pewne'] ? 1 : 0,
		'metoda'           => $w['metoda']['nazwa'] ?? '',
		'metoda_id'        => $w['metoda']['metoda'] ?? '',
		'kursy'            => $w['metoda']['kursy'] ?? 1,
		'stan_transportu'  => $w['stan_transportu'],
		// Sedno: proponowane OBOK podanego. Roznica jest tym, o co chodzi.
		'cena_proponowana' => $w['cena_proponowana'],
		'cena_podana'      => $w['cena_t'],
		'cena_min'         => $w['cena_min'],
		'transport_proponowany' => $w['metoda']['koszt'] ?? 0,
		'transport_podany' => $w['transport'],
		'wartosc_towaru'   => $w['wartosc_towaru'],
		'za_tone'          => $w['za_tone_z_dostawa'],
		'razem'            => $w['razem'],
		'wystawil'         => get_current_user_id(),
		'wystawiono'       => current_time( 'mysql' ),
		'uwagi'            => sanitize_textarea_field( $wejscie['uwagi'] ?? '' ),
	];
	foreach ( $zapis as $k => $v ) {
		update_post_meta( $id, 'agria_of_' . $k, $v );
	}
	return (int) $id;
}

add_action( 'wp_ajax_agria_of_zapisz', function (): void {
	check_ajax_referer( 'agria_of' );
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_send_json_error( [], 403 );
	}
	$wejscie = wp_unslash( $_POST );
	$w = agria_of_wycen( $wejscie );
	if ( empty( $w['zaklad'] ) ) {
		wp_send_json_error( [ 'blad' => $w['blad'] ?? 'Nie da się wycenić.' ] );
	}
	$id = agria_of_zapisz_oferte( $wejscie, $w );
	if ( ! $id ) {
		wp_send_json_error( [ 'blad' => 'Nie udało się zapisać.' ] );
	}
	wp_send_json_success( [
		'id'     => $id,
		'wydruk' => add_query_arg( [ 'agria_of_oferta' => $id ], home_url( '/wycena/' ) ),
	] );
} );

/** Wydruk oferty — ten sam adres za logowaniem, tylko z numerem oferty. */
add_action( 'template_redirect', function (): void {
	if ( ! get_query_var( 'agria_of_ekran' ) || empty( $_GET['agria_of_oferta'] ) ) {
		return;
	}
	if ( ! is_user_logged_in() || ! current_user_can( AGRIA_OF_CAP ) ) {
		auth_redirect();
		exit;
	}
	agria_of_render_wydruk( (int) $_GET['agria_of_oferta'] );
	exit;
}, 9 );

function agria_of_render_wydruk( int $id ): void {
	$o = get_post( $id );
	if ( ! $o || $o->post_type !== AGRIA_OF_CPT_OFERTA ) {
		wp_die( 'Nie ma takiej oferty.' );
	}
	$m  = fn( string $k ) => get_post_meta( $id, 'agria_of_' . $k, true );
	$zl = fn( $g ) => $g === '' || $g === null ? '—' : number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' ) . ' zł';
	$kanaly = agria_of_kanaly();
	$klient = $m( 'klient_id' ) ? get_post( (int) $m( 'klient_id' ) ) : null;
	?><!doctype html>
<html lang="pl"><head>
<meta charset="utf-8"><meta name="robots" content="noindex, nofollow">
<title>Oferta <?php echo (int) $id; ?> — AGRIA</title>
<style>
body { font:15px/1.55 -apple-system,Segoe UI,Roboto,sans-serif; color:#1b1b1b; background:#fff; max-width:44rem; margin:0 auto; padding:2.5rem 1.5rem; }
h1 { font-size:1.35rem; margin:0 0 .2rem; }
.meta { color:#666; font-size:.86rem; margin-bottom:2rem; }
table { border-collapse:collapse; width:100%; margin:1.2rem 0; }
td, th { text-align:left; padding:.45rem .2rem; border-bottom:1px solid #e5e5e5; vertical-align:top; }
th { color:#666; font-weight:400; width:14rem; font-size:.9rem; }
.suma td { border-top:2px solid #354E33; border-bottom:0; font-size:1.15rem; font-weight:700; padding-top:.8rem; }
.num { text-align:right; font-variant-numeric:tabular-nums; }
.klauzula { color:#666; font-size:.8rem; margin-top:2.5rem; border-top:1px solid #e5e5e5; padding-top:1rem; }
.narzedzia { margin:2rem 0 0; }
button, a.btn { font:inherit; padding:.5rem .9rem; border:1px solid #ccc; border-radius:.3rem; background:#fff; cursor:pointer; text-decoration:none; color:inherit; }
@media print { .narzedzia { display:none; } body { padding:0; } }
</style></head><body>
<h1>Wycena — AGRIA Sp. z o.o.</h1>
<p class="meta">
	Nr <?php echo (int) $id; ?> · <?php echo esc_html( mysql2date( 'j.m.Y, H:i', (string) $m( 'wystawiono' ) ) ); ?>
	· wystawił <?php echo esc_html( get_userdata( (int) $m( 'wystawil' ) )->display_name ?? '—' ); ?>
	<?php if ( $klient ) : ?>· dla <?php echo esc_html( $klient->post_title ); ?><?php endif; ?>
	<?php if ( $m( 'kanal' ) ) : ?>· kontakt: <?php echo esc_html( $kanaly[ $m( 'kanal' ) ] ?? $m( 'kanal' ) ); ?><?php endif; ?>
</p>

<table>
	<tr><th>Towar</th><td><?php echo esc_html( (string) $m( 'produkt' ) ); ?><?php if ( $m( 'sku' ) ) : ?> <span style="color:#666">(<?php echo esc_html( (string) $m( 'sku' ) ); ?>)</span><?php endif; ?></td></tr>
	<tr><th>Forma dostawy</th><td><?php echo esc_html( (string) $m( 'forma' ) ); ?><?php if ( $m( 'frakcja' ) ) : ?>, frakcja <?php echo esc_html( (string) $m( 'frakcja' ) ); ?><?php endif; ?></td></tr>
	<tr><th>Ilość</th><td><?php echo esc_html( (string) $m( 'tony' ) ); ?> t<?php if ( $m( 'palet' ) ) : ?> (<?php echo (int) $m( 'palet' ); ?> pal.)<?php endif; ?></td></tr>
	<tr><th>Miejsce dostawy</th><td><?php echo esc_html( (string) $m( 'miejscowosc' ) ); ?><?php if ( $m( 'wojewodztwo' ) ) : ?>, <?php echo esc_html( (string) $m( 'wojewodztwo' ) ); ?><?php endif; ?></td></tr>
	<tr><th>Wysyłka z zakładu</th><td><?php echo esc_html( (string) $m( 'zaklad' ) ); ?> — <?php echo (int) $m( 'km' ); ?> km<?php echo $m( 'km_pewne' ) ? '' : ' (szacunek)'; ?></td></tr>
</table>

<table>
	<tr><th>Cena towaru</th><td class="num"><?php echo esc_html( $zl( $m( 'cena_podana' ) ) ); ?>/t × <?php echo esc_html( (string) $m( 'tony' ) ); ?> t</td><td class="num"><?php echo esc_html( $zl( $m( 'wartosc_towaru' ) ) ); ?></td></tr>
	<tr><th>Transport<?php if ( $m( 'stan_transportu' ) === 'gratis' ) : ?> (gratis)<?php elseif ( $m( 'stan_transportu' ) === 'odbior' ) : ?> (odbiór własny)<?php endif; ?></th>
		<td class="num"><?php echo esc_html( (string) $m( 'metoda' ) ); ?><?php echo (int) $m( 'kursy' ) > 1 ? ', ' . (int) $m( 'kursy' ) . ' kursy' : ''; ?></td>
		<td class="num"><?php echo esc_html( $zl( $m( 'transport_podany' ) ) ); ?></td></tr>
	<tr><th>Cena z dostawą</th><td></td><td class="num"><?php echo esc_html( $zl( $m( 'za_tone' ) ) ); ?>/t</td></tr>
	<tr class="suma"><td colspan="2">Razem netto</td><td class="num"><?php echo esc_html( $zl( $m( 'razem' ) ) ); ?></td></tr>
</table>

<?php if ( $m( 'uwagi' ) ) : ?><p><strong>Uwagi:</strong> <?php echo esc_html( (string) $m( 'uwagi' ) ); ?></p><?php endif; ?>

<p class="klauzula">
	Ceny netto, nie zawierają podatku VAT. Wycena orientacyjna, ważna 14 dni od wystawienia,
	nie stanowi oferty handlowej w rozumieniu Kodeksu cywilnego. Dostępność towaru i termin dostawy
	potwierdza handlowiec.
</p>

<p class="narzedzia">
	<button onclick="window.print()">Drukuj / zapisz PDF</button>
	<a class="btn" href="<?php echo esc_url( home_url( '/wycena/' ) ); ?>">Nowa wycena</a>
</p>
</body></html>
	<?php
}

/**
 * Lista ofert w panelu — kolumny, ktore odpowiadaja na pytanie „co sie dzieje w sprzedazy".
 * Kolumna z roznica wobec cennika jest tu celowo: to ona zamienia zapis oferty w informacje.
 */
add_filter( 'manage_' . AGRIA_OF_CPT_OFERTA . '_posts_columns', function ( array $k ): array {
	return [
		'cb'        => $k['cb'] ?? '',
		'title'     => 'Oferta',
		'kanal'     => 'Kanał',
		'ilosc'     => 'Ilość',
		'cena'      => 'Cena zł/t',
		'roznica'   => 'Wobec cennika',
		'razem'     => 'Razem netto',
		'status'    => 'Status',
		'author'    => 'Wystawił',
		'date'      => 'Data',
	];
} );

add_action( 'manage_' . AGRIA_OF_CPT_OFERTA . '_posts_custom_column', function ( string $kol, int $id ): void {
	$m  = fn( string $k ) => get_post_meta( $id, 'agria_of_' . $k, true );
	$zl = fn( $g ) => $g === '' || $g === null ? '—' : number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );

	switch ( $kol ) {
		case 'kanal':
			echo esc_html( agria_of_kanaly()[ $m( 'kanal' ) ] ?? '—' );
			break;
		case 'ilosc':
			echo esc_html( $m( 'tony' ) ) . ' t';
			break;
		case 'cena':
			echo esc_html( $zl( $m( 'cena_podana' ) ) );
			break;
		case 'roznica':
			$prop = (int) $m( 'cena_proponowana' );
			$pod  = (int) $m( 'cena_podana' );
			if ( ! $prop || ! $pod || $prop === $pod ) {
				echo '<span style="color:#888">bez zmian</span>';
				break;
			}
			$r = $pod - $prop;
			printf( '<span style="color:%s">%s%s zł (%s%.1f%%)</span>',
				$r < 0 ? '#a33' : '#2d6a2d',
				$r > 0 ? '+' : '−', esc_html( $zl( abs( $r ) ) ),
				$r > 0 ? '+' : '−', abs( $r ) / $prop * 100 );
			break;
		case 'razem':
			echo esc_html( $zl( $m( 'razem' ) ) ) . ' zł';
			break;
		case 'status':
			echo esc_html( agria_of_statusy()[ $m( 'status' ) ] ?? '—' );
			break;
	}
}, 10, 2 );

add_filter( 'manage_' . AGRIA_OF_CPT_KLIENT . '_posts_columns', function ( array $k ): array {
	return [ 'cb' => $k['cb'] ?? '', 'title' => 'Klient', 'telefon' => 'Telefon', 'nip' => 'NIP',
	         'miejscowosc' => 'Miejscowość', 'ofert' => 'Ofert', 'date' => 'Pierwszy kontakt' ];
} );

add_action( 'manage_' . AGRIA_OF_CPT_KLIENT . '_posts_custom_column', function ( string $kol, int $id ): void {
	if ( $kol === 'ofert' ) {
		$n = new WP_Query( [ 'post_type' => AGRIA_OF_CPT_OFERTA, 'meta_key' => 'agria_of_klient_id',
		                     'meta_value' => $id, 'fields' => 'ids', 'posts_per_page' => -1 ] );
		echo (int) $n->found_posts;
		return;
	}
	echo esc_html( get_post_meta( $id, 'agria_of_' . $kol, true ) ?: '—' );
}, 10, 2 );
