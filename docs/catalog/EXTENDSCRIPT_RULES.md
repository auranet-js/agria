# ExtendScript Rules for InDesign — Gotchas & Solutions

## Krytyczne błędy API

### 1. Justification enum
```javascript
// DOBRZE:
Justification.LEFT_ALIGN
Justification.CENTER_ALIGN
Justification.RIGHT_ALIGN
Justification.FULL_JUSTIFY

// ŹLE (nie istnieje):
Justification.LEFT_ALIGNED    // ← BŁĄD
Justification.CENTER_ALIGNED  // ← BŁĄD
```

### 2. Array.indexOf nie istnieje
ExtendScript (ES3) nie ma Array.prototype.indexOf. Użyj helpera:
```javascript
function inArray(arr, val) {
    for (var x = 0; x < arr.length; x++) {
        if (arr[x] === val) return true;
    }
    return false;
}
```
String.prototype.indexOf DZIAŁA normalnie.

### 3. Tworzenie kolorów
NIE przekazuj obiektu w konstruktorze — ustaw właściwości po kolei:
```javascript
// DOBRZE:
var col = doc.colors.add();
col.name = "MojaBarwa";
col.model = ColorModel.PROCESS;
col.space = ColorSpace.CMYK;
col.colorValue = [32, 0, 35, 69];

// ŹLE (może crashować w polskim InDesign):
doc.colors.add({name: "X", model: ColorModel.PROCESS, ...});
```

### 4. Tworzenie stylów akapitowych
```javascript
// DOBRZE:
var ps = doc.paragraphStyles.add();
ps.name = "MojStyl";
applyFont(ps, "Plus Jakarta Sans", "SemiBold");
ps.pointSize = 22;
ps.fillColor = myColor;

// ŹLE:
doc.paragraphStyles.add({name: "X", pointSize: 22, ...});
```

### 5. Przypisywanie fontów
```javascript
function applyFont(style, family, fStyle) {
    try {
        style.appliedFont = app.fonts.itemByName(family + "\t" + fStyle);
    } catch (e) {
        try {
            style.appliedFont = family;
            style.fontStyle = fStyle;
        } catch (e2) {
            // Zostaw domyślny — InDesign pokaże [Missing Font]
        }
    }
}
```

### 6. Nowe linie w tekście
```javascript
// W contents:
tf.contents = "Linia 1\rLinia 2";   // \r = nowy akapit (DOBRZE)
tf.contents = "Linia 1\nLinia 2";   // \n = może nie działać
```

### 7. Facing Pages
```javascript
// Dla katalogu jednostronnego:
doc.documentPreferences.facingPages = false;
// Jeśli true — InDesign robi spready lewo/prawo i content ląduje tylko na lewych
```

### 8. Duplikacja stron (KLUCZOWE)
```javascript
// DOBRZE — zachowuje pozycje WSZYSTKICH elementów:
var newPage = srcPage.duplicate(LocationOptions.AFTER, srcPage);

// ŹLE — gubi pozycje:
var dup = item.duplicate();
dup.move(newPage);
```

### 9. Iterowanie po elementach strony (w tym w grupach)
```javascript
// allPageItems zwraca WSZYSTKIE elementy, również zagnieżdżone w grupach:
var allItems = page.allPageItems;
var textFrames = [];
for (var i = 0; i < allItems.length; i++) {
    if (allItems[i].constructor.name === "TextFrame") {
        textFrames.push(allItems[i]);
    }
}
```

### 10. Tabele w TextFrame
```javascript
// Sprawdź czy ramka zawiera tabelę:
if (tf.tables.length > 0) {
    var table = tf.tables[0];
    // Wiersz 0 = header, wiersze 1+ = dane
    table.rows[1].cells[0].contents = "Parametr";
    table.rows[1].cells[1].contents = "Wartość";
}
```

## Struktura skryptu (szablon)

```javascript
#target indesign

try {
    app.scriptPreferences.measurementUnit = MeasurementUnits.MILLIMETERS;
    
    // ... logika ...
    
    alert("GOTOWE!");
} catch (err) {
    alert("BLAD: " + err.message + " (linia " + err.line + ")");
}
```

## Testowanie
- `$.writeln(">>> log")` — pisze do konsoli ExtendScript
- Globalny try-catch z `err.line` — krytyczne do debugowania
- Alert z postępem po każdej sekcji — pomaga zlokalizować problem

## Polski InDesign
- Menu: Okno → Narzędzia → Skrypty (nie File → Scripts)
- Panel Skrypty → Użytkownik → prawoklik → Odsłoń w Eksploratorze
- Wrzuć .jsx do tego folderu, dwuklik w panelu uruchamia
