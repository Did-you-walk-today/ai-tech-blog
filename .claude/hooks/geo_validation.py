#!/usr/bin/env python3
"""
GEO (Generative Engine Optimization) validation — Section D of post-validation.

Rules live in SEO_GUIDE.md §11–§13. This checks the *post-level*, per-post
half of GEO: whether a post carries the evidence a generative engine needs to
cite it. The other half — site-wide schema and entity declaration — is one-off
infrastructure and is not checked here.

Emits the same protocol as image_validation.py:
    ERROR:<message>
    WARN:<message>

Severity is downgraded to WARN for _drafts/ on every rule. A draft legitimately
predates its data file (written at Phase 3) and its source links; these must be
fixed before Phase 6, which is exactly what WARN means in this pipeline.

Usage:
    python3 geo_validation.py <post_path>
    python3 geo_validation.py --report        # repo-wide status
"""

import json
import os
import re
import sys
from pathlib import Path

# _data/*.json fields CLAUDE.md declares mandatory for every post dataset.
REQUIRED_DATA_FIELDS = [
    "schema_version", "slug", "title", "description", "data_updated",
    "source_post", "category", "cluster", "format",
    "key_facts", "faq_summary", "primary_sources",
]

MIN_PRIMARY_SOURCES = 3
MIN_INLINE_CITATIONS = 1
KEY_FACTS_RANGE = (5, 10)

OWN_HOSTS = ("jsonhouse.com",)

FENCE_RE = re.compile(r"```.*?```", re.S)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
# An image is not a citation. Strip ![alt](url) before looking for links,
# otherwise a post carrying one remote image and no sources passes D1.
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)")
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
# [ref]: https://... — reference-style definitions render as real links.
REF_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(https?://\S+)", re.M)
# Raw HTML anchors are valid in kramdown and render as real links.
HTML_HREF_RE = re.compile(r"""<a\s[^>]*href=["'](https?://[^"']+)["']""", re.I)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def split_post(path: Path):
    """Return (frontmatter_text, body_text_without_code_fences)."""
    raw = path.read_text(encoding="utf-8")
    fm_match = FRONTMATTER_RE.match(raw)
    fm = fm_match.group(0) if fm_match else ""
    body = raw[len(fm):]
    return fm, FENCE_RE.sub("", body)


def inline_citations(body: str):
    """External primary-source links in the body, own domain excluded.

    Counts every form that renders as a followable link: markdown links,
    autolinks, reference-style definitions, and raw HTML anchors. A bare domain
    written as prose ('platform.claude.com') is not a citation — a crawler
    cannot follow it. That distinction is the entire point of rule D1.

    Images are excluded: a remote illustration is not evidence for a claim.
    """
    body = IMAGE_RE.sub("", body)
    urls = (MD_LINK_RE.findall(body) + AUTOLINK_RE.findall(body)
            + REF_DEF_RE.findall(body) + HTML_HREF_RE.findall(body))
    return [u for u in urls if not any(h in u for h in OWN_HOSTS)]


def check(post_path: Path, root: Path):
    """Yield (severity, message). Severity is 'ERROR' or 'WARN' pre-downgrade."""
    name = post_path.stem                      # YYYY-MM-DD-slug
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name)
    _, body = split_post(post_path)

    # --- D1: inline outbound primary-source citation ---
    cites = inline_citations(body)
    if len(cites) < MIN_INLINE_CITATIONS:
        yield ("ERROR",
               f"D1 NO INLINE CITATION: 0 outbound primary-source links in the body. "
               f"A generative engine reads the HTML, not _data/*.json — bare domains "
               f"in prose ('platform.claude.com') do not count. Link at least "
               f"{MIN_INLINE_CITATIONS} primary source where the claim is made "
               f"(usually the Methodology section). See SEO_GUIDE.md §12.")

    # --- D4: body links its own dataset ---
    if f"data/{slug}.json" not in body:
        yield ("ERROR",
               f"D4 NO DATASET LINK: body must link its dataset — "
               f"https://www.jsonhouse.com/data/{slug}.json — so crawlers "
               f"discover the machine-readable copy. See CLAUDE.md.")

    # --- data file presence gate for D2/D3/D5 ---
    data_path = root / "_data" / f"{name}.json"
    if not data_path.exists():
        yield ("ERROR",
               f"D5 NO DATA FILE: _data/{name}.json is missing. Every post ships "
               f"as a 3-piece set (post + dataset + Korean review). See CLAUDE.md.")
        return

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except Exception as exc:
        yield ("ERROR", f"D5 DATA FILE UNPARSEABLE: _data/{name}.json — {exc}")
        return

    # --- D5: required schema fields ---
    missing = [f for f in REQUIRED_DATA_FIELDS if f not in data]
    if missing:
        yield ("ERROR",
               f"D5 DATA FIELDS MISSING: _data/{name}.json lacks {', '.join(missing)}. "
               f"All 12 required fields must be present. See CLAUDE.md.")

    # --- D2: primary_sources depth ---
    sources = data.get("primary_sources") or []
    if len(sources) < MIN_PRIMARY_SOURCES:
        yield ("ERROR",
               f"D2 THIN SOURCES: primary_sources has {len(sources)} entries "
               f"(minimum {MIN_PRIMARY_SOURCES}). These become the Dataset "
               f"schema's citation array — thin sourcing is thin evidence.")
    for i, s in enumerate(sources):
        if not isinstance(s, dict) or not s.get("url") or not s.get("title"):
            yield ("ERROR",
                   f"D2 MALFORMED SOURCE: primary_sources[{i}] needs both "
                   f"'title' and 'url'.")
            break

    # --- D3: key_facts count ---
    facts = data.get("key_facts") or []
    lo, hi = KEY_FACTS_RANGE
    if not (lo <= len(facts) <= hi):
        yield ("WARN",
               f"D3 KEY FACTS COUNT: {len(facts)} (expected {lo}-{hi}). "
               f"These are the units a model can lift and attribute.")

    # --- D5b: data_updated must mirror the post's ---
    fm, _ = split_post(post_path)
    fm_updated = re.search(r"^data_updated:\s*(\S+)", fm, re.M)
    if fm_updated and data.get("data_updated") != fm_updated.group(1).strip("\"'"):
        yield ("ERROR",
               f"D5 DATE MISMATCH: front matter data_updated="
               f"{fm_updated.group(1)} but _data/{name}.json has "
               f"{data.get('data_updated')}. Freshness is a citation signal; "
               f"the two copies must agree.")


