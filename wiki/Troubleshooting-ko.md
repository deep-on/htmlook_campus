# Troubleshooting

> 자주 보이는 이슈의 빠른 해결. 여기 없으면 최신 `/tmp/htmlook-debug.log` 첨부해서 알려주세요.

## 앱이 안 켜져요

- 앱이 DMG 안이 아니라 `/Applications` 에 있는지 확인
- macOS Sequoia 이상: System Settings → 개인 정보 보호 및 보안 → 앱 관리 → HTMLook Pro 토글
- 최악의 경우: 앱 종료 → `rm -rf "~/Library/Application Support/com.deep-on.htmlook-pro/"` — 워크스페이스는 영향 없음

## 자동 업데이트 알림이 안 떠요

- 앱 종료 후 재시작 — 체크는 launch 시
- macOS Sequoia 이상은 *앱 관리* 권한 필요 (System Settings → 개인 정보 보호 및 보안 → 앱 관리 → HTMLook Pro 토글)
- 매우 오래된 빌드 (v1.0.7 이하) 면 `htmlook.app/download/pro-mac` 에서 최신 직접 다운로드 — 그 빌드들은 자동 업데이트 불가

## "FFmpeg / LibreOffice / Quarto 미설치" toast

**지금 설치** 클릭 — HTMLook 이 Homebrew 로 streaming 로그 모달과 함께 진행. Homebrew 자체가 없으면 모달이 그것부터 설치.

cask 패키지 (LibreOffice · Quarto) 설치가 hang 처럼 보이면: 백그라운드에 macOS 관리자 password prompt 가 떠있을 수 있음 → 권한 부여.

## 한글 IME doubling

터미널에서 `다` 대신 `ㄷㅏ` 가 보이면 IME 디버그 로그 (Settings → Terminal → IME debug enable) 캡쳐해서 알려주세요 — 최근 빌드가 이 부류 fix 했지만 새 edge case 가능.

## 음성 미터가 0 / 무음 녹음

M3 + MacBook Pro 의 lid 닫음 (클램쉘) 시 내부 마이크가 디지털 무음 — 알려진 macOS 버그. lid 열거나 외부 마이크.

## iframe 렌더 HTML 이 상대 CSS / JS 못 불러옴

HTMLook 이 서버 없이 페이지 렌더되도록 상대 asset 을 인라인. 브라우저에선 정상이지만 HTMLook 안에서 빈 페이지면 asset 이 파일 디렉토리에서 접근 불가능할 수 있음. CSS / JS 파일이 `.html` 의 형제 (또는 하위 폴더) 인지 확인.

## 멀티 윈도우: 한쪽 변경이 다른 쪽에 반영 안 됨

두 윈도우 모두 파일시스템 watch. 업데이트는 약간 시간차. 지속적 stale:

- stale 윈도우 클릭 → re-sync 강제
- 종료 후 재시작 (last-session restore 가 탭 복원)
- 네트워크 마운트 (SMB / NFS) 의 워크스페이스는 변경 알림 항상 fire 하지 않음 — 로컬 폴더가 가장 안정

## AI 어시스턴트 "no response"

- *Settings → AI* 확인 — provider 가 요청 거부했거나 usage limit
- ⌘. 로 스트리밍 응답 취소 가능 — resume 안 되면 provider 측에서 실제 취소된 것 (HTMLook 아님)
- 같은 provider 의 다른 모델로 sanity check

## 버그 보고

`support@htmlook.app` 로 최신 `/tmp/htmlook-debug.log` 첨부 + 상황 한 줄 + 열어둔 파일 타입 이메일.

## 다음

- [Settings →](Settings-ko.md)
- [Home](Home-ko.md) 로
