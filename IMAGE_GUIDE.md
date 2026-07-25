# IMAGE_GUIDE.md — 포스트 이미지 제작 규칙

이 문서는 jsonhouse.com 포스트에 들어가는 **모든 이미지**의 생성·검증 규칙이다.
이미지를 만들기 전에 반드시 읽는다. `post-images` 스킬의 Step 0 필독 문서.

---

## 0. 전략적 위치 — 이미지는 왜 "최소한"이어야 하는가

CLAUDE.md의 판정 기준은 하나다: **"AI 에이전트가 이걸 소비할 수 있는가."**
이미지는 그 기준에서 기여도가 사실상 0이다. 에이전트는 표와 JSON을 읽지, PNG를 읽지 않는다.

그래서 이미지는 다음 3가지 목적에만 존재한다:

1. **og:image** — 소셜 카드, Google Discover 후보 진입. 커버 1장이 이 역할 전부를 한다.
2. **표로 표현 불가능한 관계** — 흐름·계층·시간축. 도식이 표보다 나은 경우에만.
3. **AdSense 페이지 체류 품질** — 스크롤 피로 완화. 단, 페이지 속도를 깎으면 순손실.

여기에 해당하지 않는 이미지는 **넣지 않는다**. 장식용 이미지는 용량만 늘리고
Core Web Vitals를 깎는다. 게다가 이 블로그는 `youtube-ai-monetization-2026`,
`google-ai-content-penalties-2026`에서 "가치 없는 AI 생성물 = AI slop"이라고
직접 주장했다. 장식용 AI 이미지를 도배하면 자기 논지와 충돌한다.

---

## 1. 핵심 원칙 6개

| # | 원칙 | 이유 |
|---|---|---|
| P1 | **수치 차트는 이미지 생성 모델에 절대 맡기지 않는다** | 이미지 모델은 숫자를 지어낸다. 축·레이블·막대 길이가 실제 데이터와 무관해진다. 차트는 `_data/` JSON에서 코드로 생성 (`dataviz` 스킬) |
| P2 | 이미지 안에 텍스트를 굽지 않는다 | 오타 수정 불가, 번역 불가, 크롤러 파싱 불가. 설명은 캡션과 alt로 |
| P3 | 이미지에만 있는 정보는 없다 | 이미지가 주장하는 모든 사실은 본문 표나 문단에도 반드시 존재해야 한다. 이미지는 중복 표현일 뿐 |
| P4 | 스타일 토큰은 고정이다 | 매번 다른 화풍이면 브랜드가 없다. §5의 토큰 블록을 글자 그대로 복사해 쓴다 |
| P5 | alt는 라벨이 아니라 주장이다 | "비교 차트"가 아니라 "5개 프로바이더의 컨텍스트 윈도우는 5% 이내로 수렴했다" |
| P6 | **형태가 수량을 표현하면 그것은 차트다** | "개념도니까 대충"이 허용되는 영역은 없다. §6-4 참조 |

P1과 P6은 **하드 리젝 조건**이다. 실제 수치가 들어가는 그래프를 Codex/이미지 모델로 뽑아
쓰는 순간, 이 블로그의 유일한 자산인 데이터 신뢰도가 무너진다.

---

## 2. 포스트당 이미지 개수

**총 상한 5장 (커버 포함).** 포맷별 권장치:

| Format | 유형 | 커버 | 도식 | 차트 | 스크린샷 | 권장 총계 |
|---|---|---|---|---|---|---|
| A | 도구 비교 | 1 | 0~1 | 0 | 0 | **2** |
| B | 프롬프트 라이브러리 | 1 | 0 | 0 | 0 | **1** |
| C | 기술 가이드 | 1 | 0~1 | 0 | 2~3 | **3~4** |
| D | 구조화 데이터 | 1 | 0~1 | 0~1 | 0 | **2** |
| E | 워크플로/템플릿 | 1 | 1 | 0 | 0~2 | **2~4** |
| F | 벤치마크 리포트 | 1 | 0~1 | 1~2 | 0 | **3** |
| G | 주간 다이제스트 | 1 | 0 | 0 | 0 | **1** |

A/D가 2장인 이유: 이 포맷의 본체는 비교표다. 이미지를 늘리면 페이지 안의
정보 밀도(크롤러가 파싱할 텍스트 비율)가 떨어진다. 정확히 반대 방향이다.

**커버 1장은 모든 포맷에서 필수.** 없으면 og:image가 404가 되고, 소셜 공유 카드가
빈 채로 뜨며, Discover 후보에서 빠진다.

---

## 3. 파일 규격

