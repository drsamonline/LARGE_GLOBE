#!/usr/bin/env python3
"""A size budget per page, so a regeneration cannot quietly ship a monster."""
import glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BUDGET_KB = {"print-edition.html": 1000, "search.html": 400, "compare.html": 200, "topics.html": 400}
DEFAULT_KB = 120
over = []
for p in sorted(glob.glob("*.html")):
    kb = os.path.getsize(p) // 1024
    cap = BUDGET_KB.get(p, DEFAULT_KB)
    if kb > cap:
        over.append(f"{p}: {kb} KB over a {cap} KB budget")
total = sum(os.path.getsize(p) for p in glob.glob("*.html")) // 1024
print("\n".join(over) or "every page inside its budget")
print(f"total HTML: {total} KB")
sys.exit(1 if over else 0)
