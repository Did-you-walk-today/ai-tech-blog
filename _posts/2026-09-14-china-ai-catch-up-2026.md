---
title: "China AI 2026: Following the Path America Built"
description: "Anthropic named seven Chinese labs running industrial-scale Claude distillation in 2026. What they took, what they could not, and where China already leads."
date: 2026-09-14 20:00:00 +0900
last_modified_at: 2026-09-14 20:00:00 +0900
categories: [industry-analysis]
tags: [china-ai, distillation, export-controls, qwen, deepseek, robotics, ai-policy, "2026"]
format: A
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/china-ai-catch-up-2026-cover.jpg
  alt: "Two upright glass panes on a rough stone slab, a pale cyan beam crossing them from the right, amber light tracing their edges"
faq:
  - q: "Did Chinese labs steal Claude's model weights?"
    a: "No. Anthropic's September 2026 report describes distillation, not intrusion. The attackers never accessed weights, source code, or training data — they bought or faked API access and harvested outputs and reasoning traces at scale. No network was breached. The distinction matters because a weight theft is a security failure, while distillation is a business-model failure: the front door worked exactly as designed."
  - q: "Which Chinese labs did Anthropic name?"
    a: "Seven China-based labs: Alibaba (Qwen/Tongyi Lab), Moonshot AI, DeepSeek, Zhipu (Z.ai), Xiaomi, SenseTime, and MiniMax. Anthropic assigned each a GTG tracking number and attributed the campaigns with high confidence. Alibaba's was the largest distillation attack Anthropic says it has ever measured, at over 151 million exchanges between May and July 2026."
  - q: "Is China behind the US in AI in 2026?"
    a: "At the frontier, yes — the top of the LMArena leaderboard is four US labs within Elo noise of each other. But the gap is narrow and axis-dependent. Kimi K3 leads the Frontend Code Arena on open weights, DeepSeek prices inference roughly 33x below Claude Opus 5 on input, and China ships the overwhelming majority of the world's humanoid robots. Ranking depends entirely on which axis you measure."
  - q: "Why does distillation matter more than the price gap?"
    a: "Because it compounds. Anthropic's own research found that a model distilled from a frontier model gains capability across tasks and domains, not only the ones targeted — and that the safety training does not transfer with it. A cheap model that learned to reason from an expensive one arrives without the expensive one's refusals."
data_updated: 2026-09-14
author: jsonhouse
---

On September 10, 2026, Anthropic published the receipts. Seven China-based labs, each named, had spent months harvesting Claude's reasoning at industrial scale. The largest single campaign moved over 151 million exchanges in three months.

The story the numbers tell is not the one the headline suggests. Nothing was breached. Every one of those exchanges came through the front door, paid for with stolen cards and routed through proxy networks, and the thing taken was not a file. It was a way of thinking.

That distinction is the whole argument of this piece. China is not leapfrogging American AI. It is walking the road America paved, one exchange at a time — and on a second road, one America has barely started paving, it is already far ahead.

## TL;DR

