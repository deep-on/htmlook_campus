# Apply-edit round-trip

> Change the file. Reload the viewer. Verify. Audit. The single most-used workflow.

## The pattern

```text
1. capture_selector(".cta")              ← before
2. apply_edit(path, find, replace)       ← change
3. (viewer reloads via an internal event)
4. capture_selector(".cta")              ← after
5. capture_diff(before, after)           ← verify
   ↳ audit_log already has the apply_edit row
```

## apply_edit shape

```jsonc
{
  "tool": "htmlook_apply_edit",
  "args": {
    "path":    "/abs/path/to/file.html",   // required
    "find":    "Sign up free",
    "replace": "Start free trial"
  }
}
```

Returns:

```jsonc
{
  "path":         "/abs/path/to/file.html",
  "applied":      true,
  "bytes_before": 8423,
  "bytes_after":  8426,
  "backup_path":  "/abs/path/to/.file.html.bak.20260517-031400"
}
```

The server writes a timestamped `.bak.<ts>` next to the original on every successful edit so you can roll back manually if needed.

`find` must match **exactly once**. If it matches more than once, you get a plain-English failure of the form
`find string matched N places in /abs/path; expected exactly 1. Widen the context and retry.` Narrow the find string (add surrounding context) and retry. Note: there is no machine-readable `kind` enum on these errors — they're plain strings; match on the prefix.

If `find` is absent: `find string not found in /abs/path. Widen the context…`.

Path safety: the file must resolve inside the active workspace root. Targets outside the workspace are refused with `refused: <p> is outside the current workspace. Open the file in HTMLook Pro first…`.

## insert_at_selection

For inserting at the user's current selection:

```jsonc
{
  "tool": "htmlook_insert_at_selection",
  "args": { "html": "<p>Updated 2026-05-17.</p>" }
}
```

The single argument is `html` (string). The selection must exist on the active viewer pane.

## create_file

```jsonc
{
  "tool": "htmlook_create_file",
  "args": {
    "path":    "drafts/q3-plan.md",
    "content": "# Q3 plan\n\n…",
    "open":    true,         // optional: open the new file in a tab
    "position": "after"      // optional: where to drop the new tab
  }
}
```

`create_file` is not constrained by the workspace `path_guard` the way `apply_edit` is — pass an absolute or workspace-relative path; callers are responsible for keeping it inside the workspace if that's what they want.

## When the find string isn't reliable

For HTML with attributes, whitespace, or generated IDs, prefer:

1. `select_element({ selector })` + `replace_in_active({ … })`
2. `select_text_range({ start, end })` + `insert_at_selection({ html })`
3. As a last resort, fetch `selection_html`, mutate, write back via `replace_in_active`

## Audit log

Every successful `apply_edit` appends an entry to `<workspace>/.htmlook/audit-log.jsonl`. Each line: `{ tool, args, ts }`. Query with:

```jsonc
{
  "tool": "htmlook_audit_log_query",
  "args": {
    "tool":     "htmlook_apply_edit",   // optional filter
    "since_ts": 1715900000000,           // optional UNIX-ms lower bound
    "limit":    50
  }
}
```

The server only filters on `tool`, `since_ts`, `limit` — no `agent`, no `ok`-vs-error split. Returned per-entry shape is just `{ tool, args, ts }`.

If you're sharing the workspace with other agents (see [Multi-agent collaboration](AI-Collaboration.md)), inspect this before re-applying an edit — you might be racing.

## Failure modes (plain-text prefixes, not `data.kind`)

| Prefix you'll see in the error | Meaning | Recovery |
|---|---|---|
| `find string matched N places…` | Ambiguous find | Widen the find string |
| `find string not found in…` | Find absent | Re-read the file via the renderer; `find_in_active` first |
| `refused: <p> is outside the current workspace…` | Path traversal | Use a path inside the workspace |
| `canonicalize <p>: No such file or directory` | File missing | Check `workspace_files` / `active_file` |
| `refused: HTMLook is in Free Viewer mode…` | Trial expired | Surface to the user; can't bypass |
| `rate-limited: <tool_name> burst exhausted. Retry after ~<ms> ms.` | Per-tool token bucket | Back off the specified ms |
| `DEPENDENCY_MISSING:{…}` | External tool absent | Special — see [Errors & recovery](AI-Errors-Recovery.md) |

## Next

- [Multi-agent collaboration →](AI-Collaboration.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
