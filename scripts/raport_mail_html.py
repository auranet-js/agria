#!/usr/bin/env python3
"""Mail z raportem AGRII: .md -> HTML w stylu wysłanego raportu sierpniowego (mail ID 292, Outlook).

Wzór wyglądu: Roboto, #1A1A1A, akapity z odstępem 9,6 pt, nagłówki sekcji pogrubione z dwukropkiem,
pogrubione kluczowe liczby, listy <ul>, pogrubione „Razem”, link do rozpiski pogrubiony.

Składnia źródła: akapity oddzielone pustą linią; linia „## Tekst:” = nagłówek sekcji;
linie „* ” = lista; **…** = pogrubienie; sam URL w akapicie = link.

Użycie: raport_mail_html.py docs/raporty/2026-09-mail.md > out.html
"""
import html, re, sys

P = "<p style=\"margin:0 0 9.6pt 0\"><span style=\"font-family:Roboto,Arial,sans-serif;color:#1A1A1A\">{}</span></p>"
LI = "<li style=\"color:#1A1A1A;margin:2.4pt 0\"><span style=\"font-family:Roboto,Arial,sans-serif\">{}</span></li>"


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"(https?://[^\s*<]+)", r'<a href="\1" style="color:#0563C1">\1</a>', t)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def render(src):
    out = []
    for blok in re.split(r"\n\s*\n", src.strip()):
        linie = blok.splitlines()
        if linie[0].startswith("## "):
            out.append(P.format("<strong>" + inline(linie[0][3:]) + "</strong>"))
            linie = linie[1:]
            if not linie:
                continue
        if all(l.startswith("* ") for l in linie):
            out.append("<ul style=\"margin-top:0\" type=disc>" + "".join(LI.format(inline(l[2:])) for l in linie) + "</ul>")
        else:
            out.append(P.format("<br>".join(inline(l) for l in linie)))
    return ("<html><head><meta charset=\"utf-8\"></head><body style=\"font-family:Roboto,Arial,sans-serif;"
            "font-size:11pt;color:#1A1A1A\">" + "\n".join(out) + "</body></html>")


if __name__ == "__main__":
    print(render(open(sys.argv[1], encoding="utf-8").read()))
