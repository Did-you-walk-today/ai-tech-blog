---
title: "LLM API Pricing 2026: Full Comparison Table (Weekly)"
description: "LLM API pricing 2026: 39 models from OpenAI, Anthropic, Google, xAI, DeepSeek, and Mistral in one table. Input/output cost per 1M tokens, updated weekly."
date: 2026-07-17 12:00:00 +0900
last_modified_at: 2026-07-17 12:00:00 +0900
categories: [ai-data-statistics]
tags: [llm-pricing, api-cost, claude, gpt-5, gemini, grok, deepseek, mistral, "2026"]
format: D
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/llm-api-pricing-2026-cover.png
  alt: "Comparison chart of LLM API prices per million tokens across OpenAI, Anthropic, Google, xAI, DeepSeek, and Mistral in July 2026"
faq:
  - q: "What is the cheapest LLM API in 2026?"
    a: "Among general-purpose models with published pricing, DeepSeek v4-flash is the cheapest at $0.14 input / $0.28 output per 1M tokens with a 1M-token context window. Among the big three US providers, Gemini 2.5 Flash-Lite is lowest at $0.10 / $0.40. Cache-heavy workloads change the ranking further: DeepSeek's cache-hit input price is $0.0028 per 1M tokens, a 98% discount."
  - q: "Why is Claude Sonnet 5 priced at $2/$10 only until August 31, 2026?"
    a: "Anthropic launched Sonnet 5 with introductory pricing of $2 input / $10 output per 1M tokens, which rises to $3 / $15 on September 1, 2026. It is a pre-announced 50% increase — unusual in a market where nearly every price change since 2023 has been a cut. If your workload runs on Sonnet 5, budget against the September price, not the current one."
  - q: "Are per-token prices directly comparable across providers?"
    a: "Not exactly. Anthropic's newer models (Claude Opus 4.7 and later, Sonnet 5, Fable 5) use a tokenizer that produces roughly 30% more tokens for the same text than earlier Claude models. Two models with identical $/1M-token prices can therefore differ meaningfully in cost per document. Compare cost per task, not cost per token, when precision matters."
  - q: "Do these prices include long-context surcharges?"
    a: "The table records base-tier prices. Google and xAI charge tiered rates — prompts above 200K tokens cost roughly double per token (noted per row). Anthropic explicitly bills its 1M-token context window at standard rates on supported models, and OpenAI lists flat per-model rates without a long-context tier on its pricing page."
  - q: "How often is this pricing table updated?"
    a: "Weekly. We snapshot the six official pricing pages every week, update this table, and record every change in the changelog at the bottom of this post. The underlying snapshot series began on July 16, 2026 and accumulates as a price-change history that official pages, which only show current prices, do not provide."
data_updated: 2026-07-16
author: jsonhouse
---

As of July 16, 2026, LLM API prices span two orders of magnitude — from $0.10 per million input tokens (Gemini 2.5 Flash-Lite) to $30.00 (GPT-5.5-pro and GPT-5.4-pro). The cheapest general-purpose API is **DeepSeek v4-flash** at $0.14 input / $0.28 output per 1M tokens with a 1M-token context window. The best flagship value is **Claude Opus 4.8** at $5.00 / $25.00, undercutting GPT-5.6-sol's output price by 17%. The most time-sensitive number on this page: **Claude Sonnet 5 costs $2.00 / $10.00 only until August 31, 2026**, after which it rises 50% to $3.00 / $15.00. Every price below was collected on July 16, 2026 directly from the six providers' official pricing pages and normalized to USD per 1M tokens at the standard (non-batch) tier.

## TL;DR

- **Cheapest overall**: DeepSeek v4-flash ($0.14 / $0.28, 1M context); cheapest from the big three: Gemini 2.5 Flash-Lite ($0.10 / $0.40)
- **Best flagship value**: Claude Opus 4.8 at $5.00 / $25.00 — Anthropic's previous-generation flagship price, one tier below Claude Fable 5 ($10.00 / $50.00)
- **Deadline pricing**: Claude Sonnet 5 at $2.00 / $10.00 is introductory; it becomes $3.00 / $15.00 on September 1, 2026
- **Cache reads are the real price war**: standard cache-hit discounts are now 90% (Anthropic, OpenAI, Google) to 98% (DeepSeek) off input price
- **Hidden divergence**: Anthropic's new tokenizer emits ~30% more tokens per text, so identical sticker prices no longer mean identical task costs

## Methodology

