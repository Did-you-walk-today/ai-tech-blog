# IMAGE_GUIDE.md — 포스트 이미지 제작 규칙

이 문서는 jsonhouse.com 포스트에 들어가는 **모든 이미지**의 생성·검증 규칙이다.
이미지를 만들기 전에 반드시 읽는다. `post-images` 스킬의 Step 0 필독 문서.

**2026-07-26 전면 개정.** 개정 이유는 §1에 있다. 이전 판의 "커버는 핵심 주장의
도식이다" 규칙은 폐기됐다.

---

## 0. 전략적 위치 — 이미지는 왜 "최소한"이어야 하는가

CLAUDE.md의 판정 기준은 하나다: **"AI 에이전트가 이걸 소비할 수 있는가."**
이미지는 그 기준에서 기여도가 사실상 0이다. 에이전트는 표와 JSON을 읽지, PNG를 읽지 않는다.

그래서 이미지는 다음 3가지 목적에만 존재한다:

1. **og:image** — 소셜 카드, Google Discover 후보 진입. 커버 1장이 이 역할 전부를 한다.
2. **표로 표현 불가능한 관계** — 흐름·계층·시간축. 도식이 표보다 나은 경우에만.
3. **AdSense 페이지 체류 품질** — 스크롤 피로 완화. 단, 페이지 속도를 깎으면 순손실.

여기에 해당하지 않는 이미지는 **넣지 않는다**. 장식용 이미지는 용량만 늘리고
Core Web Vitals를 깎는다.

---

## 1. 이미지는 두 계층이다 (가장 중요 — 나머지 규칙의 뿌리)

이 블로그의 이미지 사고는 전부 이 하나에서 갈린다:

> **이 이미지는 본문의 값을 주장하는가?**

답에 따라 **생성 도구가 완전히 달라진다.** 섞으면 반드시 사고가 난다.

| | **클래스 A — 표지 이미지 (Cover art)** | **클래스 B — 서술 도형 (Explanatory figure)** |
|---|---|---|
| 역할 | og:image, 소셜 카드, 시각적 진입점 | 본문의 관계·흐름·수량 설명 |
| 값을 주장하는가 | **아니오. 절대로.** | 예. 그게 존재 이유다 |
| 생성 도구 | **이미지 생성 모델.** Claude Code는 생성하지 못한다 — 프롬프트를 만들어 기웅에게 요청한다 (§10) | **코드만** (Python/SVG). Claude Code가 직접 만든다. 이미지 모델 금지 |
| T1~T7 진실성 규칙 | **면제** — 주장이 없으면 틀릴 수 없다 | **전면 적용** |
| 근거 대응표 | 불필요 | **필수** |
| alt 성격 | 장면의 사실적 서술 | 그림이 주장하는 명제 |
| 개수 | 포스트당 1장 (필수) | 포맷별 예산 (§4) |

### 왜 이렇게 갈랐는가 — 2026-07-25 사고의 진짜 원인

이전 판은 "커버는 제목의 삽화가 아니라 **핵심 주장 1개의 도식**"이라고 요구했다.
그 요구가 커버를 클래스 B로 만들었고, 클래스 B를 이미지 모델에 맡기게 했다.
결과는 세 장 전부 실패였다 — 규격 검사는 100% 통과, 의미는 전부 어긋남.

실패는 프롬프트가 부실해서가 아니었다. `$imagegen`은 정상 호출됐고
gpt-image-2는 1730×909 산출물을 제대로 만들었다. 그런데:

- 금지한 **해칭을 스스로 추가**했다 (§5 `no fill patterns` 위반)
- 깔때기 단계별 개수가 8 → 6 → **7** → 6으로 나왔다 (단조성 위반)
- 다단계 도식에서 개체 도형이 원→사각→삼각→육각으로 **바뀌었다** (정체성 위반)
- 본문이 "Not published"인 값에 **명확한 끝점을 부여**했다

이건 프롬프트로 고칠 수 있는 종류가 아니다. OpenAI 자신이 문서에서 인정한다 —
gpt-image 계열은 *"may have difficulty placing elements precisely in structured
compositions"*. **정밀한 구조적 배치는 이 모델의 능력 밖이다.**

그래서 결론은 두 갈래다:

