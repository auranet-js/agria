<?php
/**
 * Ekran /wycena/ — arkusz wyceny, pelnoekranowy, za logowaniem.
 *
 * KIERUNEK: kwit wagowy, nie panel aplikacji. Handlowiec ma to otwarte caly dzien i czyta stad
 * liczby na glos, w trakcie rozmowy. Dlatego liczby sa monospace i wyrownane w kolumnach
 * (w kolumnie musza sie zgadzac co do znaku), etykiety sa ciche, a jedyny element graficzny
 * to pasek wypelnienia auta — stoi tam, gdzie leza pieniadze, bo dopelnienie auta jest jedyna
 * rzecza, ktora sama z siebie podnosi wartosc zamowienia.
 *
 * ZASADA IMPLEMENTACYJNA: JavaScript aktualizuje wylacznie komorki WYNIKOWE. Nigdy nie dotyka
 * pola, w ktorym uzytkownik wlasnie pisze — inaczej przy kazdym przeliczeniu gubi sie kursor
 * i nie da sie poprawic „12" na „13".
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
	if ( ! agria_of_wpuszczamy() ) {
		exit;
	}
	// Goly adres = pulpit z lista ofert. Arkusz otwiera sie swiadomie: „Nowa oferta" albo „edytuj".
	if ( ! isset( $_GET['nowa'] ) && empty( $_GET['edytuj'] ) ) {
		agria_of_render_pulpit();
		exit;
	}
	agria_of_render_ekran( isset( $_GET['edytuj'] ) ? (int) $_GET['edytuj'] : 0 );
	exit;
} );

add_action( 'wp_ajax_agria_of_miejscowosci', function (): void {
	check_ajax_referer( 'agria_of' );
	if ( ! current_user_can( AGRIA_OF_CAP ) ) {
		wp_send_json_error( [], 403 );
	}
	wp_send_json_success( agria_of_szukaj_miejscowosci( sanitize_text_field( $_GET['q'] ?? '' ) ) );
} );

add_action( 'wp_ajax_agria_of_wycen', function (): void {
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
	wp_send_json_success( agria_of_koszyk_na_widok( $w ) );
} );

/** Grosze na tekst komorki. Bez znaku waluty — jednostka stoi w naglowku kolumny. */
function agria_of_zl( $g, bool $puste_gdy_null = true ): string {
	if ( $g === null || $g === '' ) {
		return $puste_gdy_null ? '' : '0,00';
	}
	return number_format( (float) agria_of_na_zlote( (int) $g ), 2, ',', ' ' );
}

function agria_of_koszyk_na_widok( array $w ): array {
	$pozycje = [];
	foreach ( $w['pozycje'] as $k => $p ) {
		$pozycje[ $k ] = [
			'tony'             => $p['tony'],
			'palet'            => $p['palet'],
			'zaklad_id'        => $p['zaklad']['term_id'],
			'zaklady'          => array_map( fn( $z ) => [
				'id'   => $z['term_id'],
				'nazwa'=> $z['nazwa'],
				'km'   => $z['km'],
				'brak' => $z['cena'] === null,
			], $p['zaklady'] ),
			'cena'             => agria_of_zl( $p['cena'] ),
			'cena_proponowana' => agria_of_zl( $p['cena_proponowana'] ),
			'zmieniona'        => $p['cena'] !== null && $p['cena_proponowana'] !== null && $p['cena'] !== $p['cena_proponowana'],
			'ponizej_podlogi'  => $p['ponizej_podlogi'],
			'cena_min'         => agria_of_zl( $p['cena_min'] ),
			'wartosc'          => agria_of_zl( $p['wartosc'] ),
			'brak_ceny'        => $p['brak_ceny'],
		];
	}

	$grupy = array_map( fn( $g ) => [
		'zaklad_id'   => $g['zaklad_term_id'],
		'zaklad'      => $g['zaklad'],
		'km'          => $g['km'],
		'km_pewne'    => $g['km_pewne'],
		'tony'        => $g['tony'],
		'wypelnienie' => $g['wypelnienie'] ?? null,
		'mieszana'    => $g['mieszana'],
		'metoda_id'   => $g['metoda']['metoda'] ?? '',
		'kursy'       => $g['metoda']['kursy'] ?? 1,
		'metody'      => array_map( fn( $m ) => [
			'id' => $m['metoda'], 'nazwa' => $m['nazwa'], 'koszt' => agria_of_zl( $m['koszt'] ),
		], $g['metody'] ),
		'koszt'       => agria_of_zl( $g['koszt'], false ),
		'za_tone'     => agria_of_zl( $g['za_tone'] ),
		'dopelnienie' => $g['dopelnienie'] ? [
			'brakuje' => $g['dopelnienie']['brakuje'],
			'pelne'   => $g['dopelnienie']['pelne'],
			'teraz'   => agria_of_zl( $g['dopelnienie']['teraz'] ),
			'potem'   => agria_of_zl( $g['dopelnienie']['potem'] ),
		] : null,
	], $w['grupy'] );

	return [
		'pozycje'   => $pozycje,
		'grupy'     => $grupy,
		'towar'     => agria_of_zl( $w['towar'], false ),
		'transport' => agria_of_zl( $w['transport'], false ),
		'razem'     => agria_of_zl( $w['razem'], false ),
		'za_tone'   => agria_of_zl( $w['za_tone'], false ),
		'tony'      => $w['tony'],
		'bez_ceny'  => $w['bez_ceny'],
	];
}


