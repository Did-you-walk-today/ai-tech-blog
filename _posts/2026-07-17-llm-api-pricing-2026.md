---
title: "LLM API Pricing 2026: Full Comparison Table (Weekly)"
description: "LLM API pricing 2026: 43 models from OpenAI, Anthropic, Google, xAI, DeepSeek, and Mistral in one table. Input/output cost per 1M tokens, updated weekly."
date: 2026-07-17 12:00:00 +0900
last_modified_at: 2026-08-17 23:40:00 +0900
categories: [ai-data-statistics]
tags: [llm-pricing, api-cost, claude, gpt-5, gemini, grok, deepseek, mistral, "2026"]
format: D
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/llm-api-pricing-2026-cover.jpg
  alt: "A single triangular glass prism on a dark matte surface with cyan and amber light tracing its edges"
faq:
  - q: "What is the cheapest LLM API in 2026?"
    a: "Gemini 2.5 Flash-Lite, at $0.10 input / $0.40 output per 1M tokens. DeepSeek v4-flash held that title until August 17, 2026, when DeepSeek raised it to $0.22 / $0.66 — a 57% input and 136% output increase. DeepSeek still wins decisively on cached input at $0.007 per 1M tokens, a 96.8% discount, so context-reuse workloads should be priced separately from stateless ones."
  - q: "Is Claude Sonnet 5's price going up on September 1, 2026?"
    a: "No. Anthropic cancelled the increase. The $2 input / $10 output rate announced at launch as introductory is now the standard price, and the pricing page states that the scheduled move to $3 / $15 will not occur. If you budgeted against the September number, that reserve can be released."
  - q: "Are per-token prices directly comparable across providers?"
    a: "Not exactly. Anthropic's newer models (Claude Opus 4.7 and later, Sonnet 5, Fable 5) use a tokenizer that produces roughly 30% more tokens for the same text than earlier Claude models. Two models with identical $/1M-token prices can therefore differ meaningfully in cost per document. Compare cost per task, not cost per token, when precision matters."
  - q: "Do these prices include long-context surcharges?"
    a: "The table records base-tier prices. Google and xAI charge tiered rates — prompts above 200K tokens cost roughly double per token (noted per row). Anthropic explicitly bills its 1M-token context window at standard rates on supported models, and OpenAI lists flat per-model rates without a long-context tier on its pricing page."
  - q: "How often is this pricing table updated?"
    a: "Weekly, from the six official pricing pages, with every change recorded in the changelog at the bottom of this post. A missed week is marked as a gap rather than back-filled, because a reconstructed price was never observed. The series began on July 16, 2026 and accumulates as a price-change history that official pages, which only show current prices, do not provide."
data_updated: 2026-08-17
author: jsonhouse
---

As of August 17, 2026, LLM API prices span two orders of magnitude — from $0.10 per million input tokens (Gemini 2.5 Flash-Lite) to $30.00 (GPT-5.5-pro and GPT-5.4-pro). **This was the loudest week since the series began**, and it moved in both directions. DeepSeek raised prices for the first time on record, taking v4-flash from $0.14 / $0.28 to $0.22 / $0.66 and surrendering the cheapest-API title to Gemini 2.5 Flash-Lite. Google cut Gemini 3.6 Flash in half to $0.75 / $3.75 alongside the launch of Gemini 3.7 Flash at the same rate. Anthropic cancelled the Sonnet 5 increase outright: **$2.00 / $10.00 is now the standard price**, not a deadline. Every price below was collected on August 17, 2026 directly from the six providers' official pricing pages and normalized to USD per 1M tokens at the standard (non-batch) tier.

## TL;DR

