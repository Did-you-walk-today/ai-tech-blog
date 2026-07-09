---
name: publish-post
description: 기웅 승인이 완료된 드래프트를 발행하는 Phase 6 워크플로. 발행 전 점검 → _posts/ 이동 → 포스트+데이터 페어 커밋 → 배포 확인 → 라이브 URL 검증까지. 승인 없이는 절대 실행하지 않는다.
---

# publish-post — 발행 워크플로 (Phase 6)

## 전제 조건 (하나라도 아니면 즉시 중단)

- 기웅이 이 드래프트를 **명시적으로 승인**했는가? 애매하면 물어본다.
- `_drafts/YYYY-MM-DD-{slug}.md` 와 `_data/YYYY-MM-DD-{slug}.json` 페어가 모두 존재하는가?
- `_reviews/YYYY-MM-DD-{slug}.ko.md` 리뷰 리포트가 존재하는가?

## Step 1 — 발행 전 점검

- `CLAUDE.md` Hard Reject 조건 전체 재확인
- 가격 데이터 검증일이 7일 이내인가 — 리뷰 기간이 길어졌으면 수치 재검증
- 내부 링크 대상 슬러그가 `_posts/`에 실존하는가
- 데이터 파일의 `slug`/`title`/`description`이 frontmatter와 일치하는가
- frontmatter에 `canonical_url`이 없는가

## Step 2 — 이동 및 날짜 통일

- `git mv _drafts/YYYY-MM-DD-{slug}.md _posts/YYYY-MM-DD-{slug}.md`
- 파일명 날짜 = frontmatter `date` = 실제 발행일로 통일.
  날짜가 바뀌면 데이터 파일명도 같은 날짜로 rename (slug 본체는 불변)
- `last_modified_at`, `data_updated` 갱신
- 저장 시 훅 재검증 — ERROR 0건 확인

## Step 3 — 커밋 & 푸시

- 포스트 + 데이터 파일은 **반드시 같은 커밋**: `feat: publish {slug}`
- 커밋 메시지는 영어, conventional commits 형식
- `git push origin master`

## Step 4 — 배포 검증

- `gh run watch`로 pages-deploy 워크플로 성공 확인
- 라이브 검증 (모두 200이어야 함):
  - `https://www.jsonhouse.com/posts/{slug}/`
  - `https://www.jsonhouse.com/data/{slug}.json`
  - `/api/posts.json`에 신규 포스트 노출
  - `/data/index.json` count 증가
- 실패 시: 원인 분석 후 해결 방법 2~3가지 제시 (전역 규칙)

## Step 5 — 보고

한국어 작업 보고서 (작업 내용 / 변경된 파일 / 결과 / 다음 단계) + 발행 URL 포함.
다음 단계에는 다음 발행 슬롯(화/금)과 후보 주제를 제안한다.
