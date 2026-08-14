#!/usr/bin/env bash
# ads_call.sh — helper do Google Ads API dla CID 6742071446 (AGRIA, direct, NIE pod MCC)
#
# Konto założone 2026-08-11 przez Janka (karta Auranet — budżet opłacany z góry,
# zgodnie z planem wysłanym klientowi 06.08). Waluta PLN, strefa Europe/Warsaw,
# auto-tagging ON. Widoczne pod js@auranet.com.pl w listAccessibleCustomers.
#
# Wersja API: czytana z ~/secrets/google/ads-config.json (pole `api_version`) — NIE hardkoduj.
#   Google sunsetuje wersje ~rok po wydaniu. Stan 2026-08-07: v25 (sunset 2027-08).
# Access token: świeży z ~/bin/google-access-token (surowy z tokens.json wygasa po ~60 min).
#
# Użycie:
#   bash ads_call.sh <PATH> <METHOD> [JSON_BODY_FILE]
#   PATH np. /googleAds:searchStream, /campaigns:mutate, /campaignBudgets:mutate,
#            /adGroups:mutate, /adGroupAds:mutate, /adGroupCriteria:mutate,
#            /conversionActions:mutate, /campaignCriteria:mutate, /assets:mutate
#
# Uwaga: dopóki na koncie nie jest domknięte rozliczenie, część zasobów zwraca
#   CUSTOMER_NOT_ENABLED (403). Konwersje i customer czytają się mimo to.
#
# Output: surowy JSON.

set -euo pipefail

CID="6742071446"
CFG="/home/host476470/secrets/google/ads-config.json"

API_VER=$(python3 -c "import json; print(json.load(open('$CFG')).get('api_version','v25'))")
ENDPOINT_BASE="https://googleads.googleapis.com/${API_VER}/customers/${CID}"

PATH_API="${1:?PATH wymagany (np. /campaigns:mutate)}"
METHOD="${2:-POST}"
BODY_FILE="${3:-}"

ACCESS=$("$HOME/bin/google-access-token")
DEV=$(python3 -c "import json; print(json.load(open('$CFG'))['developer_token'])")

URL="${ENDPOINT_BASE}${PATH_API}"

if [[ -n "$BODY_FILE" && -f "$BODY_FILE" ]]; then
  curl -sS -X "$METHOD" \
    -H "Authorization: Bearer $ACCESS" \
    -H "developer-token: $DEV" \
    -H "Content-Type: application/json" \
    --data-binary @"$BODY_FILE" \
    "$URL"
else
  curl -sS -X "$METHOD" \
    -H "Authorization: Bearer $ACCESS" \
    -H "developer-token: $DEV" \
    -H "Content-Type: application/json" \
    "$URL"
fi
