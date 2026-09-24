"""Cienie nagłówków: maska luminancji (obraz szary) w SMask ExtGState. Podmieniamy obraz maski."""
import re, io
import pymupdf
from PIL import Image, ImageFilter, ImageChops
import engine


def find_masks(doc, page):
    """[(img_xref, rect_topleft, (w,h))] dla masek z pojedynczym obrazem."""
    out = []
    res = doc.xref_object(page.xref)
    H = page.mediabox.height
    for gx in set(int(x) for x in re.findall(r'/GS\d+ (\d+) 0 R', res)):
        m = re.search(r'/SMask (\d+) 0 R', doc.xref_object(gx))
        if not m:
            continue
        g = re.search(r'/G (\d+) 0 R', doc.xref_object(int(m.group(1))))
        if not g:
            continue
        fx = int(g.group(1))
        st = doc.xref_stream(fx).decode('latin1')
        cm = re.search(r'([-\d.]+) 0 0 ([-\d.]+) ([-\d.]+) ([-\d.]+) cm\s*/(Im\d+) Do', st)
        im = re.search(r'/Im\d+ (\d+) 0 R', doc.xref_object(fx))
        if not cm or not im:
            continue
        a, d, e, f = map(float, cm.groups()[:4])
        ix = int(im.group(1))
        w = int(doc.xref_get_key(ix, 'Width')[1]); h = int(doc.xref_get_key(ix, 'Height')[1])
        rect = pymupdf.Rect(e, H - (f + d), e + a, H - f)
        out.append((ix, rect, (w, h)))
    return out


def render_text_mask(rect, size_px, items, sigma, dx, dy, gain):
    """items: [(x, y, text, fontfile, fontsize, sx)] we współrzędnych strony."""
    w, h = size_px
    doc = pymupdf.open()
    pg = doc.new_page(width=rect.width, height=rect.height)
    pg.draw_rect(pg.rect, color=None, fill=(0, 0, 0))
    for k, (x, y, t, ff, fs, sx) in enumerate(items):
        pg.insert_font(fontname='S%d' % k, fontfile=ff)
        px, py = x - rect.x0 + dx, y - rect.y0 + dy
        pg.insert_text((px, py), t, fontname='S%d' % k, fontsize=fs, color=(1, 1, 1),
                       morph=(pymupdf.Point(px, py), pymupdf.Matrix(sx, 1)))
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(w / rect.width, h / rect.height), colorspace=pymupdf.csGRAY)
    im = Image.frombytes('L', (pix.width, pix.height), pix.samples).resize((w, h))
    im = im.filter(ImageFilter.GaussianBlur(sigma))
    return im.point(lambda v: min(255, int(v * gain)))


def load_mask(doc, ix, size):
    pix = pymupdf.Pixmap(doc, ix)
    if pix.n != 1:
        pix = pymupdf.Pixmap(pymupdf.csGRAY, pix)
    return Image.frombytes('L', (pix.width, pix.height), pix.samples)


def diff(a, b):
    return sum(ImageChops.difference(a, b).getdata())


def calibrate(doc, ix, rect, size, items):
    orig = load_mask(doc, ix, size)
    best = None
    for sigma in (3, 5, 7, 9, 12):
        for dx in (0, 1, 2, 3):
            for dy in (0, 1, 2, 3):
                im = render_text_mask(rect, size, items, sigma, dx, dy, 1.0)
                mo, mi = max(orig.getdata()), max(im.getdata()) or 1
                gain = mo / mi
                im = im.point(lambda v: min(255, int(v * gain)))
                s = diff(orig, im)
                if best is None or s < best[0]:
                    best = (s, sigma, dx, dy, gain)
    return best


def replace_mask(doc, ix, im):
    doc.update_stream(ix, im.tobytes(), compress=True)
    doc.xref_set_key(ix, 'Filter', '/FlateDecode')
    doc.xref_set_key(ix, 'DecodeParms', 'null')
    doc.xref_set_key(ix, 'ColorSpace', '/DeviceGray')
    doc.xref_set_key(ix, 'BitsPerComponent', '8')
