# 이미지 팩 — mcp-registry-report-2026

- **슬러그**: `mcp-registry-report-2026`
- **포맷**: F (벤치마크 리포트)
- **클러스터**: `CLUSTER_DEVTOOLS`
- **이미지 구성**: 커버 1장만. **서술 도형 0장**

## 서술 도형을 만들지 않은 이유

Format F의 도형 예산은 1~2장이지만 `IMAGE_GUIDE.md` §3의 기본값은 0장이고,
"표로 표현 가능하면 표를 쓴다"가 규칙이다. 이 포스트가 주장하는 값은 전부
**순위표·라벨 분포표·수집 파라미터표**로 이미 표현돼 있다. 흐름도 계층도 시간축도
없다. 도형을 넣으면 표를 그림으로 옮기는 중복이므로 만들지 않는다.

따라서 **근거 대응표도 없다** (대응시킬 그림 요소가 없다). 훅 C10은 본문에 body
figure가 있을 때만 이 표를 요구한다.

## 커버 — 소재 선택과 근거

| 항목 | 값 |
|---|---|
| 클러스터 시각 세계 | 정밀 기계와 공구 (`IMAGE_GUIDE.md` §8) |
| 선택 소재 | 기계 가공된 황동 스퍼 기어 1개 |
| 저장 경로 (원본) | `assets/img/posts/mcp-registry-report-2026-cover-raw.png` |
| 최종 경로 | `assets/img/posts/mcp-registry-report-2026-cover.jpg` (1200×630, ≤200KB) |

**같은 클러스터 최근 커버와의 중복 회피**

| 포스트 | 기존 소재 | 충돌 |
|---|---|---|
| `best-ai-coding-tools-2026` | 선반 가공 강철 실린더, 나선형 공구 자국 | 회피 — 선반 절삭면 제외 |
| `ai-content-quality-gates-2026` | 산화된 구리 시트 | 회피 — 판재 제외 |

**풀에서 제외한 소재와 이유**

- 캘리퍼 / 마이크로미터 / 강철 자 → 눈금이 읽히면 P6 하드 리젝. §6 AVOID의
  `readable scales`가 살아 있어도 눈금 자체가 소재의 정체성이라 위험이 크다
- 정밀 드릴 비트 **배열** → "셀 수 있는 반복 요소"(P6)에 정면으로 해당
- 선반 절삭면 → 위 표대로 이미 사용됨

**기어를 택한 판단**: §8이 `기어 트레인`을 이 클러스터의 승인 소재로 명시한다.
기어 이(teeth)는 반복 요소이지만 수량을 주장하지 않는 표면 질감이며, 본문의 어떤
수치와도 대응되지 않는다. 다만 P6 경계에 가까우므로 **단일 기어**로 한정하고
(트레인 = 복수 기어 = 개수 암시 회피), 프롬프트에서 대부분의 이를 그림자와
얕은 심도에 두도록 지시했다. 검수 시 이 지점을 최우선으로 본다.

## 완성 프롬프트 (§7 템플릿 + §6 스타일 블록 — 축약 금지)

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A single machined brass spur gear, solid and heavy, with a smooth
polished hub and a faintly turned surface finish.

SCENE: The gear rests at a slight angle on a dark slate surface, tipped so one
edge lifts away from the stone. Most of its rim falls into deep shadow and soft
focus; only a short arc of the near edge is sharp.

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

## alt 초안 (장면 서술 — 데이터 주장 금지)

```
A single brass gear tipped against dark slate, one edge sharp under raking cyan light while the rest of its rim falls into shadow
```

126자로 상한(125자)을 1자 넘겨 아래로 확정한다:

```
A brass gear tipped against dark slate, one edge sharp under raking cyan light while the rest of the rim falls into shadow
```

→ 121자. 장면만 서술하고 레지스트리·소유권·순위 등 본문의 어떤 주장도 담지 않는다.

**폐기한 초안**: `"A registry shelf of identical labelled boxes where a few labels point to
boxes on a different shelf entirely"` — 이것은 포스트의 핵심 주장(소유권 오귀속)을
시각적 은유로 옮긴 것으로, `IMAGE_GUIDE.md` §5의 클래스 A alt 하드 리젝에 해당한다.
커버는 아무것도 주장하지 않아야 하므로 alt도 주장하면 안 된다.

## 반입 검증 결과 (2026-08-17 수행, 전 항목 통과)

생성 도구는 **Gemini** (파일명 `Gemini_Generated_Image_6annmd6annmd6ann.png`).

