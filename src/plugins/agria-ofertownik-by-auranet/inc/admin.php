<?php
/**
 * Panel: cennik i ustawienia transportu — ekrany, ktore obsluguje AGRIA (spec §4.7).
 *
 * Jeden ekran zbiorczy zamiast panelu wariantow WooCommerce: 78 pozycji trzeba widziec naraz,
 * przefiltrowac po produkcie i wpisac cene w miejscu. Panel wariantow przy tej liczbie
 * jest nie do przejscia — i to byl argument juz w specyfikacji, zanim odpadly same warianty.
 */

defined( 'ABSPATH' ) || exit;



add_action( 'admin_menu', function (): void {
	add_menu_page( 'Ofertownik', 'Ofertownik', AGRIA_OF_CAP, 'agria-of-cennik',
		'agria_of_ekran_cennika', 'dashicons-calculator', 56 );
	add_submenu_page( 'agria-of-cennik', 'Cennik', 'Cennik', AGRIA_OF_CAP, 'agria-of-cennik', 'agria_of_ekran_cennika' );
	add_submenu_page( 'agria-of-cennik', 'Transport', 'Transport', AGRIA_OF_CAP, 'agria-of-transport', 'agria_of_ekran_transportu' );
} );

function agria_of_ekran_cennika(): void {
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_die( 'Brak uprawnien.' );
	}
	global $wpdb;
	$tab = agria_of_tabela( 'ceny' );
	$komunikaty = [];

	if ( isset( $_POST['agria_of_cennik_nonce'] ) && wp_verify_nonce( $_POST['agria_of_cennik_nonce'], 'agria_of_cennik' ) ) {
		foreach ( (array) ( $_POST['cena'] ?? [] ) as $id => $wartosc ) {
			$id = (int) $id;
			$nowa = agria_of_na_grosze( sanitize_text_field( $wartosc ) );
			$stara = $wpdb->get_var( $wpdb->prepare( "SELECT cena FROM {$tab} WHERE id=%d", $id ) );
			$stara = $stara === null ? null : (int) $stara;
			if ( $nowa === $stara ) {
				continue;
			}
			$w = agria_of_ustaw_cene( $id, 'cena', $nowa, get_current_user_id() );
			if ( $w['ostrzezenie'] ) {
				$komunikaty[] = $w['ostrzezenie'];
			}
		}
		foreach ( (array) ( $_POST['cena_min'] ?? [] ) as $id => $wartosc ) {
			$id = (int) $id;
			$nowa = agria_of_na_grosze( sanitize_text_field( $wartosc ) );
			$stara = $wpdb->get_var( $wpdb->prepare( "SELECT cena_min FROM {$tab} WHERE id=%d", $id ) );
			$stara = $stara === null ? null : (int) $stara;
			if ( $nowa !== $stara ) {
				agria_of_ustaw_cene( $id, 'cena_min', $nowa, get_current_user_id() );
			}
		}
		echo '<div class="notice notice-success"><p>Cennik zapisany.</p></div>';
		foreach ( $komunikaty as $k ) {
			echo '<div class="notice notice-warning"><p><strong>Uwaga.</strong> ' . esc_html( $k ) . '</p></div>';
		}
	}

	if ( isset( $_GET['zasiej'] ) && check_admin_referer( 'agria_of_zasiej' ) ) {
		$w = agria_of_zasiej_cennik();
		printf( '<div class="notice notice-success"><p>Dodano %d brakujacych pozycji, %d juz bylo (nietkniete).</p></div>',
			$w['dodane'], $w['pominiete'] );
	}

	$filtr = isset( $_GET['produkt'] ) ? (int) $_GET['produkt'] : 0;
	$where = $filtr ? $wpdb->prepare( 'WHERE c.produkt_id=%d', $filtr ) : '';
	$wiersze = $wpdb->get_results( "SELECT c.* FROM {$tab} c {$where} ORDER BY c.produkt_id, c.zaklad_term_id, c.forma_term_id, c.frakcja", ARRAY_A );

	$bez_ceny = (int) $wpdb->get_var( "SELECT COUNT(*) FROM {$tab} WHERE cena IS NULL" );
	?>
	<div class="wrap">
		<h1>Cennik ofertownika</h1>
		<p class="description">
			Ceny <strong>netto za tone</strong>, za sam towar, bez transportu. Nie sa nigdzie publikowane —
			nie trafiaja ani na strone, ani do REST API, ani do danych strukturalnych.
			<?php if ( $bez_ceny ) : ?>
				<br><strong><?php echo $bez_ceny; ?></strong> pozycji nie ma jeszcze ceny — przy nich wycena powie „do ustalenia".
			<?php endif; ?>
		</p>

		<form method="get" style="margin:1em 0">
			<input type="hidden" name="page" value="agria-of-cennik">
			<select name="produkt" onchange="this.form.submit()">
				<option value="0">— wszystkie produkty —</option>
				<?php foreach ( agria_of_produkty() as $p ) : ?>
					<option value="<?php echo $p->ID; ?>" <?php selected( $filtr, $p->ID ); ?>>
						<?php echo esc_html( wp_strip_all_tags( html_entity_decode( $p->post_title ) ) ); ?>
					</option>
				<?php endforeach; ?>
			</select>
			<a class="button" href="<?php echo esc_url( wp_nonce_url( admin_url( 'admin.php?page=agria-of-cennik&zasiej=1' ), 'agria_of_zasiej' ) ); ?>">
				Dodaj brakujace pozycje
			</a>
		</form>

		<form method="post">
			<?php wp_nonce_field( 'agria_of_cennik', 'agria_of_cennik_nonce' ); ?>
			<table class="wp-list-table widefat striped">
				<thead><tr>
					<th>Produkt</th><th>Zaklad</th><th>Forma</th><th>Frakcja</th>
					<th style="width:9em">Cena zl/t</th><th style="width:9em">Minimalna</th><th>Ostatnia zmiana</th>
				</tr></thead>
				<tbody>
				<?php foreach ( $wiersze as $w ) :
					$zaklad = get_term( (int) $w['zaklad_term_id'] );
					$forma  = get_term( (int) $w['forma_term_id'] );
					$kto    = $w['zmienil'] ? get_userdata( (int) $w['zmienil'] ) : null;
					?>
					<tr>
						<td><?php echo esc_html( wp_strip_all_tags( html_entity_decode( get_the_title( (int) $w['produkt_id'] ) ) ) ); ?>
							<br><span class="description"><?php echo esc_html( get_post_meta( (int) $w['produkt_id'], '_sku', true ) ?: '—' ); ?></span></td>
						<td><?php echo esc_html( $zaklad ? agria_of_nazwa_zakladu( $zaklad->name ) : '?' ); ?></td>
						<td><?php echo esc_html( $forma ? $forma->name : '?' ); ?></td>
						<td><?php echo esc_html( $w['frakcja'] ?: '—' ); ?></td>
						<td><input type="text" name="cena[<?php echo (int) $w['id']; ?>]" style="width:100%"
								   value="<?php echo $w['cena'] !== null ? esc_attr( number_format( (float) agria_of_na_zlote( (int) $w['cena'] ), 2, ',', '' ) ) : ''; ?>"
								   placeholder="brak"></td>
						<td><input type="text" name="cena_min[<?php echo (int) $w['id']; ?>]" style="width:100%"
								   value="<?php echo $w['cena_min'] !== null ? esc_attr( number_format( (float) agria_of_na_zlote( (int) $w['cena_min'] ), 2, ',', '' ) ) : ''; ?>"
								   placeholder="—"></td>
						<td class="description">
							<?php echo $kto ? esc_html( $kto->display_name ) . ', ' : ''; ?>
							<?php echo esc_html( $w['zmieniono'] ? mysql2date( 'j.m.Y H:i', $w['zmieniono'] ) : '—' ); ?>
						</td>
					</tr>
				<?php endforeach; ?>
				</tbody>
			</table>
			<p><button class="button button-primary">Zapisz cennik</button></p>
		</form>
	</div>
	<?php
}

