"""T-147 — słoweński katalog: podmiana tekstu w PDF do druku z zachowaniem układu.
Użycie: python build.py <PDF-druk-źródłowy> <wynik.pdf>   (potem export_web.py)
Źródło: Drive AGRIA / Agria-katalog-2026-05-13-druk.pdf. Tłumaczenia: tr_final.json (PL -> SL)."""
import json, os, sys
import engine, shadowhook

HERE = os.path.dirname(os.path.abspath(__file__))
engine.SHADOWS = shadowhook.hook
# kreda pastewna: bez wierszy pH i reakcji (błąd w oryginale, decyzja Janka 24.09)
engine.ROW_REMOVE = {17: {'y0': 450, 'y1': 760, 'rows': [479.7, 499.5], 'white': [(44.0, 703.0, 568.5, 724.0)]}}
tr = json.load(open(os.path.join(HERE, 'tr_final.json'), encoding='utf-8'))
iss = engine.rebuild(sys.argv[1], sys.argv[2], tr)
for i in iss:
    print('PRZEPEŁNIENIE', i)
for l in shadowhook.LOG:
    print('CIEŃ', l)
