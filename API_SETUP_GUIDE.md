# Google Gemini API 설정 가이드

이 가이드는 Google Gemini API를 설정하고 사용하는 방법을 단계별로 설명합니다.

## 📋 목차

1. [API 키 발급받기](#1-api-키-발급받기)
2. [환경 변수 설정](#2-환경-변수-설정)
3. [설정 확인](#3-설정-확인)
4. [사용 예제](#4-사용-예제)
5. [문제 해결](#5-문제-해결)

---

## 1. API 키 발급받기

### 단계 1: Google AI Studio 접속

1. 웹 브라우저에서 [Google AI Studio](https://makersuite.google.com/app/apikey) 접속
2. Google 계정으로 로그인
   - Gmail 계정이 필요합니다
   - 없다면 [Google 계정 만들기](https://accounts.google.com/signup)

### 단계 2: API 키 생성

1. **"Get API Key"** 또는 **"Create API Key"** 버튼 클릭
2. 두 가지 옵션이 나타납니다:
   - **Create API key in new project**: 새 프로젝트 생성 (추천)
   - **Create API key in existing project**: 기존 프로젝트 사용

3. 원하는 옵션 선택 후 생성 버튼 클릭

### 단계 3: API 키 복사

1. 생성된 API 키가 화면에 표시됩니다
   - 형식: `AIzaSy...` (약 39자)
2. **"Copy"** 버튼을 클릭하여 클립보드에 복사
3. ⚠️ **중요**: 이 키는 다시 확인할 수 없으므로 안전한 곳에 보관하세요

### API 키 예시

```
AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe
```

---

## 2. 환경 변수 설정

### 방법 1: .env 파일 사용 (추천) ⭐

#### Windows (PowerShell)

```powershell
# 프로젝트 디렉토리로 이동
cd "c:\Users\ysj\Desktop\upload_all\PPT오토geminiAPI"

# .env.example을 복사하여 .env 파일 생성
Copy-Item .env.example .env

# 메모장으로 .env 파일 열기
notepad .env
```

#### Windows (CMD)

```cmd
cd "c:\Users\ysj\Desktop\upload_all\PPT오토geminiAPI"
copy .env.example .env
notepad .env
```

#### .env 파일 편집

메모장이 열리면 다음과 같이 수정:

```env
GEMINI_API_KEY=AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe
```

- `your_api_key_here`를 실제 발급받은 API 키로 교체
- 저장 후 닫기 (Ctrl+S)

### 방법 2: 시스템 환경 변수 설정

#### Windows

1. **시작 메뉴** → **"환경 변수"** 검색
2. **"시스템 환경 변수 편집"** 클릭
3. **"환경 변수"** 버튼 클릭
4. **"사용자 변수"** 섹션에서 **"새로 만들기"** 클릭
5. 변수 이름: `GEMINI_API_KEY`
6. 변수 값: 발급받은 API 키 입력
7. **확인** 클릭

#### PowerShell (현재 세션만)

```powershell
$env:GEMINI_API_KEY = "AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe"
```

---

## 3. 설정 확인

### Python으로 확인

```python
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API 키 확인
api_key = os.getenv('GEMINI_API_KEY')

if api_key:
    print(f"✓ API 키가 설정되었습니다: {api_key[:10]}...")
else:
    print("❌ API 키가 설정되지 않았습니다.")
```

### 간단한 테스트

프로젝트 디렉토리에서 다음 명령 실행:

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✓ API 키 설정됨' if os.getenv('GEMINI_API_KEY') else '❌ API 키 없음')"
```

---

## 4. 사용 예제

### 기본 사용법

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# API 설정
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# 모델 초기화
model = genai.GenerativeModel('gemini-pro')

# 텍스트 생성
response = model.generate_content("양자 컴퓨팅에 대해 설명해주세요.")
print(response.text)
```

### PPT 생성 스크립트 실행

```bash
python generate_ppt.py
```

실행 후:
1. 모드 선택: `2` (Gemini API로 새로운 슬라이드 생성)
2. 주제 입력: `양자 컴퓨팅의 미래`
3. 슬라이드 개수: `5`

---

## 5. 문제 해결

### ❌ "GEMINI_API_KEY 환경 변수가 설정되지 않았습니다"

**원인**: API 키가 제대로 설정되지 않음

**해결 방법**:
1. `.env` 파일이 프로젝트 루트 디렉토리에 있는지 확인
2. `.env` 파일 내용 확인:
   ```env
   GEMINI_API_KEY=실제_API_키
   ```
3. 공백이나 따옴표가 없는지 확인
4. Python 스크립트를 재실행

### ❌ "API key not valid"

**원인**: 잘못된 API 키 또는 만료된 키

**해결 방법**:
1. [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 재확인
2. 새 API 키 생성
3. `.env` 파일 업데이트

### ❌ "Quota exceeded"

**원인**: API 사용량 한도 초과

**해결 방법**:
1. [Google Cloud Console](https://console.cloud.google.com/)에서 할당량 확인
2. 무료 티어 한도 확인
3. 필요시 유료 플랜으로 업그레이드

### ❌ "Module not found: google.generativeai"

**원인**: 패키지가 설치되지 않음

**해결 방법**:
```bash
pip install google-generativeai python-dotenv
```

또는

```bash
pip install -r requirements.txt
```

### ❌ ".env 파일을 찾을 수 없습니다"

**원인**: 잘못된 디렉토리에서 실행

**해결 방법**:
```bash
# 프로젝트 디렉토리로 이동
cd "c:\Users\ysj\Desktop\upload_all\PPT오토geminiAPI"

# 현재 디렉토리 확인
pwd  # PowerShell
cd   # CMD

# .env 파일 존재 확인
ls .env  # PowerShell
dir .env # CMD
```

---

## 📊 API 사용량 및 요금

### 무료 티어 (2024년 1월 기준)

- **분당 요청**: 60회
- **일일 요청**: 1,500회
- **월별 토큰**: 무료

### 요금 확인

- [Google AI Pricing](https://ai.google.dev/pricing)에서 최신 요금 확인

---

## 🔒 보안 주의사항

1. ⚠️ **절대 API 키를 코드에 직접 입력하지 마세요**
   ```python
   # ❌ 나쁜 예
   api_key = "AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe"
   
   # ✅ 좋은 예
   api_key = os.getenv('GEMINI_API_KEY')
   ```

2. ⚠️ **`.env` 파일을 Git에 커밋하지 마세요**
   - `.gitignore`에 `.env`가 포함되어 있는지 확인

3. ⚠️ **API 키를 공개 저장소에 올리지 마세요**
   - GitHub, GitLab 등에 실수로 업로드하지 않도록 주의

4. ⚠️ **API 키가 노출되었다면 즉시 폐기하세요**
   - [Google AI Studio](https://makersuite.google.com/app/apikey)에서 키 삭제
   - 새 키 생성

---

## 📚 추가 자료

- [Google Gemini API 공식 문서](https://ai.google.dev/docs)
- [Python SDK 문서](https://ai.google.dev/api/python/google/generativeai)
- [API 레퍼런스](https://ai.google.dev/api)
- [예제 코드](https://github.com/google/generative-ai-python)

---

## ✅ 체크리스트

설정이 완료되었는지 확인하세요:

- [ ] Google AI Studio에서 API 키 발급
- [ ] `.env` 파일 생성 및 API 키 입력
- [ ] 필수 패키지 설치 (`pip install -r requirements.txt`)
- [ ] API 키 설정 확인 (테스트 스크립트 실행)
- [ ] `.gitignore`에 `.env` 포함 확인
- [ ] `generate_ppt.py` 실행 테스트

모든 항목이 체크되었다면 사용 준비 완료입니다! 🎉
