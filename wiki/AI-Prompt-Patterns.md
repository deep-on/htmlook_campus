# Prompt patterns

> Reusable prompt skeletons. These are the loops we've validated across the 13-persona scenario set.

## 1. "What is the user looking at?" (cheap orientation)

Every conversation should start with this if you don't have explicit state.

```
1. workspace_info     → root, tab count
2. active_file        → path + size
3. (if HTML / .md)  layout_map  → structure
   (if .pdf)        outline     → heading tree + page count
   (if video)       video_info  → duration + codec
```

Three calls, max ~50 KB of return. After this you know the room. Skip the heavier capture tools until you actually plan an edit.

## 2. Round-trip edit (the workhorse)

```
capture_selector(target)      ← before.png
apply_edit(find, replace)     ← change
capture_selector(target)      ← after.png
capture_diff(before, after)   ← verify
```

Notes:
- Wait nothing — the viewer reload is driven by the `htmlook:apply-edit-reload` event, which fires before the apply_edit response returns.
- If the diff shows changes outside the target's bbox, your CSS cascade is wider than you thought — investigate before announcing success.

## 3. "Show me, then change" (user-led)

When the user asks "make this clearer" without specifying:

```
selection_text  /  selection_html  /  element_active   ← read the focus
region_current_png                                     ← if they captured a region
… reason from those inputs …
apply_edit(...) or insert_at_selection(...)
```

The current-state context (top of this wiki: "Workspace root", "Active file") is your starting point — but always re-confirm with the selection tools, because the user may have moved on.

## 4. Multi-candidate exploration

```
for variant in candidates:
    apply_edit(find, variant)
    capture_selector(target)
    sketch_save  / annotation_add  ← persist the result
    (undo by reapplying with find=variant, replace=original)
```

Keep each candidate small. Don't actually mutate the file 5 times — capture, undo, capture again.

## 5. Audio / video review

```
video_info                              ← duration, fps
video_scene_detect(threshold=0.3)       ← cut list
for cut in cuts[:N]:
    capture_video_frame_region(time=cut.start, rect=center)
    → propose chapter title
video_chapter_create(...)
```

## 6. PDF citation chain

```
pdf_text_spans(page)                  ← find the sentence
pdf_citation_anchor(page)             ← htmlook:// URL
pdf_highlight_add(rects, label)       ← persistent marker
agent_message_post(body: "<quote> — <link>")   ← so the user sees it
```

## 7. Multi-agent handoff

Before applying a known-contentious edit:

```
audit_log_query(tool=apply_edit, path=current_file, since=now-300s)
  → any other agent edited recently? if yes, post a message:
agent_message_post(to=any, subject="claim: hero.html for 5min")
sleep ~3s ← user / other agent has a chance to react via chatpanel
apply_edit(...)
```

## 8. The "stop, ask a human" surface

When the model decides it shouldn't proceed without confirmation:

- `confirm({ prompt, timeout_ms? })` → blocks until user clicks; returns boolean
- `request_user_input({ prompt, default_value?, timeout_ms? })` → returns a string
- `wait_for_user_action({ hint, timeout_ms? })` → blocks until the user clicks the hint button you described
- `show_toast({ message, kind?: 'info'|'success'|'warn'|'error', duration_ms? })` → fire-and-forget notice
- `chatpanel_post({ role: 'user'|'assistant'|'note', content })` → push a message into ChatPanel (not the user-typed input box, but the conversation stream)

Default to `confirm` for "any irreversible action" and `request_user_input` for "I need a value I can't reasonably guess".

## 9. Long-running plan

For multi-step plans (e.g. "rebuild this slide deck from the audio transcript"), checkpoint into the audit log explicitly:

```
agent_message_post(subject="plan",
                   body="1) extract transcript 2) outline 3) draft 4) review")
… do step 1 …
agent_message_post(subject="plan", body="step 1 done")
…
```

The user can read the plan at any time without reading the audit log. Future-you (next session) can read the messages to resume.

## Anti-patterns

- **Capture-spam**: 20× `capture_viewport` calls. Always pick the tightest scope.
- **`apply_edit` with vague find**: long natural-language find strings invite `MULTIPLE_MATCHES`. Use selectors or selections instead.
- **Ignoring rate limit**: when you get `RATE_LIMITED`, back off — don't retry-loop. The limiter is meant to protect the user's CPU and the viewer's interactivity.
- **Polling messages**: faster than every 2 s gets dropped. Ask the user to ping you instead.
- **Silent failures**: when a tool returns `ok: false`, surface it to the user (`show_toast` or chat). Don't swallow.

## Next

- [Errors & recovery →](AI-Errors-Recovery.md)
- Back to [Overview](AI-Overview.md)
