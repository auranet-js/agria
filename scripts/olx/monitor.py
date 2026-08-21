#!/usr/bin/env python3
"""Codzienna kontrola kanału OLX — statusy, auto_extend, pakiet, statystyki.

Uruchamiany z crona raz dziennie. Cichy, gdy wszystko gra; pisze na Telegram tylko wtedy,
gdy jest o czym mówić (albo z flagą --zawsze).

Alarmuje, gdy:
  • któreś ogłoszenie wypadło z `active` (moderacja, blokada, wygaśnięcie),
  • któremuś zgasł `auto_extend` — to on wygasił konto 18.07,
  • pakiet kończy się w ciągu 7 dni — bez odnowienia gasną WSZYSTKIE ogłoszenia naraz,
  • token OAuth wygasł (żyje 24 h, więc skrypt sam go odświeża przed odczytem).

    monitor.py             kontrola, alarm tylko gdy trzeba
    monitor.py --zawsze    zawsze wyślij podsumowanie
"""
import json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
D = os.path.join(ROOT, "data", "olx")
POSTED = os.path.join(D, "posted.json")
LOG = os.path.join(D, "monitor-log.json")
API = "https://www.olx.pl/api"
PROG_DNI = 7


def token():
    subprocess.run([os.path.expanduser("~/bin/olx-agria"), "refresh"],
                   capture_output=True, text=True)
    return json.load(open(os.path.expanduser(
        "~/domains/auratest.pl/olx-private/agria-tokens.json")))["access_token"]


def api(sciezka, tk):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", "-H", f"Authorization: Bearer {tk}",
                        "-H", "Version: 2.0", API + sciezka], capture_output=True, text=True).stdout
    try:
        return json.loads(r)
    except json.JSONDecodeError:
        return {}


def telegram(tekst):
    d = os.path.expanduser("~/secrets/telegram")
    subprocess.run(["curl", "-sS", "-o", "/dev/null",
                    f"https://api.telegram.org/bot{open(d + '/bot-token.txt').read().strip()}/sendMessage",
                    "--data-urlencode", f"chat_id={open(d + '/chat-id.txt').read().strip()}",
                    "--data-urlencode", f"text={tekst}"], check=False)


def main():
    tk = token()
    reg = json.load(open(POSTED, encoding="utf-8"))
    nasze = {v["advert_id"]: v for v in reg.values()}

    stany, offset = {}, 0
    while True:
        d = api(f"/partner/adverts?limit=100&offset={offset}", tk)
        strona = d.get("data") or []
        stany.update({a["id"]: a for a in strona})
        if len(strona) < 100:
            break
        offset += 100

    zle = [(i, stany[i]["status"], nasze[i]) for i in nasze
           if i in stany and stany[i]["status"] != "active"]
    bez_ae = [(i, nasze[i]) for i in nasze
              if i in stany and not stany[i].get("auto_extend_enabled")]
    brak = [i for i in nasze if i not in stany]

    pakiet = next((p for p in (api("/partner/users/me/packets", tk).get("data") or [])
                   if p.get("size") == 200), None)
    dni = None
    if pakiet:
        koniec = time.mktime(time.strptime(pakiet["active_to"], "%Y-%m-%d %H:%M:%S"))
        dni = int((koniec - time.time()) // 86400)

    alarmy = []
    if zle:
        alarmy.append(f"{len(zle)} ogłoszeń poza statusem active:\n" +
                      "\n".join(f"  {i} {st} — {v['city']} {v['sku']}" for i, st, v in zle[:12]))
    if bez_ae:
        alarmy.append(f"{len(bez_ae)} ogłoszeń bez auto_extend — to on wygasił konto 18.07:\n" +
                      "\n".join(f"  {i} {v['city']} {v['sku']}" for i, v in bez_ae[:12]))
    if brak:
        alarmy.append(f"{len(brak)} ogłoszeń z rejestru nie ma na koncie: {brak[:12]}")
    if dni is not None and dni <= PROG_DNI:
        alarmy.append(f"PAKIET KOŃCZY SIĘ ZA {dni} DNI ({pakiet['active_to']}). "
                      f"Bez odnowienia gasną wszystkie ogłoszenia naraz.")

    naglowek = (f"OLX AGRIA — kontrola {time.strftime('%d.%m %H:%M')}\n"
                f"ogłoszeń w rejestrze: {len(nasze)} | active: {len(nasze) - len(zle) - len(brak)}"
                f" | auto_extend: {len(nasze) - len(bez_ae) - len(brak)}"
                + (f" | pakiet: {dni} dni do końca" if dni is not None else ""))
    tekst = naglowek + ("\n\n" + "\n\n".join(alarmy) if alarmy else "\nWszystko w porządku.")
    print(tekst)

    hist = json.load(open(LOG, encoding="utf-8")) if os.path.exists(LOG) else []
    hist.append({"kiedy": time.strftime("%Y-%m-%d %H:%M"), "w_rejestrze": len(nasze),
                 "poza_active": len(zle), "bez_auto_extend": len(bez_ae),
                 "brak_na_koncie": len(brak), "dni_pakietu": dni})
    json.dump(hist[-180:], open(LOG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    if alarmy or "--zawsze" in sys.argv:
        telegram(tekst)
    return 1 if alarmy else 0


if __name__ == "__main__":
    sys.exit(main())
