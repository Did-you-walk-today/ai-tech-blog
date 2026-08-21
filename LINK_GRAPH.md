# 내부 링크 그래프

포스트끼리 어떻게 엮여 있는지를 보여주는 색인. **이 문서는 자동 생성됩니다.**

- **최종 갱신**: 2026-08-21 (자동)
- **소스**: `_posts/*.md` 본문의 `](/posts/<slug>/)` 링크
- **생성**: `python3 .claude/hooks/link_graph.py "$(git rev-parse --show-toplevel)"`
- **점검만**: `python3 .claude/hooks/link_graph.py --report`
- `AUTO:` 마커 사이는 직접 고쳐도 덮어써집니다 — 단 1번 표의 `메모` 칸은
  슬러그 기준으로 보존됩니다. 링크를 바꾸려면 문서가 아니라 **포스트 본문**을 고치십시오.

> 손으로 쓰는 링크 색인을 만들지 않는 이유: 링크를 고칠 때마다 두 곳을 고쳐야 하고,
> 언젠가 반드시 한 곳을 빠뜨립니다. 그래프는 포스트에서 파생되는 값이므로 파생시킵니다.

---

## 1. 포스트별 요약

`인` = 이 글로 들어오는 링크 수, `아웃` = 이 글에서 나가는 링크 수.
noindex 글은 인바운드를 잃는 것이 정상이라 고아로 세지 않습니다.

<!-- AUTO:GRAPH-TABLE-START -->
| # | 슬러그 | 클러스터 | 인 | 아웃 | 상태 | 메모 |
|---|---|---|---|---|---|---|
| 1 | llm-price-war-balance-sheet-2026 | LLM | 0 | 3 | **고아** |  |
| 2 | ai-agent-payments-crawl-toll-2026 | AEO | 0 | 5 | **고아** |  |
| 3 | ai-crawler-traffic-2026 | AEO | 3 | 3 | ok |  |
| 4 | ai-content-quality-gates-2026 | DEVTOOLS | 1 | 3 | ok |  |
| 5 | china-ai-coding-plans-2026 | LLM | 1 | 4 | ok |  |
| 6 | llm-cache-pricing-2026 | LLM | 3 | 7 | ok |  |
| 7 | best-ai-coding-tools-2026 | DEVTOOLS | 1 | 2 | ok |  |
| 8 | best-llm-2026 | LLM | 3 | 6 | ok |  |
| 9 | llm-subscription-guide-2026 | LLM | 4 | 2 | ok |  |
| 10 | ai-overviews-seo-2026 | AEO | 1 | 5 | noindex |  |
| 11 | ai-crawler-ecosystem-2026 | AEO | 8 | 6 | ok |  |
| 12 | llm-api-pricing-2026 | LLM | 14 | 5 | ok |  |
| 13 | chatgpt-ads-2026-aeo-reddit-citations | AEO | 6 | 2 | ok |  |
| 14 | gigo-prompts-2026-why-vague-prompts-fail | PROMPTS | 2 | 2 | ok |  |
| 15 | helpful-content-system-2026 | AI_CONTENT_POLICY | 3 | 2 | ok |  |
| 16 | synthid-c2pa-explained-2026 | AI_CONTENT_POLICY | 1 | 2 | ok |  |
| 17 | eeat-ai-content-2026 | AI_CONTENT_POLICY | 6 | 2 | ok |  |
| 18 | youtube-ai-monetization-2026 | AI_CONTENT_POLICY | 2 | 2 | noindex |  |
| 19 | google-ai-content-penalties-2026 | AI_CONTENT_POLICY | 6 | 2 | ok |  |
<!-- AUTO:GRAPH-TABLE-END -->

---

## 2. 지적 사항

<!-- AUTO:GRAPH-FINDINGS-START -->
| 심각도 | 유형 | 슬러그 | 내용 |
|---|---|---|---|
| WARN | NOINDEX<- | ai-content-quality-gates-2026 | links to noindex page /posts/ai-overviews-seo-2026/ ('how citation and ranking have split into different games') |
| WARN | NOINDEX<- | eeat-ai-content-2026 | links to noindex page /posts/youtube-ai-monetization-2026/ ('YouTube AI Monetization 2026: What Is Inauthentic Content') |
| WARN | NOINDEX<- | google-ai-content-penalties-2026 | links to noindex page /posts/youtube-ai-monetization-2026/ ('YouTube AI monetization and inauthentic-content rules') |
| WARN | ORPHAN | ai-agent-payments-crawl-toll-2026 | no inbound internal link |
| WARN | ORPHAN | llm-price-war-balance-sheet-2026 | no inbound internal link |
<!-- AUTO:GRAPH-FINDINGS-END -->

