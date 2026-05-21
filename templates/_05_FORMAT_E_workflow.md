<!--
═══════════════════════════════════════════════════════════════
AGENT B INSTRUCTIONS — FORMAT E: Workflow / Downloadable Template
═══════════════════════════════════════════════════════════════
PURPOSE: Production-ready automation workflow that readers can download and deploy
PRIMARY ENGINE: ChatGPT + Gemini (HowTo schema + actionable steps)
SCHEMAS: Article + HowTo + FAQPage

YOUR JOB:
1. Replace every [PLACEHOLDER]
2. The downloadable repo URL is MANDATORY (front matter workflow.download_url)
3. Use "## Step N:" pattern (plugin extracts steps)
4. Include "Real-World Results" with actual production numbers if available
5. Cost Breakdown table is mandatory

DO NOT:
- Describe a workflow without providing the actual template file
- Skip "Who This Is For" (anti-use-cases prevent bad-fit readers)
- Omit "Variants and Extensions" (this is what makes the template reusable)
═══════════════════════════════════════════════════════════════
-->
---
layout: post
format: E
title: "[Workflow Name]: Complete Template (Download + Walkthrough)"
slug: workflow-name-2026
description: "Production-ready [workflow] template for 2026. Download, configure, deploy in 30 minutes."
date: 2026-XX-XX
data_updated: 2026-XX-XX
category: CAT4
tags: [workflow, automation, template, 2026]
primary_engine: chatgpt
schema_types: [Article, HowTo, FAQPage]

# Workflow metadata
workflow:
  name: "[Workflow Name]"
  total_time: "PT30M"
  difficulty: "intermediate"
  download_url: "https://github.com/jsonhouse/workflows/[name]"
  tested_with:
    - "[Platform 1] vX.Y"
    - "[Platform 2] vX.Y"
  monthly_cost_estimate: "$X-Y"
---

# {{ page.title }}

> **What you get**: A working [workflow type] template that [outcome]. Includes [N] nodes, [N] integrations, full configuration. Tested in production. Download: [{{ page.workflow.download_url }}]({{ page.workflow.download_url }}).

[1-2 paragraphs. What problem this workflow solves, who it's for, what you'll have at the end.]

## TL;DR

1. **Outcome**: [Final result in one sentence]
2. **Setup time**: ~{{ page.workflow.total_time | replace: "PT", "" | replace: "M", " minutes" }}
3. **Monthly cost**: {{ page.workflow.monthly_cost_estimate }}
4. **Download**: [GitHub repo]({{ page.workflow.download_url }})
5. **Difficulty**: {{ page.workflow.difficulty }}

## Who This Is For

✅ **Use this if you**:
- [Specific situation 1]
- [Specific situation 2]
- [Specific situation 3]

❌ **Don't use this if you**:
- [Anti-use-case 1]
- [Anti-use-case 2]

<!-- ═══════════════════════════════════════════════════════════
     WORKFLOW DIAGRAM — big picture first
     ═══════════════════════════════════════════════════════════ -->

## Workflow Overview

```
[Trigger]
    │
    ▼
[Step 1: Input]  ──── [Integration A]
    │
    ▼
[Step 2: Process]  ──── [LLM Call]
    │
    ▼
[Step 3: Validate]  ──── [Check]
    │
    ├──▶ [Pass] ──▶ [Step 4: Action]
    │
    └──▶ [Fail] ──▶ [Notify]
```

**Key components**:
- **Trigger**: [What kicks off the workflow]
- **Processing**: [Core logic]
- **Output**: [Final result form]

## What This Workflow Does (Plain English)

[3-5 paragraphs. Explain the automation concept in plain language.]

> **Real example**: When [specific scenario], this workflow [specific action], saving [measurable result — time/money/errors].

## Prerequisites

Before you start, you'll need:

- [ ] [Tool A] account ([free tier link] sufficient)
- [ ] [Tool B] API key ([signup link])
- [ ] [Tool C] installed locally (`npm install ...`)
- [ ] Basic familiarity with [concept]

Estimated setup cost: {{ page.workflow.monthly_cost_estimate }}/month at moderate usage.

## Step 1: Download the Template

```bash
git clone {{ page.workflow.download_url }}.git
cd [folder-name]
```

The repo structure:
```
[folder-name]/
├── workflow.json         # Main template (import this)
├── config/
│   ├── credentials.example
│   └── settings.yaml
├── prompts/
│   └── system-prompt.md  # Customize this
└── README.md
```

