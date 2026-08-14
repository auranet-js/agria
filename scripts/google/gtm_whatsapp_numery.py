#!/usr/bin/env python3
"""GTM: pomiar WhatsAppa + rozbicie kliknięć telefonu na numery.

Kontekst (13.08.2026): AGRIA ma dwa główne numery — Paweł 664 393 062
i Kazimierz 781 875 411 — oraz WhatsApp w headerze, który nie był mierzony wcale.
Do tej pory tag "GA4 Event - Phone Click" wysyłał zdarzenie bez informacji,
w który numer kliknięto.

Co robi:
  1. trigger "Click - WhatsApp" (wa.me / api.whatsapp.com)
  2. tag "GA4 Event - WhatsApp Click" -> whatsapp_click (struktura kopiowana
     z istniejącego tagu telefonu, żeby zachować konfigurację GA4)
  3. dokłada do tagu telefonu parametr `phone_number` = {{Click URL}},
     dzięki czemu w GA4 widać rozbicie na numery

Idempotentny. NIE publikuje — zmiany lądują w workspace. Publikacja: gtm_publish.py
"""
import json, os, sys, copy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import api

ACCOUNT = "6356149706"
CONTAINER = "252883347"
BASE = "https://tagmanager.googleapis.com"
CONTAINER_PATH = f"/tagmanager/v2/accounts/{ACCOUNT}/containers/{CONTAINER}"
WORKSPACE_NAME = "M1 - eventy konwersji"
DRY = "--dry-run" in sys.argv


def find_by_name(items, key, name):
    return next((it for it in items if it.get(key) == name), None)


wss = api("GET", BASE, f"{CONTAINER_PATH}/workspaces").get("workspace", [])
ws = find_by_name(wss, "name", WORKSPACE_NAME)
if not ws:
    sys.exit(f"Brak workspace '{WORKSPACE_NAME}' — uruchom najpierw gtm_conversions.py")
WS = f"{CONTAINER_PATH}/workspaces/{ws['workspaceId']}"
print(f"Workspace: {WORKSPACE_NAME} (id={ws['workspaceId']})")

triggers = api("GET", BASE, f"{WS}/triggers").get("trigger", [])
tags = api("GET", BASE, f"{WS}/tags").get("tag", [])

# ── 1. Trigger WhatsApp ───────────────────────────────────────────────────────
print("\n=== Trigger WhatsApp ===")
trg = find_by_name(triggers, "name", "Click - WhatsApp")
if trg:
    print(f"SKIP Click - WhatsApp (exists, id={trg['triggerId']})")
    wa_trigger_id = trg["triggerId"]
else:
    body = {
        "name": "Click - WhatsApp",
        "type": "linkClick",
        "parameter": [
            {"type": "boolean", "key": "waitForTags", "value": "false"},
            {"type": "boolean", "key": "checkValidation", "value": "false"},
        ],
        "filter": [{
            "type": "contains",
            "parameter": [
                {"type": "template", "key": "arg0", "value": "{{Click URL}}"},
                {"type": "template", "key": "arg1", "value": "wa.me"},
            ],
        }],
        "notes": ("Klik w link WhatsApp (wa.me). Kanał asynchroniczny — działa poza "
                  "godzinami pracy 8-16, gdy telefon nie jest odbierany. "
                  "Wzorzec: PrimaAuto ma click_whatsapp jako konwersję główną."),
    }
    if DRY:
        print("DRY:", json.dumps(body, ensure_ascii=False)[:200]); wa_trigger_id = "DRY"
    else:
        r = api("POST", BASE, f"{WS}/triggers", body)
        if "error" in r: sys.exit(f"BŁĄD triggera: {r['error']}")
        wa_trigger_id = r["triggerId"]
        print(f"UTWORZONO Click - WhatsApp (id={wa_trigger_id})")

# ── 2. Tag WhatsApp — struktura kopiowana z tagu telefonu ─────────────────────
print("\n=== Tag WhatsApp ===")
phone_tag = find_by_name(tags, "name", "GA4 Event - Phone Click")
if not phone_tag:
    sys.exit("Brak tagu 'GA4 Event - Phone Click' — nie mam z czego skopiować konfiguracji")

if find_by_name(tags, "name", "GA4 Event - WhatsApp Click"):
    print("SKIP GA4 Event - WhatsApp Click (exists)")
else:
    nowy = copy.deepcopy(phone_tag)
    for k in ("tagId", "fingerprint", "path", "workspaceId", "accountId", "containerId"):
        nowy.pop(k, None)
    nowy["name"] = "GA4 Event - WhatsApp Click"
    nowy["firingTriggerId"] = [wa_trigger_id]
    nowy["notes"] = ("Klik w WhatsApp. Kanał całodobowy — łapie zapytania spoza godzin "
                     "pracy, których telefon nie obsłuży.")
    for p in nowy.get("parameter", []):
        if p.get("key") == "eventName":
            p["value"] = "whatsapp_click"
    if DRY:
        print("DRY:", json.dumps(nowy, ensure_ascii=False)[:300])
    else:
        r = api("POST", BASE, f"{WS}/tags", nowy)
        if "error" in r: sys.exit(f"BŁĄD tagu: {r['error']}")
        print(f"UTWORZONO GA4 Event - WhatsApp Click (id={r['tagId']})")

# ── 3. Rozbicie telefonu na numery ────────────────────────────────────────────
print("\n=== Parametr phone_number w tagu telefonu ===")
params = phone_tag.get("parameter", [])
est = next((p for p in params if p.get("key") == "eventSettingsTable"), None)


def ma_phone_number(tabela):
    for row in tabela.get("list", []):
        for m in row.get("map", []):
            if m.get("key") == "parameter" and m.get("value") == "phone_number":
                return True
    return False


wiersz = {"type": "map", "map": [
    {"type": "template", "key": "parameter", "value": "phone_number"},
    {"type": "template", "key": "parameterValue", "value": "{{Click URL}}"},
]}

if est and ma_phone_number(est):
    print("SKIP — parametr phone_number już jest")
else:
    upd = copy.deepcopy(phone_tag)
    for k in ("fingerprint", "path", "workspaceId", "accountId", "containerId"):
        upd.pop(k, None)
    e2 = next((p for p in upd.get("parameter", []) if p.get("key") == "eventSettingsTable"), None)
    if e2:
        e2.setdefault("list", []).append(wiersz)
    else:
        upd.setdefault("parameter", []).append(
            {"type": "list", "key": "eventSettingsTable", "list": [wiersz]})
    upd["notes"] = ("Klik w numer telefonu. Parametr phone_number niesie kliknięty numer "
                    "(Click URL), żeby w GA4 rozdzielić Pawła 664 393 062 od "
                    "Kazimierza 781 875 411.")
    if DRY:
        print("DRY:", json.dumps(upd, ensure_ascii=False)[:400])
    else:
        r = api("PUT", BASE, f"{WS}/tags/{phone_tag['tagId']}", upd)
        if "error" in r: sys.exit(f"BŁĄD update: {r['error']}")
        print("ZAKTUALIZOWANO GA4 Event - Phone Click (+ phone_number)")

print("\nGOTOWE — zmiany w workspace, NIEOPUBLIKOWANE." if not DRY else "\nDRY-RUN.")
print("Publikacja: python3 scripts/google/gtm_publish.py")
