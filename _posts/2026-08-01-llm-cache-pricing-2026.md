---
title: "LLM Cache Pricing 2026: The Real Cost of Cached Input"
description: "LLM cache pricing 2026 normalized across six providers: effective input cost at real hit rates, hidden write fees, and which vendors publish nothing at all."
date: 2026-08-01 10:00:00 +0000
last_modified_at: 2026-09-14 16:30:00 +0000
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
    a: "The cached-read discount converged on 90% at OpenAI, Google, and most of Anthropic's line, and two vendors have since left that consensus: Anthropic discounts 97.5% on Claude Fable 5.1 and Mythos 5.1, DeepSeek 98% on deepseek-flash. xAI discounts 75–85%. The discount applies only to the cached portion of your prompt, so the saving you actually see is roughly your cache hit rate times the discount. At a 50% hit rate a 90% discount is a 45% saving on input, not 90%."
  - q: "Do you pay to write to the cache?"
    a: "At Anthropic, yes and always: a 5-minute cache write costs 1.25x base input, a 1-hour write 2x. OpenAI introduced the same 1.25x write charge with the GPT-5.6 family; models before it had none. Google charges no write fee but bills cache storage per hour. xAI, DeepSeek, and Mistral publish no write price at all."
  - q: "Which LLM API is cheapest for a cache-heavy agent?"
    a: "It depends on your hit rate, and the hinge moved back into normal agent territory on 2026-09-14. Gemini 2.5 Flash-Lite is cheapest from 0% to 87.7%; above that DeepSeek flash wins, reaching $0.0104 per 1M effective input tokens at a 95% hit rate against Flash-Lite's $0.0145. That crossover was 84.7% before August 17, 97.6% after it, and 87.7% now — measure your own hit rate rather than inheriting the answer."
  - q: "Is prompt caching automatic or do I have to enable it?"
    a: "OpenAI, Google, DeepSeek, and xAI cache automatically. Anthropic requires an explicit cache_control field. The distinction now carries a price: because OpenAI's GPT-5.6 family caches automatically and bills writes at 1.25x, a long prompt you never reuse can be billed above the base rate unless you set prompt_cache_options.mode to explicit."
  - q: "Why can't I compare cache prices straight from provider pricing pages?"
    a: "Because no two publish the same fields. Anthropic states multipliers, DeepSeek an absolute cache-hit price, xAI a single cached-input column, Google a per-hour storage rate, and Mistral only a headline -90% with no per-model figure. Four of the six publish no cache TTL. Normalizing them to one unit is the reason this table exists."
data_updated: 2026-09-14
author: jsonhouse
---

Prompt caching is sold as a 90% discount, and at the sticker level that is now true almost everywhere: Anthropic, OpenAI, and Google all price a cache read at exactly one tenth of base input. The number that decides your invoice is different. It is the **effective input price** — what you pay per million input tokens once your actual cache hit rate, the write surcharge, and the storage fee are all folded in.

On that measure the answer reversed on 2026-09-14, four weeks after it had reversed the other way. DeepSeek's August rise had pushed the budget-tier crossover out to 97.6%, past where any real workload sits, and sticker price took over the ranking. Retiring v4-flash for `deepseek-flash` at $0.15 base / $0.003 cache read **brought that crossover back to 87.7%** — inside the band where long-running agents actually operate. At a 95% hit rate DeepSeek is once again the cheapest row on this page.

A second flip opened at the opposite end of the price list. Anthropic's 0.025x cache-read multiplier on Claude Fable 5.1 means a $10.00 model undercuts the $5.00 Claude Opus 5 above a 95.2% hit rate. This page normalizes cache pricing for 18 models across six providers to a single unit, using prices collected on 2026-09-14.

## TL;DR

