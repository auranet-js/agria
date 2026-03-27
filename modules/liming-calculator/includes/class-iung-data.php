<?php
/**
 * Tablice dawek CaO wg IUNG-PIB Puławy (Jadczyszyn, Lipiński, 2022)
 * "Zasady ustalania dawek wapna w doradztwie nawozowym"
 * ISBN 978-83-7562-385-7
 *
 * Dane publiczne, statyczne — nie wymagają bazy danych.
 */

defined( 'ABSPATH' ) || exit;

class Agria_IUNG_Data {

    /**
     * Grunty orne — dawki CaO [t/ha]
     * Klucz: pH (string z kropką), Wartość: [total, part1, part2]
     */
    public static function get_arable_doses(): array {
        return [
            'bardzo_lekka' => [
                '5.0' => [0.2, 0.2, 0],
                '4.9' => [0.5, 0.5, 0],
                '4.8' => [0.8, 0.8, 0],
                '4.7' => [1.0, 1.0, 0],
                '4.6' => [1.3, 1.3, 0],
                '4.5' => [1.6, 1.6, 0],
                '4.4' => [1.8, 1.8, 0],
                '4.3' => [2.0, 2.0, 0],
                '4.2' => [2.2, 2.2, 0],
                '4.1' => [2.4, 2.4, 0],
                '4.0' => [2.8, 2.8, 0],
                '3.9' => [3.1, 3.1, 0],
                '3.8' => [3.4, 3.4, 0],
            ],
            'lekka' => [
                '5.5' => [0.2, 0.2, 0],
                '5.4' => [0.5, 0.5, 0],
                '5.3' => [0.9, 0.9, 0],
                '5.2' => [1.2, 1.2, 0],
                '5.1' => [1.5, 1.5, 0],
                '5.0' => [1.8, 1.8, 0],
                '4.9' => [2.1, 2.1, 0],
                '4.8' => [2.3, 2.3, 0],
                '4.7' => [2.6, 2.6, 0],
                '4.6' => [2.9, 2.9, 0],
                '4.5' => [3.1, 3.1, 0],
                '4.4' => [3.4, 3.4, 0],
                '4.3' => [4.5, 3.5, 1.0],
                '4.2' => [4.7, 3.5, 1.2],
                '4.1' => [5.5, 3.5, 2.0],
                '4.0' => [5.9, 3.5, 2.4],
                '3.9' => [6.3, 3.5, 2.8],
                '3.8' => [6.5, 3.5, 3.0],
            ],
            'srednia' => [
                '6.0' => [0.4, 0.4, 0],
                '5.9' => [0.8, 0.8, 0],
                '5.8' => [1.2, 1.2, 0],
                '5.7' => [1.6, 1.6, 0],
                '5.6' => [2.0, 2.0, 0],
                '5.5' => [2.4, 2.4, 0],
                '5.4' => [2.8, 2.8, 0],
                '5.3' => [3.2, 3.2, 0],
                '5.2' => [3.6, 3.6, 0],
                '5.1' => [3.9, 3.9, 0],
                '5.0' => [4.2, 4.2, 0],
                '4.9' => [4.4, 4.4, 0],
                '4.8' => [4.8, 4.8, 0],
                '4.7' => [5.0, 5.0, 0],
                '4.6' => [5.4, 5.0, 0.4],
                '4.5' => [5.8, 5.0, 0.8],
                '4.4' => [6.2, 5.0, 1.2],
                '4.3' => [6.4, 5.0, 1.4],
                '4.2' => [6.6, 5.0, 1.6],
                '4.1' => [7.0, 5.0, 2.0],
                '4.0' => [7.4, 5.0, 2.4],
                '3.9' => [7.8, 5.0, 2.8],
            ],
            'ciezka' => [
                '6.3' => [0.2, 0.2, 0],
                '6.2' => [0.2, 0.2, 0],
                '6.1' => [0.5, 0.5, 0],
                '6.0' => [0.8, 0.8, 0],
                '5.9' => [1.0, 1.0, 0],
                '5.8' => [1.5, 1.5, 0],
                '5.7' => [2.0, 2.0, 0],
                '5.6' => [2.5, 2.5, 0],
                '5.5' => [3.0, 3.0, 0],
                '5.4' => [3.5, 3.5, 0],
                '5.3' => [3.8, 3.8, 0],
                '5.2' => [4.1, 4.1, 0],
                '5.1' => [4.5, 4.5, 0],
                '5.0' => [4.8, 4.8, 0],
                '4.9' => [5.1, 5.1, 0],
                '4.8' => [5.4, 5.4, 0],
                '4.7' => [5.7, 5.7, 0],
                '4.6' => [5.8, 5.8, 0],
                '4.5' => [6.0, 6.0, 0],
                '4.4' => [7.0, 6.0, 1.0],
                '4.3' => [7.5, 6.0, 1.5],
                '4.2' => [8.0, 6.0, 2.0],
                '4.1' => [9.0, 6.0, 3.0],
                '4.0' => [9.8, 6.0, 3.8],
                '3.9' => [10.8, 6.0, 4.8],
            ],
        ];
    }

