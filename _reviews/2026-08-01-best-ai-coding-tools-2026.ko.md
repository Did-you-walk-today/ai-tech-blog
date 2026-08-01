# Phase 5 리뷰 리포트 — Best AI Coding Tools 2026

- **슬러그**: `best-ai-coding-tools-2026`
- **드래프트**: `_drafts/2026-07-25-best-ai-coding-tools-2026.md`
- **데이터**: `_data/2026-07-25-best-ai-coding-tools-2026.json`
- **포맷/클러스터/스타일**: Format A · CLUSTER_DEVTOOLS · jsonhouse DNA
- **1차 출처 경로**: ④ 정규화(가격·과금모델 표준화) → 매월 재검증으로 ① 시계열 축적 전환

---

## 1. 핵심 주장 요약 (3줄)

1. 2026년 AI 코딩 툴의 진짜 승부처는 벤치마크 순위가 아니라 **과금 모델**이다 — Cursor·Copilot·Windsurf 모두 사용량 기반 과금으로 전환했고, 월 정액은 이제 '바닥값'일 뿐이다.
2. "SWE-bench 점수로 툴 순위를 매기는 것"은 **범주 오류**다. SWE-bench는 모델을 측정하며, 툴은 백엔드 모델을 갈아끼우는 하네스일 뿐이다.
3. OpenAI 스스로 SWE-bench Verified 보고를 중단(감사 문제의 59.4%가 결함 테스트)했다 — 서드파티 리더보드 스크랩을 툴 순위로 쓰는 것은 정당화 불가.

## 2. 인용된 수치/벤치마크 출처 목록

| 수치 | 출처 | Tier | 검증 상태 |
|---|---|---|---|
| Opus 4.6 = 80.84%, Opus 4.1 = 74.5% (SWE-bench Verified) | Anthropic 공식 발표(2026-02) | 1 | 벤더 발표 확인 |
| GPT-5 = 74.9%, GPT-5.2 Thinking = 80% | OpenAI 발표 | 1 | 도메인 제한 검색으로 openai.com 확인 |
| 감사 문제의 **59.4%** 결함 테스트 케이스 | OpenAI "Why we no longer evaluate SWE-bench Verified" | 1 | openai.com 자체 문구 (원문 페이지는 403, 검색 스니펫으로 확인) |
| 툴 구독 가격 (Claude Code/Cursor/Copilot/Windsurf) | 각 벤더 pricing 페이지 | 1 | 2026-07-25 수집 |
| Windsurf $15→$20 인상, 2026-03-19 크레딧→쿼터 전환 | Windsurf pricing | 1 | 2026-07-25 수집 |
| 모델 API 단가(참조) | 자체 주간 스냅샷 `_data/pricing_history/2026-07-16.json` | 1 | 9일 경과(참조용, 본문 표엔 미노출) |

## 3. 적용된 스타일 + 근거

- **jsonhouse DNA (합성 스타일)** — CAT2(개발툴 비교)의 기본값.
- 5단계 구조 준수: ① 훅+TL;DR → ② 팩트+데이터(가격 비교표+Raw data 링크) → ③ **이면 분석**(툴≠모델, 과금 체제 전환) → ④ 큰 그림+연결(모델 경제·크롤러 생태계 내부링크) → ⑤ 실용 결론(선택 가이드)+FAQ.
- 영어 포스트 = 전문 분석가 톤 유지.

## 4. 이면 분석 핵심 (한국어 2~3문장)

3월 원본은 "Claude Code = SWE-bench 80.8%"처럼 **모델 점수를 툴에 귀속**시키는 치명적 오류가 있었다. 이번 재작성은 그 오류 자체를 콘텐츠의 중심 논지로 뒤집어, "툴은 하네스, 지능은 교체 가능한 모델"이라는 구조를 드러낸다. 여기에 2026년 전 벤더의 **사용량 기반 과금 전환**(에이전트 작업의 토큰 폭증이 원인)을 얹어, 독자가 "벤치마크 1등"이 아니라 "워크플로+과금+백엔드 모델"로 판단하게 만든다.

