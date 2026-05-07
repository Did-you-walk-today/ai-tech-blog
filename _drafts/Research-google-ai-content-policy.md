# 자료 조사 보고서

**주제**: 구글이 블락하는 AI 콘텐츠 종류와 기준
**조사일**: 2026-04-27
**조사 범위**: Google 검색, YouTube, 이미지/동영상, 심사 과정, 불리 요소

---

## 핵심 발견 (글의 차별화 포인트)

대부분의 블로그가 잘못 쓰는 표현이 두 개 있어요. 이걸 글 도입부에서 짚고 가면 차별화됩니다.

**오해 1: "구글이 AI 콘텐츠를 블락한다"**
→ 사실: 구글은 AI 사용 자체를 처벌하지 않는다. 공식 입장 명확함.

**오해 2: "AI 콘텐츠는 들키면 디인덱스된다"**
→ 사실: 구글은 AI 탐지 자체를 목적으로 하지 않는다. 품질로 판단한다.

진짜 처벌받는 건 **품질, 의도, 검증 가능한 신뢰**의 문제예요.

---

## 1. Google 검색의 공식 입장 (1차 출처)

**출처**: Google Search Central Blog (2023년 2월) + 2025년 12월 갱신
URL: https://developers.google.com/search/blog/2023/02/google-search-and-ai-content

### 공식 원칙
"AI를 포함한 자동화의 적절한 사용은 가이드라인 위반이 아니다. 검색 순위를 조작할 목적으로 콘텐츠를 생성하는 데 사용되는 경우만 스팸 정책 위반이다."

### 핵심 판단 기준: E-E-A-T
- **Experience** (경험): 직접 해본 것인가
- **Expertise** (전문성): 주제에 대한 깊이 있는 지식인가
- **Authoritativeness** (권위): 신뢰할 만한 출처인가
- **Trustworthiness** (신뢰성): 사실 검증이 되는가

### 구글이 권장하는 AI 사용 자세
- AI를 "독창적이고 도움 되는 콘텐츠 생산을 돕는 수단"으로 본다면 OK
- AI를 "값싸게 검색 순위를 조작하는 수단"으로 본다면 NG
- 작성자 바이라인 표시 권장 (특히 Google News)
- AI 사용 사실의 적절한 공개 권장

---

## 2. 진짜 처벌받는 콘텐츠 유형

### 2-1. 스팸 정책 위반 (즉시 처벌)
- **랭킹 조작 목적의 대량 생산**: 키워드만 바꿔 양산하는 AI 글
- **Scaled content abuse**: 같은 템플릿으로 수백~수천 페이지 생성
- **Site reputation abuse** (parasite SEO): 권위 있는 도메인 빌려서 무관한 AI 콘텐츠 게시
- **Expired domain abuse**: 만료 도메인 사서 AI 콘텐츠로 채우기

### 2-2. Helpful Content System으로 디모트 (점진적 처벌)
2022년 도입, 2024년 3월부터 core 알고리즘에 통합됨.

**디모트 패턴 (March 2024 Core Update 분석)**:
- 사이트 전체의 40%가 저품질로 판정되면 사이트 전체 디모트 가능
- 출처: Google March 2024 Core Update가 검색 결과에서 저품질 콘텐츠 40% 감소시킴
- 영향 큰 카테고리: e-commerce 52%, YMYL/health 67%, affiliate 71%

**디인덱싱(완전 제외)되는 패턴**:
- 사이트 자체 전문성 영역을 벗어난 주제 대량 발행
- thin product/service 페이지
- 직접 경험 없는 주제에 답하려는 콘텐츠
- 출처 없는 가짜 사례 연구, 가짜 통계

### 2-3. December 2025 Core Update 패턴 (가장 최근)
- 1,200단어가 4,000단어보다 높게 랭크되는 사례 다수
- 차이: "이 일을 매일 하는 사람"이 쓴 글 vs "조사해서 짜깁기한" 글
- E-E-A-T 가중치를 YMYL 외 전체 콘텐츠로 확대
- AI 탐지보다 "진짜 인간 전문성의 표지(markers)"를 보상

