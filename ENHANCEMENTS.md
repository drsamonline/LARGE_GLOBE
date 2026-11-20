# Enhancement list — The Larger World Archive

An audit of all 170 pages, followed by everything worth changing, ordered by what it buys you per hour spent. Items marked **shipped** are already in this repository as of 19 November 2026; the rest are written so they can be applied without redesigning anything.

Measured baseline after the November 2026 expansion: 183 HTML pages (5.1 MB), 162 dossiers, ~117,000 words, 166 AVIF photographs plus 18 original SVG figures, 3,220 citations to 1,151 distinct URLs across 299 domains, 992 search records, one stylesheet, one inline search script, zero runtime dependencies.

---

## 0. Shipped in the November 2026 expansion

The audit found that the five collections name **830 topics** while the archive had written **150** of them. This pass closed part of that gap and built the instrument for closing the rest.

| # | Change | Why |
|---|---|---|
| 1 | **Twelve new dossiers**, written to the existing template and voice: cold fusion, the placebo effect, learning styles, growth mindset, the aquatic ape, Snowball Earth, the dinosaur extinction, panpsychism, the free energy principle, polyvagal theory, fast radio bursts, magnetoreception | Six of the twelve are topics the collections already named and labelled but had never written. Each is sourced to 4–5 links, carries an at-a-glance panel, an answer box and a pager entry. |
| 2 | **Twelve original SVG diagrams**, one per new dossier, in the site's own palette — the replication ledger for cold fusion, the crossover plot learning styles never produced, the Cryogenian timeline, the K–Pg boundary column, the Markov blanket, the dispersion sweep | A scientific archive with no figures is a bibliography. These are drawn from the numbers on the page, not stock art, so the licence question disappears. |
| 3 | **Six figures added to existing dossiers** — the Hubble tension, dark matter, the Great Filter, turbulence, ego depletion, AMOC | The most-visited pages were the least illustrated. Each figure makes the argument visible: two rulers, a flat rotation curve, three filter placements, a −5/3 slope, four shrinking effect sizes, one overturning loop. |
| 4 | **Six expansion sections** — "What would change the label" on those same pages | Every dossier states a verdict; almost none stated what would overturn it. That is the difference between a reference work and an opinion column. |
| 5 | **`topics.html` — the topic register**, 726 rows, grouped by collection and theme, each keeping the label the collection gave it | The single most important structural addition: it is the work queue, and it is the anti-duplication map. A topic on that page is unwritten by definition; a topic that has become a dossier is removed from it. |
| 6 | **Counts recomputed from data, not edited by hand** — dossiers, sources, figures, per-theme tallies, the theme bar chart, the search index, the sitemap, the print edition's table of contents | The site claimed 150 dossiers in twenty places. It now derives them. |
| 7 | **Search index and collections retargeted** — 12 new records, and the collection rows whose topics now have pages point at the dossier instead of the collection | No duplication: a promoted topic leaves the collection link and appears as a dossier. |
| 8 | **Print edition extended** to 164 parts, with the twelve new dossiers in reading order and in its contents list | Otherwise the single-volume edition silently omits everything added after it was generated. |
| 9 | **Sources page extended** with section 13, the 48 new citations, deduplicated against everything already listed | The bibliography has to stay the count the footer claims. |
| 10 | **Sixty-two theme-list rows repaired** — each had an empty `src` and an empty summary, so a third of the archive's theme shelves showed a blank tile and a bare title | The images existed all along; the build that generated the page had simply failed to fill them. Each row now carries its dossier's hero image and the first line of its standfirst. |
| 11 | **Topic register regrouped by theme**, not by row number, so a heading no longer sits above rows that belong to a different shelf | The first version inherited the collections' interleaved order, which made the page misleading. |

What this pass deliberately did **not** do: no photographs were added to the twelve new dossiers, because the archive cannot licence what it cannot credit, and a diagram it drew itself is honest about its provenance. Sourcing photographs for them is item 1 of the next list.

