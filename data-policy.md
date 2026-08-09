---
layout: page
title: Data Use Policy
permalink: /data-policy/
description: "How to use Json House datasets: attribution is required, what we allow and reserve, the privacy rules we hold ourselves to, and the quality commitments attached to every published dataset."
---

*Version 1.0 — August 9, 2026*

Json House publishes machine-readable datasets alongside every post. This page states
what we ask of anyone using them, and what we commit to in return. Both halves matter:
a policy that only makes demands has not earned the right to make them.

This policy covers:

- `https://www.jsonhouse.com/data/{slug}.json` — per-post structured datasets
- `https://www.jsonhouse.com/data/index.json` — the dataset catalogue
- `https://www.jsonhouse.com/api/posts.json` — the post index
- `https://www.jsonhouse.com/llms.txt` — the machine-readable entry point

It does not cover post prose, which is a separate work.

---

## Attribution is required

You may cite, analyse, redistribute, and generate answers from these datasets.
**Attribution is required in every case.**

Preferred form:

```
Json House, "{title}", https://www.jsonhouse.com/data/{slug}.json (retrieved YYYY-MM-DD)
```

Every dataset carries a ready-to-use `attribution` block, so nothing has to be
assembled by hand:

```json
"attribution": {
  "source": "Json House",
  "source_url": "https://www.jsonhouse.com/posts/{slug}/",
  "dataset_url": "https://www.jsonhouse.com/data/{slug}.json",
  "citation": "Json House, \"{title}\", jsonhouse.com (2026-08-03)",
  "attribution_required": true,
  "terms_url": "https://www.jsonhouse.com/data-policy/"
}
```

If you use this data in a generated answer, the answer should name either
**jsonhouse.com** or the dataset URL. "According to one blog" is not attribution.

### Allowed

- Citation and excerpting for citation
- Analysis and derived figures
- Answer and summary generation
- Redistribution that keeps the attribution intact

### Reserved — ask first

- **Bulk mirroring with attribution stripped.** Full-catalogue harvesting already
  happens against this site; this clause is about that
- **Republishing our measurements as your own primary source**
- Commercial bulk redistribution

---

## No licence is declared

This page requires attribution. It does **not** grant a licence, and our datasets
carry no `license` field. That is deliberate.

These datasets are largely factual measurements, and facts attract weak copyright
protection in most jurisdictions — a licence label would promise an enforceability
that does not exist. Standard open licences are also irrevocable for copies already
distributed, and we are not ready to make that call permanently. What we actually
want is not litigation but citation, and citation is won with machine-readable
provenance rather than a licence badge.

---

## What we commit to

**Stated cadence, kept.** Every dataset declares how often it is refreshed. We raise
that cadence rather than lower it, and only declare what we can sustain.

**No silent overwrites.** When a figure changes, the change is recorded. We do not
retroactively edit past snapshots to look as though they were always correct.

**Stated measurement limits.** Where a number is a floor rather than a total, we say
so. Where instrumentation began partway through a series, we give the date and leave
earlier rows empty instead of inferring them. Where we excluded something — our own
verification requests, for instance — we say what and why.

**Published methodology.** Measurement datasets ship with an account of how the
measurement was made. A figure nobody can reproduce is an assertion, not a source.

---

## Privacy rules we hold ourselves to

| Item | Rule |
|---|---|
| Client IP | Never stored. Country and network operator only |
| `cookie` / `authorization` headers | Stripped before any capture |
| Human visits arriving from AI answers | Published as counts only, never joined with country, user agent, or timestamp |
| Ordinary visitors | Not logged at all |

Small samples make re-identification easier, not harder. A handful of referral visits
combined with country and user agent could single out a person, so those fields never
leave together.

---

## How we write about what we observe

A user agent string can be set by anyone. When a request claims to be a given
company's crawler, that claim is not evidence, and we do not report it as one.

We name a company only on the basis of signals a client cannot forge — Cloudflare's
verified-bot classification, or the originating network. When an identity turns out
to be forged, the named company is the party impersonated, and our writing says so.

---

## Changes

This policy is versioned. Changes are dated and explained, and are **not applied
retroactively** to data already distributed. Tightened conditions take effect from the
next refresh, not backwards.

---

## Questions

Anything not covered here — bulk access, unusual use, corrections to a dataset —
see the [contact details on the about page](/about/).
