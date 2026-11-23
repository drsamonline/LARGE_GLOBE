#!/usr/bin/env python3
"""Structural validation of the EPUB, since epubcheck needs Java.

This is not a substitute for epubcheck. It checks what can be checked without it:
the container, the package document, the manifest, the spine, well-formedness of
every XHTML file, and unique ids.

    python3 tools/check-epub.py
"""
import os, re, sys, zipfile
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PATH = os.environ.get("EPUB_PATH", "assets/larger-world-archive.epub")
problems = []


def main():
    if not os.path.exists(PATH):
        print("no EPUB to check")
        return 0
    z = zipfile.ZipFile(PATH)
    names = z.namelist()

    # 1. the mimetype entry must be first and stored uncompressed
    if "mimetype" not in names:
        problems.append("no mimetype entry")
    else:
        info = z.getinfo("mimetype")
        if info.compress_type != zipfile.ZIP_STORED:
            problems.append("mimetype is compressed; readers require it stored")
        if names[0] != "mimetype":
            problems.append("mimetype is not the first entry")
        if z.read("mimetype").strip() != b"application/epub+zip":
            problems.append("mimetype has the wrong value")

    # 2. container points at a package document that exists
    if "META-INF/container.xml" not in names:
        problems.append("no META-INF/container.xml")
        return report()
    root = ET.fromstring(z.read("META-INF/container.xml"))
    opf_path = None
    for el in root.iter():
        if el.tag.endswith("rootfile"):
            opf_path = el.get("full-path")
    if not opf_path or opf_path not in names:
        problems.append(f"container points at {opf_path}, which is not in the archive")
        return report()

    # 3. the package document: unique ids, manifest items exist, spine refs resolve
    opf = ET.fromstring(z.read(opf_path))
    base = os.path.dirname(opf_path)
    ids, items, spine = {}, {}, []
    for el in opf.iter():
        tag = el.tag.split("}")[-1]
        if tag == "item":
            iid, href = el.get("id"), el.get("href")
            if iid in ids:
                problems.append(f"duplicate manifest id {iid}")
            ids[iid] = href
            items[iid] = os.path.normpath(os.path.join(base, href)).replace("\\", "/")
        elif tag == "itemref":
            spine.append(el.get("idref"))
    for iid, path in items.items():
        if path not in names:
            problems.append(f"manifest item {iid} -> {path} is missing from the archive")
    for ref in spine:
        if ref not in ids:
            problems.append(f"spine references {ref}, which is not in the manifest")

    # 4. every XHTML file parses, and ids inside a file are unique
    xhtml = [n for n in names if n.endswith((".xhtml", ".html"))]
    for n in xhtml:
        try:
            tree = ET.fromstring(z.read(n))
        except ET.ParseError as e:
            problems.append(f"{n} is not well-formed XML: {e}")
            continue
        seen = set()
        for el in tree.iter():
            eid = el.get("id")
            if eid:
                if eid in seen:
                    problems.append(f"{n} has duplicate id {eid}")
                seen.add(eid)

    # 5. a navigation document should be declared
    if not any("nav" in (el.get("properties") or "") for el in opf.iter()
               if el.tag.split("}")[-1] == "item"):
        problems.append("no navigation document declared in the manifest")

    print(f"epub: {len(xhtml)} documents, {len(items)} manifest items, {len(spine)} spine entries")
    return report()


def report():
    if problems:
        for p in problems[:20]:
            print("  problem:", p)
        print(f"{len(problems)} problem(s)")
        return 1
    print("  ok  container, manifest, spine, XHTML well-formedness, ids unique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
