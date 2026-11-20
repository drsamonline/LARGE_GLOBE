#!/usr/bin/env python3
"""One source of truth for the shared shell.

The header and footer are copied into 188 static files. This rewrites them from
the canonical copy in index.html, so a change to the navigation is one edit and
one command instead of 188 edits.

    python3 tools/rebuild-shell.py          # rewrite every page
    python3 tools/rebuild-shell.py --check  # exit 1 if any page is out of step
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# pages that deliberately carry a different, shorter shell
EXEMPT = {"charts.html", "themes.html", "offline.html", "404.html"}

canon = open("index.html", encoding="utf-8").read()
HEADER = re.search(r'<header class="site-head">.*?</header>', canon, re.S).group(0)
FOOTER = re.search(r'<footer class="site-foot">.*?</footer>', canon, re.S).group(0)
HEADER_BARE = HEADER.replace(' aria-current="page"', "")


def header_for(page):
    """The canonical header, with aria-current on the link for this page."""
    h = HEADER_BARE
    if page == "index.html":
        return h.replace('<a href="index.html">Index</a>',
                         '<a href="index.html" aria-current="page">Index</a>', 1)
    needle = f'<a href="{page}">'
    if needle in h:
        h = h.replace(needle, f'<a href="{page}" aria-current="page">', 1)
    return h


def wanted(page):
    return header_for(page), FOOTER


def current(page, text):
    h = re.search(r'<header class="site-head">.*?</header>', text, re.S)
    f = re.search(r'<footer class="site-foot">.*?</footer>', text, re.S)
    return (h.group(0) if h else None), (f.group(0) if f else None)


def main():
    check = "--check" in sys.argv
    changed, problems = [], []
    for p in sorted(glob.glob("*.html")):
        if p in EXEMPT:
            continue
        text = open(p, encoding="utf-8").read()
        want_h, want_f = wanted(p)
        have_h, have_f = current(p, text)
        if have_h is None or have_f is None:
            problems.append(f"{p}: shell not found")
            continue
        if have_h == want_h and have_f == want_f:
            continue
        changed.append(p)
        if not check:
            new = text.replace(have_h, want_h, 1).replace(have_f, want_f, 1)
            open(p, "w", encoding="utf-8").write(new)

    if check:
        for p in changed:
            print(f"out of step: {p}")
        print(f"{len(changed)} page(s) out of step")
        sys.exit(1 if changed or problems else 0)

    for p in changed:
        print(f"rewrote {p}")
    print(f"{len(changed)} page(s) rewritten from the canonical shell")
    if problems:
        print("\n".join(problems))
        sys.exit(1)


if __name__ == "__main__":
    main()
