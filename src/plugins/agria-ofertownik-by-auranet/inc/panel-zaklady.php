<?php
/**
 * Panel: zaklady wysylkowe — wspolrzedne i ich poprawianie.
 *
 * Ekran istnieje z konkretnego powodu. Dopasowanie zakladu do miejscowosci po samej nazwie
 * pomylilo sie na CZTERECH z czternastu (25.08.2026): Checiny trafily do lubuskiego zamiast
 * pod Kielce, Lagow do dolnoslaskiego, Bukowa do lodzkiego, a „Kornica" zlapala „Piskornice"
 * pod Radomiem — 180 km od wlasciwego miejsca. Filtr po kodzie pocztowym to naprawil,
 * ale nazwy miejscowosci w Polsce powtarzaja sie na tyle czesto, ze przy kazdym nowym zakladzie
 * czlowiek musi miec gdzie zajrzec i poprawic.
 *
 * Dlatego: kazdy zaklad pokazuje, ktora miejscowosc dostal, czy dopasowanie bylo pewne,
 * i pozwala wybrac inna z listy kandydatow albo wpisac wspolrzedne recznie.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'admin_menu', function (): void {
	add_submenu_page( 'agria-of-cennik', 'Zakłady', 'Zakłady', AGRIA_OF_CAP,
		'agria-of-zaklady', 'agria_of_ekran_zakladow' );
}, 11 );

function agria_of_ekran_zakladow(): void {
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_die( 'Brak uprawnien.' );
	}
	global $wpdb;

	if ( isset( $_POST['agria_of_zaklady_nonce'] ) && wp_verify_nonce( $_POST['agria_of_zaklady_nonce'], 'agria_of_zaklady' ) ) {
		$zmian = 0;
		foreach ( (array) ( $_POST['wybor'] ?? [] ) as $term_id => $mie_id ) {
			if ( $mie_id === '' ) {
				continue;
			}
			$m = agria_of_miejscowosc( (int) $mie_id );
			if ( $m ) {
				agria_of_ustaw_wspolrzedne_zakladu( (int) $term_id, (float) $m['lat'], (float) $m['lon'], true );
				$zmian++;
			}
		}
		foreach ( (array) ( $_POST['lat'] ?? [] ) as $term_id => $lat ) {
			$lon = $_POST['lon'][ $term_id ] ?? '';
			if ( $lat === '' || $lon === '' ) {
				continue;
			}
			$stare = agria_of_wspolrzedne_zakladu( (int) $term_id );
			if ( $stare && abs( $stare['lat'] - (float) $lat ) < 0.00001 && abs( $stare['lon'] - (float) $lon ) < 0.00001 ) {
				continue;
			}
			agria_of_ustaw_wspolrzedne_zakladu( (int) $term_id, (float) $lat, (float) $lon, true );
			$zmian++;
		}
		if ( $zmian ) {
			printf( '<div class="notice notice-success"><p>Poprawiono %d %s. Trasy liczone od starego punktu zostały skasowane — policzą się na nowo przy najbliższej wycenie.</p></div>',
				$zmian, $zmian === 1 ? 'zakład' : 'zakłady' );
		}
	}

	if ( isset( $_GET['przelicz'] ) && check_admin_referer( 'agria_of_przelicz_geo' ) ) {
		$w = agria_of_zasiej_wspolrzedne_zakladow( true );
		$niepewne = count( array_filter( $w, fn( $r ) => ( $r['stan'] ?? '' ) !== 'ok' ) );
		printf( '<div class="notice notice-%s"><p>Dopasowano %d zakładów, z tego %d wymaga sprawdzenia.</p></div>',
			$niepewne ? 'warning' : 'success', count( $w ), $niepewne );
	}

	$termy = get_terms( [ 'taxonomy' => AGRIA_OF_TAX_ZAKLAD, 'hide_empty' => true ] );
	$trasy = agria_of_tabela( 'trasy' );
	?>
	<div class="wrap">
		<h1>Zakłady wysyłkowe</h1>
		<p class="description">
			Z tych punktów liczą się kilometry do klienta, więc błąd tutaj wraca jako błąd na fakturze.
			Współrzędne dopasowujemy po nazwie i kodzie pocztowym — <strong>nazwy miejscowości w Polsce
			się powtarzają</strong>, więc pozycje oznaczone jako niepewne trzeba przejrzeć okiem.
		</p>
		<p>
			<a class="button" href="<?php echo esc_url( wp_nonce_url( admin_url( 'admin.php?page=agria-of-zaklady&przelicz=1' ), 'agria_of_przelicz_geo' ) ); ?>">
				Dopasuj wszystkie od nowa
			</a>
		</p>

		<form method="post">
			<?php wp_nonce_field( 'agria_of_zaklady', 'agria_of_zaklady_nonce' ); ?>
			<table class="wp-list-table widefat striped">
				<thead><tr>
					<th>Zakład</th><th style="width:6rem">Produktów</th><th style="width:9rem">Stan</th>
					<th style="width:22rem">Miejscowość</th>
					<th style="width:14rem">Współrzędne</th><th style="width:8rem">Tras w pamięci</th>
				</tr></thead>
				<tbody>
				<?php foreach ( $termy as $t ) :
					$w      = agria_of_wspolrzedne_zakladu( $t->term_id );
					$pewne  = get_term_meta( $t->term_id, 'agria_of_geo_pewne', true ) !== '0';
					$ile    = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(*) FROM {$trasy} WHERE zaklad_term_id=%d", $t->term_id ) );
					$kandydaci = ( ! $w || ! $pewne ) ? agria_of_kandydaci_zakladu( $t->name ) : [];
					?>
					<tr>
						<td><strong><?php echo esc_html( agria_of_nazwa_zakladu( $t->name ) ); ?></strong>
							<br><span class="description"><?php echo esc_html( agria_of_kod_zakladu( $t->name ) ?: '—' ); ?></span></td>
						<td><?php echo (int) $t->count; ?></td>
						<td><?php if ( ! $w ) : ?>
								<span style="color:#a33">brak punktu</span>
							<?php elseif ( ! $pewne ) : ?>
								<span style="color:#b8801f">do sprawdzenia</span>
							<?php else : ?>
								<span style="color:#2d6a2d">ustalony</span>
							<?php endif; ?></td>
						<td><?php if ( $kandydaci ) : ?>
								<select name="wybor[<?php echo (int) $t->term_id; ?>]" style="width:100%">
									<option value="">— zostaw jak jest —</option>
									<?php foreach ( $kandydaci as $k ) : ?>
										<option value="<?php echo (int) $k['id']; ?>">
											<?php echo esc_html( sprintf( '%s — pow. %s, %s', $k['nazwa'], $k['powiat'] ?: '?', $k['wojewodztwo'] ) ); ?>
										</option>
									<?php endforeach; ?>
								</select>
							<?php else : ?>
								<span class="description">dopasowana automatycznie</span>
							<?php endif; ?></td>
						<td>
							<input type="text" name="lat[<?php echo (int) $t->term_id; ?>]" style="width:6em"
								value="<?php echo $w ? esc_attr( number_format( $w['lat'], 5, '.', '' ) ) : ''; ?>" placeholder="lat">
							<input type="text" name="lon[<?php echo (int) $t->term_id; ?>]" style="width:6em"
								value="<?php echo $w ? esc_attr( number_format( $w['lon'], 5, '.', '' ) ) : ''; ?>" placeholder="lon">
						</td>
						<td><?php echo $ile ?: '—'; ?></td>
					</tr>
				<?php endforeach; ?>
				</tbody>
			</table>
			<p><button class="button button-primary">Zapisz zakłady</button></p>
		</form>
	</div>
	<?php
}
