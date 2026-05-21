<!--
═══════════════════════════════════════════════════════════════
AGENT B INSTRUCTIONS — FORMAT F: Benchmark Report (Direct Testing)
═══════════════════════════════════════════════════════════════
PURPOSE: Original benchmark report with full methodology transparency
PRIMARY ENGINE: Perplexity + Claude (primary data + long-form analysis)
SCHEMAS: Article + Dataset + FAQPage

YOUR JOB:
1. Replace every [PLACEHOLDER]
2. Methodology section MUST be the first major section after TL;DR
3. Include 95% confidence intervals on all accuracy numbers
4. "Limitations and Caveats" is mandatory — honesty boosts citation rate
5. Reproducibility section must include actual runnable commands

DO NOT:
- Publish benchmarks without methodology transparency
- Hide failed test cases or excluded data
- Skip "What we deliberately excluded" — this is a major trust signal
- Use vague claims like "our tests show" without numbers
═══════════════════════════════════════════════════════════════
-->
---
layout: post
format: F
title: "[Benchmark Name] 2026: Tested Results ([N] Models)"
slug: benchmark-name-2026
description: "Real-world benchmark of [N] [AI models/tools] on [task]. Methodology, raw data, surprises."
date: 2026-XX-XX
data_updated: 2026-XX-XX
category: CAT1  # or CAT2
tags: [benchmark, testing, comparison, 2026]
primary_engine: perplexity
schema_types: [Article, Dataset, FAQPage]

# Benchmark metadata
benchmark:
  name: "[Benchmark Name]"
  task_category: "[coding / reasoning / hallucination / long-context]"
  models_tested: XX
  tasks_per_model: XX
  total_runs: XXX
  testing_period: "2026-XX-XX to 2026-XX-XX"
  cost_to_run: "$XX"
  raw_data_url: "https://github.com/jsonhouse/benchmarks/[name]"
  reproducible: true
---

# {{ page.title }}

> **Bottom line:** We tested **{{ page.benchmark.models_tested }} models** across **{{ page.benchmark.tasks_per_model }} tasks** ({{ page.benchmark.total_runs }} total runs) on **{{ page.benchmark.task_category }}**. **[Winner]** came out on top with **XX.X%** accuracy, but the real story is [surprising insight in one sentence].

[1-2 paragraphs. What was benchmarked, why, what makes it different from existing benchmarks.]

## TL;DR (Verified {{ page.data_updated }})

1. **Overall winner**: [Model] — XX.X% accuracy
2. **Best value (accuracy/$)**: [Model] — $X.XX per correct answer
3. **Biggest surprise**: [Finding in 15 words]
4. **Total testing cost**: {{ page.benchmark.cost_to_run }}
5. **Reproducible**: Yes — full code + data at [{{ page.benchmark.raw_data_url }}]({{ page.benchmark.raw_data_url }})

<!-- ═══════════════════════════════════════════════════════════
     METHODOLOGY — Perplexity's most critical trust signal
     - All value of primary data flows from methodology transparency
     ═══════════════════════════════════════════════════════════ -->

## Methodology

> **TL;DR methodology**: {{ page.benchmark.total_runs }} runs across {{ page.benchmark.models_tested }} models, each tested {{ page.benchmark.tasks_per_model }} times on identical inputs. Temperature 0.7, no system prompts, fresh sessions per run. Tested {{ page.benchmark.testing_period }}.

### Models tested

| Model | Provider | Version | API endpoint | Cost per 1M tokens |
|---|---|---|---|---|
| [Model 1] | [Provider] | vX.Y | [endpoint] | $X.XX in / $X.XX out |
| [Model 2] | [Provider] | vX.Y | [endpoint] | $X.XX in / $X.XX out |
| ... | ... | ... | ... | ... |

### Tasks

We selected {{ page.benchmark.tasks_per_model }} tasks designed to be:
- **Reproducible**: Same input → measurable correct output
- **Realistic**: Drawn from [source — actual use cases]
- **Discriminating**: Tasks where previous benchmarks gave different scores

**Task categories**:
1. [Category 1] — [N] tasks
2. [Category 2] — [N] tasks
3. [Category 3] — [N] tasks

### Scoring

[Exactly how scoring worked — auto-grading vs manual, what counts as correct, partial credit handling]

