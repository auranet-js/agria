#!/usr/bin/env python3
"""Zbiera ogloszenia z kategorii Nawozy (4368) na OLX i agreguje po sprzedawcy."""
import json, time, urllib.request, urllib.parse, sys, collections

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
BASE = "https://www.olx.pl/api/v1/offers/"


def fetch(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def crawl(category_id, max_pages=20, limit=50):
    out, seen = [], set()
    for page in range(max_pages):
        try:
            d = fetch({"offset": page * limit, "limit": limit, "category_id": category_id,
                       "sort_by": "created_at:desc"})
        except urllib.error.HTTPError as exc:
            # OLX odcina paginacje w okolicach offsetu 1000 — konczymy tym, co zebrane
            print(f"  stop na offsecie {page*limit}: HTTP {exc.code}", file=sys.stderr)
            break
        items = d.get("data", [])
        if not items:
            break
        for it in items:
            if it["id"] not in seen:
                seen.add(it["id"])
                out.append(it)
        total = d.get("metadata", {}).get("total_elements")
        print(f"  strona {page+1}: +{len(items)} (razem {len(out)} / total {total})", file=sys.stderr)
        if len(items) < limit:
            break
        time.sleep(0.4)
    return out


def price_of(offer):
    for p in offer.get("params", []):
        if p.get("key") == "price":
            v = p.get("value", {})
            return v.get("value"), v.get("currency"), v.get("negotiable")
    return None, None, None


if __name__ == "__main__":
    cat = int(sys.argv[1]) if len(sys.argv) > 1 else 4368
    offers = crawl(cat)
    rows = []
    for o in offers:
        val, cur, neg = price_of(o)
        u = o.get("user", {})
        rows.append({
            "id": o["id"], "title": o["title"], "price": val, "currency": cur, "negotiable": neg,
            "user_id": u.get("id"), "user_name": u.get("name"), "is_business": u.get("company_name") is not None or u.get("is_business"),
            "company": u.get("company_name"), "city": (o.get("location") or {}).get("city", {}).get("name"),
            "region": (o.get("location") or {}).get("region", {}).get("name"),
            "created": o.get("created_time"), "refreshed": o.get("last_refresh_time"),
            "promoted": bool((o.get("promotion") or {}).get("highlighted") or (o.get("promotion") or {}).get("top_ad")),
            "url": o.get("url"),
        })
    json.dump(rows, open(f"olx-market-{cat}.json", "w"), ensure_ascii=False, indent=1)

    by_user = collections.Counter(r["user_id"] for r in rows)
    names = {r["user_id"]: (r["company"] or r["user_name"]) for r in rows}
    print(f"\n=== kategoria {cat}: {len(rows)} ogloszen, {len(by_user)} sprzedawcow ===")
    print(f"{'ogl':>4} | {'promo':>5} | sprzedawca")
    for uid, n in by_user.most_common(20):
        promo = sum(1 for r in rows if r["user_id"] == uid and r["promoted"])
        print(f"{n:>4} | {promo:>5} | {names.get(uid)} (id {uid})")
