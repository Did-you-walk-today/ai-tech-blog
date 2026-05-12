# Phase 5 한국어 검토 보고서

**포스트**: GIGO Prompts 2026: Why Vague Prompts Fail (Data + Fix)
**슬러그**: `gigo-prompts-2026-why-vague-prompts-fail`
**작성일**: 2026-05-07
**검토 대상 파일**: `_posts/2026-05-07-gigo-prompts-2026-why-vague-prompts-fail.md`

---

## 핵심 주장 요약 (3줄)

1. LLM은 "이해"하지 않고 다음 토큰의 확률을 계산한다 — 모호한 프롬프트는 prior를 under-specify해서 모델이 학습 데이터 평균으로 수렴하게 만든다.
2. "Parasitic creativity": 불확실할 때 모델은 거부하지 않고 통계적으로 그럴듯한 내용을 생성한다 — 할루시네이션의 구조적 원인.
3. 구조화된 프롬프트는 2025년 연구들에서 22–33 퍼센트포인트 할루시네이션 감소 — 모델 교체 없이, 프롬프트 작성법 변경만으로.

---

## 인용된 수치/벤치마크 출처 목록

| 수치 | 출처 | 신뢰도 |
|------|------|--------|
| ~22pp 할루시네이션 감소 | Nature digital medicine, 프롬프트 미티게이션 연구 (2025) | ⚠️ 근사값 ("~22pp") — 포스트와 데이터 파일 모두 "~" 표기 ✅ |
| 33pp 할루시네이션 감소 | Medical AI structured prompt study (2025) | ⚠️ 특정 의료 도메인 연구 — 일반화 범위 제한적 |
| 73% annotator preference | OpenAI prompting guide study (2024) | ✅ OpenAI 공식 문서 기반 |
| 3.1%–19.1% 범위 | 5-model frontier benchmark (April 2026) | ⚠️ 구체적 벤치마크 이름 없음 (Phase 3 verified list 출처) |
| 40–80% 오픈엔드 생성 | Frontiers in AI hallucination survey (2025) | ⚠️ survey aggregates — 표에 출처 명시됨 ✅ |
| 58–88% 법률 인용 | Frontiers in AI hallucination survey (2025) | ⚠️ survey aggregates |
| 43–64% 의료 Q&A | Frontiers in AI hallucination survey (2025) | ⚠️ survey aggregates |
| <2% 요약+출처 기반 | Frontiers in AI hallucination survey (2025) | ⚠️ survey aggregates |

---

## 적용된 스타일

**jsonhouse DNA (합성 스타일)**

적용 근거:
- CAT3 (Prompt Engineering) → jsonhouse DNA 기본값
- 거시 맥락 (LLM 확률 계산 메커니즘) + 데이터 (할루시네이션 수치 테이블) + 실용 (Before/After 예시 3개, Fix Template 코드블록) 동시 포함
- 5단계 구조 준수: Hook+TL;DR → 팩트+데이터 → ★이면 분석 → 큰 그림 → 실용 결론+FAQ

---

## 이면 분석 핵심 (2~3문장)

모호한 프롬프트의 실패는 "모델이 부족해서"가 아니라 "prior를 under-specify했기 때문"이다 — LLM 아키텍처 자체의 작동 방식에서 나온 구조적 결과다. Parasitic creativity 개념이 핵심: 모델은 확실하지 않을 때 거부하는 게 아니라 통계적으로 그럴듯한 내용을 생성하도록 훈련됐다. GIGO는 2026년의 컨텍스트 엔지니어링 트렌드에서 더 심각해지는데, 멀티스텝 파이프라인에서 모호성이 각 단계를 거치며 증폭되기 때문이다.

---

## 의심스러운 사실 관계 항목 ⚠️

### 1. "5-model frontier hallucination benchmark (April 2026)"

- **현황**: 소스 섹션에 구체적 벤치마크 이름 없음
- **검토 요청**: Phase 3 verified statistics list에 포함된 수치이므로 수치 자체는 OK. 구체적 벤치마크 이름(예: HELM, HallucinationBench 등) 확인 후 Sources에 추가 권장.

### 2. 의료/법률 할루시네이션 범위 — domain 일반화

