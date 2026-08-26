<?php
/**
 * Panel: zestawienie sprzedazy — etap 2 ze specyfikacji.
 *
 * Odpowiada na pytanie, ktorego dzis nie da sie zadac: ile wycen padlo w miesiacu, na co,
 * w jakich rejonach, ktory kanal przynosi rozmowy i o ile schodzimy ponizej cennika.
 *
 * Nie wymagalo zbierania nowych danych — kazda oferta od poczatku trzyma cene proponowana
 * OBOK podanej i kanal kontaktu. To jest ten „efekt uboczny wart tyle co reszta" ze specyfikacji:
 * roznica jest mierzalna, bo lezy w bazie, a nie dlatego, ze ktos ja gdzies wpisal.
 *
 * Uwaga na czytanie liczb: kanaly ocenia sie dzis w AGRII po tym, ile razy ktos zobaczyl numer
 * telefonu. To pokazuje zainteresowanie, ale nie mowi, co sie z niego zrobilo. Oferty domykaja
 * ten lancuch — ale tylko dla telefonow, ktore handlowiec wycenil w narzedziu.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'admin_menu', function (): void {
	add_submenu_page( 'agria-of-cennik', 'Zestawienie', 'Zestawienie', AGRIA_OF_CAP,
		'agria-of-zestawienie', 'agria_of_ekran_zestawienia' );
}, 12 );

/** Oferty z okresu, z rozpakowanymi pozycjami. */
function agria_of_oferty_okresu( string $od, string $do ): array {
	return get_posts( [
		'post_type'      => AGRIA_OF_CPT_OFERTA,
		'post_status'    => 'publish',
		'posts_per_page' => -1,
		'date_query'     => [ [ 'after' => $od, 'before' => $do . ' 23:59:59', 'inclusive' => true ] ],
	] );
}

