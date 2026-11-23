#!/usr/bin/env python3
"""Regenerate sitemap.xml from the pages that exist.

    python3 tools/build-sitemap.py            # rewrite
    python3 tools/build-sitemap.py --check    # exit 1 if a page is missing
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://drsamonline.github.io/LARGE_GLOBE/"
SKIP = {"404.html", "offline.html"}
CHECK = "--check" in sys.argv


def main():
    pages = sorted(p for p in glob.glob("*.html") if p not in SKIP)
    pages.sort(key=lambda p: (p != "index.html", p))
    old = open("sitemap.xml", encoding="utf-8").read() if os.path.exists("sitemap.xml") else ""
    listed = set(re.findall(r"<loc>" + re.escape(BASE) + r"([^<]*)</loc>", old))
    missing = [p for p in pages if p not in listed]
    if CHECK:
        if missing:
            print(f"sitemap is missing {len(missing)} page(s): {missing[:5]}")
            return 1
        print(f"sitemap lists all {len(pages)} pages")
        return 0
    today = subprocess.run(["date", "+%Y-%m-%d"], capture_output=True, text=True).stdout.strip()
    last = dict(re.findall(r"<loc>" + re.escape(BASE) + r"([^<]*)</loc><lastmod>([^<]*)</lastmod>", old))
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages:
        pri = "1.0" if p == "index.html" else ("0.9" if p in ("reading-paths.html", "topics.html") else "0.7")
        freq = "daily" if p == "index.html" else "monthly"
        out.append(f"  <url><loc>{BASE}{p}</loc><lastmod>{last.get(p, today)}</lastmod>"
                   f"<changefreq>{freq}</changefreq><priority>{pri}</priority></url>")
    out.append("</urlset>")
    new = "\n".join(out) + "\n"
    if new != old:
        open("sitemap.xml", "w", encoding="utf-8").write(new)
        print(f"sitemap written: {len(pages)} urls")
    else:
        print("sitemap already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
