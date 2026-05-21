<!--
═══════════════════════════════════════════════════════════════
AGENT B INSTRUCTIONS — FORMAT D: Structured Data Resource
═══════════════════════════════════════════════════════════════
PURPOSE: Continuously-updated database posts (pricing, specs, etc.)
PRIMARY ENGINE: Perplexity (favors fact-dense + primary data)
SCHEMAS: Article + Dataset (Google Dataset Search target) + FAQPage

YOUR JOB:
1. Replace every [PLACEHOLDER]
2. The Methodology section is MANDATORY — it determines Perplexity trust
3. Always expose the dataset as both human table AND raw JSON
4. Include a Changelog (last 3 updates minimum)
5. Mention update_frequency in multiple places (data_updated, FAQ, footer)

DO NOT:
- Skip the Methodology box
- Hide what you excluded (exclusion criteria is a trust signal)
- Omit raw JSON sample (this is what agents call)
═══════════════════════════════════════════════════════════════
-->
---
layout: post
format: D
title: "[Topic] Database 2026: Complete Comparison (Updated [Frequency])"
slug: topic-database-2026
description: "Comprehensive [topic] data for 2026. [N] entries, updated [frequency]. Raw JSON available."
date: 2026-XX-XX
data_updated: 2026-XX-XX  # Auto-refreshed by Phase 7
update_frequency: "weekly"  # daily | weekly | monthly
category: CAT5
tags: [data, database, comparison, 2026]
primary_engine: perplexity
schema_types: [Article, Dataset, FAQPage]

# Dataset schema auto-generation (targets Google Dataset Search)
dataset:
  name: "[Topic] Database 2026"
  description: "[150-200 char description for Dataset schema]"
  license: "https://creativecommons.org/licenses/by/4.0/"
  creator: "jsonhouse.com"
  distribution_url: "https://jsonhouse.com/api/[topic].json"
  variable_measured:
    - "[Measured variable 1]"
    - "[Measured variable 2]"
    - "[Measured variable 3]"
  spatial_coverage: "Global"
  temporal_coverage: "2026"
  entry_count: XX
---

# {{ page.title }}

> **What this is:** The most current [topic] database for 2026, with **{{ page.dataset.entry_count }} entries** verified as of **{{ page.data_updated }}**. Updated **{{ page.update_frequency }}**. Raw JSON for agents/scripts: [`/api/[topic].json`]({{ page.dataset.distribution_url }}).

[1-2 paragraphs. Why this database exists, how data is collected/verified, what makes it different.]

## TL;DR

1. **Total entries**: {{ page.dataset.entry_count }}
2. **Last updated**: {{ page.data_updated }}
3. **Update frequency**: {{ page.update_frequency }}
4. **Cheapest in category**: [entry name] — $X
5. **Best value**: [entry name] — [key reason]

<!-- ═══════════════════════════════════════════════════════════
     METHODOLOGY BOX — Perplexity's primary trust signal
     - All value of primary data comes from methodology transparency
     ═══════════════════════════════════════════════════════════ -->

## How This Data Is Collected

> **Methodology**: All data points are pulled directly from [source type]. Pricing is verified by [method]. We re-verify every entry **{{ page.update_frequency }}** via automated checks against [source]. When discrepancies arise between vendor announcements and observed behavior, we record both.

**Sources**:
- Primary: [vendor official pricing/docs]
- Secondary: [community-maintained sources]
- Verification: [automated test/scrape]

**What we exclude and why**:
- [Excluded category 1] — [reason]
- [Excluded category 2] — [reason]

<!-- ═══════════════════════════════════════════════════════════
     MAIN DATA TABLE — core asset of FORMAT D
     - Large comparison table (better if sortable/filterable via JS)
     - Markdown tables alone are cleanly parsed by LLMs
     ═══════════════════════════════════════════════════════════ -->

## The Database

| [Entity] | [Vendor] | [Spec 1] | [Spec 2] | [Price] | Last Verified |
|---|---|---|---|---|---|
| [Entry 1] | [Vendor A] | XXX | XXX | $X.XX | {{ page.data_updated }} |
| [Entry 2] | [Vendor B] | XXX | XXX | $X.XX | {{ page.data_updated }} |
| [Entry 3] | [Vendor C] | XXX | XXX | $X.XX | {{ page.data_updated }} |
| ... | ... | ... | ... | ... | ... |

