#!/usr/bin/env python3
"""AiTechBlog — Post image validation (Section C).

Two modes:

  1. Hook mode (called from post-validation.sh):
         python3 image_validation.py <post_file.md>
     Emits `ERROR:`/`WARN:` lines on stdout, one per line. The caller merges
     them into its own report.

  2. Report mode (manual, whole repo):
         python3 image_validation.py --report
     Prints a per-slug status table for every file in _posts/ and _drafts/.

Rules (see IMAGE_GUIDE.md):
  C1 cover file exists            C5 body image alt non-empty
  C2 cover alt present & useful   C6 total image count <= 5
  C3 cover 1200x630, <= 200KB     C7 filename convention
  C4 body image refs resolve      C8 body image size limits

Severity depends on location: _drafts/ downgrades every ERROR to WARN,
because a draft legitimately has no artwork yet. _posts/ is the real gate.
"""

from __future__ import annotations

import os
import re
import struct
import sys

COVER_W, COVER_H = 1200, 630
COVER_MAX_BYTES = 200 * 1024
FIGURE_MAX_BYTES = 150 * 1024
SVG_MAX_BYTES = 100 * 1024
FIGURE_MAX_WIDTH = 1600
MAX_IMAGES_PER_POST = 5
ALT_MIN_CHARS = 25
ALT_MAX_CHARS = 125

# Body figures allowed per post format, excluding the cover (IMAGE_GUIDE.md §2).
# A and D are table-driven formats — extra figures dilute what the crawler reads.
FIGURE_BUDGET = {"A": 1, "B": 0, "C": 4, "D": 2, "E": 3, "F": 3, "G": 0}

# alt text that describes the medium instead of the claim
LABEL_ALT_RE = re.compile(
    r"^\s*(an?\s+)?(image|photo|picture|chart|graph|diagram|figure|screenshot|illustration|graphic)\b",
    re.IGNORECASE,
)

BODY_IMG_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
FILENAME_RE = re.compile(
    r"^(?P<slug>.+?)-(cover|fig\d+|chart\d+|shot\d+)\.(png|webp|svg|jpg|jpeg)$"
)


# ---------------------------------------------------------------- image size


def _png_size(data: bytes):
    if len(data) >= 24 and data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
        return struct.unpack(">II", data[16:24])
    return None


def _webp_size(data: bytes):
    if len(data) < 30 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return None
    fourcc = data[12:16]
    if fourcc == b"VP8X":
        w = int.from_bytes(data[24:27], "little") + 1
        h = int.from_bytes(data[27:30], "little") + 1
        return w, h
    if fourcc == b"VP8 ":
        w = int.from_bytes(data[26:28], "little") & 0x3FFF
        h = int.from_bytes(data[28:30], "little") & 0x3FFF
        return w, h
    if fourcc == b"VP8L":
        bits = int.from_bytes(data[21:25], "little")
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    return None


def image_size(path: str):
    """(width, height) or None when the format is unreadable (e.g. SVG)."""
    try:
        with open(path, "rb") as fh:
            head = fh.read(64)
    except OSError:
        return None
    return _png_size(head) or _webp_size(head)


# ------------------------------------------------------------- post parsing


def split_front_matter(text: str):
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[3:end], text[end + 4 :]


def parse_cover(front: str):
    """Return (path, alt) from the `image:` block. Either may be None."""
    path = alt = None
    in_block = False
    for line in front.splitlines():
        if re.match(r"^image:\s*$", line):
            in_block = True
            continue
        if re.match(r"^image:\s*\S", line):  # `image: /path.png` shorthand
            path = line.split(":", 1)[1].strip().strip("\"'")
            continue
        if in_block:
            if line and not line.startswith((" ", "\t")):
                in_block = False
                continue
            m = re.match(r"\s+(path|alt):\s*(.+)$", line)
            if m:
                value = m.group(2).strip().strip("\"'")
                if m.group(1) == "path":
                    path = value
                else:
                    alt = value
    return path, alt


def slug_of(post_path: str) -> str:
    base = os.path.basename(post_path)[:-3]
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)


def asset_path(repo_root: str, url_path: str) -> str:
    return os.path.join(repo_root, url_path.lstrip("/"))


# ------------------------------------------------------------------- checks


