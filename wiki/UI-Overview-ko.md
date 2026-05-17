# UI 한눈에 보기

> 한 레이아웃에 모든 영역 명명. 북마크 추천.

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⎙  ▼ workspace          file.md            ●  HTMLook Pro    🪟 ⊟ ⨯ │ ← Title bar
├──┬──────────────┬────────────────────────────────┬──────────────────┤
│A │  Sidebar     │  Tabs strip                     │  AI 어시스턴트   │
│c │              │ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │   (⌘I 토글)     │
│t │   filter…    │                                 │                  │
│i │   ▾ docs/    │      Viewer                     │   대화           │
│v │     • intro.md│                                │                  │
│i │     • plan.md│      (Markdown / HTML / PDF /   │                  │
│t │   ▾ images/  │       이미지 / 비디오 / 오디오/ │   ▸ "요약해줘…" │
│y │     • hero.png│      DOCX / PPTX / 코드)       │   ▸ 응답 …       │
│B │              │                                 │                  │
│a │              │                                 │                  │
│r │              │                                 │                  │
├──┴──────────────┴────────────────────────────────┴──────────────────┤
│  Terminal panel  (⌘J)  ⠿ + Claude + Codex + Gemini + Shell      ⊟  │ ← dock 가능
│  ─ tab 1 ─ tab 2 ─ tab 3 ─                                          │
│  $                                                                  │
├──────────────────────────────────────────────────────────────────────┤
│  ▣ 12 files · 1 modified ●   ⏺ rec 00:12   ▾ Easier mode      🟢 OK│ ← 상태바
└──────────────────────────────────────────────────────────────────────┘
```

## 여섯 개 영역

### 1. Activity Bar (좌측 끝 32 px)
빠른 토글: 파일 리스트 표시 · 보기 모드 (preview / source / split / gallery) · Paint · Present · 터미널 dock 위치 순환. 호버하면 단축키 툴팁.

### 2. Sidebar
현재 워크스페이스의 파일 트리 + 필터 입력 + Finder/Mail/Slack 로 drag-out · 다중 선택 (⌘+클릭 / ⇧+클릭) · 컨텍스트 메뉴 (이름변경 · 복제 · Finder 표시 · 터미널에서 열기 · N 개 삭제). 상단 드롭다운으로 최근 열어본 워크스페이스 전환.

→ 상세: [사이드바](Sidebar-ko.md)

### 3. Tabs strip
연 파일이 탭. ⌘⌥1..9 점프. ⌘W 닫기. 수정 시 ● 점. 우클릭으로 *Pin* · *다른 탭 닫기* · *Finder 표시* · *경로 복사*. 터미널 탭은 brand letter mark (Cl/Cx/Gm/Sh).

### 4. Viewer (중앙, 가장 큰 영역)
활성 탭을 렌더. 렌더러가 확장자에 따라 자동 전환:

- `.md` → WYSIWYG Markdown 에디터. autocorrect · ⌘K 링크 다이얼로그 · ⌘B/I/U 인라인 포맷 · 코드블록 언어 picker · 이미지 popover (alt + 정렬)
- `.html` → iframe sandbox + 상대경로 asset 인라인
- `.pdf` → PDF.js + text-layer + 하이라이트 도구
- 비디오 / 오디오 → 자체 플레이어 + 북마크 + transcript
- 그 외 → 예쁜 렌더 또는 syntax-highlighted 코드

Dual-view (split = ⌘3) 로 두 파일 좌우 분할. Present 모드로 chrome 숨김.

→ 상세: [뷰어 · 마크다운 에디터](Viewer-ko.md)

### 5. Terminal panel
Bottom / right / left / center 어디든 dock. 각 탭이 진짜 터미널 (기본 zsh) + 선택적 preset (Claude / Codex / Gemini / Shell). ⌘J 표시 토글. ⌘T 새 탭. ⌘D / ⌘⇧D 로 pane split.

→ 상세: [터미널](Terminal-ko.md)

### 6. AI 어시스턴트
Bring-Your-Own-Model 채팅. ⌘I 토글. 어시스턴트가 워크스페이스를 변경하려는 첫 시도에 4-버튼 동의 모달.

→ 상세: [AI 어시스턴트](ChatPanel-BYOM-ko.md)

## 레이어 형 surface

- **Find bar**: 뷰어 안 ⌘F. ⌘G 다음 매치.
- **Paint canvas**: ⌘⌥P 토글. 펜 / 도형 / 화살표 / 텍스트, undo 50 step, PNG export.
- **Voice player**: `.m4a` 선택 시 하단 등장. 다중 메모 navi · transcript · waveform.
- **Update notifier**: 새 빌드 발견 시 우상단.

## 보기 모드

| 모드 | 단축키 | 동작 |
|---|---|---|
| Preview | ⌘1 | 기본 — 렌더된 출력 |
| Source | ⌘2 | 원본 소스 |
| Split | ⌘3 | preview + source 좌우 |
| Gallery | ⌘G | 워크스페이스 파일들의 thumbnail grid |
| Paint | ⌘⌥P | 뷰어 위에 스케치 |
| Present | View 메뉴 | chrome 숨기고 뷰어 풀스크린 |

## [Settings](Settings-ko.md) 에서 조정

테마 · 폰트 · 터미널 preset 명령 · AI provider/key · 기본 정렬 · 언어별 코드 기본 · 뷰어 인쇄 머리/꼬리말.

## 다음

- [탭과 보기 모드 →](Tabs-and-Views-ko.md)
- [사이드바 →](Sidebar-ko.md)