유형 설명 — `DANGLING`: 없는 슬러그로 링크(ERROR, 발행 차단) · `ORPHAN`: 인바운드 0 ·
`DEADEND`: 아웃바운드 0 · `THIN`: 아웃바운드 2개 미만 · `NOINDEX<-`: 라이브 글이
색인 제외된 글을 링크 · `SELFLINK`: 자기 자신을 링크.

---

## 3. 백링크 위치 (인바운드 상세)

각 글마다 **어느 글의 어떤 문장에서** 링크가 걸렸는지. 슬러그를 바꾸거나 글을
내릴 때 어디를 고쳐야 하는지 여기서 확인합니다.

<!-- AUTO:GRAPH-EDGES-START -->

### llm-price-war-balance-sheet-2026

LLM Price War 2026: Who Is Paying for Your Discount

_인바운드 없음 — 이 글로 들어오는 내부 링크가 하나도 없습니다._

### ai-agent-payments-crawl-toll-2026

AI Agent Payments 2026: What a Crawl Toll Really Earns

_인바운드 없음 — 이 글로 들어오는 내부 링크가 하나도 없습니다._

### ai-crawler-traffic-2026

AI Crawler Traffic 2026: 747 Crawls per Human Visit

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-agent-payments-crawl-toll-2026 | AI Crawler Observatory traffic report |
| ai-agent-payments-crawl-toll-2026 | AI Crawler Traffic 2026: 5,227 Crawls, 7 Visitors |
| llm-price-war-balance-sheet-2026 | crawler measurements |

### ai-content-quality-gates-2026

AI Content Quality Gates 2026: 33 Rules That Caught Us

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-crawler-ecosystem-2026 | AI Content Quality Gates 2026 |

### china-ai-coding-plans-2026

China AI Coding Plans 2026: Quotas You Can't Compare

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-content-quality-gates-2026 | the documentation existed on a domain we had not checked |

### llm-cache-pricing-2026

LLM Cache Pricing 2026: The Real Cost of Cached Input

| 걸린 글 | 앵커 텍스트 |
|---|---|
| best-llm-2026 | LLM Cache Pricing 2026 |
| llm-api-pricing-2026 | LLM Cache Pricing 2026 |
| llm-price-war-balance-sheet-2026 | cache pricing analysis |

### best-ai-coding-tools-2026

Best AI Coding Tools 2026: Pricing & Benchmark Reality

| 걸린 글 | 앵커 텍스트 |
|---|---|
| china-ai-coding-plans-2026 | Best AI Coding Tools 2026 |

### best-llm-2026

Best LLM 2026: Capability and Limits Compared

| 걸린 글 | 앵커 텍스트 |
|---|---|
| china-ai-coding-plans-2026 | Best LLM 2026 |
| llm-cache-pricing-2026 | Best LLM 2026: Capability and Limits Compared |
| llm-cache-pricing-2026 | capability limits rather than raw benchmark scores |

### llm-subscription-guide-2026

Best LLM Subscription 2026: What You Really Pay For

| 걸린 글 | 앵커 텍스트 |
|---|---|
| best-llm-2026 | Best LLM Subscription 2026 |
| best-llm-2026 | Best LLM Subscription 2026: What You Really Pay For |
| china-ai-coding-plans-2026 | Best LLM Subscription 2026 |
| llm-cache-pricing-2026 | Best LLM Subscription 2026: What You Really Pay For |

### ai-overviews-seo-2026 *(noindex)*

AI Overviews SEO 2026: Recover Your Lost Traffic

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-content-quality-gates-2026 | how citation and ranking have split into different games |

### ai-crawler-ecosystem-2026

AI Crawler Ecosystem 2026: Who Scrapes the Web and Who Pays

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-agent-payments-crawl-toll-2026 | The AI Crawler Ecosystem 2026 |
| ai-agent-payments-crawl-toll-2026 | our July analysis of the AI crawler ecosystem |
| ai-content-quality-gates-2026 | how much crawlers take relative to what they send back |
| ai-crawler-traffic-2026 | AI crawler ecosystem |
| ai-overviews-seo-2026 | AI Crawler Ecosystem 2026 |
| ai-overviews-seo-2026 | how the AI crawler ecosystem works in 2026 |
| best-ai-coding-tools-2026 | AI crawler ecosystem in 2026 |
| best-llm-2026 | AI Crawler Ecosystem 2026: Who Scrapes the Web and Who Pays |

### llm-api-pricing-2026

