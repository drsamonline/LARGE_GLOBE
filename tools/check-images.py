#!/usr/bin/env python3
"""Image hygiene: one command that keeps the galleries, the credits page and the
charts consistent with each other.

This exists because the same failure kept recurring: an audit removes figures,
the credits page and the charts are left describing the old set, and CI goes red
after the fact. Every step below is derived from the pages themselves, so running
this after any image change is enough.

    python3 tools/check-images.py            # verify only, exit 1 on a problem
    python3 tools/check-images.py --fix      # repair what it finds
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FIX = "--fix" in sys.argv
problems = []


def pages():
    return [p for p in glob.glob("*.html") if p != "credits.html"]


def figures():
    """(page, src) for every gallery figure on the site."""
    out = []
    pat = re.compile(r'<img src="(assets/img/(?:gallery|diagrams)/[^"]+)"[^>]*>.*?<figcaption>', re.S)
    for p in pages():
        t = open(p, encoding="utf-8").read()
        if "Maps, diagrams and images" not in t:
            continue
        for m in pat.finditer(t):
            out.append((p, m.group(1)))
    return out


def check_references(figs):
    """Every src on a page must exist, and every file must be referenced."""
    missing = [(p, s) for p, s in figs if not os.path.exists(s)]
    if missing:
        problems.append(f"{len(missing)} figure(s) point at files that do not exist: "
                        + ", ".join(s for _, s in missing[:5]))
    referenced = {s for _, s in figs}
    orphans = [p for d in ("assets/img/gallery", "assets/img/diagrams")
               for p in glob.glob(d + "/*")
               if "assets/img/" + os.path.relpath(p, "assets/img") not in referenced]
    if orphans:
        problems.append(f"{len(orphans)} image file(s) are not used by any page")
        if FIX:
            for p in orphans:
                os.remove(p)
            print(f"  removed {len(orphans)} orphan file(s)")


def check_blank():
    """A frame that saved empty is not an image. Catch it before a reader does."""
    try:
        from PIL import Image, ImageStat
    except ImportError:
        problems.append("Pillow is not installed, so the blank-frame test cannot run")
        return
    blank = []
    for p in glob.glob("assets/img/gallery/*.webp") + glob.glob("assets/img/*.webp") + glob.glob("assets/img/*.avif"):
        try:
            if ImageStat.Stat(Image.open(p).convert("L")).stddev[0] < 6:
                blank.append(p)
        except Exception:
            blank.append(p)
    if blank:
        problems.append(f"{len(blank)} blank or unreadable image(s): "
                        + ", ".join(os.path.basename(b) for b in blank[:5]))
        if FIX:
            for b in blank:
                name = os.path.basename(b)
                for f in pages():
                    t = open(f, encoding="utf-8").read()
                    if name not in t:
                        continue
                    t2 = re.sub(r'<figure><a href="https://commons[^"]*"[^>]*><img src="assets/img/gallery/'
                                + re.escape(name) + r'".*?</figure>', "", t, flags=re.S)
                    m = re.search(r'<div class="gallery no-toc"><h3 class="no-toc">Maps, diagrams and images'
                                  r'</h3><div class="gal-grid">(.*?)</div></div>', t2, re.S)
                    if m and "<figure" not in m.group(1):
                        t2 = t2.replace(m.group(0), "")
                    if t2 != t:
                        open(f, "w", encoding="utf-8").write(t2)
                if os.path.exists(b):
                    os.remove(b)
            print(f"  removed {len(blank)} blank image(s) and their figures")


def check_credits(figs):
    """credits.html must list exactly the figures the pages use."""
    t = open("credits.html", encoding="utf-8").read()
    listed = set(re.findall(r'<img src="(assets/img/[^"]+)"', t))
    thumb = {os.path.basename(x) for x in listed if "/thumb/" in x}
    used = {s for _, s in figs}
    missing = {s for s in used - listed if os.path.basename(s) not in thumb}
    stale = {s for s in listed if not os.path.exists(s)}
    if missing:
        problems.append(f"{len(missing)} figure(s) are not listed on credits.html")
    if stale:
        problems.append(f"{len(stale)} credits entr(y/ies) point at files that no longer exist")
    if FIX and (missing or stale):
        subprocess.run([sys.executable, "tools/build-credits.py"], check=False)


def check_counts():
    """The number a page prints must match what the site serves."""
    t = open("credits.html", encoding="utf-8").read()
    real = len(re.findall(r"<li><img", t))
    idx = open("index.html", encoding="utf-8").read()
    m = re.search(r"<p class=\"eyebrow\">([^<]+)</p>", idx)
    if m:
        claimed = re.search(r"([\d,]+) images", m.group(1))
        if claimed and int(claimed.group(1).replace(",", "")) != real:
            problems.append(f"index.html claims {claimed.group(1)} images; credits lists {real}")
            if FIX:
                idx = idx.replace(claimed.group(0), f"{real:,} images")
                open("index.html", "w", encoding="utf-8").write(idx)
                print(f"  index.html count corrected to {real:,}")


def check_dimensions():
    """Every image with a src must declare width and height, or the page jumps as it loads."""
    bad = 0
    for f in glob.glob("*.html"):
        t = open(f, encoding="utf-8").read()
        for m in re.finditer(r"<img[^>]*>", t):
            tag = m.group(0)
            if 'src="assets/' not in tag:
                continue
            if 'width=' not in tag or 'height=' not in tag:
                bad += 1
    if bad:
        problems.append(f"{bad} image(s) lack width/height and will shift the layout")


def check_pdf():
    """The stated page count must match the file that ships."""
    if not os.path.exists("assets/larger-world-archive.pdf"):
        return
    try:
        import pymupdf
        real = pymupdf.open("assets/larger-world-archive.pdf").page_count
    except Exception:
        return
    for f in ("print-edition.html", "README.md"):
        if not os.path.exists(f):
            continue
        t = open(f, encoding="utf-8").read()
        m = re.search(r"(\d[\d,]*)-page PDF|PDF — (\d[\d,]*) pages", t)
        claimed = (m.group(1) or m.group(2)) if m else None
        if claimed and int(claimed.replace(",", "")) != real:
            problems.append(f"{f} claims a {claimed}-page PDF; the file has {real}")


def check_pdf_bookmarks():
    """A 2,343-page book needs an outline; an empty one is a navigation failure."""
    path = "assets/larger-world-archive.pdf"
    if not os.path.exists(path):
        return
    try:
        import pymupdf
        d = pymupdf.open(path)
        n = len(d.get_toc())
    except Exception:
        return
    if n < 100:
        problems.append(f"the PDF has {n} bookmarks; a book this long needs an outline")


def check_epub():
    """The stated part count must match the EPUB that ships."""
    import zipfile
    path = "assets/larger-world-archive.epub"
    if not os.path.exists(path):
        return
    try:
        z = zipfile.ZipFile(path)
        real = len([n for n in z.namelist() if n.endswith(".xhtml")]) - 3
    except Exception:
        return
    t = open("print-edition.html", encoding="utf-8").read()
    m = re.search(r"same (\d[\d,]*) parts", t)
    if m and int(m.group(1).replace(",", "")) != real:
        problems.append(f"print-edition.html claims {m.group(1)} EPUB parts; the file has {real}")


def check_charts():
    r = subprocess.run([sys.executable, "tools/rebuild-charts.py", "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        problems.append("charts.html is out of step with the ledger")
        if FIX:
            subprocess.run([sys.executable, "tools/rebuild-charts.py"], check=False)
            print("  charts rebuilt")


def main():
    figs = figures()
    check_references(figs)
    check_blank()
    check_credits(figs)
    check_dimensions()
    check_counts()
    check_pdf()
    check_pdf_bookmarks()
    check_epub()
    check_charts()
    if not problems:
        print(f"images: {len(figs)} figures on {len(set(p for p, _ in figs))} pages, "
              f"credits and charts in step, no blanks")
        return 0
    for p in problems:
        print("  problem:", p)
    if not FIX:
        print("\nrun with --fix to repair")
    return 1


if __name__ == "__main__":
    sys.exit(main())
