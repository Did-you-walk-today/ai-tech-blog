# 자료 조사 보고서 #4

**주제**: SynthID and C2PA Explained — How AI Image Detection Actually Works
**조사일**: 2026-04-27
**Cluster**: CLUSTER_AI_CONTENT_POLICY (pillar 글의 spoke #3)

---

## 핵심 발견

이 글의 차별화 포인트:

1. **두 기술은 경쟁이 아니라 보완 관계**
   - 흔한 오해: SynthID vs C2PA 어느 게 표준이 될까
   - 실제: 픽셀 워터마크(SynthID) + 메타데이터 서명(C2PA) = 이중 레이어
   - 둘이 합쳐져야 의미 있음

2. **"가짜 잡기"가 아니라 "진짜 인증"으로의 패러다임 전환**
   - Provenance(출처) ≠ Detection(탐지)
   - SynthID-Image 논문 명시: "establishing provenance is materially different from detecting AI-generated content"
   - 진짜를 인증하는 방향이 더 효과적

3. **2025년이 분기점**
   - SynthID-Image 100억 개 콘텐츠 워터마크 (2025년)
   - C2PA 2.3 출시 (2025년 12월)
   - Google의 Nano Banana Pro부터 자동 부착 (2025년 11월)
   - 합성 콘텐츠가 2026년까지 온라인 미디어의 90%까지 증가 예상

---

## 1. SynthID — 픽셀 레벨 워터마킹

### 1-1. 개발 주체와 발표
- **개발**: Google DeepMind (with Google Research, Jigsaw)
- **첫 발표**: 2023년 Google I/O
- **논문**: "SynthID-Image: Image watermarking at internet scale" (arXiv 2510.09263, 2025년 10월)
- **Nature 논문**: SynthID Text 검증 논문 게재 (2024년 10월)

### 1-2. 작동 원리 (기술적 정확성)
**핵심 메커니즘**: Steganography + Neural Network

**이미지 워터마킹 과정**:
1. 생성 시점에 픽셀값 미세 수정 (인간 눈에 보이지 않음)
2. 두 개의 신경망:
   - **Embedder**: 워터마크 패턴을 픽셀에 분산 삽입
   - **Detector**: 변형된 이미지에서도 워터마크 검출
3. **Adversarial training**: 두 네트워크가 동시 훈련됨
   - JPEG 압축, 필터, 회전, 노이즈, 리사이징 공격 시뮬레이션
   - 워터마크가 약해질수록 embedder 페널티
   - 결과: 실제 변형에 견디는 워터마크

### 1-3. 핵심 특성

| 특성 | 설명 |
|---|---|
| **Invisibility** | 인간 눈으로 식별 불가, 이미지 품질 저하 없음 |
| **Holographic** | 분산 저장 — 크롭된 조각도 검출 가능 |
| **Robustness** | 압축, 리사이즈, 회전, 필터 후에도 살아남음 |
| **No "original"** | 워터마크 키 없이 생성된 원본이 존재하지 않음 |

### 1-4. 시간순 발전
| 시점 | 발전 |
|---|---|
| 2023.8 | Imagen 모델용 이미지 워터마킹 프로토타입 |
| 2024.5 | Text (Gemini), Video (Veo)로 확장 |
| 2024.10 | SynthID Text 오픈소스화 (Hugging Face Transformers) |
| 2024.10 | Nature 논문 게재 |
| 2025.10 | SynthID-Image 논문 (arXiv) — 100억+ 워터마크 |
| 2025.11 | Gemini 앱에 검증 도구 추가 |

### 1-5. 한계 (객관적 평가)
- **AI 탐지기가 아님** — Google AI 모델 출력물만 검출
- 극단적 이미지 변형(완전 재생성)에는 약함
- 의도적 적대 공격(specifically engineered attacks)에 일부 취약
- 다른 회사 AI 모델은 검출 안 됨 (각자 워터마크 시스템 필요)

### 1-6. SynthID의 핵심 비대칭
**탐지는 쉽고 제거는 불가능**:
- 키 K를 가진 자(Google)는 검출 가능
- 키를 모르는 자는 워터마크 위치 모름
- 가시 워터마크와 달리 "원본 복구" 수식 자체가 존재하지 않음

---

## 2. C2PA — 메타데이터 기반 표준

### 2-1. 표준 주체
- **C2PA**: Coalition for Content Provenance and Authenticity
- **창립 멤버**: Adobe, Microsoft, BBC, NYT, Arm (2021년)
- **현재 사양**: v2.3 (2025년 12월)
- **라이선스**: Royalty-free open standard
- **거버넌스**: Joint Development Foundation

### 2-2. 핵심 구조 — Manifest

**C2PA Manifest** = 디지털 서명된 출처 정보 패키지

구성요소:
```
Manifest
  ├── Assertions (주장들)
  │   ├── 캡처 정보 (device, GPS, timestamp)
  │   ├── 편집 이력 (edit actions)
  │   ├── AI 사용 정보 (prompt, model)
  │   └── 작성자 정보
  ├── Claim (주장의 묶음)
  │   ├── created_assertions
  │   ├── gathered_assertions
  │   └── content bindings (hash)
  └── Claim Signature (X.509 인증서로 서명)
```

### 2-3. 작동 3단계

**Stage 1: Signing**
- Claim Generator가 assertion 모음을 claim으로 묶음
- COSE 형식으로 서명 (signer's private key)
- X.509 인증서 첨부 (Certificate Authority 발급)
- 콘텐츠 해시 → hard binding 생성

**Stage 2: Embedding**
- Manifest를 JUMBF 컨테이너에 패키징
- 미디어 파일에 임베드 (또는 sidecar 파일 .c2pa)
- 지원 안 되는 포맷은 remote manifest store 사용

**Stage 3: Verification**
- Validator가 manifest 읽음
- 인증서 체인 검증 (C2PA Trust List 기준)
- Hard binding hash와 현재 파일 비교
- 변경되면 hash 불일치 → tampering 감지

### 2-4. 두 종류의 Binding

| 종류 | 설명 | 예시 |
|---|---|---|
| **Hard binding** | 암호학적 해시 — 1비트만 바뀌어도 깨짐 | SHA-256 hash |
| **Soft binding** | 메타데이터 제거돼도 콘텐츠로 재발견 | Watermark, fingerprint |

→ 흥미로운 점: **C2PA는 SynthID 같은 워터마크를 soft binding으로 활용 가능**

### 2-5. 신뢰 모델
- SSL/TLS, PDF 서명과 같은 PKI 기반
- C2PA Trust List에 등재된 CA만 인증서 발급
- C2PA Conformance Program 통과 제품만 등재
- 위조 = 현재 암호 표준을 깨야 함 (현실적으로 불가능)

### 2-6. 누가 쓰고 있나
- **Adobe**: Photoshop, Firefly (Content Credentials 브랜드)
- **Microsoft**: Bing Image Creator, Designer
- **OpenAI**: DALL-E
- **Meta**: AI 이미지 생성 도구
- **NYT, BBC**: 보도 사진 검증
- **카메라**: Leica M11-P (세계 최초 C2PA 통합 카메라)
- **Google**: 2025년 11월부터 Nano Banana Pro, Vertex AI, Google Ads

---

## 3. SynthID vs C2PA — 정확한 비교

### 3-1. 근본적 차이

| 차원 | SynthID | C2PA |
|---|---|---|
| **저장 위치** | 픽셀 자체 | 메타데이터 |
| **변경 시 동작** | 살아남음 (robust) | 깨짐 (tamper-evident) |
| **검증 주체** | 키 보유자만 | 누구나 (공개 인증서) |
| **정보 범위** | "AI 생성 여부"만 | 작성자, 편집 이력, 모델 등 풍부 |
| **표준화** | Google 독점 | 산업 표준 (Adobe, MS, NYT 등) |
| **메타데이터 제거 시** | 그대로 작동 | 무력화 (soft binding 없으면) |
| **목적** | Detection 보조 | Provenance 확립 |

### 3-2. 두 기술이 함께 작동하는 방식 (Google의 접근)

2025년 11월부터 Google이 시작한 **이중 레이어 접근**:

```
이미지 생성 시:
  1. 픽셀에 SynthID 임베드 (변형에 견딤)
  2. 메타데이터에 C2PA Manifest 첨부 (풍부한 정보)
  3. C2PA의 soft binding으로 SynthID 등록 (메타데이터 제거 시 복구)
```

**결과**: 메타데이터 제거하면 C2PA는 사라지지만, SynthID로 다시 찾을 수 있음.

---

## 4. Google의 검증 도구 (Gemini App)

### 4-1. 사용 방법
1. Gemini 앱에 이미지 업로드
2. "이 이미지가 Google AI로 만들어졌나요?" 같은 질문
3. SynthID 검출 결과 + Gemini의 추론 보고

### 4-2. 검증 가능 범위
- ✅ Google AI 모델로 생성된 이미지
- ✅ 부분적으로 SynthID 검출 (비디오의 특정 구간만)
- ❌ 다른 회사 AI (OpenAI, Adobe, MS) — 향후 C2PA로 확장 예정
- ❌ 일반 카메라 사진 (워터마크 없음)

### 4-3. 향후 확장
- SynthID를 비디오/오디오로 확장
- 다른 회사 C2PA 검증 지원
- Google Search 결과에 통합 가능성

---

## 5. AI 이미지 정책의 실용적 의미 (블로그 운영자 관점)

### 5-1. 자기 블로그에 AI 이미지 쓸 때

**자동 부착되는 것 (사용자가 신경 안 써도 됨)**:
- Google AI (Imagen, Gemini, Nano Banana Pro): SynthID + C2PA 자동
- Adobe Firefly: C2PA 자동
- DALL-E: C2PA 자동
- Microsoft Designer: C2PA 자동

**사용자가 직접 처리해야 할 것**:
- IPTC DigitalSourceType 메타데이터: AI 이미지에 "TrainedAlgorithmicMedia" 표기 필수
- 블로그 시스템에서 메타데이터 보존 (워드프레스 일부 플러그인은 제거함)

### 5-2. Google Search에 영향

**Google Merchant Center 정책 (2025년~)**:
- AI 생성 상품 이미지: IPTC 메타데이터 필수
- 누락 시 상품 노출 제한 가능

**Google Search 일반 영역**:
- 명시적 처벌 정책은 아직 없음
- 그러나 Helpful Content System이 "AI 사실 은폐"를 trustworthiness 신호로 사용

### 5-3. 메타데이터 살리는 방법
- Squoosh, ImageOptim 등에서 "Strip metadata" 옵션 끄기
- WordPress: ShortPixel, EWWW 등 플러그인의 "Remove EXIF" 옵션 끄기
- Cloudflare Images: 기본적으로 메타데이터 보존 옵션 있음
- Jekyll/Hugo: 정적 파일 그대로 서빙 시 보존됨

---

## 6. 한계와 우회 시도

### 6-1. SynthID 우회 시도
**잘 안 되는 시도**:
- JPEG 재압축 → 견딤
- 크롭 → 견딤 (분산 저장)
- 색상 조정 → 견딤
- 회전 → 견딤

**성공 가능성 있는 공격**:
- 완전 재생성 (img2img로 노이즈 가하기)
- 적대적 공격 (specifically engineered)
- 극단적 화질 저하

→ 단, 이런 우회는 이미지 품질 자체도 망가뜨림

### 6-2. C2PA 한계
- 메타데이터 제거되면 무력 (soft binding 없으면)
- 스크린샷으로 우회 가능
- Manifest 없는 카메라/도구는 어차피 검증 불가
- "C2PA 없음" = "AI 생성됐다"가 아님 (단순 정보 없음 상태)

### 6-3. 현실적 도전
- 합성 콘텐츠가 2026년까지 온라인 미디어의 90% 차지 예측
- 소비자 74%가 신뢰하는 매체의 사진/영상도 의심
- 표준 채택이 빠르지만 아직 보편적 아님

---

## 7. 1차 출처 (글에서 인용)

### Google/SynthID
1. **SynthID 공식 페이지**: https://deepmind.google/models/synthid/
2. **DeepMind 발표**: https://deepmind.google/blog/identifying-ai-generated-images-with-synthid/
3. **SynthID-Image 논문**: https://arxiv.org/abs/2510.09263
4. **Gemini 검증 도구 가이드**: https://support.google.com/gemini/answer/16722517
5. **Google 검증 발표**: https://blog.google/innovation-and-ai/products/ai-image-verification-gemini-app/

### C2PA
1. **C2PA 공식 사양 v2.3**: https://spec.c2pa.org/
2. **C2PA Explainer**: https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html
3. **C2PA FAQ**: https://c2pa.org/faqs/
4. **CAI Open Source**: https://opensource.contentauthenticity.org/
5. **CAI getting started**: https://opensource.contentauthenticity.org/docs/getting-started/

### Google Search 관련
1. **AI 콘텐츠 가이드**: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
2. **Merchant Center 정책**: https://support.google.com/merchants

---

## 8. 글에 쓸 만한 인사이트 (이면 분석)

### 인사이트 1: 두 기술의 진짜 관계 — 경쟁이 아닌 상호보완
대부분 글이 SynthID와 C2PA를 경쟁 표준처럼 다룸. 사실은 다른 레이어. SynthID는 "픽셀 안에 진실", C2PA는 "메타데이터에 진실". Google이 2025년 11월부터 둘 다 자동 부착하는 게 정답을 보여줌.

### 인사이트 2: Provenance ≠ Detection
SynthID-Image 논문이 명시: "establishing provenance is materially different from detecting AI-generated content." Detection은 신뢰성 떨어지고, 설사 가능해도 provenance를 보장하지 않음. 패러다임이 "AI 잡기"에서 "진짜 인증"으로 이동 중.

### 인사이트 3: 비대칭 — 탐지는 쉽고 제거는 불가능
SynthID의 가장 중요한 특성. 가시 워터마크는 "원본 = (워터마크 - 로고)/투명도" 수식으로 복구 가능. SynthID는 워터마크 키 없이 생성된 원본 자체가 존재하지 않음. 이게 가시 워터마크와의 근본적 차이.

### 인사이트 4: 카메라 메이커의 진입 (Leica M11-P)
2023년 Leica가 세계 최초 C2PA 통합 카메라 출시. 이건 "AI 이미지 vs 실제 사진"의 경계를 카메라 단계에서 찍는다는 의미. 보도사진의 진위 검증, 법정 증거의 chain of custody 등에 영향. AI vs 인간 양극화에서 인간 측 인프라.

---

## 9. FAQ 후보

1. SynthID와 C2PA 중 어느 게 표준이 되나요?
2. AI로 만든 이미지가 블로그에 있으면 SEO에 불리한가요?
3. SynthID 워터마크를 제거할 수 있나요?
4. 내 블로그가 메타데이터를 자동으로 제거하는데 어떻게 보존하나요?
5. C2PA 인증을 받으려면 어떻게 하나요?
6. Gemini의 검증 도구는 모든 AI 이미지를 잡아내나요?
7. 카메라로 찍은 사진도 C2PA가 붙어있나요?

---

조사 완료. 다음 단계: Claude Code 작성 명령 프롬프트.
