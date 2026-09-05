---
title: "LLM Price War 2026: Who Is Paying for Your Discount"
description: "CoreWeave raised compute prices 25% in July, citing component costs. Token prices fell anyway. Five snapshots, 48 models, and the gap capital is paying for."
date: 2026-08-21 10:00:00 +0000
last_modified_at: 2026-09-05 14:40:00 +0000
categories: [industry-analysis]
tags: [llm-pricing, ai-capex, data-centers, nvidia, openai, ai-economics, compute-contracts, "2026"]
format: F
cluster: CLUSTER_LLM
image:
  path: /assets/img/posts/llm-price-war-balance-sheet-2026-cover.jpg
  alt: "A single rectangular block of thick optical glass tilted on dark stone, one bevelled corner catching cyan light"
faq:
  - q: "Why are AI data center prices going up in 2026?"
    a: "Three costs moved at once. PC DRAM contract prices rose 105-110% quarter-over-quarter in Q1 2026, the steepest single-quarter increase on record, and HBM capacity for 2026 is sold out. AI racks draw 10-20 kW against 3-5 kW for a standard rack, so power replaced floor space as the binding constraint. And PJM capacity prices rose 833% between the 2024-25 and 2025-26 delivery years. CoreWeave raised prices 25% in July citing demand and component costs."
  - q: "Will rising data center costs push LLM API prices up?"
    a: "It already pushed compute prices up — CoreWeave raised its rates 25% in July 2026 — and stopped there. Over the same period the labs that rent compute most heavily cut their token prices or cancelled planned increases. The pass-through is real at the infrastructure layer and has not reached published token prices. Something is absorbing the difference."
  - q: "Do AI companies that own their data centers have a pricing advantage?"
    a: "Less than the framing suggests, because the categories have collapsed. Google owns one of the world's largest TPU fleets and still reportedly agreed to rent roughly 110,000 GPUs from SpaceX. Anthropic rented essentially all of xAI's Colossus 1. Meta is preparing to sell its spare capacity. Owning does not insulate you when your marginal capacity is rented, and the margin is where price gets set."
  - q: "Why don't LLM API prices change more often?"
    a: "Because the published price is not where the competition happens. Across 48 models we tracked between 2026-07-16 and 2026-08-17, 43 did not change at all in 32 days. Discounting runs through subscription plans, promotional tiers, free allowances, and enterprise contracts — none of which appear on a pricing page."
  - q: "Is Google's Gemini Flash price cut permanent?"
    a: "No, and Google says so on its own pricing page. Both gemini-3.6-flash and gemini-3.7-flash carry an introductory rate that expires 2026-12-31 and doubles to $1.50 input / $7.50 output on 2027-01-01. It is a published forward price, not a price cut, and it should be budgeted as one."
  - q: "Does OpenAI have bonds coming due?"
    a: "No bonds have been reported. OpenAI was reported to carry no debt as of 2026-03-31, with under $750 million in lease obligations. What it holds is credit capacity — a revolving facility of roughly $4.7 billion plus a $520 million line — and roughly $600 billion in forward compute commitments. The borrowing sits with its counterparties instead."
data_updated: 2026-08-17
author: jsonhouse
---
In July 2026, CoreWeave raised the price of its AI compute by 25%. The reason it gave was component costs. Its capacity sold out anyway.

Over the same weeks we recorded every published price change across 48 large language models. Every major move went down.

Compute got more expensive. Tokens got cheaper. Someone is paying the difference, and working out who explains more about this industry than either number does alone.

## TL;DR

- **The rent is genuinely rising.** DRAM contract prices rose 105–110% in a single quarter, AI racks draw 3–5× the power of a standard rack, and PJM capacity prices rose 833% in one delivery year. CoreWeave passed 25% of it on in July.
- **43 of 48 models did not move at all** in 32 days. The published price is not where the price war is being fought.
- **The moves that happened went down.** Google halved gemini-3.6-flash. OpenAI cut gpt-5.6-luna 80% and gpt-5.6-terra 20%.
- **Anthropic cancelled a scheduled increase.** The $3/$15 move planned for 2026-09-01 will not happen. $2/$10 is now standard.
- **Google's cut has an expiry printed on it.** The Flash rate is introductory and doubles on 2027-01-01.
- **Owning your data centers no longer means what it sounds like.** Google reportedly rents ~110,000 GPUs from SpaceX. Anthropic rented essentially all of xAI's Colossus 1. Everyone is both landlord and tenant.
- **OpenAI has no bonds to mature.** It has commitments. The debt sits with Oracle, SoftBank and private credit, and S&P has already cut Oracle toward junk over it.

