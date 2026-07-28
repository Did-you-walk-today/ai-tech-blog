#!/usr/bin/env python3
"""Submit changed URLs to IndexNow (Bing, Yandex, Seznam, Naver).

IndexNow is a push notification: it tells participating engines that a URL
changed so they can recrawl it, instead of waiting for a scheduled crawl.
Google does not participate — GSC submission stays manual (see GSC_INDEXING.md).

Ownership is proved by hosting a key file at the site root. That file must be
live BEFORE any submission, or the API answers 403.

Usage:
    # everything in the deployed sitemap
    python3 .claude/hooks/indexnow_submit.py --sitemap

    # a single post, straight after publishing
    python3 .claude/hooks/indexnow_submit.py \
        https://www.jsonhouse.com/posts/some-slug/

    # show what would be sent, contact nothing
    python3 .claude/hooks/indexnow_submit.py --sitemap --dry-run

Exit status is 0 only when every batch was accepted.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HOST = "www.jsonhouse.com"
SITE = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"

# IndexNow caps a submission at 10,000 URLs. Batches are also a courtesy to the
# API, so pause briefly between them rather than firing back to back.
BATCH_SIZE = 10_000
BATCH_PAUSE_SECONDS = 1.0
TIMEOUT_SECONDS = 30

# Documented IndexNow responses. Anything else is reported verbatim.
STATUS_MEANING = {
    200: "accepted",
    202: "accepted — key validation pending",
    400: "bad request — malformed payload",
    403: "forbidden — key file not found or does not match",
    422: "unprocessable — a URL does not belong to the host, or the key is wrong",
    429: "rate limited — too many requests",
}


def log(msg: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    print(f"[{stamp}] {msg}", flush=True)


def repo_root() -> Path:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
        return Path(out.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fall back to the layout this script ships in: <root>/.claude/hooks/
        return Path(__file__).resolve().parents[2]


def find_key(root: Path) -> tuple[str, str]:
    """Locate the root key file. Returns (key, keyLocation URL)."""
    candidates = [
        p for p in root.glob("*.txt")
        if re.fullmatch(r"[A-Za-z0-9-]{8,128}", p.stem)
        and p.read_text(encoding="utf-8", errors="ignore").strip() == p.stem
    ]
    if not candidates:
        raise SystemExit(
            "ERROR: no IndexNow key file at the repo root.\n"
            "       Expected <key>.txt whose contents are exactly <key>\n"
            "       (8-128 chars of [A-Za-z0-9-])."
        )
    if len(candidates) > 1:
        names = ", ".join(sorted(p.name for p in candidates))
        raise SystemExit(
            f"ERROR: multiple IndexNow key files found ({names}).\n"
            "       Keep exactly one so submissions are unambiguous."
        )
    key = candidates[0].stem
    return key, f"{SITE}/{candidates[0].name}"


def fetch_sitemap_urls() -> list[str]:
    url = f"{SITE}/sitemap.xml"
    log(f"fetching {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "jsonhouse-indexnow/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            body = resp.read().decode("utf-8", "ignore")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SystemExit(f"ERROR: could not fetch sitemap: {exc}") from exc
    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", body)
    if not urls:
        raise SystemExit("ERROR: sitemap contained no <loc> entries.")
    return urls


def verify_key_is_live(key_location: str, key: str) -> None:
    """The API returns 403 if the key file is not reachable. Check first so the
    failure is reported here, with a clear cause, instead of as an opaque 403."""
    log(f"verifying key file at {key_location}")
    req = urllib.request.Request(key_location, headers={"User-Agent": "jsonhouse-indexnow/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            served = resp.read().decode("utf-8", "ignore").strip()
    except urllib.error.HTTPError as exc:
        raise SystemExit(
            f"ERROR: key file is not live (HTTP {exc.code}).\n"
            "       Deploy it to the site root before submitting."
        ) from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SystemExit(f"ERROR: could not reach the key file: {exc}") from exc

    if served != key:
        raise SystemExit(
            "ERROR: key file is live but its contents do not match its filename.\n"
            f"       served={served!r} expected={key!r}"
        )
    log("key file OK")


def submit(batch: list[str], key: str, key_location: str) -> tuple[int, str]:
    payload = json.dumps({
        "host": HOST,
        "key": key,
        "keyLocation": key_location,
        "urlList": batch,
    }).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "jsonhouse-indexnow/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return resp.status, resp.read().decode("utf-8", "ignore").strip()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "ignore").strip()
    except (urllib.error.URLError, TimeoutError) as exc:
        return 0, str(exc)


def main() -> int:
    ap = argparse.ArgumentParser(description="Submit URLs to IndexNow.")
    ap.add_argument("urls", nargs="*", help=f"absolute {SITE} URLs")
    ap.add_argument("--sitemap", action="store_true",
                    help="submit every URL in the deployed sitemap")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the payload and exit without contacting the API")
    args = ap.parse_args()

    if not args.urls and not args.sitemap:
        ap.error("give at least one URL, or --sitemap")

    urls = list(args.urls)
    if args.sitemap:
        urls.extend(fetch_sitemap_urls())

    # De-duplicate, preserving order, then reject anything off-host: IndexNow
    # answers 422 for the whole batch if a single URL belongs elsewhere.
    seen: set[str] = set()
    accepted, rejected = [], []
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        (accepted if u.startswith(f"{SITE}/") or u == SITE else rejected).append(u)

    if rejected:
        log(f"WARNING: skipping {len(rejected)} URL(s) not under {SITE}")
        for u in rejected[:5]:
            log(f"  skipped: {u}")
    if not accepted:
        log("ERROR: nothing to submit after filtering.")
        return 1

    key, key_location = find_key(repo_root())
    log(f"host={HOST} key={key[:8]}… urls={len(accepted)}")

    if args.dry_run:
        log("dry run — not contacting the API")
        for u in accepted:
            print(f"  {u}")
        return 0

    verify_key_is_live(key_location, key)

    batches = [accepted[i:i + BATCH_SIZE] for i in range(0, len(accepted), BATCH_SIZE)]
    ok = 0
    for n, batch in enumerate(batches, 1):
        if n > 1:
            time.sleep(BATCH_PAUSE_SECONDS)
        status, body = submit(batch, key, key_location)
        meaning = STATUS_MEANING.get(status, "unexpected response")
        detail = f" — {body}" if body else ""
        if status in (200, 202):
            ok += 1
            log(f"batch {n}/{len(batches)} ({len(batch)} urls): HTTP {status} {meaning}{detail}")
        else:
            log(f"batch {n}/{len(batches)} ({len(batch)} urls): FAILED HTTP {status} {meaning}{detail}")

    failed = len(batches) - ok
    log(f"summary: {ok} batch(es) accepted, {failed} failed, {len(accepted)} url(s) submitted")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
