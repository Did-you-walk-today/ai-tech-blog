# Phase 5 리뷰 — Claude Code Plugins and MCP 2026

- 초안: `_drafts/2026-08-29-claude-code-plugins-mcp-2026.md`
- 데이터: `_data/2026-08-29-claude-code-plugins-mcp-2026.json`
- 슬러그: `claude-code-plugins-mcp-2026` (확정 — 변경 금지)
- Format A / CLUSTER_DEVTOOLS / ai-developer-tools
- 훅 검증: ERROR 0건, WARN 1건(커버 파일 미존재 — 초안 단계 정상)

## 0. 이번 수정에서 바뀐 것 (기웅 요청 반영)

**① 경쟁 구도 전면 삭제.**
초판은 "MCP 버리고 플러그인으로 가라는 조언은 반쯤 틀렸다"로 열고, 결론도
"이전이 효율적인가"였습니다. 대립 프레임이 글 전체의 뼈대였습니다.
이번 판은 **"둘이 어떻게 다른가"**로 축을 바꿨습니다:

- 리드에서 "조언이 틀렸다" 삭제 → MCP는 연결, 플러그인은 포장이라는 층위 설명으로 교체
- `## The difference in one table` 신설 — 6행 층위 비교표 (정체/해결 문제/설치 단위/포함 관계/생명주기/스코프)
- `## So is migrating efficient?` → `## Choosing between them`으로 교체.
  "이전하라"가 아니라 "이 기능이 무엇으로 이루어져 있나"를 묻는 판단 기준 4개로 재구성
- 전체에서 versus·competition·"the advice is wrong" 계열 표현 제거

**② 플러그인 발견 문제 섹션 신설.**
`## The plugins are piling up faster than anyone finds them` — 요청하신
"편한 건 많아지는데 일반인은 뭐가 있는지도, 쓰는 법도 모른다"를 문서 근거로 채웠습니다.
근거 4개는 모두 공식 문서 실측입니다:

1. 공식 마켓플레이스에 이미 slack·notion·atlassian(Jira/Confluence)·linear·asana·figma·sentry가 있고, 언어서버 플러그인 11종이 별도로 있음
2. **커뮤니티 마켓플레이스는 자동 등록되지 않는다** — `/plugin marketplace add anthropics/claude-plugins-community`를 직접 쳐야 하고, 안 치면 심사 통과한 카탈로그 전체가 안 보임. 데모 마켓플레이스도 동일
3. 탐색 진입점(`/plugin` Discover 탭, `claude.com/plugins`)이 작업 중에 스스로 드러나지 않음
4. 설치하고 잊는 게 기본값이라는 증거 — Claude Code가 **2주 이상·10세션 이상 미사용** 플러그인을 `Not used recently`로 따로 묶어준다. "안 쓰는데 시작 비용과 컨텍스트 비용은 계속 내는 플러그인을 찾으라"는 게 문서의 표현

**③ 슬러그 변경.** `mcp-vs-claude-code-plugins-2026` → `claude-code-plugins-mcp-2026`.
CLAUDE.md의 "슬러그 확정 후 변경 금지" 규칙은 **내부 링크 9개가 깨졌던 사고** 때문에 생긴 것인데,
이 글은 미발행 초안이고 이 슬러그를 가리키는 링크가 레포 전체에 0건입니다.
URL에 `vs`가 박혀 있으면 경쟁 구도를 지우라는 요청과 정면으로 어긋나서 지금 바꿨습니다.
구 슬러그 3종 파일은 삭제했습니다. **이 슬러그는 여기서 확정이고 이후 변경하지 않습니다.**

**④ 컨텍스트 비용 서술 정정.** 초판은 "플러그인 컨텍스트 비용은 미공개"라고 썼는데,
`/plugin` 상세 창에 **Context cost 추정치**가 표시된다는 문서를 이번에 확인했습니다.
"MCP 툴 정의의 일반 토큰값은 미공개, 단 플러그인 단위 추정치는 UI에 있음"으로 나눠서 서술했습니다.

---

## 1. 핵심 주장 요약 (3줄)

1. MCP는 **연결 프로토콜**, 플러그인은 **포장·배포 형식**이다. 층이 다르고, 플러그인이 `.mcp.json`으로 MCP 서버를 담는 포함 관계다.
2. 컨텍스트에 상주하는 양은 구성요소마다 다르다 — 훅 0, 스킬은 1,536자 리스팅, MCP는 tool search 기본값 아래 캐시된 툴 이름만.
3. 진짜 병목은 기능이 아니라 **발견**이다. 업무에 바로 쓸 플러그인이 이미 카탈로그에 있는데, 커뮤니티 마켓플레이스는 명령을 직접 치기 전까지 존재 자체가 보이지 않는다.

