---
title: "MCP Server Rankings 2026: 24,477 Servers, Ownership Checked"
description: "We swept 24,477 servers in the official MCP registry and joined GitHub stars. Four of the top 100 declare a repo they do not own, and 13.8% of links are dead."
date: 2026-08-24 09:00:00 +0000
last_modified_at: 2026-08-24 10:10:00 +0000
categories: [ai-developer-tools]
tags: [mcp, model-context-protocol, ai-agents, developer-tools, "2026"]
format: F
cluster: CLUSTER_DEVTOOLS
image:
  path: /assets/img/posts/mcp-registry-report-2026-cover.jpg
  alt: "A brass gear tipped against dark slate, one edge sharp under raking cyan light while the rest of the rim falls into shadow"
data_updated: 2026-08-24
author: jsonhouse
faq:
  - q: "How many MCP servers exist in the official registry?"
    a: "24,477 servers had a latest version on 2026-08-24, of which 24,220 were active and 257 deprecated. The registry grew by 2,388 servers in the seven days since our previous sweep, against 28 that disappeared."
  - q: "Does the MCP registry verify that a server owns the repository it links to?"
    a: "No. The registry verifies the namespace through GitHub OAuth or a DNS TXT record, but the repository URL is a self-declared field. Its own documentation states the publishing token needs no repository scopes because the registry never reads your code."
  - q: "Does a namespace-repository mismatch mean the server is fraudulent?"
    a: "No. Mismatch only means the namespace owner and the repository owner are different strings, and ownership transfers produce that difference honestly. It is a prompt to look at the specific entry, not a verdict — though the four in our top 100 are hard to read charitably."
  - q: "Why do MCP server rankings disagree with each other?"
    a: "Most rank by GitHub stars taken from the repository field without checking whether that repository belongs to the publisher. Any entry pointing at a large unrelated project inherits its star count and jumps the ranking."
  - q: "How often is this ranking updated?"
    a: "Every Monday. The full registry is swept, GitHub stars are re-joined, and the table plus the changelog below are updated in place at this same URL. Week-over-week star movement appears from the 2026-08-24 edition onward, once two snapshots existed to compare."
---

The official Model Context Protocol registry held **24,477 servers** when we swept it on 2026-08-24. Rank them by GitHub stars and you get a leaderboard that looks authoritative. It is not. The registry never checks whether the repository a server points at actually belongs to the publisher — so four of the top 100 borrow the star count of a project they do not own, and one of them is a hip-hop analytics server wearing a 79,252-star repository.

This page is the full sweep, ranked, with an ownership label on every row.

## TL;DR

- **24,477 servers** carried a latest version on 2026-08-24 — 24,220 active, 257 deprecated, and 2,388 more than seven days earlier
- **Of the top 100 by stars: 75 verified, 4 mismatched, 21 unverifiable.** A quarter of the leaderboard cannot be mechanically tied to its repository
- **65 of the top 100 point at a repository that is not a dedicated MCP server** — their stars belong to a whole product
- **2,630 declared repositories (13.8%) are not publicly reachable** — deleted, renamed, or private
- **5,428 servers (22.2%) declare no repository at all** and cannot appear in any star ranking
- One namespace, `io.github.pipeworx-io`, holds **5.36%** of the entire registry — 1,312 servers, and the top ten now hold 16.06%, up from 12.44% in a single week
- **The registry cannot tell you when a server was registered.** Its date field tracks the latest version, so 583 servers moved months this week without being new

## The ranking — top 20 by GitHub stars

Measured by jsonhouse, 2026-08-24. The `7d` column is the change in stars since our 2026-08-17 sweep. One repository occupies one slot; where several servers declare the same repository, the highest-ranked entry is shown.

A dagger (†) marks rows whose declared repository is not dedicated to the MCP server. We apply one mechanical rule — the repository name does not contain `mcp` — so the marking is reproducible rather than a judgement call. It is a proxy, and it is coarse: `oraios/serena` is an agent toolkit that ships an MCP server, not a mislabelled row.

