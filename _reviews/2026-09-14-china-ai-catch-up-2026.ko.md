# Phase 5 리뷰 리포트 — China AI 2026: Following the Path America Built

- **슬러그**: `china-ai-catch-up-2026`
- **발행 예정 슬롯**: 2026-09-18 (금요일, 분석형)
- **포맷 / 클러스터 / 카테고리**: A / `CLUSTER_LLM` / `industry-analysis`
- **data_updated**: 2026-09-14
- **파일 3종**
  - `_drafts/2026-09-18-china-ai-catch-up-2026.md`
  - `_data/2026-09-18-china-ai-catch-up-2026.json`
  - `_reviews/2026-09-18-china-ai-catch-up-2026.ko.md` (이 파일)

---

## 1. 핵심 주장 요약 (3줄)

1. Anthropic이 2026-09-10 보고서에서 중국 7개 랩의 Claude 증류 캠페인을 실명으로 공개했고, 최대 건(알리바바)만 3개월간 1억 5,100만 교환이다.
2. 가져간 것은 가중치가 아니라 **출력과 추론 흔적**이며, 침입은 없었다 — 정문으로 들어와 제품 그 자체를 학습해 갔다는 점에서 침해보다 고치기 어려운 문제다.
3. 중국이 이 길을 택한 이유는 능력 부족이 아니라 산술이다(BIS 규칙이 연산 상한을 규정). 다만 축을 가격과 로보틱스로 옮기면 순위가 뒤집힌다.

---

## 2. 인용된 수치·출처 목록

| 수치 | 출처 | 종류 | 확인일 |
|---|---|---|---|
| 7개 랩 실명, 2025-12~2026-08 기간, 7개 피해 영역 | Anthropic, *Countering misuse of AI: September 2026* | 1차 | 2026-09-14 |
| 알리바바 1억 5,100만+ 교환 / 일 최대 300만 / 3,500+ 계정 / Opus 4.6·4.7 → Qwen 3.5~3.7 | 동일 | 1차 | 2026-09-14 |
| Moonshot 2,300만+ / 5,380 계정 / 10일간 30만 요청 relay | 동일 | 1차 | 2026-09-14 |
| DeepSeek 1,210만+ (7월 14일간) | 동일 | 1차 | 2026-09-14 |
| Zhipu 340만+ (17일간) / 273 계정 | 동일 | 1차 | 2026-09-14 |
| Xiaomi 40만+ (20일간) / 1,500+ 계정 | 동일 | 1차 | 2026-09-14 |
| SenseTime·MiniMax 수치 **미공개** | 동일 (보고서가 수치를 안 냄) | 1차 | 2026-09-14 |
| "never sees the target's source code, its weights, or its training data" | 동일 | 1차 인용 | 2026-09-14 |
| Zhipu가 Fable 포기 → "expressly because they assessed the safeguards were weaker" | 동일 | 1차 인용 | 2026-09-14 |
| Mythos 5 / Mythos Preview 대상 시도 미관측 | 동일 | 1차 | 2026-09-14 |
| 안전 훈련이 증류로 전이되지 않음 | 동일 | 1차 | 2026-09-14 |
| 12,000+ 요청 프로빙, 카타카나 번역 우회, 교차 세션 리플레이 | 동일 | 1차 | 2026-09-14 |
| TPP 21,000 / DRAM 6,500 GB/s 상한, presumption of denial → case-by-case | Federal Register 91 FR 1684 (문서 2026-00789, 발효 2026-01-15) | 1차 | 2026-09-14 |
| 중국·마카오향 총 TPP ≤ 미국 내 최종사용 출하분의 50% | 동일 | 1차 | 2026-09-14 |
| 중국 휴머노이드 출하 증가율 최대 94%, Unitree+AgiBot 약 80% | TrendForce 보도자료 2026-04-09 | 1차(업계 조사기관 발표문) | 2026-09-14 |
| DeepSeek flash $0.15/$0.60, Opus 5 $5.00/$25.00, 33배·42배 | jsonhouse 자체 가격 스냅샷 `_data/pricing_history/2026-09-14.json` | 자체 1차 | 2026-09-14 |
| 상위 리더보드 4개 미국 랩 밀집, Kimi K3 Frontend Code Arena 1위 | 공개 리더보드 요약(2차) | **2차** | 2026-09-14 |

---

## 3. 적용된 스타일 + 근거

**박종훈 스타일 (CAT7 Deep Dive)**