LLM API Pricing 2026: Full Comparison Table (Weekly)

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-agent-payments-crawl-toll-2026 | LLM API Pricing 2026 |
| ai-crawler-ecosystem-2026 | LLM API Pricing 2026: Full Comparison Table |
| ai-crawler-ecosystem-2026 | LLM API pricing table |
| ai-crawler-traffic-2026 | LLM API pricing table |
| best-ai-coding-tools-2026 | LLM API pricing comparison for 2026 |
| best-llm-2026 | LLM API Pricing 2026 |
| best-llm-2026 | LLM API Pricing 2026: Full Comparison Table (Weekly) |
| china-ai-coding-plans-2026 | LLM API Pricing 2026 |
| llm-cache-pricing-2026 | LLM API Pricing 2026: Full Comparison Table (Weekly) |
| llm-cache-pricing-2026 | pricing table |
| llm-cache-pricing-2026 | splitting between rising flagship prices and deflating everything else |
| llm-cache-pricing-2026 | weekly LLM API pricing table |
| llm-price-war-balance-sheet-2026 | LLM API Pricing 2026 |
| llm-subscription-guide-2026 | LLM API pricing, where per-token rates are published openly |

### chatgpt-ads-2026-aeo-reddit-citations

ChatGPT Ads 2026: AEO Traffic and Reddit Citations

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-crawler-ecosystem-2026 | ChatGPT Ads 2026: AEO Traffic and Reddit Citations |
| ai-crawler-ecosystem-2026 | ChatGPT ads and AEO analysis |
| ai-crawler-traffic-2026 | where AI answer engines source their citations |
| llm-api-pricing-2026 | ChatGPT Ads 2026: AEO Traffic and Reddit Citations |
| llm-api-pricing-2026 | ChatGPT ads and AEO economics |
| llm-subscription-guide-2026 | ChatGPT ads and AI citation behavior in 2026 |

### gigo-prompts-2026-why-vague-prompts-fail

GIGO Prompts 2026: Why Vague Prompts Fail (Data + Fix)

| 걸린 글 | 앵커 텍스트 |
|---|---|
| llm-api-pricing-2026 | GIGO Prompt Engineering: Why Vague Prompts Fail |
| llm-api-pricing-2026 | vague prompts inflate token consumption and degrade output quality simultaneously |

### helpful-content-system-2026

Google's Helpful Content System 2026: How It Really Decides

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-overviews-seo-2026 | Helpful Content System principles from 2026 |
| chatgpt-ads-2026-aeo-reddit-citations | Google's Helpful Content System: how it decides what content survives |
| gigo-prompts-2026-why-vague-prompts-fail | how Google's Helpful Content System evaluates content across a site, not just a page |

### synthid-c2pa-explained-2026

SynthID and C2PA: How AI Image Verification Works in 2026

| 걸린 글 | 앵커 텍스트 |
|---|---|
| youtube-ai-monetization-2026 | SynthID and C2PA image verification for 2026 |

### eeat-ai-content-2026

Pass Google E-E-A-T 2026: AI-Assisted Content Survival Guide

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-overviews-seo-2026 | E-E-A-T for AI content in 2026 |
| chatgpt-ads-2026-aeo-reddit-citations | How Google's E-E-A-T framework evaluates AI-assisted content in 2026 |
| gigo-prompts-2026-why-vague-prompts-fail | E-E-A-T signals, as Google's quality systems operationalize them |
| google-ai-content-penalties-2026 | Google E-E-A-T survival guide for AI-assisted content |
| helpful-content-system-2026 | E-E-A-T survival guide for AI-assisted content |
| synthid-c2pa-explained-2026 | E-E-A-T and AI Content: The 2026 Survival Guide |

### youtube-ai-monetization-2026 *(noindex)*

YouTube AI Monetization 2026: What Is Inauthentic Content

| 걸린 글 | 앵커 텍스트 |
|---|---|
| eeat-ai-content-2026 | YouTube AI Monetization 2026: What Is Inauthentic Content |
| google-ai-content-penalties-2026 | YouTube AI monetization and inauthentic-content rules |

### google-ai-content-penalties-2026

What Google AI Content Policy Actually Penalizes in 2026

| 걸린 글 | 앵커 텍스트 |
|---|---|
| ai-crawler-ecosystem-2026 | Google AI Content Penalties 2026 |
| ai-overviews-seo-2026 | Google's AI content penalties in 2026 |
| eeat-ai-content-2026 | What Google AI Content Policy Actually Penalizes in 2026 |
| helpful-content-system-2026 | What Google AI Content Policy Actually Penalizes in 2026 |
| synthid-c2pa-explained-2026 | AI-generated content and quality signals |
| youtube-ai-monetization-2026 | What Google AI Content Policy Actually Penalizes in 2026 |
<!-- AUTO:GRAPH-EDGES-END -->
