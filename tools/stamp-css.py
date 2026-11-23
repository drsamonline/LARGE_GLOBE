#!/usr/bin/env python3
"""Stamp the current stylesheet hash into every page's <link>.

A cache-busting query that is typed by hand is a query that goes stale. This reads
the file, hashes it and writes the hash into every page, so a CSS change reaches a
returning reader instead of sitting behind a browser cache.

    python3 tools/stamp-css.py
    python3 tools/stamp-css.py --check
"""
import glob, hashlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CHECK = "--check" in sys.argv


def main():
    h = hashlib.md5(open("assets/style.css", "rb").read()).hexdigest()[:8]
    stale = []
    for p in glob.glob("*.html"):
        t = open(p, encoding="utf-8").read()
        if re.search(r"assets/style\.css\?v=(?!%s)" % h, t):
            stale.append(p)
            if not CHECK:
                t = re.sub(r"assets/style\.css\?v=[0-9a-z]+", f"assets/style.css?v={h}", t)
                open(p, "w", encoding="utf-8").write(t)
    if CHECK:
        if stale:
            print(f"{len(stale)} page(s) carry a stale stylesheet hash — run tools/stamp-css.py")
            return 1
        print(f"stylesheet hash {h} on every page")
        return 0
    print(f"stylesheet hash {h}: {len(stale)} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
