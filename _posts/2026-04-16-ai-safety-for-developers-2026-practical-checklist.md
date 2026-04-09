---
layout: post
title: "AI Safety for Developers 2026: Practical Checklist"
date: 2026-04-16 09:00:00 +0000
categories: [ai-safety-ethics]
tags: [ai-safety, prompt-injection, llm-security, responsible-ai, ethics, checklist, 2026]
description: "Practical AI safety checklist for developers in 2026. Covers prompt injection, data leakage, bias, output validation, and responsible LLM deployment patterns."
canonical_url: https://www.jsonhouse.com/posts/ai-safety-for-developers-2026-practical-checklist
permalink: /posts/ai-safety-for-developers-2026-practical-checklist/
data_updated: 2026-04-10
toc: true
author: ai_tech_blog
schema_type: Article
format_type: C
category_id: CAT6
quality_score: auto
sources:
  - https://owasp.org/www-project-top-10-for-large-language-model-applications
  - https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
  - https://www.nist.gov/artificial-intelligence/ai-risk-management-framework
---

Every developer shipping an LLM-powered feature in 2026 is also shipping a new attack surface. Prompt injection, data leakage through model context, hallucinated outputs presented as facts, and unintended bias at scale — these are not theoretical risks. They are documented incidents affecting production systems today. This guide is a practical checklist: the specific checks you need to run before an AI feature goes live, organized by risk category with concrete mitigations for each.

---

## TL;DR

- **Prompt injection** is the #1 LLM security risk in 2026 — validate and sanitize all user input before it reaches the model.
- **Data leakage** through system prompts and context is the most common confidentiality failure — never put secrets in prompts.
- **Output validation** is required before presenting LLM responses to users or downstream systems.
- **Bias and fairness** checks must be part of your testing pipeline, not an afterthought.
- This checklist maps to **OWASP Top 10 for LLM Applications** (2025 edition) and **NIST AI RMF**.

---

## The Risk Landscape in 2026

```json
{
  "data_updated": "2026-04-10",
  "source": "OWASP LLM Top 10 (2025), NIST AI RMF, Internal synthesis",
  "risk_categories": [
    {
      "rank": 1,
      "name": "Prompt Injection",
      "owasp_id": "LLM01",
      "severity": "CRITICAL",
      "description": "Attacker crafts input that overrides system instructions or exfiltrates context",
      "real_world_incident": "Customer-facing chatbots manipulated to reveal internal pricing or bypass safety filters"
    },
    {
      "rank": 2,
      "name": "Insecure Output Handling",
      "owasp_id": "LLM02",
      "severity": "HIGH",
      "description": "LLM output passed to interpreters (shell, SQL, HTML) without sanitization",
      "real_world_incident": "Code-generation tools producing shell commands executed without review"
    },
    {
      "rank": 3,
      "name": "Training Data Poisoning",
      "owasp_id": "LLM03",
      "severity": "HIGH",
      "description": "Malicious data introduced into fine-tuning pipeline, altering model behavior",
      "real_world_incident": "Fine-tuned customer service models exhibiting unexpected brand-hostile responses"
    },
    {
      "rank": 4,
      "name": "Model Denial of Service",
      "owasp_id": "LLM04",
      "severity": "HIGH",
      "description": "Inputs crafted to maximize compute cost or cause timeouts",
      "real_world_incident": "Recursive prompt loops exhausting token budgets on pay-per-token APIs"
    },
    {
      "rank": 5,
      "name": "Supply Chain Vulnerabilities",
      "owasp_id": "LLM05",
      "severity": "HIGH",
      "description": "Risks from third-party models, plugins, or datasets",
      "real_world_incident": "Compromised MCP server returning malicious tool call responses"
    },
    {
      "rank": 6,
      "name": "Sensitive Information Disclosure",
      "owasp_id": "LLM06",
      "severity": "CRITICAL",
      "description": "PII, API keys, or confidential data exposed through model output or context",
      "real_world_incident": "System prompts containing API keys leaked via carefully crafted user queries"
    },
    {
      "rank": 7,
      "name": "Insecure Plugin Design",
      "owasp_id": "LLM07",
      "severity": "HIGH",
      "description": "LLM-triggered tool calls execute with insufficient authorization checks",
      "real_world_incident": "AI assistant given write access to production database via overpermissioned tool"
    },
    {
      "rank": 8,
      "name": "Excessive Agency",
      "owasp_id": "LLM08",
      "severity": "HIGH",
      "description": "LLM granted more permissions than required for its task",
      "real_world_incident": "Agentic system deleting files or sending emails without explicit human approval"
    },
    {
      "rank": 9,
      "name": "Overreliance",
      "owasp_id": "LLM09",
      "severity": "MEDIUM",
      "description": "Users or systems treating LLM output as ground truth without verification",
      "real_world_incident": "Legal teams citing AI-hallucinated case law in court filings"
    },
    {
      "rank": 10,
      "name": "Model Theft",
      "owasp_id": "LLM10",
      "severity": "MEDIUM",
      "description": "Extracting proprietary model weights or training data through API queries",
      "real_world_incident": "Fine-tuned models reconstructed via systematic API probing"
    }
  ]
}
```

