#!/usr/bin/env python3
"""Build the internal link graph from _posts/ and report on its health.

Two modes:

  link_graph.py <repo_root>            regenerate LINK_GRAPH.md (the index document)
  link_graph.py --report [<repo_root>] print findings to stdout, exit 1 on ERROR

The graph is derived entirely from the posts, never hand-maintained. A written
index of internal links drifts the moment someone edits a link and forgets the
index; regenerating it removes that failure mode. The human-maintained column in
LINK_GRAPH.md is 메모 only, preserved by slug across regenerations.

Findings:
  ORPHAN     post has no inbound internal link — nothing points readers or crawlers to it
  DANGLING   link targets a slug that does not exist in _posts/
  SELFLINK   post links to itself
  NOINDEX<-  a live post links to a noindex page, sending readers to a withdrawn page
  DEADEND    post has no outbound internal links
  THIN       post has fewer than 2 outbound internal links (SEO_GUIDE rule A9)
"""

import datetime
import pathlib
import re
import sys
from collections import defaultdict

TABLE_START = "<!-- AUTO:GRAPH-TABLE-START -->"
TABLE_END = "<!-- AUTO:GRAPH-TABLE-END -->"
EDGES_START = "<!-- AUTO:GRAPH-EDGES-START -->"
EDGES_END = "<!-- AUTO:GRAPH-EDGES-END -->"
FINDINGS_START = "<!-- AUTO:GRAPH-FINDINGS-START -->"
FINDINGS_END = "<!-- AUTO:GRAPH-FINDINGS-END -->"

FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
# [anchor text](/posts/some-slug/) — trailing slash optional, anchors/queries tolerated
LINK_RE = re.compile(r"\[([^\]]*)\]\(/posts/([a-z0-9][a-z0-9-]*)/?(?:[#?][^)]*)?\)")
MIN_OUTBOUND = 2


def split_front_matter(text):
    """Return (front_matter, body). Body is '' when the file has no front matter."""
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1], parts[2]


