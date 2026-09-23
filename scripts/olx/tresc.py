#!/usr/bin/env python3
"""Poprawki treści wystawionych ogłoszeń OLX — punktowe podmiany w tytule i opisie (T-142, T-143)
oraz zmiana produktu w miejscu (T-146). Audyt 23.09.2026: docs/raporty/2026-09-OLX_AUDYT.md.

Treść NIE jest składana od nowa z build_adverts.py: opisy na koncie różnią się między seriami
(seria C „w niskiej cenie”, sekcja naboru łódzkiego, tytuły z „, AGRIA”), więc regeneracja
cofnęłaby cudze zmiany. Zamiast tego: GET → putable() → podmiana dokładnych fraz → PUT.
Każda reguła musi trafić — fraza, której nie ma w ogłoszeniu, zatrzymuje to ogłoszenie.

    tresc.py --dry-run                 co się zmieni (odczyt z konta, zero zapisu)
    tresc.py --pilot N | --all         T-142 + T-143
    tresc.py --t146 --dry-run|--pilot N|--all    8 × Mg granulowane → węglanowe granulowane
    tresc.py --sprawdz                 odczyt per ogłoszenie: status, telefon, stare frazy

Po każdym PUT aktualizowane są posted.json (title) i adverts-payload.json (title, description,
a przy T-146 cały wpis) — inaczej `post_adverts.py --update` cofnąłby poprawki.
"""
import json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from post_adverts import call, putable, load_posted, save_posted, moderation_check, D  # noqa: E402
from przeloz import sprawdz_ladunek as _sprawdz  # noqa: E402


def sprawdz_ladunek(body, aid):
    """Jak w przeloz.py, bez reguły o district_id — przy zmianie treści ogłoszenie zostaje w tym samym
    mieście, a w 7 dużych miastach dzielnica jest WYMAGANA (bez niej HTTP 400)."""
    return [b for b in _sprawdz(body, aid) if not b.startswith("district_id")]

PAYLOAD = os.path.join(D, "adverts-payload.json")
BACKUP = os.path.join(HERE, "..", "..", "data", "backups", "olx-tresc-przed-2026-09-23.json")
DATA = "2026-09-23"
PAUZA, GUARD = 2, 25

# T-142: sekcja naboru łódzkiego w ogłoszeniach przełożonych poza łódzkie (T-106/T-139).
LODZKIE_POZA = {1092690340, 1092695461, 1092695809, 1092696116, 1092696176}
LODZKIE_RE = re.compile(r"\n\nNABÓR W WOJEWÓDZTWIE ŁÓDZKIM\n[^\n]*regulamin naboru\.")

# T-143: tabela parametrów wg kart po T-136 (tabele 1:1 z kart PDF producentów), render 23.09.
# (pole, stara fraza, nowa fraza); pole = "title" | "description".
A70 = [
    ("description", "• Typ reakcji: Egzotermiczna\n", "• Typ reakcji: Szybka (egzotermiczna)\n"),
    ("description", "• Zastosowanie funkcjonalne: Odkażania wody i dna stawu, Odkwaszanie gleb średnich "
                    "i ciężkich, podniesienie pH, poprawa struktury gleby",
                    "• Zastosowanie: Odkwaszanie gleb, korekta pH stawów, sadownictwo"),
    ("description", "• Dodatkowe zastosowanie: Przyspieszenie mineralizacji mułu stawowego, Rekultywacja "
                    "terenów zdegradowanych", "• Dodatkowe zastosowanie: Sadownictwo, hurtownie rolnicze"),
]
TLENKOWE_90 = [
    ("description", "odkażania wody i dna stawu, Szybkie odkwaszanie gleb kwaśnych",
                    "neutralizacja, odkwaszanie interwencyjne"),
    ("description", "• Dodatkowe zastosowanie: Gleby bardzo kwaśne (pH < 5), intensywna hodowla ryb, "
                    "neutralizacja ścieków przemysłowych",
                    "• Dodatkowe zastosowanie: Stabilizacja pH przed rekultywacją"),
]
REGULY = {
    "agrobielik-70-gleba": A70,
    # decyzja Janka 23.09: „do stawu” wyrównane do karty — karta mówi o korekcie pH stawów,
    # nie o odkażaniu dna ani mineralizacji mułu; szybkość na karcie 2–4 tygodnie
    "agrobielik-70-staw": A70 + [
        ("title", "odkażanie dna i podniesienie pH wody", "korekta pH wody w stawie"),
        ("description", "Podnosi pH wody, odkaża dno i przyspiesza mineralizację mułu, zwiększając "
                        "pojemność użytkową stawu. Reakcja egzotermiczna — działanie widoczne w 2–3 tygodnie.",
                        "Podnosi pH wody w stawie. Reakcja egzotermiczna — działanie widoczne w 2–4 tygodnie."),
    ],
    "agrobielik-90": TLENKOWE_90 + [
        ("description", "• Zastosowanie funkcjonalne: higienizacja i stabilizacja osadów ściekowych, ",
                        "• Zastosowanie: Higienizacja osadów, "),
        ("description", ", 40–60 kg/1000 m³ (stawy)", ""),
        ("description", "• Szybkość działania: Bardzo szybkie (7-14 dni)",
                        "• Szybkość działania: Bardzo szybkie, 2–4 dni (0–3 mm) · szybkie, 7–14 dni (2–8 mm)"),
    ],
    "oxyfertil-90": TLENKOWE_90 + [
        ("description", "• Reaktywność: ~100%", "• Reaktywność: Bardzo wysoka"),
        ("description", "• Zastosowanie funkcjonalne: Higienizacja i stabilizacja osadów ściekowych, ",
                        "• Zastosowanie: Higienizacja osadów, "),
        ("description", "• Dawkowanie: 1-3 t/ha (rolnictwo), 40-60 kg/1000 m³ (stawy), 20-40% suchej masy osadu",
                        "• Dawkowanie: 20–40% suchej masy osadu, 1–3 t/ha (rolnictwo)"),
        ("description", "• Szybkość działania: Bardzo szybkie (7-14 dni)", "• Szybkość działania: Szybkie (7–14 dni)"),
    ],
    "weglanowe-granulowane": [
        ("description", "• Producent: Grankal, Lhoist\n", "• Producent: Grankal, Lhoist, Celiny (Hochel Group)\n"),
    ],
    "weglanowe-odmiana-04": [
        ("description", "Celiny(Hochcel Group)", "Celiny (Hochel Group)"),
    ],
}