- **값을 그려야 한다면 → 이미지 모델을 쓰지 않는다.** 코드가 그린다. 그러면
  T1~T7은 사람이 눈으로 검증하는 규칙이 아니라 **코드 상수로 보장되는 성질**이 된다.
- **값을 그릴 필요가 없다면 → 값을 요구하지 않는다.** 커버가 그렇다. 커버의 역할은
  §0에 적힌 대로 og:image이지 정보 전달이 아니다. 소셜 카드에서 630px 도식을 읽는
  독자는 없다.

### "포스트와 무관한 커버"가 품질 저하가 아닌 이유

커버가 포스트 데이터를 지시하지 않게 되면, 커버는 **틀릴 수가 없다**.
잡지 표지가 기사의 수치를 그리지 않는 것과 같다. 표지는 톤을 전달하고,
데이터는 본문이 전달한다.

이 블로그는 `youtube-ai-monetization-2026`, `google-ai-content-penalties-2026`에서
"가치 없는 AI 생성물 = AI slop"이라고 직접 주장했다. **AI slop은 이미지가 예뻐서가
아니라 거짓을 말해서 slop이다.** 아무것도 주장하지 않는 표지 이미지는 자기모순이
아니라 편집 디자인이다. 반대로 비율이 틀린 도식은, 밋밋하게 그리든 화려하게 그리든
slop이다.

---

## 2. 핵심 원칙 6개

| # | 원칙 | 이유 |
|---|---|---|
| P1 | **값을 나타내는 시각화는 전부 코드로 만든다** | 이미지 모델은 길이·개수·순서를 통제하지 못한다. 벤더 문서가 인정한 한계다. `_data/` JSON을 입력으로 코드 생성 (`dataviz` 스킬) |
| P2 | 이미지 안에 텍스트를 굽지 않는다 | 오타 수정 불가, 번역 불가, 크롤러 파싱 불가. 설명은 캡션과 alt로 |
| P3 | **서술 도형**에만 있는 정보는 없다 | 클래스 B가 주장하는 사실은 본문 표나 문단에도 반드시 존재해야 한다. 클래스 A는 애초에 주장하지 않으므로 이 규칙의 대상이 아니다 |
| P4 | 스타일 토큰은 고정이다 | 매번 다른 화풍이면 브랜드가 없다. §6·§9의 토큰 블록을 글자 그대로 복사해 쓴다 |
| P5 | alt는 계층에 따라 다르다 | 클래스 A → 장면 서술. 클래스 B → 주장 문장. §5 참조 |
| P6 | **형태가 수량을 표현하면 그것은 클래스 B다** | "커버니까 대충"은 없다. 커버에 막대·축·눈금·셀 수 있는 반복 요소가 들어가는 순간 그것은 표지가 아니라 도형이며, 즉시 폐기 대상이다 |

P1과 P6은 **하드 리젝 조건**이다.

---

## 3. 포스트당 이미지 개수

**총 상한 5장 (커버 포함).** 포맷별 권장치:

| Format | 유형 | 커버 (A) | 서술 도형 (B) | 스크린샷 | 권장 총계 |
|---|---|---|---|---|---|
| A | 도구 비교 | 1 | 0~1 | 0 | **1~2** |
| B | 프롬프트 라이브러리 | 1 | 0 | 0 | **1** |
| C | 기술 가이드 | 1 | 0~1 | 2~3 | **3~4** |
| D | 구조화 데이터 | 1 | 0~1 | 0 | **1~2** |
| E | 워크플로/템플릿 | 1 | 1 | 0~2 | **2~4** |
| F | 벤치마크 리포트 | 1 | 1~2 | 0 | **2~3** |
| G | 주간 다이제스트 | 1 | 0 | 0 | **1** |

**커버 1장은 모든 포맷에서 필수.** 없으면 og:image가 404가 되고, 소셜 공유 카드가
빈 채로 뜨며, Discover 후보에서 빠진다.

서술 도형은 **0장이 기본값이다.** 표로 표현 가능하면 표를 쓴다. 도형은 코드로 만들어야
하므로 제작 비용이 있고, 그 비용을 정당화하지 못하는 도형은 만들지 않는다.

---

## 4. 파일 규격

