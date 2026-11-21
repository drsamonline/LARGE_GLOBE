#!/usr/bin/env python3
"""A size budget per page, so a regeneration cannot quietly ship a monster."""
import glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
# print-edition.html is the whole archive in one page and grows with it: budget
# per dossier rather than a flat cap, so the check fails on a runaway build and
# not on the archive simply getting bigger.
import glob as _glob
_DOSSIERS = len([f for f in _glob.glob("*.html") if '<aside class="facts">' in open(f, encoding="utf-8").read()])
BUDGET_KB = {"print-edition.html": 300 + 6 * _DOSSIERS, "themes.html": 200 + 0.5 * _DOSSIERS, "search.html": 500, "credits.html": 200 + 0.5 * _DOSSIERS,
             "compare.html": 250, "topics.html": 400}
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
