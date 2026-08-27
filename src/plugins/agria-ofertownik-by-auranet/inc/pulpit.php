<?php
/**
 * Pulpit — to, co widac zaraz po zalogowaniu.
 *
 * Prosto: przycisk „Nowa oferta" po lewej, pod spodem lista wszystkich ofert.
 * WSZYSTKICH, nie tylko swoich — Bogdan bierze telefon po Kazimierzu i musi widziec,
 * co tamten wycenil. Przy trzech osobach ukrywanie ofert przed soba nie ma sensu,
 * a szukanie „gdzie jest ta wycena z wtorku" ma koszt liczony w minutach przy kliencie.
 *
 * Kazdy wiersz mowi, KTO wystawil i — jesli ktos ja pozniej ruszyl — KTO zaktualizowal.
 * Wzorzec sladu edycji przeniesiony z victorini2025 (`saved-carts-cpt.php`).
 */

defined( 'ABSPATH' ) || exit;

/** Po zalogowaniu dzial handlowy ląduje na pulpicie, nie w kokpicie WordPressa. */
add_filter( 'login_redirect', function ( $do_czego, $zadane, $user ) {
	if ( is_wp_error( $user ) || ! $user instanceof WP_User ) {
		return $do_czego;
	}
	// Zadany cel wygrywa — nie odbieramy nikomu linku, w ktory kliknal.
	if ( $zadane && ! str_contains( (string) $zadane, '/wp-admin/' ) ) {
		return $do_czego;
	}
	return user_can( $user, AGRIA_OF_CAP ) ? home_url( '/wycena/' ) : $do_czego;
}, 10, 3 );

function agria_of_render_pulpit(): void {
	$oferty = get_posts( [
		'post_type'      => AGRIA_OF_CPT_OFERTA,
		'post_status'    => 'publish',
		'posts_per_page' => 60,
		'orderby'        => 'date',
		'order'          => 'DESC',
	] );
	$zl = fn( $g ) => $g === '' || $g === null ? '—' : number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );
	?><!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Oferty — AGRIA</title>
<style>
<?php agria_of_style_wspolny(); ?>
.pulpit{display:grid;grid-template-columns:15rem 1fr;gap:0;align-items:start;}
@media(max-width:60rem){.pulpit{grid-template-columns:1fr;}}
.bok{padding:1.2rem;border-right:1px solid var(--kreska);background:var(--karta);
	position:sticky;top:2.8rem;align-self:start;}
@media(max-width:60rem){.bok{position:static;border-right:0;border-bottom:1px solid var(--kreska);}}
.nowa{display:block;text-align:center;padding:.75rem 1rem;background:var(--zielen);
	color:var(--przycisk-tekst);border:1px solid var(--zielen);border-radius:2px;
	font-weight:600;text-decoration:none;}
.nowa:hover{opacity:.9;}
.bok nav{margin-top:1.2rem;display:grid;gap:.15rem;}
.bok nav a{color:var(--tekst);text-decoration:none;padding:.3rem .1rem;font-size:.9rem;}
.bok nav a:hover{color:var(--zielen);}
.bok .etyk{font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--slaby);
	margin:1.4rem 0 .4rem;font-weight:600;}
.lista{padding:0 0 4rem;}
.lista h1{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--slaby);
	padding:1rem 1.2rem .4rem;margin:0;font-weight:600;}
table{width:100%;border-collapse:collapse;}
thead th{font-size:.66rem;letter-spacing:.09em;text-transform:uppercase;color:var(--slaby);
	font-weight:600;text-align:left;padding:.45rem .6rem;border-bottom:1px solid var(--kreska-mocna);
	background:var(--karta);position:sticky;top:2.8rem;}
tbody td{padding:.5rem .6rem;border-bottom:1px solid var(--kreska);vertical-align:top;}
tbody tr:hover{background:var(--zielen-jasna);}
.p{text-align:right;}
.kwota{font-family:ui-monospace,Menlo,Consolas,monospace;font-variant-numeric:tabular-nums;}
.kto{font-size:.78rem;color:var(--cichy);}
.kto b{color:var(--tekst);font-weight:600;}
.edytowal{color:var(--ochra);}
.klient{font-weight:600;}
.gdzie{font-size:.8rem;color:var(--cichy);}
.dzialania a{font-size:.8rem;color:var(--zielen);text-decoration:none;margin-right:.6rem;}
.dzialania a:hover{text-decoration:underline;}
.rabat-w-dol{color:var(--alarm);}
.rabat-w-gore{color:var(--zielen);}
.pusto{padding:2rem 1.2rem;color:var(--cichy);}
.znacznik{font-size:.7rem;padding:.1rem .35rem;border:1px solid var(--kreska-mocna);
	border-radius:2px;color:var(--cichy);}
</style>
</head>
<body>

<div class="gora">
	<span class="marka">AGRIA <span>· oferty</span></span>
	<span class="kto"><?php echo esc_html( wp_get_current_user()->display_name ); ?>
		· <a href="<?php echo esc_url( wp_logout_url( home_url( '/wycena/' ) ) ); ?>">wyloguj</a></span>
</div>

