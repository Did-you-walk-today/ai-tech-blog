# 이미지 프롬프트 팩 — best-ai-coding-tools-2026

## 대상

| 항목 | 값 |
|---|---|
| 슬러그 | `best-ai-coding-tools-2026` |
| 포맷 | A (도구 비교) |
| 클러스터 | `CLUSTER_DEVTOOLS` |
| 이미지 예산 | 커버 1장 (§3 Format A = 1~2, 서술 도형 0장) |
| 클래스 | A — 표지 이미지. 값을 주장하지 않는다 |

## 소재 선택과 근거

**선택: 선반(lathe)으로 갓 절삭된 강철 원통 1개.**

- `CLUSTER_DEVTOOLS`의 시각 세계는 §8에서 **정밀 기계와 공구**로 고정돼 있고,
  소재 예시 중 "선반 절삭면"에 해당한다.
- 이 클러스터는 발행 0건이라 중복 회피 대상 커버가 없다. 이 커버가 클러스터의
  첫 시각 기준점이 된다.
- **캘리퍼·마이크로미터·강철 자를 의도적으로 배제했다.** 세 소재 모두 눈금이
  실물에 새겨져 있어 §6 AVOID의 `readable scales` 조항과 정면으로 충돌한다.
  독자가 눈금을 값으로 읽는 순간 P6 위반이고 하드 리젝이다.
- **기어 트레인·드릴 비트 배열도 배제했다.** 톱니와 비트는 셀 수 있는 반복
  요소라 수량을 암시한다 (P6).
- 남은 것이 절삭면이다. 나선형 공구 자국은 연속적인 표면 질감이라 세어지지 않고,
  절삭 금속 특유의 광택이 §6의 측광(raking light)과 잘 맞는다.

서술 도형은 만들지 않는다. 본문의 가격·벤치마크 비교는 전부 표로 표현되며,
표가 표현하지 못하는 흐름·계층·시간축이 본문에 없다 (§3 기본값 0장).

## 완성 프롬프트

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: One solid steel cylinder, roughly the size of a fist, freshly turned
on a lathe — a continuous helical tool path wrapping its curved flank, one
crisply chamfered end face, faint bluing from cutting heat near the shoulder.

SCENE: The cylinder rests on its side on a dark matte stone slab, angled slightly
away from the viewer so the machined flank catches the light along its length,
with a fine curl of steel swarf settled on the stone beside it.

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
A lathe-turned steel cylinder resting on dark stone, helical tool marks catching a raking cyan light
```

101자. 장면 서술이며 데이터 주장이 없다 (§5 클래스 A 규칙).

**교체 대상**: 현재 드래프트의 alt는 `"Best AI coding tools 2026 pricing and
benchmark comparison — Claude Code, Cursor, GitHub Copilot, Windsurf"`로,
커버가 하지 않는 주장(가격·벤치마크 비교)을 하고 있어 §11 클래스 A 하드 리젝
조건("alt가 커버에 없는 사실을 주장함")에 해당한다. 반드시 위 문안으로 바꾼다.

## 저장 경로 · 규격 · 명령

| 항목 | 값 |
|---|---|
| 원본 | `assets/img/posts/best-ai-coding-tools-2026-cover-raw.png` (2048×1152) |
| 최종 | `assets/img/posts/best-ai-coding-tools-2026-cover.jpg` (1200×630, ≤200KB) |
| frontmatter | `image.path`를 `.png` → **`.jpg`로 교체** (2026-07-28 `deb2c8c` 이후 `.png` 커버는 ERROR) |

```bash
codex exec '$imagegen <위 완성 프롬프트 전체>'
python3 -c "from PIL import Image; im=Image.open('assets/img/posts/best-ai-coding-tools-2026-cover-raw.png').convert('RGB'); n=len(im.getcolors(maxcolors=999999) or []); print(im.size, n, 'colors', '→ OK' if n>5000 else '→ 코드 렌더. 폐기')"
python3 .claude/hooks/optimize_image.py assets/img/posts/best-ai-coding-tools-2026-cover-raw.png --cover -o assets/img/posts/best-ai-coding-tools-2026-cover.jpg
rm assets/img/posts/best-ai-coding-tools-2026-cover-raw.png
```

근거 대응표는 없다 — 클래스 A는 대응시킬 값이 없다 (§1).
