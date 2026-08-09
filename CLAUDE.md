# CLAUDE.md — AI Tech Resource Blog

This file is automatically loaded by Claude Code. It contains all context needed to operate the blog automation pipeline.

## Blog Identity

- **Name**: AI Tech Resource Blog
- **Platform**: GitHub Pages (Jekyll + Chirpy)
- **Domain**: https://www.jsonhouse.com
- **Audience**: AI power users, developers, engineers (global)
- **Core value**: "Structured data you can actually USE"
- **Stage**: Phase 2 (2026-07 ~) — 발행 재가동(주 2회) + 측정 인프라 구축. Full plan: `_plans/2026-07-09-phase2-roadmap.md`

## Mission & Strategy (READ FIRST — why this blog exists)

Surface goal: passive income ladder (AdSense → Gumroad → 제휴 → API billing).
**Real goal: build a data asset for the AI-agent era.** The endpoint is becoming
a data source that AI agents cite and eventually pay for. Every technical
investment (llms.txt, /api/posts.json, /data/*.json, JSON-LD, bot logs, future
MCP server) exists to serve Phase 3 (agent API billing / data licensing).

Operating principles derived from this goal:

1. **A post without its data file is a liability, not an asset.** Every post
   ships as a 3-piece set: English post + `_data/` JSON + Korean review report.
2. **License is deliberately NOT declared** (awareness-first strategy, decided
   2026-07-09). Do NOT add `license` fields to data files, JSON-LD, or llms.txt.
   Do not re-propose licensing unless 기웅 changes this policy.
3. **Consumption data is irreplaceable.** Bot crawls, AI citations, AI referrals
   from the past cannot be recovered. Systems that capture them come first.
   Bot logging spec (separate dedicated session): `_plans/2026-07-09-bot-logging-cloudflare-spec.md`
4. **Time-series data is the moat.** Weekly pricing snapshots in
   `_data/pricing_history/` compound into something competitors cannot copy.
   Never skip a Monday snapshot; never backfill one.
5. **Judge every proposal by: "Can an AI agent consume this?"**
6. **Data-type posts must aim to be a primary source** — pass the test
   "can an AI skip us and cite the original?" If yes, redesign the topic.
   Method: `PRIMARY_SOURCE_GUIDE.md` (topic selection, required elements,
   distribution). MANDATORY READ before planning any Format A/D/F post.

Publishing cadence (Phase 2): **2 posts per week** — Tuesday (data-type:
Format D/F/A, follows PRIMARY_SOURCE_GUIDE.md) and Friday (analysis-type).
Do not promise or plan more.

## Operating Skills (use these — don't improvise the workflow)

Project skills in `.claude/skills/` encode the standard workflows:

| Skill | When |
|---|---|
| `new-post` | Any post creation request (Phase 1–5, stops at human review) |
| `post-images` | Cover/diagram image work — plans images, writes Codex prompt packs, normalizes and verifies returned files |
| `publish-post` | After 기웅 approves a draft (Phase 6) |
| `pricing-snapshot` | Every Monday, or any pricing-data refresh request |

Hard boundary: **Phase 5 (human review) is never skipped.** No post moves to
`_posts/` or gets committed without explicit approval from 기웅.

## Language Policy

- **Posts**: English only (global audience, English SEO/AEO)
- **Reports / Previews / Phase 5 Review materials**: Korean (for 기웅's review efficiency)
- **Claude Code communication**: Korean
- Every Phase 5 review MUST include a Korean summary report alongside the English post draft

## Pipeline Overview

8-phase automated content pipeline. Human review (기웅) only at Phase 5.

| Phase | Name | When |
|-------|------|------|
| 1 | Content Discovery | Daily 09:00 UTC |
| 2 | Data Collection | After Phase 1 |
| 3 | Draft Generation | After Phase 2 |
| 4 | Technical Validation | After Phase 3 |
| 5 | Human Review | Manual |
| 6 | Publishing | After PR merge |
| 7 | Data Freshness | Weekly Monday |
| 8 | SEO Tracking | Weekly Monday |

## Style Guide (MANDATORY READ before writing)

Before writing ANY post, you MUST read STYLE_GUIDE.md.

All posts are in English. The 박종훈/메르/jsonhouse DNA distinction refers
to STRUCTURE and ANALYSIS METHODOLOGY, not language register.

- 박종훈 style → macro context + flow analysis (5-step structure)
- 메르 style → accessible explanation + practical connection (5-step structure)
- jsonhouse DNA → hybrid: context + data + practical (5-step structure)

Style selection by category:
- CAT1~CAT6 → jsonhouse DNA (default)
- CAT7 Deep Dive → 박종훈 structure
- CAT7 Weekly Digest → 메르 structure

Wrong style application is a HARD REJECT condition.

## SEO / AEO / GEO Rules (MANDATORY — every post)

Three layers, one checklist. SEO optimizes for ranking, AEO for extraction,
GEO for **citation** — being named as the source when a generative engine
writes an answer. Rules 10–14 are the GEO layer; full detail in
SEO_GUIDE.md §11–§13.

**SEO / AEO**

1. Title: max 60 chars, include "2026", primary keyword in first 5 words
2. Meta description: 150–160 chars, directly answer search intent
3. First paragraph: answer main question within 150 words
4. TL;DR: 3–5 bullets (Featured Snippet targeting)
5. Structured data: comparison table required — HARD REQUIREMENT (JSON code blocks forbidden)
6. FAQ section: min 3 questions (People Also Ask)
7. Internal links: 2–3 within same topic cluster (verified to exist)
8. Word count: min 600 words (excluding code/data blocks)
9. data_updated field: always present

**GEO**

10. Inline citation: min 1 outbound markdown link to a primary source, placed
    where the claim is made. **Bare domains in prose do not count** — a crawler
    cannot follow `platform.claude.com` written as text
11. Source depth: paired data file carries min 3 `primary_sources`, each with
    `title` and `url` (these become the Dataset schema's `citation` array)
12. Dataset link: body links its own `/data/{slug}.json`
13. Data file: all 13 required fields present; `data_updated` identical in
    front matter and data file
14. `key_facts`: 5–10 entries — the units a model can lift and attribute
15. `attribution` block present and complete — the terms have to travel inside
    the payload, because a consumer reads the dataset and never the terms page.
    See DATA_POLICY.md §3. `license` remains forbidden; the two are not the same

Site-level GEO infrastructure (Dataset/Organization/DataCatalog JSON-LD,
entity `sameAs`, logo assets) is one-off build work specified in
`_plans/2026-08-05-geo-implementation-spec.md`, not a per-post rule.

## Hard Reject Conditions (auto-regenerate)

- Title > 60 chars
- No year "2026" in title
- Meta description outside 140–165 chars
- No comparison table (JSON code blocks are also forbidden — use tables or prose)
- Word count < 600 (excl. data blocks)
- Pricing data > 7 days old
- Code syntax errors
- Any quality score < 7.0
- No "이면 분석" / deep analysis (just news summary, no "why")
- Wrong style applied (e.g., 메르 structure used for CAT1 deep technical post)
- Broken internal links (linking to non-existent slug)
- canonical_url field hardcoded in frontmatter (must be auto-generated)
- No inline outbound citation (D1) — zero primary-source links in the body
- Fewer than 3 `primary_sources` in the paired data file (D2)
- Body does not link its own `/data/{slug}.json` (D4)

## Frontmatter Required Fields

Every post MUST have:
- `title`, `description`, `date`, `last_modified_at`
- `categories`, `tags`
- `format` (A~G)
- `cluster` (must be an `id` declared in `_data/taxonomy.yml` — see Topic Clusters)
- `image` (path: `/assets/img/posts/{slug}-cover.jpg`, alt text required — see IMAGE_GUIDE.md)
- `faq` (array of `{q, a}` — minimum 3 entries, used for FAQPage schema auto-generation)
- `data_updated` (YYYY-MM-DD)
- `author`

Do NOT include:
- `canonical_url` field — let jekyll-seo-tag auto-generate based on permalink
  (hardcoding caused trailing slash mismatch in previous posts)

## Slug Rules

- Format: lowercase, hyphens, year suffix (e.g., `llm-api-pricing-2026`)
- Once a slug is decided in draft phase, NEVER change it
  (previous slug changes caused 9 broken internal links)
- Before linking to another post, verify slug exists in `_posts/`
- Do NOT link to unpublished/planned posts
- Internal link verification is part of Phase 4 Technical Validation

## Post Formats

| ID | Type | Requirement |
|----|------|-------------|
| A | Tool comparison | Comparison table required |
| B | Prompt library | 15+ prompts, tested score >= 8.0 |
| C | Technical guide | Step-by-step with code |
| D | Structured data | Tables only (no JSON code blocks), updated monthly |
| E | Workflow/template | Downloadable |
| F | Benchmark report | Tested data, transparent methodology |
| G | Weekly AI digest | Fully automated |

## Content Categories

| ID | Category | SEO Priority |
|----|----------|-------------|
| CAT1 | AI Models & Intelligence | Highest |
| CAT2 | AI Developer Tools | Highest CPC |
| CAT3 | Prompt Engineering | High |
| CAT4 | AI Productivity & Workflows | Medium |
| CAT5 | AI Data & Statistics | Medium |
| CAT6 | AI Safety & Ethics | Medium |
| CAT7 | Industry Analysis & Weekly Digest | Medium |

## Topic Clusters

**`_data/taxonomy.yml` is the single source of truth** for cluster and category
names. Do not introduce either anywhere else — a post using an undeclared name is
an ERROR, and `taxonomy_validation.py` blocks it. Adding a cluster or category
means editing `taxonomy.yml` first.

Priority build order (all declared in `taxonomy.yml`):

1. **CLUSTER_LLM**: Pillar `best-llm-2026` + comparisons, pricing DB, coding benchmark
2. **CLUSTER_DEVTOOLS**: Pillar `best-ai-coding-tools-2026` + Claude Code, Cursor vs Copilot, MCP
3. **CLUSTER_PROMPTS**: Pillar "Ultimate AI Prompt Library 2026" — **not yet published**
4. **CLUSTER_AEO**: Answer-engine optimization, citation supply, crawler economics — no pillar yet
5. **CLUSTER_AI_CONTENT_POLICY**: `status: deprecated`. Off-mission for a developer
   audience; the five published posts stay, but do not plan new posts into it.

The cluster's pillar is declared in two places that must agree: `pillar:` in
`taxonomy.yml` and `pillar: true` in that post's front matter. Disagreement is an
ERROR — that is what keeps a renamed or unpublished pillar from going unnoticed.

### Category hubs

Each category maps to one hub tab in `taxonomy.yml`. Hub tabs render through the
shared `_includes/hub-post-list.html`; never hand-write the listing Liquid again.
Validated automatically: a category with live posts whose hub is `published: false`
is an ERROR (this shipped once — a tab stayed hidden after its first post landed),
and a visible hub whose category has no live posts is a WARN.

## Phase 5: Human Review (기웅) — Korean report required

Auto-validation passed. Claude Code MUST generate a Korean review report
alongside the English post draft so 기웅 can review efficiently.

Korean report format (required sections):
- 핵심 주장 요약 (3줄)
- 인용된 수치/벤치마크 출처 목록
- 적용된 스타일 (박종훈 / 메르 / jsonhouse DNA) + 적용 근거
- 이면 분석 핵심 (2~3문장 한국어 요약)
- 의심스러운 사실 관계 항목 (있으면)
- 내부 링크 목록 + 검증 결과 (존재 여부)

Human reviews:
- 핵심 주장이 의도와 일치하는가
- 수치/가격/벤치마크 사실 관계
- 이면 분석이 일반론에 그치지 않는가
- 톤앤매너가 카테고리에 맞는가
- 영어 표현의 자연스러움 (전문 분석가 톤 유지)

Reject → PR comment with reason → Phase 3 regenerate

## File Paths

- Posts: `_posts/YYYY-MM-DD-slug.md`
- Data: `_data/YYYY-MM-DD-slug.json`
- API: `api/posts.json`
- LLMs: `llms.txt`
- Phase 5 Korean reports: `_reviews/YYYY-MM-DD-slug.ko.md`

**MANDATORY**: Every post Write MUST be accompanied by a `_data/YYYY-MM-DD-slug.json` file.
Extract the post's structured data (timelines, comparison tables, case studies) into JSON.
Commit both files together. Never publish a post without its data file.

## Public Data Architecture

### Data File Requirements

Every `_data/YYYY-MM-DD-{slug}.json` file MUST follow this schema.
The plugin auto-publishes these to `https://www.jsonhouse.com/data/{slug}.json`.

#### Required Fields (every post — all 9)

| Field | Type | Description |
|---|---|---|
| `schema_version` | string | Always `"1.0"` for now. Bump on breaking changes. |
| `slug` | string | Matches the post slug exactly. NO `post_slug` — use `slug`. |
| `title` | string | Post title (mirrors frontmatter `title`). |
| `description` | string | Post description (mirrors frontmatter `description`). |
| `data_updated` | string | YYYY-MM-DD format. When the data was last verified. |
| `source_post` | string | Full URL to the post (e.g., `https://www.jsonhouse.com/posts/{slug}/`). |
| `category` | string | Mirrors frontmatter `categories[0]`. |
| `cluster` | string | Mirrors frontmatter `cluster`. |
| `format` | string | Mirrors frontmatter `format` (A~G). |

#### Required Content Fields (every post — all 4)

| Field | Type | Description |
|---|---|---|
| `key_facts` | array of objects | 5-10 verifiable facts. See structure below. |
| `faq_summary` | array of objects | 3-5 FAQ items. Subset of post's full FAQ. |
| `primary_sources` | array of objects | 1차 출처 list. See structure below. |
| `attribution` | object | Use terms carried in the payload. See structure below and DATA_POLICY.md §3. |

#### `attribution` structure

```json
"attribution": {
  "source": "Json House",
  "source_url": "https://www.jsonhouse.com/posts/{slug}/",
  "dataset_url": "https://www.jsonhouse.com/data/{slug}.json",
  "citation": "Json House, \"{title}\", jsonhouse.com ({data_updated})",
  "attribution_required": true,
  "terms_url": "https://www.jsonhouse.com/data-policy/"
}
```

All six keys are required. `citation` must be copy-ready — a string a machine has
to assemble from parts is a string nothing will bother to assemble. Never add a
`license` field: DATA_POLICY.md §2 explains why declaring one forecloses Phase 3.

#### `key_facts` structure (option B — structured)

```json
"key_facts": [
  {
    "fact": "Google does not penalize AI content per se",
    "source": "Google Search Central, 2023.2",
    "category": "policy"
  }
]
```

- `fact`: 한 문장. 검증 가능한 사실.
- `source`: 어디서 나왔는지. 책임 가능한 인용 단위.
- `category`: `policy` / `data` / `trend` / `definition` / `case_study` 중 하나.

#### `faq_summary` structure

```json
"faq_summary": [
  {
    "q": "Question text",
    "a": "Concise answer (1-3 sentences)"
  }
]
```

#### `primary_sources` structure

```json
"primary_sources": [
  {
    "title": "Source title",
    "url": "https://...",
    "publisher": "Google Search Central"
  }
]
```

#### Variable Fields (use only when applicable)

| Field | When to use | Format |
|---|---|---|
| `comparison_data` | Format A (Tool comparison), F (Benchmark) | Object with `dimensions` and `entries` |
| `timeline` | Policy/history posts | Array of `{date, event, source}` |
| `numerical_data` | Statistics/benchmark posts | Object with `metrics` array |
| `code_examples` | Format C (Technical guide) | Array of `{language, snippet, description}` |

#### Field Sourcing Rule (CRITICAL)

When generating or updating data files:
- **Extract from the published post body — DO NOT invent.**
- If a field has no corresponding content in the post, omit it (variable fields) or ask the user (required fields).
- `title`, `description`, `cluster`, `format`, `category` are **manually mirrored** from frontmatter (not auto-synced). When the post's frontmatter changes, update the data file in the same commit.

#### Naming Convention (CRITICAL)

The plugin publishes a `_data/` file matching `YYYY-MM-DD-*.json` **only when a
post of the same basename exists in `_posts/`**. A data file written at Phase 3
stays private until its post clears Phase 5 and lands in `_posts/`; both go live
in the same deploy. Drafts are excluded even under `jekyll build --drafts`.

The build logs each withheld file (`DataPublisher: Withholding …`) — seeing that
line for a draft is expected, not an error.

**RULE**: Date prefix means PUBLIC *once the post is published*.

- Post-specific data (PUBLIC): `_data/YYYY-MM-DD-{slug}.json`
- Site config data (PRIVATE): `_data/{name}.yml` or `_data/{name}.json` (NO date prefix — examples: `authors.yml`, `navigation.yml`)

NEVER prefix non-post data with a date. A file like `_data/2026-05-03-authors.json` would be exposed publicly.

DO NOT create a top-level `data/` directory in the project root. The plugin generates this at build time. Manual creation causes permalink conflicts.

#### Linking Data Files in Post Body

Every post must include a link to its data file. Recommended placement:
- After the first comparison table or JSON block
- Format: `> **Raw data**: [data/{slug}.json](https://www.jsonhouse.com/data/{slug}.json) — machine-readable structured data for AI crawlers and citation.`

This signals AI crawlers that machine-readable data is available.

#### Example: Minimal Valid File

```json
{
  "schema_version": "1.0",
  "slug": "synthid-c2pa-explained-2026",
  "title": "SynthID and C2PA: How AI Image Verification Works in 2026",
  "description": "SynthID embeds invisible pixel watermarks. C2PA signs metadata. They're complementary layers, not competitors.",
  "data_updated": "2026-04-27",
  "source_post": "https://www.jsonhouse.com/posts/synthid-c2pa-explained-2026/",
  "category": "AI Trust",
  "cluster": "CLUSTER_AI_CONTENT_POLICY",
  "format": "C",
  "key_facts": [
    {
      "fact": "SynthID and C2PA operate on different layers — pixel vs metadata",
      "source": "SynthID-Image paper (arXiv 2510.09263)",
      "category": "definition"
    }
  ],
  "faq_summary": [
    {
      "q": "Will SynthID or C2PA become the standard?",
      "a": "Neither replaces the other. Google attaches both automatically since November 2025 because they cover different attack surfaces."
    }
  ],
  "primary_sources": [
    {
      "title": "SynthID official page",
      "url": "https://deepmind.google/models/synthid/",
      "publisher": "Google DeepMind"
    }
  ]
}
```

## Quality Score Formula

Weighted score (required >= 7.0 to publish):
- technical_accuracy × 0.30
- structural_quality × 0.25
- practical_value × 0.25
- data_completeness × 0.20

---

See PIPELINE_PROMPT.md for full phase instructions.
See SEO_GUIDE.md for detailed SEO enforcement rules.
See SOURCES.md for trusted source list and priority ranking.
See PRIMARY_SOURCE_GUIDE.md for primary-source post methodology (data-type posts).
See IMAGE_GUIDE.md for image rules (count per format, specs, fixed style tokens, alt text).
See DATA_POLICY.md for what we require of data consumers (attribution) and what we
owe them (cadence, revision, stated measurement limits). It does NOT declare a
license — `license` fields remain forbidden; `attribution` is a separate thing.

## Post Writing Principles (MANDATORY)

These apply to every post, regardless of format type. They are writing-level quality gates — not automatable, but required before Phase 5 (Human Review) sign-off.

1. **Partial code must declare its limits**
   If a code example solves only part of the problem, add an inline comment or a `> Note:` callout immediately after the block. Never present a partial solution as if it is complete.

2. **No simplistic-only approach**
   Do not present a naive solution (e.g., regex blacklist, simple keyword filter) as the primary or only recommendation. Always pair it with a stronger alternative or explicitly describe its limitations in the same section.

3. **Section depth must match heading scope**
   If a heading implies a broad or important topic, the section must have proportional content. A 2-line section under a significant H2 is a sign the topic was mentioned but not covered — expand or merge.

4. **Standards and documents need real context**
   When restructuring external standards (OWASP, RFC, ISO, etc.), add at least one concrete example, real-world incident, or specific implementation context. Do not restate the standard verbatim.

5. **Figures are claims, and claims need evidence in the post**
   Images split into two classes and the rule applies to one of them (IMAGE_GUIDE.md §1). An explanatory figure — any diagram or chart in the body — is an assertion. Every value-bearing element in it (a length, a count, a position, an order) must map to a number or statement that already exists in the post body, so these are generated by code, never by an image model. If the post says a value is unpublished, the figure may not give it a concrete form. If the post says something splits four ways, the figure may not compress it to one. Record the mapping in the prompt pack's 근거 대응표 before writing the code. A figure that is spec-perfect and semantically wrong is worse than no figure — it looks authoritative while contradicting the text.
   The cover is the other class: it is editorial art, it depicts no data, and it need not relate to the topic. Its freedom comes from asserting nothing, so the moment a cover shows bars, axes, scales, or countable repeated elements it has become a figure and is rejected.

6. **Paragraphs carry one idea**
   This blog's paragraph median is 53 words. Past 120 words a paragraph becomes an unreadable block on mobile and readers skip it entirely, taking the analysis with it. Long reasoning gets split, not compressed — the depth stays, the block does not.

7. **Match the assertion to the evidence you actually have**
   State published numbers as published, unpublished ones as unpublished, and inferred ones as inferred. "Not published" is a finding worth reporting, not a hole to paper over with an estimate. This applies to prose, tables, data files, and figures equally.

## Hook Configuration

Post validation runs automatically on every `Write` or `Edit` to `_posts/*.md` and `_drafts/*.md`.

- **Config**: `.claude/settings.json` (project-level, triggers `post-validation.sh`)
- **Script**: `.claude/hooks/post-validation.sh` (SEO + content quality checks)
- **Rules**: See the Hook Enforcement table below for full rule list

### GSC Indexing List Sync

`GSC_INDEXING.md` holds the manual Google Search Console index-submission list.
Its post table is regenerated automatically — never edit it by hand.

- **Script**: `.claude/hooks/sync-indexing-list.sh` → `sync_indexing_list.py`
- **Triggers**: `Write`/`Edit` to `_posts/*.md`, and `Bash` commands touching
  `_posts/` or running `git mv|commit|push|rm` (covers the publish-post skill's `git mv`)
- **Preserved on regen**: the 상태 checkbox and 메모 columns, keyed by URL
- **Manual run**: `python3 .claude/hooks/sync_indexing_list.py "$(git rev-parse --show-toplevel)"`

`sitemap.xml` needs no maintenance — `jekyll-sitemap` regenerates it from `_posts/`
on every deploy. Local `_site/sitemap.xml` is a gitignored build artifact and is
often stale; always verify against `https://www.jsonhouse.com/sitemap.xml`.

### Internal Link Graph

`LINK_GRAPH.md` is the index of how posts link to each other — per-post inbound and
outbound counts, the findings list, and section 3 showing **where every backlink is
placed and under what anchor text**. Use section 3 before changing a slug or
withdrawing a post: it lists exactly which files to edit.

The document is regenerated, never hand-written. A hand-maintained link index
drifts the moment someone edits a link and forgets the index, so the graph is
derived from post bodies instead.

- **Script**: `.claude/hooks/sync-link-graph.sh` → `link_graph.py`
- **Triggers**: same gating as the GSC sync — `Write`/`Edit` to `_posts/*.md`, and
  `Bash` commands touching `_posts/` or running `git mv|commit|push|rm`
- **Preserved on regen**: the 메모 column in section 1, keyed by slug
- **Manual run**: `python3 .claude/hooks/link_graph.py "$(git rev-parse --show-toplevel)"`
- **Check only**: `python3 .claude/hooks/link_graph.py --report` (exit 1 on ERROR)

Findings and severity:

| Finding | Meaning | Severity |
|---|---|---|
| `DANGLING` | link targets a slug not in `_posts/` | ERROR — hook exits 2, blocks publishing |
| `ORPHAN` | no inbound internal link | WARN |
| `DEADEND` | no outbound internal links | WARN |
| `THIN` | fewer than 2 outbound links (rule A9) | WARN |
| `NOINDEX<-` | a live post links to a `noindex: true` page | WARN |
| `SELFLINK` | post links to itself | WARN |

`noindex` posts are exempt from `ORPHAN` — losing inbound links is the intended
outcome for a withdrawn page.

The same hook also runs `taxonomy_validation.py`; either an ERROR there or a
`DANGLING` link exits 2 and blocks publishing.

**Build-time backstop**: `_plugins/link_checker.rb` fails the Jekyll build on a
dangling internal link. The hook only fires on Claude Code edits — links also
arrive from other sessions sharing this working tree and from the GitHub web
editor, and this catches those before deploy. It checks dangling links only;
orphans and thin link counts are judgment calls that belong in `LINK_GRAPH.md`,
not gates on a deploy.

## Hook Enforcement (Auto-triggered on every post write)

`.claude/hooks/post-validation.sh` runs automatically after every Write/Edit to `_posts/` or `_drafts/`.

### Checked Automatically

**Section A — SEO / Front Matter**

| Rule | Condition | Severity |
|------|-----------|----------|
| A1 Title length | <= 60 chars | ERROR |
| A2 Title year | Must contain "2026" | ERROR |
| A3 Meta description | 140–165 chars | ERROR |
| A4 Structured data | Comparison table required (```json forbidden — see B1) | ERROR |
| A5 Word count | >= 600 words (excl. code blocks) | ERROR |
| A6 data_updated field | Must be present in front matter | ERROR |
| A7 FAQ section | >= 3 question headings | WARN |
| A8 TL;DR section | Must exist | WARN |
| A9 Internal links | >= 2 links to /posts/ | WARN |

**Section B — Content Quality**

| Rule | Condition | Severity |
|------|-----------|----------|
| B1 JSON code block | Forbidden — convert to table or prose | ERROR |
| B2 Code block intro | Must have 1-2 sentences before code block | ERROR |
| B3 Code block outro | Must have 1 sentence after code block | ERROR |
| B4 Heading → code | No code block directly under a heading | ERROR |
| B5 Checklist coverage | Risk landscape items must all appear in checklist | ERROR |
| B6 FAQ/code mismatch | Open-problem FAQ + definitive code → add caveats | WARN |
| B7 Thin sections | Each section needs >= 40 words of prose. FAQ answers, TL;DR, changelog, and container headings are exempt | WARN |
| B8 Wall of text | No single paragraph over 120 words (blog median is 53) | WARN |

**Section C — Post Images** (delegated to `image_validation.py`, rules in `IMAGE_GUIDE.md`)

| Rule | Condition | Severity |
|------|-----------|----------|
| C1 Cover exists | `image.path` declared AND file present in `assets/img/posts/` | ERROR |
| C2 Cover alt | Present, 25–125 chars, describes the scene, contains no figure | ERROR / WARN |
| C3 Cover spec | Exactly 1200×630, <= 200KB | ERROR |
| C4 Body image refs | Every `![](/assets/…)` path resolves | ERROR |
| C5 Body image alt | Non-empty | ERROR |
| C6 Image count | <= 5 total including cover | WARN |
| C7 Filename convention | `{slug}-cover.jpg` / `-fig1.svg` / `-chart1.svg` / `-shot1.webp` | WARN |
| C8 Body image weight | Figures SVG/PNG, screenshots WebP, width <= 1600px, <= 150KB (SVG <= 100KB) | WARN |
| C9 Figure budget | Body images per format: A=1, B=0, C=3, D=1, E=3, F=2, G=0 | WARN |
| C10 Evidence table | Post with body figures needs `_reviews/{date}-{slug}.images.md` containing a 근거 대응표 | WARN |
| C11 Cover is generated art | Cover with <= 1,000 distinct colours is a code render, not a `$imagegen` output | ERROR |

**Section D — GEO / Citation Evidence** (delegated to `geo_validation.py`, rules in `SEO_GUIDE.md` §11–§13)

| Rule | Condition | Severity |
|------|-----------|----------|
| D1 Inline citation | >= 1 outbound markdown link to a primary source in the body (bare domains in prose do not count) | ERROR |
| D2 Source depth | Paired data file has >= 3 `primary_sources`, each with `title` + `url` | ERROR |
| D3 Fact granularity | `key_facts` holds 5–10 entries | WARN |
| D4 Dataset link | Body links its own `/data/{slug}.json` | ERROR |
| D5 Data file schema | Data file exists, parses, has all 13 required fields, `data_updated` matches front matter | ERROR |
| D6 Attribution block | `attribution` complete (6 keys), `attribution_required: true`, no `license` field | ERROR |

In `_drafts/` every Section C and Section D ERROR is downgraded to WARN — artwork
legitimately arrives after the draft, and a draft predates its data file and
source links. In `_posts/` they block publishing.

Repo-wide status: `python3 .claude/hooks/image_validation.py --report`
GEO status: `python3 .claude/hooks/geo_validation.py --report`

### Behavior

- **ERROR**: Shown prominently after file save — must fix before publishing
- **WARN**: Advisory — shown after save, fix before Phase 6 (Publishing)
- Hook only activates for `_posts/*.md` and `_drafts/*.md` files

See STYLE_GUIDE.md for tone, voice, and post structure rules (박종훈 / 메르 / jsonhouse DNA).
