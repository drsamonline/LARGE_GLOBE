#!/usr/bin/env python3
"""Fail the build if a page breaks the archive's own rules."""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
pages = sorted(glob.glob("*.html"))
problems = []

for p in pages:
    h = open(p, encoding="utf-8").read()
    if h.count('rel="canonical"') != 1:
        problems.append(f"{p}: canonical tag count {h.count('rel=\"canonical\"')}")
    if len(re.findall(r"<h1[ >]", h)) != 1:
        problems.append(f"{p}: {len(re.findall(r'<h1[ >]', h))} h1 elements")
    if 'class="skip"' not in h:
        problems.append(f"{p}: no skip link")
    if p != "support.html" and 'class="support-band"' not in h:
        problems.append(f"{p}: no support band")
    if 'src=""' in h:
        problems.append(f"{p}: empty image src")
    for t in re.findall(r'href="([^"#:?]+\.html)[^"]*"', h):
        if not os.path.exists(t):
            problems.append(f"{p}: broken internal link -> {t}")
    for s in re.findall(r'src="([^":]+\.(?:avif|svg|png|webp|jpg))"', h):
        if not os.path.exists(s):
            problems.append(f"{p}: missing asset -> {s}")

for p in problems:
    print(p)
print(f"\n{len(pages)} pages checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