- **현황**: 40–80% (오픈엔드), 58–88% (법률 인용) — 넓은 범위
- **리스크**: 범위가 넓어서 "40%도 맞고 80%도 맞다"는 면책이 가능한 반면, AI 답변 엔진이 하한(40%)이나 상한(80%)만 발췌할 경우 오해 유발 가능
- **검토 요청**: 현재 표현("2025–2026 survey aggregates")으로 충분한지, 아니면 추가 컨텍스트 필요한지 확인.

### 3. Wireless mouse 예시 — 제품 현황

- **현황**: Logitech MX Master 3S와 Microsoft Arc Mouse를 2026년 5월 기준 예시로 사용
- **검토 요청**: 두 제품이 2026년 5월 현재도 판매 중인지 확인. MX Master 3S는 2022년 출시 제품으로, 2026년 기준으로 여전히 현행 모델인지 또는 후속작이 있는지 검토 권장. (교육적 예시용이라 큰 문제는 아니지만 신뢰도 관련)

---

## 내부 링크 목록 + 검증 결과

| 링크 텍스트 | 대상 슬러그 | 파일 존재 여부 |
|------------|------------|--------------|
| E-E-A-T signals, as Google's quality systems operationalize them | `eeat-ai-content-2026` | ✅ `_posts/2026-04-29-eeat-ai-content-2026.md` |
| how Google's Helpful Content System evaluates content across a site | `helpful-content-system-2026` | ✅ `_posts/2026-05-01-helpful-content-system-2026.md` |

내부 링크 2개 ✅ (A9 조건 충족)

**참고**: 두 링크 모두 CLUSTER_AI_CONTENT_POLICY (다른 클러스터). 이 포스트가 CLUSTER_PROMPTS 첫 번째 글이라 같은 클러스터 내 링크 없음 — 구조적으로 불가피. 다음 CAT3 포스트 발행 시 상호 링크 업데이트 필요.

---

## SEO / Hard Reject 자체 점검

| 조건 | 결과 |
|------|------|
| Title ≤ 60자 + "2026" | ✅ 54자 |
| Meta description 140–165자 | ✅ 152자 |
| 비교표 존재 | ✅ 2개 (태스크별 할루시네이션 레이트, 연구별 감소 수치) |
| JSON code block 금지 (B1) | ✅ 없음 — 모든 code block은 텍스트 프롬프트 예시 |
| Word count ≥ 600 | ✅ 약 2,300+ |
| canonical_url 없음 | ✅ |
| data_updated 있음 | ✅ 2026-05-07 |
| FAQ ≥ 3개 (hard) / 5개 (target) | ✅ 5개 |
| TL;DR 존재 | ✅ |
| 내부 링크 ≥ 2개 | ✅ 2개 |
| 이면 분석 ≥ 4단락 | ✅ 4개 H3 소섹션 |
| Before/After 예시 3개 도메인 | ✅ tech writing, code debugging, everyday product |
| Fix template (5요소) | ✅ PERSONA / TASK / EXAMPLE / FORMAT / CONSTRAINTS |
| Sources 섹션 (6개) | ✅ 6개 출처 명시 |
| code block 전 intro (B2) | ✅ 각 code block 앞에 문장 있음 |
| code block 후 outro (B3) | ✅ 각 code block 뒤에 설명 문장 있음 |
| heading 바로 아래 code block 금지 (B4) | ✅ 모든 code block 앞에 intro 텍스트 있음 |

---

## 검토자 (기웅) 확인 요청 사항

1. **"5-model frontier benchmark" 출처** — 구체적 벤치마크 이름 추가 필요한가, 현재 표기로 충분한가?
2. **의료/법률 범위 (40–80%, 58–88%)** — 범위가 넓은 것이 독자에게 혼란을 줄 수 있는가?
3. **Wireless mouse 예시 (MX Master 3S / Arc Mouse)** — 2026년 5월 기준 여전히 적절한 예시인가?
4. **CLUSTER_PROMPTS 첫 포스트** — 글의 톤과 메커니즘 설명 깊이가 CAT3 카테고리 기준에 맞는가? 이 글이 앞으로 나올 프롬프트 라이브러리/고급 기법 포스트들의 기반이 됨.
5. **Fix Template 코드블록** — 5요소 구조가 충분히 copy-ready한가, 아니면 더 구체적인 예시가 필요한가?

승인 시 → Phase 6 (Publishing) 진행
거절 시 → 거절 사유와 함께 Phase 3 재생성 요청