def run_one(post_path: Path, root: Path) -> list:
    is_draft = "_drafts" in post_path.parts
    out = []
    for severity, msg in check(post_path, root):
        if is_draft:
            severity = "WARN"
        out.append(f"{severity}:{msg}")
    return out


def report(root: Path):
    """Repo-wide status, mirroring image_validation.py --report."""
    targets = sorted(list((root / "_posts").glob("*.md")) +
                     list((root / "_drafts").glob("*.md")))
    total_err = total_warn = 0
    for p in targets:
        lines = run_one(p, root)
        errs = [l for l in lines if l.startswith("ERROR:")]
        warns = [l for l in lines if l.startswith("WARN:")]
        total_err += len(errs)
        total_warn += len(warns)
        status = "FAIL" if errs else ("warn" if warns else "ok  ")
        loc = "draft" if "_drafts" in p.parts else "post "
        print(f"[{status}] {loc} {p.stem}")
        for l in lines:
            tag, msg = l.split(":", 1)
            print(f"         {tag}: {msg.split('.')[0]}.")
    print(f"\n{len(targets)} files — {total_err} errors, {total_warn} warnings")
    return 1 if total_err else 0


def main():
    if len(sys.argv) < 2:
        return 0
    if sys.argv[1] == "--report":
        return report(repo_root())

    post_path = Path(sys.argv[1])
    if not post_path.exists():
        return 0
    root = repo_root()
    for line in run_one(post_path, root):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
