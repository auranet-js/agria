<?php
/**
 * Bezpieczenstwo: ograniczenie ekspozycji kont uzytkownikow — Auranet 2026-08-19 (T-029)
 *
 * POWOD: audyt 15.06 wykazal, ze login administratora wychodzil na zewnatrz trzema
 * kanalami naraz: schema JSON-LD ("name":"js"), REST /wp-json/wp/v2/users
 * (publicznie, razem z "is_super_admin":true) oraz enumeracja /?author=N -> /author/js/.
 * Login to polowa pary logowania — jego ujawnienie zamienia atak na haslo w atak
 * na jedno pole zamiast dwoch.
 *
 * Dwa pierwsze kanaly zamknieto poza kodem, 19.08:
 *   - display_name i user_nicename uzytkownika 1 zmienione na "AGRIA Sp. z o.o." / "agria"
 *     (login `js` NIE byl zmieniany — to pole logowania),
 *   - Rank Math: disable_author_archives = on, co daje 301 na strone glowna
 *     dla /author/* oraz dla /?author=N.
 *
 * Ten plik domyka kanal trzeci: kolekcje uzytkownikow w REST API.
 *
 * ZAKRES: blokada dotyczy WYLACZNIE zadan nieuwierzytelnionych. Zalogowany uzytkownik
 * z uprawnieniem `list_users` dostaje pelna odpowiedz — inaczej rozsypuje sie panel,
 * edytor blokow i Elementor, ktore czytaja liste autorow.
 *
 * CZEGO TU NIE MA: blokady /wp-json/wp/v2/posts?_fields=author — numer autora (1)
 * sam w sobie nie jest sekretem, a wylaczenie pola psuje integracje. Nie ruszamy tez
 * naglowka Link rel="https://api.w.org/", bo wskazuje on korzen API, nie uzytkownika.
 */

defined( 'ABSPATH' ) || exit;

if ( ! function_exists( 'agria_block_anon_user_endpoints' ) ) {
	/**
	 * Zwraca 401 dla anonimowych zapytan o /wp/v2/users oraz /wp/v2/users/<id>.
	 *
	 * @param mixed           $wynik   Dotychczasowy wynik (null = brak decyzji).
	 * @param mixed           $serwer  Instancja WP_REST_Server.
	 * @param WP_REST_Request $zadanie Zadanie REST.
	 * @return mixed
	 */
	function agria_block_anon_user_endpoints( $wynik, $serwer, $zadanie ) {
		if ( ! empty( $wynik ) ) {
			return $wynik;
		}
		// Przepuszczamy kazdego zalogowanego, kto w ogole redaguje tresc.
		// Warunek `list_users` (tylko administrator) odcinal redaktorowi liste autorow
		// w edytorze blokow — sprawdzone 19.08: rola editor dostawala 403 zamiast 200.
		if ( is_user_logged_in() && current_user_can( 'edit_posts' ) ) {
			return $wynik;
		}

		$sciezka = $zadanie->get_route();
		if ( preg_match( '#^/wp/v2/users(/|$)#', $sciezka ) ) {
			return new WP_Error(
				'agria_rest_users_forbidden',
				__( 'Lista uzytkownikow nie jest publicznie dostepna.', 'agria-auranet' ),
				[ 'status' => rest_authorization_required_code() ]
			);
		}

		return $wynik;
	}
	add_filter( 'rest_pre_dispatch', 'agria_block_anon_user_endpoints', 10, 3 );
}
