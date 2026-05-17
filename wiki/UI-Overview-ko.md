# UI 한눈에 보기

> 다이어그램 하나에 모든 영역 명명. 북마크 추천.

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⎙  ▼ workspace          file.md            ●  HTMLook Pro    🪟 ⊟ ⨯ │ ← Title bar
├──┬──────────────┬────────────────────────────────┬──────────────────┤
│A │  Sidebar     │  Tabs strip · ⌘1..9             │  ChatPanel       │
│c │              │ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │   (⌘L 토글)     │
│t │   filter…    │                                 │                  │
│i │   ▾ docs/    │      Viewer                     │   시스템 프롬프트│
│v │     • intro.md│                                │   • Skill chip   │
│i │     • plan.md│      (Markdown / HTML / PDF /   │                  │
│t │   ▾ images/  │       이미지 / 비디오 / 오디오/ │   ▸ "요약해줘…" │
│y │     • hero.png│      DOCX / PPTX / 코드)       │   ▸ tool call    │
│B │              │                                 │   ▸ 응답 …       │
│a │              │                                 │                  │
│r │              │                                 │                  │
├──┴──────────────┴────────────────────────────────┴──────────────────┤
│  Terminal panel  (Cmd+`)  ⠿ + Claude + Codex + Gemini + Shell   ⊟  │ ← dock 가능
│  ─ tab 1 ─ tab 2 ─ tab 3 ─                                          │
│  $                                                                  │
├──────────────────────────────────────────────────────────────────────┤
│  ▣ 12 files · 1 modified ●   ⏺ rec 00:12   ▾ Easier mode      🟢 OK│ ← 상태바
└──────────────────────────────────────────────────────────────────────┘
```

## 여섯 개 영역

### 1. Activity Bar (좌측 끝 32 px)
빠른 토글: 파일 리스트 표시 · 뷰어 / 듀얼 / 코드 모드 · paint · present · 터미널 dock 위치 순환. 호버하면 단축키 툴팁.

### 2. Sidebar
현재 워크스페이스의 파일 트리 + 필터 입력 + Finder 로 drag-out (`.html`) · 다중 선택 (⌘+클릭 / ⇧+클릭) · 컨텍스트 메뉴 (이름변경 · 복제 · Finder 표시 · 터미널에서 열기 · N 개 삭제). 상단 드롭다운으로 최근 열어본 워크스페이스 전환.

→ 상세: [사이드바](Sidebar-ko.md)

### 3. Tabs strip
연 파일이 탭. ⌘1..9 점프. Cmd+W 닫기. 수정 시 ● 점. 우클릭으로 *Pin* · *다른 탭 닫기* · *Reveal* · *경로 복사*. 터미널 탭 제목은 brand letter mark (Cl/Cx/Gm/Sh).

### 4. Viewer (중앙, 가장 큰 영역)
활성 탭을 렌더. 렌더러가 확장자에 따라 자동 전환:

- `.md` → WYSIWYG Markdown 에디터. autocorrect · ⌘K 링크 다이얼로그 · ⌘B/I/U 인라인 포맷 · 코드블록 언어 picker · 이미지 popover (alt + 정렬)
- `.html` → iframe sandbox + 상대경로 asset 인라인
- `.pdf` → PDF.js + text-layer + 하이라이트 도구
- 비디오 / 오디오 → 자체 플레이어 + 북마크 + transcript
- 그 외 → 예쁜 렌더 또는 syntax-highlighted 코드

Dual-view (⌘⇧D) 로 좌우 분할. Present mode (⌘⌥P) 로 chrome 숨김.

→ 상세: [뷰어](Viewer-ko.md)

### 5. Terminal panel
Bottom / right / left / center 어디든 dock. 각 탭이 진짜 PTY (기본 zsh) + 선택적 preset (Claude / Codex / Gemini / Shell). 한글 IME 정상 동작 (KoreanComposer state machine). Cmd+\` 표시 토글. Cmd+T 새 탭. Cmd+D / Cmd+⇧D 로 pane split.

→ 상세: [터미널](Terminal-ko.md)

### 6. ChatPanel
Bring-Your-Own-Model AI 채팅. ⌘L 토글. MCP + skill 매니페스트에서 tool 자동 로드. 첫 tool call 시 워크스페이스마다 4-버튼 consent 모달.

→ 상세: [ChatPanel · BYOM](ChatPanel-BYOM-ko.md)

## 레이어 형 surface

- **Find bar**: 뷰어 안 ⌘F. ⌘G 다음 매치.
- **Paint canvas**: ⌘⇧P 토글. 펜 / 도형 / 화살표 / 텍스트, undo 50 step, PNG export.
- **Voice player**: `.m4a` 선택 시 하단 등장. 다중 메모 navi · transcript · waveform.
- **Region selector**: Cmd+⌥+R 로 화면 영역 캡처 → 클립보드 / Paint / AI.
- **Update notifier**: 새 빌드 manifest 발견 시 우상단.

## 보기 모드

| 모드 | 단축키 | 동작 |
|---|---|---|
| Single | ⌘1 | 기본 — 단일 뷰어 |
| Dual | ⌘⇧D | 좌우 분할 + sync-scroll 토글 |
| Code | (Easier) ⌘⌥E (Pro) ⌘E | 원본 소스 옆에 렌더 |
| Paint | ⌘⇧P | 뷰어 위에 스케치 |
| Present | ⌘⌥P | chrome 숨기고 풀스크린 |

## [Settings](Settings-ko.md) 에서 조정

테마 · 폰트 · 터미널 preset 명령 · BYOM provider/key · 자동저장 delay · 업데이트 채널 · 사이드바 collapse 기본값 · 언어별 코드 기본 · 뷰어 툴바 표시.

## 다음

- [탭과 보기 모드 →](Tabs-and-Views-ko.md)
- [사이드바 →](Sidebar-ko.md)
