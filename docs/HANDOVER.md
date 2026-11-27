# Handover — The Larger World Archive

State at commit `d1d48e993` (27 November 2026). Everything here is measured, not estimated.

## What this repository is

A static site of 1,010 evidence dossiers, published to GitHub Pages from `main`. No build
step for the site itself: the HTML in the repository root is the site. The PDF, EPUB, credits,
charts, feed and sitemap are generated from `data/claims.json` and the pages.

- Live: https://drsamonline.github.io/LARGE_GLOBE/
- Branch: `main` (Pages deploys from it on every push)

## Current numbers

| Measure | Value |
|---|---|
| Dossiers | 1,010 |
| Sources | 4,644 |
| Distinct source domains | 267 |
| archive.org primary sources added | 336 |
| Dossiers citing only Wikipedia | 425 |
| Images | 2,985 (1,965 figures on 1,008 pages) |
| Words | 882,407 |
| PDF | 2,211 A5 pages, 1,012 bookmarks |
| EPUB | 1,010 chapters |
| Checks in `tools/check-all.py` | 11, all passing |

## The work in progress: breaking the Wikipedia monocle

The archive's weakest point is that its sourcing was encyclopaedia-shaped. The current job is
to give every dossier at least one source that is **not** Wikipedia — ideally the primary
document the claim rests on.

Progress: 838 → 425 Wikipedia-only dossiers, 413 converted, 4,223 → 4,644 sources.

The 425 is an over-count of the real gap. 122 of those pages already link an archive.org, DOI
or JSTOR item from their further-reading block; they are only Wikipedia-sourced in
`data/claims.json`. Eight pages met in the first three batches were exactly this case
(`expanding-earth`, `manna-machine`, `polyvagal`, `tired-light`, `cambrian-explosion`,
`damascus-steel`, `gunung-padang`, `mast-cell-activation`) and were left alone rather than cited
twice. Whether to promote those links into `sources.urls`, or to measure the gap from the pages
instead of the ledger, is undecided. The real gap is 366 pages.

### Method that works

1. Read the Wikipedia article title the page already cites: `c['sources']['urls'][0]` →
   `/wiki/<Article>`.
2. Search archive.org with **that title**, not the page's own title:
   `https://archive.org/advancedsearch.php?q=title:(<Article>) AND mediatype:(texts)`
   Page titles match words; article titles match subjects.
3. Read the returned titles and pick the one that is the same subject. Reject adjacent
   subjects even when the words match.
4. Verify before writing: `https://archive.org/metadata/<identifier>` must return a
   `metadata` block.
5. Insert one `<li>` into `ul.srclist` on the page and append the URL to
   `data/claims.json` → `sources.urls`, then set `sources.count`.

### Method that does not work

Automating steps 3–4 destroys quality. A script matching on 80% word overlap ran 25 pages and
produced three additions, two wrong: the AI box experiment matched *Hokuto no Ken 5* for the
Super Nintendo, and the alignment tax matched a self-published tract on "sovereign
resonance". Reverted. A third of automated matches are wrong, and a wrong citation on a page
about evidence is worse than no citation.

### Sample from the real gap, not the ledger

The ledger's Wikipedia-only list includes pages whose further-reading block already cites a
non-Wikipedia source. Sampling from it wastes a batch: in the first three batches eight of the
78 sampled pages were this case. Filter first — page body must contain no
`archive.org/details/`, `doi.org` or `jstor.org` — and the pool is 146 pages rather than 425.

### Sampling matters

Scanning the list in order keeps returning pages already done. Sample at intervals instead:
`w[::max(1,len(w)//26)][:26]` finds fresh pages. Throughput with that change is 10–15 per
batch instead of 2–5.

## Per-batch loop

```
cd /scratch/work/repo && git fetch -q origin && git reset --hard -q origin/main   # pod rollbacks
# 1. search 26 sampled pages, print candidates
# 2. verify + write the batch in one pass
python3 tools/rebuild-charts.py
python3 tools/update-readme.py
python3 tools/check-all.py --fast      # must print "all 11 checks pass"
python3 tools/check-images.py
git add -A && git commit -m "..." && git push origin main
gh api repos/drsamonline/LARGE_GLOBE/actions/runs --jq '.workflow_runs[0:3][]|{name,conclusion}'
```

