---
title: "MCP Server Rankings 2026: 22,117 Servers, Ownership Checked"
description: "We swept 22,117 servers in the official MCP registry and joined GitHub stars. Four of the top 100 declare a repo they do not own, and 14.7% of links are dead."
date: 2026-08-21 09:00:00 +0000
last_modified_at: 2026-08-21 09:00:00 +0000
categories: [ai-developer-tools]
tags: [mcp, model-context-protocol, ai-agents, developer-tools, "2026"]
format: F
cluster: CLUSTER_DEVTOOLS
image:
  path: /assets/img/posts/mcp-registry-report-2026-cover.jpg
  alt: "A brass gear tipped against dark slate, one edge sharp under raking cyan light while the rest of the rim falls into shadow"
data_updated: 2026-08-17
author: jsonhouse
faq:
  - q: "How many MCP servers exist in the official registry?"
    a: "22,117 servers had a latest version on 2026-08-17, of which 21,867 were active and 250 deprecated. That is roughly 2.3x the counts still circulating in articles written in mid-2026."
  - q: "Does the MCP registry verify that a server owns the repository it links to?"
    a: "No. The registry verifies the namespace through GitHub OAuth or a DNS TXT record, but the repository URL is a self-declared field. Its own documentation states the publishing token needs no repository scopes because the registry never reads your code."
  - q: "Does a namespace-repository mismatch mean the server is fraudulent?"
    a: "No. Mismatch only means the namespace owner and the repository owner are different strings, and ownership transfers produce that difference honestly. It is a prompt to look at the specific entry, not a verdict — though the four in our top 100 are hard to read charitably."
  - q: "Why do MCP server rankings disagree with each other?"
    a: "Most rank by GitHub stars taken from the repository field without checking whether that repository belongs to the publisher. Any entry pointing at a large unrelated project inherits its star count and jumps the ranking."
  - q: "How often is this ranking updated?"
    a: "Every Monday. The full registry is swept, GitHub stars are re-joined, and the table plus the changelog below are updated in place at this same URL."
---

The official Model Context Protocol registry held **22,117 servers** when we swept it on 2026-08-17. Rank them by GitHub stars and you get a leaderboard that looks authoritative. It is not. The registry never checks whether the repository a server points at actually belongs to the publisher — so four of the top 100 borrow the star count of a project they do not own, and one of them is a hip-hop analytics server wearing a 78,598-star repository.

This page is the full sweep, ranked, with an ownership label on every row.

## TL;DR

- **22,117 servers** carried a latest version on 2026-08-17 — 21,867 active, 250 deprecated
- **Of the top 100 by stars: 74 verified, 4 mismatched, 22 unverifiable.** A quarter of the leaderboard cannot be mechanically tied to its repository
- **65 of the top 100 point at a repository that is not a dedicated MCP server** — their stars belong to a whole product
- **2,575 declared repositories (14.7%) are not publicly reachable** — deleted, renamed, or private
- **4,577 servers (20.7%) declare no repository at all** and cannot appear in any star ranking
- One namespace, `io.github.pipeworx-io`, holds **5.93%** of the entire registry — 1,312 servers
- Registrations are accelerating: **5,411 in July 2026** alone, up from 351 in September 2025

## The ranking — top 20 by GitHub stars

Measured by jsonhouse, 2026-08-17. One repository occupies one slot; where several servers declare the same repository, the highest-ranked entry is shown.

A dagger (†) marks rows whose declared repository is not dedicated to the MCP server. We apply one mechanical rule — the repository name does not contain `mcp` — so the marking is reproducible rather than a judgement call. It is a proxy, and it is coarse: `oraios/serena` is an agent toolkit that ships an MCP server, not a mislabelled row.

The proportion is the point. **65 of the top 100 carry a dagger.** Their median star count is 6,250 against 4,081 for the 35 dedicated repositories, so the leaderboard systematically ranks products above the servers it claims to rank.

