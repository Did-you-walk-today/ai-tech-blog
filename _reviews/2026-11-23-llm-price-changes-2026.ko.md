# 리뷰 리포트 — llm-price-changes-2026

- 초안: `_posts/2026-11-23-llm-price-changes-2026.md`
- 데이터: `_data/2026-11-23-llm-price-changes-2026.json`
- 포맷 / 카테고리 / 클러스터: D / CAT5 (ai-data-statistics) / CLUSTER_LLM
- 데이터 기준일: 2026-11-23 (스냅샷 18개, 2026-07-16 ~ 2026-11-23)

## 1. 핵심 주장 요약 (3줄)

1. 계속 판매 중인 모델의 가격은 130일 동안 주간 점검 814번 중 10번만 바뀌었어요(1.2%). 그중 인하 7번, 인상 3번이에요.
2. 8월 24일 이후로 기존 모델 ID의 입력·출력 가격 인하는 0건이에요(Mistral Large 4가 자기 인상을 되돌린 1건만 예외). 같은 기간 새 모델 ID 8개가 이전 모델보다 20~90% 싸게 나왔어요.
3. 그렇다고 새 버전이 늘 싼 건 아니에요. 후속 모델 19쌍 중 입력 가격이 내린 건 8쌍, 같은 건 10쌍, 오른 건 1쌍이라 중앙값은 0%예요.

## 2. 인용 수치와 출처

| 수치 | 출처 |
|---|---|
| 스냅샷 18개, 130일, 행-구간 814개, 가격 변동 10건 | jsonhouse 자체 집계 (`_data/pricing_history/` 18개 파일) |
| 18개 시점 내내 추적한 29개 모델 중 24개가 7월 가격 그대로 | jsonhouse 자체 집계 |
| 후속 모델 19쌍 입력 가격 비교 (8 인하 / 10 동일 / 1 인상) | jsonhouse 자체 집계, 가격 자체는 각사 공식 가격 페이지 |
| 가격 변동 10건의 개별 수치 | 각 주의 스냅샷 (각사 공식 가격 페이지에서 수집) |
| 12-01 Gemini 4 Argon·Carbon 2배, 2027-01-01 Gemini 3.8·3.6 Flash 2배 | Google 가격 페이지 (2026-11-23 스냅샷) |
| 11-30 GPT-5.6-sol 프로모션 종료 | OpenAI 가격 페이지 (2026-11-23 스냅샷) |
| 11-30 Claude Sonnet 4.5 퇴역, 대체 모델 Sonnet 5.5 | Anthropic 지원 종료 페이지 |
| Anthropic 신형 토크나이저 약 30% 토큰 증가 | Anthropic 가격 페이지 |

집계 스크립트는 스크래치패드에만 있어요(커밋 안 함). 월간 갱신 때 같은 로직으로 다시 돌리면 돼요.

## 3. 적용 스타일과 근거

- **스타일:** jsonhouse DNA (데이터 강화형)
- **근거:** CAT5 데이터·통계 글이라 스타일 가이드 ④에 따라 "합성 스타일(데이터 강화)"을 적용했어요.
- **5단계 구성:** 훅+TL;DR → 데이터 표 4개(가격 변동, 장기 추적 모델, 후속 모델, 예정된 변동) → 이면 분석("Why Prices Move Through New Model IDs") → 큰 그림(가격 전쟁·지원 종료 글과 연결) → 예산 관점의 실용 결론 + FAQ
- **1차 출처 필수 8요소:** Methodology, 기준일, Raw data 링크, Limitations, 월간 갱신 약속, Changelog, 단위 통일 표, 표 헤더의 출처 표기를 모두 넣었어요.

## 4. 이면 분석 핵심

기존 모델의 가격을 내리면 원래 가격을 계속 낼 고객까지 혜택을 받아요. 반면 새 모델 ID로 내리면 옮겨 갈 수고를 감수하는 고객만 혜택을 받아요. 그래서 공급사는 가격이 떨어지는 그림을 보여주면서도 기존 매출은 예전 요율로 지킬 수 있다는 것이 이 글의 해석이에요. 본문에서는 이 부분을 공급사가 밝힌 이유가 아니라 우리의 해석이라고 분명히 적었어요.

