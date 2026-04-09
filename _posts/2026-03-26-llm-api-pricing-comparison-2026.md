---
layout: post
title: "LLM API Pricing 2026: Full Comparison Table"
date: 2026-03-26 09:00:00 +0000
categories: [ai-data]
tags: [llm-pricing, api-cost, gpt-4o, claude, gemini, "2026"]
description: "LLM API pricing comparison 2026: 30+ models from OpenAI, Anthropic, Google, xAI, DeepSeek and more. Updated monthly with input/output costs per 1M tokens."
canonical_url: https://www.jsonhouse.com/posts/llm-api-pricing-comparison-2026
permalink: /posts/llm-api-pricing-comparison-2026/
data_updated: 2026-03-26
toc: true
author: ai_tech_blog
schema_type: Dataset
format_type: D
category_id: CAT5
quality_score: auto
sources:
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://openai.com/api/pricing/
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://mistral.ai/pricing
  - https://api-docs.deepseek.com/quick_start/pricing
---

## LLM API Pricing Comparison 2026: Which Model Costs Least for Your Use Case?

As of March 2026, LLM API pricing spans four orders of magnitude — from $0.02/1M tokens for small open-source models to $25.00/1M tokens for top-tier flagship outputs. The cheapest model for production is **Gemini 2.5 Flash-Lite** at $0.10 input / $0.40 output per million tokens, while **GPT-4o mini** holds the crown among proprietary mid-range budget models at $0.15 input / $0.60 output. For reasoning tasks, **o4-mini** undercuts competitors significantly at $1.10 input / $4.40 output. If you need maximum context window with strong performance, **Grok 4** offers 2M context at $3.00 / $15.00. Prices below are per 1M tokens at standard (non-batch) API rates.

---

## TL;DR

- **Cheapest proprietary model**: Gemini 2.5 Flash-Lite ($0.10 / $0.40 per 1M tokens), followed by Mistral Small 3.1 ($0.10 / $0.30)
- **Best budget reasoning**: o4-mini ($1.10 / $4.40) — significantly cheaper than o3 or GPT-5 for structured tasks
- **Best context-per-dollar**: Grok 4 at 2M tokens; Gemini 2.5 Flash at 1M for $0.30 / $2.50
- **Batch API discounts**: All major providers (Anthropic, OpenAI, Google) offer 50% off for async batch jobs; DeepSeek cache reads are 90% cheaper
- **Open-source hosted**: Llama 3.2 3B on DeepInfra costs just $0.02 / $0.02 — suitable for high-volume classification or extraction pipelines

---

## Quick Comparison: Flagship Models

| Model | Provider | Input $/1M | Output $/1M | Context Window |
|---|---|---|---|---|
| Claude Opus 4.6 | Anthropic | $5.00 | $25.00 | 1M |
| GPT-5.4 | OpenAI | $2.50 | $15.00 | 1.05M |
| GPT-5 | OpenAI | $1.25 | $10.00 | 1M |
| Gemini 3.1 Pro | Google | $2.00 | $12.00 | 1M |
| Grok 4 | xAI | $3.00 | $15.00 | 2M |
| o3 | OpenAI | $2.00 | $8.00 | 200K |

> Note: Claude Opus 4.6 is the most expensive output model in this tier. GPT-5 offers the best input cost among flagship models at $1.25/1M. Grok 4 is the only model with a 2M context window in this category.

---

## Full LLM API Pricing Table 2026

### Flagship Tier

| Model | Provider | Input $/1M | Output $/1M | Context |
|---|---|---|---|---|
| Claude Opus 4.6 | Anthropic | $5.00 | $25.00 | 1M |
| GPT-5.4 | OpenAI | $2.50 | $15.00 | 1.05M |
| GPT-5 | OpenAI | $1.25 | $10.00 | 1M |
| Gemini 3.1 Pro | Google | $2.00 | $12.00 | 1M |
| Grok 4 | xAI | $3.00 | $15.00 | 2M |
| o3 | OpenAI | $2.00 | $8.00 | 200K |