### 2-4. 가장 크게 타격받은 사이트 유형
- **Affiliate review 사이트**: 안 써본 제품 리뷰 → 큰 폭 디모트
- **AI로 가짜 사례 생성한 사이트**: 검증 불가능한 케이스 스터디
- 2024년 이후 일부 사이트는 트래픽 50~60% 영구 손실

---

## 3. AI 이미지에 대한 정책 (가장 빠르게 변하는 영역)

### 3-1. Google의 식별 기술
**SynthID** (Google DeepMind 개발)
- 이미지 픽셀에 직접 박는 invisible watermark
- 편집, 압축, 크롭 후에도 살아남음
- Gemini 앱에서 검증 도구 제공 (2025년 11월~)

**C2PA 메타데이터** (산업 표준)
- Adobe, Microsoft, BBC, NYT 등이 만든 컨소시엄 표준
- 암호학적으로 서명된 메타데이터
- Nano Banana Pro, Vertex AI, Google Ads에서 생성된 이미지에 자동 부착됨 (2025년 11월~)

### 3-2. 이미지 정책 핵심
- AI 이미지 자체는 금지가 아님
- **메타데이터 위변조는 금지**: IPTC DigitalSourceType "TrainedAlgorithmicMedia" 표기 필수
- e-commerce: AI 생성 상품 이미지/설명은 별도 표시 의무
- Google Merchant Center에 별도 정책 있음

### 3-3. 이미지에서 진짜 처벌받는 케이스
- 실존 인물의 비동의 deepfake (특히 성적 이미지)
- AI 임을 숨기고 보도성 콘텐츠로 사용
- 메타데이터 조작/제거 후 재배포
- 선거 관련 기만적 합성 콘텐츠

---

## 4. YouTube 정책 (가장 강력한 처벌 시스템)

### 4-1. 타임라인
- 2023년 11월: AI 공개 정책 발표
- 2024년 3월: "Altered or Synthetic Content" 토글 출시
- **2025년 5월 21일: 의무화 본격 시행** (no grace period)
- **2025년 7월 15일: YPP 수익화 정책 강화** (AI slop 단속)

### 4-2. 의무 공개 대상 ("realistic" 콘텐츠)
시청자가 진짜로 오해할 만한 모든 합성 콘텐츠.

**공개 필수 사례**:
- 실존 인물이 안 한 말/행동을 한 것처럼 보이는 영상
- 일어나지 않은 사건의 사실적 영상 (예: AI가 만든 군중 영상)
- 의료 시술처럼 보이는 합성 영상
- 사망한 인물의 목소리 합성

**공개 불필요 사례**:
- 명백히 비현실적인 애니메이션, 특수효과
- 색상 조정, 조명 보정 등 미용적 편집
- 자막 생성, 캡션 같은 생산성 향상

### 4-3. 처벌 단계 (6단계)
1. **레이블 추가**: 공개 누락 영상에 자동 레이블
2. **노출 제한**: 추천 알고리즘에서 빠짐
3. **수익화 제한**: 광고 게재 제한
4. **영상 삭제**: 오해 가능성 큰 영상은 즉시 삭제
5. **커뮤니티 가이드라인 strike**: 3 strike 누적 시 채널 종료
6. **YPP 영구 정지/채널 종료**

### 4-4. 2025년 7월 YPP 수익화 정책 (AI slop 타격)
**수익화 박탈 기준**:
- 정적 이미지 + AI 음성만으로 만든 영상
- 같은 템플릿 반복 생산 (AI 자동화 채널)
- 편집/논평/변형 없는 그대로의 AI 출력물
- "면 없는 채널" 중 가치 부가 없는 것

**살아남는 패턴**:
- 자기 의견/논평 추가
- 스토리텔링, 내러티브 구조
- 교육적/정보적 깊이
- 일관된 작가 관점

