<?php
// Uzycie: wp eval-file wdroz-karta.php <id> <slug> <oczekiwana_dlugosc_obecnej_tresci>
// Z ~/agria-backups/t136-seria/ bierze <slug>-post_content.html, <slug>-post_excerpt.html i <slug>-meta.json (klucze jak w §2 pliku tresci).
[$id, $slug, $len] = [(int) $args[0], $args[1], (int) $args[2]];
$dir = getenv('HOME') . '/agria-backups/t136-seria/';
kses_remove_filters();
$p = get_post($id);
if (strlen($p->post_content) !== $len) { echo "STOP $id: dlugosc " . strlen($p->post_content) . " != $len\n"; return; }
file_put_contents($dir . "$slug-post_content-przed.html", $p->post_content);
file_put_contents($dir . "$slug-post_excerpt-przed.html", $p->post_excerpt);
$c = file_get_contents($dir . "$slug-post_content.html");
$e = file_get_contents($dir . "$slug-post_excerpt.html");
$r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $c, 'post_excerpt' => $e]), true);
if (is_wp_error($r)) { echo "BLAD $id: " . $r->get_error_message() . "\n"; return; }
$pola = ['title' => 'rank_math_title', 'meta description' => 'rank_math_description', 'focus keyword' => 'rank_math_focus_keyword'];
foreach (json_decode(file_get_contents($dir . "$slug-meta.json"), true) as $k => $v) {
	if (isset($pola[$k])) { update_post_meta($id, $pola[$k], wp_slash($v)); echo "$id: {$pola[$k]} = " . get_post_meta($id, $pola[$k], true) . "\n"; }
}
clean_post_cache($id);
$n = get_post($id);
echo "$id: tresc " . strlen($n->post_content) . " B, zgodna: " . ($n->post_content === $c ? 'TAK' : 'NIE') . ", lead zgodny: " . ($n->post_excerpt === $e ? 'TAK' : 'NIE') . "\n";
if (function_exists('rocket_clean_post')) { rocket_clean_post($id); echo "$id: cache WP Rocket wyczyszczony\n"; }
