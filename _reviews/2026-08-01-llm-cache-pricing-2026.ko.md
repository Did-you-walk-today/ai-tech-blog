# Phase 5 리뷰 리포트 — LLM Cache Pricing 2026

- **슬러그**: `llm-cache-pricing-2026`
- **파일**: `_drafts/2026-07-28-llm-cache-pricing-2026.md` / `_data/2026-07-28-llm-cache-pricing-2026.json`
- **Format / Cluster / Category**: D / CLUSTER_LLM / CAT5 (ai-data-statistics)
- **data_updated**: 2026-07-28
- **분량**: 본문 2,179단어 (표 제외) · 문단 중앙값 48단어

---

## 1. 핵심 주장 요약 (3줄)

1. 캐시 할인율은 90%로 수렴했지만(Anthropic·OpenAI·Google), **공시 수준은 전혀 수렴하지 않았다** — 6개사 중 4개사가 TTL을 공개하지 않고 Mistral은 모델별 캐시 가격 자체가 없다.
2. **캐시 적중률 84% 부근에서 최저가 모델이 뒤바뀐다.** 그 아래에서는 Gemini 2.5 Flash-Lite, 위에서는 DeepSeek v4-flash가 싸다. 서로 무관한 세 쌍이 83.3~84.7% 좁은 구간에서 모두 역전된다.
3. 캐시 *쓰기* 과금이 번지고 있다 — OpenAI가 GPT-5.6부터 1.25배를 매기기 시작했다. 다만 2회만 재사용해도 손익분기를 넘겨서, 쓰기 비용은 에이전트에겐 무의미하고 **일회성 프롬프트에만 실질 손해**다.

## 2. 인용된 수치 / 출처 목록

### 우리가 1차 출처인 수치 (jsonhouse 원 계산)

| 수치 | 산출 근거 |
|---|---|
| 실효 입력가 공식 `base×(1−h) + cache×h` | 자체 정의. 본문 Methodology에 공개 |
| 실효가 표 14개 모델 × 4개 적중률 | 2026-07-28 스냅샷 가격으로 계산 |
| 교차점 84.7% / 83.7% / 83.3% | `h* = (i₂−i₁) / ((i₂−c₂)−(i₁−c₁))` 로 산출 |
| 손익분기 N≥2 (1.25배) / N≥3 (2배) | 자체 계산. Anthropic 공식 문서의 "1회 읽기 후 이득 / 2회 읽기 후 이득" 서술과 일치해 교차 검증됨 |
| 50K 프롬프트 1,000회 = $100.00 → $10.12 (89.9% 절감) | 자체 계산 |

### 외부 인용 수치 (전부 2026-07-28 확인)

| 수치 | 출처 |
|---|---|
| 모델별 base input / cache read 가격 | 6개사 공식 pricing 페이지 (`_data/pricing_history/2026-07-28.json`와 동일 수집분) |
| Anthropic 쓰기 1.25배(5분) / 2배(1시간), 저장료 없음 | platform.claude.com 가격 페이지 |
| Anthropic 최소 캐시 길이 512~4,096 토큰 (모델별) | platform.claude.com prompt caching 문서 |
| OpenAI GPT-5.6+ 쓰기 1.25배, 이전 모델 무료 | developers.openai.com prompt caching 가이드 |
| OpenAI 자동 캐싱 1,024 토큰 이상, TTL 30분 이상 | 동일 |
| OpenAI 옵트아웃 `prompt_cache_options.mode: explicit` | 동일 |
| Google 저장료 $1.00~$4.50 / 1M토큰 / 시간 | ai.google.dev 가격 페이지 |
| Google 암묵 캐싱 기본 활성, 최소 2,048~4,096 토큰 | ai.google.dev caching 문서 |
| DeepSeek 자동 캐싱, TTL "수 시간~수 일, 보장 없음" | api-docs.deepseek.com kv_cache 가이드 |
| Mistral "-90% on input token" 문구 | mistral.ai/pricing/api |

## 3. 적용된 스타일 + 근거

**jsonhouse DNA (합성 스타일, 데이터 강화)**

STYLE_GUIDE 스타일 선택표에서 **CAT5(데이터/통계) → 합성 스타일(데이터 강화)** 로 지정돼 있습니다. 5단계 구조를 그대로 따랐습니다.

| 단계 | 본문 대응 |
|---|---|
| ① 훅 + TL;DR | 도입 2문단 + TL;DR 5불릿 |
| ② 팩트 + 데이터 | Methodology / 실효가 표 / 공시 매트릭스 |
| ③ **이면 분석** | "The Deep Analysis: Three Things This Table Says" 3개 주장 |
| ④ 큰 그림 + 연결 | "The Bigger Picture" — 에이전트 경제학, 내부 링크 2개 |
| ⑤ 실용 결론 + FAQ | 워크로드별 추천 5종 + FAQ 5문항 |

PRIMARY_SOURCE_GUIDE 필수 8요소도 전부 포함했습니다 (Methodology, 수집 시점, Raw data 콜아웃, Limitations, 갱신 약속, Changelog, 단위 통일 비교표, 출처 표기).

**1차 출처 판별 테스트**: 통과. 경로 ④(정규화) + 자체 계산. AI가 원출처로 가면 6개 페이지를 각각 읽고 서로 다른 단위(배수 / 절대값 / 시간당 저장료 / 마케팅 문구)를 손으로 맞춰야 하고, Mistral 자리에는 답이 아예 없습니다. 실효가·교차점·손익분기는 원출처 어디에도 존재하지 않습니다.

## 4. 이면 분석 핵심

