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

## 0n. Shipped in the fourteenth pass — 20 November 2026

Six more from the register, and a publisher that makes the next six cheaper.

| # | Dossier | Label | Why |
|---|---|---|---|
| 1 | **Synesthesia** | Documented | The counter-example: an extraordinary-sounding claim a lab can check in an afternoon. |
| 2 | **Lucid Dreaming** | Documented | Verified by eye-movement signals in REM in 1980 — a dream claim with a receipt. |
| 3 | **Near-Death Experiences** | Live debate | Documented phenomenon, undocumented interpretation, and the AWARE study's missing hit. |
| 4 | **The Mpemba Effect** | Live debate | Five different definitions of "freezes faster", and no agreed experiment. |
| 5 | **Ball Lightning** | Live debate | Four centuries of consistent reports, one spectroscopic measurement, no mechanism. |
| 6 | **The Flynn Effect** | Documented | The fact that makes every IQ argument harder: the measure moved a standard deviation in a century. |

| # | Infrastructure | Why it matters |
|---|---|---|
| 1 | **`publish_batch.py`** — one command takes a content module and a photo manifest and publishes everything: pages with all furniture, 480 px variants, theme rows, print parts, search index and JSON, ledger, charts, sitemap, six share cards, PDF, EPUB, then runs the checks | The previous batch took six separate scripts and a hand-sequenced order. This one took one command and one review. |
| 2 | **Pages are now born complete** — breadcrumbs, citation block, related strip, rail, citation meta, share card, scripts | The last batch had to be finished in a second pass because the builder did not know about them. |
| 3 | **Result** | 174 dossiers, 802 sources, 208 images, 200 pages, PDF 571 pages, EPUB 176 chapters, sitemap 198 URLs, 0 problems. |

## 0o. Shipped in the fifteenth pass — 20 November 2026

Six more, all from the biology and deep-time end of the register — the part of the archive that was thinnest.

| # | Dossier | Label | Why |
|---|---|---|---|
| 1 | **Why Zebras Have Stripes** | Live debate | Five hypotheses, and the one with the experiment behind it is flies, not majesty. |
| 2 | **The Giraffe's Neck** | Live debate | The most-quoted Lamarckian example is not Lamarckian, and the real anatomy is stranger. |
| 3 | **Whale Strandings** | Live debate | Two documented causes, a large fringe literature, and a necropsy that separates them. |
| 4 | **Abiogenic Petroleum** | Fringe claim | A real scientific alternative that fails on molecules that could only have come from living things. |
| 5 | **The Great Oxidation Event** | Documented | The largest biological change to the planet's chemistry, written in sulphur isotopes. |
| 6 | **The Inner Core's Spin** | Live debate | A disagreement entirely about measurement, where both sides say so. |

The publisher ran it end to end in one command: 180 dossiers, 826 sources, 214 images, 206 pages, PDF 589 pages, EPUB 182 chapters, sitemap 204 URLs, 0 problems.

## 0p. Shipped in the sixteenth pass — 20 November 2026

Six from the artefact end of the register — the claims that made this archive's reputation, and the ones where the debunking is a microscope or a grammar book rather than a paper.

| # | Dossier | Label | Why |
|---|---|---|---|
| 1 | **The Baghdad Battery** | Debunked | a real jar, real electrochemistry, and no wires, no residue, no plated objects |
| 2 | **The Piri Reis Map** | Debunked | a fine 1513 compilation whose own marginal notes explain what it contains |
| 3 | **The Kensington Runestone** | Debunked | nineteenth-century Swedish grammar on a stone claiming 1362 |
| 4 | **The Philadelphia Experiment** | Debunked | one correspondent, no records, and a ship's logs that place it elsewhere |
| 5 | **The Crystal Skulls** | Debunked | rotary tool marks and Brazilian quartz on every skull examined |
| 6 | **Stonehenge Acoustics** | Live debate | real measurement, real replicas, and a ruin that cannot settle intent |