/** Tokeny i pasek gorny — wspolne dla arkusza, pulpitu i kazdego kolejnego ekranu. */
function agria_of_style_wspolny(): void {
	?>
:root{
	--tlo:#F2F2EE; --karta:#FFFFFF; --tekst:#161A16; --cichy:#6B7268; --slaby:#99A095;
	--kreska:#DEDFD7; --kreska-mocna:#C4C7BB; --zielen:#354E33; --zielen-jasna:#EAEFE7;
	--ochra:#A56A1F; --ochra-tlo:#FBF3E4; --alarm:#A3382F; --alarm-tlo:#FAEDEC;
	--przycisk-tekst:#FFFFFF;
}
@media (prefers-color-scheme:dark){:root{
	--tlo:#111411; --karta:#181C18; --tekst:#E7E9E4; --cichy:#9BA296; --slaby:#6E756A;
	--kreska:#272B26; --kreska-mocna:#3A4038; --zielen:#93C08A; --zielen-jasna:#1B221A;
	--ochra:#D9A45C; --ochra-tlo:#241D12; --alarm:#E08D84; --alarm-tlo:#251715;
	--przycisk-tekst:#0F120F;
}}
*{box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{margin:0;background:var(--tlo);color:var(--tekst);
	font:14px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;}
.num,.kwota{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-variant-numeric:tabular-nums;}

.gora{position:sticky;top:0;z-index:20;background:var(--karta);border-bottom:1px solid var(--kreska-mocna);
	display:flex;align-items:center;gap:1.5rem;padding:.6rem 1.2rem;}
.marka{font-weight:650;letter-spacing:.02em;color:var(--zielen);}
.marka span{color:var(--slaby);font-weight:400;}
.gora .kto{margin-left:auto;color:var(--cichy);font-size:.82rem;}
.gora a{color:var(--zielen);}

	<?php
}

function agria_of_render_ekran( int $edytuj = 0 ): void {
	$produkty = agria_of_produkty();
	$nonce    = wp_create_nonce( 'agria_of' );
	$oferta   = $edytuj ? agria_of_oferta_do_arkusza( $edytuj ) : null;
	?><!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Arkusz wyceny — AGRIA</title>
<style>
<?php agria_of_style_wspolny(); ?>
.pas{background:var(--karta);border-bottom:1px solid var(--kreska);}
.pas-tytul{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--slaby);
	padding:.7rem 1.2rem .35rem;font-weight:600;}
.pas-tytul .dopisek{text-transform:none;letter-spacing:0;font-weight:400;}
.wnetrze{padding:0 1.2rem 1rem;}

.rzad{display:grid;gap:.5rem;align-items:end;
	grid-template-columns:minmax(11rem,1.6fr) 8.5rem 8rem auto minmax(9rem,1fr) minmax(10rem,1.4fr);}
.rzad-dostawa{grid-template-columns:minmax(14rem,22rem) 12rem;}
@media(max-width:70rem){.rzad,.rzad-dostawa{grid-template-columns:1fr 1fr;}}
.pole label{display:block;font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;
	color:var(--slaby);margin-bottom:.2rem;}
input,select{width:100%;padding:.4rem .5rem;font:inherit;color:var(--tekst);
	background:var(--tlo);border:1px solid var(--kreska-mocna);border-radius:2px;}
input:focus,select:focus{outline:2px solid var(--zielen);outline-offset:-1px;background:var(--karta);}
button{font:inherit;cursor:pointer;}
.btn{padding:.42rem .7rem;border:1px solid var(--kreska-mocna);border-radius:2px;
	background:var(--tlo);color:var(--tekst);}
.btn:hover{border-color:var(--zielen);}
.platnik{margin-top:.6rem;font-size:.82rem;color:var(--cichy);min-height:1.2rem;}
.platnik b{color:var(--tekst);font-weight:600;}
.platnik .zle{color:var(--alarm);}

.szukaj{position:relative;}
.podpowiedzi{position:absolute;z-index:30;left:0;right:0;top:100%;background:var(--karta);
	border:1px solid var(--kreska-mocna);max-height:15rem;overflow:auto;}
.podpowiedzi div{padding:.35rem .5rem;cursor:pointer;font-size:.85rem;}
.podpowiedzi div:hover{background:var(--zielen-jasna);}
.podpowiedzi small{color:var(--slaby);}

table{width:100%;border-collapse:collapse;table-layout:fixed;}
td:nth-child(2){white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
thead th{font-size:.66rem;letter-spacing:.09em;text-transform:uppercase;color:var(--slaby);
	font-weight:600;text-align:left;padding:.4rem .5rem;border-bottom:1px solid var(--kreska-mocna);
	position:sticky;top:2.8rem;background:var(--karta);z-index:10;}
tbody td{padding:.2rem .5rem;border-bottom:1px solid var(--kreska);vertical-align:middle;}
tbody tr:not(.wybrany) td input:not(:focus),
tbody tr:not(.wybrany) td select:not(:focus){border-color:transparent;background:transparent;color:var(--cichy);}
tbody tr:not(.wybrany):hover td input:not(:focus),
tbody tr:not(.wybrany):hover td select:not(:focus){border-color:var(--kreska);}
tbody tr.wybrany{background:var(--zielen-jasna);}
tbody tr.wybrany td:first-child{box-shadow:inset 3px 0 0 var(--zielen);}
.p{text-align:right;}
.produkt-nazwa{font-weight:500;}
.produkt-sku{color:var(--slaby);font-size:.74rem;margin-left:.4rem;}
td input,td select{padding:.28rem .4rem;}
td input.num{text-align:right;}
.ptak{width:auto;}
.komorka-cena{display:flex;align-items:center;gap:.35rem;justify-content:flex-end;}
.komorka-cena input{width:5.6rem;}
.sugestia{min-width:4.4rem;text-align:right;font-size:.76rem;color:var(--slaby);
	background:none;border:0;padding:.12rem .2rem;border-radius:2px;
	font-family:ui-monospace,monospace;font-variant-numeric:tabular-nums;cursor:default;}
.sugestia[data-czynna=tak]{color:var(--ochra);background:var(--ochra-tlo);cursor:pointer;}
.sugestia[data-czynna=tak]:hover{outline:1px solid var(--ochra);}
input.zmieniona{border-color:var(--ochra);background:var(--ochra-tlo);}
input.podloga{border-color:var(--alarm);background:var(--alarm-tlo);}
.wartosc{font-weight:600;}
.brak{color:var(--alarm);font-size:.78rem;font-weight:400;}

.auto{display:grid;gap:.5rem 1rem;align-items:end;padding:.6rem 1.2rem;
	grid-template-columns:minmax(7rem,1fr) 5.5rem minmax(9rem,12rem) 6.5rem 11rem 8rem;
	border-bottom:1px solid var(--kreska);}
@media(max-width:70rem){.auto{grid-template-columns:1fr 1fr;}}
.auto .etyk{font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--slaby);display:block;margin-bottom:.2rem;}
/* Naglowki kolumn maja stac raz. Ukrywamy je przy kolejnych autach, ale przez `visibility`,
   zeby wiersze nie zmienily wysokosci; na waskim ekranie wracaja, bo tam kolumny sie zawijaja. */
@media(min-width:70rem){.auto + .auto .etyk{visibility:hidden;}}
.auto .zaklad-nazwa{font-weight:600;}
/* SYGNATURA: pasek wypelnienia auta. Jedyna grafika na ekranie — bo dopelnienie jest
   jedyna rzecza, ktora sama z siebie podnosi wartosc zamowienia. */
.wypelnienie{height:1.35rem;max-width:11rem;background:var(--tlo);border:1px solid var(--kreska-mocna);
	position:relative;overflow:hidden;}
.wypelnienie i{position:absolute;inset:0 auto 0 0;background:var(--zielen);opacity:.22;}
.wypelnienie.pelne i{opacity:.45;}
.wypelnienie b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
	font:600 .72rem/1 ui-monospace,monospace;letter-spacing:.03em;}
