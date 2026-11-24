#!/usr/bin/env python3
"""Rebuild every number on charts.html from the data, not from memory.

Sources of truth: data/claims.json (labels, themes, sources) and credits.html
(the licence of every image). Run with --check to fail when the page has drifted.

    python3 tools/rebuild-charts.py
    python3 tools/rebuild-charts.py --check
"""
import json, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

LEDGER = json.load(open("data/claims.json", encoding="utf-8"))
CLAIMS = LEDGER["claims"]

LABEL_ORDER = [("b-doc", "Documented", "#7fae7a"),
               ("b-debate", "Live debate", "#7d9ec4"),
               ("b-fringe", "Fringe", "#d3a95f"),
               ("b-debunk", "Debunked", "#c96a5a"),
               ("b-fiction", "Fiction", "#8f723c"),
               ("b-open", "Open problem", "#8b8477")]
THEMES = [("earth", "Earth"), ("cosmos", "Cosmos"), ("ancient", "Ancient world"),
          ("mind", "Mind"), ("anomalies", "Anomalies"), ("states", "States"), ("internet", "Internet")]

lab_counts = Counter(c["label_class"] for c in CLAIMS)
theme_counts = Counter(c["theme_id"] for c in CLAIMS)
src_counts = [(c["title"], c["sources"]["count"]) for c in CLAIMS]
total_sources = sum(s for _, s in src_counts)
avg_sources = total_sources / max(len(CLAIMS), 1)

# the master list has its own four-verdict tally, over a different population
ml = open("master-list.html", encoding="utf-8").read()
VERDICTS = [("doc", "Documented", "#7fae7a"), ("deb", "Live debate", "#7d9ec4"),
            ("fri", "Fringe", "#d3a95f"), ("deb2", "Debunked", "#c96a5a")]
verdict_counts = Counter()
for code, _, _c in VERDICTS:
    verdict_counts[code] = len(re.findall(r'<td class="v %s">' % code, ml))
claims_total = sum(verdict_counts.values())

# licences, from the credits page
credits = open("credits.html", encoding="utf-8").read()
lic = Counter()
for m in re.finditer(r'<span class="u">(.*?)</span>', credits, re.S):
    bits = [b.strip() for b in re.sub(r"<[^>]+>", "", m.group(1)).split("·")]
    if len(bits) >= 2:
        lic[bits[1]] += 1
images_total = sum(lic.values())

FONT = "ui-sans-serif,system-ui,sans-serif"
MONO = "ui-monospace,Menlo,monospace"


def bar_chart(rows, colour, label_x, bar_x, max_w, aria):
    """rows: [(label, value)] — same markup the page already uses."""
    top = max(v for _, v in rows) or 1
    h = 14 + 32 * len(rows) + 12
    out = [f'<svg viewBox="0 0 760 {h}" role="img" aria-label="{aria}">']
    for i, (label, value) in enumerate(rows):
        y = 14 + i * 32
        w = max(2, round(max_w * value / top))
        out.append(f'<text x="{label_x}" y="{y + 13:.1f}" text-anchor="end" font-size="12.5" '
                   f'fill="#b9b2a2" font-family="{FONT}">{label}</text>')
        out.append(f'<rect x="{bar_x}" y="{y}.0" width="{w}" height="16" fill="{colour}" opacity=".85"/>')
        out.append(f'<text x="{bar_x + w + 10}" y="{y + 13:.1f}" font-size="12" fill="#8b8477" '
                   f'font-family="{MONO}">{value}</text>')
    out.append("</svg>")
    return "\n".join(out)


def stacked_bar(counts, order, total_label):
    segs = [(name, counts.get(k, 0), col) for k, name, col in order if counts.get(k, 0)]
    total = sum(v for _, v, _ in segs) or 1
    out = [f'<svg viewBox="0 0 760 64" role="img" aria-label="{total_label}">', "<g>"]
    x = 0.0
    for _, value, col in segs:
        w = 760 * value / total
        out.append(f'<rect x="{x:.1f}" y="8" width="{w:.1f}" height="34" fill="{col}"/>')
        out.append(f'<text x="{x + w / 2:.0f}" y="32" text-anchor="middle" font-size="13" '
                   f'fill="#0b0e14" font-family="{FONT}">{value}</text>')
        x += w
    out.append("</g>")
    lx = 16
    for k, name, col in order:
        if not counts.get(k):
            continue
        out.append(f'<g transform="translate({lx},48)"><rect width="9" height="9" fill="{col}" y="2"/>'
                   f'<text x="15" y="10" font-size="11.5" fill="#8b8477" font-family="{FONT}">{name}</text></g>')
        lx += 26 + 6.6 * len(name)
    out.append("</svg>")
    return "\n".join(out)


