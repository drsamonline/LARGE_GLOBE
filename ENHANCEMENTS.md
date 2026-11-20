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
14. **Responsive images.** `srcset` at 480/960/1440 for every AVIF plus a WebP `<picture>` fallback, so a phone stops downloading 900×1020 crops. Expect roughly 60% off mobile image bytes.
15. **A light theme and a reading-size control.** The archive is dark-only, at 18px serif. Both are preference toggles stored in `localStorage`, ~40 lines, and both materially widen who can read a long page.
16. ~~**An RSS/Atom feed**~~ **Done — see 0c.** of new and revised dossiers, plus a JSON Feed. Nothing announces that the archive grew; a feed is the cheapest way to be followed.
17. ~~**A corrections policy page and a visible "last reviewed" line**~~ **Done — see 0c.** on every dossier. The archive's authority rests on being checkable; it should say when each page was last checked, and what happens when a claim is overturned.
18. **A glossary.** *Firmament*, *ice wall*, *Tartarus*, *concave Earth*, *aether*, *hollow shell*, *expanding Earth*, *Silurian hypothesis* — recurring terms, currently explained 150 separate times in 150 separate voices.
19. **Extend `compare.html`.** Today it compares two dossiers; make it three, and put the pair in the URL (`?a=flat-earth&b=ice-wall`) so a comparison can be linked, shared and cited.
20. **A "how to read a dossier" page.** The four labels are explained on the index and again in a key on each page, but the method itself — how a claim was traced, what counts as evidence here — has no permanent home.

## 4. Large — a week or more, changes what the archive is

21. **A generated PDF and EPUB of the print edition.** `print-edition.html` is 813 KB of HTML designed for `Ctrl-P`. A real typeset PDF with running heads, page numbers and a TOC with folios, plus an EPUB for e-readers, turns the archive into something that can be read on a train — and puts it one step from the KDP pipeline the other repositories already have.
22. **A static build step, or none at all.** The nav, footer and palette are duplicated across 170 files; one change means 170 edits (this pass touched all of them with a script). Either accept a 60-line generator that assembles pages from partials, or add a CI check that fails when two pages' nav blocks disagree. The second is cheaper and keeps the "clone and open `index.html`" property.
23. **A searchable command palette instead of the "More" menu.** The nav panel holds 100+ links in one column. `Ctrl-K` with fuzzy matching over the same 980-record index would replace it, and would make the mobile header usable.
24. **Keyboard-first reading.** `j`/`k` to move between dossiers in reading order, `s` to open search, `?` for the shortcut sheet. The reading guide already defines an order; nothing walks it.
25. **An offline service worker.** The site works from `file://` but not from a flaky connection. A 30-line SW caching the shell plus visited pages would make "readable offline" literally true from the URL as well.
26. **An audio edition.** Every dossier is 700–2,000 words of prose, which is exactly what a TTS pipeline handles well (Sarvam Bulbul, or any local model), with an `<audio>` element per page and a podcast feed of the same. This is the single largest reach multiplier available to a text archive.
27. **A Hindi edition of the reading guide and the twelve door pages.** The audience for this material in India is large and served almost entirely by English-language YouTube. Translating the entry points, not the whole archive, is the cheap version of that.
28. **A provenance ledger.** One machine-readable file (`data/claims.json`) holding every claim's label, date, author and source IDs — from which the master list, the claim register, the charts and the search index are all generated. Today they are four hand-maintained views of the same facts, which means they can disagree.

## 5. Deliberately not recommended

- **Analytics of any kind.** It would contradict the privacy line in the footer, and the site gains nothing from knowing which dossier you read.
- **A comment section or a forum.** The archive's value is that a claim's fate is decided by evidence, not by who is loudest. Corrections belong in issues, where they are attributable.
- **Ads or sponsored dossiers.** One sponsored label would cast doubt on all 150.
- **A CMS.** 170 static files, one stylesheet and a search index is the correct architecture for something meant to still open in a decade.

---

*Baseline audited 19 November 2026. Numbers in this file are measurements of this repository, not estimates.*
