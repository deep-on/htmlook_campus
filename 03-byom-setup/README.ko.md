# Step 3 · BYOM Setup (vendor 1개 선택)

<p align="center">
  <a href="README.md">English</a> | <b>한국어</b> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — 사용자가 직접 vendor 키를 등록. 토큰 마진 0.
> ~ 5 분.

HTMLook 은 LLM 을 번들하지 않고 *어댑터* 만 제공합니다. v1.0 에서 9 vendor
지원: Claude / GPT / Gemini / DeepSeek / Mistral / Together / Groq / Cerebras / Ollama (로컬).
이번 step 에서는 **하나만 골라서** 동작 확인 — 나중에 [Step 5](../05-command/) 에서
swap.

## 3.1 · 진입 경로 3 가지

HTMLook 에서 LLM 을 호출하는 경로가 셋. 다 동일한 MCP 도구 (`htmlook_*`) 노출:

| 경로 | 어디서 | 누구에게 권장 |
|---|---|---|
| **내장 BYOM 채팅** ⭐ | Settings → Models → 키 등록 후 우측 AI 패널 | 처음 쓰는 사람 |
| **내장 Terminal + CLI** | ⌘J 토글 후 `claude` / `codex` / `gemini` 실행 | CLI 익숙한 사람 |
| **외부 MCP 클라이언트** | Claude Code / Cursor / Windsurf / Zed 의 mcp.json 병합 | 이미 별도 클라이언트 사용 중 |

자세한 사용 가이드 + MCP 도구 목록: [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · 추천: 내장 BYOM 채팅

1. HTMLook 우측 상단 톱니 → **Settings → Models** 탭
2. vendor 한 개 골라서 *Add Provider*
   - Anthropic Claude (가장 안정) 또는
   - OpenAI GPT 또는
   - Google Gemini (free tier 가장 큼)
3. API key 붙여넣고 *Test* — 200 OK 확인
4. *Save* — 우측 AI 패널이 활성화됨

> 영상: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnostic via MCP)

## 3.3 · Ollama (로컬, 키 없음)

키를 외부 서비스에 보내고 싶지 않다면:

1. [ollama.com](https://ollama.com) 에서 Ollama 설치
2. `ollama pull llama3.2` (또는 원하는 모델)
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (default)

## 3.4 · 외부 MCP 클라이언트 사용 시

이미 Claude Code / Cursor / Windsurf / Zed 를 쓰고 있다면 [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
의 내용을 각 클라이언트의 mcp.json 에 병합. HTMLook MCP 서버가 22여개의
`htmlook_*` 도구 (cite, apply_edit, selection, region_current_png, outline,
link, video_*, …) 를 노출합니다.

## 3.5 · 첫 hello

AI 패널 활성화 됐으면 다음을 채팅창에 입력:

> *현재 워크스페이스의 첫 file 한 줄 요약해 줘.*

LLM 이 `htmlook_active_file` MCP 도구로 컨텍스트를 가져온 뒤 응답하는지 확인.
응답이 워크스페이스 인지 못하면 **Settings → AI → Connect** 한 번 더 누르거나,
외부 MCP 클라이언트 사용 시 mcp.json 병합 상태를 다시 점검.

## 3.6 · auto-reload — 모델이 응답한 뒤

apply_edit 으로 파일이 변경되면 file watcher 가 감지 → 분할뷰의 우측 pane 이
자동 reload.

> 영상: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Step 3 체크포인트

- 한 vendor (또는 Ollama) 의 키가 Settings → Models 에 저장됨.
- 채팅창에 hello 보내서 응답 받아봄.
- 응답이 워크스페이스 컨텍스트를 인지하는 것 확인.

문제 있으면 [`AI_GUIDE.md`](AI_GUIDE.md) 의 *디버깅* 섹션 참고.

다 맞으면 → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## 더 자세히

- [`AI_GUIDE.md`](AI_GUIDE.md) — MCP 도구 22여종 + 페르소나 follow-along 패턴 +
  AI agent 출력 톤.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json) —
  외부 MCP 클라이언트용 설정 샘플.
