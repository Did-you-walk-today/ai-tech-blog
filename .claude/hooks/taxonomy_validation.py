#!/usr/bin/env python3
"""Validate posts and hub tabs against _data/taxonomy.yml.

Usage:
  taxonomy_validation.py --report [<repo_root>]     print findings, exit 1 on ERROR
  taxonomy_validation.py <post_path> [<repo_root>]  check one post, exit 1 on ERROR

Clusters and categories used to live only as free text in front matter plus a
hardcoded string in each hub tab. Three kinds of drift got through: an undeclared
cluster (CLUSTER_AEO), two categories for one idea (ai-data vs ai-data-statistics),
and a category with no hub tab (industry-analysis). This makes taxonomy.yml the
only place those names may be introduced.

No third-party YAML dependency: the taxonomy file is a small fixed shape, so it is
parsed directly rather than pulling PyYAML into the hook path.
"""

import pathlib
import re
import sys

FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
INCLUDE_RE = re.compile(r'include\s+hub-post-list\.html\s+category="([^"]+)"')


def split_front_matter(text):
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    return (parts[1], parts[2]) if len(parts) >= 3 else ("", text)


def fm_field(front, field):
    m = re.search(rf"^{field}:\s*(.*)$", front, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def fm_list(front, field):
    raw = fm_field(front, field)
    if not raw.startswith("["):
        return [raw] if raw else []
    return [x.strip().strip('"').strip("'") for x in raw.strip("[]").split(",") if x.strip()]


def parse_taxonomy(path):
    """Parse the two top-level lists of _data/taxonomy.yml.

    Recognises `- id: X` to open a record and `key: value` to fill it, ignoring
    comments and blank lines. Bare `null` becomes None.
    """
    section, records = None, {"clusters": [], "categories": []}
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip() if not raw.strip().startswith("#") else ""
        if not line.strip():
            continue
        if re.match(r"^(clusters|categories):\s*$", line):
            section = line.split(":")[0]
            current = None
            continue
        if section is None:
            continue
        m = re.match(r"^\s*-\s*id:\s*(.+)$", line)
        if m:
            current = {"id": m.group(1).strip().strip('"').strip("'")}
            records[section].append(current)
            continue
        m = re.match(r"^\s+(\w+):\s*(.*)$", line)
        if m and current is not None:
            val = m.group(2).strip().strip('"').strip("'")
            current[m.group(1)] = None if val == "null" else val
    return records


def load_posts(repo_root):
    posts = {}
    for path in sorted((repo_root / "_posts").glob("*.md")):
        m = FILENAME_RE.match(path.name)
        if not m:
            continue
        front, _ = split_front_matter(path.read_text(encoding="utf-8", errors="replace"))
        posts[m.group(2)] = {
            "slug": m.group(2),
            "path": path,
            "cluster": fm_field(front, "cluster"),
            "categories": fm_list(front, "categories"),
            "pillar": fm_field(front, "pillar").lower() == "true",
            "noindex": fm_field(front, "noindex").lower() == "true",
        }
    return posts


def load_hubs(repo_root):
    """Map hub name (tab basename) -> {category, visible}."""
    hubs = {}
    for path in sorted((repo_root / "_tabs").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        front, body = split_front_matter(text)
        m = INCLUDE_RE.search(body)
        if not m:
            continue  # not a category hub (archives, categories, methodology)
        hubs[path.stem] = {
            "path": path,
            "category": m.group(1),
            "visible": fm_field(front, "published").lower() != "false",
        }
    return hubs


def validate(repo_root, only_slug=None):
    findings = []
    add = lambda sev, code, subj, msg: findings.append((sev, code, subj, msg))

    tax_path = repo_root / "_data" / "taxonomy.yml"
    if not tax_path.exists():
        add("ERROR", "NO-TAXONOMY", "_data/taxonomy.yml", "file missing")
        return findings

    tax = parse_taxonomy(tax_path)
    clusters = {c["id"]: c for c in tax["clusters"]}
    categories = {c["id"]: c for c in tax["categories"]}
    posts = load_posts(repo_root)
    hubs = load_hubs(repo_root)

    checked = {only_slug: posts[only_slug]} if only_slug and only_slug in posts else posts

    # --- posts conform to the declared taxonomy ---
    for slug, post in checked.items():
        if not post["cluster"]:
            add("ERROR", "NO-CLUSTER", slug, "front matter has no cluster")
        elif post["cluster"] not in clusters:
            add("ERROR", "UNKNOWN-CLUSTER", slug,
                f"{post['cluster']} is not declared in taxonomy.yml")
        elif clusters[post["cluster"]].get("status") == "deprecated":
            add("WARN", "DEPRECATED-CLUSTER", slug,
                f"{post['cluster']} is deprecated — do not plan new posts into it")

        if not post["categories"]:
            add("ERROR", "NO-CATEGORY", slug, "front matter has no categories")
        for cat in post["categories"]:
            if cat not in categories:
                add("ERROR", "UNKNOWN-CATEGORY", slug,
                    f"{cat} is not declared in taxonomy.yml")

    # --- pillar declarations agree in both directions ---
    if only_slug is None:
        by_cluster = {}
        for slug, post in posts.items():
            if post["pillar"]:
                by_cluster.setdefault(post["cluster"], []).append(slug)

        for cid, cluster in clusters.items():
            declared = cluster.get("pillar")
            marked = by_cluster.get(cid, [])
            if len(marked) > 1:
                add("ERROR", "MULTI-PILLAR", cid,
                    f"{len(marked)} posts claim pillar: true — {', '.join(sorted(marked))}")
            if declared:
                if declared not in posts:
                    add("ERROR", "MISSING-PILLAR", cid,
                        f"declared pillar {declared} is not a post in _posts/")
                elif not posts[declared]["pillar"]:
                    add("ERROR", "PILLAR-UNMARKED", cid,
                        f"taxonomy names {declared} as pillar but its front matter lacks pillar: true")
            else:
                if marked:
                    add("ERROR", "PILLAR-UNDECLARED", cid,
                        f"{marked[0]} claims pillar: true but taxonomy declares no pillar")
                elif cluster.get("status") != "deprecated":
                    add("WARN", "NO-PILLAR", cid, "active cluster has no pillar post yet")

    # --- every category with posts has a working hub, and vice versa ---
    if only_slug is None:
        live_counts = {}
        for post in posts.values():
            if post["noindex"]:
                continue
            for cat in post["categories"]:
                live_counts[cat] = live_counts.get(cat, 0) + 1

        hub_by_category = {}
        for name, hub in hubs.items():
            hub_by_category.setdefault(hub["category"], []).append(name)
            if hub["category"] not in categories:
                add("ERROR", "HUB-UNKNOWN-CATEGORY", f"_tabs/{name}.md",
                    f"renders category {hub['category']} which is not in taxonomy.yml")

        for cid, cat in categories.items():
            want_hub = cat.get("hub")
            names = hub_by_category.get(cid, [])
            n = live_counts.get(cid, 0)
            if not names:
                add("ERROR", "NO-HUB", cid,
                    f"taxonomy names hub '{want_hub}' but no tab renders this category")
                continue
            if want_hub and want_hub not in names:
                add("ERROR", "HUB-MISMATCH", cid,
                    f"taxonomy names hub '{want_hub}' but it is rendered by {', '.join(names)}")
            for name in names:
                if n > 0 and not hubs[name]["visible"]:
                    add("ERROR", "HUB-HIDDEN", f"_tabs/{name}.md",
                        f"published: false but category {cid} has {n} live post(s)")
                if n == 0 and hubs[name]["visible"]:
                    add("WARN", "HUB-EMPTY", f"_tabs/{name}.md",
                        f"visible but category {cid} has no live posts")
    return findings


def main():
    args = [a for a in sys.argv[1:]]
    report = "--report" in args
    args = [a for a in args if a != "--report"]

    if report:
        repo_root = pathlib.Path(args[0]) if args else pathlib.Path.cwd()
        only_slug = None
    else:
        if not args:
            print("usage: taxonomy_validation.py --report [<repo_root>] | <post_path> [<repo_root>]",
                  file=sys.stderr)
            return 2
        post_path = pathlib.Path(args[0])
        repo_root = pathlib.Path(args[1]) if len(args) > 1 else post_path.resolve().parents[1]
        m = FILENAME_RE.match(post_path.name)
        only_slug = m.group(2) if m else None
        if only_slug is None:
            return 0

    findings = validate(repo_root, only_slug)
    errors = [f for f in findings if f[0] == "ERROR"]
    for sev, code, subj, msg in sorted(findings, key=lambda f: (f[0] != "ERROR", f[1], f[2])):
        print(f"[{sev:5s}] {code:22s} {subj}: {msg}")
    if report:
        print(f"\n{len(errors)} error(s), {len(findings) - len(errors)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