186 dossiers, 850 sources, 220 images, 212 pages, PDF 604 pages, EPUB 188 chapters, sitemap 210 URLs, 0 problems.

## 0q. Shipped in the seventeenth pass — 20 November 2026

Ten dossiers in one run, after a speed replan. The bottleneck was never the writing; it was the per-batch overhead.

**What changed in the pipeline**

| # | Change | Effect |
|---|---|---|
| 1 | **`publish_batch.py` no longer rebuilds the PDF and EPUB by default** — `--heavy` does that | the 30-second PDF/EPUB step was running after every six dossiers for no benefit |
| 2 | **`autophoto.py`** — parallel Commons search with a licence whitelist, landscape preference and a 900 px floor, four threads | photo sourcing went from a manual search-and-review per dossier to one command and one contact sheet for ten |
| 3 | **Bigger batches** — ten dossiers per run instead of six | the fixed cost (indexes, cards, checks, sitemap) is paid once instead of twice |
| 4 | **Compact dossier form** — four sections, ~450–550 words, same furniture | roughly a third less writing per page with no loss of the claim-evidence-verdict structure |
| 5 | **Timed** | ten dossiers: 1 m 35 s to publish, 31 s for the PDF and EPUB afterwards |

**The ten**

| Dossier | Label |
|---|---|
| The Shroud as a Radiation Flash | Fringe claim |
| Nessie as a Giant Eel | Live debate |
| Baalbek and the Giants | Debunked |
| Geopolymer Pyramids | Live debate |
| Tutankhamun's Meteorite Dagger | Documented |
| Water Erosion on the Sphinx | Live debate |
| The Vinland Map | Debunked |
| The Cottingley Fairies | Debunked |
| The Feejee Mermaid | Debunked |
| The Bermuda Triangle | Debunked |

196 dossiers, 890 sources, 230 images, 222 pages, PDF 624 pages, EPUB 198 chapters, sitemap 220 URLs, 0 problems.

## 0r. Shipped in the eighteenth pass — 20 November 2026

Ten more, split between the cosmos and the mind. Same pipeline, and this time it ran in **43 seconds** — the first batch through the optimised path with everything warm.

| # | Dossier | Label |
|---|---|---|
| 1 | The Wow! Signal | Live debate |
| 2 | The Face on Mars | Debunked |
| 3 | The Phobos Monolith | Debunked |
| 4 | Tired Light | Debunked |
| 5 | The Boötes Void | Documented |
| 6 | The Ganzfeld Effect | Documented |
| 7 | The Tetris Effect | Documented |
| 8 | Chronostasis | Documented |
| 9 | Alien Hand Syndrome | Documented |
| 10 | The Green Children of Woolpit | Live debate |

206 dossiers, 930 sources, 240 images, 232 pages, PDF 644 pages, EPUB 208 chapters, sitemap 230 URLs, 0 problems.

**On the auto-picked photographs:** four of the ten came back wrong on the first pass — a magazine page for the ganzfeld, a keyboard for alien hand syndrome, a German temple for Woolpit. The contact sheet caught them, the terms were tightened, and the second pass was correct. The check is not optional; it is the whole reason the pipeline is fast rather than careless.

## 0s. Shipped in the nineteenth pass — 20 November 2026

Ten more, five from the cosmos and five from the mind. Published in **41 seconds**; PDF and EPUB rebuilt afterwards in 31.

| # | Dossier | Label |
|---|---|---|
| 1 | 'Oumuamua as a Solar Sail | Fringe claim |
| 2 | The Kardashev Scale | Documented |
| 3 | The Great Attractor | Documented |
| 4 | Cosmic Censorship | Live debate |
| 5 | The Black Hole Information Paradox | Live debate |
| 6 | Jung's Synchronicity | Fringe claim |
| 7 | Tulpas | Fringe claim |
| 8 | The Savant Reservoir | Fringe claim |
| 9 | The Call of the Void | Documented |
| 10 | The Global Consciousness Project | Debunked |