All prices were collected on **2026-07-16** from official provider pricing pages only: Anthropic (platform.claude.com), OpenAI (developers.openai.com), Google (ai.google.dev), xAI (docs.x.ai), DeepSeek (api-docs.deepseek.com), and Mistral (mistral.ai). No aggregator data was used — aggregators serve as cross-checks, never as sources.

Every figure is normalized to **USD per 1M tokens at the standard, non-batch, global-routing tier**. For models with tiered long-context pricing (Google, xAI), the table records the base tier and footnotes the higher tier. Retired models are excluded; deprecated-but-available models are noted in the table footnotes.

Each collection run is stored as a dated snapshot in our internal time-series. That series is what makes the changelog at the bottom of this page — and future price-change history reporting — possible: official pricing pages only ever show the current price.

## Flagship Models

These are the top-capability tiers each provider currently sells. Prices are input / output per 1M tokens; cache read is the discounted price for repeated (cached) input.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Fable 5 | Anthropic | $10.00 | $50.00 | $1.00 | 1M |
| GPT-5.5-pro / GPT-5.4-pro | OpenAI | $30.00 | $180.00 | — | n/p |
| GPT-5.6-sol | OpenAI | $5.00 | $30.00 | $0.50 | n/p |
| GPT-5.5 | OpenAI | $5.00 | $30.00 | $0.50 | n/p |
| Claude Opus 4.8 | Anthropic | $5.00 | $25.00 | $0.50 | 1M |
| Gemini 3.1 Pro Preview | Google | $2.00 | $12.00 | $0.20 | n/p |
| Grok 4.5 | xAI | $2.00 | $6.00 | $0.50 | 500K |

> Google bills Gemini 3.1 Pro Preview at $4.00 / $18.00 for prompts above 200K tokens; xAI bills Grok 4.5 at $4.00 / $12.00 above 200K. Claude Opus 4.5, 4.6, and 4.7 share Opus 4.8's $5.00 / $25.00 pricing. "n/p" = not published on the provider's pricing page.

