#!/usr/bin/env python3
"""Zbiera statystyki ogłoszeń OLX z rejestru: odsłony, odsłony numeru, obserwujący.

    statystyki.py                 podsumowanie na ekran
    statystyki.py --zapisz        dopisuje pomiar do data/olx/statystyki.json (historia)
    statystyki.py --telegram      wysyła podsumowanie Jankowi

Statystyki są KUMULATYWNE od wystawienia — przyrost liczy się z różnicy między pomiarami,
dlatego pomiar zapisujemy z datą i nie nadpisujemy poprzednich.
"""
import json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "..", "data", "olx")
POSTED, HIST = os.path.join(D, "posted.json"), os.path.join(D, "statystyki.json")
API = "https://www.olx.pl/api"


def token():
    return json.load(open(os.path.expanduser(
        "~/domains/auratest.pl/olx-private/agria-tokens.json")))["access_token"]


def stat(v, prob=3):
    """Jedno ogłoszenie. Przy 8 wątkach API gubiło co trzecie zapytanie — stąd powtórki."""
    for i in range(prob):
        r = subprocess.run(["curl", "-sS", "--max-time", "30",
                            "-H", f"Authorization: Bearer {token()}", "-H", "Version: 2.0",
                            f"{API}/partner/adverts/{v['advert_id']}/statistics"],
                           capture_output=True, text=True).stdout
        try:
            d = json.loads(r)["data"]
            return dict(d, advert_id=v["advert_id"], sku=v["sku"], city=v["city"],
                        title=v["title"])
        except Exception:
            time.sleep(1 + i)
    return None


if __name__ == "__main__":
    reg = json.load(open(POSTED, encoding="utf-8"))
    print(f"odpytuję {len(reg)} ogłoszeń…", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=4) as ex:
        wyniki = [w for w in ex.map(stat, reg.values()) if w]
    ods = sum(w["advert_views"] for w in wyniki)
    tel = sum(w["phone_views"] for w in wyniki)
    obs = sum(w["users_observing"] for w in wyniki)
    z_tel = sum(1 for w in wyniki if w["phone_views"])
    top = sorted(wyniki, key=lambda w: -w["phone_views"])[:8]

    linie = [f"OLX AGRIA — pomiar {time.strftime('%d.%m %H:%M')}",
             f"ogłoszeń odpytanych: {len(wyniki)}/{len(reg)} | odsłony: {ods} | "
             f"odsłony numeru: {tel} | obserwujący: {obs}",
             f"ogłoszeń z choć jedną odsłoną numeru: {z_tel}"]
    linie += [f"  {w['phone_views']:>3} tel · {w['advert_views']:>4} odsł · {w['sku']} {w['city']}"
              for w in top if w["phone_views"] or w["advert_views"]]
    tekst = "\n".join(linie)
    print(tekst)

    if "--zapisz" in sys.argv:
        hist = json.load(open(HIST, encoding="utf-8")) if os.path.exists(HIST) else []
        hist.append({"kiedy": time.strftime("%Y-%m-%d %H:%M"), "ogloszen": len(wyniki),
                     "odslony": ods, "telefony": tel, "obserwujacy": obs,
                     "per_ogloszenie": {str(w["advert_id"]): [w["advert_views"], w["phone_views"]]
                                        for w in wyniki}})
        json.dump(hist, open(HIST, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"→ zapisane, pomiarów w historii: {len(hist)}")

    if "--telegram" in sys.argv:
        d = os.path.expanduser("~/secrets/telegram")
        subprocess.run(["curl", "-sS", "-o", "/dev/null",
                        f"https://api.telegram.org/bot{open(d + '/bot-token.txt').read().strip()}/sendMessage",
                        "--data-urlencode", f"chat_id={open(d + '/chat-id.txt').read().strip()}",
                        "--data-urlencode", f"text={tekst}"], check=False)
