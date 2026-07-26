# 이미지 제작 기록 — gigo-prompts-2026-why-vague-prompts-fail

## 대상

- 포맷: C
- 클러스터: `CLUSTER_PROMPTS`
- 이미지 클래스: A — 커버

## 소재 선택

- 선택한 소재: 단일 목재 손잡이 인쇄용 잉크 롤러
- 근거: `CLUSTER_PROMPTS`의 직물과 인쇄 세계에 속하는 구체적인 실물 오브젝트다.
  기존 커버에 사용되지 않은 소재이며 읽을 수 있는 활자나 반복 무늬가 없다.

## 완성 프롬프트

```text
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One vintage printing ink brayer with a dark rubber roller and tactile wooden handle.

SCENE: The solitary brayer rests diagonally on a dark unprinted sheet of textured paper, with no ink marks or printed characters.

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

`A vintage printing ink brayer resting on dark textured paper under cyan and amber directional light`

## 저장 및 검증

- 원본: `assets/img/posts/gigo-prompts-2026-why-vague-prompts-fail-cover-raw.png`
- 최종: `assets/img/posts/gigo-prompts-2026-why-vague-prompts-fail-cover.jpg`
- 최종 규격: 1200×630 JPEG, 200KB 이하
- 정규화: `python3 .claude/hooks/optimize_image.py assets/img/posts/gigo-prompts-2026-why-vague-prompts-fail-cover-raw.png --cover -o assets/img/posts/gigo-prompts-2026-why-vague-prompts-fail-cover.jpg`

## 검수 결과

- 원본 색상 수: 70,433 — 이미지 모델 생성 확인
- 최종: 1200×630, 104,642 bytes, 24,065 colors
- 육안 검수: 텍스트·수치·로고·인쇄 문자·반복 수량 요소·금지 AI 소재 없음
- 크롭 검수: 피사체 전체와 상하 안전 여백 유지
