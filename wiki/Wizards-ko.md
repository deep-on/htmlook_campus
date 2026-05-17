# 위자드

> 진행 중 만나게 될 setup 마법사들 — 무엇을 묻고, 무엇을 하고, 언제 다시 나타나는지.

위자드는 짧은 모달 시퀀스 — 보통 3~5 카드 — 로 올바른 상태에 도달하게 돕습니다. 절대 가두지 않음 (모든 위자드에 *Skip* / *Later* 있음) 그리고 대응 메뉴에서 언제든 다시 실행 가능.

## 첫 AI Setup (Pro)

**등장**: ⌘I 처음 누르거나 AI 어시스턴트 글리프 클릭 시.
**질문**: provider 선택 (OpenAI / DeepSeek / Mistral / Together / Groq / Cerebras / Ollama / Custom) → API 키 paste → 기본 모델 선택 → 연결 테스트.
**결과**: *Settings → AI* 아래 AI provider 레코드, 사용 준비 완료.
**다시 실행**: *Settings → AI → + Add provider*.

원하면 skip — AI 어시스턴트 패널이 과거 대화 browse 용으로 여전히 사용 가능. setup 은 언제든 다시.

## 첫 실행 onboarding (두 빌드 모두)

**등장**: 앱의 아주 첫 실행.
**질문**: 어떤 역할이 본인을 가장 잘 표현 (작가 / 엔지니어 / 리서처 / PM / 변호사 / 디자이너 / 교육자 / 데이터 분석가 / 컨설턴트 + "skip" 옵션).
**결과**: HTMLook 이 어울리는 튜토리얼 하나 제안하고 그 샘플 워크스페이스 unlock.
**다시 실행**: *Help → 첫 실행 onboarding 다시 보기*.

역할은 추천 소스일 뿐 — 그것 뒤에 잠긴 건 없음. 선택과 무관하게 어떤 튜토리얼이든 가능.

## 새 워크스페이스 위자드 (Pro · ⌘⇧N)

**등장**: ⌘⇧N, 또는 *File → New → Workspace Wizard…*.
**질문**: 시작점 선택 — *빈 폴더* · *템플릿에서* · *Profile pack 에서* · *URL 에서 clone*. 그 다음 이름 + 위치.
**결과**: 새 워크스페이스 폴더, 선택한 템플릿 파일이 seed 됨.
**팁**: Profile pack 은 특정 역할 위한 사전 구축 워크스페이스 (예: "컨설턴트 — 클라이언트 피치 덱"), 적합한 확장 활성화 + 샘플 파일 포함.

## 템플릿에서 새로 (⌘⇧T)

**등장**: ⌘⇧T, 또는 *File → New → From Template…*.
**질문**: 템플릿 선택 — Markdown article, Slide outline, Meeting note, Research one-pager, 빈 HTML 등.
**결과**: 현재 워크스페이스에 새 파일, 탭으로 열림.

## 확장 추가 위자드 (Pro)

**등장**: *Settings → Tools → + Add*.
**질문**: 이름 · 설명 · 버전 · 라이선스 · 무엇을 하는지 (코드블록 언어 렌더러? 새 Export 포맷? AI 헬퍼?) · 레시피 본문.
**결과**: 워크스페이스의 `.claude/skills/` 에 invoke 준비된 Markdown 파일.
**Skip 가능**: 예 — 빌트인 확장만으로 계속 사용 가능.

## Profile 설치 (Pro)

**등장**: *File → New → Install from URL…*.
**질문**: Profile pack URL paste (또는 큐레이션 목록에서).
**결과**: HTMLook 이 pack 을 새 워크스페이스 폴더로 다운, 그 확장 활성화.
**위치**: Profile 카탈로그, *File → Browse profiles…* 에서 browse.

## 의존성 설치 (외부 도구 사용 시)

**등장**: 외부 도구가 필요한 기능 호출 시 (예: *Export → PowerPoint* 가 LibreOffice 필요) 그 도구 미설치 상태.
**질문**: 설치 명령 표시 (`brew install --cask libreoffice`) + **지금 설치** / **명령어 복사** / **닫기**.
**결과**: 설치 로그가 모달에 라이브 stream; 성공 시 원래 기능 실행.
**다시 실행**: *Settings → Tools → 미설치 도구 옆의 흐린 ring 클릭*.

## 앱 관리 권한 (macOS Sequoia 이상)

**등장**: 자동 업데이트가 번들 교체 시도 시 macOS 가 차단할 때.
**질문**: *System Settings 열기* 클릭 → System Settings 의 올바른 패널로 바로 이동.
**결과**: 토글 켠 후 *Retry* 클릭 → 업데이트 진행.

## Save as preset (터미널)

**등장**: 터미널 preset 툴바의 책갈피 아이콘 클릭 시.
**질문**: 방금 쓴 프롬프트의 이름 + (선택) 설명.
**결과**: preset 툴바에 새 "+ <이름>" 버튼 — 한 클릭에 그 프롬프트를 활성 터미널로 paste.

## 왜 이렇게 많아?

HTMLook 의 원칙: 컨텍스트를 가정하지 않음. 값이 필요한 모든 상태 (API 키 · provider · 대상 폴더 · 미설치 의존성) 가 각자의 짧은 위자드를 가지고, 평이한 표현으로, *Skip* 옵션과 함께. trade-off: 초반에 다이얼로그를 더 많이 만남 — 그러나 첫 주 이후로는 거의 만나지 않음.

## 다음

- [튜토리얼 →](Tutorials-ko.md)
- [Settings →](Settings-ko.md)