.namowa{grid-column:1/-1;font-size:.8rem;color:var(--ochra);background:var(--ochra-tlo);
	padding:.35rem .55rem;border-left:2px solid var(--ochra);}
.namowa b{font-weight:650;}
.mieszana{grid-column:1/-1;font-size:.78rem;color:var(--cichy);}

.dol{position:sticky;bottom:0;z-index:20;background:var(--karta);border-top:2px solid var(--zielen);
	display:flex;align-items:center;gap:1.6rem;padding:.7rem 1.2rem;flex-wrap:wrap;}
.dol .poz{font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;color:var(--slaby);}
.dol .poz b{display:block;font-size:1rem;color:var(--tekst);font-weight:600;letter-spacing:0;
	text-transform:none;font-family:ui-monospace,monospace;font-variant-numeric:tabular-nums;}
.dol .suma{margin-left:auto;text-align:right;}
.dol .suma .etyk{display:block;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--slaby);}
.dol .suma b{font-size:1.5rem;font-weight:650;font-family:ui-monospace,monospace;
	font-variant-numeric:tabular-nums;letter-spacing:-.01em;}
.btn-glowny{padding:.55rem 1.1rem;background:var(--zielen);color:var(--przycisk-tekst);
	border:1px solid var(--zielen);border-radius:2px;font-weight:600;}
