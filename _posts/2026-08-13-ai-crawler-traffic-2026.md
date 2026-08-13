---
title: "AI Crawler Traffic 2026: 747 Crawls per Human Visit"
description: "Twenty days of first-party Cloudflare logs: AI crawlers made 5,227 requests to this site and sent back 7 human visitors. Full dataset, method, and limits."
date: 2026-08-13 10:00:00 +0000
last_modified_at: 2026-08-13 10:00:00 +0000
categories: [ai-crawler-observatory]
tags: [ai-crawlers, bot-traffic, aeo, crawler-economics, cloudflare, llms-txt, "2026"]
format: F
cluster: CLUSTER_AEO
image:
  path: /assets/img/posts/ai-crawler-traffic-2026-cover.jpg
  alt: "A single pitted iron meteorite fragment tilted on rough dark stone, amber light on one face and cyan raking the other"
faq:
  - q: "How much traffic do AI crawlers actually send back to a website?"
    a: "On this site, almost none. Over 20 days AI crawlers made 5,227 requests and AI answer surfaces referred 7 human visitors — a ratio of 746.7 crawls per visit. Referrals are undercounted because some clients strip the Referer header, so treat 7 as a floor. The direction of the gap, however, is not a measurement artifact: it is three orders of magnitude."
  - q: "Does anything actually read llms.txt?"
    a: "Yes, but rarely. Our /llms.txt was fetched 46 times by 5 distinct agents in 20 days, against 4,561 requests for ordinary HTML pages. It is read, so it is not dead, but nothing in our logs supports treating it as a major distribution channel. The per-post JSON files were read far more often: 591 successful machine-endpoint reads in total."
  - q: "Can you tell if an AI crawler is faking its user agent?"
    a: "Partly. The user-agent string is self-reported and trivially forged. Cloudflare's verified-bot classification checks the connection rather than the string, and that is the only discriminator we trust. It has only been instrumented here since 2026-08-09. A separate and harder signal is behavioral: 459 requests, 8.8% of all traffic, asked for paths like .env and .git that no real crawler requests."
  - q: "Which AI crawler hits sites hardest in 2026?"
    a: "On this site, ByteDance's Bytespider — 1,815 requests, 34.7% of all crawls, present on every one of the 20 days. OpenAI's ChatGPT-User was second at 1,185. Note that Bytespider is a training and indexing crawler, while ChatGPT-User fetches a page to answer a question being asked right now, so the two numbers mean different things."
  - q: "Is a crawl the same thing as being cited by an AI?"
    a: "No, and conflating them is the most common mistake in this area. An indexing crawl means a page was collected. An answer-time fetch by ChatGPT-User, Claude-User, or Perplexity-User means a page was pulled while an answer was being written, which is the closest observable proxy for citation we have. We logged 1,041 such fetches across 14 posts."
data_updated: 2026-08-13
author: jsonhouse
---

Between 2026-07-25 and 2026-08-13, AI crawlers made **5,227 requests** to this site. Over the same 20 days, AI answer surfaces sent back **7 human visitors**. That is 746.7 crawls for every visit — a ratio most publishers can suspect but cannot prove, because the platforms that would know do not publish it and web analytics cannot see it.

This page is the first report from our own edge logs. Every number below was measured by a Cloudflare Worker sitting in front of this domain, not estimated, not sourced from a vendor. The raw aggregate is published as JSON alongside it, and the method and its limits are stated in full so the numbers can be argued with.

## TL;DR

- **746.7 : 1.** 5,227 AI crawler requests, 7 AI-referred human visits, 20 days, one site. Referrals are a floor, not an exact count.
- **Bytespider dominates.** ByteDance's crawler alone made 1,815 requests — 34.7% of all crawls, present every single day. OpenAI's ChatGPT-User was second at 1,185.
- **8.8% of all requests were not what they claimed.** 459 requests wearing crawler names asked for `.env`, `.git`, and credential paths. On 2026-08-01, thirteen different vendors' bot names arrived within a 30-millisecond window from what was plainly one source.
- **The machine-readable investment is consumed, modestly.** 591 successful reads of `/data/*.json`, `/api/posts.json`, and `/llms.txt`. The `llms.txt` file itself: 46 reads by 5 agents.
- **Crawling is not citation.** 1,041 answer-time fetches across 14 posts. One post, our weekly pricing table, took 503 of them and was fetched on all 20 days.

## The ledger

