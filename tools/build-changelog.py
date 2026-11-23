#!/usr/bin/env python3
"""Generate CHANGELOG.md from the repository's own history.

Grouped by date, one line per commit, newest first. The archive has no release
tags — every push is a release — so the log is the changelog.

    python3 tools/build-changelog.py
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

LIMIT = 400


def commits():
    out = subprocess.run(
        ["git", "log", f"-{LIMIT}", "--date=short",
         "--format=%ad%x1f%s%x1f%h"],
        capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split("\x1f")
        if len(parts) == 3:
            rows.append(parts)
    return rows


def group(rows):
    days = {}
    for date, subject, sha in rows:
        days.setdefault(date, []).append((subject, sha))
    return days


def main():
    rows = commits()
    days = group(rows)
    total = subprocess.run(["git", "rev-list", "--count", "HEAD"],
                           capture_output=True, text=True).stdout.strip()
    lines = [
        "# Changelog",
        "",
        "Every change to the archive, newest first, generated from the repository history.",
        f"{total} commits. The site is deployed on every push to `main`.",
        "",
    ]
    for date in sorted(days, reverse=True):
        lines.append(f"## {date}")
        lines.append("")
        for subject, sha in days[date]:
            lines.append(f"- {subject} (`{sha}`)")
        lines.append("")
    text = "\n".join(lines)
    old = open("CHANGELOG.md", encoding="utf-8").read() if os.path.exists("CHANGELOG.md") else ""
    if text != old:
        open("CHANGELOG.md", "w", encoding="utf-8").write(text)
        print(f"changelog written: {len(rows)} entries across {len(days)} days")
    else:
        print("changelog already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
