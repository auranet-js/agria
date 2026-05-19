// =====================================================================
// AGRIA — DUPLIKACJA STRONY + PODMIANA NA AGROBIELIK 70 (v2)
// Uruchom na OTWARTYM dokumencie z szablonem Dolomitu
// WAZNE: Najpierw USUN strone 2 jesli istnieje z poprzedniej proby!
// =====================================================================

#target indesign

try {

    if (app.documents.length === 0) {
        alert("Otworz najpierw dokument z szablonem!");
        exit();
    }

    var doc = app.activeDocument;
    app.scriptPreferences.measurementUnit = MeasurementUnits.MILLIMETERS;

    // ── DANE PRODUKTU: AGROBIELIK 70 ──

    var PROD = {
        name: "AGROBIELIK 70",
        descHead: "Agrobielik 70: szybka korekta pH gleb i staw\u00F3w",
        shortDesc: "Szybkodzia\u0142aj\u0105ce wapno tlenkowe o reaktywno\u015Bci ~100%, przeznaczone do odkwaszania gleb kwa\u015Bnych, korekty pH staw\u00F3w rybnych i sadownictwa. Efekty widoczne w 2\u20134 tygodnie. Dost\u0119pne luzem (24 t), w big-bagach 1000 kg oraz workach 20 i 40 kg. Dostawy w\u0142asn\u0105 flot\u0105 z magazyn\u00F3w Niedomice i Sitk\u00F3wka. Marka Agrobielik \u2014 od 1989 roku.",
        longDesc: "Agrobielik 70 to flagowy produkt AGRIA z zawarto\u015Bci\u0105 min. 70% CaO i reaktywno\u015Bci\u0105 ~100%. Dzia\u0142a szybko (2\u20134 tygodnie), ale bezpiecznie \u2014 bez ryzyka wypalenia pr\u00F3chnicy na glebach \u015Brednioci\u0119\u017Ckich. Uniwersalne zastosowanie: od wielkopowierzchniowego rolnictwa, przez sadownictwo, po regulacj\u0119 pH staw\u00F3w hodowlanych. Producent: Nordkalk (Sitk\u00F3wka). Marka: Agrobielik.",
        sectionHead: "Szybkie odkwaszanie\ri wzrost plon\u00F3w",
        benefitsHead: "Kluczowe korzy\u015Bci",
        bullets: [
            "Szybka korekta pH \u2014 efekty widoczne w 2\u20134 tygodnie, idealne przed zasiewami wiosennymi i jesiennymi",
            "Uniwersalno\u015B\u0107 zastosowania \u2014 gleby orne, sady, \u0142\u0105ki, stawy rybne, hurtownie agro",
            "Wysoka reaktywno\u015B\u0107 (~100%) \u2014 pe\u0142ne wykorzystanie CaO, minimalne straty",
            "Elastyczno\u015B\u0107 dostaw \u2014 luz 24 t, big-bag 1000 kg, worki 20/40 kg z dw\u00F3ch magazyn\u00F3w",
            "Stabilno\u015B\u0107 parametr\u00F3w \u2014 sta\u0142a jako\u015B\u0107 gwarantowana przez Nordkalk i 35-letnie relacje AGRIA"
        ],
        params: [
            ["Zawarto\u015B\u0107 CaO", "min. 70% CaO"],
            ["Reaktywno\u015B\u0107", "~100%"],
            ["Typ reakcji", "Szybka (egzotermiczna)"],
            ["Forma fizyczna", "Sypkie"],
            ["Frakcja", "0\u20132 mm"],
            ["Zastosowanie", "Odkwaszanie gleb, korekta pH staw\u00F3w, sadownictwo"],
            ["Efekt zastosowania", "Wzrost pH gleby i wody"],
            ["Dawkowanie", "2\u20136 t/ha (rolnictwo), 60\u2013100 kg/1000 m\u00B3 (stawy)"],
            ["Szybko\u015B\u0107 dzia\u0142ania", "Szybkie (2\u20134 tygodnie)"],
            ["Dodatkowe zastosowanie", "Sadownictwo, hurtownie agro"],
            ["Segment", "Rolnictwo, Rybactwo, Sadownictwo, Hurtownie"],
            ["Forma dostawy", "Big-bag 1000 kg, Worek 20 kg, Worek 40 kg, Luz"],
            ["Magazyn", "Niedomice (33-132), Sitk\u00F3wka (26-052)"],
            ["Producent", "Nordkalk"],
            ["Dost\u0119pno\u015B\u0107", "Ca\u0142y rok"]
        ]
    };

    // ══════════════════════════════════════════
    // KROK 1: DUPLIKACJA CALEJ STRONY
    // (zachowuje pozycje wszystkich elementow)
    // ══════════════════════════════════════════

    var srcPage = doc.pages[0];
    var newPage = srcPage.duplicate(LocationOptions.AFTER, srcPage);

    $.writeln(">>> Zduplikowano strone 1 -> strona 2");

    // ══════════════════════════════════════════
    // KROK 2: PODMIANA TEKSTOW NA STRONIE 2
    // ══════════════════════════════════════════

    // Zbierz WSZYSTKIE textFrames na stronie 2 (wlacznie z tymi w grupach)
    var allItems = newPage.allPageItems;
    var textFrames = [];
    for (var i = 0; i < allItems.length; i++) {
        if (allItems[i].constructor.name === "TextFrame") {
            textFrames.push(allItems[i]);
        }
    }

    $.writeln(">>> Strona 2: " + textFrames.length + " ramek tekstowych");

    var replaced = [];

    // Helper: ExtendScript nie ma Array.indexOf
    function inArray(arr, val) {
        for (var x = 0; x < arr.length; x++) {
            if (arr[x] === val) return true;
        }
        return false;
    }

    for (var f = 0; f < textFrames.length; f++) {
        var tf = textFrames[f];
        var content = "";
        try { content = tf.contents; } catch(e) { continue; }

        // NAZWA PRODUKTU
        if (content.indexOf("NAZWA PRODUKTU") !== -1) {
            tf.contents = PROD.name;
            replaced.push("nazwa");
            continue;
        }

        // NAGLOWEK OPISOWY "Dolomit: naturalne odkwaszanie..."
        if (content.indexOf("naturalne odkwaszanie") !== -1) {
            tf.contents = PROD.descHead;
            replaced.push("descHead");
            continue;
        }

        // SEKCJA "Trwale odkwaszanie i regeneracja"
        if (content.indexOf("odkwaszanie") !== -1 && content.indexOf("regeneracja") !== -1) {
            tf.contents = PROD.sectionHead;
            replaced.push("sectionHead");
            continue;
        }

        // KLUCZOWE KORZYSCI (naglowek)
        if (content.indexOf("Kluczowe korzy") !== -1) {
            tf.contents = PROD.benefitsHead;
            replaced.push("benefitsHead");
            continue;
        }

        // BULLET POINTS
        if (content.indexOf("Kompleksowe") !== -1 || content.indexOf("Niezawodno") !== -1) {
            var bulletText = "";
            for (var b = 0; b < PROD.bullets.length; b++) {
                if (b > 0) bulletText += "\r";
                bulletText += PROD.bullets[b];
            }
            tf.contents = bulletText;
            replaced.push("bullets");
            continue;
        }

        // KROTKI OPIS (dwa wystapienia - pod zdjeciem i w opisie)
        if (content.indexOf("d\u0142ugodzia\u0142aj\u0105cy") !== -1) {
            // Pierwsze wystapienie = shortDesc, drugie = longDesc
            if (!inArray(replaced, "shortDesc")) {
                tf.contents = PROD.shortDesc;
                replaced.push("shortDesc");
            } else {
                tf.contents = PROD.longDesc;
                replaced.push("longDesc");
            }
            continue;
        }

        // TABELA (ramka zawierajaca tabele)
        try {
            if (tf.tables.length > 0) {
                var table = tf.tables[0];
                for (var r = 0; r < PROD.params.length; r++) {
                    var rowIdx = r + 1; // +1 bo header row
                    if (rowIdx < table.rows.length) {
                        try {
                            table.rows[rowIdx].cells[0].contents = PROD.params[r][0];
                            table.rows[rowIdx].cells[1].contents = PROD.params[r][1];
                        } catch(e) {}
                    }
                }
                replaced.push("tabela (" + PROD.params.length + " wierszy)");
            }
        } catch(e) {}
    }

    // ── PRZEJDZ NA STRONE 2 ──
    app.activeWindow.activePage = newPage;

    alert(
        "GOTOWE! Strona 2: AGROBIELIK 70\n\n" +
        "Podmieniono:\n  " + replaced.join("\n  ") + "\n\n" +
        "ZROB RECZNIE:\n" +
        "  1. Podmien zdjecie produktu\n" +
        "  2. Wygeneruj nowy QR (agria.pl/agrobielik-70)\n" +
        "  3. Sprawdz czy tekst miesci sie w ramkach"
    );

} catch(err) {
    alert("BLAD: " + err.message + " (linia " + err.line + ")");
}
