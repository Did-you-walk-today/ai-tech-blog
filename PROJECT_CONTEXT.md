# PROJECT_CONTEXT.md
# AI Tech Resource Blog — Claude Project System Context
# Upload this file to your Claude Project. Claude will read it in every conversation.

---

## WHO YOU ARE TALKING TO

**Project owner**: 기웅 (Giwung)
**Goal**: Build and operate an AI-focused technical blog that generates passive income through AdSense, Gumroad digital products, and affiliate marketing.
**Current stage**: Phase 1 — Setting up GitHub Pages + Jekyll + Claude Code automation pipeline.

---

## BLOG OVERVIEW

| Field | Value |
|-------|-------|
| Platform | GitHub Pages (Jekyll) |
| Domain | Custom domain required (not github.io) |
| Target audience | AI power users, developers, engineers |
| Language | English (global audience) |
| Core value | "Structured data you can actually USE" |
| Monetization | AdSense → Gumroad → Affiliate marketing → API billing |

---

## THREE-PHASE ROADMAP

### Phase 1 (NOW — months 1–3): GitHub Pages + AI layer
**Status**: In progress
- Build and launch blog on GitHub Pages with Jekyll
- Publish 20+ posts (3x/week via automation)
- Add AI agent layer: llms.txt + /api/posts.json + JSON-LD schemas
- Apply for Google AdSense
- Run Claude Code pipeline Phase 1–5

**Do NOT do yet**: Headless CMS, Vector DB, API billing — all premature.

### Phase 2 (months 4–8): Cloudflare Workers + traffic scaling
- API gateway via Cloudflare Workers
- Edge caching via Cloudflare KV
- Rate limiting for bot/agent traffic
- Start affiliate marketing (Claude Pro, Cursor referrals)
- Launch first Gumroad product (prompt library PDF $9–29)

### Phase 3 (months 8+): Agent hub transformation
- Supabase (PostgreSQL + pgvector) for semantic search
- Knowledge Graph metadata between posts
- Semantic chunking (200–400 chars per chunk)
- API billing model for agent queries
- Data licensing exploration

---

## AUTOMATION PIPELINE (8 Phases)

The blog runs on a Claude Code automation pipeline. Human review (기웅) only happens at Phase 5.

| Phase | Name | Agent | Frequency |
|-------|------|-------|-----------|
| 1 | Content Discovery | Agent A | Daily 09:00 UTC |
| 2 | Data Collection | Agent A | After Phase 1 |
| 3 | Draft Generation | Agent B | After Phase 2 |
| 4 | Technical Validation | Agent B | After Phase 3 |
| 5 | Human Review | 기웅 (manual) | Daily, 5–15 min |
| 6 | Publishing | Agent C | After PR merge |
| 7 | Data Freshness | Agent C | Weekly Monday |
| 8 | SEO Tracking | Agent C | Weekly Monday |

**Agent setup**: Claude Code (claude-sonnet-4) + bash orchestrator
**Execution environment**: GitHub Actions (free tier, 2000 min/month)
**Backup**: Cloudflare Workers for Phase 8 SEO tracking

---

## CONTENT STRUCTURE

### 7 Post Formats
- **FORMAT A**: Tool comparison (JSON data block required)
- **FORMAT B**: Prompt library (copy-ready prompts)
- **FORMAT C**: Technical guide (step-by-step with code)
- **FORMAT D**: Structured data resource (tables + JSON, updated monthly)
- **FORMAT E**: Workflow/template (downloadable)
- **FORMAT F**: Benchmark report (tested data, methodology transparent)
- **FORMAT G**: Weekly AI digest (fully automated)

### 6 Content Categories
- **CAT1**: AI Models & Intelligence (LLM comparisons, benchmarks) — highest SEO value
- **CAT2**: AI Developer Tools (Cursor, Copilot, APIs, Claude Code) — highest CPC
- **CAT3**: Prompt Engineering (libraries, templates, patterns)
- **CAT4**: AI Productivity & Workflows (automation templates)
- **CAT5**: AI Data & Statistics (adoption data, market research)
- **CAT6**: AI Safety & Ethics (practical hallucination prevention)

### 3 Topic Clusters (build these first)
1. **CLUSTER_LLM**: Pillar "Best LLM 2026" + support posts (comparisons, pricing DB, coding benchmark)
2. **CLUSTER_DEVTOOLS**: Pillar "Best AI Coding Tools 2026" + support posts (Claude Code, Cursor vs Copilot, MCP)
3. **CLUSTER_PROMPTS**: Pillar "Ultimate AI Prompt Library 2026" + support posts (by job role, system prompts)

---

## SEO RULES (mandatory for every post)

1. **Title**: max 60 chars, include year "2026", primary keyword in first 5 words
2. **Meta description**: 150–160 chars, directly answer search intent
3. **First paragraph**: answer the main question within 150 words
4. **TL;DR**: 3–5 bullets (Featured Snippet targeting)
5. **Structured data**: at least 1 JSON block OR comparison table per post — HARD REQUIREMENT
6. **FAQ section**: min 3 questions (People Also Ask research)
7. **Internal links**: 2–3 links within same topic cluster
8. **Word count**: min 600 words (excluding code/data blocks)
9. **data_updated field**: always present, auto-updated by Phase 7

