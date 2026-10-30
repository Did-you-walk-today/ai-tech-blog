# Phase 5 리뷰 리포트 — solo-developer-window-2026

- 대상: `_drafts/2026-10-30-solo-developer-window-2026.md` (금요일 분석형 슬롯)
- 데이터: `_data/2026-10-30-solo-developer-window-2026.json`
- 제목: Solo Developer Window 2026: Ship and Operate Before AGI (55자)
- 카테고리 / 클러스터 / 포맷: industry-analysis (CAT7 Deep Dive) / CLUSTER_DEVTOOLS / A
- 자료 수집일: 2026-10-30

## 1. 핵심 주장 요약 (3줄)

1. 지금은 구현 비용이 싸고 경력 개발자 수요도 살아 있어서, skills와 강한 모델로 결과물을 완성해 실제 서비스로 운영하기 좋은 시기예요.
2. 플랫폼은 중소 AI 서비스의 기능을 계속 흡수하고 있고, AGI가 나오면 이 흐름이 한꺼번에 일어날 수 있어요. 이 부분은 추론이라고 본문에 밝혔어요.
3. 일찍 낸다고 안전해지지는 않아요. 기능이 복제돼도 남는 매출, 고객, 쌓인 데이터를 운영으로 벌어 둬야 해요.

## 2. 인용된 수치 / 출처 목록

