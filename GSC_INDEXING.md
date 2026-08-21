# GSC 색인 등록 URL 목록

Google Search Console(속성: `https://www.jsonhouse.com`) 에 수동 색인 요청(URL 검사 → 색인 생성 요청)할 URL 모음.

- **최종 갱신**: 2026-08-21 (자동)
- **소스**: `_posts/` + `_tabs/` + 루트 정적 페이지
- **주의**: GSC 수동 색인 요청은 하루 약 10건 제한. 아래 우선순위 순서대로 진행.
- **1번 표와 복사용 블록은 자동 생성**됩니다 (`.claude/hooks/sync-indexing-list.sh`).
  `AUTO:` 마커 사이는 직접 수정해도 덮어써집니다 — 단, `상태`/`메모` 칸은 URL 기준으로 보존됩니다.

---

## 1. 포스트 (우선순위 최상)

발행일 역순. 새 글일수록 먼저 요청.

<!-- AUTO:POSTS-TABLE-START -->
| # | 상태 | URL | 발행일 | 제목 | 메모 |
|---|---|---|---|---|---|
| 1 | [ ] | https://www.jsonhouse.com/posts/llm-price-war-balance-sheet-2026/ | 2026-08-21 | LLM Price War 2026: Who Is Paying for Your Discount |  |
| 2 | [ ] | https://www.jsonhouse.com/posts/ai-agent-payments-crawl-toll-2026/ | 2026-08-18 | AI Agent Payments 2026: What a Crawl Toll Really Earns |  |
| 3 | [ ] | https://www.jsonhouse.com/posts/ai-crawler-traffic-2026/ | 2026-08-13 | AI Crawler Traffic 2026: 747 Crawls per Human Visit |  |
| 4 | [ ] | https://www.jsonhouse.com/posts/ai-content-quality-gates-2026/ | 2026-08-06 | AI Content Quality Gates 2026: 33 Rules That Caught Us |  |
| 5 | [ ] | https://www.jsonhouse.com/posts/china-ai-coding-plans-2026/ | 2026-08-05 | China AI Coding Plans 2026: Quotas You Can't Compare |  |
| 6 | [ ] | https://www.jsonhouse.com/posts/llm-cache-pricing-2026/ | 2026-08-01 | LLM Cache Pricing 2026: The Real Cost of Cached Input |  |
| 7 | [ ] | https://www.jsonhouse.com/posts/best-ai-coding-tools-2026/ | 2026-08-01 | Best AI Coding Tools 2026: Pricing & Benchmark Reality |  |
| 8 | [ ] | https://www.jsonhouse.com/posts/best-llm-2026/ | 2026-07-25 | Best LLM 2026: Capability and Limits Compared |  |
| 9 | [ ] | https://www.jsonhouse.com/posts/llm-subscription-guide-2026/ | 2026-07-25 | Best LLM Subscription 2026: What You Really Pay For |  |
| 10 | [ ] | https://www.jsonhouse.com/posts/ai-crawler-ecosystem-2026/ | 2026-07-17 | AI Crawler Ecosystem 2026: Who Scrapes the Web and Who Pays |  |
| 11 | [ ] | https://www.jsonhouse.com/posts/llm-api-pricing-2026/ | 2026-07-17 | LLM API Pricing 2026: Full Comparison Table (Weekly) |  |
| 12 | [ ] | https://www.jsonhouse.com/posts/chatgpt-ads-2026-aeo-reddit-citations/ | 2026-05-17 | ChatGPT Ads 2026: AEO Traffic and Reddit Citations |  |
| 13 | [ ] | https://www.jsonhouse.com/posts/gigo-prompts-2026-why-vague-prompts-fail/ | 2026-05-07 | GIGO Prompts 2026: Why Vague Prompts Fail (Data + Fix) |  |
| 14 | [ ] | https://www.jsonhouse.com/posts/helpful-content-system-2026/ | 2026-05-01 | Google's Helpful Content System 2026: How It Really Decides |  |
| 15 | [ ] | https://www.jsonhouse.com/posts/synthid-c2pa-explained-2026/ | 2026-04-30 | SynthID and C2PA: How AI Image Verification Works in 2026 |  |
| 16 | [ ] | https://www.jsonhouse.com/posts/eeat-ai-content-2026/ | 2026-04-29 | Pass Google E-E-A-T 2026: AI-Assisted Content Survival Guide |  |
| 17 | [ ] | https://www.jsonhouse.com/posts/google-ai-content-penalties-2026/ | 2026-04-27 | What Google AI Content Policy Actually Penalizes in 2026 |  |
<!-- AUTO:POSTS-TABLE-END -->

### 복사용 (포스트만)

