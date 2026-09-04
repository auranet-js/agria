<?php
/**
 * AGRIA Liming Calculator — Product Matcher
 *
 * Pobiera produkty WooCommerce z segmentem "rolnictwo",
 * wyciąga % CaO z taksonomii pa_min-cao i przelicza dawkę nawozu.
 *
 * Od T-044 (04.09.2026) także dobór nawozów magnezowych: %MgO z taksonomii
 * pa_agria-mgo, dwuetapowo (najpierw magnez, potem dopokrycie CaO).
 */

defined( 'ABSPATH' ) || exit;

class Agria_Product_Matcher {

    /**
     * Typy wapna — mapowanie na podstawie nazwy produktu
     */
    private const TYPE_KEYWORDS = [
        'tlenkowe' => ['tlenkowe', 'agrobielik', 'oxyfertil', 'palone'],
        'weglanowe' => ['węglanowe', 'weglanowe', 'dolomit', 'kreda'],
        'mieszanka' => ['mieszanka', 'tlenkowo-węglanowa'],
    ];

    /**
     * Produkt referencyjny do dopokrycia CaO w kroku 2 doboru magnezowego.
     *
     * Agrobielik 70 (#310) — wybór z prototypu zaakceptowanego przez K. Nowaka
     * 28.08.2026. Świadomie NIE bierzemy automatycznie najwyższego CaO bez
     * magnezu, bo to Agrobielik 90 i zmieniłoby liczby, które klient
     * zatwierdził. %CaO czytamy z taksonomii, nie z kodu.
     */
    private const CAO_TOPUP_ID = 310;

    /**
     * Pobierz produkty rolnicze z przeliczoną dawką
     *
     * @param float $cao_dose Dawka CaO [t/ha]
     * @param float $cao_part1 Część I dawki
     * @param float $cao_part2 Część II dawki (0 jeśli bez podziału)
     * @param bool  $mg_declared Czy rolnik podał zawartość magnezu — jeśli nie,
     *                           z listy wypadają nawozy magnezowe (T-043)
     * @return array Produkty posortowane wg typu, potem dawki
     */
    public static function get_products( float $cao_dose, float $cao_part1, float $cao_part2, bool $mg_declared = false ): array {
        if ( $cao_dose <= 0 ) {
            return [];
        }

        $products = self::query_agriculture_products();
        $results  = [];

        foreach ( $products as $product_id ) {
            $cao_pct = self::extract_cao_percent( $product_id );

            if ( $cao_pct <= 0 ) {
                continue;
            }

            // Bez deklaracji magnezu nie proponujemy nawozów magnezowych
            if ( ! $mg_declared && self::extract_mgo_percent( $product_id ) > 0 ) {
                continue;
            }

            $name       = get_the_title( $product_id );
            $type       = self::detect_product_type( $name );
            $dose_total = round( $cao_dose / ( $cao_pct / 100 ), 2 );
            $dose_p1    = $cao_part1 > 0 ? round( $cao_part1 / ( $cao_pct / 100 ), 2 ) : 0;
            $dose_p2    = $cao_part2 > 0 ? round( $cao_part2 / ( $cao_pct / 100 ), 2 ) : 0;

            $results[] = [
                'id'         => $product_id,
                'name'       => $name,
                'cao_pct'    => $cao_pct,
                'dose_total' => $dose_total,
                'dose_p1'    => $dose_p1,
                'dose_p2'    => $dose_p2,
                'url'        => get_permalink( $product_id ),
                'thumbnail'  => get_the_post_thumbnail_url( $product_id, 'thumbnail' ) ?: '',
                'type'       => $type,
                'type_label' => self::type_label( $type ),
            ];
        }

        // Sortuj: tlenkowe najpierw, potem mieszanka, potem węglanowe; wewnątrz — rosnąco wg dawki
        usort( $results, function ( $a, $b ) {
            $type_order = [ 'tlenkowe' => 1, 'mieszanka' => 2, 'weglanowe' => 3 ];
            $oa = $type_order[ $a['type'] ] ?? 9;
            $ob = $type_order[ $b['type'] ] ?? 9;

            if ( $oa !== $ob ) {
                return $oa <=> $ob;
            }

            return $a['dose_total'] <=> $b['dose_total'];
        });

        return $results;
    }

