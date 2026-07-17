# Phase 5 리뷰 리포트 — llm-api-pricing-2026

- 대상: `_posts/2026-07-17-llm-api-pricing-2026.md` (W1 데이터형 슬롯, Format D, CLUSTER_LLM) — 2026-07-17 발행 승인됨
- 데이터: `_data/2026-07-17-llm-api-pricing-2026.json`
- 원천 스냅샷: `_data/pricing_history/2026-07-16.json` (커밋 완료: 21de925)
- 작성일: 2026-07-16

## 0. 기획 판별 (PRIMARY_SOURCE_GUIDE 기준)

- **경로**: ④ 정규화(6개사 39개 모델을 $/1M tokens 단일 기준으로 통일)로 시작해 → ① 시계열(주간 스냅샷 + Changelog 누적)로 진화하는 설계. 로드맵 A-3와 동일.
- **판별 테스트 통과 논리**: 현재가만 보면 AI가 공식 페이지로 건너뛸 수 있다. 그러나 (a) 6개사를 한 표에 정규화한 최신본 + (b) 가격 **변경 이력**(Changelog + 주간 스냅샷)은 공식 페이지에 존재하지 않는다. 시간이 지날수록 (b)가 해자가 된다.
- **갱신 약속**: 주 1회 (주간 스냅샷 → 표 갱신 → Changelog 기록). pricing-snapshot 스킬로 유지.
- **경쟁 우위 축**: pricepertoken 등 집계 사이트 대비 ① 공식 페이지 단독 소싱(책임 가능한 인용 단위) ② 티어드 가격·토크나이저 차이 등 각주 수준의 엄밀함 ③ 변경 이력 축적.

## 1. 핵심 주장 요약 (3줄)

1. 2026-07-16 기준 최저가 범용 API는 DeepSeek v4-flash($0.14/$0.28, 1M 컨텍스트), 플래그십 가성비는 Claude Opus 4.8($5/$25).
2. Claude Sonnet 5는 8/31까지 $2/$10 프로모션 가격이며 9/1부터 $3/$15로 50% 인상 — 시장 최초의 사전 예고형 가격 인상.
3. 스티커 가격은 더 이상 등가 비교 단위가 아니다 — 토크나이저 차이(~30%), 캐시 할인(90~98%), 티어드 장문맥 과금이 실제 청구액을 좌우한다.

## 2. 인용된 수치/출처 목록

| 수치 | 출처 | 확인일 |
|---|---|---|
| Claude 전 모델 가격, 캐시 배율, 1M 컨텍스트 표준 과금, 토크나이저 ~30% | platform.claude.com 공식 pricing | 2026-07-16 |
| GPT-5.4/5.5/5.6 계열 가격 | developers.openai.com 공식 pricing | 2026-07-16 |
| Gemini 3.5 Flash / 3.1 Pro Preview / 2.5 계열 가격, >200K 티어 | ai.google.dev 공식 pricing | 2026-07-16 |
| Grok 4.5/4.3/build 가격, >200K 티어 | docs.x.ai | 2026-07-16 |
| DeepSeek v4 가격, 캐시히트 $0.0028, 레거시 ID 7/24 폐기 | api-docs.deepseek.com | 2026-07-16 |
| Mistral 전 모델 가격 | mistral.ai/pricing/api | 2026-07-16 |

모든 수치는 오늘 수집한 `pricing_history/2026-07-16.json`과 일치. 가격 데이터 7일 규칙 충족(0일).

## 3. 적용된 스타일 + 근거

**jsonhouse DNA** (합성 스타일). CAT5(AI Data & Statistics) 데이터형 포스트 → 기본 스타일. 5단계 구조 적용: ① 훅+TL;DR ② 팩트+비교표 4개 ③ 이면 분석("The Fine Print") ④ 큰 그림("The Bigger Picture") ⑤ 실용 결론(워크로드별 추천)+FAQ.

## 4. 이면 분석 핵심 (2~3문장)

토큰 단가표가 객관적으로 보이지만 실제로는 세 가지 구조 변수가 순위를 뒤집는다: Anthropic 신형 토크나이저가 같은 텍스트에서 ~30% 더 많은 토큰을 만들어 스티커 가격 비교를 무효화하고, 가격 전쟁의 전선이 기본 단가에서 캐시 리드(90~98% 할인)로 이동했으며, 장문맥 과금이 플랫(Anthropic) vs 티어드(Google/xAI)로 갈라져 에이전트 아키텍처 설계 자체를 강제한다. 그리고 시장은 균일 하락이 아니라 프런티어 인상 + 그 이하 붕괴로 **분열** 중이다.

## 5. 의심스러운 사실 관계 (기웅 확인 요청)

1. **"시장 최초의 사전 예고형 가격 인상"** — Sonnet 5 인트로 가격 종료(9/1 $3/$15)는 공식 문서 확인. 다만 "최초" 여부는 우리의 분석적 주장이라 반례가 있을 수 있음. 필요시 "among major providers, the first we can find"로 완화 가능.
2. **Mistral Large 3 $0.50/$1.50** — API pricing 페이지 기준. 단, 같은 사이트 FAQ에는 "Mistral Large: $2/$6"라는 구식 문구가 남아 있음(구세대 Large 2 혹은 미갱신 FAQ로 추정). 교차 확인 권장.
3. **OpenAI 컨텍스트 윈도우** — 공식 pricing 페이지에 미기재라 표에서 "n/p" 처리. 별도 models 페이지에서 보강 가능하나 이번 판은 pricing 페이지 단독 소싱 원칙 유지.
4. **Gemini 모델명** — "Gemini 3.5 Flash", "Gemini 3.1 Pro Preview"는 공식 페이지 표기 그대로. 프리뷰 모델 특성상 가격 변동 가능성 높음(주간 스냅샷이 잡아줄 것).

## 6. 내부 링크 + 검증

| 링크 | 대상 존재 여부 |
|---|---|
| `/posts/chatgpt-ads-2026-aeo-reddit-citations/` | ✅ `_posts/2026-05-17-chatgpt-ads-2026-aeo-reddit-citations.md` |
| `/posts/gigo-prompts-2026-why-vague-prompts-fail/` | ✅ `_posts/2026-05-07-gigo-prompts-2026-why-vague-prompts-fail.md` |

구 초안의 미발행 링크 3개(best-llm-models-coding-2026 등)는 전부 제거함.

## 검증 결과 & 품질 자가 점수

- post-validation.sh: **ERROR 0건**, WARN 1건(THIN SECTIONS — TL;DR/FAQ/Changelog 등 구조적 리스트 섹션. 기발행 포스트들과 동일 패턴, Methodology·Bigger Picture는 보강 완료)
- 하드 리젝트 조건 전수 통과: 제목 53자+2026 포함, description 153자, 비교표 4개, JSON 코드블록 0개, canonical_url 없음, 가격 데이터 0일
- 자가 점수: technical_accuracy 8.5×0.30 + structural_quality 8.5×0.25 + practical_value 8.5×0.25 + data_completeness 8.0×0.20 = **8.4** (기준 7.0 통과)

## 미결 항목 (발행 전 처리 필요)

- 커버 이미지 `/assets/img/posts/llm-api-pricing-2026-cover.png` 미생성 — Phase 6 전에 제작 필요
- 구 초안 `_drafts/2026-03-26-llm-api-pricing-comparison-2026.md` 삭제 여부 — 승인 시 함께 정리 제안
