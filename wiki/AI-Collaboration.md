# Multi-agent collaboration

> Loose-coupled cross-agent messaging via JSONL + an append-only audit log.

## Why this exists

Real workflows now mix agents: Claude does the prose, Codex the tests, Gemini the visual diff. Without a structured channel they overwrite each other, repeat each other, or both miss something. HTMLook gives them:

- A shared **message stream** (`agent_message_post / list`)
- Question / answer helpers that go through the same stream (`agent_question_ask / agent_answer_post`)
- An **append-only audit log** of every successful tool call
- All scoped to the current workspace

These live as files (`.htmlook/agent-messages.jsonl`, `.htmlook/audit-log.jsonl`) so they survive restarts, are inspectable, and version-control if you want.

> Important: there is no agent handshake or registry. `to` is a free-form string, and no other agent is guaranteed to read your messages — treat them as broadcast hints, not RPCs. There is no deadline / timeout mechanism on questions either.

## agent_message_post

```jsonc
{
  "tool": "htmlook_agent_message_post",
  "args": {
    "body": "Trying these 3 phrasings — see hero.html .cta",   // required
    "from": "claude",                                          // optional
    "to":   "any",                                              // optional, free-form
    "ref":  "hero.html#cta"                                    // optional, flat string
  }
}
```

`ref` is a flat string (file path, anchor, link-sidecar id, whatever convention you want). There is no `subject` field, and `ref` is not a nested object. Stored as one JSONL line in `<workspace>/.htmlook/agent-messages.jsonl`.

## agent_message_list

```jsonc
{ "tool": "htmlook_agent_message_list",
  "args": {
    "kind":     "message",          // optional: "message" | "question" | "answer"
    "to":       "any",               // optional
    "since_ts": 1715900000000,        // optional, UNIX-ms integer (NOT ISO)
    "limit":    50
  } }
```

Server-side filters are only `kind`, `to`, `since_ts`, `limit`. No `from`, no `subject`, no regex, no ISO date. If you need finer matching, fetch a batch and filter client-side.

## Question / answer convention

Questions and answers are stored in the same stream — they're just messages with a different `kind`. There is no enforced deadline.

```jsonc
{ "tool": "htmlook_agent_question_ask",
  "args": {
    "body": "Did the v2 test suite pass for the new CTA component?",
    "to":   "codex",
    "ref":  "hero.html"
  } }
```

Returns the persisted entry `{ id, kind: "question", from, to, body, ref, ts }`. The `id` starts with `q_`.

To answer, post with the question's `id` as `ref` and the answer in `body`:

```jsonc
{ "tool": "htmlook_agent_answer_post",
  "args": {
    "body": "Yes — 47/47 green.",
    "ref":  "q_a3f9",
    "to":   "claude"
  } }
```

There is no built-in timeout. If you want one, poll `agent_message_list` for an answer whose `ref` equals your question id and give up after your own deadline.

## Audit log

Every successful tool call appends one JSONL line to `<workspace>/.htmlook/audit-log.jsonl`:

```jsonc
{ "tool": "htmlook_apply_edit", "args": { "path": "hero.html", … }, "ts": 1715901400000 }
```

The entry shape is just `{ tool, args, ts }` — no `agent`, no `workspace`, no `args_summary`. Query with:

```jsonc
{ "tool": "htmlook_audit_log_query",
  "args": {
    "tool":     "htmlook_apply_edit",   // optional
    "since_ts": 1715900000000,           // optional, UNIX-ms
    "limit":    200
  } }
```

The query side-filters are only `tool`, `since_ts`, `limit`. To get a per-agent or success/failure split, filter client-side.

## Patterns that work

- **Negotiated edit**: agent A posts `body: "I'll touch hero.html"` → agent B reads via `agent_message_list` → A applies → A posts `body: "done"` with the diff summary in the body
- **Stale-write check**: before `apply_edit`, query the audit log for the last write to the same path; if it's recent, post a heads-up message and wait briefly before retrying
- **Self-rolling digest**: every 50 turns, post a digest so the user can see what you've been up to without reading the audit log

## Patterns that don't

- Don't poll `agent_message_list` faster than every ~2 s — the per-tool rate limiter (~8 / sec) will drop you. Use longer polls or wait for the user to ping you
- Don't write tool results into messages — they're already in the audit log; use messages for *intent* and *coordination*
- Don't assume another agent is running — the user might be solo. Messages are eventually consistent; expect to be ignored

## Privacy

Messages and audit log live inside the workspace. Quitting the app doesn't truncate them. If you want them gone, the user deletes `.htmlook/agent-messages.jsonl` and `.htmlook/audit-log.jsonl`.

## Next

- [PDF tools →](AI-PDF-Tools.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
