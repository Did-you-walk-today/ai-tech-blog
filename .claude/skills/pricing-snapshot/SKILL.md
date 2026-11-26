---
name: pricing-snapshot
description: 매주 월요일 LLM API 가격 스냅샷을 _data/pricing_history/YYYY-MM-DD.json에 적재하는 워크플로. 시계열 데이터 해자의 핵심 — 한 주라도 놓치면 복구 불가. "가격 스냅샷", "pricing snapshot", "가격 데이터 갱신" 요청 시 사용.
---

# pricing-snapshot — 주간 가격 스냅샷

## 원칙

- 이 시계열은 Phase 3(에이전트 과금)의 핵심 자산이다. 경쟁자가 베낄 수 없는 유일한 데이터.
- **소급 생성 금지.** 파일명 날짜 = 실제 수집일. 놓친 주는 놓친 대로 둔다 (공백도 데이터).
- `_data/pricing_history/`는 하위 디렉터리라 data_publisher 플러그인이 공개하지
  않는다 — 의도된 비공개. 원본 시계열은 자산으로 보관하고, 포스트에는 가공본만 노출.

## Step 1 — 수집

공식 가격 페이지에서만 수집한다 (집계 사이트는 교차 검증용):

- OpenAI: platform.openai.com/docs/pricing
- Anthropic: docs.anthropic.com (pricing)
- Google: ai.google.dev/pricing (Gemini)
- 기타 대상은 `SOURCES.md` 참조 (Mistral, DeepSeek, xAI 등)

모델별 필수 기록 항목: `input_per_1m`, `output_per_1m`, `cache_read_per_1m`(있으면), `context_window`, `source_url`, `retrieved_at`(ISO 8601).
공식 가격 페이지에 명시된 경우 함께 분리해 적는 선택 구조화 항목(복합 요금 계산용, 과거 스냅샷 소급 수정 금지):
- `cache_write_5m_per_1m`, `cache_write_1h_per_1m`, `min_cache_tokens`
- `long_context_threshold`, `long_context_input_multiplier`, `long_context_output_multiplier`
- `regional_multiplier`, `offpeak_multiplier`, `tokenizer_inflation_factor`
- `retirement_date` (YYYY-MM-DD) — 벤더가 공식 발표한 모델 종료일
- `scheduled_price_change` — 공식 발표된 단가 변경 예정. `{effective_date, new_input_per_1m, new_output_per_1m, source_url}`. `source_url`은 발표 원문(가격 페이지가 아니면 공지·changelog)

종료·인상 예고는 날짜로 조회할 수 있어야 쓸모가 있다. 공식 원문에 날짜가 있을 때만 적고, `note`에만 남기지 않는다. 날짜가 지난 예고는 다음 스냅샷에서 뺀다.

## Step 2 — 파일 작성

`_data/pricing_history/YYYY-MM-DD.json`:

```json
{
  "snapshot_date": "2026-07-13",
  "models": [
    {
      "provider": "anthropic",
      "model": "claude-sonnet-5",
      "input_per_1m": 2.0,
      "output_per_1m": 10.0,
      "cache_read_per_1m": 0.2,
      "cache_write_5m_per_1m": 2.5,
      "cache_write_1h_per_1m": 4.0,
      "min_cache_tokens": 1024,
      "regional_multiplier": 1.1,
      "tokenizer_inflation_factor": 1.3,
      "context_window": 200000,
      "source_url": "https://docs.anthropic.com/...",
      "retrieved_at": "2026-07-13T09:00:00Z"
    }
  ]
}
```

## Step 3 — 전주 대비 비교

- 직전 스냅샷과 diff: 신규 모델 / 삭제 모델 / 가격 변동률 산출
- **±10% 이상 변동 또는 신규·삭제 모델 발견 → 커밋 전에 한국어로 보고**하고
  관련 포스트 갱신 여부를 확인받는다
- 변동이 그 미만이면 바로 커밋: `chore: weekly pricing snapshot YYYY-MM-DD`

## Step 3.5 — agents.jsonhouse.com 적재

커밋·푸시가 끝난 **뒤에만** 한다. 가격 계산(`/compare`)과 변경 경보(`/alerts`)가 이 데이터를 쓴다.

- 로컬 `jsonhouse-workers` 레포의 `agents/`에서 `npm run sync:remote`
- 스크립트는 블로그 레포 **HEAD에 커밋된 스냅샷만** 읽는다. 확인 대기로 커밋하지 않은 주는 자동으로 빠지고, 기웅이 커밋한 뒤 같은 명령을 다시 실행하면 들어간다
- 여러 번 실행해도 안전하다 (경보는 처음 적재된 것만 남는다)
- 실패해도 스냅샷 커밋은 되돌리지 않는다. 보고서에 실패와 오류 메시지를 적는다

## Step 4 — 연쇄 갱신 점검

가격 변동이 있으면 pricing 관련 포스트(예: llm-api-pricing-2026)의 비교표와
`data_updated`, 대응하는 `_data/YYYY-MM-DD-{slug}.json` 갱신이 필요한지
점검하고 다음 단계로 제안한다 (가격 데이터 7일 규칙 때문에 방치하면 Hard Reject 상태가 됨).

## Step 5 — 보고

변동 요약(신규/삭제/변동 모델 수), 커밋 여부, 다음 스냅샷 예정일을 포함한
한국어 작업 보고서 작성.
