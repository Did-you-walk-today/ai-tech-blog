# 이미지 프롬프트 팩 — llm-cache-pricing-2026

## 대상

| 항목 | 값 |
|---|---|
| 슬러그 | `llm-cache-pricing-2026` |
| 포맷 | D (구조화 데이터) |
| 클러스터 | `CLUSTER_LLM` |
| 이미지 예산 | 커버 1장 (§3 Format D = 1~2, 서술 도형 0장) |
| 클래스 | A — 표지 이미지. 값을 주장하지 않는다 |

## 소재 선택과 근거

**선택: 어두운 돌 대야에 담긴 얕고 잔잔한 물, 표면에서 꺾이는 빛.**

- `CLUSTER_LLM`의 시각 세계는 §8에서 **광학과 굴절**로 고정돼 있고, 소재 예시 중
  "수면의 빛 굴절"에 해당한다.
- **같은 클러스터 최근 커버 3장과 겹치지 않는다** (§8 중복 확인):

  | 슬러그 | 소재 |
  |---|---|
  | `llm-api-pricing-2026` (07-17) | 삼각 광학 프리즘 |
  | `best-llm-2026` (07-25) | 평볼록 렌즈 |
  | `llm-subscription-guide-2026` (07-25) | 광섬유 유리 봉 |

  유리 고체 3연속이라 이번엔 같은 광학 세계 안에서 **매질을 물로 바꿨다.**
  시리즈감은 유지되고 화면은 반복되지 않는다.
- 물은 셀 수 있는 반복 요소도, 눈금도 만들지 않는다 (P6 안전).

**드래프트에 이미 적힌 alt 소재("두 장의 겹친 유리판")를 폐기했다.** "두 장"은
셀 수 있는 반복 요소이고, 안쪽이 바깥쪽보다 밝다는 서술은 두 값의 대소를
암시한다. 본문이 캐시 적중률별 유효 단가를 다루는 글이라 독자가 그 대비를
곧바로 값으로 읽는다 — P6 위반 소지가 명확해서 소재 단계에서 걷어냈다.

서술 도형은 만들지 않는다. 본문의 벤더별 캐시 단가는 전부 표로 표현되며,
표가 표현하지 못하는 관계가 없다 (§3 기본값 0장).

## 완성 프롬프트

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One shallow pool of perfectly still water held in a hand-carved basin
of dark grey stone, the water only a finger deep, its surface unbroken except
where a single slow ripple crosses it.

SCENE: A narrow shaft of light enters the pool at a low angle and visibly bends
at the water surface, throwing one soft caustic band across the rough stone
floor of the basin.

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
A shallow pool of still water in a carved dark stone basin, one shaft of light bending at the surface
```

101자. 장면 서술이며 데이터 주장이 없다 (§5 클래스 A 규칙).

## 저장 경로 · 규격 · 명령

| 항목 | 값 |
|---|---|
| 원본 | `assets/img/posts/llm-cache-pricing-2026-cover-raw.png` (2048×1152) |
| 최종 | `assets/img/posts/llm-cache-pricing-2026-cover.jpg` (1200×630, ≤200KB) |
| frontmatter | `image.path`는 이미 `.jpg`로 올바름. **alt만 위 문안으로 교체** |

```bash
codex exec '$imagegen <위 완성 프롬프트 전체>'
python3 -c "from PIL import Image; im=Image.open('assets/img/posts/llm-cache-pricing-2026-cover-raw.png').convert('RGB'); n=len(im.getcolors(maxcolors=999999) or []); print(im.size, n, 'colors', '→ OK' if n>5000 else '→ 코드 렌더. 폐기')"
python3 .claude/hooks/optimize_image.py assets/img/posts/llm-cache-pricing-2026-cover-raw.png --cover -o assets/img/posts/llm-cache-pricing-2026-cover.jpg
rm assets/img/posts/llm-cache-pricing-2026-cover-raw.png
```

근거 대응표는 없다 — 클래스 A는 대응시킬 값이 없다 (§1).
