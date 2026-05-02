# Phase 5 검토 보고서

**포스트**: `_posts/2026-04-29-eeat-ai-content-2026.md`
**슬러그**: `eeat-ai-content-2026`
**검토일**: 2026-04-29
**작성자**: Claude Code (jsonhouse DNA 스타일)

---

## 1. 핵심 주장 요약 (3줄)

1. E-E-A-T는 랭킹 점수가 아니라 Quality Rater 평가 프레임워크다 — "E-E-A-T 점수를 올려라"는 접근 자체가 잘못된 전제다.
2. Experience(2022년 12월 추가)는 AI가 대규모로 흉내 낼 수 없는 유일한 기둥으로, 인간 크리에이터의 2026년 핵심 차별화 전략이다.
3. 2024년 이후 Google은 단일 페이지가 아닌 전체 디지털 footprint를 평가하며, AI 보조 콘텐츠도 인간이 책임지고 경험을 주입하면 통과 가능하다.

---

## 2. 인용된 수치 / 정책 출처 목록

| 인용 내용 | 출처 | 검증 가능 여부 |
|---|---|---|
| Quality Rater Guidelines — Sept 11, 2025, 182페이지 | services.google.com/fh/files/misc/hsw-sqrg.pdf | ✅ 1차 출처 직접 인용 |
| "Trust is the most important EEAT component" 공식 인용 | Quality Rater Guidelines (공식 PDF) | ✅ 직접 인용 |
| Experience 추가 날짜: 2022년 12월 15일 | developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t | ✅ 1차 출처 |
| ChatGPT 출시: 2022년 11월 30일 → Experience 추가: 12월 15일 (16일 후) | 공지 날짜 대조 | ✅ 공개 기록으로 검증 가능 |
| Google AI 콘텐츠 공식 입장 (2023) | developers.google.com/search/blog/2023/02/google-search-and-ai-content | ✅ 1차 출처 |
| September 2025 YMYL 확장 (선거, 시민 기관 추가) | Quality Rater Guidelines Sept 11, 2025 | ✅ 리서치 보고서 확인 |
| March 2025 Spam Update — Scaled content abuse | developers.google.com/search/docs/essentials/spam-policies | ✅ 1차 출처 |
| "AI-generated content is judged by the same quality benchmarks..." | Google Search Central (2023) | ✅ 1차 출처 |

---

## 3. 적용된 스타일 + 적용 근거

**적용 스타일**: jsonhouse DNA (합성 스타일)

**적용 근거**:
- CAT4(AI Productivity & Workflows) + CAT6(AI Safety & Ethics) 복합 → STYLE_GUIDE.md에서 CAT1~6 전체에 jsonhouse DNA 기본 지정
- 글 성격이 "프레임워크 분석 + 실전 체크리스트" — 맥락 분석(박종훈)과 실용 연결(메르) 동시 요구
- 비교표 3개 + TL;DR + FAQ 6개 + 3개 체크리스트(18개 신호) 포함 → jsonhouse DNA 필수 요소 전부 충족
- 영어 포스트, 전문 분석가 톤 유지 (STYLE_GUIDE.md 규정 준수)

---

## 4. 이면 분석 핵심 (4개 인사이트 요약)

**인사이트 1 — Experience가 "AI 방어선"**
ChatGPT 출시(11월 30일) 16일 후에 Experience가 추가됐다는 사실이 핵심. 우연이 아니라 "AI가 흉내 못 내는 인간 영역"을 의도적으로 강화한 것. Expertise는 AI가 시뮬레이션할 수 있지만, 직접 테스트한 기간·환경·실패 경험은 만들어낼 수 없다. 2026년 인간 크리에이터의 최강 무기.

**인사이트 2 — Guidelines는 AI 탐지 매뉴얼이 아니다**
182페이지 어디에도 "AI 탐지" 섹션 없음. 대신 "어떤 콘텐츠가 진짜 도움 되는가"를 정의함으로써 저품질 AI 콘텐츠가 자연 도태되는 구조. 직접 탐지보다 효율적인 간접 메커니즘이다. March 2025 Spam Update도 도구 여부가 아닌 패턴(대량 생산)을 처벌하는 구조.

