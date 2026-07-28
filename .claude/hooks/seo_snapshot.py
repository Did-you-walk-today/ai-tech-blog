#!/usr/bin/env python3
"""Snapshot every page's SEO <head> data so two states can be diffed.

Built for changes that touch shared templates, layouts, or _config.yml, where
the damage is invisible in a browser: a wrong locale key renders an empty
<title> while og:title stays correct, and nothing looks broken until a search
engine reports duplicate titles weeks later. Diffing a snapshot taken before
the change against one taken after makes the blast radius explicit — which
pages moved, which fields moved, and whether any URL shifted.

Output is one TSV row per page, sorted by URL, so plain `diff` works.

Usage:
    # snapshot a local build (matches CI: JEKYLL_ENV=production)
    JEKYLL_ENV=production bundle exec jekyll build -d /tmp/base
    python3 .claude/hooks/seo_snapshot.py /tmp/base > /tmp/base.tsv

    # ... make the change, rebuild to /tmp/after, then:
    python3 .claude/hooks/seo_snapshot.py /tmp/after > /tmp/after.tsv
    diff /tmp/base.tsv /tmp/after.tsv

    # snapshot the deployed site instead (walks sitemap.xml)
    python3 .claude/hooks/seo_snapshot.py --live > /tmp/live.tsv

What to check in the diff:
  1. The `url` column is unchanged — a permalink shift breaks live links.
  2. Post pages are untouched unless the change was meant to reach them.
  3. Only the fields you intended to move actually moved.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import html
import os
import re
import sys
import urllib.error
import urllib.request

SITE = "https://www.jsonhouse.com"
FIELDS = ("url", "title", "desc", "robots", "canonical", "og_title", "words")
TIMEOUT_SECONDS = 30
# Enough to finish a ~90 page site quickly; low enough to stay polite.
MAX_WORKERS = 8
UA = "jsonhouse-seo-snapshot/1.0"


def visible_word_count(doc: str) -> int:
    body = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", " ", doc)
    return len(re.sub(r"(?s)<[^>]+>", " ", body).split())


def meta(doc: str, name: str, attr: str = "name") -> str:
    """Read a meta tag's content. Attribute order is not guaranteed, so try
    both arrangements before giving up."""
    for pattern in (
        rf'<meta\s+[^>]*{attr}=["\']{re.escape(name)}["\'][^>]*content=["\'](.*?)["\']',
        rf'<meta\s+[^>]*content=["\'](.*?)["\'][^>]*{attr}=["\']{re.escape(name)}["\']',
    ):
        m = re.search(pattern, doc, re.S | re.I)
        if m:
            return html.unescape(m.group(1)).strip()
    return ""


def extract(url: str, doc: str) -> dict[str, str]:
    t = re.search(r"<title>(.*?)</title>", doc, re.S)
    c = re.search(r'<link\s+[^>]*rel=["\']canonical["\'][^>]*href=["\'](.*?)["\']', doc, re.I)
    return {
        "url": url,
        "title": html.unescape(t.group(1)).strip() if t else "",
        "desc": meta(doc, "description"),
        "robots": meta(doc, "robots"),
        "canonical": c.group(1).strip() if c else "",
        "og_title": meta(doc, "og:title", attr="property"),
        "words": str(visible_word_count(doc)),
    }


def from_build(root: str) -> list[dict[str, str]]:
    rows = []
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(dirpath, fn)
            url = "/" + os.path.relpath(path, root).replace(os.sep, "/")
            url = re.sub(r"index\.html$", "", url)
            with open(path, encoding="utf-8", errors="ignore") as fh:
                rows.append(extract(url, fh.read()))
    return rows


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        return resp.read().decode("utf-8", "ignore")


def from_live() -> list[dict[str, str]]:
    try:
        sitemap = fetch(f"{SITE}/sitemap.xml")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SystemExit(f"ERROR: could not fetch sitemap: {exc}") from exc

    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", sitemap)
    if not urls:
        raise SystemExit("ERROR: sitemap contained no <loc> entries.")
    print(f"fetching {len(urls)} live pages...", file=sys.stderr)

    def one(u: str) -> dict[str, str]:
        path = u[len(SITE):] or "/"
        try:
            return extract(path, fetch(u))
        except Exception as exc:  # noqa: BLE001 - a failed page must not abort the run
            print(f"  WARN {path}: {exc}", file=sys.stderr)
            return {**{f: "" for f in FIELDS}, "url": path, "title": f"<FETCH FAILED: {exc}>"}

    with concurrent.futures.ThreadPoolExecutor(MAX_WORKERS) as ex:
        return list(ex.map(one, urls))


def main() -> int:
    ap = argparse.ArgumentParser(description="Snapshot SEO head data as TSV.")
    ap.add_argument("build_dir", nargs="?", help="path to a built _site directory")
    ap.add_argument("--live", action="store_true", help=f"crawl {SITE} via its sitemap instead")
    args = ap.parse_args()

    if args.live == bool(args.build_dir):
        ap.error("give either a build directory or --live, not both")

    rows = from_live() if args.live else from_build(args.build_dir)
    rows.sort(key=lambda r: r["url"])

    print("\t".join(FIELDS))
    for r in rows:
        print("\t".join(r[f].replace("\t", " ").replace("\n", " ") for f in FIELDS))
    print(f"{len(rows)} pages", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
