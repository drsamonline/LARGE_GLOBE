#!/usr/bin/env python3
"""Build reading-paths.html — twelve curated trails through the archive.

Each trail is a hand-picked sequence with a line on why the pages sit in that
order. The slugs are checked against search-index.json, so a trail can never
point at a page that does not exist.
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

TRAILS = [
    ("The shape of the Earth, in six pages",
     "Start with the argument the archive is named for. Each page takes one version of "
     "the claim seriously enough to test it, and the sequence ends where the evidence does.",
     ["larger-globe", "flat-earth", "hollow-earth", "ice-wall", "expanding-earth", "suns-stars"],
     ["Begin with the three theories that share a name but not an argument.",
      "Then the strongest version, and the one with the most careful proponents.",
      "The ice wall is the version with the least evidence and the most certainty.",
      "End on the sky, because the same reasoning is used there."]),

    ("How a claim gets tested",
     "Six claims that were testable, were tested, and failed in instructive ways. Read them "
     "together and the shape of a good test becomes visible.",
     ["cold-fusion", "polywater", "n-rays", "memory-of-water", "quantum-healing", "crystal-skulls"],
     ["Two chemistry claims, both announced with confidence.",
      "Two physics claims where the instrument was the problem.",
      "Two that were never really testable, which is why they survive."]),

    ("Where the evidence runs out",
     "Not every mystery is a debunking. These are pages where the record genuinely stops, and "
     "the archive says so rather than filling the gap.",
     ["voynich-manuscript", "oak-island", "dyatlov-pass", "somerton-man", "roanoke", "disappearances"],
     ["A document nobody can read.",
      "A hole nobody has finished digging.",
      "Two deaths and a colony, each with a real gap in the record."]),

    ("Fakes and honest errors",
     "A forgery and a mistake are different things, and the difference matters to how you read "
     "the rest of the archive.",
     ["giants", "feejee-mermaid", "cottingley-fairies", "vinland-map", "piri-reis-map", "kensington-runestone"],
     ["Objects made to deceive.",
      "Photographs made to deceive, and the people who believed them.",
      "Two documents that were real, and were read wrongly."]),

    ("Science correcting itself",
     "The archive cites peer-reviewed work, so it owes the reader an account of what that "
     "citation is worth.",
     ["replication-crisis", "p-hacking", "publication-bias", "peer-review-evidence", "paper-mills", "sokal-hoax"],
     ["What happens when studies are repeated.",
      "Why the published literature is skewed before anyone repeats it.",
      "What happens when the checks are gamed."]),

    ("Medicine's own mistakes",
     "A century of confident practice that did not work, and what ended each one.",
     ["four-humours", "bloodletting", "lobotomy", "phrenology", "hysteria", "trepanation"],
     ["The theory that lasted two thousand years.",
      "The treatment that killed more people than it cured.",
      "The diagnosis that described the doctor, not the patient."]),

    ("Myths everyone repeats",
     "Fifteen things you have probably been told, and what happens when you check.",
     ["ten-percent-brain", "tongue-map", "five-second-rule", "goldfish-memory",
      "shaving-hair-thicker", "cracking-knuckles"],
     ["Two that came from a misread paper.",
      "Two that came from a misread study design.",
      "Two that were settled by somebody counting."]),

    ("Places that were invented",
     "Six places that exist on maps and nowhere else, and what the maps were for.",
     ["tartarian", "atlantis-antarctica", "el-dorado", "lost-continents", "atlantis-thera", "atlantis-donana"],
     ["A whole continent invented from a cartographic habit.",
      "Atlantis, tested against three real places.",
      "The idea of a lost continent, which outlived every candidate."]),

    ("Documents that changed the argument",
     "Leaked files, declassified records and court exhibits: the pages where a document did the "
     "persuading rather than a theory.",
     ["panama-papers", "twitter-files", "pentagon-uap-programme", "1mdb-heist", "pfas-coverup", "libor-rigging"],
     ["Two leaks that changed policy.",
      "One programme that was funded because a senator asked.",
      "Two sets of internal papers that a company did not want read."]),

    ("Fiction that became a belief",
     "Stories written to frighten people, and the people who decided they were true.",
     ["backrooms", "slender-man-tulpa", "ted-the-caver", "momo-panic", "blue-whale-challenge", "petscop"],
     ["An image with no author.",
      "Two internet stories that left the internet.",
      "Two panics that reached parents before they reached evidence."]),

    ("The mathematics that will not close",
     "Six problems that a century of effort has not settled, each stated plainly and each "
     "checked numerically where checking is possible.",
     ["collatz-conjecture", "riemann-hypothesis", "abc-conjecture", "twin-prime-conjecture",
      "goldbach-conjecture", "p-versus-np"],
     ["A problem a child can state.",
      "Two that a proof would reorganise.",
      "Two where the numbers hold far beyond where anyone has proved."]),

    ("Conspiracies that turned out true",
     "The archive is not a debunking site. These are the plots that the record establishes, "
     "which is why the ones that fail are worth taking seriously.",
     ["proven-conspiracies", "iran-contra", "secret-tests", "fbi-mlk", "purdue-oxycontin"],
     ["What it takes for a conspiracy to be documented.",
      "Two operations run by governments against their own publics.",
      "One run by a company against its customers."]),
]


def main():
    si = json.load(open("search-index.json"))
    titles = {d["u"][:-5]: d["t"] for d in si["d"]}
    verdicts = {d["u"][:-5]: d.get("v", "") for d in si["d"]}

    missing = [(n, s) for n, _, slugs, _ in TRAILS for s in slugs if s not in titles]
    if missing:
        print("trails point at pages that do not exist:", missing)
        return 1

    blocks = []
    for name, lede, slugs, notes in TRAILS:
        items = []
        for i, s in enumerate(slugs):
            note = notes[i] if i < len(notes) else ""
            cls = {"Documented": "doc", "Debunked": "debunk", "Live debate": "debate",
                   "Fringe claim": "fringe", "Fiction": "fiction", "Open problem": "open"}.get(verdicts[s], "doc")
            items.append(
                '<li><a href="' + s + '.html">' + html.escape(titles[s]) + '</a> '
                '<span class="badge b-' + cls + '">' + html.escape(verdicts[s]) + '</span></li>')
        blocks.append(
            f'<section class="path"><h2>{html.escape(name)}</h2>'
            f'<p class="path-lede">{html.escape(lede)}</p>'
            f'<p class="path-how">{html.escape(" ".join(notes))}</p>'
            f'<ol class="path-list">{"".join(items)}</ol></section>')

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reading paths — twelve ways into the archive | The Larger World Archive</title>
<meta name="description" content="Twelve curated trails through 1,010 dossiers: the shape of the Earth, how a claim gets tested, where the evidence runs out, science correcting itself, and more.">
<link rel="stylesheet" href="assets/style.css?v=1">
<link rel="canonical" href="https://drsamonline.github.io/LARGE_GLOBE/reading-paths.html">
<meta name="theme-color" content="#0b0e14">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
</head>
<body>
<main class="wrap" id="main">
<article>
<div class="article-head">
<p class="kicker">Reading paths</p>
<h1>Twelve ways into the archive.</h1>
<p class="standfirst">A thousand dossiers is not a reading list. These are twelve short sequences, six pages each, chosen so that the argument builds rather than repeats — and every one of them can be read in a sitting.</p>
</div>
<p>If you only have twenty minutes, take the first trail. If you want to know how the archive decides anything, take the second and the fifth together.</p>
{''.join(blocks)}
<div class="cta-row"><a class="btn solid" href="reading-guide.html">The reading guide</a><a class="btn" href="topics.html">Browse the register</a><a class="btn" href="random.html">Open a page at random</a></div>
</article>
</main>
</body></html>'''

    old = open("reading-paths.html", encoding="utf-8").read() if os.path.exists("reading-paths.html") else ""
    open("reading-paths.html", "w", encoding="utf-8").write(page)
    print(f"reading-paths.html written: {len(TRAILS)} trails, "
          f"{sum(len(t[2]) for t in TRAILS)} links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
