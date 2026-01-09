---
description: 트렌디한 글라스모피즘 스타일의 고퀄리티 PowerPoint 프레젠테이션을 생성합니다
---

# 🎨 트렌디 학술 PPT 자동 생성 워크플로우

이 워크플로우는 주제를 입력받아 **글라스모피즘 스타일**의 트렌디하고 고퀄리티 PowerPoint 프레젠테이션을 자동으로 생성합니다.
**Gemini API**를 적극 활용하여 학술적이면서도 재미있는 콘텐츠를 생성합니다.

## 사용법
```
/create_academic_ppt [주제]
```

예시: `/create_academic_ppt 양자 컴퓨팅의 미래`

---

## 🎯 디자인 특징

- 🎨 **글라스모피즘 스타일**: 투명한 배경, 블러 효과, 그라데이션
- 🌈 **트렌디한 색상**: 생동감 있는 그라데이션과 네온 컬러
- 💎 **프리미엄 느낌**: 현대적이고 세련된 디자인
- 📝 **강조 표현**: 중요 개념은 **굵은 글씨**로 강조
- 😄 **위트와 재미**: 학술적이면서도 흥미로운 비유와 예시

---

## 실행 단계

### 1. 주제 이해
- 슬래시 명령 인수에 제공된 주제를 식별합니다.
- 주제가 제공되지 않은 경우 사용자에게 "어떤 주제에 대한 프레젠테이션을 만들고 싶으신가요?"라고 묻고 응답을 기다립니다.

### 2. Gemini API로 고퀄리티 콘텐츠 생성 ⭐

**Gemini API를 사용하여 10장의 슬라이드 콘텐츠를 생성합니다.**

프롬프트 요구사항:
- **슬라이드 개수**: 10장 (타이틀 제외)
- **톤**: 학술적이면서도 재미있고 흥미로운 스타일
- **강조**: 핵심 개념은 **굵은 글씨**로 표현 (마크다운 `**텍스트**` 형식)
- **비유와 예시**: 중간중간 위트있는 비유로 이해를 돕기
- **구조**: 논리적 흐름 (도입 → 핵심 개념 → 심화 → 응용 → 미래 전망)

**JSON 구조 예시:**
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
        "**핵심 개념**: 설명과 함께",
        "재미있는 비유: 마치 ~처럼",
        "구체적인 예시와 수치",
        "**강조할 포인트**: 중요한 내용"
      ],
      "image_prompt": "modern glassmorphism style, gradient background with purple and blue tones, semi-transparent elements, blur effects, [구체적인 다이어그램 설명], professional tech illustration, vibrant colors, clean design",
      "notes": "발표자 노트 (선택사항)"
    }
  ]
}
```

**Gemini API 프롬프트 템플릿:**
```
주제: [사용자 입력 주제]

위 주제에 대한 트렌디하고 고퀄리티 프레젠테이션을 위한 10개의 슬라이드 콘텐츠를 생성해주세요.

요구사항:
1. 총 10장의 슬라이드 (논리적 구조)
2. 각 슬라이드는 4-6개의 핵심 포인트
3. **중요 개념**은 마크다운 굵은 글씨로 표현 (예: **트랜스포머**)
4. 학술적 정확성 + 위트있는 비유/예시 포함
5. 각 슬라이드마다 글라스모피즘 스타일 이미지 프롬프트 생성
6. 이미지 프롬프트는 "modern glassmorphism style, gradient background..."로 시작
7. 색상 테마: 보라-파랑 그라데이션 (#667eea, #764ba2, #f093fb)

JSON 형식으로만 응답하세요.
```

이 JSON 콘텐츠를 `slides.json` 파일에 저장합니다.

### 3. 글라스모피즘 이미지 생성 🎨

- `slides.json`의 각 슬라이드에 대해 `image_prompt`를 사용하여 이미지를 생성합니다.
- **스타일**: 글라스모피즘, 그라데이션 배경, 반투명 요소, 블러 효과
- **색상**: 보라-파랑-핑크 그라데이션 톤
- 생성된 이미지는 `images/` 디렉토리에 `slide_1.png`, `slide_2.png` 등의 이름으로 저장됩니다.

### 4. PPT 생성 (자동 실행)

생성된 JSON 파일과 이미지를 사용하여 Python 스크립트를 실행합니다.
스크립트는 자동으로 모드 1 (기존 JSON 사용)을 선택합니다.

// turbo
```bash
echo 1 | python generate_ppt.py
```

### 5. 정리 및 확인 ✅

- 출력 파일 이름 (예: `[주제]_presentation.pptx`)을 사용자에게 알려줍니다.
- 생성된 PPT 파일의 위치를 안내합니다.
- 총 슬라이드 수: 11장 (타이틀 + 콘텐츠 10장)

---

## 🎨 디자인 가이드라인

### 색상 팔레트
- **Primary**: #667eea (보라-파랑)
- **Secondary**: #764ba2 (진한 보라)
- **Accent**: #f093fb (핑크)
- **Background**: 그라데이션 (투명 효과)

### 이미지 스타일
```
modern glassmorphism style, gradient background with purple and blue tones, 
semi-transparent frosted glass elements, subtle blur effects, 
[다이어그램 설명], professional tech illustration, 
vibrant neon accents, clean minimalist design, 
soft shadows, depth layers
```

### 텍스트 강조
- **핵심 개념**: 굵은 글씨
- 일반 설명: 일반 글씨
- 비유/예시: 이탤릭 또는 특별 표시

---

## 사전 요구사항

필요한 Python 라이브러리를 설치해야 합니다:

// turbo
```bash
pip install -r requirements.txt
```

Gemini API 키가 설정되어 있어야 합니다:
```bash
# .env 파일에 API 키 설정
GEMINI_API_KEY=your_api_key_here
```

## 출력 파일
- **PPT 파일**: `output/[주제]_presentation.pptx`
- **JSON 파일**: `slides.json` (Gemini가 생성한 콘텐츠)
- **이미지 파일**: `images/slide_*.png` (10장의 글라스모피즘 이미지)

## 📊 예상 결과

- **슬라이드 수**: 11장 (타이틀 + 콘텐츠 10장)
- **스타일**: 트렌디한 글라스모피즘
- **콘텐츠**: 학술적 + 재미있는
- **품질**: 프리미엄 고퀄리티
- **생성 시간**: 약 3-5분 (Gemini API + 이미지 생성)

## 💡 팁

- 주제는 구체적일수록 좋습니다
- Gemini API가 창의적인 비유와 예시를 생성합니다
- 생성 후 PowerPoint에서 추가 편집 가능
- 색상 테마는 JSON에서 커스터마이즈 가능