### Mid-Range Tier

| Model | Provider | Input $/1M | Output $/1M | Context |
|---|---|---|---|---|
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | 1M |
| GPT-4.1 | OpenAI | $2.00 | $8.00 | 128K |
| GPT-4o | OpenAI | $2.50 | $10.00 | 128K |
| o4-mini | OpenAI | $1.10 | $4.40 | 200K |
| Gemini 2.5 Pro | Google | $1.25 | $10.00 | 1M |
| Gemini 3 Flash | Google | $0.50 | $3.00 | 1M |
| Mistral Large 3 | Mistral | $2.00 | $6.00 | 128K |
| DeepSeek-R1 | DeepSeek | $0.55 | $2.19 | 128K |
| Qwen3-Max | Alibaba | $0.78 | $3.90 | 128K |

### Budget Tier

| Model | Provider | Input $/1M | Output $/1M | Context |
|---|---|---|---|---|
| Claude Haiku 4.5 | Anthropic | $1.00 | $5.00 | 200K |
| GPT-4o mini | OpenAI | $0.15 | $0.60 | 128K |
| Gemini 2.5 Flash | Google | $0.30 | $2.50 | 1M |
| Gemini 2.5 Flash-Lite | Google | $0.10 | $0.40 | 1M |
| Grok 3 Mini | xAI | $0.30 | $0.50 | 131K |
| Mistral Small 3.1 | Mistral | $0.10 | $0.30 | 128K |
| DeepSeek-V3.2 | DeepSeek | $0.28 | $0.42 | 128K |
| DeepSeek-V4 | DeepSeek | $0.30 | $0.50 | 128K |
| Qwen3.5-Plus | Alibaba | $0.26 | $1.56 | 128K |

### Open-Source Hosted (Inference Providers)

| Model | Provider | Input $/1M | Output $/1M |
|---|---|---|---|
| Llama 4 Maverick | Together AI | $0.27 | $0.85 |
| Llama 4 Scout | Groq | $0.11 | $0.34 |
| Llama 3.1 8B | Groq | $0.06 | $0.06 |
| Llama 3.2 3B | DeepInfra | $0.02 | $0.02 |

---

## Structured Data: Full Pricing Dataset (JSON)

