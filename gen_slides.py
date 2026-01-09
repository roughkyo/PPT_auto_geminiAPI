import os
import json
import sys

# UTF-8 출력 설정
sys.stdout.reconfigure(encoding='utf-8')

import google.generativeai as genai
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키를 환경 변수에서 가져오기
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("❌ 오류: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
    print("📝 .env 파일에 다음과 같이 설정해주세요:")
    print("   GEMINI_API_KEY=your_api_key_here")
    sys.exit(1)

if api_key == "your_api_key_here":
    print("❌ 오류: .env 파일의 API 키를 실제 키로 변경해주세요.")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

topic = "어텐션과 트랜스포머, 그리고 GPT"

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

print("Generating slides...")

try:
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.8,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
        )
    )
    
    content = response.text.strip()
    
    if content.startswith('```'):
        content = content.split('```')[1]
        if content.startswith('json'):
            content = content[4:]
        content = content.strip()
    
    slides_data = json.loads(content)
    
    with open('slides.json', 'w', encoding='utf-8') as f:
        json.dump(slides_data, f, ensure_ascii=False, indent=2)
    
    print(f"SUCCESS: Generated {len(slides_data.get('slides', []))} slides")
    print(f"Saved to: slides.json")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