`_plans/STYLE_GUIDE.md` §4 선택표에서 "CAT7 Deep Dive (경제·사회 분석) → 박종훈 스타일"에 해당한다. 주제가 모델 비교나 개발 실무가 아니라 **지정학·산업 구조 분석**이고, 독자가 읽고 나서 "미중 AI 경쟁의 큰 지도"를 얻는 것이 목표이기 때문이다.

5단계 매핑:

| 단계 | 해당 섹션 |
|---|---|
| ① 훅 | 도입 3문단 ("On September 10, 2026, Anthropic published the receipts…") |
| ② 원재료 소개 | *What the Report Actually Says* — 보고서 정의 + 7개 랩 표 |
| ③ **이면 분석** | *The Thing That Was Not Taken* + *Why This Is the Only Road Available* (합계 9문단) |
| ④ 큰 그림 연결 | *Change the Axis and the Ranking Inverts* + *Direction and Extensibility* |
| ⑤ 실용적 결론 | *What Follows for the Rest of Us* |

박종훈 금지 사항 점검: "전문가들은 말한다" 식 무출처 인용 없음 ✅ / 뉴스 요약으로 끝나지 않음 ✅ / 이면 분석 존재 ✅

---

## 4. 이면 분석 핵심 (한국어 요약)

증류는 중국 랩들이 영리해서 고른 방법이 아니라, **연산이 규칙으로 배급되는 상황에서 남은 유일한 산술**이다. BIS 규칙은 중국의 연산 상한을 미국 출하량의 함수로 정의해 버렸고(50% 조항), 그 천장 아래에서 역량 격차를 메우려면 실험을 더 돌리거나(=없는 연산이 필요) 이미 실험을 끝낸 쪽의 답을 사는 수밖에 없다.

동시에 이 길에는 벽이 있다. Zhipu는 Anthropic 최상위 공개 모델 Fable을 노리다 **포기하고 방어가 약한 모델로 옮겨갔고**, 아예 공개되지 않은 Mythos 계열에는 시도 자체가 관측되지 않았다. 증류자는 자기가 샘플링할 수 있는 것만 배울 수 있다 — 즉 **선두가 속도뿐 아니라 천장까지 정한다**는 뜻이고, 따라가는 쪽의 최선은 남이 고른 목적지에 두 번째로 도착하는 것이다.

그래서 글의 결론은 "중국이 못한다"가 아니라 **축이 바뀌면 순위가 뒤집힌다**로 간다. 가격(33~42배)과 로보틱스(출하 증가율 94%, 두 기업이 80%)는 미국이 아직 포장하지 않은 두 번째 도로이고, 모델 품질이 수렴할수록 "무엇에 연결되는가"가 승부처가 된다.

---

## 5. 의심스러운 사실 관계 / 기웅 확인 요청

### 5-1. 기웅님 최초 지시 중 **수정한 항목** (중요)

> "과거에 클로드의 가중치 결과를 자기들만의 방법으로 빼내어 중국의 ai 모델에 학습 시킨 뉴스"

**가중치는 유출된 적이 없다.** Anthropic 보고서는 증류(distillation)를 다루며, 공격자는 소스코드·가중치·학습데이터에 접근하지 못한다고 명시한다. 과거 건(2026-02 Anthropic 첫 공개, 2025 초 OpenAI의 DeepSeek 지적)도 모두 출력 증류이지 가중치 절취가 아니다. 지시대로 **이 항목만 수정**해서 "훔쳤다"의 대상을 가중치 → 역량·추론 흔적으로 바꿨다. 나머지 논지는 원안 유지.

### 5-2. 2차 출처에 의존한 단 한 줄

리더보드 관련 서술("상위 4개 미국 랩이 Elo 오차 범위 내", "Kimi K3가 Frontend Code Arena 1위")은 **집계 매체 요약에서 왔고 1차 리더보드를 직접 확인하지 않았다.** `SOURCES.md`는 TIER 3를 배경 조사용으로만 허용한다.

- 현재 처리: 본문에서 구체 Elo 수치를 쓰지 않고 "top four labs / below the top cluster"라는 정성 서술로만 남겼고, 비교표에도 숫자를 넣지 않았다.
- **발행 전 선택**: (a) lmarena.ai를 직접 확인해 1차로 승격, (b) 이 줄을 빼고 가격·로보틱스 축만 남긴다.

### 5-3. 쓰지 않은 수치