- **A crossover is back inside the agent band.** Gemini 2.5 Flash-Lite and DeepSeek flash cross at **87.7%** — down from the 97.6% the August price rise had pushed it to. Below that hit rate Flash-Lite is cheaper; above it DeepSeek is.
- **Sticker price lost the 95% column again.** At `h = 95%` DeepSeek flash costs $0.0104 per 1M effective input tokens against Flash-Lite's $0.0145. It held that lead before 2026-08-17, lost it for four weeks, and has it back.
- **The flagship band now flips too.** Claude Fable 5.1 discounts a cache read 97.5% against Claude Opus 5's 90%, so the $10.00 model is cheaper than the $5.00 one above a 95.2% hit rate — the first crossover this page has recorded at the top of the price list rather than the bottom.
- **The discount converged, then two vendors left the consensus.** 90% at OpenAI, Google, and most of Anthropic's line; 75–85% at xAI; 97.5% on Anthropic's two newest models; 96.7% and 98% at DeepSeek.
- **Caching still pays after two calls.** Even at a 2x write multiplier, reusing a prefix three times beats not caching. Write fees are a rounding error for agents — and a real penalty for one-shot prompts.
- **"90% off" is not a 90% saving.** The discount applies only to the cached share of your prompt. At a 50% hit rate it is a 45% cut.

## Methodology

