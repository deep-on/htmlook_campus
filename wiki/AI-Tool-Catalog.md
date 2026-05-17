# Tool catalog

> All 123 tools by category. Schema and parameter detail in the linked sub-pages.

Names are listed without the `htmlook_` prefix for readability. Real names are `htmlook_<name>` on the wire.

## 1. Workspace · Tabs · Window (≈20)

| Tool | Returns / Effect |
|---|---|
| `ping` | `{ version, build_id, started_at }` |
| `workspace_info` | Current workspace `{ root, name, opened_at, tab_count }` |
| `workspace_files` | Recursive list (paged) of files in the workspace |
| `workspace_tree` | Tree representation |
| `workspace_tools` | Tools registered in `.htmlook/tools.json` |
| `search_workspace` | Full-text search (and-or, file/path filters) |
| `active_file` | Path + basic metadata of the active tab |
| `active_file_thumbnail` | PNG preview of the active tab |
| `open_file` | Open a path (new or existing tab) |
| `create_file` | Create with content |
| `close_tab` | Close a tab by id or path |
| `focus_tab` | Focus a tab |
| `set_view_mode` | `single` / `dual` / `code` / `present` |
| `set_dual_view` | Set dual-view file + sync-scroll |
| `pane_pair` | Read which two files are paired |
| `present_mode_toggle` | Toggle present mode |
| `new_window` | Open a new window |
| `zoom` | Set viewer zoom 0.5 .. 3.0 |
| `outline` | Heading outline (`.md`, `.html`, `.pdf`) |
| `hyperframes` | Active hyperframe links of the current file |

## 2. Selection · Element · Navigation (≈15)

| Tool | Use |
|---|---|
| `selection_text` | Current selection as plain text |
| `selection_html` | Current selection as HTML |
| `selection_scope` | Selection's containing element |
| `sidebar_selection` | Currently selected sidebar files |
| `element_active` | Currently selected element info |
| `select_element` | Programmatically select via CSS selector |
| `select_text_range` | Select text range within active doc |
| `highlight_element` | Highlight (visual only, not selection) |
| `scroll_to` | Scroll to element / line / page |
| `jump_to_line` | Jump to line N |
| `find_in_active` | Find term, returns matches with offsets |
| `replace_in_active` | Replace-in-place |
| `computed_style_get` | Computed CSS for an element |
| `visual_overlap_check` | Detect text-truncation / overflow / zero-size |
| `layout_map` | Landmark / heading / button / link / form survey |

## 3. Visual Capture (≈10)

| Tool | What you get |
|---|---|
| `capture_viewport` | PNG of the active pane |
| `capture_selector` | PNG of an element by CSS selector |
| `capture_active_element` | PNG of the selected element |
| `capture_text_match` | PNG of an element containing matched text |
| `capture_rect` | PNG of a rectangular region |
| `capture_diff` | Diff two PNGs with bbox output |
| `region_current_png` | Last region the user captured |

Full how-to: [Visual Capture](AI-Visual-Capture.md)

## 4. Apply-edit family (≈5)

| Tool | Effect |
|---|---|
| `apply_edit` | Find + replace inside the active file with audit |
| `insert_at_selection` | Insert at current cursor / selection |
| `replace_in_active` | Same as #3 but for the active file specifically |
| `create_file` | Write a new file |
| `cite` / `citation_anchor` | Drop a `htmlook://` anchor |

Full how-to: [Apply-edit round-trip](AI-Apply-Edit.md)

## 5. Annotation · Sketch · Paint (≈15)

| Tool | Effect |
|---|---|
| `annotation_add` / `annotation_list` | Workspace annotations (note + bounding region) |
| `view_state_snapshot` / `view_state_restore` | Save and restore the viewer state |
| `paint_enable` / `paint_disable` / `paint_dimensions` | Toggle and size paint canvas |
| `sketch_add_shape` / `sketch_set_color` / `sketch_set_stroke` | Programmatic paint |
| `sketch_undo` / `sketch_redo` / `sketch_clear` / `sketch_save` | History + persistence |
| `sketch_current_png` | Current sketch as base64 |
| `highlight_element` | Soft visual highlight |