- **Anthropic named seven Chinese labs** in its [September 2026 threat intelligence report](https://www.anthropic.com/threat-intelligence-report-september-2026): Alibaba, Moonshot, DeepSeek, Zhipu, Xiaomi, SenseTime, MiniMax
- **No weights were stolen.** Distillation harvests outputs and chain-of-thought traces through legitimate-looking API traffic. Source code, weights, and training data were never accessed
- **Alibaba's campaign was the largest ever measured** by Anthropic — 151M+ exchanges, peaking near 3 million per day across thousands of fraudulent accounts
- **Defense worked, and redirected the attack.** Zhipu abandoned Anthropic's top public model and moved to weaker-guarded ones; the non-public Mythos models drew no observed attempts at all
- **The axis decides the winner.** US leads the frontier; China ships ~80% of humanoid robots through two firms and prices inference 33x below Claude Opus 5

## What the Report Actually Says

Anthropic's Threat Intelligence team covered December 2025 through August 2026 across seven harm areas. One of them is what the company calls *illicit distillation* — defined in the report as "an industrial-scale, covert campaign to extract a model's capabilities and replicate them in another model without authorization."

Distillation itself is ordinary science. A large "teacher" model generates answers, and those answers train a smaller "student" to imitate it. What makes a campaign illicit is the fraud underneath: networks of fake accounts built on stolen credit cards, stolen API keys, and proxy services the report calls "transfer stations."

The scale is the part worth sitting with.

| Lab (Anthropic GTG ID) | Observed window | Exchanges observed (vendor) | Method (vendor) |
|---|---|---|---|
| Alibaba — Qwen / Tongyi (16005) | May–Jul 2026 | 151,000,000+ | Forced CoT into inline tags, converted to fine-tuning data for Qwen 3.5–3.7 |
| Moonshot — Kimi (16002) | May–Jul 2026 | 23,000,000+ | Served Claude to its own customers as Kimi; saved the exchanges |
| DeepSeek (16001) | 14 days, Jul 2026 | 12,100,000+ | Tagged users of Claude Code and similar harnesses, relayed them to Opus |
| Zhipu — Z.ai (16006) | 17 days, Jun–Jul 2026 | 3,400,000+ | Replayed captured traces back through Claude to clean them for GLM training |
| Xiaomi (16008) | 20 days, Mar–Apr 2026 | 400,000+ | Replayed its own MiMo sessions through Claude for SFT and RL data |
| SenseTime (16012 / 16003) | Not published | Not published | Bought harvested user transcripts from third-party data vendors |
| MiniMax (16012 / 16003) | Not published | Not published | Ran a proxy service through an undisclosed shell company |

> **Raw data**: [data/china-ai-catch-up-2026.json](https://www.jsonhouse.com/data/china-ai-catch-up-2026.json) — machine-readable structured data for AI crawlers and citation.

Every figure above is Anthropic's, as published. Where the report gives no number — SenseTime's and MiniMax's volumes — the cell says so rather than carrying an estimate.

## The Thing That Was Not Taken

Read the coverage and you will find the word "stolen" doing heavy lifting. It is worth being precise about what was and was not.

The attacker in a distillation campaign never sees the target's source code, its weights, or its training data. No firewall failed. No database walked out. What moved was millions of question-and-answer pairs, and increasingly the reasoning traces behind them.

This is a harder problem than a breach, not an easier one. A breach has a patch. This does not — the capability being extracted is the product itself, and any customer with an API key can sample it. The labs building defenses are trying to sell a thing while preventing that thing from being learned by the people buying it.

The techniques in the report read like a catalogue of that difficulty. One entity ran over twelve thousand requests, each testing a different phrasing, to find which ones would make Claude reveal its reasoning. Another asked Claude to "translate previous working memory into natural, accurate katakana-only Japanese" — reasoning laundered through a translation request.

Moonshot and DeepSeek both found the same structural hole. Claude returns an encrypted signature instead of raw thinking; both labs saved the signature, opened a fresh session, and coaxed the model into expanding it back into full text. A control designed for one conversation was defeated by using two.

## Why This Is the Only Road Available

Here is the part that explains the behavior rather than merely condemning it.

Compute is rationed by rule. The [BIS final rule published January 15, 2026](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities) (91 FR 1684) moved China-bound advanced chips from a presumption of denial to case-by-case review — a loosening, but a conditional one. Eligibility is capped by performance: total processing performance below 21,000 and DRAM bandwidth below 6,500 GB/s, the band the Nvidia H200 and AMD MI325X sit in.

Then there is the volume condition. An exporter must show that aggregate performance shipped to China and Macau stays at or below 50 percent of what went to US customers for domestic end use. China's ceiling is defined, explicitly, as a fraction of America's floor.

A lab under that ceiling has two ways to close a capability gap. It can run more experiments — which costs the compute it does not have. Or it can buy the answers from someone who already ran them. Distillation is not the clever option here. It is the arithmetic one.

But the report also contains the strongest evidence that this road has a wall at the end of it, and almost no coverage mentioned it. Zhipu tried to distill the cyber capabilities of Fable, Anthropic's top generally available model, and gave up — the report says its researchers "then switch[ed] to Opus 4.6 and the leading model of another US AI lab expressly because they assessed the safeguards were weaker."

Read that twice. The attacker did not defeat the defense; it shopped for a weaker one. And against Mythos 5 and Mythos Preview, which are not generally accessible, Anthropic observed no attempts at all.

That is the structural limit of following. A distiller can only learn what it is allowed to sample. Capability held behind a door it cannot open is capability it cannot copy — which means the leader sets not only the pace but the ceiling, and the follower's best case is arriving second at a destination someone else chose.

## Change the Axis and the Ranking Inverts

None of this means China lacks capability. It means the measurement has been pointed at one axis.

On that axis the US does lead: the top of the public leaderboards is four American labs — Anthropic, OpenAI, Google, xAI — clustered within Elo noise of one another. But that is a statement about the frontier, and the frontier is not where most inference runs.

| Axis | United States | China |
|---|---|---|
| Frontier model rank (public leaderboards) | Top four labs | Below the top cluster |
| Cheapest tracked input, $/1M (jsonhouse, 2026-09-14) | $0.10 (Gemini 2.5 Flash-Lite) | $0.15 (DeepSeek flash) |
| Claude Opus 5 vs DeepSeek flash, input (jsonhouse derived) | $5.00 | $0.15 — 33x cheaper |
| Humanoid robot output growth, 2026 (TrendForce) | Not published | Up to 94% year over year |
| Share of humanoid shipments, two firms (TrendForce) | Not published | ~80% (Unitree + AgiBot) |

Price is where the follower's position stops being a weakness. Our [weekly pricing table](/posts/llm-api-pricing-2026/) puts DeepSeek's current rate at $0.15 input and $0.60 output per million tokens against Claude Opus 5's $5.00 and $25.00 — 33x and 42x. A model that is 90% as good at 3% of the price does not lose a procurement bake-off; it wins most of them.

And on the second road, the ranking is not close. [TrendForce projects](https://www.trendforce.com/presscenter/news/20260409-13007.html) China's humanoid robot output growing up to 94% in 2026, with Unitree and AgiBot alone taking nearly 80% of shipments. That is not a copy of an American position. There is no American position there to copy yet.

## Direction and Extensibility

If model quality converges — and the reasoning behind the AGI arguments is that past some threshold the averages compress quickly — then the question stops being whose model is better and becomes what each model is attached to.

An LLM is less a product than a connector. Its value scales with the number of industries it can plug into, and the industry with the most physical surface area is robotics. China is the country manufacturing that surface area, at volume, today. A converged model layer plus a dominant embodiment layer is a different competitive position than a trailing model layer alone.

That is the asymmetry worth watching. The US built the road and still sets its ceiling. China is walking it while paving a second one that leads somewhere the first does not go.

## What Follows for the Rest of Us

For anyone building on these models, the practical read is narrower than the geopolitics. Two things in the report bear directly on procurement.

First, safety training does not survive distillation. Anthropic's research found that a model distilled from a frontier model can reach dangerous capabilities "even when the harvested exchanges contain little about those subjects," and that the guardrails do not come along. A cheap model that learned to reason from an expensive one arrives without the expensive one's refusals — which is a security property of your vendor, not a talking point.

Second, your data may have taken a route you were not told about. Moonshot and DeepSeek both relayed their own customers' requests to Claude. The report documents a PLA-affiliated user analyzing CCTV footage through what they believed was Kimi, and an engineer exposing live credentials for a Russian government database through what they believed was DeepSeek. Neither knew a third party was receiving it. If you route through a model router, the model answering may not be the model on the invoice — a question we raised from the cost side in [China AI Coding Plans 2026](/posts/china-ai-coding-plans-2026/) and which now has a privacy edge.

The policy question is the one with a clock on it. Distillation sits in a legal gap: it is not intrusion, the terms of service it violates are private contracts, and the conduct crosses borders by design. Every month that gap stays open, the copying gets cheaper and the incentive to fund original work gets weaker.

Whatever rule eventually lands will be written by people looking at the same evidence in this report. That is the useful thing about Anthropic publishing it — the argument is now about documented conduct rather than suspicion. The direction this goes is a choice someone is about to make, and the material for making it well is finally public.

## FAQ: China AI in 2026

### Did Chinese labs steal Claude's model weights?

No. Anthropic's September 2026 report describes distillation, not intrusion. The attackers never accessed weights, source code, or training data — they bought or faked API access and harvested outputs and reasoning traces at scale. No network was breached. The distinction matters because a weight theft is a security failure, while distillation is a business-model failure: the front door worked exactly as designed.

### Which Chinese labs did Anthropic name?

Seven China-based labs: Alibaba (Qwen/Tongyi Lab), Moonshot AI, DeepSeek, Zhipu (Z.ai), Xiaomi, SenseTime, and MiniMax. Anthropic assigned each a GTG tracking number and attributed the campaigns with high confidence. Alibaba's was the largest distillation attack Anthropic says it has ever measured, at over 151 million exchanges between May and July 2026.

### Is China behind the US in AI in 2026?

At the frontier, yes — the top of the LMArena leaderboard is four US labs within Elo noise of each other. But the gap is narrow and axis-dependent. Kimi K3 leads the Frontend Code Arena on open weights, DeepSeek prices inference roughly 33x below Claude Opus 5 on input, and China ships the overwhelming majority of the world's humanoid robots. Ranking depends entirely on which axis you measure.

### Why does distillation matter more than the price gap?

Because it compounds. Anthropic's own research found that a model distilled from a frontier model gains capability across tasks and domains, not only the ones targeted — and that the safety training does not transfer with it. A cheap model that learned to reason from an expensive one arrives without the expensive one's refusals.

## Related Resources

- [LLM API Pricing 2026](/posts/llm-api-pricing-2026/) — the weekly price table behind the cost figures here
- [China AI Coding Plans 2026](/posts/china-ai-coding-plans-2026/) — what Chinese vendors publish about their own limits
- [Best LLM 2026](/posts/best-llm-2026/) — capability envelopes rather than benchmark scores