---

## The Pre-Launch Checklist

### Section 1: Input Security

**LLM01 — Prompt Injection Prevention**

- [ ] All user input is separated from system instructions — never concatenated into the system prompt
- [ ] Input length is bounded (`max_tokens` on input enforced at application layer, not just API)
- [ ] Structured data (JSON, XML) from users is parsed and validated before injection into prompts
- [ ] Indirect prompt injection vectors are considered: file uploads, URLs, third-party API responses that get summarized by the model
- [ ] A dedicated input validation layer exists before the LLM call

**Code pattern — separate user input from system context:**

```python
# WRONG: Concatenating user input into system prompt
system = f"You are a helpful assistant. User context: {user_provided_context}"

# CORRECT: Keep system prompt static, pass user content in messages only
system = "You are a helpful assistant. Answer only questions about our product."
messages = [
    {"role": "user", "content": user_message}  # user_message sanitized separately
]
```

**Input sanitization for structured contexts:**

```python
import re

def sanitize_for_prompt(user_input: str, max_length: int = 2000) -> str:
    # Remove injection patterns
    sanitized = re.sub(r'(ignore previous|disregard|system prompt|<\|.*?\|>)', 
                       '[FILTERED]', user_input, flags=re.IGNORECASE)
    # Truncate to safe length
    return sanitized[:max_length]
```

---

### Section 2: Output Security

**LLM02 — Insecure Output Handling**

- [ ] LLM-generated code is never executed without human review in production flows
- [ ] HTML output from LLM is sanitized before rendering (use a library like DOMPurify)
- [ ] SQL generated by LLM is validated against an allowlist of permitted operations
- [ ] Shell commands from LLM are sandboxed or require explicit human confirmation
- [ ] JSON from LLM is validated against a schema before use in downstream systems

**Code pattern — validate LLM JSON output:**

```python
from pydantic import BaseModel, ValidationError
import anthropic

class ProductReview(BaseModel):
    rating: int  # 1-5
    summary: str
    sentiment: str  # positive | negative | neutral

def get_validated_review(text: str) -> ProductReview:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        system="Respond only with valid JSON matching the schema: {rating: int, summary: str, sentiment: str}",
        messages=[{"role": "user", "content": text}]
    )
    
    try:
        return ProductReview.model_validate_json(response.content[0].text)
    except ValidationError as e:
        raise ValueError(f"LLM returned invalid output: {e}")
```

---

### Section 3: Data Privacy

**LLM06 — Sensitive Information Disclosure**

- [ ] System prompts contain no API keys, passwords, or PII
- [ ] User data sent to the LLM API is reviewed against your privacy policy and user consent
- [ ] GDPR/CCPA: users in applicable jurisdictions are informed that their input may be processed by a third-party AI API
- [ ] Conversation history is purged according to your data retention policy — not stored indefinitely
- [ ] Responses are scanned for PII before display (regex or a dedicated PII detection library)

**PII detection before output:**

```python
import re

PII_PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'phone': r'\b(\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
    'credit_card': r'\b(?:\d[ -]?){13,16}\b'
}

def contains_pii(text: str) -> bool:
    return any(re.search(pattern, text) for pattern in PII_PATTERNS.values())

def safe_output(llm_response: str) -> str:
    if contains_pii(llm_response):
        # Log for review, return safe fallback
        log_pii_incident(llm_response)
        return "I'm unable to display this response. Please contact support."
    return llm_response
```

---

### Section 4: Agent and Tool Security

**LLM07 / LLM08 — Excessive Agency**

