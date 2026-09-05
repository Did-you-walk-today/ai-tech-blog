---
title: "LLM Cost per Task 2026: When a Pricier Model Is Cheaper"
description: "GPT-6 Astra costs 2.5x GPT-5.6 Sol per token yet 43% less per BenchCAD task. We invert every published cost claim into the token ratio it implies."
date: 2026-09-05 10:00:00 +0000
last_modified_at: 2026-09-05 10:00:00 +0000
categories: [ai-models-intelligence]
tags: [llm-pricing, cost-per-task, gpt-6-astra, benchmarks, token-efficiency, model-routing, "2026"]
format: D
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/llm-cost-per-task-2026-cover.jpg
  alt: "A stack of thick glass prisms on dark stone, cyan light raking one polished edge and amber catching the far corner"
faq:
  - q: "Is GPT-6 Astra cheaper than GPT-5.6 Sol?"
    a: "Per token, no — Astra is exactly 2.5x Sol on every rate line ($10/$50 against $4/$20). Per task, it depends entirely on the task. OpenAI reports Astra finishing BenchCAD at roughly 43% lower estimated API cost than Sol, while Artificial Analysis measured Astra as 75% more expensive per task than Sol on its Intelligence Index at max effort. Both figures can hold at once, because they describe different workloads."
  - q: "How much more token-efficient does a model have to be to justify a 2.5x price?"
    a: "It has to finish the task using less than 40% of the cost-weighted tokens the cheaper model used. That is the break-even line: 1 divided by the price ratio. At 2.5x, a 50% token reduction still leaves you paying 25% more; you need roughly a 60% reduction just to draw level."
  - q: "Why does the cost advantage appear on CAD and terminal tasks but not on reasoning benchmarks?"
    a: "Because the savings come from not retrying. On long agentic tasks with a verifiable success criterion, a weaker model spends tokens on failed attempts, re-reads, and repair loops, and those wasted tokens are where the whole gap lives. A single-turn question has no retry loop to eliminate, so a stronger model has almost no waste to remove and the higher per-token price shows up undiluted."
  - q: "What is cost per successful task, and why is it different?"
    a: "Published cost deltas divide money by attempts, but a business pays for finished work. Dividing the cost ratio by the pass rate gives cost per success, and on Terminal-Bench 4.0 that turns a 9% saving into a 41% one because Astra resolves 57.9% of tasks against Sol's 37.3%. The correction only applies to pass/fail-scored benchmarks — BenchCAD's geometric-overlap score is partial credit, so cost per success cannot be computed for the very claim that carries the biggest headline number."
  - q: "Do the vendors publish a task success rate I can buy against?"
    a: "Rarely, and only in one place in this launch. SRE-Bench is reported as a resolution curve — Astra solved 88.0% of tasks in a single attempt and 99.2% within four, against 55.9% and 68.7% for GPT-5.6 Sol — which is the metric procurement actually needs, because a second attempt is a second bill. Everywhere else, cost, pass rate, and turn budget appear in separate tables that cannot be joined."
  - q: "Can I verify OpenAI's cost-per-task claims?"
    a: "Not directly. OpenAI publishes the percentage but not the token counts, the reasoning-effort setting, or the price basis behind the phrase 'in the configurations shown'. The footnote attached to the BenchCAD claim renders empty on the announcement page. What you can do is invert the claim against the published rate card, which is what the table on this page does."
  - q: "Does this mean I should route every task to the most expensive model?"
    a: "No — the data says the opposite of a blanket rule. The cost advantage is concentrated in long, tool-heavy, verifiable work. On short reasoning and Q&A the premium model costs 75% more for a 0.3-point score gain. The efficient policy is routing by task shape, not by model rank."
data_updated: 2026-09-05
author: jsonhouse
---

GPT-6 Astra costs exactly 2.5 times GPT-5.6 Sol per token. On BenchCAD, a 3D CAD-reconstruction benchmark, OpenAI reports it finishing tasks at roughly **43% lower estimated API cost** than Sol. Those two facts are not in conflict, and reconciling them gives a number neither vendor publishes: the token ratio the expensive model had to hit. This page inverts every published cost-per-task claim from the 2026-09-03 GPT-6 Astra launch into that ratio, and states the break-even line for each baseline model.

## TL;DR