## 0b. Shipped in the second pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **Twelve credited photographs** for the new dossiers, sourced from Wikimedia Commons with licence and author recorded per file | The archive's pattern is a credited photograph at the top and a diagram in the body. The new pages had inverted it. Cold fusion now opens on a vial of palladium pellets; Snowball Earth on the Elatina tillite; the dinosaur extinction on the Stevns Klint boundary; magnetoreception on a robin. |
| 2 | **The diagrams moved into the body** as inline figures, so each page carries both | Nothing was discarded: the twelve SVGs are now the second figure on their own page. |
| 3 | **`citation_*` meta tags** on all 162 dossiers — title, author, publication and online date, abstract URL | This is what Google Scholar reads. A reference library that Scholar cannot see is a blog. |
| 4 | **`random.html`**, linked from every footer | A 162-page archive is navigated by wandering, and there was no way in except the index. |
| 5 | **Keyboard navigation in search** — ↓/↑ through results, Esc to clear | The best tool on the site was mouse-only. |
| 6 | **`rel="noopener"` on all 2,841 external links**, not just the support band | Cheap hardening on every outbound citation. |
| 7 | **CI gate** — `tools/check-structure.py`, `check-size.py`, `check-links.py`, wired to `.github/workflows/check.yml` | 184 pages, 0 problems at the time of writing. Internal links, assets, one `h1` per page, canonical present, no empty `src`, and a per-page size budget now fail the build instead of shipping. |
| 8 | **Weekly dead-link sweep** against every cited URL, uploading a report artifact | Closes the gap this session left: the 48 new DOIs were never machine-checked. |
| 9 | **Credits page extended** to 178 photographs with author, licence and source for each | Every image on the site now has a line on that page. |

## 0c. Shipped in the third pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **162 per-dossier share cards** (`assets/og/<slug>.jpg`, 1200×630, 32 KB average) and `og:image` repointed per page | Every dossier previously shared as the same generic card. Now a link to Cold Fusion shows Cold Fusion, its label and its first sentence. |
| 2 | **Breadcrumbs on every dossier**, visible and as `BreadcrumbList` JSON-LD | Index › theme › dossier, which is how the site is actually navigated and how a crawler learns the hierarchy. |
| 3 | **A citation block** — APA, MLA, Chicago and BibTeX, each with a copy button, plus the last-reviewed date and a link to the corrections policy | A reference work that cannot be cited in a footnote is only half a reference work. |
| 4 | **A related strip** — four neighbours, preferring the same label inside the same theme | 162 pages that previously linked to each other only through the 100-item nav. |
| 5 | **`corrections.html`** — five kinds of error ranked by seriousness, how to report one, and the annotate-first rule | The archive asks to be trusted on its attributions; it now states what happens when one is wrong. |
| 6 | **Atom feed** (`feed.xml`, 162 entries) linked from every page | Nothing announced that the archive grew. |
| 7 | **`lastmod` from git history** in the sitemap, not the build date | The one crawl signal that is actually earned. |
| 8 | **CI extended** — every dossier must keep its breadcrumbs, citation block, related strip and a share card that exists on disk | 185 pages, 0 problems. The invariants now fail the build rather than drifting. |

## 0d. Shipped in the fourth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **A light theme** — warm paper palette, applied through the existing design tokens, with the header, hero band and panels re-tuned | The archive was dark-only at 18px serif. Half of the people who would read a 2,000-word dossier on palaeomagnetism are not going to do it on a black screen at night. |
| 2 | **A type-size control** — three steps, remembered per browser | 18px is a compromise; it is too small for some readers and too large for others. |
| 3 | **No flash on load** — a 3-line inline script applies the stored preference before first paint | The usual failure of a theme toggle is a white flash on every navigation. |
| 4 | **`glossary.html` — 40 working definitions** in four groups: geology and the sky, claims and evidence, mind, media | The archive uses *firmament*, *tillite*, *base rate*, *steelman* and *Markov blanket* in a specific sense on 162 pages and had never defined any of them in one place. |
| 5 | **CI extended** — every page must keep its reader-preference controls | 186 pages, 0 problems. |

Deliberately deferred: `compare.html` still takes two dossiers, not three. Extending it means rewriting its render function, and the two-way version is not broken — it is just less than it could be.