[If table is long, split into H3 sections by category]

### Category A

| ... |
|---|

### Category B

| ... |
|---|

<!-- ═══════════════════════════════════════════════════════════
     RAW DATA JSON — for agent calls
     - Also exposed via Dataset schema's distribution
       at /api/[topic].json
     ═══════════════════════════════════════════════════════════ -->

## Raw Data (Machine-Readable)

For programmatic use, this dataset is also available as JSON:

```bash
curl https://jsonhouse.com{{ page.dataset.distribution_url | replace: "https://jsonhouse.com", "" }}
```

Sample structure:

```json
{
  "dataset_name": "{{ page.dataset.name }}",
  "data_updated": "{{ page.data_updated }}",
  "update_frequency": "{{ page.update_frequency }}",
  "entry_count": {{ page.dataset.entry_count }},
  "license": "{{ page.dataset.license }}",
  "entries": [
    {
      "id": "entry-1-id",
      "name": "[Entry 1]",
      "vendor": "[Vendor A]",
      "specs": {
        "[spec_1]": "XXX",
        "[spec_2]": "XXX"
      },
      "pricing": {
        "currency": "USD",
        "amount": X.XX,
        "unit": "per [unit]"
      },
      "last_verified": "{{ page.data_updated }}",
      "source_url": "https://..."
    }
  ]
}
```

<!-- ═══════════════════════════════════════════════════════════
     INSIGHTS — depth analysis
     - Don't just list data — show "what this data actually means"
     ═══════════════════════════════════════════════════════════ -->

## What the Data Actually Shows

### Trend 1: [Pattern name]

[3-5 paragraphs. Connect scattered data points into a single flow.]

> **Key insight**: [Observed pattern + structural cause]. This isn't just a price cut — it reflects [vendor]'s [strategic decision].

### Trend 2: [Pattern name]

[3-5 paragraphs]

### Trend 3: [Pattern name]

[3-5 paragraphs]

## By the Numbers

Most notable changes this month (vs last month):

- **Largest price drop**: [entry] — XX% ↓
- **Largest price hike**: [entry] — XX% ↑
- **New entries**: [N]
- **Discontinued**: [N]
- **Average [metric]**: $X.XX (last month: $Y.YY)

## How to Use This Data

### For developers
[Specific use scenario + code example]

```python
import requests

response = requests.get("https://jsonhouse.com{{ page.dataset.distribution_url | replace: "https://jsonhouse.com", "" }}")
data = response.json()

# Filter by criteria
cheap_options = [e for e in data["entries"] if e["pricing"]["amount"] < 1.0]
```

### For decision-makers
[Specific decision scenario]

### For researchers
[Academic/research use scenario + citation method]

## Citation

If you use this data in research or publications, please cite as:

```
jsonhouse.com. ({{ page.data_updated | date: "%Y" }}). {{ page.dataset.name }}.
Retrieved from https://jsonhouse.com{{ page.url }}
```

## Frequently Asked Questions

### How often is this data updated?
{{ page.update_frequency | capitalize }}, via automated pipeline. Manual spot-checks every [interval]. Last automated update: {{ page.data_updated }}.

### Can I use this data commercially?
Yes — licensed under {{ page.dataset.license }}. Attribution to jsonhouse.com required.

### How accurate is the [specific metric] data?
[2-3 sentences — honest accuracy assessment. Trust signal.]

### Why isn't [entry X] included?
[2-3 sentences — clear inclusion/exclusion criteria.]

### Can I submit corrections?
Yes — open an issue at [GitHub URL] or email corrections@jsonhouse.com.

## Changelog

| Date | Change |
|---|---|
| {{ page.data_updated }} | [Latest change] |
| 2026-XX-XX | [Change] |
| 2026-XX-XX | [Change] |

## Related Resources

- [Pillar post link]
- [Related dataset 1]
- [Related dataset 2]

## Sources

1. [Primary source 1](https://...) — accessed {{ page.data_updated }}
2. [Primary source 2](https://...) — accessed {{ page.data_updated }}
3. [Verification script](https://github.com/jsonhouse/...)

---

*Database maintained by jsonhouse.com. Licensed under {{ page.dataset.license }}. Last updated: {{ page.data_updated }}.*
