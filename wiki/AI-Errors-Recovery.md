# Errors & recovery

> How HTMLook surfaces failures, what the strings actually look like, and how to react.

## The shape of a failure

HTMLook's MCP tools do **not** return a structured `error.data.kind` enum. Almost every failure is a plain English string surfaced one of two ways:

1. **As an MCP error** (`error.message` carries the text, no machine-readable `kind`)
2. **As a `CallToolResult::success` whose text body starts with a prefix** like `refused: …` or `rate-limited: …`

The one structured exception is `DEPENDENCY_MISSING:` (see below) — that prefix is followed by a JSON payload you can parse.

For everything else, **pattern-match on the message prefix**. The table below lists the prefixes you'll actually see in v1.0.9 builds.

## Prefix table

| Prefix you'll see | What it means | What to do |
|---|---|---|
| `find string matched N places in <abs>; expected exactly 1.` | `apply_edit` find is ambiguous (>1 match) | Widen the find string with surrounding context |
| `find string not found in <abs>.` | `apply_edit` find is absent | Re-read the file via the renderer; use `find_in_active` first |
| `refused: <p> is outside the current workspace. Open the file in HTMLook Pro first…` | Path-guard rejected a target outside the workspace | Use a path inside the workspace |
| `canonicalize <p>: No such file or directory` | Target doesn't exist on disk | Check `workspace_files` / `active_file` |
| `refused: HTMLook is in Free Viewer mode (trial expired). Upgrade to Pro to enable edits.` | License gate | Surface to the user; can't bypass |
| `rate-limited: <tool_name> burst exhausted. Retry after ~<ms> ms.` | Per-tool token bucket (8 burst, 8/s refill, **per tool name**) | Back off the specified ms; don't retry-loop |
| `selector "<sel>" matched no elements in <pane> pane` | `capture_selector` / `select_element` zero match | Call `layout_map` for real selectors |
| `text "<t>" not found in <pane> pane (mode=<mode>)` | `capture_text_match` quote not on screen | Confirm visibility with `find_in_active` |
| `no <pane> viewer pane available — open a file first` | Targeted pane isn't mounted | Open a file in that pane first |
| `<pane> viewer is not same-origin (cross-origin srcdoc, asset:// load barrier)…` | iframe blocks DOM access for this capture | Use `capture_viewport` or `capture_rect` instead |
| `DEPENDENCY_MISSING:{…}` | External tool absent (ffmpeg / soffice / …) | Special — see below |

If you see a prefix not in this table, it's a generic forwarded backend error — surface it to the user as text.

## DEPENDENCY_MISSING envelope

Special-cased because it's both an error and a UX moment.

The message looks like:

```
DEPENDENCY_MISSING:{"dep_id":"ffmpeg","dep_label":"FFmpeg","purpose":"비디오 씬 감지","install_via":"brew install ffmpeg","brew_present":true}
```

Strip the `DEPENDENCY_MISSING:` prefix and parse the JSON:

```jsonc
{
  "dep_id":       "ffmpeg",
  "dep_label":    "FFmpeg",
  "purpose":      "비디오 씬 감지",
  "install_via":  "brew install ffmpeg",
  "brew_present": true
}
```

The user simultaneously sees an actionable toast in HTMLook with **지금 설치** / **명령어 복사** / **닫기**. Your role: explain *why* you needed it, *what* will happen if they install, and that the install takes ~30 s for ffmpeg. Don't retry the original tool call until the user confirms install (the toast publishes a `htmlook:dependency-install-done` event the app handles internally, but agent-side it's easier to just wait for the user to ping you).

If `brew_present: false`, the toast offers to install Homebrew first (~3 min). Be patient — don't retry mid-install.

## Asking for confirmation

HTMLook gives you four small primitives to involve the user without polling:

| Tool | Args | Notes |
|---|---|---|
| `htmlook_confirm` | `{ prompt, timeout_ms? }` | Returns boolean. Single `prompt` string — no `title` / `message` split. |
| `htmlook_request_user_input` | `{ prompt, default_value?, timeout_ms? }` | Returns a string |
| `htmlook_wait_for_user_action` | `{ hint, timeout_ms? }` | Blocks until the user clicks the hint button |
| `htmlook_show_toast` | `{ message, kind?: 'info'\|'success'\|'warn'\|'error', duration_ms? }` | Fire-and-forget notice. Field is `kind`, valid values are `info / success / warn / error` (NOT `level: "warning"`). |
| `htmlook_chatpanel_post` | `{ role: 'user'\|'assistant'\|'note', content }` | Push a message into the ChatPanel conversation stream. `role` is required; the field is `content`, not `text`. |

Default to `confirm` for "any irreversible action" and `request_user_input` for "I need a value I can't reasonably guess".

## Recovery patterns

### Idempotent retry with rate-limit back-off

```python
for attempt in range(3):
    res = call_tool(...)
    if not is_error(res):
        break
    msg = res.error.message
    if msg.startswith("rate-limited:"):
        # parse "~Nms" out of the message
        retry_ms = parse_retry_ms(msg)
        sleep(retry_ms / 1000.0 * 1.2)   # 20% safety margin
        continue
    break  # other errors aren't worth retrying without changes
```

### Cascade-aware retry

If `apply_edit` failed because the file changed under you (file-not-found, or multiple-matches when you expected one), re-fetch with `active_file` and re-plan — do not blindly retry the same find/replace.

### Politely give up

After two failed attempts at the same operation, surface to the user:

```
show_toast({
  message: "Tried twice, can't apply this change automatically.",
  kind:    "warn"
})
chatpanel_post({
  role:    "assistant",
  content: "I tried to change … but the file changed under me. Want to do this manually, or should I try a different approach?"
})
```

## Audit your own failures

`audit_log_query({ tool: "htmlook_apply_edit", since_ts: today_start_ms })` returns your tool calls of the day (success and failure aren't split server-side — inspect each `args` entry and cross-reference with what you saw in responses).

## Reporting bugs

When you hit an `INTERNAL_ERROR` (`-32603` JSON-RPC code) or an unrecognised prefix, ask the user to attach the latest `/tmp/htmlook-debug.log` (last ~500 lines) and email it to support.

## End

Back to [Overview](AI-Overview.md) · [Tool catalog](AI-Tool-Catalog.md) · [Home](Home.md)
