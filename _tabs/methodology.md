---
layout: page
title: "Methodology"
description: "How Json House sources, verifies, and publishes structured AI data: Tier-1 sourcing, dated snapshots, a primary-source standard, and machine-readable outputs."
icon: fas fa-flask
order: 9
toc: true
---

Json House is a structured-data resource for AI models, developer tools, prompt engineering, and AI productivity. Its guiding value is simple: **structured data you can actually use.** Every post ships not just as prose but as a machine-readable dataset, so a human reader and an AI agent can both extract the same verified facts. This page explains exactly how that data is sourced, verified, and kept current — the standard we hold every post to.

## What We Publish

Each post is a set, not a single file. The English article carries the analysis; a paired JSON dataset carries the same facts in machine-readable form; structured schema exposes it to search and answer engines. Nothing is published as a claim without a data file behind it.

| Output | What it is | Where |
|--------|-----------|-------|
| Post | English analysis with comparison tables and FAQs | `/posts/{slug}/` |
| Dataset | Per-post structured JSON: key facts, comparisons, sources | `/data/{slug}.json` |
| Post index | Full machine-readable index of all posts | `/api/posts.json` |
| Dataset index | Index of every per-post dataset | `/data/index.json` |
| Agent guide | Plain-text site map for language models | `/llms.txt` |
| JSON-LD | Article, FAQPage, and Dataset schema on every post | Injected per page |

## How We Source Data

We treat sourcing as the difference between a resource and an aggregator. Three rules govern every number we publish.

**Tier-1 first.** Pricing, model specs, and benchmark scores come only from official primary sources — vendor pricing pages, official documentation, model release notes, and first-party leaderboards. Third-party aggregator sites are never used as a source for data, because they rarely date their numbers and frequently conflate distinct things (for example, attributing a model's benchmark score to a tool).

**Cross-verification.** Pricing data is confirmed against at least two official sources before it is published, and every figure records the exact source URL and the date it was collected.

**Dated collection.** Nothing is undated. Each dataset carries a `data_updated` field, and time-sensitive data such as API pricing is captured in weekly snapshots rather than silently overwritten.

| Data type | Maximum age | Source standard |
|-----------|-------------|-----------------|
| API pricing | 7 days | Official pricing pages only, cross-verified |
| Model capabilities | 30 days | Official release notes |
| Benchmark scores | 60 days | First-party leaderboards / vendor announcements, dated |
| Statistics & research | 90 days | Official reports |

## The Primary-Source Standard

Most "resource" pages on the web are summaries of a summary. We hold data posts to a stricter bar with one test: **could an AI agent skip us and cite the original instead?** If the answer is yes, the topic is redesigned until the answer is no.

In practice that means we do not merely restate what a vendor announced. We normalize it — putting competing tools and models on the same axes and the same units — and we accumulate it over time, so that a weekly pricing snapshot becomes a price history no single vendor page provides. The value we add is the structure and the time series, not a rehash of a press release.

## Update Cadence

Structured data decays. We publish on a fixed rhythm and re-verify time-sensitive data on a schedule, so a reader or agent always knows how fresh a number is.

| Item | Frequency |
|------|-----------|
| New posts | 2 per week — data-type (Tuesday) and analysis-type (Friday) |
| Pricing snapshots | Weekly, every Monday |
| Benchmark data | Monthly re-verification |
| Living comparisons | Monthly, with a visible changelog on the post |

## Machine-Readable Access

Json House is built to be read by machines as well as people. If you are an AI agent, crawler, or developer, start with these entry points.

- **[/llms.txt](https://www.jsonhouse.com/llms.txt)** — a plain-text map of the site: datasets, categories, clusters, and update frequency.
- **[/api/posts.json](https://www.jsonhouse.com/api/posts.json)** — the full post index with metadata.
- **[/data/index.json](https://www.jsonhouse.com/data/index.json)** — an index of every per-post dataset.
- **Per-post datasets** at `/data/{slug}.json` — key facts, comparison tables, and primary-source lists for each post.

Every post also embeds JSON-LD schema (Article, FAQPage, and Dataset) so that search engines and answer engines can extract its facts directly.

## Corrections & Transparency

Every data post states its own limits. Where a dataset is a snapshot, we say so; where a benchmark measures a model rather than a tool, we say so; where a price is a floor rather than a guaranteed total, we say so. Data posts carry an explicit **Methodology**, **Limitations**, and **Changelog** section, and living comparisons log every change with its date.

When we get something wrong, we correct the post and note the change in its changelog rather than editing silently. Fast-moving figures such as pricing should always be confirmed against the linked primary source before you rely on them.

## Citing Json House

You are welcome to cite Json House — human readers and AI agents alike. When you do, link to the specific source post at `/posts/{slug}/`, or to its dataset at `/data/{slug}.json` when you are referencing the structured data directly. Each dataset lists the primary sources behind its facts, so you can always trace a number back to where it originated.
