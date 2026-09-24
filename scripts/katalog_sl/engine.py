"""Podmiana tekstu w PDF katalogu AGRIA z zachowaniem geometrii linii.

extract(pdf) -> lista akapitów (per strona), każdy: styl, linie (x0,x1,baseline), tekst PL.
rebuild(pdf_in, pdf_out, translations) -> usuwa tekst PL i wlewa tłumaczenie w sloty linii.
"""
import json, os, re, statistics, sys
import pymupdf

FONTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts') + os.sep
BAI = {'BaiJamjuree-ExtraLight', 'BaiJamjuree-Light', 'BaiJamjuree-Regular', 'BaiJamjuree-Medium'}
_fonts = {}


def font(name):
    if name not in _fonts:
        _fonts[name] = pymupdf.Font(fontfile=FONTDIR + name + '.ttf')
    return _fonts[name]


def map_font(embedded, size):
    """Nazwa osadzona -> plik pełnego fontu. PJS 'Regular' w PDF to instancje zmiennego fontu."""
    if embedded in BAI:
        return embedded
    if 'Italic' in embedded:
        return 'PlusJakartaSans-Italic'
    return None  # ustalane pomiarem w style_weights()


def span_style(s):
    return (s['font'], round(s['size'], 1), s['color'])


def page_lines(page):
    """Linie tekstu podzielone na runy stylu. Pomija puste i same kropki wypunktowań."""
    out = []
    for b in page.get_text('dict', flags=0)['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            if l['dir'] != (1.0, 0.0):
                continue
            runs = []
            for s in l['spans']:
                if not s['text']:
                    continue
                st = span_style(s)
                if runs and runs[-1]['style'] == st:
                    runs[-1]['text'] += s['text']
                    runs[-1]['bbox'] |= pymupdf.Rect(s['bbox'])
                else:
                    runs.append({'style': st, 'text': s['text'], 'bbox': pymupdf.Rect(s['bbox']),
                                 'origin': s['origin'], 'span': s})
            # scal runy różniące się tylko białymi znakami
            runs = [r for r in runs if r['text'].strip()]
            if not runs:
                continue
            txt = ''.join(r['text'] for r in runs).strip()
            if txt in ('•', '·'):
                continue
            # linie z jednym stylem -> jedna linia; wiele stylów -> każdy run osobno jako "linia"
            if len({r['style'] for r in runs}) == 1:
                r0 = runs[0]
                bb = pymupdf.Rect(runs[0]['bbox'])
                for r in runs[1:]:
                    bb |= r['bbox']
                out.append({'style': r0['style'], 'text': ' '.join(r['text'].strip() for r in runs),
                            'bbox': bb, 'y': r0['origin'][1], 'multi': False})
            else:
                for i, r in enumerate(runs):
                    out.append({'style': r['style'], 'text': r['text'].strip(), 'bbox': r['bbox'],
                                'y': r['origin'][1], 'multi': True, 'run_of': id(l), 'run_idx': i,
                                'lead_ws': r['text'][:1].isspace(), 'trail_ws': r['text'][-1:].isspace()})
    return out


def merge_pieces(lines):
    """Justowane linie PyMuPDF potrafi pociąć na kawałki - sklej te o tej samej bazie i stylu."""
    lines = sorted(lines, key=lambda l: (round(l['y'], 1), l['bbox'].x0))
    out = []
    for l in lines:
        prev = out[-1] if out else None
        if (prev and not l['multi'] and not prev['multi'] and prev['style'] == l['style'] and l['style'][1] > 7
                and not l['text'].startswith('•')
                and abs(prev['y'] - l['y']) < 0.6 and 0 <= l['bbox'].x0 - prev['bbox'].x1 < 3 * l['style'][1]):
            prev['text'] = prev['text'] + ' ' + l['text']
            prev['bbox'] = prev['bbox'] | l['bbox']
        else:
            out.append(l)
    return out


def group_paragraphs(lines):
    lines = merge_pieces(lines)
    lines = sorted(lines, key=lambda l: (l['y'], l['bbox'].x0))
    paras = []
    for l in lines:
        size = l['style'][1]
        best = None
        if not l['multi'] and not l['text'].startswith('•'):
            for p in paras:
                last = p['lines'][-1]
                if p['style'] != l['style'] or last['multi']:
                    continue
                dy = l['y'] - last['y']
                if not (0.9 * size <= dy <= 1.75 * size):
                    continue
                if len(p['lines']) >= 2:
                    lead = p['lines'][-1]['y'] - p['lines'][-2]['y']
                    if abs(dy - lead) > 0.15 * lead:
                        continue
                # poziome pokrycie
                ov = min(last['bbox'].x1, l['bbox'].x1) - max(last['bbox'].x0, l['bbox'].x0)
                if ov < 0.3 * min(last['bbox'].width, l['bbox'].width):
                    continue
                if best is None or last['y'] > best['lines'][-1]['y']:
                    best = p
        if best:
            best['lines'].append(l)
        else:
            paras.append({'style': l['style'], 'lines': [l]})
    for p in paras:
        p['text'] = join_lines([l['text'] for l in p['lines']])
        p['align'] = detect_align(p)
        if p['align'] == 'single' and p['style'][1] <= 7 and p['text'].upper() == p['text']:
            p['force_align'] = 'center'
    # pojedyncza linia nad/pod wyśrodkowanym akapitem o tym samym środku -> też środek
    cen = lambda r: (r.x0 + r.x1) / 2
    for p in paras:
        if p['align'] != 'single' or 'force_align' in p:
            continue
        b = p['lines'][0]['bbox']
        for q in paras:
            if q['align'] == 'center' and any(abs(cen(l['bbox']) - cen(b)) < 3 and abs(l['y'] - p['lines'][0]['y']) < 2.5 * p['style'][1] for l in q['lines']):
                p['force_align'] = 'center'
    return paras


def join_lines(texts):
    out = ''
    for t in texts:
        t = t.strip()
        if not out:
            out = t
        elif re.search(r'[a-ząćęłńóśźż]-$', out) and re.match(r'[a-ząćęłńóśźż]', t):
            out = out[:-1] + t  # przeniesienie wyrazu
        else:
            out += ' ' + t
    return re.sub(r'\s+', ' ', out)


def detect_align(p):
    ls = p['lines']
    if len(ls) == 1:
        return 'single'
    x0 = [l['bbox'].x0 for l in ls]
    x1 = [l['bbox'].x1 for l in ls]
    s0 = max(x0) - min(x0)
    s1 = max(x1) - min(x1)
    if len(ls) >= 3 and max(x0[:-1]) - min(x0[:-1]) < 1.5 and max(x1[:-1]) - min(x1[:-1]) < 1.5:
        return 'justify'
    if s0 < 2 and s1 < 2:
        return 'left'
    if s0 < 2:
        return 'left'
    if s1 < 2:
        return 'right'
    c = [(a + b) / 2 for a, b in zip(x0, x1)]
    if max(c) - min(c) < 3:
        return 'center'
    return 'left'


def extract(path):
    d = pymupdf.open(path)
    pages = []
    for pn, page in enumerate(d):
        paras = group_paragraphs(page_lines(page))
        pages.append(paras)
    return d, pages


# ---------- pomiar grubości PJS ----------
def ink(pix):
    sa = pix.samples
    return sum(255 - sa[i] for i in range(0, len(sa), pix.n)) / (pix.width * pix.height)


def coverage(pix, color):
    """Udział pikseli w kolorze tekstu (0..1), niezależnie od koloru tła."""
    sa, n = pix.samples, pix.n
    tc = [c * 255 for c in color]
    ds = [sum(abs(sa[i + k] - tc[k]) for k in range(3)) for i in range(0, len(sa), n)]
    D = sorted(ds)[int(len(ds) * 0.95)] or 1
    return sum(max(0.0, 1 - d / D) for d in ds) / len(ds)


def measure_weight(page, line):
    r = line['bbox']
    color = pymupdf.sRGB_to_pdf(line['style'][2])
    orig = coverage(page.get_pixmap(dpi=200, clip=r), color)
    best = None
    for w in ['Regular', 'Medium', 'SemiBold', 'Bold', 'ExtraBold']:
        fn = 'PlusJakartaSans-' + w
        try:
            F = font(fn)
        except Exception:
            continue
        nd = pymupdf.open()
        q = nd.new_page(width=r.width * 1.2 + 10, height=r.height)
        q.insert_font(fontname='F', fontfile=FONTDIR + fn + '.ttf')
        q.insert_text((0, line['y'] - r.y0), line['text'], fontname='F', fontsize=line['style'][1], color=(0, 0, 0))
        tw = F.text_length(line['text'], line['style'][1])
        v = ink(q.get_pixmap(dpi=200, clip=pymupdf.Rect(0, 0, r.width, r.height), colorspace=pymupdf.csGRAY)) / 255
        v *= tw / max(r.width, 1)  # normalizacja o tracking
        if best is None or abs(v - orig) < best[0]:
            best = (abs(v - orig), fn)
    return best[1]


def resolve_fonts(doc, pages):
    cache = {}
    for pn, paras in enumerate(pages):
        for p in paras:
            emb = p['style'][0]
            fn = map_font(emb, p['style'][1])
            p['font'] = fn
            if fn is None:
                ln = max(p['lines'], key=lambda l: len(l['text']))
                if len(ln['text']) >= 4:
                    p['font'] = measure_weight(doc[pn], ln)
                    cache.setdefault(p['style'], []).append(p['font'])
    for paras in pages:
        for p in paras:
            if p['text'] in FONT_OVERRIDE:
                p['font'] = FONT_OVERRIDE[p['text']]
                continue
            if not p['style'][0] in BAI and 'Italic' not in p['style'][0]:
                c = cache.get(p['style'])
                p['font'] = max(set(c), key=c.count) if c else 'PlusJakartaSans-Bold'
    return cache


def tracking(p):
    """Stosunek rzeczywistej szerokości do teoretycznej (tracking InDesign)."""
    F = font(p['font'])
    rs = []
    for l in p['lines']:
        tw = F.text_length(l['text'], p['style'][1])
        if tw > 40 and not l.get('multi'):
            rs.append(l['bbox'].width / tw)
    if not rs:
        return 1.0
    return max(0.94, min(1.03, statistics.median(rs)))


# ---------- skład ----------
def wrap(words, slots, F, size, sx):
    """Zachłanne wlewanie słów w sloty (szerokości). Zwraca listę linii lub None przy przepełnieniu."""
    lines, cur, i = [], '', 0
    for w in words:
        width = slots[min(i, len(slots) - 1)]
        cand = (cur + ' ' + w).strip()
        if F.text_length(cand, size) * sx <= width or not cur:
            cur = cand
        else:
            lines.append(cur)
            i += 1
            cur = w
    if cur:
        lines.append(cur)
    return lines


def layout(p, text, sx):
    F = font(p['font'])
    size = p['style'][1]
    ls = p['lines']
    widths = [l['bbox'].width for l in ls]
    maxw = max(widths)
    if len(ls) == 1:
        slots = [widths[0] + p.get('room', 0)]
    elif p['align'] == 'center':
        slots = [maxw * 1.35] * len(ls)
    else:
        slots = [maxw if w < 0.6 * maxw else min(maxw, w + 0.02 * maxw) for w in widths]
        slots[-1] = max(slots[:-1] + [widths[-1]])
    if '\n' in text:  # wymuszone łamanie z pliku tłumaczeń
        return [t.strip() for t in text.split('\n')], size, False
    words = []
    for w in text.split():
        last = words[-1].split('\u00a0')[-1] if words else ''
        if words and (w.startswith('%') or w in ('°C', 'kg', 't', 't/ha', 'mm', 'h', 'dni', 'm³')):
            words[-1] += '\u00a0' + w
        elif len(last) == 1 and last.lower() in 'aiouwzvskh':
            words[-1] += '\u00a0' + w
        else:
            words.append(w)
    for scale in (1.0, 0.97, 0.94, 0.91, 0.88):
        s = size * scale
        out = wrap(words, [w / 1.0 for w in slots], F, s, sx)
        if len(out) <= len(ls) + p.get('extra_lines', 0) and all(F.text_length(t, s) * sx <= slots[min(k, len(slots) - 1)] + 0.5 for k, t in enumerate(out)):
            return out, s, False
    return out, s, True


SHADOWS = None
ROW_REMOVE = {}
FONT_OVERRIDE = {'Pracujemy z najlepszymi producentami': 'PlusJakartaSans-Bold'}
MARGIN_R = 570.0
MARGIN_L = 42.0


def compute_room(page, paras, todo):
    obst = [(pymupdf.Rect(l['bbox']), l.get('run_of')) for q in paras for l in q['lines']]
    for info in page.get_image_info():
        r = pymupdf.Rect(info['bbox'])
        if r.width < page.rect.width * 0.8:  # tła całostronicowe pomijamy
            obst.append((r, None))
    for p in todo:
        ls = p['lines']
        mine = [pymupdf.Rect(l['bbox']) for l in ls]
        ro = ls[0].get('run_of')
        others = [o for o, r in obst if not any(o == m for m in mine) and (ro is None or r != ro)]
        if len(ls) == 1:
            b = ls[0]['bbox']
            band = lambda o: o.y1 > b.y0 + 1 and o.y0 < b.y1 - 1
            right = min([o.x0 for o in others if band(o) and o.x0 >= b.x1 - 1] + [MARGIN_R]) - 5 - b.x1
            left = b.x0 - max([o.x1 for o in others if band(o) and o.x1 <= b.x0 + 1] + [MARGIN_L]) - 5
            align = p['align'] if p['align'] != 'single' else p.get('force_align', 'left')
            if align == 'right':
                room = left
            elif align == 'center':
                room = 2 * min(left, right)
            else:
                room = right
            p['room'] = max(0.0, room)
        else:
            x0 = min(m.x0 for m in mine); x1 = max(m.x1 for m in mine)
            lead = (ls[-1]['y'] - ls[0]['y']) / (len(ls) - 1)
            below = pymupdf.Rect(x0, mine[-1].y1, x1, mine[-1].y1 + lead)
            free = not any(o.intersects(below) for o in others)
            p['extra_lines'] = 1 if free else 0


def rebuild(src, dst, translations, only_pages=None, force=False):
    doc, pages = extract(src)
    resolve_fonts(doc, pages)
    issues = []
    for pn, page in enumerate(doc):
        if only_pages is not None and pn not in only_pages:
            continue
        todo = []
        for p in pages[pn]:
            new = translations.get(p['text'])
            if new is None or (new == p['text'] and not force):
                continue
            todo.append((p, new))
        rr = ROW_REMOVE.get(pn)
        if rr:
            ys = sorted({round(l['y'], 1) for q in pages[pn] for l in q['lines'] if rr['y0'] < l['y'] < rr['y1']})
            pitch = statistics.median([b - a for a, b in zip(ys, ys[1:])])
            inl = {id(p): i for i, (p, _) in enumerate(todo)}
            for q in pages[pn]:
                y = q['lines'][0]['y']
                if not (rr['y0'] < y < rr['y1']):
                    continue
                k = sum(1 for r in rr['rows'] if r < y - 1)
                if any(abs(y - r) < 1 for r in rr['rows']):
                    new = ''
                elif k:
                    new = translations.get(q['text'], q['text'])
                    q['dy'] = -k * pitch
                else:
                    continue
                if id(q) in inl:
                    todo[inl[id(q)]] = (q, new)
                else:
                    todo.append((q, new))
        if not todo:
            continue
        # runy wielostylowe: jeśli jeden run się zmienia, przerysowujemy całą linię
        runs = {p['lines'][0]['run_of'] for p, _ in todo if p['lines'][0].get('multi')}
        inl = {id(p) for p, _ in todo}
        for q in pages[pn]:
            if q['lines'][0].get('multi') and q['lines'][0]['run_of'] in runs and id(q) not in inl:
                todo.append((q, translations.get(q['text'], q['text'])))
        for p, _ in todo:
            for l in p['lines']:
                r = pymupdf.Rect(l['bbox'])
                r.y0 += r.height * 0.2
                r.y1 -= r.height * 0.2
                page.add_redact_annot(r)
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                              text=pymupdf.PDF_REDACT_TEXT_REMOVE)
        for p, _ in todo:
            if p.get('dy'):
                p['lines'] = [dict(l, y=l['y'] + p['dy'], bbox=pymupdf.Rect(l['bbox']) + (0, p['dy'], 0, p['dy'])) for l in p['lines']]
        todo = [(p, n) for p, n in todo if n != '']
        if rr:
            for r in rr.get('white', []):
                page.draw_rect(pymupdf.Rect(r), color=None, fill=(1, 1, 1))
        compute_room(page, pages[pn], [p for p, _ in todo])
        new_of = {id(p): new for p, new in todo}
        # runy wielostylowe: kolejność od lewej, żeby znać koniec poprzedniego
        runs_end = {}
        todo.sort(key=lambda t: (t[0]['lines'][0].get('run_idx', 0)))
        used = {}
        placed = {}
        for p, new in todo:
            placed[id(p)] = []
            fn = p['font']
            if fn not in used:
                used[fn] = 'F%d' % len(used)
                page.insert_font(fontname=used[fn], fontfile=FONTDIR + fn + '.ttf')
            F = font(fn)
            sx = tracking(p)
            out, s, over = layout(p, new, sx)
            if over:
                issues.append((pn + 1, p['text'][:60], len(out), len(p['lines'])))
            color = pymupdf.sRGB_to_pdf(p['style'][2])
            ls = p['lines']
            lead = (ls[-1]['y'] - ls[0]['y']) / (len(ls) - 1) if len(ls) > 1 else p['style'][1] * 1.2
            align = p['align']
            if align == 'single':
                align = p.get('force_align', 'left')
            first = ls[0]
            if len(ls) == 1 and p.get('room'):
                # rozszerzenie slotu w stronę wolnego miejsca
                b = pymupdf.Rect(ls[0]['bbox'])
                if align == 'right':
                    b.x0 -= p['room']
                elif align == 'center':
                    b.x0 -= p['room'] / 2
                    b.x1 += p['room'] / 2
                else:
                    b.x1 += p['room']
                ls = [dict(ls[0], bbox=b)]
            x_shift = 0.0
            if first.get('multi') and first['run_idx'] > 0:
                prev = runs_end.get((first['run_of'], first['run_idx'] - 1))
                if prev is not None:
                    # oryginalna przerwa liczona od widocznego końca poprzedniego runu
                    x_shift = prev[0] - prev[1]
                    if first.get('lead_ws'):
                        x_shift += F.text_length(' ', p['style'][1]) * sx  # przesunięcie końca poprzedniego runu
            for k, t in enumerate(out):
                ref = ls[min(k, len(ls) - 1)]
                y = ref['y'] if k < len(ls) else ls[-1]['y'] + lead * (k - len(ls) + 1)
                t = t.replace('\u00a0', ' ')
                tw = F.text_length(t, s) * sx
                x0, x1 = ref['bbox'].x0 + x_shift, ref['bbox'].x1
                if align == 'justify' and k < len(out) - 1 and ' ' in t:
                    x1 = max(l['bbox'].x1 for l in ls)
                    ws = t.split(' ')
                    gap = (x1 - x0 - sum(F.text_length(w, s) * sx for w in ws)) / (len(ws) - 1)
                    if F.text_length(' ', s) * sx * 0.8 <= gap < F.text_length(' ', s) * sx * 2.2:
                        x = x0
                        for w in ws:
                            page.insert_text((x, y), w, fontname=used[fn], fontsize=s, color=color,
                                             morph=(pymupdf.Point(x, y), pymupdf.Matrix(sx, 1)))
                            x += F.text_length(w, s) * sx + gap
                        continue
                if align == 'right':
                    x = x1 - tw
                elif align == 'center':
                    x = (x0 + x1) / 2 - tw / 2
                else:
                    x = x0
                page.insert_text((x, y), t, fontname=used[fn], fontsize=s, color=color,
                                 morph=(pymupdf.Point(x, y), pymupdf.Matrix(sx, 1)))
                placed[id(p)].append((x, y, t, FONTDIR + fn + '.ttf', s, sx))
                if first.get('multi'):
                    orig_end = p['lines'][0]['bbox'].x1 - (F.text_length(' ', p['style'][1]) if first.get('trail_ws') else 0)
                    runs_end[(first['run_of'], first['run_idx'])] = (x + tw, orig_end)
        if SHADOWS:
            SHADOWS(doc, page, todo, placed)
    doc.save(dst, garbage=3, deflate=True)
    return issues