## 6. PDF tools (≈6)

| Tool | Effect |
|---|---|
| `pdf_highlight_add` / `pdf_highlight_clear` | Persistent highlights |
| `pdf_comment_add` | Comment tied to a highlight |
| `pdf_citation_anchor` | Cite the current PDF page |
| `pdf_text_spans` | All text spans of a page with bboxes |
| `capture_pdf_region` | PNG of a sub-rectangle of a page |

Full how-to: [PDF tools](AI-PDF-Tools.md)

## 7. Audio · Video · Voice (≈25)

### Voice memos
| Tool | Effect |
|---|---|
| `voice_record_start` / `_record_stop` | Start / stop |
| `voice_list` / `_workspace_all` | List memos |
| `voice_get_bytes` | Base64 of the file |
| `voice_rename` / `_delete` | Manage |
| `voice_transcript_get` / `_transcript_set` | Read / write transcript sidecar |
| `voice_search` | Search transcripts |
| `audio_segment_create` | Add `<file>.segments.json` entries |
| `audio_quote_extract` | Search transcript for quotes |
| `audio_waveform_get` | Loudness envelope (Web Audio decoded) |

### Video
| Tool | Effect |
|---|---|
| `video_info` | Codec + duration + dimensions |
| `video_position` / `video_seek` | Read / set playhead |
| `video_clip_range` | Define a clip |
| `video_bookmarks` | List `<file>.bookmarks.json` |
| `video_chapter_create` | Append chapter |
| `video_review_marker_add` | Append review marker |
| `video_subtitle_align` | Apply offset to .vtt / .srt |
| `video_scene_detect` | ffmpeg `select=gt(scene,..)` parse |
| `capture_video_frame_region` | Frame → cropped PNG |

Full how-to: [Audio / video tools](AI-Audio-Video-Tools.md)

## 8. Terminal & process (≈3)

| Tool | Effect |
|---|---|
| `terminal_buffer_get` | Active terminal scrollback |
| `terminal_process_tree` | Active terminal's process tree |
| `link` / `links` | Open external URL |

> v1.0.9 explicitly excludes `terminal_run_managed` and `send_keys` to limit blast radius.

## 9. Collaboration · Audit (≈5)

| Tool | Effect |
|---|---|
| `agent_message_post` / `agent_message_list` | Cross-agent JSONL messages |
| `agent_question_ask` / `agent_answer_post` | Structured Q&A |
| `audit_log_query` | Read `<workspace>/.htmlook/audit-log.jsonl` |

Full how-to: [Multi-agent collaboration](AI-Collaboration.md)

## 10. User-facing UI hooks (≈8)

| Tool | Effect |
|---|---|
| `show_toast` | Toast in user's window |
| `confirm` | Yes / no modal |
| `request_user_input` | Prompt + return value |
| `wait_for_user_action` | Block on user click |
| `chatpanel_post` | Push a message into ChatPanel |
| `export_active` | Trigger Export menu programmatically |
| `print_active` | Trigger Print |
| `insert_at_selection` | (also listed above) |

## 11. Region & screenshot (≈2)

| Tool | Effect |
|---|---|
| `region_current_png` | Last user-captured region |
| `active_file_thumbnail` | Generic thumbnail (≠ region) |

## Names you won't find here (deferred)

- `terminal_run_managed`, `send_keys` — exec arbitrary processes / keystrokes (out of scope v1.0.9)
- `semantic_search`, `visual_search` — embedding infrastructure (separate track)
- `audio_speaker_map`, `pdf_figure_detect`, `pdf_table_extract` — ML-heavy (v1.0.10+)
- `responsive_probe` — hidden-iframe lifecycle complexity, deferred to v1.0.10

## Next

- [Visual Capture →](AI-Visual-Capture.md)
- [Apply-edit round-trip →](AI-Apply-Edit.md)
