<?php
$dir = getenv('HOME') . '/agria-backups/t136/v2/';
$id = 312; $len = 7741;
kses_remove_filters();
$p = get_post($id);
if (strlen($p->post_content) !== $len) { echo "STOP: dlugosc " . strlen($p->post_content) . " != $len\n"; return; }
$c = file_get_contents($dir . 'oxyfertil-90-post_content.html');
$r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $c]), true);
if (is_wp_error($r)) { echo "BLAD: " . $r->get_error_message() . "\n"; return; }
clean_post_cache($id);
echo "312: tresc " . strlen(get_post($id)->post_content) . " B, zgodna: " . (get_post($id)->post_content === $c ? 'TAK' : 'NIE') . "\n";
if (function_exists('rocket_clean_post')) { rocket_clean_post($id); echo "rocket_clean_post OK\n"; }
