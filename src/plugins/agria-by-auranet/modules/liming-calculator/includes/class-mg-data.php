<?php
/**
 * AGRIA Liming Calculator — dane magnezowe
 *
 * Granice zasobności gleby w magnez wg grupy mechanicznej, przelicznik dawki
 * i ocena niedoboru. Odpowiednik Agria_IUNG_Data po stronie magnezu.
 *
 * Wartości i logika 1:1 z prototypu zaakceptowanego przez K. Nowaka 28.08.2026
 * (mockups/agria-kalkulator-mg-test-2026-08-18.html, zadanie T-043).
 */

defined( 'ABSPATH' ) || exit;

class Agria_Mg_Data {

    /**
     * Granice zasobności [mg Mg / 100 g gleby] wg grupy mechanicznej gleby.
     * Kolejno progi: bardzo niska <= [0], niska <= [1], średnia <= [2],
     * wysoka <= [3], powyżej [3] — bardzo wysoka.
     * Granica "do X" należy do klasy NIŻSZEJ (4,0 na ciężkiej = bardzo niska).
     */
    public const THRESHOLDS = [
        'bardzo_lekka' => [ 1.0, 2.0, 4.0, 6.0 ],
        'lekka'        => [ 2.0, 3.0, 5.0, 7.0 ],
        'srednia'      => [ 3.0, 5.0, 7.0, 9.0 ],
        'ciezka'       => [ 4.0, 6.0, 10.0, 14.0 ],
    ];

    /** +1 mg Mg/100 g gleby = 30 kg czystego Mg/ha */
    public const KG_PER_UNIT = 30;

    /** 1 kg Mg = 1,658 kg MgO (masy molowe 40,304 / 24,305) */
    public const TO_MGO = 40.304 / 24.305;

    /**
     * Etykiety grup mechanicznych (krótkie — do zdań w wynikach)
     */
    public static function get_groups(): array {
        return [
            'bardzo_lekka' => 'Bardzo lekka',
            'lekka'        => 'Lekka',
            'srednia'      => 'Średnia',
            'ciezka'       => 'Ciężka',
        ];
    }

    /**
     * Zakres celu nawożenia dla grupy gleby.
     * min = dolna granica zawartości "średniej" (próg niskiej + 0,1)
     * max = górna granica zawartości "wysokiej" — i to jest wartość domyślna
     */
    public static function target_range( string $group ): ?array {
        if ( ! isset( self::THRESHOLDS[ $group ] ) ) {
            return null;
        }

        $t = self::THRESHOLDS[ $group ];

        return [
            'min' => round( $t[1] + 0.1, 1 ),
            'max' => (float) $t[3],
        ];
    }

    /**
     * Zakresy celu dla wszystkich grup — do przekazania do JS
     */
    public static function get_target_ranges(): array {
        $ranges = [];
        foreach ( array_keys( self::THRESHOLDS ) as $group ) {
            $ranges[ $group ] = self::target_range( $group );
        }
        return $ranges;
    }

    /**
     * Ocena zasobności i dawka magnezu
     *
     * @param string     $group  Grupa mechaniczna gleby
     * @param float      $mg     Zbadana zawartość [mg Mg / 100 g]
     * @param float|null $target Cel nawożenia; null = górna granica "wysokiej"
     * @return array|null
     */
    public static function assess( string $group, float $mg, ?float $target = null ): ?array {
        if ( ! isset( self::THRESHOLDS[ $group ] ) ) {
            return null;
        }

        $t     = self::THRESHOLDS[ $group ];
        $range = self::target_range( $group );

        if ( $mg <= $t[0] ) {
            $class = 'Bardzo niska';
            $key   = 'bniska';
        } elseif ( $mg <= $t[1] ) {
            $class = 'Niska';
            $key   = 'niska';
        } elseif ( $mg <= $t[2] ) {
            $class = 'Średnia';
            $key   = 'srednia';
        } elseif ( $mg <= $t[3] ) {
            $class = 'Wysoka';
            $key   = 'wysoka';
        } else {
            $class = 'Bardzo wysoka';
            $key   = 'bwysoka';
        }

        // Cel: wybrany przez rolnika, przycięty do zakresu; domyślnie górna granica "wysokiej"
        $tgt = ( null === $target ) ? $range['max'] : $target;
        $tgt = round( min( max( $tgt, $range['min'] ), $range['max'] ), 1 );

        $deficit  = max( 0, round( $tgt - $mg, 1 ) );
        $dose_mg  = round( $deficit * self::KG_PER_UNIT, 1 );
        $dose_mgo = round( $dose_mg * self::TO_MGO, 1 );

        return [
            'class'      => $class,
            'key'        => $key,
            'group'      => $group,
            'group_label'=> self::get_groups()[ $group ],
            'mg'         => $mg,
            'target'     => $tgt,
            'range'      => $range,
            'deficit'    => $deficit,
            'dose_mg'    => $dose_mg,
            'dose_mgo'   => $dose_mgo,
            'needs'      => $deficit > 0,
        ];
    }
}