## The ledger

Every row is a change between two observed snapshots, not a vendor announcement. Prices are USD per 1M tokens, standard non-batch tier.

| Model | Input (vendor) | Output (vendor) | Output change (jsonhouse derived) | Direction (jsonhouse derived) |
|---|---|---|---|---|
| gpt-5.6-luna | $1.00 → $0.20 | $6.00 → $1.20 | −80% | Cut |
| gemini-3.6-flash | $1.50 → $0.75 | $7.50 → $3.75 | −50% | Cut, expires 2026-12-31 |
| gpt-5.6-terra | $2.50 → $2.00 | $15.00 → $12.00 | −20% | Cut |
| deepseek-v4-flash | $0.14 → $0.22 | $0.28 → $0.66 | +136% | Increase |
| deepseek-v4-pro | $0.435 → $0.66 | $0.87 → $1.98 | +128% | Increase |

> **Raw data**: [data/llm-price-war-balance-sheet-2026.json](https://www.jsonhouse.com/data/llm-price-war-balance-sheet-2026.json) — machine-readable structured data for AI crawlers and citation.

The first number that matters is not in the table.

Forty-three of the 48 models we track did not change price at all in 32 days. In a market everyone calls a price war, almost nothing moves.

That is because the published price is a marketing surface, not a battlefield. Real discounting happens in subscription plans, promotional tiers, free allowances and enterprise contracts. None of it appears on a pricing page.

This post is about the handful of moves that did.

The two DeepSeek increases are in the table because they happened. They are deliberately left out of the analysis below.

DeepSeek announced the rise on its own pricing page before it landed, moved to a clean 1:3 output-to-input ratio that is still near the bottom of the industry range, and introduced peak and off-peak hourly rates in the same week. That reads as packaging and capacity management. It also sits outside the Western compute-financing structure this post is about.

One thing that did not move matters as much as the ones that did.

Anthropic had told the market that Claude Sonnet 5's $2/$10 launch price was introductory, and that it would rise to $3/$15 on 2026-09-01. The increase was cancelled.

A company that had already announced it would charge more decided not to.

## What was happening to the money

The same five weeks were extraordinarily active on the financing side.

On 2026-08-10, Nvidia [announced memorandums of understanding](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital) with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to mobilize over $500 billion of third-party capital for AI compute. The release calls NVIDIA compute "an investable asset." It also says the partnerships "remain subject to execution of the final agreements." These are MOUs, not signed deals.

A week later, [CNBC reported](https://www.cnbc.com/2026/08/17/nvidia-financing-open-ai-data-center-ohio.html) that Nvidia would guarantee up to $105 billion of OpenAI's leases at an SB Energy campus in Pike County, Ohio. Up to 8 gigawatts, first 800 megawatts online in 2028, on a 20-year lease. Nvidia had reportedly weighed roughly $250 billion before scaling back.

Neither of those is a chip sale. Both are credit.

Nvidia is lending its balance sheet so that customers who could not otherwise finance compute can buy compute. Why that is necessary explains the price table better than the price table does.

## The analysis

### Why the landlords are raising prices

Start with the obvious question. If compute is scarce and expensive, what made it scarce and expensive?

The providers say their costs went up. They are right, and the rise is unusually easy to trace, because it arrived in three layers at once.

**Silicon.** PC DRAM contract prices rose 105–110% quarter over quarter in Q1 2026. That is the steepest single-quarter increase on record.

The cause was reallocation. Roughly 70% of DRAM output went to AI server customers, HBM capacity for 2026 sold out completely, and manufacturers began refusing new orders. Gartner has projected memory costs rising on the order of 130%, with the crunch running into 2027. SK Hynix has warned the shortage could outlast 2030.

A server is not a GPU by itself. The parts around the GPU repriced violently.

**Density.** The hardware also got hungrier.

A standard rack draws 3–5 kW. A high-density AI rack draws 10–20 kW, which turns a $300–1,000 monthly power charge into $1,000–4,000 or more.

That is why power, not floor space, now decides where a data center can go. North American colocation vacancy sits near 1%, and roughly 92% of the capacity under construction is spoken for before a single cabinet is installed.

**Power.** Then electricity itself repriced.

PJM capacity prices rose 833% between the 2024–25 and 2025–26 delivery years. Data centers now account for around 40% of US electricity demand growth, and researchers estimate generation costs could run 20–30% higher by 2028 than they would have otherwise.

Households can see it. Virginia residential rates are up more than 13% in a year.

That last cost is contested enough that one lab has taken a public position on it.

In February 2026 Anthropic [committed to covering the electricity price increases](https://www.anthropic.com/news/covering-electricity-price-increases) its data centers cause. It pledged to pay "100% of the grid upgrades needed to interconnect our data centers," on the grounds that "AI companies shouldn't leave American ratepayers to pick up the tab."

In accounting terms, that is a cost moved off the ratepayer and onto the lab.

### The rent rose 25%. Token prices fell

CoreWeave is where the cost story turns into an observed price.

In July it raised rates 25% across its SKUs. On its [Q2 2026 earnings call](https://www.fool.com/earnings/call-transcripts/2026/08/18/coreweave-crwv-q2-2026-earnings-call-transcript/) management put the move down to the demand environment and component costs. Backlog reached $104.2 billion, up 246% year over year. Capacity stayed effectively sold out afterwards.

So the recontracting has already started. It just has not arrived where you pay.

One detail complicates the cost explanation, and it is the most revealing number here. CEO Michael Intrator said contracts signed in the quarter carry contribution margins **five to ten percentage points higher** than recent ones.

A pure cost pass-through leaves margins flat. This one widened them.

The costs are real, then, and the increase was bigger than the costs. That is what a market at 1% vacancy lets you do. "Our components got expensive" is accurate, and it still understates what happened.

Now the step that should follow, and does not.

Labs that rent compute should be squeezed at renewal and pass it on. Labs that own should hold their prices and take share. It is a clean prediction with a visible signature.

Our window shows the reverse. OpenAI runs on Azure, Oracle and CoreWeave and owns no data centers, and it cut 80%. Anthropic buys compute from AWS, Google, Microsoft, CoreWeave and xAI, and it cancelled a planned increase. Google owns one of the largest compute fleets in existence, and is the only vendor in our set to have published a future rise.

### Nobody is purely an owner any more

The prediction assumes a line between owners and renters. That line has quietly disappeared.

Google owns an enormous TPU fleet. It also, per reporting, agreed to rent roughly 110,000 GPUs from SpaceX between October 2026 and June 2029, at about $920 million a month.

Anthropic is the archetypal renter. In May 2026 it rented essentially all the capacity of xAI's Colossus 1, which makes one AI lab the landlord of another.

Meta owns Prometheus and Hyperion, and is reportedly preparing to sell its spare capacity as a cloud product.

| Vendor | Owns compute | Rents compute | Rents out to others |
|---|---|---|---|
| Google | Yes, large TPU fleet | Yes, ~110k GPUs from SpaceX, reported ~$920M/month | Yes, Google Cloud |
| xAI | Yes, Colossus, ~770k GPUs, ~1 GW | — | Yes, Colossus 1 to Anthropic |
| Anthropic | Building, via a Fluidstack partnership | Yes, AWS, Google, Microsoft, CoreWeave, xAI | — |
| OpenAI | No | Yes, Azure, Oracle, CoreWeave, plus a 20-year Ohio lease | — |
| Meta | Yes, Prometheus and Hyperion | Yes, Google TPUs | Reportedly planned |

So owning does not protect you. Your marginal capacity is rented, and the margin is where price gets set.

It is not free either. On 2026-07-24 [Moody's warned](https://www.cnbc.com/2026/07/24/moodys-ai-spending-credit-quality-amazon-meta-alphabet.html) that unprecedented AI spending threatens the credit quality of Amazon, Meta and Alphabet.

The real exposure is not ownership. It is your renewal date.

And that is the number nobody publishes. Not one vendor in the table above discloses when its compute contracts reprice. The most decision-relevant figure in this market is missing from every pricing page, every model card and every announcement.

### Google printed the expiry date on its own subsidy

There is exactly one exception, which is why it is worth dwelling on.

Halving gemini-3.6-flash looks like the boldest move in the ledger until you read the footnote on Google's pricing page. The rate is introductory. It expires 2026-12-31. On 2027-01-01 it doubles to $1.50/$7.50, and the newer 3.7-flash carries the same terms.

Google has done what no competitor has done. It published what it intends to charge later.

If you are building a cost model on Flash today, the number to model is the 2027 one.

This is what a land grab looks like when the company running it can afford to announce the end date. It is also the closest thing here to an answer on recontracting. Not because Google's rent is rising, but because a subsidy with a published expiry is the only kind you can plan around.

### OpenAI did not borrow. The world borrowed against OpenAI

The premise that OpenAI faces a wall of maturing bonds does not survive contact with the record.

OpenAI was reported to hold no debt as of 2026-03-31, with under $750 million in lease obligations. What it holds is capacity: a revolving credit facility [expanded to roughly $4.7 billion](https://openai.com/index/new-credit-facility-enhances-financial-flexibility/) across an eleven-bank syndicate, plus a $520 million line added in July.

A revolver is undrawn headroom. It is not a bond with a maturity date.

The obligation is real. It simply sits on the other side of the table.

OpenAI has committed roughly $600 billion in forward compute spending, and its counterparties financed it. Oracle borrowed. SoftBank borrowed $40 billion to buy its stake. SB Energy is building against a 20-year lease that Nvidia now guarantees. Private credit has put roughly $60 billion into data center development through instruments the SEC never sees.

OpenAI is unrated, so no agency can downgrade it. The market repriced its counterparties instead.

S&P cut Oracle toward junk, citing OpenAI exposure. Moody's flagged significant counterparty risk on Oracle's $300 billion OpenAI contract. S&P trimmed SoftBank's outlook, calling OpenAI the weakest credit quality among its investments. Roughly half of Oracle's $638 billion in remaining performance obligations is one customer.

That is why finance is uncomfortable with OpenAI. Not that it is unprofitable. That it is unpriceable.

Being private means the market cannot put a number on the risk directly. So it puts the number on everyone standing next to it.

## The bigger picture

One more force is pressing on the same constraint.

Inference demand is no longer driven by humans typing. Our own [crawler measurements](/posts/ai-crawler-traffic-2026/) recorded 747 machine requests for every human visit that AI answers sent back. Agent traffic is heavy on output tokens by construction, so the demand pushing against that 1% vacancy is growing from a direction that did not exist three years ago.

Put the halves together and the next two years become legible. Compute supply is constrained and repricing in the landlord's favour, and one landlord has already moved 25%. Token prices are flat or falling because capital, not revenue, is paying the difference.

Both cannot hold forever. The published data gives us exactly one date on which one of them is scheduled to give.

## What this means if you are the one paying the bill

Put 2027-01-01 in your calendar.

It is the only scheduled future price change any tracked vendor has published, and it doubles the rate on both Gemini Flash tiers. Flash is not the cheapest option in the ledger, since Flash-Lite and DeepSeek both sit below it. But it is where a great deal of production traffic actually runs, and any cost model built on today's Flash economics is wrong on a known date.

Then ask your vendor something their pricing page does not answer: when do your compute contracts reprice?

You will probably not get a number. That is the finding. It tells you how much weight to put on any current price when you are choosing what to build on for the next three years.

Finally, separate the two questions you are actually asking. "Which model is best?" and "which vendor will still price this way in eighteen months?" have different answers, and only the second is a procurement decision.

If your workload is cache-heavy, our [cache pricing analysis](/posts/llm-cache-pricing-2026/) shows how far the effective rate drifts from the headline. Single-vendor lock-in is the risk this ledger is really measuring.

## Methodology

Prices come from each vendor's official pricing page, collected manually every Monday and recorded in `_data/pricing_history/`. This post covers five snapshots dated 2026-07-16, 2026-07-28, 2026-08-03, 2026-08-10 and 2026-08-17, spanning 32 days and 48 unique models across Anthropic, OpenAI, Google, xAI, DeepSeek and Mistral.

All figures are USD per 1M tokens on the standard non-batch tier. Tiered-price models are recorded at their base tier. A "price move" means the input or output figure differed from the immediately preceding snapshot. Percentages are computed from the first and last observed values in the window.

Data center vacancy, rental-rate, memory-price and electricity-price figures come from published commercial real estate market reports, memory market trackers and grid-market reporting for 2026. None of them are our measurements.

Financing figures come from company announcements and the outlets that reported them, each attributed with its date. Compute ownership and rental arrangements are drawn from public reporting, and where a figure is reported rather than announced by the parties, this post says "reportedly." Where a source publishes no number, this post says so rather than estimating one.

## Limitations

Five snapshots over 32 days is a short series, and the interval is uneven. Twelve days separate the first two collections. Treat the direction of these moves as observed and their frequency as provisional.

The series tracks the model set fixed on 2026-07-16 so week-over-week deltas stay comparable. Older, non-text and out-of-scope models on the same vendor pages are excluded, so this is not a census of every SKU a vendor sells.

The two DeepSeek increases are reported in the ledger but excluded from the analysis, and the exclusion is deliberate. The increase was pre-announced on DeepSeek's own pricing page, landed on a clean 1:3 output-to-input ratio still near the bottom of the industry distribution, and arrived alongside a new peak and off-peak schedule. Those are packaging and capacity signals, and DeepSeek sits outside the financing structure this post examines. Anyone arguing the increase is compute-cost pass-through needs evidence this series does not contain.

The cost chain here is assembled from separate sources that were never designed to be read together: memory contract pricing, colocation vacancy, grid capacity auctions and one company's earnings call. Each is credible on its own. The claim that they add up to CoreWeave's 25% is a reconstruction, and CoreWeave's own margin expansion shows the increase was not a pure pass-through of them.

Most importantly, this post connects datasets that are not causally linked by any evidence we hold. The price ledger is ours and is measured. Vacancy rates, financing and compute contracts are reported by others. The relationship drawn between them is an argument, not a measurement. The central claim of that argument, that capital rather than revenue is currently paying for low token prices, is an inference we cannot settle with a pricing table alone.

## Update cadence

The underlying price series is collected every Monday. This analysis is refreshed monthly, or sooner if a tracked vendor announces a price change above 25%. The weekly table itself lives in [LLM API Pricing 2026](/posts/llm-api-pricing-2026/) and is the place to look for current rates.

## Changelog

| Date | Change |
|---|---|
| 2026-08-21 | First publication. Covers snapshots 2026-07-16 through 2026-08-17. |

## FAQ

### Why are AI data center prices going up in 2026?

Three costs moved at once. PC DRAM contract prices rose 105–110% quarter over quarter in Q1 2026, the steepest single-quarter increase on record, and HBM capacity for 2026 is sold out. AI racks draw 10–20 kW against 3–5 kW for a standard rack, so power replaced floor space as the binding constraint. And PJM capacity prices rose 833% between the 2024–25 and 2025–26 delivery years. CoreWeave raised prices 25% in July, citing demand and component costs.

### Will rising data center costs push LLM API prices up?

It already pushed compute prices up, since CoreWeave raised its rates 25% in July 2026, and it stopped there. Over the same period the labs that rent compute most heavily cut their token prices or cancelled planned increases. The pass-through is real at the infrastructure layer and has not reached published token prices. Something is absorbing the difference.

### Do AI companies that own their data centers have a pricing advantage?

Less than the framing suggests, because the categories have collapsed. Google owns one of the world's largest TPU fleets and still reportedly agreed to rent roughly 110,000 GPUs from SpaceX. Anthropic rented essentially all of xAI's Colossus 1. Meta is preparing to sell its spare capacity. Owning does not insulate you when your marginal capacity is rented, and the margin is where price gets set.

### Why don't LLM API prices change more often?

Because the published price is not where the competition happens. Across 48 models we tracked between 2026-07-16 and 2026-08-17, 43 did not change at all in 32 days. Discounting runs through subscription plans, promotional tiers, free allowances and enterprise contracts, none of which appear on a pricing page.

### Is Google's Gemini Flash price cut permanent?

No, and Google says so on its own pricing page. Both gemini-3.6-flash and gemini-3.7-flash carry an introductory rate that expires 2026-12-31 and doubles to $1.50 input / $7.50 output on 2027-01-01. It is a published forward price, not a price cut, and it should be budgeted as one.

### Does OpenAI have bonds coming due?

No bonds have been reported. OpenAI was reported to carry no debt as of 2026-03-31, with under $750 million in lease obligations. What it holds is credit capacity, a revolving facility of roughly $4.7 billion plus a $520 million line, against roughly $600 billion in forward compute commitments. The borrowing sits with its counterparties instead.
