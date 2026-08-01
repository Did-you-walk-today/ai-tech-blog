---
title: "LLM Cache Pricing 2026: The Real Cost of Cached Input"
description: "LLM cache pricing 2026 normalized across six providers: effective input cost at real hit rates, hidden write fees, and which vendors publish nothing at all."
date: 2026-08-01 10:00:00 +0000
last_modified_at: 2026-08-01 10:00:00 +0000
categories: [ai-data-statistics]
tags: [prompt-caching, llm-pricing, api-cost, claude, gpt-5, gemini, deepseek, "2026"]
format: D
cluster: CLUSTER_LLM
category_id: CAT5
image:
  path: /assets/img/posts/llm-cache-pricing-2026-cover.jpg
  alt: "A shallow pool of still water in a carved dark stone basin, one shaft of light bending at the surface"
faq:
  - q: "How much does prompt caching actually save in 2026?"
    a: "The cached-read discount has converged on 90% at Anthropic, OpenAI, and Google. xAI discounts 84–85% and DeepSeek 98–99%. But the discount applies only to the cached portion of your prompt, so the saving you actually see is roughly your cache hit rate times the discount. At a 50% hit rate a 90% discount is a 45% saving on input, not 90%."
  - q: "Do you pay to write to the cache?"
    a: "At Anthropic, yes and always: a 5-minute cache write costs 1.25x base input, a 1-hour write 2x. OpenAI introduced the same 1.25x write charge with the GPT-5.6 family; models before it had none. Google charges no write fee but bills cache storage per hour. xAI, DeepSeek, and Mistral publish no write price at all."
  - q: "Which LLM API is cheapest for a cache-heavy agent?"
    a: "It depends on your hit rate, and the ranking flips. Below roughly 83% hit rate Gemini 2.5 Flash-Lite is the cheapest per effective input token; above it DeepSeek v4-flash takes over, reaching $0.0097 per 1M effective input tokens at a 95% hit rate. Three separate model pairs cross over in the same 83–85% band."
  - q: "Is prompt caching automatic or do I have to enable it?"
    a: "OpenAI, Google, DeepSeek, and xAI cache automatically. Anthropic requires an explicit cache_control field. The distinction now carries a price: because OpenAI's GPT-5.6 family caches automatically and bills writes at 1.25x, a long prompt you never reuse can be billed above the base rate unless you set prompt_cache_options.mode to explicit."
  - q: "Why can't I compare cache prices straight from provider pricing pages?"
    a: "Because no two publish the same fields. Anthropic states multipliers, DeepSeek an absolute cache-hit price, xAI a single cached-input column, Google a per-hour storage rate, and Mistral only a headline -90% with no per-model figure. Four of the six publish no cache TTL. Normalizing them to one unit is the reason this table exists."
data_updated: 2026-07-28
author: jsonhouse
---

Prompt caching is sold as a 90% discount, and at the sticker level that is now true almost everywhere: Anthropic, OpenAI, and Google all price a cache read at exactly one tenth of base input. The number that decides your invoice is different. It is the **effective input price** — what you pay per million input tokens once your actual cache hit rate, the write surcharge, and the storage fee are all folded in.

On that measure the cheapest model in 2026 is not the one with the lowest sticker price, and the ranking flips at a hit rate most production agents already exceed. This page normalizes cache pricing for 14 models across six providers to a single unit, using prices collected on 2026-07-28.

## TL;DR

- **The discount converged, the disclosure did not.** 90% cache-read discount at Anthropic, OpenAI, and Google; 84–85% at xAI; 98–99% at DeepSeek. But four of six providers publish no cache TTL, and Mistral publishes no per-model cache price at all.
- **Write fees are spreading.** Anthropic has always charged 1.25x (5-minute) or 2x (1-hour) to write. OpenAI added a 1.25x write charge with the GPT-5.6 family; earlier OpenAI models had none.
- **The cheapest model changes at ~84% hit rate.** Below it Gemini 2.5 Flash-Lite wins on effective input cost; above it DeepSeek v4-flash does. Three unrelated model pairs cross over in an 83–85% band.
- **Caching still pays after two calls.** Even at a 2x write multiplier, reusing a prefix three times beats not caching. The break-even is low enough that write fees are a rounding error for agents — and a real penalty for one-shot prompts.
- **"90% off" is not a 90% saving.** The discount applies only to the cached share of your prompt. At a 50% hit rate it is a 45% cut.

## Methodology

