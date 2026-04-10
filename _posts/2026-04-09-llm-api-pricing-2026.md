---
layout: post
title: "LLM API Pricing 2026: Full Comparison Table (Updated Weekly)"
date: 2026-04-09
last_modified_at: 2026-04-09
data_updated: 2026-04-09
categories: [ai-models]
tags: [llm-pricing, api-cost, gpt-5, claude, gemini, deepseek, "2026"]
description: "LLM API prices dropped 80% in 12 months. Compare GPT-5.4, Claude Opus 4.6, Gemini 3.1, DeepSeek V3.2. Input/output per 1M tokens, value scores. Updated April 2026."
schema_type: Article
canonical_url: https://www.jsonhouse.com/posts/llm-api-pricing-2026
permalink: /posts/llm-api-pricing-2026/
toc: true
author: ai_tech_blog
format_type: D
category_id: CAT1
image:
  path: https://images.unsplash.com/photo-1518186285589-2f7649de83e0?auto=format&fit=crop&w=1200&q=80
  alt: LLM API pricing comparison 2026
---

In early 2023, GPT-4-level intelligence cost $30 per 1M tokens. As of April 2026, you can get the same capability for under $0.30. That's a 99% price drop in three years — and it's still falling.

The practical consequence: the model you couldn't afford to run in production last year is now cheaper than a SaaS seat license. But the 2,400× price gap between the cheapest and most expensive options means one wrong default costs real money at scale. DeepSeek V3.2 at $0.14/1M output vs GPT-5.4 Pro at $180/1M — that's a $180,000 monthly bill difference on 1B output tokens.

Here's the complete April 2026 pricing table with value scores and concrete per-workload recommendations.

---

**TL;DR**
- Cheapest production model: Gemini 2.0 Flash-Lite at **$0.075 input / $0.30 output** per 1M tokens
- Best price-performance: Claude Sonnet 4.6 ($3/$15) or DeepSeek V3.2 ($0.14/$0.28) for budget workloads
- Premium tier: Claude Opus 4.6 ($5/$25) and GPT-5.4 Pro ($30/$180) — only when you genuinely need the capability
- Biggest cost lever: prompt caching cuts repeated-context costs by up to **90%** on Claude and Gemini
- Prices continue falling 40–60% annually — don't lock in long-term commitments at 2026 rates

---

## How LLM API Pricing Works