| 용도 | 포맷 | 크기 | 용량 상한 | 비고 |
|---|---|---|---|---|
| 커버 (og:image) | PNG | **1200×630** (고정) | **200KB** | sRGB. 1.91:1은 OG 표준 — 벗어나면 크롭됨 |
| 본문 도식 | WebP | 가로 ≤ 1600px | 150KB | |
| 본문 차트 | **SVG 우선** | — | 100KB | 코드 생성물. 불가 시 WebP |
| 스크린샷 | WebP | 가로 ≤ 1600px | 150KB | 민감정보 마스킹 필수 |

경로는 전부 `assets/img/posts/`.

### 네이밍 (슬러그 정확히 일치)

```
{slug}-cover.png      커버 (1장, 필수)
{slug}-fig1.webp      도식 1, 2, 3…
{slug}-chart1.svg     차트 1, 2…
{slug}-shot1.webp     스크린샷 1, 2…
```

슬러그 변경 금지 규칙(CLAUDE.md)은 이미지 파일명에도 그대로 적용된다.
슬러그가 바뀌면 이미지 파일명·frontmatter·본문 참조가 전부 깨진다.

---

## 4. frontmatter 및 본문 삽입

커버는 frontmatter에만 넣는다. 본문 최상단에 같은 이미지를 또 넣지 않는다.

```yaml
image:
  path: /assets/img/posts/{slug}-cover.png
  alt: "이미지가 주장하는 사실 한 문장 (125자 이내)"
```

본문 이미지는 마크다운으로 삽입하고, 바로 뒤에 캡션 한 줄을 붙인다.

```markdown
![Alt text stating the claim](/assets/img/posts/{slug}-fig1.webp)
_Figure 1. What the reader should take away from this diagram._
```

### alt 작성 규칙

- 125자 이내, 영어 (포스트가 영어이므로)
- "Image of", "Chart showing", "Diagram of"로 시작 금지 — 스크린리더가 이미
  "이미지"라고 읽는다. 중복이다
- 그 이미지가 **주장하는 내용**을 문장으로. 명사 나열 금지
- 키워드 스터핑 금지. 자연스러운 문장 하나

| 나쁨 | 좋음 |
|---|---|
| `"LLM comparison chart 2026"` | `"Context windows converge within 5% across five providers while max output tokens still span 32K to 384K"` |
| `"AI crawler diagram"` | `"GPTBot and ClaudeBot fetch content at crawl time, while user-triggered fetchers bypass robots.txt entirely"` |

---

## 5. 스타일 토큰 (고정 — 수정 금지)

모든 이미지 생성 프롬프트 맨 앞에 **이 블록을 글자 그대로** 붙인다.
기웅 승인 없이 바꾸지 않는다. 바뀌는 순간 과거 커버와 화풍이 갈라진다.

```
STYLE: Flat vector, technical-editorial illustration.
Background #0F172A (deep navy), primary accent #38BDF8 (sky blue),
secondary accent #94A3B8 (slate), highlight #F8FAFC (near-white).
Thin 1.5px strokes, geometric shapes, generous negative space.
No gradients, no 3D render, no photorealism, no glossy highlights.
No hatching, no cross-hatching, no fill patterns — shapes stay unfilled or solid.
No human figures, no faces, no hands, no brains, no robots, no glowing orbs.
No text, no letters, no numbers anywhere in the image.
Clean, restrained, engineering-diagram feel.
```

마지막 두 줄이 핵심이다. AI 이미지 모델의 기본값은 "빛나는 뇌 / 로봇 손 /
푸른 회로 기판"이며, 그건 2023년 AI 블로그의 클리셰다. 명시적으로 금지해야 한다.

---

## 6. 프롬프트 템플릿

### 6-1. 커버 (모든 포스트)

커버는 **제목의 삽화가 아니라 핵심 주장 1개의 도식**이다.
"LLM 비교 글이니까 로고 여러 개" 같은 접근은 금지.

```
[§5 STYLE 블록 전체]

SUBJECT: {포스트의 핵심 주장을 시각적 은유 1개로. 20단어 이내}
COMPOSITION: Single centered concept, wide horizontal layout,
             empty margins on left and right for text overlay safety.
ASPECT RATIO: 1200x630 (1.91:1)
```

작성 예 — `best-llm-2026` (핵심 주장: 컨텍스트는 수렴했고 출력 한계는 갈라졌다):

```
SUBJECT: Five identical horizontal bars converging into one aligned edge
on the left, then fanning out into dramatically different lengths on the
right. Two axes implied, no labels.
```

### 6-2. 본문 도식 (관계·흐름·계층)