```json
{
  "dataset": "llm-api-pricing-2026",
  "updated": "2026-03-26",
  "currency": "USD",
  "unit": "per 1M tokens",
  "models": [
    {
      "id": "claude-opus-4-6",
      "name": "Claude Opus 4.6",
      "provider": "Anthropic",
      "tier": "flagship",
      "input_per_1m": 5.00,
      "output_per_1m": 25.00,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "gpt-5-4",
      "name": "GPT-5.4",
      "provider": "OpenAI",
      "tier": "flagship",
      "input_per_1m": 2.50,
      "output_per_1m": 15.00,
      "context_window_k": 1050,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "gpt-5",
      "name": "GPT-5",
      "provider": "OpenAI",
      "tier": "flagship",
      "input_per_1m": 1.25,
      "output_per_1m": 10.00,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "gemini-3-1-pro",
      "name": "Gemini 3.1 Pro",
      "provider": "Google",
      "tier": "flagship",
      "input_per_1m": 2.00,
      "output_per_1m": 12.00,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "grok-4",
      "name": "Grok 4",
      "provider": "xAI",
      "tier": "flagship",
      "input_per_1m": 3.00,
      "output_per_1m": 15.00,
      "context_window_k": 2000,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "o3",
      "name": "o3",
      "provider": "OpenAI",
      "tier": "flagship",
      "input_per_1m": 2.00,
      "output_per_1m": 8.00,
      "context_window_k": 200,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "claude-sonnet-4-6",
      "name": "Claude Sonnet 4.6",
      "provider": "Anthropic",
      "tier": "mid-range",
      "input_per_1m": 3.00,
      "output_per_1m": 15.00,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "gpt-4-1",
      "name": "GPT-4.1",
      "provider": "OpenAI",
      "tier": "mid-range",
      "input_per_1m": 2.00,
      "output_per_1m": 8.00,
      "context_window_k": 128,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "gpt-4o",
      "name": "GPT-4o",
      "provider": "OpenAI",
      "tier": "mid-range",
      "input_per_1m": 2.50,
      "output_per_1m": 10.00,
      "context_window_k": 128,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "o4-mini",
      "name": "o4-mini",
      "provider": "OpenAI",
      "tier": "mid-range",
      "input_per_1m": 1.10,
      "output_per_1m": 4.40,
      "context_window_k": 200,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "gemini-2-5-pro",
      "name": "Gemini 2.5 Pro",
      "provider": "Google",
      "tier": "mid-range",
      "input_per_1m": 1.25,
      "output_per_1m": 10.00,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "gemini-3-flash",
      "name": "Gemini 3 Flash",
      "provider": "Google",
      "tier": "mid-range",
      "input_per_1m": 0.50,
      "output_per_1m": 3.00,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "mistral-large-3",
      "name": "Mistral Large 3",
      "provider": "Mistral",
      "tier": "mid-range",
      "input_per_1m": 2.00,
      "output_per_1m": 6.00,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "deepseek-r1",
      "name": "DeepSeek-R1",
      "provider": "DeepSeek",
      "tier": "mid-range",
      "input_per_1m": 0.55,
      "output_per_1m": 2.19,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": 0.90
    },
    {
      "id": "qwen3-max",
      "name": "Qwen3-Max",
      "provider": "Alibaba",
      "tier": "mid-range",
      "input_per_1m": 0.78,
      "output_per_1m": 3.90,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "claude-haiku-4-5",
      "name": "Claude Haiku 4.5",
      "provider": "Anthropic",
      "tier": "budget",
      "input_per_1m": 1.00,
      "output_per_1m": 5.00,
      "context_window_k": 200,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "gpt-4o-mini",
      "name": "GPT-4o mini",
      "provider": "OpenAI",
      "tier": "budget",
      "input_per_1m": 0.15,
      "output_per_1m": 0.60,
      "context_window_k": 128,
      "batch_discount": 0.50,
      "cache_read_discount": 0.50
    },
    {
      "id": "gemini-2-5-flash",
      "name": "Gemini 2.5 Flash",
      "provider": "Google",
      "tier": "budget",
      "input_per_1m": 0.30,
      "output_per_1m": 2.50,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "gemini-2-5-flash-lite",
      "name": "Gemini 2.5 Flash-Lite",
      "provider": "Google",
      "tier": "budget",
      "input_per_1m": 0.10,
      "output_per_1m": 0.40,
      "context_window_k": 1000,
      "batch_discount": 0.50,
      "cache_read_discount": 0.90
    },
    {
      "id": "grok-3-mini",
      "name": "Grok 3 Mini",
      "provider": "xAI",
      "tier": "budget",
      "input_per_1m": 0.30,
      "output_per_1m": 0.50,
      "context_window_k": 131,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "mistral-small-3-1",
      "name": "Mistral Small 3.1",
      "provider": "Mistral",
      "tier": "budget",
      "input_per_1m": 0.10,
      "output_per_1m": 0.30,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "deepseek-v3-2",
      "name": "DeepSeek-V3.2",
      "provider": "DeepSeek",
      "tier": "budget",
      "input_per_1m": 0.28,
      "output_per_1m": 0.42,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": 0.90
    },
    {
      "id": "deepseek-v4",
      "name": "DeepSeek-V4",
      "provider": "DeepSeek",
      "tier": "budget",
      "input_per_1m": 0.30,
      "output_per_1m": 0.50,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": 0.90
    },
    {
      "id": "qwen3-5-plus",
      "name": "Qwen3.5-Plus",
      "provider": "Alibaba",
      "tier": "budget",
      "input_per_1m": 0.26,
      "output_per_1m": 1.56,
      "context_window_k": 128,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "llama-4-maverick",
      "name": "Llama 4 Maverick",
      "provider": "Together AI",
      "tier": "open-source-hosted",
      "input_per_1m": 0.27,
      "output_per_1m": 0.85,
      "context_window_k": null,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "llama-4-scout",
      "name": "Llama 4 Scout",
      "provider": "Groq",
      "tier": "open-source-hosted",
      "input_per_1m": 0.11,
      "output_per_1m": 0.34,
      "context_window_k": null,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "llama-3-1-8b",
      "name": "Llama 3.1 8B",
      "provider": "Groq",
      "tier": "open-source-hosted",
      "input_per_1m": 0.06,
      "output_per_1m": 0.06,
      "context_window_k": null,
      "batch_discount": null,
      "cache_read_discount": null
    },
    {
      "id": "llama-3-2-3b",
      "name": "Llama 3.2 3B",
      "provider": "DeepInfra",
      "tier": "open-source-hosted",
      "input_per_1m": 0.02,
      "output_per_1m": 0.02,
      "context_window_k": null,
      "batch_discount": null,
      "cache_read_discount": null
    }
  ],
  "discounts": {
    "anthropic": {
      "batch_api": "50% off standard price",
      "cache_read": "90% off standard price"
    },
    "openai": {
      "batch_api": "50% off standard price",
      "cache_read": "50% off standard price"
    },
    "google": {
      "batch_api": "50% off standard price",
      "cache_read": "90% off standard price"
    },
    "deepseek": {
      "cache_read": "90% off standard price"
    }
  }
}
```

