# Errors & recovery

> Every error code HTMLook emits, what it means, and what to do.

## Error response shape

HTMLook follows JSON-RPC. A failed tool call comes back as:

```jsonc
{
  "jsonrpc": "2.0",
  "id": 17,
  "error": {
    "code": -32000,
    "message": "MULTIPLE_MATCHES: 'Sign up' occurs 8 times",
    "data": {
      "kind": "MULTIPLE_MATCHES",
      "count": 8,
      "path": "site/hero.html"
    }
  }
}
```

Read `error.message` for the human prefix. Read `error.data.kind` for the machine-stable code. Use both — the `kind` is stable across versions, the message wording isn't.

## Code reference

### Edit / file errors

| `kind` | Meaning | Recovery |
|---|---|---|
| `MULTIPLE_MATCHES` | `find` string occurs more than 5× | Narrow `find` (more context, longer span); or switch to selector-driven `select_element` + `replace_in_active` |
| `NO_MATCH` | `find` string absent | Re-read the current file content; `find_in_active` first |
| `PATH_OUT_OF_SCOPE` | Target file outside workspace root | Use a path inside the workspace |
| `FILE_NOT_FOUND` | Target doesn't exist | Check `workspace_files` / `active_file` first |
| `STALE_HASH` | File was modified between read and write | Re-read, re-plan |

### Permission / consent

| `kind` | Meaning | Recovery |
|---|---|---|
| `PERMISSION_REFUSED` | User clicked "No" in the consent modal | Don't retry the same call this session; surface the refusal to the user (`show_toast`) |
| `PERMISSION_PENDING` | Consent modal still open | Block, don't re-issue; the original call will resolve when the user clicks |
| `WORKSPACE_DENIED` | The whole workspace has revoked the tool | Suggest the user re-enable in *Settings → Permissions* |

### Capture / DOM

| `kind` | Meaning | Recovery |
|---|---|---|
| `SELECTOR_NOT_FOUND` | CSS selector didn't match | Call `layout_map` to find a real selector |
| `TEXT_NOT_FOUND` | `capture_text_match` didn't find the string | Use `find_in_active` to confirm the string exists in the rendered view |
| `ZERO_SIZE_ELEMENT` | The selector matched but is `display: none` / 0×0 | Use `visual_overlap_check` to diagnose |
| `VIEWPORT_DETACHED` | The tab isn't currently visible | `focus_tab` first |

### Rate limit / state

| `kind` | Meaning | Recovery |
|---|---|---|
| `RATE_LIMITED` | Token-bucket exhausted (8 per second per tool) | Back off ~125 ms; **do not** retry-loop |
| `TOOL_DISABLED` | Tool was explicitly disabled in this build | Do not retry; degrade to a different approach |
| `INTERNAL_ERROR` | Backend panicked | Report to user with `show_toast`; capture the next 10 lines of `/tmp/htmlook-debug.log` if user is debugging |

### External dependency

| `kind` | Meaning | Recovery |
|---|---|---|
| `DEPENDENCY_MISSING` | An external tool (ffmpeg, soffice, …) isn't on PATH | The user already sees a friendly toast. Surface the install command in chat; don't retry until the user confirms install |
| `DEPENDENCY_HUNG` | Started but no output in N seconds | Show progress toast; ask the user whether to abort |

### Q&A / collab

| `kind` | Meaning | Recovery |
|---|---|---|
| `TIMED_OUT` | `agent_question_ask` deadline elapsed | Treat as no answer; proceed best-effort or escalate to user |
| `UNKNOWN_AGENT` | `agent_message_post` `to` doesn't match a connected agent | Verify with `agent_message_list`; fall back to `to: "any"` |

## The DEPENDENCY_MISSING envelope

Special-cased because it's both an error and a UX moment.

`error.message` is prefixed with `DEPENDENCY_MISSING:` followed by JSON:

```jsonc
{
  "dep_id": "ffmpeg",
  "dep_label": "FFmpeg",
  "purpose": "비디오 씬 감지",
  "install_via": "brew install ffmpeg",
  "brew_present": true
}
```

The user sees an actionable toast in HTMLook with **지금 설치** / **명령어 복사** / **닫기**. Your role: explain *why* you needed it, *what* will happen if they install, and that the install will take ~30 s for ffmpeg.

If `brew_present: false`, the toast offers to install Homebrew first (~3 min). Be patient — don't retry the original tool call mid-install.

## Recovery patterns

### Idempotent retry

```python
for attempt in range(3):
    res = call_tool(...)
    if res.ok: break
    if res.kind == "RATE_LIMITED":
        sleep(0.15 * (attempt + 1))
        continue
    break  # other errors aren't worth retrying
```

### Cascade-aware retry

If an `apply_edit` failed with `STALE_HASH`, re-fetch with `active_file` and re-plan — do not blindly retry the same find/replace.

### Politely give up

After two failed attempts at the same operation, *surface to the user*:

```
show_toast({
  message: "Tried twice, can't apply this change automatically.",
  level: "warning"
})
chatpanel_post({
  text: "I tried to change … but the file changed under me. Want to do this manually, or should I try a different approach?"
})
```

## Audit your own failures

`audit_log_query({ ok: false, agent: "claude", since: today_start })` returns your tool failures of the day. Periodically self-review — many failure clusters indicate a wrong mental model of the workspace, not a bug.

## Reporting bugs

When you encounter an `INTERNAL_ERROR`, ask the user to email `/tmp/htmlook-debug.log` (the last ~500 lines) to `kdk3606@deep-on.com`. The repo is private during pre-launch.

## End

Back to [Overview](AI-Overview.md) · [Tool catalog](AI-Tool-Catalog.md) · [Home](Home.md)
