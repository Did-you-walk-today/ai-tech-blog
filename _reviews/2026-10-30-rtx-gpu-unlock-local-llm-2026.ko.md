# Phase 5 리뷰 리포트 — rtx-gpu-unlock-local-llm-2026

- 대상: `_drafts/2026-10-30-rtx-gpu-unlock-local-llm-2026.md` (기웅 승인 즉시 발행, 2026-10-30 같은 날 두 번째 글)
- 데이터: `_data/2026-10-30-rtx-gpu-unlock-local-llm-2026.json`
- 제목: RTX GPU Unlock 2026: What It Means for Local LLMs (49자)
- 카테고리 / 클러스터 / 포맷: ai-models-intelligence (CAT1) / CLUSTER_LLM / A
- 자료 수집일: 2026-10-30

## 1. 핵심 주장 요약 (3줄)

1. GPU 언락은 프롬프트 처리, 파인튜닝, 이미지 생성을 빠르게 하지만 토큰 생성 속도와 VRAM은 바꾸지 못해요.
2. 입문자가 많이 쓰는 Ollama·GGUF 조합의 이득은 0~15%뿐이고, 중고 고VRAM 카드도 2026년에는 싸지 않아요.
3. 한 사람이 큰 모델을 돌린다면 아직 애플 실리콘이 DGX Spark보다 낫고, 모델이 작아질수록 소비자용 RTX의 쓰임새가 넓어져요.

## 2. 인용된 수치 / 출처 목록

