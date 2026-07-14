<?php
/**
 * mcp-ext.php — rozszerzenia narzędzi MCP Agria (ładowane przez mcp.php v2.0.1).
 *   - update_post_content : setter post_content (wp_posts) + cache flush + readback
 *   - update_postmeta     : setter postmeta.meta_value (np. _elementor_data) + readback
 *   - query_db_write      : ograniczony zapis SQL (UPDATE / INSERT / REPLACE)
 * @version ext-1.1  (2026-06-29, STR-02 + STR-04 backlog agria)
 */
defined('ABSPATH') || ( PHP_SAPI === 'cli' ) || true;

$GLOBALS['MCP_EXT_TOOLS'][] = [
    'name' => 'update_post_content',
    'description' => 'Zapis post_content (wp_posts) po ID. Aktualizuje post_modified, czyści cache, readback. expect_old_len w BAJTACH.',
    'inputSchema' => ['type'=>'object','properties'=>['post_id'=>['type'=>'integer'],'content'=>['type'=>'string'],'expect_old_len'=>['type'=>'integer']],'required'=>['post_id','content']],
];
$GLOBALS['MCP_EXT_HANDLERS']['update_post_content'] = function (array $args) {
    $pid=(int)($args['post_id']??0);
    if($pid<=0) throw new \Exception('post_id is required');
    if(!array_key_exists('content',$args)||!is_string($args['content'])) throw new \Exception('content (string) is required');
    $content=$args['content'];
    if($content==='') throw new \Exception('content is empty — refusing to wipe post_content');
    load_wp(); global $wpdb;
    $old=$wpdb->get_var($wpdb->prepare("SELECT post_content FROM {$wpdb->posts} WHERE ID = %d",$pid));
    if($old===null) throw new \Exception("Post not found: $pid");
    $old_len=strlen($old);
    if(isset($args['expect_old_len']) && (int)$args['expect_old_len']!==$old_len)
        throw new \Exception("expect_old_len mismatch: server has $old_len, expected ".(int)$args['expect_old_len']." — aborting (stale state)");
    if($content===$old) return ['post_id'=>$pid,'old_len'=>$old_len,'new_len'=>$old_len,'affected'=>0,'note'=>'identical — no change'];
    $now=current_time('mysql'); $now_gmt=current_time('mysql',1);
    $res=$wpdb->update($wpdb->posts,['post_content'=>$content,'post_modified'=>$now,'post_modified_gmt'=>$now_gmt],['ID'=>$pid],['%s','%s','%s'],['%d']);
    if($res===false) throw new \Exception("DB update failed: {$wpdb->last_error}");
    if(function_exists('clean_post_cache')) clean_post_cache($pid);
    $new=$wpdb->get_var($wpdb->prepare("SELECT post_content FROM {$wpdb->posts} WHERE ID = %d",$pid));
    return ['post_id'=>$pid,'old_len'=>$old_len,'new_len'=>strlen((string)$new),'affected'=>(int)$res,'match'=>($new===$content)];
};

$GLOBALS['MCP_EXT_TOOLS'][] = [
    'name' => 'update_postmeta',
    'description' => 'Zapis postmeta.meta_value (string) po post_id + meta_key (np. _elementor_data). Czyści cache, readback. expect_old_len w BAJTACH.',
    'inputSchema' => ['type'=>'object','properties'=>['post_id'=>['type'=>'integer'],'meta_key'=>['type'=>'string'],'value'=>['type'=>'string'],'expect_old_len'=>['type'=>'integer']],'required'=>['post_id','meta_key','value']],
];
$GLOBALS['MCP_EXT_HANDLERS']['update_postmeta'] = function (array $args) {
    $pid=(int)($args['post_id']??0); $key=(string)($args['meta_key']??'');
    if($pid<=0||$key==='') throw new \Exception('post_id and meta_key required');
    if(!array_key_exists('value',$args)||!is_string($args['value'])) throw new \Exception('value (string) required');
    $val=$args['value'];
    if($val==='') throw new \Exception('value is empty — refusing');
    load_wp(); global $wpdb;
    $old=$wpdb->get_var($wpdb->prepare("SELECT meta_value FROM {$wpdb->postmeta} WHERE post_id=%d AND meta_key=%s",$pid,$key));
    if($old===null) throw new \Exception("postmeta not found: $pid / $key");
    $old_len=strlen($old);
    if(isset($args['expect_old_len']) && (int)$args['expect_old_len']!==$old_len)
        throw new \Exception("expect_old_len mismatch: server has $old_len");
    if($val===$old) return ['affected'=>0,'old_len'=>$old_len,'new_len'=>$old_len,'note'=>'identical'];
    $res=$wpdb->update($wpdb->postmeta,['meta_value'=>$val],['post_id'=>$pid,'meta_key'=>$key],['%s'],['%d','%s']);
    if($res===false) throw new \Exception("update failed: {$wpdb->last_error}");
    if(function_exists('clean_post_cache')) clean_post_cache($pid);
    $new=$wpdb->get_var($wpdb->prepare("SELECT meta_value FROM {$wpdb->postmeta} WHERE post_id=%d AND meta_key=%s",$pid,$key));
    return ['affected'=>(int)$res,'old_len'=>$old_len,'new_len'=>strlen((string)$new),'match'=>($new===$val)];
};

