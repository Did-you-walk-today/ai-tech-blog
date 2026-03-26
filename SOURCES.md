# SOURCES.md — Trusted Source List

Trusted sources for content discovery and data collection. Listed by trust tier.

---

## TIER 1 — Official Sources (always check, use exclusively for pricing data)

### AI Model Providers
- https://anthropic.com/news — Model releases, policy updates
- https://anthropic.com/pricing — Claude API pricing (official)
- https://openai.com/blog — GPT model releases, API changes
- https://platform.openai.com/docs/models — OpenAI model specs
- https://openai.com/api/pricing/ — OpenAI pricing (official)
- https://deepmind.google/research — DeepMind research announcements
- https://blog.google/technology/google-deepmind/ — Google AI blog
- https://mistral.ai/news/ — Mistral releases
- https://www.cohere.com/blog — Cohere releases

### Benchmarks & Leaderboards
- https://lmarena.ai — LMSYS Chatbot Arena leaderboard
- https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard — Open LLM Leaderboard
- https://scale.com/leaderboard — HELM leaderboard
- https://paperswithcode.com/sota — Papers with Code benchmarks

### Models & Papers
- https://huggingface.co/models — New models (filter: downloads > 1000, last 48h)
- https://arxiv.org/list/cs.AI/recent — AI papers
- https://arxiv.org/list/cs.CL/recent — NLP/LLM papers

### Developer Tools
- https://cursor.com/changelog — Cursor updates
- https://github.blog — GitHub/Copilot updates
- https://code.visualstudio.com/updates — VS Code + Copilot
- https://docs.anthropic.com/en/release-notes/api — Claude API release notes
- https://modelcontextprotocol.io — MCP protocol updates

---

## TIER 2 — Community Sources (check if time allows, verify with Tier 1)

- https://news.ycombinator.com — Filter: points > 100, AI/ML topic, last 48h
- https://reddit.com/r/MachineLearning/hot — Top posts last 48h
- https://reddit.com/r/LocalLLaMA/hot — Local LLM community
- https://twitter.com/search?q=LLM+AI — Recent AI announcements (verify with official)

---

## TIER 3 — News & Analysis (background research only, never primary source for data)

- https://techcrunch.com/tag/artificial-intelligence/
- https://venturebeat.com/ai/
- https://the-decoder.com
- https://simonwillison.net — Reliable AI commentary

---

## Source Trust Rules

1. Pricing data: TIER 1 only, cross-verify with at least 2 official sources
2. Benchmark scores: TIER 1 only, cite specific leaderboard and date
3. Model specs: TIER 1 only, official documentation
4. News/announcements: TIER 1 preferred, TIER 2 acceptable if TIER 1 confirms
5. Opinion/analysis: TIER 2–3, clearly labeled as "community perspective"

## Data Staleness

Always record the exact URL and access date when collecting data:
```json
{
  "url": "https://anthropic.com/pricing",
  "accessed_date": "2026-03-26",
  "trust_tier": 1,
  "data_type": "pricing"
}
```
