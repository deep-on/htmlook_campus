# 워크스페이스

> HTMLook Pro 가 가리키는 모든 폴더가 곧 워크스페이스. 데이터베이스도, 프로젝트 파일도, "import" 단계도 없습니다.

## 폴더 = 프로젝트

`~/Notes` 든, 회사 클라이언트 폴더든, 비어있는 `~/Desktop/scratch` 든 — 그게 워크스페이스입니다. HTMLook Pro 는 그 안의 파일들을 읽고, 인식 가능한 타입별 탭을 띄우고, 생성하는 모든 결과물도 *같은 폴더 안* 의 평범한 파일로 저장합니다. 폴더 옮기면 워크스페이스도 같이 이동. Dropbox · git · USB 로 보내면 그대로 따라갑니다.

여러 워크스페이스를 동시에 열 수 있고, 각각이 자체 설정 / AI 권한 / 도구 감지 결과를 갖습니다.

## HTMLook 이 읽는 파일 타입

| 카테고리 | 확장자 |
|---|---|
| 웹 · 구조화 | `.html`, `.htm`, `.svg`, `.json`, `.csv`, `.tsv` |
| Markdown 계열 | `.md`, `.markdown`, `.mdx`, `.qmd` |
| Office (LibreOffice / Quarto 로 read-only 렌더) | `.docx`, `.pptx`, `.xlsx` |
| PDF | `.pdf` |
| 이미지 | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.heic` |
| 비디오 | `.mp4`, `.mov`, `.webm` |
| 오디오 | `.m4a`, `.mp3`, `.wav`, `.aac` |
| 다이어그램 (skill 통해) | `.mmd` (Mermaid), `.d2` |
| 소스 코드 (code 로 렌더) | 주요 언어들 |

그 외는 hex / text fallback.

## 사이드카 폴더 (dot-prefix 형제들)

HTMLook 이 생성하는 내용은 파일 옆 dot-prefix 폴더에 보관합니다. *내 것* 이라 git 에 넣든 `.gitignore` 하든 자유.

| 사이드카 | 보관 내용 |
|---|---|
| `.htmlook/` | 앱 관리: `tools.json` · `chat-history/` · `sketches/` · `agent-messages.jsonl` · `audit-log.jsonl` · paste 자산 · view-state 스냅샷 |
| `.htmlook-voice/` | 음성 메모 (AAC `.m4a`) + 짝맞는 `*.transcript.json` |
| `.claude/skills/` | 워크스페이스 한정 skill. BYOM ChatPanel 과 AI 도구 카탈로그에 자동 로드 |
| `.agents/skills/` | Codex · Gemini · Aider 호환 cross-tool skill |

글로벌 `~/.claude/skills/` (와 `~/.agents/skills/`) 가 그 아래 레이어. 충돌 시 워크스페이스가 이깁니다.

## Companion 파일 (파일 바로 옆)

특정 파일은 사이드카 대신 *형제 파일* 로 떨어집니다 — Finder 에서 관계가 명확히 보이고 `mv` 에도 살아남도록.

| 형제 패턴 | 소유 기능 |
|---|---|
| `foo.mp4.segments.json` | 오디오/비디오 segment marker |
| `foo.mp4.chapters.json` | 비디오 챕터 |
| `foo.mp4.bookmarks.json` | 리뷰 마커 / 스크럽 북마크 |
| `foo.pdf.highlights.json` | PDF 하이라이트 + 코멘트 |
| `foo.m4a.transcript.json` | 음성 메모 transcript |
| `foo.html.draft.md` | Markdown round-trip 초안 |

## 멀티 윈도우 · 멀티 워크스페이스

`File → New Window` (⌘N) 으로 독립 두 번째 윈도우. 각 윈도우는 하나의 워크스페이스 root 에 고정, 자체 탭 목록 / 터미널 패널 / ChatPanel. 두 윈도우가 같은 워크스페이스를 봐도 충돌 없음 — 파일 watcher 가 변경 전파, 사이드카는 append-only.

## HyperFrames (워크스페이스 내 가벼운 cross-file 링크)

워크스페이스 안 파일끼리 `htmlook://` 링크로 참조 가능: `[Q3 회귀 결과](htmlook://regression-results.html#sec-q3)` 클릭하면 같은 윈도우에서 그 파일 + anchor 까지. 페르소나 영상 13편의 멀티렌즈 워크플로우가 이 위에서 동작합니다.

## 클라우드로 나가는 것

기본적으로 없음. 텔레메트리 없음, 워크스페이스 업로드 없음. 기본 install 의 outbound 트래픽은:

- 자동 업데이트 check (`htmlook-releases.kdk3606.workers.dev/pro/latest.json`)
- 직접 설정한 BYOM provider (OpenAI · DeepSeek 등) — ChatPanel 사용 시에만

BYOM setup + 자동 업데이트 둘 다 끄면 완전 오프라인 동작 가능.

## 다음

- [UI 한눈에 보기 →](UI-Overview-ko.md)
- [Pro vs Easier 차이점 →](Pro-vs-Easier-ko.md)