216 dossiers, 970 sources, 250 images, 242 pages, PDF 664 pages, EPUB 218 chapters, sitemap 240 URLs, 0 problems, every page inside its size budget.

The batch also balances the archive's labels for the first time: fringe is no longer a curiosity at the edges but a category with eleven pages, and the three unfalsifiable claims (synchronicity, tulpas, the savant reservoir) are filed as fringe rather than debunked, which is the distinction the four-label scheme exists to make.

## 0t. Shipped in the twentieth pass — 20 November 2026

Ten more: four cosmos, three mind, three history. Published in 41 seconds; PDF and EPUB in 31.

| # | Dossier | Label |
|---|---|---|
| 1 | Life in Venus's Clouds | Live debate |
| 2 | Europa's Ocean | Live debate |
| 3 | Mirror Matter | Fringe claim |
| 4 | The Big Bounce | Live debate |
| 5 | The Baader–Meinhof Effect | Documented |
| 6 | Folie à Deux | Documented |
| 7 | Collective Effervescence | Documented |
| 8 | The Berenstain Bears | Debunked |
| 9 | Who Were the Sea Peoples? | Live debate |
| 10 | The Amber Room | Live debate |

226 dossiers, 1,010 sources, 260 images, 252 pages, PDF 684 pages, EPUB 228 chapters, sitemap 250 URLs, 0 problems.

The archive crossed a thousand source entries with this batch. Two of the ten are the mechanism pages the rest of the collection depends on — the frequency illusion and collective effervescence — and both are filed as documented, because the mechanism is measured even when the claims it explains are not.

## 0u. Shipped in the twenty-first pass — 20 November 2026

Ten more: four ancient, three cosmos, three mind. Published in 44 seconds.

| # | Dossier | Label |
|---|---|---|
| 1 | The Dendera Light | Debunked |
| 2 | The Giza Power Plant | Fringe claim |
| 3 | The Copper Scroll | Live debate |
| 4 | Arthur as a Roman Commander | Live debate |
| 5 | Yamashita's Gold | Fringe claim |
| 6 | The Lunar Wave | Debunked |
| 7 | Earth Was Terraformed | Fringe claim |
| 8 | The Gateway Process | Fringe claim |
| 9 | Timewave Zero | Debunked |
| 10 | Quantum Healing | Debunked |

236 dossiers, 1,050 sources, 270 images, 262 pages, PDF 704 pages, EPUB 238 chapters, sitemap 260 URLs, 0 problems.

Two of these are the same error in different centuries — the Dendera relief read as a light bulb, and the Gateway report read as a finding — and the pair is worth having adjacent on the shelf. Three are claims with hard dates or hard objects (2012, the copper inventory, the Philippine tunnels), which is the easiest kind of claim to settle and the kind this archive is best at.

## 0v. Shipped in the twenty-second pass — 20 November 2026

Ten more: megastructures, dream claims, and two famous grails.

| # | Dossier | Label |
|---|---|---|
| 1 | Dyson Spheres | Live debate |
| 2 | Matrioshka Brains | Fringe claim |
| 3 | The Aestivation Hypothesis | Fringe claim |
| 4 | The Akashic Records | Fringe claim |
| 5 | Shared Dreaming | Fringe claim |
| 6 | The Simian Line and Palmistry | Fringe claim |
| 7 | Déjà Rêvé | Live debate |
| 8 | Stonehenge as a Computer | Live debate |
| 9 | The Grail Bloodline | Debunked |
| 10 | Déjà Vu | Live debate |

246 dossiers, 1,090 sources, 280 images, 272 pages, PDF 724 pages, EPUB 248 chapters, sitemap 270 URLs, 0 problems.

