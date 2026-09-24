"""Wersja ekranowa: bez spadów, bez pustej strony 2 (była pod druk), obrazy 150 dpi, język sl-SI.
Użycie: python export_web.py sl-vNN.pdf wynik.pdf"""
import sys, pymupdf
d = pymupdf.open(sys.argv[1])
d.delete_page(1)
for p in d:
    p.set_cropbox(p.trimbox)
d.rewrite_images(dpi_threshold=200, dpi_target=150, quality=82)
d.set_metadata({'title': 'AGRIA — Apnene in mineralne surovine (katalog)', 'author': 'AGRIA Sp. z o.o.',
                'subject': 'Katalog izdelkov', 'creator': 'AGRIA'})
d.xref_set_key(d.pdf_catalog(), 'Lang', '(sl-SI)')
d.save(sys.argv[2], garbage=4, deflate=True, clean=True)
