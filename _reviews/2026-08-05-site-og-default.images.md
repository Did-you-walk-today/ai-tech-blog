# 이미지 프롬프트 팩 — 사이트 기본 소셜 이미지 (og-default)

- **대상**: 포스트가 아니라 **사이트 공통 폴백**. `_config.yml`의 `social_preview_image`
- **클래스**: A (표지 이미지) — 값을 주장하지 않는다. 근거 대응표 없음
- **클러스터**: 해당 없음 → `IMAGE_GUIDE.md` §8의 "그 외 / 신규 = 지질과 재료"
- **출력**: `assets/img/og-default.jpg` (1200×630, 200KB 이하)

## 왜 이 파일이 필요한가

`_config.yml:41`이 `/assets/img/og-default.png`를 가리키는데 **파일이 레포에 없다.**
라이브에서 404이며, 자체 커버가 없는 모든 페이지(홈, 탭, 아카이브)의 og:image가
현재 깨져 있다. 포스트 커버가 아직 없는 글을 발행하려면 이 폴백이 먼저 있어야
소셜 카드 캐시에 빈 카드가 박히지 않는다.

## 소재 선택과 근거

**산화된 구리판 한 장, 한 모서리가 들린 채 어두운 석재 위에 놓임.**

- 사이트 전체 폴백이라 특정 클러스터의 시각 세계에 묶이면 안 된다 →
  §8의 클러스터 중립 항목(지질과 재료)에서 고름
- 기존 커버 14장은 광학(유리·프리즘·렌즈)과 정밀기계(강철·황동)에 몰려 있다.
  산화 금속 표면은 그 둘과 겹치지 않으면서 같은 재료 계열 안에 있다
- **P6 안전성이 선택의 결정적 이유다.** 지층 단면·암석 코어는 줄무늬가
  셀 수 있는 반복 요소로 읽혀 수량을 암시할 수 있다. 산화 표면은 불규칙한
  질감이라 어떤 값으로도 읽히지 않는다

## 완성 프롬프트

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single sheet of oxidized copper, its patina in mottled verdigris and
warm brown, one corner lifted slightly off the surface.

SCENE: The sheet rests on rough dark stone, the lifted corner catching light
along its torn edge while the rest of the plate lies flat in shadow.

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

사이트 기본 이미지는 페이지별 alt를 갖지 않는다(og:image 메타 태그로만 쓰임).
포스트 커버로 전용할 경우를 대비한 장면 서술 초안:

> A single sheet of oxidized copper on dark stone, one lifted corner catching a
> cyan edge of light against warm patina

101자. 장면 서술이며 데이터 주장 없음.

## 생성 명령 (Step 3A)

```bash
codex exec '$imagegen 아래 프롬프트로 이미지를 생성해서
/workspaces/ai-tech-blog/assets/img/og-default-raw.png 에 저장해줘.

<위 완성 프롬프트 전체>'
```

색상 수 확인 → 5,000색 미만이면 코드 렌더이므로 폐기하고 재생성.

## 정규화

```bash
python3 .claude/hooks/optimize_image.py assets/img/og-default-raw.png --cover \
    -o assets/img/og-default.jpg
rm assets/img/og-default-raw.png
```

`_config.yml`의 `social_preview_image`를 `.png` → `.jpg`로 함께 수정한다
(§4: 질감을 가진 화상은 PNG로 1200×630을 200KB에 담을 수 없다).

근거 대응표는 없다 — 클래스 A는 대응시킬 값이 없다 (§1).
