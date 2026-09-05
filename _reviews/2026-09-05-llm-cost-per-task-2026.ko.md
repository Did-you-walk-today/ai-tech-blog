# Phase 5 리뷰 리포트 — llm-cost-per-task-2026

- **초안**: `_drafts/2026-09-05-llm-cost-per-task-2026.md`
- **데이터**: `_data/2026-09-05-llm-cost-per-task-2026.json`
- **Format**: D (구조화 데이터) / **Cluster**: CLUSTER_LLM / **Category**: ai-models-intelligence
- **훅 상태**: ERROR 0건, WARN 1건 (커버 파일 미존재 — 드래프트 단계에서는 정상)

---

## 1. 핵심 주장 요약 (3줄)

1. GPT-6 Astra는 GPT-5.6 Sol 대비 **모든 요금 항목에서 정확히 2.5배**인데, OpenAI는 BenchCAD에서 태스크당 추정 API 비용이 약 43% 낮다고 발표했다.
2. 이 둘을 나누면 아무도 발표하지 않은 숫자가 나온다 — Astra가 Sol의 **비용가중 토큰 23%**만 써야 성립하는 수치이고, 손익분기선은 40%다.
3. 그런데 같은 모델이 Artificial Analysis Intelligence Index에서는 태스크당 **75% 더 비쌌다.** 절감은 모델이 아니라 **과제 형태**에 붙는다.
4. (2차 개정 추가) 벤더가 내는 비용은 전부 **시도당** 비용이다. 성공률로 나누면 Terminal-Bench 4.0의 9% 절감이 **41%**가 된다. 하위 모델의 에러가 곧 비용이라는 것이 이 계산의 내용이다.

---

## 2. 인용된 수치 / 벤치마크 출처 목록

