# jsonhouse Master Content Template Set

> **Version**: 1.0 (2026-05-20)
> **Purpose**: Five-channel optimized content templates that go beyond standard AEO+SEO
> **Target channels**: Google SERP / Google AI Overview / ChatGPT / Claude / Perplexity
> **Primary consumer**: Claude Code (Agent B) producing draft posts

---

## How This Template Set Works

### 3-Layer architecture

```
┌─────────────────────────────────────────────────────────┐
│ Layer 3: _layouts/post.html (auto-injection)            │
│ - JSON-LD Schema Stacking (Article + format-specific)   │
│ - Open Graph / Twitter Card                             │
│ - Canonical / sitemap auto-registration                 │
├─────────────────────────────────────────────────────────┤
│ Layer 2: Format-specific branches (FORMAT A–G)          │
│ - Format-unique sections (comparison tables, prompts,   │
│   HowTo steps, datasets, etc.)                          │
│ - Format-specific schemas (Product/HowTo/Dataset/FAQ)   │
├─────────────────────────────────────────────────────────┤
│ Layer 1: Universal skeleton                             │
│ - Front matter (metadata)                               │
│ - Hook + TL;DR + Quick Answer Block                     │
│ - Body (synthesis style 5-stage)                        │
│ - FAQ + Sources                                         │
└─────────────────────────────────────────────────────────┘
```

Agent B (or human author) fills Layer 1+2 only. Layer 3 is handled automatically by Jekyll.

---

## Format Selection Matrix

| Post topic example | Choose format | Primary engine target |
|---|---|---|
| "Claude vs GPT-5 Comparison 2026" | FORMAT A | Perplexity + Claude |
| "50 Cursor System Prompts" | FORMAT B | ChatGPT |
| "How to Build a Claude Code MCP Server" | FORMAT C | Claude |
| "LLM API Pricing Database 2026" (weekly) | FORMAT D | Perplexity |
| "AI Marketing Automation Workflow (n8n)" | FORMAT E | ChatGPT + Gemini |
| "Claude 3.7 vs GPT-5 Coding Benchmark (tested)" | FORMAT F | Perplexity + Claude |
| "This Week in AI #N" (automated) | FORMAT G | ChatGPT |

---

## Universal GEO Citation Triggers (in every template)

Each template has these 6 triggers pre-wired. Authors only fill the blanks:

| Trigger | Effect | Location in template |
|---|---|---|
| Quote block (`>`) | +41% citation rate | "Key Insight" sections |
| Statistics + source | +40% citation rate | "By the Numbers" sections |
| External authority citation | +40% citation rate | "What [Source] Says" sections |
| Comparison table | #1 for Featured Snippets | Format-specific core table |
| Definition Lead | Captures first-30% extraction | Right after Hook |
| Quick Answer Block | Maximum extractability | Right after TL;DR |

---

## Usage Workflow

### For Agent B (Claude Code)

```bash
# Step 1: Copy the format template into _posts/
cp _templates/_01_FORMAT_A_comparison.md _posts/YYYY-MM-DD-slug.md

# Step 2: Replace [PLACEHOLDER] tokens with actual content
# DO NOT modify section structure, heading order, or schema field names.
# DO NOT remove HTML comments — they guide the structure.

# Step 3: Verify all [PLACEHOLDER] tokens are replaced
grep -n "\[" _posts/YYYY-MM-DD-slug.md  # should return no leftover placeholders

# Step 4: Submit for Phase 4 validation
```

### For human review (기웅, Phase 5)

1. Confirm front matter completeness (especially `data_updated`, `schema_types`)
2. Spot-check 1-2 statistics for source accuracy
3. Verify FAQ answers are 2-3 sentences (not paragraphs)
4. Approve or request specific fixes

---

## File Manifest

| File | Purpose |
|---|---|
| `_00_MASTER_GUIDE.md` | This file — operating guide |
| `_01_FORMAT_A_comparison.md` | Tool comparison template |
| `_02_FORMAT_B_prompt_library.md` | Prompt library template |
| `_03_FORMAT_C_technical_guide.md` | Technical guide template |
| `_04_FORMAT_D_data_resource.md` | Structured data resource template |
| `_05_FORMAT_E_workflow.md` | Workflow / downloadable template |
| `_06_FORMAT_F_benchmark.md` | Benchmark report template |
| `_07_FORMAT_G_weekly_digest.md` | Weekly AI digest template |
| `_08_layout_post_html.liquid` | Auto-injecting JSON-LD layout |
| `_09_plugin_schema_extractors.rb` | FAQ/HowTo extractor plugin |

---

## Critical Rules for Agent B

**DO**:
- Copy the template file first, then fill placeholders
- Preserve all HTML comments (they guide structure during edits)
- Keep section order exactly as templated
- Include the `data_updated` field on every post
- Fill every `[PLACEHOLDER]` — never leave any in the published file

**DO NOT**:
- Reorder sections
- Skip the Methodology / Sources sections (these are GEO trust signals)
- Replace markdown tables with prose
- Use keyword stuffing — GEO penalizes -10% for repetition
- Add formatting beyond what's templated (excess headers/bullets hurt citation rates)
