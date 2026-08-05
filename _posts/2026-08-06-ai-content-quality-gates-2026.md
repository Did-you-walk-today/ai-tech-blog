---
title: "AI Content Quality Gates 2026: 33 Rules That Caught Us"
description: "A 33-rule automated gate for AI-written content, the three shapes a lost citation takes, and the one check that finds all three in your rendered HTML."
date: 2026-08-06 04:00:00 +0900
last_modified_at: 2026-08-06 04:00:00 +0900
categories: [ai-productivity-workflows]
tags: [ai-content, content-ops, quality-gates, validation, geo, editorial-workflow, "2026"]
format: E
cluster: CLUSTER_DEVTOOLS
category_id: CAT4
image:
  path: /assets/img/posts/ai-content-quality-gates-2026-cover.jpg
  alt: "A single sheet of oxidized copper on dark stone, one lifted corner catching a cyan edge of light against warm patina"
faq:
  - q: "What should an AI content quality checklist actually check?"
    a: "Four layers, in this order: front matter and SEO fields, prose quality, images, and citation evidence. The first three are what most teams build. The fourth decides whether a generative engine can attribute you, and it is the one almost nobody automates — which is why it can fail silently for months without anyone noticing."
  - q: "Do bare domain names in prose count as citations?"
    a: "Not to a parser. Google's documentation states it can only crawl a link that is an anchor element with an href attribute, so 'Anthropic (platform.claude.com)' written as text is a citation to a human reader and plain prose to everything else. It is the most deceptive of the three failure shapes, because the page looks scrupulous to an editor."
  - q: "How do I check whether my own posts are citable?"
    a: "Count the outbound anchor links in your rendered HTML — not in your CMS, not in your metadata, and not in any JSON sidecar you publish alongside the page. If a well-researched post returns zero, its sources are invisible to the engines deciding whom to attribute, and that has probably been true for as long as the habit has existed."
  - q: "Can automated gates replace human review of AI writing?"
    a: "No, and ours does not try. Every rule here is a shape check — length, presence, count, structure. The two most damaging errors we shipped this year were a vendor renamed two months earlier and a claim that a vendor documented no quotas when it did. Both passed all 33 rules and were caught by a person re-reading the sources."
  - q: "How many rules is the right number?"
    a: "Fewer than you think, and each one must be enforced by something that runs without being remembered. We run 33. The count matters less than the property that every rule is executable: a rule that lives only in a style guide is a norm, and norms do not fail builds."
data_updated: 2026-08-05
author: jsonhouse
---

Automated quality gates for AI-written content are usually pitched as a way to catch bad prose. That is the least valuable thing they do. The failures worth catching are the ones an editor cannot see: a field that is present but wrong, a link that reads as a citation but is not one, a claim that is well sourced in a file nobody serves. This post publishes the 33-rule gate we run before a human reads a draft, the three shapes a lost citation takes, and the single check that detects all three. It ends with what happened when we ran that check against our own archive, which is the reason we think the gap is worth naming.

## TL;DR

- **33 rules in four layers**: 9 front matter and SEO, 8 prose quality, 11 image, 5 citation evidence. All executable, all run on save.
- **The citation layer is the one teams skip**, and it is the only one that decides whether a generative engine can attribute you at all.
- **A lost citation takes three shapes**: a bare domain in prose, a source migrated into a data file, and a table column holding source names as plain text. All three look correct to an editor.
- **One check finds all three**: count outbound anchor links in the rendered HTML. Not the CMS, not the metadata, not the JSON sidecar.
- **We failed our own check on 9 of 15 posts.** One blog is not evidence of a trend — it is evidence that a team actively optimising for machine readability can ship nine consecutive posts with zero crawlable sources.

## The four layers

Each layer runs as a hook on write, on any file in `_posts/` or `_drafts/`. Layers C and D are downgraded to warnings for drafts, because artwork and datasets legitimately arrive after a first draft — a gate that fires too early just teaches you to ignore it.

| Layer | What it checks | Rules | Fails the build on |
|---|---|---|---|
| A — Front matter & SEO | Title length, year, description range, comparison table present, word count, freshness field, FAQ, TL;DR, internal links | A1–A9 | Title over 60 chars, description outside 140–165, under 600 words, missing freshness date |
| B — Prose quality | Forbidden JSON blocks, code block framing, headings, checklist coverage, thin sections, paragraph length | B1–B8 | A code block with no introduction or no follow-through, a paragraph over 120 words |
| C — Images | Cover presence, alt text, exact dimensions, weight, filename, per-format figure budget, evidence table | C1–C11 | Missing cover, wrong dimensions, a cover that is a code render rather than art |
| D — Citation evidence | Inline outbound citation, source depth, fact granularity, dataset link, dataset schema | D1–D5 | Zero outbound links in the body, fewer than 3 primary sources, missing or mismatched dataset |

