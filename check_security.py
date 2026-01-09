"""
🔒 깃허브 업로드 전 보안 체크 스크립트

이 스크립트는 깃허브에 업로드하기 전에 민감한 정보가 노출되지 않는지 확인합니다.
"""

import os
import re
import sys
from pathlib import Path

# 색상 코드
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header(text):
    """헤더 출력"""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text:^60}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

def print_success(text):
    """성공 메시지 출력"""
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    """에러 메시지 출력"""
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    """경고 메시지 출력"""
    print(f"{YELLOW}⚠️  {text}{RESET}")

def check_gitignore_exists():
    """1. .gitignore 파일 존재 확인"""
    print_header("1. .gitignore 파일 확인")
    
    if os.path.exists('.gitignore'):
        print_success(".gitignore 파일이 존재합니다.")
        return True
    else:
        print_error(".gitignore 파일이 없습니다!")
        print(f"   {YELLOW}해결 방법: .gitignore 파일을 생성하세요.{RESET}")
        return False

def check_env_in_gitignore():
    """2. .env가 .gitignore에 포함되어 있는지 확인"""
    print_header("2. .env 파일 제외 확인")
    
    if not os.path.exists('.gitignore'):
        print_error(".gitignore 파일이 없습니다!")
        return False
    
    with open('.gitignore', 'r', encoding='utf-8') as f:
        content = f.read()
    
    patterns = ['.env', '*.env', '.env.local', '.env.*.local']
    found_patterns = [p for p in patterns if p in content]
    
    if '.env' in content or '*.env' in content:
        print_success(f".env 파일이 .gitignore에 포함되어 있습니다.")
        print(f"   {BLUE}발견된 패턴: {', '.join(found_patterns)}{RESET}")
        return True
    else:
        print_error(".env 파일이 .gitignore에 없습니다!")
        print(f"   {YELLOW}해결 방법: .gitignore에 '.env'를 추가하세요.{RESET}")
        return False

def check_hardcoded_api_keys():
    """3. Python 파일에서 하드코딩된 API 키 확인"""
    print_header("3. 하드코딩된 API 키 검색")
    
    # API 키 패턴 (Google API 키는 보통 AIza로 시작)
    api_key_pattern = re.compile(r'["\']AIza[A-Za-z0-9_-]{35}["\']')
    
    issues_found = []
    
    for py_file in Path('.').rglob('*.py'):
        # __pycache__ 등 제외
        if '__pycache__' in str(py_file) or 'venv' in str(py_file):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = api_key_pattern.findall(content)
                
                if matches:
                    issues_found.append({
                        'file': str(py_file),
                        'keys': matches
                    })
        except Exception as e:
            print_warning(f"파일 읽기 실패: {py_file} - {e}")
    
    if issues_found:
        print_error(f"하드코딩된 API 키를 {len(issues_found)}개 파일에서 발견했습니다!")
        for issue in issues_found:
            print(f"\n   {RED}파일: {issue['file']}{RESET}")
            for key in issue['keys']:
                masked_key = key[:15] + '...' + key[-5:]
                print(f"   {RED}키: {masked_key}{RESET}")
        print(f"\n   {YELLOW}해결 방법: 모든 API 키를 환경 변수로 변경하세요.{RESET}")
        print(f"   {YELLOW}예시: api_key = os.getenv('GEMINI_API_KEY'){RESET}")
        return False
    else:
        print_success("하드코딩된 API 키가 발견되지 않았습니다.")
        return True