| 용도 | 클래스 | 포맷 | 크기 | 용량 상한 | 비고 |
|---|---|---|---|---|---|
| 커버 (og:image) | A | **JPEG** | **1200×630** (고정) | **200KB** | sRGB. 1.91:1은 OG 표준 |
| 서술 도형 | B | **SVG 우선** | — | 100KB | 코드 생성물. 불가 시 PNG ≤150KB |
| 스크린샷 | — | WebP | 가로 ≤ 1600px | 150KB | 민감정보 마스킹 필수 |

경로는 전부 `assets/img/posts/`.

**커버가 PNG에서 JPEG로 바뀐 이유**: 표지 이미지는 질감·조명·심도를 가진다.
그런 화상은 PNG로 1200×630을 200KB에 담을 수 없다 (팔레트 양자화를 하면 밴딩이 생긴다).
JPEG q82~88이면 같은 화상이 80~150KB에 들어간다. 서술 도형은 반대로 색이 적고
경계가 날카로우므로 SVG/PNG가 맞다.

전환은 2026-07-28에 끝났다 — 커버 12장 전부 `.jpg`이고 `.png` 커버는 남아있지 않다.
검증기는 `.jpg`만 받는다. `.png` 커버는 200KB 예산을 넘기거나(픽셀당 0.27바이트),
넘지 않으려고 팔레트를 줄이면 C11(1,000색)에 걸린다. 둘 중 하나는 반드시 실패한다.

### 네이밍 (슬러그 정확히 일치)

```
{slug}-cover.jpg      커버 (1장, 필수)          ← 클래스 A
{slug}-fig1.svg       서술 도형 1, 2…           ← 클래스 B
{slug}-chart1.svg     수치 차트 1, 2…           ← 클래스 B
{slug}-shot1.webp     스크린샷 1, 2…
```

슬러그 변경 금지 규칙(CLAUDE.md)은 이미지 파일명에도 그대로 적용된다.

---

## 5. frontmatter · 본문 삽입 · alt

커버는 frontmatter에만 넣는다. 본문 최상단에 같은 이미지를 또 넣지 않는다.

```yaml
image:
  path: /assets/img/posts/{slug}-cover.jpg
  alt: "장면을 서술한 한 문장 (125자 이내)"
```

서술 도형은 마크다운으로 삽입하고, 바로 뒤에 캡션 한 줄을 붙인다.

```markdown
![Alt text stating the claim](/assets/img/posts/{slug}-fig1.svg)
_Figure 1. What the reader should take away from this diagram._
```

### alt 작성 규칙 — 계층마다 다르다

공통: 125자 이내, 영어. `"Image of"`, `"Chart showing"`, `"Diagram of"`로 시작 금지
(스크린리더가 이미 "이미지"라고 읽는다). 키워드 스터핑 금지.

**클래스 A (커버) — 장면을 사실대로 서술한다.**
커버는 아무것도 주장하지 않으므로, alt가 주장을 하면 **본문에 없는 사실을 alt가
만들어내는 셈**이 된다. 보이는 것만 적는다.

| 나쁨 | 좋음 |
|---|---|
| `"Context windows converge across five providers"` (커버는 그런 말을 하지 않는다) | `"A stack of glass prisms splitting a single cyan beam into separate paths on a dark surface"` |
| `"AI model comparison cover"` (라벨) | `"Machined brass calipers resting on a dark workbench under angled amber light"` |

**클래스 B (서술 도형) — 그림이 주장하는 명제를 문장으로 쓴다.**

| 나쁨 | 좋음 |
|---|---|
| `"AI crawler diagram"` | `"GPTBot and ClaudeBot fetch content at crawl time, while user-triggered fetchers bypass robots.txt entirely"` |

---

## 6. 클래스 A — 커버 스타일 토큰 (고정 — 수정 금지)

모든 커버 프롬프트에 **이 블록을 글자 그대로** 붙인다. 기웅 승인 없이 바꾸지 않는다.

```
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
```

`AVOID` 블록의 앞쪽 절반은 **P2와 P6을 강제**한다 — 텍스트·숫자·축·눈금이 들어가는
순간 커버가 클래스 B로 미끄러진다.