    /**
     * Użytki zielone — dawki CaO [t/ha]
     * Klucz pH → [C<2.5%, C 2.6-5.0%, C 5.1-10.0%, C>10%]
     */
    public static function get_grassland_doses(): array {
        return [
            '3.8' => [1.5, 2.0, 3.0, 3.0],
            '3.9' => [1.5, 2.0, 3.0, 3.0],
            '4.0' => [1.5, 2.0, 3.0, 3.0],
            '4.1' => [1.5, 2.0, 3.0, 3.0],
            '4.2' => [1.5, 2.0, 3.0, 2.9],
            '4.3' => [1.5, 2.0, 3.0, 2.8],
            '4.4' => [1.5, 2.0, 3.0, 2.7],
            '4.5' => [1.5, 2.0, 3.0, 2.4],
            '4.6' => [1.5, 1.9, 2.9, 2.1],
            '4.7' => [1.3, 1.8, 2.8, 1.7],
            '4.8' => [1.2, 1.7, 2.7, 1.3],
            '4.9' => [1.1, 1.6, 2.6, 0.9],
            '5.0' => [1.0, 1.5, 2.5, 0.5],
            '5.1' => [0.9, 0.9, 0.0, 0.0],
            '5.2' => [0.8, 0.8, 0.0, 0.0],
            '5.3' => [0.7, 0.7, 0.0, 0.0],
            '5.4' => [0.6, 0.6, 0.0, 0.0],
            '5.5' => [0.5, 0.5, 0.0, 0.0],
            '5.6' => [0.0, 0.5, 0.0, 0.0],
            '5.7' => [0.0, 0.4, 0.0, 0.0],
            '5.8' => [0.0, 0.3, 0.0, 0.0],
            '5.9' => [0.0, 0.2, 0.0, 0.0],
        ];
    }

    /**
     * Indeks zawartości C dla użytków zielonych
     */
    public static function get_carbon_index( string $carbon_class ): int {
        $map = [
            'c_below_2_5'  => 0,
            'c_2_6_to_5'   => 1,
            'c_5_1_to_10'  => 2,
            'c_above_10'   => 3,
        ];
        return $map[ $carbon_class ] ?? 1; // domyślnie: 2,6-5,0%
    }

    /**
     * Lookup dawki CaO — grunty orne
     *
     * @return array|null [total, part1, part2] lub null jeśli brak danych
     */
    public static function lookup_arable( string $soil_category, string $ph ): ?array {
        $data = self::get_arable_doses();
        return $data[ $soil_category ][ $ph ] ?? null;
    }

    /**
     * Lookup dawki CaO — użytki zielone
     *
     * @return array|null [total, part1, part2] lub null
     */
    public static function lookup_grassland( string $ph, string $carbon_class ): ?array {
        $data  = self::get_grassland_doses();
        $index = self::get_carbon_index( $carbon_class );

        if ( ! isset( $data[ $ph ] ) ) {
            return null;
        }

        $dose = $data[ $ph ][ $index ];

        if ( $dose <= 0 ) {
            return [0.0, 0.0, 0.0];
        }

        // Użytki zielone — brak podziału dawki w tabeli IUNG
        return [ $dose, $dose, 0.0 ];
    }

    /**
     * Dostępne wartości pH dla danej kategorii gleby (grunty orne)
     */
    public static function get_ph_range_arable( string $soil_category ): array {
        $data = self::get_arable_doses();
        if ( ! isset( $data[ $soil_category ] ) ) {
            return [];
        }
        $keys = array_keys( $data[ $soil_category ] );
        // Sortuj malejąco (najwyższe pH najpierw)
        usort( $keys, fn( $a, $b ) => (float) $b <=> (float) $a );
        return $keys;
    }

    /**
     * Dostępne wartości pH dla użytków zielonych
     */
    public static function get_ph_range_grassland(): array {
        $keys = array_keys( self::get_grassland_doses() );
        usort( $keys, fn( $a, $b ) => (float) $b <=> (float) $a );
        return $keys;
    }

    /**
     * Kategorie agronomiczne gleby — labele
     */
    public static function get_soil_categories(): array {
        return [
            'bardzo_lekka' => 'Bardzo lekka (piasek luźny, 0-10% frakcji &lt;0,02 mm)',
            'lekka'        => 'Lekka (piasek gliniasty, 11-20% frakcji &lt;0,02 mm)',
            'srednia'      => 'Średnia (glina lekka, 21-35% frakcji &lt;0,02 mm)',
            'ciezka'       => 'Ciężka (glina średnia/ciężka, &gt;35% frakcji &lt;0,02 mm)',
        ];
    }

    /**
     * Klasy zawartości C — labele
     */
    public static function get_carbon_classes(): array {
        return [
            'c_below_2_5' => '&lt; 2,5% C (gleba mineralna, niska zawartość próchnicy)',
            'c_2_6_to_5'  => '2,6 – 5,0% C (gleba mineralna, średnia zawartość próchnicy)',
            'c_5_1_to_10' => '5,1 – 10,0% C (gleba mineralna, wysoka zawartość próchnicy)',
            'c_above_10'  => '&gt; 10% C (gleba organiczna)',
        ];
    }
}
