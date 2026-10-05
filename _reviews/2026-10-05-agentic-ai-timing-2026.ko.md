# Phase 5 리뷰 리포트 — agentic-ai-timing-2026

- 포스트: `_posts/2026-10-05-agentic-ai-timing-2026.md` (초안 `_drafts/2026-10-09-…`에서 발행 시 이동)
- 데이터: `_data/2026-10-05-agentic-ai-timing-2026.json`
- 제목: Agentic AI 2026: Why Every Lab Moved at Once (44자)
- 카테고리 / 클러스터 / 포맷: industry-analysis (CAT7 Deep Dive) / CLUSTER_LLM / A
- 발행: 2026-10-05(월) — 초안은 10-09(금) 분석형 슬롯으로 잡았으나 기웅 승인 즉시 발행
- 자료 수집일: 2026-10-05

## 1. 핵심 주장 요약 (3줄)

1. 에이전틱 AI가 "지금" 온 이유는 모델 하나가 똑똑해져서가 아니에요. 9/7~10/5 4주 동안 세 곡선이 동시에 교차했기 때문이에요: 장기 작업용 모델 출시, 에이전트가 실제로 내는 가격(캐시 읽기) 인하, 기업 클라우드(AWS) 안으로의 유통.
2. 이 가격 경쟁은 중국(DeepSeek)이 먼저 연 "캐시 열"에서 벌어졌어요. 미국 벤더가 그 열로 따라 들어왔고, 미·중 가격 격차는 양쪽이 같이 움직여 좁혀졌어요(DeepSeek 인상 + 미국 인하).
3. 에이전트는 사용량에 상한이 없는 새로운 토큰 소비처라 정액제가 버티지 못해요. OpenAI가 같은 주에 API 캐시가는 반값으로, Pro 200 사용량은 축소한 게 그 증거예요. 데이터 측면에서는 "돈으로 내는 계층"과 "데이터로 내는 계층"이 분리되고 있어요.

## 2. 인용된 수치 / 출처 목록

