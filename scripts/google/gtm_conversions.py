#!/usr/bin/env python3
"""GTM eventy KONWERSJI dla AGRIA container GTM-TDC85TQN (252883347, ws 3).

Dodaje do istniejacej konfiguracji (Consent + GA4 + 4 base events) eventy
specyficzne dla katalogu B2B "zapytaj o oferte" (brak transakcji online):

Triggery:
- Click - Telefon (tel:)   linkClick, Click URL startsWith tel:
- Click - Email (mailto:)  linkClick, Click URL startsWith mailto:
- Form Success - Elementor elementVisibility na .elementor-message-success
                           (Elementor Pro = AJAX, natywny Form Submit zawodny;
                            lapiemy komunikat sukcesu pojawiajacy sie po AJAX)

Tagi (GA4 event, gaawe, ref "GA4 - Google Tag"):
- GA4 Event - Phone Click    -> phone_click
- GA4 Event - Email Click    -> email_click
- GA4 Event - Generate Lead  -> generate_lead  (GLOWNA konwersja: wyslany formularz)

Idempotentny: skip jesli element o danej nazwie juz istnieje. NIE publikuje —
zmiany laduja w workspace 3. Publikacja: gtm_publish.py po akceptacji.

Uwaga GA4: oznaczenie phone_click / email_click / generate_lead jako "kluczowe
zdarzenia" (konwersje) robi sie w GA4 Admin (osobno) — GTM tylko wysyla eventy.

Run: python3 ~/projekty/agria/scripts/google/gtm_conversions.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import api

ACCOUNT = "6356149706"
CONTAINER = "252883347"
BASE = "https://tagmanager.googleapis.com"
CONTAINER_PATH = f"/tagmanager/v2/accounts/{ACCOUNT}/containers/{CONTAINER}"
WORKSPACE_NAME = "M1 - eventy konwersji"


def step(title):
    print(f"\n=== {title} ===")


def find_by_name(items, key, name):
    for it in items:
        if it.get(key) == name:
            return it
    return None


def get_or_create_workspace():
    """Workspace 3 jest 'submitted' (zablokowany po publikacji v3).
    Znajdz lub utworz dedykowany workspace na eventy konwersji."""
    wss = api("GET", BASE, f"{CONTAINER_PATH}/workspaces").get("workspace", [])
    found = find_by_name(wss, "name", WORKSPACE_NAME)
    if found:
        print(f"Workspace istnieje: '{WORKSPACE_NAME}' (id={found['workspaceId']})")
        return found["workspaceId"]
    r = api("POST", BASE, f"{CONTAINER_PATH}/workspaces", {
        "name": WORKSPACE_NAME,
        "description": "Eventy konwersji M1: phone_click, email_click, generate_lead (T-176).",
    })
    if "error" in r:
        print(f"ERR create workspace: HTTP {r.get('code')}: {r.get('error')[:400]}")
        sys.exit(1)
    print(f"Workspace utworzony: '{WORKSPACE_NAME}' (id={r['workspaceId']})")
    return r["workspaceId"]


step("Workspace")
WORKSPACE = get_or_create_workspace()
WS_PATH = f"{CONTAINER_PATH}/workspaces/{WORKSPACE}"


def link_click_trigger(name, url_prefix, notes):
    return {
        "name": name,
        "type": "linkClick",
        "parameter": [
            {"type": "boolean", "key": "waitForTags", "value": "false"},
            {"type": "boolean", "key": "checkValidation", "value": "false"},
        ],
        "filter": [
            {
                "type": "startsWith",
                "parameter": [
                    {"type": "template", "key": "arg0", "value": "{{Click URL}}"},
                    {"type": "template", "key": "arg1", "value": url_prefix},
                ],
            },
        ],
        "notes": notes,
    }


TRIGGERS = [
    link_click_trigger(
        "Click - Telefon", "tel:",
        "Klik w numer telefonu (link tel:). Sygnal lead B2B.",
    ),
    link_click_trigger(
        "Click - Email", "mailto:",
        "Klik w adres email (link mailto:). Sygnal lead B2B.",
    ),
    {
        "name": "Form Success - Elementor",
        "type": "elementVisibility",
        "parameter": [
            {"type": "template", "key": "selectorType", "value": "CSS"},
            {"type": "template", "key": "elementSelector", "value": ".elementor-message-success"},
            {"type": "template", "key": "firingFrequency", "value": "ONCE_PER_ELEMENT"},
            {"type": "boolean", "key": "useOnScreen", "value": "true"},
            {"type": "template", "key": "onScreenRatio", "value": "50"},
            {"type": "boolean", "key": "useDomChangeListener", "value": "true"},
        ],
        "notes": (
            "Pojawienie sie komunikatu sukcesu formularza Elementor Pro "
            "(.elementor-message-success) po wyslaniu AJAX. useDomChangeListener=true "
            "bo komunikat jest wstrzykiwany dynamicznie. To glowna konwersja agria.pl."
        ),
    },
]

step("Triggery konwersji")
existing_triggers = api("GET", BASE, f"{WS_PATH}/triggers").get("trigger", [])
trigger_ids = {}
for trg in TRIGGERS:
    found = find_by_name(existing_triggers, "name", trg["name"])
    if found:
        trigger_ids[trg["name"]] = found["triggerId"]
        print(f"SKIP {trg['name']} (exists, id={found['triggerId']})")
        continue
    r = api("POST", BASE, f"{WS_PATH}/triggers", trg)
    if "error" in r:
        print(f"ERR {trg['name']}: HTTP {r.get('code')}: {r.get('error')[:600]}")
    else:
        trigger_ids[trg["name"]] = r["triggerId"]
        print(f"OK {trg['name']} -> {r['triggerId']}")
        if trg["type"] == "elementVisibility":
            print("  [pełna odpowiedź elementVisibility do walidacji schematu:]")
            print("  " + json.dumps(r, ensure_ascii=False)[:900])


def ga4_event_params(name, params_dict):
    event_params_list = []
    for k, v in params_dict.items():
        event_params_list.append({
            "type": "map",
            "map": [
                {"type": "template", "key": "name", "value": k},
                {"type": "template", "key": "value", "value": v},
            ],
        })
    return [
        {"type": "tagReference", "key": "measurementId", "value": "GA4 - Google Tag"},
        {"type": "template", "key": "eventName", "value": name},
        {"type": "list", "key": "eventParameters", "list": event_params_list},
    ]


TAGS = [
    {
        "name": "GA4 Event - Phone Click",
        "parameter": ga4_event_params("phone_click", {
            "link_url": "{{Click URL}}",
            "link_text": "{{Click Text}}",
        }),
        "trigger_name": "Click - Telefon",
        "notes": "Event phone_click — klik w numer telefonu.",
    },
    {
        "name": "GA4 Event - Email Click",
        "parameter": ga4_event_params("email_click", {
            "link_url": "{{Click URL}}",
        }),
        "trigger_name": "Click - Email",
        "notes": "Event email_click — klik w adres email.",
    },
    {
        "name": "GA4 Event - Generate Lead",
        "parameter": ga4_event_params("generate_lead", {
            "method": "elementor_form",
        }),
        "trigger_name": "Form Success - Elementor",
        "notes": "Event generate_lead — udane wyslanie formularza (glowna konwersja).",
    },
]

step("Tagi GA4 (eventy konwersji)")
existing_tags = api("GET", BASE, f"{WS_PATH}/tags").get("tag", [])
for tag in TAGS:
    if find_by_name(existing_tags, "name", tag["name"]):
        print(f"SKIP {tag['name']} (exists)")
        continue
    tid = trigger_ids.get(tag["trigger_name"])
    if not tid:
        print(f"ERR {tag['name']}: trigger '{tag['trigger_name']}' niedostepny (patrz wyzej)")
        continue
    body = {
        "name": tag["name"],
        "type": "gaawe",
        "parameter": tag["parameter"],
        "firingTriggerId": [tid],
        "tagFiringOption": "oncePerEvent",
        "notes": tag.get("notes", ""),
    }
    r = api("POST", BASE, f"{WS_PATH}/tags", body)
    if "error" in r:
        print(f"ERR {tag['name']}: HTTP {r.get('code')}: {r.get('error')[:600]}")
    else:
        print(f"OK {tag['name']} -> {r.get('tagId')}")


step("Stan workspace po zmianach")
finals = api("GET", BASE, f"{WS_PATH}/tags").get("tag", [])
print(f"Tagi: {len(finals)}")
for t in finals:
    print(f"  - {t['name']} (type={t['type']})")
trgs = api("GET", BASE, f"{WS_PATH}/triggers").get("trigger", [])
print(f"Triggery: {len(trgs)}")
for t in trgs:
    print(f"  - {t['name']} (type={t['type']}, id={t['triggerId']})")