def fm_field(front_matter, field):
    m = re.search(rf"^{field}:\s*(.+)$", front_matter, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def strip_code(body):
    """Drop fenced code blocks so example markdown inside them is not counted."""
    return re.sub(r"```.*?```", "", body, flags=re.S)


def load_posts(repo_root):
    posts = {}
    for path in sorted((repo_root / "_posts").glob("*.md")):
        m = FILENAME_RE.match(path.name)
        if not m:
            continue
        file_date, slug = m.group(1), m.group(2)
        text = path.read_text(encoding="utf-8", errors="replace")
        front, body = split_front_matter(text)
        fm_date = fm_field(front, "date")
        posts[slug] = {
            "slug": slug,
            "path": path,
            "date": (fm_date.split(" ")[0] if fm_date else file_date),
            "sort_key": fm_date or file_date,
            "title": fm_field(front, "title") or slug,
            "cluster": fm_field(front, "cluster") or "—",
            "noindex": fm_field(front, "noindex").lower() == "true",
            "body": strip_code(body),
        }
    return posts


def build_edges(posts):
    """Return list of (src_slug, dst_slug, anchor). Cover-image paths never match:
    they live under /assets/, not /posts/."""
    edges = []
    for slug, post in posts.items():
        seen = set()
        for anchor, dst in LINK_RE.findall(post["body"]):
            if (dst, anchor) in seen:
                continue
            seen.add((dst, anchor))
            edges.append((slug, dst, anchor.strip()))
    return edges


def analyse(posts, edges):
    inbound = defaultdict(list)
    outbound = defaultdict(list)
    findings = []

    for src, dst, anchor in edges:
        if dst == src:
            findings.append(("SELFLINK", src, f"links to itself ({anchor!r})"))
            continue
        if dst not in posts:
            findings.append(
                ("DANGLING", src, f"/posts/{dst}/ does not exist in _posts/ ({anchor!r})")
            )
            continue
        inbound[dst].append((src, anchor))
        outbound[src].append((dst, anchor))
        if posts[dst]["noindex"] and not posts[src]["noindex"]:
            findings.append(
                ("NOINDEX<-", src, f"links to noindex page /posts/{dst}/ ({anchor!r})")
            )

    for slug, post in posts.items():
        if post["noindex"]:
            continue  # a withdrawn page is expected to lose its inbound links
        if not inbound[slug]:
            findings.append(("ORPHAN", slug, "no inbound internal link"))
        if not outbound[slug]:
            findings.append(("DEADEND", slug, "no outbound internal links"))
        elif len(outbound[slug]) < MIN_OUTBOUND:
            findings.append(
                ("THIN", slug, f"{len(outbound[slug])} outbound link(s), rule A9 wants {MIN_OUTBOUND}")
            )
    return inbound, outbound, findings


# ERROR blocks publishing; WARN is advisory. Mirrors post-validation.sh severities.
SEVERITY = {
    "DANGLING": "ERROR",
    "SELFLINK": "WARN",
    "ORPHAN": "WARN",
    "NOINDEX<-": "WARN",
    "DEADEND": "WARN",
    "THIN": "WARN",
}


def existing_notes(text):
    """Map slug -> 메모 from the current table so human notes survive regeneration."""
    notes = {}
    block = text.split(TABLE_START, 1)
    if len(block) < 2:
        return notes
    block = block[1].split(TABLE_END, 1)[0]
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and cells[0].isdigit():
            notes[cells[1]] = cells[6]
    return notes


def render_table(posts, inbound, outbound, notes):
    rows = [
        "| # | 슬러그 | 클러스터 | 인 | 아웃 | 상태 | 메모 |",
        "|---|---|---|---|---|---|---|",
    ]
    ordered = sorted(posts.values(), key=lambda p: (p["sort_key"], p["slug"]), reverse=True)
    for i, post in enumerate(ordered, 1):
        slug = post["slug"]
        n_in, n_out = len(inbound[slug]), len(outbound[slug])
        if post["noindex"]:
            state = "noindex"
        elif n_in == 0:
            state = "**고아**"
        elif n_out == 0:
            state = "**막다른길**"
        else:
            state = "ok"
        rows.append(
            f"| {i} | {slug} | {post['cluster'].replace('CLUSTER_', '')} | "
            f"{n_in} | {n_out} | {state} | {notes.get(slug, '')} |"
        )
    return "\n".join(rows)


def render_edges(posts, inbound):
    """Inbound view: for each post, exactly where its backlinks are placed."""
    out = []
    ordered = sorted(posts.values(), key=lambda p: (p["sort_key"], p["slug"]), reverse=True)
    for post in ordered:
        slug = post["slug"]
        flag = " *(noindex)*" if post["noindex"] else ""
        out.append(f"\n### {slug}{flag}")
        out.append(f"\n{post['title']}\n")
        if not inbound[slug]:
            out.append("_인바운드 없음 — 이 글로 들어오는 내부 링크가 하나도 없습니다._")
            continue
        out.append("| 걸린 글 | 앵커 텍스트 |")
        out.append("|---|---|")
        for src, anchor in sorted(inbound[slug]):
            anchor = (anchor or "—").replace("|", "\\|")
            out.append(f"| {src} | {anchor} |")
    return "\n".join(out)


def render_findings(findings):
    if not findings:
        return "현재 지적 사항 없음. 모든 포스트가 인바운드·아웃바운드를 갖고 있습니다."
    order = {"ERROR": 0, "WARN": 1}
    findings = sorted(findings, key=lambda f: (order[SEVERITY[f[0]]], f[0], f[1]))
    rows = ["| 심각도 | 유형 | 슬러그 | 내용 |", "|---|---|---|---|"]
    for kind, slug, detail in findings:
        rows.append(f"| {SEVERITY[kind]} | {kind} | {slug} | {detail.replace('|', '\\|')} |")
    return "\n".join(rows)


def replace_block(text, start, end, payload):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    return pattern.sub(f"{start}\n{payload}\n{end}", text, count=1)


DOC_TEMPLATE = """# 내부 링크 그래프

포스트끼리 어떻게 엮여 있는지를 보여주는 색인. **이 문서는 자동 생성됩니다.**

- **최종 갱신**: {today} (자동)
- **소스**: `_posts/*.md` 본문의 `](/posts/<slug>/)` 링크
- **생성**: `python3 .claude/hooks/link_graph.py "$(git rev-parse --show-toplevel)"`
- **점검만**: `python3 .claude/hooks/link_graph.py --report`
- `AUTO:` 마커 사이는 직접 고쳐도 덮어써집니다 — 단 1번 표의 `메모` 칸은
  슬러그 기준으로 보존됩니다. 링크를 바꾸려면 문서가 아니라 **포스트 본문**을 고치십시오.

> 손으로 쓰는 링크 색인을 만들지 않는 이유: 링크를 고칠 때마다 두 곳을 고쳐야 하고,
> 언젠가 반드시 한 곳을 빠뜨립니다. 그래프는 포스트에서 파생되는 값이므로 파생시킵니다.

---

## 1. 포스트별 요약

`인` = 이 글로 들어오는 링크 수, `아웃` = 이 글에서 나가는 링크 수.
noindex 글은 인바운드를 잃는 것이 정상이라 고아로 세지 않습니다.

{table_start}
{table_end}

---

## 2. 지적 사항

{findings_start}
{findings_end}

유형 설명 — `DANGLING`: 없는 슬러그로 링크(ERROR, 발행 차단) · `ORPHAN`: 인바운드 0 ·
`DEADEND`: 아웃바운드 0 · `THIN`: 아웃바운드 2개 미만 · `NOINDEX<-`: 라이브 글이
색인 제외된 글을 링크 · `SELFLINK`: 자기 자신을 링크.

---

## 3. 백링크 위치 (인바운드 상세)

각 글마다 **어느 글의 어떤 문장에서** 링크가 걸렸는지. 슬러그를 바꾸거나 글을
내릴 때 어디를 고쳐야 하는지 여기서 확인합니다.

{edges_start}
{edges_end}
"""


def build_doc(today):
    return DOC_TEMPLATE.format(
        today=today,
        table_start=TABLE_START,
        table_end=TABLE_END,
        findings_start=FINDINGS_START,
        findings_end=FINDINGS_END,
        edges_start=EDGES_START,
        edges_end=EDGES_END,
    )


def main():
    args = [a for a in sys.argv[1:]]
    report_only = "--report" in args
    args = [a for a in args if a != "--report"]
    repo_root = pathlib.Path(args[0]) if args else pathlib.Path.cwd()

    posts = load_posts(repo_root)
    if not posts:
        print(f"[link-graph] _posts/ 에서 포스트를 찾지 못했습니다: {repo_root}", file=sys.stderr)
        return 1

    edges = build_edges(posts)
    inbound, outbound, findings = analyse(posts, edges)
    errors = [f for f in findings if SEVERITY[f[0]] == "ERROR"]

    if report_only:
        for kind, slug, detail in sorted(
            findings, key=lambda f: ({"ERROR": 0, "WARN": 1}[SEVERITY[f[0]]], f[0], f[1])
        ):
            print(f"[{SEVERITY[kind]:5s}] {kind:10s} {slug}: {detail}")
        print(
            f"\n{len(posts)} posts, {len(edges)} links — "
            f"{len(errors)} error(s), {len(findings) - len(errors)} warning(s)"
        )
        return 1 if errors else 0

    doc_path = repo_root / "LINK_GRAPH.md"
    today = datetime.date.today().isoformat()
    notes = existing_notes(doc_path.read_text(encoding="utf-8")) if doc_path.exists() else {}

    text = build_doc(today)
    text = replace_block(text, TABLE_START, TABLE_END, render_table(posts, inbound, outbound, notes))
    text = replace_block(text, FINDINGS_START, FINDINGS_END, render_findings(findings))
    text = replace_block(text, EDGES_START, EDGES_END, render_edges(posts, inbound))
    doc_path.write_text(text, encoding="utf-8")

    print(
        f"[link-graph] LINK_GRAPH.md 갱신됨 — 포스트 {len(posts)}건, 링크 {len(edges)}건, "
        f"에러 {len(errors)}건, 경고 {len(findings) - len(errors)}건"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
