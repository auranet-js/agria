#!/usr/bin/env python3
"""PreToolUse (Bash): każdy zapis na koncie OLX AGRII wymaga zgody Janka, także w trybie auto.

Powód: 13.10.2026 zmiana cen na 38 ogłoszeniach poszła bez „ok” — dry-run nie zatrzymał wykonania.
Łapie: skrypty scripts/olx/* z flagą zapisu, olx-agria api z metodą zapisu, inline call("PUT"/"POST"/...).
"""
import json, re, sys

cmd = (json.load(sys.stdin).get("tool_input") or {}).get("command", "")
olx = re.search(r"scripts/olx/|olx-agria|post_adverts|partner/adverts|olx\.pl/api", cmd)
zapis = (
    re.search(r"--(pilot|all|update|auto-extend|ids|wyslij|apply)\b", cmd)
    or re.search(r"-X\s*['\"]?(PUT|POST|DELETE|PATCH)", cmd)
    or re.search(r"call\(\s*['\"](PUT|POST|DELETE|PATCH)['\"]", cmd)
    or re.search(r"--request\s+(PUT|POST|DELETE|PATCH)", cmd)
)
if olx and zapis:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": "ZAPIS NA KONCIE OLX AGRII — wymaga wyraźnej zgody Janka (hook olx-guard).",
    }}))
