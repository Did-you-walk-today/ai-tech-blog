---
title: "LLM API Pricing 2026: Full Comparison Table (Weekly)"
description: "LLM API pricing 2026: 51 models from OpenAI, Anthropic, Google, xAI, DeepSeek, and Mistral in one table. Input/output cost per 1M tokens, updated weekly."
date: 2026-07-17 12:00:00 +0900
last_modified_at: 2026-09-28 15:00:00 +0900
categories: [ai-data-statistics]
tags: [llm-pricing, api-cost, claude, gpt-5, gemini, grok, deepseek, mistral, "2026"]
format: D
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/llm-api-pricing-2026-cover.jpg
  alt: "A single triangular glass prism on a dark matte surface with cyan and amber light tracing its edges"
faq:
  - q: "What is the cheapest LLM API in 2026?"
    a: "Gemini 2.5 Flash-Lite, at $0.10 input / $0.40 output per 1M tokens. OpenAI's GPT-6-luna, added on September 28, 2026, ties it on input ($0.10) and cached input ($0.01) but costs $0.50 on output. DeepSeek's deepseek-flash follows at $0.15 / $0.60 and is the cheapest on cached input at $0.003 per 1M — a 98% discount, the deepest in these tables."
  - q: "Is Claude Sonnet 5's price going up on September 1, 2026?"
    a: "No. Anthropic cancelled the increase, and $2 input / $10 output has held in every collection since. After the cancellation the pricing page said the introductory rate had become the standard price; by September 28 that sentence was gone and the page simply lists $2 / $10 with no scheduled change. If you budgeted against the September number, that reserve can be released."
  - q: "Why is Claude Fable 5.1's cache read cheaper than Claude Opus 5's?"
    a: "Anthropic prices a cache hit as a multiplier on base input, and since September 7, 2026 it has not used one multiplier for the whole line. Claude Fable 5.1 and Claude Mythos 5.1 bill cache hits at 0.025x base input ($0.25 per 1M tokens). Claude Opus 5.5, added September 28, bills them at 0.05x ($0.20). Every other Claude model, Opus 5 included, stays at 0.1x. Anthropic's most expensive models carry its deepest cache discount, at 97.5%."
  - q: "Are per-token prices directly comparable across providers?"
    a: "Not exactly. Anthropic's newer models (Claude Opus 4.7 and later, Sonnet 5, Fable 5) use a tokenizer that produces roughly 30% more tokens for the same text than earlier Claude models. Two models with identical $/1M-token prices can therefore differ meaningfully in cost per document. Compare cost per task, not cost per token, when precision matters."
  - q: "Do these prices include long-context surcharges?"
    a: "The table records base-tier prices. Google and xAI charge tiered rates — prompts above 200K tokens cost roughly double per token (noted per row). OpenAI lists a long-context tier on ten of its twelve tracked rows, every one except GPT-5.4-mini and GPT-5.4-nano. Anthropic is the only tracked vendor that explicitly bills its full 1M-token context window at standard rates."
  - q: "If no LLM price changed this week, is my bill unchanged?"
    a: "Not necessarily. Per-token rates can hold while token counts move. Anthropic states that Claude 4.7 and later models use a tokenizer producing roughly 30% more tokens for the same text than Sonnet 4.6 and earlier, so nine of our fourteen Anthropic rows bill more per page of English at an unchanged per-token price. Compare cost per task, not cost per token, whenever a comparison crosses a tokenizer change."
  - q: "How often is this pricing table updated?"
    a: "Weekly, from the six official pricing pages, with every change recorded in the changelog at the bottom of this post. A missed week is marked as a gap rather than back-filled, because a reconstructed price was never observed. The series began on July 16, 2026 and accumulates as a price-change history that official pages, which only show current prices, do not provide."
data_updated: 2026-09-28
author: jsonhouse
---

As of September 28, 2026, LLM API prices span two orders of magnitude — from $0.10 per million input tokens (Gemini 2.5 Flash-Lite, now joined by GPT-6-luna) to $30.00 (GPT-5.5-pro and GPT-5.4-pro). No tracked price moved this week: all 47 rows carried from September 21 hold their input, output and cache-read rates, a fifth consecutive flat week. Four models arrived and none left, taking the tracked set to 51.

The arrivals are where the prices fell. Claude Opus 5.5 lists at $4.00 / $20.00, 20% under Claude Opus 5. GPT-6-sol lists at $2.00 / $10.00, half of GPT-5.6-sol's promotional rate. GPT-6-luna lists at $0.10 / $0.50, half of GPT-5.6-luna on input. Only Grok 4.7 arrived at its predecessor's price.

None of the older models was repriced to meet them. Opus 5 still costs $5.00 / $25.00, and GPT-5.6-luna still costs $0.20 / $1.20. That is the pattern five flat weeks were hiding: the market is still getting cheaper, but the cuts ship as new model IDs, and a buyer only receives them by migrating.

