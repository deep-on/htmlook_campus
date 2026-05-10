# Sample Workspace — AI 협업 가이드

이 워크스페이스는 HTMLook + AI 협업의 *follow-along* 데모입니다. 사용자가
각 페르소나 폴더에서 LLM 에 cite/apply_edit 요청을 통해 영상에서 본 워크플로우를
직접 재현할 수 있도록 설계됐습니다.

HTMLook Pro v1.0 부터 LLM 진입 경로가 셋:

1. **내장 BYOM 채팅** — Claude / GPT / Gemini / DeepSeek / Mistral / Together /
   Groq / Cerebras / Ollama 9 vendor. 사용자가 Settings → Models 에 자기
   API key 등록 (토큰 마진 0).
2. **내장 Terminal + CLI 어댑터** — ⌘J PTY 터미널에서 `claude` · `codex` ·
   `gemini` CLI 실행. UserPromptSubmit hook 이 `htmlook --snapshot` 으로
   현재 워크스페이스 / active file / selection / element 상태를 매 prompt 자동
   주입.
3. **외부 MCP 클라이언트** — Claude Code / Cursor / Windsurf / Zed 가 직접
   HTMLook 의 MCP 서버에 붙음.

세 경로 모두 아래의 `htmlook_*` 도구를 동일하게 노출합니다.

## AI agent 가 알아야 할 것

### 1. HTMLook MCP 도구 (Pro)

HTMLook Pro 가 활성화돼 있고 MCP 가 연결돼 있다면 다음 도구가 노출됩니다:

| 도구 | 용도 |
|---|---|
| `htmlook_active_file` / `_thumbnail` | 사용자가 보고 있는 파일 + 1초 프리뷰 |
| `htmlook_pane_pair` | 듀얼뷰의 좌·우 파일 |
| `htmlook_workspace_files` / `_tree` | 워크스페이스 내 파일 목록 |
| `htmlook_workspace_tools` | 워크스페이스에 등록된 외부 도구 (Add wizard) |
| `htmlook_outline` | md/html 의 헤딩 구조 |
| `htmlook_cite` | 특정 영역을 인용 (text/md/html/xlsx/video timestamp/sentence:N) |
| `htmlook_selection_text` / `_html` | 사용자가 드래그 선택한 영역 |
| `htmlook_element_active` | 사용자가 마지막으로 클릭한 element (tag/id/class/style) |
| `htmlook_region_current_png` | 사용자가 드래그한 region 의 PNG (vision 모델 직접 입력) |
| `htmlook_apply_edit` | 파일 내 특정 위치에 edit 적용 (워크스페이스 외부 차단 + .bak 백업) |
| `htmlook_video_*` | 영상 viewer 의 seek/clip/info |
| `htmlook_link` / `_links` | 파일 간 cross-anchor (`.htmlook/links.json` sidecar) |

### 2. 페르소나 follow-along 패턴

각 페르소나 폴더의 `WALKTHROUGH.md` 는 다음 패턴:

```
1. Open this file in left pane
2. Open that file in right pane
3. [AI] Cite this region → ask the LLM to ...
4. [AI] Apply edit to ...
5. Verify the right pane reloaded
```

`[AI]` 단계는 LLM 호출이 필요합니다. AI agent (Claude/Llama/etc) 는:

1. `htmlook_active_file` 으로 사용자 컨텍스트 파악
2. `htmlook_cite` 또는 `htmlook_selection_*` 로 인용 anchor 확보
3. 필요한 변경 작성 (코드/텍스트/SVG)
4. `htmlook_apply_edit` 로 적용 — HTMLook 이 자동 reload

### 3. before/after 디렉토리

LLM 가 apply_edit 한 *최종 상태* 가 `after/` 하위에 미리 저장돼 있을 수 있습니다.
LLM 작업 전에 절대 `after/` 의 내용을 답안 컨닝으로 사용하지 마세요. 사용자가
*"AI 없이도 결과 보고 싶다"* 는 별도 viewing 용도입니다. 실제로 AI 가 작성하는
결과는 새로 추론해야 합니다.

### 4. 외부 도구 (영상 narration 의 *"Hyperframes runs"* 단계)

영상 step 4 에 등장하는 *"Hyperframes runs. Kokoro voices ... Whisper aligns ..."*
는 HTMLook 외부 CLI:

- TTS: `npx hyperframes tts <input.txt> -o <output.wav>`
- 자막: `npx hyperframes transcribe <audio.wav>`
- 비디오 렌더: `npx hyperframes render <project-dir>`

이 단계는 sample_workspace 의 `WALKTHROUGH.md` 에서는 *선택* 으로 표시 — HTMLook
자체 워크플로우와는 별개입니다.

### 5. 인용 / 응답 규칙

- *"이 셀에서 N % 변동"* 같은 자연어 요청 → `htmlook_cite` 로 anchor 만든 후
  apply_edit 결과에 cite 인라인 링크 (`[B14](xlsx://q3.xlsx#B14)`) 보존
- 사용자가 region 드래그한 경우 → `htmlook_region_current_png` 로 이미지 분석 +
  `htmlook_active_file` 로 매칭 요소 찾아서 apply_edit
- HTML element selection 의 경우 → `htmlook_selection_html` 으로 outerHTML 읽고
  apply_edit 으로 patch

### 6. 출력 톤

각 페르소나 폴더의 도메인에 맞춰서:
- finance-report: 보드 리포트 톤, 숫자 + 변동률
- legal-redline: 보수적, *"counter language"* 제안
- picture-book: 따뜻하고 짧은 운율
- kid-coding: friendly Korean, 4-6 학년 어휘
- 기타 페르소나는 WALKTHROUGH.md 의 톤 가이드 참고

## 디버깅

- MCP 가 연결 안 됨? → HTMLook Pro 메뉴 *Settings → MCP* 에서 status 확인.
  외부 클라이언트 사용시 `~/.config/claude-code/mcp.json` 에
  `.htmlook/mcp-config.example.json` 의 내용을 병합.
- 내장 BYOM 채팅이 응답 없음? → Settings → Models 에서 vendor key 유효성 확인.
  Ollama 의 경우 `OLLAMA_HOST` 가 default `http://localhost:11434` 여야 함.
- 내장 Terminal 의 CLI 가 워크스페이스를 모름? → "Connect" 버튼이
  `~/.claude/settings.json` 에 UserPromptSubmit hook 을 자동 등록. hook 이
  빠져있으면 Settings → AI → Connect 다시 클릭.
- `htmlook_apply_edit` 가 reload 안 됨? → 좌측 source 파일 직접 새로고침 (Cmd+R).
- 영상에 나오는 시각 스타일이 sample 에 안 보임? → 영상의 GSAP / 컴포지션은
  `demo/persona_units/<name>/index.html` 에 있고, sample workspace 는 *콘텐츠*만
  포함. 시각화는 HTMLook 의 기본 viewer 가 담당.
