#!/usr/bin/env python3
"""Regenerate the auto-managed post URL blocks in GSC_INDEXING.md from _posts/.

Idempotent. Preserves the human-maintained 상태 (checkbox) and 메모 columns by
keying existing rows on their URL, so marking a URL as submitted survives
regeneration.

Usage: sync_indexing_list.py <repo_root>
"""

import datetime
import pathlib
import re
import sys

SITE_URL = "https://www.jsonhouse.com"

TABLE_START = "<!-- AUTO:POSTS-TABLE-START -->"
TABLE_END = "<!-- AUTO:POSTS-TABLE-END -->"
URLS_START = "<!-- AUTO:POSTS-URLS-START -->"
URLS_END = "<!-- AUTO:POSTS-URLS-END -->"
UPDATED_RE = re.compile(r"^- \*\*최종 갱신\*\*: .*$", re.MULTILINE)

FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")


def read_frontmatter_field(text, field):
    """Return a top-level front matter scalar, or '' if absent."""
    m = re.search(rf"^{field}:\s*(.+)$", text, re.MULTILINE)
    if not m:
        return ""
    return m.group(1).strip().strip('"').strip("'")


def collect_posts(repo_root):
    posts = []
    for path in sorted((repo_root / "_posts").glob("*.md")):
        m = FILENAME_RE.match(path.name)
        if not m:
            continue
        file_date, slug = m.group(1), m.group(2)
        text = path.read_text(encoding="utf-8", errors="replace")
        title = read_frontmatter_field(text, "title") or slug
        # front matter date wins over filename when present
        fm_date = read_frontmatter_field(text, "date")
        date = fm_date.split(" ")[0] if fm_date else file_date
        posts.append(
            {
                "slug": slug,
                "date": date,
                # full timestamp so same-day posts order by publish time
                "sort_key": fm_date or file_date,
                "title": title.replace("|", "\\|"),
                "url": f"{SITE_URL}/posts/{slug}/",
            }
        )
    # newest first — freshest posts get submitted to GSC first
    posts.sort(key=lambda p: (p["sort_key"], p["slug"]), reverse=True)
    return posts


def existing_state(block):
    """Map URL -> (상태, 메모) from the current table so edits survive."""
    state = {}
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        url_cell = cells[2]
        if not url_cell.startswith("http"):
            continue
        status = cells[1] if cells[1] else "[ ]"
        memo = cells[5] if len(cells) >= 6 else ""
        state[url_cell] = (status, memo)
    return state


def build_table(posts, state):
    rows = [
        "| # | 상태 | URL | 발행일 | 제목 | 메모 |",
        "|---|---|---|---|---|---|",
    ]
    for i, p in enumerate(posts, 1):
        status, memo = state.get(p["url"], ("[ ]", ""))
        rows.append(
            f"| {i} | {status} | {p['url']} | {p['date']} | {p['title']} | {memo} |"
        )
    return "\n".join(rows)


def replace_block(text, start, end, body):
    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end), re.DOTALL
    )
    if not pattern.search(text):
        return text, False
    return pattern.sub(f"{start}\n{body}\n{end}", text), True


def main():
    if len(sys.argv) < 2:
        return 0
    repo_root = pathlib.Path(sys.argv[1])
    target = repo_root / "GSC_INDEXING.md"
    if not target.is_file():
        return 0

    original = target.read_text(encoding="utf-8")
    posts = collect_posts(repo_root)
    if not posts:
        return 0

    table_block = ""
    m = re.search(
        re.escape(TABLE_START) + r"(.*?)" + re.escape(TABLE_END), original, re.DOTALL
    )
    if m:
        table_block = m.group(1)

    updated = original
    updated, ok_table = replace_block(
        updated, TABLE_START, TABLE_END, build_table(posts, existing_state(table_block))
    )
    updated, ok_urls = replace_block(
        updated,
        URLS_START,
        URLS_END,
        "```\n" + "\n".join(p["url"] for p in posts) + "\n```",
    )

    if not (ok_table or ok_urls):
        print(
            "[gsc-sync] GSC_INDEXING.md 에 AUTO 마커가 없습니다 — 자동 갱신 건너뜀",
            file=sys.stderr,
        )
        return 0

    today = datetime.date.today().isoformat()
    updated = UPDATED_RE.sub(f"- **최종 갱신**: {today} (자동)", updated, count=1)

    if updated == original:
        return 0

    target.write_text(updated, encoding="utf-8")
    print(f"[gsc-sync] GSC_INDEXING.md 갱신됨 — 포스트 {len(posts)}건", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