> **Raw data**: [data/ai-content-quality-gates-2026.json](https://www.jsonhouse.com/data/ai-content-quality-gates-2026.json) — machine-readable structured data for AI crawlers and citation.

Layers A through C encode things an editor would eventually catch anyway, just earlier and more consistently. They are worth automating and they are not interesting.

Layer D is the one worth arguing about. It asks whether the post links to the sources it rests on, in the body, where a crawler will find them. Nothing in the other three layers knows that a citation has a location requirement at all — which is precisely how a site can pass every quality check it runs while becoming progressively harder to attribute.

## Three shapes a lost citation takes

A missing citation is easy to spot. A citation that exists but does not function is not, and it comes in three recognisable forms. None of them is a writing failure, and all three survive editorial review.

**The bare domain.** The source is named as text in parentheses — "Anthropic (platform.claude.com)" — sometimes in backticks, which makes it look more deliberate rather than less. To a reader this is a proper attribution. Google's documentation is explicit that it can only crawl a link that is [an anchor element with an href attribute](https://developers.google.com/search/docs/crawling-indexing/links-crawlable); a domain typed into a sentence is not one. This is the most deceptive shape because the page reads as scrupulous.

**The migrated source.** The URLs live in a structured sidecar — a JSON dataset, a CMS field, a references table — and the body names only the organisation: "collected from each vendor's official pricing page (Anthropic, Cursor, GitHub)". Accurate, verifiable by hand, and inert to anything parsing the page.

**The plain-text table column.** A comparison table lists studies, vendors, or standards in its first column as text. That table is usually the most citation-worthy object on the page, and it points nowhere.

## The check that finds all three

Count the outbound anchor links in your rendered HTML, per post, excluding your own domain. That single number catches every shape above, because all three produce the same result: a well-researched page that resolves to zero.

The important word is *rendered*. Not the count in your CMS, not the length of a references array, not the sources in a sidecar file you publish alongside the page. The HTML you actually serve is what a generative engine parses, and it is the only surface where the answer counts.

Run it against your archive, not just against new drafts. A gate that checks only what you write next tells you nothing about what you have already published, and the back catalogue is most of what a crawler sees.

## What that check found here

We added Layer D on 2026-08-05 and ran it retroactively over everything already published. This is a single organisation's archive — one pipeline, one schema, one set of habits — so treat it as a worked example, not as a measurement of the field.

| Era | Posts | Outbound links in body | Sources in the dataset | Layer D |
|---|---|---|---|---|
| 2026-04-27 → 2026-05-07 | 6 | 1–15 (median 6.5) | 3–4 | All pass |
| 2026-05-17 → 2026-08-05 | 9 | **0 in every post** | 4–11 | All fail |

Nine of fifteen failed, and the transition happens between two consecutive posts rather than gradually. The most heavily sourced post in the archive — eleven verified sources, each with a title and a URL in its dataset — was one of the failures.

Our account of why is simple, and it is testimony rather than data: as the dataset schema matured, recording a source there became the natural place to put it, and linking in prose stopped feeling necessary. Somewhere better for us. A generative engine reads the rendered HTML of the page it is summarising; it does not open a sidecar at a different path on the chance one exists.

We cannot tell you that this generalises. Fifteen posts from one blog written under one set of conventions is closer to a single observation than to a sample, and we have no way to distinguish a structural pattern from one team's habit from the inside. What the case does establish is narrower and still worth stating: **a team actively optimising for machine readability shipped nine consecutive posts with zero crawlable sources, and every internal quality signal it tracked went up over the same period.** If it can happen to a pipeline that validates its own datasets on every write, the check is cheap enough to run on yours.

## A rule you cannot execute is not a rule

Our guidelines had said "cite primary sources" from the beginning. Nine consecutive posts violated it. The instruction was not ignored — it was satisfied, in the writer's understanding, by filling in a sources array.

That gap between a norm and its enforcement is where content quality leaks. Norms get interpreted, and interpretation drifts toward whatever is easiest to satisfy. An executable rule cannot be reinterpreted; it either passes or it does not.

The rule we wrote needed two corrections on its first day before it judged correctly — one that let bad content through, two that flagged good content. That is the real cost of this approach and it is worth stating plainly. **Writing the rule is not the work. Making the rule agree with what you meant is the work.** A gate that errs toward strictness is worse than no gate, because it teaches everyone to override it.

## What gates do not buy you

Every rule here is a shape check: a length, a presence, a count, a structural relationship. That covers a specific and limited class of error.

It does not cover truth. The two most damaging mistakes we published this year both passed all 33 rules. One described a vendor under a name it had abandoned two months earlier. The other stated flatly that a vendor documented no usage quotas, when [the documentation existed on a domain we had not checked](/posts/china-ai-coding-plans-2026/). Both were caught by a person re-reading the primary sources before publication.

Nor can we tell you that restoring citations produces citations. Fixing the nine posts took an afternoon; establishing whether generative engines attribute us more often because of it needs crawl and referral data we are still accumulating. We have written about [how citation and ranking have split into different games](/posts/ai-overviews-seo-2026/) and [how much crawlers take relative to what they send back](/posts/ai-crawler-ecosystem-2026/) — neither of those makes a causal claim available to us here. Anyone reporting a measured lift from a change made this week is showing you a hope.

## Running this yourself

The layer structure transfers even though our individual rules will not. Three properties are what make it work.

**Put every rule where it executes.** Ours run as editor hooks on file save, so feedback arrives while the draft is open rather than at review time. A pre-commit hook or a CI step on pull requests works equally well.

**Separate errors from warnings, and vary severity by stage.** A draft without a cover image is normal; a published post without one is broken. Same rule, different severity by directory. Without that split, people learn to ignore the entire output.

**Start with the citation count.** If you adopt one thing from this post, make it the outbound-anchor count on your rendered HTML, run across your archive. It is the cheapest check here and the only one that tells you something you cannot see by reading your own pages.

## Limitations

The measurement in this post covers one blog and fifteen posts. Those posts are not independent observations — they share an author, a template, and a schema — so the effective sample is closer to one than to fifteen. It is an existence proof, not a correlation, and it should not be cited as evidence that structured-data practices reduce inline citation generally.

The rules are tuned to a specific format: long-form technical posts that each ship with a dataset. A newsroom, a documentation site, or a marketing blog would keep the layer structure and replace nearly every individual rule.

Our thresholds are conventions rather than findings. The 120-word paragraph ceiling comes from this blog's own median of 53 words, not from research on reading behaviour. Treat the specific numbers as ours and the layering as the transferable part.

## FAQ

### What should an AI content quality checklist actually check?

Four layers, in this order: front matter and SEO fields, prose quality, images, and citation evidence. The first three are what most teams build. The fourth decides whether a generative engine can attribute you, and it is the one almost nobody automates — which is why it can fail silently for months without anyone noticing.

### Do bare domain names in prose count as citations?

Not to a parser. Google's documentation states it can only crawl a link that is an anchor element with an href attribute, so "Anthropic (platform.claude.com)" written as text is a citation to a human reader and plain prose to everything else. It is the most deceptive of the three failure shapes, because the page looks scrupulous to an editor.

### How do I check whether my own posts are citable?

Count the outbound anchor links in your rendered HTML — not in your CMS, not in your metadata, and not in any JSON sidecar you publish alongside the page. If a well-researched post returns zero, its sources are invisible to the engines deciding whom to attribute, and that has probably been true for as long as the habit has existed.

### Can automated gates replace human review of AI writing?

No, and ours does not try. Every rule here is a shape check — length, presence, count, structure. The two most damaging errors we shipped this year were a vendor renamed two months earlier and a claim that a vendor documented no quotas when it did. Both passed all 33 rules and were caught by a person re-reading the sources.

### How many rules is the right number?

Fewer than you think, and each one must be enforced by something that runs without being remembered. We run 33. The count matters less than the property that every rule is executable: a rule that lives only in a style guide is a norm, and norms do not fail builds.

## Update cadence

The rule set changes as the pipeline does. We re-publish the layer table and the rule count whenever a layer is added or a severity changes, and log it below. The archive measurement is a point-in-time observation dated 2026-08-05 and will not be silently updated — a later re-run is a new row, not an edit.

## Changelog

- **2026-08-05** — First publication. Rule count 33 across four layers. Layer D added the same day and run retroactively against 15 published posts; 9 failed and were subsequently fixed.