- **Cheapest overall**: Gemini 2.5 Flash-Lite ($0.10 / $0.40) — it takes the title from DeepSeek v4-flash, which rose 57% on input and 136% on output this week
- **Best flagship value**: Claude Opus 5 at $5.00 / $25.00 — a new generation launched at the outgoing Opus price, one tier below Claude Fable 5 ($10.00 / $50.00)
- **A deadline that vanished**: Sonnet 5's $2.00 / $10.00 was scheduled to rise 50% on September 1; Anthropic cancelled it and made the rate permanent
- **A deadline that appeared**: Gemini 3.7 and 3.6 Flash are $0.75 / $3.75 only through 2026-12-31, then double on 2027-01-01
- **Cache reads are still the real price war**: cache-hit discounts run 90% (Anthropic, OpenAI, Google) to 96.8% (DeepSeek, down from 98% after this week's increase)

## Methodology

All prices were collected on **2026-08-17** from official provider pricing pages only: [Anthropic](https://platform.claude.com/docs/en/docs/about-claude/pricing), [OpenAI](https://developers.openai.com/api/docs/pricing), [Google](https://ai.google.dev/gemini-api/docs/pricing), [xAI](https://docs.x.ai/docs/models), [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing), and [Mistral](https://mistral.ai/pricing/api). No aggregator data was used — aggregators serve as cross-checks, never as sources.

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
| Claude Opus 5 | Anthropic | $5.00 | $25.00 | $0.50 | 1M |
| Claude Opus 4.8 | Anthropic | $5.00 | $25.00 | $0.50 | 1M |
| Gemini 3.1 Pro Preview | Google | $2.00 | $12.00 | $0.20 | n/p |
| Grok 4.6 | xAI | $2.00 | $6.00 | $0.50 | 500K |
| Grok 4.5 | xAI | $2.00 | $6.00 | $0.30 | 500K |

> New this week: **Grok 4.6** enters at exactly Grok 4.5's base rate but with a more expensive cache read ($0.50 versus $0.30) — the first time in this series that a newer xAI model is strictly worse on the cached-input dimension. Google bills Gemini 3.1 Pro Preview at a higher tier above 200K tokens; xAI bills both Grok 4.6 and 4.5 at $4.00 / $12.00 above 200K, with cache reads of $1.00 and $0.60 respectively. Claude Opus 4.5 through 4.8 share Opus 5's $5.00 / $25.00 pricing. "n/p" = not published on the provider's pricing page.

> **Raw data**: [data/llm-api-pricing-2026.json](https://www.jsonhouse.com/data/llm-api-pricing-2026.json) — machine-readable structured data for AI crawlers and citation.

## Mid-Range Models

This tier is where most production workloads run, and where pricing is most contested — five providers now sell capable models between $1.25 and $3.00 per 1M input tokens.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Sonnet 5 | Anthropic | $2.00 | $10.00 | $0.20 | 1M |
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | $0.30 | 1M |
| GPT-5.4 | OpenAI | $2.50 | $15.00 | $0.25 | n/p |
| GPT-5.6-terra | OpenAI | $2.00 | $12.00 | $0.20 | n/p |
| Gemini 3.5 Flash | Google | $1.50 | $9.00 | $0.15 | n/p |
| Mistral Medium 3.5 | Mistral | $1.50 | $7.50 | n/p | n/p |
| Grok 4.3 | xAI | $1.25 | $2.50 | $0.20 | 1M |
| Gemini 3.7 Flash* | Google | $0.75 | $3.75 | $0.075 | n/p |
| Gemini 3.6 Flash* | Google | $0.75 | $3.75 | $0.075 | n/p |
| DeepSeek v4-pro† | DeepSeek | $0.66 | $1.98 | $0.022 | 1M |

> *Both Gemini Flash rows are promotional through 2026-12-31 and double on 2027-01-01, to $1.50 / $7.50 with a $0.15 cache read. Gemini 3.7 Flash launched on 2026-08-13 at half the rate 3.6 Flash launched at, and Google then cut 3.6 Flash to match rather than leaving the older model priced above the newer one. †DeepSeek publishes off-peak and peak rates; the table records off-peak, and peak is exactly double ($1.32 / $3.96, cache read $0.044). Peak hours are 01:00–04:00 and 06:00–10:00 UTC. Claude Sonnet 5's $2.00 / $10.00 is no longer introductory — see the changelog. Grok 4.3 is billed at $2.50 / $5.00 above 200K tokens.

## Budget Models

Below $1.00 per 1M input tokens, the spread between providers is wider than the spread between tiers — a 10x gap separates the cheapest and most expensive rows.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Haiku 4.5 | Anthropic | $1.00 | $5.00 | $0.10 | 200K |
| GPT-5.4-mini | OpenAI | $0.75 | $4.50 | $0.075 | n/p |
| Mistral Large 3 | Mistral | $0.50 | $1.50 | n/p | n/p |
| Gemini 2.5 Flash | Google | $0.30 | $2.50 | $0.03 | 1M |
| Gemini 3.1 Flash-Lite | Google | $0.25 | $1.50 | $0.025 | n/p |
| DeepSeek v4-flash† | DeepSeek | $0.22 | $0.66 | $0.007 | 1M |
| GPT-5.6-luna | OpenAI | $0.20 | $1.20 | $0.02 | n/p |
| GPT-5.4-nano | OpenAI | $0.20 | $1.25 | $0.02 | n/p |
| Mistral Small 4 | Mistral | $0.15 | $0.60 | n/p | n/p |
| Gemini 2.5 Flash-Lite | Google | $0.10 | $0.40 | $0.01 | n/p |

> †DeepSeek v4-flash rose this week from $0.14 / $0.28 to $0.22 / $0.66 off-peak, dropping it four places in this table and ending its run as the cheapest maintained general-purpose API. Peak rates are double ($0.44 / $1.32, cache read $0.014). Note the shape of the increase: input rose 57% while output rose 136%, moving DeepSeek's output-to-input ratio from 2x to 3x and into line with the 3–6x every other provider charges. Mistral Large 3 still costs a third of the newer Mistral Medium 3.5 — Mistral has repositioned its former flagship as a budget option rather than retiring it. GPT-5.6-luna sits on exactly GPT-5.4-nano's input and cache-read prices, so OpenAI sells two generations at an identical input cost and separates them only by a five-cent output difference.

## Coding and Specialist Models

This tier shrank sharply this week. Mistral's pricing page no longer lists Magistral Medium, Magistral Small, Devstral 2, or Devstral Small 2, and its models overview gives retirement dates for all four running from 2025-10-31 to 2026-07-31. Four of the seven rows this section carried last week were models Mistral had already withdrawn — a reminder that a pricing page is a better record of what exists than of what stopped existing.

| Model | Provider | Input $/1M | Output $/1M | Context |
|---|---|---|---|---|
| Grok-build-0.1 (coding) | xAI | $1.00 | $2.00 | 256K |
| Codestral (coding) | Mistral | $0.30 | $0.90 | n/p |
| Ministral 3 (3B / 8B / 14B) | Mistral | $0.10–0.20 | $0.10–0.20 | n/p |

> Grok-build-0.1 is billed at $2.00 / $4.00 above 200K tokens. Ministral 3 models are priced symmetrically (identical input and output rates), which is rare — output tokens typically cost 3–6x input. Ministral 3 sits outside the weekly-tracked snapshot set and is shown here for completeness of Mistral's lineup, without week-over-week change tracking. Also newly on Mistral's pricing page but outside the tracked set: Z.ai's GLM 5.2 at $1.40 / $4.40, resold under Mistral's API. It is the first third-party model to appear on a tracked provider's own pricing page, and how to count it is an open question for this series rather than a settled one.

## The Fine Print That Changes the Rankings

A per-token price table looks objective, but three structural details buried in provider documentation change what these numbers actually mean.

**First, tokens are no longer a stable unit.** Anthropic discloses that Claude Opus 4.7 and later, Sonnet 5, and Fable 5 use a new tokenizer that produces roughly 30% more tokens for the same text. That means Sonnet 5's $2.00 input price is closer to an effective ~$2.60 per old-tokenizer-equivalent input, which erases most of its apparent advantage over GPT-5.4's $2.50 — a gap the sticker prices hide entirely. No other provider publishes tokenizer efficiency data at all, which makes cross-provider per-token comparison an approximation, not an equivalence. This is why cost-per-task benchmarking is replacing cost-per-token math in serious procurement.

**Second, the price war moved from base rates to cache reads — but not everywhere, and not permanently.** Anthropic, OpenAI, and Google all price a cache read at 10% of base input, a flat 90% discount. DeepSeek goes further, to 96.8%, though that is down from 98% because its cache-read price rose faster this week than its base rate did.

xAI shows the direction running both ways within one vendor. It cut Grok 4.5's cache read from $0.50 to $0.30 between our July 16 and July 28 snapshots, deepening that discount from 75% to 85% while leaving the $2.00 base input untouched. Then this week it launched Grok 4.6 at the same $2.00 base with a $0.50 cache read — reverting to the 75% discount for the newer model. If cache reads are where the competition is, xAI just made its newest model less competitive on exactly that axis.

For agentic workloads, where the same system prompt and tool definitions are re-sent on every call, cached input routinely dominates total token volume. In that regime, the cache-read column of the tables above predicts your bill better than the input column does. A provider with a higher base price and cheaper effective caching can win on real invoices.

The cache-read column alone does not settle it, though, because the write fee and the minimum cacheable prefix differ by vendor and neither appears in this table. We normalized those into an effective cost per hit rate in [LLM Cache Pricing 2026](/posts/llm-cache-pricing-2026/), which is the companion to this page for anyone whose bill is mostly repeated input.

**Third, pricing structure — flat versus tiered — is a strategic split, not an accounting detail.** Anthropic explicitly bills its 1M-token context window at standard rates: a 900K-token request costs the same per token as a 9K one. Google and xAI took the opposite path, roughly doubling per-token rates above 200K tokens. Flat pricing sells predictability to agent builders whose context sizes vary wildly at runtime; tiered pricing protects margins on the expensive long-context serving path. Which structure wins will shape how retrieval-augmented and long-context architectures are designed, because a 2x cliff at 200K tokens is an architectural forcing function.

## The Bigger Picture

The market is not uniformly deflating, and this week exposed that "deflation" has been hiding two different things.

Two of the three price moves came with a clock attached. Google's Gemini Flash rows are $0.75 / $3.75 only through December 31, 2026, and the pricing page already prints the January 1 rate beside it. Anthropic used the same instrument in the opposite direction, converting Sonnet 5's introductory rate into the standard one and cancelling an increase it had pre-announced. Both are promotional pricing being managed. Neither says anything about what it costs to serve those models.

DeepSeek is the counterexample, and it is the informative one. It runs no promotional clock. It raised prices outright — 57% on v4-flash input, 136% on output — after its pricing page had warned for weeks that an increase was coming without naming a figure or a date. That is a structural reprice, not an expiring discount.

Read together, the two moves invert the story this page has been telling since July. The pre-announced increase everyone was told to budget for was cancelled; the increase nobody could size arrived instead, and it was larger. Frontier prices are still rising — Fable 5 at $10 / $50, OpenAI's pro tier at $30 / $180 — on the theory that frontier capability is price-inelastic. What is newly in question is the assumption underneath the rest of the table: that the commodity tier can only ever get cheaper.

This matters beyond procurement because API pricing is becoming the cost structure of AI-mediated traffic itself. As we documented in our analysis of [ChatGPT ads and AEO economics](/posts/chatgpt-ads-2026-aeo-reddit-citations/), AI answers are now a monetized distribution channel; the margin between what a model costs to run and what its answers earn determines which models power that channel. And token efficiency is not only a provider-side variable — [vague prompts inflate token consumption and degrade output quality simultaneously](/posts/gigo-prompts-2026-why-vague-prompts-fail/), so prompt discipline compounds directly with the per-token rates in these tables.

## How to Choose: Recommendations by Workload

**High-volume extraction and classification.** Gemini 2.5 Flash-Lite ($0.10 / $0.40) is now the price floor among maintained models on its own; this week's increase moved DeepSeek v4-flash ($0.22 / $0.66) to more than double it on input and above Mistral Small 4 as well. DeepSeek's 1M context and near-free cache reads still make it the stronger pick when documents repeat across requests, but for stateless pipelines the case for it has narrowed considerably.

**Agentic workloads with heavy context reuse.** Rank by cache-read price, not input price: DeepSeek v4-flash ($0.007), Gemini 2.5 Flash-Lite ($0.01), GPT-5.4-nano and GPT-5.6-luna ($0.02 each), Claude Haiku 4.5 ($0.10). If your agent re-sends a 50K-token system prompt on every call, these numbers are your effective input price. DeepSeek still leads this ranking after the increase, but by 1.4x rather than the 3.6x it led by last week.

**Long-context analysis.** Claude Sonnet 5 ($2.00 / $10.00, flat 1M context) is the standout, and as of this week it is no longer on a clock — flagship-adjacent quality, no long-context surcharge, and no scheduled increase. Grok 4.3 ($1.25 / $2.50 base, 1M) undercuts it on sticker price, but only if your prompts stay under the 200K-token cliff where xAI's rates double.

**Frontier reasoning.** Claude Opus 5 ($5.00 / $25.00) is the value anchor of the top tier, and Opus 4.5 through 4.8 sit at the same price if you need an older revision pinned. Claude Fable 5 ($10.00 / $50.00) and GPT-5.6-sol ($5.00 / $30.00) price above it; the pro-grade OpenAI models ($30.00 / $180.00) only make sense where a single hard task justifies a 6–7x premium over Opus 5.

## Limitations

- **Standard tier only.** Batch discounts (typically 50% off at Anthropic, OpenAI, Google, and Mistral) and regional/data-residency surcharges (10% at OpenAI and Anthropic for US-only routing) are not baked into the tables.
- **Context windows marked "n/p"** are not published on the provider's official pricing page; we do not fill gaps from third-party sources.
- **Mistral does not publish cache-read pricing**, so its rows cannot be compared on the caching dimension.
- **Coverage is six providers (43 models tracked).** The tables show the notable rows and footnote price-identical siblings, so the visible row count is lower than the tracked count. Open-source hosted inference (Groq, Together, DeepInfra) and Alibaba/Qwen are excluded from this edition; we would rather ship a fully verified narrow table than a broad one with stale rows.
- **DeepSeek's rows are off-peak rates and are not strictly comparable to the rest of the table.** Every other provider publishes one rate that applies at all hours. DeepSeek publishes two, and a workload that runs during the 01:00–04:00 and 06:00–10:00 UTC peak windows pays exactly double the figures shown. We record the lower tier for consistency with how tiered pricing is handled elsewhere, not because it is the rate most users will pay.
- **Prices are list prices.** Enterprise volume discounts are negotiated and unobservable.

## Update Cadence and Changelog

This table is refreshed **weekly** from the six official pricing pages, and every change lands here as a dated entry. Official pricing pages only show current prices — the change history below, and the snapshot series behind it, is what this page accumulates that they do not.

| Date | Change |
|---|---|
| 2026-08-17 | The largest week in the series. **DeepSeek raised prices**, the first increase recorded here from any provider: v4-flash $0.14 / $0.28 → $0.22 / $0.66 (cache read $0.0028 → $0.007) and v4-pro $0.435 / $0.87 → $0.66 / $1.98 (cache read $0.003625 → $0.022), all off-peak. This is the increase the 2026-08-10 entry flagged as expected but unsized. DeepSeek also shipped build V4-Pro-0813. **Google halved Gemini 3.6 Flash** to $0.75 / $3.75 (cache read $0.075) to match new arrival **Gemini 3.7 Flash**, launched 2026-08-13 at the same rate; both are promotional through 2026-12-31 and double on 2027-01-01. **Anthropic cancelled the Claude Sonnet 5 increase** — $2.00 / $10.00 is now the standard price and the 2026-09-01 move to $3.00 / $15.00 will not occur. Added: Gemini 3.7 Flash, Grok 4.6 ($2.00 / $6.00, cache read $0.50). Removed: Claude Opus 4.1, retired from the first-party API on 2026-08-05, and Magistral Medium, Magistral Small, Devstral 2, and Devstral Small 2, all absent from Mistral's pricing page with retirement dates between 2025-10-31 and 2026-07-31. Those five had been carried in earlier snapshots after their retirement dates passed; the earlier files are left as collected rather than corrected. Tracked set: 46 → 43 models. |
| 2026-08-10 | No change. Every row in the tables above holds last week's price, and no model entered or left the six providers' pricing pages — the first flat week since the series began. Two things visible on the pages but not yet in the table: Anthropic's Sonnet 5 introductory rate still expires 2026-08-31, and DeepSeek's pricing page states that a significant increase is expected, without naming a date or a figure. Neither is recorded as a price until it takes effect. |
| 2026-08-03 | OpenAI cut two GPT-5.6 models: luna from $1.00 / $6.00 to $0.20 / $1.20 (−80%, cache read $0.10 → $0.02) and terra from $2.50 / $15.00 to $2.00 / $12.00 (−20%, cache read $0.25 → $0.20). Both were cross-verified against OpenAI's models page before recording. No models added or removed; every other row across the six providers was unchanged. Gemini 3.5 Flash-Lite's $0.03 cache read was recorded for the first time — a gap in the prior collection, not a price change. |
| 2026-07-28 | Added Claude Opus 5 and Gemini 3.6 Flash. Grok 4.5 cache read cut from $0.50 to $0.30 (−40%), the only base-table price change. DeepSeek's legacy IDs retired on schedule. No snapshot was taken on 2026-07-20 or 2026-07-27; those two weeks are absent from the series and were not reconstructed. |
| 2026-07-16 | Initial 2026 edition: baseline of 39 models across 6 providers. Supersedes the March 2026 draft dataset. |

## FAQ: LLM API Pricing 2026

### What is the cheapest LLM API in 2026?

Gemini 2.5 Flash-Lite, at $0.10 input / $0.40 output per 1M tokens. DeepSeek v4-flash held the title until August 17, 2026, when DeepSeek raised it to $0.22 / $0.66 — 57% on input, 136% on output — and dropped it below four other rows in the budget table. DeepSeek still wins on cached input at $0.007 per 1M tokens, a 96.8% discount, so a workload that reuses context should be priced on the cache-read column rather than this one.

### Is Claude Sonnet 5's price going up on September 1, 2026?

No. Anthropic cancelled the increase. The $2.00 / $10.00 rate announced at launch as introductory is now the standard price, and the pricing page states plainly that the scheduled move to $3.00 / $15.00 will not occur. This page carried the September deadline as its most time-sensitive number for six weeks; it is gone. If you budgeted a 50% cost increase for Sonnet 5 workloads from September, that reserve can be released.

### Are per-token prices directly comparable across providers?

Only approximately. Anthropic's newest models tokenize the same text into roughly 30% more tokens than its earlier models, and other providers publish no tokenizer efficiency data at all. Two models with the same $/1M price can produce meaningfully different invoices for the same documents — compare cost per task when the decision matters.

### Do these prices include long-context surcharges?

No — tables record base tiers. Google and xAI roughly double per-token rates for prompts above 200K tokens (footnoted per table), while Anthropic bills its full 1M context at standard rates and OpenAI publishes flat per-model prices without a long-context tier.

### How often is this table updated?

Weekly, from official provider pages only, with every change recorded in the changelog above. Missed weeks are marked as gaps rather than back-filled: the 2026-07-20 and 2026-07-27 snapshots were not taken, and reconstructing them after the fact would put unobserved prices into a series whose whole value rests on every row having been read off a live page. The series began July 16, 2026 and compounds into a price-change history that current-price-only official pages do not offer.

## Related Resources

- [ChatGPT Ads 2026: AEO Traffic and Reddit Citations](/posts/chatgpt-ads-2026-aeo-reddit-citations/) — the revenue side of the same equation: what AI-mediated answers earn
- [GIGO Prompt Engineering: Why Vague Prompts Fail](/posts/gigo-prompts-2026-why-vague-prompts-fail/) — cutting token waste at the prompt level compounds with every rate in this table
