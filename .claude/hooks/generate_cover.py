#!/usr/bin/env python3
"""AiTechBlog — generate a cover with the Antigravity CLI (IMAGE_GUIDE.md §10).

    python .claude/hooks/generate_cover.py <slug>              # generate raw only
    python .claude/hooks/generate_cover.py <slug> --normalize  # + 1200x630 JPEG

Reads the prompt from the "커버 이미지 프롬프트" section of
_reviews/YYYY-MM-DD-<slug>.ko.md (the single copy of the prompt), runs
`agy -p` headless with the image-generator subagent, and copies the image it
saved under ~/.gemini/antigravity-cli/brain/<conversation_id>/ to
assets/img/posts/<slug>-cover-raw.<ext>.

Needs `agy` installed and logged in once interactively. Grants no extra tool
permissions: the image tool saves into the brain folder on its own, and this
script does the copy. The color-count gate rejects code-drawn output (P1).
Visual review (P6, watermark, crop) is still a human/Claude step.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

MODEL = "gemini-4-hydrogen-medium"
MIN_COLORS = 5000  # raw-image gate, IMAGE_GUIDE.md §10
TIMEOUT_S = 600
AGY = shutil.which("agy") or os.path.join(os.environ.get("LOCALAPPDATA", ""), "agy", "bin", "agy.exe")
BRAIN = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity-cli", "brain")
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")

WRAPPER = (
    "Use your built-in image generation tool (the image-generator, an image "
    "generation model). Do NOT use Python, PIL, SVG, HTML canvas or any code to "
    "draw it, and do not write any files yourself. Generate exactly one image, "
    "16:9 landscape, from the prompt below, then reply with the absolute path "
    "of the saved image.\n\n"
)


def repo_root() -> str:
    return subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()


def read_prompt(root: str, slug: str) -> str:
    hits = glob.glob(os.path.join(root, "_reviews", f"*-{slug}.ko.md"))
    if len(hits) != 1:
        sys.exit(f"error: expected one _reviews/*-{slug}.ko.md, found {len(hits)}")
    text = open(hits[0], encoding="utf-8").read()
    m = re.search(r"^##[^\n]*커버 이미지 프롬프트[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        sys.exit("error: no '커버 이미지 프롬프트' section in " + hits[0])
    block = re.search(r"```[^\n]*\n(.*?)```", m.group(1), re.S)
    if not block:
        sys.exit("error: no fenced prompt block in the cover section")
    return block.group(1).strip()


def kill_tree(pid: int) -> None:
    if os.name == "nt":
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True)
    else:
        try:
            os.killpg(pid, 9)
        except OSError:
            pass


def run_agy(prompt: str) -> dict:
    # agy prints its JSON result and then may not exit, so poll the output file.
    work = tempfile.mkdtemp(prefix="agy-cover-")
    out_path = os.path.join(work, "out.json")
    with open(out_path, "w", encoding="utf-8") as out, open(os.path.join(work, "err.txt"), "w", encoding="utf-8") as err:
        proc = subprocess.Popen(
            [AGY, "-p", WRAPPER + prompt, "--model", MODEL, "--output-format", "json"],
            cwd=work, stdout=out, stderr=err, stdin=subprocess.DEVNULL,
            start_new_session=(os.name != "nt"),
        )
        deadline = time.time() + TIMEOUT_S
        result = None
        while time.time() < deadline:
            time.sleep(3)
            try:
                result = json.loads(open(out_path, encoding="utf-8").read())
                break
            except (ValueError, OSError):
                if proc.poll() is not None:
                    time.sleep(1)
                    try:
                        result = json.loads(open(out_path, encoding="utf-8").read())
                    except ValueError:
                        pass
                    break
        kill_tree(proc.pid)
    if result is None:
        err = open(os.path.join(work, "err.txt"), encoding="utf-8", errors="replace").read()[-2000:]
        sys.exit(f"error: agy returned no JSON within {TIMEOUT_S}s (work dir {work})\n{err}")
    if result.get("status") != "SUCCESS":
        sys.exit(f"error: agy status {result.get('status')}: {result.get('error') or result.get('response')}")
    return result


def find_image(conv_id: str) -> str:
    folder = os.path.join(BRAIN, conv_id)
    imgs = [p for p in glob.glob(os.path.join(folder, "*")) if p.lower().endswith(IMG_EXT)]
    if not imgs:
        sys.exit(f"error: no image in {folder} — the agent may have answered without generating")
    return max(imgs, key=os.path.getmtime)


def color_count(path: str) -> tuple[tuple[int, int], int]:
    from PIL import Image
    im = Image.open(path).convert("RGB")
    return im.size, len(im.getcolors(maxcolors=99999999) or [])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--normalize", action="store_true", help="also run optimize_image.py --cover")
    args = ap.parse_args()

    if not os.path.exists(AGY):
        sys.exit("error: agy not found — install the Antigravity CLI and log in once")
    root = repo_root()
    prompt = read_prompt(root, args.slug)
    print(f"generating with {MODEL} ...", flush=True)
    result = run_agy(prompt)
    src = find_image(result["conversation_id"])
    size, n = color_count(src)
    print(f"source {src}\n  {size[0]}x{size[1]}, {n} colors")
    if n <= MIN_COLORS:
        sys.exit(f"error: {n} colors <= {MIN_COLORS} — looks code-rendered, not an image-model output (P1). Discarded.")

    ext = os.path.splitext(src)[1].lower()
    raw = os.path.join(root, "assets", "img", "posts", f"{args.slug}-cover-raw{ext}")
    shutil.copy2(src, raw)
    print(f"raw  -> {os.path.relpath(raw, root)}")
    print(f"conversation_id {result['conversation_id']}")

    if args.normalize:
        out = os.path.join(root, "assets", "img", "posts", f"{args.slug}-cover.jpg")
        subprocess.check_call([sys.executable, os.path.join(root, ".claude", "hooks", "optimize_image.py"), raw, "--cover", "-o", out])
        print(f"cover-> {os.path.relpath(out, root)}  (review it visually before publishing)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