.btn-glowny:disabled{opacity:.4;cursor:default;}
.komunikat{font-size:.82rem;color:var(--cichy);}
.komunikat.zle{color:var(--alarm);}
.pas-edycji{background:var(--ochra-tlo);border-bottom:1px solid var(--ochra);
	padding:.6rem 1.2rem;font-size:.86rem;color:var(--tekst);}
.pas-edycji b{font-weight:650;}
.komunikat a{color:var(--zielen);}
@media (prefers-reduced-motion:no-preference){.wypelnienie i{transition:width .18s ease-out;}}
</style>
</head>
<body>

<div class="gora">
	<span class="marka">AGRIA <span>· <?php echo $oferta ? 'oferta nr ' . (int) $oferta['id'] : 'nowa wycena'; ?></span></span>
	<span class="kto"><?php echo esc_html( wp_get_current_user()->display_name ); ?>
		· <a href="<?php echo esc_url( home_url( '/wycena/' ) ); ?>">← wszystkie oferty</a>
		· <a href="<?php echo esc_url( admin_url( 'admin.php?page=agria-of-cennik' ) ); ?>">cennik</a></span>
</div>

<?php if ( $oferta ) :
	$wystawil = agria_of_wystawil( (int) $oferta['id'] );
	$slad     = agria_of_slad_edycji( (int) $oferta['id'] ); ?>
	<div class="pas-edycji">
		Edytujesz ofertę nr <b><?php echo (int) $oferta['id']; ?></b>, którą wystawił <b><?php echo esc_html( $wystawil ); ?></b>.
		<?php if ( $slad ) : ?>Ostatnio zmieniał ją <b><?php echo esc_html( $slad['kto'] ); ?></b>
			(<?php echo esc_html( mysql2date( 'j.m.Y, H:i', $slad['kiedy'] ) ); ?>).<?php endif; ?>
		Zapisanie nadpisze tę ofertę i odnotuje, że zaktualizował ją <b><?php echo esc_html( wp_get_current_user()->display_name ); ?></b>.
	</div>
<?php endif; ?>

<section class="pas">
	<div class="pas-tytul">Klient</div>
	<div class="wnetrze">
		<div class="rzad">
			<div class="pole"><label for="k_nazwa">Nazwa lub nazwisko</label><input id="k_nazwa" autocomplete="off"></div>
			<div class="pole"><label for="k_tel">Telefon</label><input id="k_tel" inputmode="tel" autocomplete="off"></div>
			<div class="pole"><label for="k_nip">NIP</label><input id="k_nip" class="num" inputmode="numeric" autocomplete="off"></div>
			<div class="pole"><label>&nbsp;</label><button class="btn" id="k_gus" type="button">Dane z GUS</button></div>
			<div class="pole"><label for="k_kanal">Skąd kontakt</label><select id="k_kanal">
				<?php foreach ( agria_of_kanaly() as $k => $n ) : ?>
					<option value="<?php echo esc_attr( $k ); ?>"><?php echo esc_html( $n ); ?></option>
				<?php endforeach; ?></select></div>
			<div class="pole"><label for="k_uwagi">Uwagi</label><input id="k_uwagi" placeholder="np. rozładunek HDS"></div>
		</div>
		<div class="platnik" id="platnik"></div>
	</div>
</section>