<!-- AUTO:POSTS-URLS-START -->
```
https://www.jsonhouse.com/posts/llm-price-war-balance-sheet-2026/
https://www.jsonhouse.com/posts/ai-agent-payments-crawl-toll-2026/
https://www.jsonhouse.com/posts/ai-crawler-traffic-2026/
https://www.jsonhouse.com/posts/ai-content-quality-gates-2026/
https://www.jsonhouse.com/posts/china-ai-coding-plans-2026/
https://www.jsonhouse.com/posts/llm-cache-pricing-2026/
https://www.jsonhouse.com/posts/best-ai-coding-tools-2026/
https://www.jsonhouse.com/posts/best-llm-2026/
https://www.jsonhouse.com/posts/llm-subscription-guide-2026/
https://www.jsonhouse.com/posts/ai-crawler-ecosystem-2026/
https://www.jsonhouse.com/posts/llm-api-pricing-2026/
https://www.jsonhouse.com/posts/chatgpt-ads-2026-aeo-reddit-citations/
https://www.jsonhouse.com/posts/gigo-prompts-2026-why-vague-prompts-fail/
https://www.jsonhouse.com/posts/helpful-content-system-2026/
https://www.jsonhouse.com/posts/synthid-c2pa-explained-2026/
https://www.jsonhouse.com/posts/eeat-ai-content-2026/
https://www.jsonhouse.com/posts/google-ai-content-penalties-2026/
```
<!-- AUTO:POSTS-URLS-END -->

---

## 2. 허브 / 탭 페이지 (우선순위 중)

내부 링크 허브. 크롤 경로 확보용으로 포스트 다음 순서로 요청.

> `/ai-tools/`, `/productivity/` 탭은 해당 카테고리에 발행 글이 0건이라
> 숨김 처리(`published: false`)했다. 첫 글 발행 시 탭을 되살리고 이 표에
> 다시 추가할 것.

| 상태 | URL | 설명 |
|---|---|---|
| [ ] | https://www.jsonhouse.com/ | 홈 |
| [ ] | https://www.jsonhouse.com/ai-models/ | AI Models 탭 |
| [ ] | https://www.jsonhouse.com/prompts/ | Prompts 탭 |
| [ ] | https://www.jsonhouse.com/data/ | Data 탭 |
| [ ] | https://www.jsonhouse.com/safety/ | Safety 탭 |
| [ ] | https://www.jsonhouse.com/categories/ | 카테고리 인덱스 |
| [ ] | https://www.jsonhouse.com/archives/ | 아카이브 |

---

## 3. 기타 페이지 (우선순위 하)

| 상태 | URL | 설명 |
|---|---|---|
| [ ] | https://www.jsonhouse.com/privacy/ | 개인정보처리방침 (AdSense 심사 필수) |

---

## 4. 색인 요청 대상 아님 (참고)

크롤러/에이전트용 엔드포인트. GSC 색인 요청 불필요하지만 `robots.txt` 접근 허용 여부는 확인.

- `https://www.jsonhouse.com/sitemap.xml` — GSC Sitemaps 메뉴에 제출 (색인 요청 아님)
- `https://www.jsonhouse.com/robots.txt`
- `https://www.jsonhouse.com/llms.txt`
- `https://www.jsonhouse.com/api/posts.json`
- `https://www.jsonhouse.com/data/{slug}.json` — 포스트별 데이터 파일 (플러그인 자동 생성)
- `https://www.jsonhouse.com/tags/*` — 태그 아카이브. 자동 생성 저품질 페이지로 분류될 수 있어 수동 요청 지양.

---

## 5. 미발행 (발행되면 이 목록에 추가)

| 파일 | 예상 URL | 상태 |
|---|---|---|
| `_tabs/methodology.md` | https://www.jsonhouse.com/methodology/ | untracked — 커밋/배포 전 |
| `_drafts/*` | — | 드래프트, Phase 5 미완 |

---

## 6. 운영 규칙

1. **1번 표는 자동 갱신**된다. `_posts/`에 새 포스트가 들어오면(Write/Edit 또는 `git mv`) 훅이 표와 복사용 블록을 다시 만든다. 수동으로 행을 추가할 필요 없음.
2. 색인 요청 완료 시 `[ ]` → `[x]` 로 변경. 이 값은 URL 기준으로 보존되므로 자동 갱신에 지워지지 않는다.
3. 색인 거부(`발견됨 - 현재 색인이 생성되지 않음` 등) 시 사유를 `메모` 칸에 기록. 메모도 보존된다.
4. **`sitemap.xml` 은 손댈 필요 없다.** `jekyll-sitemap` 플러그인이 매 배포마다 `_posts/` 기준으로 새로 생성한다. 로컬 `_site/sitemap.xml` 은 gitignore 대상 빌드 아티팩트라 오래된 상태일 수 있으니 **판단 근거로 쓰지 말 것** — 확인은 항상 아래 라이브 URL로.
5. 2번·3번 표(탭/정적 페이지)는 수동 관리. 탭이 추가되면 직접 넣는다.
6. GSC `Sitemaps` 메뉴에는 `sitemap.xml` 이 한 번만 등록돼 있으면 되고, 재제출은 불필요하다.

### 라이브 사이트맵에서 URL 목록 재생성

```bash
curl -s https://www.jsonhouse.com/sitemap.xml \
  | grep -o '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g'
```

### 이 파일 수동 재생성 (훅이 안 돌았을 때)

```bash
python3 .claude/hooks/sync_indexing_list.py "$(git rev-parse --show-toplevel)"
```
