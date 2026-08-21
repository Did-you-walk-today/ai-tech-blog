# 이미지 팩 — llm-price-war-balance-sheet-2026

- 대상: `_drafts/2026-08-28-llm-price-war-balance-sheet-2026.md`
- 포맷: F / 클러스터: **CLUSTER_LLM** / 카테고리: industry-analysis
- 이미지 예산: 커버 1장. **서술 도형 0장** (아래 §3 참조)

## 1. 소재 선택 근거

`IMAGE_GUIDE.md` §8에서 CLUSTER_LLM의 시각 세계는 **광학과 굴절**이다.
같은 클러스터 최근 커버 5장과 실루엣이 겹치지 않는 것을 골랐다:

| 슬러그 | 기존 소재 |
|---|---|
| llm-api-pricing-2026 | 삼각 프리즘 |
| best-llm-2026 | 두꺼운 렌즈 요소 |
| llm-subscription-guide-2026 | 광학 유리 로드 (원기둥) |
| llm-cache-pricing-2026 | 석재 수반의 수면 |
| china-ai-coding-plans-2026 | 유리 돔 (반구) |
| **이번** | **직육면체 광학 유리 블록의 베벨 모서리** |

삼각·원반·원기둥·평면·반구는 이미 썼고, **직육면체**는 처음이다.
포스트 주장과는 무관하다 — 무관한 편이 안전하다 (§1: 주장하지 않으면 틀릴 수 없다).

## 2. P6 위험 점검

의도적으로 배제한 후보:

- **광섬유 다발 단면** — §8 소재 예시에 있으나 **셀 수 있는 반복 요소**라 P6 위반 위험.
  독자가 가닥 수를 값으로 읽을 수 있다
- **렌즈 요소 분해도** — 같은 이유 (요소 개수가 세어진다)
- **적층 원반** — 같은 이유. 초안 단계의 alt에 쓰여 있었으나 이번에 교체한다

선택한 유리 블록은 단일 개체이고 눈금·축·반복 요소가 없다.

## 3. 서술 도형을 만들지 않는 이유

본문의 관계는 전부 표로 표현된다 — 가격 변동 원장, 소유/임차 매트릭스, 체인지로그.
`IMAGE_GUIDE.md` §0에 따라 표로 되는 것은 표로 둔다. Format F 예산은 2장이지만
**흐름·계층·시간축 중 표가 못 담는 것이 없어 0장으로 간다.**
따라서 이 팩에는 **근거 대응표가 없다** (커버는 값을 주장하지 않으므로 대응시킬 값이 없다).

## 4. 완성 프롬프트 (기웅 실행용 — 축약 금지)

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single rectangular block of thick optical glass, solid and heavy,
with polished bevelled edges.

SCENE: The block rests on its long edge on rough dark stone, tilted slightly
off vertical so one bevelled corner faces the viewer. Light enters through
that corner and pools inside the body of the glass, leaving the interior
brighter than the surface it sits on.

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

## 5. alt 초안

```
A single rectangular block of thick optical glass tilted on dark stone, one bevelled corner catching cyan light
```

110자. 장면 서술이며 데이터 주장 없음 (§5 클래스 A 규칙).

## 6. 반입 규격

- 생성물 저장: `assets/img/posts/llm-price-war-balance-sheet-2026-cover-raw.png`
- 정규화 명령:
  ```bash
  python3 .claude/hooks/optimize_image.py \
      assets/img/posts/llm-price-war-balance-sheet-2026-cover-raw.png --cover \
      -o assets/img/posts/llm-price-war-balance-sheet-2026-cover.jpg
  rm assets/img/posts/llm-price-war-balance-sheet-2026-cover-raw.png
  ```
- 최종: `llm-price-war-balance-sheet-2026-cover.jpg`, 1200×630, 200KB 이하, 색상 수 1,000 초과

## 7. 반입 검증 기록 (2026-08-21)

기웅이 2장 업로드. **2번 채택, 1번 반려.**

| | 파일 | 규격 | 색상 수 | 판정 |
|---|---|---|---|---|
| 1 | `Gemini_Generated_Image_qg6qj6...png` | 2752×1536 (1.792) | 59,260 | **반려** |
| 2 | `Gemini_Generated_Image_a2hzpb...png` | 1424×752 (1.894) | 47,436 | **채택** |

### 1번 반려 사유 — 소재 불일치

산출물은 **거친 콘크리트/석재 쐐기**로, 프롬프트가 지정한 "thick optical glass,
polished bevelled edges, light pooling inside the body"와 재질이 반대다(불투명·무광·다공성).

- `IMAGE_GUIDE.md` §8 기준 이 소재는 **지질과 재료** = "그 외/신규" 클러스터의 시각 세계이며,
  CLUSTER_LLM(광학과 굴절)이 아니다
- 실루엣이 **삼각형**이라 `llm-api-pricing-2026`의 삼각 프리즘 커버와 충돌한다

스타일·조명·구도·AVOID 조항은 전부 준수했으므로 프롬프트 문제가 아니라 소재 해석 문제다.

### 2번 채택 — 프롬프트 전 항목 일치

SUBJECT(직육면체 광학 유리, 베벨 모서리), SCENE(석재 위 기울어짐, 유리 내부에 빛이 고임),
COMPOSITION(좌측 3분할, 우측 여백), LIGHTING(딥 네이비 + 시안 키 + 앰버 림) 전부 일치.

### 워터마크 처리

Gemini 생성 표식(4점 스파클)이 우하단에 구워져 있었다. bbox `x 1280~1327, y 608~655`.

**리터칭하지 않고 크롭으로 프레임 밖에 뒀다** (§11 출처 표시 제거 금지).
스킬 지침대로 **폭부터** 줄였다 — 상하를 깎으면 §7이 확보한 안전 여백을 이중으로 잃는다.

- 크롭 박스 `(0, 44, 1272, 712)` → 1272×668 (40:21 = 1.90419)
- 폭: 1272로 잘라 워터마크(1280~) 8px 여유로 제외
- 높이: 상단 44 / 하단 40 제거. 유리 상단이 새 프레임의 9.9% 지점에 놓여 §7 안전여백 8% 확보
- 최종 검사: 우하단 밝은 픽셀 0개 → 제거 확인

### 최종 산출물

`assets/img/posts/llm-price-war-balance-sheet-2026-cover.jpg`
**1200×630 / 73.4KB / 49,449색** — C1·C3·C11 전부 통과, `image_validation.py` → `OK`

### 육안 검수 (Step 4)

- 값으로 읽히는 요소(막대·축·눈금·계기판·셀 수 있는 반복): **없음** — P6 통과
- §6 AVOID 금지 소재(로봇·사람·뇌·회로기판·홀로그램 HUD·구워진 텍스트): **없음**
- 크롭 후 피사체 온전성: **온전** — 유리 블록 전체가 프레임 안
- alt와 장면 일치: **일치**

원본 업로드 2장은 레포에 커밋하지 않고 스크래치패드로 이동했다
(`scratchpad/cover-uploads/`). 1번 반려본도 함께 보관 중이다.