뒤쪽 절반은 **AI 클리셰 차단**이다. 이미지 모델의 기본값은 "빛나는 뇌 / 로봇 손 /
푸른 회로 기판 / 홀로그램 UI"이며 그건 2023년 AI 블로그의 클리셰다. 명시적으로 금지하지
않으면 반드시 나온다. 우리가 직접 "AI slop"을 비판한 블로그이므로 여기서 걸리면
논지가 무너진다.

---

## 7. 클래스 A — 커버 프롬프트 템플릿

작성 순서는 **용도 → 피사체 → 장면 → 구도 → 스타일 → 조명/색 → 비율 → 유지 조건 → 제외**다.
이 순서를 지키면 모델이 주제를 먼저 잡고 스타일을 나중에 입힌다.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: {§8 소재 풀에서 1개. 구체적인 실물 오브젝트로.}

SCENE: {그 피사체가 어떤 상태인가. 동작·배치를 한 문장으로.}

COMPOSITION: Wide horizontal establishing shot. One dominant subject placed on
the left or right third, not dead center. Clear foreground-to-background
separation with real depth. Keep the outer 8% of the top and bottom edges free
of critical detail — the frame is cropped to 1.91:1 afterwards.

[§6 STYLE / LIGHTING & COLOR / AVOID 블록 전체]

ASPECT RATIO: 2048x1152

