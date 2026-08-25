<?php
/**
 * Ekran /wycena/ — pelnoekranowy front za logowaniem.
 *
 * Nie wp-admin, bo handlowiec trzyma to otwarte przez caly dzien: panel laduje sie wolniej
 * i ma pasek boczny, ktory tu do niczego nie sluzy. Adres za logowaniem jest z definicji poza cache CDN.
 *
 * Kalkulacja idzie przez AJAX, nie w przegladarce. Specyfikacja przewidywala liczenie po stronie
 * klienta, ale to wymagaloby wyslania calego cennika do JavaScriptu — a ceny warstwy B maja pozostac
 * niejawne. Przy kilku wycenach dziennie roznica w odczuciu jest zadna, a cennik nie opuszcza serwera.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'init', function (): void {
	add_rewrite_rule( '^wycena/?$', 'index.php?agria_of_ekran=1', 'top' );
	add_rewrite_tag( '%agria_of_ekran%', '1' );
} );

add_action( 'template_redirect', function (): void {
	if ( ! get_query_var( 'agria_of_ekran' ) ) {
		return;
	}
	if ( ! is_user_logged_in() || ! current_user_can( AGRIA_OF_CAP ) ) {
		auth_redirect();
		exit;
	}
	agria_of_render_ekran();
	exit;
} );

/** Podpowiedzi miejscowosci. */
add_action( 'wp_ajax_agria_of_miejscowosci', function (): void {
	check_ajax_referer( 'agria_of' );
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_send_json_error( [], 403 );
	}
	wp_send_json_success( agria_of_szukaj_miejscowosci( sanitize_text_field( $_GET['q'] ?? '' ) ) );
} );

/** Formy dostepne dla produktu — lista zmienia sie po wyborze produktu. */
add_action( 'wp_ajax_agria_of_formy', function (): void {
	check_ajax_referer( 'agria_of' );
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_send_json_error( [], 403 );
	}
	$id = (int) ( $_GET['produkt'] ?? 0 );
	$out = [];
	foreach ( agria_of_formy_produktu( $id ) as $f ) {
		$out[] = [ 'klucz' => $f['klucz'], 'nazwa' => $f['nazwa'], 'rodzaj' => $f['rodzaj'], 'kg' => $f['kg'] ];
	}
	wp_send_json_success( $out );
} );

add_action( 'wp_ajax_agria_of_wycen', function (): void {
	check_ajax_referer( 'agria_of' );
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_send_json_error( [], 403 );
	}
	$w = agria_of_wycen( wp_unslash( $_POST ) );
	wp_send_json_success( agria_of_wycena_na_widok( $w ) );
} );

/** Przeklada wynik kalkulacji na to, co ma sie pojawic na ekranie — grosze na zlotowki, opisy. */
function agria_of_wycena_na_widok( array $w ): array {
	if ( ! empty( $w['blad'] ) && empty( $w['zaklad'] ) ) {
		return [ 'blad' => $w['blad'] ];
	}
	$zl = fn( $g ) => $g === null ? null : number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );

	return [
		'blad'      => $w['blad'],
		'tony'      => $w['tony'],
		'palet'     => $w['palet'],
		'zaklad'    => $w['zaklad']['nazwa'],
		'zaklad_id' => $w['zaklad']['term_id'],
		'zaklady'   => array_map( fn( $z ) => [
			'id'    => $z['term_id'],
			'nazwa' => $z['nazwa'],
			'km'    => $z['km'],
			'cena'  => $z['cena'] !== null ? $zl( $z['cena'] ) : null,
		], $w['zaklady'] ),
		'km'          => $w['km'],
		'km_pewne'    => $w['km_pewne'],
		'metoda'      => $w['metoda']['nazwa'] ?? null,
		'metoda_id'   => $w['metoda']['metoda'] ?? null,
		'metoda_opis' => $w['metoda']['opis'] ?? null,
		'metody'      => array_map( fn( $m ) => [
			'id' => $m['metoda'], 'nazwa' => $m['nazwa'], 'koszt' => $zl( $m['koszt'] ), 'opis' => $m['opis'],
		], $w['metody'] ),
		'cena_t'           => $zl( $w['cena_t'] ),
		'cena_proponowana' => $zl( $w['cena_proponowana'] ),
		'cena_min'         => $zl( $w['cena_min'] ),
		'ponizej_podlogi'  => $w['ponizej_podlogi'],
		'wartosc_towaru'   => $zl( $w['wartosc_towaru'] ),
		'transport'        => $zl( $w['transport'] ),
		'za_tone'          => $zl( $w['za_tone_z_dostawa'] ),
		'razem'            => $zl( $w['razem'] ),
		'dopelnienie'      => $w['dopelnienie'] ? [
			'brakuje' => $w['dopelnienie']['brakuje_t'],
			'pelne'   => $w['dopelnienie']['pelne_t'],
			'teraz'   => $zl( $w['dopelnienie']['teraz_za_tone'] ),
			'potem'   => $zl( $w['dopelnienie']['potem_za_tone'] ),
		] : null,
	];
}

