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

Codex 산출 이미지를 규격에 맞게 정규화. **Pillow 필요** (훅이 아니라 수동 도구).

```bash
python3 .claude/hooks/optimize_image.py IN.png --cover    # 1200x630 PNG, ≤200KB
python3 .claude/hooks/optimize_image.py IN.png --figure   # WebP, ≤1600px, ≤150KB
```

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