    /**
     * Dobór nawozów magnezowych — krok 1 doboru dwuetapowego (Mg-first).
     *
     * Dawkę nawozu ustala niedobór magnezu, NIE potrzeba wapnowania. To, czego
     * przy tej dawce zabraknie do dawki CaO wg IUNG, dopokrywa wapno bez magnezu.
     * Poprzednie max(wg Mg, wg CaO) dawało nierealne 16–19 t/ha dolomitu.
     *
     * @param float $dose_mgo_kg Potrzeba MgO [kg/ha]
     * @param float $cao_dose    Dawka CaO wg IUNG [t/ha]
     * @return array
     */
    public static function get_mg_products( float $dose_mgo_kg, float $cao_dose ): array {
        if ( $dose_mgo_kg <= 0 ) {
            return [];
        }

        $topup   = self::get_cao_topup();
        $results = [];

        foreach ( self::query_agriculture_products() as $product_id ) {
            $mgo_pct = self::extract_mgo_percent( $product_id );

            if ( $mgo_pct <= 0 ) {
                continue;
            }

            // W tabeli magnezowej liczy się CaO netto — dla dolomitu deklaracja
            // pa_min-cao niesie sumę CaO+MgO, więc magnez trzeba odjąć
            $cao_pct = self::extract_cao_percent_net( $product_id );

            $by_mg     = round( ( $dose_mgo_kg / ( $mgo_pct / 100 ) ) / 1000, 2 ); // t nawozu/ha
            $cao_given = round( $by_mg * ( $cao_pct / 100 ), 2 );                  // t CaO/ha z tej dawki
            $cao_left  = max( 0, round( $cao_dose - $cao_given, 2 ) );             // t CaO/ha brakujące
            $topup_t   = ( $cao_left > 0 && $topup['cao_pct'] > 0 )
                ? round( $cao_left / ( $topup['cao_pct'] / 100 ), 2 )
                : 0;

            $results[] = [
                'id'          => $product_id,
                'name'        => get_the_title( $product_id ),
                'url'         => get_permalink( $product_id ),
                'mgo_pct'     => $mgo_pct,
                'cao_pct'     => $cao_pct,
                'declaration' => self::declaration_note( $product_id ),
                'dose_by_mg'  => $by_mg,
                'cao_given'   => $cao_given,
                'cao_left'    => $cao_left,
                'topup'       => $topup_t,
            ];
        }

        // Od najwyższej zawartości MgO
        usort( $results, fn( $a, $b ) => $b['mgo_pct'] <=> $a['mgo_pct'] );

        return $results;
    }

    /**
     * Produkt do dopokrycia CaO w kroku 2 — nazwa i %CaO z bazy
     */
    public static function get_cao_topup(): array {
        $id = (int) apply_filters( 'agria_calc_cao_topup_id', self::CAO_TOPUP_ID );

        $cao  = self::extract_cao_percent( $id );
        $name = get_the_title( $id );

        // Zabezpieczenie: gdyby produkt zniknął — najwyższe CaO bez magnezu
        if ( $cao <= 0 || ! $name ) {
            $best = [ 'id' => 0, 'name' => '', 'cao' => 0.0 ];
            foreach ( self::query_agriculture_products() as $pid ) {
                if ( self::extract_mgo_percent( $pid ) > 0 ) {
                    continue;
                }
                $c = self::extract_cao_percent( $pid );
                if ( $c > $best['cao'] ) {
                    $best = [ 'id' => $pid, 'name' => get_the_title( $pid ), 'cao' => $c ];
                }
            }
            return [ 'id' => $best['id'], 'name' => $best['name'], 'cao_pct' => $best['cao'] ];
        }

        return [ 'id' => $id, 'name' => $name, 'cao_pct' => $cao ];
    }

    /**
     * WP_Query — produkty z segmentem "rolnictwo" lub "sadownictwo"
     */
    private static function query_agriculture_products(): array {
        $args = [
            'post_type'      => 'product',
            'posts_per_page' => 50,
            'post_status'    => 'publish',
            'fields'         => 'ids',
            // STR-01 (zgłoszenie Pawła 2026-06-15): kreda malarska (#304) i kreda
            // pastewna (#307) mają segment "rolnictwo" + wartość CaO, więc wpadałyby
            // do doboru kalkulatora — ale to NIE są wapna do odkwaszania pola
            // (malarska = budowlana, pastewna = dodatek paszowy). Wykluczamy.
            'post__not_in'   => [ 304, 307 ],
            'tax_query'      => [
                [
                    'taxonomy' => 'pa_agria-segment',
                    'field'    => 'slug',
                    'terms'    => [ 'rolnictwo', 'sadownictwo' ],
                    'operator' => 'IN',
                ],
            ],
        ];

        $query = new WP_Query( $args );
        return $query->posts;
    }

    /**
     * Pierwszy slug produktu w danej taksonomii
     */
    private static function first_term_slug( int $product_id, string $taxonomy ): string {
        $terms = wp_get_object_terms( $product_id, $taxonomy, [ 'fields' => 'slugs' ] );

        if ( is_wp_error( $terms ) || empty( $terms ) ) {
            return '';
        }

        return (string) $terms[0];
    }