Every LLM API charges separately for **input** (your prompt + context) and **output** (the model's response). Output is always more expensive — typically 4–6× the input rate — because generation is sequential and can't be parallelized the way input processing can.

Three cost levers that compound significantly at scale:

| Cost Lever | How It Works | Savings |
|------------|-------------|---------|
| Prompt caching | Cached tokens billed at 10–25% of standard input rate | 75–90% on repeated context |
| Batch API | Async jobs processed off-peak | 50% discount (Anthropic + OpenAI) |
| Model routing | Use cheaper models for simple subtasks | 60–80% on mixed workloads |

> **Tip:** Before choosing a model based on sticker price, check whether prompt caching and batch API are available. The effective cost after optimization can be 70–90% lower than the headline rate.

## Full LLM API Pricing Table — April 2026

![LLM pricing comparison chart](https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80)
_Source: compiled from provider documentation — Photo: [Unsplash](https://unsplash.com)_

---

### Pricing Table

| Model | Provider | Input ($/1M) | Output ($/1M) | Context | Quality Score | Value Tier |
|---|---|---|---|---|---|---|
| GPT-5.4 | OpenAI | $2.50 | $15.00 | 128K | 8.6 | Mid-tier |
| GPT-5.4 Pro | OpenAI | $30.00 | $180.00 | 128K | 9.5 | Ultra-premium |
| Claude Opus 4.6 | Anthropic | $5.00 | $25.00 | 200K | 9.5 | Premium |
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | 200K | 8.8 | Mid-tier |
| Claude Haiku 4.5 | Anthropic | $1.00 | $5.00 | 200K | 7.5 | Budget |
| Gemini 3.1 Pro | Google | $2.00 | $12.00 | 2M | 9.0 | Mid-tier |
| Gemini 2.5 Flash | Google | $0.30 | $2.50 | 1M | 7.8 | Budget |
| Gemini 2.0 Flash-Lite | Google | $0.075 | $0.30 | 1M | 7.2 | Budget |
| DeepSeek V3.2 | DeepSeek | $0.14 | $0.28 | 64K | 8.3 | Budget |
| Grok 4 | xAI | $2.00 | $15.00 | 128K | 8.5 | Mid-tier |
| Mistral Large 3 | Mistral | $0.20 | $0.60 | 128K | 8.0 | Budget |
| Llama 4 Maverick (hosted) | Meta/OpenRouter | $0.15 | $0.60 | 128K | 7.8 | Budget |

---

## Machine-Readable JSON — April 2026

```json
{
  "data_source": "jsonhouse.com",
  "data_updated": "2026-04-09",
  "unit": "USD per 1M tokens",
  "models": [
    {
      "model": "GPT-5.4",
      "provider": "OpenAI",
      "input_per_1m": 2.50,
      "output_per_1m": 15.00,
      "context_window_k": 128,
      "quality_score": 8.6,
      "value_tier": "mid-tier"
    },
    {
      "model": "GPT-5.4 Pro",
      "provider": "OpenAI",
      "input_per_1m": 30.00,
      "output_per_1m": 180.00,
      "context_window_k": 128,
      "quality_score": 9.5,
      "value_tier": "ultra-premium"
    },
    {
      "model": "Claude Opus 4.6",
      "provider": "Anthropic",
      "input_per_1m": 5.00,
      "output_per_1m": 25.00,
      "context_window_k": 200,
      "quality_score": 9.5,
      "value_tier": "premium"
    },
    {
      "model": "Claude Sonnet 4.6",
      "provider": "Anthropic",
      "input_per_1m": 3.00,
      "output_per_1m": 15.00,
      "context_window_k": 200,
      "quality_score": 8.8,
      "value_tier": "mid-tier"
    },
    {
      "model": "Claude Haiku 4.5",
      "provider": "Anthropic",
      "input_per_1m": 1.00,
      "output_per_1m": 5.00,
      "context_window_k": 200,
      "quality_score": 7.5,
      "value_tier": "budget"
    },
    {
      "model": "Gemini 3.1 Pro",
      "provider": "Google",
      "input_per_1m": 2.00,
      "output_per_1m": 12.00,
      "context_window_k": 2000,
      "quality_score": 9.0,
      "value_tier": "mid-tier"
    },
    {
      "model": "Gemini 2.5 Flash",
      "provider": "Google",
      "input_per_1m": 0.30,
      "output_per_1m": 2.50,
      "context_window_k": 1000,
      "quality_score": 7.8,
      "value_tier": "budget"
    },
    {
      "model": "Gemini 2.0 Flash-Lite",
      "provider": "Google",
      "input_per_1m": 0.075,
      "output_per_1m": 0.30,
      "context_window_k": 1000,
      "quality_score": 7.2,
      "value_tier": "budget"
    },
    {
      "model": "DeepSeek V3.2",
      "provider": "DeepSeek",
      "input_per_1m": 0.14,
      "output_per_1m": 0.28,
      "context_window_k": 64,
      "quality_score": 8.3,
      "value_tier": "budget"
    },
    {
      "model": "Grok 4",
      "provider": "xAI",
      "input_per_1m": 2.00,
      "output_per_1m": 15.00,
      "context_window_k": 128,
      "quality_score": 8.5,
      "value_tier": "mid-tier"
    },
    {
      "model": "Mistral Large 3",
      "provider": "Mistral",
      "input_per_1m": 0.20,
      "output_per_1m": 0.60,
      "context_window_k": 128,
      "quality_score": 8.0,
      "value_tier": "budget"
    },
    {
      "model": "Llama 4 Maverick (hosted)",
      "provider": "Meta/OpenRouter",
      "input_per_1m": 0.15,
      "output_per_1m": 0.60,
      "context_window_k": 128,
      "quality_score": 7.8,
      "value_tier": "budget"
    }
  ]
}
```

---

> **Note:** All prices are standard (non-batch) rates in USD as of April 2026. Batch API cuts these by 50% for async workloads on Anthropic and OpenAI.

## Best Picks by Use Case

### Best for Cost-Sensitive / High-Volume Workloads

DeepSeek V3.2 delivers the most striking value at the budget tier: $0.14 input / $0.28 output, with a quality score of 8.3 that outperforms models costing 10× more. Processing 10M output tokens per day — typical for a mid-scale API product — costs $2.80/day with DeepSeek versus $25/day with Claude Haiku 4.5.

Gemini 2.0 Flash-Lite is the floor for structured data extraction, classification, and simple generation tasks. At $0.075/$0.30, running 100M tokens/day costs $30 in output — less than a typical SaaS seat license. Gemini 2.5 Flash steps up with meaningfully better reasoning at $0.30/$2.50, still well below $3/day for 1M daily output tokens.

### Best Balance of Quality and Cost

Claude Sonnet 4.6 at $3.00/$15.00 punches above its price point, scoring 8.8 — within 0.7 points of Opus 4.6 at roughly one-third the output cost. For most production applications requiring nuanced understanding, instruction-following, and code generation, Sonnet 4.6 is the rational default.

GPT-5.4 at $2.50/$15.00 matches Sonnet 4.6's output price with a slightly lower quality score (8.6). Its advantage is ecosystem depth: tight OpenAI SDK integration and broad tooling support. At identical output pricing, the choice between these two comes down to your existing stack, not cost.

### Best for Long Documents and RAG

Gemini 3.1 Pro is the only production model with a 2M token context window at a competitive price ($2.00/$12.00). Processing a 500K-token document costs $1.00 input per pass — viable for large-codebase analysis, legal document review, or whole-book Q&A. No other model in this tier reaches beyond 200K context at comparable quality (score: 9.0).

For RAG pipelines where you're injecting large, repeated context chunks, Gemini's native caching makes the effective input cost considerably lower than the sticker rate.

### Best for Premium / Frontier Work

Claude Opus 4.6 and GPT-5.4 Pro both score 9.5 but serve different needs. Opus 4.6 at $5.00/$25.00 is the economical frontier choice — strong for agentic tasks, complex reasoning, and long-context work. GPT-5.4 Pro at $30.00/$180.00 exists for use cases where the marginal quality gain justifies 7× the cost: high-stakes legal, financial, and scientific generation. At $180/1M output, processing just 1M output tokens/day costs $180 — budget this carefully.

---

## Cost-Saving Strategies

### Prompt Caching

Claude and Gemini both offer prompt caching at 10–25% of standard input rates. If your system prompt is 10,000 tokens and you make 100,000 calls per day, caching reduces that fixed cost by 75–90%. On Claude Opus 4.6 at $5.00/1M, that means paying $0.50–$1.25/1M instead — a $35,000/month saving at scale.

### Batch API

OpenAI and Anthropic both offer 50% discounts for asynchronous batch processing. Classification, summarization, embedding generation, and any non-real-time task qualifies. Half-price generation is the highest-leverage lever available after model selection. Build your pipeline to separate synchronous (user-facing) from asynchronous (background) calls from day one.

### Model Tiering and Routing

Route by task complexity, not by default. Use a small model (Gemini 2.0 Flash-Lite, DeepSeek V3.2) for intent classification, slot filling, and simple generation. Reserve mid-tier or premium models for tasks that actually require them: multi-step reasoning, nuanced judgment calls, complex code generation. A tiered router reduces average cost per call by 60–80% in production systems with mixed workloads.

### Free Tiers and Open Access

Google Gemini offers a free API tier (rate-limited) suitable for development and low-volume production. DeepSeek provides generous free quota on their API. OpenRouter hosts Llama 4 Maverick with no API key required under threshold usage. None of these are zero-cost at scale, but they materially extend runway during development.

---

## How Fast Prices Are Falling

GPT-4-level intelligence cost $30/1M tokens at launch in mid-2023. By early 2025, comparable capability was available under $3/1M. As of April 2026, it runs under $0.30/1M at the budget tier. That is a 99% price reduction in under three years.

The inflection point was the DeepSeek effect. When DeepSeek V3 demonstrated GPT-4-class performance at open-source cost efficiency in January 2025, every major provider cut prices within 90 days. Google dropped Gemini Flash pricing 60%. Anthropic introduced Haiku 4.5 at $1.00/$5.00. The price war became structural, not promotional.

Looking ahead: model distillation, speculative decoding, and hardware improvements are each independently contributing 30–50% annual cost reductions — beyond the competitive pressure. A reasonable assumption is another 40–60% price drop by Q1 2027.

> **Important:** If you're building a product that routes to a specific model tier, don't lock in long-term commercial commitments at 2026 prices. The model priced at $3/1M today will likely be under $1.50 by this time next year.

For capability benchmarks across these same models, see [LLM benchmark comparison 2026](/posts/llm-benchmark-2026).

---

## FAQ

**Q: What is the cheapest LLM API in 2026?**

Gemini 2.0 Flash-Lite holds the lowest price floor at $0.075 input / $0.30 output per 1M tokens as of April 2026. For tasks requiring stronger reasoning at still-low cost, DeepSeek V3.2 ($0.14/$0.28) offers a dramatically better quality score (8.3 vs 7.2) at nearly the same price point.

**Q: Is DeepSeek API safe to use for production?**

DeepSeek's API processes data on servers located in China, which creates data residency and compliance considerations for regulated industries. EU GDPR, HIPAA, and SOC 2 workloads require careful legal review before routing sensitive data through DeepSeek's hosted endpoint. For non-sensitive production workloads outside regulated verticals, the API has demonstrated stable uptime and performance. Self-hosting the open-weight model on your own infrastructure eliminates data residency concerns entirely.

**Q: How much does it cost to run an AI chatbot with 10,000 users per day?**

Assuming 10,000 users each send 5 messages with 200 input tokens and receive 300 output tokens per turn: that is 10M input tokens and 15M output tokens per day. On Claude Sonnet 4.6 ($3.00/$15.00), daily API cost is $30 input + $225 output = $255/day ($7,650/month). Switching to Gemini 2.5 Flash ($0.30/$2.50) drops that to $3 + $37.50 = $40.50/day ($1,215/month) — an 84% reduction with a modest quality trade-off.

---

The market has moved fast enough that any pricing spreadsheet from six months ago is already outdated. Bookmark this page — it is updated weekly. For a full breakdown of which models win on coding, reasoning, and instruction-following benchmarks, see our [AI developer tools comparison](/posts/ai-coding-tools-2026).