The proportion is the point. **65 of the top 100 carry a dagger.** Their median star count is 6,562 against 4,334 for the 35 dedicated repositories, so the leaderboard systematically ranks products above the servers it claims to rank. The 65/35 split is identical to last week — the registry grew by 2,388 servers and the composition of its leaderboard did not budge.

| # | Server name | Repository | Stars | 7d | Namespace↔repo |
|---|---|---|---:|---:|---|
| 1 | `com.browser-use/browser-use` | `browser-use/browser-use` † | 110,288 | +812 | Unverifiable |
| 2 | `app.worldmonitor/mcp` | `koala73/worldmonitor` † | 83,966 | +1,467 | Unverifiable |
| 3 | `io.github.netdata/mcp-server` | `netdata/netdata` † | 80,269 | +61 | Verified |
| 4 | `io.github.IncorporatedPartners/labelhead-artist-momentum` | `paperclipai/paperclip` † | 79,252 | +654 | **Mismatch** |
| 5 | `io.github.D4Vinci/Scrapling` | `D4Vinci/Scrapling` † | 76,144 | +1,490 | Verified |
| 6 | `io.github.ruvnet/claude-flow` | `ruvnet/claude-flow` † | 69,132 | +1,100 | Verified |
| 7 | `io.github.upstash/context7` | `upstash/context7` † | 61,126 | +267 | Verified |
| 8 | `io.github.tldraw/tldraw` | `tldraw/tldraw` † | 49,927 | +116 | Verified |
| 9 | `io.github.ChromeDevTools/chrome-devtools-mcp` | `ChromeDevTools/chrome-devtools-mcp` | 49,617 | +338 | Verified |
| 10 | `io.github.metabase/mcp` | `metabase/metabase` † | 48,897 | +102 | Verified |
| 11 | `com.puter/mcp-server` | `HeyPuter/puter` † | 43,204 | +127 | Unverifiable |
| 12 | `io.github.amruthpillai/reactive-resume` | `amruthpillai/reactive-resume` † | 41,605 | +902 | Verified |
| 13 | `io.github.DeusData/codebase-memory-mcp` | `DeusData/codebase-memory-mcp` | 40,204 | +1,021 | Verified |
| 14 | `io.github.PostHog/mcp` | `PostHog/posthog` † | 38,791 | +1,078 | Verified |
| 15 | `io.github.bytedance/mcp-server-browser` | `bytedance/UI-TARS-desktop` † | 38,699 | +88 | Verified |
| 16 | `io.github.microsoft/playwright-mcp` | `microsoft/playwright-mcp` | 36,408 | +216 | Verified |
| 17 | `io.github.github/github-mcp-server` | `github/github-mcp-server` | 32,458 | +162 | Verified |
| 18 | `io.github.oraios/serena` | `oraios/serena` † | 28,423 | +302 | Verified |
| 19 | `ai.com.mcp/skills-search` | `agentskills/agentskills` † | 24,633 | +277 | Unverifiable |
| 20 | `dev.ohmyposh/validator` | `JanDeDobbeleer/oh-my-posh` † | 23,335 | +46 | Unverifiable |

