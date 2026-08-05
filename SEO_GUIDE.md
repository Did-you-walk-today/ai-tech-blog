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

---

## Section 11 — GEO: Optimizing for Citation

Sections 1–10 optimize for **ranking** (SEO) and **extraction** (AEO). Section 11–13
optimize for **citation** (GEO) — being named as the source when a generative
engine writes an answer.

The three layers are not alternatives. They stack, and they diverge at exactly
one point:

| | SEO | AEO | GEO |
|---|---|---|---|
| Consumer | ranking algorithm | extraction algorithm | generative model |
| Unit | page | answer block | verifiable fact + its source |
| Success | impressions, clicks | snippet ownership | **our name appears in the answer** |

A generative model does not rank. When it composes an answer it asks which
claim it can attach to which source. So GEO reduces to one requirement Sections
1–10 never enforce: **every claim must be traceable to a source a crawler can
follow.**

### 11.1 The failure this section exists to prevent

Between 2026-05-17 and 2026-08-05, nine consecutive posts shipped with **zero
outbound citation links in the body**. Sourcing had not gotten worse — those
posts carry 4–11 entries each in `primary_sources`, more than the earlier posts
that did link out. The research was done; only the rendering disappeared.

The failure mode is specific: sources written as **bare domains in prose**.

```
Bad:   Anthropic (platform.claude.com), OpenAI (developers.openai.com)
Good:  [Anthropic pricing](https://platform.claude.com/docs/…),
       [OpenAI pricing](https://developers.openai.com/api/docs/pricing)
```

To a crawler these are not the same thing. The first is a string; the second is
an edge in the citation graph. No rule in Sections 1–10 caught the difference
for nine posts running, which is why Section 12 is enforced by hook.

### 11.2 Scope

Section 11–13 govern **post-level** GEO — what every post must carry. Site-level
GEO infrastructure (Dataset/Organization/DataCatalog JSON-LD, entity `sameAs`,
logo assets) is one-off build work and is specified separately in
`_plans/2026-08-05-geo-implementation-spec.md`, not here.

---

## Section 12 — Primary Source Citation Standard

### 12.1 Inline citation (Rule D1 — ERROR)

Every post must contain **at least one outbound markdown link to a primary
source** in the body, placed where the claim is made — normally the Methodology
section.

This is not a request to dump all 11 sources into the prose. The full list is
rendered from `primary_sources` at the layout level; Section 12 requires that
the *load-bearing* claims carry their source inline. A generative model weighs
the proximity of a claim to its evidence, so a link next to the number is a
stronger signal than the same link in a footer list.

- Bare domains in prose do not count
- Links to jsonhouse.com do not count (that is Section 5, internal linking)
- Autolinks `<https://…>` count; markdown links `[text](https://…)` count

### 12.2 Source depth (Rule D2 — ERROR)

The paired `_data/YYYY-MM-DD-{slug}.json` must carry **at least 3 entries** in
`primary_sources`, each with both `title` and `url`.

These entries are not bookkeeping. They become the `citation` array of the post's
`Dataset` JSON-LD, which is how the claim-to-evidence mapping reaches a model
that never parses our prose. Thin sourcing is thin evidence.

### 12.3 Dataset discoverability (Rule D4 — ERROR)

The body must link its own dataset:

```
> **Raw data**: [data/{slug}.json](https://www.jsonhouse.com/data/{slug}.json) —
> machine-readable structured data for AI crawlers and citation.
```

Recommended placement: immediately after the first comparison table.

### 12.4 Evidence calibration

Restating Post Writing Principle 7 because it is a citation rule, not only a
style rule: state published numbers as published, unpublished as unpublished,
inferred as inferred. A model that cites a fabricated precision once will not
cite the source again. **"Not published" is itself a citable finding.**

---

## Section 13 — Dataset Schema Validation

### 13.1 Required fields (Rule D5 — ERROR)

All 12 fields defined in `CLAUDE.md` must be present in the paired data file:

```
schema_version  slug       title       description
data_updated    source_post category    cluster
format          key_facts  faq_summary primary_sources
```

Missing fields are an ERROR because the site-level `Dataset` JSON-LD reads them
directly. A missing field does not degrade the schema — it produces an invalid
one, and an invalid JSON-LD block is discarded whole.

### 13.2 Freshness agreement (Rule D5 — ERROR)

Front matter `data_updated` and the data file's `data_updated` must be identical.
Freshness is a primary citation signal for time-sensitive data; two copies
disagreeing means at least one is lying about it.

### 13.3 Fact granularity (Rule D3 — WARN)

`key_facts` should hold **5–10 entries**. These are the units a model can lift
and attribute individually — too few and there is nothing to cite, too many and
they stop being the post's key facts.

### 13.4 What is deliberately NOT declared

**Never add a `license` field** to data files, JSON-LD, or `llms.txt`.

This is an intentional awareness-first decision (`CLAUDE.md`, 2026-07-09). It
matters here because schema.org lists `license` as a *recommended* field for
`Dataset`, so implementing schema naturally surfaces the temptation to add it.
Omitting it leaves the schema valid. Do not re-propose this unless 기웅 changes
the policy.
