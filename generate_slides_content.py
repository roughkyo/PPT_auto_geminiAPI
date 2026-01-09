"""
Gemini API를 사용하여 고퀄리티 슬라이드 콘텐츠를 생성하는 스크립트
"""

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Gemini API 초기화
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("❌ GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# 주제
topic = "어텐션과 트랜스포머, 그리고 GPT"

# 프롬프트
prompt = f"""
주제: {topic}

위 주제에 대한 트렌디하고 고퀄리티 프레젠테이션을 위한 10개의 슬라이드 콘텐츠를 생성해주세요.

각 슬라이드는 다음 형식의 JSON으로 작성해주세요:

{{
  "topic": "{topic}",
  "design_theme": {{
    "primary_color": "#667eea",
    "secondary_color": "#764ba2",
    "accent_color": "#f093fb",
    "style": "glassmorphism"
  }},
  "slides": [
    {{
      "title": "슬라이드 제목",
      "content": [
        "**핵심 개념**: 설명과 함께",
        "재미있는 비유: 마치 ~처럼",
        "구체적인 예시와 수치",
        "**강조할 포인트**: 중요한 내용"
      ],
      "image_prompt": "modern glassmorphism style, gradient background with purple and blue tones, semi-transparent frosted glass elements, subtle blur effects, [구체적인 다이어그램 설명], professional tech illustration, vibrant neon accents, clean minimalist design, soft shadows, depth layers"
    }}
  ]
}}

요구사항:
1. 총 10장의 슬라이드 (논리적 구조: 도입 → 핵심 개념 → 심화 → 응용 → 미래 전망)
2. 각 슬라이드는 4-6개의 핵심 포인트로 구성
3. **중요 개념**은 마크다운 굵은 글씨로 표현 (예: **트랜스포머**, **어텐션 메커니즘**)
4. 학술적 정확성을 유지하면서도 위트있는 비유와 예시를 포함
   - 예: "마치 ~처럼", "~와 비슷하게", "쉽게 말하면 ~"
5. 각 슬라이드마다 글라스모피즘 스타일 이미지 프롬프트 생성
6. 이미지 프롬프트는 반드시 "modern glassmorphism style, gradient background with purple and blue tones..."로 시작
7. 색상 테마: 보라-파랑-핑크 그라데이션 (#667eea, #764ba2, #f093fb)
8. 전문적이면서도 흥미롭고 재미있는 톤 유지
9. 각 포인트는 간결하지만 정보가 풍부하게

JSON 형식만 반환하고, 다른 설명은 포함하지 마세요.
"""

print("\n" + "="*60)
print("🤖 Gemini API로 고퀄리티 슬라이드 생성 중...")
print("="*60)
print(f"📝 주제: {topic}")
print(f"📊 슬라이드 개수: 10장")
print(f"🎨 스타일: 글라스모피즘 (보라-파랑 그라데이션)")
print(f"✨ 특징: 학술적 + 위트있는 콘텐츠")
print("\n⏳ 생성 중... (약 30초 소요)")

try:
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.8,  # 창의성을 높여 위트있는 콘텐츠 생성
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,  # 10장 슬라이드를 위해 토큰 수 증가
        )
    )
    
    # JSON 파싱
    content = response.text.strip()
    
    # 마크다운 코드 블록 제거
    if content.startswith('```'):
        content = content.split('```')[1]
        if content.startswith('json'):
            content = content[4:]
        content = content.strip()
    
    slides_data = json.loads(content)
    
    # slides.json에 저장
    with open('slides.json', 'w', encoding='utf-8') as f:
        json.dump(slides_data, f, ensure_ascii=False, indent=2)
    
    print("\n✅ 슬라이드 콘텐츠 생성 완료!")
    print(f"📁 저장 위치: slides.json")
    print(f"📊 생성된 슬라이드 수: {len(slides_data.get('slides', []))}장")
    print(f"🎨 디자인 테마: {slides_data.get('design_theme', {}).get('style', 'default')}")
    
    # 슬라이드 제목 출력
    print("\n📋 슬라이드 목록:")
    for i, slide in enumerate(slides_data.get('slides', []), 1):
        print(f"  {i}. {slide.get('title', 'N/A')}")
    
    print("\n" + "="*60)
    
except json.JSONDecodeError as e:
    print(f"\n❌ JSON 파싱 오류: {e}")
    print(f"응답 내용: {response.text[:500]}...")
except Exception as e:
    print(f"\n❌ 오류 발생: {e}")
