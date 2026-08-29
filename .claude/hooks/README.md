# Hooks — 자동 품질 게이트

## post-validation.sh

`_posts/*.md`, `_drafts/*.md`에 Write/Edit가 발생할 때마다 자동 실행되는
PostToolUse 훅. 설정은 `.claude/settings.json`.

### 동작 방식

- stdin으로 툴 호출 JSON을 받아 `tool_input.file_path`를 추출
- 대상이 `_posts/`/`_drafts/`의 `.md`가 아니면 조용히 통과 (exit 0)
- 검사 규칙 전체 목록: `CLAUDE.md`의 "Hook Enforcement" 섹션
  (Section A: SEO/frontmatter A1~A9, Section B: 콘텐츠 품질 B1~B8,
   Section C: 이미지 C1~C10)

### B7/B8 설계 노트 (2026-07-25 개정)

B7은 원래 "섹션당 3줄 미만"이었는데, 마크다운 문단은 몇 문장이든 한 줄이라
**잘 쓴 FAQ 답변이 걸리고 337단어짜리 벽글은 통과**했다. `best-llm-2026` 한 편에서
오탐 7건이 나와 경고 자체가 무시되는 상태였다.

- B7: 줄 수 → **산문 단어 수 40단어** 기준. FAQ 답변(H3), TL;DR, changelog,
  하위 소제목만 담는 컨테이너 제목은 제외
- B8: 신설. **개별 문단 120단어 초과** 시 경고. 이 블로그 문단 426개 실측에서
  중앙값 53w, 95분위 112w — 120w는 상위 3%에 해당

개정 후 12개 포스트 전체에서 오탐 0건, 실제 지적 4건.

## image_validation.py

`post-validation.sh`의 Section C가 호출하는 이미지 검사기.
`ERROR:` / `WARN:` 한 줄 프로토콜로 결과를 넘겨주면 호출 측이 병합한다.
규칙 근거는 `IMAGE_GUIDE.md`.

- `_drafts/`에서는 모든 ERROR를 WARN으로 강등 (초안 시점엔 이미지가 없는 게 정상)
- Pillow 등 외부 의존성 없음 — PNG/WebP 헤더를 직접 파싱한다
- 레포 전체 현황: `python3 .claude/hooks/image_validation.py --report`
  (`_posts/`에 ERROR가 하나라도 있으면 exit 1)

## optimize_image.py

기웅이 생성해 반입한 이미지를 규격에 맞게 정규화. **Pillow 필요** (훅이 아니라 수동 도구).

```bash
python3 .claude/hooks/optimize_image.py RAW.png --cover -o assets/img/posts/{slug}-cover.jpg
python3 .claude/hooks/optimize_image.py IN.png --figure   # WebP, ≤1600px, ≤150KB
```

**`--cover`에는 `-o`를 반드시 준다.** 생략하면 출력 경로가 입력 파일이 되어
**원본을 덮어쓴다.** 게다가 입력이 `.png`면 PNG로 저장하려다 200KB에 맞추려고
32색까지 양자화하며, 사진형 커버는 그 시점에 밴딩으로 망가진다 — 되돌릴 원본은
이미 없다. 커버는 JPEG여야 한다 (`IMAGE_GUIDE.md` §4). 이 줄이 예전에
`--cover`만 적어둔 탓에 실제로 반입 원본 하나가 소실됐다 (2026-08-29).
작업 전에 원본을 레포 밖으로 한 벌 복사해 두는 것을 권한다.

### ERROR vs WARN

- **ERROR**: 발행 불가. 저장 직후 표시되며 반드시 수정
- **WARN**: 권고. Phase 6(발행) 전까지 해결

### 수동 실행 (파일 저장 없이 검사하고 싶을 때)

```bash
echo '{"tool_name":"Write","tool_input":{"file_path":"'$PWD'/_drafts/2026-07-14-example-2026.md"}}' \
  | bash .claude/hooks/post-validation.sh
```

### 금지 사항