---

## Best Value Recommendations by Use Case

### High-Volume Text Classification or Extraction

Use **Gemini 2.5 Flash-Lite** ($0.10 / $0.40) or **Mistral Small 3.1** ($0.10 / $0.30). At batch scale, apply Google's 50% discount to bring Flash-Lite to effectively $0.05 input / $0.20 output — well under $1 per 10M output tokens. For workloads where latency is not a factor, DeepInfra's Llama 3.2 3B at $0.02 / $0.02 is the lowest available price across all hosted options.

### Reasoning and Code Generation (Budget)

**o4-mini** ($1.10 / $4.40) is the clearest choice. It costs roughly half of o3 for input and significantly less than GPT-5 or Claude Sonnet, while retaining strong structured reasoning capabilities. Apply OpenAI's 50% batch discount for async jobs to reach $0.55 / $2.20 effective rates.

### Long-Context Document Analysis

**Grok 4** (2M context, $3.00 / $15.00) is the only flagship model with a 2M token window. For 1M context needs, **Claude Opus 4.6**, **Claude Sonnet 4.6**, **Gemini 2.5 Pro**, and **Gemini 2.5 Flash** all support 1M context. Gemini 2.5 Flash at $0.30 / $2.50 is the most cost-effective 1M context option by a wide margin.

### Cost-Optimized Repeated Prompts with Caching

If your application sends the same large system prompt repeatedly, cache reads can reduce costs by 90% on Anthropic and Google models. A 100K-token system prompt with Claude Sonnet 4.6 cache reads costs effectively $0.30 per 1M cached input tokens instead of $3.00. This is the single largest lever for reducing LLM API spend in production.

### Open-Source with No Vendor Lock-In

**Llama 4 Scout** on Groq ($0.11 / $0.34) gives you a current-generation Meta model at near-budget-tier pricing. **Llama 4 Maverick** on Together AI ($0.27 / $0.85) offers a stronger capability tier. Both are fully compatible with the OpenAI-compatible API format used by most inference providers.