# T-146: 8 ogłoszeń węglanowego z Mg granulowanego (0,33 odsłony numeru / 100 ogł. / dobę, 0 kontaktów
# każde) → węglanowe granulowane (1,48). W żadnym z tych miast nie stoi węglanowe granulowane.
T146 = [1092688834, 1092695960, 1092696271, 1092696372, 1092696210, 1092695988, 1092696339, 1092696045]
OBRAZY_T146 = [("weglanowe-magnez-granulowane", "weglanowe-granulowane"),
               ("granulowane-z-magnezem", "granulowane-bez-magnezu"),
               ("mini4-wapno-magnezowe-", "mini4-wapno-granulowane-")]
V_DIR = os.path.expanduser("~/domains/auratest.pl/public_html/agria-olx")


def zmiany(ad, wariant):
    """Lista reguł do zastosowania; None + powód, gdy któraś fraza nie trafia."""
    reg = [(p, s, n) for p, s, n in REGULY.get(wariant, [])]
    if ad["id"] in LODZKIE_POZA:
        reg.append(("description", "__LODZKIE__", ""))
    return reg


def zastosuj(body, reguly):
    for pole, stara, nowa in reguly:
        if stara == "__LODZKIE__":
            if not LODZKIE_RE.search(body["description"]):
                return f"brak sekcji naboru łódzkiego"
            body["description"] = LODZKIE_RE.sub("", body["description"])
            continue
        if stara not in body[pole]:
            return f"fraza nie trafia w {pole}: {stara[:50]!r}"
        body[pole] = body[pole].replace(stara, nowa)
    return None


def wczytaj():
    reg = load_posted()
    payload = json.load(open(PAYLOAD, encoding="utf-8"))
    backup = json.load(open(BACKUP, encoding="utf-8")) if os.path.exists(BACKUP) else {}
    return reg, payload, backup