| Measure | Value |
|---|---|
| Collection window | 2026-07-25 to 2026-08-13 (20 days) |
| AI crawler requests (`bot_crawl`) | 5,227 |
| Human visits referred by AI answers (`ai_referral`) | 7 |
| Crawls per referred visit | 746.7 |
| Distinct agents observed | 19 |
| Distinct paths requested | 691 |
| Answer-time fetches (citation proxy) | 1,041 across 14 posts |
| Successful machine-endpoint reads | 591 |
| Requests matching credential-scanner patterns | 459 (8.8%) |

> **Raw data**: [data/ai-crawler-traffic-2026.json](https://www.jsonhouse.com/data/ai-crawler-traffic-2026.json) — machine-readable structured data for AI crawlers and citation.

The two referral rows are worth stating in full, because seven is a number you can print entirely. Six visits arrived from `chatgpt.com` to our [LLM API pricing table](/posts/llm-api-pricing-2026/). One arrived from `www.perplexity.ai` to an older post on E-E-A-T. That is the complete list of humans that AI answers sent us in 20 days.

## Methodology

A Cloudflare Worker runs in front of the GitHub Pages origin for this domain and records a row for three kinds of request: a user-agent matching a known AI crawler, a `Referer` header from an AI answer surface, and any request to `/data/`, `/api/`, or `/llms.txt` regardless of user agent. Ordinary human page views are not recorded at all, and raw client IP addresses are never stored.

Aggregation is a single read-only script against the log store, and its output is the JSON file linked above. Four short windows of our own verification traffic — the requests we made to prove the logger works, wearing real crawler names — are excluded by explicit timestamp range rather than by filtering on network origin, so it stays auditable which test produced which exclusion.

Two counting rules matter for reading the tables. Answer-time fetches count only successful requests for `/posts/` pages by ChatGPT-User, Claude-User, Perplexity-User, and DuckAssistBot. Machine-endpoint reads count only HTTP 200 responses, so a request for a JSON file that does not exist is not counted as consumption.

Referral rows describe real people, so only counts per referring host and per landing path leave the log. No country, no user agent, no timestamp.

## Which agents actually arrive

Nineteen distinct agents appeared. The error column is the share of requests that returned 4xx or 5xx, and it turns out to be the most informative column in the table.

| Agent | Requests | Distinct paths | Error rate | Days seen |
|---|---|---|---|---|
| Bytespider | 1,815 | 115 | 2.0% | 2026-07-25 to 08-13 |
| ChatGPT-User | 1,185 | 139 | 10.5% | 2026-07-25 to 08-13 |
| unknown-data-consumer | 552 | 49 | 5.6% | 2026-07-25 to 08-13 |
| ClaudeBot | 439 | 151 | 14.4% | 2026-07-25 to 08-09 |
| Amazonbot | 252 | 238 | 60.3% | 2026-07-25 to 08-13 |
| OAI-SearchBot | 227 | 76 | 18.9% | 2026-07-25 to 08-13 |
| Meta-ExternalAgent | 192 | 94 | 16.7% | 2026-07-26 to 08-10 |
| GPTBot | 171 | 132 | 33.3% | 2026-07-26 to 08-13 |
| PerplexityBot | 165 | 94 | 35.8% | 2026-07-26 to 08-13 |
| GoogleOther | 115 | 115 | 100% | 2026-08-08 only |
| Google-Extended | 38 | 37 | 100% | 2026-08-01 to 08-08 |
| Claude-User | 30 | 4 | 0% | 2026-07-26 to 08-11 |
| CCBot | 25 | 23 | 48.0% | 2026-08-01 to 08-09 |
| Cohere | 6 | 6 | 83.3% | 2026-08-01 only |
| Perplexity-User | 6 | 6 | 100% | 2026-08-01 only |
| anthropic-ai | 6 | 6 | 100% | 2026-08-01 only |
| DuckAssistBot | 3 | 2 | 0% | 2026-08-07 to 08-09 |

Read the top and bottom of that table together. Bytespider made 1,815 requests across only 115 paths with a 2.0% error rate — the signature of something that follows links and revisits them. GoogleOther made 115 requests across 115 paths and every single one failed.

One request per path, all failing, all on one day, is not crawling. It is guessing.

## Why the ratio is 747 to 1

The obvious reading of 746.7 : 1 is that AI is extracting value without returning any. That reading is right about the direction and wrong about the mechanism, and the mechanism is what tells you whether the number will move.

Crawling and referring are not two ends of one pipe. An indexing crawler collects pages on its own schedule whether or not anyone ever asks a question that touches them. Bytespider's 1,815 requests were not caused by 1,815 user questions; they were caused by a crawl budget. The denominator of this ratio is set by vendor infrastructure decisions, not by reader demand.

The numerator is set by something else entirely: whether an answer engine both used our page *and* rendered a link a human then chose to click. Three conditional steps, each of which loses most of the population.

This is why the ratio is a poor measure of extraction and a good measure of substitution. A search engine that sends no traffic has, in the older model, failed. An answer engine that sends no traffic has succeeded — it answered the question, which is the product. The 7 visits are not the payoff for the 5,227 crawls. They are the residue of the cases where the answer was insufficient.

The intermediate signal is the one worth tracking. Answer-time fetches — pages pulled by ChatGPT-User, Claude-User, and Perplexity-User while an answer was being composed — ran to 1,041 across 14 posts. That is 149 answer-time fetches for every referred visit. Our pricing table alone accounted for 503 of them and was fetched on all 20 days without a break.

So the page was used roughly 500 times and clicked six times. Both numbers are real, and only one of them appears in any conventional analytics tool. That gap is the entire argument for measuring at the edge — and it is the supply-side counterpart to the demand-side picture in our look at [where AI answer engines source their citations](/posts/chatgpt-ads-2026-aeo-reddit-citations/), where the traffic that does arrive converts far better than organic.

## Nearly one request in eleven is forged

The user-agent string is self-reported. Anyone can send `GPTBot` in a header, and our logger, like every log-based measurement, records what it is told.

Two independent methods put a floor under how much of this traffic is fake.

The first is behavioral. 459 requests — 8.8% of everything logged — asked for paths like `.env`, `.git`, `service_account`, and `credentials`. No documented AI crawler requests those. Every such request arrived wearing a real crawler's name, and the names most used were not the ones you would guess: Amazonbot (94), ChatGPT-User (83), GoogleOther (57), and ClaudeBot and GPTBot at 42 each.

This is deliberately a floor rather than an estimate. A forger who requests an ordinary post URL leaves a row that is byte-for-byte identical to a genuine crawler's, and no pattern can separate them.

The second is temporal. On 2026-08-01, between 11:25:09.531 and 11:25:09.561 UTC, thirteen different agent names made their first appearance in that burst: GPTBot, Bytespider, ClaudeBot, Meta-ExternalAgent, OAI-SearchBot, anthropic-ai, Cohere, Google-Extended, ChatGPT-User, PerplexityBot, Perplexity-User, CCBot, and an unidentified data consumer.

Thirty milliseconds. Thirteen vendors. OpenAI, Anthropic, ByteDance, Meta, Google, Perplexity, Cohere, and Common Crawl do not coordinate their crawl schedules to the millisecond. This was one source cycling a user-agent list, and it explains why several agents in the table appear on 2026-08-01 and never again.

The practical consequence is that any published statistic about AI crawler market share, including the table above, is contaminated by an unknown amount of impersonation unless it states how it separated the two. Most do not state it, which is a reason to distrust the confident ones.

## What actually separates a real crawler from a forger

Not the user agent, and not the network the request came from. An ASN check fails on this specific problem because vendor agents legitimately egress from general-purpose clouds — OpenAI's agents arrive from Microsoft ASNs, and so does any VM someone rents.

The signal we trust is [Cloudflare's verified-bot classification](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/), which validates the connection rather than the string. We only began recording it on 2026-08-09, so the window below is four days, not twenty.

| Agent | Verified as | Verified | Unverified |
|---|---|---|---|
| Bytespider | Search Engine Crawler | 299 | 56 |
| ChatGPT-User | AI Assistant | 215 | 1 |
| GPTBot | AI Crawler | 55 | 0 |
| OAI-SearchBot | Search Engine Crawler | 35 | 0 |
| PerplexityBot | — | 0 | 30 |
| Amazonbot | AI Crawler | 19 | 0 |
| unknown-data-consumer | mixed | 15 | 60 |

Bytespider splits: 299 verified against 56 that were not. Those 56 requests carried ByteDance's name over a connection Cloudflare would not confirm as ByteDance.

PerplexityBot's row needs care. Zero of its 30 requests verified — but "unverified" means Cloudflare did not confirm the connection, which is not the same as proving forgery, and a vendor absent from the verified list would produce exactly this row. We are reporting what the field says, not what it implies. Four days and 30 requests is too little to conclude anything, and this is precisely the row to watch next month.

The public crawler documentation from [OpenAI](https://platform.openai.com/docs/bots) and [Anthropic](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) both publish IP ranges for exactly this reason. If you are making decisions from crawler logs, the user-agent column alone is not evidence.

## Does anything read llms.txt

This site publishes an [llms.txt](https://llmstxt.org/) file, per-post JSON at `/data/{slug}.json`, and an index at `/api/posts.json`. Whether any of it is consumed is the question the whole investment rests on, and until we had edge logs we could not answer it.

| Endpoint | Successful reads | Distinct agents |
|---|---|---|
| `/data/` index page | 47 | 4 |
| `/llms.txt` | 46 | 5 |
| `/data/index.json` | 41 | 4 |
| `/api/posts.json` | 33 | 2 |
| Individual `/data/{slug}.json` files | 424 | up to 4 each |
| **Total machine-endpoint reads** | **591** | — |

The honest summary is: read, but not much. 591 machine reads against 4,561 requests for ordinary HTML pages means roughly one machine-endpoint read for every eight page fetches. `llms.txt` specifically was fetched 46 times by 5 agents over 20 days.

That is enough to say the file is not dead and not enough to call it a distribution channel. Anyone telling you that publishing `llms.txt` is how AI systems will find your content is, on this evidence, overselling it — and we would have had no basis to say so without our own logs.

The per-post JSON files did better than the summary endpoints, which is the mildly surprising result. Individual dataset files drew 424 reads spread across nearly every published post, suggesting agents that already know a URL and fetch its structured form, rather than agents discovering the site through an index. That pattern also matches what we described in our earlier survey of the [AI crawler ecosystem](/posts/ai-crawler-ecosystem-2026/).

## Limitations

This is one small site over 20 days. It is not a sample of the web, and nothing here should be read as a global rate. What it is: a complete, unfiltered census of one origin, which is a different and rarer thing than a survey.

Referrals are undercounted. Clients strip `Referer`, some apps open links without one, and privacy settings suppress it. Seven is a floor. The crawl side has no equivalent undercount, so the true ratio is lower than 746.7 : 1 by an unknown factor — though it would take a 100x referral undercount to move the conclusion.

Answer-time fetches are a proxy for citation, not a measure of it. A fetch by ChatGPT-User means a page was retrieved while an answer was being written. It does not prove the page was used in the answer, and it certainly does not prove the answer named us.

Network identity — ASN, verified-bot status, byte counts — begins on 2026-08-09. Rows before that date carry nothing in those columns, and we have left them empty rather than filling them with plausible guesses. Any statement in this report about verification covers four days.

Finally, the 8.8% forgery figure is a floor derived from one pattern. The real share is higher by an amount we cannot measure with these fields.

## Update cadence

This dataset is regenerated and republished **monthly**, on the same aggregation script, with the window extending as the log accumulates. The next update covers through 2026-09-13. Each update adds a Changelog line below rather than silently overwriting, so the revision history is itself part of the record.

We are committing to monthly and not weekly because the interesting movements here — a vendor appearing, a verification rate shifting — are monthly-scale events, and because a cadence we can keep is worth more than one we announce.

## FAQ

### How much traffic do AI crawlers actually send back to a website?

On this site, almost none. Over 20 days AI crawlers made 5,227 requests and AI answer surfaces referred 7 human visitors — 746.7 crawls per visit. Referrals are undercounted because some clients strip the `Referer` header, so treat 7 as a floor. The direction of the gap is not a measurement artifact: it is three orders of magnitude.

### Does anything actually read llms.txt?

Yes, but rarely. Our `/llms.txt` was fetched 46 times by 5 distinct agents in 20 days, against 4,561 requests for ordinary HTML pages. It is read, so it is not dead, but nothing in our logs supports treating it as a major distribution channel. The per-post JSON files were read far more often, at 591 machine-endpoint reads in total.

### Can you tell if an AI crawler is faking its user agent?

Partly. The user-agent string is self-reported and trivially forged. Cloudflare's verified-bot classification checks the connection rather than the string, and that is the only discriminator we trust — instrumented here only since 2026-08-09. A separate and harder signal is behavioral: 459 requests, 8.8% of all traffic, asked for paths like `.env` and `.git` that no real crawler requests.

### Which AI crawler hits sites hardest in 2026?

On this site, ByteDance's Bytespider — 1,815 requests, 34.7% of all crawls, present on every one of the 20 days. OpenAI's ChatGPT-User was second at 1,185. The two numbers mean different things: Bytespider is a training and indexing crawler, while ChatGPT-User fetches a page to answer a question being asked at that moment.

### Is a crawl the same thing as being cited by an AI?

No, and conflating them is the most common mistake in this area. An indexing crawl means a page was collected. An answer-time fetch by ChatGPT-User, Claude-User, or Perplexity-User means a page was pulled while an answer was being written, which is the closest observable proxy for citation we have. We logged 1,041 such fetches across 14 posts.

## Changelog

| Date | Change |
|---|---|
| 2026-08-13 | Initial publication. Window 2026-07-25 to 2026-08-13, 5,234 logged hits. |