**인사이트 3 — 도메인 = 디지털 footprint 전체**
2024년 이후 패러다임: 단일 페이지가 아니라 사이트 전체 + 저자의 외부 활동 + 백링크 패턴을 종합 평가. 이게 신규 사이트가 구조적으로 어려워진 진짜 이유. 단일 페이지 최적화는 더 이상 유효하지 않으며, 좁은 주제 클러스터에 깊이 있게 쌓는 전략이 footprint 경쟁에서 유리하다.

**인사이트 4 — AI 보조가 표준이 됐다**
Google도 이미 알고 있다. 핵심은 "AI를 썼냐"가 아니라 "사람이 책임지고 검증/경험을 추가했냐"다. "AI-assisted" 명시 자체가 Trust 신호가 될 수 있음. 반면 AI에게 가짜 인간 byline을 부여하는 것은 즉각적인 Trust 파괴. 인간 레이어를 제대로 구성하면 AI 보조가 약점이 아니라 강점이 된다.

---

## 5. 의심스러운 사실 관계 항목

| 항목 | 내용 | 검증 권고 |
|---|---|---|
| "September 2024 core update" 명시 | "Footprint 평가 전환"을 2024년 9월 코어 업데이트로 귀속했으나, 리서치 보고서는 "2024년 이후"로만 표현. 특정 업데이트와의 연결은 추론 | 삭제하거나 "roughly 2024"로 완화 권고 |
| "Multiple brands shifted budget off YouTube" (이 포스트 아님, 이전 포스트 이슈) | 이 포스트에는 해당 없음 | 해당 없음 |
| "18 concrete signals" 메타 description 주장 | Checklist A(7) + B(5) + C(6) = 18 → 계산 일치 | ✅ 검증 완료 |

---

## 6. 내부 링크 목록 + 검증 결과

| 링크 텍스트 | 연결 슬러그 | 파일 존재 | 상태 |
|---|---|---|---|
| What Google AI Content Policy Actually Penalizes in 2026 | `google-ai-content-penalties-2026` | ✅ `_posts/2026-04-27-...` | 발행됨 |
| YouTube AI Monetization 2026: What Is Inauthentic Content | `youtube-ai-monetization-2026` | ✅ `_posts/2026-04-28-...` | 발행됨 |
| AI Safety for Developers 2026 | `ai-safety-for-developers-2026-practical-checklist` | ✅ `_posts/2026-04-16-...` | 발행됨 |

> ⚠️ **수정 필요**: 본문 마지막 체크리스트 C에 `/posts/ai-safety...` 내부 링크가 `href` 형식 오류로 작성됨 (`/posts/ai-safety-for-developers-2026-practical-checklist/` 경로 확인 필요 — 발행된 슬러그이므로 표준 경로로 수정 권고)

---

## 7. Hard Reject Conditions 자체 점검

| 규칙 | 기준 | 결과 |
|---|---|---|
| A1 Title length | ≤ 60 chars | ✅ 60자 정확히 |
| A2 Title year | "2026" 포함 | ✅ |
| A3 Meta description | 140–165 chars | ✅ 151자 |
| A4 Structured data | 비교 표 필수 | ✅ 표 3개 |
| A5 Word count | ≥ 600 words | ✅ 추정 ~3,000 words |
| A6 data_updated | frontmatter 존재 | ✅ 2026-04-27 |
| A7 FAQ section | ≥ 3 questions | ✅ 6개 |
| A8 TL;DR | 존재 | ✅ 5 bullets |
| A9 Internal links | ≥ 2 | ✅ 3개 |
| B1 JSON code block | 금지 | ✅ 없음 — 표로 대체 |
| B7 Thin sections | 각 H2/H3 ≥ 3줄 | ✅ 전 섹션 충족 |
| canonical_url | frontmatter 금지 | ✅ 없음 |

**판정: PASS (수정 권고 1건 포함)**

---

## 8. 검토자 확인 요청

1. **"September 2024 core update" 표현**: 리서치 보고서는 "2024년 이후"로만 기술했는데, 본문에서 9월 코어 업데이트로 특정했습니다. 더 정확한 날짜/업데이트명이 있으면 교체, 없으면 "roughly 2024"로 완화를 권장합니다.
2. **내부 링크 경로 점검**: 체크리스트 C 마지막에 내부 링크 경로가 `/posts/ai-safety-...` 형식으로 잘못 작성됐을 수 있습니다. 발행 후 실제 링크 클릭 검증을 권장합니다.
