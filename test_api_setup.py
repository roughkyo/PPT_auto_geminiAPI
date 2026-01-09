"""
Gemini API 설정 테스트 스크립트
API 키가 올바르게 설정되었는지 확인합니다.
"""

import os
from dotenv import load_dotenv

def test_env_file():
    """환경 변수 파일 확인"""
    print("\n" + "="*60)
    print("🔍 환경 변수 파일 확인")
    print("="*60)
    
    if os.path.exists('.env'):
        print("✓ .env 파일이 존재합니다.")
    else:
        print("❌ .env 파일이 없습니다.")
        print("   .env.example을 복사하여 .env 파일을 만드세요:")
        print("   PowerShell: Copy-Item .env.example .env")
        print("   CMD: copy .env.example .env")
        return False
    
    return True


def test_api_key():
    """API 키 확인"""
    print("\n" + "="*60)
    print("🔑 API 키 확인")
    print("="*60)
    
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
        print("   .env 파일을 열고 API 키를 설정하세요:")
        print("   GEMINI_API_KEY=your_api_key_here")
        return False
    
    if api_key == "your_api_key_here":
        print("❌ API 키가 기본값으로 설정되어 있습니다.")
        print("   .env 파일에 실제 API 키를 입력하세요.")
        return False
    
    if not api_key.startswith("AIza"):
        print("⚠ 경고: API 키 형식이 올바르지 않을 수 있습니다.")
        print(f"   API 키는 보통 'AIza'로 시작합니다. 현재: {api_key[:4]}...")
    
    print(f"✓ API 키가 설정되었습니다: {api_key[:10]}...{api_key[-4:]}")
    print(f"  (길이: {len(api_key)} 문자)")
    
    return True


def test_packages():
    """필수 패키지 설치 확인"""
    print("\n" + "="*60)
    print("📦 필수 패키지 확인")
    print("="*60)
    
    packages = {
        'google.generativeai': 'google-generativeai',
        'dotenv': 'python-dotenv',
        'pptx': 'python-pptx',
        'PIL': 'Pillow'
    }
    
    all_installed = True
    
    for module_name, package_name in packages.items():
        try:
            __import__(module_name)
            print(f"✓ {package_name} 설치됨")
        except ImportError:
            print(f"❌ {package_name} 설치 필요")
            all_installed = False
    
    if not all_installed:
        print("\n다음 명령으로 패키지를 설치하세요:")
        print("  pip install -r requirements.txt")
        return False
    
    return True


def test_api_connection():
    """Gemini API 연결 테스트"""
    print("\n" + "="*60)
    print("🌐 Gemini API 연결 테스트")
    print("="*60)
    
    try:
        import google.generativeai as genai
        
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key or api_key == "your_api_key_here":
            print("⚠ API 키가 설정되지 않아 연결 테스트를 건너뜁니다.")
            return False
        
        print("API 연결 시도 중...")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        print("간단한 테스트 요청 전송 중...")
        response = model.generate_content(
            "안녕하세요! 짧게 인사해주세요.",
            generation_config=genai.types.GenerationConfig(
                temperature=0.5,
                max_output_tokens=50,
            )
        )
        
        print("✓ API 연결 성공!")
        print(f"\n테스트 응답:\n{response.text}\n")
        return True
        
    except Exception as e:
        print(f"❌ API 연결 실패: {e}")
        print("\n가능한 원인:")
        print("  1. API 키가 올바르지 않음")
        print("  2. 인터넷 연결 문제")
        print("  3. API 할당량 초과")
        print("  4. API 키가 비활성화됨")
        return False


def main():
    """메인 테스트 함수"""
    print("\n" + "="*60)
    print("🧪 Gemini API 설정 테스트")
    print("="*60)
    
    results = {
        "환경 변수 파일": test_env_file(),
        "API 키": test_api_key(),
        "필수 패키지": test_packages(),
    }
    
    # 기본 설정이 완료된 경우에만 API 연결 테스트
    if all(results.values()):
        results["API 연결"] = test_api_connection()
    
    # 최종 결과
    print("\n" + "="*60)
    print("📊 테스트 결과 요약")
    print("="*60)
    
    for test_name, result in results.items():
        status = "✅ 통과" if result else "❌ 실패"
        print(f"{test_name}: {status}")
    
    print("\n" + "="*60)
    
    if all(results.values()):
        print("🎉 모든 테스트 통과! Gemini API를 사용할 준비가 되었습니다.")
        print("\n다음 명령으로 PPT를 생성할 수 있습니다:")
        print("  python generate_ppt.py")
    else:
        print("⚠ 일부 테스트가 실패했습니다. 위의 오류 메시지를 확인하세요.")
        print("\n자세한 설정 방법은 API_SETUP_GUIDE.md를 참조하세요.")
    
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
