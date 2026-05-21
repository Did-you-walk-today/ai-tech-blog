<!--
═══════════════════════════════════════════════════════════════
AGENT B INSTRUCTIONS — FORMAT B: Prompt Library
═══════════════════════════════════════════════════════════════
PURPOSE: Curated, tested prompt collection for a tool or role
PRIMARY ENGINE: ChatGPT (highest "lift" rate for FAQ/list formats)
SCHEMAS: Article + HowTo + FAQPage

YOUR JOB:
1. Replace every [PLACEHOLDER]
2. For each prompt, include ALL fields: use case, best model, why it works, prompt text, example input, example output
3. Every prompt block follows the exact same structure
4. Prompts must be copy-paste functional (no truncation)
5. Include "What We Tested and Rejected" section — trust signal

DO NOT:
- Skip the "Why it works" line on any prompt
- Use different structures across prompts (consistency is the value)
- Omit example output (this is what ChatGPT lifts)
═══════════════════════════════════════════════════════════════
-->
---
layout: post
format: B
title: "[N] Best [Tool/Role] Prompts for 2026 (Copy & Paste)"
slug: tool-prompts-2026
description: "[N] proven prompts for [use case] in 2026. Copy-paste ready. Tested with [model]."
date: 2026-XX-XX
data_updated: 2026-XX-XX
category: CAT3
tags: [prompts, prompt-engineering, tool-name, 2026]
primary_engine: chatgpt
schema_types: [Article, HowTo, FAQPage]

# Library metadata
prompt_count: XX
tested_with: ["Claude Sonnet 4.6", "GPT-5", "Gemini 2.5"]
license: "CC BY 4.0"
---

# {{ page.title }}

> **What this is:** {{ page.prompt_count }} battle-tested prompts for [use case]. Each prompt is verified to work with **{{ page.tested_with | join: ", " }}** as of {{ page.data_updated }}. Copy, paste, ship.

[1-2 paragraph introduction. Who this library is for, how it was tested, why it matters.]

## TL;DR

1. **For [use case 1]**: Use Prompt #X — [core effect]
2. **For [use case 2]**: Use Prompt #X — [core effect]
3. **For [use case 3]**: Use Prompt #X — [core effect]
4. **All prompts**: Tested {{ page.data_updated }} | Licensed {{ page.license }}
5. **Best model overall**: [model name] (consistency score X.X/5)

<!-- ═══════════════════════════════════════════════════════════
     QUICK NAVIGATION — essential for long list-style pages
     - When ChatGPT lifts, it includes section anchors in citations
     ═══════════════════════════════════════════════════════════ -->

## Quick Navigation

| # | Prompt | Best For | Tested Model |
|---|---|---|---|
| 1 | [Prompt Title 1](#prompt-1) | [Use case] | Claude Sonnet 4.6 ✅ |
| 2 | [Prompt Title 2](#prompt-2) | [Use case] | GPT-5 ✅ |
| 3 | [Prompt Title 3](#prompt-3) | [Use case] | All ✅ |
| ... | ... | ... | ... |

<!-- ═══════════════════════════════════════════════════════════
     PROMPT BLOCK — standard structure, repeated for each prompt
     ═══════════════════════════════════════════════════════════ -->

---

## Prompt 1: [Descriptive Title]

**Use case**: [One sentence describing exactly when to use this]
**Best model**: [model name]
**Why it works**: [Core mechanism in one sentence — trust signal]

```text
[Full prompt text.
Copy-paste functional as written.
Variables marked as [VARIABLE_NAME].

Example:
You are an expert [ROLE]. Your task is to [TASK].

Context:
[CONTEXT]

Constraints:
- [CONSTRAINT 1]
- [CONSTRAINT 2]

Output format:
[FORMAT]

Begin.]
```

**Example input**:
```text
[Actual usage example — something a reader can follow]
```

**Example output** ({{ page.tested_with[0] }}):
```text
[Actual model response — truncated if long]
```

> **Pro tip**: [Practical operational tip in one sentence — authority signal]

---

## Prompt 2: [Descriptive Title]

**Use case**: [...]
**Best model**: [...]
**Why it works**: [...]

```text
[Prompt text]
```

**Example input**:
```text
[...]
```

**Example output**:
```text
[...]
```

---

<!-- Repeat the pattern N times — every prompt has identical structure -->

## How to Customize These Prompts

[Guide for tailoring prompts to the reader's situation. 3-5 paragraphs.]

### Variable substitution patterns

| Placeholder | What to replace with | Example |
|---|---|---|
| `[ROLE]` | The expertise persona | "senior backend engineer" |
| `[CONTEXT]` | Your specific situation | "Python FastAPI codebase, 50k LOC" |
| `[TASK]` | The desired action verb + outcome | "refactor for testability" |

## Why These Prompts Work (The Pattern)

[3-5 paragraphs. Behind-the-scenes analysis — "why this pattern consistently works." Recommend citing Anthropic/OpenAI official guides.]

> **Anthropic's official guidance**: "[Direct quote from docs.anthropic.com]" — this is why we applied [pattern] to every prompt in the library.

## What We Tested and Rejected

[Trust signal — "we tested X and only N survived." Highly effective in GEO.]

During testing, the following patterns were eliminated for low consistency:

- **Pattern X**: XX% success rate — [reason for failure]
- **Pattern Y**: XX% success rate — [reason for failure]
- **Pattern Z**: XX% success rate — [reason for failure]

## Frequently Asked Questions

### Can I use these prompts commercially?
Yes. All prompts are licensed under {{ page.license }} — attribution to jsonhouse.com appreciated but not required.

### Do these work with [model not in tested list]?
[2-3 sentences — honest answer about generalization.]

### How often is this library updated?
We re-verify every prompt monthly against the latest model versions. Last verified: {{ page.data_updated }}.

### Why didn't you include [popular prompt pattern]?
[2-3 sentences — trust signal.]

### Can I submit my own prompts?
[Yes/No + submission process.]

## Related Resources

- [Ultimate AI Prompt Library 2026](/posts/ultimate-prompt-library-2026) — pillar
- [Claude vs GPT-5 Prompt Differences](/posts/claude-vs-gpt5-prompts)
- [System Prompts for Coding Agents](/posts/system-prompts-coding)

## Sources

1. [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/...) — accessed {{ page.data_updated }}
2. [OpenAI Cookbook](https://...) — accessed {{ page.data_updated }}
3. [Our prompt testing repo](https://github.com/jsonhouse/prompts) — raw test results

---

*All prompts in this library are licensed under {{ page.license }}. Last verified: {{ page.data_updated }}.*
