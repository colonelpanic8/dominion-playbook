#!/usr/bin/env python3
"""Look up Card Glicko ratings by exact card name (case-insensitive).

Usage: card-ratings.py <name>... e.g. card-ratings.py Remake "King's Court"
"""

import difflib
import json
import sys
from pathlib import Path

rows = [json.loads(line) for line in (Path(__file__).parent / "card-ratings.jsonl").open(encoding="utf-8")]
cards = [r for r in rows if "name" in r]
by_name = {}
for r in cards:
    by_name.setdefault(r["name"].casefold(), []).append(r)
for r in cards:
    for half in r["name"].split("/") if "/" in r["name"] else []:
        by_name.setdefault(half.casefold(), []).append(r)

if len(sys.argv) < 2:
    sys.exit(__doc__.strip())

print("| Card | Rating | Rank | Kind | Edition |")
print("| --- | ---: | ---: | --- | --- |")
missing, shown = [], set()
for query in sys.argv[1:]:
    found = by_name.get(query.strip().casefold())
    if not found:
        missing.append(query)
    for r in found or []:
        if id(r) in shown:
            continue
        shown.add(id(r))
        print(f"| {r['name']} | {r['rating']:.1f} | {r['rank']}/{r['of']} | {r['kind']} | {r['edition']} |")
if missing:
    print()
for query in missing:
    close = difflib.get_close_matches(query.casefold(), list(by_name), n=3, cutoff=0.75)
    hint = f" Did you mean: {', '.join(by_name[c][0]['name'] for c in close)}?" if close else ""
    print(f"Not rated: {query}.{hint}")