<section class="pas">
	<div class="pas-tytul">Dostawa</div>
	<div class="wnetrze">
		<div class="rzad rzad-dostawa">
			<div class="pole szukaj">
				<label for="miejscowosc">Miejscowość</label>
				<input id="miejscowosc" autocomplete="off" placeholder="zacznij pisać…">
				<div class="podpowiedzi" id="podpowiedzi" hidden></div>
			</div>
			<div class="pole"><label for="stan">Transport</label><select id="stan">
				<option value="wyliczony">wyliczony</option>
				<option value="gratis">gratis — auto planujemy</option>
				<option value="odbior">odbiór własny</option>
			</select></div>
		</div>
	</div>
</section>

<section class="pas">
	<div class="pas-tytul">Pozycje <span class="dopisek">— wpisz ilość przy tym, o co pyta klient</span></div>
	<table>
		<thead><tr>
			<th style="width:2.4rem"></th>
			<th style="width:auto">Produkt</th>
			<th style="width:8.5rem">Forma</th>
			<th style="width:6.5rem" class="p">Ilość</th>
			<th style="width:4.5rem">Jedn.</th>
			<th style="width:11rem" class="p">Cena zł/t</th>
			<th style="width:12rem">Zakład</th>
			<th style="width:7.5rem" class="p">Wartość</th>
		</tr></thead>
		<tbody id="arkusz">
		<?php foreach ( $produkty as $p ) :
			$formy = agria_of_formy_produktu( $p->ID );
			if ( ! $formy ) { continue; }
			// Luz idzie pierwszy, bo tak wyglada wiekszosc sprzedazy. Alfabet ustawialby
			// „Big-bag" na czele i handlowiec musialby poprawiac przy kazdej pozycji.
			uasort( $formy, fn( $a, $b ) => ( $b['rodzaj'] === 'luz' ) <=> ( $a['rodzaj'] === 'luz' ) );
			$sku = get_post_meta( $p->ID, '_sku', true );
			?>
			<tr data-klucz="<?php echo (int) $p->ID; ?>">
				<td><input type="checkbox" class="ptak"></td>
				<td><span class="produkt-nazwa"><?php echo esc_html( agria_of_tytul_produktu( $p->ID ) ); ?></span><?php
					if ( $sku ) : ?><span class="produkt-sku"><?php echo esc_html( $sku ); ?></span><?php endif; ?></td>
				<td><select class="forma"><?php foreach ( $formy as $f ) : ?>
					<option value="<?php echo esc_attr( $f['klucz'] ); ?>"><?php echo esc_html( $f['nazwa'] ); ?></option>
				<?php endforeach; ?></select></td>
				<td><input class="ilosc num" inputmode="decimal" placeholder=""></td>
				<td><select class="jednostka"><option value="tona">t</option><option value="sztuka">szt.</option></select></td>
				<td><div class="komorka-cena">
					<input class="cena num" inputmode="decimal" placeholder="—">
					<button type="button" class="sugestia" data-czynna="nie" tabindex="-1"></button>
				</div></td>
				<td><select class="zaklad"><option value="">—</option></select></td>
				<td class="p wartosc kwota"></td>
			</tr>
		<?php endforeach; ?>
		</tbody>
	</table>
</section>

<section class="pas" id="pas-transport" hidden>
	<div class="pas-tytul">Transport <span class="dopisek">— auto jedzie z jednego zakładu, więc każdy zakład to osobny kurs</span></div>
	<div id="auta"></div>
</section>

<div class="dol">
	<div class="poz">Towar<b id="s_towar">0,00</b></div>
	<div class="poz">Transport<b id="s_transport">0,00</b></div>
	<div class="poz">Tonaż<b id="s_tony">0 t</b></div>
	<div class="poz">Za tonę z dostawą<b id="s_zatone">0,00</b></div>
	<div class="suma"><span class="etyk">Razem netto</span><b id="s_razem">0,00 zł</b></div>
	<button class="btn-glowny" id="zapisz" disabled><?php echo $oferta ? "Zapisz zmiany" : "Zapisz ofertę"; ?></button>
	<span class="komunikat" id="komunikat"></span>
</div>

<script>
const AJAX=<?php echo wp_json_encode( admin_url( 'admin-ajax.php' ) ); ?>, NONCE=<?php echo wp_json_encode( $nonce ); ?>;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
let miejscowoscId=0, platnik=null, licznik=0, timerPodp=null, timer=null;
const OFERTA=<?php echo wp_json_encode( $oferta ); ?>;

async function api(action,params,metoda='GET'){
	const u=new URL(AJAX);
	if(metoda==='GET'){u.search=new URLSearchParams({action,_wpnonce:NONCE,...params});
		return (await fetch(u,{credentials:'same-origin'})).json();}
	const b=new URLSearchParams();b.append('action',action);b.append('_wpnonce',NONCE);
	for(const [k,v] of Object.entries(params)) b.append(k,v);
	return (await fetch(u,{method:'POST',credentials:'same-origin',body:b})).json();
}