def check_post(post_path: str, repo_root: str):
    """Return a list of (severity, message). Severity is 'ERROR' or 'WARN'."""
    out = []

    def err(msg):
        out.append(("ERROR", msg))

    def warn(msg):
        out.append(("WARN", msg))

    try:
        with open(post_path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        return [("WARN", f"IMAGE CHECK SKIPPED: cannot read file ({exc})")]

    front, body = split_front_matter(text)
    slug = slug_of(post_path)
    cover_path, cover_alt = parse_cover(front)

    # --- C1: cover declared and present -----------------------------------
    if not cover_path:
        err("MISSING COVER: front matter has no image.path — og:image will be empty")
    else:
        expected = f"/assets/img/posts/{slug}-cover.png"
        if cover_path != expected:
            warn(f"COVER PATH MISMATCH: '{cover_path}' — convention is '{expected}'")
        abs_cover = asset_path(repo_root, cover_path)
        if not os.path.isfile(abs_cover):
            err(f"COVER FILE NOT FOUND: {cover_path} — og:image resolves to 404")
        else:
            # --- C3: cover dimensions and weight ---------------------------
            size = image_size(abs_cover)
            if size and size != (COVER_W, COVER_H):
                err(
                    f"COVER SIZE WRONG: {size[0]}x{size[1]} — must be "
                    f"{COVER_W}x{COVER_H} (OG 1.91:1, otherwise cropped)"
                )
            nbytes = os.path.getsize(abs_cover)
            if nbytes > COVER_MAX_BYTES:
                err(
                    f"COVER TOO HEAVY: {nbytes // 1024}KB (max "
                    f"{COVER_MAX_BYTES // 1024}KB) — run optimize_image.py --cover"
                )

    # --- C2: cover alt quality --------------------------------------------
    if cover_path and not cover_alt:
        err("COVER ALT MISSING: image.alt is required")
    elif cover_alt:
        if len(cover_alt) < ALT_MIN_CHARS:
            warn(
                f"COVER ALT TOO SHORT: {len(cover_alt)} chars — state the claim, "
                "not a label (IMAGE_GUIDE.md §4)"
            )
        elif len(cover_alt) > ALT_MAX_CHARS:
            warn(f"COVER ALT TOO LONG: {len(cover_alt)} chars (max {ALT_MAX_CHARS})")
        if LABEL_ALT_RE.match(cover_alt):
            warn(
                "COVER ALT IS A LABEL: starts with the medium "
                f"(\"{cover_alt[:40]}...\") — describe what it claims"
            )

    # --- C4/C5/C7/C8: body images -----------------------------------------
    body_no_code = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    body_images = [
        m for m in BODY_IMG_RE.finditer(body_no_code) if not m.group("path").startswith("http")
    ]

    for m in body_images:
        rel = m.group("path")
        alt = m.group("alt").strip()
        abs_img = asset_path(repo_root, rel)
        name = os.path.basename(rel)

        if not os.path.isfile(abs_img):
            err(f"BODY IMAGE NOT FOUND: {rel}")
            continue

        if not alt:
            err(f"BODY IMAGE ALT EMPTY: {name}")
        elif LABEL_ALT_RE.match(alt):
            warn(f"BODY IMAGE ALT IS A LABEL: {name} — \"{alt[:40]}\"")

        fm = FILENAME_RE.match(name)
        if not fm:
            warn(
                f"FILENAME OFF-CONVENTION: {name} — expected "
                f"{{slug}}-fig1.webp / -chart1.svg / -shot1.webp"
            )
        elif fm.group("slug") != slug:
            warn(f"FILENAME SLUG MISMATCH: {name} — post slug is '{slug}'")

        nbytes = os.path.getsize(abs_img)
        limit = SVG_MAX_BYTES if name.endswith(".svg") else FIGURE_MAX_BYTES
        if nbytes > limit:
            warn(f"BODY IMAGE TOO HEAVY: {name} is {nbytes // 1024}KB (max {limit // 1024}KB)")

        size = image_size(abs_img)
        if size and size[0] > FIGURE_MAX_WIDTH:
            warn(f"BODY IMAGE TOO WIDE: {name} is {size[0]}px (max {FIGURE_MAX_WIDTH}px)")

        if name.endswith((".png", ".jpg", ".jpeg")) and "-chart" not in name:
            warn(f"BODY IMAGE NOT WEBP: {name} — convert to .webp (IMAGE_GUIDE.md §3)")

    # --- C6: total count ---------------------------------------------------
    total = len(body_images) + (1 if cover_path else 0)
    if total > MAX_IMAGES_PER_POST:
        warn(
            f"TOO MANY IMAGES: {total} (max {MAX_IMAGES_PER_POST}) — "
            "each one costs LCP and dilutes text density"
        )

    # --- C9: per-format body-figure budget (IMAGE_GUIDE.md §2) -------------
    fmt_m = re.search(r"^format:\s*([A-G])\s*$", front, flags=re.MULTILINE)
    if fmt_m:
        fmt = fmt_m.group(1)
        budget = FIGURE_BUDGET.get(fmt)
        if budget is not None and len(body_images) > budget:
            warn(
                f"FIGURE BUDGET EXCEEDED: Format {fmt} allows {budget} body image(s), "
                f"found {len(body_images)} — the comparison tables carry this format, "
                "extra figures dilute text density (IMAGE_GUIDE.md §2)"
            )

    # --- C10: prompt pack with the claim/evidence table --------------------
    # Body figures without a recorded evidence mapping are how the 2026-07-25
    # best-llm figures shipped: spec-perfect, semantically wrong.
    if body_images:
        base = os.path.basename(post_path)[:-3]
        pack = os.path.join(repo_root, "_reviews", f"{base}.images.md")
        if not os.path.isfile(pack):
            warn(
                f"NO IMAGE PROMPT PACK: _reviews/{base}.images.md missing — "
                "body figures need a recorded claim/evidence mapping"
            )
        else:
            try:
                with open(pack, encoding="utf-8") as fh:
                    pack_text = fh.read()
            except OSError:
                pack_text = ""
            if "본문 근거" not in pack_text:
                warn(
                    f"PROMPT PACK HAS NO EVIDENCE TABLE: _reviews/{base}.images.md is "
                    "missing the 근거 대응표 (IMAGE_GUIDE.md §8) — every value-bearing "
                    "shape must map to a number in the post"
                )

    return out


# -------------------------------------------------------------------- modes


def repo_root_of(path: str) -> str:
    d = os.path.dirname(os.path.abspath(path))
    while d != "/":
        if os.path.isdir(os.path.join(d, "_posts")):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


def hook_mode(post_path: str) -> int:
    repo_root = repo_root_of(post_path)
    is_draft = "/_drafts/" in post_path
    for severity, msg in check_post(post_path, repo_root):
        # Drafts have no artwork yet — never block, just inform.
        if is_draft and severity == "ERROR":
            severity = "WARN"
        print(f"{severity}:{msg}")
    return 0


def report_mode() -> int:
    repo_root = os.getcwd()
    if not os.path.isdir(os.path.join(repo_root, "_posts")):
        print("_posts/ not found — run from the repo root", file=sys.stderr)
        return 1

    total_err = total_warn = 0
    for folder in ("_posts", "_drafts"):
        d = os.path.join(repo_root, folder)
        if not os.path.isdir(d):
            continue
        files = sorted(f for f in os.listdir(d) if f.endswith(".md"))
        if not files:
            continue
        print(f"\n=== {folder}/ ({len(files)} files) ===")
        for f in files:
            issues = check_post(os.path.join(d, f), repo_root)
            if "_drafts" in folder:
                issues = [("WARN", m) for _, m in issues]
            errs = [m for s, m in issues if s == "ERROR"]
            warns = [m for s, m in issues if s == "WARN"]
            total_err += len(errs)
            total_warn += len(warns)
            if not issues:
                print(f"  OK    {slug_of(f)}")
                continue
            print(f"  ISSUE {slug_of(f)}")
            for m in errs:
                print(f"          [ERROR] {m}")
            for m in warns:
                print(f"          [WARN]  {m}")

    print(f"\n--- {total_err} error(s), {total_warn} warning(s) ---")
    return 1 if total_err else 0


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "--report":
        return report_mode()
    return hook_mode(args[0])


if __name__ == "__main__":
    sys.exit(main())