### 4-5. 실제 처벌 사례
- 8만 3천 구독자 true crime 채널 종료 (AI 살인 사연 미공개)
- 흑인 셀럽 가짜 뉴스 deepfake 네트워크 통째 해체
- StoriezTold 채널: AI 동물 내레이션 반복 → 플래그
- 살해당한 아이 목소리로 범죄 사연 만든 채널들 다수 삭제

---

## 5. Google의 심사 메커니즘

### 5-1. 자동 시스템
- **SpamBrain**: AI 기반 스팸 탐지. 검색 결과의 40% 스팸 감소
- **Helpful Content System**: 사이트 전체/페이지별 평가 (2024년 3월부터 core 알고리즘 통합)
- **Core Update**: 정기적 (1년에 3~4회) 알고리즘 재조정

### 5-2. 수동 액션
- Google human reviewer가 직접 검토
- "Major spam problems" 같은 사유로 수동 페널티 부과
- Search Console에서 manual action 통지
- 재심사 요청(reconsideration request) 가능

### 5-3. AI 콘텐츠 자체를 탐지하는가?
**공식 입장**: "AI 탐지 자체를 목적으로 하지 않는다."
**실제 작동**: AI 콘텐츠의 흔한 패턴(저품질, 일반론, 검증 불가 정보)을 통해 간접 탐지.

### 5-4. December 2025 Core Update의 변화
- 사이트 전체 평가에서 페이지 단위 평가로 이동
- E-E-A-T 가중치를 모든 콘텐츠 유형으로 확대
- "진짜 인간 전문성의 표지" 가중치 상승

---

## 6. 심사에 불리한 요소 (체크리스트)

### 6-1. 콘텐츠 자체
- 사이트 주력 분야 벗어난 주제 대량 발행
- 같은 템플릿 반복 (AI farm 패턴)
- 직접 검증 안 된 통계, 사례
- 단어 수만 늘린 thin content
- 출처 없는 인용
- 동일 주제 글의 재탕/짜깁기

### 6-2. 신뢰 신호 결여
- 작성자 정보 없음 (anonymous)
- 작성자 약력/전문성 없음
- 발행일/수정일 없음
- 외부 권위 출처 인용 없음
- 1차 자료 없음

### 6-3. AI 사용의 잘못된 형태
- 인간 검토 없는 자동 발행
- AI에 작성자 바이라인 부여
- AI 사용 사실 은폐
- 가짜 사례 연구, 가짜 데이터
- 사실 확인 없는 수치 인용

### 6-4. 기술적 문제
- AI 이미지의 메타데이터 제거
- 구조화 데이터(schema)와 본문 내용 불일치
- 광고 비율 과다
- 가독성 떨어지는 레이아웃

### 6-5. 사이트 차원의 문제
- 만료 도메인 사서 AI 콘텐츠 채우기
- 권위 있는 도메인의 무관한 게스트 포스트
- 같은 IP/계정의 사이트 네트워크
- 백링크 매수

---

## 7. 살아남는 패턴 (긍정적 사례)

### 7-1. 검색에서 살아남는 패턴
- 1인칭 직접 경험 ("우리가 2주간 테스트한 결과...")
- 측정 가능한 구체적 수치 (저조도 34% 개선, ISO 6400)
- 원본 비교 사진/스크린샷
- 작성자가 해당 분야 일상 종사자임이 드러나는 디테일
- 수치/주장의 출처 링크

### 7-2. YouTube에서 수익화 살아남는 패턴
- 대본은 AI가 짜도 본인 의견/관점 추가
- 일관된 화자(face or voice)
- 깊이 있는 내러티브 구조
- 인용 출처 명시
- 변형/편집을 통한 부가가치

### 7-3. AI 사용을 잘 공개하는 방법 (Google 권장)
- 작성자는 사람 이름으로 표시
- 제작 과정에 대한 별도 설명 추가
- AI 보조 사용 사실의 자연스러운 공개
- 이미지의 IPTC 메타데이터 표기
- 산업별 표준 (예: e-commerce 별도 라벨)

---

## 8. 글 작성 시 권장 구조 (jsonhouse DNA 적용)

