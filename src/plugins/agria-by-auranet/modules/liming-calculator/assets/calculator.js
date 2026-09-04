/**
 * AGRIA Kalkulator wapnowania — Frontend JS
 * Vanilla JS, zero zależności
 *
 * Od T-044 (04.09.2026) także moduł magnezowy: kroki 3b–3d, ocena zasobności
 * i dobór dwuetapowy (najpierw magnez, potem dopokrycie wapnem bez magnezu).
 * Liczenie po stronie PHP — tu tylko obsługa pól i render.
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
    var step3mg      = document.getElementById('agria-step3-mg');
    var mgEnable     = document.getElementById('agria-mg-enable');
    var mgInputWrap  = document.getElementById('agria-mg-input-wrap');
    var mgInput      = document.getElementById('agria-mg');
    var step3mgSoil  = document.getElementById('agria-step3-mg-soil');
    var mgSoil       = document.getElementById('agria-mg-soil');
    var step3mgTgt   = document.getElementById('agria-step3-mg-target');
    var mgTarget     = document.getElementById('agria-mg-target');
    var mgTargetHint = document.getElementById('agria-mg-target-hint');
    var step4        = document.getElementById('agria-step4');
    var areaInput    = document.getElementById('agria-area');
    var stepSubmit   = document.getElementById('agria-step-submit');
    var submitBtn    = document.getElementById('agria-calc-submit');
    var loader       = document.getElementById('agria-calc-loader');
    var results      = document.getElementById('agria-calc-results');
    var caoBox       = document.getElementById('agria-cao-box');
    var zeroResult   = document.getElementById('agria-calc-zero');
    var mgBox        = document.getElementById('agria-mg-box');
    var mgProdBox    = document.getElementById('agria-mg-products');
    var resetBtn     = document.getElementById('agria-calc-reset');

    if (!usageType) return; // shortcode nie załadowany

    // --- Helpers ---

    function show(el) { if (el) el.classList.remove('agria-calc__step--hidden'); }
    function hide(el) { if (el) el.classList.add('agria-calc__step--hidden'); }

    function populatePhSelect(values) {
        phSelect.innerHTML = '<option value="">Wybierz</option>';
        values.forEach(function (ph) {
            var opt = document.createElement('option');
            opt.value = ph;
            opt.textContent = ph.replace('.', ',');
            phSelect.appendChild(opt);
        });
    }

    function formatNumber(num, decimals) {
        var d = (decimals === undefined) ? 2 : decimals;
        return parseFloat(num).toFixed(d).replace('.', ',');
    }

    function toFloat(val) {
        var n = parseFloat(String(val).replace(',', '.'));
        return isNaN(n) ? null : n;
    }

    // Grupa mechaniczna gleby do oceny Mg: orne biorą ją z kroku 2, zielone z 3c
    function mgGroup() {
        return usageType.value === 'grunty_orne' ? soilCategory.value : mgSoil.value;
    }

    // --- Step logic ---

    usageType.addEventListener('change', function () {
        var val = this.value;

        // Reset downstream
        hide(step2Arable);
        hide(step2Grass);
        hide(step3);
        hide(step3mg);
        hide(step3mgSoil);
        hide(step3mgTgt);
        hide(step4);
        hide(stepSubmit);
        hide(results);
        soilCategory.value = '';
        carbonClass.value = '';
        phSelect.value = '';
        mgInput.value = '';
        mgSoil.value = '';
        mgTarget.value = '';
        mgEnable.checked = false;
        hide(mgInputWrap);

        if (val === 'grunty_orne') {
            show(step2Arable);
        } else if (val === 'uzytki_zielone') {
            show(step2Grass);
        }
    });

    // Checkbox Mg — zaznaczenie odsłania pole z wartością minimalną
    mgEnable.addEventListener('change', function () {
        if (this.checked) {
            show(mgInputWrap);
            if (mgInput.value === '') {
                mgInput.value = mgInput.getAttribute('min') || '0';
            }
            mgInput.dispatchEvent(new Event('input'));
            mgInput.focus();
            mgInput.select();
        } else {
            mgInput.value = '';
            hide(mgInputWrap);
            hide(step3mgSoil);
            hide(step3mgTgt);
        }
    });

    // Grunty orne — wybór kategorii → pokaż pH
    soilCategory.addEventListener('change', function () {
        var cat = this.value;
        hide(step4);
        hide(stepSubmit);
        hide(results);
        phSelect.value = '';

        if (cat && data.phRanges && data.phRanges[cat]) {
            populatePhSelect(data.phRanges[cat]);
            show(step3);
            show(step3mg);
        } else {
            hide(step3);
            hide(step3mg);
        }

        updateTargetField();
    });

    // Użytki zielone — wybór C → pokaż pH
    carbonClass.addEventListener('change', function () {
        var val = this.value;
        hide(step4);
        hide(stepSubmit);
        hide(results);
        phSelect.value = '';

        if (val && data.phGrassland) {
            populatePhSelect(data.phGrassland);
            show(step3);
            show(step3mg);
        } else {
            hide(step3);
            hide(step3mg);
        }
    });

    // Wybór pH → pokaż pole areału i przycisk
    phSelect.addEventListener('change', function () {
        hide(results);

        if (this.value) {
            show(step4);
            show(stepSubmit);
        } else {
            hide(step4);
            hide(stepSubmit);
        }
    });

    // Pole celu: widoczne gdy wpisano Mg i znamy grupę gleby
    function updateTargetField() {
        var group = mgGroup();
        var ranges = data.mgRanges || {};

        if (mgInput.value === '' || !group || !ranges[group]) {
            hide(step3mgTgt);
            return;
        }

        var r = ranges[group];

        // Blokada zbadanej zawartości: maksimum dla tej gleby (górna granica "wysokiej")
        mgInput.setAttribute('max', r.max);
        var mgVal = toFloat(mgInput.value);
        if (mgVal !== null && mgVal > r.max) {
            mgInput.value = String(r.max);
        }

        mgTarget.setAttribute('min', r.min);
        mgTarget.setAttribute('max', r.max);

        // Domyślnie górna granica "wysokiej"; wcześniejszy wybór przytnij do zakresu
        var cur = toFloat(mgTarget.value);
        if (cur === null || cur < r.min || cur > r.max) {
            mgTarget.value = String(r.max);
        }

        var groupLabel = (data.mgGroups && data.mgGroups[group]) ? data.mgGroups[group].toLowerCase() : '';
        mgTargetHint.textContent = 'Proponowany cel dla gleby „' + groupLabel + '": ' +
            formatNumber(r.max, 1) + ' mg/100 g (górna granica zawartości wysokiej). ' +
            'Możesz obniżyć — minimum to ' + formatNumber(r.min, 1) + ' mg/100 g (dolna granica zawartości średniej).';

        show(step3mgTgt);
    }

    // Mg wpisany przy użytkach zielonych → poproś o grupę gleby
    mgInput.addEventListener('input', function () {
        if (usageType.value === 'uzytki_zielone' && this.value !== '') {
            show(step3mgSoil);
        } else {
            hide(step3mgSoil);
        }
        updateTargetField();
    });

    mgSoil.addEventListener('change', updateTargetField);

    // --- AJAX submit ---

    submitBtn.addEventListener('click', function () {
        var usage = usageType.value;
        var ph    = phSelect.value;

        if (!usage || !ph) return;

        var mgDeclared = mgEnable.checked && mgInput.value !== '';

        var payload = {
            action: 'agria_calc_liming',
            nonce: data.nonce,
            usage_type: usage,
            ph: ph,
            soil_category: usage === 'grunty_orne' ? soilCategory.value : '',
            carbon_content: usage === 'uzytki_zielone' ? carbonClass.value : '',
            mg_value: mgDeclared ? mgInput.value : '',
            mg_soil_group: mgDeclared ? mgSoil.value : '',
            mg_target: mgDeclared ? mgTarget.value : ''
        };

        // UI state
        hide(stepSubmit);
        hide(results);
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

            renderResults(response.data, parseFloat(areaInput.value) || 1);
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
        usageType.dispatchEvent(new Event('change'));
        areaInput.value = '1';
        scrollToEl(document.getElementById('agria-liming-calc'));
    }

    resetBtn.addEventListener('click', doReset);

    // --- Render ---

    function renderResults(d, area) {
        renderCaOBox(d, area);
        renderMg(d, area);
        renderProducts(d, area);
    }

    // Blok dawki CaO albo informacja, że wapnowanie jest zbędne
    function renderCaOBox(d, area) {
        if (d.cao_dose <= 0) {
            hide(caoBox);
            show(zeroResult);
            return;
        }

        hide(zeroResult);
        show(caoBox);

        document.getElementById('agria-result-dose').textContent = formatNumber(d.cao_dose);

        var totalEl = document.getElementById('agria-result-total');
        if (area !== 1) {
            totalEl.innerHTML = '&#10132; Łącznie na <strong>' + formatNumber(area) + ' ha</strong>: ' +
                '<strong>' + formatNumber(d.cao_dose * area) + ' t CaO</strong>';
        } else {
            totalEl.innerHTML = '';
        }

        var splitEl = document.getElementById('agria-result-split');
        if (d.part_2 > 0) {
            splitEl.innerHTML =
                '&#9888; <strong>Podział dawki:</strong> ' +
                'Część I: ' + formatNumber(d.part_1) + ' t CaO/ha &nbsp;|&nbsp; ' +
                'Część II: ' + formatNumber(d.part_2) + ' t CaO/ha (w drugim, trzecim roku)';
        } else {
            splitEl.innerHTML = '';
        }
    }

    // Ocena zasobności w magnez + tabela doboru Mg-first
    function renderMg(d, area) {
        hide(mgBox);
        hide(mgProdBox);

        var mg = d.mg;
        if (!mg) return;

        var badge = document.getElementById('agria-mg-badge');
        var note  = document.getElementById('agria-mg-note');
        var sub   = document.getElementById('agria-mg-sub');
        var line  = document.getElementById('agria-mg-dose-line');

        // Użytki zielone bez wskazanej grupy gleby
        if (mg.no_group) {
            show(mgBox);
            badge.textContent = 'Brak oceny';
            badge.className = 'agria-calc__mg-badge agria-calc__mg-badge--bwysoka';
            hide(line);
            note.textContent = 'Aby ocenić zasobność w magnez, wskaż grupę mechaniczną gleby (krok 3c).';
            sub.textContent = '';
            return;
        }

        show(mgBox);
        badge.textContent = mg.class;
        badge.className = 'agria-calc__mg-badge agria-calc__mg-badge--' + mg.key;

        if (!mg.needs) {
            hide(line);
            if (mg.key === 'wysoka' || mg.key === 'bwysoka') {
                note.textContent = 'Zawartość magnezu ' + mg.class.toLowerCase() +
                    ' — nie stosuj nawozów magnezowych. Do wapnowania wybierz wapno bez magnezu.';
            } else {
                note.textContent = 'Zbadana zawartość (' + formatNumber(mg.mg, 1) + ' mg/100 g) osiąga już wybrany cel ' +
                    formatNumber(mg.target, 1) + ' mg/100 g — nawożenie magnezem nie jest konieczne. ' +
                    'Przy wapnowaniu możesz wybrać wapno z magnezem, aby utrzymać poziom.';
            }
            sub.textContent = 'Wynik: ' + formatNumber(mg.mg, 1) + ' mg Mg/100 g gleby (gleba: ' +
                mg.group_label.toLowerCase() + ').';
            return;
        }

        show(line);
        document.getElementById('agria-mg-dose').textContent = formatNumber(mg.dose_mg, 0);

        note.innerHTML = 'Zawartość ' + mg.class.toLowerCase() + ' (' + formatNumber(mg.mg, 1) +
            ' mg/100 g przy glebie: ' + mg.group_label.toLowerCase() + '). Aby osiągnąć wybrany cel <strong>' +
            formatNumber(mg.target, 1) + ' mg/100 g</strong>, uzupełnij <strong>' + formatNumber(mg.deficit, 1) +
            ' mg/100 g</strong> — czyli <strong>' + formatNumber(mg.dose_mg, 0) + ' kg czystego Mg/ha</strong> (&asymp; ' +
            formatNumber(mg.dose_mgo, 0) + ' kg MgO/ha).';

        sub.textContent = 'Na całe pole (' + formatNumber(area) + ' ha): ' + formatNumber(mg.dose_mg * area, 0) +
            ' kg Mg ≈ ' + formatNumber(mg.dose_mgo * area, 0) + ' kg MgO. Przelicznik: +1 mg Mg/100 g = 30 kg Mg/ha. ' +
            'Zakres celu dla tej gleby: ' + formatNumber(mg.range.min, 1) + '–' + formatNumber(mg.range.max, 1) + ' mg/100 g.';

        renderMgProducts(d, area);
    }

    function renderMgProducts(d, area) {
        if (!d.mg_products || d.mg_products.length === 0) return;

        var tbl = document.getElementById('agria-mg-products-tbl');
        var topup = d.cao_topup || { name: 'wapno bez magnezu', cao_pct: 0 };
        var needCaO = d.cao_dose;

        var html = '<thead><tr>' +
            '<th>Nawóz (od najwyższej zawartości MgO)</th>' +
            '<th>MgO</th><th>CaO</th>' +
            '<th>Dawka wg Mg*<br>[t/ha]</th>' +
            '<th>CaO pokryte tą dawką<br>[t CaO/ha]</th>' +
            '<th>CaO do dopokrycia<br>[t CaO/ha]</th>' +
            '<th>Krok 2: + ' + escHtml(topup.name) + '<br>[t/ha]</th>' +
            '</tr></thead><tbody>';

        d.mg_products.forEach(function (p) {
            html += '<tr>' +
                '<td><a href="' + escHtml(p.url) + '" class="agria-calc__product-link" target="_blank">' + escHtml(p.name) + '</a>' +
                (p.declaration ? '<span class="agria-calc__mg-decl">' + escHtml(p.declaration) + '</span>' : '') + '</td>' +
                '<td class="num">' + p.mgo_pct + '%</td>' +
                '<td class="num">' + p.cao_pct + '%</td>' +
                '<td class="num"><strong>' + formatNumber(p.dose_by_mg) + '</strong></td>' +
                '<td class="num">' + formatNumber(p.cao_given) + (needCaO > 0 ? ' z ' + formatNumber(needCaO) : '') + '</td>' +
                '<td class="num">' + (needCaO > 0
                    ? (p.cao_left > 0 ? formatNumber(p.cao_left) : '<span class="agria-calc__mg-ok">pokryte ✓</span>')
                    : '—') + '</td>' +
                '<td class="num">' + (p.cao_left > 0 ? '<strong>' + formatNumber(p.topup) + '</strong>' : '—') + '</td>' +
                '</tr>';
        });

        html += '</tbody>';
        tbl.innerHTML = html;

        var mg = d.mg;
        var noteText = '* Kolejność doboru: dawkę nawozu magnezowego ustala niedobór Mg (' +
            formatNumber(mg.dose_mg, 0) + ' kg Mg/ha ≈ ' + formatNumber(mg.dose_mgo, 0) + ' kg MgO/ha). ';

        noteText += needCaO > 0
            ? 'Potrzeba wapnowania wg IUNG: ' + formatNumber(needCaO) + ' t CaO/ha — jeśli nawóz magnezowy jej nie domyka, ' +
              'różnicę uzupełnij wapnem bez magnezu (przeliczono na ' + topup.name +
              (topup.cao_pct > 0 ? '; 1 t CaO = ' + formatNumber(1 / (topup.cao_pct / 100)) + ' t nawozu' : '') + ').'
            : 'Wapnowanie przy tym pH nie jest wymagane — stosujesz sam nawóz magnezowy.';

        document.getElementById('agria-mg-products-note').textContent = noteText;

        show(mgProdBox);
    }

    // Klasyczny dobór wg CaO — bez zmian względem wersji sprzed modułu Mg
    function renderProducts(d, area) {
        var productsEl = document.getElementById('agria-result-products');
        productsEl.innerHTML = '';

        if (!d.products || d.products.length === 0) {
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