$GLOBALS['MCP_EXT_TOOLS'][] = [
    'name' => 'query_db_write',
    'description' => 'Zapis SQL — TYLKO UPDATE/INSERT/REPLACE. Blok DROP/ALTER/TRUNCATE/CREATE/GRANT/REVOKE/DELETE. UPDATE wymaga WHERE. {prefix} = prefix tabel.',
    'inputSchema' => ['type'=>'object','properties'=>['sql'=>['type'=>'string']],'required'=>['sql']],
];
$GLOBALS['MCP_EXT_HANDLERS']['query_db_write'] = function (array $args) {
    $sql=trim((string)($args['sql']??''));
    if($sql==='') throw new \Exception('sql is required');
    if(!preg_match('/^(UPDATE|INSERT|REPLACE)\s/i',$sql)) throw new \Exception('Only UPDATE / INSERT / REPLACE allowed');
    if(preg_match('/\b(DROP|ALTER|TRUNCATE|CREATE|GRANT|REVOKE|DELETE)\b/i',$sql)) throw new \Exception('Blocked keyword');
    if(preg_match('/^UPDATE\s/i',$sql) && !preg_match('/\bWHERE\b/i',$sql)) throw new \Exception('UPDATE without WHERE is blocked');
    load_wp(); global $wpdb;
    $sql=str_replace('{prefix}',$wpdb->prefix,$sql);
    $res=$wpdb->query($sql);
    if($res===false) throw new \Exception("DB error: {$wpdb->last_error}");
    return ['affected'=>(int)$res,'last_error'=>$wpdb->last_error ?: null];
};

/* ── ext-1.2 (2026-07-14) — naprawa parametrów produktowych ───────────────── */

$GLOBALS['MCP_EXT_TOOLS'][] = [
    'name' => 'db_export',
    'description' => 'Zrzut tabel do pliku .sql w wp-content/ (INSERT-y). tables = lista nazw BEZ prefixu, np. ["terms","term_taxonomy","term_relationships"]. Zwraca ścieżkę i liczbę wierszy.',
    'inputSchema' => ['type'=>'object','properties'=>['tables'=>['type'=>'array','items'=>['type'=>'string']],'label'=>['type'=>'string']],'required'=>['tables']],
];
$GLOBALS['MCP_EXT_HANDLERS']['db_export'] = function (array $args) {
    $tables = $args['tables'] ?? [];
    if (!is_array($tables) || !$tables) throw new \Exception('tables (array) required');
    $label = preg_replace('/[^a-zA-Z0-9_-]/', '', (string)($args['label'] ?? 'export'));
    load_wp(); global $wpdb;
    $dir = dirname(untrailingslashit(ABSPATH)) . '/agria-backups'; // POZA web root — nigdy w wp-content (brak AllowOverride na nazwa.pl)
    if (!is_dir($dir) && !@mkdir($dir, 0755, true)) throw new \Exception('cannot create backup dir');
    $file = $dir . '/' . $label . '-' . gmdate('Ymd-His') . '.sql';
    $fh = @fopen($file, 'w');
    if (!$fh) throw new \Exception('cannot open file for writing');
    fwrite($fh, "-- agria db_export {$label} " . gmdate('c') . "\n");
    $total = 0; $summary = [];
    foreach ($tables as $t) {
        $t = preg_replace('/[^a-zA-Z0-9_]/', '', (string)$t);
        if ($t === '') continue;
        $full = $wpdb->prefix . $t;
        $exists = $wpdb->get_var($wpdb->prepare("SHOW TABLES LIKE %s", $full));
        if (!$exists) { $summary[$t] = 'MISSING'; continue; }
        $rows = $wpdb->get_results("SELECT * FROM `{$full}`", ARRAY_A);
        $n = 0;
        fwrite($fh, "\n-- table {$full} (" . count($rows) . " rows)\n");
        foreach ($rows as $r) {
            $cols = array_map(function ($c) { return '`' . $c . '`'; }, array_keys($r));
            $vals = array_map(function ($v) use ($wpdb) {
                return ($v === null) ? 'NULL' : "'" . esc_sql($v) . "'";
            }, array_values($r));
            fwrite($fh, "INSERT INTO `{$full}` (" . implode(',', $cols) . ") VALUES (" . implode(',', $vals) . ");\n");
            $n++;
        }
        $summary[$t] = $n; $total += $n;
    }
    fclose($fh);
    return ['file' => str_replace(ABSPATH, '', $file), 'abs' => $file, 'rows_total' => $total, 'tables' => $summary, 'bytes' => filesize($file)];
};