## 0e. Shipped in the fifth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **An on-this-page rail** on 162 dossiers, sticky inside the aside, with the current section highlighted by an IntersectionObserver | Dossiers run 700–2,000 words across five to seven sections with no jump list. The rail also gives every heading a permanent anchor, so a specific section can be linked and cited. |
| 2 | **Sixty more rails** added on a second pass, for pages whose headings already carried manual ids or whose aside had content after the facts list | The first pass silently skipped them; the CI check found the gap. |
| 3 | **Keyboard reading** — `j` / `k` move along the pager chain, `/` focuses search, `t` flips the theme, `?` opens a shortcut sheet, `Esc` closes it | The archive is 162 pages of prose read in sequence; it now supports reading in sequence. |
| 4 | **`compare.html` takes three dossiers**, with the selection carried in `?a=&b=&c=` and a three-column grid above 760 px | Two is the minimum that makes a point; three is where you can see a pattern across labels. Comparisons are now linkable and citable. |
| 5 | **CI extended** — a dossier with sections must keep its rail, and every rail anchor must resolve | 186 pages, 0 problems; 0 broken anchors. |

## 0f. Shipped in the sixth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **A service worker** (`sw.js`) — cache-first for the shell, styles and images; network-first for pages with a cache fallback; versioned cache, cleaned on activate | "Works offline" was true only if you had cloned the repository. A dossier read once now stays readable on a train, and a cold page gets `offline.html` instead of the browser's error page. |
| 2 | **`offline.html`** — a noindex shell that explains what is cached and what is not | The usual failure of an offline fallback is a blank page or a lie. This one says which is which. |
| 3 | **480 px WebP hero variants** for all 162 dossiers, wired through `srcset` and `sizes` | The hero is the largest thing on a phone screen and was being sent at 900 px. The mobile hero is now roughly a third of the bytes; desktop still gets the full image. |
| 4 | **Intrinsic `width`/`height` on every hero** while doing it, with duplicate attributes collapsed | CLS was already low because the CSS fixes the box, but the attributes make the reservation explicit. |
| 5 | **CI extended** — `offline.html` is exempt from the page invariants, and everything else still has to pass | 187 pages, 0 problems. |

## 0g. Shipped in the seventh pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **A ⌘K / Ctrl-K command palette** on all 187 pages — searches 992 records, arrow keys, Enter to open, Esc to close | The "More" menu is a 100-item column that is unusable on a phone and slow on a desktop. The palette answers the question people actually have: *where is the thing I half remember?* |
| 2 | **`search-index.json`**, fetched on first open rather than inlined | Inlining 233 KB into 187 pages would have cost more than the palette is worth; lazy-fetching it costs one request, once. |
| 3 | **A graceful failure** — if the index cannot load (a `file://` copy, or no connection), the palette says so and links the search page | A palette that spins forever is worse than no palette. |
| 4 | **Nav consistency in CI** — every page must carry the same top-level links as the index, with two documented exceptions | It immediately found `master-list.html` missing the Topic register link, which had been true since that page was written. |
| 5 | **Index-drift check in CI** — `search-index.json` must match the inline index on the search page | Two copies of the same data is a promise to forget one of them. |

## 0h. Shipped in the eighth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **The archive as a PDF** — `assets/larger-world-archive.pdf`, 536 pages, A5, 3 MB, generated from the print edition with a print-only stylesheet (no images, no navigation, one part per opening) | "Single-volume edition" was a 840 KB HTML page that only became a book if you pressed Ctrl-P. Now it is a file you can put on a Kindle, print, or hand to someone. |
| 2 | **A download button** on `print-edition.html` | The PDF existed nowhere the reader could find it. |
| 3 | **The contents count fixed** — the print edition said "152 parts" while listing 164 | A stale count in the one place where the count is the contents. |
| 4 | **`data/claims.json`** — the provenance ledger: 162 claims with theme, label, facts, source URLs, reviewer and licence, generated by `tools/build-ledger.py` | The first step of the largest remaining item. The ledger now exists and is checked; the views still read the pages. |
| 5 | **CI** — the ledger must match the number of dossiers on disk | A ledger that drifts is worse than none. |

**Found while building the ledger:** 57 of the 162 dossiers carry a bespoke badge text — *Ended by DNA*, *A thermal blanket*, *Geology, not architecture* — rather than one of the four canonical labels, while their colour class is correct. The colours are consistent; the words are not. That is either nuance or drift, and it is your call: the ledger records both (`label_text`, `label_canonical`) so the decision can be made with the list in front of you rather than from memory.