def check_env_file_exists():
    """4. .env 파일 존재 확인"""
    print_header("4. .env 파일 존재 확인")
    
    if os.path.exists('.env'):
        print_success(".env 파일이 존재합니다.")
        
        # .env 파일 내용 간단히 확인
        with open('.env', 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'GEMINI_API_KEY' in content:
            print_success("GEMINI_API_KEY가 .env 파일에 설정되어 있습니다.")
            
            if 'your_api_key_here' in content:
                print_warning(".env 파일에 예시 값이 있습니다. 실제 API 키로 변경하세요.")
        else:
            print_warning("GEMINI_API_KEY가 .env 파일에 없습니다.")
        
        return True
    else:
        print_warning(".env 파일이 없습니다.")
        print(f"   {YELLOW}.env.example을 복사하여 .env 파일을 생성하세요.{RESET}")
        return False

def check_env_example_safe():
    """5. .env.example 파일이 안전한지 확인"""
    print_header("5. .env.example 파일 안전성 확인")
    
    if not os.path.exists('.env.example'):
        print_warning(".env.example 파일이 없습니다.")
        return True
    
    with open('.env.example', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 실제 API 키 패턴 검색
    api_key_pattern = re.compile(r'AIza[A-Za-z0-9_-]{35}')
    matches = api_key_pattern.findall(content)
    
    if matches:
        print_error(".env.example에 실제 API 키가 포함되어 있습니다!")
        print(f"   {YELLOW}해결 방법: .env.example의 API 키를 'your_api_key_here'로 변경하세요.{RESET}")
        return False
    else:
        print_success(".env.example 파일이 안전합니다.")
        return True

def check_git_status():
    """6. Git 상태 확인 (Git이 초기화되어 있다면)"""
    print_header("6. Git 상태 확인")
    
    if not os.path.exists('.git'):
        print_warning("Git 저장소가 초기화되지 않았습니다.")
        print(f"   {BLUE}git init 명령어로 초기화하세요.{RESET}")
        return True
    
    # git status 실행
    import subprocess
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        files = result.stdout.strip().split('\n')
        
        # .env 파일이 추적되고 있는지 확인
        env_tracked = any('.env' in f and not '.env.example' in f for f in files)
        
        if env_tracked:
            print_error(".env 파일이 Git에 추적되고 있습니다!")
            print(f"   {YELLOW}해결 방법:{RESET}")
            print(f"   {YELLOW}1. git rm --cached .env{RESET}")
            print(f"   {YELLOW}2. .gitignore에 .env가 있는지 확인{RESET}")
            return False
        else:
            print_success(".env 파일이 Git에 추적되지 않습니다.")
            return True
    except Exception as e:
        print_warning(f"Git 상태 확인 실패: {e}")
        return True

def check_sensitive_files():
    """7. 기타 민감한 파일 확인"""
    print_header("7. 기타 민감한 파일 확인")
    
    sensitive_patterns = [
        'config.json',
        'secrets.json',
        'credentials.json',
        '*.pem',
        '*.key',
        'id_rsa',
        'id_dsa'
    ]
    
    found_files = []
    
    for pattern in sensitive_patterns:
        for file in Path('.').rglob(pattern):
            if '.git' not in str(file) and 'venv' not in str(file):
                found_files.append(str(file))
    
    if found_files:
        print_warning(f"민감할 수 있는 파일 {len(found_files)}개를 발견했습니다:")
        for file in found_files:
            print(f"   {YELLOW}- {file}{RESET}")
        print(f"\n   {YELLOW}이 파일들이 .gitignore에 포함되어 있는지 확인하세요.{RESET}")
        return False
    else:
        print_success("민감한 파일이 발견되지 않았습니다.")
        return True

def main():
    """메인 함수"""
    print(f"\n{BOLD}{BLUE}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║        🔒 깃허브 업로드 전 보안 체크 스크립트 🔒         ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"{RESET}\n")
    
    checks = [
        ("1. .gitignore 존재", check_gitignore_exists),
        ("2. .env 제외 확인", check_env_in_gitignore),
        ("3. 하드코딩된 API 키", check_hardcoded_api_keys),
        ("4. .env 파일 존재", check_env_file_exists),
        ("5. .env.example 안전성", check_env_example_safe),
        ("6. Git 상태", check_git_status),
        ("7. 민감한 파일", check_sensitive_files),
    ]
    
    results = []
    
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print_error(f"{name} 체크 중 오류 발생: {e}")
            results.append((name, False))
    
    # 결과 요약
    print_header("📊 검사 결과 요약")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        if result:
            print_success(f"{name}: 통과")
        else:
            print_error(f"{name}: 실패")
    
    print(f"\n{BOLD}총 {total}개 항목 중 {passed}개 통과{RESET}")
    
    # 최종 판정
    print_header("🎯 최종 판정")
    
    critical_checks = [
        results[1][1],  # .env 제외 확인
        results[2][1],  # 하드코딩된 API 키
        results[4][1],  # .env.example 안전성
    ]
    
    if all(critical_checks):
        print(f"{GREEN}{BOLD}")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║                                                            ║")
        print("║              ✅ 깃허브 업로드 준비 완료! ✅               ║")
        print("║                                                            ║")
        print("║         모든 중요 보안 검사를 통과했습니다.               ║")
        print("║         안전하게 깃허브에 업로드할 수 있습니다.           ║")
        print("║                                                            ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print(f"{RESET}\n")
        
        print(f"{BLUE}다음 단계:{RESET}")
        print(f"  1. git init")
        print(f"  2. git add .")
        print(f"  3. git commit -m \"Initial commit\"")
        print(f"  4. git remote add origin <your-repo-url>")
        print(f"  5. git push -u origin main")
        
        return 0
    else:
        print(f"{RED}{BOLD}")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║                                                            ║")
        print("║              ⚠️  보안 문제 발견! ⚠️                      ║")
        print("║                                                            ║")
        print("║         위의 오류를 수정한 후 다시 시도하세요.            ║")
        print("║                                                            ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print(f"{RESET}\n")
        
        print(f"{YELLOW}해결 후 다시 실행하세요:{RESET}")
        print(f"  python check_security.py")
        
        return 1

if __name__ == "__main__":
    sys.exit(main())
