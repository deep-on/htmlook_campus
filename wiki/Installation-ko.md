# 설치

> macOS Apple Silicon · 5분 · 회원가입 없음.

## 1. 요구사항

- macOS 12 (Monterey) 이상
- Apple Silicon (M1 / M2 / M3 / M4)
- 디스크 ~200 MB
- Windows 빌드: 준비 중. Intel Mac 빌드: 로드맵.

## 2. 다운로드

직링크: **<https://htmlook.app/download/pro-mac>**

용량 ~11 MB. Apple 서명 + 노타리 완료.

## 3. 첫 실행

1. DMG 를 엽니다.
2. **HTMLook Pro.app** 을 `Applications` 단축 아이콘으로 드래그. 기존 HTMLook Pro 가 있으면 Finder 가 *교체* 를 묻습니다 — 수락하세요. 데이터는 워크스페이스 폴더에 있지 .app 안에 없습니다.
3. Applications 폴더 또는 Spotlight 에서 실행. 첫 실행 시 *"HTMLook Pro" 는 인터넷에서 다운로드되었습니다* 메시지가 뜰 수 있어요 — **열기**.

## 4. 표시될 수 있는 권한 요청

권한은 해당 기능이 실제로 필요할 때만 요청.

| 권한 | 발생 시점 | 이유 |
|---|---|---|
| **마이크** | 첫 음성 메모 | 워크스페이스에 녹음. 녹음은 디바이스에 머뭅니다. |
| **파일 및 폴더** | 일반 dir 바깥의 워크스페이스 오픈 | macOS 가 앱별 + 폴더별 권한 분리. *허용* 선택. |
| **앱 관리** | 자동 업데이트가 번들 교체 시도 | macOS Sequoia 이상. System Settings → 개인 정보 보호 및 보안 → 앱 관리 에서 HTMLook Pro 토글. 업데이터가 올바른 패널로 안내. |

이 권한들은 추후 System Settings 에서 해제 가능. 앱은 degrade 됩니다.

## 5. 자동 업데이트

HTMLook Pro 가 launch 시 백그라운드로 업데이트 확인. 새 빌드가 있으면 윈도우 우상단에 업데이트 글리프. 클릭 → 다운로드 → 재시작. 워크스페이스 · 설정 · 노트는 손대지 않습니다.

## 6. HTMLook Pro 가 다룰 수 있는 (선택) 외부 도구

앱 실행에 필수 아님. 쓸 기능만 골라서 설치:

- `ffmpeg` → 비디오 씬 감지, 챕터 미리보기
- `LibreOffice` → DOCX / PPTX 렌더 + 변환
- `Quarto` → `.qmd` 렌더
- `Pandoc` → 더 풍부한 Markdown export
- 에이전트 CLI (`claude` · `codex` · `gemini`) → 터미널 안에서 페어 AI

미설치 상태로 기능 호출 시 HTMLook 이 **지금 설치** 버튼이 있는 친화 toast 표시 — 원클릭으로 진행 모달과 함께 설치.

## 다음

- [빠른 시작 →](Quick-Start-ko.md)
- [워크스페이스 →](Workspace-ko.md)
- [UI 한눈에 보기 →](UI-Overview-ko.md)
