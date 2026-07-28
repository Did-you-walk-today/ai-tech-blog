#!/usr/bin/env python3
"""AiTechBlog — normalize generated images to spec (IMAGE_GUIDE.md §4, §12).

gpt-image cannot emit 1200x630 directly (630 is not a multiple of 16), so
covers are generated at 2048x1152 and cropped down here.

    python3 optimize_image.py RAW.png --cover -o OUT.jpg   # -> 1200x630 JPEG, <=200KB
    python3 optimize_image.py IN.png --figure              # -> .webp, <=1600px, <=150KB

--cover center-crops to 1.91:1 before resizing, so keep the subject centered
and the top/bottom 8% free of critical detail.

Cover output defaults to JPEG: cover art carries texture, lighting and depth,
which PNG cannot fit into 200KB without visible banding. Pass an explicit
`-o ...png` only for flat-vector legacy covers. Requires Pillow.
"""

from __future__ import annotations

import argparse
import os
import sys

COVER_W, COVER_H = 1200, 630
COVER_MAX_BYTES = 200 * 1024
FIGURE_MAX_WIDTH = 1600
FIGURE_MAX_BYTES = 150 * 1024


def center_crop_to_ratio(img, ratio: float):
    w, h = img.size
    if w / h > ratio:  # too wide -> trim sides
        new_w = round(h * ratio)
        left = (w - new_w) // 2
        return img.crop((left, 0, left + new_w, h))
    new_h = round(w / ratio)
    top = (h - new_h) // 2
    return img.crop((0, top, w, top + new_h))


def do_cover(img, out_path: str) -> None:
    from PIL import Image

    img = img.convert("RGB")
    img = center_crop_to_ratio(img, COVER_W / COVER_H)
    img = img.resize((COVER_W, COVER_H), Image.LANCZOS)

    if out_path.lower().endswith((".jpg", ".jpeg")):
        for quality in (88, 84, 80, 74, 68):
            img.save(out_path, "JPEG", quality=quality, optimize=True, progressive=True)
            if os.path.getsize(out_path) <= COVER_MAX_BYTES:
                return
        print(
            f"  warning: {os.path.getsize(out_path) // 1024}KB at quality 68 — "
            "the source is unusually busy for cover art (IMAGE_GUIDE.md §6 asks for "
            "one subject and large unbroken background)",
            file=sys.stderr,
        )
        return

    # Legacy flat-vector covers only. Quantizing survives 3-4 colour line art
    # with no visible loss; it bands badly on anything with texture or gradient.
    img.save(out_path, "PNG", optimize=True)
    if os.path.getsize(out_path) <= COVER_MAX_BYTES:
        return
    for colors in (256, 128, 64, 32):
        img.quantize(colors=colors, method=Image.MEDIANCUT).save(
            out_path, "PNG", optimize=True
        )
        if os.path.getsize(out_path) <= COVER_MAX_BYTES:
            return
    print(
        f"  warning: still {os.path.getsize(out_path) // 1024}KB after quantizing — "
        "photographic cover art belongs in JPEG; pass -o {slug}-cover.jpg",
        file=sys.stderr,
    )


def do_figure(img, out_path: str) -> None:
    from PIL import Image

    if img.width > FIGURE_MAX_WIDTH:
        h = round(img.height * FIGURE_MAX_WIDTH / img.width)
        img = img.resize((FIGURE_MAX_WIDTH, h), Image.LANCZOS)

    for quality in (90, 85, 80, 72, 65):
        img.save(out_path, "WEBP", quality=quality, method=6)
        if os.path.getsize(out_path) <= FIGURE_MAX_BYTES:
            return
    print(
        f"  warning: {os.path.getsize(out_path) // 1024}KB at quality 65 — "
        "consider simplifying the diagram",
        file=sys.stderr,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--cover", action="store_true", help="1200x630 PNG, <=200KB")
    mode.add_argument("--figure", action="store_true", help="WebP, <=1600px, <=150KB")
    ap.add_argument("-o", "--output", help="defaults to in-place (cover) / .webp (figure)")
    args = ap.parse_args()

    try:
        from PIL import Image
    except ImportError:
        print("Pillow is required: pip install Pillow", file=sys.stderr)
        return 1

    if not os.path.isfile(args.input):
        print(f"not found: {args.input}", file=sys.stderr)
        return 1

    stem, _ = os.path.splitext(args.input)
    out_path = args.output or (args.input if args.cover else stem + ".webp")

    before = os.path.getsize(args.input)
    with Image.open(args.input) as img:
        src = f"{img.width}x{img.height}"
        if args.cover:
            do_cover(img, out_path)
        else:
            do_figure(img, out_path)

    after = os.path.getsize(out_path)
    print(f"{args.input} ({src}, {before // 1024}KB) -> {out_path} ({after // 1024}KB)")

    if not args.cover and out_path != args.input and os.path.exists(args.input):
        print(f"  note: original kept at {args.input} — delete it once you've checked the WebP")
    return 0


if __name__ == "__main__":
    sys.exit(main())