MUST KEEP: Exactly one subject. Consistent light direction across the whole
frame. Large areas of unbroken dark background. Nothing that could be read as
a measurement.
```

### 구도 규칙이 생긴 이유

이전 판의 구도 지침은 `wide horizontal layout, empty margins on left and right`
한 줄뿐이었다. 수직 배치에 대한 지시가 없어서 결과물 12장이 **전부 세로 중앙
35% 밴드만 쓰고 위아래가 텅 빈** 같은 구도로 나왔다. §7의 COMPOSITION 블록은
그 재발을 막는 항목이다 — 3분할 배치, 심도 분리, 상하 안전 여백.

---

## 8. 클래스 A — 소재 풀 (클러스터별 고정)

커버는 포스트 내용과 무관해도 되지만 **아무거나는 아니다.** 클러스터마다 시각 세계를
고정하면 개별 글이 무관해도 블로그 전체에는 시리즈감이 생긴다.

| 클러스터 | 시각 세계 | 소재 예시 |
|---|---|---|
| `CLUSTER_LLM` | **광학과 굴절** | 유리 프리즘 적층, 렌즈 요소 분해, 광섬유 다발 단면, 수면의 빛 굴절, 두꺼운 유리 블록의 모서리 |
| `CLUSTER_DEVTOOLS` | **정밀 기계와 공구** | 황동 캘리퍼, 마이크로미터, 기어 트레인, 선반 절삭면, 정밀 드릴 비트 배열, 강철 자 |
| `CLUSTER_PROMPTS` | **직물과 인쇄** | 활자 케이스, 제본된 종이 단면, 직조 구조 확대, 실패에 감긴 실, 잉크가 종이에 번지는 순간 |
| 그 외 / 신규 | **지질과 재료** | 암석 코어 샘플, 지층 단면, 결정 성장, 금속 산화 표면, 콘크리트 볼트 구조 |

**소재에 눈금·숫자가 있는 실물(캘리퍼, 자, 마이크로미터)을 고를 때는** §6 AVOID의
`readable scales` 조항이 반드시 살아 있어야 한다. 눈금이 읽히면 P6 위반이다 —
독자가 그것을 값으로 읽는다.

---

## 9. 클래스 B — 서술 도형은 코드로 만든다

**이미지 모델 사용 금지.** 예외 없다.

입력은 `_data/YYYY-MM-DD-{slug}.json`이고, 출력은 SVG다. 차트는 `dataviz` 스킬을
먼저 읽는다. 도식(흐름·계층·관계)은 Python으로 SVG 문자열을 직접 쓰거나 PIL로 렌더한다.

### 도형 스타일 토큰 (고정)

서술 도형은 커버와 화풍이 달라도 된다 — 역할이 다르기 때문이다. 대신 도형끼리는
일관돼야 한다.

```
Background #0F172A. Primary accent #38BDF8. Secondary #94A3B8.
Highlight #F8FAFC. Warm accent #F59E0B (강조 1곳에만).
Stroke width 2px 고정. 채움 없음 또는 단색 채움.
해칭·빗금·격자 패턴 금지 (축소 시 모아레).
그라데이션·그림자·블러 금지.
구분은 선 스타일(실선/파선/점선)과 끝점 도형으로만.
파선·점선에 의미를 부여했다면 캡션이나 alt에 그 의미를 밝힌다.
밝히지 않을 거면 전부 실선으로 통일한다.
```

### T1~T7 진실성 규칙 (클래스 B 전용)

코드로 그리면 이 규칙들은 **검증 항목이 아니라 코드가 만족해야 할 사양**이 된다.
값을 상수 배열로 선언하고, 좌표를 그 상수에서 계산한다. 좌표를 손으로 적으면 T1이 깨진다.

| # | 규칙 | 코드에서의 의미 |
|---|---|---|
| **T1** | **형태가 값을 나타내면 실제 비율을 지킨다** | 길이 = `value / max(values) * axis_length`. 눈대중 좌표 금지 |
| **T2** | **결측·미공개 값은 길이로 그리지 않는다** | `None`인 항목은 끝점 없는 열린 선으로 렌더. 임의 길이 대입 금지 |
| **T3** | **개체 정체성을 보존한다** | 개체별 도형·색을 딕셔너리로 고정하고 모든 단계에서 재사용 |
| **T4** | **단조성을 지킨다** | 본문이 "좁혀진다"면 단계별 개수 배열이 단조 감소인지 `assert` |
| **T5** | **한 그림에 회계는 하나** | 단계별 잔존 수와 탈락 수의 합이 초기값과 같은지 `assert` |
| **T6** | **방향은 의미다** | 앞/뒤·좌/우·위/아래가 본문 용어와 일치하는지 확인 |
| **T7** | **본문이 N개로 갈린다면 그림도 N개를 보여준다** | 반복 요소 개수 = 본문 항목 배열의 `len()` |

**판정 순서**: 그림에서 값으로 쓰인 요소를 전부 나열한다 → 각각을 본문 어느 수치와
대응시킬 수 있는지 적는다 → 대응이 없는 요소가 하나라도 있으면 그 요소를 지운다.

---

## 10. 클래스 A 생성 경로 — Claude Code는 생성하지 못한다

**Claude Code에는 이미지 생성 도구가 없다.** 만들 수 있는 것은 코드로 그린 SVG/PNG뿐이고
그건 §11의 하드 리젝이다. 그러므로 커버는 **기웅이 생성하고, Claude Code는 프롬프트를
만들어 넘기고 돌아온 파일을 검증한다.** 이 역할 분담은 도구가 바뀌어도 변하지 않는다.

### 기웅에게 요청하는 방법 — 프롬프트를 답변에 통째로 붙인다

**프롬프트 팩 경로만 알려주지 않는다.** 기웅이 파일을 열고 코드블록을 찾아 복사해야 하는
마찰이 생기고, 그 과정에서 스타일 토큰이 잘려 나간다. 요청 답변 안에 **완성 프롬프트
전문을 그대로 붙여** 바로 복사할 수 있게 한다. 팩 파일에도 동일한 전문을 남긴다
(재현과 기록용이지 전달용이 아니다).

요청에 반드시 포함할 4가지:

1. **완성 프롬프트 전문** — §7 템플릿 + §6 스타일 블록. 요약·축약 금지
2. **가로세로비** — `16:9`. 이유는 아래 크기 절
3. **저장 경로** — `assets/img/posts/{slug}-cover-raw.png`
4. **코드로 그리지 말 것** — 아래 벤더 함정 참조

### 벤더 함정은 도구가 바뀌어도 그대로다

커버를 코딩 에이전트(Codex CLI, Gemini CLI 등)에게 시키면, 이미지 생성 모델을 명시적으로
요구하지 않는 한 **Python/SVG로 도형을 그린다.** 2026-07-25에 레포에 들어간 3~4색
4KB 커버 12장이 정확히 그 결과물이다. 기웅이 웹앱(이미지 생성 UI)을 직접 쓰면 이 위험이
없으므로 **웹앱 경로가 CLI 경로보다 안전하다.**

CLI를 쓰는 경우 지시문에 "이미지 생성 모델을 호출할 것, Python/PIL/SVG로 그리지 말 것"을
명시한다.

### 도구는 고정하지 않는다 — 검증이 고정이다

2026-08-17 기준 Codex `$imagegen`은 구독 종료로 403이고, Gemini CLI는 OAuth 재인증이
필요한데 Claude Code 내 모든 실행 경로가 비대화형이라 로그인 플로우를 띄울 수 없다.
그래서 **특정 벤더를 규칙에 박지 않는다.** 기웅이 쓸 수 있는 이미지 생성 서비스면 되고,
아래 검증만 통과하면 출처는 묻지 않는다.

### 반입 검증 — 순서 고정

**1) 파일이 실제로 왔는지 먼저 확인한다.** Codespaces는 원격 환경이라 웹앱에서 받은
이미지가 로컬 PC 다운로드 폴더에 있으면 여기로 오지 않는다. 파일명도 벤더가 붙인
그대로일 수 있으니 이름이 아니라 **최근 생성 시각**으로 찾는다:

```bash
find . -type f \( -iname "*.png" -o -iname "*.jpg" \) -newermt "YYYY-MM-DD" \
  -not -path "./_site/*" -not -path "./node_modules/*"