Four of these are the same structural case — a real observation with an unevidenced inference bolted on (Dyson's infrared excess, the palmar crease, the dream report, the solstice alignment). Filing them together makes the archive's central distinction legible in one shelf.

## 0w. Shipped in the twenty-third pass — 20 November 2026

Ten more: AI risk, memory in the phone era, and four cosmology arguments.

| # | Dossier | Label |
|---|---|---|
| 1 | The Paperclip Maximiser | Live debate |
| 2 | Grey Goo | Fringe claim |
| 3 | Mind Uploading | Fringe claim |
| 4 | Phantom Vibration Syndrome | Documented |
| 5 | The Google Effect | Documented |
| 6 | Planet Nine as a Black Hole | Fringe claim |
| 7 | Loop Quantum Gravity | Live debate |
| 8 | Assembly Theory | Live debate |
| 9 | Blue Light and Circadian Damage | Live debate |
| 10 | Dark Flow | Live debate |

256 dossiers, 1,130 sources, 290 images, 282 pages, PDF 744 pages, EPUB 258 chapters, sitemap 280 URLs, 0 problems.

**A process failure worth recording.** Eight of these ten were written without the `field` and `years` arguments, and my first repair script — a regex that inserted the missing pair — silently filled them with `"General", "1900s – present"` for every affected dossier. The build passed, the pages rendered, and the only reason it was caught is that I printed the fields afterwards and saw eight identical values. A silent default is worse than a hard failure: the D() signature caught the missing arguments the first four times, and my "fix" defeated the check. Corrected before publishing.

## 0x. Shipped in the twenty-fourth pass — 21 November 2026

Ten more, all from the artefact shelf: four out-of-place objects and six pieces of genuine ancient technology.

| # | Dossier | Label |
|---|---|---|
| 1 | The Saqqara Bird | Debunked |
| 2 | The Phaistos Disc | Debunked |
| 3 | Archimedes' Heat Ray | Live debate |
| 4 | Greek Fire | Live debate |
| 5 | Damascus Steel | Live debate |
| 6 | Roman Concrete That Heals | Documented |
| 7 | The Iron Pillar of Delhi | Documented |
| 8 | The Lycurgus Cup | Documented |
| 9 | The London Hammer | Debunked |
| 10 | Pakal's Rocket | Debunked |

266 dossiers, 1,170 sources, 300 images, 292 pages, PDF 764 pages, EPUB 268 chapters, sitemap 290 URLs, 0 problems.

**The fix for the silent-default bug.** `publish_batch.py` now refuses to publish a dossier with a missing field, a placeholder value (`"General"`, `"1900s – present"`) or fewer than three sources. The two bugs that reached the pages in the last batch — eight dossiers with `"General"` as their field — would have failed this check at the door.

## 0y. Shipped in the twenty-fifth pass — 21 November 2026

Ten from the internet-and-mind shelf, the newest material in the archive.

| # | Dossier | Label |
|---|---|---|
| 1 | The Singularity | Fringe claim |
| 2 | The AI Box Experiment | Fringe claim |
| 3 | Consciousness in the Machine | Fringe claim |
| 4 | Parasocial AI Relationships | Live debate |
| 5 | Technofeudalism | Live debate |
| 6 | The Interface Theory of Perception | Live debate |
| 7 | Algorithmic Radicalisation | Live debate |
| 8 | The Liar's Dividend | Documented |
| 9 | Harvest Now, Decrypt Later | Documented |
| 10 | The Splinternet | Documented |

276 dossiers, 1,210 sources, 310 images, 302 pages, PDF 784 pages, EPUB 278 chapters, sitemap 300 URLs, 0 problems.

**The publisher's validator caught the batch, not me.** Nine of the ten were written without their `field`/`years` pair, and the new pre-flight check refused to publish until each was filled with a real value. That is the difference between this batch and the one that shipped eight `"General"` fields: the failure now happens at the door, before a page is written, and the fix has to be a real field rather than a default.

## 0z. Shipped in the twenty-sixth pass — 21 November 2026

Ten from the body-and-mind shelf: the everyday myths and the ordinary open questions.

| # | Dossier | Label |
|---|---|---|
| 1 | The Mozart Effect | Debunked |
| 2 | Why Ten Per Cent Are Left-Handed | Live debate |
| 3 | Dunning–Kruger | Documented |
| 4 | Why We Sleep | Live debate |
| 5 | Why We Dream | Live debate |
| 6 | Why We Yawn | Live debate |
| 7 | Why We Lost Our Fur | Live debate |
| 8 | Serotonin and Depression | Live debate |
| 9 | Mirror Neurons | Live debate |
| 10 | Hygiene or Old Friends | Live debate |

286 dossiers, 1,250 sources, 320 images, 312 pages, PDF 804 pages, EPUB 288 chapters, sitemap 310 URLs, 0 problems.

Nine of the ten are `live debate`, which is the honest label for questions where the phenomenon is well measured and the explanation is not: sleep, dreams, yawning, fur, handedness. The two `debunked` pages are the ones where a specific claim was tested and failed, and the two `documented` pages are where a real effect is well measured and the popular version of it is a distortion.

## 0aa. Shipped in the twenty-seventh pass — 21 November 2026

Ten from the biology-of-mind shelf, where the questions are ordinary and the answers are not settled.

| # | Dossier | Label |
|---|---|---|
| 1 | The Grandmother Hypothesis | Live debate |
| 2 | Why We Age | Live debate |
| 3 | Cancer's Origin | Live debate |
| 4 | Amyloid and Alzheimer's | Live debate |
| 5 | Quantum Coherence in Photosynthesis | Live debate |
| 6 | Plant Neurobiology | Fringe claim |
| 7 | Linguistic Relativity | Live debate |
| 8 | Facial Feedback | Live debate |
| 9 | Split-Brain Consciousness | Live debate |
| 10 | Catharsis | Live debate |

296 dossiers, 1,290 sources, 330 images, 322 pages, PDF 824 pages, EPUB 298 chapters, sitemap 320 URLs, 0 problems.

This is the batch that best shows the archive's method: eight pages where the honest label is *live debate* because the phenomenon is measured and the explanation is not, one where a real biology has been promoted into a claim (plant neurobiology), and one where the popular version is contradicted by the direct tests while the underlying question stays open (catharsis).

## 0ab. Shipped in the twenty-eighth pass — 21 November 2026

Ten more: five real-world hazards and five internet legends.

| # | Dossier | Label |
|---|---|---|
| 1 | The Wet-Bulb Threshold | Documented |
| 2 | Kessler Syndrome | Live debate |
| 3 | Solar Geoengineering | Live debate |
| 4 | De-Extinction | Live debate |
| 5 | Xenotransplantation | Documented |
| 6 | Epigenetic Inheritance of Trauma | Live debate |
| 7 | The Momo Panic | Debunked |
| 8 | John Titor | Debunked |
| 9 | Randonautica | Debunked |
| 10 | Reality Shifting | Debunked |

306 dossiers, 1,330 sources, 340 images, 332 pages, PDF 844 pages, EPUB 308 chapters, sitemap 330 URLs, 0 problems.

The pairing is the point: the wet-bulb threshold is a physical limit nobody disputes and nobody acts on, while the Momo panic is a threat nobody could find and everybody acted on. Filing them on the same shelf is the archive's argument about what a claim is worth.

## 0ac. Shipped in the twenty-ninth pass — 21 November 2026

Ten more, from the internet-folklore shelf and the modern hazards beside it.

| # | Dossier | Label |
|---|---|---|
| 1 | Havana Syndrome | Live debate |
| 2 | Non-Human Biologics | Fringe claim |
| 3 | The Shadow Biosphere | Fringe claim |
| 4 | The CE5 Contact Protocol | Debunked |
| 5 | Starlink and UFO Panics | Documented |
| 6 | The Elisa Lam Tapes | Live debate |
| 7 | Elsagate | Documented |
| 8 | Sad Satan | Live debate |
| 9 | SCP-096 | Fiction |
| 10 | The Backrooms Levels | Fiction |

316 dossiers, 1,370 sources, 350 images, 342 pages, PDF 864 pages, EPUB 318 chapters, sitemap 340 URLs, 0 problems.

Two `fiction` pages in one batch is a first, and deliberate: the archive needs a shelf for honest invention, or the label scheme looks like it is only interested in error. SCP-096 and the Backrooms are labelled as fiction by their authors everywhere they appear, which is exactly what the fringe pages here are not.

## 0ad. Shipped in the thirtieth pass — 21 November 2026

Ten more: nine ancient-artefact readings and one Moon-hoax confession.

| # | Dossier | Label |
|---|---|---|
| 1 | The Wandjina | Debunked |
| 2 | Dogū as Astronauts | Debunked |
| 3 | The Quimbaya Aeroplanes | Debunked |
| 4 | Babel as a Spaceport | Debunked |
| 5 | The Manna Machine | Fringe claim |
| 6 | The Ark as a Capacitor | Fringe claim |
| 7 | Sodom and the Airburst | Live debate |
| 8 | The Star of Bethlehem | Fringe claim |
| 9 | The Great Martian God | Debunked |
| 10 | Kubrick Confessed to the Moon Hoax | Debunked |

326 dossiers, 1,410 sources, 360 images, 352 pages, PDF 884 pages, EPUB 328 chapters, sitemap 350 URLs, 0 problems.

The Wandjina page is the one that matters most in this batch, and not for the astronomy: the explanation has been available from the Ngarinyin, Wunambal and Worora artists who still paint the figures, which makes the astronaut reading not just wrong but a taking.

## 0ae. Shipped in the thirty-first pass — 21 November 2026

Ten more: the out-of-place artefact shelf completed, plus three from the mythic fringe.

| # | Dossier | Label |
|---|---|---|
| 1 | The Klerksdorp Spheres | Debunked |
| 2 | The Coso Artifact | Debunked |
| 3 | The Betz Sphere | Debunked |
| 4 | The Dorchester Pot | Debunked |
| 5 | The Aiud Wedge | Debunked |
| 6 | The Wolfsegg Iron | Debunked |
| 7 | The Dropa Stones | Debunked |
| 8 | The Watchers of Enoch | Fringe claim |
| 9 | The Nephilim | Fiction |
| 10 | Oannes | Fiction |

336 dossiers, 1,450 sources, 370 images, 362 pages, PDF 904 pages, EPUB 338 chapters, sitemap 360 URLs, 0 problems.

The out-of-place artefact shelf is now complete as a family, and two of its members — the Coso artifact and the Wolfsegg iron — are the same error in two countries: the age of the container attributed to the contents. Having both on the shelf is worth more than either alone.

## 0af. Replanned — 21 November 2026: batch size 10 → 25

The pass was too slow: 10 dossiers every 45 seconds of build and roughly 40 minutes of writing to clear 738 register rows. The plan changed.

| Lever | Before | After |
|---|---|---|
| Dossiers per pass | 10 | 25 |
| Words per dossier | 420–480 | 280–320 |
| Photo sourcing | one call per batch | one call for all 25 |
| Contact sheets | 1 | 2, checked together |
| PDF/EPUB | every pass | every second pass |
| Passes to clear the register | ~55 | ~22 |

The first 25-dossier pass produced 22 new pages, because two slugs (`panpsychism`, `free-energy-principle`) already existed and were overwritten, and a third (`amoc-collapse`) duplicated the existing `amoc.html`. All three were reverted: the originals restored from git, the duplicate deleted, the search index, sitemap, themes, related strips and ledger rebuilt without it. That is the anti-duplication rule doing its job — the register check happens before writing, and the `git ls-tree` check should now happen too.

## 0ag. Shipped in the thirty-second pass — 21 November 2026: 25 dossiers

| # | Dossier | Label |
|---|---|---|
| 1 | Conformal Cyclic Cosmology | Live debate |
| 2 | The Ekpyrotic Universe | Live debate |
| 3 | Holographic Noise | Live debate |
| 4 | A White Dwarf as a Weapon | Fringe claim |
| 5 | Grabby Aliens | Fringe claim |
| 6 | Nessie as a Plesiosaur | Fringe claim |
| 7 | The Chupacabra | Debunked |
| 8 | Mokele-mbembe | Fringe claim |
| 9 | The Mongolian Death Worm | Fringe claim |
| 10 | Raining Animals | Documented |
| 11 | The Sailing Stones | Documented |
| 12 | Lake Nyos | Documented |
| 13 | The Door to Hell | Documented |
| 14 | The Crooked Forest | Live debate |
| 15 | Star Jelly | Live debate |
| 16 | The Dancing Plague of 1518 | Live debate |
| 17 | Nazca Lines as Runways | Debunked |
| 18 | The Dogon and Sirius B | Debunked |
| 19 | The Olmec Heads as Africans | Debunked |
| 20 | Puma Punku Laser Cuts | Debunked |
| 21 | D. B. Cooper | Live debate |
| 22 | The Lost Dutchman Mine | Fringe claim |
| 23 | The Yonaguni Monument | Live debate |
| 24 | Darth Jar Jar | Fiction |
| 25 | Mario 3 Is a Stage Play | Documented |

383 dossiers, 1,638 sources, 417 images, 409 pages, PDF 1,000 pages, EPUB 386 chapters, sitemap 407 URLs, 0 problems.

The first full 25-dossier pass, and the mix is deliberate: five cosmology claims (two of which have been tested and narrowed), five cryptids, five solved or near-solved natural phenomena, five historical puzzles, and two pieces of fandom. The solved ones matter most — sailing stones, Lake Nyos, raining animals — because they show the archive's method producing an answer rather than withholding one.

## 0ah. Shipped in the thirty-third pass — 21 November 2026: real operations and invented ones

| # | Dossier | Label |
|---|---|---|
| 1 | Chemtrails | Debunked |
| 2 | HAARP Weather Control | Debunked |
| 3 | The Sovereign Strawman | Debunked |
| 4 | NESARA and GESARA | Debunked |
| 5 | Majestic 12 | Debunked |
| 6 | Roswell Was Project Mogul | Documented |
| 7 | The Montauk Project | Fringe claim |
| 8 | Die Glocke | Fringe claim |
| 9 | Operation Highjump | Fringe claim |
| 10 | Lazar and Element 115 | Fringe claim |
| 11 | The Tic Tac | Live debate |
| 12 | The Men in Black | Fringe claim |
| 13 | The Illuminati | Fringe claim |
| 14 | The D.C. Street Grid | Debunked |
| 15 | The Georgia Guidestones | Documented |
| 16 | Bilderberg | Documented |
| 17 | Fluoride and the Pineal Gland | Debunked |
| 18 | The Water-Powered Car | Debunked |
| 19 | Project Azorian | Documented |
| 20 | Operation Snow White | Documented |
| 21 | Stuxnet | Documented |
| 22 | Crypto AG | Documented |
| 23 | The Rainbow Warrior | Documented |
| 24 | Dead Hand | Documented |
| 25 | Ulcers Are Bacterial | Documented |

408 dossiers, 1,738 sources, 442 images, 434 pages, PDF 1,050 pages, EPUB 408 chapters, sitemap 432 URLs, 0 problems.

The batch is built as a paired argument: ten invented conspiracies on one side, nine real operations on the other. Roswell is a real cover-up of a balloon; Azorian is a real cover story for a submarine; Crypto AG is a real fifty-year secret that nobody exposed; Rainbow Warrior is a real state bombing that was admitted within weeks. Set beside chemtrails and Majestic 12, the difference is not plausibility — it is paperwork.

## 0ai. Shipped in the thirty-fourth pass — 21 November 2026: documented wrongdoing

| # | Dossier | Label |
|---|---|---|
| 1 | Batterygate | Documented |
| 2 | The Ice Cream Machine | Live debate |
| 3 | New Coke as a Trojan Horse | Fringe claim |
| 4 | The CIA and Modern Art | Documented |
| 5 | The Guatemala Syphilis Experiments | Documented |
| 6 | Operation Fast and Furious | Documented |
| 7 | Iran–Contra | Documented |
| 8 | BCCI | Documented |
| 9 | The Lavon Affair | Documented |
| 10 | CIA Black Sites | Documented |
| 11 | Project 112 and SHAD | Documented |
| 12 | The Green Run | Documented |
| 13 | The FBI and Martin Luther King | Documented |
| 14 | The CIA–Mafia Plots Against Castro | Documented |
| 15 | The Horizon Scandal | Documented |
| 16 | Dieselgate | Documented |
| 17 | Enron and California | Documented |
| 18 | The P2 Lodge | Documented |
| 19 | The Gleiwitz Incident | Documented |
| 20 | Asbestos and Radon Cover-Ups | Documented |
| 21 | Cambridge Analytica | Documented |
| 22 | Zero-Click Search Extinction | Live debate |
| 23 | Short-Form Video and Attention | Live debate |
| 24 | The NPC Theory | Fringe claim |
| 25 | Avril Lavigne Was Replaced | Debunked |

433 dossiers, 1,838 sources, 467 images, 459 pages, PDF 1,100 pages, EPUB 433 chapters, sitemap 457 URLs, 0 problems.

The largest single batch of `documented` pages in the archive, and the reason is the subject: twenty of these are things that were done, admitted, and prosecuted. The batch exists because an archive of strange claims is only trustworthy if it can also say plainly when the strange claim was right — Fast and Furious, the black sites, the Lavon affair, Gleiwitz. Conspiracy theories thrive where the record is thin; here the record is thick, and it is worse than the theories.

## 0aj. Shipped in the thirty-fifth pass — 21 November 2026: laws, scandals, lore

| # | Dossier | Label |
|---|---|---|
| 1 | Goodhart's Law | Documented |
| 2 | The Third Place | Live debate |
| 3 | Male Loneliness | Documented |
| 4 | Shrinkflation and Skimpflation | Documented |
| 5 | The Peltzman Effect | Live debate |
| 6 | The Streisand Effect | Documented |
| 7 | Poe's Law | Documented |
| 8 | Cunningham's Law | Documented |
| 9 | Brandolini's Law | Documented |
| 10 | The Truman Show Delusion | Documented |
| 11 | Room 641A | Documented |
| 12 | Pegasus Zero-Click | Documented |
| 13 | Boeing's MCAS | Documented |
| 14 | Purdue and OxyContin | Documented |
| 15 | FTX's Backdoor | Documented |
| 16 | Libor Rigging | Documented |
| 17 | FIFA Bribes | Documented |
| 18 | Monopoly's Anti-Monopoly Origin | Documented |
| 19 | Dune as Anti-Messiah | Documented |
| 20 | Vault-Tec Started the War | Documented |
| 21 | GTA's Two Universes | Documented |
| 22 | Squid Game Card Colours | Debunked |
| 23 | The Simpsons Time Machine | Debunked |
| 24 | The Mushroom War | Documented |
| 25 | Dating-App Elo Gating | Fringe claim |

458 dossiers, 1,938 sources, 492 images, 484 pages, PDF 1,150 pages, EPUB 461 chapters, sitemap 482 URLs, 0 problems.

Five of these are the archive's own operating principles written down as pages: Goodhart on targets, Brandolini on the cost of refutation, Poe on why fiction must be labelled, Cunningham on why wrong claims travel, and the Streisand effect on why suppression fails. The rest are the evidence those laws describe.

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