| 수치 | 출처 | 확인 |
|---|---|---|
| 광범위한 대체 증거 없음, 22~25세 AI 노출 직군 19% 격차, 경력직 격차 없음, 인과 추정 아님 | [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/) (2026-08-12 개정) | 원문 초록 확인 |
| 공고 약 15% 증가, 전체 7% 감소, 시니어 71%, 팬데믹 전 대비 27.5% 낮음 | [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/) | 원문 확인 |
| 2025~2035 고용 10% 증가 전망 | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) | 원문 확인 |
| record mode 2025-06-04 / 06-18 / 07-16, Meetings 플러그인 베타 | [OpenAI 릴리스 노트](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | 원문 확인, 플러그인 날짜는 5절 참고 |
| Granola $125M, 기업가치 $1.5B, Spaces·API | [Granola](https://www.granola.ai/blog/series-c) | 원문 확인 |
| Otter ARR $100M 발표(2025-12-22) | [Otter](https://otter.ai/blog/otter-ai-caps-transformational-2025-with-100m-arr-milestone-industry-first-ai-meeting-agents-and-global-enterprise-expansion) | 원문 확인 |
| Otter $320M, "knowledge layer for enterprises" | [Business Wire](https://www.businesswire.com/news/home/20261020026393/en/General-Catalyst-Backs-Otter.ais-Voice-AI-Ambitions-with-%24320M-Growth-Investment) | 원문 확인 |
| CVF는 지분이 아니라 매출 일부를 받음 | [SiliconANGLE](https://siliconangle.com/2026/10/20/otter-ai-raises-320m-in-funding-for-its-ai-meeting-assistant/) | 2차 출처 |
| Relay, Yupp, Figgs AI, Character.ai 사례 | [TechCrunch AI graveyard](https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/), [Relay 기사](https://techcrunch.com/2026/08/17/ai-automation-startup-relay-shuts-down-staff-joins-googles-chrome-team/) | TechCrunch 서술 기준, 회사 내부 사유는 미검증 |
| Huxe $4.6M, 사유 미공개, 기능 범용화 | [TechCrunch](https://techcrunch.com/2026/05/22/audio-generation-app-huxe-founded-by-former-notebooklm-developers-shuts-down/) | 2차 출처 |
| Snyk 3,984개, 13.4%, 36.82%, 악성 76개 | [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) | 원문 확인 |
| 스킬은 호스트 권한으로 실행, USENIX 98,380개 중 157개 | [OWASP AST01](https://owasp.org/www-project-agentic-skills-top-10/ast01) | OWASP 요약 기준. USENIX 논문 원문은 못 읽음 |
| 0.16% | 157 ÷ 98,380, 우리 계산 | 본문에 "by our arithmetic" 표기 |
| ARC-AGI-3 0.51% vs 100% | [ARC Prize](https://arcprize.org/blog/arc-agi-3-launch), 기존 6G/AGI 포스트 | 2026-03 출시 시점 수치 |
| 스킬 4개·475줄, new-post 커밋 6회, 스냅샷 15개, cron 중단 2026-08-03 | 이 레포 | 직접 확인 |

## 3. 적용된 스타일 + 근거

**박종훈 구조** (CAT7 Deep Dive). 회의록 경쟁, 폐업 사례, 고용 데이터, skills를 "기능 흡수"라는 하나의 흐름으로 묶는 분석 글이라 이 구조를 골랐어요.

- ① 훅: 도입 2문단 + TL;DR
- ② 원재료: 회의록 타임라인 표, 폐업·생존 비교표
- ③ 이면 분석: "The Real Story" 흡수의 작동 방식, AGI는 이 과정의 압축, 고용 데이터
- ④ 큰 그림: skills의 경제성, 공급망 위험, 토큰 비용
- ⑤ 실용 결론: 남는 자산 표, 실행 순서 5단계, 틀릴 수 있는 조건

## 4. 이면 분석 핵심

흡수가 가져가는 건 기능이지 사업 전체가 아니에요. Granola와 Otter는 고객과 자금이 있을 때 플랫폼이 들어왔기 때문에 회의록 밖으로 넓힐 여유가 있었어요. 그래서 "빨리 내라"의 진짜 이유는 AGI 시점 예측이 아니라, 흡수가 오기 전에 옮겨 갈 여유를 벌어 두는 데 있어요.

## 5. 의심스러운 사실 관계 / 기웅 판단 필요

- **"OpenAI 때문에 폐업" 주장은 쓰지 않았어요.** 처음 의도보다 약한 표현이에요. 확인된 7건 중 회사가 플랫폼을 원인으로 직접 밝힌 사례는 0건이에요. TechCrunch가 연결 지은 사례가 Relay, Huxe 2건이고요. 더 강한 사례를 찾으면 넣을 수 있어요.
- **올트먼 "황금기" 발언은 뺐어요.** 원문을 찾지 못했어요. Fortune에서 확인된 "1인 10억 달러 회사 내기" 발언만 썼고, 토큰을 파는 회사의 CEO라는 점도 밝혔어요.
- **이전 대화의 BLS 수치 정정:** 대화에서 말한 2024~2034년 15%는 2차 요약이었어요. 현재 BLS 원문은 2025~2035년 10%이고, 본문에는 이 수치를 썼어요.
- **Meetings 플러그인 출시일:** 릴리스 노트는 9월 29일 항목, Inc.는 10월 6일로 읽혀요. 본문 Methodology에 불일치를 그대로 적었어요.
- **Relay 종료 일정:** TechCrunch는 유료 사용자 종료일을 9월 14일로 썼지만, Relay 문서는 날짜가 반대로 적혀 있다는 2차 보도가 있어요. 표는 TechCrunch 기준이에요.
- **Relay 사유:** "회사가 사유를 밝히지 않았다"는 우리가 읽은 보도 범위 안에서의 말이에요. relay.app 공지 원문은 못 읽었어요.
- **ARC-AGI-3 점수는 3월 모델 기준이에요.** 이후 모델의 점수는 확인하지 않았고, 본문에 그 한계를 적었어요.
- **skills 효과:** 생산성 향상 수치와 GitHub의 skills 수, 증가 속도는 측정하지 못했어요. 본문에 그대로 밝혔어요.
- **공개 범위 판단이 필요해요:** 비용 때문에 파이프라인을 껐다는 내용, 스킬 규모, 스타일 가이드를 비공개로 둔다는 내용을 썼어요. 매출과 gigworkertax.net은 넣지 않았어요.
- **표의 제목:** "남는 자산" 표는 측정치가 아니라 우리 판단이고, 헤더에 `jsonhouse judgment`로 표시했어요.
- **1차 출처 테스트:** 금요일 분석형이라 필수는 아니에요. 고유 기여는 "회사가 밝힌 사유"와 "언론의 해석"을 분리한 표 정도이고, 표본은 작아요.

## 6. 내부 링크 목록 + 검증 결과

| 링크 | 존재 |
|---|---|
| /posts/6g-agi-convergence-2026/ | ✅ `_posts/2026-08-21-6g-agi-convergence-2026.md` |
| /posts/claude-code-plugins-mcp-2026/ | ✅ `_posts/2026-08-29-claude-code-plugins-mcp-2026.md` |
| /posts/llm-api-pricing-2026/ | ✅ `_posts/2026-07-17-llm-api-pricing-2026.md` |
| /posts/ai-content-quality-gates-2026/ | ✅ `_posts/2026-08-06-ai-content-quality-gates-2026.md` |

아직 이 글로 들어오는 내부 링크는 없어요. 발행 후 `best-ai-coding-tools-2026`에서 연결하면 고아 경고를 없앨 수 있어요.

## 7. 커버 이미지 프롬프트 전문

CLUSTER_DEVTOOLS 소재 풀(정밀 기계와 공구)에서 골랐어요. 기존 커버의 선반 절삭 원통, 강철 칩과 겹치지 않게 **황동 기어 하나**로 했어요. 눈금이 없고 피사체도 하나라 값으로 읽힐 요소가 없어요.

- 가로세로비: 16:9
- 저장 경로: `assets/img/posts/solo-developer-window-2026-cover-raw.png`
- 웹앱의 이미지 생성 모델로 만들어 주세요. 코드로 그리면 안 돼요.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single solid brass gear, about the size of a large coin, with crisp
machined teeth and a plain central bore, unmounted and free of any markings.

SCENE: The gear rests flat on a dark machined steel plate, slightly tilted on
a small burr, its teeth catching the light while its far side falls into shadow.

COMPOSITION: Wide horizontal establishing shot. One dominant subject placed on
the left or right third, not dead center. Clear foreground-to-background
separation with real depth. Keep the outer 8% of the top and bottom edges free
of critical detail — the frame is cropped to 1.91:1 afterwards.

STYLE: High-end technical magazine cover art. Photographic realism with an
editorial, restrained mood. Tactile real-world materials with visible surface
texture — machined metal, glass, stone, paper, fabric. Shallow depth of field.
Single subject, generous empty space, quiet and precise rather than busy.

LIGHTING & COLOR: Deep navy base environment (#0F172A). Cool cyan key light
(#38BDF8) raking from one side; warm amber rim light (#F59E0B) from the
opposite edge. Strong directional light with soft falloff. No flat ambient
fill, no uniform studio lighting.

AVOID: text, letters, numbers, captions, watermarks, logos, brand marks,
charts, graphs, axes, bars, gauges, readable scales or dials, UI screenshots,
app windows, code editors, robots, humanoids, androids, human faces, hands,
brains, glowing orbs, circuit-board motifs, holographic HUD overlays, neon
cyberpunk cliché, stock-photo business people, collage, split panels, grids of
thumbnails, borders, frames, vignette.

ASPECT RATIO: 2048x1152

MUST KEEP: Exactly one subject. Consistent light direction across the whole
frame. Large areas of unbroken dark background. Nothing that could be read as
a measurement.
```

## 8. 검증 결과

- 제목 55자, description 155자
- 본문 약 2,200단어, 품질 자가 점수 7.9 (정확성 8.0 / 구조 8.5 / 실용 8.0 / 데이터 7.0)
- post-validation 훅: PASSED. 남은 경고는 커버 파일 없음 1건이에요.
- geo_validation: `[ok] draft 2026-10-30-solo-developer-window-2026`, 이 글의 오류 0건
- 깨진 내부 링크 없음

## 9. 다음 단계

1. 기웅 검토 후 승인 또는 수정 지시
2. 커버 생성(7절) → 반입·정규화
3. 승인 후 `publish-post` 스킬로 발행
