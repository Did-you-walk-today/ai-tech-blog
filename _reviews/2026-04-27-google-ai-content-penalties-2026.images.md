# Image Pack — google-ai-content-penalties-2026

## 대상

- 슬러그: `google-ai-content-penalties-2026`
- 포맷: C (기술 가이드)
- 클러스터: `CLUSTER_AI_CONTENT_POLICY`
- 이미지 구성: 커버 1장, 본문 도형 추가 없음
- 클래스: A (표지 이미지)

## 소재 선택

- 클러스터 시각 세계: 지질과 재료 (`IMAGE_GUIDE.md` §8의 그 외 / 신규)
- 선택한 소재: 단일 원통형 암석 코어 샘플
- 근거: 아직 전용 소재 풀이 없는 클러스터이므로 지질과 재료 세계를 적용했다.
  같은 백필 묶음의 다른 두 커버와 소재가 겹치지 않는다.

클래스 A는 본문의 값을 주장하지 않으므로 근거 대응표가 없다.

## 커버 생성 프롬프트

```text
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single cylindrical geological drill-core sample, forearm length,
with a rough fractured end and a weathered gray basalt surface crossed by one
irregular pale mineral vein.

SCENE: The core rests diagonally on a dark matte stone slab, with loose mineral
dust gathered naturally beneath the fractured end.

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

MUST KEEP: Exactly one drill-core sample, not a row or collection. Consistent
light direction across the whole frame. Large areas of unbroken dark
background. Nothing that could be read as a measurement.
```

## 반입 정보

- 원본: `assets/img/posts/google-ai-content-penalties-2026-cover-raw.png`
- 최종: `assets/img/posts/google-ai-content-penalties-2026-cover.jpg`
- alt: `"A weathered basalt drill-core sample with a fractured end resting on dark stone under cyan and amber light"`