### Hard reject conditions (auto-regenerate if triggered)
- Title > 60 chars
- No year in title
- Meta description outside 140–165 chars
- No JSON block or comparison table
- Word count < 600 (excl. data blocks)
- Pricing data > 7 days old
- Code syntax errors
- Any quality score < 7.0

---

## AI AGENT OPTIMIZATION LAYER

Three files that make the blog readable by AI agents (add to Jekyll blog immediately):

### 1. /llms.txt (root)
Purpose: Site guide for AI agents (like robots.txt but for LLMs)
```
# AI Tech Resource Blog
> Structured AI/LLM data resource for developers and power users.

## Data
- [All posts JSON](/api/posts.json): Full structured post index
- [LLM Pricing DB](/api/pricing.json): Updated weekly
- [Benchmark Data](/api/benchmarks.json): Tested results only

## Categories
- AI Models: /category/ai-models/
- Developer Tools: /category/ai-developer-tools/
- Prompts: /category/prompt-engineering/

## Update Frequency
- Posts: 3x/week | Pricing: weekly | Benchmarks: monthly
```

### 2. /api/posts.json (Jekyll auto-generated)
Purpose: Structured index of all posts for agent consumption
```json
[{
  "title": "Claude vs GPT-4o — 2026 Complete Guide",
  "url": "/posts/claude-vs-gpt4o-2026",
  "date": "2026-03-26",
  "data_updated": "2026-03-26",
  "category": "CAT1",
  "tags": ["claude", "gpt-4o", "llm-comparison", "2026"],
  "schema_type": "Article"
}]
```

### 3. JSON-LD schema (every post)
Purpose: Structured data for Google and AI agents to extract
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[title]",
  "datePublished": "[date]",
  "dateModified": "[data_updated]"
}
```

---

## DATABASE STRATEGY

**Current**: No DB needed — GitHub Pages static JSON is sufficient.

| Phase | Storage | Use case | Cost |
|-------|---------|----------|------|
| Phase 1 | Static JSON files | Post index, structured data | $0 |
| Phase 2 | Cloudflare KV | Edge caching, rate limit | $0–5/mo |
| Phase 3 | Supabase (pgvector) | Semantic search, Knowledge Graph | $0–25/mo |
| Future | Pinecone/Milvus | Large-scale RAG at scale | $70+/mo |

**Do NOT introduce Vector DB until**: 200+ posts AND 10,000+ monthly visitors AND agent API business.

---

## MONETIZATION STRATEGY

| Timeline | Method | Target | Est. Monthly |
|----------|--------|--------|-------------|
| Month 1–3 | AdSense (CPC $1–5) | Human readers | $0 → after approval |
| Month 3–4 | Gumroad PDF ($9–29) | Human readers | $50–300 |
| Month 4–8 | Affiliate marketing | Human + agent referral | $100–500 |
| Month 8+ | API billing | AI agents | TBD by traffic |
| Month 8+ | Data licensing | AI companies | Per deal |

**Key insight**: AI agents don't click ads. Human reader monetization (AdSense, Gumroad) is the primary revenue for Phase 1–2. Build agent-readable data layer NOW to be ready for Phase 3 revenue.

---

## MONTHLY BUDGET

| Item | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| Claude Pro | $20 | $20 | $20 |
| Custom domain | $1 | $1 | $1 |
| Claude API credits | $10–20 | $15–25 | $20–40 |
| GitHub Actions | Free | Free | Free |
| Cloudflare Workers/KV | Free | $0–5 | $0–10 |
| Supabase | — | — | $0–25 |
| **Total** | **$31–41** | **$36–51** | **$41–96** |

**Break-even target**: 3,000 monthly visitors → $30–60 AdSense revenue → covers Phase 1 costs.

---

## IMMEDIATE ACTION CHECKLIST (This Week)

- [ ] Purchase custom domain + connect to GitHub Pages
- [ ] Configure Jekyll: jekyll-sitemap, jekyll-seo-tag plugins
- [ ] Create /llms.txt and push to repo
- [ ] Create /api/posts.json Jekyll generator file
- [ ] Add JSON-LD auto-injection to _layouts/post.html
- [ ] Verify Google Search Console + submit sitemap
- [ ] Create GitHub Actions workflow for daily cron (Agent A)
- [ ] Write CLAUDE.md including reference to SEO_GUIDE.md

---

## HOW TO USE THIS PROJECT

When you start a conversation in this Claude Project, Claude already knows all of the above context. You can say things like:

- "Run Phase 1 today" → Claude starts discovery
- "Review this draft" → Claude validates against SEO rules
- "What should we write about this week?" → Claude checks sources and scores topics
- "Update the pricing table in [post]" → Claude re-fetches and updates
- "How is our SEO performing?" → Claude analyzes Phase 8 report

---

## KEY FILES IN THIS PROJECT

| File | Purpose |
|------|---------|
| `PROJECT_CONTEXT.md` (this file) | Master context — always loaded |
| `PIPELINE_PROMPT.md` | Full 8-phase execution instructions for Claude Code |
| `SEO_GUIDE.md` | Machine-readable SEO enforcement rules |
| `SEO_가이드_한국어.docx` | Human-readable SEO guide (Korean) |
| `AI_Tech_Blog_마스터기획서.docx` | Master plan (Korean, for reference) |

---

*Last updated: 2026-03-26*
*Version: 1.0*
