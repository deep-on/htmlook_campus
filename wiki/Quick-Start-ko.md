# 빠른 시작

> "HTMLook 방금 열었어" 에서 "이걸로 일할 수 있어" 까지 5분.

이 워크스루는 HTMLook Pro 가 이미 설치되어 ([설치](Installation-ko.md)) 앱이 열려 있다고 가정합니다.

## 1. 워크스페이스 고르기 (30초)

첫 실행에 HTMLook 이 폴더 가리키기 요청. 무엇이든 OK — `~/Notes`, 클라이언트 폴더, 빈 `~/Desktop/scratch`. 그 폴더가 곧 워크스페이스. (나중에 더 추가 가능, 각 워크스페이스는 독립.)

큐레이션된 예시로 시작하고 싶으면 **샘플 워크스페이스 열기** 선택 — HTMLook 이 예시 파일 몇 개와 함께 떨어뜨려 줍니다.

## 2. 파일 열기 (15초)

사이드바 아무거나 단일 클릭 → 중앙에 열림. 더블 클릭 → 새 탭. 렌더러는 파일 타입별 자동 — Markdown 은 WYSIWYG 에디터, PDF 는 PDF.js + 하이라이트, 비디오/오디오 는 북마크 있는 플레이어.

## 3. AI 어시스턴트 (1분 · Pro)

⌘I → 우측 패널 열림. 첫 사용 시 5-카드 setup 이 provider 선택 (OpenAI / DeepSeek / Ollama / …), API 키 paste, 모델 선택까지 안내. 방금 연 파일에 대해 물어보세요:

> *"세 줄로 요약해줘"*

응답이 stream 됨. ⌘. 로 언제든 취소.

## 4. 터미널 열기 (30초 · Pro)

⌘J 로 하단 터미널 패널. "+ Claude" 버튼이 워크스페이스 폴더에서 Claude 가 이미 실행 중인 탭을 엽니다. 질문 타이핑하면 Claude 가 파일들을 보고 작업 가능. "+ Codex" 와 "+ Gemini" 도 해당 CLI 설치되어 있으면 동일.

## 5. 보이는 것 마킹 (45초)

⌘⌥P 로 Paint 토글. 논의하고 싶은 것에 동그라미 → AI 어시스턴트의 📎 클릭 → 다음 메시지에 스케치 첨부 → "이 레이아웃 뭐가 잘못됐어?" 물어봄. 스크린샷이 대화에 실림.

## 6. 음성 메모 녹음 (30초 · Pro)

상태바 우측 하단의 마이크 아이콘 → 클릭 → 말함 → 다시 클릭. 녹음이 워크스페이스의 `.m4a` 로 저장. 화면 하단의 Voice Player 가 재생. transcript 원하면 AI 어시스턴트에게 부탁 ("이 메모 transcribe 해줘").

## 7. 결과 export (30초)

⌘E 로 Export 메뉴. 인쇄용 PDF, 다른 도구로 넘길 Markdown, 다듬은 Markdown (Smart), 단일 파일 발송용 HTML — 각각 마지막 저장 위치 기억.

## 끝

여기까지가 일상 사용의 ~80%. 더 깊이는 세부 페이지:

- [마크다운 에디터](Viewer-ko.md) — autocorrect · 코드블록 언어 picker · paste sanitizer
- [터미널](Terminal-ko.md) — pane split · "save as preset" · 한글 IME 메모
- [Paint](Paint-ko.md) — 도구 전체 + 첨부 흐름
- [음성 메모](Voice-Memos-ko.md) — 재생 · transcript · 메모 전체 검색
- [확장 (Extensions)](Skills-ko.md) — 빌트인 + 직접 추가
- [튜토리얼](Tutorials-ko.md) — 특정 워크플로우 in-app 가이드 워크스루
- [위자드](Wizards-ko.md) — 진행 중 만날 setup 마법사들

## 다음

- [UI 한눈에 보기 →](UI-Overview-ko.md)
- [튜토리얼 →](Tutorials-ko.md)
