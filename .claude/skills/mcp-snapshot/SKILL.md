---
name: mcp-snapshot
description: 매주 월요일 MCP 레지스트리 전수 스냅샷을 _data/mcp_registry_history/에 적재하는 워크플로. 사라진 서버와 시점별 인기 지표는 소급 복원이 불가능하다. "MCP 스냅샷", "레지스트리 스냅샷", "MCP 랭킹 갱신" 요청 시 사용.
---

# mcp-snapshot — 주간 MCP 레지스트리 스냅샷

## 원칙

- 레지스트리 API는 **"지금 무엇이 있는가"만** 답한다. 히스토리 엔드포인트가 없고,
  삭제된 엔트리는 응답에서 통째로 사라진다.
- 따라서 **소급 불가한 것은 세 가지**다: ① 사라진 엔트리 ② 특정 날짜의 스타 수
  ③ 그 날짜의 레지스트리 구성(누가 몇 %를 차지했는가). 이 셋이 수집 이유다.
- `publishedAt`이 있으므로 **신규 등록 추이는 언제든 백필된다.** 신규 등록 수는
  수집의 근거가 아니다 — 착각하지 말 것.
- **소급 생성 금지.** 파일명 날짜 = 실제 수집일. 놓친 주는 놓친 대로 둔다.
  수집기는 이미 존재하는 스냅샷 파일을 덮어쓰지 않고 종료한다(의도된 동작).
- `_data/mcp_registry_history/`는 하위 디렉터리라 data_publisher가 공개하지 않는다.
  원본 시계열은 자산으로 보관하고 포스트에는 가공본만 노출한다
  ([[PRIMARY_SOURCE_GUIDE.md]] §2 데이터 파일 정합 규칙).

## Step 1 — 수집 실행

```bash
python3 .claude/hooks/mcp_registry_collect.py --repo-root "$(git rev-parse --show-toplevel)" --keep-raw
```

- 소요: 레지스트리 스윕 약 5분(220+ 페이지) + GitHub 스타 조인 약 3분(배치 160회).
- `--keep-raw`는 21MB 전수 원본을 `raw/`에 남긴다(gitignore 대상, R2 이전 전까지 로컬 보관).
- GitHub 조인을 건너뛰려면 `--no-github`. 단, 그 주의 스타 시점 데이터는 영구 소실되므로
  **API 장애 때만** 사용한다.

산출물 두 개:

| 파일 | 내용 | 커밋 |
|---|---|---|
| `_data/mcp_registry_history/YYYY-MM-DD.json` | 집계·집중도·churn·랭킹 3종 | O |
| `_data/mcp_registry_history/roster/YYYY-MM-DD.tsv.gz` | 전 엔트리 명부(스타 포함) | O |
| `_data/mcp_registry_history/raw/YYYY-MM-DD.json` | 전수 원본 21MB | X (gitignore) |

명부(roster)가 다음 주 델타 계산의 기준이다. 이것을 커밋하지 않으면 다음 주
`ranking_by_star_delta`가 `null`이 된다.

## Step 2 — 이상치 점검 (커밋 전 필수)

스냅샷 JSON에서 아래를 확인하고, 해당하면 **커밋 전에 한국어로 보고**한다:

- `churn.disappeared`가 전주 대비 총계의 1% 초과 — 레지스트리 측 대량 정리이거나
  우리 수집 실패다. `totals.servers_latest`가 함께 급감했는지 대조할 것
- `totals.repos_resolved`가 전주보다 5% 이상 감소 — GitHub 토큰 문제 의심
- `namespace_concentration.top1_share_pct`의 급변 — 대량 등록 사건
- `registrations_by_month`의 당월 값이 전월 대비 급감 — API 페이지네이션 조기 종료 의심

이상 없으면 커밋: `chore: weekly MCP registry snapshot YYYY-MM-DD`

## Step 3 — 연쇄 갱신 점검

살아있는 랭킹 포스트(`mcp-registry-report-2026`)가 발행된 뒤에는 매주:

- 본문 순위표, `data_updated`, `last_modified_at`, Changelog 한 줄 추가
- 짝 데이터 파일 `_data/YYYY-MM-DD-mcp-registry-report-2026.json`의
  `key_facts`·`data_updated` 동시 갱신 (프론트매터와 날짜 일치는 D5 검증 대상)

갱신 약속을 어기면 [[PRIMARY_SOURCE_GUIDE.md]] §2-5의 update cadence 위반이다.
못 지킬 주가 예상되면 포스트에 약속한 주기 자체를 먼저 낮춘다.

## Step 4 — 보고

한국어 작업 보고서에 포함: 총 서버 수와 전주 대비 증감, churn 3종
(신규/소멸/신규 deprecated), 상위 네임스페이스 집중도 변화, 델타 랭킹 1~5위,
커밋 여부, 다음 스냅샷 예정일.