> **Raw data**: [data/mcp-registry-report-2026.json](https://www.jsonhouse.com/data/mcp-registry-report-2026.json) — machine-readable structured data for AI crawlers and citation.

The full 100-row table lives in that file, along with the ownership breakdown and namespace concentration figures.

## What the labels mean

Every publisher in this registry is authenticated. That part works. What is not authenticated is the pointer.

| Label | Meaning | Count (all 24,477) |
|---|---|---:|
| Verified | `io.github.X/*` namespace, repository owner is also `X` | 14,934 |
| Mismatch | `io.github.X/*` namespace, repository owner is someone else | 504 |
| Unverifiable | Domain namespace — no mechanical link to a repo owner exists | 3,611 |
| No repo | No repository declared at all | 5,428 |

"Unverifiable" is not an accusation. A publisher using `com.browser-use/*` proved control of `browser-use.com` via a DNS TXT record. That is a real credential. It simply says nothing about who owns `github.com/browser-use/browser-use`, so no automated check can confirm or deny the pairing.

"Mismatch" is not an accusation either — it only says two strings differ, and an ownership transfer makes them differ honestly. The registry holds a clean example of exactly that, and it is instructive because the transfer does **not** surface as a mismatch. Sentry [acquired XcodeBuildMCP](https://blog.sentry.io/sentry-acquires-xcodebuildmcp) in February 2026 and the repository moved to `getsentry/XcodeBuildMCP`.

The project now sits in the registry twice. Rank 43 is `com.xcodebuildmcp/XcodeBuildMCP` pointing at the new owner, labelled unverifiable because a domain namespace has no mechanical link to any repo account. Rank 44 is `io.github.cameroncooke/XcodeBuildMCP` still pointing at the founder, labelled verified because that string does match. Both read 6,274 stars and the same last-push timestamp — they are one repository reached through GitHub's redirect, occupying two ranks. The label that marks the acquisition is the one meaning "we cannot check," and the stale row is the one the checker approves.

{% include mcp-ownership-banner.html %}

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
| Sweep date | 2026-08-24 (UTC) |
| Registry endpoint | `registry.modelcontextprotocol.io/v0/servers?version=latest` |
| Entries retrieved | 24,477 |
| Star source | GitHub GraphQL `stargazerCount`, same date |
| Repositories resolved | 16,419 of 19,049 declared |
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

Rank 4 shows the ceiling. A hip-hop analytics server sits above Scrapling, claude-flow, and context7 — all of which earned their positions — because it declares a repository with 79,252 stars, and it gained 654 of them this week without touching its own code. No agent selecting a server by rank would catch this.

The other three mismatches are quieter and more instructive. Two are personal namespaces declaring repositories owned by major organisations — rank 37 points at `MystenLabs/sui` (7,737 stars), rank 79 at a widely forked Claude Code project (3,257 stars). A third, rank 95, is `io.github.PremierInc/azure-devops` pointing at `microsoft/azure-devops-mcp` (1,974 stars).

None of these is necessarily deceptive. A fork, a contribution, or a rebranded deployment all produce the same record. Every one of them would still inflate a ranking that trusts the field.

And 22.2% of the registry — the 5,428 servers with no repository at all — is invisible to every star-based ranking by construction. Whatever those servers are, popularity ranking has no opinion about them.

## What this connects to

The registry is growing faster than anyone is verifying it: 2,388 servers appeared in the seven days between our two sweeps, against 28 that disappeared.

We cannot tell you how that compares to July, and neither can anyone else — including from the registry's own data. Each entry carries a `publishedAt` timestamp that reads like a registration date, and it is not one. The API serves one row per server at `version=latest`, so publishing a new version moves that server's timestamp forward and out of the month it was actually registered in.

Comparing our two rosters makes the size of the leak concrete. **583 servers present in both weeks changed months**, every one of them with a changed version string. July's count fell from 5,411 to 5,166 in seven days; June's fell from 3,699 to 3,502. The August bucket reads 7,516, of which 2,388 are genuinely new this week and 583 are older servers that shipped a release.

The practical consequence is that any "registrations per month" chart built from this field understates the past and overstates the present, and gets worse the further back you look. This page carried exactly that chart in draft, sourced from our 2026-08-17 sweep. The second sweep is what caught it — a single sweep cannot detect this at all, which is why the claim came out before publication rather than after.

Concentration is measurable, and it moved. One namespace, `io.github.pipeworx-io`, holds 1,312 servers — 5.36% of everything, down from 5.93% only because the denominator grew. The top ten namespaces went from 12.44% to **16.06% in one week**: `io.github.mcp-dir` went from 236 servers to 1,095, `io.github.Evozim` from 99 to 375, and `io.github.Wxt-ai` arrived with 122. Bulk publishing is now a meaningful share of the registry, and bulk publishers are precisely the population least likely to hand-check a repository field.

This is the same structural gap we found measuring [AI crawler traffic](/posts/ai-crawler-traffic-2026/): infrastructure gets built for discovery long before it gets built for verification, and the measurement layer arrives last. It is also why we run [content quality gates](/posts/ai-content-quality-gates-2026/) as executable checks rather than review conventions — an unenforced field drifts, always.

For anyone choosing tooling from these lists, the practical companion is our [AI coding tools comparison](/posts/best-ai-coding-tools-2026/), which ranks on measured behaviour instead of declared metadata.

## What to do with this

If you are picking an MCP server, do not treat a star count as a property of the server. It is a property of whatever repository the publisher typed in. Open the repository and confirm it contains the server you are about to install.

If you publish a ranking or a directory, compare the namespace to the repository owner. For `io.github.*` entries this is one string comparison and it catches 504 rows. Label them rather than deleting them — legitimate transfers look identical.

If you maintain a server, check your own entry. Mismatches also happen by copy-paste, and yours will be read by agents that cannot tell.

## Limitations

State these before citing this data.

The ownership check only works on `io.github.*` namespaces. For the 3,611 servers on domain namespaces we report "unverifiable" and stop — we do not infer ownership from names.

Repository resolution failures are not classified. Of 19,049 declared repositories, 2,630 returned nothing. We verified a random sample of these by hand and all returned HTTP 404, but a 404 covers deleted, renamed, and private repositories alike, and we do not distinguish them.

Star counts measure attention, not quality, and they are not comparable across repository types. Our dagger rule — repository name lacks `mcp` — is a proxy for "not a dedicated server repository" and it misfires in both directions. It flags `oraios/serena`, which genuinely ships a server inside a toolkit, and it clears any dedicated repository that happens to omit the string. Treat the 65% as an order of magnitude, not a precise count.

This sweep excludes servers whose status is `deleted`. The registry hides these from default listings while retaining their metadata, so they are retrievable but not counted here.

Registration dates are not reported on this page, and the omission is deliberate. The registry's `publishedAt` field tracks the latest version rather than first registration, so any month-by-month registration series built from it decays as servers republish. We measured 583 servers moving months in one week. Until the registry exposes a first-published timestamp, the honest statement is that registration history is not retrievable from this API — and we will not derive an estimate and present it as a count.

Star deltas cover one week only. The `7d` column compares this sweep against 2026-08-17, the earliest sweep we hold; longer windows accumulate from here rather than being reconstructed.

## FAQ

### How many MCP servers exist in the official registry?

24,477 servers had a latest version on 2026-08-24 — 24,220 active and 257 deprecated. The registry gained 2,388 servers in the seven days since our previous sweep. Counts near 9,000 still circulate in articles written earlier in 2026.

### Does the MCP registry verify that a server owns the repository it links to?

No. It verifies the namespace through GitHub OAuth or a DNS TXT record, but the repository URL is self-declared. The publishing token requires no repository scopes at all, because the registry never reads your code.

### Does a namespace-repository mismatch mean the server is fraudulent?

No. Mismatch only means the namespace owner and the repository owner are different strings, and an ownership transfer produces that difference honestly. Treat it as a prompt to look at the specific entry, not as a verdict — though the four in our top 100 are hard to read charitably.

### Why do MCP server rankings disagree with each other?

Because most rank on stars read from the repository field without checking ownership, and because 22.2% of the registry declares no repository and silently drops out of every such ranking.

### How often is this page updated?

Every Monday. We sweep the full registry, re-join GitHub stars, and update the table, the data file, and the changelog in place at this URL.

## Changelog

| Date | Change |
|---|---|
| 2026-08-24 | First edition. Full sweep of 24,477 servers, ownership labelling introduced, and week-over-week star deltas against our 2026-08-17 sweep. That earlier sweep was collected but never published: comparing the two showed that the registry's `publishedAt` field tracks latest-version date rather than registration date, which invalidated the registration-growth section this page carried in draft. That section was removed before publication and replaced with the measurement itself. |