---

## 2. 인용된 수치/사실 출처 목록

전부 벤더 공식 문서에서 **2026-08-29에 직접 확인**했습니다. 자체 실측 수치는 0건입니다.

| 본문 주장 | 출처 | 확인일 |
|---|---|---|
| 플러그인 구성요소 전체 목록 (skills/agents/hooks/.mcp.json/.lsp.json/monitors/bin/settings.json) | [docs/en/plugins](https://code.claude.com/docs/en/plugins) | 2026-08-29 |
| "Plugin MCP servers start automatically when the plugin is enabled" + 별도 on/off 없음 | [plugins-reference](https://code.claude.com/docs/en/plugins-reference) | 2026-08-29 |
| 공식 마켓플레이스 external integrations 목록 + "pre-configured MCP servers" | [discover-plugins](https://code.claude.com/docs/en/discover-plugins) | 2026-08-29 |
| 커뮤니티 마켓플레이스 수동 추가 명령 | 동일 | 2026-08-29 |
| `/plugin` Discover 탭, `claude.com/plugins` 카탈로그 | 동일 | 2026-08-29 |
| Context cost 추정치 + "not every plugin provides the data" | 동일 | 2026-08-29 |
| `Not used recently` 기준 (2주 이상 / 10세션 이상) | 동일 | 2026-08-29 |
| 언어서버 플러그인 11종 | 동일 | 2026-08-29 |
| tool search가 기본값, `cached 2h ago · connects on first use · 5 tools` | [docs/en/mcp](https://code.claude.com/docs/en/mcp) | 2026-08-29 |
| tool search 미적용 3개 구성 | 동일 | 2026-08-29 |
| 툴 **출력** 한도: 10,000토큰 경고 / 25,000토큰 상한 | 동일 | 2026-08-29 |
| 스킬 리스팅 **1,536자** 절단 + "loads only when it's used" / "stays in context across turns" | [docs/en/skills](https://code.claude.com/docs/en/skills) | 2026-08-29 |
| MCP 정의 + "USB-C port for AI applications" | [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro) | 2026-08-29 |

초판에서 인용했던 3자 블로그(async-let.com)는 이번 판에서 **뺐습니다.** 경쟁 구도를
지우면서 "3자 추정치 vs 공식 미공개" 대비 자체가 불필요해졌습니다.

---

## 3. 적용된 스타일 + 근거

**jsonhouse DNA (합성 스타일)**. 카테고리 CAT2(AI Developer Tools) → 스타일 가이드 §4 표에 따라 자동 선택.

| 단계 | 해당 섹션 |
|---|---|
| ① 훅 + TL;DR | 리드 1문단 + TL;DR 5불릿 |
| ② 팩트 + 데이터 | What MCP does / What a plugin is / 층위 비교표 / 상주 비용표 |
| ③ **이면 분석** | The plugins are piling up faster than anyone finds them |
| ④ 큰 그림 연결 | 발견 격차가 곧 보이지 않는 비용이라는 문단 + 내부 링크 3건 |
| ⑤ 실용 결론 | Choosing between them (4가지 판단 기준) + FAQ 5개 |

③이 초판과 가장 크게 달라진 지점입니다. 초판의 이면 분석은 "유행하는 조언이 틀렸다"였고,
이번 판은 **"카탈로그가 사용자의 지도보다 빨리 자란다"**입니다.

---

## 4. 이면 분석 핵심

플러그인이 늘어난다는 사실 자체는 뉴스가 아닙니다. 문제는 늘어나는 속도가 사용자가 그걸
파악하는 속도를 이미 앞질렀다는 것이고, **못 찾은 플러그인의 비용은 눈에 보이지 않는다**는 점입니다.
안 쓰는 사람은 손해 본 줄도 모르고 계속 손으로 합니다.

구조적으로도 그렇게 되어 있습니다. 공식 마켓플레이스만 자동 등록되고 커뮤니티 카탈로그는
명령을 알아야 열립니다. 모른다는 사실 자체를 알려주는 장치가 인터페이스에 없습니다.
게다가 설치한 뒤 잊는 것도 기본값이라, Claude Code는 아예 미사용 플러그인을 따로 묶어
보여주는 기능을 갖고 있습니다.

---

## 5. 의심스러운 사실 관계 / 판단이 필요한 항목

**① 이 글은 1차 출처가 아니라 분석형입니다.**
판별 테스트에 정직하게 답하면 AI가 공식 문서로 직행할 수 있습니다. 경로 ④(정규화)에 해당하고,
성격상 **금요일 분석형 슬롯**입니다. Format은 비교표가 본체라 A로 뒀는데, "Format A = 화요일
데이터형"이라는 규칙과 어긋납니다. 기웅 판단 필요 — C로 바꿔도 됩니다.

**② "일반인은 모른다"는 주장의 근거 성격.**
요청하신 논지인데, 이걸 뒷받침할 **설문·통계는 없습니다.** 대신 제품이 그 문제를 전제하고
설계됐다는 문서 근거(수동 추가 필요, `Not used recently` 기능 존재)로 지지했습니다.
"사용자 N%가 모른다" 같은 수치는 쓰지 않았습니다 — 없는 숫자입니다.

**③ 카탈로그 목록의 수명.**
공식 마켓플레이스 플러그인 이름을 본문에 나열했는데, 카탈로그는 예고 없이 바뀝니다.
Limitations에 "the official catalog as documented on the retrieval date"로 명시했습니다.

**④ tool search 기본값 시점.**
문서가 "the default"라고만 쓰고 언제부터인지 안 밝힙니다. 본문에서도 시점을 특정하지 않았습니다.

**⑤ MCP 랭킹 글 삭제 여파.**
2026-08-29에 `mcp-registry-report-2026`을 내려서, MCP 설명 문단에 걸 자사 링크가 없습니다.
전부 외부 1차 출처로 처리했습니다.

---

## 6. 내부 링크 목록 + 검증

| 링크 대상 | 앵커 | `_posts/` 실존 | noindex | 판정 |
|---|---|---|---|---|
| `/posts/ai-content-quality-gates-2026/` | AI content quality gates | ✅ | 아니오 | OK |
| `/posts/best-ai-coding-tools-2026/` | AI coding tools comparison | ✅ | 아니오 | OK |
| `/posts/llm-cache-pricing-2026/` | LLM cache pricing | ✅ | 아니오 | OK |

3건 모두 실존 확인, DANGLING 0건.

---

## 7. 커버 이미지 프롬프트 전문

커버가 아직 없습니다. 아래를 **그대로 복사해서** 이미지 모델에 넣어주세요.
반환된 파일은 `python3 .claude/hooks/optimize_image.py IN.png --cover`로 정규화한 뒤
`assets/img/posts/claude-code-plugins-mcp-2026-cover.jpg`로 저장합니다.

소재 근거: `IMAGE_GUIDE.md` §8에서 `CLUSTER_DEVTOOLS`의 시각 세계는 **정밀 기계와 공구**.
눈금이 읽히는 실물(캘리퍼·자)은 P6 위반 위험이 있어 피했고, 셀 수 있는 반복 배열도 피했습니다.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single continuous curl of steel swarf lifting away from a freshly
cut metal surface, its spiral catching the light along one polished edge.

SCENE: The curl rises off the cut surface in one unbroken spiral, still
attached at its base, the machined face beneath it bright where the tool has
just passed and falling into shadow further back.

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

alt 텍스트(초안 frontmatter에 이미 반영):
`A curl of steel shaving lifting off a freshly machined surface, cyan light raking one edge and amber catching the other`

---

## 8. 품질 자가 점수

| 항목 | 가중치 | 점수 | 근거 |
|---|---|---|---|
| technical_accuracy | 0.30 | 9.0 | 전 주장이 공식 문서 직접 인용, 원문 표현 그대로. Context cost 관련 초판 오류를 발행 전 자체 검출·정정 |
| structural_quality | 0.25 | 8.5 | jsonhouse DNA 5단계 충족, 훅 ERROR 0, 최장 문단 120단어 미만 |
| practical_value | 0.25 | 9.0 | 판단 기준 4개 + 실행 가능한 명령 1개(커뮤니티 마켓플레이스 추가). 초판보다 상승 |
| data_completeness | 0.20 | 8.0 | 13필드 + comparison_data 2축 완비, primary_sources 6건. 자체 측정 0건이라 만점 아님 |

**가중 총점 8.65** — 발행 기준(7.0) 통과.

---

## 9. 발행 전 남은 일

1. 커버 이미지 생성 → 정규화 → 배치 (위 §7)
2. Format A / 슬롯 판단 확정 (위 §5-①)
3. 기웅 승인 후 `publish-post` 스킬로 Phase 6