| 수치 | 출처 | 확인 |
|---|---|---|
| Argon 출력 1M 토큰(기존 64K), 도입가 $2/$10, 캐시 95% 할인, 정가 $4/$20, Fairwind 우선 배포, DeepSWE 77.9%, AutomationBench 51.3% | [Google Argon 발표문](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) (2026-09-30) | 원문 확인 |
| Argon 캐시 $0.10 | 위 "95% off"로 우리가 계산 — 표 셀에 "jsonhouse derived" 표기 | 파생값 |
| Gemini 3.8 Flash Cyber 존재 | [Google 9월 업데이트 요약](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/) | 원문 확인 |
| $2/$10 모델 수 1→4, 0.1x 미만 캐시 모델 수(미국 0→4), sol vs DeepSeek v4-pro 배수 11.5x→3.0x / 34.5x→5.1x / 138x→4.5x | `_data/pricing_history/` 주간 스냅샷 직접 계산 | 재계산 확인 |
| GPT-6.1-sol h=95% $0.195 vs GPT-6-sol $0.29 | llm-cache-pricing 포스트(10-05 갱신분) | 일치 |
| DeepSeek 8/17 인상이 시리즈 최초 인상 | llm-api-pricing 변경 이력(changelog) | 일치 |
| Pro 200: 가격 $200 유지, 신규 구독 사용량 축소, 그랜드파더링 10/29까지, Pro 500 출시 | [OpenAI 도움말](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers) | 원문 확인 |
| Codex 20x→10x, Pro 메시지 200→100 | 구독자가 공개 인용한 OpenAI 안내 메일(X 게시물, 2차 매체 다수) | **OpenAI 페이지에서 미확인** — 본문에 "quoted, not published"로 명시 |
| GPT-6 Astra Bedrock GA 9/8, Sol·Luna 9/22, Claude Platform on AWS 5/11 | AWS What's New 3건 | 원문 날짜 확인 |
| OpenAI on AWS 인용문("operate within the systems…"), "All customer data is processed by Amazon Bedrock" | [OpenAI 발표](https://openai.com/index/openai-on-aws/) | 원문 확인(게시일 본문에 없음) |
| 에이전트 4배·멀티에이전트 15배 토큰, 토큰 사용량이 성능 분산 80% 설명 | [Anthropic 엔지니어링](https://www.anthropic.com/engineering/multi-agent-research-system) (2025-06-13) | 원문 확인 |
| Meta AI 대화 → 콘텐츠·광고 개인화(2025-12-16 시행), 민감 주제 광고 제외, 월 10억+ 사용자 | [Meta Newsroom](https://about.fb.com/news/2025/10/improving-your-recommendations-apps-ai-meta/) (2025-10-01) | 원문 확인 |
| Claude 소비자 학습 선택제, 허용 시 5년·미허용 30일 보관, API·상업용 제외 | [Anthropic 약관 업데이트](https://www.anthropic.com/news/updates-to-our-consumer-terms) (2025-08-28) | 원문 확인 |

## 3. 적용된 스타일 + 근거

**박종훈 구조** (CAT7 Deep Dive). 개별 뉴스(모델 출시, 가격 인하, 파트너십, 요금제 변경)를 "에이전트라는 새 고객"이라는 하나의 흐름으로 꿰는 거시 분석이라서요.

- ① 훅: 도입 3문단 + TL;DR
- ② 원재료: "What Shipped in Four Weeks" 일정 표 + $2/$10 가격대 표
- ③ 이면 분석: "The Real Story" — 에이전트의 토큰 소비 구조 → 캐시 열 경쟁 → 미·중 격차 수렴 → 유통망 경쟁 → 정액제 축소, 5개 하위 절
- ④ 큰 그림: 데이터가 두 번째 화폐가 됨(프라이버시의 가격 계층화, 보안의 제품 라인화) + 중국 증류 포스트와 연결
- ⑤ 실용 결론: 빌드·구매자 관점 4개 원칙 + FAQ

데이터 표가 5개라 jsonhouse DNA와 경계에 있지만, 카테고리가 industry-analysis이고 글의 목적이 흐름 해석이라 박종훈 구조로 판단했어요.

## 4. 이면 분석 핵심

에이전트는 "토큰을 더 쓸수록 성능이 좋아지는" 첫 워크로드라서, 토큰을 파는 연구소에게는 기다려온 고객이에요. 그래서 경쟁이 정가가 아니라 반복 컨텍스트 가격(캐시 읽기)과 구매 경로(클라우드 약정)로 옮겨갔어요. 같은 이유로, 상한 없이 소비하는 에이전트 앞에서 정액제는 축소되고 종량제로 밀려나요.

## 5. 의심스러운 사실 관계 (확인 요청)

1. **Pro 200 20x→10x 수치** — OpenAI 자체 페이지에는 없어요. 본문은 "구독자가 공개 인용한 안내"로만 적었어요. 이 수치를 아예 빼고 싶으시면 말씀해 주세요.
2. **Argon 도입가 종료 시점** — Google이 공개하지 않았어요. 본문에 "not published"로 적었어요.
3. **Argon은 공개 가격 페이지에 없음**(10/5 기준). 그래서 표에서 Argon 행만 출처가 발표문이에요.
4. **"observed" 날짜**는 출시일이 아니라 우리 주간 수집에서 처음 본 날짜예요. 실제로 GPT-6 Sol은 Bedrock GA(9/22)가 우리 첫 관측(9/28)보다 빨라요. 표 헤더와 Methodology에 구분해 적었어요.
5. **Meta "옵트아웃 불가"·"EU·영국·한국 제외"** — 2차 매체에서 흔히 쓰는 표현이지만 Meta 원문에는 없어요(원문은 "most regions"). 그래서 본문에서 쓰지 않았어요.
6. **Anthropic 4배·15배**는 2025-06 자료이고 Anthropic 자체 시스템 기준이에요. Limitations에 명시했어요.
7. **"프라이버시가 가격 계층이 된다"는 전망**은 우리의 해석이라고 본문에 명시했어요.

## 6. 내부 링크 검증

| 링크 | 위치 | 존재 |
|---|---|---|
| `/posts/llm-api-pricing-2026/` | 일정 표 도입, Methodology | ✅ `_posts/2026-07-17-llm-api-pricing-2026.md` |
| `/posts/llm-cache-pricing-2026/` | 캐시 열 분석 | ✅ `_posts/2026-08-01-llm-cache-pricing-2026.md` |
| `/posts/china-ai-catch-up-2026/` | 보안 문단 | ✅ `_posts/2026-09-14-china-ai-catch-up-2026.md` |

## 7. 자동 검증 결과

- post-validation 훅: PASS. 남은 WARN은 커버 파일 없음 1건뿐(초안 단계 허용).
- GEO 검증: ok. primary_sources 11개, key_facts 9개, attribution 완비, `license` 필드 없음.
- 본문 약 2,490단어(표 제외). 제목 44자, description 156자.
- 품질 자가 점수: 정확도 8.0×0.30 + 구조 8.0×0.25 + 실용성 7.5×0.25 + 데이터 8.5×0.20 = **7.98**

## 8. 커버 이미지 프롬프트 전문

- 가로세로비: **16:9**
- 저장 경로: `assets/img/posts/agentic-ai-timing-2026-cover-raw.png`
- **코드로 그리지 말 것** — 이미지 모델로 생성해야 해요(C11: 색상 1,000개 이하면 거부).
- 소재 근거: CLUSTER_LLM = 광학과 굴절(IMAGE_GUIDE §8). 피사체는 하나만, 셀 수 있는 반복 요소는 없어요.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single heavy faceted glass prism, hand-polished, with slightly
chipped edges, resting on a slab of dark slate.

SCENE: A narrow beam of light enters one face of the prism and leaves the
opposite face as one bent line that runs out toward the edge of the frame,
grazing the slate surface as it goes.

COMPOSITION: Wide horizontal establishing shot. One dominant subject placed on
the left or right third, not dead center. Clear foreground-to-background
separation with real depth. Keep the outer 8% of the top and bottom edges free
of critical detail — the frame is cropped to 1.91:1 afterwards.

STYLE: High-end technical magazine cover art. Photographic realism with an
editorial, restrained mood. Tactile real-world materials with visible surface
texture — machined metal, glass, stone, paper, fabric. Shallow depth of field.
Single subject, generous empty space, quiet and precise rather than busy.

LIGHTING & COLOR: Deep navy base environment (#0F172A). Cool cyan key light
(#38BDF8) raking from one side; warm amber rim light (#F59E0B) from the
opposite edge. Strong directional light with soft falloff. No flat ambient
fill, no uniform studio lighting.

AVOID: text, letters, numbers, captions, watermarks, logos, brand marks,
charts, graphs, axes, bars, gauges, readable scales or dials, UI screenshots,
app windows, code editors, robots, humanoids, androids, human faces, hands,
brains, glowing orbs, circuit-board motifs, holographic HUD overlays, neon
cyberpunk cliché, stock-photo business people, collage, split panels, grids of
thumbnails, borders, frames, vignette.

ASPECT RATIO: 2048x1152

MUST KEEP: Exactly one subject. Consistent light direction across the whole
frame. Large areas of unbroken dark background. Nothing that could be read as
a measurement.
```