## 0i. Shipped in the ninth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **An EPUB 3** — `assets/larger-world-archive.epub`, 164 chapters, 388 KB | The PDF is a fixed page; an EPUB is the same book on a phone, reflowing to whatever screen it lands on. Built from the print edition's parts, with the web links flattened to plain text so a chapter does not depend on a network. |
| 2 | **Structure verified** — mimetype stored first and uncompressed, container → OPF → spine all resolving, 167 manifest items all present, 165 nav links all valid, no remote resources in any chapter | An EPUB that a reader refuses to open is worse than no EPUB. `epubcheck` is not available here, so the checks are the ones that matter mechanically. |
| 3 | **Both downloads on the print edition page**, side by side | The PDF had a button; the EPUB needed to sit next to it or nobody would find it. |

## 0j. Shipped in the tenth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **A cover for the EPUB** — 1600×2400, the site's own palette and ring mark, declared as `cover-image` and placed first in the spine | Without one, every library view shows a grey rectangle with the title in Helvetica. |
| 2 | **`how-to-read.html`** — the label scale, the five parts of a page, the three ways in, what to do when you disagree, and what the archive will not do | 162 dossiers in a fixed shape, and nothing that explained the shape. The reading guide sequences the material; this explains the furniture. |
| 3 | **Linked from the reading guide and the glossary**, and from every footer | A page nobody can reach is a page that does not exist. |
| 4 | **Sitemap and CI** — 186 indexable URLs; the new page is in the utility list and carries the same invariants as the rest | 188 pages, 0 problems. |

## 0k. Shipped in the eleventh pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **`tools/rebuild-shell.py`** — the header and footer live once, in `index.html`, and are copied into all 188 pages with `aria-current` applied per page. `--check` fails if any page has drifted | Every previous pass ended with a script doing 188 string replacements and hoping. This is the last time that is necessary: a navigation change is now one edit and one command. |
| 2 | **182 pages normalised** — most had a shorter footer than the index, and the rest had drifted in small ways | The site had two footers and several variants of the same nav. It now has one of each. |
| 3 | **CI runs the check** | Drift is caught at push, not discovered three passes later. |
| 4 | **A CSS bug found by the shell work** — the citation block carried 52 px of padding above its heading, inherited from the global `section{padding:52px 0}` | It had been visible on all 162 dossiers since the citation block shipped, and nobody had looked at the bottom of a page closely enough. |

## 0l. Shipped in the twelfth pass — 20 November 2026

| # | Change | Why it mattered |
|---|---|---|
| 1 | **`tools/rebuild-charts.py`** — every number on `charts.html` rebuilt from `data/claims.json`, `master-list.html` and the credits page: both label charts, the theme sizes, the licence split, the longest and thinnest source lists, the captions, and the generated date | The page claimed "nothing here is typed by hand" while carrying 150 dossiers, 706 sources and 167 images, all stale. |
| 2 | **A correction to this pass, recorded rather than buried** — my first version replaced the 47/39/32/32 bar with a 23/107/14/16/2 bar and called the old numbers wrong. They were not: that bar counted the 150 catalogued claims, and I had swapped in the 162 dossiers. The page now shows both, each labelled with its population, and the prose says why they need not agree | Two different populations measured by two different methods is the kind of error that looks like a fix. It was caught by checking where the original 47/39/32/32 came from before defending its replacement. |
| 3 | **CI runs `--check`** | The page and the ledger can no longer disagree without failing the build. |
| 4 | **The caption and the thinnest-dossier sentence are generated too** | Prose is where stale numbers survive longest: the chart was regenerated, and the sentence beneath it still said 150. |

## 0m. Shipped in the thirteenth pass — 20 November 2026

Six dossiers written from the topic register, each with a credited Commons photograph, the full page furniture (breadcrumbs, citation block, related strip, on-this-page rail, share card) and four sources.

