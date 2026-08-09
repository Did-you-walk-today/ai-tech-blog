---
layout: page
title: "AI Crawler Observatory"
description: "First-party measurement of the AI agents that read jsonhouse.com: which crawlers arrive, which forge their identity, and whether llms.txt and structured data are actually consumed."
icon: fas fa-satellite-dish
order: 7
published: false
---

<p>Every other page on this site reports what someone else published. This one reports what we measured ourselves — a Cloudflare Worker in front of the origin records every AI crawler, answer-engine fetch, and machine-endpoint read, and those logs become the datasets below.</p>

<p>The questions this section exists to answer: does anything actually read <code>llms.txt</code>, does publishing machine-readable JSON get it consumed, how much traffic do AI answers send back, and how often does a request wearing a crawler's name turn out not to be that crawler.</p>

{% include hub-post-list.html category="ai-crawler-observatory" %}
