<?php
// T-136 pilot: zapis 3 kart. Guard: długość obecnej treści = backup, inaczej STOP.
$dir = getenv('HOME') . '/agria-backups/t136/';
$karty = [312 => ['oxyfertil-90', 6997], 315 => ['weglanowe-odmiana-04', 7056], 307 => ['kreda-pastewna', 5557]];
kses_remove_filters();
foreach ($karty as $id => [$slug, $len]) {
    $p = get_post($id);
    if (strlen($p->post_content) !== $len) { echo "STOP $id: dlugosc " . strlen($p->post_content) . " != $len\n"; continue; }
    $c = file_get_contents("$dir$slug-post_content.html");
    $e = file_get_contents("$dir$slug-post_excerpt.html");
    $r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $c, 'post_excerpt' => $e]), true);
    if (is_wp_error($r)) { echo "BLAD $id: " . $r->get_error_message() . "\n"; continue; }
    foreach (['rank_math_title', 'rank_math_description', 'rank_math_focus_keyword'] as $k) {
        $f = "$dir$slug-$k.txt";
        if (file_exists($f)) update_post_meta($id, $k, wp_slash(file_get_contents($f)));
    }
    clean_post_cache($id);
    $p = get_post($id);
    $ok = ($p->post_content === $c) && ($p->post_excerpt === $e);
    echo "$id $slug: tresc " . strlen($p->post_content) . " B, zgodna z plikiem: " . ($ok ? 'TAK' : 'NIE') .
         " | title: " . get_post_meta($id, 'rank_math_title', true) . "\n";
}
