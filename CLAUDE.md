# CLAUDE.md — AI Tech Resource Blog

This file is automatically loaded by Claude Code. It contains all context needed to operate the blog automation pipeline.

## Blog Identity

- **Name**: AI Tech Resource Blog
- **Platform**: GitHub Pages (Jekyll)
- **Audience**: AI power users, developers, engineers
- **Language**: English (global)
- **Core value**: "Structured data you can actually USE"
- **Stage**: Phase 1 (months 1-3) — launch and first 20+ posts

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

## SEO Rules (MANDATORY — every post)

1. Title: max 60 chars, include "2026", primary keyword in first 5 words
2. Meta description: 150–160 chars, directly answer search intent
3. First paragraph: answer main question within 150 words
4. TL;DR: 3–5 bullets (Featured Snippet targeting)
5. Structured data: 1 JSON block OR comparison table — HARD REQUIREMENT
6. FAQ section: min 3 questions (People Also Ask)
7. Internal links: 2–3 within same topic cluster
8. Word count: min 600 words (excluding code/data blocks)
9. data_updated field: always present

## Hard Reject Conditions (auto-regenerate)

- Title > 60 chars
- No year "2026" in title
- Meta description outside 140–165 chars
- No JSON block or comparison table
- Word count < 600 (excl. data blocks)
- Pricing data > 7 days old
- Code syntax errors
- Any quality score < 7.0

## Post Formats

| ID | Type | Requirement |
|----|------|-------------|
| A | Tool comparison | JSON data block required |
| B | Prompt library | 15+ prompts, tested score >= 8.0 |
| C | Technical guide | Step-by-step with code |
| D | Structured data | Tables + JSON, updated monthly |
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

## Topic Clusters (build these first)

1. **CLUSTER_LLM**: Pillar "Best LLM 2026" + comparisons, pricing DB, coding benchmark
2. **CLUSTER_DEVTOOLS**: Pillar "Best AI Coding Tools 2026" + Claude Code, Cursor vs Copilot, MCP
3. **CLUSTER_PROMPTS**: Pillar "Ultimate AI Prompt Library 2026" + by job role, system prompts

## File Paths

- Posts: `_posts/YYYY-MM-DD-slug.md`
- Data: `_data/YYYY-MM-DD-slug.json`
- API: `api/posts.json`
- LLMs: `llms.txt`

## Post Creation Rule — MANDATORY

Every post MUST produce TWO separate files:

1. `_posts/YYYY-MM-DD-slug.md` — human-readable blog post (SEO content, narrative, analysis)
2. `_data/YYYY-MM-DD-slug.json` — machine-readable structured data (extracted from the JSON block inside the MD)

**Why separate files:**
- `_data/` JSON can be updated independently on a schedule (Phase 7 Data Freshness) without regenerating the full post
- Jekyll templates can reference `site.data` directly for dynamic rendering
- `api/posts.json` endpoint exposes the data programmatically to external consumers
- Pricing/benchmark data stays fresh by updating only the JSON — the post content remains stable

**Workflow:**
- Generate MD first, embed JSON block inside post body (for inline display)
- Extract that same JSON block → save as standalone `_data/YYYY-MM-DD-slug.json`
- Both files committed and pushed together

## Quality Score Formula

Weighted score (required >= 7.0 to publish):
- technical_accuracy × 0.30
- structural_quality × 0.25
- practical_value × 0.25
- data_completeness × 0.20

See PIPELINE_PROMPT.md for full phase instructions.
See SEO_GUIDE.md for detailed SEO enforcement rules.
See SOURCES.md for trusted source list and priority ranking.