$GLOBALS['MCP_EXT_TOOLS'][] = [
    'name' => 'wc_product_attributes',
    'description' => 'Odczyt/zapis atrybutów produktu przez API WooCommerce. action=get zwraca atrybuty. action=set_terms ustawia wartości atrybutu taksonomicznego (terms = lista nazw; pusta lista USUWA atrybut z produktu, także z _product_attributes). Czyści cache.',
    'inputSchema' => ['type'=>'object','properties'=>[
        'product_id'=>['type'=>'integer'],
        'action'=>['type'=>'string','enum'=>['get','set_terms']],
        'taxonomy'=>['type'=>'string'],
        'terms'=>['type'=>'array','items'=>['type'=>'string']],
        'visible'=>['type'=>'boolean'],
    ],'required'=>['product_id','action']],
];
$GLOBALS['MCP_EXT_HANDLERS']['wc_product_attributes'] = function (array $args) {
    $pid = (int)($args['product_id'] ?? 0);
    $action = (string)($args['action'] ?? '');
    if ($pid <= 0) throw new \Exception('product_id required');
    load_wp();
    if (!function_exists('wc_get_product')) throw new \Exception('WooCommerce not loaded');
    $product = wc_get_product($pid);
    if (!$product) throw new \Exception("Product not found: $pid");

    $dump = function ($p) {
        $out = [];
        foreach ($p->get_attributes() as $key => $a) {
            $out[$key] = [
                'name'      => $a->get_name(),
                'taxonomy'  => $a->is_taxonomy() ? $a->get_taxonomy() : null,
                'visible'   => $a->get_visible(),
                'options'   => $a->is_taxonomy()
                    ? wp_list_pluck(get_terms(['taxonomy'=>$a->get_taxonomy(),'include'=>$a->get_options(),'hide_empty'=>false]), 'name')
                    : $a->get_options(),
            ];
        }
        return $out;
    };

    if ($action === 'get') return ['product_id'=>$pid,'title'=>$product->get_name(),'attributes'=>$dump($product)];

    if ($action !== 'set_terms') throw new \Exception('unknown action');
    $tax = (string)($args['taxonomy'] ?? '');
    if ($tax === '') throw new \Exception('taxonomy required for set_terms');
    if (!taxonomy_exists($tax)) throw new \Exception("taxonomy does not exist: $tax");
    if (!array_key_exists('terms', $args) || !is_array($args['terms'])) throw new \Exception('terms (array) required');

    $names = array_values(array_filter(array_map('strval', $args['terms']), function ($s) { return trim($s) !== ''; }));
    $before = $dump($product);
    $attrs  = $product->get_attributes();

    if (!$names) {
        // pusta lista = usuń atrybut z produktu (znika też z _product_attributes)
        unset($attrs[$tax]);
        wp_set_object_terms($pid, [], $tax);
    } else {
        $ids = [];
        foreach ($names as $n) {
            $term = get_term_by('name', $n, $tax);
            if (!$term) {
                $new = wp_insert_term($n, $tax);
                if (is_wp_error($new)) throw new \Exception("cannot create term '$n' in $tax: " . $new->get_error_message());
                $ids[] = (int)$new['term_id'];
            } else {
                $ids[] = (int)$term->term_id;
            }
        }
        wp_set_object_terms($pid, $ids, $tax);
        $a = isset($attrs[$tax]) ? $attrs[$tax] : new WC_Product_Attribute();
        $a->set_id(wc_attribute_taxonomy_id_by_name($tax));
        $a->set_name($tax);
        $a->set_options($ids);
        $a->set_visible(array_key_exists('visible', $args) ? (bool)$args['visible'] : true);
        $a->set_variation(false);
        $attrs[$tax] = $a;
    }

    $product->set_attributes($attrs);
    $product->save();
    if (function_exists('clean_post_cache')) clean_post_cache($pid);
    if (function_exists('wc_delete_product_transients')) wc_delete_product_transients($pid);
    delete_post_meta($pid, '_elementor_element_cache');

    $fresh = wc_get_product($pid);
    return ['product_id'=>$pid,'taxonomy'=>$tax,'before'=>($before[$tax] ?? null),'after'=>($dump($fresh)[$tax] ?? null),'removed'=>empty($names)];
};