All three workflows must read `success` before the batch is done: `check`, `Build + deploy`,
`pages build and deployment`.

## Hazards

| Hazard | What to do |
|---|---|
| Sandbox rolls back to an old snapshot | `git log --oneline -1` at the start of every batch. A commit from months ago means reset to `origin/main` before editing |
| `write_file` creates root-owned files | Copy to `/tmp`, patch, `rm` the original, copy back |
| Wikipedia API rate-limits | Slow to ~1.3 s between calls, or skip verification and add no source that batch |
| Removing figures changes ledger counts | Rebuild charts in the same commit |
| `rebuild-charts.py --check` is date-sensitive | It normalises the "Generated" line; keep that normalisation |
| Large pushes occasionally fail | A plain retry of `git push origin main` has always worked |
| A `--depth 1` clone breaks two checks | `build-feed.py` dates every entry from its first-publication commit, so a shallow clone dates all 1,000 entries to today and the feed check fails on a file that was never wrong. Clone with full history, or `git fetch --unshallow`, before trusting `feed` or `README` checks |

## Generators

| Script | Builds |
|---|---|
| `tools/build-print.py` | `print-edition.html` from the dossier bodies — the book cannot disagree with the site |
| `tools/rebuild-charts.py` | `charts.html` and the ledger |
| `tools/update-readme.py` | The numbers block in `README.md` |
| `tools/build-credits.py` | `credits.html` |
| `tools/build-sitemap.py`, `build-feed.py` | `sitemap.xml`, `feed.xml` |
| `tools/stamp-css.py` | CSS hash for the service worker cache |
| `tools/rebuild-shell.py` | The shared page shell |
| `tools/build-paths.py`, `build-changelog.py` | `reading-paths.html`, `CHANGELOG.md` |

## Decisions already taken

| Decision | Outcome |
|---|---|
| Topics not set on the repository | Dropped; the description and homepage are enough |
| Demo site | Never published; `deploy_path: ""` with a `check-docs.py` guard |
| KDP paperback | Deferred; the PDF and EPUB are enough |
| Hindi and audio editions | Cancelled |
| Depth vs breadth | Expand existing dossiers; no new pages |
| Sourcing | One non-Wikipedia source per page, verified, curated by hand |

## What is left

| Job | Size |
|---|---|
| Finish the sourcing pass | 425 in the ledger, of which 303 have no non-Wikipedia link on the page at all; ~20 batches at 6–15 per batch |
| Ledger drift | 47 pages list 56 sources the page does not show, all in one direction: `data/claims.json` over-counts. No page shows a source the ledger omits. `dutch-disease`, `sugar-hyperactivity` and `2008-bailouts` were fixed by hand on 27 November; the rest need a decision — write the missing `<li>`, or drop the URL from the ledger. The list: 2008-bailouts, ai-bubble, ai-hallucination, alcohol-brain-cells, anunnaki, aztlan-utah, barbie-red-pill, blue-whale-challenge, bosnian-pyramids, bowery-hidden-army, chewing-gum-seven-years, chimera (and 37 more — find them by comparing each page's `ul.srclist` `<li>` count with `sources.urls`) |
| Accessibility beyond structure | Medium: screen-reader semantics, landmarks, skip targets |
| Image weight | 2,985 images at ~90 MB; AVIF and `srcset` would cut it substantially |
| Search filters | Small: by verdict, theme, year |
| Weekly dead-link run | `tools/check-links.py` exists; never reviewed |

## Reproduce the checks

```
python3 tools/check-all.py --fast    # 11 checks, ~45 s
python3 tools/check-images.py        # figures, credits, charts in step
python3 tools/check-epub.py          # EPUB structure
python3 tools/check-structure.py     # 1,038 pages, 0 problems
```
