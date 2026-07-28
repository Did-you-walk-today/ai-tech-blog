# 이미지 제작 기록 — llm-subscription-guide-2026

## 대상

- 포맷: A
- 클러스터: `CLUSTER_LLM`
- 이미지 클래스: A — 커버

## 소재 선택

- 선택한 소재: 단일 용융 광섬유 유리 봉 단면
- 근거: `CLUSTER_LLM`의 광학과 굴절 세계에 속하며, 기존 프리즘·주조 유리 블록·볼록 렌즈와 실루엣과 재료 표현이 겹치지 않는다.

## 완성 프롬프트

```text
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One thick fused optical-fiber glass rod segment, palm-sized and cylindrical, with a smooth circular cut face and a rough frosted outer sleeve.

SCENE: The solitary glass rod lies diagonally on a dark matte stone surface, its cut face catching a soft cyan glow while warm amber light traces the opposite rim.

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

MUST KEEP: Exactly one glass rod segment — no bundle, no loose fibers, no row,
no set, nothing countable. The cut face must remain smooth and abstract, with
no grid, dots, cells, rings, scale, or repeated pattern. Consistent light
direction across the whole frame. Large areas of unbroken dark background.
Nothing that could be read as a measurement.
```

## Alt 초안

`A single thick optical glass rod on dark stone, with cyan light on its cut face and amber light along the rim`

## 저장 및 검증

- 원본: `assets/img/posts/llm-subscription-guide-2026-cover-raw.png`
- 최종: `assets/img/posts/llm-subscription-guide-2026-cover.jpg`
- 최종 규격: 1200×630 JPEG, 200KB 이하

## 검수 결과

- 원본: 1672×941, 117,499색 — 이미지 모델 생성 확인
- 최종: 1200×630, 92,260 bytes, 52,794색
- 육안 검수: 텍스트·수치·로고·반복 수량 요소·금지 AI 소재 없음
- 크롭 검수: 광학 유리 봉 전체와 상하 안전 여백 유지