| # | Dossier | Label | Why it earns a page |
|---|---|---|---|
| 1 | **Tardigrades Between Planets** | Documented | The animal is real and extraordinary; the panspermia inference attached to it is neither, and the 2015 genome claim was retracted. |
| 2 | **The Cambrian Explosion** | Live debate | Twenty million years of body plans, and a century and a half of argument about whether the explosion is in the animals or in the fossil record. |
| 3 | **Earthquake Prediction** | Live debate | The cleanest case in the archive of a field where failure is the evidence: Parkfield, Haicheng, Tangshan, and no scoreable protocol. |
| 4 | **Aphantasia** | Documented | The counterweight to every page that treats the mind as one thing with a standard setting. |
| 5 | **Multiple Intelligences** | Debunked | Eight independent intelligences, forty years of curricula, and no psychometric support for the structure. |
| 6 | **The Anthropocene** | Documented | The contested part is the label, not the evidence — and the proposers lost the vote and accepted it. |

Downstream, in one pass: theme shelves (6 rows), print edition (170 parts), search index and `search-index.json` (168 dossiers), `data/claims.json`, `charts.html`, sitemap (192 URLs), PDF (554 pages), EPUB (170 chapters), six share cards, six 480 px hero variants, and the register retargeted so those six rows now point at pages instead of collections. 194 pages, 0 problems.

## 1. Shipped in the first pass

These were gaps found in the audit and closed without touching a single sentence of content.

| # | Change | Why it mattered |
|---|---|---|
| 1 | **Social and search metadata on all 170 pages** — `og:*`, `twitter:card`, canonical URL, `theme-color`, per-page title and description carried through | Every page was previously a blank card when shared on X, WhatsApp, Slack, LinkedIn or Telegram. For an archive whose whole distribution model is "someone links you a dossier", this was the largest single loss. |
| 2 | **A 1200×630 share card** (`assets/og-card.png`) in the site's own palette, plus `og:image:alt` | Shared links now show the title, the subtitle and the counts instead of a grey rectangle. |
| 3 | **JSON-LD structured data** — `WebSite` + `SearchAction` on the index, `Article` with author, publisher and `isPartOf` on all 150 dossiers, `CollectionPage`/`Book` on the indexes and the print edition | Machine-readable authorship, which is the difference between being cited and being scraped. |
| 4 | **Favicon set** — `favicon.svg` (the amber ring mark, matching the header), 192/512 PNG, `apple-touch-icon`, `site.webmanifest` | Every tab and every home-screen shortcut showed a default globe icon. |
| 5 | **`sitemap.xml` (169 URLs) and `robots.txt`** | Nothing pointed a crawler at 170 pages. Indexing was happening by luck. |
| 6 | **A real `404.html`** with a `<base href>` so assets resolve at any depth, plus the five most-wanted destinations and a search entry point | GitHub Pages served its generic 404; deep links from old posts died there. |
| 7 | **A sponsor block in the site footer on all 170 pages** — band above the footer notes, five destinations, one line about what is and is not gated | The site had no support path at all, while the READMEs of the other repos did. |
| 8 | **A dedicated `support.html`** — UPI with QR and payee name, GitHub Sponsors, Ko-fi, PayPal, books, the three free things that help more, and an honest statement of where the money goes | A footer band cannot carry a UPI QR or explain that no tier exists. |
| 9 | **`.github/FUNDING.yml`** — GitHub, Ko-fi, PayPal, the support page | Puts the Sponsor button in the repository header, where it is actually clicked. |
| 10 | **Skip link, `id="main"` landmark, visible `:focus-visible` rings** | The 100-item nav is the first thing a keyboard user hits on every page, and there was no way past it. |
| 11 | **One `<h1>` per page** — the print edition had 153 (one per part); part titles are now `<h2 class="part-title">` with the same visual weight | A 153-heading page has no outline at all for a screen reader or a crawler. |
| 12 | **A print stylesheet** — nav, hero, cards and the support band removed; every external link expanded to its URL; page-break rules on headings and sections | The archive's own print edition was the only printable page. Now any dossier prints as a citation-ready sheet. |
| 13 | **Lazy-loading and decode hints audited across 437 images**, with the front-page hero switched to `fetchpriority="high"` | The hero is the LCP element on the index; everything below the fold now defers. (Explicit `width`/`height` was tried and reverted — see item 14 in the next list, which is where it belongs once the figure CSS is made dimension-safe.) |
| 15 | **Deep-linkable search** — `search.html?q=atlantis`, kept in sync with `history.replaceState`, restored on load | Search results could not be shared, linked, or reached from the `SearchAction` schema. |
| 16 | **`LICENSE`** — CC BY-NC 4.0 for the writing, with images, quotations and marks explicitly excluded | 170 pages of original research with no stated terms is unquotable by anyone cautious. |
| 17 | **A dead-source issue template** | Turns "the link is broken" into a structured, fixable report. |