Base input and cache-read prices were collected on **2026-07-28** from the six providers' official pricing pages, the same sources and normalization used in our [weekly LLM API pricing table](/posts/llm-api-pricing-2026/): Anthropic (platform.claude.com), OpenAI (developers.openai.com), Google (ai.google.dev), xAI (docs.x.ai), DeepSeek (api-docs.deepseek.com), Mistral (mistral.ai). Caching mechanics — write cost, storage fee, TTL, trigger, minimum cacheable length — were read from each provider's prompt-caching documentation on the same date.

Effective input price is computed as `base x (1 - h) + cache_read x h`, where `h` is the cache hit rate: the share of input tokens served from cache. It deliberately excludes write and storage costs, which are handled separately below, because those are one-time or time-based rather than per-token and would otherwise make the columns non-comparable.

All figures are USD per 1M tokens at the standard, non-batch, base long-context tier. Where a provider publishes nothing, the cell reads "not published" — we do not derive a figure and present it as a price. The one derivation we do make is labelled as such.

## Effective Input Price by Cache Hit Rate

`h = 0%` is the sticker price. `h = 95%` is a realistic figure for an agent that re-sends a stable system prompt and tool definitions on every turn.

| Model | Provider | h = 0% | h = 50% | h = 80% | h = 95% | Discount |
|---|---|---|---|---|---|---|
| Claude Opus 5 | Anthropic | $5.0000 | $2.7500 | $1.4000 | $0.7250 | 90% |
| GPT-5.6-sol | OpenAI | $5.0000 | $2.7500 | $1.4000 | $0.7250 | 90% |
| GPT-5.6-terra | OpenAI | $2.5000 | $1.3750 | $0.7000 | $0.3625 | 90% |
| Claude Sonnet 5 | Anthropic | $2.0000 | $1.1000 | $0.5600 | $0.2900 | 90% |
| Grok 4.5 | xAI | $2.0000 | $1.1500 | $0.6400 | $0.3850 | 85% |
| Gemini 3.6 Flash | Google | $1.5000 | $0.8250 | $0.4200 | $0.2175 | 90% |
| Mistral Medium 3.5 | Mistral | $1.5000 | not published | not published | not published | −90% stated |
| Grok 4.3 | xAI | $1.2500 | $0.7250 | $0.4100 | $0.2525 | 84% |
| Claude Haiku 4.5 | Anthropic | $1.0000 | $0.5500 | $0.2800 | $0.1450 | 90% |
| GPT-5.6-luna | OpenAI | $1.0000 | $0.5500 | $0.2800 | $0.1450 | 90% |
| DeepSeek v4-pro | DeepSeek | $0.4350 | $0.2193 | $0.0899 | $0.0252 | 99.2% |
| Gemini 2.5 Flash | Google | $0.3000 | $0.1650 | $0.0840 | $0.0435 | 90% |
| DeepSeek v4-flash | DeepSeek | $0.1400 | $0.0714 | $0.0302 | $0.0097 | 98% |
| Gemini 2.5 Flash-Lite | Google | $0.1000 | $0.0550 | $0.0280 | $0.0145 | 90% |

