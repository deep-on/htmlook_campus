# 다중 에이전트 협업

> JSONL 기반 loose-coupled cross-agent 메시징 + append-only audit log.

## 왜 있나

실제 워크플로우는 에이전트 혼합: Claude 가 글, Codex 가 테스트, Gemini 가 시각 diff. 구조화된 채널 없으면 서로 덮어쓰고, 반복하고, 모두 놓침. HTMLook 이 제공:

- 공유 **메시지 스트림** (`agent_message_post / list`)
- 같은 스트림 위의 질문/답변 헬퍼 (`agent_question_ask / agent_answer_post`)
- 모든 성공한 tool call 의 **append-only audit log**
- 현재 워크스페이스 스코프

파일로 보존 (`.htmlook/agent-messages.jsonl`, `.htmlook/audit-log.jsonl`) — 재시작 survival · inspect 가능 · 원하면 git 관리.

> 중요: 에이전트 handshake / registry 없음. `to` 는 free-form 문자열이며 다른 에이전트가 내 메시지를 읽는다는 보장 없음 — RPC 가 아닌 broadcast hint 로 다룰 것. 질문에 deadline / timeout 메커니즘도 없음.

## agent_message_post

```jsonc
{
  "tool": "htmlook_agent_message_post",
  "args": {
    "body": "3 phrasing 시도 — hero.html .cta 보세요",       // 필수
    "from": "claude",                                       // 옵션
    "to":   "any",                                           // 옵션, free-form
    "ref":  "hero.html#cta"                                 // 옵션, flat 문자열
  }
}
```

`ref` 는 flat 문자열 (파일 경로 · anchor · 링크 sidecar id 등 본인이 원하는 컨벤션). `subject` 필드 없음, `ref` 는 nested 객체 아님. `<workspace>/.htmlook/agent-messages.jsonl` 에 JSONL 한 줄로 저장.

## agent_message_list

```jsonc
{ "tool": "htmlook_agent_message_list",
  "args": {
    "kind":     "message",          // 옵션: "message" | "question" | "answer"
    "to":       "any",               // 옵션
    "since_ts": 1715900000000,        // 옵션, UNIX-ms 정수 (ISO 아님)
    "limit":    50
  } }
```

서버 사이드 필터는 `kind` · `to` · `since_ts` · `limit` 만. `from` · `subject` · regex · ISO date 없음. 더 세밀한 매칭은 batch 가져와 client 측에서 필터.

## 질문 / 답변 컨벤션

질문과 답변은 같은 스트림 — 그저 다른 `kind` 의 메시지. 강제 deadline 없음.

```jsonc
{ "tool": "htmlook_agent_question_ask",
  "args": {
    "body": "v2 테스트 스위트가 새 CTA 컴포넌트로 통과했어?",
    "to":   "codex",
    "ref":  "hero.html"
  } }
```

persisted entry 반환 `{ id, kind: "question", from, to, body, ref, ts }`. `id` 는 `q_` 로 시작.

답변하려면 질문의 `id` 를 `ref` 로, 답을 `body` 로 post:

```jsonc
{ "tool": "htmlook_agent_answer_post",
  "args": {
    "body": "예 — 47/47 green.",
    "ref":  "q_a3f9",
    "to":   "claude"
  } }
```

빌트인 timeout 없음. 원하면 `agent_message_list` 로 `ref` 가 본인 질문 id 인 답을 폴 하고 본인 deadline 으로 포기.

## Audit log

모든 성공한 tool call 이 `<workspace>/.htmlook/audit-log.jsonl` 에 JSONL 한 줄 append:

```jsonc
{ "tool": "htmlook_apply_edit", "args": { "path": "hero.html", … }, "ts": 1715901400000 }
```

entry shape 은 `{ tool, args, ts }` 만 — `agent` · `workspace` · `args_summary` 없음. 조회:

```jsonc
{ "tool": "htmlook_audit_log_query",
  "args": {
    "tool":     "htmlook_apply_edit",   // 옵션
    "since_ts": 1715900000000,           // 옵션, UNIX-ms
    "limit":    200
  } }
```

쿼리 사이드 필터는 `tool` · `since_ts` · `limit` 만. 에이전트별 또는 성공/실패 분리는 client 측 필터링.

## 동작하는 패턴

- **협의 편집**: 에이전트 A 가 `body: "hero.html 건드릴 예정"` post → B 가 `agent_message_list` 로 읽음 → A 가 apply → A 가 diff 요약과 함께 `body: "완료"` post
- **Stale-write 체크**: `apply_edit` 전 audit log 에서 같은 경로의 마지막 쓰기 query. 최근이면 heads-up 메시지 post 후 짧게 대기
- **자기 정리 digest**: 50 턴마다 digest post — 사용자가 audit log 안 읽고도 진행 파악

## 동작 안 하는 패턴

- `agent_message_list` 를 ~2 s 보다 빠르게 폴 하지 말 것 — 도구별 rate limiter (~8 / sec) 가 drop. 긴 폴 또는 사용자가 알릴 때만
- tool 결과를 메시지에 쓰지 말 것 — 이미 audit log 에 있음. 메시지는 *의도* 와 *조율* 용
- 다른 에이전트가 실행 중이라고 가정 말 것 — 사용자가 솔로일 수도. 메시지는 eventually consistent, 무시될 수 있다고 예상

## 프라이버시

메시지와 audit log 는 워크스페이스 안. 앱 종료해도 truncate 안 됨. 지우려면 사용자가 `.htmlook/agent-messages.jsonl` 과 `.htmlook/audit-log.jsonl` 삭제.

## 다음

- [PDF 도구 →](AI-PDF-Tools-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
