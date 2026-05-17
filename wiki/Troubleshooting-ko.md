# Troubleshooting

> 자주 보이는 이슈의 빠른 해결. 여기 없으면 `/tmp/htmlook-debug.log` 첨부해서 티켓.

## 앱이 안 켜져요

**증상**: 아이콘 클릭해도 반응 없음 또는 즉시 종료.

- `/tmp/htmlook-debug.log` 의 마지막 run 확인
- 번들이 stapled 인지 — `xcrun stapler validate "/Applications/HTMLook Pro.app"` 가 *worked* 출력해야
- macOS Sequoia: System Settings → 개인 정보 보호 및 보안 → 앱 관리 → HTMLook Pro 토글
- 최악의 경우 설정 완전 리셋: `rm -rf "~/Library/Application Support/com.deep-on.htmlook-pro/"` — 워크스페이스는 영향 없음

## 자동 업데이트 알림이 안 떠요

- v1.0.7 이하는 자동 업데이트 불가 (private repo 이슈 + 하드코딩된 버전). `htmlook.app/download/pro-mac` 에서 v1.0.9 직접 다운로드
- v1.0.8+ : `https://htmlook-releases.kdk3606.workers.dev/pro/latest.json` 접근 가능한지 확인
- macOS 15 Sequoia 이상은 *앱 관리* 권한도 필요

## "FFmpeg / LibreOffice / Quarto 미설치" toast

*지금 설치* 클릭 — HTMLook 이 Homebrew 로 설치를 streaming 로그 모달로 진행. Homebrew 자체가 없으면 모달이 그것부터 설치.

brew install 이 영원히 hang: cask 패키지의 sudo timestamp 이슈일 가능성 높음. cask (LibreOffice · Quarto) 는 일반 brew 대신 macOS pkg installer + osascript admin prompt 사용.

## 한글 IME doubling

터미널에서 `ㄷㅏ` 가 `다` 대신 보이면 `IME_DEBUG=true` 녹화 (Settings → Terminal → IME debug enable) 후 로그 첨부 issue. v1.0.9 가 KoreanComposer state machine 으로 이 부류 fix. 회귀는 새 edge case 의미.

## 음성 미터가 0 / 무음 녹음

M3+ MacBook Pro 의 lid 닫음 (클램쉘) 시 **내부 마이크 디지털 무음** — 알려진 macOS 버그. lid 열거나 외부 마이크. HTMLook 이 1회 경고 toast.

## 터미널 닫고 CPU 100% 발생

증상: 모든 터미널 탭 닫은 후 `login -pf` orphan 프로세스가 CPU 잡음. 원인: Tauri dev rebuild + 터미널 패널 interaction. v1.0.8+ 가 탭 close 시 orphan reap 패치. v1.0.9+ 에서 보이면 `ps aux | grep login` 출력 첨부 issue.

## iframe 렌더 HTML 이 상대 CSS / JS 못 불러옴

뷰어가 `srcdoc` 에 상대 asset 을 인라인 — WKWebView 의 base-URL 처리가 그것들을 못 풀기 때문. 브라우저에선 정상이지만 HTMLook 에선 빈 페이지면 HTML 받아 파일 디렉토리에서 리소스 접근 가능 여부 확인. 최소 repro 로 issue.

## 멀티 윈도우: 한쪽 변경이 다른 쪽에 반영 안 됨

두 윈도우 모두 파일시스템 watch. 파일 watcher debounce ~300 ms. 지속적 stale:

- stale 윈도우 클릭 → focus 이벤트 강제 → 활성 탭 re-sync
- 종료 후 재시작 (워크스페이스 복원)
- 파일시스템 corner case: 워크스페이스가 네트워크 마운트면 SMB / NFS 가 FSEvents 항상 fire 하지 않음

## ChatPanel "no response"

- *Settings → AI · BYOM → 권한* — provider 가 요청 거부했을 수 있음
- BYOM provider 의 상태 페이지 확인. HTMLook 이 상류 에러를 평문으로 표시
- ⌘. 로 스트리밍 응답 취소 가능 — resume 안 되면 provider 측에서 실제 취소된 것

## 이슈 제보 위치

pre-launch 단계라 repo 가 private: maintainer (`kdk3606@deep-on.com`) 로 `/tmp/htmlook-debug.log` + 상황 설명 메일.

## 다음

- [Settings →](Settings-ko.md)
- [Home](Home-ko.md) 로