<div class="pulpit">
	<aside class="bok">
		<a class="nowa" href="<?php echo esc_url( home_url( '/wycena/?nowa=1' ) ); ?>">Nowa oferta</a>
		<div class="etyk">Ustawienia</div>
		<nav>
			<a href="<?php echo esc_url( admin_url( 'admin.php?page=agria-of-cennik' ) ); ?>">Cennik</a>
			<a href="<?php echo esc_url( admin_url( 'admin.php?page=agria-of-transport' ) ); ?>">Transport</a>
			<a href="<?php echo esc_url( admin_url( 'admin.php?page=agria-of-zaklady' ) ); ?>">Zakłady</a>
		</nav>
		<div class="etyk">Podsumowania</div>
		<nav>
			<a href="<?php echo esc_url( admin_url( 'admin.php?page=agria-of-zestawienie' ) ); ?>">Zestawienie</a>
			<a href="<?php echo esc_url( admin_url( 'edit.php?post_type=agria_client' ) ); ?>">Klienci</a>
		</nav>
	</aside>

	<main class="lista">
		<h1>Ostatnie wyceny</h1>
		<?php if ( ! $oferty ) : ?>
			<p class="pusto">Nie ma jeszcze żadnej wyceny. Zacznij od „Nowa oferta”.</p>
		<?php else : ?>
		<table>
			<thead><tr>
				<th style="width:22%">Klient</th>
				<th>Co i skąd</th>
				<th style="width:7%" class="p">Tonaż</th>
				<th style="width:11%" class="p">Wartość netto</th>
				<th style="width:9%" class="p">Wobec cennika</th>
				<th style="width:15%">Kto</th>
				<th style="width:12%">Kiedy</th>
				<th style="width:9%"></th>
			</tr></thead>
			<tbody>
			<?php foreach ( $oferty as $o ) :
				$m       = fn( string $k ) => get_post_meta( $o->ID, 'agria_of_' . $k, true );
				$pozycje = agria_of_pozycje_oferty( $o->ID );
				$slad    = agria_of_slad_edycji( $o->ID );
				[ $prop, $pod ] = agria_of_roznica_oferty( $o->ID );
				$klient  = (string) $m( 'klient_nazwa' );
				if ( ! $klient && $m( 'klient_id' ) ) {
					$klient = get_the_title( (int) $m( 'klient_id' ) );
				}
				?>
				<tr>
					<td>
						<span class="klient"><?php echo esc_html( $klient ?: 'bez nazwy' ); ?></span>
						<?php if ( $m( 'klient_telefon' ) ) : ?>
							<br><span class="gdzie"><?php echo esc_html( (string) $m( 'klient_telefon' ) ); ?></span>
						<?php endif; ?>
					</td>
					<td>
						<?php
						$nazwy = array_map( fn( $p ) => $p['produkt'], $pozycje );
						echo esc_html( implode( ' · ', array_slice( $nazwy, 0, 2 ) ) );
						if ( count( $nazwy ) > 2 ) {
							printf( ' <span class="znacznik">+%d</span>', count( $nazwy ) - 2 );
						}
						?>
						<br><span class="gdzie"><?php echo esc_html( (string) $m( 'miejscowosc' ) ); ?>
							<?php if ( $m( 'kanal' ) ) : ?> · <?php echo esc_html( agria_of_kanaly()[ $m( 'kanal' ) ] ?? '' ); ?><?php endif; ?>
						</span>
					</td>
					<td class="p kwota"><?php echo esc_html( $m( 'tony' ) ); ?> t</td>
					<td class="p kwota"><strong><?php echo esc_html( $zl( $m( 'razem' ) ) ); ?></strong></td>
					<td class="p kwota"><?php
						if ( ! $prop || $prop === $pod ) {
							echo '<span class="gdzie">bez zmian</span>';
						} else {
							$r = $pod - $prop;
							printf( '<span class="%s">%s%.1f%%</span>',
								$r < 0 ? 'rabat-w-dol' : 'rabat-w-gore',
								$r < 0 ? '−' : '+', abs( $r ) / $prop * 100 );
						}
					?></td>
					<td class="kto">
						wystawił <b><?php echo esc_html( agria_of_wystawil( $o->ID ) ); ?></b>
						<?php if ( $slad ) : ?>
							<br><span class="edytowal">zaktualizował <b><?php echo esc_html( $slad['kto'] ); ?></b></span>
						<?php endif; ?>
					</td>
					<td class="kto">
						<?php echo esc_html( mysql2date( 'j.m.Y, H:i', (string) $m( 'wystawiono' ) ) ); ?>
						<?php if ( $slad && $slad['kiedy'] ) : ?>
							<br><span class="edytowal"><?php echo esc_html( mysql2date( 'j.m.Y, H:i', $slad['kiedy'] ) ); ?></span>
						<?php endif; ?>
					</td>
					<td class="dzialania">
						<a href="<?php echo esc_url( home_url( '/wycena/?edytuj=' . $o->ID ) ); ?>">edytuj</a>
						<a href="<?php echo esc_url( home_url( '/wycena/?agria_of_oferta=' . $o->ID ) ); ?>" target="_blank">wydruk</a>
					</td>
				</tr>
			<?php endforeach; ?>
			</tbody>
		</table>
		<?php endif; ?>
	</main>
</div>
</body>
</html>
	<?php
}
