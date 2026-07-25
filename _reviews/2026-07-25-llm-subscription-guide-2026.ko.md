# Phase 5 리뷰 리포트 — Best LLM Subscription 2026

- **슬러그**: `llm-subscription-guide-2026`
- **드래프트**: `_drafts/2026-07-25-llm-subscription-guide-2026.md`
- **데이터**: `_data/2026-07-25-llm-subscription-guide-2026.json`
- **포맷/클러스터/스타일**: Format A · CLUSTER_LLM(CAT1) · jsonhouse DNA
- **기웅 지시 반영(2차 개고)**: ① "토큰량 미공개" 지적을 **글의 중심 논지로 승격** ② 전 벤더 요금제 비교 폐기 → **ChatGPT만 예시**로 ③ **베스트셀러(Plus $20) + 최고 요금제(Pro $200) 2개**만 비교 ④ Google USD 미표기 문제는 "원래 아무도 안 밝힌다"로 흡수

## 1. 핵심 주장 요약 (3줄)

1. **어떤 벤더도 구독으로 주는 토큰량을 공개하지 않는다** — 메시지 수, 배수, "allowance" 같은 단위로만 판다.
2. 그래서 구매 결정이 **사전 검증 불가**하다. API는 토큰당 단가가 공개되지만, 구독은 **다 써봐야 크기를 아는 상품**이다.
3. 유료로 사는 건 지능이 아니라 **여유(headroom)·편의성·통합**이며, 한도에 닿으면 차단이 아니라 **조용한 모델 강등**이 일어난다.

## 2. 인용된 수치/출처 목록 (전부 2026-07-25 수집)

| 항목 | 출처 | Tier | 비고 |
|---|---|---|---|
| Plus/Go: GPT-5.5 Instant **3시간당 160메시지**, 초과 시 **Instant mini로 전환** | OpenAI Help Center | 1 | ✅ 핵심 근거 |
| Plus: GPT-5.5 Thinking **주 3,000메시지** | OpenAI Help Center | 1 | ✅ |
| Pro $200 (+ $100 저한도 티어), 한도는 **"some models have separate usage allowances"만 명시** | OpenAI Help Center | 1 | ✅ 불투명성 직접 증거 |
| Go/Plus/Pro **연간결제 없음** | OpenAI | 1 | ✅ |
| GPT-5.6 Sol = Medium/High/Extra High, **Sol Pro = Pro티어**; 한도 초과 시 GPT-5.4 Thinking mini로 폴백 | OpenAI Help Center | 1 | ✅ |
| **GPT-5.2 2026-06-12 ChatGPT에서 퇴역** → GPT-5.5로 마이그레이션 | OpenAI Help Center | 1 | ⚠️ 1차 개고 때 낡은 모델명 썼던 것 **수정 완료** |
| Claude 5시간 세션·Max 5x/20x, Google Ultra 5x/20x | claude.com/pricing, gemini.google | 1 | 배수 구조만 인용(금액 미기재) |

> **금액은 ChatGPT만 기재.** Claude/Google/Perplexity/Grok은 **특징만 정성 서술**, 금액 미기재 → 지역가·미검증 리스크 원천 제거.

## 3. 적용된 스타일 + 근거

- **jsonhouse DNA** — CAT1 기본값.
- 5단계: ① 훅(첫 문장에 "토큰량 안 밝힌다" 직답)+TL;DR → ② **팩트(벤더가 안 밝히는 것)** + ChatGPT 2요금제 비교표 → ③ **이면 분석**(지능이 아니라 용량을 판다 + 조용한 강등) → ④ 큰 그림(벤더별 특징 5종, API 경제·무료티어 광고화 링크) → ⑤ 실용(2주 테스트 7단계)+FAQ 5개.

## 4. 이면 분석 핵심 (한국어 2~3문장)

표에서 드러나는 역전이 이 글의 진짜 발견이다 — **주류 요금제(Plus)는 검증 가능한 숫자를 주는데, 10배 비싼 최고 요금제(Pro)는 산문만 준다.** 프리미엄 구매자에게 파는 것이 "특정 한도"가 아니라 "한도를 신경 쓰지 않아도 되는 상태"이기 때문이다. 게다가 한도 도달이 차단이 아니라 **mini 모델로의 조용한 강등**이라, 사용자는 "오늘 모델이 멍청해졌네"로 체감할 뿐 임계선을 넘은 줄 모른다.

## 5. 의심스러운 사실 관계 항목

**1차 개고 대비 대부분 해소**되었습니다:

| 이전 우려 | 처리 |
|---|---|
| Google USD 미확인 | ✅ **해소** — 금액 자체를 안 쓰고 "아무도 안 밝힌다"는 논지로 흡수 |
| Claude Max 20x 금액 불명 | ✅ **해소** — 금액 미기재, 배수 구조만 인용 |
| Perplexity Pro 금액 불명 | ✅ **해소** — 금액 미기재, 특징만 서술 |
| Grok Lite/Heavy 금액 불명 | ✅ **해소** — 동일 |
| (신규 발견) GPT-5.2 모델명 낡음 | ✅ **수정** — 6/12 퇴역 확인 후 GPT-5.5/5.6로 갱신, 퇴역 사실 자체를 본문에 명시 |

**남은 확인 1건**: ChatGPT Pro $200 / $100 두 티어 구조는 헬프센터 검색 스니펫 기반입니다(직접 fetch는 403). 발행 전 결제 화면에서 눈으로 한 번 확인해 주시면 완벽합니다.

## 6. 내부 링크 목록 + 검증 결과

| 링크 텍스트 | 대상 슬러그 | 존재 | 클러스터 |
|---|---|---|---|
| LLM API pricing, where per-token rates are published openly | `/posts/llm-api-pricing-2026/` | ✅ | CLUSTER_LLM (동일) |
| ChatGPT ads and AI citation behavior in 2026 | `/posts/chatgpt-ads-2026-aeo-reddit-citations/` | ✅ | CLUSTER_LLM (동일) |

> API 링크는 **"공개 단가 vs 비공개 할당량"** 대비 지점에 배치해 논지를 강화하는 자리에 넣었습니다.

## 7. 자동 검증(Hook) + 자가 점수

- 훅 **PASSED (ERROR 0)**. 제목 51자 / 메타 155자 / 본문 **1,879단어** / 비교표 2개 / JSON 코드블록 없음 / 내부링크 2개 / TL;DR·FAQ 5개 / 프론트매터↔데이터 JSON 5필드 일치.
- 잔여 WARN: THIN SECTIONS(FAQ 단일 문단 오탐) — 조치 불필요.
- Format A 필수 8요소: Methodology ✅ / 수집일 ✅ / Raw data ✅ / Limitations ✅(4개) / 갱신 주기 ✅ / Changelog ✅ / 정규화 비교표 ✅ / 출처 표기 ✅
- 자가 품질 점수: technical_accuracy 9.0 / structural 8.5 / practical 9.0 / data_completeness 8.5 → **가중 ≈ 8.8**

---

**요청**: 승인해 주시면 발행하겠습니다(§5의 Pro 티어 구조만 결제화면 확인 권장). 커버 이미지 `llm-subscription-guide-2026-cover.png` 필요.
