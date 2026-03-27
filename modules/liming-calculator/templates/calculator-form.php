<?php
/**
 * Template: Kalkulator wapnowania AGRIA
 * Renderowany przez shortcode [agria_kalkulator_wapnowania]
 *
 * @var array $soil_categories  Kategorie agronomiczne
 * @var array $carbon_classes   Klasy zawartości C
 * @var array $ph_ranges        Zakresy pH per kategoria
 * @var array $ph_grassland     Zakres pH użytki zielone
 */

defined( 'ABSPATH' ) || exit;
?>

<div id="agria-liming-calc" class="agria-calc">

    <div class="agria-calc__header">
        <h2 class="agria-calc__title">Kalkulator wapnowania</h2>
        <p class="agria-calc__subtitle">Oblicz zalecaną dawkę wapna dla Twojej gleby wg metodyki IUNG-PIB Puławy</p>
    </div>

    <div class="agria-calc__form">

        <!-- KROK 1: Rodzaj użytku -->
        <div class="agria-calc__step">
            <label class="agria-calc__label">
                <span class="agria-calc__step-num">Krok 1</span>
                Rodzaj użytku rolnego
            </label>
            <select id="agria-usage-type" class="agria-calc__select">
                <option value="">Wybierz</option>
                <option value="grunty_orne">Grunty orne</option>
                <option value="uzytki_zielone">Użytki zielone</option>
            </select>
        </div>

        <!-- KROK 2A: Kategoria gleby (grunty orne) -->
        <div class="agria-calc__step agria-calc__step--hidden" id="agria-step2-arable">
            <label class="agria-calc__label">
                <span class="agria-calc__step-num">Krok 2</span>
                Kategoria agronomiczna gleby
            </label>
            <select id="agria-soil-category" class="agria-calc__select">
                <option value="">Wybierz</option>
                <?php foreach ( $soil_categories as $key => $label ) : ?>
                    <option value="<?php echo esc_attr( $key ); ?>"><?php echo $label; ?></option>
                <?php endforeach; ?>
            </select>
        </div>

        <!-- KROK 2B: Zawartość C (użytki zielone) -->
        <div class="agria-calc__step agria-calc__step--hidden" id="agria-step2-grassland">
            <label class="agria-calc__label">
                <span class="agria-calc__step-num">Krok 2</span>
                Zawartość węgla organicznego (C) w glebie
            </label>
            <select id="agria-carbon-class" class="agria-calc__select">
                <option value="">Wybierz</option>
                <?php foreach ( $carbon_classes as $key => $label ) : ?>
                    <option value="<?php echo esc_attr( $key ); ?>"><?php echo $label; ?></option>
                <?php endforeach; ?>
            </select>
            <span class="agria-calc__hint">Wartość z badania gleby (OSChR). Jeśli nie znasz — wybierz 2,6–5,0%.</span>
        </div>

        <!-- KROK 3: pH gleby -->
        <div class="agria-calc__step agria-calc__step--hidden" id="agria-step3">
            <label class="agria-calc__label">
                <span class="agria-calc__step-num">Krok 3</span>
                Aktualne zbadane pH gleby
            </label>
            <select id="agria-ph" class="agria-calc__select">
                <option value="">Wybierz</option>
            </select>
        </div>

        <!-- KROK 4: Wielkość działki -->
        <div class="agria-calc__step agria-calc__step--hidden" id="agria-step4">
            <label class="agria-calc__label">
                <span class="agria-calc__step-num">Krok 4</span>
                Wielkość działki (ha)
            </label>
            <input type="number" id="agria-area" class="agria-calc__input" min="0.01" max="9999" step="0.01" value="1" placeholder="np. 12,5">
            <span class="agria-calc__hint">Wpisz powierzchnię pola w hektarach. Domyślnie: 1 ha.</span>
        </div>

        <!-- PRZYCISK -->
        <div class="agria-calc__step agria-calc__step--hidden" id="agria-step-submit">
            <button type="button" id="agria-calc-submit" class="agria-calc__btn">
                Oblicz dawkę
            </button>
        </div>

    </div>

    <!-- LOADER -->
    <div id="agria-calc-loader" class="agria-calc__loader agria-calc__step--hidden">
        <span class="agria-calc__spinner"></span> Obliczam...
    </div>

    <!-- WYNIKI -->
    <div id="agria-calc-results" class="agria-calc__results agria-calc__step--hidden">

        <!-- Dawka CaO -->
        <div class="agria-calc__result-box">
            <div class="agria-calc__result-header">Zalecana dawka</div>
            <div class="agria-calc__result-value">
                <span id="agria-result-dose">0,00</span> t CaO / ha
            </div>
            <div id="agria-result-total" class="agria-calc__result-total"></div>
            <div id="agria-result-split" class="agria-calc__result-split"></div>
            <div class="agria-calc__result-source">
                wg IUNG-PIB Puławy (Jadczyszyn, 2021)
            </div>
        </div>

        <!-- Tabela produktów -->
        <div id="agria-result-products" class="agria-calc__products"></div>

        <!-- Disclaimery -->
        <div class="agria-calc__disclaimer">
            <p>* Dawka nawozu = dawka CaO [t/ha] &divide; (% CaO w nawozie &divide; 100)</p>
            <p>* Jeśli dawka przekracza 4 t na glebach lekkich lub 5 t na ciężkich — należy ją podzielić na 2 aplikacje.</p>
        </div>

        <!-- CTA -->
        <div class="agria-calc__cta">
            <button type="button" id="agria-calc-reset" class="agria-calc__btn agria-calc__btn--outline">
                Oblicz ponownie
            </button>
            <a href="/kontakt/" class="agria-calc__btn">Zapytaj o cenę</a>
        </div>
    </div>

    <!-- Zero dawki -->
    <div id="agria-calc-zero" class="agria-calc__zero agria-calc__step--hidden">
        <div class="agria-calc__result-box agria-calc__result-box--ok">
            <div class="agria-calc__result-header">Wapnowanie zbędne</div>
            <p>Przy aktualnym pH Twojej gleby wapnowanie nie jest konieczne. Zalecamy kontrolne badanie gleby za 3–4 lata.</p>
        </div>
        <div class="agria-calc__cta">
            <button type="button" id="agria-calc-reset-zero" class="agria-calc__btn agria-calc__btn--outline">
                Oblicz ponownie
            </button>
        </div>
    </div>

</div>

<!-- Dane pH per kategoria (do JS) -->
<script>
    var agriaCalcData = {
        ajaxUrl: <?php echo wp_json_encode( admin_url( 'admin-ajax.php' ) ); ?>,
        nonce: <?php echo wp_json_encode( wp_create_nonce( 'agria_calc_nonce' ) ); ?>,
        phRanges: <?php echo wp_json_encode( $ph_ranges ); ?>,
        phGrassland: <?php echo wp_json_encode( $ph_grassland ); ?>
    };
</script>
