#!/usr/bin/env python3
"""Keep the README's numbers true.

The README drifted twice: it advertised 796 images when the site served 2,927, and
its own summary said 117,000 words while the body said 364,000. Every figure below
is computed from the repository, never typed.

    python3 tools/update-readme.py           # rewrite the numbers
    python3 tools/update-readme.py --check   # exit 1 if they disagree
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

CHECK = "--check" in sys.argv


def stats():
    claims = json.load(open("data/claims.json"))["claims"]
    urls = [u for c in claims for u in c["sources"]["urls"]]
    domains = {re.match(r"https?://([^/]+)", u).group(1) for u in urls if re.match(r"https?://([^/]+)", u)}
    credits = open("credits.html", encoding="utf-8").read()
    images = len(re.findall(r"<li><img", credits))
    photos = len(re.findall(r'<li><img src="assets/img/(?!diagrams)', credits))
    diagrams = images - photos
    pages = len(glob.glob("*.html"))
    words = 0
    for c in claims:
        p = c["slug"] + ".html"
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
        t = re.sub(r"<[^>]+>", " ", t)
        words += len(t.split())
    topics = len(re.findall(r"<tr>", open("topics.html", encoding="utf-8").read()))
    html_mb = sum(os.path.getsize(p) for p in glob.glob("*.html")) / (1024 * 1024)
    pdf = "assets/larger-world-archive.pdf"
    epub = "assets/larger-world-archive.epub"
    pdf_pages = None
    try:
        import pymupdf
        pdf_pages = pymupdf.open(pdf).page_count
    except Exception:
        pass
    epub_kb = os.path.getsize(epub) // 1024 if os.path.exists(epub) else None
    from collections import Counter
    verdicts = Counter(c.get("verdict", "") for c in claims)
    return {
        "verdicts": verdicts,
        "dossiers": len(claims), "sources": len(urls), "domains": len(domains),
        "images": images, "photos": photos, "diagrams": diagrams, "pages": pages,
        "words": words, "topics": topics, "html_mb": html_mb,
        "pdf_pages": pdf_pages, "epub_kb": epub_kb,
    }


def rewrite(s, st):
    subs = [
        (r"badge/dossiers-\d+-", f"badge/dossiers-{st['dossiers']}-"),
        (r"badge/linked%20sources-\d+-", f"badge/linked%20sources-{st['sources']}-"),
        (r"badge/images-\d+%20\(\d+%20photos%20%C2%B7%20\d+%20drawn\)",
         f"badge/images-{st['images']}%20({st['photos']}%20photos%20%C2%B7%20{st['diagrams']}%20drawn)"),
        (r"badge/pages-\d+%20static%20files", f"badge/pages-{st['pages']}%20static%20files"),
        (r"\*\*\d+ dossiers\. About [\d,]+ words\. [\d,]+ linked sources\. [\d,]+ images — [\d,]+ credited photographs and \d+ (?:original )?diagrams",
         f"**{st['dossiers']} dossiers. About {st['words']:,} words. {st['sources']:,} linked sources. "
         f"{st['images']:,} images — {st['photos']:,} credited photographs and {st['diagrams']} diagrams"),
        (r"\[\d+ topics\]", f"[{st['topics']} topics]"),
        (r"six labels, applied the same way across all \d+ dossiers — \d+ as \*live debate\*, \d+ as \*documented\*, \d+ as \*debunked\*, \d+ as \*fringe claim\*, \d+ as \*fiction\*, \d+ as \*open problem\*\.",
         "six labels, applied the same way across all {n} dossiers — {a} as *live debate*, {b} as *documented*, {c} as *debunked*, {d} as *fringe claim*, {e} as *fiction*, {f} as *open problem*.".format(n=st["dossiers"], a=st["verdicts"]["Live debate"], b=st["verdicts"]["Documented"], c=st["verdicts"]["Debunked"], d=st["verdicts"]["Fringe claim"], e=st["verdicts"]["Fiction"], f=st["verdicts"]["Open problem"])),
        (r"\*\*\d+ pages, [\d.]+ MB of HTML\*\*", f"**{st['pages']} pages, {st['html_mb']:.1f} MB of HTML**"),
        (r"[\d,]+ credited photographs, plus \d+ vector figures",
         f"{st['photos']:,} credited photographs, plus {st['diagrams']} vector figures"),
    ]
    if st["pdf_pages"]:
        subs.append((r"A \[\d+-page PDF, A5\]", f"A [{st['pdf_pages']}-page PDF, A5]"))
    if st["epub_kb"]:
        subs.append((r"a \[\d+ KB EPUB with a cover\]", f"a [{st['epub_kb']} KB EPUB with a cover]"))
    for pat, rep in subs:
        s = re.sub(pat, rep, s)
    return s


def main():
    st = stats()
    s = open("README.md", encoding="utf-8").read()
    new = rewrite(s, st)
    if CHECK:
        if new != s:
            print("README numbers are out of date — run tools/update-readme.py")
            for pat, _ in [(r"badge/dossiers-\d+-", ""), (r"\*\*\d+ dossiers", "")]:
                pass
            return 1
        print("README numbers match the repository")
        return 0
    if new != s:
        open("README.md", "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("README already current")
    print(f"  {st['dossiers']} dossiers · {st['sources']:,} sources · {st['domains']} domains · "
          f"{st['images']:,} images · {st['words']:,} words · {st['pages']} pages · {st['topics']} topics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