## Step 2: Import the Workflow

[Platform-specific import guide — screenshots or clear text]

In [Platform name]:
1. Navigate to [menu path]
2. Click [button name]
3. Select `workflow.json` from the cloned repo
4. Click Import

**Expected result**: You should see [N] nodes in your workflow editor.

## Step 3: Configure Credentials

Copy the example credentials file:
```bash
cp config/credentials.example config/credentials.json
```

Edit `config/credentials.json` with your actual keys:
```json
{
  "platform_a_api_key": "YOUR_KEY_HERE",
  "platform_b_token": "YOUR_TOKEN_HERE",
  "webhook_url": "YOUR_WEBHOOK_HERE"
}
```

> **Security note**: Never commit `credentials.json` to git. The `.gitignore` already excludes it.

## Step 4: Customize the System Prompt

Open `prompts/system-prompt.md` and tailor it to your use case:

```markdown
You are a [ROLE] assistant. Your task is to [TASK].

Context about the user's business:
[BUSINESS_CONTEXT]

Output format:
[FORMAT_REQUIREMENTS]
```

**Variables to customize**:
| Variable | Description | Example |
|---|---|---|
| `[ROLE]` | The expertise persona | "marketing analyst" |
| `[TASK]` | The specific action | "draft email responses" |
| `[BUSINESS_CONTEXT]` | Your context | "B2B SaaS, 50 employees" |

## Step 5: Test Run

Trigger the workflow manually with test data:

```bash
[test command]
```

**Expected output**:
```json
{
  "status": "success",
  "processed_at": "2026-XX-XX...",
  "result": "..."
}
```

If you see errors, jump to [Troubleshooting](#troubleshooting).

## Step 6: Deploy to Production

[Production deployment steps — include schedule, monitoring, alerts]

**Recommended schedule**: [Specific recommendation]
**Monitoring**: [How to monitor]
**Cost alerts**: [Budget alert setup]

## How It Works Under the Hood

[3-5 paragraphs of architecture analysis — why this design, what trade-offs.]

> **Design decision**: We chose [approach] because [structural reason]. The alternative [B approach] is possible but has [specific drawback].

### Component-by-component breakdown

**[Component 1]**:
- Purpose: [Role]
- Cost: [Cost]
- Common failures: [Common failure modes + responses]

**[Component 2]**:
- [Same structure]

## Cost Breakdown

| Component | Usage | Monthly Cost |
|---|---|---|
| [Platform A] subscription | [Plan] | $XX |
| [LLM API] | ~XXX calls × $Y | $XX |
| [Storage] | [N] GB | $X |
| **Total** | | **${{ page.workflow.monthly_cost_estimate }}** |

> **Cost scaling**: This estimate assumes [scale]. At 10x volume, expect [number] due to [factor].

## Variants and Extensions

### Variant 1: [Variant name]
[2-3 paragraphs. How to extend to a different use case.]

### Variant 2: [Variant name]
[2-3 paragraphs]

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Workflow stops at step X | [Cause] | [Fix] |
| API timeout | [Cause] | [Fix] |
| Wrong output format | [Cause] | [Fix] |
| Cost spike | [Cause] | [Fix] |

## Real-World Results

[Actual production results — concrete numbers. Strongest trust signal.]

> **Production data**: We ran this workflow for [duration] processing [volume]. Results:
> - Time saved: [number]
> - Error rate: [number]
> - Cost per task: [number]
> - Failure modes encountered: [number]

## Frequently Asked Questions

### Can I use this with [alternative platform]?
[2-3 sentences — compatibility + conversion approach.]

### How do I scale this beyond [scale]?
[2-3 sentences — scaling strategy + next steps.]

### Is this safe for production?
[2-3 sentences — honest assessment. Link to production-readiness checklist.]

### Can I monetize a service built on this?
Yes — licensed under [license]. [Detailed conditions].

### What if [platform] changes their API?
We re-verify this template [frequency]. Subscribe to updates: [link].

## Related Workflows

- [Pillar post]
- [Related workflow 1]
- [Related workflow 2]

## Sources

1. [[Platform A] documentation](https://...) — accessed {{ page.data_updated }}
2. [[Platform B] documentation](https://...) — accessed {{ page.data_updated }}
3. [Working template repository]({{ page.workflow.download_url }})

---

*Template maintained by jsonhouse.com. Last verified working on {{ page.data_updated }}. Issues: [GitHub link].*
