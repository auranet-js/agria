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

/**
 * Zapisuje oferte WIELOPOZYCYJNA jako stan zamrozony.
 *
 * Wszystko w wartosciach, nie w referencjach do cennika: otwarcie oferty za dwa miesiace
 * ma pokazac to, co klient uslyszal przez telefon, a nie przeliczyc sume po nowych cenach.
 */
function agria_of_zapisz_oferte( array $wejscie, array $w ): int {
	$mie       = agria_of_miejscowosc( (int) ( $wejscie['miejscowosc_id'] ?? 0 ) );
	$platnik   = json_decode( (string) ( $wejscie['klient_platnik'] ?? '' ), true );
	$klient_id = agria_of_klient( [
		'nazwa'       => $wejscie['klient_nazwa'] ?? ( $platnik['nazwa'] ?? '' ),
		'telefon'     => $wejscie['klient_telefon'] ?? '',
		'nip'         => $wejscie['klient_nip'] ?? '',
		'miejscowosc' => $mie['nazwa'] ?? '',
	] );
	if ( $klient_id && is_array( $platnik ) ) {
		update_post_meta( $klient_id, 'agria_of_platnik', $platnik );
	}

	$ile = count( $w['pozycje'] );
	$pierwsza = reset( $w['pozycje'] );
	$tytul = sprintf( '%s — %s%s, %s t%s',
		$mie['nazwa'] ?? '?',
		$pierwsza['produkt'],
		$ile > 1 ? sprintf( ' i %d %s', $ile - 1, $ile === 2 ? 'inna pozycja' : 'inne pozycje' ) : '',
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

	$pozycje = [];
	foreach ( $w['pozycje'] as $p ) {
		$pozycje[] = [
			'produkt_id'       => $p['produkt_id'],
			'produkt'          => $p['produkt'],
			'sku'              => $p['sku'],
			'forma'            => $p['forma']['nazwa'],
			'forma_klucz'      => $p['forma']['klucz'],
			'frakcja'          => $p['frakcja'],
			'ilosc'            => $p['ilosc'],
			'jednostka'        => $p['jednostka'],
			'tony'             => $p['tony'],
			'palet'            => $p['palet'],
			'zaklad'           => $p['zaklad']['nazwa'],
			'zaklad_term_id'   => $p['zaklad']['term_id'],
			'km'               => $p['zaklad']['km'],
			// Sedno warstwy raportowej: proponowane OBOK podanego.
			'cena_proponowana' => $p['cena_proponowana'],
			'cena_podana'      => $p['cena'],
			'cena_min'         => $p['cena_min'],
			'wartosc'          => $p['wartosc'],
		];
	}

	$grupy = [];
	foreach ( $w['grupy'] as $g ) {
		$grupy[] = [
			'zaklad'         => $g['zaklad'],
			'zaklad_term_id' => $g['zaklad_term_id'],
			'km'             => $g['km'],
			'km_pewne'       => $g['km_pewne'] ? 1 : 0,
			'tony'           => $g['tony'],
			'metoda'         => $g['metoda']['nazwa'] ?? '',
			'metoda_id'      => $g['metoda']['metoda'] ?? '',
			'kursy'          => $g['metoda']['kursy'] ?? 1,
			'transport_proponowany' => $g['metoda']['koszt'] ?? 0,
			'transport_podany'      => $g['koszt'],
			'wypelnienie'    => $g['wypelnienie'] ?? null,
		];
	}

	// Roznica wobec cennika liczona raz, przy zapisie — zeby lista ofert nie musiala jej wyliczac.
	$prop = 0;
	$pod  = 0;
	foreach ( $w['pozycje'] as $p ) {
		if ( $p['cena_proponowana'] !== null && $p['cena'] !== null ) {
			$prop += (int) round( $p['cena_proponowana'] * $p['tony'] );
			$pod  += $p['wartosc'];
		}
	}

	$zapis = [
		'klient_id'       => $klient_id,
		'platnik'         => is_array( $platnik ) ? $platnik : '',
		'kanal'           => sanitize_text_field( $wejscie['kanal'] ?? 'inne' ),
		'status'          => 'nowa',
		'miejscowosc'     => $mie['nazwa'] ?? '',
		'miejscowosc_id'  => (int) ( $wejscie['miejscowosc_id'] ?? 0 ),
		'wojewodztwo'     => $mie['wojewodztwo'] ?? '',
		'pozycje'         => $pozycje,
		'grupy'           => $grupy,
		'ile_pozycji'     => $ile,
		'tony'            => $w['tony'],
		'stan_transportu' => $w['stan_transportu'],
		'towar'           => $w['towar'],
		'transport'       => $w['transport'],
		'razem'           => $w['razem'],
		'za_tone'         => $w['za_tone'],
		'towar_wg_cennika'=> $prop,
		'towar_podany'    => $pod,
		'wystawil'        => get_current_user_id(),
		'wystawiono'      => current_time( 'mysql' ),
		'uwagi'           => sanitize_textarea_field( $wejscie['uwagi'] ?? '' ),
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
	$dane = wp_unslash( $_POST );
	$w = agria_of_wycen_koszyk(
		(array) ( $dane['pozycje'] ?? [] ),
		(int) ( $dane['miejscowosc_id'] ?? 0 ),
		[
			'stan_transportu' => sanitize_text_field( $dane['stan_transportu'] ?? 'wyliczony' ),
			'km'              => (array) ( $dane['km'] ?? [] ),
			'metoda'          => (array) ( $dane['metoda'] ?? [] ),
			'transport'       => (array) ( $dane['transport'] ?? [] ),
		]
	);
	if ( empty( $w['pozycje'] ) ) {
		wp_send_json_error( [ 'blad' => 'Nie ma czego zapisać — wpisz ilość przy którejś pozycji.' ] );
	}
	$id = agria_of_zapisz_oferte( $dane, $w );
	if ( ! $id ) {
		wp_send_json_error( [ 'blad' => 'Nie udało się zapisać.' ] );
	}
	wp_send_json_success( [ 'id' => $id, 'wydruk' => add_query_arg( [ 'agria_of_oferta' => $id ], home_url( '/wycena/' ) ) ] );
} );

/** Wydruk oferty — ten sam adres za logowaniem, tylko z numerem. */
add_action( 'template_redirect', function (): void {
	if ( ! get_query_var( 'agria_of_ekran' ) || empty( $_GET['agria_of_oferta'] ) ) {
		return;
	}
	if ( ! agria_of_wpuszczamy() ) {
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
	$zl = fn( $g ) => $g === '' || $g === null ? '—' : number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );
	$pozycje = agria_of_pozycje_oferty( $id );   // czyta oba formaty — patrz nizej
	$grupy   = agria_of_grupy_oferty( $id );
	$platnik = $m( 'platnik' );
	$klient  = $m( 'klient_id' ) ? get_post( (int) $m( 'klient_id' ) ) : null;
	?><!doctype html>
<html lang="pl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Oferta <?php echo (int) $id; ?> — AGRIA</title>
<style>
body{font:14px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#161A16;background:#fff;
	max-width:50rem;margin:0 auto;padding:2.5rem 1.5rem;}
h1{font-size:1.3rem;margin:0 0 .15rem;color:#354E33;}
.meta{color:#6B7268;font-size:.84rem;margin:0 0 1.8rem;}
h2{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:#99A095;
	margin:1.8rem 0 .4rem;font-weight:600;}
table{border-collapse:collapse;width:100%;}
th,td{text-align:left;padding:.4rem .45rem;border-bottom:1px solid #E4E5DE;vertical-align:top;}
thead th{font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:#99A095;font-weight:600;}
.p{text-align:right;}
.num{font-family:ui-monospace,Menlo,Consolas,monospace;font-variant-numeric:tabular-nums;}
.suma{border-top:2px solid #354E33;font-size:1.1rem;font-weight:650;}
.suma td{border-bottom:0;padding-top:.7rem;}
.dane{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.5rem 1.5rem;}
.dane div span{display:block;font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:#99A095;}
.klauzula{color:#6B7268;font-size:.78rem;margin-top:2.2rem;border-top:1px solid #E4E5DE;padding-top:.9rem;}
.narzedzia{margin-top:1.6rem;}
button,a.btn{font:inherit;padding:.5rem .9rem;border:1px solid #C4C7BB;border-radius:2px;
	background:#fff;cursor:pointer;text-decoration:none;color:inherit;}
@media print{.narzedzia{display:none;}body{padding:0;max-width:none;}}
</style></head><body>

<h1>Wycena — AGRIA Sp. z o.o.</h1>
<p class="meta">Nr <?php echo (int) $id; ?> · <?php echo esc_html( mysql2date( 'j.m.Y, H:i', (string) $m( 'wystawiono' ) ) ); ?>
	· wystawił <?php echo esc_html( get_userdata( (int) $m( 'wystawil' ) )->display_name ?? '—' ); ?></p>

<h2>Dla kogo</h2>
<div class="dane">
	<?php if ( $klient ) : ?><div><span>Klient</span><?php echo esc_html( $klient->post_title ); ?></div><?php endif; ?>
	<?php if ( is_array( $platnik ) && ! empty( $platnik['nazwa'] ) ) : ?>
		<div><span>Płatnik (REGON)</span><?php echo esc_html( $platnik['nazwa'] ); ?><br>
			<?php echo esc_html( $platnik['adres'] ?? '' ); ?><br>
			NIP <?php echo esc_html( $platnik['nip'] ?? '' ); ?></div>
	<?php endif; ?>
	<div><span>Miejsce dostawy</span><?php echo esc_html( (string) $m( 'miejscowosc' ) ); ?><?php
		if ( $m( 'wojewodztwo' ) ) : ?>, <?php echo esc_html( (string) $m( 'wojewodztwo' ) ); ?><?php endif; ?></div>
	<div><span>Kontakt przez</span><?php echo esc_html( agria_of_kanaly()[ $m( 'kanal' ) ] ?? '—' ); ?></div>
</div>

<h2>Towar</h2>
<table>
	<thead><tr><th>Produkt</th><th>Forma</th><th class="p">Ilość</th><th class="p">Cena zł/t</th>
		<th>Z zakładu</th><th class="p">Wartość</th></tr></thead>
	<tbody>
	<?php foreach ( $pozycje as $p ) : ?>
		<tr>
			<td><?php echo esc_html( $p['produkt'] ); ?><?php if ( ! empty( $p['sku'] ) ) : ?>
				<span style="color:#99A095"> <?php echo esc_html( $p['sku'] ); ?></span><?php endif; ?></td>
			<td><?php echo esc_html( $p['forma'] ); ?><?php if ( ! empty( $p['frakcja'] ) ) : ?>, <?php echo esc_html( $p['frakcja'] ); ?><?php endif; ?></td>
			<td class="p num"><?php echo esc_html( $p['tony'] ); ?> t</td>
			<td class="p num"><?php echo esc_html( $zl( $p['cena_podana'] ) ); ?></td>
			<td><?php echo esc_html( $p['zaklad'] ); ?></td>
			<td class="p num"><?php echo esc_html( $zl( $p['wartosc'] ) ); ?></td>
		</tr>
	<?php endforeach; ?>
	</tbody>
</table>

<h2>Transport<?php if ( $m( 'stan_transportu' ) === 'gratis' ) : ?> — gratis<?php
	elseif ( $m( 'stan_transportu' ) === 'odbior' ) : ?> — odbiór własny<?php endif; ?></h2>
<table>
	<thead><tr><th>Z zakładu</th><th class="p">km</th><th>Środek</th><th class="p">Ładunek</th><th class="p">Koszt</th></tr></thead>
	<tbody>
	<?php foreach ( $grupy as $g ) : ?>
		<tr>
			<td><?php echo esc_html( $g['zaklad'] ); ?></td>
			<td class="p num"><?php echo (int) $g['km']; ?><?php echo empty( $g['km_pewne'] ) ? '*' : ''; ?></td>
			<td><?php echo esc_html( $g['metoda'] ); ?><?php echo (int) $g['kursy'] > 1 ? ', ' . (int) $g['kursy'] . ' kursy' : ''; ?></td>
			<td class="p num"><?php echo esc_html( $g['tony'] ); ?> t</td>
			<td class="p num"><?php echo esc_html( $zl( $g['transport_podany'] ) ); ?></td>
		</tr>
	<?php endforeach; ?>
	</tbody>
</table>

<table style="margin-top:1.4rem">
	<tr><td>Towar</td><td class="p num"><?php echo esc_html( $zl( $m( 'towar' ) ) ); ?></td></tr>
	<tr><td>Transport</td><td class="p num"><?php echo esc_html( $zl( $m( 'transport' ) ) ); ?></td></tr>
	<tr><td>Cena z dostawą za tonę</td><td class="p num"><?php echo esc_html( $zl( $m( 'za_tone' ) ) ); ?></td></tr>
	<tr class="suma"><td>Razem netto</td><td class="p num"><?php echo esc_html( $zl( $m( 'razem' ) ) ); ?> zł</td></tr>
</table>

<?php if ( $m( 'uwagi' ) ) : ?><p style="margin-top:1.2rem"><strong>Uwagi:</strong> <?php echo esc_html( (string) $m( 'uwagi' ) ); ?></p><?php endif; ?>

<p class="klauzula">
	Ceny netto, nie zawierają podatku VAT. Wycena orientacyjna, ważna 14 dni od wystawienia,
	nie stanowi oferty handlowej w rozumieniu Kodeksu cywilnego. Dostępność towaru i termin dostawy
	potwierdza handlowiec.<?php
	$szacunek = array_filter( $grupy, fn( $g ) => empty( $g['km_pewne'] ) );
	if ( $szacunek ) : ?> Kilometry oznaczone gwiazdką to szacunek — trasa nie została policzona.<?php endif; ?>
</p>

<p class="narzedzia">
	<button onclick="window.print()">Drukuj / zapisz PDF</button>
	<a class="btn" href="<?php echo esc_url( home_url( '/wycena/' ) ); ?>">Nowa wycena</a>
</p>
</body></html>
	<?php
}

/**
 * Lista ofert w panelu. Kolumna „wobec cennika" jest tu celowo — to ona zamienia
 * zapis oferty w informacje o tym, gdzie schodzi marza.
 */
add_filter( 'manage_' . AGRIA_OF_CPT_OFERTA . '_posts_columns', fn( array $k ): array => [
	'cb' => $k['cb'] ?? '', 'title' => 'Oferta', 'kanal' => 'Kanał', 'pozycji' => 'Poz.',
	'ilosc' => 'Tonaż', 'roznica' => 'Wobec cennika', 'razem' => 'Razem netto',
	'status' => 'Status', 'author' => 'Wystawił', 'date' => 'Data',
] );

add_action( 'manage_' . AGRIA_OF_CPT_OFERTA . '_posts_custom_column', function ( string $kol, int $id ): void {
	$m  = fn( string $k ) => get_post_meta( $id, 'agria_of_' . $k, true );
	$zl = fn( $g ) => $g === '' || $g === null ? '—' : number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );
	switch ( $kol ) {
		case 'kanal':   echo esc_html( agria_of_kanaly()[ $m( 'kanal' ) ] ?? '—' ); break;
		case 'pozycji': echo (int) ( $m( 'ile_pozycji' ) ?: count( agria_of_pozycje_oferty( $id ) ) ); break;
		case 'ilosc':   echo esc_html( $m( 'tony' ) ) . ' t'; break;
		case 'razem':   echo esc_html( $zl( $m( 'razem' ) ) ) . ' zł'; break;
		case 'ilosc2':  break;
		case 'status':  echo esc_html( agria_of_statusy()[ $m( 'status' ) ] ?? '—' ); break;
		case 'roznica':
			[ $prop, $pod ] = agria_of_roznica_oferty( $id );
			if ( ! $prop || $prop === $pod ) { echo '<span style="color:#888">bez zmian</span>'; break; }
			$r = $pod - $prop;
			printf( '<span style="color:%s">%s%s zł (%s%.1f%%)</span>',
				$r < 0 ? '#a33' : '#2d6a2d', $r > 0 ? '+' : '−', esc_html( $zl( abs( $r ) ) ),
				$r > 0 ? '+' : '−', abs( $r ) / $prop * 100 );
			break;
	}
}, 10, 2 );

add_filter( 'manage_' . AGRIA_OF_CPT_KLIENT . '_posts_columns', fn( array $k ): array => [
	'cb' => $k['cb'] ?? '', 'title' => 'Klient', 'telefon' => 'Telefon', 'nip' => 'NIP',
	'miejscowosc' => 'Miejscowość', 'ofert' => 'Ofert', 'date' => 'Pierwszy kontakt',
] );

add_action( 'manage_' . AGRIA_OF_CPT_KLIENT . '_posts_custom_column', function ( string $kol, int $id ): void {
	if ( $kol === 'ofert' ) {
		$q = new WP_Query( [ 'post_type' => AGRIA_OF_CPT_OFERTA, 'meta_key' => 'agria_of_klient_id',
			'meta_value' => $id, 'fields' => 'ids', 'posts_per_page' => -1 ] );
		echo (int) $q->found_posts;
		return;
	}
	echo esc_html( get_post_meta( $id, 'agria_of_' . $kol, true ) ?: '—' );
}, 10, 2 );

/**
 * Pozycje oferty — niezaleznie od tego, w ktorym formacie zostala zapisana.
 *
 * Ofertownik zaczynal od wyceny JEDNEJ pozycji i tak zapisywal oferty (plaskie meta:
 * `produkt`, `tony`, `cena_podana`). Od 0.5.0 oferta trzyma tablice `pozycje`.
 * Starych NIE przepisujemy — oferta ma byc zamrozona, a przepisanie jej w bazie
 * zmienialoby dokument, ktory ktos juz wydrukowal i wyslal. Zamiast tego czytamy oba formaty.
 */
function agria_of_pozycje_oferty( int $id ): array {
	$p = get_post_meta( $id, 'agria_of_pozycje', true );
	if ( is_array( $p ) && $p ) {
		return $p;
	}
	$m = fn( string $k ) => get_post_meta( $id, 'agria_of_' . $k, true );
	if ( ! $m( 'produkt' ) ) {
		return [];
	}
	return [ [
		'produkt_id'       => (int) $m( 'produkt_id' ),
		'produkt'          => (string) $m( 'produkt' ),
		'sku'              => (string) $m( 'sku' ),
		'forma'            => (string) $m( 'forma' ),
		'forma_klucz'      => (string) $m( 'forma_klucz' ),
		'frakcja'          => (string) $m( 'frakcja' ),
		'ilosc'            => $m( 'ilosc_podana' ),
		'jednostka'        => (string) $m( 'jednostka' ),
		'tony'             => $m( 'tony' ),
		'palet'            => $m( 'palet' ),
		'zaklad'           => (string) $m( 'zaklad' ),
		'zaklad_term_id'   => (int) $m( 'zaklad_term_id' ),
		'km'               => (int) $m( 'km' ),
		'cena_proponowana' => $m( 'cena_proponowana' ) !== '' ? (int) $m( 'cena_proponowana' ) : null,
		'cena_podana'      => $m( 'cena_podana' ) !== '' ? (int) $m( 'cena_podana' ) : null,
		'cena_min'         => $m( 'cena_min' ) !== '' ? (int) $m( 'cena_min' ) : null,
		'wartosc'          => (int) $m( 'wartosc_towaru' ),
	] ];
}

/** Grupy transportowe oferty — jak wyzej, oba formaty. */
function agria_of_grupy_oferty( int $id ): array {
	$g = get_post_meta( $id, 'agria_of_grupy', true );
	if ( is_array( $g ) && $g ) {
		return $g;
	}
	$m = fn( string $k ) => get_post_meta( $id, 'agria_of_' . $k, true );
	if ( ! $m( 'zaklad' ) ) {
		return [];
	}
	return [ [
		'zaklad'                => (string) $m( 'zaklad' ),
		'zaklad_term_id'        => (int) $m( 'zaklad_term_id' ),
		'km'                    => (int) $m( 'km' ),
		'km_pewne'              => (int) $m( 'km_pewne' ),
		'tony'                  => $m( 'tony' ),
		'metoda'                => (string) $m( 'metoda' ),
		'metoda_id'             => (string) $m( 'metoda_id' ),
		'kursy'                 => (int) $m( 'kursy' ) ?: 1,
		'transport_proponowany' => (int) $m( 'transport_proponowany' ),
		'transport_podany'      => (int) $m( 'transport_podany' ),
		'wypelnienie'           => null,
	] ];
}

/**
 * Roznica wobec cennika, w groszach: [wg cennika, podane].
 * Stare oferty nie mialy tych sum policzonych przy zapisie — skladamy je z pozycji.
 */
function agria_of_roznica_oferty( int $id ): array {
	$prop = get_post_meta( $id, 'agria_of_towar_wg_cennika', true );
	$pod  = get_post_meta( $id, 'agria_of_towar_podany', true );
	if ( $prop !== '' && $pod !== '' ) {
		return [ (int) $prop, (int) $pod ];
	}
	$prop = $pod = 0;
	foreach ( agria_of_pozycje_oferty( $id ) as $p ) {
		if ( $p['cena_proponowana'] !== null && $p['cena_podana'] !== null ) {
			$prop += (int) round( $p['cena_proponowana'] * (float) $p['tony'] );
			$pod  += (int) $p['wartosc'];
		}
	}
	return [ $prop, $pod ];
}
