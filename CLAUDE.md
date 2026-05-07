# CLAUDE.md — AI Tech Resource Blog

This file is automatically loaded by Claude Code. It contains all context needed to operate the blog automation pipeline.

## Blog Identity

- **Name**: AI Tech Resource Blog
- **Platform**: GitHub Pages (Jekyll + Chirpy)
- **Domain**: https://www.jsonhouse.com
- **Audience**: AI power users, developers, engineers (global)
- **Core value**: "Structured data you can actually USE"
- **Stage**: Phase 1 (months 1-3) — launch and first 20+ posts

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

## SEO Rules (MANDATORY — every post)

1. Title: max 60 chars, include "2026", primary keyword in first 5 words
2. Meta description: 150–160 chars, directly answer search intent
3. First paragraph: answer main question within 150 words
4. TL;DR: 3–5 bullets (Featured Snippet targeting)
5. Structured data: comparison table required — HARD REQUIREMENT (JSON code blocks forbidden)
6. FAQ section: min 3 questions (People Also Ask)
7. Internal links: 2–3 within same topic cluster (verified to exist)
8. Word count: min 600 words (excluding code/data blocks)
9. data_updated field: always present

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

## Frontmatter Required Fields

Every post MUST have:
- `title`, `description`, `date`, `last_modified_at`
- `categories`, `tags`
- `format` (A~G)
- `cluster` (CLUSTER_LLM | CLUSTER_DEVTOOLS | CLUSTER_PROMPTS)
- `image` (path: `/assets/img/posts/{slug}-cover.png`, alt text required)
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

## Topic Clusters (build these first)

1. **CLUSTER_LLM**: Pillar "Best LLM 2026" + comparisons, pricing DB, coding benchmark
2. **CLUSTER_DEVTOOLS**: Pillar "Best AI Coding Tools 2026" + Claude Code, Cursor vs Copilot, MCP
3. **CLUSTER_PROMPTS**: Pillar "Ultimate AI Prompt Library 2026" + by job role, system prompts

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

#### Required Content Fields (every post — all 3)

| Field | Type | Description |
|---|---|---|
| `key_facts` | array of objects | 5-10 verifiable facts. See structure below. |
| `faq_summary` | array of objects | 3-5 FAQ items. Subset of post's full FAQ. |
| `primary_sources` | array of objects | 1차 출처 list. See structure below. |

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

The plugin auto-publishes any `_data/` file matching `YYYY-MM-DD-*.json`.

**RULE**: Date prefix means PUBLIC.

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

## Hook Configuration

Post validation runs automatically on every `Write` or `Edit` to `_posts/*.md` and `_drafts/*.md`.

- **Config**: `.claude/settings.json` (project-level, triggers `post-validation.sh`)
- **Script**: `.claude/hooks/post-validation.sh` (SEO + content quality checks)
- **Rules**: See the Hook Enforcement table below for full rule list

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
| B7 Thin sections | Each H2/H3 section must have >= 3 lines | WARN |

### Behavior

- **ERROR**: Shown prominently after file save — must fix before publishing
- **WARN**: Advisory — shown after save, fix before Phase 6 (Publishing)
- Hook only activates for `_posts/*.md` and `_drafts/*.md` files

See STYLE_GUIDE.md for tone, voice, and post structure rules (박종훈 / 메르 / jsonhouse DNA).
