"""Wspólne narzędzia auth + API dla skryptów Google AGRIA.

Auth z ~/secrets/google/tokens.json + auto-refresh przy 401.
Konwencja: każdy skrypt importuje api(method, base, path, body=None) i loguje wynik.
"""
import json
import os
import urllib.parse
import urllib.request
from urllib.error import HTTPError

TOKENS_FILE = os.path.expanduser("~/secrets/google/tokens.json")
CLIENT_FILE = os.path.expanduser("~/secrets/google/oauth-desktop-client.json")


def _load_token():
    with open(TOKENS_FILE) as f:
        return json.load(f)


def _refresh():
    t = _load_token()
    with open(CLIENT_FILE) as f:
        c = json.load(f)["installed"]
    data = urllib.parse.urlencode({
        "client_id": c["client_id"],
        "client_secret": c["client_secret"],
        "refresh_token": t["refresh_token"],
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as r:
        new = json.loads(r.read())
    t.update({k: v for k, v in new.items() if k != "refresh_token"})
    with open(TOKENS_FILE, "w") as f:
        json.dump(t, f, indent=2)
    os.chmod(TOKENS_FILE, 0o600)


def api(method, base, path, body=None, retry=True):
    """Call Google API. base=https://..., path=/v1beta/...
    Returns dict (json) or {"error": str, "code": int} on error.
    """
    t = _load_token()
    headers = {
        "Authorization": f"Bearer {t['access_token']}",
        "Content-Type": "application/json",
    }
    url = f"{base}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except HTTPError as e:
        body_err = e.read().decode()
        if e.code == 401 and retry:
            _refresh()
            return api(method, base, path, body, retry=False)
        return {"error": body_err, "code": e.code}