| # | Server name | Repository | Stars | Namespace↔repo |
|---|---|---|---:|---|
| 1 | `com.browser-use/browser-use` | `browser-use/browser-use` † | 109,476 | Unverifiable |
| 2 | `app.worldmonitor/mcp` | `koala73/worldmonitor` † | 82,499 | Unverifiable |
| 3 | `io.github.netdata/mcp-server` | `netdata/netdata` † | 80,208 | Verified |
| 4 | `io.github.IncorporatedPartners/labelhead-artist-momentum` | `paperclipai/paperclip` † | 78,598 | **Mismatch** |
| 5 | `io.github.D4Vinci/Scrapling` | `D4Vinci/Scrapling` † | 74,654 | Verified |
| 6 | `io.github.ruvnet/claude-flow` | `ruvnet/claude-flow` † | 68,032 | Verified |
| 7 | `io.github.upstash/context7` | `upstash/context7` † | 60,859 | Verified |
| 8 | `io.github.tldraw/tldraw` | `tldraw/tldraw` † | 49,811 | Verified |
| 9 | `io.github.ChromeDevTools/chrome-devtools-mcp` | `ChromeDevTools/chrome-devtools-mcp` | 49,279 | Verified |
| 10 | `io.github.metabase/mcp` | `metabase/metabase` † | 48,795 | Verified |
| 11 | `com.puter/mcp-server` | `HeyPuter/puter` † | 43,077 | Unverifiable |
| 12 | `io.github.amruthpillai/reactive-resume` | `amruthpillai/reactive-resume` † | 40,703 | Verified |
| 13 | `io.github.DeusData/codebase-memory-mcp` | `DeusData/codebase-memory-mcp` | 39,183 | Verified |
| 14 | `io.github.bytedance/mcp-server-browser` | `bytedance/UI-TARS-desktop` † | 38,611 | Verified |
| 15 | `io.github.PostHog/mcp` | `PostHog/posthog` † | 37,713 | Verified |
| 16 | `io.github.microsoft/playwright-mcp` | `microsoft/playwright-mcp` | 36,192 | Verified |
| 17 | `io.github.github/github-mcp-server` | `github/github-mcp-server` | 32,296 | Verified |
| 18 | `io.github.oraios/serena` | `oraios/serena` † | 28,121 | Verified |
| 19 | `ai.com.mcp/skills-search` | `agentskills/agentskills` † | 24,356 | Unverifiable |
| 20 | `dev.ohmyposh/validator` | `JanDeDobbeleer/oh-my-posh` † | 23,289 | Unverifiable |

