# 다중 에이전트 협업

> 여러 에이전트가 워크스페이스 공유 시 JSONL 로 대화, 서로 질문, 서로의 audit log 읽기.

## 왜 있나

실제 워크플로우는 에이전트 혼합: Claude 가 글, Codex 가 테스트, Gemini 가 시각 diff. 구조화된 채널 없으면 서로 덮어쓰고, 반복하고, 모두 놓침. HTMLook 이 제공:

- 공유 **메시지 버스** (`agent_message_post / list`)
- **구조화 Q&A** primitive (`agent_question_ask / agent_answer_post`)
- 모든 에이전트의 tool call 이 쓰는 **append-only audit log**
- 현재 워크스페이스 스코프

파일로 보존 (`.htmlook/agent-messages.jsonl`, `.htmlook/audit-log.jsonl`) — 재시작 survival · inspect 가능 · 원하면 git 관리.

## agent_message_post

```jsonc
{
  "tool": "htmlook_agent_message_post",
  "args": {
    "to":      "any",                  // any | claude | codex | gemini | <handle>
    "from":    "claude",
    "subject": "CTA copy candidates",
    "body":    "3 phrasing 시도 — 파일 보세요.",
    "ref":     { "path": "site/hero.html", "anchor": ".cta" }
  }
}
```

JSONL 한 줄로 저장. 사용자가 *사이드바 → 메시지* 에서 읽기, 다른 에이전트는 `agent_message_list`.

## agent_message_list

```jsonc
{ "tool": "htmlook_agent_message_list",
  "args": { "since": "2026-05-17T00:00:00Z", "to": "any", "limit": 50 } }
```

정렬된 메시지 반환. `from`, `to`, `subject`, 또는 임의 regex 로 필터.

## Q&A primitive

다른 에이전트로부터 결정론적 답이 필요할 때:

```jsonc
{ "tool": "htmlook_agent_question_ask",
  "args": {
    "to":       "codex",
    "question": "v2 테스트 스위트가 새 CTA 컴포넌트로 통과했어?",
    "deadline_sec": 120
  }
}
```

`question_id` 반환. 상대가 `agent_answer_post({ question_id, answer })` 로 응답. deadline 지나면 만료, 질문자에게 `TIMED_OUT`.

## Audit log

모든 tool call append:

```jsonc
{
  "ts": "2026-05-17T10:14:00Z",
  "tool": "htmlook_apply_edit",
  "agent": "claude",
  "workspace": "/Users/vincent/Notes",
  "args_summary": { "path": "hero.html", "find_len": 12, "replace_len": 15 }
}
```

조회:

```jsonc
{ "tool": "htmlook_audit_log_query",
  "args": {
    "since": "2026-05-17T00:00:00Z",
    "tool":  "htmlook_apply_edit",     // optional
    "agent": "codex",                   // optional
    "limit": 200
  } }
```

## 동작하는 패턴

- **협의 편집**: 에이전트 A 가 "hero.html 건드릴 예정" post → B 가 `agent_message_list` 로 읽음 → A 가 apply → A 가 diff 요약과 함께 "완료" post
- **Stale-write 체크**: `apply_edit` 전 audit log 에서 같은 경로의 마지막 쓰기 query. 60 s 안에 다른 에이전트라면 `agent_question_ask` 로 완료 여부 묻기
- **자기 정리 노트**: 50 턴마다 `to: "any"` 로 digest post — 사용자가 audit log 안 읽고도 진행 파악

## 동작 안 하는 패턴

- `agent_message_list` 를 ~2 s 보다 빠르게 폴 하지 말 것 — rate limiter 가 drop. 긴 폴 또는 사용자가 알릴 때만
- tool 결과를 메시지에 쓰지 말 것 — 이미 audit log 에 있음. 메시지는 *의도* 와 *조율* 용
- 다른 에이전트가 실행 중이라고 가정 말 것 — 사용자가 솔로일 수도. 메시지는 eventually consistent

## 프라이버시

메시지와 audit log 는 워크스페이스 안. 앱 종료해도 truncate 안 됨. 지우려면 사용자가 `.htmlook/agent-messages.jsonl` 과 `.htmlook/audit-log.jsonl` 삭제.

## 다음

- [PDF 도구 →](AI-PDF-Tools-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
