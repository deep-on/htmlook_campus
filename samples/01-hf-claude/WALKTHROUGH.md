# 01 · hf-claude — Code on the left, result on the right

> 영상: `demo/persona_units/hf-claude/renders/hf-claude_voiced_bgm.en+ko.mp4`

이 follow-along 은 **HTMLook + Claude (or any MCP-aware LLM)** 으로 영상의 워크플로우를
재현합니다. 영상 step1-3 의 *cite + apply_edit* 사이클을 직접 실행합니다.

## 사전 준비

- HTMLook Pro 실행, 이 워크스페이스 (`sample_workspace/`) 를 *Open Folder* 로 열기
- (선택) Claude Code / Cursor / 호환 클라이언트에서 `.htmlook/mcp-config.example.json`
  내용 병합

## 단계

### 1. [VIEW] 듀얼뷰로 source + result 동시 보기

- 좌측 사이드바에서 `01-hf-claude/landing.html` 더블클릭 → 우측에 렌더된 페이지 표시
- 단축키 ⌘\\ 또는 *View → Split* 로 분할뷰 토글 → 좌측에 source, 우측에 결과
- 화면 가운데에 *"Cloud-native."* 라는 짧은 부제 보임 → 이게 너무 짧다는 의도

### 2. [AI] hook 부제 cite + 확장 요청

좌측 source 에서 `<h2>Cloud-native.</h2>` 의 *Cloud-native* 텍스트를 드래그-선택.

선택 상태에서 LLM 에 다음과 같이 요청:

> *"이 부제 (Cloud-native) 는 너무 짧다. Apex 의 가치 (edge compute, 빠른 배포)
> 를 한 줄로 늘려서 apply_edit 해줘."*

LLM 이 (MCP 가 연결됐다면) 자동으로:

1. `htmlook_selection_text` 또는 `htmlook_cite` 로 anchor 확보
2. 새 문구 작성 — 예: *"Cloud-native edge compute, deployed in seconds."*
3. `htmlook_apply_edit` 로 `landing.html` 의 해당 라인 patch

### 3. [VIEW] 우측 reload 확인

- HTMLook 의 file watcher 가 변경 감지 → 우측 pane 자동 reload
- 부제가 새 문구로 표시됨

### 4. [AI 없는 사용자] before/after 비교

LLM 없으면 다음으로 시각 비교 가능:

- 좌측 탭: `01-hf-claude/before/landing.html`
- 우측 탭: `01-hf-claude/after/landing.html`
- 두 파일을 분할뷰에 띄우고 차이를 시각적으로 확인

## 검증 포인트

- ✅ `htmlook_pane_pair` (듀얼뷰) — HTMLook 기본
- ✅ `htmlook_selection_text` (드래그 선택) — Pro 기능
- ✅ `htmlook_apply_edit` (LLM 적용) — Pro 기능
- ✅ 파일 watcher → 자동 reload — HTMLook 기본
- ⚠️ 영상 step4 의 *"Hyperframes runs. Kokoro voices..."* 는 별도 CLI:
  `npx hyperframes tts narration.txt -o voice.wav` (HTMLook 내장 아님)

## 다음 페르소나

`02-hf-llama/` — 같은 워크플로우, Claude 대신 로컬 Llama