> **Raw data**: [data/mcp-registry-report-2026.json](https://www.jsonhouse.com/data/mcp-registry-report-2026.json) — machine-readable structured data for AI crawlers and citation.

The full 100-row table lives in that file, along with the ownership breakdown and namespace concentration figures.

## What the labels mean

Every publisher in this registry is authenticated. That part works. What is not authenticated is the pointer.

| Label | Meaning | Count (all 22,117) |
|---|---|---:|
| Verified | `io.github.X/*` namespace, repository owner is also `X` | 13,636 |
| Mismatch | `io.github.X/*` namespace, repository owner is someone else | 483 |
| Unverifiable | Domain namespace — no mechanical link to a repo owner exists | 3,421 |
| No repo | No repository declared at all | 4,577 |

"Unverifiable" is not an accusation. A publisher using `com.browser-use/*` proved control of `browser-use.com` via a DNS TXT record. That is a real credential. It simply says nothing about who owns `github.com/browser-use/browser-use`, so no automated check can confirm or deny the pairing.

"Mismatch" is not an accusation either — it only says two strings differ, and an ownership transfer makes them differ honestly. The registry holds a clean example of exactly that, and it is instructive because the transfer does **not** surface as a mismatch. Sentry [acquired XcodeBuildMCP](https://blog.sentry.io/sentry-acquires-xcodebuildmcp) in February 2026 and the repository moved to `getsentry/XcodeBuildMCP`.

The project now sits in the registry twice. Rank 43 is `com.xcodebuildmcp/XcodeBuildMCP` pointing at the new owner, labelled unverifiable because a domain namespace has no mechanical link to any repo account. Rank 44 is `io.github.cameroncooke/XcodeBuildMCP` still pointing at the founder, labelled verified because that string does match. Both read 6,247 stars and the same last-push timestamp — they are one repository reached through GitHub's redirect, occupying two ranks. The label that marks the acquisition is the one meaning "we cannot check," and the stale row is the one the checker approves.

## Methodology

Every number on this page comes from a full sweep we ran ourselves. Nothing is taken from an aggregator.

The registry API is paginated by cursor and exposes only current state — there is no history endpoint. We walk every page with `version=latest`, which yields one row per server rather than one per version, then join GitHub metadata for each declared repository through the GraphQL API in aliased batches of 100.

Anyone can reproduce the rank-4 row in a single request against the live registry:
```bash
curl -s "https://registry.modelcontextprotocol.io/v0/servers?search=labelhead-artist-momentum&version=latest"
```
That returns a server described as "Trending hip-hop artist momentum scores across four cultural dimensions" with `repository.url` set to `https://github.com/paperclipai/paperclip`. No step in the publishing flow objected.

Collection parameters, for reproduction:

| Parameter | Value |
|---|---|
| Sweep date | 2026-08-17 (UTC) |
| Registry endpoint | `registry.modelcontextprotocol.io/v0/servers?version=latest` |
| Entries retrieved | 22,117 |
| Star source | GitHub GraphQL `stargazerCount`, same date |
| Repositories resolved | 14,965 of 17,540 declared |
| Update cadence | Weekly, every Monday |

Star counts are a snapshot, not an average. A repository that gained 400 stars the day before the sweep carries them.

## Why the registry does not check this

It would be easy to read the mismatches as a bug. They are a documented design choice, and the reasoning holds up.

The registry authenticates namespaces two ways. GitHub OAuth grants `io.github.<username>/*`, and organization namespaces require you to be an **Owner** of that org — ordinary membership no longer suffices. Domain namespaces require a DNS TXT record at the apex. Both are real proofs of control.

But the [authentication documentation](https://modelcontextprotocol.io/registry/authentication) is explicit about where that proof stops: the publishing token needs **no** repository scopes, because "the registry never reads or writes your code." Verifying repository ownership would mean demanding read access to every publisher's source. That is a large permission to request from 14,126 distinct namespaces in order to police a display field.

The moderation policy makes the same trade openly. It removes illegal content, malware, spam, and non-functioning servers — and states that the registry "does not make guarantees about moderation, and consumers should assume minimal-to-no moderation."

Then comes the line every ranking has ignored: ["Consumers should treat scraped data accordingly."](https://modelcontextprotocol.io/registry/moderation-policy)

So the registry is not making a false claim. It is publishing a self-declared field, labelling it as such, and telling downstream consumers to verify. The failure is entirely downstream.

## The part that actually breaks

An unverified pointer is harmless while nobody ranks on it. Ranking is exactly what everyone does.

The moment a directory sorts by stars pulled from `repository.url`, an entry pointing at a large unrelated project inherits that project's popularity. It does not need many stars of its own. It needs one plausible URL.

Rank 4 shows the ceiling. A hip-hop analytics server published in April 2026 sits above Scrapling, claude-flow, and context7 — all of which earned their positions — because it declares a repository with 78,598 stars. No agent selecting a server by rank would catch this.

The other three mismatches are quieter and more instructive. Two are personal namespaces declaring repositories owned by major organisations — one points at `MystenLabs/sui` (7,737 stars), another at a widely forked Claude Code project. A third, `io.github.PremierInc/azure-devops`, points at `microsoft/azure-devops-mcp` (1,958 stars).

None of these is necessarily deceptive. A fork, a contribution, or a rebranded deployment all produce the same record. Every one of them would still inflate a ranking that trusts the field.

And 20.7% of the registry — the 4,577 servers with no repository at all — is invisible to every star-based ranking by construction. Whatever those servers are, popularity ranking has no opinion about them.

## What this connects to

The registry is growing faster than anyone is verifying it. Monthly registrations went from 351 in September 2025 to 5,411 in July 2026, a 15x increase in ten months. August was at 4,552 when we swept on the 17th.

Concentration grew with it. One namespace, `io.github.pipeworx-io`, holds 1,312 servers — 5.93% of everything. The top ten namespaces hold 12.44% between them. Bulk publishing is now a meaningful share of the registry, and bulk publishers are precisely the population least likely to hand-check a repository field.

This is the same structural gap we found measuring [AI crawler traffic](/posts/ai-crawler-traffic-2026/): infrastructure gets built for discovery long before it gets built for verification, and the measurement layer arrives last. It is also why we run [content quality gates](/posts/ai-content-quality-gates-2026/) as executable checks rather than review conventions — an unenforced field drifts, always.

For anyone choosing tooling from these lists, the practical companion is our [AI coding tools comparison](/posts/best-ai-coding-tools-2026/), which ranks on measured behaviour instead of declared metadata.

## What to do with this

If you are picking an MCP server, do not treat a star count as a property of the server. It is a property of whatever repository the publisher typed in. Open the repository and confirm it contains the server you are about to install.

If you publish a ranking or a directory, compare the namespace to the repository owner. For `io.github.*` entries this is one string comparison and it catches 483 rows. Label them rather than deleting them — legitimate transfers look identical.

If you maintain a server, check your own entry. Mismatches also happen by copy-paste, and yours will be read by agents that cannot tell.

## Limitations

State these before citing this data.

The ownership check only works on `io.github.*` namespaces. For the 3,421 servers on domain namespaces we report "unverifiable" and stop — we do not infer ownership from names.

Repository resolution failures are not classified. Of 17,540 declared repositories, 2,575 returned nothing. We verified a random sample of these by hand and all returned HTTP 404, but a 404 covers deleted, renamed, and private repositories alike, and we do not distinguish them.

Star counts measure attention, not quality, and they are not comparable across repository types. Our dagger rule — repository name lacks `mcp` — is a proxy for "not a dedicated server repository" and it misfires in both directions. It flags `oraios/serena`, which genuinely ships a server inside a toolkit, and it clears any dedicated repository that happens to omit the string. Treat the 65% as an order of magnitude, not a precise count.

This sweep excludes servers whose status is `deleted`. The registry hides these from default listings while retaining their metadata, so they are retrievable but not counted here.

Week-over-week movement is absent from this first edition. Delta columns require a prior snapshot and appear from the 2026-08-24 update onward.

## FAQ

### How many MCP servers exist in the official registry?

22,117 servers had a latest version on 2026-08-17 — 21,867 active and 250 deprecated. Counts near 9,000 still circulate in articles written earlier in 2026; the registry has more than doubled since.

### Does the MCP registry verify that a server owns the repository it links to?

No. It verifies the namespace through GitHub OAuth or a DNS TXT record, but the repository URL is self-declared. The publishing token requires no repository scopes at all, because the registry never reads your code.

### Does a namespace-repository mismatch mean the server is fraudulent?

No. Mismatch only means the namespace owner and the repository owner are different strings, and an ownership transfer produces that difference honestly. Treat it as a prompt to look at the specific entry, not as a verdict — though the four in our top 100 are hard to read charitably.

### Why do MCP server rankings disagree with each other?

Because most rank on stars read from the repository field without checking ownership, and because 20.7% of the registry declares no repository and silently drops out of every such ranking.

### How often is this page updated?

Every Monday. We sweep the full registry, re-join GitHub stars, and update the table, the data file, and the changelog in place at this URL.

## Changelog

| Date | Change |
|---|---|
| 2026-08-21 | First edition. Full sweep of 22,117 servers on 2026-08-17, ownership labelling introduced. Delta columns pending a second snapshot. |
