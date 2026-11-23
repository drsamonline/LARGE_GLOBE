# How this archive is checked

Measured 23 November 2026. Everything below is a command in `tools/` that can be
re-run; nothing depends on a person remembering.

## The ten checks

| Command | What it proves |
|---|---|
| `python3 tools/check-all.py` | runs all ten, one verdict, about 40 seconds |
| `check-structure.py` | internal links, in-page and cross-page anchors, one `h1` per page, skip links, canonical tags, nav consistency |
| `check-size.py` | every page inside its byte budget |
| `check-images.py` | figures point at files that exist, no orphan files, no blank frames, credits list every figure, stated counts match the files, every image declares width and height, PDF page count and EPUB part count match the artefacts |
| `rebuild-shell.py --check` | header and footer identical to the canonical shell |
| `rebuild-charts.py --check` | charts agree with the ledger |
| `build-sitemap.py --check` | every page is in the sitemap |
| `build-feed.py --check` | the feed lists current entries |
| `stamp-css.py --check` | one stylesheet hash on every page |
| `update-readme.py --check` | no number in the README has drifted |
| `check-math.py` | the arithmetic claims in the mathematics dossiers still hold |

Generators rebuild their artefact from the repository: `build-credits.py`,
`build-changelog.py`, `build-paths.py`, `build-sitemap.py`, `build-feed.py`,
`update-readme.py`, `build-ledger.py`, `rebuild-charts.py`, `rebuild-shell.py`.

## The image audit

The archive holds 1,965 figures. Every one has been looked at on contact sheets, in
three passes, by a person rather than a heuristic.

| Pass | Reviewed | Wrong | Rate | What it caught |
|---|---|---|---|---|
| First | 1,992 | 401 | 20.1% | wholesale mismatches — a football team on a physics page, a reactor on a quantum page |
| Second | 1,914 | 33 | 1.7% | marginal mismatches — a band on a film page, a dancer on a mathematics page |
| Third | 120 | 2 | 1.7% | name collisions — a map of the Low Countries on a King Lear page, a cruise ship photographed at a pier called *Europa* on the page about Jupiter's moon |

Method: `build/sweep3.py` shuffles every figure with a fixed seed, draws 24 per
contact sheet with the dossier slug and caption beneath, and rasterises SVG diagrams
through Chromium so a diagram cannot pass as a blank cell. Sheets are reviewed four
at a time; a wrong figure is removed with its credit, the orphan file is deleted, and
the credits page is rebuilt in the same commit.

Automated scoring was tried and abandoned. Vocabulary overlap, a homograph detector
and a Commons-category check each found real errors, and each then went quiet while
wrong images remained: the failure mode is a caption word that matches the wrong
thing, which no word-level test can see.

## What the checks have caught

Fourteen defects, every one invisible on screen and most of them mine:

| Defect | Found by |
|---|---|
| A cache that could never expire, so returning readers kept old CSS forever | reading `sw.js` |
| `sitemap.xml` missing the homepage, the About page and a new page | `build-sitemap.py` |
| A feed frozen at 162 entries, all dated the same day, nine titles double-escaped | `build-feed.py` |
| 421 links pointing at anchors that did not exist | `check-structure.py` |
| 830 index rows with no `id` for those links to reach | the same check |
| A count reading `2,2,2,923` on 1,034 pages | `check-images.py` |
| A PDF page count overwritten by the site's own page count | `check-images.py` |
| An EPUB part count stale by 849 | `check-images.py` |
| Search blind to the verdict field it displayed | reading `search.html` |
| 6,700 images with no width or height, so the page jumped as it loaded | `check-images.py` |
| A blank hero image on a live page | the blank-frame test |
| The credits page dropping every figure after the first on a page | rebuilding it |
| A README claiming 117,000 words in one place and 364,000 in another | `update-readme.py` |
| A tool hard-coding my sandbox path, so CI could never pass | CI |

## What is not checked

- **Prose accuracy.** Facts are checked against the sources cited, not against the world.
- **External links** except on the weekly scheduled run (`check-links.py`).
- **EPUB validity** — `epubcheck` needs Java, which the build environment does not have; the EPUB is verified structurally only.
- **Accessibility beyond structure.** Contrast, focus and touch targets were audited once by hand; there is no automated gate.
