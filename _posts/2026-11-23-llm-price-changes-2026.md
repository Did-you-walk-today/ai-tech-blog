---
title: "LLM Price Changes 2026: 18 Weekly Snapshots, One Pattern"
description: "We checked up to 60 LLM APIs weekly for 130 days. Listed model IDs changed price 10 times in 814 checks; since August, every list-price cut came as a new model."
date: 2026-11-23 18:40:00 +0900
last_modified_at: 2026-11-23 18:40:00 +0900
categories: [ai-data-statistics]
tags: [llm-pricing, api-cost, price-history, claude, gpt-6, gemini, deepseek, mistral, "2026"]
format: D
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/llm-price-changes-2026-cover.jpg
  alt: "A solid glass sphere resting on dark stone, a narrow beam of cyan light bending through it onto the surface beyond"
faq:
  - q: "Do LLM API prices go down over time in 2026?"
    a: "Not on the model you already use. Across 18 weekly snapshots from July 16 to November 23, 2026, 24 of the 29 models we tracked the whole time ended at exactly their July price. Lower prices arrived mostly as new model names: since August 24, every input or output list-price cut we recorded came with a new model ID."
  - q: "How often does an LLM API price change?"
    a: "Rarely. We recorded 10 price changes in 814 week-to-week checks of models that stayed listed, about 1.2%. Seven were cuts and three were increases, and two of the ten touched only the cache-read price."
  - q: "Is a new LLM model version cheaper than the one it replaces?"
    a: "About half the time on input price. Of 19 same-line successors we observed at launch, 8 had a lower input price, 10 matched their predecessor and 1 was higher. Cache-read prices fell more often: 10 of 19 successors launched with a cheaper cache read."
  - q: "Did any LLM API provider raise prices in 2026?"
    a: "Yes, three times on models that stayed listed. DeepSeek raised v4-flash and v4-pro on August 17, 2026, and Mistral Large 4 doubled on October 26 when a sale ended, then fell back by half by November 10."
  - q: "Which LLM API prices are scheduled to change next?"
    a: "As published on November 23, 2026: OpenAI's GPT-5.6-sol promotion ends November 30; Google's Gemini 4 Argon and Gemini 4 Carbon double to $4.00 / $20.00 on December 1; Gemini 3.8 Flash and 3.6 Flash double to $1.50 / $7.50 on January 1, 2027."
data_updated: 2026-11-23
author: jsonhouse
---

LLM API prices in 2026 do fall, but almost never on the model ID you already pay for. We read the official pricing pages of six providers every week from July 16 to November 23, 2026 — 18 snapshots over 130 days, tracking between 38 and 60 models at a time. Models that stayed listed changed price 10 times in 814 week-to-week checks, about 1.2% of the time. Seven of those changes were cuts and three were increases.

The cuts moved somewhere else. Since August 24, no model that was already listed has had its input or output price cut, apart from Mistral Large 4 undoing its own increase. In the same 91 days, eight new model IDs launched below the price of the model they succeed — by 20% to 90% on input.

This page is the record that makes that claim checkable. Vendor pricing pages show only today's price, so the history below exists nowhere else.

## TL;DR

- **Listed prices barely move**: 10 price changes in 814 weekly checks (1.2%), on 9 models; 24 of the 29 models tracked for all 130 days ended at exactly their July price
- **Since August 24, cuts came only as new names**: zero input or output cuts on existing IDs (one reversal aside), while 8 new IDs launched cheaper than their predecessor
- **A new version is not automatically cheaper**: of 19 same-line successors, 8 cut input price, 10 matched it and 1 raised it; the median input change at launch was 0%
- **The cache-read column moves more than the list price**: 10 of 19 successors launched with a cheaper cache read, including two that kept every other price identical
- **Increases happen, and only at smaller vendors**: DeepSeek on August 17 and Mistral on October 26; none of Anthropic, OpenAI, Google or xAI raised a price on a listed model

## Methodology

