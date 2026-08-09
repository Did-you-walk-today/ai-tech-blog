---
title: "China AI Coding Plans 2026: Quotas You Can't Compare"
description: "China AI coding plans 2026: GLM, Qwen, MiniMax, Kimi, and DeepSeek quotas from official docs. Four vendors publish numbers; only one publishes the conversion."
date: 2026-08-05 12:00:00 +0900
last_modified_at: 2026-08-05 12:00:00 +0900
categories: [ai-data-statistics]
tags: [china-ai, glm, kimi, minimax, qwen, deepseek, coding-plan, usage-limits, "2026"]
format: D
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/china-ai-coding-plans-2026-cover.jpg
  alt: "A thick dome of clear optical glass resting flat-side-down on rough dark stone, light pinching beneath it"
faq:
  - q: "Which Chinese AI coding plan is cheapest in 2026?"
    a: "MiniMax Plus at $20 per month is the lowest verified price, and Zhipu's GLM Coding Plan advertises an entry tier from $18. But neither number answers the question you are actually asking, because the two plans meter completely different things — MiniMax sells agent capacity, Zhipu sells token-derived credits. Price per month is comparable; price per unit of work is not."
  - q: "Do Chinese AI vendors publish their usage quotas?"
    a: "Four of the five do, which makes them unusual — Anthropic returns null for its dollar limits, while Zhipu, Alibaba, MiniMax, and Moonshot all publish numbers. The catch is that no two publish the same kind of number, and only one publishes the conversion. Zhipu documents its credit formula and every per-model multiplier, so its quota reduces to tokens; Alibaba's request, MiniMax's agent, and Moonshot's request range have no published token content. Publishing a quota and publishing a comparable quota are different things."
  - q: "When do Chinese coding plan weekly quotas reset?"
    a: "It depends on the vendor, and the difference is operational, not cosmetic. Alibaba's Model Studio plan resets every Monday at 00:00 (UTC+8), a fixed calendar anchor you can plan a sprint around. Zhipu and Moonshot both roll 7 days from your subscription date instead, so your reset lands at whatever hour you happened to sign up and no two teammates share it."
  - q: "Does Kimi Code publish its usage limits?"
    a: "Partly, and on a different site than most people check. Moonshot's Kimi Code documentation publishes a rolling 5-hour window of roughly 300 to 1,200 requests with up to 30 concurrent, and states that the weekly quota refreshes every 7 days from your subscription date. What it does not publish is the weekly number itself, or what a request contains. The 5-hour range is also wide enough — a 4x spread — that the ceiling is not something you can plan a deadline around."
  - q: "Does DeepSeek have a coding subscription plan?"
    a: "No. DeepSeek sells pay-per-token API access only, with concurrency limits (2,500 concurrent requests on v4-flash, 500 on v4-pro) instead of usage quotas. There is no quota and therefore no reset. The best-known Chinese AI lab internationally is absent from the category this post covers."
data_updated: 2026-08-05
author: jsonhouse
---

Five Chinese vendors sell AI coding subscriptions in 2026, and four of them publish a usage quota. That is more disclosure than the American market offers, and it is less useful than it sounds. Zhipu's GLM Coding Plan meters **credits**. Alibaba's Model Studio plan meters **requests**. MiniMax meters **agent capacity**. Moonshot's Kimi Code meters requests too, but publishes them as a range four times wider at the top than the bottom, drawn from a balance the chat app also spends. DeepSeek sells no subscription at all. This post records what each vendor's official documentation actually states, and marks plainly what could not be verified.

## TL;DR

- **Four of five vendors publish quotas, in four different units**: credits, requests, agent capacity, and a request range shared with a chat app. DeepSeek sells no subscription.
- **Exactly one publishes the conversion.** Zhipu documents both its credit formula and every per-model multiplier, so its quota reduces to tokens. Nobody else publishes a token content for their unit.
- **Two vendors meter "requests" and mean different things.** Alibaba states a firm 6,000 per 5 hours; Moonshot states roughly 300–1,200, from a pool the Kimi web app also draws down.
- **"Weekly limit" has two anchors.** Alibaba resets on a fixed calendar (Monday 00:00 UTC+8); Zhipu and Moonshot both roll 7 days from your subscription date.
- **Aggregators disagree with the vendor.** Third-party sites describe Zhipu's Pro as roughly 5× Lite and Max as 20×; the published credit figures give 6× and 14×.