The unit underneath moved too, and it moved against the sticker. [Anthropic's pricing page](https://platform.claude.com/docs/en/about-claude/pricing) states that Claude 4.7 and later models use a tokenizer producing roughly 30% more tokens for the same text. Opus 5.5 is one of them, so nine of the fourteen Anthropic rows below now bill more per page of English than their per-token prices suggest.

Every price below was collected on September 28, 2026 directly from the six providers' official pricing pages and normalized to USD per 1M tokens at the standard (non-batch) tier.

## TL;DR

- **Cheapest overall**: Gemini 2.5 Flash-Lite ($0.10 / $0.40). New GPT-6-luna ties it on input and cache read and loses only on output ($0.50)
- **Best flagship value**: Claude Opus 5.5 at $4.00 / $20.00 matches GPT-5.6-sol's promotional rate with no expiry attached and half its cache-read price ($0.20 against $0.40)
- **Price cuts now arrive as new models**: Opus 5.5 is 20% under Opus 5, GPT-6-sol half of GPT-5.6-sol, GPT-6-luna half of GPT-5.6-luna on input. None of the older rows was repriced to match
- **Anthropic runs three cache-read multipliers**: 0.1x on most of its line, 0.05x on Opus 5.5, 0.025x on Fable 5.1 and Mythos 5.1. The deepest cache discount overall is still DeepSeek's `deepseek-flash` at 98%
- **Fifth straight flat week on the carried set**: all 47 rows held their prices; four arrivals and no removals take the tracked set to 51
- **An unchanged price is not an unchanged bill**: Claude 4.7 and later, Opus 5.5 included, count roughly 30% more tokens for the same text

## Methodology

All prices were collected on **2026-09-28** from official provider pricing pages only: [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI](https://developers.openai.com/api/docs/pricing), [Google](https://ai.google.dev/gemini-api/docs/pricing), [xAI](https://docs.x.ai/developers/pricing), [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing), and [Mistral](https://mistral.ai/pricing/api). No aggregator data was used — aggregators serve as cross-checks, never as sources.

Every figure is normalized to **USD per 1M tokens at the standard, non-batch, global-routing tier**. For models with tiered long-context pricing (Google, xAI), the table records the base tier and footnotes the higher tier. Retired models are excluded; deprecated-but-available models are noted in the table footnotes.

Each collection run is stored as a dated snapshot in our internal time-series. That series is what makes the changelog at the bottom of this page — and future price-change history reporting — possible: official pricing pages only ever show the current price.

## Flagship Models

These are the top-capability tiers each provider currently sells. Prices are input / output per 1M tokens; cache read is the discounted price for repeated (cached) input.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Fable 5.1 | Anthropic | $10.00 | $50.00 | $0.25 | 1M |
| Claude Fable 5 | Anthropic | $10.00 | $50.00 | $1.00 | 1M |
| GPT-6-astra | OpenAI | $10.00 | $50.00 | $1.00 | n/p |
| GPT-5.5-pro / GPT-5.4-pro | OpenAI | $30.00 | $180.00 | — | n/p |
| GPT-5.5 | OpenAI | $5.00 | $30.00 | $0.50 | n/p |
| Claude Opus 5 | Anthropic | $5.00 | $25.00 | $0.50 | 1M |
| Claude Opus 4.8 | Anthropic | $5.00 | $25.00 | $0.50 | 1M |
| Claude Opus 5.5* | Anthropic | $4.00 | $20.00 | $0.20 | 1M |
| GPT-5.6-sol | OpenAI | $4.00 | $20.00 | $0.40 | n/p |
| Gemini 3.1 Pro Preview | Google | $2.00 | $12.00 | $0.20 | n/p |
| Grok 4.7* | xAI | $2.00 | $6.00 | $0.50 | 500K |
| Grok 4.6 | xAI | $2.00 | $6.00 | $0.50 | 500K |
| Grok 4.5 | xAI | $2.00 | $6.00 | $0.30 | 500K |

> *Added 2026-09-28. **Claude Opus 5.5** lists at $4.00 / $20.00, 20% under Opus 5 on both input and output, and Anthropic's models page now names it the default starting model. Its cache hit is priced at 0.05x base input ($0.20 per 1M), a third Claude multiplier beside the 0.1x standard and the 0.025x on Fable 5.1 and Mythos 5.1. **Grok 4.7** matches Grok 4.6 at both tiers, including a $4.00 / $12.00 rate above 200K tokens (cache read $1.00).

> GPT-5.6-sol's $4.00 / $20.00 is promotional, stated available at least through 2026-11-21, with a long-context tier at $8.00 / $30.00 (cache read $0.80). GPT-6-astra carries a $20.00 / $75.00 long-context tier (cache read $2.00). Claude Mythos 5 and 5.1 are priced identically to Fable 5 and 5.1 but are application-gated, so they are carried in our snapshot without a row here. Google bills Gemini 3.1 Pro Preview at a higher tier above 200K tokens; xAI bills Grok 4.5 at $4.00 / $12.00 above 200K with a $0.60 cache read. Claude Opus 4.5 through 4.8 share Opus 5's $5.00 / $25.00 pricing. "n/p" = not published on the provider's pricing page.

> **Raw data**: [data/llm-api-pricing-2026.json](https://www.jsonhouse.com/data/llm-api-pricing-2026.json) — machine-readable structured data for AI crawlers and citation.

## Mid-Range Models

This tier is where most production workloads run, and where pricing is most contested — five providers now sell capable models between $1.25 and $3.00 per 1M input tokens.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Sonnet 5 | Anthropic | $2.00 | $10.00 | $0.20 | 1M |
| GPT-6-sol‡ | OpenAI | $2.00 | $10.00 | $0.20 | n/p |
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | $0.30 | 1M |
| GPT-5.4 | OpenAI | $2.50 | $15.00 | $0.25 | n/p |
| GPT-5.6-terra | OpenAI | $2.00 | $12.00 | $0.20 | n/p |
| Gemini 3.5 Flash | Google | $1.50 | $9.00 | $0.15 | n/p |
| Mistral Medium 3.5 | Mistral | $1.50 | $7.50 | n/p | n/p |
| Grok 4.3 | xAI | $1.25 | $2.50 | $0.20 | 1M |
| Gemini 3.8 Flash* | Google | $0.75 | $3.75 | $0.075 | n/p |
| Gemini 3.7 Flash* | Google | $0.75 | $3.75 | $0.075 | n/p |
| Gemini 3.6 Flash* | Google | $0.75 | $3.75 | $0.075 | n/p |
| DeepSeek v4-pro† | DeepSeek | $0.66 | $1.98 | $0.022 | 1M |

> *All three Gemini Flash rows are promotional through 2026-12-31 and double on 2027-01-01, to $1.50 / $7.50 with a $0.15 cache read. Gemini 3.8 Flash arrived on 2026-09-07 at exactly the rate its two predecessors already carried, expiry included — Google is now selling three generations of Flash at one price with one shared deadline. Gemini 3.7 Flash launched on 2026-08-13 at half the rate 3.6 Flash launched at, and Google then cut 3.6 Flash to match rather than leaving the older model priced above the newer one. †DeepSeek publishes off-peak and peak rates; the table records off-peak, and peak is exactly double ($1.32 / $3.96, cache read $0.044). Peak hours are 01:00–04:00 and 06:00–10:00 UTC. v4-pro was the DeepSeek row that did *not* change on 2026-09-14. The page's statement that its service continues past that date was removed by 2026-09-28, but the model is still listed at unchanged rates. Claude Sonnet 5's $2.00 / $10.00 is no longer introductory — see the changelog. Grok 4.3 is billed at $2.50 / $5.00 above 200K tokens. ‡GPT-6-sol, added 2026-09-28, lands on exactly Claude Sonnet 5's $2.00 / $10.00 and $0.20 cache read, and costs half of GPT-5.6-sol's promotional rate. Unlike Sonnet 5 it carries a long-context tier, at $4.00 / $15.00 (cache read $0.40).

## Budget Models

Below $1.00 per 1M input tokens, the spread between providers is wider than the spread between tiers — a 10x gap separates the cheapest and most expensive rows.

| Model | Provider | Input $/1M | Output $/1M | Cache read $/1M | Context |
|---|---|---|---|---|---|
| Claude Haiku 4.5 | Anthropic | $1.00 | $5.00 | $0.10 | 200K |
| GPT-5.4-mini | OpenAI | $0.75 | $4.50 | $0.075 | n/p |
| Mistral Large 3 | Mistral | $0.50 | $1.50 | n/p | n/p |
| Gemini 2.5 Flash | Google | $0.30 | $2.50 | $0.03 | 1M |
| Gemini 3.1 Flash-Lite | Google | $0.25 | $1.50 | $0.025 | n/p |
| GPT-5.6-luna | OpenAI | $0.20 | $1.20 | $0.02 | n/p |
| GPT-5.4-nano | OpenAI | $0.20 | $1.25 | $0.02 | n/p |
| DeepSeek flash† | DeepSeek | $0.15 | $0.60 | $0.003 | 1M |
| Mistral Small 4 | Mistral | $0.15 | $0.60 | n/p | n/p |
| GPT-6-luna‡ | OpenAI | $0.10 | $0.50 | $0.01 | n/p |
| Gemini 2.5 Flash-Lite | Google | $0.10 | $0.40 | $0.01 | n/p |

> †This row changed identity on 2026-09-14. DeepSeek retired v4-flash (build V4-Flash-0731) and now serves that name from DeepSeek-V4.1-Flash under the id `deepseek-flash`; the legacy id is still accepted and billed at the new rate. Read the row as a substitution, not a 32% input cut — the product behind the earlier figures no longer exists. Peak rates are double ($0.30 / $1.20, cache read $0.006), with peak hours 01:00–04:00 and 06:00–10:00 UTC. The new rate ties Mistral Small 4 to the cent on both input and output, and the two separate only on caching, which Mistral does not price at all. Mistral Large 3 still costs a third of the newer Mistral Medium 3.5 — Mistral has repositioned its former flagship as a budget option rather than retiring it. GPT-5.6-luna sits on exactly GPT-5.4-nano's input and cache-read prices, so OpenAI sells two generations at an identical input cost and separates them only by a five-cent output difference.

> ‡GPT-6-luna, added 2026-09-28, halves GPT-5.6-luna's input and cache read and cuts its output 58%, from $1.20 to $0.50. That puts OpenAI level with Gemini 2.5 Flash-Lite on input and cache read for the first time in this series, $0.10 behind on output. It carries a long-context tier at $0.20 / $0.75 (cache read $0.02).

## Coding and Specialist Models

This tier shrank sharply in the week to 2026-08-17. Mistral's pricing page no longer lists Magistral Medium, Magistral Small, Devstral 2, or Devstral Small 2, and its models overview gives retirement dates for all four running from 2025-10-31 to 2026-07-31. Four of the seven rows this section carried the week before were models Mistral had already withdrawn — a reminder that a pricing page is a better record of what exists than of what stopped existing.

| Model | Provider | Input $/1M | Output $/1M | Context |
|---|---|---|---|---|
| Grok-build-0.1 (coding) | xAI | $1.00 | $2.00 | 256K |
| Codestral (coding) | Mistral | $0.30 | $0.90 | n/p |
| Ministral 3 (3B / 8B / 14B) | Mistral | $0.10–0.20 | $0.10–0.20 | n/p |

> Grok-build-0.1 is billed at $2.00 / $4.00 above 200K tokens. Ministral 3 models are priced symmetrically (identical input and output rates), which is rare — output tokens typically cost 3–6x input. Ministral 3 sits outside the weekly-tracked snapshot set and is shown here for completeness of Mistral's lineup, without week-over-week change tracking. Also newly on Mistral's pricing page but outside the tracked set: Z.ai's GLM 5.2 at $1.40 / $4.40, resold under Mistral's API. It is the first third-party model to appear on a tracked provider's own pricing page, and how to count it is an open question for this series rather than a settled one.

## The Fine Print That Changes the Rankings

A per-token price table looks objective, but three structural details buried in provider documentation change what these numbers actually mean.

**First, tokens are no longer a stable unit.** Anthropic states that Claude 4.7 and later models, plus Mythos Preview, use a tokenizer producing roughly 30% more tokens for the same text, and that Sonnet 4.6 and earlier use the previous one. The split runs through Anthropic's own table: nine of the fourteen rows we track count one way, five the other. Claude Opus 5.5, added this week, is on the newer side.

The effect is an invisible price. Sonnet 5's $2.00 input is closer to ~$2.60 per old-tokenizer-equivalent page, which erases most of its apparent advantage over GPT-5.4's $2.50 — and makes the $3.00 Sonnet 4.6 the cheaper row for some English text, despite costing 50% more per token. That inversion appears nowhere in the price columns.

In a week where no carried price moved, this is the one thing that separates rows that look identical. No other provider publishes tokenizer efficiency data at all, which makes cross-provider per-token comparison an approximation, not an equivalence. This is why [cost-per-task benchmarking](/posts/llm-cost-per-task-2026/) is replacing cost-per-token math in serious procurement.

**Second, the price war moved from base rates to cache reads — but not everywhere, and not permanently.** Anthropic, OpenAI, and Google have all priced a cache read at 10% of base input, a flat 90% discount. Two vendors have now gone past it, and the lead between them changed twice in eight days.

On September 7 Anthropic broke its own flat rule: Claude Fable 5.1 and Mythos 5.1 bill cache hits at 0.025x base input, a 97.5% discount, while every older Claude model stays at 0.1x. That is a discount of unusual size sitting on the most expensive models a vendor sells rather than the cheapest — a shape that only makes sense if the buyer being courted is one whose bill is mostly re-sent context and who is not shopping on sticker price.

On September 14 DeepSeek took the title back at 98%, and it got there by a different route. Anthropic cut a multiplier. DeepSeek changed the model: `deepseek-flash` prices a cache hit at $0.003 against $0.15 base input, restoring roughly the 98% ratio v4-flash carried before August 17 and briefly lost. The competitive fact is that two vendors are now bidding on the cache column specifically, while the other four hold a flat 90% — and the vendor whose sticker price is near the bottom of the table and the vendor whose sticker price is at the top are the two doing it.

On September 28 Anthropic added a third step. Claude Opus 5.5 bills a cache hit at 0.05x base input, a 95% discount, halfway between its standard 0.1x and the 0.025x on Fable 5.1. Anthropic now sets the cache multiplier per model rather than per line. A buyer cannot infer a Claude model's cache price from its base price any more.

xAI shows the direction running both ways within one vendor. It cut Grok 4.5's cache read from $0.50 to $0.30 between our July 16 and July 28 snapshots, deepening that discount from 75% to 85% while leaving the $2.00 base input untouched. Then on August 17 it launched Grok 4.6 at the same $2.00 base with a $0.50 cache read — reverting to the 75% discount for the newer model. If cache reads are where the competition is, xAI just made its newest model less competitive on exactly that axis.

For agentic workloads, where the same system prompt and tool definitions are re-sent on every call, cached input routinely dominates total token volume. In that regime, the cache-read column of the tables above predicts your bill better than the input column does. A provider with a higher base price and cheaper effective caching can win on real invoices.

The cache-read column alone does not settle it, though, because the write fee and the minimum cacheable prefix differ by vendor and neither appears in this table. We normalized those into an effective cost per hit rate in [LLM Cache Pricing 2026](/posts/llm-cache-pricing-2026/), which is the companion to this page for anyone whose bill is mostly repeated input.

**Third, pricing structure — flat versus tiered — is a strategic split, not an accounting detail.** Anthropic explicitly bills its 1M-token context window at standard rates: a 900K-token request costs the same per token as a 9K one. Google and xAI took the opposite path, roughly doubling per-token rates above 200K tokens. OpenAI crossed that line on August 24 with GPT-5.6-sol's $8.00 / $30.00 tier, and from September 1 our collections show a long-context tier on every OpenAI row except GPT-5.4-mini and nano. Both GPT-6 models added this week carry one.

That leaves Anthropic as the only one of the four still billing long context flat. Flat pricing sells predictability to agent builders whose context sizes vary wildly at runtime; tiered pricing protects margins on the expensive long-context serving path. Which structure wins will shape how retrieval-augmented and long-context architectures are designed, because a 2x cliff at 200K tokens is an architectural forcing function.

## The Bigger Picture

The market is not uniformly deflating, and the week to August 17 exposed that "deflation" has been hiding two different things.

Two of the three price moves came with a clock attached. Google's Gemini Flash rows are $0.75 / $3.75 only through December 31, 2026, and the pricing page already prints the January 1 rate beside it. Anthropic used the same instrument in the opposite direction, converting Sonnet 5's introductory rate into the standard one and cancelling an increase it had pre-announced. Both are promotional pricing being managed. Neither says anything about what it costs to serve those models.

DeepSeek is the counterexample, and five weeks later it is a more complicated one than it looked. On August 17 it raised prices outright — 57% on v4-flash input, 136% on output — with no promotional clock and no pre-announced figure. We recorded that as a structural reprice. On September 14 it walked most of it back, but only on one axis and only by replacing the model.

The asymmetry is the finding. Input returned to within a cent of the pre-increase rate; output stayed at more than double it. Across the three states DeepSeek's output-to-input ratio went 2x, then 3x, then 4x — converging on the 3–6x every other provider in these tables charges, and away from the cheap-generation model it launched as. Those two axes bill different workloads. Extraction, classification and retrieval are input-dominated and are close to their July prices again; generation and long-form reasoning are output-dominated and are paying the August increase in full. A vendor that needed margin on generation and not on ingestion would produce exactly this shape, and it is invisible in any table that quotes one blended price per model.

It also shows what a version bump can carry. Nothing on the page reads as a price change — the name that appears in customer code still resolves, and the invoice per token falls. What changed underneath is which model answers. A buyer tracking cost per token would log a discount here; a buyer tracking cost per task has to re-measure, because the thing being measured was replaced.

The September 28 arrivals put that lesson on a larger scale. Five collections have now passed without a single carried row changing price. This week, three of the four arrivals came in below the model they sit beside. Opus 5.5 is 20% under Opus 5; GPT-6-sol is half of GPT-5.6-sol's promotional rate; GPT-6-luna is half of GPT-5.6-luna on input. The September 14 DeepSeek substitution was an early instance of the same pattern.

A cut delivered as a new model ID is a cut the vendor controls. It reaches only buyers who migrate, and migration costs evaluation time, prompt re-tuning and, for Anthropic, a tokenizer that counts roughly 30% more tokens. The old list prices stay in place for everyone who does not move. A flat price table and a deflating market are both true at once; which one describes your bill depends on whether you switch model IDs.

The top of the table has not joined in. Fable 5 and 5.1 hold $10 / $50 and OpenAI's pro tier $30 / $180, on the theory that frontier capability is price-inelastic. What is newly in question is the assumption underneath the rest of the table: that a falling number means the same product got cheaper.

This matters beyond procurement because API pricing is becoming the cost structure of AI-mediated traffic itself. As we documented in our analysis of [ChatGPT ads and AEO economics](/posts/chatgpt-ads-2026-aeo-reddit-citations/), AI answers are now a monetized distribution channel; the margin between what a model costs to run and what its answers earn determines which models power that channel. And token efficiency is not only a provider-side variable — [vague prompts inflate token consumption and degrade output quality simultaneously](/posts/gigo-prompts-2026-why-vague-prompts-fail/), so prompt discipline compounds directly with the per-token rates in these tables.

## How to Choose: Recommendations by Workload

**High-volume extraction and classification.** Gemini 2.5 Flash-Lite ($0.10 / $0.40) holds the price floor among maintained models, and GPT-6-luna ($0.10 / $0.50) now shares it on input. For input-heavy classification the two are effectively tied; output-heavy extraction favours Flash-Lite by 20%. DeepSeek sits at $0.15 / $0.60, tied with Mistral Small 4. Its 1M context and near-free cache reads make it the stronger pick as soon as documents repeat across requests.

**Agentic workloads with heavy context reuse.** Rank by cache-read price, not input price: DeepSeek flash ($0.003), Gemini 2.5 Flash-Lite and GPT-6-luna ($0.01 each), GPT-5.4-nano and GPT-5.6-luna ($0.02 each), Claude Haiku 4.5 ($0.10). If your agent re-sends a 50K-token system prompt on every call, these numbers are your effective input price. DeepSeek's September 14 swap restored a 3.3x lead over Flash-Lite here, up from the 1.4x it had been cut to in August — but the lead now belongs to a model that has only been in the table since September 14, not to the one that was benchmarked into these pipelines.

**Long-context analysis.** Claude Sonnet 5 ($2.00 / $10.00, flat 1M context) is the standout, and since August 17 it is no longer on a clock — flagship-adjacent quality, no long-context surcharge, and no scheduled increase. GPT-6-sol matches Sonnet 5's $2.00 / $10.00 exactly, but not above its long-context threshold, where OpenAI bills $4.00 / $15.00. Grok 4.3 ($1.25 / $2.50 base, 1M) undercuts both on sticker price, but only if your prompts stay under the 200K-token cliff where xAI's rates double.

**Frontier reasoning.** Claude Opus 5.5 and GPT-5.6-sol share the cheapest rate in this tier at $4.00 / $20.00. Only Opus 5.5's rate is standard; OpenAI commits to sol's only through 2026-11-21. Opus 5.5 is therefore the value anchor for any budget that runs past November, and its $0.20 cache read is half of sol's.

Opus 5 and Opus 4.5 through 4.8 stay at $5.00 / $25.00 for a pinned older revision. Moving to Opus 5.5 cuts the sticker by 20%, less whatever its tokenizer adds against an Opus 4.6-or-earlier baseline. Claude Fable 5 ($10.00 / $50.00) prices above all of them. The pro-grade OpenAI models ($30.00 / $180.00) only make sense where a single hard task justifies a 7.5–9x premium over Opus 5.5.

## Limitations

- **Standard tier only.** Batch discounts (typically 50% off at Anthropic, OpenAI, Google, and Mistral) and regional/data-residency surcharges (10% at OpenAI and Anthropic for US-only routing) are not baked into the tables.
- **Context windows marked "n/p"** are not published on the provider's official pricing page; we do not fill gaps from third-party sources.
- **Mistral does not publish cache-read pricing**, so its rows cannot be compared on the caching dimension.
- **Coverage is six providers (51 models tracked).** The tables show the notable rows and footnote price-identical siblings, so the visible row count is lower than the tracked count. Open-source hosted inference (Groq, Together, DeepInfra) and Alibaba/Qwen are excluded from this edition; we would rather ship a fully verified narrow table than a broad one with stale rows.
- **DeepSeek's rows are off-peak rates and are not strictly comparable to the rest of the table.** Every other provider publishes one rate that applies at all hours. DeepSeek publishes two, and a workload that runs during the 01:00–04:00 and 06:00–10:00 UTC peak windows pays exactly double the figures shown. We record the lower tier for consistency with how tiered pricing is handled elsewhere, not because it is the rate most users will pay.
- **Prices are list prices.** Enterprise volume discounts are negotiated and unobservable.

## Update Cadence and Changelog

This table is refreshed **weekly** from the six official pricing pages, and every change lands here as a dated entry. Official pricing pages only show current prices — the change history below, and the snapshot series behind it, is what this page accumulates that they do not.

| Date | Change |
|---|---|
| 2026-09-28 | **No carried price moved; four models arrived, three of them cheaper than the model they sit beside.** All 47 rows carried from 2026-09-21 hold their input, output and cache-read prices, a fifth consecutive flat collection across all six providers. Tracked set 47 → 51, nothing removed. Added: **Claude Opus 5.5** at $4.00 / $20.00 (cache read $0.20), 20% under Opus 5 and priced at a new 0.05x cache-read multiplier — Anthropic's third, beside 0.1x and 0.025x. Added: **GPT-6-sol** at $2.00 / $10.00 (cache read $0.20; long context $4.00 / $15.00), half of GPT-5.6-sol's promotional rate. Added: **GPT-6-luna** at $0.10 / $0.50 (cache read $0.01; long context $0.20 / $0.75), level with Gemini 2.5 Flash-Lite on input. Added: **Grok 4.7** at $2.00 / $6.00 (cache read $0.50), identical to Grok 4.6 at both tiers. No older row was repriced to meet the new ones. Two vendor statements this page quoted are no longer on the pages: Anthropic's sentence that Sonnet 5's $2 / $10 "is now the standard price", and DeepSeek's statement that v4-pro service continues past 2026-09-14. Neither price changed. xAI's rows are now read from its [pricing page](https://docs.x.ai/developers/pricing), because its models page lists only Grok 4.7. **Correction:** this page said OpenAI's rows other than GPT-5.6-sol had no long-context tier. Our 2026-09-01 collection already recorded a tier on every OpenAI row except GPT-5.4-mini and nano, and the text was not updated. Fixed in the fine print and both long-context FAQ answers. Newly recorded outside the tracked set: Google's Gemini Omni Flash ($1.50 / $9.00 text output), pending a scope decision. |
| 2026-09-21 | **Nothing moved.** All 47 tracked rows hold the input, output and cache-read prices recorded on 2026-09-14, across all six providers, and no model entered or left the tracked set. This is the fourth consecutive collection without a price change on the carried set and the first of the four in which the set is also identical in composition — the three before it each carried an arrival, a removal or a substitution. Two entries are recorded that are not price changes. Anthropic's tokenizer split (Claude 4.7 and later counting roughly 30% more tokens for the same text) is now named row by row in our snapshot series; it has been on the provider's page and in this post's Fine Print section since July, and is recorded now so that the snapshot files do not read as though the eight affected rows were directly comparable to the five that are not. And OpenAI's pricing page lists a cyber line — gpt-5.6-cyber and gpt-5.5-cyber, both $12.50 / $75.00 with cached input $1.25 — that this series had never recorded; that gpt-5.5-cyber pairs with a generation already outside our July 16 scope suggests it predates the tracked set rather than arriving this week, but the page carries no dates, so that is inference and the rows stay out pending a scope decision. Mistral added GLM 5.3 at $1.40 / $4.40, a third-party Z.ai model resold on its API, joining the GLM 5.2 resale already excluded on the same grounds. Two dated commitments still stand: GPT-5.6-sol through at least 2026-11-21, and the three Gemini Flash rows through 2026-12-31. |
| 2026-09-14 | **DeepSeek retired v4-flash; the row was replaced, not repriced.** The pricing page now lists `deepseek-flash` (build DeepSeek-V4.1-Flash) at $0.15 / $0.60 off-peak, cache read $0.003, and states that the legacy ids deepseek-v4-flash and deepseek-v4-flash-vision-exp are still accepted but that the models behind them have been retired, with those requests served and billed at the Flash rate. Against the rate v4-flash carried last week this is −31.8% on input, −9.1% on output and −57.1% on cache read; against the rate it carried before the 2026-08-17 increase it is +7% on input and +114% on output. The August increase was therefore reversed on input and kept on output, and DeepSeek's output-to-input ratio went 2x (pre-August) to 3x to 4x across the three states. The 98% cache discount retakes the deepest-cache position from Claude Fable 5.1 eight days after Anthropic took it. **No other row moved** — a third consecutive collection with no price change on the carried set, across all six providers. Tracked set holds at 47: one out, one in. DeepSeek also states that **v4-pro API service continues past 2026-09-14 with billing unchanged**, cancelling a date that had been read as an end-of-life; v4-pro's own prices are untouched. Two dated commitments still stand: GPT-5.6-sol through at least 2026-11-21, and the three Gemini Flash rows through 2026-12-31. Still outside the tracked set and unchanged: Mistral's resale of Z.ai GLM 5.2 and the Ministral 3 line. |
| 2026-09-07 | **No price change, four arrivals.** All 43 rows carried over from 2026-09-01 hold their prices — a second consecutive collection with no move anywhere across the six providers. Tracked set 43 → 47. Added: **Claude Fable 5.1** and **Claude Mythos 5.1** at $10.00 / $50.00, matching Fable 5 and Mythos 5 on base rates but pricing cache hits at 0.025x base input ($0.25 / 1M) against the 0.1x every other Claude model uses — the first split in Anthropic's cache-read multiplier recorded in this series, and at 97.5% the deepest cache discount in these tables. Added: **GPT-6-astra** at $10.00 / $50.00 (cache read $1.00) with a $20.00 / $75.00 long-context tier, the most expensive OpenAI row outside the $30.00 / $180.00 pro tier. Added: **Gemini 3.8 Flash** at $0.75 / $3.75 (cache read $0.075) on the same 2026-12-31 introductory expiry as Gemini 3.7 and 3.6 Flash, taking the rows scheduled to double on 2027-01-01 from two to three. Nothing was removed. Collected Monday 2026-09-07, six days after the previous file rather than seven, because 2026-09-01 was collected on a Tuesday. Two dated commitments still stand: GPT-5.6-sol through at least 2026-11-21, and the three Gemini Flash rows through 2026-12-31. Still outside the tracked set and unchanged: Mistral's resale of Z.ai GLM 5.2, the Ministral 3 line, and DeepSeek's deepseek-v4-flash-vision-exp. |
| 2026-09-01 | **No change.** All 43 tracked rows hold the prices recorded on 2026-08-24, across all six providers — the first collection in this series with no price move anywhere. No model entered or left the tracked set. Collected Tuesday 2026-09-01 rather than Monday; the 2026-08-31 slot was missed and is left as a gap rather than backfilled, so this entry covers eight days. Two dated commitments still stand on the pages: GPT-5.6-sol's promotional rate through at least 2026-11-21, and the 2026-12-31 expiry on both Gemini Flash rows. Anthropic's cancelled Sonnet 5 increase reached its 2026-09-01 date with the rate unmoved. Still outside the tracked set and unchanged: Mistral's resale of Z.ai GLM 5.2 and the Ministral 3 line. |
| 2026-08-24 | **OpenAI cut GPT-5.6-sol** from $5.00 / $30.00 to $4.00 / $20.00 (cache read $0.50 → $0.40) — input −20%, output −33.3%, the largest single-model cut recorded here since the GPT-5.6-luna cut on 2026-08-03. The page marks the rate promotional and available at least through 2026-11-21, so it is recorded as a dated cut rather than a new standard price. The same model gained OpenAI's **first long-context tier** at $8.00 / $30.00 (cache read $0.80); every other OpenAI row stays flat. GPT-5.6-terra and GPT-5.6-luna did not move, and no other provider changed a price. No models added or removed — tracked set holds at 43. Still outside the tracked set and unchanged from last week: Mistral's resale of Z.ai GLM 5.2 ($1.40 / $4.40) and the Ministral 3 line. DeepSeek added deepseek-v4-flash-vision-exp at v4-flash rates, excluded here as a non-text model. |
| 2026-08-17 | The largest week in the series. **DeepSeek raised prices**, the first increase recorded here from any provider: v4-flash $0.14 / $0.28 → $0.22 / $0.66 (cache read $0.0028 → $0.007) and v4-pro $0.435 / $0.87 → $0.66 / $1.98 (cache read $0.003625 → $0.022), all off-peak. This is the increase the 2026-08-10 entry flagged as expected but unsized. DeepSeek also shipped build V4-Pro-0813. **Google halved Gemini 3.6 Flash** to $0.75 / $3.75 (cache read $0.075) to match new arrival **Gemini 3.7 Flash**, launched 2026-08-13 at the same rate; both are promotional through 2026-12-31 and double on 2027-01-01. **Anthropic cancelled the Claude Sonnet 5 increase** — $2.00 / $10.00 is now the standard price and the 2026-09-01 move to $3.00 / $15.00 will not occur. Added: Gemini 3.7 Flash, Grok 4.6 ($2.00 / $6.00, cache read $0.50). Removed: Claude Opus 4.1, retired from the first-party API on 2026-08-05, and Magistral Medium, Magistral Small, Devstral 2, and Devstral Small 2, all absent from Mistral's pricing page with retirement dates between 2025-10-31 and 2026-07-31. Those five had been carried in earlier snapshots after their retirement dates passed; the earlier files are left as collected rather than corrected. Tracked set: 46 → 43 models. |
| 2026-08-10 | No change. Every row in the tables above holds last week's price, and no model entered or left the six providers' pricing pages — the first flat week since the series began. Two things visible on the pages but not yet in the table: Anthropic's Sonnet 5 introductory rate still expires 2026-08-31, and DeepSeek's pricing page states that a significant increase is expected, without naming a date or a figure. Neither is recorded as a price until it takes effect. |
| 2026-08-03 | OpenAI cut two GPT-5.6 models: luna from $1.00 / $6.00 to $0.20 / $1.20 (−80%, cache read $0.10 → $0.02) and terra from $2.50 / $15.00 to $2.00 / $12.00 (−20%, cache read $0.25 → $0.20). Both were cross-verified against OpenAI's models page before recording. No models added or removed; every other row across the six providers was unchanged. Gemini 3.5 Flash-Lite's $0.03 cache read was recorded for the first time — a gap in the prior collection, not a price change. |
| 2026-07-28 | Added Claude Opus 5 and Gemini 3.6 Flash. Grok 4.5 cache read cut from $0.50 to $0.30 (−40%), the only base-table price change. DeepSeek's legacy IDs retired on schedule. No snapshot was taken on 2026-07-20 or 2026-07-27; those two weeks are absent from the series and were not reconstructed. |
| 2026-07-16 | Initial 2026 edition: baseline of 39 models across 6 providers. Supersedes the March 2026 draft dataset. |

## FAQ: LLM API Pricing 2026

### What is the cheapest LLM API in 2026?

Gemini 2.5 Flash-Lite, at $0.10 input / $0.40 output per 1M tokens. OpenAI's GPT-6-luna, added on September 28, 2026, ties it on input and cached input and costs $0.10 more on output. DeepSeek follows at $0.15 / $0.60, tied with Mistral Small 4, after retiring v4-flash on September 14 and serving the name from `deepseek-flash`. It is cheapest of all on cached input at $0.003 per 1M — a 98% discount — so a workload that reuses context should be priced on the cache-read column rather than this one.

### Is Claude Sonnet 5's price going up on September 1, 2026?

No. Anthropic cancelled the increase, and the $2.00 / $10.00 rate announced at launch as introductory has held in every collection since. After the cancellation the pricing page stated that the rate had become standard and that the move to $3.00 / $15.00 would not occur. By September 28 that statement had been removed, and the page now lists $2.00 / $10.00 with no scheduled change. If you budgeted a 50% cost increase for Sonnet 5 workloads from September, that reserve can be released.

### Why is Claude Fable 5.1's cache read cheaper than Claude Opus 5's?

Anthropic prices a cache hit as a multiplier on base input, and since September 7, 2026 it has not used one multiplier for the whole line. Claude Fable 5.1 and Claude Mythos 5.1 bill cache hits at 0.025x base input ($0.25 per 1M tokens). Claude Opus 5.5, added on September 28, bills them at 0.05x ($0.20). Every other Claude model, Opus 5 included, stays at 0.1x. Anthropic's most expensive models carry its deepest cache discount, at 97.5%, and the multiplier is now set per model.

### Are per-token prices directly comparable across providers?

Only approximately. Anthropic's newest models tokenize the same text into roughly 30% more tokens than its earlier models, and other providers publish no tokenizer efficiency data at all. Two models with the same $/1M price can produce meaningfully different invoices for the same documents — compare cost per task when the decision matters.

### Do these prices include long-context surcharges?

No — tables record base tiers. Google and xAI roughly double per-token rates for prompts above 200K tokens (footnoted per table). OpenAI lists a long-context tier on ten of its twelve tracked rows, every one except GPT-5.4-mini and nano; GPT-5.6-sol, for example, is billed at $8.00 / $30.00 on long context against a $4.00 / $20.00 base. Anthropic bills its full 1M context at standard rates.

### If no price changed this week, can I assume my bill is flat?

Not on Anthropic models. The per-token rates in these tables are unchanged, but Anthropic's page states that Claude 4.7 and later models count roughly 30% more tokens for the same text than Sonnet 4.6 and earlier. A price that holds and a token count that rises produce a bill that rises. Cost-per-token is the wrong unit for any comparison that crosses that line; measure cost per task instead.

### How often is this table updated?

Weekly, from official provider pages only, with every change recorded in the changelog above. Missed weeks are marked as gaps rather than back-filled: the 2026-07-20 and 2026-07-27 snapshots were not taken, and reconstructing them after the fact would put unobserved prices into a series whose whole value rests on every row having been read off a live page. The series began July 16, 2026 and compounds into a price-change history that current-price-only official pages do not offer.

## Related Resources

- [ChatGPT Ads 2026: AEO Traffic and Reddit Citations](/posts/chatgpt-ads-2026-aeo-reddit-citations/) — the revenue side of the same equation: what AI-mediated answers earn
- [GIGO Prompt Engineering: Why Vague Prompts Fail](/posts/gigo-prompts-2026-why-vague-prompts-fail/) — cutting token waste at the prompt level compounds with every rate in this table
