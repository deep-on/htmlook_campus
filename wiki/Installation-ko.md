# 설치

> macOS Apple Silicon · 5분 · 회원가입 없음.

## 1. 요구사항

- macOS 12 (Monterey) 이상
- Apple Silicon (M1 / M2 / M3 / M4)
- 디스크 ~200 MB
- Intel Mac 빌드는 로드맵 (v1.0.x). 현재 Apple-Silicon 빌드가 Rosetta 로 동작은 하지만 일상 사용 권장하지 않습니다

## 2. 다운로드

직링크: **<https://htmlook.app/download/pro-mac>**

위 링크가 R2 의 최신 서명/노타리 완료 DMG 로 302 redirect 합니다. 용량 ~11 MB.

## 3. 첫 실행

1. DMG 를 엽니다.
2. **HTMLook Pro.app** 을 `Applications` 단축 아이콘으로 드래그합니다. 기존 HTMLook Pro 가 있으면 Finder 가 *교체* 를 묻습니다 — 수락하세요. 데이터는 워크스페이스 폴더에 있지 .app 안에 없습니다.
3. Applications 폴더 (또는 Spotlight) 에서 실행. 첫 실행 시 *"HTMLook Pro" 는 인터넷에서 다운로드되었습니다* 메시지가 뜰 수 있어요 — **열기**. Deep-On Inc. (F4GL4XC335) 서명 + Apple 노타리 완료 빌드입니다.

> 빌드 검증 (`spctl --assess -vv`):
> ```
> source=Notarized Developer ID
> origin=Developer ID Application: Deep-On Inc. (F4GL4XC335)
> ```

## 4. 표시될 수 있는 권한 요청

권한은 게으르게 요청합니다 — 해당 기능이 처음 필요할 때만.

| 권한 | 발생 시점 | 이유 |
|---|---|---|
| **마이크** | 첫 음성 메모 녹음 | `.htmlook-voice/*.m4a` AAC 녹음. 시스템 prompt 아래 부연: 녹음은 로컬에만 저장. |
| **파일 및 폴더** | 일반 dir 바깥의 워크스페이스 오픈 | macOS 가 앱별 + 폴더별 권한 분리. *허용* 선택. |
| **앱 관리** | 자동 업데이트가 번들 교체 시도 | macOS Sequoia 이상. System Settings → 개인 정보 보호 및 보안 → 앱 관리 에서 HTMLook Pro 토글. 앱 내에서도 안내 toast. |

이 권한들은 추후 System Settings 에서 해제 가능. 앱은 degrade 됩니다.

## 5. 자동 업데이트

HTMLook Pro **v1.0.8 이상**은 launch 마다 <https://htmlook-releases.kdk3606.workers.dev/pro/latest.json> 매니페스트를 확인합니다. 서명된 신버전이 발견되면 우상단에 업데이트 글리프 등장 → 클릭 → 다운로드 → 재시작. 워크스페이스 / 설정 / sidecar 는 손대지 않습니다.

> **v1.0.7 이하**는 자동 업데이트 불가 — 빌드 시점에 (지금은 private 으로 잠긴) GitHub Releases 엔드포인트로 묶여 있어요. 위 다운로드 링크로 v1.0.9 DMG 직접 받아서 `/Applications` 에 drag-and-drop 하시면 Finder 가 자동 교체.

## 6. HTMLook Pro 가 다룰 수 있는 (선택) 외부 도구

앱 실행 자체엔 불필요. 쓸 기능만 골라서 설치:

- `ffmpeg` → 비디오 씬 감지, 비디오 챕터 미리보기 — `brew install ffmpeg`
- `soffice` (LibreOffice) → DOCX/PPTX → PDF — `brew install --cask libreoffice`
- `quarto` → `.qmd` 렌더 — `brew install --cask quarto`
- `pandoc` → 더 풍부한 Markdown export — `brew install pandoc`
- 에이전트 CLI (`claude` · `codex` · `gemini`) → 터미널 안에서 페어 AI 로 실행, 벤더 문서 따라 설치

의존성 없는 상태로 기능을 호출하면 HTMLook 이 *친절한 toast* 로 설치 명령 + **지금 설치** 원클릭 버튼을 띄웁니다.

## 다음

- [워크스페이스 →](Workspace-ko.md)
- [UI 한눈에 보기 →](UI-Overview-ko.md)
