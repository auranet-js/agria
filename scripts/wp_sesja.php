<?php
/**
 * Ciasteczka sesji WordPressa dla istniejącego konta — bez znajomości hasła.
 *
 * WP-CLI działa wewnątrz WordPressa, więc ma dostęp do kluczy uwierzytelniających
 * (AUTH_KEY, LOGGED_IN_KEY itd.) i może podpisać ciasteczko dokładnie tak samo,
 * jak zrobiłby to formularz logowania. Hasło nie jest do tego potrzebne
 * i nigdzie tu nie występuje.
 *
 * Po co: żeby Puppeteer wchodził do panelu WordPressa (analiza Rank Math, Elementor)
 * bez pożyczania przeglądarki Janka. Wynik idzie do ~/secrets/agria/wp-sesja.json (600).
 *
 * ODCIĘCIE — jedna komenda na serwerze, unieważnia wyłącznie tę sesję:
 *     wp --path=. --user=1 eval 'WP_Session_Tokens::get_instance(1)->destroy("TOKEN");'
 * albo wszystkie sesje konta naraz:
 *     wp --path=. user session destroy 1 --all
 *
 * Uwaga na ślad audytowy: sesja jest wystawiona na konto `js` (ID 1), więc wpisy
 * w historii WordPressa będą podpisane Jankiem. Czystsze byłoby osobne konto
 * serwisowe — do decyzji, tworzenie użytkowników wymaga osobnej zgody.
 *
 * Użycie (na serwerze agria-prod, z katalogu WordPressa):
 *     wp --path=. --user=1 eval-file wp_sesja.php
 */

$user_id = 1;
$dni     = 30;
$exp     = time() + $dni * DAY_IN_SECONDS;

$user = get_user_by( 'id', $user_id );
if ( ! $user ) {
	fwrite( STDERR, "brak uzytkownika $user_id\n" );
	exit( 1 );
}

$manager = WP_Session_Tokens::get_instance( $user_id );
$token   = $manager->create( $exp );

echo json_encode(
	[
		'user'    => $user->user_login,
		'user_id' => $user_id,
		'wygasa'  => gmdate( 'Y-m-d H:i', $exp ) . ' UTC',
		'token'   => $token,
		'domena'  => parse_url( home_url(), PHP_URL_HOST ),
		'cookies' => [
			LOGGED_IN_COOKIE   => wp_generate_auth_cookie( $user_id, $exp, 'logged_in', $token ),
			SECURE_AUTH_COOKIE => wp_generate_auth_cookie( $user_id, $exp, 'secure_auth', $token ),
		],
	],
	JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE
);
