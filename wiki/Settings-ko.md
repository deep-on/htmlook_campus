# Settings

> ⌘, 로 Settings 다이얼로그. 워크스페이스 + 글로벌 키 모두 여기.

## 탭

| 탭 | 내용 |
|---|---|
| **General** | 테마 (system / light / dark), 언어 (auto / en / ko), 업데이트 채널 (stable / staging), 자동저장 delay, telemetry (기본 off + 유지) |
| **Viewer** | 인쇄 머리/꼬리말 토큰, 듀얼뷰 sync-scroll 기본, `.md` 의 code-view 기본, 폰트 family + size, OpenType feature |
| **Terminal** | preset 명령 (Claude / Codex / Gemini / Shell), preset prompt-to-text, 셸 환경, zsh-autosuggestions 설치 버튼, 폰트 family + size, 커서 스타일 |
| **AI · BYOM** | provider별 키 목록, 기본 모델, request timeout, vision 토글, system-prompt 헤더, skill auto-inject limit |
| **Permissions** | 4-버튼 consent 결정. 도구별 / 워크스페이스별 / 글로벌 행 해제 / 편집 |
| **Power tools** | `tools.json` 에디터. tier 배지. 추가 마법사. "detected" 강제 |
| **Sidebar** | 기본 정렬, dot 파일 숨김, 활성 파일 따라가기, 다중 선택 max (기본 200) |
| **Keyboard** | 모든 단축키 ([단축키](Keyboard-Shortcuts-ko.md)) + 재바인드 |
| **Voice** | 마이크 디바이스 override, 샘플레이트, transcript provider 훅 |
| **About** | 빌드 버전, 서명 identity, manifest 엔드포인트, "업데이트 확인" 버튼 |

## 스코프: 워크스페이스 vs 글로벌

대부분 필드에 `W` / `G` 배지로 스코프 표시. 워크스페이스 필드는 빈 값일 때 글로벌로 fallback, 값 설정 시 pin. *Settings → reset to global* 로 워크스페이스 override 해제.

워크스페이스 설정: `<workspace>/.htmlook/settings.json`. 글로벌: `~/Library/Application Support/com.deep-on.htmlook-pro/settings.json`.

## 업데이트 채널

`stable` = `pro/latest.json`. `staging` = `pro/staging/latest.json` — ship 파이프라인이 `publish-update.sh --staging` 시 쓰는 별도 매니페스트. dev 빌드에서 auto-update 인프라 테스트할 때만 staging.

## 앱 관리 권한 (macOS Sequoia+)

업데이터가 번들 교체 불가 감지 시 인앱 모달에 *System Settings 열기* 버튼 → 올바른 패널로. HTMLook Pro 토글 후 *Retry*.

## CLI 도구 자동 설치

Settings → Power tools → *+Add* 가 BYOM tool 마법사. 아래의 *의존성 자동 설치* 가 `brew install <tool>` (또는 `--cask` · `pipx install …` · `npm i -g …`) 을 streaming 로그 모달과 함께 실행하는 consent 흐름. 의존성-missing toast 와 동일 인프라.

## 로그인 vs 계정

Pro 는 로그인 없음. "계정" 개념은 설정한 BYOM provider 만. Easier 는 구독 계정, Pro 는 없음.

## 리셋 / nuke

*About → 설정 리셋* 이 글로벌 설정 파일 클리어 (확인 묻기). 워크스페이스 설정은 영향 없음 — 워크스페이스 옆에.

완전 리셋: 앱 종료 → `rm -rf "~/Library/Application Support/com.deep-on.htmlook-pro/"`. 워크스페이스는 그대로.

## 다음

- [단축키 →](Keyboard-Shortcuts-ko.md)
- [Troubleshooting →](Troubleshooting-ko.md)