    /**
     * Wyciągnij wartość liczbową CaO% z taksonomii pa_min-cao
     * Format slugów: "min-70-cao" → 70, "min-50-cao" → 50
     */
    private static function extract_cao_percent( int $product_id ): float {
        $slug = self::first_term_slug( $product_id, 'pa_min-cao' );

        if ( '' === $slug ) {
            return 0.0;
        }

        if ( preg_match( '/(\d+)/', $slug, $matches ) ) {
            return (float) $matches[1];
        }

        return 0.0;
    }

    /**
     * Wyciągnij wartość liczbową MgO% z taksonomii pa_agria-mgo
     * Format slugów: "min-25-mgo" → 25, "min-8-20-mgo" → 8 (dolna granica)
     */
    private static function extract_mgo_percent( int $product_id ): float {
        $slug = self::first_term_slug( $product_id, 'pa_agria-mgo' );

        if ( '' === $slug ) {
            return 0.0;
        }

        if ( preg_match( '/(\d+)/', $slug, $matches ) ) {
            return (float) $matches[1];
        }

        return 0.0;
    }

    /**
     * CaO netto — czyste CaO bez magnezu.
     *
     * Część deklaracji podaje SUMĘ CaO+MgO (dolomit: "cao-mgo-min-45-w-tym-mgo-min-15",
     * karta producenta i katalog AGRII: "CaO + MgO min 45%, w tym MgO min 15%").
     * Wtedy czyste CaO = 45 − 15 = 30. Pozostałe produkty deklarują samo CaO
     * ("min-70-cao"), więc wartość zostaje bez zmian.
     *
     * Uwaga: dotyczy WYŁĄCZNIE tabeli magnezowej. Klasyczny dobór wg CaO
     * korzysta z extract_cao_percent i liczy jak przed wdrożeniem — poprawka
     * tamtej ścieżki to osobne zadanie z własną regresją.
     */
    private static function extract_cao_percent_net( int $product_id ): float {
        $cao  = self::extract_cao_percent( $product_id );
        $slug = self::first_term_slug( $product_id, 'pa_min-cao' );

        if ( $cao > 0 && str_starts_with( $slug, 'cao-mgo' ) ) {
            $mgo = self::extract_mgo_percent( $product_id );
            if ( $mgo > 0 && $mgo < $cao ) {
                return $cao - $mgo;
            }
        }

        return $cao;
    }

    /**
     * Pełna deklaracja producenta — pokazywana tam, gdzie liczba w tabeli
     * nie jest dosłownym odczytem deklaracji (suma CaO+MgO albo widełki).
     */
    private static function declaration_note( int $product_id ): string {
        $cao_slug = self::first_term_slug( $product_id, 'pa_min-cao' );
        $mgo_slug = self::first_term_slug( $product_id, 'pa_agria-mgo' );

        $is_sum   = str_starts_with( $cao_slug, 'cao-mgo' );
        $is_range = preg_match( '/\d+-\d+-(cao|mgo)/', $cao_slug ) || preg_match( '/\d+-\d+-(cao|mgo)/', $mgo_slug );

        if ( ! $is_sum && ! $is_range ) {
            return '';
        }

        // Gdy deklaracja CaO niesie sumę, sama podaje już MgO — nie dublujemy
        $taxonomies = $is_sum ? [ 'pa_min-cao' ] : [ 'pa_min-cao', 'pa_agria-mgo' ];

        $parts = [];
        foreach ( $taxonomies as $taxonomy ) {
            $terms = wp_get_object_terms( $product_id, $taxonomy, [ 'fields' => 'names' ] );
            if ( ! is_wp_error( $terms ) && ! empty( $terms ) ) {
                $parts[] = $terms[0];
            }
        }

        return $parts ? 'deklaracja: ' . implode( ', ', $parts ) : '';
    }

    /**
     * Wykryj typ wapna na podstawie nazwy produktu
     */
    private static function detect_product_type( string $name ): string {
        $name_lower = mb_strtolower( $name );

        // Mieszanka sprawdzaj jako pierwszą (zawiera "tlenkowo" i "węglanowe")
        foreach ( self::TYPE_KEYWORDS['mieszanka'] as $keyword ) {
            if ( str_contains( $name_lower, $keyword ) ) {
                return 'mieszanka';
            }
        }

        foreach ( self::TYPE_KEYWORDS['tlenkowe'] as $keyword ) {
            if ( str_contains( $name_lower, $keyword ) ) {
                return 'tlenkowe';
            }
        }

        foreach ( self::TYPE_KEYWORDS['weglanowe'] as $keyword ) {
            if ( str_contains( $name_lower, $keyword ) ) {
                return 'weglanowe';
            }
        }

        return 'inne';
    }

    /**
     * Label typu wapna
     */
    private static function type_label( string $type ): string {
        return match ( $type ) {
            'tlenkowe'  => 'Wapno tlenkowe (szybkie działanie)',
            'weglanowe' => 'Wapno węglanowe (działanie długotrwałe)',
            'mieszanka' => 'Mieszanka tlenkowo-węglanowa',
            default     => 'Inne',
        };
    }
}