| # | 항목 | 결과 |
|---|---|---|
| 1 | 파일 탐색 | 생성 시각 기준으로 발견. 벤더 파일명 그대로 도착 |
| 2 | 원본 규격 | 2752×1536 (비 1.7917) |
| 3 | **색상 수 74,762** | 기준 5,000 초과 → **이미지 모델 산출물 확정** (코드 렌더 아님) |
| 4 | 레터박스 | **실재.** 행 평균으로 판정 — 상단 0~146, 하단 1435~1535이 평균 8.1로 균일. 콘텐츠 y=147~1434 (높이 1288) |
| 5 | 가시 워터마크 | **있음** — Gemini ✦, 원본 우하단 약 (2690, 1380) |
| 6 | 워터마크 처리 | 레터박스 제거 후 `--cover`의 대칭 센터 크롭이 x=149~2602를 남겨 **프레임 밖으로 배제**. 리터칭·덮어쓰기 없음 |
| 7 | 정규화 | 1200×630 JPEG, **68KB** (상한 200KB), 47,704색 (훅 C11 기준 1,000 초과) |
| 8 | 육안 검수 | 통과 — 아래 |

**육안 검수 세부**

- P6(값으로 읽히는 요소): 막대·축·눈금·계기판 **없음**
- §6 AVOID 금지 소재: 텍스트·숫자·로고·로봇·사람·뇌·회로기판·홀로그램 **없음**
- 구도: 단일 피사체가 좌측 1/3, 우측은 큰 여백 — §7 준수
- 조명: 좌측 시안 키 + 우측 앰버 림, 방향 일관
- 크롭 후 기어 온전, 잘림 없음

**P6 경계 판단 기록**: 기어 이(teeth)는 셀 수 있는 반복 요소다. 그러나 본문의 어떤
수치와도 대응되지 않는 표면 질감이고, §8이 `기어 트레인`을 이 클러스터의 승인 소재로
명시하므로 P6의 취지(수량 주장)에 해당하지 않는다고 판단했다. 이미 발행된
`best-ai-coding-tools-2026` 커버의 나선형 공구 자국도 같은 성격이며, 그 선례와
일관되게 처리했다.

## 출처 메타데이터 — 규칙 충돌을 기록한다

원본 PNG에는 **C2PA 매니페스트가 실재한다** (`caBX` 청크 33,011바이트).

| 항목 | 값 |
|---|---|
| 발급 | Google C2PA Media Services 1P ICA G3 / Google C2PA Root CA G3 |
| 생성기 | Google C2PA Core Generator Library |
| 타임스탬프 | Google Core Time Stamping Authority T1 |
| 활성 매니페스트 | `urn:c2pa:4d45a2de-95e5-4066-6563-4974d4487ec3` |
| 인그리디언트 | `urn:c2pa:0e10a4de-…`, `urn:c2pa:4dd1839f-…`, `urn:c2pa:fca990cc-…` |
| 어설션 | `c2pa.created`, `c2pa.edited`, `c2pa.converted`, `c2pa.hash.data` |

**발행되는 `.jpg`에는 이 매니페스트가 없다.** 제거한 것이 아니라 **보존이 불가능**하다 —
C2PA 서명은 픽셀 데이터에 암호학적으로 결속되므로, 워터마크 배제를 위한 크롭과
JPEG 재인코딩을 거치는 순간 서명 검증이 실패한다. 원본을 부모 인그리디언트로 삼는
파생 매니페스트를 새로 발급하려면 우리 서명 인증서가 필요한데 보유하고 있지 않다.

> **`IMAGE_GUIDE.md`의 두 규칙이 충돌한다.** §10은 가시 워터마크를 크롭으로 배제하라고
> 요구하고, §11은 출처 메타데이터 제거를 하드 리젝으로 금지한다. 크롭은 필연적으로
> C2PA 서명을 무효화하므로 두 규칙을 동시에 만족시킬 수 없다. 가이드 개정이 필요하다.

**택한 처리**: 매니페스트를 온전히 보유한 원본을 `mcp-registry-report-2026-cover-source.png`로
보관하고 `.gitignore`에 등록했다(5.9MB). 위 표가 커밋되는 텍스트 출처 기록이다.
매니페스트를 위조하거나 제거 사실을 감추지 않는다.

**남는 한계**: 비가시 워터마크(SynthID 등)가 발행본에 잔존하는지는 우리가 검증할
수단이 없다.