---

## 2. Quick wins — under an hour each, high return

0. ~~**Photographs for the twelve new dossiers.**~~ **Done — see 0b.** Each currently leads with a diagram. The archive's visual language is a credited historical photograph at the top and diagrams in the body; the new pages invert that. One Commons search per topic, one credit line each, and the pattern is restored.
0b. **A claim stub for every register row.** The 726 rows carry a title, a label and one sentence. Promoting 20 of them per month, in the order the register lists them, closes the gap in about three years — and the register makes that pace visible instead of aspirational.

1. ~~**Per-dossier share cards.**~~ **Done — see 0c.** Render `assets/og/<slug>.png` for all 150 dossiers from the same HTML template as the site card (title, label, hero crop). 150 headless renders, one script, no design work. Every shared dossier then carries its own claim and label.
2. ~~**`citation_*` meta tags**~~ **Done — see 0b.** (Highwire/Dublin Core: `citation_title`, `citation_author`, `citation_publication_date`, `citation_pdf_url`) on every dossier. This is what Google Scholar reads; without it a reference library is invisible to the one index that matters to researchers.
3. ~~**A "Cite this page" box**~~ **Done — see 0c.** at the foot of each dossier — APA, MLA, Chicago and BibTeX, generated from the page's own title, author and date, with a copy button. Nothing else would do more to make the archive quotable.
4. ~~**`lastmod` from git history.**~~ **Done — see 0c.** `sitemap.xml` currently stamps all 169 URLs with the build date; deriving it from `git log -1 --format=%cI -- <page>` is a one-line change per URL and is the signal crawlers actually trust.
5. ~~**A random-dossier button**~~ **Done — see 0b.** in the header (`?random` → redirect to a random page). A 150-page archive is navigated by wandering; there is currently no way in except the index.
6. ~~**`/` to focus search, `Esc` to clear, ↑/↓/Enter to walk results**~~ **Done — see 0b.** in `search.html`, plus a `aria-live="polite"` on the result count. The search box is the archive's best tool and it is mouse-only.
7. ~~**A "related dossiers" strip**~~ **Done — see 0c.** at the foot of each page — 4 links computed from shared theme and label. 150 pages currently link outward to each other only through the nav.
8. ~~**`rel="noopener"` on every external link**~~ **Done — see 0b.**, not just the new support links (682 of 2,841 currently carry it). Cheap hardening, no visual change.
9. **A `humans.txt` and a `.well-known/security.txt`.** Two small files, both expected of a site that takes its own claims about privacy seriously.
10. **Intrinsic image dimensions, done safely.** 589 images carry no `width`/`height`, so every page reflows as it loads. The blanket fix (`img{height:auto}`) breaks the front-page hero and the dossier figures, both of which are absolutely positioned — the fix is per-figure: give `.fig`/`.hero-band` an `aspect-ratio`, then add the attributes. Worth ~0.05 of CLS on a slow connection.
11. **Breadcrumbs** on every dossier: `Archive › <theme> › <dossier>`, as both a visible strip and `BreadcrumbList` JSON-LD.

## 3. Medium — a day each, changes how the archive is used

