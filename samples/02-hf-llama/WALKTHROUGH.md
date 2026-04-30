# 02 · hf-llama — 같은 워크플로우, 로컬 Llama

> 영상: `demo/persona_units/hf-llama/renders/hf-llama_voiced_bgm.en+ko.mp4`

01-hf-claude 와 같은 cite + apply_edit 워크플로우 — Claude 대신 로컬에서 도는
Llama 를 붙입니다. MCP 호출은 동일.

## 사전 준비

- HTMLook Pro 실행, 이 워크스페이스를 *Open Folder*
- 로컬 Llama 서버 (Ollama, llama.cpp, LM Studio 중 택일) 가 MCP-호환 클라이언트에
  연결돼 있을 것
- (선택) `.htmlook/mcp-config.example.json` 을 클라이언트 mcp config 에 병합

## 단계

### 1. [VIEW] 듀얼뷰로 source + result

- 좌측 사이드바 → `02-hf-llama/landing.html` 더블클릭
- ⌘\ 로 분할뷰 → 좌측 source, 우측 렌더 결과
- 부제 *"Your AI."* 가 너무 짧음 (영상 step3 의 그 문구)

### 2. [AI] hook 부제 cite + 확장 요청

`<h2>Your AI.</h2>` 의 *Your AI* 텍스트를 좌측에서 드래그-선택.

LLM (이번엔 로컬 Llama) 에 요청:

> *"이 부제는 너무 짧다. Borealis 의 가치 (local-first, private weights)
> 를 한 줄로 늘려서 apply_edit 해줘."*

Llama 가 MCP 로:

1. `htmlook_selection_text` 로 anchor 확보
2. 새 문구 작성 — 예: *"Your AI, running on your laptop. Private weights, public throughput."*
3. `htmlook_apply_edit` 로 patch

### 3. [VIEW] 우측 reload

- 파일 watcher 변경 감지 → 우측 자동 reload
- 새 부제가 표시됨

### 4. [AI 없는 사용자] before/after 비교

- 좌측: `02-hf-llama/before/landing.html`
- 우측: `02-hf-llama/after/landing.html`
- 분할뷰로 차이 시각 비교

## 검증 포인트

- ✅ `htmlook_pane_pair` (듀얼뷰)
- ✅ `htmlook_selection_text` (드래그)
- ✅ `htmlook_apply_edit` (Llama가 적용)
- ✅ 파일 watcher 자동 reload
- ⚠️ Kokoro/Whisper 단계는 외부 CLI: `npx hyperframes tts/transcribe`

## 다음 페르소나

`03-dev-pr-docs/` — PR diff 와 docs 동시 보면서 stale 문서 patch