## 5. 확인이 필요한 사항

- **11-23 스냅샷이 미커밋 상태예요.** `_data/pricing_history/2026-11-23.json`은 제가 만든 파일이 아니고 아직 커밋되지 않았어요. 이 글의 18번째 시점과 GPT-6.2 두 쌍이 이 파일에 의존해요. 발행 전에 이 스냅샷이 커밋돼 있어야 해요.
- **"후속 모델" 분류는 우리 정의예요.** 19쌍 중 공급사 근거가 있는 쌍은 3개예요(DeepSeek의 레거시 ID 처리, Google의 3.5→3.6·3.7→3.8 자동 전환). 나머지 16쌍은 이름 체계로 짝지었어요. Opus 4.8 → Opus 5처럼 공급사가 대체 관계를 명시하지 않은 쌍이 있어요.
- **Mistral Large 4의 +36%는 출시 당시 할인가 기준이에요.** 당시 정가($1.36)로 계산하면 +172%예요. 본문에 둘 다 적었어요.
- **7월 28일 신규 진입 8개는 대부분 실제 출시가 아니에요.** 추적 범위를 넓히면서 추가된 모델들이에요. 그래서 진입 수를 "출시 수"로 쓰지 않았고 Limitations에 적었어요.
- **기획 보고 때 수치를 정정해요.** 기획안에는 가격 변동을 "9건(내림 7, 올림 2)"으로 적었는데, 다시 세어 보니 10건(내림 7, 올림 3)이에요. Mistral Large 4가 두 번 움직인 것을 한 건으로 셌던 오류예요. 초안은 10건으로 썼어요.

## 6. 내부 링크 검증

| 링크 | `_posts/` 존재 |
|---|---|
| `/posts/llm-api-pricing-2026/` | 있음 |
| `/posts/llm-cache-pricing-2026/` | 있음 |
| `/posts/llm-price-war-balance-sheet-2026/` | 있음 |
| `/posts/best-llm-2026/` | 있음 |

외부 1차 출처 링크는 Methodology에 6개사 가격 페이지를 본문 링크로 넣었어요.

## 7. 커버 이미지 프롬프트 전문

CLUSTER_LLM 소재 풀(광학과 굴절)에서 골랐어요. 기존 LLM 커버는 막대, 판유리, 수면, 렌즈, 프리즘, 블록, 돔, 쐐기라서 겹치지 않게 **통유리 구 하나**로 했어요. 피사체가 하나이고 눈금이 없어서 값으로 읽힐 요소가 없어요.

- 가로세로비: 16:9
- 저장 경로: `assets/img/posts/llm-price-changes-2026-cover-raw.png`
- 웹앱의 이미지 생성 모델로 만들어 주세요. 코드로 그리면 안 돼요.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single solid sphere of clear optical glass, the size of an orange,
flawless and free of any markings, engravings or bubbles.

SCENE: The sphere rests on a slab of rough dark stone. A narrow beam of light
passes through it and converges into a small, soft bright point on the stone
behind, with a faint inverted refraction visible inside the glass.

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

AVOID에 `glowing orbs`가 있어요. 구 자체가 빛나 보이면 안 되므로, 생성 결과에서 구가 스스로 발광하는 구슬처럼 나오면 다시 생성해 주세요(빛은 구를 통과해 바닥에 맺혀야 해요).

## 8. 검증 결과

- 제목 56자, description 160자, 본문 약 2,200단어
- post-validation 훅: PASSED. 남은 경고는 커버 파일 없음 1건이에요.
- geo_validation: 이 초안 OK
- taxonomy_validation: 이 초안 관련 오류 없음
- 깨진 내부 링크 없음
- 품질 자가 점수 8.1 (정확성 8.0 / 구조 8.5 / 실용 7.5 / 데이터 8.5). 1차 시계열 데이터라 데이터 점수를 높게 잡았어요. 실용 점수는 개별 모델 추천이 없어서 조금 낮게 잡았어요.

## 9. 다음 단계

1. 기웅 검토 후 승인 또는 수정 지시
2. 11-23 스냅샷 커밋 확인
3. 커버 생성(7절) → 반입·정규화
4. `publish-post` 스킬로 발행