**Auto-scored**: [N] tasks via [method]
**Manually scored**: [N] tasks via [method]
**Inter-rater agreement** (manual): XX% (Cohen's kappa = X.XX)

### What we deliberately excluded

[Trust signal — what you excluded and why]
- [Exclusion 1] — [reason]
- [Exclusion 2] — [reason]

<!-- ═══════════════════════════════════════════════════════════
     MAIN RESULTS TABLE — core of FORMAT F
     ═══════════════════════════════════════════════════════════ -->

## Results

### Overall Accuracy

| Model | Accuracy | 95% CI | Median latency | Cost per correct answer |
|---|---|---|---|---|
| [Model 1] | XX.X% | [XX.X, XX.X] | XXXms | $X.XXX |
| [Model 2] | XX.X% | [XX.X, XX.X] | XXXms | $X.XXX |
| [Model 3] | XX.X% | [XX.X, XX.X] | XXXms | $X.XXX |
| ... | ... | ... | ... | ... |

> All results from {{ page.benchmark.total_runs }} runs conducted {{ page.benchmark.testing_period }}. Full raw data: [{{ page.benchmark.raw_data_url }}]({{ page.benchmark.raw_data_url }}).

### By Task Category

#### Category 1: [Name]

| Model | Accuracy | Notes |
|---|---|---|
| [Model 1] | XX.X% | [Observation] |
| [Model 2] | XX.X% | [Observation] |

#### Category 2: [Name]

[Same structure]

#### Category 3: [Name]

[Same structure]

<!-- ═══════════════════════════════════════════════════════════
     RAW DATA JSON
     ═══════════════════════════════════════════════════════════ -->

### Raw data (machine-readable)

```json
{
  "benchmark_name": "{{ page.benchmark.name }}",
  "data_updated": "{{ page.data_updated }}",
  "methodology_version": "1.0",
  "total_runs": {{ page.benchmark.total_runs }},
  "models": [
    {
      "name": "[Model 1]",
      "version": "vX.Y",
      "overall_accuracy": XX.X,
      "confidence_interval_95": [XX.X, XX.X],
      "median_latency_ms": XXX,
      "cost_per_correct_usd": X.XXX,
      "by_category": {
        "category_1": XX.X,
        "category_2": XX.X,
        "category_3": XX.X
      }
    }
  ],
  "reproducibility": {
    "code_url": "{{ page.benchmark.raw_data_url }}",
    "data_url": "{{ page.benchmark.raw_data_url }}/data",
    "license": "MIT"
  }
}
```

<!-- ═══════════════════════════════════════════════════════════
     ANALYSIS — depth analysis at its sharpest
     ═══════════════════════════════════════════════════════════ -->

## What These Results Actually Mean

### Finding 1: [Insight title]

[3-5 paragraphs. Not just numbers — what these results actually show.]

> **Key insight**: [Model]'s [performance gap] is not coincidence. It's the result of [provider]'s [structural decision], and it's decisive in [specific use case].

### Finding 2: [Insight title]

[3-5 paragraphs]

### Finding 3: The Surprise

[The most unexpected finding — clickbait-adjacent but honest]

[3-5 paragraphs. "We expected X. We got Y. Here's why."]

## Where Each Model Wins

Where each model has a clear advantage:

**[Model 1]**:
- ✅ [Category]: XX% better than next
- ✅ [Specific task]: [Specific advantage]

**[Model 2]**:
- ✅ [Category]: XX% better than next
- ✅ [Specific task]: [Specific advantage]

**[Model 3]**:
- ✅ [Category]: XX% better than next
- ✅ [Specific task]: [Specific advantage]

## Cost-Performance Frontier

[Pareto frontier analysis — which model is optimal at which budget]

| Budget tier | Best choice | Why |
|---|---|---|
| Free/free tier | [Model] | [Reason] |
| < $X/month | [Model] | [Reason] |
| Enterprise | [Model] | [Reason] |

## Limitations and Caveats

> **Honest limitations**: This benchmark has the following blind spots:

- [Limitation 1 — what we couldn't measure]
- [Limitation 2 — external validity issue]
- [Limitation 3 — temporal limitation]

[2-3 paragraphs of honest assessment — this actually boosts citation rate.]

## Reproducing This Benchmark

Full code + data at: [{{ page.benchmark.raw_data_url }}]({{ page.benchmark.raw_data_url }})

```bash
git clone {{ page.benchmark.raw_data_url }}.git
cd [folder]
pip install -r requirements.txt

# Set your API keys
cp .env.example .env
# Edit .env

# Run the benchmark (cost: ~{{ page.benchmark.cost_to_run }})
python run_benchmark.py --models all
```

Expected runtime: [time]. Expected cost: {{ page.benchmark.cost_to_run }}.

## How We Differ from [Other Benchmark]

[Differences from existing benchmarks — trust signal]

| Aspect | jsonhouse benchmark | [Other benchmark] |
|---|---|---|
| Task source | [Source] | [Source] |
| Models tested | {{ page.benchmark.models_tested }} | XX |
| Reproducible | ✅ Full code + data | [Status] |
| Cost transparency | ✅ {{ page.benchmark.cost_to_run }} disclosed | [Status] |

## Frequently Asked Questions

### Why aren't results from [other benchmark] used here?
[2-3 sentences — methodological difference + honest acknowledgment.]

### How do these results change with [variable]?
[2-3 sentences — honest answer on external validity.]

### Can you re-run with [new model]?
[2-3 sentences — update plan.]

### What's your confidence in these numbers?
[2-3 sentences — statistical significance, CI, limitations.]

### How can I trust these numbers?
[2-3 sentences — emphasize full reproducibility, raw data disclosure.]

## Update Schedule

This benchmark will be re-run:
- When a major new model is released
- Every quarter for trending updates
- Minor methodology improvements as needed

Subscribe to updates: [link]

## Related Benchmarks

- [Pillar post]
- [Related benchmark 1]
- [Related benchmark 2]

## Sources

1. [Task source 1](https://...)
2. [Methodology reference](https://...) — academic paper
3. [Raw data and code]({{ page.benchmark.raw_data_url }})
4. [Pricing data sources]

---

*Benchmark conducted by jsonhouse.com {{ page.benchmark.testing_period }}. All raw data, code, and methodology are public. Last updated: {{ page.data_updated }}. License: MIT (code) / CC BY 4.0 (data).*
