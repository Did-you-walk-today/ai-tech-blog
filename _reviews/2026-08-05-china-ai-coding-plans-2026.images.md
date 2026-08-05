# 이미지 프롬프트 팩 — china-ai-coding-plans-2026

## 대상

| 항목 | 값 |
|---|---|
| 슬러그 | `china-ai-coding-plans-2026` |
| 포맷 | D (구조화 데이터) |
| 클러스터 | `CLUSTER_LLM` |
| 이미지 예산 | 커버 1장 (§3 Format D = 1~2, 서술 도형 0장) |
| 클래스 | A — 표지 이미지. 값을 주장하지 않는다 |

## 소재 선택과 근거

**선택: 어두운 돌 위에 놓인 두꺼운 유리 반구(솔리드 글라스 돔) 1개.**

- `CLUSTER_LLM`의 시각 세계는 §8에서 **광학과 굴절**로 고정돼 있다. 곡면
  단일 매질을 통과하며 휘는 빛은 이 세계의 정중앙에 있다.
- **같은 클러스터 최근 커버와 겹치지 않는다** (§8 중복 확인):

  | 슬러그 | 소재 |
  |---|---|
  | `llm-api-pricing-2026` (07-17) | 삼각 프리즘 — 평면 다면체 |
  | `best-llm-2026` (07-25) | 평볼록 렌즈 — 얇은 광학 부품 |
  | `llm-subscription-guide-2026` (07-25) | 광섬유 봉 — 원통 |
  | `llm-cache-pricing-2026` (이번 배치) | 수면 굴절 — 액체 매질 |

  반구는 위 넷 어느 것과도 실루엣이 다르다. 두껍고 덩어리진 곡면 고체다.
- 셀 수 있는 반복 요소도, 눈금도 없다 (P6 안전).

**드래프트에 이미 적힌 alt 소재("옆으로 넘어진 황동 계량컵")를 폐기했다.**
두 가지가 걸린다. 첫째, 계량컵은 **계량 도구**라 §6 AVOID의 `readable scales`와
`gauges`에 정면으로 걸린다 — 본문이 "서로 환산되지 않는 다섯 개의 단위"를
다루는 글이라 독자가 그 컵을 곧바로 값의 그릇으로 읽는다 (P6). 둘째, 황동
공구는 `CLUSTER_DEVTOOLS`의 시각 세계이고 이 포스트는 `CLUSTER_LLM`이라
§8 클러스터 고정 규칙과도 어긋난다.

포스트의 주장("단위가 서로 환산되지 않는다")을 시각적 은유로 번역하려는
시도였는데, 그게 정확히 스킬 Step 1A가 금지하는 동작이다. 커버는 주장하지
않아야 틀리지 않는다.

서술 도형은 만들지 않는다. 본문의 벤더별 쿼터는 전부 표로 표현되며, 단위가
환산되지 않는다는 것 자체가 도형으로 그리면 안 되는 성질이다 — 서로 다른 단위를
한 화면에 나란히 그리는 순간 그림이 비교 가능성을 암시하게 되고, 이는 본문 주장과
정면으로 모순된다 (P3·T1).

## 완성 프롬프트

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One thick solid hemisphere of clear optical glass, roughly palm-sized,
with a polished domed top, a flat ground base, and a few fine internal
striations left from casting.

SCENE: The dome sits flat-side-down on a slab of dark unpolished stone, and the
light passing through its curved body is gathered into one bright pinched
highlight where the glass meets the stone.

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

## alt 초안

```
A thick dome of clear optical glass resting flat-side-down on rough dark stone, light pinching beneath it
```

104자. 장면 서술이며 데이터 주장이 없다 (§5 클래스 A 규칙).

## 저장 경로 · 규격 · 명령

| 항목 | 값 |
|---|---|
| 원본 | `assets/img/posts/china-ai-coding-plans-2026-cover-raw.png` (2048×1152) |
| 최종 | `assets/img/posts/china-ai-coding-plans-2026-cover.jpg` (1200×630, ≤200KB) |
| frontmatter | `image.path`는 이미 `.jpg`로 올바름. **alt만 위 문안으로 교체** |

```bash
codex exec '$imagegen <위 완성 프롬프트 전체>'
python3 -c "from PIL import Image; im=Image.open('assets/img/posts/china-ai-coding-plans-2026-cover-raw.png').convert('RGB'); n=len(im.getcolors(maxcolors=999999) or []); print(im.size, n, 'colors', '→ OK' if n>5000 else '→ 코드 렌더. 폐기')"
python3 .claude/hooks/optimize_image.py assets/img/posts/china-ai-coding-plans-2026-cover-raw.png --cover -o assets/img/posts/china-ai-coding-plans-2026-cover.jpg
rm assets/img/posts/china-ai-coding-plans-2026-cover-raw.png
```

근거 대응표는 없다 — 클래스 A는 대응시킬 값이 없다 (§1).
