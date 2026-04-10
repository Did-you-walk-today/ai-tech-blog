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
5. Structured data: comparison table required — HARD REQUIREMENT (JSON code blocks forbidden)
6. FAQ section: min 3 questions (People Also Ask)
7. Internal links: 2–3 within same topic cluster
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

## Topic Clusters (build these first)

1. **CLUSTER_LLM**: Pillar "Best LLM 2026" + comparisons, pricing DB, coding benchmark
2. **CLUSTER_DEVTOOLS**: Pillar "Best AI Coding Tools 2026" + Claude Code, Cursor vs Copilot, MCP
3. **CLUSTER_PROMPTS**: Pillar "Ultimate AI Prompt Library 2026" + by job role, system prompts

## File Paths

- Posts: `_posts/YYYY-MM-DD-slug.md`
- Data: `_data/YYYY-MM-DD-slug.json`
- API: `api/posts.json`
- LLMs: `llms.txt`

## Quality Score Formula

Weighted score (required >= 7.0 to publish):
- technical_accuracy × 0.30
- structural_quality × 0.25
- practical_value × 0.25
- data_completeness × 0.20

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
