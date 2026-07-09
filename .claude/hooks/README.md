# Hooks — 자동 품질 게이트

## post-validation.sh

`_posts/*.md`, `_drafts/*.md`에 Write/Edit가 발생할 때마다 자동 실행되는
PostToolUse 훅. 설정은 `.claude/settings.json`.

### 동작 방식

- stdin으로 툴 호출 JSON을 받아 `tool_input.file_path`를 추출
- 대상이 `_posts/`/`_drafts/`의 `.md`가 아니면 조용히 통과 (exit 0)
- 검사 규칙 전체 목록: `CLAUDE.md`의 "Hook Enforcement" 섹션
  (Section A: SEO/frontmatter A1~A9, Section B: 콘텐츠 품질 B1~B7)

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
