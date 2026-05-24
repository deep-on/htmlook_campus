# What's New — v1.0.14

릴리스: **2026-05-24** · 다운로드: [htmlook.app](https://htmlook.app)

[htmlook.app/#whats-new](https://htmlook.app/#whats-new) 의 4-카드 하이라이트의
campus 측 풀버전. 전체 ChangeLog 는 desktop 레포 의 `CHANGELOG_v1.0.14.md`,
이 페이지는 campus 독자를 위한 정리.

> 다른 언어: [English](Whats-New-v1.0.14.md)

---

## 한눈에

- **멀티 윈도우 탭 모드** — 모든 윈도우가 한 사각형으로 정렬 + Chrome 스타일 탭 strip + 드래그 reorder + 워크스페이스별 색상 + 이름 붙인 레이아웃 저장/복원.
- **AI 허가창 다시쓰기** — `"이 파일을 수정해도 됩니까? · 되돌리기: ⌘Z"` 가 raw JSON 덤프를 대체. 6개 카테고리 기본값 (Read / Capture / Annotate / Navigate / Write / Run) 이 일상 모달의 ~70% 를 자동 통과.
- **앱을 닫아도 살아있는 터미널** — tmux 백엔드로 세션 영속. `⌘F` 버퍼 내 검색, 분할 패인 입력 동기화, 패인 detach 로 새 윈도우, 키보드 선택 모드 `⌃⇧K`.
- **마크다운 WYSIWYG 안전망** — edit-collapse guard, NFC/NFD 경로 sweep, 196 문서 round-trip corpus 의 실제 drift = **0**, 모두 1014 테스트가 매 빌드 검증.
- **한글 폴리시** — workspace claim, recent 목록, sidecar, 탭 dedup, 터미널 cwd 폴링, IME 중복 입력 — 모두 fix. 한글 폴더가 다른 path 처럼 정상 동작.
- **Sidecar 이동** — `.htmlook/<category>/` 하위로. `*.annotations.json` · `*.bookmarks.json` · `*.clips.json` · `*.segments.json` · `*.chapters.json` 더 이상 워크스페이스 root 에 어지럽지 않음.
- **MCP bridge 다중 인스턴스 race fix** — dev + prod 가 `~/.htmlook/mcp-bridge.port` 를 두고 다투지 않음. per-PID port file + ping 검증된 발견.

---

## 멀티 윈도우 탭 모드

이전 v1.0.13 의 멀티 윈도우 모델은 모든 Pro 윈도우를 완전히 독립적으로
다뤘다. v1.0.14 는 그 기반 위에 "단일 논리 윈도우" 모드를 얹는다:

- `Settings → General → Window tabs → Tab mode: On`. 열린 모든 윈도우가
  포커스된 윈도우의 rect 로 정렬되고, 그 후로 드래그 / 리사이즈 / +Add 가
  peer 들에게 전파.
- 탭 strip 은 툴바 위에 자리. 탭 1 개 = 워크스페이스 1 개.
  오른쪽 클릭 → Focus / Move-out / Close. Hover 하면 전체 워크스페이스
  경로가 적힌 preview 카드.
- 색상 코딩은 워크스페이스로부터 파생된 hue 로 각 탭을 칠한다.
- 이름 붙인 레이아웃 저장 / 복원은 `~/.htmlook/window-layouts.json` 에서.
  Layout 모드 (Exact / Cascade 30 px) 를 존중한다.
- `⌘⌃1-9` 로 N 번째 윈도우 점프; `⌘⌃`` 로 cycle.

→ 레퍼런스: [Tabs and Views](Tabs-and-Views-ko.md)

---

## AI 허가창 UX 다시쓰기

ChatPanel 의 허가 모달이 예전에는 raw JSON 을 보여줬다:

```
🔧 Allow LLM to run htmlook_apply_edit?
arguments
{"path": "/Users/.../foo.md", "find": "abc", "replace": "xyz"}
```

지금은:

```
● AI 가 하려는 것: 활성 문서 수정
  현재 파일에서 find-and-replace 편집
  범위        foo.md
  카테고리    write
  되돌리기    예 — ⌘Z 로 취소 가능
  ▸ Raw call — htmlook_apply_edit
```

- Tool descriptor 맵이 ~70 개의 HTMLook MCP tool 을 다룸.
- **Settings → AI → Permissions → Tool permission defaults** 신설: 6 개
  카테고리 각각에 Auto / Ask / Block. Destructive tool (voice memo 삭제,
  탭 닫기, annotation 클리어) 은 카테고리 default 와 상관없이 항상 묻는다.
- 기본 정책: Read / Capture / Navigate → Auto, Annotate / Write / Run →
  Ask. 일상 세션의 모달 ~70% 자동 통과.

→ 레퍼런스: [AI Apply Edit](AI-Apply-Edit-ko.md)

---

## 터미널 — tmux 백엔드 + 영속화

이제 터미널은 raw PTY 소유가 아니라 tmux 가 받친다. 앱을 닫았다가
다시 열면 정확히 마지막 자리에서 다시 시작.

- **패인별 안정 tmux 이름** — `htmlook-<sha8>-tab<N>-pane<M>`,
  SHA8 은 NFC 정규화된 워크스페이스 path. 재시작 간 deterministic.
- **Preset 자동 resume** — Claude / Codex / Gemini 세션은 resume flag 를
  감지하고 reattach 시 paste 단계를 건너뛴다.
- **버퍼 내 검색** — `⌘F` 가 SearchAddon 오버레이를 띄움. hit counter 포함.
  `↵` / `⇧↵` 로 hit 들 사이 이동.
- **입력 동기화 sync** — 패인 그룹 전체에 타이핑을 broadcast (참여
  패인에 초록 표시).
- **패인 드래그 swap** — 패인 헤더를 다른 패인 헤더로 드래그해 위치 교환.
- **패인 detach** — `⌘D` (또는 context menu) 로 포커스된 패인을 새 윈도우로
  분리. tmux 세션이 같이 이동.
- **키보드 선택 모드** — `⌃⇧K` 로 화살표 기반 블록 선택. Shift+arrow 로
  확장, Home/End/PgUp/PgDn, `⌘C` 복사. (이전엔 `⌃⇧Space` 였지만 macOS
  Input Sources 가 가로채서 변경.)
- **탭 close → 왼쪽 이웃** — 가장 오른쪽 탭을 닫으면 포커스가 왼쪽으로
  이동, 탭 0 으로 안 돌아감. macOS Terminal / iTerm 과 일치.
- **한글 cwd freeze fix** — `lsof` fork+exec 가 Tauri sync worker 를
  block 해서 한글 cwd 워크스페이스 열 때 양쪽 윈도우 beachball 되던
  치명적 버그 해결.

→ 레퍼런스: [Terminal](Terminal-ko.md)

---

## 마크다운 WYSIWYG 안전망

사용자가 보고한 corruption 스레드가 수직 fix slice 로 이어졌다:

- **선택적 tilde escape** — Turndown 이 더 이상 `200~300%` 를
  strikethrough 로 오해하지 않음.
- **Task list loose-paragraph 보존** — 체크박스가 `<p>` 안에 wrap 된
  리스트 항목에서도 보존.
- **Frontmatter / KaTeX / GFM-strikethrough 규칙** — 세 가지 Turndown
  규칙으로 YAML frontmatter, display + inline math, `~~strike~~` 가
  render → edit → save 사이클을 살아남는다.
- **File-watcher own-write echo dedup with NFC/NFD dual-key** — 저장
  후 macOS watcher 가 같은 파일을 다시 fire 하면서 앱이 자기가 쓴
  것을 raw markdown 으로 reload 하던 버그 해결.
- **저장 직전 디스크 백업** — 매 write 직전에 timestamped 사본을
  `~/.htmlook-backup/<basename>.<ts>.md` 로 떠둠. 나쁜 round-trip 도 복구
  가능.
- **Block-collapse guard** — MutationObserver 가 rendered block count
  가 0 으로 떨어지는 write 를 거부 (WKWebView contenteditable 실패
  모드).
- **196 문서 round-trip corpus** — 9-bucket drift classifier 와 함께
  매 CI build 실행. 현재 genuine drift: **0**.

→ 레퍼런스: [Markdown Editor](Markdown-Editor-ko.md)

---

## Sidecar 가 `.htmlook/<category>/` 로 이동

다섯 카테고리의 co-located JSON sidecar 가 워크스페이스 폴더를 어지럽혀
`ls` 와 Finder 뷰가 시끄러웠다:

- `*.annotations.json` — PDF annotation
- `*.bookmarks.json` — 비디오 책갈피
- `*.clips.json` — 비디오 클립
- `*.segments.json` — 오디오 segment
- `*.chapters.json` — 오디오/비디오 chapter

이제 다섯 모두 `<workspace>/.htmlook/<category>/<source>.json` 하위로 이동
— 사이드바의 hidden-folder filter 에 잡혀서 안 보이고, 모든 file picker
에서도 사라진다.

- Read-time 자동 마이그레이션: 매 read 가 새 path 를 먼저 시도, 못 찾으면
  legacy 를 rename-migrate.
- 워크스페이스 claim 시 eager 스캔이 모든 매칭 파일을 background 에서
  이동.
- JSON 이 pretty-print 됨. empty body 는 write 안 하고 파일 자체를 삭제.

---

## 한글 폴리시

한글 이름 워크스페이스에서 long-tail 도그푸딩으로 5 개의 NFD-vs-NFC
alignment gap 이 드러남. 모두 수리:

1. **Voice memo indicator** — `voice_list_for_dir` 가 NFD key 를 반환,
   JS `activeFileStem()` 는 NFC 생성 → 한글 파일명은 voice player +
   sidebar indicator 모두 빈 상태.
2. **Workspace claim** — 같은 한글 워크스페이스가 NFC + NFD 두 form 으로
   서로 다른 윈도우에 의해 두 번 claim 됨.
3. **Recent workspaces** — 같은 워크스페이스가 두 entry 로.
4. **Sidecar path** — `.htmlook/<category>/<name>.json` 이 일관되지 않은
   form 으로 작성됨.
5. **탭 dedup** — 같은 한글 파일이 두 source 에서 열리면 두 탭 생성.

여기에 v1.0.14 ship-blocker 추가: 한글 cwd 가 `proc_pidinfo` 를 empty 로
만들어 `lsof` shell-out 으로 fall back — 그 lsof 가 Mutex 를 200-800 ms
fork+exec 동안 잡고 있어서 그 뒤의 모든 Tauri sync command 가 beachball.
fix 는 lsof 를 sync worker 가 아닌 `spawn_blocking` 으로 옮기고 fork
전에 락 drop.

---

## MCP bridge 다중 인스턴스 fix

두 Pro 인스턴스가 동시 실행 시 (dev + prod), 나중에 시작된 인스턴스가
`~/.htmlook/mcp-bridge.port` 를 자기 포트로 overwrite. 그 인스턴스가
종료되면 파일은 dead port 를 가리킨 채로 남아, Claude Code / Codex CLI /
Cursor 가 spawn 한 `htmlook --mcp-server` 가 아무것도 못 만나는 상황.

지금은: 각 인스턴스가 추가로 `~/.htmlook/bridges/<pid>.port` 도 쓴다.
graceful shutdown 시 drop guard 가 이를 삭제. subprocess 는 디렉토리를
스캔하고 각 candidate 를 ping-validate (`{"kind":"ping"}` → `"pong"`),
가장 먼저 살아있는 포트로 연결. stale 파일은 opportunistically prune.

다중 인스턴스 dev 워크플로우가 그냥 작동.

---

## 품질 게이트 — 1014 테스트

이번 사이클에 테스트 suite 가 크게 확장:

- **vitest** (frontend + helper): **814 passing**
- **cargo** (Rust, `pro` feature): **200 passing**
- **Total**: **1014**

대표 커버리지:
- `md-roundtrip.test.ts` — 95 case + 196 문서 워크스페이스 corpus walk +
  9-bucket drift classifier.
- `terminal-tab-close.test.ts` — 닫기 → 왼쪽 이웃 포커스 회귀 케이스.
- `korean-jamo.test.ts` + `composer.test.ts` + `scenarios.test.ts` —
  KoreanComposer 상태 머신 72 case.
- `mcp_server` · `tools_manifest` · `llm_adapter::permissions` ·
  `workspace_meta` · `tools_diag` — Rust 측 커버리지가 가장 빠르게 증가.

전체 카탈로그: desktop 레포의 [`docs/TEST_SUITE.md`](https://github.com/deep-on/htmlook/blob/main/docs/TEST_SUITE.md).

---

## 작은 폴리시

- **License dev bypass** — `pnpm tauri dev` 빌드는 `'pro'` 로 short-circuit.
  expired trial 상태에서 dogfooding 할 때 Edit / Save / AI 가 조용히
  비활성화되지 않게.
- **Settings 폴리시** — 즉시 저장 settings 의 `Saved ✓` 플래시,
  AI 탭 명명 섹션 분할 (Model / Capabilities / Permissions / Usage),
  Window-tabs settings 가 적절한 hierarchy 카드로 묶임.
- **macOS chrome** — Settings 가 앱 메뉴로 이동, PRO 배지 툴바 내부로,
  최소 윈도우 사이즈 강제, 1000 px 미만에서 viewport pill 자동 hide,
  뷰어 AI-state chip 이 우상단.
- **사이드바 폴리시** — Name 칼럼 +12 px (한글 파일명이 음절 중간에서
  잘리지 않게), drag-drop 이 윈도우별 scope — Finder drop 이 한 윈도우의
  사이드바에만 영향.

---

## 더 읽을거리

- 전체 ChangeLog: desktop 레포의 `CHANGELOG_v1.0.14.md`
- 테스트 카탈로그: [`docs/TEST_SUITE.md`](https://github.com/deep-on/htmlook/blob/main/docs/TEST_SUITE.md)
- Round-trip 테스트 deep-dive: [`docs/MD_ROUNDTRIP_TESTING.md`](https://github.com/deep-on/htmlook/blob/main/docs/MD_ROUNDTRIP_TESTING.md)
- 마케팅용 하이라이트: [htmlook.app/#whats-new](https://htmlook.app/#whats-new)