```
[§5 STYLE 블록 전체]

SUBJECT: {관계 구조를 서술. 노드와 연결의 의미를 명시}
COMPOSITION: {left-to-right flow | layered stack | radial hub}
ASPECT RATIO: 16:9
CONSTRAINT: Shapes must be distinguishable by form, not only by color
            (colorblind-safe). No text labels — captions live outside the image.
```

### 6-3. 차트 — **이미지 모델 사용 금지**

수치가 들어가는 모든 시각화는 `_data/YYYY-MM-DD-{slug}.json`을 입력으로
코드로 생성한다. `dataviz` 스킬을 먼저 읽고 SVG를 만든다.
이미지 모델에 "make a bar chart of these prices"라고 넣는 것은 P1 위반이다.

### 6-4. 진실성 규칙 T1~T7 (제출 전 자가 점검)

2026-07-25 `best-llm-2026` 이미지 3장이 규격은 100% 통과하고 의미는 전부 어긋난
사고에서 나온 규칙이다. 세 장의 실패 원인이 전부 여기 있다.

| # | 규칙 | 실패 사례 |
|---|---|---|
| **T1** | **형태가 값을 나타내면 실제 비율을 지킨다.** 길이·크기·개수·위치가 수량을 표현하는 순간 개념도가 아니라 차트다. 본문 값에 비례시키거나, 그 요소를 아예 그리지 마라 | 커버가 출력 한계 발산을 2.32:1로 그림. 본문 실제는 5.86:1 — 핵심 주장이 40% 세기로 축소됨 |
| **T2** | **결측·미공개 값은 길이로 그리지 않는다.** 본문이 "Not published"인 항목에 끝점을 주면 본문에 없는 사실을 이미지가 만들어낸다. 끝점 없는 열린 선으로 표현 | 커버가 Grok의 미공개 max output에 명확한 끝점을 부여 |
| **T3** | **개체 정체성을 보존한다.** 다단계 도식에서 같은 개체는 처음부터 끝까지 같은 도형·색을 유지한다 | fig2에서 관문마다 도형이 원→사각→삼각→육각으로 바뀌어 후보 추적 불가 |
| **T4** | **단조성을 지킨다.** 본문이 "좁혀진다/걸러진다/줄어든다"고 말하면 그림의 개수도 단조 감소해야 한다 | fig2 관문별 개수 8 → 6 → **7** → 6. 깔때기가 중간에 넓어짐 |
| **T5** | **한 그림에 회계는 하나.** 같은 그림에서 두 가지 세는 방식이 공존하면 안 된다 | fig2의 판 내부 개수(8/6/7/6)와 탈락 더미 합(11)이 서로 안 맞음 |
| **T6** | **방향은 의미다.** 앞/뒤·좌/우·위/아래가 본문 용어와 일치해야 한다 | fig1이 prefix 재사용 루프를 체인 **꼬리**에 붙임. 임계 미달 프롬프트를 임계선 **오른쪽**에 배치 |
| **T7** | **본문이 N개로 갈린다면 그림도 N개를 보여준다.** 대표 사례 하나로 축약하면 주장 자체가 사라진다 | fig1이 모델별 캐시 임계값 4종(512/1,024/2,048/4,096)을 수직선 **1개**로 압축. 섹션 제목이 "Side by Side"인데 나란히 놓을 대상이 없어짐 |

**판정 순서**: 그림에서 값으로 쓰인 요소를 전부 나열한다 → 각각을 본문 어느 수치와
대응시킬 수 있는지 적는다 → 대응이 없는 요소가 하나라도 있으면 그 요소를 지우거나
그림을 재설계한다. "보기 좋으니까 남긴다"는 없다.

### 6-5. 렌더링 일관성

한 포스트의 모든 이미지는 **같은 렌더링 파이프라인**으로 만든다.
커버는 고유색 4개 하드엣지 벡터인데 본문 도식은 1.7만 색 안티앨리어싱이면,
같은 글 안에서 질감이 갈려 따로 만든 티가 난다.

- 하드 엣지 벡터 렌더 (안티앨리어싱 최소)
- 해칭·빗금·격자 등 **채움 패턴 금지** — §5의 `no texture` 위반이며 축소 시 모아레가 생긴다
- 구분은 선 스타일(실선/파선/점선)과 끝점 도형으로만
- 선 스타일에 의미를 부여했다면 캡션이나 alt에 그 의미를 밝힌다.
  밝히지 않을 거면 전부 실선으로 통일한다 (파선·점선은 도면 관례상 "추정/미확정"으로 읽힌다)

---

## 7. 하드 리젝 조건

하나라도 걸리면 그 이미지는 폐기하고 재생성한다.

