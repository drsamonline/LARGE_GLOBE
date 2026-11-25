#!/usr/bin/env python3
"""Rebuild the print edition from the dossier pages, so the book matches the site.

The print edition was written as a separate document and had drifted: the site's pages
had gained sections the book did not have, and the book carried sections the site had
lost. This generates every part from the dossier's own body, in reading order.

    python3 tools/build-print.py
"""
import glob, html, json, os, re, sys

ROOT = "/scratch/work/repo"
os.chdir(ROOT)

THEME_ORDER = ["earth", "cosmos", "ancient", "mind", "anomalies", "states", "internet"]


def body_of(slug):
    """The article body: sections with their headings and paragraphs, plus sources."""
    t = open(slug + ".html", encoding="utf-8").read()
    m = re.search(r"<article[^>]*>(.*?)</article>", t, re.S)
    if not m:
        return None
    art = m.group(1)
    # keep h3 sections and their content; drop galleries, related strips, ctas, cite blocks
    for junk in ("gallery", "related", "openres", "cite", "pager", "cta-row", "path"):
        art = re.sub(rf'<div class="{junk}[^"]*">.*?</div>\s*(?=<(?:h3|h4|p|ul|div|section|/article))',
                     "", art, flags=re.S)
    art = re.sub(r"<figure.*?</figure>", "", art, flags=re.S)
    art = re.sub(r'<div class="cite">.*?</section>', "", art, flags=re.S)
    # the standfirst and the body paragraphs
    keep = re.findall(r"<h3[^>]*>.*?</h3>|<p[^>]*>.*?</p>|<ul class=\"srclist\">.*?</ul>|<h4>Sources for this page</h4>",
                      art, re.S)
    keep = [k for k in keep if "cite-foot" not in k]
    out = []
    for chunk in keep:
        if "Cite this page" in chunk or "cite-row" in chunk:
            continue
        out.append(chunk)
    return "\n".join(out)


def main():
    cl = json.load(open("data/claims.json"))
    claims = cl["claims"]
    by_slug = {c["slug"]: c for c in claims}
    si = json.load(open("search-index.json"))
    order = {d["u"][:-5]: i for i, d in enumerate(si["d"])}

    page = open("print-edition.html", encoding="utf-8").read()
    head_end = page.find("<section class=\"part\"")
    tail_start = page.find("</main>")
    if head_end < 0 or tail_start < 0:
        print("cannot find the parts region")
        return 1

    parts = []
    built = 0
    for c in claims:
        slug = c["slug"]
        body = body_of(slug)
        if not body or len(body) < 200:
            continue
        title = c["title"]
        verdict = c.get("verdict", "")
        note = c["label_text"] if not c.get("label_canonical") else ""
        vline = verdict + (f" — {note}" if note else "")
        parts.append(
            f'<section class="part" id="part-{slug}">\n'
            f'<h2 class="part-title">{html.escape(title)}</h2>'
            f'<p class="part-verdict">{html.escape(vline)}</p>\n'
            f'{body}\n</section>\n')
        built += 1

    # the contents list is rebuilt from the same set
    toc = "\n".join(f'<li><a href="#part-{c["slug"]}">{html.escape(c["title"])}</a></li>'
                    for c in claims if f'id="part-{c["slug"]}"' in "".join(parts))
    new = page[:head_end] + "".join(parts) + page[tail_start:]
    new = re.sub(r'<ol class="toc">.*?</ol>',
                 f'<ol class="toc">\n{toc}\n</ol>', new, flags=re.S)
    new = re.sub(r"<h2><span class=\"num\">Contents</span>\d+ parts</h2>",
                 f'<h2><span class="num">Contents</span>{built} parts</h2>', new)
    open("print-edition.html", "w", encoding="utf-8").write(new)
    print(f"print edition rebuilt: {built} parts, {len(new)//1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
