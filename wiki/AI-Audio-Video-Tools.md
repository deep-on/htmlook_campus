# Audio / video tools

> Voice memos, transcript search, video chapters, scene detection, frame capture, subtitle align.

## Voice memo recording

You can drive the workspace's mic recorder programmatically:

```jsonc
{ "tool": "htmlook_voice_record_start" }
// … later …
{ "tool": "htmlook_voice_record_stop" }
```

Returns the file path. `voice_list` enumerates `.htmlook-voice/` memos. `voice_get_bytes` returns the file as base64 for upload to a STT provider you run.

The clamshell-mode silent-mic bug on M3+ MacBook Pro is detected automatically — the start call will surface a warning if zero amplitude is sustained.

## Transcript sidecars

`voice_transcript_set` writes `<file>.m4a.transcript.json`:

```jsonc
{
  "tool": "htmlook_voice_transcript_set",
  "args": {
    "file_path": "voice_2026-05-17.m4a",
    "transcript": {
      "segments": [
        { "start_sec": 0.0, "end_sec": 2.4, "text": "안녕하세요" },
        { "start_sec": 2.4, "end_sec": 5.1, "text": "오늘 회의는 …" }
      ],
      "language": "ko",
      "provider": "whisper-large-v3"
    }
  }
}
```

The voice player picks it up immediately and shows clickable transcript lines synced to playback.

## audio_quote_extract

Search a transcript for time-anchored snippets:

```jsonc
{ "tool": "htmlook_audio_quote_extract",
  "args": { "file_path": "voice.m4a", "query": "회의실 예약", "limit": 5 } }
```

Returns matching segments with timecodes, so you can quote them back at the user with a link that seeks.

## audio_segment_create

Add a labelled segment marker. Stored as `<file>.segments.json`:

```jsonc
{ "tool": "htmlook_audio_segment_create",
  "args": {
    "file_path": "voice.m4a",
    "start_sec": 12.3,
    "end_sec":   45.0,
    "label":     "Q1 review section",
    "color":     "#ffc107"
  } }
```

Useful for "split a 1-hour memo into 5 chunks" workflows.

## audio_waveform_get

```jsonc
{ "tool": "htmlook_audio_waveform_get",
  "args": { "file_path": "voice.m4a", "bin_count": 256 } }
```

Returns a list of `bin_count` loudness values (0..1) decoded via Web Audio. Cheap; use it to draw a thumbnail or detect quiet sections.

## Video

### `video_info`

```jsonc
{ "tool": "htmlook_video_info", "args": { "file_path": "clip.mp4" } }
// → { "duration_sec": 142.5, "width": 1920, "height": 1080, "codec": "h264", "fps": 30 }
```

### `video_position`, `video_seek`

Read or set the playhead of the active video viewer.

### `video_chapter_create`

Add a chapter. Stored as `<file>.chapters.json` (sorted by `start_sec`):

```jsonc
{ "tool": "htmlook_video_chapter_create",
  "args": { "file_path": "clip.mp4", "start_sec": 0,
            "title": "Intro", "color": "#22d3ee" } }
```

### `video_review_marker_add`

Add a single-point marker for review:

```jsonc
{ "tool": "htmlook_video_review_marker_add",
  "args": { "file_path": "clip.mp4", "time_sec": 73.4,
            "marker_kind": "issue", "note": "audio sync" } }
```

Marker kinds: `issue`, `accept`, `revise`, `note`. Stored as `<file>.bookmarks.json`.

### `video_subtitle_align`

Apply a global offset to a `.vtt` or `.srt` next to the video. Useful when subtitles drift:

```jsonc
{ "tool": "htmlook_video_subtitle_align",
  "args": { "subtitle_path": "clip.en.vtt", "offset_sec": -1.25 } }
```

In-place rewrite, original kept as `.bak.<ts>`.

### `video_scene_detect`

ffmpeg-driven scene detection:

```jsonc
{ "tool": "htmlook_video_scene_detect",
  "args": { "file_path": "clip.mp4", "threshold": 0.3, "limit": 50 } }
// → { "count": 12, "scene_times_sec": [0.0, 8.2, 14.7, …] }
```

Requires ffmpeg on PATH. If missing, returns a `DEPENDENCY_MISSING:` error (and HTMLook surfaces a friendly toast to the user with a one-click brew install).

### `capture_video_frame_region`

Capture a sub-rectangle of the current frame (or a specific time):

```jsonc
{ "tool": "htmlook_capture_video_frame_region",
  "args": {
    "file_path": "clip.mp4",
    "time_sec": 14.7,
    "rect": { "x": 100, "y": 80, "w": 400, "h": 220 }
  } }
```

Returns the standard PNG envelope. Cheaper than re-encoding a clip — perfect for "what was on screen at second 14.7".

## Patterns

- **Chapter from scenes**: `video_scene_detect` → for each cut, `video_chapter_create` with the user-friendly title you generate from a frame capture
- **Subtitle quality pass**: read subtitle file, capture frames at every cue start, summarise mismatch
- **Memo digest**: `voice_workspace_all` → for each memo `audio_quote_extract({ query: "action item" })` → digest to ChatPanel

## Next

- [Skill authoring →](AI-Skill-Authoring.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
