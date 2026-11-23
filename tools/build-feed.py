#!/usr/bin/env python3
"""Regenerate feed.xml from the dossiers themselves.

The old feed was frozen at 162 entries, all dated 20 November, with nine titles
double-escaped so they displayed "&amp;" to the reader. This builds it from
data/claims.json and each page's git date, newest first.

    python3 tools/build-feed.py
    python3 tools/build-feed.py --check
"""
import html, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://drsamonline.github.io/LARGE_GLOBE/"
LIMIT = 1000   # the whole catalogue: a feed of 50 entries spans two days of a fast build
CHECK = "--check" in sys.argv


def git_date(path):
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ad", "--date=short",
                        "-1", "--", path], capture_output=True, text=True)
    d = r.stdout.strip()
    if d:
        return d
    r = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short", "--", path],
                       capture_output=True, text=True)
    return r.stdout.strip() or "2026-11-20"


def main():
    claims = json.load(open("data/claims.json"))["claims"]
    rows = []
    for c in claims:
        p = c["slug"] + ".html"
        if not os.path.exists(p):
            continue
        rows.append({
            "slug": c["slug"],
            "title": c["title"],
            "summary": c.get("standfirst", ""),
            "date": git_date(p),
            "verdict": c.get("verdict", ""),
        })
    rows.sort(key=lambda r: (r["date"], r["slug"]), reverse=True)
    rows = rows[:LIMIT]

    # titles in the ledger were stored HTML-escaped at some point; normalise first
    esc = lambda s: html.escape(html.unescape(s), quote=True)
    out = ['<?xml version="1.0" encoding="utf-8"?>',
           '<feed xmlns="http://www.w3.org/2005/Atom">',
           '  <title>The Larger World Archive</title>',
           '  <subtitle>Hidden-world claims, their sources, and what the evidence says.</subtitle>',
           f'  <link href="{BASE}feed.xml" rel="self"/>',
           f'  <link href="{BASE}"/>',
           f'  <id>{BASE}</id>',
           f'  <updated>{rows[0]["date"]}T06:00:00Z</updated>',
           '  <author><name>Dr. Sohil Momin</name><uri>https://github.com/drsamonline</uri></author>',
           '  <rights>CC BY-NC 4.0</rights>']
    for r in rows:
        url = f"{BASE}{r['slug']}.html"
        summary = f"{r['verdict']}. {r['summary']}".strip()
        out += ['  <entry>',
                f'    <title>{esc(r["title"])}</title>',
                f'    <link href="{url}"/>',
                f'    <id>{url}</id>',
                f'    <updated>{r["date"]}T06:00:00Z</updated>',
                f'    <summary>{esc(summary)}</summary>',
                '    <author><name>Dr. Sohil Momin</name></author>',
                '  </entry>']
    out.append('</feed>')
    new = "\n".join(out) + "\n"

    old = open("feed.xml", encoding="utf-8").read() if os.path.exists("feed.xml") else ""
    if CHECK:
        old_entries = len(re.findall(r"<entry>", old))
        if old_entries != len(rows) or "&amp;amp;" in old or old != new:
            print(f"feed.xml is stale: {old_entries} entries, expected {len(rows)}")
            return 1
        print(f"feed.xml has {len(rows)} current entries")
        return 0
    if new != old:
        open("feed.xml", "w", encoding="utf-8").write(new)
        print(f"feed written: {len(rows)} entries, newest {rows[0]['date']}")
    else:
        print("feed already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