Each snapshot reads the standard (non-batch) API price of every tracked model directly from the provider's own pricing page: [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI](https://developers.openai.com/api/docs/pricing), [Google](https://aistudio.google.com/docs/pricing), [xAI](https://docs.x.ai/docs/models), [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) and [Mistral](https://docs.mistral.ai/inference/pricing). Prices are normalized to USD per 1M tokens. Tiered models record their base tier, and DeepSeek rows record the off-peak rate. The same snapshots feed our weekly [LLM API pricing table](/posts/llm-api-pricing-2026/).

The numbers on this page come from comparing each snapshot with the one before it. Three terms carry the analysis, and all three are our definitions, not vendor ones.

A **row-interval** is one model present in two consecutive snapshots. There are 814 of them across the 17 intervals between 18 snapshots. A **price event** is a row-interval in which the input, output or cache-read price differs. A cache-read price recorded for the first time (five cases, all Google or Mistral) is a gap being filled, not an event.

A **same-line successor** is a model whose name is the next version of a model in the same product line and tier — Claude Opus 5 to Opus 5.5, GPT-6.1-sol to GPT-6.2-sol, Grok 4.6 to Grok 4.7. Three pairs are also backed by the vendor: DeepSeek served the retired `deepseek-v4-flash` ID from `deepseek-flash`, and Google routes `gemini-3.5-flash` and `gemini-3.7-flash` requests to `gemini-3.6-flash` and `gemini-3.8-flash`. Each successor is compared with its predecessor in the snapshot where the successor first appears.

The collection was weekly but not perfectly so. Thirteen of the 17 intervals are 6 to 8 days long. Two are long gaps — 12 days from July 16 to 28, and 15 days from October 26 to November 10 — so a change inside them is dated only to the gap.

## How Often Did a Listed Price Change?

Ten times. The table lists every price event on a model that stayed listed between two consecutive snapshots, with the window in which it happened.

| Window (measured by jsonhouse) | Provider | Model | Input change (jsonhouse derived) | Output change (jsonhouse derived) | Cache-read change (jsonhouse derived) |
|---|---|---|---|---|---|
| Jul 16 – Jul 28 | xAI | Grok 4.5 | 0% | 0% | −40% ($0.50 → $0.30) |
| Jul 28 – Aug 3 | OpenAI | GPT-5.6-terra | −20% ($2.50 → $2.00) | −20% | −20% |
| Jul 28 – Aug 3 | OpenAI | GPT-5.6-luna | −80% ($1.00 → $0.20) | −80% | −80% |
| Aug 10 – Aug 17 | Google | Gemini 3.6 Flash | −50% ($1.50 → $0.75) | −50% | −50% |
| Aug 10 – Aug 17 | DeepSeek | v4-flash | +57.1% ($0.14 → $0.22) | +135.7% | +150% |
| Aug 10 – Aug 17 | DeepSeek | v4-pro | +51.7% ($0.435 → $0.66) | +127.6% | +506.9% |
| Aug 17 – Aug 24 | OpenAI | GPT-5.6-sol | −20% ($5.00 → $4.00) | −33.3% | −20% |
| Oct 5 – Oct 14 | Anthropic | Claude Sonnet 5.5 | 0% | 0% | −50% ($0.20 → $0.10) |
| Oct 19 – Oct 26 | Mistral | Mistral Large 4 | +100% ($0.68 → $1.36) | +100% | +100% |
| Oct 26 – Nov 10 | Mistral | Mistral Large 4 | −48.5% ($1.36 → $0.70) | −49.8% | −50% |

