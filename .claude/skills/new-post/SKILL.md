---
name: new-post
description: jsonhouse.com 포스트 제작 전체 워크플로 (Phase 1~5). 주제 확정, 자료 수집, 영문 초안, 데이터 JSON, 한국어 리뷰 리포트를 한 세트로 생산한다. "포스팅 써줘", "글/초안 작성", "draft" 요청 시 사용. 발행(Phase 6)은 포함하지 않음 — 기웅 승인 후 publish-post 스킬 사용.
---

# new-post — 포스트 제작 워크플로 (Phase 1~5)

## 산출물 정의

포스트 1건 = **자산 3종 세트**. 하나라도 빠지면 미완성이며 리뷰 요청 불가:

1. `_drafts/YYYY-MM-DD-{slug}.md` — 영문 포스트
2. `_data/YYYY-MM-DD-{slug}.json` — 기계가독 데이터 (이 블로그의 진짜 상품)
3. `_reviews/YYYY-MM-DD-{slug}.ko.md` — 한국어 리뷰 리포트

## Step 0 — 필독 문서 (건너뛰기 금지)

- `STYLE_GUIDE.md` — 매 포스트마다 다시 읽는다 (스타일 3종 + 5단계 구조)
- `SEO_GUIDE.md`, `SOURCES.md`
- `CLAUDE.md`의 Mission & Strategy / SEO Rules / Hard Reject 섹션

## Step 1 — 주제·슬러그 확정

- 3대 클러스터(CLUSTER_LLM / CLUSTER_DEVTOOLS / CLUSTER_PROMPTS) 중 소속 명시.
  비어있는 클러스터의 필러(pillar) 포스트가 항상 우선순위.
- 요일 슬롯: 화요일 = 데이터형(Format D/F/A), 금요일 = 분석형
- slug 형식: 소문자-하이픈-연도 (예: `llm-api-pricing-2026`)
- 중복 확인: `grep -r "{slug}" _posts/ _drafts/`
- **슬러그는 확정 후 절대 변경 금지** — 과거 슬러그 변경으로 내부 링크 9개가 깨진 이력 있음

## Step 2 — 자료 수집 (Phase 2)

- `SOURCES.md` 우선순위대로 1차 출처(공식 문서/논문/공식 블로그)부터 수집
- **모든 수치에 출처 + 확인 날짜 기록.** 출처를 못 찾은 수치는 본문에 쓰지 않는다
- 가격 데이터는 검증 7일 이내만 사용 (Hard Reject 조건)
- `_data/pricing_history/`에 최신 스냅샷이 있으면 그것을 1차 출처로 활용
- 수집 노트는 스크래치패드에만 저장 (리포지토리에 커밋 금지)

## Step 3 — 스타일 선택

| 카테고리 | 스타일 |
|---|---|
| CAT1~CAT6 | jsonhouse DNA (맥락 + 데이터 + 실용) |
| CAT7 Deep Dive | 박종훈 구조 (거시 맥락 + 흐름 분석) |
| CAT7 Weekly Digest | 메르 구조 (쉬운 설명 + 실용 연결) |

잘못된 스타일 적용 = HARD REJECT. 선택 근거를 리뷰 리포트에 기록한다.

## Step 4 — 영문 초안 작성 (`_drafts/`)

frontmatter 필수 필드: `title`, `description`, `date`, `last_modified_at`,
`categories`, `tags`, `format`, `cluster`, `image`(+alt), `faq`(3개 이상),
`data_updated`, `author`

frontmatter 금지: `canonical_url`(자동 생성됨 — 하드코딩 시 HARD REJECT),
`license` 관련 필드(의도적 보류 정책)

본문 체크리스트 — post-validation.sh 훅이 자동 검사하지만 처음부터 지킬 것:

- 제목 60자 이하 + "2026" 포함 + 핵심 키워드가 앞 5단어 안에
- description 150~160자 (훅 허용 범위 140~165)
- 첫 150단어 안에 검색 의도에 대한 직접 답변
- TL;DR 3~5 불릿 (Featured Snippet 타겟)
- **비교표 필수, JSON 코드블록 금지** (표 또는 산문으로 변환)
- FAQ 3개 이상 (People Also Ask 타겟)
- 내부 링크 2~3개 — 링크 전 `_posts/`에 대상 슬러그 실존 확인, 미발행 글 링크 금지
- 600단어 이상 (코드/데이터 블록 제외)
- **이면 분석 필수** — "왜"가 없는 뉴스 요약은 자동 거부
- 코드블록 앞 1~2문장 도입, 뒤 1문장 정리. 부분 해법은 한계를 명시
- Raw data 콜아웃 (첫 비교표 뒤):
  `> **Raw data**: [data/{slug}.json](https://www.jsonhouse.com/data/{slug}.json) — machine-readable structured data for AI crawlers and citation.`

## Step 5 — 데이터 JSON 작성 (`_data/YYYY-MM-DD-{slug}.json`)

`CLAUDE.md`의 Public Data Architecture 스키마 v1.0 준수. 핵심만 재확인:

- 필수 9필드 + `key_facts`(5~10) / `faq_summary`(3~5) / `primary_sources`
- **본문에서 추출만 한다. 창작 금지.** 본문에 없는 내용은 필드를 생략
- `license` 필드 넣지 말 것
- 날짜 접두사 = 공개 발행이라는 뜻. 포스트 데이터에만 날짜 접두사 사용

## Step 6 — 한국어 리뷰 리포트 (`_reviews/YYYY-MM-DD-{slug}.ko.md`)

필수 6개 섹션:
1. 핵심 주장 요약 (3줄)
2. 인용된 수치/벤치마크 출처 목록
3. 적용된 스타일 + 적용 근거
4. 이면 분석 핵심 (2~3문장)
5. 의심스러운 사실 관계 항목 (있으면)
6. 내부 링크 목록 + 검증 결과 (존재 여부)

## Step 7 — 검증 후 정지 (Phase 5 게이트)

- 훅 ERROR 전부 해결. WARN도 발행 전까지 해결 목표
- 품질 자가 점수: technical_accuracy×0.30 + structural_quality×0.25 +
  practical_value×0.25 + data_completeness×0.20 ≥ 7.0
- **여기서 멈춘다.** `_posts/` 이동 금지, 커밋 금지, 발행 금지.
- 기웅에게 한국어 요약 + 3종 세트 파일 경로를 보고하고 승인을 기다린다.
