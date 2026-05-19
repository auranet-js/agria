#!/usr/bin/env python3
"""GA4 base config for AGRIA property 538301430 — idempotent.

Wykonuje:
- Data retention 14 months + reset on new activity
- Google Signals disabled (no Signals na start, zgodnie z ADR pre-M1)
- 5 custom dimensions (segmenty AGRIA z keyword research klastrami)
- 4 key events (form_submit, phone_click, file_download, generate_lead)

Idempotentny: sprawdza istniejące dimensions/key events przed POST.

Run: python3 ~/projekty/agria/scripts/google/ga4_setup.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import api

PROPERTY_ID = "538301430"
ADMIN = "https://analyticsadmin.googleapis.com"


def step(name):
    print(f"\n=== {name} ===")


# 1. Data retention
step("Data retention 14 months + reset on new activity")
r = api(
    "PATCH",
    ADMIN,
    f"/v1beta/properties/{PROPERTY_ID}/dataRetentionSettings"
    f"?updateMask=eventDataRetention,resetUserDataOnNewActivity",
    {"eventDataRetention": "FOURTEEN_MONTHS", "resetUserDataOnNewActivity": True},
)
print(json.dumps(r, indent=2, ensure_ascii=False))

# 2. Google Signals OFF (na start)
step("Google Signals DISABLED")
r = api(
    "PATCH",
    ADMIN,
    f"/v1beta/properties/{PROPERTY_ID}/googleSignalsSettings?updateMask=state",
    {"state": "GOOGLE_SIGNALS_DISABLED"},
)
print(json.dumps(r, indent=2, ensure_ascii=False))

# 3. Custom dimensions (segmenty AGRIA)
DIMS = [
    {
        "parameter_name": "cluster",
        "display_name": "Klaster",
        "description": (
            "Klaster tematyczny treści: rolnictwo/budownictwo/drogownictwo/"
            "rybactwo/oczyszczalnie/paszarstwo/marka. Źródło: KEYWORD_RESEARCH_2026-05-19."
        ),
        "scope": "EVENT",
    },
    {
        "parameter_name": "intent_type",
        "display_name": "Typ intencji",
        "description": "Intencja zapytania: informational/transactional/commercial.",
        "scope": "EVENT",
    },
    {
        "parameter_name": "content_type",
        "display_name": "Typ treści",
        "description": "Typ strony: produkt_wc/landing/blog/faq/kontakt/karta_techniczna/inne.",
        "scope": "EVENT",
    },
    {
        "parameter_name": "season_phase",
        "display_name": "Faza sezonowa",
        "description": (
            "Sezon: wiosna_rolnictwo (III-IV) / jesien_rolnictwo (IX-XI) / "
            "lato_drogownictwo (V-VIII) / przed_zima_rybactwo (IX-XI) / caly_rok."
        ),
        "scope": "EVENT",
    },
    {
        "parameter_name": "user_segment",
        "display_name": "Segment uzytkownika",
        "description": (
            "Persona: rolnik/instytucja_przetargowa/budownictwo_b2b/drogownictwo/"
            "rybactwo/handel_b2c/inne. Heurystyka na podstawie scieżki nawigacji."
        ),
        "scope": "USER",
    },
]

step("Existing custom dimensions")
existing = api("GET", ADMIN, f"/v1beta/properties/{PROPERTY_ID}/customDimensions")
existing_params = {d.get("parameterName") for d in existing.get("customDimensions", [])}
print(f"Existing: {existing_params}")

step("Creating custom dimensions (skip if exists)")
for dim in DIMS:
    if dim["parameter_name"] in existing_params:
        print(f"SKIP {dim['parameter_name']} (exists)")
        continue
    r = api(
        "POST",
        ADMIN,
        f"/v1beta/properties/{PROPERTY_ID}/customDimensions",
        {
            "parameterName": dim["parameter_name"],
            "displayName": dim["display_name"],
            "description": dim["description"],
            "scope": dim["scope"],
        },
    )
    if "error" in r:
        print(f"ERR {dim['parameter_name']}: HTTP {r.get('code')}: {r.get('error')}")
    else:
        print(f"OK {dim['parameter_name']} -> {r.get('name')}")

# 4. Key events (=conversions w starej terminologii GA4)
EVENTS = ["form_submit", "phone_click", "file_download", "generate_lead"]

step("Existing key events")
existing_ke = api("GET", ADMIN, f"/v1beta/properties/{PROPERTY_ID}/keyEvents")
existing_ke_names = {e.get("eventName") for e in existing_ke.get("keyEvents", [])}
print(f"Existing: {existing_ke_names}")

step("Creating key events (skip if exists)")
for ev in EVENTS:
    if ev in existing_ke_names:
        print(f"SKIP {ev} (exists)")
        continue
    r = api(
        "POST",
        ADMIN,
        f"/v1beta/properties/{PROPERTY_ID}/keyEvents",
        {"eventName": ev, "countingMethod": "ONCE_PER_EVENT"},
    )
    if "error" in r:
        print(f"ERR {ev}: HTTP {r.get('code')}: {r.get('error')}")
    else:
        print(f"OK {ev} -> {r.get('name')}")

# Final state
step("Final summary")
print(f"Property: properties/{PROPERTY_ID} (agria.pl)")
print(f"Measurement ID: G-KVFMR3NZDH (web stream 14906073685)")
dims_final = api("GET", ADMIN, f"/v1beta/properties/{PROPERTY_ID}/customDimensions")
print(f"Custom dimensions: {len(dims_final.get('customDimensions', []))}")
ke_final = api("GET", ADMIN, f"/v1beta/properties/{PROPERTY_ID}/keyEvents")
print(f"Key events: {len(ke_final.get('keyEvents', []))}")
print("\nDone.")