Base input and cache-read prices were collected on **2026-09-14** from the six providers' official pricing pages, the same sources and normalization used in our [weekly LLM API pricing table](/posts/llm-api-pricing-2026/): [Anthropic](https://platform.claude.com/docs/en/docs/about-claude/pricing), [OpenAI](https://developers.openai.com/api/docs/pricing), [Google](https://ai.google.dev/gemini-api/docs/pricing), [xAI](https://docs.x.ai/docs/models), [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing), [Mistral](https://mistral.ai/pricing/api). Caching mechanics — write cost, storage fee, TTL, trigger, minimum cacheable length — were last re-read from each provider's prompt-caching documentation on 2026-08-03 and are unchanged: [Anthropic](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching), [OpenAI](https://developers.openai.com/api/docs/guides/prompt-caching), [Google](https://ai.google.dev/gemini-api/docs/caching), [xAI](https://docs.x.ai/developers/advanced-api-usage/prompt-caching/usage-and-pricing), and [DeepSeek](https://api-docs.deepseek.com/guides/kv_cache).

Effective input price is computed as `base x (1 - h) + cache_read x h`, where `h` is the cache hit rate: the share of input tokens served from cache. It deliberately excludes write and storage costs, which are handled separately below, because those are one-time or time-based rather than per-token and would otherwise make the columns non-comparable.

Every cell in the table below except the `h = 0%` column is computed by us from vendor rate cards; `h = 0%` is the vendor's published base input price. All figures are USD per 1M tokens at the standard, non-batch, base long-context tier. Where a provider publishes nothing, the cell reads "not published" — we do not derive a figure and present it as a price. The one derivation we do make is labelled as such.

## Effective Input Price by Cache Hit Rate

`h = 0%` is the sticker price. `h = 95%` is a realistic figure for an agent that re-sends a stable system prompt and tool definitions on every turn.

| Model | Provider | h = 0% (vendor) | h = 50% (jsonhouse derived) | h = 80% (jsonhouse derived) | h = 95% (jsonhouse derived) | Discount (jsonhouse derived) |
|---|---|---|---|---|---|---|
| Claude Fable 5.1 | Anthropic | $10.0000 | $5.1250 | $2.2000 | $0.7375 | 97.5% |
| Claude Opus 5 | Anthropic | $5.0000 | $2.7500 | $1.4000 | $0.7250 | 90% |
| GPT-5.6-sol | OpenAI | $4.0000 | $2.2000 | $1.1200 | $0.5800 | 90% |
| Claude Sonnet 5 | Anthropic | $2.0000 | $1.1000 | $0.5600 | $0.2900 | 90% |
| GPT-5.6-terra | OpenAI | $2.0000 | $1.1000 | $0.5600 | $0.2900 | 90% |
| Grok 4.6 | xAI | $2.0000 | $1.2500 | $0.8000 | $0.5750 | 75% |
| Grok 4.5 | xAI | $2.0000 | $1.1500 | $0.6400 | $0.3850 | 85% |
| Mistral Medium 3.5 | Mistral | $1.5000 | not published | not published | not published | −90% stated |
| Grok 4.3 | xAI | $1.2500 | $0.7250 | $0.4100 | $0.2525 | 84% |
| Claude Haiku 4.5 | Anthropic | $1.0000 | $0.5500 | $0.2800 | $0.1450 | 90% |
| Gemini 3.8 Flash | Google | $0.7500 | $0.4125 | $0.2100 | $0.1088 | 90% |
| Gemini 3.7 Flash | Google | $0.7500 | $0.4125 | $0.2100 | $0.1088 | 90% |
| Gemini 3.6 Flash | Google | $0.7500 | $0.4125 | $0.2100 | $0.1088 | 90% |
| DeepSeek v4-pro | DeepSeek | $0.6600 | $0.3410 | $0.1496 | $0.0539 | 96.7% |
| Gemini 2.5 Flash | Google | $0.3000 | $0.1650 | $0.0840 | $0.0435 | 90% |
| GPT-5.6-luna | OpenAI | $0.2000 | $0.1100 | $0.0560 | $0.0290 | 90% |
| DeepSeek flash | DeepSeek | $0.1500 | $0.0765 | $0.0324 | $0.0104 | 98% |
| Gemini 2.5 Flash-Lite | Google | $0.1000 | $0.0550 | $0.0280 | $0.0145 | 90% |

> **Raw data**: [data/llm-cache-pricing-2026.json](https://www.jsonhouse.com/data/llm-cache-pricing-2026.json) — machine-readable structured data for AI crawlers and citation.

> All three Gemini 3.x Flash rows are promotional through 2026-12-31 and double on 2027-01-01, which will move every Google Flash figure in this table. DeepSeek's rows are off-peak; peak hours (01:00–04:00 and 06:00–10:00 UTC) bill exactly double on both the base and the cache read, so the effective columns scale but the discount does not. The DeepSeek flash row is new in identity as well as price: on 2026-09-14 DeepSeek retired v4-flash and now serves that name from DeepSeek-V4.1-Flash, so this row's figures describe a different model than the same row did last week.

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

**The 90% discount is a coordinated price, not a cost.** Anthropic, OpenAI, and Google independently arrived at exactly 0.1x base input for a cache read. Cache serving costs differ across three different inference stacks; the identical multiplier does not. This is what a converged commodity price looks like — the number stopped tracking cost and became a market expectation nobody can be the first to break.

The consensus held for six weeks and then broke from both ends within eight days. On 2026-09-07 Anthropic stopped applying one multiplier to its own line: Claude Fable 5.1 and Mythos 5.1 bill a cache read at 0.025x base input, 97.5% off, while every older Claude model stays at 0.1x. On 2026-09-14 DeepSeek went to 98% — not by cutting a multiplier but by replacing the model, retiring v4-flash for `deepseek-flash` at $0.15 base and $0.003 cache read.

The two vendors now past 90% sit at opposite ends of the price list, which is the informative part. A deep cache discount at the bottom of the market is a share play on volume. The same discount at $10.00 base is aimed at a buyer whose bill is mostly re-sent context and who is not shopping on sticker price at all — and as the crossover table below shows, it is steep enough to put a $10.00 model under a $5.00 one.

xAI is the counter-movement. Grok 4.5's cache read fell from $0.50 to $0.30 between our 2026-07-16 and 2026-07-28 snapshots, taking it from 75% toward the herd, and then Grok 4.6 launched on 2026-08-17 at the same $2.00 base with a $0.50 cache read — back to 75%. The newer model is strictly worse on the axis the market says it competes on.

**Write fees appeared exactly when caching became automatic.** Anthropic has always charged to write, and has always required you to ask for caching. OpenAI did the reverse for years: automatic caching, free writes. With GPT-5.6 it added a 1.25x write charge while keeping caching automatic and on by default above 1,024 tokens.

Those two facts interact in a way the documentation does not resolve. OpenAI's guide says an eligible prefix "may" be cached and that written tokens bill at the write rate; it does not say whether a write is charged on a prompt that is never read again. There is an opt-out — `prompt_cache_options.mode` set to `explicit` — and the existence of an opt-out is itself informative. But the cost of failing to use it is not published, and one-shot long-prompt workloads are exactly where it would bite.

**Storage is Google's version of the same charge, moved in time.** Google takes no write fee and instead bills $1.00 per 1M cached tokens per hour, rising to $4.50 on Gemini 2.5 Pro and 3.1 Pro. For an agent that keeps a 200K-token context warm all day, that is a real line item that never appears in a per-token comparison. Anthropic front-loads the same economics into the write; Google meters it. Neither is hidden, but they are not comparable without doing the arithmetic yourself — which is the point of this page.

## Where the Ranking Flips

Cache hit rate does not merely scale costs down uniformly. It reorders them, because providers discount by different amounts from different starting points.

On 2026-08-03 five pairs crossed inside the 0–100% range and three of them crossed in the same 83–85% band. DeepSeek's August rise pushed every budget-tier crossover out past 97%, and this page reported that the flip had stopped happening where agents run. **That lasted four weeks.** Seven pairs now cross, and one of them is back inside the band:

| Cheaper below the crossover | Cheaper above it | Crossover hit rate (jsonhouse derived) | Effective price at crossover (jsonhouse derived) |
|---|---|---|---|
| Gemini 2.5 Flash-Lite | DeepSeek flash | 87.7% | $0.0211 / 1M |
| Claude Opus 5 | Claude Fable 5.1 | 95.2% | $0.7143 / 1M |
| Grok 4.6 | GPT-5.6-sol | 95.2% | $0.5714 / 1M |
| Grok 4.6 | Claude Fable 5.1 | 97.0% | $0.5455 / 1M |
| GPT-5.6-sol | Claude Fable 5.1 | 97.6% | $0.4878 / 1M |
| Gemini 2.5 Flash | DeepSeek v4-pro | 97.8% | $0.0359 / 1M |
| Grok 4.5 | Claude Fable 5.1 | 99.4% | $0.3106 / 1M |

**The budget crossover came back 10 points.** Flash-Lite × DeepSeek moved from 97.6% to 87.7%, because DeepSeek cut base and cache read together: the sticker gap against Flash-Lite narrowed from $0.12 to $0.05 while the discount slope stayed steep. That is the same tool working in the direction it is designed for, after four weeks of working against itself. One crossover vanished in the process — GPT-5.6-luna × DeepSeek at 60.6% is gone, because `deepseek-flash` now beats luna on base price and on cache read simultaneously, and a model losing on both axes cannot win at any hit rate.

**Four of the seven crossovers are new, and all four involve Claude Fable 5.1.** They are the first this page has recorded at the top of the price list. The Opus 5 pair is the one to look at: above a 95.2% hit rate, Anthropic's $10.00 model costs less per effective input token than its own $5.00 model. Sticker price and effective price now disagree inside a single vendor's catalogue, which is a thing a procurement spreadsheet built on base rates cannot represent at all.

**One correction.** The 2026-08-24 entry below recorded that OpenAI's cut to GPT-5.6-sol moved no crossover, on the reasoning that nothing in the flagship band was priced where sol could cross it. That was wrong. Grok 4.6 × GPT-5.6-sol sat at exactly 100% before the cut — mathematically present, unreachable in practice — and the cut brought it to 95.2%. It has been in range for three weeks and this page missed it. The crossover set is now computed exhaustively over all pairs each week rather than by inspecting the pairs we expect to move.

The practical consequence is that **sticker price is no longer sufficient at either end of the table**. A plain [pricing table](/posts/llm-api-pricing-2026/) now ranks the wrong quantity for long-running agents in the budget tier and for heavy-context work in the flagship tier, and it lands on the right answer only in the middle. That is close to the reverse of what this page reported a fortnight ago, and the reversal took two vendor changes eight days apart.

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

It also changes who wins, and the last four weeks ran the mechanism in both directions on the same vendor. A provider with a mediocre sticker price and an aggressive cache discount can undercut a cheaper rival on real invoices — DeepSeek did that above an 84% hit rate until 2026-08-17, lost it when it raised its base, and recovered it on 2026-09-14 when the replacement model brought the base back down. The discount was never the asset on its own. It is leverage on the sticker price, and leverage moves with the thing it is levered on.

Claude Fable 5.1 is the same lesson from the other side. A 97.5% discount on a $10.00 base beats a 90% discount on a $5.00 base above 95.2% — enough leverage to invert two models in the same catalogue. That is a real inversion, and also a narrow one: it requires a hit rate almost no workload sustains by accident, which is precisely the buyer Anthropic appears to be pricing for.

## How to Choose: Recommendations by Workload

**Stateless, high-volume extraction (hit rate near 0%).** Rank on sticker price and ignore this page's other columns. Gemini 2.5 Flash-Lite ($0.10) leads, then DeepSeek flash ($0.15) and GPT-5.6-luna ($0.20).

**Long-running agents with a stable system prompt (hit rate above 85%).** The order inverts again, and the hinge is 87.7%. At `h = 95%` it is DeepSeek flash ($0.0104), Gemini 2.5 Flash-Lite ($0.0145), GPT-5.6-luna ($0.0290), Gemini 2.5 Flash ($0.0435), DeepSeek v4-pro ($0.0539). Measure your hit rate before choosing: the two leaders swap across 87.7%, and this crossover has now moved three times in six weeks. Note also that the DeepSeek row is a different model than it was last week, so a benchmark you ran against v4-flash no longer describes what you would be buying.

**Heavy-context work on Claude (hit rate above 95%).** Check Claude Fable 5.1 against Claude Opus 5 rather than assuming the cheaper sticker wins. Above 95.2% the $10.00 model is the cheaper one per effective input token, and the gap widens fast from there — at 95% Opus 5 still leads $0.7250 to $0.7375, but by 98% it is Fable 5.1 at $0.4450 against Opus 5's $0.5900. Below that hit rate Opus 5 wins and the comparison is not close.

**One-shot long prompts on OpenAI GPT-5.6+.** Measure `cache_write_tokens` on a representative request before assuming caching is free. If the prompt is never reused, `prompt_cache_options.mode` set to `explicit` is the documented way to suppress the implicit breakpoint.

**Anything on Claude.** Check the minimum cacheable length for your specific model before budgeting a saving. At 4,096 tokens on Haiku 4.5 and Opus 4.5, a prompt that caches fine on Opus 5 will silently not cache, with no error returned.

**Anything on Mistral.** You cannot model cache economics from published data. Treat the −90% headline as unverified until per-model rates appear.

## Limitations

- **Effective price excludes write and storage costs.** Those are one-time or hourly, not per-token, and are analyzed separately above rather than folded into a single number that would hide which component moved.
- **Cache hit rate is an input, not a measurement.** We publish the formula and the price inputs; we have not measured hit rates on real workloads. That is a separate experiment and a future post.
- **Four of six providers publish no TTL**, so time-based cache expiry cannot be modelled for them. Real hit rates on those providers may be materially lower than configured.
- **Mistral rows are unfillable**, not estimated. Its cache economics are outside this comparison until it publishes per-model rates.
- **Prices are list prices** at the standard non-batch tier. Batch discounts and negotiated enterprise rates are excluded.
- **Coverage is 18 models across six providers**, chosen to span every tier and every disclosure pattern rather than to be exhaustive.
- **Three Google rows and both DeepSeek rows are conditional prices.** Gemini 3.6, 3.7 and 3.8 Flash are promotional through 2026-12-31 and double after it; DeepSeek's figures are off-peak and bill double during peak UTC windows. Both effective columns and crossovers move with them.
- **The DeepSeek flash row changed model, not just price, on 2026-09-14.** Its figures are comparable to the previous v4-flash row as a line item on an invoice, but not as a measurement of the same product. Week-over-week deltas on that row should be read as a substitution.

## Update Cadence and Changelog

This page is refreshed **weekly** from the same snapshot series that backs our pricing table, and every change lands below as a dated entry. Caching mechanics — write fees, TTLs, minimum lengths — are re-read from provider documentation monthly, since they change far more slowly than prices.

| Date | Change |
|---|---|
| 2026-09-14 | **Both ends of the table left the 90% consensus, and a crossover returned to the agent band.** DeepSeek retired v4-flash and now serves that name from `deepseek-flash` (build DeepSeek-V4.1-Flash) at $0.15 base / $0.003 cache read, a 98% discount — the row is a substitution, not a repricing, and its figures describe a different model than last week's. Effective prices on it fall to $0.0765 at h = 50%, $0.0324 at h = 80%, $0.0104 at h = 95%, which takes back the `h = 95%` lead from Gemini 2.5 Flash-Lite. **Flash-Lite × DeepSeek moved from 97.6% to 87.7%**, back inside the range where long-running agents operate, and **GPT-5.6-luna × DeepSeek (60.6%) vanished** because the new row beats luna on base and cache read at once. Added two rows missed in the 2026-09-07 collection, which this page skipped: **Claude Fable 5.1** ($10.00 / $0.25, a 97.5% discount — the first Anthropic row not on the flat 0.1x multiplier) and **Gemini 3.8 Flash** ($0.75 / $0.075), taking the table from 16 models to 18. Fable 5.1 opens four crossovers at the top of the price list, including **Claude Opus 5 × Claude Fable 5.1 at 95.2%**, where a $10.00 model becomes cheaper per effective input token than a $5.00 one. **Correction:** the 2026-08-24 entry stated that no crossover moved; Grok 4.6 × GPT-5.6-sol in fact fell from exactly 100% to 95.2% on that cut and was missed for three weeks. Crossovers are now computed exhaustively across all pairs rather than by inspecting expected movers. Caching mechanics were not re-read and are unchanged from 2026-08-03. |
| 2026-09-07 | **Not collected.** This page skipped its weekly refresh; the two models that arrived that week (Claude Fable 5.1, Gemini 3.8 Flash) were folded into the 2026-09-14 entry instead. No base or cache-read price moved at any of the six providers during that week, so no effective-price column in the 2026-09-01 table was wrong while the gap stood — but the table was two rows short of complete, and Fable 5.1's 97.5% discount was the largest single change to the discount picture since this page began. The miss is recorded rather than backfilled. |
| 2026-09-01 | **No change.** Every base and cache-read rate behind this table holds the value recorded on 2026-08-24, so all four effective-price columns and all sixteen discount figures are unchanged. This is the first collection in the series with no price move at any of the six providers. Collected Tuesday 2026-09-01; the 2026-08-31 Monday slot was missed and left as a gap rather than backfilled. The 2027-01-01 doubling on both Gemini Flash rows still stands and will move every Google Flash figure here when it lands. |
| 2026-08-24 | **GPT-5.6-sol cut to $4.00 base / $0.40 cache read** (from $5.00 / $0.50), lowering every effective column on that row by 20% — $2.2000 at h = 50%, $1.1200 at h = 80%, $0.5800 at h = 95%. The discount stays 90%, because OpenAI cut base and cache read by the same proportion, so the row moves down without changing shape. **No crossover moved**: sol sits in the flagship band where nothing it could cross is priced, and the three surviving crossovers are all between budget models. The `h = 95%` leader is still Gemini 2.5 Flash-Lite. OpenAI marks the new rate promotional through at least 2026-11-21, so this row now carries an expiry the others do not. No other price changed; the table stays at 16 models. Caching mechanics were not re-read and are unchanged from 2026-08-03. |
| 2026-08-17 | **The 83–85% crossover band disappeared.** DeepSeek raised v4-flash to $0.22 base / $0.007 cache read (from $0.14 / $0.0028) and v4-pro to $0.66 / $0.022 (from $0.435 / $0.003625), taking its discount from 98–99% to 96.7–96.8%. Google halved Gemini 3.6 Flash to $0.75 / $0.075. Of the five crossovers, three vanished — Grok 4.3 × Gemini 3.6 Flash (Gemini now wins on both axes) and both DeepSeek v4-pro pairs (pushed past a 100% hit rate) — and the surviving Flash-Lite × v4-flash moved from 84.7% to 97.6%. One is new: GPT-5.6-luna × DeepSeek v4-flash at 60.6%. The `h = 95%` leader changed hands from DeepSeek v4-flash to Gemini 2.5 Flash-Lite. Added Gemini 3.7 Flash and Grok 4.6; the table is now 16 models. Caching mechanics were not re-read and are unchanged from 2026-08-03. |
| 2026-08-03 | OpenAI cut GPT-5.6-luna to $0.20 base / $0.02 cache read (−80%) and GPT-5.6-terra to $2.00 / $0.20 (−20%). Both keep a 90% discount, so every effective column scaled without changing the discount picture. One crossover changed hands: Grok 4.5 x GPT-5.6-terra (90.9%) is gone and GPT-5.6-luna x DeepSeek v4-pro (93.5%) is new. The three crossovers inside the 83–85% band are untouched. Also corrected the crossover section, which described three pairs as the total when three was the count inside the band. |
| 2026-07-28 | Initial edition. 14 models, six providers. Records xAI's Grok 4.5 cache read moving $0.50 to $0.30 and OpenAI's 1.25x write charge on the GPT-5.6 family. |

## FAQ: LLM Cache Pricing 2026

### How much does prompt caching actually save in 2026?

The cached-read discount converged on 90% at OpenAI, Google, and most of Anthropic's line, and two vendors have since left that consensus from opposite ends: Anthropic discounts 97.5% on Claude Fable 5.1 and Mythos 5.1, and DeepSeek 98% on `deepseek-flash`. xAI sits at 75–85%. That discount applies only to the cached share of a prompt, so your realized saving is roughly the hit rate times the discount. A 50% hit rate against a 90% discount is a 45% cut to input cost, not 90%.

### Do you pay to write to the cache?

At Anthropic, always: 1.25x base input for the 5-minute cache, 2x for the 1-hour. OpenAI introduced the same 1.25x charge with the GPT-5.6 family, having charged nothing on earlier models. Google levies no write fee but bills storage at $1.00–$4.50 per 1M cached tokens per hour. xAI, DeepSeek, and Mistral publish no write price.

### Which LLM API is cheapest for a cache-heavy agent?

It depends on your hit rate again, which it did not four weeks ago. Gemini 2.5 Flash-Lite is cheapest from 0% through 87.7%; above that DeepSeek flash takes over, reaching $0.0104 per 1M effective input tokens at a 95% hit rate against Flash-Lite's $0.0145. That crossover has now moved three times in six weeks — 84.7%, then 97.6% after DeepSeek's August 17 rise, then 87.7% once it retired v4-flash for a cheaper model on September 14 — so inherit no answer here without measuring your own hit rate first.

### Is prompt caching automatic or do I have to enable it?

OpenAI, Google, DeepSeek, and xAI cache automatically; Anthropic requires an explicit `cache_control` field. That difference now costs money: because GPT-5.6 caches automatically above 1,024 tokens and bills writes at 1.25x, a long prompt you never reuse may be billed above base rate unless you set `prompt_cache_options.mode` to `explicit`.

### Why can't I compare cache prices straight from provider pricing pages?

No two providers publish the same fields. Anthropic gives multipliers, DeepSeek an absolute cache-hit price, xAI one cached-input column, Google a per-hour storage rate, and Mistral only a headline −90% with no per-model number. Four of six publish no TTL. Normalizing those into one unit is the reason this page exists.

## Related Resources

- [LLM API Pricing 2026: Full Comparison Table (Weekly)](/posts/llm-api-pricing-2026/) — the base prices these effective rates are computed from
- [Best LLM 2026: Capability and Limits Compared](/posts/best-llm-2026/) — what you get for the token, once you know what the token costs
- [Best LLM Subscription 2026: What You Really Pay For](/posts/llm-subscription-guide-2026/) — the same hidden-cost problem on the consumer side of the bill