| 수치 | 출처 | 확인일 |
|---|---|---|
| BenchCAD 95.9% / 83.3% / 84.3%, 비용 −43% vs Sol, −86% vs Fable 5.1 | [OpenAI, "GPT-6 Astra: A new generation of intelligence"](https://openai.com/index/gpt-6-astra/) | 2026-09-05 |
| Terminal-Bench 4.0 57.9% / 37.3% / 55.8%, 비용 −9% / −63% | 동일 | 2026-09-05 |
| Terminal-Bench Science 0.1 64.6% vs 52.6% (−31%), 저비용 설정 61.1% vs 22.4% (−27%) | 동일 | 2026-09-05 |
| GPQA Diamond 저비용 설정 94.9% vs 94.6% (−37%) | 동일 | 2026-09-05 |
| Agents' Last Exam 59.3% vs 55.5%, 출력 토큰 −65% vs Opus 5 (**비용 수치 미공개**) | 동일 | 2026-09-05 |
| Astra $10/$1/$50, 롱컨텍스트 $20/$2/$75, fast mode 2배 | [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) | 2026-09-05 |
| Sol $4/$0.40/$20, 프로모션 "at least through 2026-11-21" | 동일 | 2026-09-05 |
| Fable 5.1 $10/$50, 캐시 히트 0.025x = $0.25 | [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing) | 2026-09-05 |
| Opus 5 $5/$0.50/$25 | 동일 | 2026-09-05 |
| Claude 4.7 이후 토크나이저가 같은 텍스트에 약 30% 더 많은 토큰 생성 | 동일 (Note 블록) | 2026-09-05 |
| AA Intelligence Index v4.1.1 61.2 vs 60.9, 태스크당 +75%, Astra max $2.57/task | [Artificial Analysis, "Benchmarking GPT-6 Astra"](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) | 2026-09-05 |
| AA Coding Agent Index v1.4 67.0 vs 65.1, 비용 "about the same" | 동일 | 2026-09-05 |
| BenchCAD 벤치마크 정의 (CadQuery 17,900개 프로그램, 106개 산업 부품군) | [arXiv 2605.10865](https://arxiv.org/abs/2605.10865) | 2026-09-05 |
| SRE-Bench 1회 시도 88.0% / 4회 이내 99.2% vs Sol 55.9% / 68.7% | OpenAI 발표문 본문 | 2026-09-05 |
| ExploitBench(6~8월) Sol 5.5%는 "300턴 제한의 산물", 제한 완화 시 11.5% | OpenAI 발표문 각주 14 | 2026-09-05 |
| ExploitGym 6시간 제한 해제 후 측정 | OpenAI 발표문 각주 13 | 2026-09-05 |
| OSWorld 2.0 Astra 72.6% @ 약 40분 vs Sol 65.7% @ 약 75분 | OpenAI 발표문 본문 | 2026-09-05 |
| 내부 hallucination 벤치 4.2% vs 12.2% (낮을수록 좋음) | OpenAI 발표문 Alignment 표 | 2026-09-05 |
| Sol $4/$20 프로모션이 스냅샷에 기록됨 | 자체 `_data/pricing_history/2026-09-01.json` | 2026-09-01 |

**파생 수치(우리가 원출처인 것)**: 손익분기 토큰비(40% / 50% / 100%), 각 행의 implied token ratio 10건, **성공당 비용 5건(−41% / −64% / −44% / −73% / −37%)**. 데이터 파일 `key_facts`에 `"jsonhouse original derivation, 2026-09-05"`로 표기했다.

**성공당 비용 계산식** — 각 모델의 상대 성공당 비용 = 비용비 ÷ 성공률, 절감 = 1 − (Astra값 ÷ 기준모델값). Terminal-Bench 4.0 vs Sol: Astra 0.91÷0.579 = 1.572, Sol 1.00÷0.373 = 2.681 → 1 − 1.572÷2.681 = **41%**.

**BenchCAD 두 행은 "Not derivable"로 남겼다.** geometric overlap은 통과율이 아니라 연속 부분점수라서 95.9%를 "95.9% 성공"으로 읽으면 안 된다. 가장 큰 비용 주장이 붙은 벤치마크가 성공당 비용으로 환산이 안 되는 유일한 벤치마크라는 점 자체를 본문에서 발견으로 다뤘다.

---

## 3. 적용된 스타일 + 근거

**jsonhouse DNA (합성 스타일).** 카테고리가 CAT1(ai-models-intelligence)이므로 스타일 가이드 §4 표에 따라 합성 스타일이 강제된다. 5단계 대응:

| 단계 | 본문 위치 |
|---|---|
| ① 훅 + TL;DR | 도입 문단 + TL;DR 5불릿 |
| ② 팩트 + 데이터 | "What the vendors actually published" + "The price ratios" 표 |
| ③ 이면 분석 | "The part the percentages hide"(+ 하위 섹션 "The weaker model's errors are the line item") + "Cost per successful task" + "What is not published" |
| ④ 큰 그림 연결 | "What benchmarks would have to report"(기업 조달 관점) + 라우팅 정책 / 캐시 가격 / 가격 전쟁 포스트 연결 |
| ⑤ 실용 결론 | "How to compute your own break-even" + FAQ |

PRIMARY_SOURCE_GUIDE 필수 8요소도 전부 배치했다 — Methodology(H2), 수집 시점(표 각주 + `data_updated`), Raw data 콜아웃, Limitations, 갱신 약속(월 1회 + 출시 48시간), Changelog, 단위 통일($/1M), 출처 표기.

**1차 출처 판별 테스트**: 경로 ④(정규화) + 파생. OpenAI는 % 만 내고 토큰 수를 안 낸다. 벤더 %를 요금표로 역산해 **implied token ratio**와 **손익분기선**을 만든 곳은 우리뿐이다. AI가 원출처로 가면 43%까지만 얻고 23%는 못 얻는다.

---

## 4. 이면 분석 핵심

절감의 정체는 "답을 짧게 쓰는 것"이 아니라 **"재시도를 하지 않는 것"**이다. BenchCAD·Terminal-Bench처럼 도구를 오래 쓰고 성공 여부가 기계로 판정되는 과제에서는 약한 모델이 0점짜리 시도에 예산을 태우고, 그 실패분이 전부 정가로 청구된다. 강한 모델이 지우는 건 그 낭비다.

그래서 같은 모델·같은 요금표인데 BenchCAD에서는 43% 싸고 Intelligence Index에서는 75% 비싸다. 단발 추론 질문에는 지울 낭비가 없으니 2.5배 단가가 희석되지 않고 그대로 드러난다. 결론은 "똑똑한 모델이 싸다"가 아니라 **"과제에 낭비가 많을수록 프리미엄 모델이 회수된다"**이고, 이게 모델 순위가 아니라 과제 형태로 라우팅해야 하는 이유다.

**2차 개정에서 강화한 부분 — 에러가 곧 비용이라는 것을 추론이 아니라 벤더 자백으로 세웠다.** 각주 14가 결정적이다. OpenAI가 스스로 "Sol의 5.5%는 300턴 제한의 산물"이라고 적었다. 하위 모델이 300턴을 다 태우고도 못 끝냈고 그 턴은 전부 과금됐다는 뜻이다. ExploitGym 6시간 제한 해제, OSWorld 40분 대 75분도 같은 방향의 증거다. 여기에 SRE-Bench가 못을 박는다 — Sol은 **4회 시도(=4번 청구)에서도 68.7%**로, Astra의 **1회 시도 88.0%**에 19.3점 못 미친다.

그리고 그 자백들을 숫자로 바꾼 게 성공당 비용 표다. 시도당 9%였던 절감이 성공당 41%가 된다. 부분점수 채점이 이걸 가린다는 점도 짚었다 — 기하 일치도 83.3%짜리 CAD는 "83.3%의 부품"이 아니라 **안 맞는 부품**이고, 그 비용은 API 청구서 바깥(반려된 도면, 폐기된 가공, 두 번 하는 설계 리뷰)에 떨어진다.

---

## 5. 의심스러운 사실 관계 / 판단이 필요한 항목

1. **the-decoder 기사의 "DeepSWE 57% 절감" 주장은 채택하지 않았다.** OpenAI 원문에는 DeepSWE 비용 수치가 없다. 2차 매체가 다른 벤치마크 수치를 옮기며 섞은 것으로 보인다. 우리 본문·데이터 파일 어디에도 넣지 않았다.
2. **OpenAI 각주 5번(BenchCAD 비용 주장에 붙은 것)이 빈 채로 렌더된다.** 각주 2·6·7·15도 마찬가지다. 본문에서 "renders empty"라고 사실 그대로 적었다. 기웅이 브라우저로 열었을 때 내용이 보인다면 알려주세요 — 그 경우 해당 문장을 고쳐야 한다.
3. **AA의 "+75%"는 자체 분해가 없다.** 2.5배 단가에서 +75%가 되려면 토큰비 0.70이어야 하는데, AA가 별도로 말한 "출력 토큰 약 10% 감소"만으로는 +125%가 나온다. 입력·캐시 구성이 다르기 때문일 가능성이 높지만 AA가 공개하지 않는다. Limitations에 "less well-constrained"로 명시했고, 이 행만 다른 행보다 근거가 약하다.
4. **Fable 5.1 대비 k=1.00은 캐시 무시 가정이다.** Fable 5.1 캐시 히트가 0.025x($0.25)라 Astra($1.00)보다 4배 싸다. 캐시 비중이 크면 k<1.00이고 86%·63% 절감은 과대평가된다. Limitations에 적었다.
5. **Anthropic 토크나이저 30% 문제.** Fable 5.1 비교 두 행은 토크나이저 경계를 넘는다. 절감분 일부는 효율이 아니라 단위 차이다. "What is not published"에서 명시했다. 이 지적을 하는 매체는 현재 못 찾았다 — 우리 차별점이다.
6. **Sol $4/$20은 프로모션이다.** 2026-11-21 이후 요금 미공개. 만료되면 모든 Sol 행이 움직인다. 참고로 방향은 Astra에 유리해진다(Sol이 비싸지므로).
7. **성공당 비용은 "실패 1회 비용 ≈ 성공 1회 비용"을 가정한다.** 실제 에이전트 실패는 턴·시간 한도를 다 태우므로 대개 더 비싸다. 즉 이 가정은 **보수적인 방향**이고 실제 절감은 표보다 클 가능성이 높다. Limitations에 명시했다.
8. **제안 섹션("What benchmarks would have to report")은 새 벤치마크를 만들자는 주장이 아니다.** SRE-Bench(시도별 해결 곡선)·Terminal-Bench(통과/실패)가 이미 하고 있고, 빠진 건 **비용·통과율·턴 예산을 한 표에 같이 내는 규율**이라는 형태로 썼다. 없는 기관이나 없는 벤치마크를 있는 것처럼 쓰지 않았다.
9. **발행 슬롯 이슈.** 오늘은 토요일(2026-09-05)이라 화요일 데이터형 슬롯이 아니다. 화요일 09-08은 `mcp-spec-adoption-2026`이 이미 차 있다. PRIMARY_SOURCE_GUIDE는 "이벤트 후 48시간 내 발행"을 요구하는데 출시가 09-03이라 이미 초과했다. **권고: 슬롯 규칙보다 신선도를 택해 즉시 발행**, 09-08 화요일은 MCP 포스트 그대로 유지. 최종 판단은 기웅.

---

## 6. 내부 링크 목록 + 검증 결과

| 링크 | 대상 파일 | 존재 |
|---|---|---|
| `/posts/llm-api-pricing-2026/` | `_posts/2026-07-17-llm-api-pricing-2026.md` | ✅ |
| `/posts/best-llm-2026/` | `_posts/2026-07-25-best-llm-2026.md` | ✅ (CLUSTER_LLM 필러) |
| `/posts/llm-cache-pricing-2026/` | `_posts/2026-08-01-llm-cache-pricing-2026.md` | ✅ |
| `/posts/llm-price-war-balance-sheet-2026/` | `_posts/2026-08-21-llm-price-war-balance-sheet-2026.md` | ✅ |

미발행 드래프트 `llm-price-expiry-2026`은 Sol 프로모션 만료를 다루므로 링크하고 싶었지만 **아직 `_posts/`에 없어 링크하지 않았다.** 그 글이 발행되면 이 포스트의 "promotional" 문단에 링크를 추가하는 것을 권한다.

외부 1차 출처 인라인 링크(D1): OpenAI 발표문, OpenAI 요금표, Claude 요금표, arXiv BenchCAD, Artificial Analysis — 5건 전부 본문 주장 지점에 배치.

---

## 7. 품질 자가 점수

| 항목 | 가중치 | 점수 | 근거 |
|---|---|---|---|
| technical_accuracy | 0.30 | 8.5 | 전 수치 1차 출처 대조, 2차 매체 오류(DeepSWE) 배제, 파생식 재현 가능 |
| structural_quality | 0.25 | 8.0 | 합성 스타일 5단계 + 1차출처 8요소 충족, 문단 120단어 이하 |
| practical_value | 0.25 | 9.0 | 손익분기 + 성공당 비용 두 계산법 모두 독자 워크로드에 적용 가능 |
| data_completeness | 0.20 | 8.5 | key_facts 10, comparison_data 10행, cost_per_success 7행, reporting_gaps 3, numerical_data 8, primary_sources 5 |

**가중 총점 8.50 / 10** (발행 기준 7.0 이상). 본문 3,978단어.

---

## 8. 커버 이미지 프롬프트 전문

- **가로세로비**: `16:9`
- **저장 경로(원본)**: `assets/img/posts/llm-cost-per-task-2026-cover-raw.png`
- **최종 경로**: `assets/img/posts/llm-cost-per-task-2026-cover.jpg` (1200×630, 200KB 이하로 정규화 — Claude Code가 처리)
- **주의**: 이미지 **생성 모델**로 만들어야 한다. CLI 에이전트에 맡길 경우 "이미지 생성 모델을 호출할 것, Python/PIL/SVG로 그리지 말 것"을 반드시 지시. 코드 렌더는 색상 수 검사(원본 5,000색 미만)에서 폐기된다.
- **소재 근거**: CLUSTER_LLM = 광학과 굴절. 유리 프리즘 적층을 골랐다. 커버는 값을 주장하지 않으므로 본문과 무관해도 된다.

아래 블록을 **그대로 전부** 복사해 사용하세요.

```
PURPOSE: Editorial cover art for a technical blog post. Decorative only.
It must not depict data, and it does not need to relate to the article topic.

SUBJECT: A short stack of thick solid glass prisms with polished bevelled
edges, resting on a slab of dark rough stone.

SCENE: The prisms sit slightly offset from one another, their polished edges
catching the light while the stone around them stays in deep shadow.

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

---

## 9. 기웅 확인 요청 사항

1. 발행 슬롯 — 즉시 발행 vs 다음 화요일 이후 (§5-7 권고: 즉시)
2. OpenAI 각주 5번이 브라우저에서 비어 있는지 (§5-2)
3. 커버 이미지 생성 후 파일 반입