/* ---------- miejscowosc ---------- */
$('#miejscowosc').addEventListener('input',e=>{
	miejscowoscId=0; clearTimeout(timerPodp);
	timerPodp=setTimeout(async()=>{
		const q=e.target.value.trim(), l=$('#podpowiedzi');
		if(q.length<2){l.hidden=true;return;}
		const r=await api('agria_of_miejscowosci',{q});
		l.innerHTML='';
		(r.data||[]).forEach(m=>{
			const d=document.createElement('div');
			d.innerHTML=`${m.nazwa} <small>${m.powiat?'pow. '+m.powiat+', ':''}${m.wojewodztwo}</small>`;
			d.onclick=()=>{miejscowoscId=+m.id;$('#miejscowosc').value=m.nazwa;l.hidden=true;policz();};
			l.appendChild(d);
		});
		l.hidden=!(r.data||[]).length;
	},170);
});
document.addEventListener('click',e=>{if(!e.target.closest('.szukaj'))$('#podpowiedzi').hidden=true;});

/* ---------- platnik z GUS ---------- */
$('#k_gus').onclick=async()=>{
	const nip=$('#k_nip').value.replace(/\D+/g,''), p=$('#platnik');
	if(nip.length!==10){p.innerHTML='<span class="zle">NIP ma dziesięć cyfr.</span>';return;}
	p.textContent='Szukam w rejestrze REGON…';
	const r=await api('agria_of_gus',{nip});
	if(!r.success){p.innerHTML=`<span class="zle">${(r.data&&r.data.blad)||'Nie udało się pobrać.'}</span>`;return;}
	platnik=r.data;
	p.innerHTML=`Płatnik: <b>${platnik.nazwa}</b> · ${platnik.adres}${platnik.regon?' · REGON '+platnik.regon:''}`;
	if(!$('#k_nazwa').value.trim()) $('#k_nazwa').value=platnik.nazwa;
};

/* ---------- arkusz ---------- */
const wiersze=()=>$$('#arkusz tr');

function zbierzPozycje(){
	const poz={};
	wiersze().forEach(tr=>{
		const il=tr.querySelector('.ilosc').value.trim();
		if(!il||!(parseFloat(il.replace(',','.'))>0)) return;
		const k=tr.dataset.klucz;
		poz[`pozycje[${k}][produkt_id]`]=k;
		poz[`pozycje[${k}][forma_klucz]`]=tr.querySelector('.forma').value;
		poz[`pozycje[${k}][ilosc]`]=il;
		poz[`pozycje[${k}][jednostka]`]=tr.querySelector('.jednostka').value;
		poz[`pozycje[${k}][zaklad_term_id]`]=tr.querySelector('.zaklad').value;
		poz[`pozycje[${k}][cena_reczna]`]=tr.querySelector('.cena').value.trim();
	});
	return poz;
}

function zbierzTransport(){
	const o={};
	$$('#auta [data-zaklad]').forEach(el=>{
		const z=el.dataset.zaklad;
		const km=el.querySelector('.km'), me=el.querySelector('.metoda'), kw=el.querySelector('.kwota-transport');
		if(km&&km.value.trim()) o[`km[${z}]`]=km.value.trim();
		if(me&&me.value) o[`metoda[${z}]`]=me.value;
		if(kw&&kw.value.trim()) o[`transport[${z}]`]=kw.value.trim();
	});
	return o;
}

async function policz(){
	const poz=zbierzPozycje(), pusto=!Object.keys(poz).length;
	if(pusto||!miejscowoscId){wyczysc(pusto?'':'Wskaż miejscowość dostawy.');return;}
	const moj=++licznik;
	const r=await api('agria_of_wycen',{miejscowosc_id:miejscowoscId,
		stan_transportu:$('#stan').value,...poz,...zbierzTransport()},'POST');
	if(moj!==licznik) return;                 // starsza odpowiedz nie nadpisuje nowszej
	if(r.success) rysuj(r.data);
}
const przelicz=()=>{clearTimeout(timer);timer=setTimeout(policz,140);};

function wyczysc(msg){
	wiersze().forEach(tr=>{
		tr.querySelector('.wartosc').textContent='';
		const s=tr.querySelector('.sugestia'); s.textContent=''; s.dataset.czynna='nie';
		const c=tr.querySelector('.cena');
		c.classList.remove('zmieniona','podloga');
		if(!c.dataset.tkniete) c.value='';
	});
	$('#auta').innerHTML=''; $('#pas-transport').hidden=true;
	$('#s_towar').textContent='0,00'; $('#s_transport').textContent='0,00';
	$('#s_zatone').textContent='0,00'; $('#s_tony').textContent='0 t'; $('#s_razem').textContent='0,00 zł';
	$('#zapisz').disabled=true;
	$('#komunikat').className='komunikat'; $('#komunikat').textContent=msg||'';
}

