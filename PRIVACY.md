# Privacy — what this site does with your data

The Larger World Archive · version 1.0 · effective 23 November 2026

Short version: **the site collects nothing about you.** There is no account, no
analytics, no advertising, no third-party script, no cookie and no server that the
archive controls. Everything below is a checkable statement about the code in this
repository, not a promise about intentions.

## 1. What is served

The site is a set of static HTML files, images and one stylesheet, published through
GitHub Pages. When you open a page, your browser requests those files from GitHub's
servers. GitHub, as the host, may keep standard web-server logs — IP address, user
agent, requested path, timestamp — under
[GitHub's own privacy statement](https://docs.github.com/en/site-policy/privacy-policies).
The archive does not receive, store or process those logs, and has no analytics of any
kind on the pages.

| Question | Answer | How to check |
|---|---|---|
| Any analytics or tag manager? | No | `grep -r "google-analytics\|gtag\|plausible\|matomo" *.html` returns nothing |
| Any third-party script? | No | Every `<script src>` is a local path under `assets/` |
| Any cookie set? | No | `document.cookie` appears nowhere in the codebase |
| Any form or input that transmits? | No | The site has no `<form>` element |
| Any ad or tracking pixel? | No | No external images are loaded; all images are served from this repository |

## 2. What is stored on your device

Two things, both chosen by you, both local to your browser:

| Stored item | Key | Purpose | Lifetime |
|---|---|---|---|
| Theme preference | `lwa-theme` | Remembers dark or light | Until you clear site data |
| Text size preference | `lwa-size` | Remembers your chosen type size | Until you clear site data |
| Offline cache | service worker cache `lwa-v1` | Keeps pages readable without a network | Until you clear site data |

These are stored with `localStorage` and the Cache API. They never leave your device,
are not transmitted anywhere, and contain no identifier — the value stored is the word
`light` or `dark`, or `sm`/`md`/`lg`. You can remove them at any time by clearing site
data for this domain; the site continues to work without them.

## 3. What is not collected

No name, email address, account, password, payment detail, location, device
fingerprint, referral path, session recording, heat map or crash report. There is no
newsletter and no contact form. The archive has no way to identify a reader.

## 4. Donations

The support links point to GitHub Sponsors, Ko-fi, PayPal and a UPI address. Choosing
one takes you to that provider's site, where **their** privacy terms apply; the archive
receives only the notification the provider sends, which typically includes a display
name and an amount. No donation data is stored on this site, and no reader is ever
asked to identify themselves to read anything.

## 5. Your rights, and the honest position on them

Under India's Digital Personal Data Protection Act, 2023, a data principal has rights
of access, correction, erasure and grievance redressal in relation to personal data
processed by a data fiduciary. **This site processes no personal data**, so there is
nothing here to access, correct or erase. The two preferences in §2 stay on your device
and are under your control through your browser.

If you believe the archive holds something about you — for example because you emailed
the author — you can ask what is held and ask for it to be deleted, and the request
will be answered. Grievance contact: the address on the
[about page](https://drsamonline.github.io/LARGE_GLOBE/about.html).

This document describes the software as shipped. It is not legal advice, and it makes
no claim of certification or regulatory approval.

## 6. Children

The archive is a reference work and is not directed at children. It collects no data
from anyone, so it collects none from children.

## 7. Changes

If the site ever adds analytics, accounts or a comment system, this document changes in
the same commit that adds them, and the version number above is incremented. The
repository history is public, so any such change is visible.
