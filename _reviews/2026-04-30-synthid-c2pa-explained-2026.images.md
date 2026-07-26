# 이미지 제작 기록 — synthid-c2pa-explained-2026

## 대상

- 포맷: C
- 클러스터: `CLUSTER_AI_CONTENT_POLICY`
- 이미지 클래스: A — 커버

## 소재 선택

- 선택한 소재: 단일 투명 석영 결정 표본
- 근거: 전용 소재 풀이 없는 클러스터에 적용하는 지질과 재료 세계의 오브젝트다.
  직전 커버 3장의 암석 코어, 산화 구리판, 슬레이트 판석과 겹치지 않는다.

## 완성 프롬프트

```text
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One natural transparent quartz crystal specimen with an irregular stone base.

SCENE: The solitary crystal rests on a dark matte stone surface, with subtle internal refraction and ample empty background.

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

`A transparent quartz crystal specimen resting on dark stone under cyan and amber side lighting`

## 저장 및 검증

- 원본: `assets/img/posts/synthid-c2pa-explained-2026-cover-raw.png`
- 최종: `assets/img/posts/synthid-c2pa-explained-2026-cover.jpg`
- 최종 규격: 1200×630 JPEG, 200KB 이하
- 정규화: `python3 .claude/hooks/optimize_image.py assets/img/posts/synthid-c2pa-explained-2026-cover-raw.png --cover -o assets/img/posts/synthid-c2pa-explained-2026-cover.jpg`

## 검수 결과

- 원본 색상 수: 147,895 — 이미지 모델 생성 확인
- 최종: 1200×630, 80,142 bytes, 56,748 colors
- 육안 검수: 텍스트·수치·로고·반복 수량 요소·금지 AI 소재 없음
- 크롭 검수: 피사체 전체와 상하 안전 여백 유지
