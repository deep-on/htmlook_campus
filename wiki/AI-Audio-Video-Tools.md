# Audio / video tools

> Voice memos, transcript search, video chapters, scene detection, frame capture, subtitle align.

## Voice memo recording

```jsonc
{ "tool": "htmlook_voice_record_start",
  "args": { "file_path": "/abs/.htmlook-voice/note.m4a", "label": "Q3 sync" } }
// … later …
{ "tool": "htmlook_voice_record_stop" }
```

Both args on `_start` are optional — omit to let the app pick the destination and label. Returns the file path. `voice_list` enumerates `.htmlook-voice/` memos; `voice_get_bytes` returns the file as base64 for upload to a STT provider you run.

The clamshell-mode silent-mic bug on M3+ MacBook Pro is detected automatically — the start call will surface a warning if zero amplitude is sustained.

## Transcript sidecars

`voice_transcript_set` writes `<file>.m4a.transcript.json` next to the memo. The args are **flat** — there is no `transcript` wrapper:

```jsonc
{
  "tool": "htmlook_voice_transcript_set",
  "args": {
    "path":     "/abs/.htmlook-voice/note.m4a",   // path, NOT file_path
    "text":     "안녕하세요 오늘 회의는…",            // required, top-level
    "language": "ko",                              // optional
    "provider": "whisper-large-v3",                // optional
    "segments": [                                  // optional
      { "start_sec": 0.0, "end_sec": 2.4, "text": "안녕하세요" },
      { "start_sec": 2.4, "end_sec": 5.1, "text": "오늘 회의는 …" }
    ]
  }
}
```

The voice player picks it up immediately and shows clickable transcript lines synced to playback.

## audio_quote_extract

Search a transcript for time-anchored snippets:

```jsonc
{ "tool": "htmlook_audio_quote_extract",
  "args": { "file_path": "/abs/note.m4a", "query": "회의실 예약", "limit": 5 } }
```

Returns `{ transcript, query, count, hits: [{ text, start_sec?, end_sec?, speaker?, match_offset? }] }`.

## audio_segment_create

Add a labelled segment marker. Stored as `<file>.segments.json`:

```jsonc
{ "tool": "htmlook_audio_segment_create",
  "args": {
    "file_path": "/abs/note.m4a",
    "start_sec": 12.3,
    "end_sec":   45.0,
    "label":     "Q1 review section",   // optional
    "reason":    "key decision point"    // optional
  } }
```

No `color` arg.

## audio_waveform_get

```jsonc
{ "tool": "htmlook_audio_waveform_get",
  "args": { "file_path": "/abs/note.m4a", "bins": 256 } }
```

`bins` (not `bin_count`), range 16-4096, default 256. Returns `{ bins, duration_sec, sample_rate, channels, peaks: number[] }` — `peaks` is mono envelope.

## Video

### `video_info`

```jsonc
{ "tool": "htmlook_video_info", "args": { "file_path": "/abs/clip.mp4" } }
// → { duration_sec, width, height, codec, fps, … }
```

### `video_position` / `video_seek`

Read or set the playhead of the active video viewer.

### `video_chapter_create`

```jsonc
{ "tool": "htmlook_video_chapter_create",
  "args": {
    "file_path": "/abs/clip.mp4",
    "start_sec": 0,
    "end_sec":   72.5,           // REQUIRED
    "title":     "Intro",
    "summary":   "Welcome + recap of last week"   // optional
  } }
```

Note: `end_sec` is required (chapters are explicit ranges, not anchor points). No `color` field.

### `video_review_marker_add`

```jsonc
{ "tool": "htmlook_video_review_marker_add",
  "args": {
    "file_path": "/abs/clip.mp4",
    "t_sec":     73.4,            // arg is t_sec, NOT time_sec
    "kind":      "issue",          // arg is kind, NOT marker_kind
    "note":      "audio sync"      // optional
  } }
```

`kind` is a free-form string (convention: `issue` / `accept` / `revise` / `note`, default `review`). Stored as `<file>.bookmarks.json`.

### `video_subtitle_align`

Apply a global offset to a `.vtt` or `.srt` next to the video:

```jsonc
{ "tool": "htmlook_video_subtitle_align",
  "args": { "file_path": "/abs/clip.en.vtt", "offset_sec": -1.25 } }
```

`file_path` (not `subtitle_path`). The rewrite is **in-place** — no `.bak.<ts>` is written. Keep your own copy if you might need to revert.

### `video_scene_detect`

ffmpeg-driven scene detection:

```jsonc
{ "tool": "htmlook_video_scene_detect",
  "args": { "file_path": "/abs/clip.mp4", "threshold": 0.4, "limit": 100 } }
// → { count, scene_times_sec: [0.0, 8.2, 14.7, …] }
```

Default `threshold` 0.4 (higher = fewer scenes), default `limit` 100. Requires ffmpeg on PATH. If missing, returns a `DEPENDENCY_MISSING:` prefix error (and HTMLook surfaces a friendly toast to the user with a one-click install).

### `capture_video_frame_region`

Capture a sub-rectangle of a frame (or a specific time):

```jsonc
{ "tool": "htmlook_capture_video_frame_region",
  "args": {
    "file_path":      "/abs/clip.mp4",
    "timestamp_sec":  14.7,
    "rect":           { "x": 100, "y": 80, "w": 400, "h": 220 }
  } }
```

Returns the standard capture envelope (image content block + JSON sibling with `timestamp_sec` + `rect` flat).

## Patterns

- **Chapter from scenes**: `video_scene_detect` → for each cut, `video_chapter_create` with the title you generate from a frame capture (remember `end_sec` is required — use the next cut as the end).
- **Subtitle quality pass**: read subtitle file, capture frames at every cue start, summarise mismatch.
- **Memo digest**: `voice_workspace_all` → for each memo `audio_quote_extract({ query: "action item" })` → digest to ChatPanel via `chatpanel_post`.

## Next

- [Skill authoring →](AI-Skill-Authoring.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
