#!/usr/bin/env python3
"""Run every check in the repository, in order, and print one verdict.

    python3 tools/check-all.py          # full run
    python3 tools/check-all.py --fast   # skip the slow arithmetic sweep

Each check is a separate script so it can be read, argued with and replaced. This
is the front door: one command that answers "is the archive consistent?" without
anyone having to remember the list.
"""
import subprocess, sys, time

CHECKS = [
    ("structure — links, anchors, page invariants", ["tools/check-structure.py"], False),
    ("size budget", ["tools/check-size.py"], False),
    ("images — references, blanks, credits, counts, dimensions", ["tools/check-images.py"], False),
    ("shared shell in step with index.html", ["tools/rebuild-shell.py", "--check"], False),
    ("charts in step with the ledger", ["tools/rebuild-charts.py", "--check"], False),
    ("sitemap lists every page", ["tools/build-sitemap.py", "--check"], False),
    ("EPUB structure — container, manifest, spine, XHTML", ["tools/check-epub.py"], False),
    ("feed lists current entries", ["tools/build-feed.py", "--check"], False),
    ("stylesheet hash current on every page", ["tools/stamp-css.py", "--check"], False),
    ("README numbers match the repository", ["tools/update-readme.py", "--check"], False),
    ("arithmetic in the mathematics dossiers", ["tools/check-math.py"], True),
]


def main():
    fast = "--fast" in sys.argv
    failed = []
    print("The Larger World Archive — consistency checks\n")
    for name, cmd, slow in CHECKS:
        if fast and slow:
            print(f"  skip  {name}")
            continue
        t0 = time.time()
        r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True)
        dt = time.time() - t0
        out = (r.stdout or r.stderr).strip().splitlines()
        tail = out[-1] if out else ""
        if r.returncode == 0:
            print(f"  ok    {name}  ({dt:.1f}s)  {tail[:70]}")
        else:
            failed.append(name)
            print(f"  FAIL  {name}  ({dt:.1f}s)")
            for line in out[:6]:
                print(f"        {line}")

    print()
    if failed:
        print(f"{len(failed)} check(s) failed: {', '.join(failed)}")
        return 1
    print(f"all {len(CHECKS) - (1 if fast else 0)} checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
