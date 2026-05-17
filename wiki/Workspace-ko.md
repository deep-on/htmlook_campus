# 워크스페이스

> HTMLook Pro 가 가리키는 모든 폴더가 곧 워크스페이스. 데이터베이스도, 프로젝트 파일도, "import" 단계도 없습니다.

## 폴더 = 프로젝트

`~/Notes` 든, 회사 클라이언트 폴더든, 비어있는 `~/Desktop/scratch` 든 — 그게 워크스페이스입니다. HTMLook Pro 가 그 안을 읽고, 인식 가능한 타입별 탭을 띄우고, 생성하는 모든 결과물도 *같은 폴더 안* 의 평범한 파일로 저장. 폴더 옮기면 워크스페이스 같이 이동. Dropbox · git · USB 로 보내면 그대로 따라감.

여러 워크스페이스 동시 가능, 각각 자체 설정 + 도구 감지 결과.

## HTMLook 이 읽는 파일 타입

| 카테고리 | 확장자 |
|---|---|
| 웹 · 구조화 | `.html`, `.htm`, `.svg`, `.json`, `.csv`, `.tsv` |
| Markdown 계열 | `.md`, `.markdown`, `.mdx`, `.qmd` |
| Office (read-only 렌더) | `.docx`, `.pptx`, `.xlsx` (LibreOffice / Quarto 설치 필요) |
| PDF | `.pdf` |
| 이미지 | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.heic` |
| 비디오 | `.mp4`, `.mov`, `.webm` |
| 오디오 | `.m4a`, `.mp3`, `.wav`, `.aac` |
| 다이어그램 (확장 통해) | `.mmd` (Mermaid), `.d2` |
| 소스 코드 (code 로 렌더) | 주요 언어들 |

그 외는 hex / text fallback.

## HTMLook 이 파일 옆에 보관하는 것

HTMLook 이 생성하는 모든 것은 워크스페이스 안 평범한 파일로 — 보고 · 버전 관리 · `.gitignore` 모두 본인 자유.

| 경로 | 보관 내용 |
|---|---|
| `.htmlook/` | 앱 관리: 그린 스케치 · 채팅 히스토리 · 설정 · paste 자산 |
| `.htmlook-voice/` | 음성 메모 (`.m4a`) + 선택적 transcript 형제 |

특정 파일은 사이드카 대신 *형제 파일* 로 떨어집니다 — Finder 에서 관계가 명확하고 `mv` 에도 살아남도록.

| 형제 패턴 | 저장 내용 |
|---|---|
| `foo.m4a.transcript.json` | 음성 메모 transcript |
| `foo.pdf.highlights.json` | PDF 하이라이트 + 코멘트 |
| `foo.mp4.chapters.json` | 비디오 챕터 |
| `foo.mp4.bookmarks.json` | 비디오 스크럽 북마크 |

## 멀티 윈도우 · 멀티 워크스페이스

*File → New Window* (Pro 에선 ⌘⌥⇧N) 로 독립 두 번째 윈도우. 각 윈도우는 하나의 워크스페이스 root 에 고정, 자체 탭 / 터미널 / AI 어시스턴트. 두 윈도우가 같은 워크스페이스를 봐도 충돌 없음 — 파일 변경 전파.

## 워크스페이스 내 cross-file 링크 (HyperFrames)

워크스페이스 안 파일끼리 참조 가능. 어느 파일에서든 `htmlook://` 링크 클릭 (`[Q3 결과](htmlook://results.html#sec-q3)`) → 같은 윈도우에서 그 파일 + anchor 까지. 리포트 + raw 데이터 + 차트를 하나의 navigable 흐름으로 엮기에 유용.

## 클라우드로 나가는 것

기본은 없음. 텔레메트리 없음, 워크스페이스 업로드 없음. 기본 install 의 outbound 트래픽은:

- launch 시 자동 업데이트 check
- 직접 설정한 AI provider (OpenAI · DeepSeek 등) — AI 어시스턴트 사용 시에만

AI provider setup 스킵하면 완전 오프라인 동작.

## 다음

- [UI 한눈에 보기 →](UI-Overview-ko.md)
- [빠른 시작 →](Quick-Start-ko.md)