### Multi-Modal or Agent Pipelines

For pipelines that require repeated short calls with tool use, **GPT-4o mini** ($0.15 / $0.60) remains the most battle-tested and cost-efficient option with native function calling support. **DeepSeek-V3.2** ($0.28 / $0.42) offers surprisingly low output pricing for a capable model, making it attractive for high-output-ratio workloads.

---

## API Pricing Discount Summary

| Provider | Batch API Discount | Cache Read Discount |
|---|---|---|
| Anthropic | 50% off | 90% off |
| OpenAI | 50% off | 50% off |
| Google | 50% off | 90% off |
| DeepSeek | N/A | 90% off |
| xAI | N/A | N/A |
| Mistral | N/A | N/A |
| Alibaba | N/A | N/A |

Anthropic and Google offer the most aggressive cache read discounts (90%), making them especially cost-effective for applications with repetitive system prompts or retrieval-augmented generation (RAG) workflows where retrieved chunks repeat across requests.

---

## FAQ: LLM API Pricing 2026

### What is the cheapest LLM API available in 2026?

The cheapest hosted LLM option is **Llama 3.2 3B on DeepInfra** at $0.02 per 1M tokens for both input and output. Among proprietary providers, **Gemini 2.5 Flash-Lite** and **Mistral Small 3.1** are tied at $0.10/1M input. For general-purpose work with a major provider, **GPT-4o mini** at $0.15 / $0.60 remains one of the most cost-effective choices with reliable quality.

### How do batch API discounts work and when should I use them?

Batch API (sometimes called async API) lets you submit jobs that run within a 24-hour window instead of returning results in real time. In exchange, providers offer 50% off standard pricing. This is suitable for offline data processing, document summarization, content moderation queues, and any workload without a real-time latency requirement. Anthropic, OpenAI, and Google all support batch mode. At scale, this discount alone can reduce your monthly API bill by half.

### Which model has the largest context window in 2026?

**Grok 4** by xAI leads with a 2M token context window at $3.00 / $15.00 per 1M tokens. Among more affordable models, **Claude Opus 4.6**, **Claude Sonnet 4.6**, **Gemini 2.5 Pro**, **Gemini 2.5 Flash**, and **Gemini 2.5 Flash-Lite** all support 1M token contexts. GPT models are generally capped at 128K–200K tokens.

### Is DeepSeek a reliable alternative to OpenAI and Anthropic for production use?

DeepSeek models (R1, V3.2, V4) have gained significant traction in 2025-2026 as cost-effective alternatives, particularly for code and reasoning tasks. **DeepSeek-R1** at $0.55 / $2.19 with 90% cache read discounts competes closely with models costing 3-4x more. However, for regulated industries or applications with data residency requirements, verify whether DeepSeek's API infrastructure meets your compliance needs before committing to production use.

### How should I choose between Claude Sonnet 4.6 and GPT-4o for my application?

Both are mid-range models with strong general capabilities. **Claude Sonnet 4.6** ($3.00 / $15.00, 1M context) is more expensive but supports much longer context windows than **GPT-4o** ($2.50 / $10.00, 128K context). If your application involves long documents, multi-turn conversations, or large codebases, Claude Sonnet's 1M context window provides significant architectural advantages. For shorter context workloads where cost is the primary concern, GPT-4o or GPT-4.1 are more economical.

---

## Related Resources

- [Best LLM Models for Coding in 2026](/posts/best-llm-models-coding-2026) — benchmark-based ranking for code generation tasks
- [How to Reduce LLM API Costs with Prompt Caching](/posts/llm-prompt-caching-guide-2026) — practical guide to implementing cache reads with Anthropic and Google
- [Open-Source vs Proprietary LLMs: Production Trade-offs in 2026](/posts/open-source-vs-proprietary-llm-2026) — latency, compliance, and cost analysis

---

Last updated: 2026-03-26
