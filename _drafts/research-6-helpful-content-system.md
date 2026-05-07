# 자료 조사 보고서 #6

**주제**: Inside Google's Helpful Content System — How It Actually Decides
**조사일**: 2026-04-27
**Cluster**: CLUSTER_AI_CONTENT_POLICY (pillar 글의 spoke #4)

---

## 핵심 발견

이 글의 차별화 포인트:

1. **HCS는 더 이상 "독립 시스템"이 아니다**
   - 흔한 오해: "다음 HCU를 기다리자"
   - 실제: 2024년 3월부터 core 알고리즘에 통합됨 (deprecated as standalone)
   - 이제는 상시 작동 — 항상 평가됨

2. **"site-level"과 "page-level"의 미묘한 균형**
   - 2022-2023: 사이트 단위 평가 (전체 사이트가 unhelpful이면 전체 강등)
   - 2024년 3월부터: 사이트 단위 + 페이지 단위 양쪽 작동
   - 시스템들이 "counterbalance" 함 — 한 시스템의 평가가 다른 시스템에 의해 상쇄될 수 있음

3. **Recovery는 즉각적이지 않다**
   - 분류기가 항상 작동하지만, "unhelpful" 라벨 제거에는 시간 필요
   - 인간 리뷰어 없음 — 알고리즘 단독 결정
   - 일부 사이트는 80~97% 트래픽 손실 후 회복 못 함

---

## 1. HCS 정확한 타임라인

| 시점 | 사건 | 효과 |
|---|---|---|
| 2022.8 | Helpful Content Update 첫 도입 | 사이트 단위 분류기 |
| 2022.12 | "Experience" Quality Rater에 추가 | E-A-T → E-E-A-T |
| 2023.9 | September 2023 HCU 대규모 강타 | 일부 사이트 80%+ 트래픽 손실 |
| 2023.9 | "written by people" 표현 가이드라인에서 삭제 | "for people"로 변경 |
| 2024.3.5 | **March 2024 Core Update — HCS를 core 알고리즘에 통합** | 독립 시스템으로 deprecated |
| 2024.3-4 | Roll-out 45일 소요 (역대 가장 긴 core update) | 다중 시스템 동시 업데이트 |
| 2024 전체 | 4개 core update + 3개 spam update | 품질 신호 강화 |
| 2025-2026 | 정기 core update에 HCS 신호 포함 | 별도 HCS 발표 없음 |

---

## 2. HCS의 작동 메커니즘

### 2-1. 핵심 구조 (March 2024 이전 vs 이후)

**이전 (Standalone System)**:
- 단일 분류기 (single classifier)
- 사이트 전체에 unhelpful 라벨 부여
- 일정 주기로 업데이트
- 추가 신호 적용 명확

**이후 (Core Integration)**:
- 단일 신호가 아님 — "variety of innovative signals and approaches"
- Site-level + Page-level 양쪽 작동
- 상시 평가 (continuous)
- 다른 core 시스템과 상호작용 (counterbalance)

### 2-2. Google 공식 발표 (March 2024)
"Our core ranking systems will now show more helpful results using a variety of innovative signals and approaches without using one signal or system to do this."

핵심: HCS는 더 이상 단일 신호 아님. 여러 신호의 조합.

### 2-3. 측정 가능한 결과
- **40-45% 감소**: 저품질/원본성 없는 콘텐츠 search 결과에서
- 출처: Google Search Central 공식 발표
- 두 수치 차이: 40%는 March 2024 직후, 45%는 누적 효과

---

## 3. Site-level vs Page-level 평가 (가장 헷갈리는 부분)

### 3-1. 이전 방식 (사이트 단위만)
- 사이트의 substantial portion이 unhelpful → 사이트 전체 demotion
- 한두 페이지 좋아도 전체 끌려 내려감
- "사이트 평판" 같은 효과

### 3-2. 현재 방식 (양쪽 작동)
**Glenn Gabe (GSQi) 분석 — 실제 사이트 추적 결과**:
- HCU(September 2023)로 80%+ 손실한 사이트들이 March 2024 Core로 추가 손실
- 한 사이트는 누적 97% 손실
- "Site-level quality algorithms"가 broad core update에서 핵심 역할
- 시스템들이 서로 강화하거나 상쇄

### 3-3. Page-level 평가 추가의 의미
- 도움 안 되는 페이지 식별 가능
- 그러나 사이트의 substantial portion이 도움 안 되면 여전히 사이트 전체 영향
- 도움 안 되는 페이지를 제거하면 다른 페이지 성능 개선 가능 (Google 공식)
- 단, 즉각적이지 않음 — 시스템이 처리하는 시간 필요

---

## 4. 분류기의 특성 (가장 중요한 미세 차이)

### 4-1. 자동화 — 인간 리뷰어 없음
- Google 공식: "There is no human reviewer involved"
- 알고리즘 단독으로 unhelpful 라벨 부여
- Manual action과 다름 (Manual action은 인간 검토 후 부과)

### 4-2. 상시 작동
- Always-on classifier
- 새 콘텐츠 + 기존 콘텐츠 모두 지속 평가
- 업데이트 시점에만 작동하는 게 아님
- "negative signal can persist after improvements"

### 4-3. Recovery 메커니즘
**Google 공식 입장**:
- Recovery 즉각적이지 않음
- 시스템이 "clear, long-term improvements"를 봐야 라벨 제거
- Unhelpful 콘텐츠 제거가 다른 페이지 성능 개선에 도움될 수 있음
- 그러나 정해진 타임라인 없음

**실제 사례 (Amsive 분석 — 약 400 사이트 추적)**:
- September 2023 HCU 피해 사이트 중 March 2024 이후 의미 있는 회복 없음
- 일부는 추가 손실 발생
- 회복은 일반적으로 다음 core update와 정렬되어 발생
- 회복 시간: 2-6개월 (substantial improvements 시)

---

## 5. HCS와 E-E-A-T의 관계

### 5-1. 공식 관계
- HCS는 E-E-A-T를 명시적으로 호출하지 않음
- 그러나 HCS 가이드라인에 E-E-A-T 언급
- **E-E-A-T는 HCS 통과의 가장 좋은 방법** (공식 권장)

### 5-2. September 2023의 미묘한 변화
- "written by people" 표현 → "for people"로 변경
- AI 콘텐츠를 직접 차별하지 않는다는 명시적 신호
- 그러나 품질 기준은 동일 (사람용이든 AI용이든)

---

## 6. 실제 Demote된 콘텐츠 패턴 (Lily Ray 분석 등)

### 6-1. 가장 큰 타격을 받은 패턴
**여행 사이트 사례 (Lily Ray의 분석)**:
- 미국 모든 도시의 "things to do" 페이지 대량 생성
- Google Maps, TripAdvisor, Yelp의 generic 정보 사용
- 원본 인사이트나 직접 경험 없음
- 인위적으로 편집된 날짜 (2024 in title이지만 실제 업데이트는 2023 이전)

**범주별 패턴**:
- **Affiliate review**: 직접 안 써본 제품 리뷰
- **Travel sites**: 가지 않은 곳 가이드
- **How-to**: 직접 안 해본 작업 설명
- **Mass topic coverage**: 사이트 전문 영역 벗어나 모든 주제 다루기

### 6-2. 위험 신호 체크리스트
**Content 차원**:
- 다른 사이트들의 정보 종합
- 직접 경험/관찰 없음
- 인위적 날짜 갱신
- 키워드 매칭 위주 작성

**Site 차원**:
- 사이트가 다루는 topic의 광범위함 (특화 부족)
- Author 정보 없음 또는 가짜
- Thin content 다수
- 광고/affiliate 비율 과다

---

## 7. Information Gain — 새 개념 (2026)

### 7-1. 의미
**Google 자체 정의는 명시 안 함, 그러나 third-party 분석에서 부상**:
- 한 페이지가 경쟁 페이지 대비 제공하는 unique value
- "Fresh, original content"를 수학적으로 점수화 가능성
- 단순히 SERP 1-10위 짜깁기는 Information Gain 낮음

### 7-2. 측정 신호 (추정)
- 다른 페이지에 없는 정보 비율
- 1차 출처 인용 vs 2차 인용
- Original research vs aggregation
- 전문가 의견의 unique 정도

### 7-3. 실용적 의미
- "10 Best AI Tools 2026" 류 글이 어려운 이유
- 같은 정보 짜깁기 → Information Gain 0
- 본인 측정/경험/의견 → Information Gain 높음

---

## 8. AI 콘텐츠와 HCS

### 8-1. Google 공식 입장 (변하지 않음)
"AI-generated content isn't automatically penalized, but it must meet Google's quality standards."

### 8-2. 2024년 실제 데이터
- AI 콘텐츠 전략 사이트들이 큰 타격
- 단, AI 도구 사용 자체가 원인 아님
- 진짜 원인: 인간 검토 부재, 원본 인사이트 결여, 1차 경험 부재

### 8-3. AI 콘텐츠가 HCS 통과하는 조건
1. **Substantial human editing**: 단순 검토 아닌 실질 편집
2. **Fact-checking**: AI 출력의 사실 관계 검증
3. **Unique insights**: AI가 만들 수 없는 개인적/전문적 시각 추가
4. **First-hand expertise**: 직접 경험 표지 명시

---

## 9. Self-Assessment Questions (Google 공식)

Google이 site owners에게 제공하는 자체 평가 질문 (가장 중요한 1차 출처):

**Content 자체 평가**:
- Does the content provide original information, reporting, research, or analysis?
- Does the content provide a substantial, complete, or comprehensive description of the topic?
- Does the content provide insightful analysis or interesting information that is beyond the obvious?
- If the content draws on other sources, does it avoid simply copying or rewriting?
- Does the headline or page title provide a descriptive, helpful summary of the content?
- Does the headline avoid being exaggerating or shocking?
- Is this the sort of page you'd want to bookmark, share, or recommend?
- Would you expect to see this content in a printed magazine, encyclopedia, or book?

**Expertise 평가**:
- Does the content present information in a way that makes you want to trust it?
- Is the content produced by someone with demonstrable, first-hand expertise?
- Does the content have any easily verified errors?
- Would you trust the information for issues relating to your money or your life?

**Presentation/Production 평가**:
- Is the content free from spelling or stylistic errors?
- Was the content produced well, or does it appear sloppy?
- Is the content mass-produced or outsourced to large numbers of creators?
- Does the content have an excessive number of ads?
- Does the content display well on mobile?

---

## 10. 1차 출처 (글에서 인용)

1. **Google Search Central — Helpful Content**: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
2. **Google Helpful Content Update FAQ**: https://developers.google.com/search/blog/2024/03/core-update-spam-policies (2024년 3월 발표)
3. **Google Search Quality Rater Guidelines**: https://services.google.com/fh/files/misc/hsw-sqrg.pdf
4. **Google AI content guidance**: https://developers.google.com/search/blog/2023/02/google-search-and-ai-content
5. **Spam policies**: https://developers.google.com/search/docs/essentials/spam-policies

---

## 11. 글에 쓸 만한 인사이트 (이면 분석)

### 인사이트 1: HCS는 "삭제"되었지만 "사라진" 게 아니다
2024년 3월 deprecated는 system이 사라진 게 아니라 core에 흡수된 것. 이제 별도 발표 없이 항상 작동. "다음 HCU"를 기다리는 사이트 owner는 평생 못 기다림. 그게 핵심.

### 인사이트 2: 시스템들의 "Counterbalance" 동학
Glenn Gabe 분석에서 가장 흥미로운 부분. core 알고리즘의 여러 시스템들이 서로 동의하거나 반대할 수 있음. 한 시스템이 "이 사이트는 helpful"이라고 평가해도 다른 시스템이 "spam"이라고 평가하면 상쇄. 단순 수학이 아닌 다중 평가 게임.

### 인사이트 3: Recovery의 비대칭성
Demote는 빠르고 immediate(다음 update 시), recovery는 느리고 incremental. 80% 잃은 사이트가 substantial improvement 후에도 회복 못 한 사례 다수. 이게 "예방이 치료보다 훨씬 중요"한 진짜 이유.

### 인사이트 4: Information Gain의 부상이 의미하는 것
Google이 직접 정의하지 않지만 산업이 이 개념을 받아들이는 중. 2026년 SEO의 새로운 게임: "검색 1-10위 짜깁기" 끝. "그들이 갖지 못한 것을 가진" 콘텐츠만 살아남음. 본인 데이터, 본인 경험, 본인 분석이 결정적.

---

## 12. FAQ 후보

1. Helpful Content Update가 이제 별도로 안 나오나요?
2. 사이트 전체가 demote되면 어떻게 회복하나요?
3. AI 콘텐츠가 HCS에 자동 demote되나요?
4. HCS와 E-E-A-T의 관계가 뭔가요?
5. Unhelpful 페이지를 삭제하면 사이트 전체가 회복되나요?
6. Information Gain이 뭔가요?
7. 회복까지 얼마나 걸리나요?

---

조사 완료. 다음 단계: Claude Code 작성 명령 프롬프트.