## What each vendor actually publishes

Every figure below comes from the vendor's own documentation, retrieved 2026-08-05. Blank cells are blank because we could not verify them, not because the value is zero.

| Vendor | Tiers | Quota unit | 5-hour limit | Weekly limit | Weekly reset anchor | Verification |
|---|---|---|---|---|---|---|
| Zhipu GLM (z.ai) | Lite / Pro / Max | credits (token-derived) | 2,000 / 12,000 / 28,000 | 10,000 / 60,000 / 140,000 | 7 days from subscription | Official docs |
| Alibaba Qwen | Pro | requests | 6,000 | 45,000 (also 90,000/month) | Monday 00:00 (UTC+8) | Official docs |
| MiniMax | Plus / Max / Ultra | agent capacity | 3–4 / 4–5 / 6–7 agents | 5-hour rolling + weekly windows, values not published | Not published | Official docs |
| Moonshot Kimi | Moderato / Allegretto and above | requests, shared with the Kimi web app | ~300–1,200 requests, 30 concurrent | Refreshes weekly, values not published | 7 days from subscription | Official docs |
| DeepSeek | No subscription plan | — | — | — | — | Official docs |

> **Raw data**: [data/china-ai-coding-plans-2026.json](https://www.jsonhouse.com/data/china-ai-coding-plans-2026.json) — machine-readable structured data for AI crawlers and citation.

Prices are the one dimension that is genuinely comparable, because everyone quotes dollars per month.

| Vendor | Tier | Monthly price (USD) | Verification |
|---|---|---|---|
| MiniMax | Plus | $20 | Official docs |
| MiniMax | Max | $50 | Official docs |
| MiniMax | Ultra | $120 | Official docs |
| Alibaba Qwen | Pro | $50 | Official docs |
| Zhipu GLM | Entry tier | From $18 | Official docs (per-tier prices not itemized) |
| Moonshot Kimi | Moderato / Allegretto and above | Not verified | Tier names documented; the membership pricing page served no readable figures |

Two qualifiers travel with this table. Zhipu's documentation states only "starting at just 18 USD per month" and does not itemize Pro and Max. Moonshot names its tiers in the Kimi Code documentation but prices them on a membership page we could not read. In both cases we record what the vendor published and leave the rest blank rather than import an aggregator figure — see Methodology for why that restraint is not fussiness.

### The one vendor that shows its work

Zhipu's credit is not an opaque token of goodwill. The documentation publishes the formula outright:

> Model credit usage = (Input tokens × Input multiplier + Cached Input tokens × Cached Input multiplier + Output tokens × Output multiplier) / 10,000

And it publishes every multiplier the formula needs.

| Model | Input | Cached input | Output |
|---|---|---|---|
| GLM-5.2 | 6.9 | 1.7 | 24 |
| GLM-5-Turbo | 5.7 | 1.5 | 21 |
| GLM-4.7 | 4.6 | 1.2 | 16 |
| GLM-4.6V (vision) | 1.2 | 0.3 | 2.7 |

MCP tool calls are billed separately as calls × output multiplier, with Web Search, Web Reader and Zread each at 1.2.

Two things follow. A Zhipu credit is a **token count wearing a costume** — divide by the multiplier and you are back to tokens. And because the multipliers differ by model, the same credit balance buys a different amount of work depending on which model you route to, which is a pricing decision the vendor has made legible rather than hidden.

The output multiplier is the number to watch. On GLM-5.2 an output token costs 3.5× an input token and 14× a cached input token. A verbose agent is not marginally more expensive on this plan; it is the dominant term.

## Why the units diverge

The obvious reading is that vendors obscure quotas to prevent comparison shopping. That is probably part of it, but it does not explain why they picked these particular units, because a vendor that simply wanted opacity could pick any of them.

A better reading: **each vendor chose the resource that is scarce for them.** A request is a slot in a scheduling queue. Agent capacity is a live seat on a machine. A credit is compute already spent. Those are three different bottlenecks, and each vendor is metering the one it actually runs out of.

Read that way, the unit is a disclosure rather than a concealment. Alibaba metering requests suggests queue admission is what constrains them. MiniMax metering agent capacity — a unit that is not a quantity consumed at all, but a parallelism cap — suggests their constraint is simultaneous occupancy rather than total volume.

Moonshot's range is a fourth case, and a different kind. A published interval of 300 to 1,200 is not a bottleneck the vendor has measured and disclosed; it is one it has declined to commit to. The gap between the bounds is where the vendor keeps its room to manoeuvre.

There is one unit that would make all five plans directly comparable: tokens. Tokens are the denominator of the entire pay-per-token API market, where cross-vendor comparison is trivial and routine. The moment a subscription is denominated in tokens, a buyer can divide price by quota and rank the market in one column.

**Exactly one of these five vendors offers that division, and it is worth being precise about which.** Zhipu's credit is defined as a function of tokens, and every coefficient in that function is published. A buyer who wants tokens per dollar on the GLM Coding Plan can compute it from the vendor's own page. That is the comparison the other plans do not permit.

The others withhold different amounts, and it is worth being exact about how much. Alibaba gets closer than it is usually given credit for: its documentation states that "each query consumes quota based on the number of model calls," and it supplies that number as a range — 5 to 10 calls for simple tasks, 10 to 30 or more for complex ones. What it never states is what a call contains in tokens, so the chain runs query → calls → nothing.

MiniMax publishes a range of agents, which cannot be converted to anything because it does not deplete. Moonshot publishes a request range whose bounds differ by a factor of four, and then routes the Kimi web app through the same balance, so the figure describes a ceiling you share with your own browsing.

Two of these vendors nominally meter the same thing, which is the cleanest illustration available that the unit name is not the disclosure. Alibaba and Moonshot both count requests. One states 6,000 per five hours; the other states somewhere between 300 and 1,200. Matching units did not make them comparable.

So the honest version of the complaint is narrower than "vendors hide their quotas," and more damning. The comparable unit exists, the market already runs on it, and one vendor in this set demonstrates that publishing the conversion costs nothing. Every other plan's incomparability is therefore a choice rather than a technical limit — a generosity claim survives precisely as long as it cannot be checked against a competitor's.

## "Weekly limit" is two different products

The reset anchor difference is easy to skim past and matters more than the headline numbers. Alibaba's weekly quota resets every Monday at 00:00 (UTC+8) — a fixed calendar anchor shared by every subscriber.

Zhipu and Moonshot both do the opposite. Zhipu's weekly limit "activates upon subscription" and resets every 7 days from there. Moonshot documents the same shape and is explicit about the arithmetic, counting cycles from the subscription date: D1–D7, D8–D14, D15–D21, and onward. Your window is anchored to whatever hour you happened to sign up, and it stays there.

That the market splits two-to-one on this is the useful part. The fixed calendar is not an industry default that Zhipu deviates from; it is one of two live conventions, and the pricing table is not where either of them is written down.

The practical difference shows up when you plan work. Under a fixed calendar you know the whole team's quota refills Monday morning and can schedule the heavy run accordingly. Under a subscription-anchored roll, every member of a team has a different reset hour, and yours drifts through the working day depending on when you subscribed.

We covered the American side of this pattern in [Best LLM Subscription 2026](/posts/llm-subscription-guide-2026/), where the finding was that vendors sell a price and a promise but almost never a quantity. The Chinese plans invert one half of that: they do give quantities. They just give them in units that do not survive contact with a second vendor.

## DeepSeek is not in this category at all

The most internationally recognized Chinese AI lab sells no coding subscription. DeepSeek's documentation describes pay-per-token pricing only — expense equals tokens times price, with separate cache-hit and cache-miss input rates.

What it publishes instead of quotas are concurrency limits: 2,500 concurrent requests on deepseek-v4-flash and 500 on deepseek-v4-pro. A concurrency limit caps how many requests run at once; it does not deplete and therefore never resets.

This matters for anyone building a "Chinese AI coding plan" shortlist, because the name most likely to be on it does not belong on it. It also isolates the variable cleanly. DeepSeek's per-token pricing is perfectly comparable against OpenAI's and Anthropic's — we track exactly that in [LLM API Pricing 2026](/posts/llm-api-pricing-2026/).

The Western coding tools these plans are pitched against have the opposite problem: their quotas are legible but their pricing is usage-based and hard to forecast. We compare that side in [Best AI Coding Tools 2026](/posts/best-ai-coding-tools-2026/).

The same vendor, in the same market, is comparable when selling tokens and would be incomparable if it sold seats. Comparability is a property of the pricing form, not of the country.

## Methodology

Figures were collected on 2026-07-28, re-verified on 2026-08-01, and re-verified again on 2026-08-05 by fetching each vendor's official English-language documentation directly. Sources: [Z.ai developer documentation](https://docs.z.ai/devpack/overview) for GLM, [Alibaba Cloud Model Studio](https://www.alibabacloud.com/help/en/model-studio/coding-plan) help pages for Qwen, the [MiniMax platform token-plan documentation](https://platform.minimax.io/docs/token-plan/intro), Moonshot's [Kimi Code documentation](https://www.kimi.com/code/docs/en/) and [membership benefits page](https://www.kimi.com/code/docs/en/kimi-code/membership.html) for Kimi, and [DeepSeek's API pricing documentation](https://api-docs.deepseek.com/quick_start/pricing).

No figure in the tables above comes from a third-party aggregator. Where a vendor's own page did not state a value, the cell says so — "not published", "not verified" — rather than filling in. This is a deliberate choice, and this edition supplies the evidence for it: aggregator pages describe Zhipu's Pro tier as roughly 5× Lite and Max as about 20×, while the vendor's published credit figures give 6× and 14×. Three aggregator sites also quote three mutually contradictory price sets for the same three tiers, each stated with equal confidence.

**One discrepancy is worth stating plainly.** Our 2026-07-28 collection recorded Zhipu's quota as prompt-denominated. The 2026-08-01 re-check found credits, with the formula and multipliers documented above. We cannot determine from the documentation whether the scheme changed in that window or the earlier reading was wrong, and the vendor publishes no changelog we could consult. Only the 2026-08-01 observation is reported in the tables. If the unit did change, the next monthly snapshot will show it changing again or holding, and that series is the only way this question gets answered.

**A correction, and where it came from.** Before publication this table recorded Moonshot as documenting no coding quota at all. That was wrong, and the error was ours rather than a change at the vendor. We had checked `platform.kimi.ai`, which is Moonshot's pay-per-token API platform and genuinely carries no subscription quota. Kimi Code is documented on a separate property — `kimi.com/code/docs` and the Kimi help centre — which was live throughout. A vendor's API documentation and its subscription documentation are not reliably the same site.

The general lesson is worth more than the specific fix. A negative finding is the most expensive kind of claim to get wrong, because a missing number is indistinguishable from a number you failed to find. Before this post asserts that something is unpublished, it now requires that the vendor's product site, help centre, and API docs have each been checked.

Two records remain unverified. Moonshot documents its tier names but its membership pricing page served us no readable figures, so Kimi prices stay blank rather than borrow an aggregator's. Zhipu's mainland pricing on bigmodel.cn requires a mainland Chinese phone number and KYC verification, so its checkout screen was not accessible to us.

## Limitations

Region matters and we only cover one side of it. Every price here is the international (USD) offering. Zhipu operates both an overseas endpoint and a mainland endpoint under one subscription, billed in USD and CNY respectively, and the two are not the same price. Our mainland figures are absent, not equivalent.

Promotional versus list pricing is not always distinguishable from the documentation. Where a vendor did not label a price as introductory, we recorded it as published without asserting which it is.

Tier lineups move faster than most pricing pages suggest. Alibaba's Lite tier stopped accepting new subscriptions on 2026-03-20 and stopped renewals and upgrades on 2026-04-13, within a single quarter. A snapshot is a snapshot.

Finally, converting a quota to tokens is not the same as knowing how much work it buys. Zhipu's formula gives you tokens per credit, but tokens per *completed task* depends on your repository, your prompts, and how many turns the agent takes — none of which any vendor can publish. MiniMax's agent count is not a consumption quantity at all. Cost per unit of real work would require measurement, not documentation, and this post is documentation.

## What to actually do with this

Compare monthly prices, because those are real. Beyond that, one conversion is available and the rest are not: on Zhipu you can compute tokens per dollar from the published formula and multipliers, so do that if GLM is on your shortlist. Any ranking that converts *across* vendors — credits to requests to agents — is inventing a rate nobody publishes.

Check the reset anchor before you commit a team, and note that the subscription-anchored roll is now the majority convention here rather than the exception. A fixed calendar reset and a subscription-anchored roll behave differently under deadline pressure, and the difference is not mentioned in any pricing table including ours until you go looking.

If Kimi is on the shortlist, check what else spends the balance. Kimi Code draws from the same membership quota as the Kimi web app, so the coding ceiling is not a coding ceiling — a heavy day of chat moves it.

Treat unverified numbers as unverified. If a figure for these plans is not on the vendor's own page, the aggregators quoting it confidently are not agreeing with each other — and on Zhipu's tier ratios they do not agree with the vendor either. For the broader question of what a subscription buys you at all, see [Best LLM 2026](/posts/best-llm-2026/).

## FAQ

### Which Chinese AI coding plan is cheapest in 2026?

MiniMax Plus at $20 per month is the lowest verified price, and Zhipu's GLM Coding Plan advertises an entry tier from $18. But neither number answers the question you are actually asking, because the two plans meter completely different things — MiniMax sells agent capacity, Zhipu sells token-derived credits. Price per month is comparable; price per unit of work is not, except on Zhipu, where the published multipliers let you compute tokens per dollar yourself.

### Do Chinese AI vendors publish their usage quotas?

Four of the five do, which makes them unusual — Anthropic returns null for its dollar limits, while Zhipu, Alibaba, MiniMax, and Moonshot all publish numbers. The catch is that no two publish the same kind of number, and only one publishes the conversion. Zhipu documents its credit formula and every per-model multiplier, so its quota reduces to tokens; Alibaba's request, MiniMax's agent, and Moonshot's request range have no published token content. Publishing a quota and publishing a comparable quota are different things.

### When do Chinese coding plan weekly quotas reset?

It depends on the vendor, and the difference is operational, not cosmetic. Alibaba's Model Studio plan resets every Monday at 00:00 (UTC+8), a fixed calendar anchor you can plan a sprint around. Zhipu and Moonshot both roll 7 days from your subscription date instead, so your reset lands at whatever hour you happened to sign up and no two teammates share it.

### Does Kimi Code publish its usage limits?

Partly, and on a different site than most people check. Moonshot's Kimi Code documentation publishes a rolling 5-hour window of roughly 300 to 1,200 requests with up to 30 concurrent, and states that the weekly quota refreshes every 7 days from your subscription date. What it does not publish is the weekly number itself, or what a request contains. The 5-hour range is also wide enough — a 4× spread — that the ceiling is not something you can plan a deadline around.

### Does DeepSeek have a coding subscription plan?

No. DeepSeek sells pay-per-token API access only, with concurrency limits (2,500 concurrent requests on v4-flash, 500 on v4-pro) instead of usage quotas. There is no quota and therefore no reset. The best-known Chinese AI lab internationally is absent from the category this post covers.

## Update cadence

This table is updated monthly. Chinese coding plan tiers changed at least twice in the first half of 2026, which is too fast for a static page and too slow to justify a weekly snapshot. The underlying snapshot series began on 2026-07-28 and accumulates as a change history that vendor pages, which show only current terms, do not provide.

## Changelog

- **2026-08-05** — Corrected the Moonshot Kimi record before publication. Kimi Code's quota documentation lives on Moonshot's product site rather than its API platform, and the row moves from unverified to documented: a rolling 5-hour window of roughly 300–1,200 requests with up to 30 concurrent, a weekly quota refreshing 7 days from the subscription date, and a balance shared with the Kimi web app. Alibaba's per-query call range (5–10 simple, 10–30 or more complex) is now quoted rather than summarised as unstated. All other vendor figures re-checked and unchanged.
- **2026-08-01** — Re-verified before publication. Zhipu's quota is recorded as credits with the published formula and per-model multipliers, replacing the prompt-denominated figures from the initial collection; the documentation does not say whether the scheme changed or the first reading was wrong. Added Alibaba's 90,000/month limit, MiniMax's rolling-window structure, and the aggregator-versus-vendor discrepancy on Zhipu's tier ratios.
- **2026-07-28** — Initial snapshot. Five vendors recorded; Moonshot Kimi and Zhipu mainland pricing marked unverified.
