# SEO_GUIDE.md — AI Tech Resource Blog SEO Rules

Machine-readable SEO enforcement guide. All rules are checked in Phase 4 validation.

---

## Section 1 — Title Rules

- Maximum 60 characters (hard limit)
- Must include year: "2026"
- Primary keyword must appear in first 5 words
- Prefer numbers, comparison words, or power words: "Best", "vs", "Complete", "Guide", "2026"

Good examples:
- "Claude vs GPT-4o: 2026 Complete Guide" (38 chars)
- "Best LLM APIs 2026: Pricing & Limits" (37 chars)
- "Top 10 Claude Prompts for Developers 2026" (42 chars)

Bad examples:
- "A Comprehensive Analysis of the Differences Between Claude and GPT-4o in 2026" (too long)
- "Claude AI Overview" (no year, no keyword prominence)

---

## Section 2 — Meta Description Rules

- Length: 150–160 characters (hard range)
- Must directly answer search intent
- Include primary keyword naturally
- Include a specific benefit or data point ("updated weekly", "with pricing table", "tested on 50+ prompts")

---

## Section 3 — Content Structure

### 3.1 First Paragraph
- Answer main question within first 150 words
- No fluff, no "In this post we will..."
- State the answer, then explain

### 3.2 TL;DR Section
- 3–5 bullet points
- Each bullet: one concrete takeaway (number, fact, or recommendation)
- Place immediately after first paragraph
- Targets Google Featured Snippets

### 3.3 Headers
- H2: Secondary keywords naturally included
- H3: FAQ questions, subsections
- Header hierarchy: H1 (title) > H2 (main sections) > H3 (subsections, FAQ)

### 3.4 FAQ Section
- Minimum 3 questions
- Questions sourced from People Also Ask (Google) for primary keyword
- Each answer: 2–4 sentences, direct and factual

---

## Section 4 — Structured Data Requirements

### 4.1 JSON-LD Schema (every post)
Required fields:
- @type: Article | HowTo | FAQPage | Dataset
- headline
- datePublished
- dateModified (= data_updated)
- author (Organization)
- publisher

### 4.2 Content Data Blocks
At least ONE of the following per post (HARD REQUIREMENT):
- JSON data block with real data (pricing, specs, benchmarks)
- Comparison table (markdown table with >= 3 columns, >= 3 rows)

---

## Section 5 — Internal Linking

- 2–3 internal links per post
- Links must go to posts in the same topic cluster
- Link text: natural keyword phrase, not "click here"
- CLUSTER_LLM posts link to other CLUSTER_LLM posts
- CLUSTER_DEVTOOLS posts link to other CLUSTER_DEVTOOLS posts

---

## Section 6 — Keyword Strategy

### 6.1 Primary Keyword
- Appears in: title, meta description, H1 (front matter), first paragraph, at least 2 H2s
- Density: 1–2% of total words

### 6.2 High-Traffic Target Keywords

**CLUSTER_LLM (CAT1)**
- "best llm 2026" — monthly searches: ~8,100
- "claude vs gpt-4o" — ~5,400
- "gpt-4o vs claude 3.5 sonnet" — ~3,600
- "llm pricing comparison 2026" — ~2,900
- "best ai model for coding 2026" — ~2,400
- "claude 3.5 sonnet pricing" — ~1,900
- "gemini vs claude vs gpt" — ~1,800

**CLUSTER_DEVTOOLS (CAT2)**
- "best ai coding tools 2026" — ~6,600
- "cursor vs github copilot 2026" — ~4,400
- "claude code review" — ~3,200
- "best ai code assistant 2026" — ~2,900
- "github copilot pricing 2026" — ~2,100
- "claude api pricing" — ~1,800
- "mcp model context protocol" — ~1,500

**CLUSTER_PROMPTS (CAT3)**
- "best claude prompts 2026" — ~5,400
- "chatgpt system prompt" — ~4,800
- "prompt engineering guide 2026" — ~3,900
- "claude prompt library" — ~2,200
- "ai prompts for developers" — ~1,600

### 6.3 Long-Tail Opportunities
- "[tool name] pricing 2026"
- "[tool A] vs [tool B] [year]"
- "how to use [tool] for [use case]"
- "best [tool] prompts [year]"

---

## Section 7 — Data Freshness Rules

| Data Type | Max Age | Source Priority |
|-----------|---------|-----------------|
| API pricing | 7 days | Official docs only |
| Model capabilities | 30 days | Official release notes |
| Benchmark scores | 60 days | LMSYS, official papers |
| Statistics/research | 90 days | Official reports |

---

## Section 8 — Quality Scoring

Weighted quality score (required >= 7.0):

| Factor | Weight | What to Check |
|--------|--------|---------------|
| technical_accuracy | 0.30 | Facts correct, sources cited, no errors |
| structural_quality | 0.25 | TL;DR present, proper H2/H3, FAQ section |
| practical_value | 0.25 | Actionable data, copy-ready code/prompts |
| data_completeness | 0.20 | JSON block or table present, data is current |

---

## Section 9 — Featured Snippet Optimization

Target featured snippets for queries with clear answers:

- Definition queries: Start answer with "X is..."
- List queries: Use numbered lists, 8 items max
- Table queries: Include comparison table with queried attributes
- How-to queries: Use numbered steps

TL;DR format for featured snippets:
```
**TL;DR**
- [Specific fact or recommendation with number]
- [Second key takeaway]
- [Third key takeaway]
- [Optional fourth point]
```

---

## Section 10 — Technical SEO Checklist

For every published post:
- [ ] canonical_url field present in front matter
- [ ] JSON-LD script block in post
- [ ] Image alt text (if images used)
- [ ] No broken internal links
- [ ] Post appears in /api/posts.json after push
- [ ] sitemap.xml includes post URL