## 5. 의심스러운 사실 관계 항목 (⚠ 기웅 확인 요망)

1. **구독 가격 정확도** — 가격은 2026-07-25 벤더 페이지에서 수집했으나, WebFetch로 페이지 원문을 캡처해 첨부하진 못했습니다(일부 403/렌더링 이슈). 발행 전 아래 4개 스팟 체크 권장:
   - GitHub Copilot: Pro **$10** / Pro+ **$39** / Business $19 / Enterprise $39 (프리미엄 리퀘스트 과금)
   - Cursor: Pro **$20**(월 ~$20 사용량 포함) / Pro+ $60 / Ultra $200 / Teams $40
   - Claude Code: Max **5×=$100 / 20×=$200**, Team **$25/seat** (멀티플라이어 방식)
   - Windsurf: Pro **$20**(2026-03-19 인상), 벤더 **Cognition** 표기 — Codeium→Windsurf→Cognition 소유 이력 확인 필요
2. **Windsurf 벤더 표기** — 본문/데이터에 "Cognition"으로 적었습니다(2024년 Cognition 인수 기준). 3월 원본은 "Codeium"이었음 → 현재 브랜드 확인 요망.
3. **Opus 4.8 SWE-bench 점수** — 공식 발표 본문에 명시 수치가 노출되지 않아 **의도적으로 인용하지 않았습니다**. 4.6(80.84%)만 인용. 시스템 카드에 수치가 있으면 추후 보강 가능.
4. **GPT-5.6 Sol 코딩 SOTA(Artificial Analysis Coding Agent Index=80)** 관련 수치는 서술에서 제외했습니다(측정 지표 혼선 방지). 필요 시 별도 문장 추가 가능.

## 6. 내부 링크 목록 + 검증 결과

| 링크 텍스트 | 대상 슬러그 | 존재 여부 |
|---|---|---|
| LLM API pricing comparison for 2026 | `/posts/llm-api-pricing-2026/` | ✅ 존재 (`_posts/2026-07-17-llm-api-pricing-2026.md`) |
| AI crawler ecosystem in 2026 | `/posts/ai-crawler-ecosystem-2026/` | ✅ 존재 (`_posts/2026-07-17-ai-crawler-ecosystem-2026.md`) |

> CLUSTER_DEVTOOLS에는 아직 발행 포스트가 없어, 가장 인접한 CLUSTER_LLM/AEO 포스트로 연결했습니다. 이 포스트가 DEVTOOLS 필러 역할을 하며, 향후 Claude Code·Cursor vs Copilot·MCP 포스트가 이 글로 역링크될 예정입니다.

## 7. 자동 검증 (Hook) 결과

- **PASSED (with warnings)** — ERROR 0건.
- WARN: THIN SECTIONS(FAQ 단일 문단 답변에 대한 알려진 오탐) — 조치 불필요.
- 제목 54자 / 메타 162자 / 본문 단어수 ≈2,075 / 비교표 존재 / JSON 코드블록 없음 / data_updated 존재 / 내부링크 2개.

## 8. 8대 필수 요소 (데이터형 포스트) 체크

- [x] Methodology 섹션 (수집일·출처)
- [x] 수집 날짜 명시 (2026-07-25)
- [x] Raw-data 접근 경로 (`/data/best-ai-coding-tools-2026.json` 링크)
- [x] Limitations 섹션 (4개 명시)
- [x] 업데이트 주기 약속 (월간 재검증)
- [x] Changelog (표)
- [x] 단위 정규화 비교표 (가격/과금모델)
- [x] 출처 표기 (벤더 발표만, 애그리게이터 배제)

---

**요청**: 위 5번 스팟 체크(특히 구독 가격 4종 + Windsurf 벤더명) 확인 후 승인해 주시면 publish-post 스킬로 발행하겠습니다. 승인 전까지 `_posts/` 이동·커밋은 하지 않습니다.