> **Raw data**: [data/llm-cache-pricing-2026.json](https://www.jsonhouse.com/data/llm-cache-pricing-2026.json) — machine-readable structured data for AI crawlers and citation.

> Mistral states a headline "-90% on input token" for cached input but publishes no per-model cache price, so its effective columns are left unfilled rather than derived. Applying the stated −90% would imply $0.15/1M for Mistral Medium 3.5, but that is an inference from a marketing line, not a published rate.

## What the Sticker Price Hides

The per-token discount is only one of four cost dimensions, and the other three are disclosed unevenly.

| Provider | Write cost | Storage fee | Cache TTL | Trigger | Min. cacheable |
|---|---|---|---|---|---|
| Anthropic | 1.25x (5 min), 2x (1 h) | None | 5 min or 1 h | `cache_control` | 512–4,096 by model |
| OpenAI | 1.25x on GPT-5.6+; none before | None | ≥ 30 min (GPT-5.6+) | Automatic | 1,024 |
| Google | Not published | $1.00–$4.50 per 1M tokens/hour | Not published | Implicit, on by default | 2,048–4,096 |
| xAI | Not published | Not published | Not published (eviction-based) | Automatic, keyed | Not published |
| DeepSeek | Not published | Not published | "Hours to days", not guaranteed | Automatic | Not published |
| Mistral | Not published | Not published | Not published | Not published | Not published |

> Anthropic's minimum cacheable length varies more than any other provider's: 512 tokens on Opus 5 and Fable 5, but 4,096 on Opus 4.5, Opus 4.6, and Haiku 4.5. A prompt that caches on one Claude model is silently not cached on another, and the API returns no error when this happens.

## The Deep Analysis: Three Things This Table Says

**The 90% discount is a coordinated price, not a cost.** Anthropic, OpenAI, and Google independently arrived at exactly 0.1x base input for a cache read. Cache serving costs differ across three different inference stacks; the identical multiplier does not. This is what a converged commodity price looks like — the number stopped tracking cost and became a market expectation nobody can be the first to break. The outliers say the same thing from opposite ends: DeepSeek prices at 98% off to buy share, and xAI's 84–85% is the one figure that moved between our 2026-07-16 and 2026-07-28 snapshots, from 75% toward the herd.

**Write fees appeared exactly when caching became automatic.** Anthropic has always charged to write, and has always required you to ask for caching. OpenAI did the reverse for years: automatic caching, free writes. With GPT-5.6 it added a 1.25x write charge while keeping caching automatic and on by default above 1,024 tokens.

Those two facts interact in a way the documentation does not resolve. OpenAI's guide says an eligible prefix "may" be cached and that written tokens bill at the write rate; it does not say whether a write is charged on a prompt that is never read again. There is an opt-out — `prompt_cache_options.mode` set to `explicit` — and the existence of an opt-out is itself informative. But the cost of failing to use it is not published, and one-shot long-prompt workloads are exactly where it would bite.

**Storage is Google's version of the same charge, moved in time.** Google takes no write fee and instead bills $1.00 per 1M cached tokens per hour, rising to $4.50 on Gemini 2.5 Pro and 3.1 Pro. For an agent that keeps a 200K-token context warm all day, that is a real line item that never appears in a per-token comparison. Anthropic front-loads the same economics into the write; Google meters it. Neither is hidden, but they are not comparable without doing the arithmetic yourself — which is the point of this page.

## Where the Ranking Flips

Cache hit rate does not merely scale costs down uniformly. It reorders them, because providers discount by different amounts from different starting points.

Three model pairs cross over, and all three cross in the same narrow band:

| Cheaper below the crossover | Cheaper above it | Crossover hit rate | Effective price at crossover |
|---|---|---|---|
| Gemini 2.5 Flash-Lite | DeepSeek v4-flash | 84.7% | $0.0237 / 1M |
| Gemini 2.5 Flash | DeepSeek v4-pro | 83.7% | $0.0741 / 1M |
| Grok 4.3 | Gemini 3.6 Flash | 83.3% | $0.3750 / 1M |

That an 83–85% hit rate is the hinge for three unrelated pairs is not a coincidence. It is where a 90% discount stops being able to defend a lower sticker price against a 98% one. Below that band, sticker price dominates and the familiar ranking from a plain [pricing table](/posts/llm-api-pricing-2026/) holds. Above it, the cache column decides, and any comparison that ignores caching is ranking the wrong quantity.

Most stateless pipelines sit well below the band. Most long-running agents sit above it.

## Does the Write Fee Actually Matter?

Less than it looks, if you reuse anything at all. For a prefix written once and read N−1 times, caching beats not caching at:

| Write multiplier | Who | Break-even |
|---|---|---|
| None | OpenAI pre-5.6, Google, and providers publishing no write fee | N ≥ 2 calls |
| 1.25x | Anthropic 5-minute, OpenAI GPT-5.6+ | N ≥ 2 calls |
| 2x | Anthropic 1-hour | N ≥ 3 calls |

A worked example makes the scale concrete. A 50,000-token system prompt sent on 1,000 calls costs $100.00 of input on Claude Sonnet 5 with no caching. With the 5-minute cache and its 1.25x write, it costs $10.12 — an 89.9% saving, within a tenth of a point of the headline 90% despite paying the write premium. The write is amortized over 999 reads and disappears.

The write fee is therefore not an agent problem. It is a one-shot problem, and only on providers that cache automatically.

## The Bigger Picture

Cache pricing is where the LLM market's economics stopped being about model quality. A 90% discount on repeated input is a bet that the dominant workload is no longer a human typing a fresh question but an agent re-sending the same 50,000 tokens of instructions on a loop. Every provider has now priced for that world, which means every provider believes it.

That belief shows up in our other numbers too. The frontier is [splitting between rising flagship prices and deflating everything else](/posts/llm-api-pricing-2026/), and the models buyers actually pick are increasingly chosen on [capability limits rather than raw benchmark scores](/posts/best-llm-2026/). Caching sits underneath both: it is the mechanism that makes a large, static, expensive context economically survivable, and therefore the reason agent architectures grew context instead of trimming it.

It also quietly changes who wins. A provider with a mediocre sticker price and an aggressive cache discount can undercut a cheaper rival on real invoices, which is exactly what DeepSeek does above an 84% hit rate. Sticker-price leaderboards no longer predict spend.

## How to Choose: Recommendations by Workload

**Stateless, high-volume extraction (hit rate near 0%).** Rank on sticker price and ignore this page's other columns. Gemini 2.5 Flash-Lite ($0.10) and DeepSeek v4-flash ($0.14) lead, in that order.

**Long-running agents with a stable system prompt (hit rate above 85%).** Rank on the `h = 95%` column, where the order inverts: DeepSeek v4-flash ($0.0097), Gemini 2.5 Flash-Lite ($0.0145), DeepSeek v4-pro ($0.0252), Gemini 2.5 Flash ($0.0435).

**One-shot long prompts on OpenAI GPT-5.6+.** Measure `cache_write_tokens` on a representative request before assuming caching is free. If the prompt is never reused, `prompt_cache_options.mode` set to `explicit` is the documented way to suppress the implicit breakpoint.

**Anything on Claude.** Check the minimum cacheable length for your specific model before budgeting a saving. At 4,096 tokens on Haiku 4.5 and Opus 4.5, a prompt that caches fine on Opus 5 will silently not cache, with no error returned.

**Anything on Mistral.** You cannot model cache economics from published data. Treat the −90% headline as unverified until per-model rates appear.

## Limitations

- **Effective price excludes write and storage costs.** Those are one-time or hourly, not per-token, and are analyzed separately above rather than folded into a single number that would hide which component moved.
- **Cache hit rate is an input, not a measurement.** We publish the formula and the price inputs; we have not measured hit rates on real workloads. That is a separate experiment and a future post.
- **Four of six providers publish no TTL**, so time-based cache expiry cannot be modelled for them. Real hit rates on those providers may be materially lower than configured.
- **Mistral rows are unfillable**, not estimated. Its cache economics are outside this comparison until it publishes per-model rates.
- **Prices are list prices** at the standard non-batch tier. Batch discounts and negotiated enterprise rates are excluded.
- **Coverage is 14 models across six providers**, chosen to span every tier and every disclosure pattern rather than to be exhaustive.

## Update Cadence and Changelog

This page is refreshed **weekly** from the same snapshot series that backs our pricing table, and every change lands below as a dated entry. Caching mechanics — write fees, TTLs, minimum lengths — are re-read from provider documentation monthly, since they change far more slowly than prices.

| Date | Change |
|---|---|
| 2026-07-28 | Initial edition. 14 models, six providers. Records xAI's Grok 4.5 cache read moving $0.50 to $0.30 and OpenAI's 1.25x write charge on the GPT-5.6 family. |

## FAQ: LLM Cache Pricing 2026

### How much does prompt caching actually save in 2026?

The cached-read discount has converged on 90% at Anthropic, OpenAI, and Google, with xAI at 84–85% and DeepSeek at 98–99%. That discount applies only to the cached share of a prompt, so your realized saving is roughly the hit rate times the discount. A 50% hit rate against a 90% discount is a 45% cut to input cost, not 90%.

### Do you pay to write to the cache?

At Anthropic, always: 1.25x base input for the 5-minute cache, 2x for the 1-hour. OpenAI introduced the same 1.25x charge with the GPT-5.6 family, having charged nothing on earlier models. Google levies no write fee but bills storage at $1.00–$4.50 per 1M cached tokens per hour. xAI, DeepSeek, and Mistral publish no write price.

### Which LLM API is cheapest for a cache-heavy agent?

It depends on hit rate, and the answer changes. Below roughly 83% Gemini 2.5 Flash-Lite is cheapest per effective input token; above it DeepSeek v4-flash takes the lead, reaching $0.0097 per 1M at a 95% hit rate. Three separate pairs of models cross over between 83.3% and 84.7%.

### Is prompt caching automatic or do I have to enable it?

OpenAI, Google, DeepSeek, and xAI cache automatically; Anthropic requires an explicit `cache_control` field. That difference now costs money: because GPT-5.6 caches automatically above 1,024 tokens and bills writes at 1.25x, a long prompt you never reuse may be billed above base rate unless you set `prompt_cache_options.mode` to `explicit`.

### Why can't I compare cache prices straight from provider pricing pages?

No two providers publish the same fields. Anthropic gives multipliers, DeepSeek an absolute cache-hit price, xAI one cached-input column, Google a per-hour storage rate, and Mistral only a headline −90% with no per-model number. Four of six publish no TTL. Normalizing those into one unit is the reason this page exists.

## Related Resources

- [LLM API Pricing 2026: Full Comparison Table (Weekly)](/posts/llm-api-pricing-2026/) — the base prices these effective rates are computed from
- [Best LLM 2026: Capability and Limits Compared](/posts/best-llm-2026/) — what you get for the token, once you know what the token costs
- [Best LLM Subscription 2026: What You Really Pay For](/posts/llm-subscription-guide-2026/) — the same hidden-cost problem on the consumer side of the bill
