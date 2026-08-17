# 이미지 프롬프트 팩 — ai-agent-payments-crawl-toll-2026

- **슬러그**: `ai-agent-payments-crawl-toll-2026`
- **포맷**: F (벤치마크 리포트) — 권장 총계 2~3장
- **클러스터**: `CLUSTER_AEO`
- **제작 대상**: 커버 1장 (클래스 A)만. **서술 도형 0장**

## 서술 도형을 만들지 않은 이유

Format F는 서술 도형 1~2장이 권장치지만 `IMAGE_GUIDE.md` §3의 기본값은 0장이고,
"표로 표현 가능하면 표를 쓴다"가 판단 기준입니다. 이 글의 값은 전부 2차원 표로
완결됩니다 — 통행료 사다리(단가 × 4열), Cloudflare 출시 상태표. 흐름·계층·시간축처럼
표가 표현하지 못하는 관계가 없으므로 도형이 새 정보를 더하지 않습니다.

따라서 **근거 대응표는 이 문서에 없습니다.** 대응시킬 값을 그리지 않기 때문입니다
(§1 — 커버는 클래스 A, T1~T7 면제).

---

## 클래스 A — 커버

### 소재 선택 근거

`CLUSTER_AEO`는 §8 표에 고유 항목이 없으므로 **"그 외 / 신규 → 지질과 재료"** 를 씁니다.

같은 클러스터의 기존 커버 4장:

| 포스트 | 소재 | 형태 |
|---|---|---|
| chatgpt-ads-2026-aeo-reddit-citations | 주조 유리 블록 | 각진 블록, 투명 |
| ai-crawler-ecosystem-2026 | 줄무늬 마노 | 타원 파편, 광물 |
| ai-overviews-seo-2026 | 흑요석 파편 | 불규칙 파편, 유리질 |
| ai-crawler-traffic-2026 | 철질 운석 파편 | 불규칙 파편, 금속질 |

넷 다 **불규칙 파편 또는 블록**입니다. 형태 축에서 확실히 갈리도록 §8 소재 풀 중
아직 쓰지 않은 **암석 시추 코어(rock drill core)** 를 고릅니다 — 기계 절단된 원통이라
기존 4장 어느 것과도 실루엣이 겹치지 않습니다.

**의도적으로 피한 것**: 초안 단계의 alt에 있던 "황동 개찰구(brass turnstile)"는
통행료라는 본문 주제의 시각적 은유입니다. §1이 명시적으로 금지하는 방식이고
(*"포스트의 주장을 시각적 은유로 번역하려 하지 마라"*), 클러스터 시각 세계와도
맞지 않아 폐기했습니다.

**P6 위험 점검**: 코어 표면의 시추 자국이 반복 요소로 읽힐 수 있으므로 프롬프트에서
`faint`로 억제하고, §6 AVOID의 `readable scales` 조항을 그대로 유지합니다.
코어는 **정확히 1개**만 둡니다 (여러 개를 나란히 두면 셀 수 있는 반복 요소가 됩니다).

### 완성 프롬프트

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single cylindrical rock drill core — a machine-cut stone cylinder
roughly a hand's length, its flat cut face exposing fine mineral grain, faint
tool marks running along the curved side.

SCENE: The core rests at a slight angle against a low ridge of dark rough
stone, one end raised so the cut face catches the light and the far end falls
into shadow.

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

### alt 초안 (클래스 A — 장면 서술)

```
A single cylindrical rock core resting at an angle on dark stone, cyan light raking its cut face and amber along one edge
```

120자. 장면만 서술하며 데이터 주장 없음 (§5, C2 25~125자 충족).

### 생성 명령

```bash
codex exec '$imagegen 아래 프롬프트로 이미지를 생성해서
/workspaces/ai-tech-blog/assets/img/posts/ai-agent-payments-crawl-toll-2026-cover-raw.png 에 저장해줘.

<위 완성 프롬프트 전체>'
```

### 검증 순서

1. **색상 수** (`$imagegen` 호출 증거, 원본 PNG 기준 5,000색 초과)
2. **정규화** — `optimize_image.py --cover` → 1200×630 JPEG, 200KB 이하
3. **육안 검수** (`Read`) — 값으로 읽히는 요소, §6 AVOID 금지 소재, 상하 크롭 후 피사체 온전성
4. `image_validation.py --report` → 슬러그 `OK`
