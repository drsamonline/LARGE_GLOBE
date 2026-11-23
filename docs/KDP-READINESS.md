# KDP readiness — what the archive needs to become a paperback

Measured 23 November 2026 against Amazon KDP's published limits, using
`kdp_specs.py` from the KDP publishing skill as the single source of constants.
Nothing here is estimated; every figure is arithmetic on the real file.

## The finding, first

**The archive cannot be one paperback.** The current print edition is **2,343 pages**
at A5 (420 × 594.96 pt). KDP's ceiling for black-ink paperback is **828 pages** at every
trim from 5×8 up to 8×10, and **590** at 8.5×11. A single volume would be rejected for
page count before anyone looked at the interior.

It needs **three volumes** at 6×9.

## What is already right

| Check | Result |
|---|---|
| Fonts embedded | Yes — 10 fonts, all embedded |
| Type 3 fonts (silent rejection) | None |
| Page size | 420 × 594.96 pt, consistent throughout |
| Interior colour | Black only, no colour plates |
| Images in the print edition | None — images are hidden in print, which keeps the file at 6 MB |

The font audit is the check that matters most, because a Type 3 font passes every
geometric test and fails at the printer. Chromium writes Type 3 for variable fonts; this
PDF uses static Liberation faces and is clean.

## The three-volume split

At 6×9, black ink, white paper (thickness 0.002252 in per page):

| Volume | Pages | Spine | Cover spread (bleed included) | Gutter |
|---|---|---|---|---|
| I | 828 | 1.8647 in | 14.115 × 9.25 in | 0.875 in |
| II | 828 | 1.8647 in | 14.115 × 9.25 in | 0.875 in |
| III | 687 | 1.5471 in | 13.797 × 9.25 in | 0.750 in |

Cream paper would allow only 776 pages per volume and would need four volumes; white is
the right choice here.

Two constraints that follow:

- **The gutter moves between volumes.** Volume III drops into the 0.750 in band, so its
  interior must be re-laid out, not simply sliced from the single-volume PDF.
- **Spine text is allowed** on all three (the threshold is 79 pages), with 0.0625 in
  clearance from both fold lines.

## What each volume needs before upload

| Item | Status |
|---|---|
| Interior PDF at 6×9 with mirrored gutter | Not built — the current file is A5, single volume |
| Cover spread per volume at 300 dpi | Not built — spine differs for volume III |
| Front-cover JPG per volume | Not built |
| ISBN | Not assigned — KDP gives a free one per volume, or use your own |
| Metadata: title, subtitle, blurb, categories, keywords | Not written |
| QA gate: trim, bleed, safe area, font, page count | Interior passes fonts; geometry untested at 6×9 |

## What I would do next, in order

1. Build a 6×9 interior from `print-edition.html` with a mirrored 0.875 in gutter, and
   confirm the page count still lands in the 701–828 band. If it grows past 828, the
   gutter requirement changes and the layout must be redone — the circular trap.
2. Split at a chapter boundary, not a page number, so no dossier is cut in half.
3. Build three covers, each with its own spine from the measured page count.
4. Write the metadata sheet once, then per volume.
5. Run the QA gate and read every line before upload.

## The honest caveat

This document is a readiness assessment, not a publication. It says what is measured and
what is missing. It does not claim the archive is ready to upload, and it does not
promise that a KDP upload will be accepted on the first attempt — the interior has not
been built at 6×9 at all yet.