> **Raw data**: [data/llm-api-pricing-2026.json](https://www.jsonhouse.com/data/llm-api-pricing-2026.json) — machine-readable structured data for AI crawlers and citation.

## Mid-Range Models

This tier is where most production workloads run, and where pricing is most contested — five providers now sell capable models between $1.25 and $3.00 per 1M input tokens.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Sonnet 5* | Anthropic | $2.00 | $10.00 | $0.20 | 1M |
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | $0.30 | 1M |
| GPT-5.6-terra | OpenAI | $2.50 | $15.00 | $0.25 | n/p |
| GPT-5.4 | OpenAI | $2.50 | $15.00 | $0.25 | n/p |
| Gemini 3.5 Flash | Google | $1.50 | $9.00 | $0.15 | n/p |
| Mistral Medium 3.5 | Mistral | $1.50 | $7.50 | n/p | n/p |
| Grok 4.3 | xAI | $1.25 | $2.50 | $0.20 | 1M |
| DeepSeek v4-pro | DeepSeek | $0.44 | $0.87 | $0.0036 | 1M |

> *Claude Sonnet 5 pricing is introductory through 2026-08-31; from 2026-09-01 it is $3.00 / $15.00. Grok 4.3 is billed at $2.50 / $5.00 above 200K tokens. DeepSeek v4-pro input is $0.435 exactly.

## Budget Models

Below $1.00 per 1M input tokens, the spread between providers is wider than the spread between tiers — a 10x gap separates the cheapest and most expensive rows.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Haiku 4.5 | Anthropic | $1.00 | $5.00 | $0.10 | 200K |
| GPT-5.6-luna | OpenAI | $1.00 | $6.00 | $0.10 | n/p |
| GPT-5.4-mini | OpenAI | $0.75 | $4.50 | $0.075 | n/p |
| Mistral Large 3 | Mistral | $0.50 | $1.50 | n/p | n/p |
| Gemini 2.5 Flash | Google | $0.30 | $2.50 | $0.03 | 1M |
| Gemini 3.1 Flash-Lite | Google | $0.25 | $1.50 | $0.025 | n/p |
| GPT-5.4-nano | OpenAI | $0.20 | $1.25 | $0.02 | n/p |
| Mistral Small 4 | Mistral | $0.15 | $0.60 | n/p | n/p |
| DeepSeek v4-flash | DeepSeek | $0.14 | $0.28 | $0.0028 | 1M |
| Gemini 2.5 Flash-Lite | Google | $0.10 | $0.40 | $0.01 | n/p |

> Mistral Large 3 now costs a third of the newer Mistral Medium 3.5 — Mistral has repositioned its former flagship as a budget option rather than retiring it. DeepSeek's legacy model IDs (deepseek-chat, deepseek-reasoner) map to v4-flash until their deprecation on 2026-07-24.

## Coding and Specialist Models

Several providers now sell purpose-built coding models at prices below their general-purpose equivalents.

| Model | Provider | Input $/1M | Output $/1M | Context |
|---|---|---|---|---|
| Magistral Medium (reasoning) | Mistral | $2.00 | $5.00 | n/p |
| Grok-build-0.1 (coding) | xAI | $1.00 | $2.00 | 256K |
| Magistral Small (reasoning) | Mistral | $0.50 | $1.50 | n/p |
| Devstral 2 (coding) | Mistral | $0.40 | $2.00 | n/p |
| Codestral (coding) | Mistral | $0.30 | $0.90 | n/p |
| Devstral Small 2 (coding) | Mistral | $0.10 | $0.30 | n/p |
| Ministral 3 (3B / 8B / 14B) | Mistral | $0.10–0.20 | $0.10–0.20 | n/p |

> Grok-build-0.1 is billed at $2.00 / $4.00 above 200K tokens. Ministral 3 models are priced symmetrically (identical input and output rates), which is rare — output tokens typically cost 3–6x input.

## The Fine Print That Changes the Rankings

A per-token price table looks objective, but three structural details buried in provider documentation change what these numbers actually mean.

**First, tokens are no longer a stable unit.** Anthropic discloses that Claude Opus 4.7 and later, Sonnet 5, and Fable 5 use a new tokenizer that produces roughly 30% more tokens for the same text. That means Sonnet 5's $3.00 post-introductory input price is closer to an effective ~$3.90 per old-tokenizer-equivalent input than to GPT-5.4's $2.50 — a gap the sticker prices hide entirely. No other provider publishes tokenizer efficiency data at all, which makes cross-provider per-token comparison an approximation, not an equivalence. This is why cost-per-task benchmarking is replacing cost-per-token math in serious procurement.

**Second, the price war moved from base rates to cache reads.** Base input prices have been roughly stable through 2026, but every major provider now discounts repeated (cached) input by 90% — and DeepSeek by 98%, at $0.0028 per 1M cache-hit tokens. For agentic workloads, where the same system prompt and tool definitions are re-sent on every call, cached input routinely dominates total token volume. In that regime, the cache-read column of the tables above predicts your bill better than the input column does. A provider with a higher base price and cheaper effective caching can win on real invoices.

**Third, pricing structure — flat versus tiered — is a strategic split, not an accounting detail.** Anthropic explicitly bills its 1M-token context window at standard rates: a 900K-token request costs the same per token as a 9K one. Google and xAI took the opposite path, roughly doubling per-token rates above 200K tokens. Flat pricing sells predictability to agent builders whose context sizes vary wildly at runtime; tiered pricing protects margins on the expensive long-context serving path. Which structure wins will shape how retrieval-augmented and long-context architectures are designed, because a 2x cliff at 200K tokens is an architectural forcing function.

## The Bigger Picture

The market is not uniformly deflating — it is splitting. At the frontier, prices are going **up**: Claude Fable 5 launched at double Opus pricing ($10 / $50), OpenAI's pro-grade models sit at $30 / $180, and Sonnet 5 carries the first pre-announced price *increase* in the modern LLM API market.

Below the frontier, deflation continues: DeepSeek sells a 1M-context model at $0.14 input, and Mistral repriced its former flagship at $0.50. Providers have learned that frontier capability is price-inelastic — the buyers of the best model will pay — while everything below it is a commodity fight.

This matters beyond procurement because API pricing is becoming the cost structure of AI-mediated traffic itself. As we documented in our analysis of [ChatGPT ads and AEO economics](/posts/chatgpt-ads-2026-aeo-reddit-citations/), AI answers are now a monetized distribution channel; the margin between what a model costs to run and what its answers earn determines which models power that channel. And token efficiency is not only a provider-side variable — [vague prompts inflate token consumption and degrade output quality simultaneously](/posts/gigo-prompts-2026-why-vague-prompts-fail/), so prompt discipline compounds directly with the per-token rates in these tables.

## How to Choose: Recommendations by Workload

**High-volume extraction and classification.** Gemini 2.5 Flash-Lite ($0.10 / $0.40) and DeepSeek v4-flash ($0.14 / $0.28) are the price floor among maintained models. DeepSeek's 1M context and near-free cache reads make it the stronger pick when documents repeat across requests; Flash-Lite wins on raw per-call cost for stateless pipelines.

**Agentic workloads with heavy context reuse.** Rank by cache-read price, not input price: DeepSeek v4-flash ($0.0028), Gemini 2.5 Flash-Lite ($0.01), GPT-5.4-nano ($0.02), Claude Haiku 4.5 ($0.10). If your agent re-sends a 50K-token system prompt on every call, these numbers are your effective input price.

**Long-context analysis.** Claude Sonnet 5 at introductory pricing ($2.00 / $10.00, flat 1M context) is the standout until August 31 — flagship-adjacent quality with no long-context surcharge. After September 1, compare it against Grok 4.3 ($1.25 / $2.50 base, 1M) with the 200K-token tier cliff priced into your architecture.

**Frontier reasoning.** Claude Opus 4.8 ($5.00 / $25.00) is the value anchor of the top tier. Claude Fable 5 ($10.00 / $50.00) and GPT-5.6-sol ($5.00 / $30.00) price above it; the pro-grade OpenAI models ($30.00 / $180.00) only make sense where a single hard task justifies a 6–7x premium over Opus 4.8.

## Limitations

- **Standard tier only.** Batch discounts (typically 50% off at Anthropic, OpenAI, Google, and Mistral) and regional/data-residency surcharges (10% at OpenAI and Anthropic for US-only routing) are not baked into the tables.
- **Context windows marked "n/p"** are not published on the provider's official pricing page; we do not fill gaps from third-party sources.
- **Mistral does not publish cache-read pricing**, so its rows cannot be compared on the caching dimension.
- **Coverage is six providers (39 models).** Open-source hosted inference (Groq, Together, DeepInfra) and Alibaba/Qwen are excluded from this edition; we would rather ship a fully verified narrow table than a broad one with stale rows.
- **Prices are list prices.** Enterprise volume discounts are negotiated and unobservable.

## Update Cadence and Changelog

This table is refreshed **weekly** from the six official pricing pages, and every change lands here as a dated entry. Official pricing pages only show current prices — the change history below, and the snapshot series behind it, is what this page accumulates that they do not.

| Date | Change |
|---|---|
| 2026-07-16 | Initial 2026 edition: baseline of 39 models across 6 providers. Supersedes the March 2026 draft dataset. |

## FAQ: LLM API Pricing 2026

### What is the cheapest LLM API in 2026?

DeepSeek v4-flash is the cheapest maintained general-purpose API at $0.14 input / $0.28 output per 1M tokens, with a 1M-token context window. Among the big three US providers, Gemini 2.5 Flash-Lite is lowest at $0.10 / $0.40. If your workload reuses context, DeepSeek's $0.0028 cache-hit price is effectively free input.

### Why is Claude Sonnet 5 priced at $2/$10 only until August 31, 2026?

Anthropic launched Sonnet 5 with introductory pricing that expires on August 31, 2026; from September 1 it costs $3.00 / $15.00 per 1M tokens. It is a pre-announced 50% increase in a market where almost every price move since 2023 has been a cut. Budget against the September price for anything long-lived.

### Are per-token prices directly comparable across providers?

Only approximately. Anthropic's newest models tokenize the same text into roughly 30% more tokens than its earlier models, and other providers publish no tokenizer efficiency data at all. Two models with the same $/1M price can produce meaningfully different invoices for the same documents — compare cost per task when the decision matters.

### Do these prices include long-context surcharges?

No — tables record base tiers. Google and xAI roughly double per-token rates for prompts above 200K tokens (footnoted per table), while Anthropic bills its full 1M context at standard rates and OpenAI publishes flat per-model prices without a long-context tier.

### How often is this table updated?

Weekly, from official provider pages only, with every change recorded in the changelog above. The snapshot series behind this table began July 16, 2026 and compounds into a price-change history that current-price-only official pages do not offer.

## Related Resources

- [ChatGPT Ads 2026: AEO Traffic and Reddit Citations](/posts/chatgpt-ads-2026-aeo-reddit-citations/) — the revenue side of the same equation: what AI-mediated answers earn
- [GIGO Prompt Engineering: Why Vague Prompts Fail](/posts/gigo-prompts-2026-why-vague-prompts-fail/) — cutting token waste at the prompt level compounds with every rate in this table