```

**2) 색상 수** — 이미지 모델 산출물인지 가리는 유일한 증거다. 벤더와 무관하게 적용한다:

```bash
python3 -c "
from PIL import Image; im=Image.open('경로').convert('RGB')
n=len(im.getcolors(maxcolors=99999999) or [])
print(im.size, n, 'colors', '→ OK' if n>5000 else '→ 코드 렌더. 폐기하고 재요청')"
```

이 5,000 기준선은 **정규화 전 원본**에 적용한다. 크롭·리사이즈·JPEG 인코딩을 거치면
색상 수가 절반 가까이 줄기 때문에(실측 3,500~35,000), 최종 `.jpg`를 검사하는 훅 C11은
더 낮은 1,000을 쓴다. 두 숫자 모두 3~4색 코드 렌더와는 자릿수가 다르다.

**3) 워터마크** — 생성 표식이 픽셀에 구워져 오는 벤더가 있다(Gemini의 ✦ 등).
§6 AVOID가 `watermarks`를 금지하므로 그대로 쓸 수 없다.

> **지우지 않는다. 크롭으로 프레임 밖에 둔다.**
> 리터칭으로 덮는 것은 `synthid-c2pa-explained-2026`에서 우리가 직접 주장한 원칙에
> 어긋나고, §11도 출처 표시 제거를 금지한다. 픽셀에 삽입되는 비가시 워터마크(SynthID 등)는
> 크롭과 무관하게 남으므로, 가시 표식을 구도 밖에 두는 것은 은폐가 아니라 구도 선택이다.
> 단 비가시 워터마크의 잔존 여부를 우리가 검증할 수단은 없다 — 팩에 그 한계를 적는다.

표식 위치는 눈이 아니라 픽셀로 특정한다:

```bash
python3 -c "
from PIL import Image
im=Image.open('경로').convert('L'); w,h=im.size; px=im.load()
bx=by=bv=-1
for y in range(int(h*0.85),h):
    for x in range(int(w*0.85),w):
        if px[x,y]>bv: bv,bx,by=px[x,y],x,y
