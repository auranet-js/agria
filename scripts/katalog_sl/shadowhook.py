import pymupdf, shadows, engine
PARAMS = {}
LOG = []

def hook(doc, page, todo, placed):
    masks = shadows.find_masks(doc, page)
    if not masks:
        return
    groups = {}
    for p, new in todo:
        b = p['lines'][0]['bbox']
        c = pymupdf.Point((b.x0 + b.x1) / 2, (b.y0 + b.y1) / 2)
        for ix, rect, size in masks:
            if c in rect and rect.height < 4.5 * b.height:
                groups.setdefault(ix, (rect, size, []))[2].append(p)
    for ix, (rect, size, ps) in groups.items():
        orig_items = []
        for p in ps:
            sx = engine.tracking(p)
            for l in p['lines']:
                orig_items.append((l['bbox'].x0, l['y'], l['text'], engine.FONTDIR + p['font'] + '.ttf', p['style'][1], sx))
        if 'best' not in PARAMS:
            PARAMS['best'] = shadows.calibrate(doc, ix, rect, size, orig_items)
            LOG.append(('kalibracja', PARAMS['best']))
        _, sigma, dx, dy, gain = PARAMS['best']
        new_items = [it for p in ps for it in placed.get(id(p), [])]
        im = shadows.render_text_mask(rect, size, new_items, sigma, dx, dy, gain)
        shadows.replace_mask(doc, ix, im)
        LOG.append((page.number + 1, [p['text'][:30] for p in ps]))
