#!/usr/bin/env python3
"""Check the pages outside the archive: the landing page and the demo app.

Every other check in this repository globs `*.html` at the root, so the two pages
under `docs/` — the landing page and the playable demo — were never examined. This
covers them.

    python3 tools/check-docs.py
"""
import glob, os, re, sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
problems = []


def check_page(p):
    t = open(p, encoding="utf-8").read()
    name = p

    if "<title>" not in t or not re.search(r"<title>[^<]{10,}</title>", t):
        problems.append(f"{name}: missing or too-short title")
    else:
        title = re.search(r"<title>([^<]*)</title>", t).group(1)
        if len(title) > 70:
            problems.append(f"{name}: title is {len(title)} characters; search results cut at about 60")
        if re.search(r"[a-z][A-Z]", title):
            problems.append(f"{name}: title looks like two words run together — {title[:50]}")
    if 'name="viewport"' not in t:
        problems.append(f"{name}: no viewport meta")
    html_tag = re.search(r"<html[^>]*>", t)
    if not html_tag or "lang=" not in html_tag.group(0):
        problems.append(f"{name}: <html> has no lang")

    # malformed CSS colour: alpha appended outside the function
    for bad in re.findall(r"hsl\([^)]*\)[0-9a-f]{2}\b", t):
        problems.append(f"{name}: malformed colour value {bad}")

    # a licence claim in structured data must match the repository
    if "opensource.org/licenses/MIT" in t and os.path.exists("LICENSE"):
        lic = open("LICENSE", encoding="utf-8").read()[:400]
        if "MIT" not in lic:
            problems.append(f"{name}: structured data claims MIT; LICENSE is not MIT")

    # links and assets that do not exist
    for attr, val in re.findall(r'(href|src)="([^"]+)"', t):
        if val.startswith(("http", "mailto:", "data:", "#", "//")):
            continue
        if val.startswith("/LARGE_GLOBE/"):
            local = val[len("/LARGE_GLOBE/"):]
        elif val.startswith("/"):
            continue
        else:
            local = os.path.normpath(os.path.join(os.path.dirname(p), val.split("?")[0]))
        local = local.split("?")[0].split("#")[0]
        if local and not os.path.exists(local) and not local.endswith(".html") \
                and os.path.exists(local + ".html"):
            continue
        if not local or not os.path.exists(local):
            problems.append(f"{name}: {attr}=\"{val}\" does not exist")


def check_robots():
    for p in ("robots.txt", "docs/robots.txt"):
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        for url in re.findall(r"Sitemap:\s*(\S+)", t):
            if "//" in url.split("://", 1)[1]:
                problems.append(f"{p}: sitemap URL has a doubled slash — {url}")
            path = url.split("drsamonline.github.io/LARGE_GLOBE/")[-1]
            if path and not os.path.exists(path):
                problems.append(f"{p}: sitemap URL points at {path}, which is not in the repository")


def check_sitemaps():
    for p in glob.glob("sitemap.xml") + glob.glob("docs/sitemap.xml"):
        try:
            ET.parse(p)
        except ET.ParseError as e:
            problems.append(f"{p}: not well-formed XML — {e}")


def main():
    pages = glob.glob("docs/**/*.html", recursive=True)
    for p in pages:
        check_page(p)
    check_robots()
    check_sitemaps()
    print(f"docs: {len(pages)} page(s) checked")
    if problems:
        for p in problems[:25]:
            print("  problem:", p)
        print(f"{len(problems)} problem(s)")
        return 1
    print("  ok  titles, viewport, lang, colours, licence, local links, robots, sitemaps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
