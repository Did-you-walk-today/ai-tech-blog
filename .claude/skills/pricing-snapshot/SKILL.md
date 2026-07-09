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

모델별 기록 항목: input/output $/1M tokens, 캐시 가격(있으면), 컨텍스트 길이.
각 항목에 `source_url`, `retrieved_at`(ISO 8601) 필수.

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

## Step 4 — 연쇄 갱신 점검

가격 변동이 있으면 pricing 관련 포스트(예: llm-api-pricing-2026)의 비교표와
`data_updated`, 대응하는 `_data/YYYY-MM-DD-{slug}.json` 갱신이 필요한지
점검하고 다음 단계로 제안한다 (가격 데이터 7일 규칙 때문에 방치하면 Hard Reject 상태가 됨).

## Step 5 — 보고

변동 요약(신규/삭제/변동 모델 수), 커밋 여부, 다음 스냅샷 예정일을 포함한
한국어 작업 보고서 작성.
