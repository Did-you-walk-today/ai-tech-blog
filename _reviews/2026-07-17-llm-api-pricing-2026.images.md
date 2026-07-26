# 이미지 제작 기록 — llm-api-pricing-2026

## 대상

- 포맷: D
- 클러스터: `CLUSTER_LLM`
- 이미지 클래스: A — 커버

## 소재 선택

- 선택한 소재: 단일 삼각 광학 유리 프리즘
- 근거: `CLUSTER_LLM`의 광학과 굴절 세계에 속하며, 기존 렌즈와 이번 배치의 주조 유리 블록과 형태가 겹치지 않는다.

## 완성 프롬프트

```text
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One solid triangular optical glass prism with slightly imperfect tactile edges.

SCENE: The solitary prism lies on a dark matte surface and catches cyan and amber edge light without projecting a spectrum, beam, scale, or repeated pattern.

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

## Alt 초안

`A single triangular glass prism on a dark matte surface with cyan and amber light tracing its edges`

## 저장 및 검증

- 원본: `assets/img/posts/llm-api-pricing-2026-cover-raw.png`
- 최종: `assets/img/posts/llm-api-pricing-2026-cover.jpg`
- 최종 규격: 1200×630 JPEG, 200KB 이하

## 검수 결과

- 원본 색상 수: 86,296 — 이미지 모델 생성 확인
- 최종: 1200×630, 63,190 bytes, 42,578 colors
- 육안 검수: 텍스트·수치·로고·스펙트럼·광선 도식·반복 수량 요소·금지 AI 소재 없음
- 크롭 검수: 피사체 전체와 상하 안전 여백 유지
