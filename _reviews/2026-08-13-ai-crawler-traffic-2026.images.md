# 이미지 프롬프트 팩 — ai-crawler-traffic-2026

- **슬러그**: `ai-crawler-traffic-2026`
- **포맷**: F (벤치마크 리포트) — 권장 총계 2~3장
- **클러스터**: `CLUSTER_AEO`
- **이번 제작 범위**: 커버 1장만 (클래스 A). 서술 도형 0장.

## 서술 도형을 만들지 않은 이유

Format F의 도형 예산은 1~2장이지만 §3의 기본값은 0장이고, 도형은 "표가 표현하지
못하는 관계"에만 쓴다. 이 포스트의 주장은 전부 **크기 비교와 순위**다 — 5,227 대 7,
에이전트별 요청 수, 엔드포인트별 읽기 수. 전부 표가 더 정확하게 전달하며, 본문에
이미 표 4개로 들어가 있다. 흐름·계층·시간축에 해당하는 주장이 없으므로 도형을
만들면 표의 중복이 된다.

예외 후보였던 8월 1일 버스트(13개 이름 / 30ms)는 시간축 주장이지만, 값이 사실상
"전부 같은 시각"이라 도형으로 그리면 30밀리초를 시각적으로 늘려야 하고 그 순간
T1(형태가 값을 나타내면 실제 비율을 지킨다)이 깨진다. 본문 문장으로 두는 것이 맞다.

---

## 커버 (클래스 A)

### 소재 선택 근거

- `CLUSTER_AEO` → §8 소재 풀의 "그 외 / 신규" = **지질과 재료**
- 같은 클러스터 최근 3장과 중복 회피:
  | 슬러그 | 기존 소재 |
  |---|---|
  | `ai-crawler-ecosystem-2026` | 밴딩 마노 (agate) |
  | `ai-overviews-seo-2026` | 흑요석 파편 |
  | `chatgpt-ads-2026-aeo-reddit-citations` | 주조 유리 블록 |
- 선택: **철질 운석 파편 (iron meteorite, fusion crust)**. 지질·재료 세계에 속하고,
  위 3장 및 타 클러스터의 석영·황철석·현무암 코어·산화 구리와도 겹치지 않는다.
- **P6 점검**: 막대·축·눈금·계기판 없음. 셀 수 있는 반복 요소 없음 — 단일 덩어리
  하나이며, 표면 질감은 불규칙해서 수량으로 읽히지 않는다. 절단·연마면
  (비트만슈테텐 무늬)은 격자 패턴으로 읽힐 수 있어 **의도적으로 제외**했다.

### 완성 프롬프트

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single fist-sized iron meteorite fragment with a matte, softly
pitted fusion crust, its surface irregular and non-repeating.

SCENE: The fragment rests at a slight tilt on a slab of rough dark stone, one
shoulder of the mass lifted just clear of the surface so a thin shadow runs
beneath it.

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

### alt 초안 (장면 서술 — 데이터 주장 없음)

```
A single pitted iron meteorite fragment tilted on rough dark stone, amber light on one face and cyan raking the other
```

116자. 보이는 것만 서술했고 수치·비교·주장을 담지 않았다. 생성물 육안 검수 후
실제 조명 방향(좌측 하단 앰버 / 우측 시안)에 맞춰 초안에서 수정했다.

### 육안 검수 결과 (2026-08-13)

| 점검 항목 | 결과 |
|---|---|
| 값으로 읽히는 요소 (막대·축·눈금·계기판·반복 요소) | 없음 — 불규칙 단일 덩어리 |
| §6 AVOID 금지 소재 (로봇·사람·뇌·회로기판·HUD·구운 텍스트) | 없음 |
| 피사체 수 | 1개, 좌측 3분할 배치 |
| 조명 일관성 | 프레임 전체에서 앰버(좌) / 시안(우) 방향 일치 |
| 상하 크롭 후 피사체 온전성 | 온전 |
| alt 성격 | 장면 서술 (데이터 주장 없음) |
| 클러스터 시리즈감 | 어두운 암반 위 단일 표본 — 기존 `CLUSTER_AEO` 3장과 일관 |

> 초안 작성 시점의 alt("A long corridor of glass doors standing open…")는 폐기했다.
> 유리문의 연속 배치가 **셀 수 있는 반복 요소**라 P6에 걸릴 소재였고, `CLUSTER_AEO`의
> 지질·재료 시각 세계에도 속하지 않았다.

### 저장 경로와 규격

| 항목 | 값 |
|---|---|
| 원본 | `assets/img/posts/ai-crawler-traffic-2026-cover-raw.png` (2048×1152) |
| 최종 | `assets/img/posts/ai-crawler-traffic-2026-cover.jpg` (1200×630, ≤200KB) |
| 정규화 | `python3 .claude/hooks/optimize_image.py …-cover-raw.png --cover -o …-cover.jpg` |

### 근거 대응표

**없음.** 커버는 클래스 A이며 어떤 값도 주장하지 않는다 (§1). 대응시킬 값이 존재하지
않으므로 표를 만들지 않는다 — 표가 필요해지는 순간 그 커버는 P6 위반이다.
