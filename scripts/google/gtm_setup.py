#!/usr/bin/env python3
"""GTM workspace config for AGRIA container GTM-TDC85TQN (252883347, ws 3).

Wykonuje:
- Enable 14 built-in variables (click + form + scroll)
- User-defined variable: GA4 Measurement ID (Constant) = G-KVFMR3NZDH
- 4 custom triggers: Scroll (25/50/75/90), Outbound Link, File Download, Form Submit
- 6 tags:
    1. Consent Default Denied (Custom HTML, Consent Init trigger)
    2. Google Tag - GA4 Config (googtag, All Pages)
    3. GA4 Event - Scroll
    4. GA4 Event - Outbound Link
    5. GA4 Event - File Download
    6. GA4 Event - Form Submit
- Create version + publish

Idempotentny: skip jesli element o tej nazwie juz istnieje.

Run: python3 ~/projekty/agria/scripts/google/gtm_setup.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import api

ACCOUNT = "6356149706"
CONTAINER = "252883347"
WORKSPACE = "3"
GA4_MEASUREMENT_ID = "G-KVFMR3NZDH"
BASE = "https://tagmanager.googleapis.com"
WS_PATH = f"/tagmanager/v2/accounts/{ACCOUNT}/containers/{CONTAINER}/workspaces/{WORKSPACE}"

# System triggers (built-in, nie wymagaja tworzenia, mozna uzywac w firingTriggerId)
TRIGGER_ALL_PAGES = "2147479553"
TRIGGER_CONSENT_INIT = "2147479572"


def step(title):
    print(f"\n=== {title} ===")


def find_by_name(items, key, name):
    for it in items:
        if it.get(key) == name:
            return it
    return None


# === BUILT-IN VARIABLES ===
step("Enable built-in variables")
TO_ENABLE = [
    "clickElement", "clickClasses", "clickId", "clickTarget", "clickUrl", "clickText",
    "formElement", "formClasses", "formId", "formTarget", "formUrl", "formText",
    "scrollDepthThreshold", "scrollDepthUnits",
]

current_biv = api("GET", BASE, f"{WS_PATH}/built_in_variables")
current_types = {b["type"] for b in current_biv.get("builtInVariable", [])}
print(f"Currently enabled: {sorted(current_types)}")

missing = [t for t in TO_ENABLE if t not in current_types]
if missing:
    # API expects type as repeated query param
    types_qs = "&".join(f"type={t}" for t in missing)
    r = api("POST", BASE, f"{WS_PATH}/built_in_variables?{types_qs}")
    if "error" in r:
        print(f"ERR built-in vars: HTTP {r.get('code')}: {r.get('error')[:200]}")
    else:
        added = [b.get("type") for b in r.get("builtInVariable", [])]
        print(f"Enabled: {added}")
else:
    print("All required built-in vars already enabled")


# === USER-DEFINED VARIABLE: GA4 Measurement ID ===
step("User-defined variable: GA4 Measurement ID")
existing_vars = api("GET", BASE, f"{WS_PATH}/variables").get("variable", [])
if find_by_name(existing_vars, "name", "GA4 Measurement ID"):
    print("SKIP (exists)")
else:
    r = api("POST", BASE, f"{WS_PATH}/variables", {
        "name": "GA4 Measurement ID",
        "type": "c",  # constant
        "parameter": [
            {"type": "template", "key": "value", "value": GA4_MEASUREMENT_ID}
        ],
        "notes": "Hardcoded Measurement ID dla agria.pl GA4 property 538301430.",
    })
    if "error" in r:
        print(f"ERR: HTTP {r.get('code')}: {r.get('error')[:300]}")
    else:
        print(f"OK -> {r.get('variableId')} {r.get('name')}")


# === TRIGGERS ===
step("Custom triggers")
existing_triggers = api("GET", BASE, f"{WS_PATH}/triggers").get("trigger", [])
trigger_ids = {}  # name -> triggerId

TRIGGERS = [
    {
        "name": "Scroll - 25/50/75/90",
        "type": "scrollDepth",
        "parameter": [
            {"type": "boolean", "key": "verticalThresholdOn", "value": "true"},
            {"type": "template", "key": "verticalThresholdsPercent", "value": "25,50,75,90"},
            {"type": "template", "key": "verticalThresholdUnits", "value": "PERCENT"},
            {"type": "template", "key": "horizontalThresholdOn", "value": "false"},
            {"type": "template", "key": "triggerStartOption", "value": "DOM_READY"},
        ],
        "notes": "Scroll depth 25/50/75/90% — base engagement metric.",
    },
    {
        "name": "Outbound Link",
        "type": "linkClick",
        "parameter": [
            {"type": "boolean", "key": "waitForTags", "value": "false"},
            {"type": "boolean", "key": "checkValidation", "value": "false"},
        ],
        "filter": [
            {
                "type": "cssSelector",
                "parameter": [
                    {"type": "template", "key": "arg0", "value": "{{Click Element}}"},
                    {"type": "template", "key": "arg1", "value": "a"},
                ],
            },
            {
                "type": "contains",
                "parameter": [
                    {"type": "template", "key": "arg0", "value": "{{Click URL}}"},
                    {"type": "template", "key": "arg1", "value": "http"},
                ],
            },
            {
                "type": "matchRegex",
                "parameter": [
                    {"type": "template", "key": "arg0", "value": "{{Click URL}}"},
                    {"type": "template", "key": "arg1", "value": "^https?://(?!(?:[^/]*\\.)?agria\\.pl(?:/|$))"},
                    {"type": "boolean", "key": "ignore_case", "value": "true"},
                ],
            },
        ],
        "notes": "Klik na link wychodzacy poza agria.pl.",
    },
    {
        "name": "File Download",
        "type": "linkClick",
        "parameter": [
            {"type": "boolean", "key": "waitForTags", "value": "false"},
            {"type": "boolean", "key": "checkValidation", "value": "false"},
        ],
        "filter": [
            {
                "type": "matchRegex",
                "parameter": [
                    {"type": "template", "key": "arg0", "value": "{{Click URL}}"},
                    {"type": "template", "key": "arg1", "value": "\\.(pdf|doc|docx|xls|xlsx|ppt|pptx|zip|csv)(\\?.*)?$"},
                    {"type": "boolean", "key": "ignore_case", "value": "true"},
                ],
            },
        ],
        "notes": "Klik na link konczacy sie rozszerzeniem dokumentu (PDF/DOC/XLS itp.).",
    },
    {
        "name": "Form Submit",
        "type": "formSubmission",
        "parameter": [
            {"type": "boolean", "key": "waitForTags", "value": "false"},
            {"type": "boolean", "key": "checkValidation", "value": "false"},
        ],
        "notes": "Wyslanie dowolnego formularza HTML.",
    },
]

for trg in TRIGGERS:
    found = find_by_name(existing_triggers, "name", trg["name"])
    if found:
        trigger_ids[trg["name"]] = found["triggerId"]
        print(f"SKIP {trg['name']} (exists, id={found['triggerId']})")
        continue
    r = api("POST", BASE, f"{WS_PATH}/triggers", trg)
    if "error" in r:
        print(f"ERR {trg['name']}: HTTP {r.get('code')}: {r.get('error')[:400]}")
    else:
        trigger_ids[trg["name"]] = r["triggerId"]
        print(f"OK {trg['name']} -> {r['triggerId']}")


# === TAGS ===
step("Tags")
existing_tags = api("GET", BASE, f"{WS_PATH}/tags").get("tag", [])

# Helper: GA4 event params builder
def ga4_event_params(name, params_dict):
    """Returns parameter list for a GA4 Event tag (type=gaawe).
    params_dict: {param_name: value (string with optional {{var}} interpolation)}
    """
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
        "name": "Consent Default Denied",
        "type": "html",
        "parameter": [
            {
                "type": "template",
                "key": "html",
                "value": (
                    "<script>\n"
                    "window.dataLayer = window.dataLayer || [];\n"
                    "function gtag(){dataLayer.push(arguments);}\n"
                    "gtag('consent', 'default', {\n"
                    "  'ad_storage': 'denied',\n"
                    "  'ad_user_data': 'denied',\n"
                    "  'ad_personalization': 'denied',\n"
                    "  'analytics_storage': 'denied',\n"
                    "  'wait_for_update': 500,\n"
                    "  'region': ['EEA','PL']\n"
                    "});\n"
                    "gtag('set', 'ads_data_redaction', true);\n"
                    "gtag('set', 'url_passthrough', true);\n"
                    "</script>"
                ),
            },
            {"type": "boolean", "key": "supportDocumentWrite", "value": "false"},
        ],
        "firingTriggerId": [TRIGGER_CONSENT_INIT],
        "tagFiringOption": "oncePerEvent",
        "notes": (
            "Consent Mode v2 default = denied dla EEA/PL. Odpalany na Consent "
            "Initialization (przed All Pages). Update consent: zarzadza Complianz GDPR plugin."
        ),
    },
    {
        "name": "GA4 - Google Tag",
        "type": "googtag",
        "parameter": [
            {"type": "template", "key": "tagId", "value": GA4_MEASUREMENT_ID},
        ],
        "firingTriggerId": [TRIGGER_ALL_PAGES],
        "tagFiringOption": "oncePerEvent",
        "notes": (
            "Google Tag (GA4) — odpalany na All Pages. Wymaga Consent "
            "analytics_storage=granted (po akceptacji w Complianz banner)."
        ),
    },
    {
        "name": "GA4 Event - Scroll",
        "type": "gaawe",
        "parameter": ga4_event_params("scroll", {
            "scroll_depth": "{{Scroll Depth Threshold}}",
            "scroll_unit": "{{Scroll Depth Units}}",
        }),
        "trigger_name": "Scroll - 25/50/75/90",
        "notes": "Event scroll z parametrem scroll_depth (25/50/75/90).",
    },
    {
        "name": "GA4 Event - Outbound Link",
        "type": "gaawe",
        "parameter": ga4_event_params("outbound_link", {
            "link_url": "{{Click URL}}",
            "link_text": "{{Click Text}}",
        }),
        "trigger_name": "Outbound Link",
        "notes": "Event outbound_link — klik na link wychodzacy poza agria.pl.",
    },
    {
        "name": "GA4 Event - File Download",
        "type": "gaawe",
        "parameter": ga4_event_params("file_download", {
            "file_name": "{{Click URL}}",
            "link_text": "{{Click Text}}",
        }),
        "trigger_name": "File Download",
        "notes": "Event file_download — klik na PDF/DOC/XLS/itp.",
    },
    {
        "name": "GA4 Event - Form Submit",
        "type": "gaawe",
        "parameter": ga4_event_params("form_submit", {
            "form_id": "{{Form ID}}",
            "form_url": "{{Form URL}}",
        }),
        "trigger_name": "Form Submit",
        "notes": "Event form_submit — wyslanie dowolnego formularza.",
    },
]

for tag in TAGS:
    if find_by_name(existing_tags, "name", tag["name"]):
        print(f"SKIP {tag['name']} (exists)")
        continue
    body = {
        "name": tag["name"],
        "type": tag["type"],
        "parameter": tag["parameter"],
        "notes": tag.get("notes", ""),
        "tagFiringOption": tag.get("tagFiringOption", "oncePerEvent"),
    }
    if "firingTriggerId" in tag:
        body["firingTriggerId"] = tag["firingTriggerId"]
    elif "trigger_name" in tag:
        tid = trigger_ids.get(tag["trigger_name"])
        if not tid:
            print(f"ERR {tag['name']}: trigger '{tag['trigger_name']}' not found")
            continue
        body["firingTriggerId"] = [tid]
    r = api("POST", BASE, f"{WS_PATH}/tags", body)
    if "error" in r:
        print(f"ERR {tag['name']}: HTTP {r.get('code')}: {r.get('error')[:400]}")
    else:
        print(f"OK {tag['name']} -> {r.get('tagId')}")


# === FINAL STATE ===
step("Workspace state")
finals = api("GET", BASE, f"{WS_PATH}/tags").get("tag", [])
print(f"Tags: {len(finals)}")
for t in finals:
    print(f"  - {t['name']} (type={t['type']}, fire={t.get('firingTriggerId')})")
trgs = api("GET", BASE, f"{WS_PATH}/triggers").get("trigger", [])
print(f"Triggers: {len(trgs)}")
for t in trgs:
    print(f"  - {t['name']} (type={t['type']}, id={t['triggerId']})")
vars_ = api("GET", BASE, f"{WS_PATH}/variables").get("variable", [])
print(f"User-defined variables: {len(vars_)}")
for v in vars_:
    print(f"  - {v['name']} (type={v['type']})")
