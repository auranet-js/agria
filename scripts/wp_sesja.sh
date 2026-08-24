#!/bin/bash
# Odnawia sesję panelu WordPressa dla Puppeteera (patrz wp_sesja.php).
#
# Uruchamiaj z katalogu repo:   bash scripts/wp_sesja.sh
# Wynik:                        ~/secrets/agria/wp-sesja.json (600)
#
# Odcięcie dostępu — na serwerze:
#   ssh agria-prod "cd ~/agria.pl && wp --path=. --user=1 user session destroy 1 --all"
# (unieważnia też sesje przeglądarkowe Janka — trzeba się zalogować ponownie)

set -euo pipefail

ZDALNY=/tmp/wp_sesja_$$.php
CEL="$HOME/secrets/agria/wp-sesja.json"
SKRYPT="$(dirname "$0")/wp_sesja.php"

[ -f "$SKRYPT" ] || { echo "BLAD: brak $SKRYPT" >&2; exit 1; }
mkdir -p "$(dirname "$CEL")"

scp -q "$SKRYPT" "agria-prod:$ZDALNY"
ssh agria-prod "cd /home/server371853/ftp/agria.pl && timeout 90 /usr/local/sbin/wp --path=. --user=1 eval-file $ZDALNY; rm -f $ZDALNY" > "$CEL"
chmod 600 "$CEL"

python3 - "$CEL" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
print(f"konto:  {d['user']} (ID {d['user_id']})")
print(f"domena: {d['domena']}")
print(f"wygasa: {d['wygasa']}")
print(f"token:  {d['token'][:16]}…")
print(f"cookies: {len(d['cookies'])} szt., zapisane w {sys.argv[1]}")
PY
