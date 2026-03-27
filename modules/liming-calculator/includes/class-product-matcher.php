<?php
/**
 * AGRIA Liming Calculator — Product Matcher
 *
 * Pobiera produkty WooCommerce z segmentem "rolnictwo",
 * wyciąga % CaO z taksonomii pa_min-cao i przelicza dawkę nawozu.
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
     * Pobierz produkty rolnicze z przeliczoną dawką
     *
     * @param float $cao_dose Dawka CaO [t/ha]
     * @param float $cao_part1 Część I dawki
     * @param float $cao_part2 Część II dawki (0 jeśli bez podziału)
     * @return array Produkty posortowane wg typu, potem dawki
     */
    public static function get_products( float $cao_dose, float $cao_part1, float $cao_part2 ): array {
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
     * WP_Query — produkty z segmentem "rolnictwo" lub "sadownictwo"
     */
    private static function query_agriculture_products(): array {
        $args = [
            'post_type'      => 'product',
            'posts_per_page' => 50,
            'post_status'    => 'publish',
            'fields'         => 'ids',
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
     * Wyciągnij wartość liczbową CaO% z taksonomii pa_min-cao
     * Format slugów: "min-70-cao" → 70, "min-50-cao" → 50
     */
    private static function extract_cao_percent( int $product_id ): float {
        $terms = wp_get_object_terms( $product_id, 'pa_min-cao', [ 'fields' => 'slugs' ] );

        if ( is_wp_error( $terms ) || empty( $terms ) ) {
            return 0.0;
        }

        $slug = $terms[0]; // np. "min-70-cao"

        if ( preg_match( '/(\d+)/', $slug, $matches ) ) {
            return (float) $matches[1];
        }

        return 0.0;
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
