#!/usr/bin/env python3
"""Przekłada wystawione ogłoszenia OLX na nowe miejscowości wg projektu przelozenie-*.json (T-106).

Zmienia DOKŁADNIE jedno pole zasobu — `location.city_id`. Reszta ładunku odtwarzana jest
z odpowiedzi GET przez `putable()`, nigdy ręcznie: PUT w tym API podmienia cały zasób, więc
pominięte pole kasuje treść. Jedno niedomknięte pole = ogłoszenie bez numeru telefonu, czyli
bez kanału, który daje wszystkie kontakty.

Zmierzone na produkcji 28.08 (ogłoszenie 1092697758, Białobrzegi → Izbicko): HTTP 200, status
`active` natychmiast, `created_at` i `valid_to` bez zmian, `auto_extend_enabled` zostaje,
`left: 0` w pakiecie niezmienione — OLX nie liczy tego jak nowej publikacji.

    przeloz.py --dry-run             podgląd serii, zero ruchu do OLX
    przeloz.py --pilot 3             przełóż N pierwszych i zatrzymaj się
    przeloz.py --all                 przełóż resztę serii A
    przeloz.py --seria-b [--limit N] seria B: zmiana miejscowości I produktu (8 slotów)
    przeloz.py --sprawdz             odczyt per ogłoszenie: czy miasta zgadzają się z projektem

Po każdym udanym PUT skrypt aktualizuje `posted.json` (city, city_id) ORAZ `adverts-payload.json`
(location.city_id, _meta.city). Bez tej drugiej aktualizacji pierwszy `post_adverts.py --update`
cofnąłby wszystkie miejscowości do stanu sprzed przekładki.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import (call, putable, load_posted, save_posted,  # noqa: E402
                          moderation_check, notify, D)

PAYLOAD = os.path.join(D, "adverts-payload.json")
PROJEKT = os.path.join(D, "przelozenie-2026-08-28.json")
BACKUP = os.path.join(HERE, "..", "..", "data", "backups",
                      "T-106-olx-przed-2026-08-28.json")
PAUZA = 2        # s między ogłoszeniami — limitów API nikt nie udokumentował
GUARD = 25       # co tyle sztuk czytamy statusy i przerywamy przy odrzucie moderacji


def wczytaj_projekt(seria="A"):
    """Seria A to sama zmiana miejscowości; B zmienia też produkt i idzie inną ścieżką."""
    p = json.load(open(PROJEKT, encoding="utf-8"))
    return [x for x in p if x["nowe_miasto"]
            and (x["nowy_wariant"] is None if seria == "A" else x["nowy_wariant"])]


def backup_wczytaj():
    if os.path.exists(BACKUP):
        return json.load(open(BACKUP, encoding="utf-8"))
    return {}


def backup_zapisz(b):
    os.makedirs(os.path.dirname(BACKUP), exist_ok=True)
    json.dump(b, open(BACKUP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def sprawdz_ladunek(body, advert_id):
    """Ostatnia bramka przed PUT-em. Pusty telefon albo zero zdjęć = ogłoszenie do wyrzucenia."""
    braki = []
    if not (body.get("contact") or {}).get("phone"):
        braki.append("brak numeru telefonu")
    if not body.get("images"):
        braki.append("brak zdjęć")
    for pole in ("title", "description", "category_id", "price"):
        if not body.get(pole):
            braki.append(f"brak {pole}")
    if len(body.get("description", "")) < 200:
        braki.append("opis krótszy niż 200 znaków")
    if not (body.get("location") or {}).get("city_id"):
        braki.append("brak city_id")
    if body.get("location", {}).get("district_id") is not None:
        braki.append("district_id przecieka do małej miejscowości")
    return braki


def przeloz_jedno(rec, reg, payload_idx, backup):
    aid, cel = rec["advert_id"], rec["nowe_miasto"]
    code, resp = call("GET", f"/partner/adverts/{aid}")
    if code != 200:
        return False, f"GET HTTP {code}"
    stan = resp["data"]
    backup.setdefault(str(aid), stan)          # stan sprzed — zapisujemy raz, przed pierwszą zmianą

    body = putable(stan)
    # putable() bierze z location tylko pola niepuste, ale stary district_id potrafi przeciec
    # przy przenosinach z dużego miasta do gminy — dlatego location budujemy od zera.
    body["location"] = {"city_id": rec["nowy_city_id"]}
    braki = sprawdz_ladunek(body, aid)
    if braki:
        return False, "ładunek odrzucony: " + "; ".join(braki)

    code, resp = call("PUT", f"/partner/adverts/{aid}",
                      dict(body, auto_extend_enabled=True))
    if code not in (200, 201):
        return False, f"PUT HTTP {code}: {json.dumps(resp, ensure_ascii=False)[:300]}"

    # Weryfikacja per ogłoszenie — lista zbiorcza oddaje statusy z opóźnieniem.
    code, resp = call("GET", f"/partner/adverts/{aid}")
    po = resp.get("data", {}) if code == 200 else {}
    if po.get("location", {}).get("city_id") != rec["nowy_city_id"]:
        return False, f"po PUT city_id to {po.get('location', {}).get('city_id')}, nie {rec['nowy_city_id']}"
    if not (po.get("contact") or {}).get("phone"):
        return False, "po PUT ogłoszenie nie ma numeru telefonu — WYCOFAĆ"

    reg[rec["klucz"]].update(city=cel, city_id=rec["nowy_city_id"],
                             poprzednie_miasto=rec["miasto"],
                             przelozone="2026-08-28")
    it = payload_idx.get(rec["klucz"])
    if it is not None:
        it["location"] = {"city_id": rec["nowy_city_id"]}
        it["_meta"]["city"] = cel
    return True, po.get("status")


def cmd_seria(limit):
    projekt = wczytaj_projekt("A")
    reg = load_posted()
    payload = json.load(open(PAYLOAD, encoding="utf-8"))
    payload_idx = {it["external_id"]: it for it in payload}
    backup = backup_wczytaj()

    todo = [r for r in projekt
            if reg.get(r["klucz"], {}).get("city") != r["nowe_miasto"]][:limit]
    if not todo:
        return print("nic do przełożenia — rejestr już zgodny z projektem")
    print(f"przekładam {len(todo)} ogłoszeń (bezpiecznik co {GUARD}, pauza {PAUZA} s)\n")

    ok = 0
    for i, rec in enumerate(todo):
        if i:
            time.sleep(PAUZA)
        udane, info = przeloz_jedno(rec, reg, payload_idx, backup)
        znak = "OK  " if udane else "BŁĄD"
        print(f"  {znak} {rec['advert_id']}  {rec['miasto']:<20} → {rec['nowe_miasto']:<20} {info}")
        if not udane:
            if ok == 0:
                backup_zapisz(backup)
                sys.exit("pierwsze ogłoszenie nie przeszło — przerywam, żeby nie mnożyć błędów")
            continue
        ok += 1
        save_posted(reg)
        json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        backup_zapisz(backup)
        if ok % GUARD == 0:
            zle = moderation_check(reg)
            if zle:
                opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
                notify(f"OLX AGRIA — STOP przy przekładce po {ok} sztukach:\n{opis}")
                sys.exit(f"STOP — moderacja wstrzymała {len(zle)}:\n{opis}")
            print(f"  … bezpiecznik: {ok} przełożonych, zero odrzutów")

    print(f"\nprzełożone: {ok}/{len(todo)}")
    if ok:
        zle = moderation_check(reg)
        if zle:
            opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
            notify(f"OLX AGRIA — STOP na koniec przekładki ({ok} sztuk):\n{opis}")
            sys.exit(f"STOP — moderacja wstrzymała {len(zle)}:\n{opis}")
        print("kontrola końcowa: zero odrzutów")


def cmd_dry():
    projekt = wczytaj_projekt("A")
    reg = load_posted()
    zrobione = sum(1 for r in projekt if reg.get(r["klucz"], {}).get("city") == r["nowe_miasto"])
    for r in projekt:
        stan = "zrobione" if reg.get(r["klucz"], {}).get("city") == r["nowe_miasto"] else "do zmiany"
        print(f"  [{stan:<9}] {r['advert_id']}  {r['miasto']:<20}{r['km']:>4} km → "
              f"{r['nowe_miasto']:<20}{r['nowy_km']:>4} km  city_id {r['nowy_city_id']}")
    print(f"\nserii A: {len(projekt)} | zrobione: {zrobione} | do zmiany: {len(projekt)-zrobione}")
    print("nic nie zostało wysłane do OLX (--dry-run)")


def cmd_seria_b(limit):
    """Osiem slotów kredy pastewnej: zmiana miejscowości I produktu, czyli pełna podmiana treści.

    Inne ryzyko niż seria A i inna weryfikacja — stąd osobny tryb, nie wspólna pętla. Tutaj PUT
    niesie nowy tytuł, opis, zdjęcia, cenę, atrybuty ORAZ nowy `external_id`: klucz historyczny
    kłamałby o produkcie, bo wariant naprawdę się zmienia. Zachowanie OLX przy zmianie
    `external_id` nie było dotąd mierzone — dlatego pierwsza sztuka idzie sama i jest sprawdzana,
    zanim ruszy reszta.
    """
    ladunki = json.load(open(os.path.join(D, "payload-seria-B-2026-08-28.json"), encoding="utf-8"))
    reg = load_posted()
    payload = json.load(open(PAYLOAD, encoding="utf-8"))
    backup = backup_wczytaj()
    todo = [it for it in ladunki if it["_meta"]["stary_klucz"] in reg][:limit]
    if not todo:
        return print("nic do zrobienia — rejestr nie zna już starych kluczy serii B")
    print(f"seria B: {len(todo)} ogłoszeń, pełna podmiana treści\n")

    ok = 0
    for i, it in enumerate(todo):
        if i:
            time.sleep(PAUZA)
        stary = it["_meta"]["stary_klucz"]
        aid = reg[stary]["advert_id"]
        code, resp = call("GET", f"/partner/adverts/{aid}")
        if code != 200:
            print(f"  BŁĄD {aid} GET HTTP {code}")
            break
        backup.setdefault(str(aid), resp["data"])

        body = {k: v for k, v in it.items() if not k.startswith("_")}
        braki = sprawdz_ladunek(body, aid)
        if braki:
            print(f"  BŁĄD {aid} ładunek: {'; '.join(braki)}")
            break
        code, resp = call("PUT", f"/partner/adverts/{aid}", dict(body, auto_extend_enabled=True))
        if code not in (200, 201):
            print(f"  BŁĄD {aid} PUT HTTP {code}: {json.dumps(resp, ensure_ascii=False)[:300]}")
            break

        code, resp = call("GET", f"/partner/adverts/{aid}")
        po = resp.get("data", {}) if code == 200 else {}
        kontrola = []
        if po.get("external_id") != it["external_id"]:
            kontrola.append(f"external_id na koncie: {po.get('external_id')!r}")
        if po.get("location", {}).get("city_id") != body["location"]["city_id"]:
            kontrola.append(f"city_id: {po.get('location', {}).get('city_id')}")
        if not (po.get("contact") or {}).get("phone"):
            kontrola.append("BRAK TELEFONU — WYCOFAĆ")
        if po.get("title") != it["title"]:
            kontrola.append("tytuł się nie zmienił")
        print(f"  {'OK  ' if not kontrola else 'UWAGA'} {aid}  {reg[stary]['city']:<20} → "
              f"{it['_meta']['city']:<20} {it['_meta']['sku']} {po.get('status')}"
              + ("  | " + "; ".join(kontrola) if kontrola else ""))
        if "BRAK TELEFONU" in " ".join(kontrola):
            break

        wpis = dict(reg.pop(stary), city=it["_meta"]["city"],
                    city_id=body["location"]["city_id"], wariant=it["_meta"]["siatka"],
                    title=it["title"], sku=it["_meta"]["sku"],
                    poprzedni_external_id=stary, przelozone="2026-08-28")
        wpis.pop("uwaga", None)
        reg[it["external_id"]] = wpis
        payload = [p for p in payload if p["external_id"] != stary]
        payload.append({k: v for k, v in it.items() if k != "_meta"}
                       | {"_meta": {k: v for k, v in it["_meta"].items()
                                    if k not in ("stary_klucz", "advert_id")}})
        save_posted(reg)
        json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        backup_zapisz(backup)
        ok += 1

    print(f"\nzrobione: {ok}/{len(todo)}")
    if ok:
        zle = moderation_check(reg)
        if zle:
            opis = "\n".join(f"{a} {s} — {t}" for a, s, t in zle)
            notify(f"OLX AGRIA — STOP w serii B po {ok} sztukach:\n{opis}")
            sys.exit(f"STOP — moderacja wstrzymała {len(zle)}:\n{opis}")
        print("kontrola moderacji: zero odrzutów")


def cmd_sprawdz():
    """Odczyt per ogłoszenie — jedyny wiarygodny; lista zbiorcza oddaje stan z opóźnieniem."""
    projekt = wczytaj_projekt("A") + wczytaj_projekt("B")
    reg = load_posted()
    zgodne, rozjazd = 0, []
    for r in projekt:
        code, resp = call("GET", f"/partner/adverts/{r['advert_id']}")
        if code != 200:
            rozjazd.append((r["advert_id"], f"GET HTTP {code}"))
            continue
        d = resp["data"]
        cid = (d.get("location") or {}).get("city_id")
        tel = (d.get("contact") or {}).get("phone")
        if cid == r["nowy_city_id"] and d.get("status") == "active" and tel:
            zgodne += 1
        else:
            rozjazd.append((r["advert_id"],
                            f"city_id {cid} (oczek. {r['nowy_city_id']}), status {d.get('status')}, tel {tel!r}"))
        # Wpisu szukamy po advert_id, nie po kluczu: seria B zmienia external_id, więc stary
        # klucz nie istnieje już w rejestrze i szukanie po nim dałoby fałszywy rozjazd.
        rej = next((v for v in reg.values() if v["advert_id"] == r["advert_id"]), {})
        if not rej:
            rozjazd.append((r["advert_id"], "brak w rejestrze"))
        elif rej.get("city_id") != cid:
            rozjazd.append((r["advert_id"], f"rejestr mówi {rej.get('city_id')}, OLX {cid}"))
    print(f"zgodnych z projektem: {zgodne}/{len(projekt)}")
    for aid, opis in rozjazd:
        print(f"  !! {aid} {opis}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--dry-run" in args:
        cmd_dry()
    elif "--sprawdz" in args:
        cmd_sprawdz()
    elif "--seria-b" in args:
        lim = int(args[args.index("--limit") + 1]) if "--limit" in args else None
        cmd_seria_b(lim)
    elif "--pilot" in args:
        cmd_seria(int(args[args.index("--pilot") + 1]))
    elif "--all" in args:
        cmd_seria(None)
    else:
        sys.exit(__doc__)
