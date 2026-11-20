#!/usr/bin/env python3
"""Check every external URL the archive cites. Weekly, not per-push."""
import argparse, concurrent.futures as cf, glob, re, urllib.request

UA = "LargerWorldArchive-linkcheck/1.0 (+https://drsamonline.github.io/LARGE_GLOBE/)"


def head(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return url, r.status
    except Exception as e:                      # noqa: BLE001
        code = getattr(e, "code", None)
        return url, code or str(e)[:60]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default="dead-links.md")
    args = ap.parse_args()

    urls, seen = [], set()
    for p in glob.glob("*.html"):
        for u in re.findall(r'href="(https?://[^"]+)"', open(p, encoding="utf-8").read()):
            u = u.split("#")[0]
            if u not in seen:
                seen.add(u); urls.append(u)

    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        results = list(ex.map(head, urls))

    dead = [(u, s) for u, s in results if s != 200]
    with open(args.report, "w", encoding="utf-8") as f:
        f.write(f"# Link check\n\n{len(urls)} unique external URLs, {len(dead)} not answering 200.\n\n")
        f.write("| URL | Result |\n|---|---|\n")
        for u, s in sorted(dead):
            f.write(f"| {u} | {s} |\n")
    print(f"{len(urls)} checked, {len(dead)} not 200 — see {args.report}")


if __name__ == "__main__":
    main()