function agria_of_ekran_zestawienia(): void {
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_die( 'Brak uprawnien.' );
	}
	$od = sanitize_text_field( $_GET['od'] ?? date( 'Y-m-01' ) );
	$do = sanitize_text_field( $_GET['do'] ?? date( 'Y-m-d' ) );
	$zl = fn( $g ) => number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );

	$oferty = agria_of_oferty_okresu( $od, $do );

	$kanaly = $produkty = $rejony = $ludzie = [];
	$razem = $towar = $transport = $prop = $pod = 0;
	$tony = 0.0;
	$statusy = [];

	foreach ( $oferty as $o ) {
		$m = fn( string $k ) => get_post_meta( $o->ID, 'agria_of_' . $k, true );
		$kanal = (string) $m( 'kanal' );
		$razem     += (int) $m( 'razem' );
		$towar     += (int) $m( 'towar' );
		$transport += (int) $m( 'transport' );
		[ $o_prop, $o_pod ] = agria_of_roznica_oferty( $o->ID );
		$prop      += $o_prop;
		$pod       += $o_pod;
		$tony      += (float) $m( 'tony' );

		$kanaly[ $kanal ]['ile']   = ( $kanaly[ $kanal ]['ile'] ?? 0 ) + 1;
		$kanaly[ $kanal ]['razem'] = ( $kanaly[ $kanal ]['razem'] ?? 0 ) + (int) $m( 'razem' );
		$kanaly[ $kanal ]['tony']  = ( $kanaly[ $kanal ]['tony'] ?? 0 ) + (float) $m( 'tony' );
		$kanaly[ $kanal ]['prop']  = ( $kanaly[ $kanal ]['prop'] ?? 0 ) + $o_prop;
		$kanaly[ $kanal ]['pod']   = ( $kanaly[ $kanal ]['pod'] ?? 0 ) + $o_pod;

		$st = (string) $m( 'status' );
		$statusy[ $st ] = ( $statusy[ $st ] ?? 0 ) + 1;

		$woj = (string) $m( 'wojewodztwo' ) ?: '—';
		$rejony[ $woj ]['ile']  = ( $rejony[ $woj ]['ile'] ?? 0 ) + 1;
		$rejony[ $woj ]['tony'] = ( $rejony[ $woj ]['tony'] ?? 0 ) + (float) $m( 'tony' );

		$kto = (int) $m( 'wystawil' );
		$ludzie[ $kto ]['ile']   = ( $ludzie[ $kto ]['ile'] ?? 0 ) + 1;
		$ludzie[ $kto ]['razem'] = ( $ludzie[ $kto ]['razem'] ?? 0 ) + (int) $m( 'razem' );
		$ludzie[ $kto ]['prop']  = ( $ludzie[ $kto ]['prop'] ?? 0 ) + $o_prop;
		$ludzie[ $kto ]['pod']   = ( $ludzie[ $kto ]['pod'] ?? 0 ) + $o_pod;

		// Oferty sprzed 0.5.0 sa jednopozycyjne — shim oddaje je w tym samym ksztalcie.
		foreach ( agria_of_pozycje_oferty( $o->ID ) as $p ) {
			$k = $p['produkt'] ?: '?';
			$produkty[ $k ]['ile']     = ( $produkty[ $k ]['ile'] ?? 0 ) + 1;
			$produkty[ $k ]['tony']    = ( $produkty[ $k ]['tony'] ?? 0 ) + (float) $p['tony'];
			$produkty[ $k ]['wartosc'] = ( $produkty[ $k ]['wartosc'] ?? 0 ) + (int) $p['wartosc'];
		}
	}

	uasort( $kanaly,   fn( $a, $b ) => $b['razem'] <=> $a['razem'] );
	uasort( $produkty, fn( $a, $b ) => $b['tony'] <=> $a['tony'] );
	uasort( $rejony,   fn( $a, $b ) => $b['tony'] <=> $a['tony'] );

	$rabat = fn( int $prop, int $pod ): string => $prop
		? sprintf( '%s%.1f%%', $pod >= $prop ? '+' : '−', abs( $pod - $prop ) / $prop * 100 )
		: '—';
	?>
	<div class="wrap">
		<h1>Zestawienie</h1>

		<form method="get" style="margin:1em 0">
			<input type="hidden" name="page" value="agria-of-zestawienie">
			od <input type="date" name="od" value="<?php echo esc_attr( $od ); ?>">
			do <input type="date" name="do" value="<?php echo esc_attr( $do ); ?>">
			<button class="button">Pokaż</button>
		</form>

		<?php if ( ! $oferty ) : ?>
			<p>W tym okresie nie ma żadnej wyceny.</p>
		</div><?php return; endif; ?>

		<table class="wp-list-table widefat" style="max-width:52rem">
			<tr><th style="width:16rem">Wycen</th><td><strong><?php echo count( $oferty ); ?></strong></td></tr>
			<tr><th>Tonaż</th><td><?php echo esc_html( number_format( $tony, 1, ',', ' ' ) ); ?> t</td></tr>
			<tr><th>Wartość wycen</th><td><strong><?php echo esc_html( $zl( $razem ) ); ?> zł</strong>
				<span class="description">(towar <?php echo esc_html( $zl( $towar ) ); ?> + transport <?php echo esc_html( $zl( $transport ) ); ?>)</span></td></tr>
			<tr><th>Wobec cennika</th><td>
				<?php if ( $prop ) : ?>
					<strong style="color:<?php echo $pod < $prop ? '#a33' : '#2d6a2d'; ?>">
						<?php echo esc_html( $rabat( $prop, $pod ) ); ?></strong>
					<span class="description">— <?php echo esc_html( $zl( abs( $pod - $prop ) ) ); ?> zł
						<?php echo $pod < $prop ? 'poniżej' : 'powyżej'; ?> cennika</span>
				<?php else : ?>—<?php endif; ?></td></tr>
			<tr><th>Udział transportu</th><td><?php
				echo $razem ? esc_html( number_format( $transport / $razem * 100, 1, ',', ' ' ) ) . '%' : '—'; ?></td></tr>
		</table>

		<h2>Skąd przychodzą</h2>
		<p class="description">Dziś kanały ocenia się po tym, ile razy ktoś zobaczył numer telefonu.
			To pokazuje zainteresowanie, ale nie mówi, co się z niego zrobiło.</p>
		<table class="wp-list-table widefat striped" style="max-width:60rem">
			<thead><tr><th>Kanał</th><th>Wycen</th><th>Tonaż</th><th>Wartość</th><th>Wobec cennika</th></tr></thead>
			<tbody>
			<?php foreach ( $kanaly as $k => $d ) : ?>
				<tr>
					<td><strong><?php echo esc_html( agria_of_kanaly()[ $k ] ?? $k ); ?></strong></td>
					<td><?php echo (int) $d['ile']; ?></td>
					<td><?php echo esc_html( number_format( $d['tony'], 1, ',', ' ' ) ); ?> t</td>
					<td><?php echo esc_html( $zl( $d['razem'] ) ); ?> zł</td>
					<td><?php echo esc_html( $rabat( (int) $d['prop'], (int) $d['pod'] ) ); ?></td>
				</tr>
			<?php endforeach; ?>
			</tbody>
		</table>

		<h2>Co schodzi</h2>
		<table class="wp-list-table widefat striped" style="max-width:60rem">
			<thead><tr><th>Produkt</th><th>Na ilu wycenach</th><th>Tonaż</th><th>Wartość towaru</th></tr></thead>
			<tbody>
			<?php foreach ( $produkty as $k => $d ) : ?>
				<tr>
					<td><?php echo esc_html( $k ); ?></td>
					<td><?php echo (int) $d['ile']; ?></td>
					<td><?php echo esc_html( number_format( $d['tony'], 1, ',', ' ' ) ); ?> t</td>
					<td><?php echo esc_html( $zl( $d['wartosc'] ) ); ?> zł</td>
				</tr>
			<?php endforeach; ?>
			</tbody>
		</table>

		<h2>Dokąd jedzie</h2>
		<table class="wp-list-table widefat striped" style="max-width:40rem">
			<thead><tr><th>Województwo</th><th>Wycen</th><th>Tonaż</th></tr></thead>
			<tbody>
			<?php foreach ( $rejony as $k => $d ) : ?>
				<tr><td><?php echo esc_html( $k ); ?></td><td><?php echo (int) $d['ile']; ?></td>
					<td><?php echo esc_html( number_format( $d['tony'], 1, ',', ' ' ) ); ?> t</td></tr>
			<?php endforeach; ?>
			</tbody>
		</table>

		<h2>Kto wystawia</h2>
		<table class="wp-list-table widefat striped" style="max-width:52rem">
			<thead><tr><th>Osoba</th><th>Wycen</th><th>Wartość</th><th>Wobec cennika</th></tr></thead>
			<tbody>
			<?php foreach ( $ludzie as $uid => $d ) :
				$u = get_userdata( $uid ); ?>
				<tr>
					<td><?php echo esc_html( $u ? $u->display_name : '—' ); ?></td>
					<td><?php echo (int) $d['ile']; ?></td>
					<td><?php echo esc_html( $zl( $d['razem'] ) ); ?> zł</td>
					<td><?php echo esc_html( $rabat( (int) $d['prop'], (int) $d['pod'] ) ); ?></td>
				</tr>
			<?php endforeach; ?>
			</tbody>
		</table>

		<h2>Co się z nimi stało</h2>
		<p class="description">Status ustawia się ręcznie przy ofercie. Dopóki nikt tego nie robi,
			wszystko zostaje „wystawione" i ta tabela nie mówi nic o skuteczności.</p>
		<table class="wp-list-table widefat striped" style="max-width:32rem">
			<tbody>
			<?php foreach ( agria_of_statusy() as $k => $n ) : ?>
				<tr><td><?php echo esc_html( $n ); ?></td><td><?php echo (int) ( $statusy[ $k ] ?? 0 ); ?></td></tr>
			<?php endforeach; ?>
			</tbody>
		</table>
	</div>
	<?php
}