/* Aktualizujemy WYLACZNIE komorki wynikowe — nigdy pola, w ktorym ktos pisze. */
function rysuj(w){
	wiersze().forEach(tr=>{
		const p=w.pozycje[tr.dataset.klucz];
		const cena=tr.querySelector('.cena'), sug=tr.querySelector('.sugestia'), zak=tr.querySelector('.zaklad');
		if(!p){
			tr.querySelector('.wartosc').textContent='';
			sug.textContent=''; sug.dataset.czynna='nie';
			cena.classList.remove('zmieniona','podloga');
			if(!cena.dataset.tkniete) cena.value='';
			return;
		}
		tr.querySelector('.wartosc').innerHTML=p.brak_ceny?'<span class="brak">brak ceny</span>':p.wartosc;

		// Pole ceny pokazuje kwote, ktora FAKTYCZNIE poszla do rachunku — dopoki handlowiec
		// sam w nie nie wpisze. Puste pole przy pozycji, ktora ma cene, kazaloby mu zgadywac.
		if(!cena.dataset.tkniete) cena.value=p.cena||'';
		if(p.cena_proponowana){
			sug.textContent=p.cena_proponowana;
			sug.dataset.czynna=p.zmieniona?'tak':'nie';
			sug.title=p.zmieniona?'Wróć do ceny z cennika':'Cena z cennika';
		}else{sug.textContent='—';sug.dataset.czynna='nie';}
		cena.classList.toggle('zmieniona',!!p.zmieniona);
		cena.classList.toggle('podloga',!!p.ponizej_podlogi);
		cena.title=p.ponizej_podlogi?('Poniżej ceny minimalnej '+p.cena_min+' zł/t'):'';

		const podpis=p.zaklady.map(z=>z.id+':'+z.km).join('|');
		if(zak.dataset.podpis!==podpis){
			const byl=zak.value;
			zak.innerHTML='';
			p.zaklady.forEach(z=>zak.add(new Option(`${z.nazwa} · ${z.km} km${z.brak?' · brak ceny':''}`,z.id)));
			zak.value=(byl&&[...zak.options].some(o=>o.value===byl))?byl:String(p.zaklad_id);
			zak.dataset.podpis=podpis;
		}
	});

	const auta=$('#auta'); auta.innerHTML='';
	w.grupy.forEach(g=>{
		const proc=g.wypelnienie!=null?Math.round(g.wypelnienie*100):null;
		const el=document.createElement('div');
		el.className='auto'; el.dataset.zaklad=g.zaklad_id;
		el.innerHTML=`
			<div><span class="etyk">Zakład</span><span class="zaklad-nazwa">${g.zaklad}</span></div>
			<div><span class="etyk">km</span><input class="km num" inputmode="numeric" value="${g.km}"
				title="${g.km_pewne?'trasa drogowa':'szacunek — router nie odpowiedział'}"></div>
			<div><span class="etyk">Środek transportu</span><select class="metoda">${
				g.metody.map(m=>`<option value="${m.id}"${m.id===g.metoda_id?' selected':''}>${m.nazwa} · ${m.koszt}</option>`).join('')
			}</select></div>
			<div><span class="etyk">Ładunek</span><span class="num">${g.tony} t${g.kursy>1?' · '+g.kursy+' kursy':''}</span></div>
			<div><span class="etyk">Wypełnienie auta</span>${
				proc!==null?`<div class="wypelnienie${proc>=100?' pelne':''}"><i style="width:${Math.min(proc,100)}%"></i><b>${proc}%</b></div>`
					:'<span class="num">—</span>'}</div>
			<div><span class="etyk">Koszt kursu</span><input class="kwota-transport num" inputmode="decimal" value="${g.koszt}"></div>
			${g.mieszana?'<div class="mieszana">W tej grupie jest i luz, i towar paletowy — jeden pojazd nie weźmie obu naraz. Sprawdź środek transportu.</div>':''}
			${g.dopelnienie?`<div class="namowa">Do pełnego auta brakuje <b>${g.dopelnienie.brakuje} t</b>. Przy ${g.dopelnienie.pelne} t przewóz spada z ${g.dopelnienie.teraz} na <b>${g.dopelnienie.potem} zł/t</b>.</div>`:''}`;
		auta.appendChild(el);
	});
	$('#pas-transport').hidden=!w.grupy.length;

	$('#s_towar').textContent=w.towar;
	$('#s_transport').textContent=w.transport;
	$('#s_tony').textContent=w.tony+' t';
	$('#s_zatone').textContent=w.za_tone;
	$('#s_razem').textContent=w.razem+' zł';
	$('#zapisz').disabled=false;
	$('#komunikat').className='komunikat'+(w.bez_ceny?' zle':'');
	$('#komunikat').textContent=w.bez_ceny
		?`${w.bez_ceny} ${w.bez_ceny===1?'pozycja nie ma':'pozycje nie mają'} ceny — ustal z Pawłem.`:'';
}