- **The price ratio is exactly 2.5x.** Astra is $10/$50 per million input/output tokens against Sol's $4/$20 — and the same 2.5 multiple holds on cached input, long-context, and fast-mode rates. That uniformity makes the inversion exact.
- **Break-even is 40%.** To cost less per task than Sol, Astra must finish using under 40% of Sol's cost-weighted tokens. Against Claude Opus 5 the line is 50%; against Claude Fable 5.1, priced identically at $10/$50, any reduction at all wins.
- **BenchCAD's 43% saving implies Astra used ~23% of Sol's tokens** — a 4.4x efficiency ratio. Terminal-Bench 4.0's 9% saving implies ~36%, barely inside the line.
- **Charge per success and the gap widens.** Terminal-Bench 4.0's 9% saving becomes **41%** once cost is divided by pass rate. On SRE-Bench, Sol at four attempts still finishes 19 points below Astra at one — on agentic work the weaker model's errors *are* the cost.
- **But the same model runs the other way on reasoning.** Artificial Analysis measured Astra at **75% more expensive per task** than Sol on its Intelligence Index at max effort, for a 0.3-point score gain. Nobody publishes the token counts behind any of it.

## What the vendors actually published

On 2026-09-03 OpenAI [announced GPT-6 Astra](https://openai.com/index/gpt-6-astra/) with benchmark tables and, unusually, cost-per-task deltas attached to several of them. The claims are stated as percentages against named competitors, never as dollar amounts or token counts.

The BenchCAD line is the sharpest of them. [BenchCAD](https://arxiv.org/abs/2605.10865) asks a model to reconstruct 3D objects from multi-view renders by writing parametric CAD code, then scores geometric overlap against ground truth. It is a long, tool-using task with a machine-checkable answer — exactly the shape where retry loops dominate spend.

OpenAI reports Astra at 95.9% geometric overlap versus 83.3% for GPT-5.6 Sol and 84.3% for Claude Fable 5.1, with estimated API cost "approximately 43% lower than Sol and 86% lower than Fable 5.1 in the configurations shown."

Three other benchmarks carry cost claims: Terminal-Bench 4.0, Terminal-Bench Science 0.1, and GPQA Diamond. A fourth, Agents' Last Exam, carries an output-token claim (65% fewer than Claude Opus 5) but **no cost figure at all** — that gap is left as-is below rather than filled with an estimate.

## The price ratios, verified against the rate cards

The inversion only works if the price relationship between two models is a single constant. For the three baselines OpenAI compares against, it is — and that is a fact about these specific rate cards, not a general property.

| Model | Input / 1M (vendor) | Cached input / 1M (vendor) | Output / 1M (vendor) | Ratio vs Astra (jsonhouse) | Uniform? (jsonhouse) |
|---|---|---|---|---|---|
| GPT-6 Astra | $10.00 | $1.00 | $50.00 | 1.00x | — |
| GPT-5.6 Sol | $4.00 | $0.40 | $20.00 | **2.50x** | Yes, all three lines |
| Claude Opus 5 | $5.00 | $0.50 | $25.00 | **2.00x** | Yes, all three lines |
| Claude Fable 5.1 | $10.00 | $0.25 | $50.00 | **1.00x** | No — cache reads differ 4x |
| GPT-5.6 Terra | $2.00 | $0.20 | $12.00 | 5.00x / 4.17x | No — input and output differ |

> **Raw data**: [data/llm-cost-per-task-2026.json](https://www.jsonhouse.com/data/llm-cost-per-task-2026.json) — machine-readable structured data for AI crawlers and citation.

Rates verified 2026-09-05 against the [OpenAI API pricing page](https://developers.openai.com/api/docs/pricing) and the [Claude API pricing page](https://platform.claude.com/docs/en/about-claude/pricing), and cross-checked against our own weekly snapshot taken 2026-09-01.

Sol's 2.5x relationship holds on every line OpenAI publishes, including the long-context tier ($8/$30 against Astra's $20/$75) and fast mode, which doubles both models identically. So the ratio survives any mix of input, output, cached, and long-context tokens.

Fable 5.1 is the exception worth naming. Its base input and output match Astra exactly, but its cache hits are priced at 0.025x base rather than the usual 0.1x — $0.25 against Astra's $1.00. On a cache-heavy workload Fable 5.1 is materially cheaper on the input side than the flat 1.00x suggests.

One more property of the Sol column matters. Sol's $4/$20 is **promotional**, stated as available at least through 2026-11-21, with no published successor rate. Every "43% lower than Sol" figure is therefore measured against a price with an expiry date on it, tracked in our [LLM API pricing database](/posts/llm-api-pricing-2026/).

## Methodology

Every derived figure on this page comes from one operation. If a model's rates all scale by a constant *k* relative to the reference model, then cost per task is *k* times the cost-weighted token spend, and the token ratio follows directly from the published cost delta.

Implied token ratio = (1 − cost saving) ÷ *k*.

For BenchCAD against Sol: (1 − 0.43) ÷ 2.5 = 0.228. Astra must have consumed about 23% of Sol's cost-weighted tokens — roughly a 4.4x efficiency ratio — for a 43% cost saving to hold at 2.5x the price.

The break-even line falls out of the same relation. Setting the cost ratio to 1 gives a token ratio of 1 ÷ *k*: 40% against Sol, 50% against Opus 5, 100% against Fable 5.1.

The cost-per-success column uses the same published inputs and one more division. Each model's relative cost per success is its cost ratio divided by its pass rate, and the saving is one minus the ratio of the two. For Terminal-Bench 4.0 against Sol: Astra is 0.91 ÷ 0.579 = 1.572, Sol is 1.00 ÷ 0.373 = 2.681, so the saving is 1 − 1.572 ÷ 2.681 = 41%.

That division is only legitimate where the score *is* a pass rate. Terminal-Bench, Terminal-Bench Science, and GPQA Diamond report resolved-or-not; BenchCAD reports geometric overlap, a continuous partial-credit score, and is therefore left as "Not derivable" rather than treated as if 95.9% meant 95.9% of tasks finished.

"Cost-weighted tokens" is the necessary unit, not raw token count. It blends input, cached input, and output at their own prices. Because *k* is uniform for these three baselines, the blend cancels and the ratio is exact — which is why the Terra row above is excluded from the derivation rather than estimated.

Inputs: OpenAI's published scores and cost deltas (retrieved 2026-09-05), vendor rate cards (retrieved 2026-09-05), and Artificial Analysis index results (retrieved 2026-09-05). Nothing here is measured by us; the arithmetic is, and it is fully reproducible from the two columns of source data.

## Every published cost claim, inverted

| Benchmark | Astra score (vendor) | Baseline | Baseline score (vendor) | Cost delta (vendor) | k (rate card) | Implied token ratio (jsonhouse derived) | Implied token reduction (jsonhouse derived) |
|---|---|---|---|---|---|---|---|
| BenchCAD | 95.9% | GPT-5.6 Sol | 83.3% | −43% | 2.50x | 0.23 | ~77% |
| BenchCAD | 95.9% | Claude Fable 5.1 | 84.3% | −86% | 1.00x | 0.14 | ~86% |
| Terminal-Bench 4.0 | 57.9% | GPT-5.6 Sol | 37.3% | −9% | 2.50x | 0.36 | ~64% |
| Terminal-Bench 4.0 | 57.9% | Claude Fable 5.1 | 55.8% | −63% | 1.00x | 0.37 | ~63% |
| Terminal-Bench Science 0.1 | 64.6% | Claude Fable 5.1 | 52.6% | −31% | 1.00x | 0.69 | ~31% |
| Terminal-Bench Science 0.1 (low-cost setting) | 61.1% | GPT-5.6 Sol | 22.4% | −27% | 2.50x | 0.29 | ~71% |
| GPQA Diamond (low-cost setting) | 94.9% | GPT-5.6 Sol | 94.6% | −37% | 2.50x | 0.25 | ~75% |
| Agents' Last Exam | 59.3% | Claude Opus 5 | 55.5% | Not published | 2.00x | Not derivable | 65% output tokens only |
| AA Intelligence Index v4.1.1 | 61.2 | GPT-5.6 Sol | 60.9 | **+75%** | 2.50x | 0.70 | ~30% |
| AA Coding Agent Index v1.4 | 67.0 | GPT-5.6 Sol | 65.1 | ~0% | 2.50x | ~0.40 | ~60% |

The bottom two rows are not OpenAI's. They come from [Artificial Analysis](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra), which runs both models itself and reports the cost it actually paid — $2.57 per Intelligence Index task for Astra at max effort.

Read the Implied token reduction column top to bottom and the pattern is not subtle. The claims cluster at two ends: roughly 60–86% reductions on tool-using agentic work, and roughly 30% on everything else.

## The part the percentages hide

The interesting result is not that Astra is cheaper. It is that **the same model, at the same price, lands on both sides of the line depending on what you ask it to do.**

OpenAI's BenchCAD claim and Artificial Analysis's Intelligence Index measurement are 43% cheaper and 75% more expensive respectively, against the same baseline model. Neither is wrong. They measure different task shapes.

The mechanism is retry, not brevity. On BenchCAD a run either produces a CAD program that matches the render or it does not, and a model that misreads a helical sweep spends its budget on attempts that score zero. Those failed attempts are billed at full rate. Eliminating them is worth far more than writing shorter answers.

### The weaker model's errors are the line item

That is not only an inference. Three of OpenAI's own disclosures show failure loops consuming budget directly, and one of them is an admission against interest.

The clearest is footnote 14. On the internal ExploitBench (June–August 2026) set, GPT-5.6 Sol scored 5.5%, and OpenAI states plainly that this figure "is an artifact of the 300-turn limit in the benchmark" — at fewer limits the same model reached 11.5%. A weaker model burned through 300 turns and still did not finish. Those turns were billed.

The second is ExploitGym, where OpenAI removed the benchmark's six-hour cap for both models because they were "fast enough that it has little impact." A time cap only binds a model that is still looping when the clock runs out, which is a statement about failure, not about speed.

The third is OSWorld 2.0. Astra scores 72.6% at roughly 40 minutes per task against Sol's 65.7% at roughly 75 minutes. Wall-clock time on an agentic benchmark is a proxy for iterations, and iterations are tokens.

Put together, the picture is consistent: on this class of work the weaker model does not produce a cheaper answer. It produces a longer, more expensive path to a worse one. **Error is not a quality problem that happens to sit next to a cost problem — on agentic work, error is the cost.**

That is why the savings concentrate where they do. Terminal-Bench 4.0, Terminal-Bench Science 0.1, and BenchCAD are all long-horizon, tool-mediated, machine-verifiable. GPQA Diamond is the outlier in the list, and it is the one where the score gap is 0.3 points — the saving there comes from a deliberately lower-cost configuration, not from being better at the task.

Turn it around and the Intelligence Index result stops being surprising. A single-turn question has no failed-attempt budget to reclaim. The stronger model produces roughly 10% fewer output tokens, the price is 2.5x, and the arithmetic does the rest.

So the usable rule is not "smarter models are cheaper." It is narrower and more useful: **a premium model pays for itself in proportion to how much waste the task contains.** Work with long tool loops and a verifiable outcome contains a great deal. A classification call or a summarization pass contains almost none.

## Cost per successful task, not cost per task

Every percentage published so far divides money by *attempts*. A business divides money by *finished work*. Those are different numbers, and on a benchmark scored pass/fail the second one is derivable from the first.

Divide the cost ratio by the success rate and the ranking shifts. Terminal-Bench 4.0 is the case that matters: a headline saving of 9% becomes 41% once each run is charged against a task actually resolved.

| Benchmark (pass/fail scored) | Baseline | Astra pass rate (vendor) | Baseline pass rate (vendor) | Cost per attempt (vendor) | **Cost per success (jsonhouse derived)** |
|---|---|---|---|---|---|
| Terminal-Bench 4.0 | GPT-5.6 Sol | 57.9% | 37.3% | −9% | **−41%** |
| Terminal-Bench 4.0 | Claude Fable 5.1 | 57.9% | 55.8% | −63% | **−64%** |
| Terminal-Bench Science 0.1 | Claude Fable 5.1 | 64.6% | 52.6% | −31% | **−44%** |
| Terminal-Bench Science 0.1 (low-cost setting) | GPT-5.6 Sol | 61.1% | 22.4% | −27% | **−73%** |
| GPQA Diamond (low-cost setting) | GPT-5.6 Sol | 94.9% | 94.6% | −37% | **−37%** |
| BenchCAD | GPT-5.6 Sol | Not a pass rate | Not a pass rate | −43% | **Not derivable** |
| BenchCAD | Claude Fable 5.1 | Not a pass rate | Not a pass rate | −86% | **Not derivable** |

The gap between the last two columns is the whole enterprise argument. Where pass rates are close, nothing moves — GPQA Diamond stays at 37% because both models answer nearly every question. Where they diverge, the correction is large, and it always runs in the stronger model's favour.

The bottom two rows are the uncomfortable ones. BenchCAD carries the largest cost claim on the page, and it is scored by geometric overlap — a continuous partial-credit measure, not a pass rate. So the one benchmark with the headline number is the one where cost per success cannot be computed at all.

That is not a rounding problem. A CAD program at 83.3% geometric overlap is not 83.3% of a part. It is a part that does not fit, and the cost of discovering that lands downstream of the API bill entirely — in a rejected drawing, a scrapped machining run, a design review that has to happen twice.

## What benchmarks would have to report

If error is the dominant cost on agentic work, then the metric buyers need is not on any current leaderboard. Scores answer "how good is it." Procurement asks "what does one finished, trustworthy unit of work cost." Three additions would close that gap.

**A resolution curve by attempt number, reported next to cost.** One benchmark in OpenAI's tables already does this, and it is the most instructive result in the announcement. On SRE-Bench, which asks a model to reverse-engineer software binaries without source, Astra solved 88.0% of tasks in a single attempt and 99.2% within four. GPT-5.6 Sol solved 55.9% and 68.7% on the same two measures.

Read the second pair against the first. Sol at four attempts — four bills — still lands nearly 20 points below Astra at one. That single line does more to justify a 2.5x price than any token-efficiency claim on the page, and it is the only place OpenAI reports the shape rather than a single number.

**The turn and retry budget consumed.** Footnote 14's admission — that a 5.5% score was an artifact of a 300-turn cap, and the same model reached 11.5% with fewer limits — shows that turn budget is doing quiet work inside every agentic result. A benchmark that reports turns consumed alongside the score makes the retry cost visible instead of leaving it to be inferred from a cost percentage.

**A silent-failure rate.** Partial-credit scoring cannot distinguish a model that refuses a task it cannot do from one that returns a confident, plausible, wrong artifact. For an enterprise those two outcomes have opposite costs: the first is cheap and the second is the expensive one, because it passes review. OpenAI does publish an internal hallucination benchmark (4.2% against Sol's 12.2%), but it sits in a separate table from every cost claim, so nothing connects the two.

None of this requires a new institution. Terminal-Bench and SRE-Bench already score pass/fail; what is missing is the discipline of publishing cost, pass rate, and turn budget as one triple rather than three tables that cannot be joined. Until a vendor does, the join has to be done by hand — which is what the table above is.

## What is not published

Three gaps are worth naming, because they set the limits on how far these numbers travel.

**The configurations.** OpenAI's cost claims are qualified as "in the configurations shown," and reasoning effort is the single largest lever on token count. The announcement states separately that scores are "the maximum at any effort" — which is not the same statement, and the footnote attached to the BenchCAD cost claim renders empty on the page. Two of the seven rows above are explicitly labelled as lower-cost settings, so the configurations demonstrably vary within the same table.

**The token counts.** No vendor publishes tokens per task for these runs. That is what makes the inverted column a derivation rather than a measurement, and it means a reader cannot check the claim against anything except the rate card.

**The tokenizer.** Anthropic states that Claude 4.7 and later use a tokenizer producing approximately 30% more tokens for the same text. Both Fable 5.1 comparisons above cross that boundary, so part of the 86% and 63% reductions is a unit difference rather than an efficiency difference. The Sol comparisons are within one vendor's tokenizer and do not carry this problem.

## How to compute your own break-even

The published percentages describe OpenAI's benchmark harness, not your workload. The same arithmetic runs on your own logs, and it needs only two numbers.

Take your current model's average cost-weighted token spend on a representative task, including failed and retried runs — that inclusion is the whole point, since excluding failures measures the wrong thing. Then take the candidate model's price ratio *k* from the rate card, checking that it is uniform across input, cached, and output lines before treating it as a single number.

The candidate wins if it finishes below 1 ÷ *k* of your current spend. At 2.5x that is 40%, which is a demanding bar that only long agentic work with real failure rates tends to clear.

This is also the calculation that decides routing. Our [best LLM comparison for 2026](/posts/best-llm-2026/) ranks models by capability; this page is the reminder that capability rank and cost rank are different orderings, and that the gap between them is where prompt caching does its work — see the [LLM cache pricing breakdown](/posts/llm-cache-pricing-2026/) for how cached input changes *k* in practice.

## Limitations

- Every score and cost delta on this page is vendor-reported or third-party-reported. We ran no benchmarks.
- The inversion assumes the published cost delta and the published score come from the same run. OpenAI does not state this explicitly.
- Percentages are rounded in the source ("approximately 43%"), so implied ratios carry that rounding forward. Treat the second decimal as noise.
- The Fable 5.1 rows assume cache reads are a negligible share of spend. If they are not, k is below 1.00x and the implied reductions overstate the gap.
- GPT-5.6 Sol's $4/$20 is promotional with a stated floor date of 2026-11-21 and no published successor rate. If it rises, every Sol row moves.
- Artificial Analysis's +75% figure is reported without a token decomposition, so its implied 0.70 ratio is less well-constrained than the OpenAI-derived rows.
- Cost per success is computed only for pass/fail-scored benchmarks. It assumes a failed attempt costs about what a successful one costs, which is the conservative direction — failed agentic runs usually cost more, because they exhaust turn or time budgets.
- Cost per success counts the API bill for a retry. It does not count the downstream cost of a wrong artifact that passes review, which is the larger number for most businesses and is not measured by any benchmark here.

## Update cadence

This table is refreshed **monthly, on the first Monday**, and additionally within 48 hours of any frontier-model launch that ships cost-per-task claims. Refresh means three things: re-verifying the rate cards, adding newly published claims, and re-deriving every row against current prices. Rows are never deleted — a superseded claim is kept with its original date so the ledger stays comparable over time.

## Changelog

- **2026-09-05** — Initial publication. Seven OpenAI cost claims from the 2026-09-03 GPT-6 Astra launch plus two Artificial Analysis index results, inverted against rate cards verified 2026-09-05.

## FAQ

### Is GPT-6 Astra cheaper than GPT-5.6 Sol?

Per token, no — Astra is exactly 2.5x Sol on every rate line ($10/$50 against $4/$20). Per task, it depends entirely on the task. OpenAI reports Astra finishing BenchCAD at roughly 43% lower estimated API cost than Sol, while Artificial Analysis measured Astra as 75% more expensive per task than Sol on its Intelligence Index at max effort. Both figures can hold at once, because they describe different workloads.

### How much more token-efficient does a model have to be to justify a 2.5x price?

It has to finish the task using less than 40% of the cost-weighted tokens the cheaper model used. That is the break-even line: 1 divided by the price ratio. At 2.5x, a 50% token reduction still leaves you paying 25% more; you need roughly a 60% reduction just to draw level.

### Why does the cost advantage appear on CAD and terminal tasks but not on reasoning benchmarks?

Because the savings come from not retrying. On long agentic tasks with a verifiable success criterion, a weaker model spends tokens on failed attempts, re-reads, and repair loops, and those wasted tokens are where the whole gap lives. A single-turn question has no retry loop to eliminate, so a stronger model has almost no waste to remove and the higher per-token price shows up undiluted.

### What is cost per successful task, and why is it different?

Published cost deltas divide money by attempts, but a business pays for finished work. Dividing the cost ratio by the pass rate gives cost per success, and on Terminal-Bench 4.0 that turns a 9% saving into a 41% one because Astra resolves 57.9% of tasks against Sol's 37.3%. The correction only applies to pass/fail-scored benchmarks — BenchCAD's geometric-overlap score is partial credit, so cost per success cannot be computed for the very claim that carries the biggest headline number.

### Do the vendors publish a task success rate I can buy against?

Rarely, and only in one place in this launch. SRE-Bench is reported as a resolution curve — Astra solved 88.0% of tasks in a single attempt and 99.2% within four, against 55.9% and 68.7% for GPT-5.6 Sol — which is the metric procurement actually needs, because a second attempt is a second bill. Everywhere else, cost, pass rate, and turn budget appear in separate tables that cannot be joined, so the join has to be done by hand.

### Can I verify OpenAI's cost-per-task claims?

Not directly. OpenAI publishes the percentage but not the token counts, the reasoning-effort setting, or the price basis behind the phrase "in the configurations shown". The footnote attached to the BenchCAD claim renders empty on the announcement page. What you can do is invert the claim against the published rate card, which is what the table on this page does.

### Does this mean I should route every task to the most expensive model?

No — the data says the opposite of a blanket rule. The cost advantage is concentrated in long, tool-heavy, verifiable work. On short reasoning and Q&A the premium model costs 75% more for a 0.3-point score gain. The efficient policy is routing by task shape, not by model rank. The same logic drove the pricing shifts we tracked in the [2026 LLM price war balance sheet](/posts/llm-price-war-balance-sheet-2026/).
