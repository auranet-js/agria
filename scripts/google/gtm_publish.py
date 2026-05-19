#!/usr/bin/env python3
"""GTM create version + publish dla AGRIA container 252883347 workspace 3.

UWAGA: container jeszcze NIE jest wstrzykniety w <head> agria.pl — publish wersji
na backendzie GTM oznacza tylko ze wersja jest gotowa do uzycia. Faktyczne odpalenie
analityki nastapi gdy skrypt GTM-TDC85TQN bedzie w <head> agria.pl (T1 M1).

Run: python3 ~/projekty/agria/scripts/google/gtm_publish.py [version_name]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import api

ACCOUNT = "6356149706"
CONTAINER = "252883347"
WORKSPACE = "3"
BASE = "https://tagmanager.googleapis.com"
WS_PATH = f"/tagmanager/v2/accounts/{ACCOUNT}/containers/{CONTAINER}/workspaces/{WORKSPACE}"

version_name = sys.argv[1] if len(sys.argv) > 1 else "v1 - pre-M1 base config (Consent Mode v2 + GA4 + 5 events)"
notes = (
    "Wersja v1 — pre-M1 konfiguracja Auranet (ADR 2026-05-19).\n\n"
    "Zawiera:\n"
    "- Consent Mode v2 default denied dla EEA/PL\n"
    "- Google Tag (G-KVFMR3NZDH) na All Pages\n"
    "- 4 base events: scroll (25/50/75/90), outbound_link, file_download, form_submit\n"
    "- 14 built-in vars enabled (click/form/scroll)\n\n"
    "UWAGA: skrypt GTM jeszcze nie wstrzykniety w <head> agria.pl. "
    "Wstrzykiwanie = T1 M1 po podpisaniu oferty."
)

print(f"=== Creating version: {version_name} ===")
r = api("POST", BASE, f"{WS_PATH}:create_version", {
    "name": version_name,
    "notes": notes,
})

if "error" in r:
    print(f"ERR create_version: HTTP {r.get('code')}")
    print(r.get("error"))
    sys.exit(1)

version = r.get("containerVersion") or r
version_id = version.get("containerVersionId")
print(f"OK version created: {version_id}")
print(f"  Tags: {len(version.get('tag', []))}")
print(f"  Triggers: {len(version.get('trigger', []))}")
print(f"  Variables: {len(version.get('variable', []))}")
print(f"  Built-in vars: {len(version.get('builtInVariable', []))}")

# Publish
print(f"\n=== Publishing version {version_id} ===")
publish_path = f"/tagmanager/v2/accounts/{ACCOUNT}/containers/{CONTAINER}/versions/{version_id}:publish"
r = api("POST", BASE, publish_path)
if "error" in r:
    print(f"ERR publish: HTTP {r.get('code')}")
    print(r.get("error"))
    sys.exit(1)

print(f"OK published")
print(json.dumps(r, indent=2, ensure_ascii=False)[:1500])
