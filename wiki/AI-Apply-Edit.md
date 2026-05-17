# Apply-edit round-trip

> Change the file. Reload the viewer. Verify. Audit. The single most-used workflow.

## The pattern

```text
1. capture_selector(".cta")              ← before
2. apply_edit(find, replace)             ← change
3. (viewer reloads automatically via htmlook:apply-edit-reload event)
4. capture_selector(".cta")              ← after
5. capture_diff(before, after)           ← verify
   ↳ audit_log already has the apply_edit row
```

The auto-reload is implemented as a Tauri event emitted by the backend after a successful `apply_edit`. The frontend listens, reads the file again, and updates the active tab's `rawContent`. No race condition.

## apply_edit shape

```jsonc
{
  "tool": "htmlook_apply_edit",
  "args": {
    "path": "/abs/path/to/file.html",   // optional; default = active file
    "find":     "Sign up free",
    "replace":  "Start free trial",
    "scope":    "active_file"            // active_file | selection | whole_file
  }
}
```

Returns:

```jsonc
{
  "ok": true,
  "edits_applied": 1,
  "before_hash": "ab12…",
  "after_hash":  "cd34…",
  "diff_summary": "1 replacement, 14 → 17 chars"
}
```

If the find string is ambiguous (>5 matches), HTMLook refuses and returns a `MULTIPLE_MATCHES` error with the count. Narrow the find string or use `scope: "selection"`.

## insert_at_selection

When you want to *add* without finding:

```jsonc
{
  "tool": "htmlook_insert_at_selection",
  "args": {
    "text": "<p>Updated 2026-05-17.</p>",
    "where": "after"   // before | after | replace
  }
}
```

Requires an active selection or cursor position in the viewer (`htmlook_selection_text` returns non-empty).

## create_file

```jsonc
{
  "tool": "htmlook_create_file",
  "args": {
    "path":    "drafts/q3-plan.md",
    "content": "# Q3 plan\n\n…"
  }
}
```

The `path` is resolved against the workspace root. `path_guard` refuses traversal outside.

## When the find string isn't reliable

For HTML with attributes, whitespace, or generated IDs, prefer:

1. `select_element({ selector })` + `replace_in_active({ text })`
2. `select_text_range({ start, end })` + `insert_at_selection`
3. As a last resort, fetch `selection_html`, mutate, write back via `replace_in_active`

## Audit log

Every successful `apply_edit` appends `{ ts, tool, path, find_len, replace_len, agent }` to `<workspace>/.htmlook/audit-log.jsonl`. Query with `audit_log_query({ since: "2026-05-17T00:00:00Z", tool: "htmlook_apply_edit" })`.

If you're sharing the workspace with other agents (see [Multi-agent collaboration](AI-Collaboration.md)), check this before re-applying an edit — you might be racing.

## Failure modes

| Code | Meaning |
|---|---|
| `MULTIPLE_MATCHES` | `find` string occurs >5×; narrow it |
| `NO_MATCH` | `find` string absent |
| `PATH_OUT_OF_SCOPE` | Target file outside workspace root |
| `PERMISSION_REFUSED` | User clicked "No" on the consent modal |
| `RATE_LIMITED` | Token bucket exhausted; back off |
| `DEPENDENCY_MISSING` | A required external tool is absent (rare for apply_edit) |

See [Errors & recovery](AI-Errors-Recovery.md) for response strategies.

## Next

- [Multi-agent collaboration →](AI-Collaboration.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
