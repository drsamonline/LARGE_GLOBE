# NOTICE — third-party works in this repository

The Larger World Archive
Copyright (c) 2026 Dr. Sohil Momin
Licence for the archive's own text, markup and diagrams: CC BY-NC 4.0 (see `LICENSE`).

This file records what is inside the repository that the archive did not create, and
under what terms it is used. It is generated from the pages themselves, so it cannot
drift from what the site actually serves.

---

## 1. Photographs and illustrations

Every photograph on the site comes from Wikimedia Commons under a free licence. Each
one is stored locally, credited on the dossier it appears on, and listed with its
author, its licence and a link to the source file on the
[image credits page](https://drsamonline.github.io/LARGE_GLOBE/credits.html).

| | |
|---|---|
| Photographs in use | 2,827 |
| Distinct licences | CC0, Public domain, CC BY 2.0/3.0/4.0, CC BY-SA 2.0/3.0/4.0, No known restrictions |
| Attribution required | Yes, for CC BY and CC BY-SA — the author is named in the caption and on the credits page |
| Share-alike | Applies to adaptations of CC BY-SA images; images are used unmodified apart from format conversion and scaling |
| Non-free content | None. No image is used under fair use or a non-free licence |

No photograph is hotlinked; all are served from this repository, which keeps the
archive readable offline and keeps the licence terms verifiable.

## 2. Diagrams

The 101 diagrams are drawn for this archive and are the copyright of the author,
released under the same CC BY-NC 4.0 terms as the text. They are labelled as the
archive's own work wherever they appear.

## 3. Fonts

The site uses no webfonts. It relies on the reader's system fonts through a font stack
(`Iowan Old Style`, `Palatino Linotype`, `Georgia`, `Times New Roman`, then generic
serif), so no font licence is implicated.

## 4. Code and libraries

No third-party JavaScript library is bundled. The scripts in `assets/` are written for
this site. Icons are inline SVG. No CDN, no analytics SDK, no tag manager.

## 5. Quoted text and sources

Dossiers quote short passages from published works for comment and criticism, with the
source named and linked. Longer extracts are not reproduced; where a full text is
freely available it is linked instead. Every dossier lists its sources, and the count
is printed on the page.

## 6. Software used to build the site

| Tool | Use | Licence |
|---|---|---|
| Python 3.12 | build scripts | PSF licence |
| Pillow | image conversion to WebP | HPND |
| PyMuPDF | page counting for the print edition | AGPL-3.0 (used as a build-time tool, not distributed) |
| Chromium (headless) | rendering the print edition to PDF | BSD-3-Clause |
| LibreOffice | document conversion during build | MPL-2.0 |

None of these are shipped to the reader; they run on the build machine.

---

## How to report an attribution error

If a credit is wrong, incomplete or missing, open an issue on the repository or write
to the address on the [about page](https://drsamonline.github.io/LARGE_GLOBE/about.html).
Corrections to attribution are treated as urgent, because a licence breach is worse
than a factual error.

*Generated from `credits.html` and the dossier pages. Last regenerated: 23 November 2026.*