def stacked_labels():
    """The four-to-six segment label bar, rebuilt with one segment per class."""
    segs = [(n, lab_counts.get(k, 0), col) for k, n, col in LABEL_ORDER if lab_counts.get(k, 0)]
    total = sum(v for _, v, _ in segs) or 1
    out = [f'<svg viewBox="0 0 760 64" role="img" aria-label="Distribution of the {len(CLAIMS)} dossiers across the evidence labels">',
           "<g>"]
    x = 0.0
    for _, value, col in segs:
        w = 760 * value / total
        out.append(f'<rect x="{x:.1f}" y="8" width="{w:.1f}" height="34" fill="{col}"/>')
        out.append(f'<text x="{x + w / 2:.0f}" y="32" text-anchor="middle" font-size="13" '
                   f'fill="#0b0e14" font-family="{FONT}">{value}</text>')
        x += w
    out.append("</g>")
    lx = 16
    for k, name, col in LABEL_ORDER:
        if not lab_counts.get(k):
            continue
        out.append(f'<g transform="translate({lx},48)"><rect width="9" height="9" fill="{col}" y="2"/>'
                   f'<text x="15" y="10" font-size="11.5" fill="#8b8477" font-family="{FONT}">{name}</text></g>')
        lx += 26 + 6.6 * len(name)
    out.append("</svg>")
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    page = open("charts.html", encoding="utf-8").read()
    orig = page

    # 1. at a glance
    glance = {
        "Dossiers": len(CLAIMS),
        "Claims in the master list": len(re.findall(r'<td class="v ', open("master-list.html", encoding="utf-8").read())),
        "Source entries": total_sources,
        "Credited images": images_total,
        "Average sources per dossier": f"{avg_sources:.1f}",
    }
    for k, v in glance.items():
        page = re.sub(rf"(<dt>{re.escape(k)}</dt><dd>)[^<]*(</dd>)", rf"\g<1>{v}\g<2>", page)

    # 3. theme sizes
    themes = [(name, theme_counts.get(tid, 0)) for tid, name in THEMES]
    themes = [(n, v) for n, v in themes if v]
    page = re.sub(r'<svg viewBox="0 0 760 \d+" role="img" aria-label="A bar chart titled">\s*<text x="158"[^>]*>Earth</text>.*?</svg>',
                  bar_chart(themes, "#d3a95f", 158, 170, 504,
                            "Dossiers per theme"), page, flags=re.S)

    # 3b. the label section: two populations, two charts, regenerated whole
    doss_bits = ", ".join(f"{lab_counts[k]} {name.lower()}" for k, name, _ in LABEL_ORDER if lab_counts.get(k))
    claim_bits = ", ".join(f"{verdict_counts[k]} {name.lower()}" for k, name, _ in VERDICTS if verdict_counts.get(k))
    section = (
        '<h2>Where the archive lands</h2>\n'
        '<p class="section-intro">Two populations, two charts, and they are not supposed to agree. '
        f'The <a href="master-list.html">master list</a> catalogues {claims_total} claims; the archive holds '
        f'{len(CLAIMS)} dossiers. A claim can be catalogued as fringe and written up as a live debate once the '
        'argument turns out to be closer than it looked, and the reverse happens too. The point of both charts is '
        'not that most claims fail — it is that the labels are used at all, including on comfortable claims.</p>\n'
        f'<h3>The {claims_total} claims in the master list, by verdict</h3>\n'
        '<figure class="fig">\n' + stacked_bar(verdict_counts, VERDICTS, f"Distribution of the {claims_total} catalogued claims across four verdicts") + '\n'
        f'<figcaption>{claims_total} claims: {claim_bits}. Filter them on the '
        '<a href="master-list.html">master list</a>.</figcaption>\n</figure>\n'
        f'<h3>The {len(CLAIMS)} dossiers, by their evidence label</h3>\n'
        '<figure class="fig">\n' + stacked_bar(lab_counts, LABEL_ORDER, f"Distribution of the {len(CLAIMS)} dossiers across the evidence labels") + '\n'
        f'<figcaption>{len(CLAIMS)} dossiers: {doss_bits}. A dossier label is set when the page is written, so it '
        'can be narrower than the catalogue verdict.</figcaption>\n</figure>'
    )
    page = re.sub(r'<h2>Where the archive lands</h2>.*?(?=</section>)', section + "\n", page, flags=re.S)

    # 4. licence sizes
    lics = lic.most_common(8)
    page = re.sub(r'<svg viewBox="0 0 760 \d+" role="img" aria-label="A bar chart titled">\s*<text x="158"[^>]*>CC BY-SA</text>.*?</svg>',
                  bar_chart(lics, "#7d9ec4", 158, 170, 504,
                            "Images by licence"), page, flags=re.S)

    # 5. longest source lists
    longest = sorted(src_counts, key=lambda t: -t[1])[:10]
    longest = [(t if len(t) <= 30 else t[:29] + "…", n) for t, n in longest]
    page = re.sub(r'<svg viewBox="0 0 760 \d+" role="img" aria-label="A bar chart titled">\s*<text x="238"[^>]*>.*?</text>.*?</svg>',
                  bar_chart(longest, "#d3a95f", 238, 250, 424,
                            "The ten dossiers with the longest source lists"), page, flags=re.S)

    # 5b. the thinnest-dossiers sentence
    thin = sorted(src_counts, key=lambda t: t[1])[:3]
    thin_txt = "; ".join(f"{t} ({n})" for t, n in thin)
    page = re.sub(r"Source entries per page\. The thinnest dossiers are .*? A short list",
                  f"Source entries per page. The thinnest dossiers are {thin_txt}. A short list", page, flags=re.S)

    # 6. generated line
    import datetime
    today = datetime.date.today().strftime("%-d %B %Y")
    page = re.sub(r"Generated \d+ \w+ \d{4} from data/claims\.json and credits\.html",
                  f"Generated {today} from data/claims.json and credits.html", page)

    if check:
        # the generated-date line changes every day, so comparing it byte-for-byte
        # made this check fail on the day after every commit. Compare everything else.
        def stable(t):
            return re.sub(r"Generated \d+ \w+ \d{4} from", "Generated TODAY from", t)
        if stable(page) != stable(orig):
            print("charts.html is out of step with the ledger — run tools/rebuild-charts.py")
            sys.exit(1)
        print("charts.html is in step")
        return

    open("charts.html", "w", encoding="utf-8").write(page)
    print(f"dossiers {len(CLAIMS)} · sources {total_sources} (avg {avg_sources:.1f}) · images {images_total}")
    print("labels:", dict(lab_counts))
    print("themes:", dict(theme_counts))
    print("changed" if page != orig else "no change")


if __name__ == "__main__":
    main()
