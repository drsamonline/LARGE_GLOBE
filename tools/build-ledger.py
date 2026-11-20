#!/usr/bin/env python3
"""Regenerate data/claims.json from the pages. The pages stay authoritative."""
import glob, html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
UTILITY = {"index.html","reading-guide.html","themes.html","charts.html","master-list.html","search.html",
           "compare.html","collections.html","links.html","sources.html","credits.html","claims-index.html",
           "print-edition.html","open-problems.html","ancient-index.html","frontier-index.html","modern-index.html",
           "mega-index.html","support.html","404.html","topics.html","random.html","corrections.html",
           "glossary.html","offline.html"}
CANON = {"Documented","Live debate","Fringe claim","Debunked","Fiction","Open problem","Debunked / hoax"}
TODAY = "2026-11-20"

claims = []
for p in sorted(glob.glob("*.html")):
    if p in UTILITY:
        continue
    h = open(p, encoding="utf-8").read()
    if '<aside class="facts">' not in h:
        continue
    title = re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", h, re.S).group(1)).strip()
    th = re.search(r'theme-tag" href="themes.html#([a-z]+)">([^<]+)<', h)
    lab = re.search(r'<span class="badge (b-[a-z]+)">([^<]+)</span>', h)
    stand = re.search(r'<p class="standfirst">(.*?)</p>', h, re.S)
    src = re.findall(r'<ul class="srclist">(.*?)</ul>', h, re.S)
    urls = re.findall(r'href="(https?://[^"]+)"', src[0]) if src else []
    facts = {}
    fm = re.search(r'<aside class="facts">.*?<dl>(.*?)</dl>', h, re.S)
    if fm:
        for dt, dd in re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", fm.group(1), re.S):
            facts[re.sub(r"<[^>]+>", "", dt).strip()] = re.sub(r"<[^>]+>", "", dd).strip()
    label_text = lab.group(2) if lab else None
    claims.append({
        "slug": p[:-5], "url": p, "title": title,
        "theme": th.group(2) if th else None, "theme_id": th.group(1) if th else None,
        "label_text": label_text, "label_class": lab.group(1) if lab else None,
        "label_canonical": label_text in CANON,
        "standfirst": html.unescape(re.sub(r"<[^>]+>", "", stand.group(1)).strip()) if stand else None,
        "facts": facts,
        "sources": {"count": len(urls), "urls": urls},
        "last_reviewed": TODAY, "reviewed_by": "Dr. Sohil Momin", "licence": "CC BY-NC 4.0",
    })

doc = {"$comment": ("The provenance ledger. Generated from the pages by tools/build-ledger.py; the pages remain "
                    "the source of truth until the views are rewired to read this file. label_class is the canonical "
                    "four-label colour; label_text is the page's own gloss, bespoke on some pages (label_canonical)."),
       "site": "The Larger World Archive", "generated": TODAY, "count": len(claims), "claims": claims}
json.dump(doc, open("data/claims.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(claims)} claims written to data/claims.json")