| 수치 | 출처 | 확인 |
|---|---|---|
| 작업별 향상률, TFLOPS, 지원 세대, 안정/실험 구분, FAQ | [gpu-unlock README](https://github.com/Zagitta/gpu-unlock) | 원문 확인. 사용자 보고를 프로젝트가 모은 수치 |
| 저장소 생성 10-18, 스타 13,192개 | GitHub API (10-30) | 직접 확인 |
| RTX 3070 8GB 성공 보고, 실험 단계, 조건 한정 | [Windows-GPU-UNLOCK](https://github.com/impacifist/Windows-GPU-UNLOCK) | 원문 확인 |
| 3080 Ti 20GB 무효 보고, 부팅 실패 가능성, 보증 무효 가능성 | [TweakTown](https://www.tweaktown.com/news/114288/modders-unlock-nvidia-geforce-rtx-20-30-and-40-series-compute-limits-nearly-doubling-some-tensor-core-throughput/index.html) | 2차 출처 |
| M5 Max 614GB/s, 128GB | [Apple 사양](https://www.apple.com/mac-studio/specs/) | 원문 확인 |
| Spark 64/128GB | [NVIDIA](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) | 원문 확인 |
| Spark 273GB/s, 벤치마크 표, $5,099, StorageReview 2,760 | [ComputingForGeeks](https://computingforgeeks.com/dgx-spark-vs-strix-halo-vs-mac-studio/) | 2차 집계 |
| Mac Studio $5,399 | [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/24654/mac-studio-m5-max-vs-dgx-spark-local-ai) | 2차 출처 |
| Spark $6,950 / $4,999, 출시가 대비 약 75% 상승 | [The Register](https://www.theregister.com/systems/2026/10/02/nvidia-debuts-4999-dgx-spark-with-half-the-ram-and-storage-amid-memory-crunch/5300622) | 기사 본문 확인. NVIDIA 공식 공지는 못 찾음 |
| 5090 210 tok/s, 70B 로드 불가 | [Contra Collective](https://contracollective.com/blog/m5-max-vs-rtx-5090-vs-dgx-spark-local-llm-inference-throughput-cost-2026) | 블로그 측정, 2026-07 |
| 3090 $1,199 / $1,450 / $1,389 | [AI Indigo](https://aiindigo.com/hardware/nvidia-rtx-3090-24gb), [OpenClawDC](https://openclawdc.com/blog/is-a-used-rtx-3090-worth-it-local-llm/), [GPUPoet](https://gpupoet.com/gpu/learn/price/october-2026/nvidia-geforce-rtx-3090) | 집계 방식이 서로 다름 |
| 2.25배 | 614 ÷ 273, 우리 계산 | 본문에 표기 |

## 3. 적용된 스타일 + 근거

**jsonhouse DNA** (CAT1). 하드웨어와 로컬 LLM을 다루고 표 데이터와 구매 판단이 핵심이라 CAT1~6 기본 스타일을 썼어요. 처음 논의할 때 카테고리를 정하지 않았고, 산업 분석보다 모델 활용 쪽에 가까워서 `ai-models-intelligence`로 정했어요.

## 4. 이면 분석 핵심

LLM 실행은 계산에 묶인 프롬프트 처리와 메모리 대역폭에 묶인 토큰 생성으로 나뉘는데, 언락은 앞쪽만 풀어요. 그래서 "2배"라는 헤드라인과 달리 채팅 체감은 거의 그대로예요. 같은 칩의 성능을 가격대로 나누는 엔비디아의 구조로 보면, 대용량 고대역폭 제품을 소비자 가격에 낼 유인도 약해 보여요. 이 부분은 추론이라고 본문에 밝혔어요.

## 5. 의심스러운 사실 관계 / 기웅 판단 필요

- **가격 기준일:** 10-30 수집, 같은 날 발행이라 7일 규칙을 충족해요.
- **Spark 우위 표현:** 기웅님 의견대로 "개인 사용자에게는 애플 우위"로 썼어요. 다만 "메모리가 더 많다", "장점이 없다"는 자료와 달라서 쓰지 않았어요. 두 제품 모두 128GB이고, CUDA와 배치 처리 강점은 적었어요.
- **프롬프트 처리는 결과가 엇갈려요.** 2K대에서는 Spark, 16K에서는 M5 Max가 높아요. 조건이 달라 우열을 단정하지 않았어요.
- **벤치마크 품질:** 통제된 동일 조건 비교를 찾지 못했어요. Contra의 M5 Max 대역폭(546GB/s)은 Apple 공식치(614GB/s)와 다르고, 7B 수치도 ComputingForGeeks와 달라요. 방향성 근거로만 썼어요.
- **언락 수치:** 독립 검증을 찾지 못했어요. 프로젝트 자체 표임을 본문 곳곳에 밝혔어요.
- **M5 Max vs M5 Ultra:** ComputingForGeeks는 96GB에 1.2TB/s인 M5 Ultra를 $5,499로 적었어요. 이 제품은 128GB 비교에서 벗어나 표에 넣지 않았어요. Apple 사양 페이지에서 96GB는 확인했지만 Ultra 가격은 확인하지 못했어요.
- **중고가 상승 원인:** 언락 영향과 메모리 가격 영향을 분리할 수 없다고 썼어요.
- **"SLM이 늘어난다":** 미발행 SLM 글을 인용할 수 없어서 "우리의 예상"으로 썼어요. 그 글이 먼저 발행되면 링크와 수치를 넣는 게 좋아요.
- **공개 범위:** 도입부에 "이 사이트 관계자가 Windows에서 RTX 3070을 쓴다"고 적었어요.

## 6. 내부 링크 목록 + 검증 결과

| 링크 | 존재 |
|---|---|
| /posts/llm-api-pricing-2026/ | ✅ `_posts/2026-07-17-llm-api-pricing-2026.md` |
| /posts/best-llm-2026/ | ✅ `_posts/2026-07-25-best-llm-2026.md` |
| /posts/solo-developer-window-2026/ | ✅ `_posts/2026-10-30-solo-developer-window-2026.md` (그 글의 고아 경고도 해소) |

## 7. 커버 이미지 프롬프트 전문

CLUSTER_LLM 소재 풀(광학과 굴절)에서 골랐어요. 기존 커버는 막대, 판유리, 수면, 렌즈, 프리즘, 블록, 돔이라 겹치지 않게 **광학 유리 쐐기 하나**로 했어요. 렌즈 커버는 SLM 글용이에요. 피사체가 하나이고 눈금이 없어 값으로 읽힐 요소가 없어요.

- 가로세로비: 16:9
- 저장 경로: `assets/img/posts/rtx-gpu-unlock-local-llm-2026-cover-raw.png`
- 웹앱의 이미지 생성 모델로 만들어 주세요. 코드로 그리면 안 돼요.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single thick wedge of clear optical glass, palm-sized, with polished
faces and one edge tapering to a thin, sharp line, free of any markings.

SCENE: The wedge lies on a slab of rough dark stone, a narrow beam of light
entering its thick face and leaving through the angled face as a soft glow on
the stone beyond.

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

- 제목 49자, description 159자, 본문 약 2,000단어
- post-validation 훅: PASSED. 남은 경고는 커버 파일 없음 1건이에요.
- geo_validation: 이 글의 오류 0건
- 깨진 내부 링크 없음
- 품질 자가 점수 7.7 (정확성 7.5 / 구조 8.5 / 실용 8.0 / 데이터 6.5). 데이터 점수는 자체 실측이 없고 벤치마크 조건이 섞여 있어 낮게 잡았어요.

## 9. 다음 단계

1. 기웅 검토 후 승인 또는 수정 지시
2. 커버 생성(7절) → 반입·정규화
3. `publish-post` 스킬로 발행
