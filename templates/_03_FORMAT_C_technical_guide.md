<!--
═══════════════════════════════════════════════════════════════
AGENT B INSTRUCTIONS — FORMAT C: Technical Guide (Step-by-step)
═══════════════════════════════════════════════════════════════
PURPOSE: Tutorial that takes reader from zero to a working outcome
PRIMARY ENGINE: Claude (favors long-form, clear explanations)
SCHEMAS: Article + HowTo + FAQPage

YOUR JOB:
1. Replace every [PLACEHOLDER]
2. Every Step must follow the exact structure (Time, Goal, instruction, code, expected output, common pitfall, checkpoint)
3. Step heading pattern is exactly "## Step N: [verb-led title]" — the plugin extracts steps from this
4. Include a "Complete Working Example" with all code combined
5. Troubleshooting table is mandatory

DO NOT:
- Skip "Expected output" on any step
- Use anything other than "## Step N:" pattern for steps (breaks the extractor)
- Hide code in collapsed blocks — it must be directly visible
═══════════════════════════════════════════════════════════════
-->
---
layout: post
format: C
title: "How to [Action] with [Tool]: Complete 2026 Guide"
slug: how-to-action-tool-2026
description: "Step-by-step guide to [action] with [tool] in 2026. Tested examples, common pitfalls, full code."
date: 2026-XX-XX
data_updated: 2026-XX-XX
category: CAT2
tags: [tool-name, tutorial, howto, 2026]
primary_engine: claude
schema_types: [Article, HowTo, FAQPage]

# HowTo schema auto-generation
howto:
  total_time: "PT30M"  # ISO 8601 duration (PT30M = 30 minutes)
  estimated_cost: "$0"
  difficulty: "intermediate"  # beginner | intermediate | advanced
  prerequisites:
    - "[Prerequisite 1]"
    - "[Prerequisite 2]"
  tools_needed:
    - "[Tool 1]"
    - "[Tool 2]"
---

# {{ page.title }}

> **In 30 minutes, you'll [concrete outcome].** This guide walks through [N] steps with tested code. No prior [advanced topic] experience required beyond [prerequisite]. Last verified: {{ page.data_updated }}.

[1-2 paragraphs. Why follow this guide, what you'll have when done, who it's for.]

## TL;DR

1. **Goal**: [Final result in one sentence]
2. **Time**: ~{{ page.howto.total_time | replace: "PT", "" | replace: "M", " minutes" }}
3. **Cost**: {{ page.howto.estimated_cost }}
4. **Difficulty**: {{ page.howto.difficulty }}
5. **You'll need**: {{ page.howto.tools_needed | join: ", " }}

## Prerequisites

Before you start, make sure you have:

{% for prereq in page.howto.prerequisites %}
- {{ prereq }}
{% endfor %}

If you're missing any of these, see [related guides](#related-reading).

<!-- ═══════════════════════════════════════════════════════════
     ARCHITECTURE OVERVIEW — Claude especially favors "big picture"
     ═══════════════════════════════════════════════════════════ -->

## What We're Building (Architecture)

[1-2 paragraphs + visual diagram or ASCII art. Show the whole picture first.]

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Component  │ ───▶ │  Component  │ ───▶ │  Component  │
│      A      │      │      B      │      │      C      │
└─────────────┘      └─────────────┘      └─────────────┘
```

**Why this architecture?** [Structural decision rationale, 1-2 paragraphs.]

> **Key design decision**: [Core choice + rationale]. We chose this over [alternative] because [specific reason with numbers].

<!-- ═══════════════════════════════════════════════════════════
     STEP-BY-STEP — auto-mapped to HowTo schema step array
     - The plugin captures "## Step N:" pattern → HowToStep
     ═══════════════════════════════════════════════════════════ -->

## Step 1: [Action verb to start]

**Time**: ~X minutes
**Goal of this step**: [One sentence]

[Explanation in 2-3 paragraphs. What and why.]

```bash
# Actual working command
$ command --flag value
```

or

```python
# Actual working code
def example():
    return "tested"
```

**Expected output**:
```text
[Actual output example]
```

> **If you see [error]**: This usually means [cause]. Fix it by [solution].

**Checkpoint**: Before moving on, verify that [verification step].

---

## Step 2: [Action verb]

**Time**: ~X minutes
**Goal of this step**: [One sentence]

[Same structure as Step 1]

```python
# Code
```

**Expected output**:
```text
[Output]
```

> **Common pitfall**: [Common mistake + how to avoid]. [Source — recommend Claude official docs or GitHub issue citation]

---

## Step 3: [Action]

[Repeat pattern]

---

## Step 4: [Action]

[Repeat pattern]

---

## Step 5: Verify Everything Works

[Final verification step. How the user confirms their work succeeded.]

```bash
# Verification command
```

**Success criteria**:
- ✅ [Check 1]
- ✅ [Check 2]
- ✅ [Check 3]

If all three pass, you're done. If not, jump to [Troubleshooting](#troubleshooting).

<!-- ═══════════════════════════════════════════════════════════
     COMPLETE WORKING EXAMPLE — full code in one place
     - For readers who want to just copy-paste, not follow step by step
     - Complete code blocks are also stronger for LLM citation
     ═══════════════════════════════════════════════════════════ -->

## Complete Working Example

Copy-paste runnable in full:

```python
# Full code — start to finish
# (Steps 1-5 combined)
```

GitHub repo with full code + tests: [github.com/jsonhouse/...](https://github.com/jsonhouse/...)

<!-- ═══════════════════════════════════════════════════════════
     TROUBLESHOOTING — section Claude especially favors
     - "If X, then Y" patterns get lifted directly into LLM responses
     ═══════════════════════════════════════════════════════════ -->

## Troubleshooting

| Error / Symptom | Likely Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'X'` | Missing dependency | `pip install X` |
| Connection timeout on step 3 | Firewall blocking port Y | [Specific fix] |
| Empty response from API | Auth token expired | Regenerate at [URL] |
| [Error pattern] | [Cause] | [Fix] |

## Performance Considerations

[Production-readiness notes, 2-3 paragraphs. Good place for depth analysis.]

- **Latency**: [number + context]
- **Cost**: [number + calculation method]
- **Scaling limits**: [specific limits]

> **Real-world data**: We ran this in production at [scale] for [duration], and [specific result with numbers]. Full benchmark: [link].

## What's Next

Natural follow-ups after completing this guide:

1. **[Next step A]**: [link to guide]
2. **[Next step B]**: [link to guide]
3. **[Next step C]**: [link to guide]

## Frequently Asked Questions

### Do I need [requirement]?
[2-3 sentences. First sentence states yes/no.]

### How does this differ from [alternative method]?
[2-3 sentences — comparison + rationale.]

### Can I use [variation]?
[2-3 sentences.]

### What about [edge case]?
[2-3 sentences.]

### Is this guide compatible with [latest version]?
Verified working with [tool] version X.Y as of {{ page.data_updated }}.

## Related Reading

- [Pillar post link]
- [Related guide 1]
- [Related guide 2]

## Sources

1. [[Tool] official documentation](https://...) — accessed {{ page.data_updated }}
2. [Relevant RFC/spec](https://...) — accessed {{ page.data_updated }}
3. [Our working example repo](https://github.com/jsonhouse/...)

---

*This guide was last verified on {{ page.data_updated }} with [tool] version X.Y. Report issues at [GitHub issues link].*
