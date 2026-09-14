<?php
// Uzycie: wp eval-file wdroz-karta.php <id> <slug> <oczekiwana_dlugosc_obecnej_tresci>
[$id, $slug, $len] = [(int) $args[0], $args[1], (int) $args[2]];
$dir = getenv('HOME') . '/agria-backups/t136-v2/';
kses_remove_filters();
$p = get_post($id);
if (strlen($p->post_content) !== $len) { echo "STOP $id: dlugosc " . strlen($p->post_content) . " != $len\n"; return; }
file_put_contents($dir . "$slug-post_content-przed.html", $p->post_content);
$c = file_get_contents($dir . "$slug-post_content.html");
$r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $c]), true);
if (is_wp_error($r)) { echo "BLAD $id: " . $r->get_error_message() . "\n"; return; }
clean_post_cache($id);
echo "$id: tresc " . strlen(get_post($id)->post_content) . " B, zgodna z plikiem: " . (get_post($id)->post_content === $c ? 'TAK' : 'NIE') . "\n";
if (function_exists('rocket_clean_post')) { rocket_clean_post($id); echo "$id: cache WP Rocket wyczyszczony\n"; }
