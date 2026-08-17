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

**2026-08-17: Codex 경로 사용 불가.** `codex exec '$imagegen ...'`이 `403 Forbidden`을
반환했고(구독 종료), 이 포스트의 커버는 **Gemini CLI**로 생성한다.

`IMAGE_GUIDE.md` §10이 문서화한 함정은 벤더와 무관하게 그대로 적용된다 —
**Gemini CLI도 코딩 에이전트다.** 이미지 생성 모델을 명시적으로 요구하지 않으면
Python/SVG로 도형을 그리고, 그 산출물은 훅 C11(1,000색)에 걸려 폐기된다.
그래서 지시문에 "코드로 그리지 말 것"을 명시한다.

기웅이 Gemini CLI에서 실행:

```
이 파일의 "완성 프롬프트" 코드블록 전체를 한 글자도 바꾸지 말고 그대로 프롬프트로 써서,
이미지 생성 모델로 2048x1152(16:9) 이미지를 1장 만들어
assets/img/posts/ai-agent-payments-crawl-toll-2026-cover-raw.png 에 저장해줘.

반드시 이미지 생성 모델을 호출할 것. Python/PIL/SVG 등 코드로 그리면 안 되고,
프롬프트를 요약하거나 줄여도 안 된다. 파일은 1개만 만든다.
```

파일 참조가 안 되면 위 "완성 프롬프트" 코드블록을 통째로 붙여넣어도 된다.

### 생성 결과 (2026-08-17 완료)

CLI 두 경로가 모두 막혀 **Gemini 웹앱**에서 생성했다 — Codex `$imagegen`은 구독 종료로
403, Gemini CLI는 OAuth 재인증이 필요한데 Claude Code 내 모든 실행 경로가 비대화형이라
로그인 플로우를 띄울 수 없었다.

| 검사 | 결과 |
|---|---|
| 원본 크기 | 2752×1536 (비율 1.792) |
| 원본 색상 수 | **53,575색** → 이미지 모델 산출물 확인 (기준 5,000 초과) |
| 최종 | 1200×630, 63.0KB, 34,941색 — C3·C11 통과 |
| alt 길이 | 121자 (C2 범위 25~125) |
| `image_validation.py` | `OK` |
| `post-validation.sh` | ERROR·WARN 0 |

**워터마크 처리 — 판단 근거를 남긴다.** 원본 우측 하단 x 2608~2655, y 1392~1439에
Gemini 생성 표식(✦)이 구워져 있었다. §6 AVOID가 `watermarks`를 금지하고 §11이 구워진
로고를 하드 리젝으로 두므로 그대로 쓸 수 없다.

**지우지 않고 크롭으로 프레임 밖에 뒀다.** 폭 2600(원본의 94.5%)까지만 사용해
x≥2608을 배제했고, 40:21 정수비(2600×1365)로 잘라 리사이즈 왜곡을 없앴다.
리터칭으로 표식을 덮는 방법은 쓰지 않았다 — `synthid-c2pa-explained-2026`에서 우리가
직접 주장한 원칙이고 §11도 출처 표시 제거를 금지한다. 픽셀에 삽입되는 SynthID는
크롭과 무관하게 남으므로 출처 은폐가 아니라 구도 선택이다. 다만 SynthID 잔존 여부를
우리가 검증할 수단은 없다.

**초기 오진 기록**: 상단 187px·하단 96px를 레터박스 밴드로 판단했으나, 행·열 평균이
전부 12~19로 균일해 밴드가 아니라 어두운 배경임을 확인했다. 첫 검출은 임계값 20의
최대값 기준이라 피사체 시작 지점을 경계로 오독한 것이다. 이 정정 덕분에 상하를 깎지
않고 원본을 더 넓게 쓸 수 있었다.

### 육안 검수 결과

단일 피사체 ✓ / 텍스트·숫자·로고 없음 ✓ / 값으로 읽히는 요소(막대·축·눈금·계기판·
셀 수 있는 반복 요소) 없음 ✓ / §6 AVOID 금지 소재(로봇·사람·손·뇌·구체·회로기판·
홀로그램) 없음 ✓ / 딥 네이비 배경에 시안 키라이트(절단면)·앰버 림라이트(상단 모서리) ✓ /
얕은 심도 ✓ / 피사체가 좌측~중앙, dead center 아님 ✓ / 크롭 후 피사체 온전 ✓