> **Raw data**: [data/llm-price-changes-2026.json](https://www.jsonhouse.com/data/llm-price-changes-2026.json) — machine-readable structured data for AI crawlers and citation.

Ten events in 814 row-intervals is a 1.2% weekly rate. They fell on nine models, since Mistral Large 4 moved twice. Eight moved input or output, and two changed only the cache read.

The timing is the first sign of the pattern. Seven of the ten events happened in the six weeks to August 24. In the 12 collections after it, the only events were a cache-read cut on a model nine days old and a Mistral sale ending and then being undone.

## What Happened to the Models We Tracked Throughout?

Twenty-nine models were listed in all 18 snapshots. They are the cleanest test of what a buyer who never changed a model ID experienced, because each one was observed in every interval.

| Provider | Models listed in all 18 snapshots (measured by jsonhouse) | Ended at July price on all three figures (jsonhouse derived) | Ended lower (jsonhouse derived) | Ended higher (jsonhouse derived) |
|---|---|---|---|---|
| Anthropic | 9 | 9 | 0 | 0 |
| OpenAI | 9 | 6 | 3 | 0 |
| Google | 5 | 5 | 0 | 0 |
| xAI | 3 | 2 | 1 (cache read only) | 0 |
| Mistral | 2 | 2 | 0 | 0 |
| DeepSeek | 1 | 0 | 0 | 1 |
| **Total** | **29** | **24** | **4** | **1** |

The four that ended lower are OpenAI's three GPT-5.6 models, all cut between July 28 and August 24, and Grok 4.5's cache read. The one that ended higher is DeepSeek v4-pro, at $0.66 / $1.98 against $0.435 / $0.87 in July. Mistral's two rows count as unchanged: Codestral and Mistral Small 4 gained a cache-read price on October 14 that this series had not recorded before.

Claude Sonnet 5 is among the unchanged, and it shows what an unchanged row can hide. Its $2.00 / $10.00 was introductory in July and scheduled to rise to $3.00 / $15.00 on September 1. Anthropic had cancelled the increase by August 17. The price never moved; the risk that it would did.

## Where the Cuts Went: Successors at Launch

If listed prices barely move, the other way a price falls is a new model. This table compares 19 successors with their predecessor in the week each successor first appeared.

| First seen (measured by jsonhouse) | Predecessor → successor | Input, predecessor → successor (vendor) | Input change (jsonhouse derived) | Cache-read change (jsonhouse derived) |
|---|---|---|---|---|
| Jul 28 | Claude Opus 4.8 → Opus 5 | $5.00 → $5.00 | 0% | 0% |
| Jul 28 | Gemini 3.5 Flash → 3.6 Flash | $1.50 → $1.50 | 0% | 0% |
| Aug 17 | Gemini 3.6 Flash → 3.7 Flash | $0.75 → $0.75 | 0% | 0% |
| Aug 17 | Grok 4.5 → Grok 4.6 | $2.00 → $2.00 | 0% | +66.7% |
| Sep 7 | Claude Fable 5 → Fable 5.1 | $10.00 → $10.00 | 0% | −75% |
| Sep 7 | Gemini 3.7 Flash → 3.8 Flash | $0.75 → $0.75 | 0% | 0% |
| Sep 14 | DeepSeek v4-flash → deepseek-flash | $0.22 → $0.15 | −31.8% | −57.1% |
| Sep 28 | Claude Opus 5 → Opus 5.5 | $5.00 → $4.00 | −20% | −60% |
| Sep 28 | GPT-5.6-sol → GPT-6-sol | $4.00 → $2.00 | −50% | −50% |
| Sep 28 | GPT-5.6-luna → GPT-6-luna | $0.20 → $0.10 | −50% | −50% |
| Sep 28 | Grok 4.6 → Grok 4.7 | $2.00 → $2.00 | 0% | 0% |
| Oct 5 | Claude Sonnet 5 → Sonnet 5.5 | $2.00 → $2.00 | 0% | 0% |
| Oct 5 | GPT-6-sol → GPT-6.1-sol | $2.00 → $2.00 | 0% | −50% |
| Oct 14 | Claude Haiku 4.5 → Haiku 5.5 | $1.00 → $0.10 | −90% | −90% |
| Oct 14 | Mistral Large 3 → Large 4 | $0.50 → $0.68 | +36% | +40% |
| Nov 10 | Claude Fable 5.1 → Fable 5.2 | $10.00 → $8.00 | −20% | −20% |
| Nov 10 | GPT-5.6-terra → GPT-6.1-terra | $2.00 → $1.00 | −50% | −75% |
| Nov 23 | GPT-6-astra → GPT-6.2-astra | $10.00 → $8.00 | −20% | −60% |
| Nov 23 | GPT-6.1-sol → GPT-6.2-sol | $2.00 → $2.00 | 0% | 0% |

Eight of the 19 cut input price, ten matched it and one raised it, so the median input change at launch is 0%. A version bump is not a price cut by default. Where a cut did come, it was large: −20% to −90%, and four of the eight were −50% or deeper.

Output moved in the same direction as input in every pair except one: Gemini 3.6 Flash launched at Gemini 3.5 Flash's input price with output 16.7% lower. Mistral Large 4's +36% is measured at the sale price it launched on. Its list price at the time was $1.36, more than double Large 3's.

## Why Prices Move Through New Model IDs

Put the two tables side by side and the shape is clear. Since August 24, a buyer who pinned a model ID saw no input or output cut. A buyer who moved to a new ID could have taken any of eight.

The vendors do not explain this choice, so what follows is our reading of it, not a statement from any of them. The first reason is that a price cut on a listed model is unconditional. It reaches every customer, including the ones who would have paid the old price indefinitely. A cut attached to a new ID reaches only the customers willing to migrate, test and re-qualify, so the vendor keeps the full price from everyone who does not.

The second reason is that a new ID resets what the price is anchored to. GPT-6-sol launched at half of GPT-5.6-sol, but GPT-5.6-sol kept its own price, so the page shows a cheap new model rather than a cheaper old one. That leaves room to cut the old model later, or to retire it, without either looking like a retreat.

The third reason is visible in the cache column. Ten of the 19 successors launched with a cheaper cache read, more than cut their input price. GPT-6.1-sol and Claude Fable 5.1 changed nothing else. A cut that sits only in the cache read benefits agent workloads that resend the same context, and is invisible on a list-price comparison. We worked through what that does to effective cost in [LLM Cache Pricing 2026](/posts/llm-cache-pricing-2026/).

The increases follow a different logic, and they came only from DeepSeek and Mistral. DeepSeek's August rise more than doubled output prices on both models. It was then partly undone the way the others cut: a new ID, `deepseek-flash`, at a lower price, with the old ID retired.

Mistral Large 4 is the clearest case of a price without notice. Its price doubled when an undated sale ended and halved again two weeks later, with nothing on the page dating either change. It is the only listed model in the series whose price moved in both directions.

## The Bigger Picture

This pattern explains a contradiction we documented in [LLM Price War 2026](/posts/llm-price-war-balance-sheet-2026/): token prices kept falling while the compute under them got more expensive. If cuts reach only buyers who migrate, a vendor can advertise a falling price curve while most of its existing revenue stays at last quarter's rates.

It also changes what a model's lifetime costs. The deprecation schedules in [Best LLM 2026](/posts/best-llm-2026/) are no longer only an availability risk. A model nobody retires but nobody cuts either becomes steadily more expensive relative to its successor. Claude Haiku 4.5 is still listed at $1.00 / $5.00, ten times its successor's price.

## What Changes Next

Several price changes on listed models are already dated on the vendor pages. Unlike the ten events above, these can be planned for. The dates below are as published on November 23, 2026.

| Date (vendor) | Model | Scheduled change (vendor) |
|---|---|---|
| 2026-11-30 | GPT-5.6-sol | Promotional $4.00 / $20.00 ends; post-promotion price not published |
| 2026-11-30 | Claude Sonnet 4.5 | Retired; Anthropic names Claude Sonnet 5.5 as replacement |
| 2026-12-01 | Gemini 4 Argon, Gemini 4 Carbon | $2.00 / $10.00 → $4.00 / $20.00 |
| 2026-12-01 | Gemini 2.5 Pro, Gemini 2.5 Flash | Requests routed to Gemini 3.8 Flash and 3.5 Flash-Lite, billed at their rates |
| 2027-01-01 | Gemini 3.8 Flash, Gemini 3.6 Flash | $0.75 / $3.75 → $1.50 / $7.50 |

If they take effect as written, December 1 will bring the first scheduled increase on listed models to actually take effect in this series. These are promotional rates ending, not list prices rising, but on an invoice the difference does not show.

## What This Means for Your Budget

**Budget a pinned model at its current price, indefinitely.** In 130 days, 24 of 29 long-tracked models did not move at all. A forecast that assumes the price of a model you already use will fall has no support in this record.

**Plan savings as migrations, not as price drops.** The eight successor cuts were worth 20% to 90% on input, but each one requires changing a model ID and re-testing output. Put a review on the calendar each quarter instead of waiting for a cut that, on this evidence, will not arrive on the model you pinned.

**Read the cache-read column before the list price.** For agent workloads it is the price that moved most often. For dated promotions, budget the post-promotion rate where the page states one, as Google's does.

## Limitations

- **Coverage is six providers and the models we track.** The set grew from 38 to 60 rows; eight of the 32 entries came on July 28, when coverage widened to models already on sale. Entries are not launch dates.
- **Exits are not all retirements.** Five of the ten exits on August 17 were models Mistral and Anthropic had already retired and that we removed late; two Mistral rows left in November because the price table stopped listing them.
- **Two gaps blur dating.** Changes between July 16 and 28, and between October 26 and November 10, are dated only to those windows.
- **List prices only.** Batch discounts, regional uplifts, long-context tiers and negotiated discounts are excluded, and DeepSeek rows use off-peak rates.
- **Same-line successor is our classification.** Sixteen of the 19 pairs rest on product naming, not on a vendor statement that one model replaces the other.
- **A per-token price is not a per-task price.** Anthropic's newer models count about 30% more tokens for the same text, which this record does not adjust for.

## Update Cadence and Changelog

This analysis is recomputed **monthly**, after the first Monday snapshot of each month, from the same weekly snapshot series. The underlying collection continues every week. The monthly refresh re-runs every count on this page and appends a line below.

| Date | Change |
|---|---|
| 2026-11-23 | Initial edition. 18 snapshots from 2026-07-16 to 2026-11-23: 814 row-intervals, 10 price events, 29 models tracked throughout, 19 same-line successor pairs. |

## FAQ: LLM Price Changes 2026

### Do LLM API prices go down over time in 2026?

Not on the model you already use. Across 18 weekly snapshots from July 16 to November 23, 2026, 24 of the 29 models we tracked the whole time ended at exactly their July price. Lower prices arrived mostly as new model names: since August 24, every input or output list-price cut we recorded came with a new model ID.

### How often does an LLM API price change?

Rarely. We recorded 10 price changes in 814 week-to-week checks of models that stayed listed, about 1.2%. Seven were cuts and three were increases, and two of the ten touched only the cache-read price.

### Is a new LLM model version cheaper than the one it replaces?

About half the time on input price. Of 19 same-line successors we observed at launch, 8 had a lower input price, 10 matched their predecessor and 1 was higher. Cache-read prices fell more often: 10 of 19 successors launched with a cheaper cache read.

### Did any LLM API provider raise prices in 2026?

Yes, three times on models that stayed listed. DeepSeek raised v4-flash and v4-pro on August 17, 2026, and Mistral Large 4 doubled on October 26 when a sale ended, then fell back by half by November 10.

### Which LLM API prices are scheduled to change next?

As published on November 23, 2026: OpenAI's GPT-5.6-sol promotion ends November 30; Google's Gemini 4 Argon and Gemini 4 Carbon double to $4.00 / $20.00 on December 1; Gemini 3.8 Flash and 3.6 Flash double to $1.50 / $7.50 on January 1, 2027.
