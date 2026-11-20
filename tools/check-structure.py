#!/usr/bin/env python3
"""Fail the build if a page breaks the archive's own rules."""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
pages = sorted(glob.glob("*.html"))
UTILITY = {"index.html","reading-guide.html","themes.html","charts.html","master-list.html","search.html",
           "compare.html","collections.html","links.html","sources.html","credits.html","claims-index.html",
           "print-edition.html","open-problems.html","ancient-index.html","frontier-index.html","modern-index.html",
           "mega-index.html","support.html","404.html","topics.html","random.html","corrections.html","glossary.html"}
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
    for a, b in re.findall(r'<div class="pager"><a href="([^"]+)">.*?</a><a href="([^"]+)">', h):
        for t in (a, b):
            path = t.split("#")[0]
            if not path.endswith(".html") or not os.path.exists(path):
                problems.append(f"{p}: pager points at {t}")
    if p not in UTILITY and '<aside class="facts">' in h and h.count("<h3>") >= 2 and 'class="toc"' not in h:
        problems.append(f"{p}: dossier with sections but no on-this-page rail")
    if 'data-pref="theme"' not in h:
        problems.append(f"{p}: no reader-preference controls")
    if 'src=""' in h:
        problems.append(f"{p}: empty image src")
    for t in re.findall(r'href="([^"#:?]+\.html)[^"]*"', h):
        if not os.path.exists(t):
            problems.append(f"{p}: broken internal link -> {t}")
    for s in re.findall(r'src="([^":]+\.(?:avif|svg|png|webp|jpg))"', h):
        if not os.path.exists(s):
            problems.append(f"{p}: missing asset -> {s}")
    og = re.search(r'property="og:image" content="[^"]*LARGE_GLOBE/([^"]+)"', h)
    if og and not os.path.exists(og.group(1)):
        problems.append(f"{p}: og:image not in the repo -> {og.group(1)}")
    if p not in UTILITY and '<aside class="facts">' in h:
        for marker, name in (('class="crumbs"', 'breadcrumbs'), ('class="cite"', 'citation block'),
                             ('class="related"', 'related strip')):
            if marker not in h:
                problems.append(f"{p}: dossier without {name}")
        if 'citation_title' not in h:
            problems.append(f"{p}: dossier without citation meta")

for p in problems:
    print(p)
print(f"\n{len(pages)} pages checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