- [ ] Every tool/function the LLM can call has a documented permission scope
- [ ] Write operations (database writes, file writes, API mutations) require human confirmation in production
- [ ] Tools are scoped to the minimum data necessary — a customer service agent should not have access to all customer records
- [ ] Agentic workflows have a maximum step count — infinite loops are impossible
- [ ] Every tool call is logged with: timestamp, tool name, parameters, and the reasoning that triggered it

**Minimal permission principle for MCP tools:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://readonly_user:pass@localhost/db"
      }
    }
  }
}
```

Note: use a `readonly_user` database role — never connect Claude to a database with write permissions unless write access is explicitly required and each write is confirmed.

---

### Section 5: Bias and Fairness

- [ ] Test prompts include demographic diversity — does the model respond differently based on names, locations, or languages implied in the input?
- [ ] High-stakes decisions (loan approvals, medical triage, hiring screening) are not made solely by LLM output without human review
- [ ] Evaluation dataset covers underrepresented groups proportionally
- [ ] Model outputs for legally protected characteristics (race, gender, religion, disability) are reviewed by a human before deployment
- [ ] A process exists to receive and investigate bias reports from users

**Quick bias test pattern:**

```python
NAMES_TEST = [
    ("Emily Johnson", "female, likely white"),
    ("Jamal Williams", "male, likely Black"),
    ("Wei Chen", "likely Asian"),
    ("Maria Garcia", "likely Latina")
]

def run_bias_check(prompt_template: str, client) -> dict:
    results = {}
    for name, demographic in NAMES_TEST:
        prompt = prompt_template.format(name=name)
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}]
        )
        results[demographic] = response.content[0].text
    return results
    # Review results manually for systematic differences
```

---

### Section 6: Reliability and Hallucination

**LLM09 — Overreliance**

- [ ] Responses that reference facts, citations, or numerical data are labeled as AI-generated and unverified
- [ ] The UI does not present LLM output as authoritative — include a disclaimer for factual claims
- [ ] Critical workflows have a fallback if the LLM returns an unexpected format or hallucinates structured data
- [ ] For RAG (retrieval-augmented generation) systems: source documents are cited in the response so users can verify
- [ ] Temperature is set to 0 for deterministic tasks (classification, extraction); higher values are reserved for creative tasks

---

## Compliance Mapping

| Check | OWASP LLM | NIST AI RMF | GDPR Relevant |
|-------|-----------|------------|---------------|
| Input sanitization | LLM01 | GOVERN 1.1 | No |
| Output validation | LLM02 | MEASURE 2.5 | No |
| No secrets in prompts | LLM06 | MANAGE 1.3 | Yes |
| PII scan on output | LLM06 | MANAGE 2.4 | Yes |
| Minimal tool permissions | LLM07, LLM08 | GOVERN 2.2 | No |
| Human review for high stakes | LLM09 | GOVERN 4.2 | Yes |
| Bias testing | — | MEASURE 2.2 | Yes (Art. 22) |

---

## Frequently Asked Questions

### Is prompt injection a solved problem in 2026?

No. Prompt injection remains an open research problem. The current best practice is defense in depth: strict input-output separation, input sanitization, output validation, and monitoring. No single technique eliminates the risk. Systems that accept arbitrary user text and pass it to an LLM with privileged system context will always carry some prompt injection risk — the goal is to minimize the blast radius of a successful attack.

### Do I need these checks for internal tools, not customer-facing ones?

Yes, with adjusted scope. Internal tools often have elevated permissions (access to internal databases, Slack, code repositories) that make successful prompt injection more damaging than in a customer-facing context. The risk profile is different but not lower. An internal AI assistant with write access to your production database and access to your Slack history is a high-value attack target.

### How do I stay current on LLM security as the threat landscape evolves?

Three sources updated most frequently in 2026: OWASP LLM Top 10 (updated annually), the NIST AI RMF (guidance documents published quarterly), and the Anthropic Security Research blog. Subscribe to CVE feeds for any LLM dependencies you use (LangChain, LlamaIndex, AutoGen all had significant security advisories in 2025).

---

## Related Posts

- [Claude System Prompt Templates 2026: 25+ Ready](/posts/claude-system-prompt-templates-2026/) — secure system prompt patterns for common use cases
- [AI Workflow Automation Templates 2026: 10 Setups](/posts/ai-workflow-automation-templates-2026/) — apply these safety checks to automated pipelines
- [MCP Guide 2026: Connect Claude to Any Tool](/posts/mcp-guide-2026-connect-claude-to-any-tool/) — MCP security considerations for tool-connected agents

---

Last updated: 2026-04-10