- 훅을 피하려고 다른 경로에 작성 후 `mv`로 옮기는 우회 금지.
  이동 후에도 최종 파일에 훅을 수동 실행해 ERROR 0건을 확인할 것
- 훅 스크립트/설정 수정은 기웅 승인 필요 (품질 게이트 완화는 단독 결정 금지)

### 규칙을 고치고 싶다면

규칙이 잘못됐다고 판단되면 (예: 연도가 2027로 바뀌는 시점) 훅을 우회하지 말고
기웅에게 규칙 변경을 제안한다. A2(제목 연도) 규칙은 매년 갱신이 필요하다.

## citation_probe.py

**훅이 아니다.** 자동 실행되지 않으며 cron·GitHub Actions에도 등록돼 있지 않다.
손으로 부를 때만 도는 수동 계측기다 — 생성 답변(Claude web search, Perplexity)이
우리를 인용하는지 재고, 결과를 `_data/citation_history/`에 쌓는다.

### 왜 자동이 아닌가

상시 추적은 하지 않기로 했다(2026-08-26 기웅 결정). 종량 과금이 붙는 일이고,
daily 파이프라인 cron을 끈 이유와 같다. 대신 **언제든 돌릴 수 있는 상태**를
유지하는 쪽을 택했다. 그 조건이 질문 세트 고정이다 —
`_plans/citation-probes.yml`(gitignored, 백업 jsonhouse_plan). 질문을 매번 새로
지으면 3월 결과와 8월 결과가 비교 불가능해지고, "언제든 추적 가능"은 말뿐이 된다.

### 실행

```bash
# 항상 여기서 시작 — 호출 없이 계획과 견적만
python3 .claude/hooks/citation_probe.py --dry-run

# 실제 실행 (core 7개 × 2회 × 2엔진 ≈ $2)
ANTHROPIC_API_KEY=... PERPLEXITY_API_KEY=... \
  python3 .claude/hooks/citation_probe.py

# 싸게 한 엔진만
python3 .claude/hooks/citation_probe.py --engines claude --model claude-haiku-4-5
```

`--dry-run` 없이 부르면 견적을 보여주고 확인을 받는다. 비대화형에서는 `--yes`가
없으면 실행을 거부한다 — 스크립트가 실수로 크론에 걸렸을 때 조용히 과금되는 것을
막는 안전장치다.

### 세 가지를 따로 판정한다

| 판정 | 뜻 | 처방 |
|---|---|---|
| `retrieved` | 검색 결과에 우리가 있었나 | False → 발견가능성 문제 |
| `cited` | 인용 목록에 우리가 있나 | retrieved만 True → 콘텐츠 문제 |
| `uncredited_use` | 본문에 우리 고유 수치가 있는데 인용엔 우리가 없음 | attribution 위반 (DATA_POLICY §3) |

뭉뚱그리면 처방이 안 나온다. "아예 안 걸림"과 "걸렸는데 안 뽑힘"은 정반대 대응을
요구한다. `retrieved: null`은 '측정 안 됨'이고 `false`(검색 안 됨)와 다르다 —
Perplexity가 `search_results`를 안 주는 경우가 있어서다.

### 이 데이터로 하면 안 되는 것

**불규칙 표본은 시계열이 아니다.** LLM은 비결정적이라 같은 질문도 실행마다 답이
갈리고, 실행 간격까지 불규칙하면 추세와 잡음을 가를 수 없다. 이 데이터로
"인용률이 올랐다"를 발행하지 않는다. 용도는 계측기 생존 확인과 시점 스팟체크뿐이며,
결과 파일의 `sampling: "ad_hoc"` 필드가 그 사실을 데이터 안에 박아둔다.
`pricing_history`/`mcp_registry_history`와 달리 **한 번 걸렀다고 손실이 나지 않는다.**

### 결과 파일에 질문 전문이 없는 이유

`_data/citation_history/`는 공개 레포에 들어가고 `_plans/`는 아니다. 결과에
`probe_id`만 남겨 계측 기준이 새지 않게 한다.
