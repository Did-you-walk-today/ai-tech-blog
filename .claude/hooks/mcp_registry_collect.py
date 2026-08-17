#!/usr/bin/env python3
"""Weekly snapshot of the official MCP registry, joined with GitHub popularity.

Why this collector exists
-------------------------
The registry API only ever answers "what exists right now". It has no history
endpoint, and an entry that is deleted stops being served entirely. Three things
are therefore unrecoverable the moment a week passes without a snapshot:

  1. entries that were removed (not deprecated — removed)
  2. the star count each repository held on a given date
  3. the composition of the registry at that date (who owned how much of it)

`publishedAt` makes *new registrations* backfillable, so growth-by-month is not
the reason to run this. Disappearance and popularity-at-a-date are.

Outputs (two, deliberately different in lifetime)
------------------------------------------------
  _data/mcp_registry_history/YYYY-MM-DD.json         aggregate + rankings (committed)
  _data/mcp_registry_history/roster/YYYY-MM-DD.tsv.gz  full roster (committed)

The roster is what makes next week's delta computable: it carries one row per
server with the star count attached, so week N+1 can diff against week N without
re-deriving anything. The 21MB raw sweep is NOT committed — it is written to
raw/ (gitignored) for local retention until the R2 lake exists.

Usage:
  python3 .claude/hooks/mcp_registry_collect.py [--repo-root PATH] [--date YYYY-MM-DD]
  python3 .claude/hooks/mcp_registry_collect.py --no-github   # registry only, fast
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import gzip
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REGISTRY_BASE = "https://registry.modelcontextprotocol.io/v0/servers"
UA = "jsonhouse-observer/1.0 (+https://www.jsonhouse.com/about-crawler)"
PAGE_LIMIT = 100
MAX_PAGES = 600
GRAPHQL_BATCH = 100
RANKING_SIZE = 100


def log(msg: str) -> None:
    print(f"[{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M:%S}Z] {msg}", file=sys.stderr)


# --------------------------------------------------------------------------
# 1. Registry sweep
# --------------------------------------------------------------------------


def http_json(url: str, tries: int = 3, timeout: int = 25):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read())
        except Exception as e:  # noqa: BLE001 — retried, then surfaced
            last = e
            if attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url} ({last})")


def sweep_registry() -> list[dict]:
    servers: list[dict] = []
    cursor = None
    pages = 0
    while True:
        params = {"version": "latest", "limit": str(PAGE_LIMIT)}
        if cursor:
            params["cursor"] = cursor
        data = http_json(f"{REGISTRY_BASE}?{urllib.parse.urlencode(params)}")
        batch = data.get("servers", [])
        servers.extend(batch)
        pages += 1
        if pages % 25 == 0:
            log(f"  registry page {pages}: {len(servers)} entries")
        cursor = data.get("metadata", {}).get("nextCursor")
        if not cursor or not batch:
            break
        if pages >= MAX_PAGES:
            raise RuntimeError(f"pagination exceeded {MAX_PAGES} pages — API contract changed?")
        time.sleep(0.15)
    log(f"registry sweep complete: {len(servers)} entries over {pages} pages")
    return servers


# --------------------------------------------------------------------------
# 2. GitHub star join
# --------------------------------------------------------------------------


def parse_repo(url: str | None) -> tuple[str, str] | None:
    """Extract (owner, name) from a github.com URL, or None if not parseable."""
    if not url:
        return None
    u = url.strip().rstrip("/")
    for prefix in ("https://github.com/", "http://github.com/", "git@github.com:"):
        if u.lower().startswith(prefix.lower()):
            rest = u[len(prefix):]
            break
    else:
        return None
    if rest.endswith(".git"):
        rest = rest[:-4]
    parts = [p for p in rest.split("/") if p]
    if len(parts) < 2:
        return None
    return parts[0], parts[1]


def namespace_owner(name: str) -> str | None:
    """The account a `io.github.*` / `io.gitlab.*` namespace asserts ownership by.

    Returns None for namespaces that encode a domain instead (com.acme/…), where
    this check cannot say anything either way.
    """
    ns = name.split("/")[0]
    for prefix in ("io.github.", "io.gitlab."):
        if ns.startswith(prefix):
            return ns[len(prefix):].lower()
    return None


def ownership_of(name: str, repo: str) -> str:
    """Whether the entry's namespace matches the repo it points at.

    The registry does not verify that `repository.url` belongs to the publisher,
    so an entry can claim any repository's stars. The top of the 2026-08-17 star
    ranking contained an entry pointing at a 78k-star repo owned by an unrelated
    account. Ranking on unverified stars would let anyone buy a rank with a URL.

    Mismatch is not the same as fraud — a project moved from a personal account
    to an org shows up here too — so entries are labelled, never dropped.
    """
    if not repo:
        return "no_repo"
    owner = namespace_owner(name)
    if owner is None:
        return "unverifiable"
    return "verified" if owner == repo.split("/")[0].lower() else "mismatch"


def fetch_stars(repos: list[tuple[str, str]]) -> dict[tuple[str, str], dict]:
    """Batch-resolve star counts via the GitHub GraphQL API (gh CLI auth).

    A missing/renamed/private repo yields a GraphQL error for that alias only;
    the rest of the batch still returns, so absence is recorded as absence
    rather than failing the run.
    """
    out: dict[tuple[str, str], dict] = {}
    total_batches = (len(repos) + GRAPHQL_BATCH - 1) // GRAPHQL_BATCH
    for i in range(0, len(repos), GRAPHQL_BATCH):
        chunk = repos[i:i + GRAPHQL_BATCH]
        parts = []
        for j, (owner, name) in enumerate(chunk):
            o = owner.replace('"', '\\"')
            n = name.replace('"', '\\"')
            parts.append(
                f'r{j}: repository(owner:"{o}", name:"{n}")'
                "{ stargazerCount forkCount pushedAt isArchived isFork }"
            )
        query = "{ " + " ".join(parts) + " }"
        try:
            proc = subprocess.run(
                ["gh", "api", "graphql", "-f", f"query={query}"],
                capture_output=True, text=True, timeout=120,
            )
            payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
        except Exception as e:  # noqa: BLE001
            log(f"  WARN batch {i // GRAPHQL_BATCH + 1} failed: {e}")
            continue
        data = (payload or {}).get("data") or {}
        for j, key in enumerate(chunk):
            node = data.get(f"r{j}")
            if node:
                out[key] = node
        done = i // GRAPHQL_BATCH + 1
        if done % 20 == 0 or done == total_batches:
            log(f"  github batch {done}/{total_batches}: {len(out)} repos resolved")
        time.sleep(0.1)
    return out


# --------------------------------------------------------------------------
# 3. Snapshot assembly
# --------------------------------------------------------------------------


def build_rows(servers: list[dict], stars: dict) -> list[dict]:
    rows = []
    for e in servers:
        sv = e.get("server", {})
        meta = (e.get("_meta") or {}).get("io.modelcontextprotocol.registry/official", {})
        repo_url = (sv.get("repository") or {}).get("url")
        rk = parse_repo(repo_url)
        gh = stars.get(rk) if rk else None
        pkgs = sv.get("packages") or []
        name = sv.get("name", "")
        repo = f"{rk[0]}/{rk[1]}" if rk else ""
        rows.append({
            "name": name,
            "ownership": ownership_of(name, repo),
            "version": sv.get("version", ""),
            "status": meta.get("status", ""),
            "published_at": (meta.get("publishedAt") or "")[:19],
            "updated_at": (meta.get("updatedAt") or "")[:19],
            "status_changed_at": (meta.get("statusChangedAt") or "")[:19],
            "repo": repo,
            "stars": gh.get("stargazerCount") if gh else None,
            "forks": gh.get("forkCount") if gh else None,
            "pushed_at": (gh.get("pushedAt") or "")[:19] if gh else "",
            "archived": bool(gh.get("isArchived")) if gh else None,
            "packages": ",".join(
                f"{p.get('registryType')}:{p.get('identifier')}" for p in pkgs
            ),
            "remotes": len(sv.get("remotes") or []),
        })
    return rows


def load_prev_roster(roster_dir: str, today: str) -> tuple[str | None, dict[str, dict]]:
    """Newest roster strictly older than `today`, as {name: row}."""
    if not os.path.isdir(roster_dir):
        return None, {}
    files = sorted(
        f for f in os.listdir(roster_dir)
        if f.endswith(".tsv.gz") and f[:10] < today
    )
    if not files:
        return None, {}
    path = os.path.join(roster_dir, files[-1])
    prev: dict[str, dict] = {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            vals = line.rstrip("\n").split("\t")
            row = dict(zip(header, vals))
            prev[row.get("name", "")] = row
    return files[-1][:10], prev


def to_int(v) -> int | None:
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def build_snapshot(rows: list[dict], prev_date: str | None, prev: dict, today: str,
                   github_enabled: bool) -> dict:
    by_status = collections.Counter(r["status"] for r in rows)
    ns = collections.Counter(r["name"].split("/")[0] for r in rows)
    pkg_reg = collections.Counter()
    for r in rows:
        for tok in filter(None, r["packages"].split(",")):
            pkg_reg[tok.split(":", 1)[0]] += 1
    by_month = collections.Counter(r["published_at"][:7] for r in rows if r["published_at"])

    own = collections.Counter(r["ownership"] for r in rows)

    total = len(rows)
    top_ns = ns.most_common(20)
    concentration = {
        "distinct_namespaces": len(ns),
        "top1_share_pct": round(100 * top_ns[0][1] / total, 2) if top_ns else 0,
        "top10_share_pct": round(100 * sum(c for _, c in ns.most_common(10)) / total, 2),
        "top_namespaces": [{"namespace": n, "servers": c} for n, c in top_ns],
    }

    # Churn against the previous roster — the part that cannot be backfilled.
    cur_names = {r["name"] for r in rows}
    churn = None
    if prev:
        prev_names = set(prev)
        disappeared = sorted(prev_names - cur_names)
        appeared = sorted(cur_names - prev_names)
        newly_deprecated = sorted(
            r["name"] for r in rows
            if r["status"] == "deprecated"
            and prev.get(r["name"], {}).get("status") not in (None, "deprecated")
        )
        churn = {
            "compared_to": prev_date,
            "appeared": len(appeared),
            "disappeared": len(disappeared),
            "newly_deprecated": len(newly_deprecated),
            "disappeared_names": disappeared[:200],
            "newly_deprecated_names": newly_deprecated[:200],
        }

    snapshot = {
        "schema_version": "1.0",
        "snapshot_date": today,
        "collected_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": {
            "registry": "https://registry.modelcontextprotocol.io/v0/servers?version=latest",
            "github": "GitHub GraphQL API (stargazerCount)" if github_enabled else None,
        },
        "totals": {
            "servers_latest": total,
            "active": by_status.get("active", 0),
            "deprecated": by_status.get("deprecated", 0),
            "with_repository": sum(1 for r in rows if r["repo"]),
            "with_packages": sum(1 for r in rows if r["packages"]),
            "with_remotes": sum(1 for r in rows if r["remotes"]),
        },
        "ownership": {
            "verified": own.get("verified", 0),
            "mismatch": own.get("mismatch", 0),
            "unverifiable": own.get("unverifiable", 0),
            "no_repo": own.get("no_repo", 0),
            "note": (
                "The registry does not verify that an entry's repository.url belongs "
                "to the publisher. 'mismatch' means the io.github.* namespace and the "
                "repository owner differ — which covers both misattribution and "
                "legitimate transfers to an org. 'unverifiable' means the namespace "
                "is a domain, so this check cannot rule either way."
            ),
        },
        "package_registries": dict(pkg_reg.most_common()),
        "registrations_by_month": dict(sorted(by_month.items())),
        "namespace_concentration": concentration,
        "churn": churn,
    }

    if github_enabled:
        starred = [r for r in rows if r["stars"] is not None]
        snapshot["totals"]["repos_resolved"] = len(starred)
        snapshot["totals"]["archived_repos"] = sum(1 for r in starred if r["archived"])
        # Entries that name a repository GitHub would not return: deleted, renamed,
        # or turned private since registration. A dead link in the registry.
        snapshot["totals"]["repo_unreachable"] = sum(
            1 for r in rows if r["repo"] and r["stars"] is None
        )

        # Ranking 1 — absolute popularity. One row per repo: a repo that
        # registered 40 server entries must not occupy 40 ranking slots.
        best_by_repo: dict[str, dict] = {}
        for r in starred:
            cur = best_by_repo.get(r["repo"])
            if cur is None or (r["stars"] or 0) > (cur["stars"] or 0):
                best_by_repo[r["repo"]] = r
        ranked = sorted(best_by_repo.values(), key=lambda r: -(r["stars"] or 0))
        snapshot["ranking_by_stars"] = [
            {
                "rank": i + 1, "name": r["name"], "repo": r["repo"],
                "stars": r["stars"], "forks": r["forks"], "pushed_at": r["pushed_at"],
                "ownership": r["ownership"],
            }
            for i, r in enumerate(ranked[:RANKING_SIZE])
        ]
        # How much of the published ranking rests on stars we cannot attribute.
        snapshot["ranking_ownership_summary"] = dict(
            collections.Counter(e["ownership"] for e in snapshot["ranking_by_stars"])
        )

        # Ranking 2 — weekly star delta. Requires a previous roster; this is the
        # ranking that is genuinely ours, and it stays absent until week two
        # rather than being faked from a single observation.
        if prev:
            movers = []
            for r in starred:
                p = prev.get(r["name"])
                if not p:
                    continue
                ps = to_int(p.get("stars"))
                if ps is None:
                    continue
                movers.append((r["stars"] - ps, r))
            seen_repo: dict[str, tuple[int, dict]] = {}
            for delta, r in movers:
                cur = seen_repo.get(r["repo"])
                if cur is None or delta > cur[0]:
                    seen_repo[r["repo"]] = (delta, r)
            top = sorted(seen_repo.values(), key=lambda t: -t[0])[:RANKING_SIZE]
            snapshot["ranking_by_star_delta"] = [
                {
                    "rank": i + 1, "name": r["name"], "repo": r["repo"],
                    "stars": r["stars"], "star_delta": d,
                    "ownership": r["ownership"], "pushed_at": r["pushed_at"],
                    "since": prev_date,
                }
                for i, (d, r) in enumerate(top)
            ]
        else:
            snapshot["ranking_by_star_delta"] = None

    # Ranking 3 — newest registrations, always available.
    fresh = sorted(rows, key=lambda r: r["published_at"], reverse=True)[:RANKING_SIZE]
    snapshot["newest_registrations"] = [
        {
            "rank": i + 1, "name": r["name"], "repo": r["repo"],
            "stars": r["stars"], "published_at": r["published_at"],
        }
        for i, r in enumerate(fresh)
    ]
    return snapshot


ROSTER_COLS = [
    "name", "version", "status", "published_at", "updated_at", "status_changed_at",
    "repo", "ownership", "stars", "forks", "pushed_at", "archived", "remotes", "packages",
]


def write_roster(path: str, rows: list[dict]) -> int:
    buf = ["\t".join(ROSTER_COLS)]
    for r in rows:
        buf.append("\t".join(
            "" if r.get(c) is None else str(r.get(c, "")).replace("\t", " ").replace("\n", " ")
            for c in ROSTER_COLS
        ))
    data = ("\n".join(buf) + "\n").encode("utf-8")
    with gzip.open(path, "wb", compresslevel=9) as fh:
        fh.write(data)
    return os.path.getsize(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=os.getcwd())
    ap.add_argument("--date", default=None, help="snapshot date (UTC today by default)")
    ap.add_argument("--no-github", action="store_true", help="skip the star join")
    ap.add_argument("--keep-raw", action="store_true", help="write the full 21MB sweep to raw/")
    ap.add_argument(
        "--from-raw", action="store_true",
        help="recompute a snapshot from the retained raw sweep + that day's roster "
             "instead of hitting the APIs. For fixing an analysis bug without "
             "re-observing (and thereby losing) the original moment.",
    )
    args = ap.parse_args()

    today = args.date or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    base = os.path.join(args.repo_root, "_data", "mcp_registry_history")
    roster_dir = os.path.join(base, "roster")
    os.makedirs(roster_dir, exist_ok=True)

    out_path = os.path.join(base, f"{today}.json")
    if os.path.exists(out_path) and not args.from_raw:
        log(f"ERROR: {out_path} already exists — refusing to overwrite a snapshot.")
        log("A snapshot is an observation, not a derivation. Use --from-raw to recompute "
            "it from the retained sweep, or delete it deliberately to re-observe.")
        return 1

    stars: dict = {}

    if args.from_raw:
        raw_path = os.path.join(base, "raw", f"{today}.json")
        roster_path = os.path.join(roster_dir, f"{today}.tsv.gz")
        if not os.path.exists(raw_path):
            log(f"ERROR: --from-raw needs {raw_path}, which does not exist.")
            return 1
        with open(raw_path) as fh:
            servers = json.load(fh)
        log(f"recomputing from raw/{today}.json ({len(servers)} entries) — no API calls")
        # Star counts are an observation too; recover them from that day's roster
        # rather than re-fetching today's values into a past-dated snapshot.
        if os.path.exists(roster_path):
            with gzip.open(roster_path, "rt", encoding="utf-8") as fh:
                header = fh.readline().rstrip("\n").split("\t")
                for line in fh:
                    row = dict(zip(header, line.rstrip("\n").split("\t")))
                    rk = parse_repo("https://github.com/" + row.get("repo", "")) \
                        if row.get("repo") else None
                    if rk and row.get("stars"):
                        stars[rk] = {
                            "stargazerCount": to_int(row.get("stars")),
                            "forkCount": to_int(row.get("forks")),
                            "pushedAt": row.get("pushed_at") or None,
                            "isArchived": row.get("archived") == "True",
                        }
            log(f"recovered star counts for {len(stars)} repos from roster/{today}.tsv.gz")
        else:
            log("WARN: no roster for this date — snapshot will be rebuilt without stars")
        rows = build_rows(servers, stars)
        prev_date, prev = load_prev_roster(roster_dir, today)
        snapshot = build_snapshot(rows, prev_date, prev, today,
                                  github_enabled=bool(stars))
        with open(out_path, "w") as fh:
            json.dump(snapshot, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        size = write_roster(os.path.join(roster_dir, f"{today}.tsv.gz"), rows)
        log(f"recomputed {out_path} and roster ({size / 1024:.0f} KB)")
        return 0

    log("sweeping registry…")
    servers = sweep_registry()

    if args.keep_raw:
        raw_dir = os.path.join(base, "raw")
        os.makedirs(raw_dir, exist_ok=True)
        with open(os.path.join(raw_dir, f"{today}.json"), "w") as fh:
            json.dump(servers, fh)
        log(f"raw sweep retained at raw/{today}.json")

    if not args.no_github:
        repo_keys = []
        seen = set()
        for e in servers:
            rk = parse_repo(((e.get("server") or {}).get("repository") or {}).get("url"))
            if rk and rk not in seen:
                seen.add(rk)
                repo_keys.append(rk)
        log(f"resolving {len(repo_keys)} distinct GitHub repos…")
        stars = fetch_stars(repo_keys)
        log(f"resolved {len(stars)}/{len(repo_keys)} repos")

    rows = build_rows(servers, stars)
    prev_date, prev = load_prev_roster(roster_dir, today)
    if prev_date:
        log(f"diffing against roster {prev_date} ({len(prev)} rows)")
    else:
        log("no previous roster — this is the baseline week; churn and delta ranking stay null")

    snapshot = build_snapshot(rows, prev_date, prev, today, github_enabled=not args.no_github)

    with open(out_path, "w") as fh:
        json.dump(snapshot, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    size = write_roster(os.path.join(roster_dir, f"{today}.tsv.gz"), rows)

    t = snapshot["totals"]
    log("--- snapshot written ---")
    log(f"  {out_path}")
    log(f"  roster/{today}.tsv.gz ({size / 1024:.0f} KB)")
    log(f"  servers={t['servers_latest']} active={t['active']} deprecated={t['deprecated']} "
        f"repos_resolved={t.get('repos_resolved', 'n/a')}")
    if snapshot.get("churn"):
        c = snapshot["churn"]
        log(f"  churn vs {c['compared_to']}: +{c['appeared']} / -{c['disappeared']} / "
            f"deprecated+{c['newly_deprecated']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