function agria_of_ekran_transportu(): void {
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_die( 'Brak uprawnien.' );
	}

	if ( isset( $_POST['agria_of_transport_nonce'] ) && wp_verify_nonce( $_POST['agria_of_transport_nonce'], 'agria_of_transport' ) ) {
		$t = agria_of_transport();
		foreach ( $t as $klucz => $metoda ) {
			if ( isset( $_POST['stawka_km'][ $klucz ] ) ) {
				$t[ $klucz ]['stawka_km'] = agria_of_na_grosze( sanitize_text_field( $_POST['stawka_km'][ $klucz ] ) );
			}
			if ( isset( $_POST['stawka_paleta'][ $klucz ] ) ) {
				$t[ $klucz ]['stawka_paleta'] = agria_of_na_grosze( sanitize_text_field( $_POST['stawka_paleta'][ $klucz ] ) );
			}
			if ( isset( $_POST['ladownosc'][ $klucz ] ) && $_POST['ladownosc'][ $klucz ] !== '' ) {
				$t[ $klucz ]['ladownosc_kg'] = (int) round( (float) str_replace( ',', '.', $_POST['ladownosc'][ $klucz ] ) * 1000 );
			}
			$t[ $klucz ]['oba_kierunki'] = ! empty( $_POST['oba_kierunki'][ $klucz ] );
		}
		update_option( AGRIA_OF_OPCJA_TRANSPORT, $t );

		$p = agria_of_paleta();
		foreach ( $p as $klucz => $dane ) {
			if ( isset( $_POST['paleta_sztuk'][ $klucz ] ) && $_POST['paleta_sztuk'][ $klucz ] !== '' ) {
				$p[ $klucz ]['sztuk']    = (int) $_POST['paleta_sztuk'][ $klucz ];
				$p[ $klucz ]['szacunek'] = false; // wpisane przez czlowieka przestaje byc naszym szacunkiem
			}
			if ( isset( $_POST['paleta_masa'][ $klucz ] ) && $_POST['paleta_masa'][ $klucz ] !== '' ) {
				$p[ $klucz ]['masa_kg'] = (int) $_POST['paleta_masa'][ $klucz ];
			}
		}
		update_option( AGRIA_OF_OPCJA_PALETA, $p );
		echo '<div class="notice notice-success"><p>Ustawienia zapisane.</p></div>';
	}

	$transport = agria_of_transport();
	$paleta    = agria_of_paleta();
	?>
	<div class="wrap">
		<h1>Transport</h1>
		<p class="description">
			Stawki netto. <strong>Beczka i wanna licza sie w dwie strony</strong> — auto wraca puste
			i AGRIA placi za powrot; naczepa liczy sie w jedna. Kurier bierze palete niezaleznie od masy.
			<br><em>Wartosci wyjsciowe pochodza od nas, nie z cennika — poprawcie je, gdy rozjezdzaja sie z rzeczywistoscia.</em>
		</p>

		<form method="post">
			<?php wp_nonce_field( 'agria_of_transport', 'agria_of_transport_nonce' ); ?>
			<table class="wp-list-table widefat striped">
				<thead><tr><th>Metoda</th><th>Stawka zl/km</th><th>Za palete</th><th>W dwie strony</th><th>Ladownosc (t)</th><th>Wozi</th></tr></thead>
				<tbody>
				<?php foreach ( $transport as $klucz => $m ) : ?>
					<tr>
						<td><strong><?php echo esc_html( $m['nazwa'] ); ?></strong></td>
						<td><?php if ( isset( $m['stawka_km'] ) ) : ?>
							<input type="text" name="stawka_km[<?php echo esc_attr( $klucz ); ?>]" style="width:7em"
								   value="<?php echo esc_attr( number_format( (float) agria_of_na_zlote( (int) $m['stawka_km'] ), 2, ',', '' ) ); ?>">
						<?php else : ?>—<?php endif; ?></td>
						<td><?php if ( isset( $m['stawka_paleta'] ) ) : ?>
							<input type="text" name="stawka_paleta[<?php echo esc_attr( $klucz ); ?>]" style="width:7em"
								   value="<?php echo esc_attr( number_format( (float) agria_of_na_zlote( (int) $m['stawka_paleta'] ), 2, ',', '' ) ); ?>">
						<?php else : ?>—<?php endif; ?></td>
						<td><input type="checkbox" name="oba_kierunki[<?php echo esc_attr( $klucz ); ?>]" value="1" <?php checked( ! empty( $m['oba_kierunki'] ) ); ?>></td>
						<td><?php if ( $m['ladownosc_kg'] ) : ?>
							<input type="text" name="ladownosc[<?php echo esc_attr( $klucz ); ?>]" style="width:5em"
								   value="<?php echo esc_attr( number_format( $m['ladownosc_kg'] / 1000, 0, ',', '' ) ); ?>">
						<?php else : ?>—<?php endif; ?></td>
						<td class="description"><?php echo esc_html( implode( ', ', $m['formy'] ) ); ?></td>
					</tr>
				<?php endforeach; ?>
				</tbody>
			</table>

			<h2>Paleta</h2>
			<p class="description">
				Paleta to jednostka miejsca na aucie, nie miary towaru — nie da sie jej wypelnic w polowie.
				Ile worków na nia wchodzi, wiecie Wy; <strong>ponizsze liczby oznaczone jako szacunek sa nasze</strong>
				i sluza tylko po to, zeby narzedzie dzialalo od pierwszego dnia.
			</p>
			<table class="wp-list-table widefat striped" style="max-width:56em">
				<thead><tr><th>Forma</th><th>Sztuk na palecie</th><th>Masa palety (kg)</th><th></th></tr></thead>
				<tbody>
				<?php foreach ( $paleta as $klucz => $d ) : ?>
					<tr>
						<td><?php echo esc_html( str_replace( '-', ' ', $klucz ) ); ?></td>
						<td><input type="number" name="paleta_sztuk[<?php echo esc_attr( $klucz ); ?>]" style="width:6em" value="<?php echo (int) $d['sztuk']; ?>"></td>
						<td><input type="number" name="paleta_masa[<?php echo esc_attr( $klucz ); ?>]" style="width:7em" value="<?php echo (int) $d['masa_kg']; ?>"></td>
						<td class="description"><?php echo ! empty( $d['szacunek'] ) ? '<em>nasz szacunek — do potwierdzenia</em>' : 'potwierdzone'; ?></td>
					</tr>
				<?php endforeach; ?>
				</tbody>
			</table>
			<p><button class="button button-primary">Zapisz ustawienia</button></p>
		</form>
	</div>
	<?php
}