print('밝은 지점 (%d,%d) lum=%d' % (bx,by,bv))"
```

### 크기 — 1200×630은 직접 생성할 수 없다

대부분의 이미지 모델이 임의 픽셀 크기를 받지 않는다(gpt-image 계열은 양변이 16의 배수여야
하고, 630은 16의 배수가 아니다). **16:9로 받아 1200×630으로 크롭한다.** §7 COMPOSITION의
"상하 8% 안전 여백"이 이 크롭을 위한 것이다.

크롭할 때 **40:21 정수비로 잘라 리사이즈 왜곡을 없앤다** (1200:630 = 40:21).
워터마크를 배제해야 하면 좌우 폭부터 줄인다 — 상하를 깎으면 §7이 확보해 둔 안전 여백을
이중으로 잃는다.

> **레터박스 오진 주의.** 행·열의 **최대값**으로 검은 밴드를 찾으면 피사체가 시작하는
> 지점을 프레임 경계로 오독한다. 2026-08-17에 이 방식으로 상단 187px·하단 96px를
> 레터박스로 잘못 판정했다. 실제로는 밴드가 없고 그냥 어두운 배경이었다.
> **행·열 평균**으로 판정한다 — 평균이 균일하면(예: 전 구간 12~19) 밴드가 아니다.

---

## 11. 하드 리젝 조건

하나라도 걸리면 그 이미지는 폐기하고 재생성한다.

**공통**

- 이미지 안에 텍스트/숫자/로고가 구워져 있음 (P2)
- 실제 제품 UI나 기업 로고를 모사함 (상표권)
- alt 누락, 또는 alt가 `"chart"`, `"diagram"` 수준의 라벨
- C2PA 등 생성 도구가 붙인 출처 메타데이터를 제거함
  (`synthid-c2pa-explained-2026`에서 우리가 직접 주장한 원칙)

**클래스 A (커버)**

- **커버가 값을 표현함** — 막대, 축, 눈금, 읽히는 계기판, 셀 수 있는 반복 요소로
  수량을 암시 (P6). 커버는 아무것도 주장하지 않아야 한다
- **alt가 커버에 없는 사실을 주장함** — 장면 서술이 아니라 데이터 주장을 씀
- 로봇·휴머노이드·사람 얼굴·손·뇌·빛나는 구체·회로기판·홀로그램 HUD 포함 (§6 AVOID)
- 코드 렌더 산출물임 — 이미지 모델 미호출. 원본 5,000색 미만 또는 정규화된
  JPEG 1,000색 이하 (훅 C11)
- **생성 도구의 가시 워터마크가 프레임 안에 남아 있음** (§6 AVOID `watermarks`).
  크롭으로 배제한다 — 리터칭으로 덮는 것은 위 "출처 메타데이터 제거" 금지와 같은 위반이다
- 크기가 1200×630이 아님 / 용량 200KB 초과

**클래스 B (서술 도형)**

- **이미지 생성 모델로 만듦** (P1 위반) — 무조건 폐기. 재생성이 아니라 코드로 다시 만든다
- §9의 T1~T7 중 하나라도 위반 — 특히:
  - 형태로 표현한 비율이 본문 실제 비율과 다름 (T1)
  - 본문이 "미공개/Not published"인 값에 구체적 형태를 부여함 (T2)
  - 본문이 여러 갈래라고 말하는데 그림은 하나로 압축함 (T7)
- 이미지에만 있고 본문에는 없는 정보가 있음 (P3)
- 해칭·빗금 등 채움 패턴 사용

---

## 12. 반입 후 정규화

```bash
# 커버: 2048x1152 원본 → 1200x630 JPEG, 200KB 이하
python3 .claude/hooks/optimize_image.py assets/img/posts/{slug}-cover-raw.png --cover \
    -o assets/img/posts/{slug}-cover.jpg

# 스크린샷: WebP 변환 + 가로 1600px + 150KB 이하
python3 .claude/hooks/optimize_image.py assets/img/posts/{slug}-shot1.png --figure
```

`--cover`는 리사이즈 전에 **센터 크롭**을 한다. 주요 요소를 중앙 세로 밴드에
두어야 하는 이유다. 정규화 후 `-raw.png` 원본은 삭제한다.

서술 도형(SVG)은 코드 생성물이므로 정규화 대상이 아니다.

---

## 13. 검증

훅이 자동으로 검사한다 (`post-validation.sh` Section C, 규칙 C1~C11).
`_drafts/`에서는 WARN, `_posts/`에서는 ERROR로 승격된다.

레포 전체 현황:

```bash
python3 .claude/hooks/image_validation.py --report
```

**훅이 잡지 못하는 것** — 사람이 `Read`로 이미지를 열어 직접 봐야 한다:

- 커버에 값으로 읽히는 요소가 있는가 (P6)
- 커버 alt가 장면 서술인가, 데이터 주장인가
- §6 AVOID 목록의 금지 소재가 들어갔는가
- 서술 도형이 근거 대응표대로 그려졌는가

발행(Phase 6) 전에 `--report`가 깨끗해야 한다.
