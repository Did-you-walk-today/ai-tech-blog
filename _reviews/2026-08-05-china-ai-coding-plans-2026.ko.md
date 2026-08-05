# Phase 5 리뷰 리포트 — China AI Coding Plans 2026

- **슬러그**: `china-ai-coding-plans-2026`
- **Format D · CLUSTER_LLM · CAT5 (ai-data-statistics)** — 데이터형 슬롯.
  초안 작성은 2026-07-28(화), 발행은 **2026-08-05**(승인 지연 + 2차 스팟체크 재작성)
- **파일 3종**: `_posts/2026-08-05-china-ai-coding-plans-2026.md` /
  `_data/2026-08-05-china-ai-coding-plans-2026.json` / 본 리포트
- **선행 스냅샷**: `_data/subscription_history/2026-07-28.json` (비공개 시계열 원본)

---

## 1. 핵심 주장 요약 (3줄)

1. 중국 AI 코딩 구독 5개사 중 **어느 둘도 같은 단위로 사용량을 계량하지 않는다** — prompts / requests / 동시 에이전트 수 / 미공개 / 해당없음.
2. 중국 벤더는 미국 벤더와 달리 **쿼터 수치를 공개하지만**, 그 수치들이 서로 환산되지 않아 비교가 불가능하다.
3. "주간 한도"라는 같은 표현이 두 개의 다른 제품을 가리킨다 — Alibaba는 고정 캘린더(월 00:00 UTC+8), Zhipu는 구독일 기준 7일 롤링.

## 2. 인용된 수치/출처 목록

전부 벤더 **공식 영문 문서**에서 2026-07-28 직접 수집. 집계 사이트 수치는 본문에 **한 건도 사용하지 않음**.

