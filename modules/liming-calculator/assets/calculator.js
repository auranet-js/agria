/**
 * AGRIA Kalkulator wapnowania — Frontend JS
 * Vanilla JS, zero zależności
 */
(function () {
    'use strict';

    var data = window.agriaCalcData || {};

    // DOM refs
    var usageType    = document.getElementById('agria-usage-type');
    var step2Arable  = document.getElementById('agria-step2-arable');
    var step2Grass   = document.getElementById('agria-step2-grassland');
    var soilCategory = document.getElementById('agria-soil-category');
    var carbonClass  = document.getElementById('agria-carbon-class');
    var step3        = document.getElementById('agria-step3');
    var phSelect     = document.getElementById('agria-ph');
    var step4        = document.getElementById('agria-step4');
    var areaInput    = document.getElementById('agria-area');
    var stepSubmit   = document.getElementById('agria-step-submit');
    var submitBtn    = document.getElementById('agria-calc-submit');
    var loader       = document.getElementById('agria-calc-loader');
    var results      = document.getElementById('agria-calc-results');
    var zeroResult   = document.getElementById('agria-calc-zero');
    var resetBtn     = document.getElementById('agria-calc-reset');
    var resetZeroBtn = document.getElementById('agria-calc-reset-zero');

    if (!usageType) return; // shortcode nie załadowany

    // --- Helpers ---

    function show(el) { el.classList.remove('agria-calc__step--hidden'); }
    function hide(el) { el.classList.add('agria-calc__step--hidden'); }

    function populatePhSelect(values) {
        phSelect.innerHTML = '<option value="">Wybierz</option>';
        values.forEach(function (ph) {
            var opt = document.createElement('option');
            opt.value = ph;
            opt.textContent = ph.replace('.', ',');
            phSelect.appendChild(opt);
        });
    }

    function formatNumber(num) {
        return parseFloat(num).toFixed(2).replace('.', ',');
    }

    // --- Step logic ---

    usageType.addEventListener('change', function () {
        var val = this.value;

        // Reset downstream
        hide(step2Arable);
        hide(step2Grass);
        hide(step3);
        hide(stepSubmit);
        hide(results);
        hide(zeroResult);
        soilCategory.value = '';
        carbonClass.value = '';
        phSelect.value = '';

        if (val === 'grunty_orne') {
            show(step2Arable);
        } else if (val === 'uzytki_zielone') {
            show(step2Grass);
        }
    });

    // Grunty orne — wybór kategorii → pokaż pH
    soilCategory.addEventListener('change', function () {
        var cat = this.value;
        hide(stepSubmit);
        hide(results);
        hide(zeroResult);
        phSelect.value = '';

        if (cat && data.phRanges && data.phRanges[cat]) {
            populatePhSelect(data.phRanges[cat]);
            show(step3);
        } else {
            hide(step3);
        }
    });

    // Użytki zielone — wybór C → pokaż pH
    carbonClass.addEventListener('change', function () {
        var val = this.value;
        hide(stepSubmit);
        hide(results);
        hide(zeroResult);
        phSelect.value = '';

        if (val && data.phGrassland) {
            populatePhSelect(data.phGrassland);
            show(step3);
        } else {
            hide(step3);
        }
    });

    // Wybór pH → pokaż pole areału i przycisk
    phSelect.addEventListener('change', function () {
        hide(results);
        hide(zeroResult);

        if (this.value) {
            show(step4);
            show(stepSubmit);
        } else {
            hide(step4);
            hide(stepSubmit);
        }
    });

    // --- AJAX submit ---

    submitBtn.addEventListener('click', function () {
        var usage = usageType.value;
        var ph    = phSelect.value;

        if (!usage || !ph) return;

        var payload = {
            action: 'agria_calc_liming',
            nonce: data.nonce,
            usage_type: usage,
            ph: ph,
            soil_category: usage === 'grunty_orne' ? soilCategory.value : '',
            carbon_content: usage === 'uzytki_zielone' ? carbonClass.value : ''
        };

        // UI state
        hide(stepSubmit);
        hide(results);
        hide(zeroResult);
        show(loader);

        var formData = new FormData();
        Object.keys(payload).forEach(function (key) {
            formData.append(key, payload[key]);
        });

        fetch(data.ajaxUrl, {
            method: 'POST',
            body: formData
        })
        .then(function (res) { return res.json(); })
        .then(function (response) {
            hide(loader);

            if (!response.success) {
                alert(response.data || 'Błąd obliczenia. Sprawdź parametry.');
                show(stepSubmit);
                return;
            }

            var d = response.data;

            if (d.cao_dose <= 0) {
                show(zeroResult);
                scrollToEl(zeroResult);
                return;
            }

            renderResults(d, parseFloat(areaInput.value) || 1);
            show(results);
            scrollToEl(results);
        })
        .catch(function () {
            hide(loader);
            alert('Błąd połączenia. Spróbuj ponownie.');
            show(stepSubmit);
        });
    });

    // --- Reset ---

    function doReset() {
        usageType.value = '';
        soilCategory.value = '';
        carbonClass.value = '';
        phSelect.value = '';
        areaInput.value = '1';
        hide(step2Arable);
        hide(step2Grass);
        hide(step3);
        hide(step4);
        hide(stepSubmit);
        hide(results);
        hide(zeroResult);
        scrollToEl(document.getElementById('agria-liming-calc'));
    }

    resetBtn.addEventListener('click', doReset);
    resetZeroBtn.addEventListener('click', doReset);

    // --- Render results ---

    function renderResults(d, area) {
        // Dawka CaO
        document.getElementById('agria-result-dose').textContent = formatNumber(d.cao_dose);

        // Łącznie na pole
        var totalEl = document.getElementById('agria-result-total');
        if (area !== 1) {
            var totalCao = d.cao_dose * area;
            totalEl.innerHTML = '&#10132; Łącznie na <strong>' + formatNumber(area) + ' ha</strong>: ' +
                '<strong>' + formatNumber(totalCao) + ' t CaO</strong>';
        } else {
            totalEl.innerHTML = '';
        }

        // Podział dawki
        var splitEl = document.getElementById('agria-result-split');
        if (d.part_2 > 0) {
            splitEl.innerHTML =
                '&#9888; <strong>Podział dawki:</strong> ' +
                'Część I: ' + formatNumber(d.part_1) + ' t CaO/ha &nbsp;|&nbsp; ' +
                'Część II: ' + formatNumber(d.part_2) + ' t CaO/ha';
        } else {
            splitEl.innerHTML = '';
        }

        // Produkty
        var productsEl = document.getElementById('agria-result-products');
        productsEl.innerHTML = '';

        if (!d.products || d.products.length === 0) {
            productsEl.innerHTML = '<p>Brak produktów do wyświetlenia.</p>';
            return;
        }

        // Grupuj po type
        var groups = {};
        d.products.forEach(function (p) {
            var key = p.type || 'inne';
            if (!groups[key]) groups[key] = { label: p.type_label, items: [] };
            groups[key].items.push(p);
        });

        var hasSplit = d.part_2 > 0;
        var showArea = area !== 1;
        var typeOrder = ['tlenkowe', 'mieszanka', 'weglanowe', 'inne'];

        typeOrder.forEach(function (type) {
            var group = groups[type];
            if (!group) return;

            var div = document.createElement('div');
            div.className = 'agria-calc__type-group';

            var label = document.createElement('div');
            label.className = 'agria-calc__type-label';
            label.textContent = group.label;
            div.appendChild(label);

            var table = document.createElement('table');
            table.className = 'agria-calc__table';

            // Header
            var thArea = showArea ? '<th>Łącznie na pole</th>' : '';
            var thead = '<thead><tr>' +
                '<th>Produkt</th>' +
                '<th>CaO</th>' +
                '<th>Dawka [t/ha]</th>' +
                thArea +
                '<th></th>' +
                '</tr></thead>';
            table.innerHTML = thead;

            var tbody = document.createElement('tbody');

            group.items.forEach(function (p, idx) {
                var tr = document.createElement('tr');

                if (idx === 0) {
                    tr.className = 'agria-calc__row--best';
                }

                var doseHtml = formatNumber(p.dose_total);
                if (hasSplit && p.dose_p2 > 0) {
                    doseHtml += '<span class="agria-calc__dose-split">' +
                        'cz. I: ' + formatNumber(p.dose_p1) +
                        ' | cz. II: ' + formatNumber(p.dose_p2) +
                        '</span>';
                }

                var tdArea = '';
                if (showArea) {
                    var totalProduct = p.dose_total * area;
                    tdArea = '<td><strong>' + formatNumber(totalProduct) + ' t</strong></td>';
                }

                var badgeHtml = idx === 0 ? '<span class="agria-calc__badge">Najefektywniejszy</span>' : '';

                tr.innerHTML =
                    '<td><a href="' + escHtml(p.url) + '" class="agria-calc__product-link" target="_blank">' +
                        escHtml(p.name) + '</a>' + badgeHtml + '</td>' +
                    '<td>' + p.cao_pct + '%</td>' +
                    '<td>' + doseHtml + '</td>' +
                    tdArea +
                    '<td><a href="' + escHtml(p.url) + '" class="agria-calc__product-link" target="_blank">Szczegóły →</a></td>';

                tbody.appendChild(tr);
            });

            table.appendChild(tbody);
            div.appendChild(table);
            productsEl.appendChild(div);
        });
    }

    // --- Util ---

    function scrollToEl(el) {
        setTimeout(function () {
            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    }

    function escHtml(str) {
        var div = document.createElement('div');
        div.appendChild(document.createTextNode(str));
        return div.innerHTML;
    }

})();