### 도입부 TL;DR 핵심 포인트
- 구글은 AI 콘텐츠 자체를 처벌하지 않는다
- 처벌받는 건 "랭킹 조작 목적 + 인간 검토 부재 + 신뢰 신호 결여"
- YouTube는 검색보다 훨씬 강한 처벌 시스템 보유 (6단계)
- 이미지는 SynthID + C2PA로 식별 가능
- 살아남는 핵심 = E-E-A-T + 진짜 경험의 표지

### 비교표 후보
| 플랫폼 | 처벌 강도 | 핵심 기준 | 의무 공개 |
|---|---|---|---|
| Google Search | 디모트 (점진적) | E-E-A-T + 품질 | 권장 |
| YouTube | 6단계 (즉각적) | 원본성 + 공개 | 의무 (realistic) |
| Google Images | 메타데이터 검증 | SynthID/C2PA | 의무 (생성 이미지) |
| Google Merchant | 즉시 제거 | 별도 라벨 | 의무 |

### FAQ 후보 (최소 3개)
1. AI로 작성한 블로그 글은 구글에 노출되나요?
2. AI 글에 작성자 이름을 사람으로 적어도 되나요?
3. YouTube에서 AI 음성 사용하면 수익화 끊기나요?
4. 구글이 AI 콘텐츠를 자동으로 탐지하나요?
5. AI 이미지를 블로그에 쓰려면 뭘 표시해야 하나요?

---

## 9. 신뢰할 만한 1차 출처 (글에서 인용)

1. Google Search Central Blog (2023.2): https://developers.google.com/search/blog/2023/02/google-search-and-ai-content
2. Google Search Documentation (Generative AI): https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
3. Google Generative AI Prohibited Use Policy: https://policies.google.com/terms/generative-ai/use-policy
4. Google Play AI-Generated Content Policy: https://support.google.com/googleplay/android-developer/answer/14094294
5. YouTube AI Disclosure Official Page: https://www.youtube.com/howyoutubeworks/ai/
6. Google SynthID Verification: https://blog.google/innovation-and-ai/products/ai-image-verification-gemini-app/
7. Google Search Content Policies: https://support.google.com/websearch/answer/10622781

---

## 10. 글에 쓸 만한 인사이트 (이면 분석 포인트)

### 인사이트 1: "AI 탐지"가 아니라 "인간 흔적 탐지"로의 이동
December 2025 Core Update에서 가장 중요한 변화. 구글은 AI를 잡아내려 하지 않고, "진짜 인간 전문성의 표지"를 보상하는 방향으로 갔어요. 이게 더 효과적이라는 판단. AI는 점점 잡기 어려워지지만, "이 사람이 정말 이걸 매일 하는 사람인가"의 표지는 잡기 쉬움.

### 인사이트 2: YouTube가 검색보다 훨씬 강경한 이유
광고주 신뢰 보호 + 시청자 직접 피해 가능성. 검색은 "유용하지 않으면 다른 결과 보여주면 됨" 인데, YouTube는 deepfake 한 개가 누군가를 직접 해칠 수 있음. 그래서 6단계 처벌 + no grace period.

### 인사이트 3: SynthID + C2PA의 진짜 노림수
"AI 콘텐츠 식별"이 아니라 "진짜 콘텐츠의 검증". 가짜를 잡는 게 아니라 진짜를 인증하는 방향. 이게 deepfake 대응의 진짜 방향성.

### 인사이트 4: "AI slop"이라는 새 단어의 의미
2025년 등장한 용어. AI가 만든 모든 콘텐츠가 아니라, "대량 생산된 저품질 자동화 콘텐츠"만 지칭. 구글/YouTube는 이걸 명확히 분리해서 타겟팅 중. 이 구분을 모르면 "AI 쓰면 다 망한다"는 잘못된 결론에 도달함.

---

조사 완료. 다음 단계는 Phase 3 Draft Generation으로 넘어가도 됩니다.
글 작성 명령 줄 때 이 보고서를 참조 자료로 첨부하세요.