function agria_of_render_ekran(): void {
	$produkty = agria_of_produkty();
	$nonce    = wp_create_nonce( 'agria_of' );
	$ajax     = admin_url( 'admin-ajax.php' );
	?><!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Wycena — AGRIA</title>
<style>
:root { --tlo:#fff; --tekst:#1b1b1b; --slabe:#666; --linia:#dcdcdc; --akcent:#354E33; --ostrz:#a33; --pas:#f7f7f5; }
@media (prefers-color-scheme: dark) { :root { --tlo:#151715; --tekst:#e8e8e6; --slabe:#9a9a95; --linia:#2f322f; --akcent:#8fbf87; --ostrz:#e08d8d; --pas:#1b1e1b; } }
* { box-sizing:border-box; }
body { margin:0; background:var(--tlo); color:var(--tekst); font:16px/1.5 -apple-system,Segoe UI,Roboto,sans-serif; }
header { border-bottom:1px solid var(--linia); padding:.9rem 1.4rem; display:flex; justify-content:space-between; align-items:baseline; }
header b { color:var(--akcent); }
header span { color:var(--slabe); font-size:.85rem; }
main { max-width:76rem; margin:0 auto; padding:1.6rem 1.4rem 5rem; display:grid; gap:2rem; grid-template-columns:minmax(20rem,26rem) 1fr; align-items:start; }
@media (max-width:56rem) { main { grid-template-columns:1fr; } }
label { display:block; font-size:.82rem; color:var(--slabe); margin:.9rem 0 .25rem; }
input, select { width:100%; padding:.55rem .65rem; font-size:1rem; border:1px solid var(--linia); border-radius:.3rem; background:var(--tlo); color:var(--tekst); }
input:focus, select:focus { outline:2px solid var(--akcent); outline-offset:-1px; }
.rzad { display:grid; grid-template-columns:1fr 9rem; gap:.6rem; }
.podpowiedzi { position:relative; }
.lista { position:absolute; z-index:9; left:0; right:0; background:var(--tlo); border:1px solid var(--linia); border-radius:0 0 .3rem .3rem; max-height:16rem; overflow:auto; }
.lista div { padding:.45rem .65rem; cursor:pointer; }
.lista div:hover, .lista div.akt { background:var(--pas); }
.lista small { color:var(--slabe); }
.wynik { border:1px solid var(--linia); border-radius:.5rem; padding:1.2rem 1.4rem; }
.pusto { color:var(--slabe); }
.linia { display:flex; justify-content:space-between; gap:1rem; padding:.5rem 0; border-bottom:1px dashed var(--linia); }
.linia:last-of-type { border-bottom:0; }
.linia b { font-variant-numeric:tabular-nums; }
.suma { border-top:2px solid var(--akcent); margin-top:.7rem; padding-top:.8rem; font-size:1.25rem; font-weight:700; }
.opis { color:var(--slabe); font-size:.84rem; }
.karta { background:var(--pas); border-left:3px solid var(--akcent); padding:.7rem .9rem; margin:1rem 0 0; border-radius:0 .3rem .3rem 0; font-size:.92rem; }
.ostrzezenie { border-left-color:var(--ostrz); color:var(--ostrz); }
.nadpisane { outline:2px solid var(--akcent); }
#zapisz { font:inherit; padding:.55rem 1rem; border:1px solid var(--akcent); border-radius:.3rem; background:var(--akcent); color:#fff; cursor:pointer; }
#zapisz[disabled] { opacity:.5; }
button.wroc { background:none; border:0; color:var(--akcent); cursor:pointer; font-size:.78rem; padding:0; text-decoration:underline; }
h2 { font-size:.95rem; color:var(--akcent); margin:0 0 .8rem; text-transform:uppercase; letter-spacing:.04em; }
</style>
</head>
<body>
<header>
	<b>AGRIA — wycena</b>
	<span><?php echo esc_html( wp_get_current_user()->display_name ); ?> · <a href="<?php echo esc_url( admin_url( 'admin.php?page=agria-of-cennik' ) ); ?>">cennik</a></span>
</header>
<main>
	<section>
		<h2>Zamówienie</h2>

		<label for="miejscowosc">Miejscowość klienta</label>
		<div class="podpowiedzi">
			<input id="miejscowosc" autocomplete="off" placeholder="zacznij pisać…">
			<div class="lista" id="lista" hidden></div>
		</div>

		<label for="produkt">Produkt</label>
		<select id="produkt">
			<option value="">— wybierz —</option>
			<?php foreach ( $produkty as $p ) : ?>
				<option value="<?php echo (int) $p->ID; ?>"><?php echo esc_html( agria_of_tytul_produktu( $p->ID ) ); ?></option>
			<?php endforeach; ?>
		</select>

		<label for="forma">Forma dostawy</label>
		<select id="forma"><option value="">— najpierw produkt —</option></select>

		<label>Ilość</label>
		<div class="rzad">
			<input id="ilosc" type="text" inputmode="decimal" placeholder="np. 24">
			<select id="jednostka">
				<option value="tona">ton</option>
				<option value="sztuka">sztuk</option>
			</select>
		</div>

		<label for="zaklad">Zakład wysyłkowy</label>
		<select id="zaklad"><option value="">— najbliższy z ceną —</option></select>

		<label for="metoda">Transport</label>
		<select id="metoda"><option value="">— najtańszy —</option></select>

		<h2 style="margin-top:2rem">Korekty — bo się negocjuje</h2>
		<div class="rzad">
			<div>
				<label for="cena_reczna">Cena zł/t</label>
				<input id="cena_reczna" type="text" inputmode="decimal" placeholder="z cennika">
			</div>
			<div>
				<label>&nbsp;</label>
				<button class="wroc" type="button" id="wroc_cena" hidden>↺ proponowana</button>
			</div>
		</div>
		<div class="rzad">
			<div>
				<label for="transport_reczny">Transport zł</label>
				<input id="transport_reczny" type="text" inputmode="decimal" placeholder="wyliczony">
			</div>
			<div>
				<label>&nbsp;</label>
				<button class="wroc" type="button" id="wroc_transport" hidden>↺ wyliczony</button>
			</div>
		</div>

		<div class="rzad">
			<div>
				<label for="stan">Stan transportu</label>
				<select id="stan">
					<option value="wyliczony">wyliczony</option>
					<option value="gratis">gratis (auto planujemy)</option>
					<option value="odbior">odbiór własny (auta nie ma)</option>
				</select>
			</div>
			<div>
				<label for="km">km ręcznie</label>
				<input id="km" type="text" inputmode="numeric" placeholder="auto">
			</div>
		</div>
	</section>

	<section>
		<h2 style="margin-top:2rem">Klient</h2>
		<label for="klient_nazwa">Nazwa lub nazwisko</label>
		<input id="klient_nazwa" placeholder="opcjonalnie">
		<div class="rzad">
			<div>
				<label for="klient_telefon">Telefon</label>
				<input id="klient_telefon" inputmode="tel" placeholder="rozpoznajemy po nim klienta">
			</div>
			<div>
				<label for="klient_nip">NIP</label>
				<input id="klient_nip" inputmode="numeric" placeholder="—">
			</div>
		</div>
		<label for="kanal">Skąd kontakt</label>
		<select id="kanal">
			<?php foreach ( agria_of_kanaly() as $k => $n ) : ?>
				<option value="<?php echo esc_attr( $k ); ?>"><?php echo esc_html( $n ); ?></option>
			<?php endforeach; ?>
		</select>
		<label for="uwagi">Uwagi</label>
		<input id="uwagi" placeholder="np. rozładunek HDS, termin">
	</section>

	<section class="wynik" id="wynik"><p class="pusto">Wpisz miejscowość, produkt i ilość — wycena pojawi się tutaj.</p></section>
</main>

<script>
const AJAX = <?php echo wp_json_encode( $ajax ); ?>, NONCE = <?php echo wp_json_encode( $nonce ); ?>;
const $ = id => document.getElementById(id);
let miejscowoscId = 0, timer = null;

async function api(action, params, metoda='GET') {
	const u = new URL(AJAX);
	if (metoda === 'GET') { u.search = new URLSearchParams({action, _wpnonce: NONCE, ...params}); return (await fetch(u, {credentials:'same-origin'})).json(); }
	return (await fetch(u, {method:'POST', credentials:'same-origin',
		body: new URLSearchParams({action, _wpnonce: NONCE, ...params})})).json();
}

// --- podpowiedzi miejscowosci ---
$('miejscowosc').addEventListener('input', e => {
	miejscowoscId = 0;
	clearTimeout(timer);
	timer = setTimeout(async () => {
		const q = e.target.value.trim();
		if (q.length < 2) { $('lista').hidden = true; return; }
		const r = await api('agria_of_miejscowosci', {q});
		const l = $('lista');
		l.innerHTML = '';
		(r.data || []).forEach(m => {
			const d = document.createElement('div');
			d.innerHTML = `${m.nazwa} <small>${m.powiat ? 'pow. ' + m.powiat + ', ' : ''}${m.wojewodztwo}</small>`;
			d.onclick = () => { miejscowoscId = +m.id; $('miejscowosc').value = m.nazwa; l.hidden = true; policz(); };
			l.appendChild(d);
		});
		l.hidden = !r.data || !r.data.length;
	}, 180);
});
document.addEventListener('click', e => { if (!e.target.closest('.podpowiedzi')) $('lista').hidden = true; });

// --- formy zalezne od produktu ---
$('produkt').addEventListener('change', async () => {
	const r = await api('agria_of_formy', {produkt: $('produkt').value});
	const s = $('forma');
	s.innerHTML = '<option value="">— wybierz —</option>';
	(r.data || []).forEach(f => s.add(new Option(f.nazwa, f.klucz)));
	if ((r.data || []).length === 1) s.selectedIndex = 1;
	$('zaklad').innerHTML = '<option value="">— najbliższy z ceną —</option>';
	policz();
});

['forma','ilosc','jednostka','zaklad','metoda','stan','km','cena_reczna','transport_reczny'].forEach(id =>
	$(id).addEventListener(['ilosc','km','cena_reczna','transport_reczny'].includes(id) ? 'input' : 'change', () => policz()));

// Powrot do wartosci proponowanej — do tej z chwili wyceny, nie do dzisiejszego cennika.
$('wroc_cena').onclick = () => { $('cena_reczna').value = ''; $('cena_reczna').classList.remove('nadpisane'); policz(); };
$('wroc_transport').onclick = () => { $('transport_reczny').value = ''; $('transport_reczny').classList.remove('nadpisane'); policz(); };

function zl(x) { return x === null || x === undefined ? '—' : x + ' zł'; }

async function policz() {
	if (!miejscowoscId || !$('produkt').value || !$('forma').value || !parseFloat(($('ilosc').value||'').replace(',','.'))) return;
	const r = await api('agria_of_wycen', dane(), 'POST');
	rysuj(r.data || {});
}

function dane() {
	return {
		produkt_id: $('produkt').value, miejscowosc_id: miejscowoscId, forma_klucz: $('forma').value,
		ilosc: ($('ilosc').value||'').replace(',','.'), jednostka: $('jednostka').value,
		zaklad_term_id: $('zaklad').value, metoda: $('metoda').value,
		stan_transportu: $('stan').value, km: $('km').value,
		cena_reczna: $('cena_reczna').value, transport_reczny: $('transport_reczny').value
	};
}

async function zapisz() {
	const b = $('zapisz');
	b.disabled = true;
	const r = await api('agria_of_zapisz', {...dane(),
		klient_nazwa: $('klient_nazwa').value, klient_telefon: $('klient_telefon').value,
		klient_nip: $('klient_nip').value, kanal: $('kanal').value, uwagi: $('uwagi').value
	}, 'POST');
	b.disabled = false;
	if (r.success) {
		$('zapisano').innerHTML = `zapisana jako nr ${r.data.id} — <a href="${r.data.wydruk}" target="_blank">wydruk</a>`;
	} else {
		$('zapisano').textContent = (r.data && r.data.blad) || 'nie udało się zapisać';
	}
}

function rysuj(w) {
	const el = $('wynik');
	if (w.blad && !w.razem) { el.innerHTML = `<p class="karta ostrzezenie">${w.blad}</p>`; return; }

	// listy wyboru uzupelniamy tym, co wyliczyl serwer — bez nadpisywania recznego wyboru
	if (w.zaklady && !$('zaklad').value) {
		$('zaklad').innerHTML = '<option value="">— najbliższy z ceną —</option>';
		w.zaklady.forEach(z => $('zaklad').add(new Option(`${z.nazwa} — ${z.km} km${z.cena ? '' : ' (brak ceny)'}`, z.id)));
	}
	if (w.metody && !$('metoda').value) {
		$('metoda').innerHTML = '<option value="">— najtańszy —</option>';
		w.metody.forEach(m => $('metoda').add(new Option(`${m.nazwa} — ${m.koszt} zł`, m.id)));
	}

	['cena_reczna','transport_reczny'].forEach(id => {
		const puste = !$(id).value.trim();
		$(id).classList.toggle('nadpisane', !puste);
		$(id === 'cena_reczna' ? 'wroc_cena' : 'wroc_transport').hidden = puste;
	});

	let h = '<h2>Wycena</h2>';
	if (w.blad) h += `<p class="karta ostrzezenie">${w.blad}</p>`;
	h += `<div class="linia"><span>Zakład<br><span class="opis">${w.km} km${w.km_pewne ? '' : ' — szacunek, trasa niepoliczona'}</span></span><b>${w.zaklad}</b></div>`;
	const korekta = w.cena_proponowana && w.cena_t && w.cena_proponowana !== w.cena_t
		? ` <span class="opis">(z cennika ${w.cena_proponowana} zł/t)</span>` : '';
	h += `<div class="linia"><span>Towar<br><span class="opis">${w.cena_t ? w.cena_t + ' zł/t × ' + w.tony + ' t' : 'brak ceny'}</span>${korekta}</span><b>${zl(w.wartosc_towaru)}</b></div>`;
	h += `<div class="linia"><span>Transport<br><span class="opis">${w.metoda ? w.metoda + ' · ' + w.metoda_opis : '—'}</span></span><b>${zl(w.transport)}</b></div>`;
	h += `<div class="linia"><span>Cena z dostawą</span><b>${zl(w.za_tone)}/t</b></div>`;
	h += `<div class="linia suma"><span>Razem netto</span><b>${zl(w.razem)}</b></div>`;

	if (w.ponizej_podlogi) h += `<p class="karta ostrzezenie">Cena poniżej minimalnej (${w.cena_min} zł/t). Możesz tak podać — tylko wiedz, że schodzisz poniżej poziomu stałych odbiorców.</p>`;
	if (w.dopelnienie) h += `<p class="karta">Do pełnego auta brakuje <b>${w.dopelnienie.brakuje} t</b>. Przy ${w.dopelnienie.pelne} t przewóz spada z <b>${w.dopelnienie.teraz}</b> na <b>${w.dopelnienie.potem} zł/t</b>.</p>`;
	if (w.palet) h += `<p class="opis" style="margin-top:1rem">Zamówienie zajmuje ${w.palet} ${w.palet === 1 ? 'paletę' : 'palet'}.</p>`;
	h += `<p style="margin-top:1.6rem"><button id="zapisz" type="button">Zapisz ofertę</button> <span id="zapisano" class="opis"></span></p>`;
	el.innerHTML = h;
	$('zapisz').onclick = zapisz;
}
</script>
</body>
</html>
	<?php
}
