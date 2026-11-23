#!/usr/bin/env python3
"""Rebuild credits.html from the credits printed on every dossier page.

Each figure carries author, licence and a source link in its caption. This
collects them into one page — image, author, licence link, and the dossier it
appears on — so the credits cannot drift from the pages.

    python3 tools/build-credits.py
"""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FIG = re.compile(r'<img src="(assets/img/(?:gallery/|diagrams/|[a-z0-9\-]+\.(?:avif|webp|jpg|png))[^"]*)"[^>]*>'
                 r'.*?<figcaption>(.*?)<span class="credit">(.*?)</span>', re.S)
LINK = re.compile(r'<a href="([^"]+)"')


def titles():
    out = {}
    for p in glob.glob("*.html"):
        if p == "credits.html":
            continue
        t = open(p, encoding="utf-8").read()
        m = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)
        out[p] = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else p[:-5]
    return out


def entries():
    seen, rows = set(), []
    for p in sorted(glob.glob("*.html")):
        if p == "credits.html":
            continue
        t = open(p, encoding="utf-8").read()
        if '<figcaption>' not in t:
            continue
        for m in FIG.finditer(t):
            src = m.group(1)
            if src in seen:
                continue
            seen.add(src)
            raw = m.group(3)
            lk = LINK.search(raw)
            url = lk.group(1) if lk else ""
            txt = re.sub(r"<[^>]+>", "", raw).replace("·", "|")
            parts = [x.strip() for x in txt.split("|") if x.strip()]
            author = html.unescape(parts[0]) if parts else "Unknown"
            lic = html.unescape(parts[1]) if len(parts) > 1 else "licence"
            rows.append({"src": src, "author": author, "lic": lic, "url": url, "page": p})
    return rows


def dims(path):
    """Intrinsic size, so the credits grid reserves its boxes."""
    try:
        if path.endswith(".svg"):
            head = open(path, encoding="utf-8", errors="ignore").read(600)
            m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', head)
            if m:
                return round(float(m.group(1))), round(float(m.group(2)))
            return 200, 200
        from PIL import Image
        with Image.open(path) as im:
            w, h = im.size
        if w > 200:
            h = round(200 * h / w)
            w = 200
        return w, h
    except Exception:
        return 200, 200


def render(rows, ttl):
    items = []
    for r in rows:
        lic = (f'<a href="{r["url"]}" rel="noopener">{html.escape(r["lic"])}</a>'
               if r["url"] else html.escape(r["lic"]))
        items.append(
            f'<li><img src="{r["src"]}" alt="" loading="lazy" decoding="async" '
            f'width="{dims(r["src"])[0]}" height="{dims(r["src"])[1]}"><div>'
            f'<span class="t">{os.path.basename(r["src"])}</span>'
            f'<span class="u">{html.escape(r["author"])} · {lic} · '
            f'<a href="{r["page"]}">{html.escape(ttl.get(r["page"], r["page"]))}</a></span></div></li>')
    return "\n".join(items)


def main():
    t = open("credits.html", encoding="utf-8").read()
    rows = entries()
    ttl = titles()
    photos = sum(1 for r in rows if "/diagrams/" not in r["src"])
    drawn = len(rows) - photos
    body = render(rows, ttl)
    t = re.sub(r'(<ul class="creditgrid">).*?(</ul>)', r"\1\n" + body + r"\n\2", t, flags=re.S)
    t = re.sub(r"\d[\d,]* photographs · \d+ drawn figures", f"{photos:,} photographs · {drawn} drawn figures", t)
    open("credits.html", "w", encoding="utf-8").write(t)
    print(f"credits: {len(rows)} entries ({photos:,} photographs, {drawn} diagrams)")


if __name__ == "__main__":
    main()
