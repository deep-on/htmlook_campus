# For AI Agents · Overview

> What HTMLook gives you that a plain filesystem doesn't.

## You are reading this because

…your runtime (Claude / Codex / Gemini / OpenAI-compatible MCP client) is about to be pointed at the `htmlook` MCP server. This track is the reference. Follow it linearly the first time, then bookmark [Tool catalog](AI-Tool-Catalog.md) for day-to-day lookups.

## The contract in one paragraph

HTMLook exposes **~100 tools** over MCP. Each call runs inside the running HTMLook Pro instance, with the same workspace context the user is currently looking at. You receive results as JSON-RPC responses or, in the case of image-bearing tools, as a `data:image/png;base64,…` payload + JSON sidecar. Tools are scoped to the workspace root — path traversal outside the workspace is refused by `path_guard`. There's a per-tool rate limit and an append-only audit log of everything you did.

## Why a desktop app and not a CLI

Three things a CLI can't easily give you:

1. **Visual capture** — `htmlook_capture_viewport`, `_selector`, `_active_element`, `_rect`, `_text_match`, `_diff`. You can see what the user sees, then act. This is the round-trip that lets you "click `.cta` → screenshot → apply edit → screenshot again → diff".
2. **Live state** — what tab is active, what's selected, what region was just captured. Tools like `htmlook_active_file`, `_element_active`, `_region_current_png`, `_selection_text` answer "what is the user looking at right now".
3. **Multi-channel collaboration** — when several agents share a workspace, `agent_message_post / list / question_ask / answer_post` give you a structured chat surface scoped to the project, plus a forensic audit log.

## The pillars of the toolset

```
                    Capture                       Edit
                  (read what                    (change it
                   the user                       in place)
                   sees)
                       │                            │
                       ▼                            ▼
              ┌──────────────────┐         ┌──────────────────┐
              │   ~100 tools     │ ◄──────►│  apply_edit      │
              │  ──────────────  │  audit  │  insert_at_      │
              │   organised in   │   log   │    selection     │
              │   six pillars    │         │   create_file    │
              └──────────────────┘         └──────────────────┘
                       ▲
                       │
   ┌────────────┬──────┴──────┬─────────────┬──────────────┐
   ▼            ▼             ▼             ▼              ▼
 Workspace   Visual /      Annotation    PDF / Audio /  Collaboration
   & Tabs    Capture       & Sketch         Video         & Audit
```

## What lives in each pillar

- **Workspace & Tabs** — `active_file`, `open_file`, `close_tab`, `focus_tab`, `workspace_files`, `workspace_info`, `workspace_tree`, `set_view_mode`, `set_dual_view`, `present_mode_toggle`, `pane_pair`, `new_window`, `confirm`, `show_toast`, `wait_for_user_action`, `request_user_input`, `chatpanel_post`
- **Visual / Capture** — `capture_viewport`, `capture_selector`, `capture_active_element`, `capture_text_match`, `capture_rect`, `capture_diff`, `region_current_png`, `active_file_thumbnail`, `layout_map`, `select_element`, `select_text_range`, `computed_style_get`, `visual_overlap_check`, `highlight_element`, `scroll_to`, `jump_to_line`, `find_in_active`, `replace_in_active`, `selection_text`, `selection_html`, `element_active`, `paint_*`, `sketch_*`
- **Annotation & Sketch** — `view_state_snapshot / restore`, `annotation_add / list`, all `sketch_*` and `paint_*`
- **PDF tools** — `pdf_highlight_add / clear`, `pdf_citation_anchor`, `pdf_comment_add`, `pdf_text_spans`, `capture_pdf_region`
- **Audio / video tools** — `audio_segment_create`, `audio_quote_extract`, `audio_waveform_get`, `video_chapter_create`, `video_review_marker_add`, `video_subtitle_align`, `video_scene_detect`, `capture_video_frame_region`, `video_*` controls (`info`, `seek`, `position`, `clip_range`, `bookmarks`), `voice_*` recorder
- **Collaboration & audit** — `agent_message_post / list`, `agent_question_ask`, `agent_answer_post`, `audit_log_query`

Full reference: [Tool catalog](AI-Tool-Catalog.md).

## The "always start with this" loop

```
htmlook_workspace_info     # what folder am I in?
htmlook_active_file        # what is the user looking at?
htmlook_layout_map         # what's on the page?
… plan …
htmlook_select_element     # narrow scope
htmlook_apply_edit         # change it
htmlook_capture_selector   # verify
htmlook_audit_log_query    # leave a trail (auto)
```

## Privacy and capability

- Everything runs locally inside the user's HTMLook Pro process. No tool result transits Deep-On servers.
- Write tools gate on three checks: Free Viewer license, workspace path-guard scope, and a per-tool rate limit. There is **no** per-call consent modal blocking the MCP write path in v1.0.9 — name what you're about to do in chat before you call the tool, so the user can interrupt if needed.
- You cannot read files outside the workspace root via `apply_edit` (path_guard refuses). You cannot exec arbitrary processes. Specifically excluded from v1.0.9: `terminal_run_managed`, `send_keys`, semantic search, visual search.

## Next

- [MCP Setup →](AI-MCP-Setup.md)
- [Tool catalog →](AI-Tool-Catalog.md)
