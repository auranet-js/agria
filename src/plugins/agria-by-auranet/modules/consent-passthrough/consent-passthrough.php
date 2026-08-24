<?php
/**
 * Modul: Consent Mode zaawansowany — url_passthrough i ads_data_redaction (T-086, 2026-08-24)
 *
 * PROBLEM: przez 30 dni kampania Google Ads nie zarejestrowala ani jednej konwersji
 * przy 215 klknieciach i 396 zl wydatku, a GA4 widzialo 26% ruchu organicznego
 * i 42% platnego wzgledem GSC i Ads. Przyczyna: Consent Mode dziala w trybie
 * PODSTAWOWYM — do klikniecia w baner Google nie dostaje nic, lacznie z gclid,
 * wiec klikniecia platne nie maja czego przypisac do konwersji.
 *
 * DLACZEGO NIE PRZEZ COMPLIANZ: wtyczka ma te dwa ustawienia w panelu
 * (cmplz-gtag-urlpassthrough, cmplz-gtag-ads_data_redaction) i sa ustawione na
 * "yes" od 24.08 — ale przy naszej konfiguracji sa martwe. Complianz wypisuje te
 * pola wylacznie z szablonow templates/statistics/gtag-*.js, a my mamy
 * compile_statistics = google-tag-manager, czyli szablon
 * google-tag-manager-consent-mode.js, w ktorym tych linii NIE MA (sprawdzone
 * w plikach wtyczki na serwerze 24.08). Ustawienia w panelu zostawiamy wlaczone,
 * zeby stan panelu zgadzal sie z zachowaniem strony, gdyby ktos kiedys przelaczyl
 * integracje z GTM na gtag.
 *
 * CO ROBI: dokłada dwa polecenia gtag przed zaladowaniem gtm.js.
 *  - ads_data_redaction: przy braku zgody na ad_storage Google nie zapisuje
 *    identyfikatorow, ale nadal odbiera sygnal bez ciasteczek. Gdy zgoda
 *    przychodzi, redakcja wylacza sie sama.
 *  - url_passthrough: gclid jedzie w adresie miedzy podstronami zamiast
 *    w ciasteczku, wiec atrybucja klikniecia przezywa brak zgody.
 * Zgody NIE sa zmieniane — wartosci domyslne nadal ustawia Complianz i nadal
 * wszystkie cztery sygnaly reklamowo-analityczne startuja jako denied.
 *
 * KOLEJNOSC: wp_head z priorytetem 20. Complianz drukuje swoj blok wczesniej,
 * a gtm.js laduje sie dopiero na zdarzeniu cmplz_cookie_warning_loaded, czyli
 * po naszym skrypcie. Atrybut data-category="functional" jest po to, zeby blokada
 * skryptow Complianza tego nie wyciela — to nie jest skrypt sledzacy.
 */

defined( 'ABSPATH' ) || exit;

if ( ! function_exists( 'agria_consent_passthrough' ) ) {
	/**
	 * Wypisuje ustawienia Consent Mode zaawansowanego przed zaladowaniem GTM.
	 */
	function agria_consent_passthrough(): void {
		if ( is_admin() ) {
			return;
		}
		// Bez Complianza nie ma czego uzupelniac.
		if ( ! defined( 'cmplz_version' ) && ! function_exists( 'cmplz_get_value' ) ) {
			return;
		}
		?>
<!-- Consent Mode zaawansowany — Agria by Auranet (T-086) -->
<script data-category="functional">
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('set', 'ads_data_redaction', true);
	gtag('set', 'url_passthrough', true);
</script>
		<?php
	}
	add_action( 'wp_head', 'agria_consent_passthrough', 20 );
}
