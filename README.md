# 🎨 트렌디 학술 PPT 자동 생성 (Gemini API 활용)

**글라스모피즘 스타일**의 트렌디하고 고퀄리티 PowerPoint 프레젠테이션을 자동으로 생성하는 Python 스크립트입니다.
**Google Gemini API**를 적극 활용하여 학술적이면서도 재미있는 콘텐츠를 생성합니다.

## ✨ 주요 기능

- 🎨 **글라스모피즘 디자인**: 투명한 배경, 블러 효과, 보라-파랑 그라데이션
- 🤖 **Gemini API 통합**: 주제만 입력하면 10장의 고퀄리티 슬라이드 자동 생성
- 💎 **프리미엄 스타일**: 현대적이고 세련된 디자인
- 📝 **스마트 강조**: 핵심 개념은 **굵은 글씨**로 자동 강조
- 😄 **위트와 재미**: 학술적이면서도 흥미로운 비유와 예시 포함
- 🖼️ **이미지 자동 생성**: 각 슬라이드에 글라스모피즘 스타일 이미지 포함
- 🔧 **3가지 생성 모드**: 기존 JSON 사용, 새로운 생성, 콘텐츠 개선

## 🎯 디자인 특징
### 스타일
- 글라스모피즘 (Glassmorphism)
- 반투명 요소와 블러 효과
- 네온 컬러 악센트
- 깔끔한 미니멀 디자인

## 🚀 빠른 시작

### 1. 설치

```bash
pip install -r requirements.txt
```

### 2. API 키 설정

[Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 발급 후:

```powershell
# .env 파일 생성
Copy-Item .env.example .env

# 메모장으로 열어서 API 키 입력
notepad .env
```

### 3. PPT 생성

```bash
python generate_ppt.py
```

**모드 2 선택** → 주제 입력 → 완성! 🎉

## 📖 사용 방법

### 모드 1: 기존 JSON 파일 사용

```
선택: 1
JSON 파일 경로: slides.json
```

### 모드 2: Gemini API로 새로운 슬라이드 생성 ⭐ (추천)

```
선택: 2
주제: 양자 컴퓨팅의 미래
슬라이드 개수: 10
```

**특징:**
- 10장의 고퀄리티 슬라이드 자동 생성
- 글라스모피즘 스타일 이미지 프롬프트 포함
- 학술적 + 위트있는 콘텐츠
- **핵심 개념** 자동 강조
- 재미있는 비유와 예시

### 모드 3: 기존 콘텐츠를 Gemini API로 개선

```
선택: 3
JSON 파일 경로: slides_example.json
```

## 🎨 워크플로우 사용

슬래시 명령으로 한 번에 생성:

```
/create_academic_ppt 양자 컴퓨팅의 미래
```

자동으로:
1. Gemini API로 10장 슬라이드 콘텐츠 생성
2. 글라스모피즘 스타일 이미지 10장 생성
3. PPT 파일 생성

## 📊 Gemini API 품질 향상

### 고퀄리티 콘텐츠 생성

```python
temperature=0.8,      # 창의성 높음 (위트있는 비유)
top_p=0.95,          # 다양성 증가
max_output_tokens=8192,  # 10장 슬라이드 지원
```

### 생성되는 콘텐츠 예시

```json
{
  "title": "트랜스포머의 핵심: 어텐션 메커니즘",
  "content": [
    "**어텐션(Attention)**: 마치 칵테일 파티에서 특정 대화에 집중하는 것처럼, 중요한 정보에 가중치를 부여",
    "**Query-Key-Value 구조**: 도서관에서 책을 찾는 것과 비슷 - Query(검색어), Key(색인), Value(실제 내용)",
    "**스케일드 닷-프로덕트**: 수식 Attention(Q,K,V) = softmax(QK^T/√d_k)V",
    "**병렬 처리의 혁신**: RNN과 달리 모든 단어를 동시에 처리 → 속도 100배 향상",
    "**멀티-헤드 어텐션**: 여러 관점에서 동시에 정보 파악 (8-16개 헤드 사용)"
  ]
}
```

## 🎯 JSON 파일 형식

```json
{
  "topic": "주제명",
  "design_theme": {
    "primary_color": "#667eea",
    "secondary_color": "#764ba2",
    "accent_color": "#f093fb",
    "style": "glassmorphism"
  },
  "slides": [
    {
      "title": "슬라이드 제목",
      "content": [
        "**핵심 개념**: 설명",
        "재미있는 비유: 마치 ~처럼",
        "구체적인 예시와 수치"
      ],
      "image_prompt": "modern glassmorphism style, gradient background with purple and blue tones..."
    }
  ]
}
```

## 💡 팁

### 좋은 주제 예시

- ✅ "의료 분야에서의 인공지능 활용과 윤리적 고려사항"
- ✅ "블록체인 기술의 원리와 실제 응용 사례"
- ✅ "양자 컴퓨팅: 원리부터 미래 전망까지"

### 슬라이드 개수

- **짧은 발표**: 5-7장
- **일반 발표**: 8-10장 (추천)
- **긴 발표**: 10-15장

### 이미지 스타일

모든 이미지는 자동으로 다음 스타일로 생성됩니다:
- 글라스모피즘 효과
- 보라-파랑-핑크 그라데이션
- 반투명 요소
- 네온 악센트

## 📁 출력 파일

- **PPT 파일**: `output/[주제]_presentation.pptx`
- **생성된 JSON**: `slides_generated_[날짜시간].json`
- **개선된 JSON**: `slides_enhanced_[날짜시간].json`
- **이미지**: `images/slide_*.png`

## 🔧 고급 설정

### Gemini API 파라미터 조정

`generate_ppt.py`에서 수정:

```python
generation_config=genai.types.GenerationConfig(
    temperature=0.8,      # 0.0-1.0: 창의성 조절
    top_p=0.95,          # 다양성 제어
    top_k=40,            # 토큰 선택 범위
    max_output_tokens=8192,  # 최대 출력 길이
)
```

### 추천 설정

- **학술 논문**: `temperature=0.5` (정확성 중시)
- **일반 프레젠테이션**: `temperature=0.7` (균형)
- **창의적 발표**: `temperature=0.8-0.9` (위트와 창의성)

## ❓ 자주 묻는 질문

**Q: 글라스모피즘 스타일이 뭔가요?**
A: 반투명한 유리 같은 효과로, 블러와 그라데이션을 활용한 현대적인 디자인 트렌드입니다.

**Q: 굵은 글씨는 어떻게 표시되나요?**
A: Gemini API가 자동으로 `**텍스트**` 형식으로 생성하며, PPT에서 강조 표시됩니다.

**Q: 위트있는 비유는 어떻게 생성되나요?**
A: Gemini API가 학술적 정확성을 유지하면서도 이해하기 쉬운 비유를 자동으로 추가합니다.

**Q: 이미지 스타일을 변경할 수 있나요?**
A: 네! JSON 파일의 `image_prompt`를 수정하거나, 워크플로우의 프롬프트를 변경하세요.

**Q: 슬라이드 개수를 변경할 수 있나요?**
A: 네! 모드 2에서 원하는 개수를 입력하거나, 기본값(10)을 사용하세요.

## 🎓 예제

### 생성된 프레젠테이션 예시

**주제**: "어텐션과 트랜스포머, 그리고 GPT"

**슬라이드 구성**:
1. 타이틀 슬라이드
2. 어텐션 메커니즘의 등장
3. 트랜스포머 아키텍처
4. 셀프 어텐션의 작동 원리
5. GPT: 생성형 사전학습 트랜스포머
6. 트랜스포머의 영향과 미래
7. ... (총 11장)

## 🔒 보안

### ⚠️ 중요: 깃허브 업로드 전 체크리스트

**반드시 확인하세요!**

- ✅ `.env` 파일이 `.gitignore`에 포함되어 있는지 확인
- ✅ 코드에 하드코딩된 API 키가 없는지 확인
- ✅ `.env.example` 파일에는 실제 키가 아닌 예시만 있는지 확인
- ✅ `git status`로 `.env` 파일이 추적되지 않는지 확인


## 📚 문서

- `QUICKSTART.md` - 5분 빠른 시작
- `API_SETUP_GUIDE.md` - 상세한 API 설정 방법
- `.agent/workflows/create_academic_ppt.md` - 워크플로우 가이드

## 🎉 시작하기

```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. API 키 설정
Copy-Item .env.example .env
notepad .env

# 3. PPT 생성
python generate_ppt.py
```

**모드 2 선택 → 주제 입력 → 완성!** 🚀

---

**Made with ❤️ using Google Gemini API**
