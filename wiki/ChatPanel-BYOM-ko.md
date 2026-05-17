# ChatPanel · BYOM

> Bring Your Own Model. 우측 패널은 *내* AI provider 를 호출하는 채팅 — 우리 서버를 거치지 않음.

## 열기 / 닫기

⌘L 로 우측 ChatPanel 토글. 첫 실행 시 **FirstRunLLMSetup** 마법사 (5 카드). 이후 ⌘L 은 단순 토글.

## Provider preset

원클릭 preset 으로 OpenAI-호환 provider 8 종:

| Provider | 어울리는 용도 |
|---|---|
| OpenAI | 가장 강력, 다양한 모델 |
| DeepSeek | 저렴, 빠름, 강한 reasoning |
| Mistral | EU 호스팅, 프랑스어 + 영어 강함 |
| Together | 다양한 오픈 모델 호스팅 |
| Groq | 최저 latency, Llama 계열 |
| Cerebras | 빠른 Llama / Qwen 추론 |
| Ollama | 로컬, 키 불필요 |
| Custom | OpenAI-호환 URL 무엇이든 |

base URL · key · 모델명 입력. OpenAICompatibleAdapter 가 streaming SSE, chunked tool-call, 벤더별 정규화 (DeepSeek `reasoning_content`, Ollama compact tool 포맷) 처리.

## 패널 구성

```
┌────────────────────────────┐
│  ⚙ AISettings  📜 history  │ ← top
├────────────────────────────┤
│  시스템 프롬프트            │
│  · Skill chip (top-5)      │
├────────────────────────────┤
│  ▸ "이 문서 요약해줘"      │
│  ▸ tool: htmlook_outline   │
│  ▸ tool 결과 …             │
│  ▸ assistant: …            │
├────────────────────────────┤
│  📎 첨부   …입력 박스…     │
│              ⏎  ⌘⏎ 제출    │
└────────────────────────────┘
```

## Skill 자동 inject

HTMLook 의 Skill 로더가 현재 워크스페이스 + 활성 파일 + 최근 히스토리를 보고 **상위 5 skill** 을 선택해 trigger 를 시스템 프롬프트에 주입. 대화 위 chip 으로 표시. 클릭하면 skill 본문 펼침.

Skill 위치: `.claude/skills/` (워크스페이스), `~/.claude/skills/` (글로벌). [Skills](Skills-ko.md) 참조.

## Tool dispatch + 동의

assistant 가 tool 호출 시 (`htmlook_outline` · `htmlook_apply_edit` 등) 워크스페이스마다 첫 호출에 **4-버튼 동의 모달**:

- **이번만** — 1회 허용
- **이 워크스페이스에서** — 워크스페이스 기억
- **모든 워크스페이스** — 글로벌 허용
- **거부**

결정은 `permissions.json` (워크스페이스) 또는 글로벌 키 스토어. *AISettings → 권한* 에서 해제.

## 첨부

📎 (또는 입력 박스에 drag):

- 이미지 (`.png`, `.jpg`, …) → OpenAI vision content block
- PDF 페이지 (PDF 뷰어의 *AI 로 페이지 보내기*) → 이미지
- Paint 캔버스 스냅샷 (`⌘⇧P → 📎`) → 이미지
- 워크스페이스 파일 (텍스트류) → 인라인 코드 블록

입력 위 배지가 메시지당 첨부 수.

## 채팅 히스토리

워크스페이스별 `.htmlook/chat-history/<thread-id>.json`. 📜 버튼이 히스토리 drawer. 핀 고정 가능. 스레드는 markdown-친화 export round-trip.

## 취소 + 재시도

스트리밍 응답을 ⌘. (Command + period) 로 취소. 마지막 user turn 에 *Retry* affordance 가 1회 재실행용으로 남음.

## 프라이버시

outbound 는 설정한 provider 로만. system prompt + tool catalog + 메시지 + 명시적으로 참조한 활성 파일 발췌가 호출 내용. HTMLook 은 Deep-On 서버를 통해 프록시 안 함.

## 다음

- [Skills →](Skills-ko.md)
- [AI 에이전트용 · MCP 설정 →](AI-MCP-Setup-ko.md)
