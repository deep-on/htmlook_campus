# Settings

> ⌘, 로 Settings 다이얼로그. 8 섹션, 뒤의 6 개는 Pro 에서만 보임.

## 섹션

| 섹션 | 내용 |
|---|---|
| **General** | 테마 (System / Light / Dark), 시작 시 동작 (마지막 세션 복원 / 빈 상태 시작), 언어 (자동 + 한국어 + English + 그 외), 강조 색상 (Default / Feature Accents / Persona Tones), **Window tabs** 카드 — Tab mode 토글 · Color tabs 토글 · Layout restore 모드 (Exact / Cascade 30 px) · 이름 붙인 레이아웃 저장 / 복원 |
| **Viewer** | 뷰어 테마 (Built-in / Persona Videos / Feature Accents), 폰트 family + 크기, OpenType features, 인쇄 머리/꼬리말 토큰 (`{filename}` `{date}` `{page}` `{pages}`), 듀얼뷰 sync-scroll 기본, `.md` code-view 기본 |
| **Files** | 워크스페이스 기본 설정, 사이드바 follow-active-file 토글, dot 파일 숨김 토글, 기본 정렬, 검색 제외 패턴 |
| **Terminal** (Pro) | preset 명령 (Claude / Codex / Gemini / Shell), Warp 스타일 인라인 suggest 토글, zsh-autosuggestions 설치 버튼, 터미널 폰트 + 크기, 커서 스타일, OSC 7 cwd 처리, **영속화** (off / visual buffer / tmux), **탭 제목에 cwd 표시** 토글, **선택 모드** 단축키 (기본 `⌃⇧K`), tmux mouse 모드 토글 |
| **AI** (Pro) | 4 개 명명 서브섹션: **Model Connection** (BYOM provider — 추가 / 편집 / 제거, 각 provider 가 base URL + key + 기본 모델 + vision 토글 보관), **Capabilities** (provider 별 기능 게이트), **Permissions** (Tool permission defaults: Read / Capture / Navigate / Annotate / Write / Run × Auto / Ask / Block + 도구별 / 워크스페이스별 / 글로벌 ledger 해제 가능), **Usage** (요청 횟수, 누적 token 비용) |
| **Tools** (Pro) | `tools.json` 에디터 — 빌트인 도구 (Mermaid · D2 · Quarto · LibreOffice · …), 커스텀 도구 추가 마법사, tier 배지, Homebrew 로 의존성 설치 |
| **Plans** | 구독 상태 (Easier) / Pro Solo 트라이얼 상태 (Pro), 업그레이드 버튼, 라이선스 키 |
| **About** | 버전, "업데이트 확인" 버튼 (Pro), 시스템 의존성 상태 (LibreOffice 감지 ✓ / 미감지 ●), 라이브러리 크레딧 (pdf.js, LibreOffice for PPTX) |

## 스코프: 워크스페이스 vs 글로벌

일부 설정 — 폰트 크기, 강조 색상, code-view 기본, 터미널 preset 명령, 기본 정렬 — 은 *글로벌* (모든 워크스페이스 적용). 나머지 — 사이드바 표시, 마지막 연 탭, 도구 권한, AI provider 상태 — 는 워크스페이스 스코프, 워크스페이스 안 `.htmlook/` 에 저장.

다이얼로그 안에 각 컨트롤이 어느 스코프인지 표시. 워크스페이스 override 는 비우면 글로벌 값으로 fallback.

## "업데이트 확인"

About → 업데이트 확인 이 지금 즉시 체크 (Pro 는 launch 시 자동). 서명된 신버전 준비 시 *다운로드 & 설치* 버튼 등장. 클릭 → 백그라운드 다운 → 재시작.

macOS Sequoia 이상에서 번들 교체 차단 시 모달이 **System Settings → 개인 정보 보호 및 보안 → 앱 관리** 경로로 안내, 그 패널 여는 버튼 포함.

## CLI 도구 (Pro 전용)

Tools → *+Add* 가 커스텀 도구 마법사. 아래의 *의존성 설치* 가 Homebrew 를 streaming 로그 모달과 함께 실행. 동일 인프라가 `brew install ffmpeg` · `brew install --cask libreoffice` · `brew install --cask quarto` · `brew install pandoc` · `pipx install <pkg>` · `npm i -g <pkg>` 모두 처리. 도구 선택 → *설치* → 로그 봄.

Homebrew 가 없으면 첫 설치가 Homebrew 부터 (~3 분).

## 로그인 vs 계정

Pro 에는 로그인 없음. "계정" 개념은 AI 섹션에서 가리키는 AI provider 만. Easier 는 Plans 에서 관리되는 구독 계정.

## 리셋

About → 리셋 이 확인 후 설정 클리어. 워크스페이스 데이터 (파일 · sidecar · 음성 메모 · 스케치) 는 그대로 — 리셋은 앱 자체의 preference 만 건드림.

## "Saved ✓" 플래시

즉시 저장 settings (토글, 드롭다운, 폰트 사이즈) 가 예전엔 silent — 저장됐는지 알 수 없었음. v1.0.14 가 다이얼로그 헤더에 작은 `Saved ✓` pill 을 추가, 사용자 변경 후 1.5 s 깜빡이고 페이드. 다른 윈도우에서 온 변경 (cross-window sync) 은 필터링 — 멀티 윈도우 setup 이 strobe 되지 않게.

## 다음

- [단축키 →](Keyboard-Shortcuts-ko.md)
- [Troubleshooting →](Troubleshooting-ko.md)