/* ---------- zdarzenia ---------- */
document.addEventListener('input',e=>{
	if(e.target.matches('.ilosc')){
		const tr=e.target.closest('tr'), ma=parseFloat((e.target.value||'').replace(',','.'))>0;
		tr.querySelector('.ptak').checked=ma;      // wpisanie ilosci zaznacza wiersz
		tr.classList.toggle('wybrany',ma);
		przelicz();
	} else if(e.target.matches('.cena')){ e.target.dataset.tkniete='1'; przelicz(); }
	else if(e.target.matches('.km,.kwota-transport')) przelicz();
});
document.addEventListener('change',e=>{
	if(e.target.matches('.forma,.jednostka,.zaklad,.metoda,#stan')) policz();
	else if(e.target.matches('.ptak')){
		const tr=e.target.closest('tr');
		tr.classList.toggle('wybrany',e.target.checked);
		if(e.target.checked) tr.querySelector('.ilosc').focus();
		else{tr.querySelector('.ilosc').value='';
			const c=tr.querySelector('.cena'); c.value=''; delete c.dataset.tkniete;}
		policz();
	}
});
document.addEventListener('click',e=>{
	const s=e.target.closest('.sugestia');
	if(s&&s.dataset.czynna==='tak'){
		const c=s.closest('tr').querySelector('.cena');
		c.value=''; delete c.dataset.tkniete;              // znow bierzemy z cennika
		policz();
	}
});

/* ---------- wczytanie oferty do edycji ---------- */
if(OFERTA){
	const v=(i,x)=>{const e=$(i); if(e&&x)e.value=x;};
	v('#k_nazwa',OFERTA.klient_nazwa); v('#k_tel',OFERTA.klient_telefon); v('#k_nip',OFERTA.klient_nip);
	v('#k_kanal',OFERTA.kanal); v('#k_uwagi',OFERTA.uwagi); v('#miejscowosc',OFERTA.miejscowosc);
	v('#stan',OFERTA.stan_transportu);
	miejscowoscId=OFERTA.miejscowosc_id||0;
	platnik=OFERTA.platnik||null;
	if(platnik) $('#platnik').innerHTML=`Płatnik: <b>${platnik.nazwa}</b> · ${platnik.adres||''}`;
	Object.entries(OFERTA.pozycje||{}).forEach(([k,p])=>{
		const tr=document.querySelector('[data-klucz="'+k+'"]'); if(!tr)return;
		tr.querySelector('.forma').value=p.forma_klucz;
		tr.querySelector('.jednostka').value=p.jednostka;
		tr.querySelector('.ilosc').value=p.ilosc;
		tr.classList.add('wybrany'); tr.querySelector('.ptak').checked=true;
		if(p.cena){const c=tr.querySelector('.cena'); c.value=p.cena; c.dataset.tkniete='1';}
	});
	policz();
}

/* ---------- zapis ---------- */
$('#zapisz').onclick=async()=>{
	const b=$('#zapisz'), k=$('#komunikat');
	b.disabled=true; k.className='komunikat'; k.textContent='Zapisuję…';
	const r=await api('agria_of_zapisz',{miejscowosc_id:miejscowoscId,stan_transportu:$('#stan').value,
		...zbierzPozycje(),...zbierzTransport(),
		aktualizuj:OFERTA?OFERTA.id:'',
		klient_nazwa:$('#k_nazwa').value,klient_telefon:$('#k_tel').value,klient_nip:$('#k_nip').value,
		klient_platnik:platnik?JSON.stringify(platnik):'',kanal:$('#k_kanal').value,uwagi:$('#k_uwagi').value},'POST');
	b.disabled=false;
	if(r.success){k.className='komunikat';
		k.innerHTML=`Oferta nr ${r.data.id} zapisana — <a href="${r.data.wydruk}" target="_blank">wydruk</a>`;}
	else{k.className='komunikat zle';k.textContent=(r.data&&r.data.blad)||'Nie udało się zapisać.';}
};
</script>
</body>
</html>
	<?php
}