- 이미지 안에 텍스트/숫자/로고가 구워져 있음
- 실제 제품 UI나 기업 로고를 모사함 (상표권)
- 수치 차트를 이미지 생성 모델로 만듦 (P1 위반)
- 이미지에만 있고 본문에는 없는 정보가 있음 (P3 위반)
- **§6-4 T1~T7 중 하나라도 위반** (P6 위반) — 특히:
  - 형태로 표현한 비율이 본문 실제 비율과 다름 (T1)
  - 본문이 "미공개/Not published"인 값에 구체적 형태를 부여함 (T2)
  - 본문이 여러 갈래라고 말하는데 그림은 하나로 압축함 (T7)
- 해칭·빗금 등 채움 패턴 사용 (§6-5)
- alt 누락, 또는 alt가 "chart", "diagram" 수준의 라벨
- 커버 크기가 1200×630이 아님
- 커버 용량 200KB 초과
- 사람 얼굴·손·뇌·로봇 등 §5 금지 요소 포함
- C2PA 등 생성 도구가 붙인 출처 메타데이터를 제거함
  (`synthid-c2pa-explained-2026`에서 우리가 직접 주장한 원칙)

---

## 8. Codex 핸드오프 형식

Claude Code는 이미지를 생성하지 못한다. 생성은 Codex(또는 다른 이미지 모델)가 한다.
`post-images` 스킬이 아래 형식의 **프롬프트 팩**을 `_reviews/{date}-{slug}.images.md`에
만들어 주면, 기웅이 그대로 Codex에 붙여넣고 결과 파일을 `assets/img/posts/`에 넣는다.

프롬프트 팩 필수 항목:

1. 대상 슬러그 / 포맷 / 계획된 이미지 목록 (파일명 + 용도)
2. 이미지별 완성 프롬프트 (§5 토큰 포함, 복사해서 바로 쓸 수 있는 상태)
3. 이미지별 alt 텍스트 초안
4. 저장 경로와 규격 (크기·용량)
5. **근거 대응표 (필수)** — 아래 형식. 이게 없으면 프롬프트 팩은 미완성이다
6. 반입 후 실행할 검증 명령

### 근거 대응표 형식

그림에서 **값을 나타내는 요소**를 빠짐없이 나열하고, 각각이 본문 어디에서 왔는지 적는다.

| 그림 요소 | 나타내는 것 | 본문 근거 | 실제 값 | 그림에 반영한 값 |
|---|---|---|---|---|
| 우측 선 길이 | max output | 비교표 4열 | 384K / 128K / 128K / 65.5K | 동일 비례 |
| 4번째 선 끝점 | Grok max output | 비교표 `Not published` | 없음 | **끝점 없이 열린 선** |
| 관문 개수 | 제약 조건 수 | "How to Choose" 4개 문단 | 4 | 4 |

작성 규칙:

- **"본문 근거"가 비는 행이 있으면 그 요소를 그림에서 지운다.** 예외 없다
- "실제 값"과 "그림에 반영한 값"이 다르면 그 차이가 정당한 이유를 한 줄로 적는다.
  적을 수 없으면 T1 위반이다
- 순수 장식 요소(배경 여백, 정렬선)는 값을 나타내지 않으므로 표에 넣지 않는다.
  단, **독자가 값으로 오독할 수 있는 요소는 장식이 아니다** — 중앙 수직선이 축으로
  읽혔던 사례를 기억할 것

---

## 9. 반입 후 최적화

Codex 산출물은 대개 규격을 벗어난다. 반입 후 이 스크립트로 정규화한다.

```bash
# 커버: 1200x630로 맞추고 200KB 이하로 압축
python3 .claude/hooks/optimize_image.py assets/img/posts/{slug}-cover.png --cover

# 본문 이미지: WebP 변환 + 가로 1600px + 150KB 이하
python3 .claude/hooks/optimize_image.py assets/img/posts/{slug}-fig1.png --figure
```

`--cover`는 리사이즈 시 크롭이 아니라 **커버 크롭(center crop)** 을 쓴다.
1.91:1이 아닌 원본은 가운데를 기준으로 잘린다 — 주요 요소를 중앙에 배치해야 하는 이유.

---

## 10. 검증

훅이 자동으로 검사한다 (`post-validation.sh` Section C, 규칙 C1~C8).
`_drafts/`에서는 WARN, `_posts/`에서는 ERROR로 승격된다 — 초안 단계에서는
이미지가 아직 없는 게 정상이기 때문이다.

레포 전체 현황을 한 번에 보려면:

```bash
python3 .claude/hooks/image_validation.py --report
```

누락된 커버, 규격 위반, 깨진 본문 참조가 슬러그별로 출력된다.
발행(Phase 6) 전에 이 명령이 깨끗해야 한다.
