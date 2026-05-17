# Multi-agent collaboration

> When several agents share a workspace, they talk via JSONL, ask each other questions, and read each other's audit logs.

## Why this exists

Real workflows now mix agents: Claude does the prose, Codex the tests, Gemini the visual diff. Without a structured channel they overwrite each other, repeat each other, or both miss something. HTMLook gives them:

- A shared **message bus** (`agent_message_post / list`)
- A **structured Q&A** primitive (`agent_question_ask / agent_answer_post`)
- An **append-only audit log** every agent's tool calls write to
- All scoped to the current workspace

These live as files (`.htmlook/agent-messages.jsonl`, `.htmlook/audit-log.jsonl`) so they survive restarts, are inspectable, and version-control if you want.

## agent_message_post

```jsonc
{
  "tool": "htmlook_agent_message_post",
  "args": {
    "to":      "any",                  // any | claude | codex | gemini | <handle>
    "from":    "claude",
    "subject": "CTA copy candidates",
    "body":    "Trying these 3 phrasings — see the file.",
    "ref":     { "path": "site/hero.html", "anchor": ".cta" }
  }
}
```

Stored as one JSONL line. The user can read it in *Sidebar → Messages*; other agents can read it via `agent_message_list`.

## agent_message_list

```jsonc
{ "tool": "htmlook_agent_message_list",
  "args": { "since": "2026-05-17T00:00:00Z", "to": "any", "limit": 50 } }
```

Returns ordered messages. Filter by `from`, `to`, `subject` or arbitrary regex.

## Q&A primitive

When you need a deterministic answer from another agent:

```jsonc
{ "tool": "htmlook_agent_question_ask",
  "args": {
    "to":       "codex",
    "question": "Did the v2 test suite pass for the new CTA component?",
    "deadline_sec": 120
  }
}
```

Returns a `question_id`. The other agent answers with `agent_answer_post({ question_id, answer })`. If the deadline passes without an answer, the question expires and the asker gets a `TIMED_OUT` response.

## Audit log

Every tool call appends:

```jsonc
{
  "ts": "2026-05-17T10:14:00Z",
  "tool": "htmlook_apply_edit",
  "agent": "claude",
  "workspace": "/Users/vincent/Notes",
  "args_summary": { "path": "hero.html", "find_len": 12, "replace_len": 15 }
}
```

Query with:

```jsonc
{ "tool": "htmlook_audit_log_query",
  "args": {
    "since": "2026-05-17T00:00:00Z",
    "tool":  "htmlook_apply_edit",     // optional
    "agent": "codex",                   // optional
    "limit": 200
  } }
```

## Patterns that work

- **Negotiated edit**: agent A posts "I'll touch `hero.html`" → agent B reads via `agent_message_list` → A applies → A posts "done" with the diff summary
- **Stale-write check**: before `apply_edit`, query the audit log for the last write to the same path; if it's from another agent in the last 60 s, ask via `agent_question_ask` whether they're done
- **Self-rolling notes**: every 50 turns, post a digest to `to: "any"` so the user can see what you've been up to without reading the audit log

## Patterns that don't

- Don't poll `agent_message_list` faster than every ~2 s — the rate limiter will start dropping. Use longer polls or have the user prompt you when something happens
- Don't write tool results into messages — they're already in the audit log; use messages for *intent* and *coordination*
- Don't assume another agent is running — the user might be solo. Messages are eventually consistent

## Privacy

Messages and audit log live inside the workspace. Quitting the app doesn't truncate them. If you want them gone, the user deletes `.htmlook/agent-messages.jsonl` and `.htmlook/audit-log.jsonl`.

## Next

- [PDF tools →](AI-PDF-Tools.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