11. ~~**A CI gate with four checks.**~~ **Done — see 0b.** HTML validation (`vnu`), link check over the 916 external URLs, an accessibility pass (`pa11y` or axe), and a per-page size budget. The archive is 170 hand-generated files; one bad regeneration currently ships silently.
12. ~~**A scheduled dead-link sweep.**~~ **Done — see 0b.** Weekly Action that re-checks all 916 URLs, queries the Wayback Machine availability API for anything that 404s, and opens one issue listing what broke with a snapshot link for each. Dead citations are the archive's slowest decay.
13. **Sticky per-page table of contents.** Dossiers run 700–2,000 words with 5–7 headed sections and no jump list. A right-hand "on this page" rail (desktop) and a collapsible summary (mobile) would cut the scroll cost of every page.
14. ~~**Responsive images.**~~ **Done — see 0f.** `srcset` at 480/960/1440 for every AVIF plus a WebP `<picture>` fallback, so a phone stops downloading 900×1020 crops. Expect roughly 60% off mobile image bytes.
15. **A light theme and a reading-size control.** The archive is dark-only, at 18px serif. Both are preference toggles stored in `localStorage`, ~40 lines, and both materially widen who can read a long page.
16. ~~**An RSS/Atom feed**~~ **Done — see 0c.** of new and revised dossiers, plus a JSON Feed. Nothing announces that the archive grew; a feed is the cheapest way to be followed.
17. ~~**A corrections policy page and a visible "last reviewed" line**~~ **Done — see 0c.** on every dossier. The archive's authority rests on being checkable; it should say when each page was last checked, and what happens when a claim is overturned.
18. ~~**A glossary.**~~ **Done — see 0d.** *Firmament*, *ice wall*, *Tartarus*, *concave Earth*, *aether*, *hollow shell*, *expanding Earth*, *Silurian hypothesis* — recurring terms, currently explained 150 separate times in 150 separate voices.
19. **Extend `compare.html`.** Today it compares two dossiers; make it three, and put the pair in the URL (`?a=flat-earth&b=ice-wall`) so a comparison can be linked, shared and cited.
20. **A "how to read a dossier" page.** The four labels are explained on the index and again in a key on each page, but the method itself — how a claim was traced, what counts as evidence here — has no permanent home.

## 4. Large — a week or more, changes what the archive is

21. ~~**A generated PDF and EPUB of the print edition.**~~ **Done — see 0h and 0i.** `print-edition.html` is 813 KB of HTML designed for `Ctrl-P`. A real typeset PDF with running heads, page numbers and a TOC with folios, plus an EPUB for e-readers, turns the archive into something that can be read on a train — and puts it one step from the KDP pipeline the other repositories already have.
22. **A static build step, or none at all.** The nav, footer and palette are duplicated across 170 files; one change means 170 edits (this pass touched all of them with a script). Either accept a 60-line generator that assembles pages from partials, or add a CI check that fails when two pages' nav blocks disagree. The second is cheaper and keeps the "clone and open `index.html`" property.
23. ~~**A searchable command palette instead of the "More" menu.**~~ **Palette done — see 0g. The menu itself remains.** The nav panel holds 100+ links in one column. `Ctrl-K` with fuzzy matching over the same 980-record index would replace it, and would make the mobile header usable.
24. ~~**Keyboard-first reading.**~~ **Done — see 0e.** `j`/`k` to move between dossiers in reading order, `s` to open search, `?` for the shortcut sheet. The reading guide already defines an order; nothing walks it.
25. ~~**An offline service worker.**~~ **Done — see 0f.** The site works from `file://` but not from a flaky connection. A 30-line SW caching the shell plus visited pages would make "readable offline" literally true from the URL as well.
26. **An audio edition.** Every dossier is 700–2,000 words of prose, which is exactly what a TTS pipeline handles well (Sarvam Bulbul, or any local model), with an `<audio>` element per page and a podcast feed of the same. This is the single largest reach multiplier available to a text archive.
27. **A Hindi edition of the reading guide and the twelve door pages.** The audience for this material in India is large and served almost entirely by English-language YouTube. Translating the entry points, not the whole archive, is the cheap version of that.
28. ~~**A provenance ledger.**~~ **Ledger done — see 0h; the views still read the pages.** One machine-readable file (`data/claims.json`) holding every claim's label, date, author and source IDs — from which the master list, the claim register, the charts and the search index are all generated. Today they are four hand-maintained views of the same facts, which means they can disagree.

## 5. Deliberately not recommended

- **Analytics of any kind.** It would contradict the privacy line in the footer, and the site gains nothing from knowing which dossier you read.
- **A comment section or a forum.** The archive's value is that a claim's fate is decided by evidence, not by who is loudest. Corrections belong in issues, where they are attributable.
- **Ads or sponsored dossiers.** One sponsored label would cast doubt on all 150.
- **A CMS.** 170 static files, one stylesheet and a search index is the correct architecture for something meant to still open in a decade.

---

*Baseline audited 19 November 2026. Numbers in this file are measurements of this repository, not estimates.*
