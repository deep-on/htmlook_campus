# v1.0.14 에 들어온 것

릴리스: **2026-05-24** · 다운로드: [htmlook.app](https://htmlook.app)

> 다른 언어: [English](Whats-New-v1.0.14.md)

이 페이지는 사용자 관점의 변경 요약입니다. 다음 실행 때 무엇이 달라졌는지
확인하는 용도.

---

## 한눈에

- **멀티 윈도우 탭 모드** — 모든 Pro 윈도우가 한 사각형으로 정렬되고 그 위에 Chrome 스타일 탭 strip. 드래그로 순서 변경, 워크스페이스별 색상 표시, 이름 붙인 레이아웃 저장.
- **AI 허가창이 영어로 읽힌다** — 권한 모달이 JSON 덤프 대신 *"AI 가 하려는 것: foo.md 수정 · 되돌리기: ⌘Z"* 로 표시. 6 개 카테고리 (Read / Capture / Navigate / Annotate / Write / Run) 기본값이 안전한 read 호출은 묻지 않고 통과.
- **앱을 닫아도 살아있는 터미널** — tmux 영속화를 켜면 앱을 닫았다가 다시 열어도 터미널 세션이 같은 scrollback 으로 reattach. ⌘F 버퍼 내 검색, pane 간 입력 sync, pane 을 새 윈도우로 detach, 키보드 선택 모드 ⌃⇧K 추가.
- **마크다운 WYSIWYG 안전망** — 라이브 마크다운 편집을 실제 워크스페이스 문서에 써도 안전. 한/영 실제 문서 라이브러리로 round-trip 안정성 검증 완료.
- **한글 파일명 폴리시** — 워크스페이스 claim, Recent 목록, sidecar, 탭 dedup, 터미널 cwd 추적, IME composition 모두 한글 폴더에서도 다른 path 와 동일하게 동작.
- **Sidecar 이동** — PDF annotation, 비디오 bookmark, 비디오 clip, 오디오 segment, chapter 가 워크스페이스 root 가 아닌 `.htmlook/<category>/` 하위로.

---

## 멀티 윈도우 탭 모드

Settings → General → **Window tabs → Tab mode**.

Tab mode 가 켜져 있으면 열린 모든 Pro 윈도우가 포커스된 윈도우의 사각형으로
정렬됩니다. 그 후로 드래그, 리사이즈, +Add 가 peer 들에게 전파 — 따라옵니다.

- **탭 strip 이 툴바 위에 위치.** 각 탭이 워크스페이스 1 개.
- **탭 드래그**로 순서 변경. Chrome 식 삽입 gap 표시.
- 탭 **오른쪽 클릭** → *Focus · Move-out · Close*. Hover 하면 전체 워크스페이스 경로가 적힌 preview 카드.
- **Color tabs** (Settings → General) 가 각 탭을 워크스페이스로부터 파생된 hue 로 칠합니다.
- **Save current layout** (Settings → General → Window tabs) 이 현재 윈도우 세트 + rect 를 이름 붙여 저장. 같은 패널에서 복원.
- **`⌘⌃1` … `⌘⌃9`** 으로 N 번째 윈도우 점프. **`⌘⌃`** 로 cycle.
- **Move-out** (오른쪽 클릭 → ↗) 이 윈도우를 현재 rect 에서 +60/+60 만큼 옮겨 stack 에서 시각적으로 분리.

Tab mode 를 끄면 윈도우들이 60 px 간격으로 cascade 되어 자동 분리됩니다
(수동 드래그 불필요).

→ 레퍼런스: [탭과 보기 모드](Tabs-and-Views-ko.md)

---

## AI 허가 — 영어로 읽히는 권한 모달

AI 권한 모달이 예전엔 raw JSON 을 보여줬습니다. 지금은:

```
● AI 가 하려는 것: 활성 문서 수정
  현재 파일에서 find-and-replace 편집
  범위        foo.md
  카테고리    write
  되돌리기    예 — ⌘Z 로 취소
  ▸ Raw call — htmlook_apply_edit
  [거부] [한 번만 허용] [항상 (워크스페이스)] [항상 (전역)]
```

Settings → AI → Permissions → **Tool permission defaults** 에서 카테고리별로
prompt 받을지 여부를 선택할 수 있습니다:

| 카테고리 | 기본값 | 무엇을 다루나 |
|---|---|---|
| **Read** | Auto | 파일 목록 / outline / 활성 파일 내용 보기 |
| **Capture** | Auto | 뷰어 / 영역 / 요소 스크린샷 |
| **Navigate** | Auto | 스크롤, 탭 사이 점프, 라인 점프 |
| **Annotate** | Ask | PDF highlight, PDF comment 추가 |
| **Write** | Ask | 활성 파일 편집, 텍스트 치환, 파일 생성 |
| **Run** | Ask | 터미널 paste, 음성 녹음 시작 |

파괴적 동작 (음성 메모 삭제, 탭 닫기, PDF highlight 클리어) 은 카테고리
default 와 상관없이 항상 묻습니다.

→ 레퍼런스: [AI Apply Edit](AI-Apply-Edit-ko.md) · [Settings](Settings-ko.md)

---

## 앱을 닫아도 살아있는 터미널

Settings → Terminal → **Persistence → tmux**.

tmux 모드에서는 세션이 앱 프로세스보다 오래 삽니다. HTMLook 을 닫고
다시 열어도 모든 pane 이 scrollback 그대로 다시 나타납니다.

이번 릴리스의 다른 터미널 개선:

- **버퍼 내 검색** — `⌘F` 가 pane 안의 검색 오버레이 열기 (hit counter 포함). `↵` 다음, `⇧↵` 이전.
- **Pane 간 입력 sync** — pane 헤더 컨텍스트 메뉴 → *Sync input with…* 이 참여 pane 들을 초록 띠로 표시하고 입력을 모두에게 broadcast.
- **Pane 드래그-swap** — 한 pane 의 헤더를 다른 pane 위로 드래그해 위치 교환.
- **Pane 을 새 윈도우로 detach** — `⌘D` (또는 컨텍스트 메뉴 → *Move to new window*) 가 포커스된 pane 을 자신의 윈도우로 분리. 세션이 함께 이동.
- **키보드 선택 모드** — `⌃⇧K` 가 활성 pane 의 화살표 기반 선택 진입. Shift+화살표 확장, Home/End/PgUp/PgDn 이동, `⌘C` 복사, `⎋` 종료.
- **가장 오른쪽 탭 닫기** 가 포커스를 왼쪽으로 이동 (macOS Terminal / iTerm 과 일치), 탭 0 으로 튀지 않음.
- **한글 cwd 가 모든 곳에서 작동** — 이전엔 한글 이름의 워크스페이스 열 때 발생하던 freeze 가 해결됨.

→ 레퍼런스: [터미널](Terminal-ko.md)

---

## 마크다운 WYSIWYG 안전망

HTMLook 의 라이브 마크다운 편집이 이제 파일을 신중하게 다룹니다:

- 한/영 실제 워크스페이스 문서 라이브러리로 round-trip 안정성 검증. edit
  → save → re-open 사이클에서 표류 (drift) 가 발생하지 않습니다.
- 편집 도중 에디터가 문제를 감지하면 (이전 같으면 한 줄짜리 corrupt 파일을
  만들 수 있었던 상태), 저장을 멈추고 경고합니다 — 나쁜 상태를 디스크에
  쓰지 않습니다.
- 매 저장 직전 이전 disk 버전의 timestamped 백업을 `~/.htmlook-backup/`
  에 떠둡니다. 나쁜 round-trip 도 복구 가능.

v1.0.14 가 해결한 구체적 증상:

- `200~300%` 같은 숫자가 round-trip 중 strikethrough 로 잘못 해석되지
  않음.
- 항목 텍스트가 단락으로 wrap 되어도 task-list 체크박스가 보존됨.
- 파일 저장이 라이브 뷰의 자기 자신을 raw markdown 텍스트로 reload 시키지
  않음.

→ 레퍼런스: [마크다운 에디터](Markdown-Editor-ko.md)

---

## Sidecar 가 `.htmlook/<category>/` 하위로

HTMLook 이 미디어 옆에 만들던 파일들이 같은 폴더에 같이 있었습니다:

- `*.annotations.json` — PDF annotation
- `*.bookmarks.json` — 비디오 책갈피
- `*.clips.json` — 비디오 클립
- `*.segments.json` — 오디오 segment
- `*.chapters.json` — 오디오/비디오 chapter

이제 다섯 모두 `<workspace>/.htmlook/<category>/` 하위로. 워크스페이스
root 가 깔끔하게 유지됩니다. 기존 파일들은 HTMLook 이 처음 읽을 때
background 에서 자동으로 이전 — 사용자가 할 일은 없습니다.

---

## 한글 파일명 폴리시

HTMLook 안에서 한글 (또는 다른 다중 codepoint) 파일명을 다뤄봤다면
이런 경험을 했을 수 있습니다:

- 한글 파일 옆에 음성 메모 indicator 가 나타나지 않음.
- 같은 워크스페이스가 Recent 목록에 두 번 등록됨.
- 같은 한글 파일을 다른 source 에서 열면 탭이 두 개 생성됨.
- 한글이 포함된 워크스페이스 경로를 열 때 freeze.

이 모두 fix 됐습니다. 한글 폴더와 파일이 앱 어디서나 ASCII path 와
동일하게 동작합니다.

---

## 작은 폴리시

- **`Saved ✓` 플래시** — 즉시 저장되는 settings (토글, 드롭다운) 가 변경
  후 다이얼로그 헤더에 작은 `Saved ✓` pill 을 1.5 s 보여줍니다. 저장
  됐는지 더 이상 추측할 필요 없음.
- **AI settings 서브섹션** — AI 탭이 4 개 명명 그룹으로 정리:
  *Model Connection* · *Capabilities* · *Permissions* · *Usage*. 같은
  필드, 더 명확한 계층.
- **macOS chrome 폴리시** — Settings 가 macOS 사용자가 기대하는 위치인
  앱 메뉴 (`⌘,`) 에서 열림, PRO 배지가 툴바 내부로 이동, 최소 윈도우
  사이즈 강제로 리사이즈 시 레이아웃이 깨지지 않음.
- **사이드바 폴리시** — Name 칼럼이 +12 px 으로 한글 파일명이 음절
  중간에서 잘리지 않음. 윈도우로의 drag-and-drop 이 그 윈도우의
  사이드바에만 영향.

---

## 더 알아보기

- [탭과 보기 모드](Tabs-and-Views-ko.md) — 멀티 윈도우 탭 모드 전체
- [터미널](Terminal-ko.md) — tmux 영속화 + 새 pane 도구
- [AI Apply Edit](AI-Apply-Edit-ko.md) — 새 권한 모달 상세
- [Settings](Settings-ko.md) — 새 토글 위치