세 곳의 추론 스택이 캐시 서빙 원가가 서로 다를 텐데도 **정확히 동일한 0.1배**에 도달했다는 건, 이 숫자가 원가를 반영하길 멈추고 시장 기대치가 됐다는 뜻입니다. 아무도 먼저 깰 수 없는 가격이 됐습니다. 더 흥미로운 건 쓰기 과금이 **캐싱이 자동화된 시점에 정확히 맞춰 등장했다**는 점입니다 — Anthropic은 원래 "요청해야 캐싱, 쓰면 과금"이었고, OpenAI는 "자동 캐싱, 쓰기 무료"였는데 GPT-5.6에서 자동은 유지한 채 과금만 도입했습니다. 그 조합이 만드는 사각지대(재사용 안 하는 긴 프롬프트도 1.25배를 무는가)를 공식 문서가 해소하지 않는다는 것 자체가 이 포스트의 발견입니다.

## 5. 의심스러운 사실 관계 / 확인 요망 항목

정확성 위험이 있는 항목을 전부 열거합니다. **본문에서는 모두 "미공개"로 표기했고 추정치로 메우지 않았습니다.**

| # | 항목 | 처리 방식 | 기웅 확인 요망 |
|---|---|---|---|
| 1 | OpenAI가 재사용 안 된 프롬프트에도 쓰기 1.25배를 청구하는가 | 문서가 "may cache"라고만 하고 명시하지 않음. **미해결로 서술**하고 옵트아웃 존재만 사실로 기재 | 이 서술 수위가 적절한지 |
| 2 | Mistral 캐시 실효가 | 모델별 가격 미공개. 표 셀을 비우고, "-90% 적용 시 $0.15" 는 **추론이라고 명시**한 각주로만 언급 | 각주까지도 뺄지 여부 |
| 3 | xAI 쓰기/저장료/TTL | 전부 미공개. 워크로드 예시에서 "쓰기 무료 가정"이라고 라벨을 붙였으나, **본문 표에는 예시를 싣지 않음** | 가정 기반 수치를 본문에서 완전히 뺀 판단이 맞는지 |
| 4 | Grok 4.5 캐시 인하 시점 | 스냅샷이 07-16 / 07-28 두 개뿐이라 12일 중 언제인지 특정 불가. 초고의 "this week"를 **"between our 2026-07-16 and 2026-07-28 snapshots"로 수정**함 | — (수정 완료) |
| 5 | 적중률 h는 측정값이 아닌 입력 파라미터 | Limitations에 명시. 실측은 별도 실험 주제로 예고 | 갱신 약속으로 읽힐 소지가 있는지 |
| 6 | Anthropic 최소 캐시 길이 512~4,096 | 공식 문서 수치 그대로. 다만 모델별 편차가 커서 오탈 위험 | 표기값 재확인 권장 |

**같은 건으로 발행 포스트 1건도 수정했습니다** — `llm-api-pricing-2026`의 "this week" 표현을 동일하게 고쳤습니다 (아직 미배포).

## 6. 내부 링크 검증

| 링크 | 존재 여부 | 위치 |
|---|---|---|
| `/posts/llm-api-pricing-2026/` | ✅ `_posts/2026-07-17-llm-api-pricing-2026.md` | Methodology, 교차점 섹션, Bigger Picture, Related |
| `/posts/best-llm-2026/` | ✅ `_posts/2026-07-25-best-llm-2026.md` | Bigger Picture, Related |
| `/posts/llm-subscription-guide-2026/` | ✅ `_posts/2026-07-25-llm-subscription-guide-2026.md` | Related |

전부 발행된 슬러그이며 미발행 글 링크는 없습니다. 동일 클러스터(CLUSTER_LLM) 내 링크 3종으로 하우스 룰(2~3개)을 충족합니다.

## 7. 검증 결과

| 항목 | 결과 |
|---|---|
| post-validation 훅 | ERROR 0건 / WARN 1건 (커버 이미지 미존재 — 초안 단계 정상) |
| title | 53자, "2026" 포함, 핵심 키워드 앞 3단어 |
| description | 156자 (허용 140~165) |
| 본문 단어수 | 2,179 (기준 600) |
| 문단 최장 | 103단어 (기준 120) · 중앙값 48단어 |
| 비교표 | 5개 · JSON 코드블록 0개 |
| FAQ | frontmatter 5문항 + 본문 5개 헤딩 |
| 데이터 파일 | key_facts 12 / faq_summary 5 / primary_sources 11 / comparison_data 14행 / numerical_data 6지표 |

**자가 품질 점수: 8.1 / 10**

- technical_accuracy 8.5 × 0.30 = 2.55 — 전 수치 공식 출처 + 자체 계산은 공식 문서와 교차 검증
- structural_quality 8.0 × 0.25 = 2.00 — 5단계 구조 + 필수 8요소 충족
- practical_value 8.0 × 0.25 = 2.00 — 적중률 구간별 의사결정표 제공
- data_completeness 7.5 × 0.20 = 1.50 — Mistral 공백, 적중률 실측 부재가 감점

## 8. 남은 작업

1. **커버 이미지 미제작** — `post-images` 스킬 필요. 발행 전 필수
2. 발행 시 `_drafts/` → `_posts/` 이동은 `publish-post` 스킬로 (승인 후)
3. 가격 데이터 7일 규칙상 **2026-08-04까지 발행하지 않으면 재수집 필요**

---

## 참고: 작업 중 발견한 문서 불일치

`new-post` 스킬 Step 6.5가 커버 경로를 `{slug}-cover.png`로 안내하는데, `IMAGE_GUIDE.md:143`과 실제 발행 포스트 전부가 `.jpg`를 씁니다. 초안은 `.jpg`로 작성했습니다. 스킬 문서 쪽이 낡은 것으로 보이니 수정이 필요합니다.