| 수치 | 출처 | 확인일 |
|---|---|---|
| GLM Lite/Pro/Max 5시간 ~80/~400/~1,600 prompts, 주간 ~400/~2,000/~8,000 | [docs.z.ai/devpack/overview](https://docs.z.ai/devpack/overview) | 2026-07-28 |
| "One prompt refers to one query… estimated to invoke the model 15–20 times" | 동일 | 2026-07-28 |
| GLM 진입 티어 "from $18/month" (티어별 개별가는 미표기) | 동일 | 2026-07-28 |
| Qwen Pro $50/월, 6,000 req/5h, 45,000 req/주, 90,000 req/월 | [alibabacloud.com/help/en/model-studio/coding-plan](https://www.alibabacloud.com/help/en/model-studio/coding-plan) | 2026-07-28 |
| Qwen 주간 리셋 월요일 00:00 (UTC+8) | 동일 | 2026-07-28 |
| Qwen Lite 신규중단 2026-03-20 / 갱신·업그레이드 중단 2026-04-13 | 동일 | 2026-07-28 |
| MiniMax Plus $20 / Max $50 / Ultra $120, 3-4 / 4-5 / 6-7 agents | [platform.minimax.io/docs/token-plan/intro](https://platform.minimax.io/docs/token-plan/intro) | 2026-07-28 |
| DeepSeek 구독 없음, v4-flash 2,500 / v4-pro 500 동시 요청 | [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing) | 2026-07-28 |

**jsonhouse 원 관측(1차 출처)으로 표기한 항목**: 단위 비환산성, 리셋 앵커 분기, 검증 실패 2건, 집계 사이트 3곳 상충 — `key_facts`에 `"jsonhouse original normalization attempt, 2026-07-28"`로 명시.

## 3. 적용 스타일 + 근거

**jsonhouse DNA (데이터 강화)**. STYLE_GUIDE ④ 선택 가이드상 **CAT5(데이터/통계) → 합성 스타일(데이터 강화)**에 해당.

5단계 구조 매핑:
- ① 훅 + TL;DR — 첫 문단(5개사 단위 불일치) + TL;DR 5불릿
- ② 팩트 + 데이터 — "What each vendor actually publishes" 비교표 2종 + Raw data 콜아웃
- ③ **이면 분석** — "Why the units diverge" + "'Weekly limit' is two different products"
- ④ 큰 그림 + 연결 — "DeepSeek is not in this category at all" (비교가능성은 국가가 아니라 **과금 형식**의 속성이라는 연결)
- ⑤ 실용 결론 + FAQ — "What to actually do with this" + FAQ 4문항

## 4. 이면 분석 핵심 (한국어 요약)

단위가 제각각인 이유를 "비교 방해용 불투명성"으로만 읽으면 **왜 하필 그 단위인지**가 설명되지 않는다. 더 나은 해석은 **각 벤더가 자기에게 희소한 자원을 단위로 삼았다**는 것이다 — request는 스케줄링 큐의 자리, 동시 에이전트는 머신 위의 좌석, prompt는 완료된 작업 1건. 즉 단위는 은폐가 아니라 **어디서 병목이 나는지에 대한 공시**로 읽힌다.

그리고 5개 플랜을 전부 비교 가능하게 만들 단위가 딱 하나 있는데(토큰), **아무도 구독 요금제에는 쓰지 않는다.** 토큰으로 표시하는 순간 가격÷쿼터로 시장이 한 줄에 정렬되기 때문이다. 의도가 무엇이든 **결과적으로 관대함 주장은 검증 불가능한 동안에만 유지된다.**

## 5. 의심스러운 사실 관계 / 주의 항목

| # | 항목 | 처리 |
|---|---|---|
| 1 | **Moonshot Kimi 전 항목 미확인** — 공식 페이지가 SPA라 티어·가격·쿼터 미노출 | 표에 "Not verified"로 표기, 추정치 미사용. 2차 출처의 "$19/월부터"는 **의도적으로 배제** |
| 2 | **Zhipu 본토(bigmodel.cn) 가격 미확인** — 본토 전화번호 + KYC 필요 | Limitations에 명시. 국제판 수치를 본토에 전용하지 않음 |
| 3 | **Zhipu 쿼터가 벤더 자신의 추정치** — 물결표(~) + "actual available usage may vary" | 본문에서 "추정이지 약속이 아니다"로 명시 |
| 4 | **MiniMax 주간 리셋 시각 미공개** — 2차 출처는 "월 00:00 UTC+8"이라 하나 공식 문서 미확인 | 표에 "Not published", 스냅샷 JSON에 `conflicting_third_party_claims`로 별도 기록 |
| 5 | **Zhipu 티어별 개별 가격 미표기** — 공식 문서는 "from $18"만 제시 | "Entry tier / from $18 (per-tier prices not itemized)"로 표기 |
| 6 | 앞선 세션 논의에서 GLM 가격을 "$3~20" → "$18/72/160"으로 정정했으나 **둘 다 집계 사이트 근거** | 본문에서 두 수치 모두 **미사용**. 공식 문서의 "from $18"만 인용 |

**전반 판단**: 미검증 2건(6개 레코드 중)을 안고 가는 초안이며, 이는 기웅 승인 사항(2026-07-28)이다. 빈칸을 남기는 것이 본 포스트의 경쟁 우위 축이므로 의도된 상태다.

## 6. 내부 링크 + 검증 결과

| 링크 | 대상 파일 | 존재 |
|---|---|---|
| `/posts/llm-subscription-guide-2026/` | `_posts/2026-07-25-llm-subscription-guide-2026.md` | ✅ |
| `/posts/llm-api-pricing-2026/` | `_posts/2026-07-17-llm-api-pricing-2026.md` | ✅ |
| `/posts/best-llm-2026/` | `_posts/2026-07-25-best-llm-2026.md` | ✅ |

3개 전부 CLUSTER_LLM 동일 클러스터. 미발행 글 링크 없음.

---

## 검증 상태

- **post-validation 훅**: PASSED (경고 1건 — 커버 이미지 미존재. 초안 단계에서는 정상)
- **데이터 JSON**: 필수 9필드 전부 존재, `key_facts` 10건, `faq_summary` 4건, `primary_sources` 5건, `license` 필드 없음
- **PRIMARY_SOURCE_GUIDE 필수 8요소**: Methodology ✅ / 수집시점 ✅ / Raw data 콜아웃 ✅ / Limitations ✅ / 갱신 약속(월간) ✅ / Changelog ✅ / 비교표 ✅ / 출처 표기 ✅

## 자가 품질 점수

| 항목 | 가중치 | 점수 | 근거 |
|---|---|---|---|
| technical_accuracy | 0.30 | 8.5 | 전 수치 공식 문서 직접 수집, 미검증은 미검증으로 표기 |
| structural_quality | 0.25 | 8.0 | jsonhouse DNA 5단계 충족, 훅 통과 |
| practical_value | 0.25 | 7.5 | 가격 비교는 되나 작업 단위 비교는 불가 — 한계를 밝히는 것이 실용 가치 |
| data_completeness | 0.20 | 6.5 | **6개 레코드 중 2개 미검증.** 의도된 공백이나 완결성 점수는 낮음 |

**가중 합계 = 7.75** (발행 기준 7.0 이상 충족)

## 발행 전 남은 작업

1. **커버 이미지** — `post-images` 스킬 필요. `/assets/img/posts/china-ai-coding-plans-2026-cover.jpg` (1200×630, ≤200KB)
2. 발행 시 `_posts/` 이동 + 포스트·데이터 파일 **동시 커밋**

**Phase 5 게이트 — 기웅 승인 대기 중. `_posts/` 이동·커밋·발행 없음.**

---

## ⚠️ 2026-08-01 발행 전 스팟체크 — 발행 보류 권고

발행 직전 벤더 문서를 재확인한 결과, **본문의 중심 논지를 무너뜨리는 불일치**를
찾았다. 커버·훅·구조는 문제없으나 **내용 개정 없이는 발행할 수 없다.**

### 1. Zhipu GLM — 단위와 수치가 둘 다 다르다 (치명)

| 항목 | 초안 (2026-07-28 수집) | 공식 문서 (2026-08-01 확인) |
|---|---|---|
| 단위 | **prompts** | **credits** |
| 5시간 한도 | ~80 / ~400 / ~1,600 | **2,000 / 12,000 / 28,000** |
| 주간 한도 | ~400 / ~2,000 / ~8,000 | **10,000 / 60,000 / 140,000** |

출처: `https://docs.z.ai/devpack/overview`, `https://docs.z.ai/devpack/faq`
("Usage for both models and MCP tools is calculated and deducted in credits.")

### 2. "아무도 토큰을 쓰지 않는다"가 사실이 아니다 (치명)

본문 "Why the units diverge" 절의 결론 문장:

> There is one unit that would make all five plans directly comparable,
> and nobody uses it: tokens.

Zhipu의 크레딧 산식은 **토큰에서 파생된다**:

```
Model credit usage = (Input tokens × Input multiplier
                    + Cached Input tokens × Cached Input multiplier
                    + Output tokens × Output multiplier) / 10,000
```

MiniMax도 월 토큰 배분(~1.7B / ~5.1B / ~9.8B)이 유통되고 있다(애그리게이터 출처,
공식 확인 필요). 이 문장은 이 포스트에서 가장 강한 주장이자 분석의 핵심인데,
지금 상태로는 **1차 출처가 반증한다.**

### 3. "one prompt = 15~20회 모델 호출"을 현재 문서에서 찾을 수 없다

본문이 "이 문서들 중 가장 유익한 한 줄"이라고 평가한 문장이다. 현재 z.ai 문서에는
prompt 정의 자체가 없다.

### 4. Alibaba Qwen — 정확. 다만 누락 2건

5시간 6,000 / 주간 45,000 / **월요일 00:00 (UTC+8)** 리셋 전부 문서와 일치.
Pro $50도 일치. 빠진 것: **월 90,000 한도**, **Lite 티어 신규가입 중단(2026-03-20)**.

### 5. MiniMax — 가격 확인, 동시 에이전트는 부분 확인

$20 / $50 / $120 일치. Max 4–5, Ultra 6–7 확인. Plus 3–4는 공식 확인 못 함.

### 개정 범위 판단

Zhipu 행 교체로 끝나지 않는다. TL;DR의 "prompts", "Why the units diverge" 절 전체,
"가장 유익한 한 줄" 단락, 데이터 JSON의 해당 `key_facts`가 모두 걸린다.
**Format D 재작성에 가깝다.**

다만 이건 나쁜 소식만은 아니다. 벤더가 쿼터 단위를 바꾼 정황 자체가
시계열 자산으로서 가치 있는 관측이다 (z.ai는 2026-07-31까지 GLM-5.2에 0.67 계수
프로모션을 운영했다). **단위 변경 시점을 특정할 수 있으면 그게 더 좋은 포스트다.**
단 스냅샷이 없어 지금은 시점을 주장할 수 없다.

---

## ✅ 2026-08-01 재작성 완료 — 위 보류 사유 해소

스팟체크에서 나온 5건을 전부 반영해 초안과 데이터 파일을 개정했다.
**논지가 약해진 게 아니라 더 강해졌다.**

### 논지 변경

| | 개정 전 | 개정 후 |
|---|---|---|
| 중심 주장 | "비교 가능한 단위는 토큰인데 **아무도 안 쓴다**" | "**정확히 한 곳만** 토큰 환산을 공개한다. 그래서 나머지의 침묵이 선택으로 드러난다" |
| 근거 | (반증됨) | Zhipu가 크레딧 산식 + 모델별 배수 4종을 전부 공개 |

개정 후 주장이 더 나은 이유: 원래 주장은 1차 출처 하나로 무너지는 것이었지만,
새 주장은 **그 1차 출처 자체가 근거**다. "숨긴다"가 아니라 "한 곳은 공개하는데
나머지는 안 한다 → 기술적 한계가 아니라 선택"으로 논증이 한 단계 내려갔다.

### 반영 내역

1. **Zhipu 행 교체** — 단위 credits, 5시간 2,000/12,000/28,000, 주간 10,000/60,000/140,000
2. **크레딧 산식 + 배수표 신설** — GLM-5.2 6.9/1.7/24, 5-Turbo 5.7/1.5/21, 4.7 4.6/1.2/16, 4.6V 1.2/0.3/2.7.
   여기서 파생 관찰 추가: GLM-5.2 출력 토큰은 입력의 3.5배, 캐시 입력의 14배
3. **"Why the units diverge" 절 재작성** — 토큰 주장 교체, 벤더별 미공개 정도를 구분
4. **Alibaba 보강** — 월 90,000 한도 추가 (5시간·주간·리셋 앵커는 문서와 완전 일치 확인)
5. **MiniMax** — "concurrent agents" → "agent capacity", 5시간 롤링 + 주간 윈도우 구조 명시
6. **Kimi** — "Not verified" → "Not documented". 공식 가격 문서가 종량제만 기술함을 확인
7. **애그리게이터 반증 사례 추가** — 3자 사이트는 Pro≈5배·Max≈20배라 하지만
   공개된 크레딧은 6배·14배다. 출처 배제 정책의 실증 사례로 본문에 넣음
8. **데이터 JSON** — `comparison_data.zhipu_credit_formula` 신설, `key_facts` 10건으로 정리,
   Kimi 출처를 실제 확인한 문서로 교체, `data_updated: 2026-08-01`

### 정직하게 남긴 것

07-28 수집분은 prompts, 08-01 재확인은 credits였다. **어느 쪽이 맞는지 단정하지 않고**
Methodology에 불일치 자체를 기록했다 — 벤더가 변경 이력을 공개하지 않아
"스킴이 바뀐 것"인지 "첫 수집이 틀린 것"인지 문서로는 판정 불가다.
표에는 08-01 관측만 싣는다. 이건 월간 스냅샷이 쌓여야 답이 나오는 질문이다.

### 검증 결과

A1 제목 52자 / A3 메타 146자 / A5 본문 2,623단어 / A4 비교표 21행 /
B1 JSON 코드블록 0 / A7 FAQ 5개 / A9 내부링크 3개 전부 실존 / B8 초과 문단 0 / 이미지 `OK`

**Phase 5 게이트 — 여전히 기웅 승인 대기. `_posts/` 이동·커밋·발행 없음.**

---

## ✅ 2026-08-05 2차 스팟체크 + 재작성 — Kimi 행 정정

`data_updated: 2026-08-01`의 7일 만료(08-08)를 앞두고 5개사를 전부 재조회했다.
**양수 수치 8개 항목은 전부 문서와 일치**했고, 부정 진술에서 중대 오류 1건이 나왔다.

### 무엇이 틀렸나

08-01 개정의 반영 내역 6번("Kimi — `Not verified` → `Not documented`. 공식 가격
문서가 종량제만 기술함을 확인")이 **틀렸다.**

- 조회한 곳: `platform.kimi.ai/docs/pricing` — Moonshot의 **API 종량 과금** 플랫폼.
  여기에 구독 쿼터가 없는 것은 사실이다
- 실제 있는 곳: `www.kimi.com/code/docs/en/` + Kimi 헬프센터 — **Kimi Code 구독 문서**

**벤더가 바꾼 게 아니라 처음부터 못 찾은 것이다.** Kimi Code CLI는 2026-05 출시고
체인지로그에 07-29자 쿼터 처리 항목이 이미 있다. 08-01 재검증 시점에 존재했다.

### 확인된 Kimi 수치

| 항목 | 값 | 출처 |
|---|---|---|
| 5시간 창 | 약 300–1,200 요청, 동시 최대 30 | kimi.com/code/docs/en/ |
| 주간 쿼터 | 7일마다 갱신, **수치는 미공개** | 동일 |
| 리셋 앵커 | 구독일 기준 7일 (D1–D7, D8–D14…) | 헬프센터 |
| 티어 | Moderato / Allegretto 이상 (모델·HighSpeed 접근 차등) | kimi.com/code/docs/en/ |
| 풀 공유 | Kimi 웹앱과 **같은 쿼터·같은 Extra Usage 잔액** | 멤버십 문서 |
| 가격 | **미검증** — 멤버십 가격 페이지가 판독 불가 | — |

### 논지 변경

| | 개정 전 | 개정 후 |
|---|---|---|
| 중심 주장 | "다섯 벤더, **다섯 개의 단위** — 그중 하나는 미문서화" | "**네 벤더가 쿼터를 공개**하고, 그중 환산식을 공개한 곳은 하나뿐" |
| Kimi의 역할 | 공백 (검증 실패) | "숫자는 주는데 **4배 폭 구간 + 챗앱과 공유**라 계획에 못 쓰는" 사례 |
| 새 관찰 | — | Alibaba와 Moonshot이 **같은 단위(requests)를 쓰는데도 비교 불가** |

Kimi가 채워지면서 논지가 약해질 것 같았지만 반대다. **"단위 이름이 곧 공시가
아니다"** 를 같은 단위 두 개로 실증할 수 있게 됐고, 리셋 앵커도 1:1이 아니라
**구독일 롤링 2 : 고정 캘린더 1**로 바뀌어 "고정 캘린더가 업계 기본값"이라는
암묵적 전제가 깨진다. 제목 *Quotas You Can't Compare* 는 그대로 유효하다.

### 반영 내역

1. **메인 표 Kimi 행 6칸 전부 교체** + Verification `Unverified` → `Official docs`
2. **가격 표 Kimi 행** — 티어명 기재, 가격은 "Not verified" 유지 (집계 사이트의
   Moderato $19 / Allegretto $39 / Allegro $99 / Vivace $199는 **의도적 미사용**)
3. **도입부·TL;DR 재작성** — "five units" → "four of five publish, in four units"
4. **"Why the units diverge"** — Moonshot을 네 번째 사례로 추가("측정해서 공시한
   병목이 아니라 확약을 피한 구간"), 같은 단위 두 벤더 문단 신설
5. **"Weekly limit"** — Zhipu + Moonshot 둘 다 구독일 롤링으로 정정, 2:1 분기 논점 추가
6. **Alibaba 인용 정밀도 수정** — 기존 "with the number left unstated"는 오도적이었다.
   문서는 실제로 쿼리당 호출 수를 **5–10(단순) / 10–30 이상(복잡)** 으로 제시한다.
   미공개인 것은 "호출당 토큰"이므로 그 지점으로 주장을 좁혔다
7. **Methodology에 정정 문단 신설** — 무엇을 어디서 잘못 봤는지 공개 기재 +
   "부정 진술 전에는 제품 사이트·헬프센터·API 문서 3곳을 본다"는 기준 명문화
8. **FAQ 5→5** — #3 리셋 앵커 갱신, **"Does Kimi Code publish its usage limits?" 신설**
9. **Changelog 2026-08-05 항목 추가**
10. **데이터 JSON** — Kimi 엔트리 교체, `key_facts` 10건 유지(2건 병합·1건 삭제),
    `faq_summary` 5건, `primary_sources` 7건(Kimi Code 문서 2건 추가, 기존 API
    페이지는 "종량제 플랫폼, 구독 쿼터 없음" 주석 달아 존치), `data_updated: 2026-08-05`

### 정직하게 남긴 것

- **Kimi 가격 미검증** — 공식 멤버십 페이지가 판독되지 않아 빈칸 유지. 집계 사이트
  수치는 쓰지 않는다. 이 포스트의 방침이 흔들리면 경쟁 우위 축이 사라진다
- **Zhipu 본토 가격 / Pro·Max 개별가** — 기존과 동일하게 미검증
- **07-28 prompts vs 08-01 credits 불일치** — 판정하지 않고 기록만 유지

### 검증 결과

- `post-validation.sh` — ERROR 0 / WARN 0 (무출력 통과)
- `image_validation.py --report` — `OK china-ai-coding-plans-2026`
- 데이터 JSON — 필수 9필드 존재, `key_facts` 10(스펙 5–10), `faq_summary` 5(스펙 3–5),
  `license` 필드 없음
- 제목 52자 / description 158자(140–165) / 본문 3,323단어 / 내부링크 3개 실존

**Phase 5 게이트 — 여전히 기웅 승인 대기. `_posts/` 이동·커밋·발행 없음.**