"중국이 세계 휴머노이드 출하의 84.7%"라는 수치가 검색 요약에 나왔으나 **TrendForce 원문에는 없었다.** 다른 출처와 섞인 것으로 보여 본문·데이터 파일 모두에서 제외했다. 로보틱스 수치는 원문이 실제로 말한 94%와 80%만 사용.

### 5-4. 표현 리스크

7개 기업을 실명으로 지목하는 글이다. 모든 지목은 Anthropic의 주장이며 본문·데이터 파일에서 전부 Anthropic 귀속으로 서술했다(표 헤더 `(vendor)`, 각 key_fact의 `source`). 우리 자체 판단으로 단정한 문장은 없다. 다만 기업 실명 + "fraud" 어휘가 들어가므로 기웅님이 톤을 한 번 봐주시면 좋겠다.

---

## 6. 내부 링크 목록 + 검증 결과

| 링크 대상 | 앵커 텍스트 | `_posts/` 존재 |
|---|---|---|
| `/posts/llm-api-pricing-2026/` | "weekly pricing table" (본문) / "LLM API Pricing 2026" (Related) | ✅ |
| `/posts/china-ai-coding-plans-2026/` | "China AI Coding Plans 2026" | ✅ |
| `/posts/best-llm-2026/` | "Best LLM 2026" | ✅ |

`link_graph.py --report` 결과 **0 error**. 외부 1차 출처 인라인 링크 3개(Anthropic 보고서, Federal Register, TrendForce) — D1 충족.

---

## 7. 훅 / 검증 상태

- `post-validation.sh`: **PASSED** — 남은 WARN은 커버 파일 미존재 1건뿐 (초안 단계 정상)
- `geo_validation.py`: `[ok] draft 2026-09-18-china-ai-catch-up-2026`
- 본문 약 2,064단어 (기준 600 이상), 문단 중앙값 50단어 / 최장 104단어 (B8 기준 120 이하)
- 데이터 파일: 필수 13필드 충족, `key_facts` 10개, `faq_summary` 4개, `primary_sources` 4개, `license` 필드 없음 ✅

### 품질 자가 점수

| 항목 | 점수 | 가중 | 근거 |
|---|---|---|---|
| technical_accuracy | 9.0 | ×0.30 | 핵심 수치 전부 1차 출처 직접 파싱. 2차 의존은 5-2 한 줄뿐이며 수치를 쓰지 않음 |
| structural_quality | 8.5 | ×0.25 | 박종훈 5단계 충족, 문단 길이 기준 통과 |
| practical_value | 8.0 | ×0.25 | 조달 관점 시사점 2개(안전훈련 미전이, 라우터 경유 데이터) 구체적 |
| data_completeness | 9.0 | ×0.20 | 비교표 + numerical_data 10지표 + field_provenance |
| **종합** | **8.65** | | 기준 7.0 통과 |

---

## 8. 커버 이미지 프롬프트 (전문 — 기웅이 이 블록을 그대로 복사해 사용)

- **가로세로비**: `16:9` (2048x1152)
- **저장 경로**: `assets/img/posts/china-ai-catch-up-2026-cover-raw.png`
- **주의**: 이미지 **생성 모델**로 만들 것. Python/PIL/SVG로 그리면 안 된다 (훅 C11이 색상 수로 걸러낸다)
- 소재 근거: `CLUSTER_LLM` 시각 세계 = 광학과 굴절 (IMAGE_GUIDE §8). 기존 커버(삼각 프리즘·유리 블록·유리 돔)와 겹치지 않는 판유리 2매 구도를 골랐다

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: Two rectangular panes of thick smoked optical glass, standing upright
on a slab of rough dark stone, one positioned behind the other and slightly
offset.

SCENE: A single beam of light enters from one side and passes through the front
pane; the rear pane is lit only across the narrow band where the front pane
lets the beam through, leaving the rest of it in shadow. Fine dust and polish
marks catch the light on the glass surfaces.

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

반입 후 처리는 `post-images` 스킬로: 색상 수 5,000 이상 확인 → 워터마크가 있으면 크롭으로 프레임 밖에 두기 → `optimize_image.py RAW.png --cover -o assets/img/posts/china-ai-catch-up-2026-cover.jpg` (`-o` 반드시 지정, 생략하면 원본이 덮어써진다).

---

## 9. 발행 전 남은 일

1. 커버 이미지 생성·반입·정규화 (§8 프롬프트)
2. 5-2 결정 — 리더보드 문장을 1차 출처로 승격할지, 뺄지
3. 5-4 톤 확인 — 기업 실명 지목 부분
4. 승인 후 `publish-post` 스킬로 Phase 6