def zapisz(reg, payload, backup):
    save_posted(reg)
    json.dump(payload, open(PAYLOAD, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.makedirs(os.path.dirname(BACKUP), exist_ok=True)
    json.dump(backup, open(BACKUP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def put_i_sprawdz(aid, body, oczekiwane):
    code, resp = call("PUT", f"/partner/adverts/{aid}", dict(body, auto_extend_enabled=True))
    if code not in (200, 201):
        return None, f"PUT HTTP {code}: {json.dumps(resp, ensure_ascii=False)[:300]}"
    code, resp = call("GET", f"/partner/adverts/{aid}")
    po = resp.get("data", {}) if code == 200 else {}
    bledy = []
    if not (po.get("contact") or {}).get("phone"):
        bledy.append("BRAK TELEFONU — WYCOFAĆ")
    for pole, wartosc in oczekiwane.items():
        if po.get(pole) != wartosc:
            bledy.append(f"{pole} na koncie inny niż wysłany")
    if po.get("location", {}).get("city_id") != body["location"]["city_id"]:
        bledy.append("city_id się zmienił")
    return po, "; ".join(bledy)


def cmd_tresc(limit, dry):
    reg, payload, backup = wczytaj()
    by_aid = {v["advert_id"]: k for k, v in reg.items()}
    pidx = {p["external_id"]: p for p in payload}
    todo = [(aid, k) for aid, k in by_aid.items()
            if reg[k]["wariant"] in REGULY or aid in LODZKIE_POZA]
    todo = [(a, k) for a, k in todo if reg[k].get("tresc") != DATA][:limit]
    print(f"do poprawy: {len(todo)} ogłoszeń{' (dry-run)' if dry else ''}\n")
    ok = 0
    for i, (aid, klucz) in enumerate(todo):
        if i and not dry:
            time.sleep(PAUZA)
        code, resp = call("GET", f"/partner/adverts/{aid}")
        if code != 200:
            print(f"  BŁĄD {aid} GET HTTP {code}")
            continue
        stan = resp["data"]
        body = putable(stan)
        blad = zastosuj(body, zmiany(stan, reg[klucz]["wariant"]))
        if blad:
            print(f"  POMIJAM {aid} {reg[klucz]['wariant']} {reg[klucz]['city']}: {blad}")
            continue
        if len(body["title"]) > 150:
            print(f"  POMIJAM {aid}: tytuł {len(body['title'])} > 150 znaków")
            continue
        braki = sprawdz_ladunek(body, aid)
        if braki:
            print(f"  POMIJAM {aid}: {'; '.join(braki)}")
            continue
        if dry:
            ok += 1
            continue
        backup.setdefault(str(aid), stan)
        po, bledy = put_i_sprawdz(aid, body, {"title": body["title"], "description": body["description"]})
        print(f"  {'OK  ' if not bledy else 'UWAGA'} {aid} {reg[klucz]['wariant']:<28} {reg[klucz]['city']:<20}"
              f" {po.get('status') if po else ''} {bledy}")
        if po is None or "TELEFONU" in bledy:
            zapisz(reg, payload, backup)
            sys.exit("STOP — ogłoszenie bez PUT albo bez telefonu")
        reg[klucz].update(title=body["title"], tresc=DATA)
        if klucz in pidx:
            pidx[klucz].update(title=body["title"], description=body["description"])
        zapisz(reg, payload, backup)
        ok += 1
        if ok % GUARD == 0:
            zle = moderation_check(reg)
            if zle:
                sys.exit(f"STOP — moderacja wstrzymała {len(zle)}: {zle}")
            print(f"  … bezpiecznik: {ok}, zero odrzutów")
    print(f"\n{'do wysłania' if dry else 'poprawione'}: {ok}/{len(todo)}")


def obrazy_t146(images):
    out = []
    for i in images:
        u = i["url"]
        for a, b in OBRAZY_T146:
            u = u.replace(a, b)
        plik = u.split("/agria-olx/", 1)[-1] if "/agria-olx/" in u else None
        if plik and not os.path.exists(os.path.join(V_DIR, plik)):
            raise RuntimeError(f"brak pliku {plik}")
        out.append({"url": u})
    return out


def front_t146(city_id, payload, reg):
    """Front z puli big bagów (T-138) — scena, której nie ma żadne węglanowe granulowane w promieniu
    100 km (ten sam napis + ta sama scena nie może się powtarzać, reguła z T-138)."""
    from fronty_v5 import BB_SC, scena, km
    miasta = {c["id"]: (c["latitude"], c["longitude"])
              for c in json.load(open(os.path.join(D, "cities-all.json"), encoding="utf-8"))}
    zajete = [(scena(p["images"][0]["url"]), p["location"]["city_id"]) for p in payload
              if reg.get(p["external_id"], {}).get("wariant") == "weglanowe-granulowane"]

    def kara(s):
        return sum(max(0.0, 1 - km(miasta[city_id], miasta[c]) / 100) for sc, c in zajete if sc == s)
    s = min(BB_SC, key=lambda s: (kara(s), BB_SC.index(s)))
    return f"https://auratest.pl/agria-olx/v4/agria-mini4-wapno-granulowane-{s}.jpg"


def cmd_t146(limit, dry):
    reg, payload, backup = wczytaj()
    by_aid = {v["advert_id"]: k for k, v in reg.items()}
    pidx = {p["external_id"]: p for p in payload}
    # wzorzec treści: żywe ogłoszenie węglanowego granulowanego, już po T-143, bez sekcji regionalnej
    wz = next(k for k, v in reg.items() if v["wariant"] == "weglanowe-granulowane"
              and v.get("tresc") == DATA and "ŁÓDZKIM" not in pidx[k]["description"])
    code, resp = call("GET", f"/partner/adverts/{reg[wz]['advert_id']}")
    wzor = putable(resp["data"])
    todo = [a for a in T146 if a in by_aid and reg[by_aid[a]]["wariant"] == "weglanowe-magnez-granulowane"][:limit]
    print(f"T-146: {len(todo)} ogłoszeń, wzorzec treści {reg[wz]['advert_id']}{' (dry-run)' if dry else ''}\n")
    for i, aid in enumerate(todo):
        if i and not dry:
            time.sleep(PAUZA)
        stary = by_aid[aid]
        code, resp = call("GET", f"/partner/adverts/{aid}")
        stan = resp["data"]
        body = putable(stan)
        for pole in ("title", "description", "price", "attributes"):
            body[pole] = wzor[pole]
        if stary not in pidx:
            print(f"  POMIJAM {aid}: brak w adverts-payload.json (galeria z auratest nieznana)")
            continue
        body["images"] = obrazy_t146(pidx[stary]["images"])
        body["images"][0] = {"url": front_t146(body["location"]["city_id"], payload, reg)}
        nowy = f"agria-weglanowe-granulowane-{body['location']['city_id']}"
        if nowy in reg:
            nowy += "-b"
        body["external_id"] = nowy
        braki = sprawdz_ladunek(body, aid)
        if braki:
            print(f"  POMIJAM {aid}: {'; '.join(braki)}")
            continue
        print(f"  {'PLAN' if dry else '...'} {aid} {reg[stary]['city']:<20} → {nowy}  front {body['images'][0]['url'].rsplit('/', 1)[-1]}")
        if dry:
            reg[nowy] = dict(reg[stary], wariant="weglanowe-granulowane")
            payload.append(dict(body, external_id=nowy))
            continue
        backup.setdefault(str(aid), stan)
        po, bledy = put_i_sprawdz(aid, body, {"title": body["title"], "external_id": nowy})
        print(f"  {'OK  ' if not bledy else 'UWAGA'} {aid} {po.get('status') if po else ''} {bledy}")
        if po is None or "TELEFONU" in bledy:
            zapisz(reg, payload, backup)
            sys.exit("STOP")
        wpis = dict(reg.pop(stary), wariant="weglanowe-granulowane", sku="AGR-008", title=body["title"],
                    poprzedni_external_id=stary, zmiana_produktu=DATA, tresc=DATA)
        reg[nowy] = wpis
        stary_p = pidx.get(stary, {})
        payload[:] = [p for p in payload if p["external_id"] != stary]
        meta = dict(stary_p.get("_meta", {}), karta="weglanowe-granulowane", sku="AGR-008",
                    siatka="weglanowe-granulowane", city=wpis["city"])
        payload.append(dict(body, _meta=meta))
        zapisz(reg, payload, backup)
    if not dry:
        zle = moderation_check(reg)
        print("kontrola moderacji:", "zero odrzutów" if not zle else zle)


def cmd_sprawdz():
    reg = load_posted()
    stare = ["ŁÓDZKIM", "intensywna hodowla ryb", "Hochcel", "odkaża dno", "mineralizacji mułu",
             "Odkażania wody i dna stawu", "odkażania wody i dna stawu"]
    zle, n = [], 0
    for k, v in reg.items():
        code, resp = call("GET", f"/partner/adverts/{v['advert_id']}")
        d = resp.get("data", {})
        n += 1
        tekst = (d.get("title") or "") + d.get("description", "")
        problemy = [s for s in stare if s in tekst and not (s == "ŁÓDZKIM" and v["advert_id"] not in LODZKIE_POZA)]
        if d.get("status") != "active" or not (d.get("contact") or {}).get("phone") or problemy \
                or not d.get("auto_extend_enabled"):
            zle.append((v["advert_id"], d.get("status"), (d.get("contact") or {}).get("phone"), problemy))
    print(f"sprawdzone {n}, z problemem {len(zle)}")
    for z in zle:
        print("  !!", z)


if __name__ == "__main__":
    a = sys.argv[1:]
    lim = int(a[a.index("--pilot") + 1]) if "--pilot" in a else None
    dry = "--dry-run" in a
    if "--sprawdz" in a:
        cmd_sprawdz()
    elif "--t146" in a and (dry or lim or "--all" in a):
        cmd_t146(lim, dry)
    elif dry or lim or "--all" in a:
        cmd_tresc(lim, dry)
    else:
        sys.exit(__doc__)
