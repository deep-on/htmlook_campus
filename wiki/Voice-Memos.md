# Voice memos

> A microphone button in the status bar. AAC files in your workspace. Transcript next to each.

## Where the recorder lives

Bottom-right of the status bar: a microphone glyph. Click → recording starts, the glyph turns red, and a live audio-meter bar appears next to it showing input level.

Click again (or press the keyboard shortcut you bind in Settings) to stop. The file lands in `<workspace>/.htmlook-voice/` as `voice_<YYYYMMDD-HHMMSS>.m4a` (AAC).

## First time

macOS asks for microphone permission once per app. The system prompt explains the recording is local-only.

On M3+ MacBook Pro with the lid closed (clamshell mode) the **internal mic is digitally silent** — known macOS bug. Open the lid or pair an external mic. HTMLook detects zero-amplitude streams and surfaces a one-time warning toast.

## Playback player

The bottom-edge **Voice Player** appears whenever a `.m4a` file is selected in the sidebar, or whenever the workspace has memos and you haven't dismissed the player.

```
┌────────────────────────────────────────────────────┐
│  ▶  ◀ 1 / 5 ▶   memo_20260517-141900.m4a   00:42  │
│  ▁▂▅▆▇▆▅▃▁  ━━━━━━━●─────────────────  ⌃ ✏ ✕    │
└────────────────────────────────────────────────────┘
```

- ◀ / ▶ navigate through the workspace's memos
- Waveform shows the loudness envelope
- ⌃ collapses the player (lives as a single ▶︎ button with a badge until expanded again)
- ✏ rename, ✕ delete

## Transcript

If you've transcribed a memo, a `<file>.m4a.transcript.json` sibling is created next to it. The player shows the transcript inline with timecodes; clicking a sentence seeks playback there.

You can transcribe via:

- An MCP-tool agent (Claude / Codex / Gemini etc.) calling `htmlook_voice_transcript_set`
- A skill you wrote that posts the transcript JSON
- Manual paste from your own STT tool

There is no built-in STT engine. Voice files are yours to process — local Whisper, an API, or a paid service like ElevenLabs Voice all work.

## Drag-out

Drag a memo from the sidebar into Finder, Mail, Slack, or Notion. The drag carries the .m4a path — drop into Mail to attach.

## Search

`htmlook_voice_search` searches transcripts (when present) for a query and returns the matching memos with timecodes. Surfaces in the *Search workspace* pane (⌘⇧F).

## MCP-exposed tools

- `htmlook_voice_record_start` / `htmlook_voice_record_stop`
- `htmlook_voice_list` / `htmlook_voice_workspace_all`
- `htmlook_voice_get_bytes` — base64 of the file
- `htmlook_voice_rename` / `htmlook_voice_delete`
- `htmlook_voice_transcript_get` / `htmlook_voice_transcript_set`
- `htmlook_voice_search`
- `htmlook_audio_segment_create` / `htmlook_audio_quote_extract` / `htmlook_audio_waveform_get`

See [AI Audio / Video Tools](AI-Audio-Video-Tools.md).

## Privacy

Voice files never leave the workspace folder by themselves. Anything you do with them — transcribing, sending to a chat — is your explicit action. The mic glyph turns red while recording so you always know.

## Next

- [Skills →](Skills.md)
- [Settings →](Settings.md)
