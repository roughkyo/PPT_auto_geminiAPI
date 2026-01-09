# 🚀 깃허브 업로드 가이드

## ✅ 보안 체크리스트 (필수!)

깃허브에 업로드하기 전에 **반드시** 다음 사항을 확인하세요:

### 1. `.gitignore` 파일 확인 ✅
- [x] `.gitignore` 파일이 프로젝트 루트에 존재
- [x] `.env` 파일이 `.gitignore`에 포함됨
- [x] 모든 민감한 정보가 제외 목록에 포함됨

### 2. API 키 보안 확인 ✅
- [x] 모든 Python 파일에서 하드코딩된 API 키 제거됨
- [x] `.env` 파일에만 실제 API 키 저장
- [x] `.env.example`에는 예시 값만 포함

### 3. 파일 확인 ✅
```powershell
# 현재 디렉토리의 모든 파일 확인
Get-ChildItem -Recurse -File | Select-Object FullName
```

---

## 📋 깃허브 업로드 단계별 가이드

### Step 1: Git 저장소 초기화

```powershell
# Git 저장소 초기화
git init

# 현재 상태 확인
git status
```

### Step 2: .env 파일이 제외되는지 확인

```powershell
# .gitignore가 제대로 작동하는지 확인
git check-ignore -v .env

# 출력 예시:
# .gitignore:5:.env    .env
# ↑ 이렇게 나오면 안전합니다!
```

**⚠️ 중요**: 만약 `.env` 파일이 추적되고 있다면:
```powershell
# .env 파일을 추적에서 제거
git rm --cached .env

# .gitignore 파일 확인
notepad .gitignore
```

### Step 3: 파일 추가 및 커밋

```powershell
# 모든 파일 추가 (단, .gitignore에 있는 파일은 제외됨)
git add .

# 추가된 파일 확인 (.env가 없어야 함!)
git status

# 커밋
git commit -m "Initial commit: PPT 자동 생성 프로젝트"
```

### Step 4: 깃허브 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단 `+` 버튼 클릭 → `New repository`
3. 저장소 이름 입력 (예: `ppt-auto-generator`)
4. Public 또는 Private 선택
5. **"Initialize this repository with a README" 체크 해제** (이미 로컬에 README가 있음)
6. `Create repository` 클릭

### Step 5: 원격 저장소 연결 및 푸시

```powershell
# 원격 저장소 추가 (YOUR_USERNAME과 REPO_NAME을 실제 값으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 기본 브랜치 이름을 main으로 설정
git branch -M main

# 푸시
git push -u origin main
```

---

## 🔍 최종 보안 검증

### 깃허브에 업로드된 후 확인할 사항

1. **깃허브 저장소 페이지에서 확인**:
   - `.env` 파일이 **없는지** 확인
   - `.env.example` 파일은 **있는지** 확인
   - 코드에 API 키가 **노출되지 않았는지** 확인

2. **검색으로 확인**:
   - 깃허브 저장소에서 `AIza` 검색
   - 결과가 없어야 안전!

---

## 🚨 만약 실수로 API 키를 업로드했다면?

### 즉시 조치 사항

1. **API 키 즉시 삭제**
   - [Google AI Studio](https://makersuite.google.com/app/apikey) 접속
   - 노출된 API 키 삭제
   - 새로운 API 키 발급

2. **Git 히스토리에서 완전히 제거**
   ```powershell
   # 민감한 파일을 히스토리에서 완전히 제거
   git filter-branch --force --index-filter `
     "git rm --cached --ignore-unmatch .env" `
     --prune-empty --tag-name-filter cat -- --all
   
   # 강제 푸시
   git push origin --force --all
   ```

3. **더 안전한 방법 (BFG Repo-Cleaner 사용)**
   ```powershell
   # BFG 다운로드
   # https://rtyley.github.io/bfg-repo-cleaner/
   
   # .env 파일 완전히 제거
   java -jar bfg.jar --delete-files .env
   
   # 정리
   git reflog expire --expire=now --all
   git gc --prune=now --aggressive
   
   # 강제 푸시
   git push origin --force --all
   ```

---

## 📝 체크리스트 요약

업로드 전 마지막 확인:

- [ ] `.gitignore` 파일이 존재하고 `.env`를 포함하는가?
- [ ] `git status`에서 `.env` 파일이 보이지 않는가?
- [ ] `git check-ignore -v .env` 명령어가 정상 작동하는가?
- [ ] 모든 Python 파일에서 하드코딩된 API 키를 제거했는가?
- [ ] `.env.example`에는 실제 키가 아닌 예시만 있는가?
- [ ] README.md에 보안 가이드가 포함되어 있는가?

**모든 항목이 체크되었다면 안전하게 업로드할 수 있습니다!** ✅

---

## 🎯 추가 보안 팁

### GitHub Secrets 사용 (CI/CD용)

만약 GitHub Actions를 사용한다면:

1. 저장소 Settings → Secrets and variables → Actions
2. `New repository secret` 클릭
3. Name: `GEMINI_API_KEY`
4. Value: 실제 API 키 입력

### .env 파일 백업

```powershell
# .env 파일을 안전한 곳에 백업 (깃허브 외부)
Copy-Item .env ~\Documents\backup\.env.backup
```

---

**✨ 이제 안전하게 깃허브에 업로드할 준비가 완료되었습니다!**
