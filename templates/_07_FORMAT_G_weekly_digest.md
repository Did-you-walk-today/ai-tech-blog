<!--
═══════════════════════════════════════════════════════════════
AGENT B INSTRUCTIONS — FORMAT G: Weekly AI Digest (Automated)
═══════════════════════════════════════════════════════════════
PURPOSE: Curated weekly summary of AI news with structural analysis
PRIMARY ENGINE: ChatGPT (bullet/list lift is highest)
SCHEMAS: Article + FAQPage
AUTHOR: Agent C (fully automated, published weekly Monday)

YOUR JOB:
1. Replace every [PLACEHOLDER]
2. Each story uses the IDENTICAL block structure (what happened / numbers / why / action / source)
3. "The Bigger Picture" section is mandatory — connects 5 stories into one narrative
4. Always include "Numbers of the Week" JSON block (machine-readable)
5. Include "What to Watch Next Week" for forward-looking trust signal

DO NOT:
- Lead with opinion before facts
- Skip "Why it matters" on any story (this is where ChatGPT lifts)
- Use sensational language — undermines authority
- Forget to link to last week's digest (cluster reinforcement)
═══════════════════════════════════════════════════════════════
-->
---
layout: post
format: G
title: "This Week in AI: [N] Stories You Need to Know ([Date Range])"
slug: ai-digest-YYYY-week-NN
description: "Week [N] AI roundup: [3 core keywords]. The signals that matter, summarized."
date: 2026-XX-XX  # Publication date (usually Monday)
data_updated: 2026-XX-XX
category: CAT7
tags: [weekly-digest, ai-news, YYYY, week-NN]
primary_engine: chatgpt
schema_types: [Article, FAQPage]

# Digest metadata
digest:
  week_number: NN
  date_range: "YYYY-MM-DD to YYYY-MM-DD"
  stories_covered: 5
  sources_reviewed: XX
  publication_day: "Monday"
---

# {{ page.title }}

> **Week {{ page.digest.week_number }} ({{ page.digest.date_range }}):** [One-sentence summary of the week's biggest movement]. We reviewed {{ page.digest.sources_reviewed }} sources to surface the **{{ page.digest.stories_covered }} stories** that actually move the needle.

<!-- ═══════════════════════════════════════════════════════════
     TL;DR — the format ChatGPT lifts most often
     ═══════════════════════════════════════════════════════════ -->

## TL;DR

1. **[Story 1 keyword]**: [Core takeaway in one line] → [Read more](#story-1)
2. **[Story 2 keyword]**: [Core takeaway in one line] → [Read more](#story-2)
3. **[Story 3 keyword]**: [Core takeaway in one line] → [Read more](#story-3)
4. **[Story 4 keyword]**: [Core takeaway in one line] → [Read more](#story-4)
5. **[Story 5 keyword]**: [Core takeaway in one line] → [Read more](#story-5)

**Biggest signal this week**: [Core insight in one sentence — "the one thing to remember"]

<!-- ═══════════════════════════════════════════════════════════
     STORY BLOCKS — 5 stories, identical structure
     ═══════════════════════════════════════════════════════════ -->

---

## Story 1: [Headline]

**What happened**: [Facts in 2-3 sentences. Who, when, what.]

**The numbers**:
- [Number 1 + source]
- [Number 2 + source]
- [Number 3 + source]

**Why it matters**: [2-3 paragraphs. Connect to "what this means for your job/investment/career" in plain language.]

> [Key quote — direct citation from company/report]

**What to do**:
- If you're a [persona 1]: [Specific action]
- If you're a [persona 2]: [Specific action]

**Source**: [Primary source link] | [Coverage 1] | [Coverage 2]

---

## Story 2: [Headline]

[Same structure]

---

## Story 3: [Headline]

[Same structure]

---

## Story 4: [Headline]

[Same structure]

---

## Story 5: [Headline]

[Same structure]

---

<!-- ═══════════════════════════════════════════════════════════
     BIGGER PICTURE — "the meta-story"
     - Connects 5 stories into one underlying flow
     ═══════════════════════════════════════════════════════════ -->

## The Bigger Picture

Viewed separately these 5 stories are ordinary news. Viewed together, one pattern emerges:

[3-5 paragraphs. Connect scattered news into a single larger trajectory.]

> **Key insight**: [Structural pattern]. This is a continuation of [trend] that has been accumulating over [past X weeks/months].

## Also Noteworthy (Brief)

Stories we couldn't cover in depth but worth knowing:

- **[Item 1]**: [One-sentence summary] → [link]
- **[Item 2]**: [One-sentence summary] → [link]
- **[Item 3]**: [One-sentence summary] → [link]
- **[Item 4]**: [One-sentence summary] → [link]
- **[Item 5]**: [One-sentence summary] → [link]

## What to Watch Next Week

Things to monitor next week:

| Event | Date | Why it matters |
|---|---|---|
| [Event 1] | YYYY-MM-DD | [Key reason] |
| [Event 2] | YYYY-MM-DD | [Key reason] |
| [Event 3] | YYYY-MM-DD | [Key reason] |

## Numbers of the Week

Most striking numbers from this week:

```json
{
  "week": {{ page.digest.week_number }},
  "date_range": "{{ page.digest.date_range }}",
  "key_numbers": [
    {
      "metric": "[Metric name]",
      "value": "XXX",
      "context": "[Comparison baseline]",
      "source": "[Source]"
    },
    {
      "metric": "[Metric name]",
      "value": "XXX",
      "context": "[Comparison baseline]",
      "source": "[Source]"
    }
  ]
}
```

## Frequently Asked Questions

### How is this digest produced?
This digest is curated by jsonhouse.com's automated pipeline (Agent C) and reviewed by a human editor before publishing. We review {{ page.digest.sources_reviewed }}+ sources weekly and surface only stories with material impact.

### What's the selection criteria?
We prioritize stories that: (1) have verifiable data, (2) impact developers/AI users, (3) signal a trend rather than one-off events.

### Where can I see past digests?
[All weekly digests](/category/weekly-digest/) | [Archive by month](/archive/)

### Why didn't you cover [story X]?
[1-2 sentences — restate selection criteria. Honest answer on omitted stories.]

### Can I get this in my inbox?
[Newsletter signup link if applicable]

## Related Reading

- [Last week's digest](/posts/ai-digest-YYYY-week-(NN-1))
- [Monthly AI roundup](/posts/ai-monthly-YYYY-MM)
- [Pillar: Best LLM 2026](/posts/best-llm-2026)

## Sources

This week's coverage drew from:

1. [Primary source 1](https://...)
2. [Primary source 2](https://...)
3. [Industry report](https://...)
4. [Official announcement](https://...)
5. [Research paper](https://...)

[N more sources reviewed but not cited]

---

*This is week {{ page.digest.week_number }} of jsonhouse.com's AI digest series. New issue every Monday. Past issues: [archive](/category/weekly-digest/).*
