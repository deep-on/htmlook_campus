# creator-podcast — HTMLook + Whisper + Claude (viral-clip pipeline)

A 15-second polished podcast clip teaser, generated end-to-end from a
long-form recording. The point: **HTMLook keeps the waveform +
transcript on the left and the kinetic-caption clip on the right** so
you can pull a 30-60 s viral moment without leaving the editor.

## What you get

- `index.html` — the completed 15 s teaser ("Workflow Cast", warm
  purple → magenta, kinetic pull-quote, host avatar + episode
  wordmark). Open it in HTMLook to see the full result.
- `prompts.txt` — five English LLM prompts to drive the workflow,
  from the basic ask to refinement variants.
- `brand.txt` — the fictional Workflow Cast palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Setup (one-time)

```bash
# 1. Install Whisper (or use HyperFrames built-in transcribe)
pip install -U openai-whisper
# 2. Verify
whisper --help
```

You can also skip the install and let `npx hyperframes transcribe`
handle it — same word-level timestamps.

## Try it

Drop your long-form podcast MP3 (1–2 h is fine) into `assets/`.
Open this folder as a workspace in **HTMLook Pro**. The sidebar
should show a HyperFrames banner with one composition.

```bash
# Transcribe the long-form recording (word-level timestamps)
npx hyperframes transcribe assets/episode.mp3 -o transcript.json

# Then in the bottom Claude tab, paste the [1] prompt from prompts.txt
```

With the HTMLook MCP attached, Claude will:

1. Call `htmlook_pane_pair` → see the dual-pane state (left=transcript+waveform, right=clip.html template).
2. Read `transcript.json` and pick the most quotable 20-s moment.
3. Call `htmlook_apply_edit` to insert the kinetic-caption scenes into `index.html` with the cited transcript range.
4. Wait for `npx hyperframes preview` hot-reload to land each version on the right pane.
5. Run `npx hyperframes lint && npx hyperframes render` for the final mp4.

When the render lands in `renders/index.mp4`, the HTMLook sidebar
banner flips from `watching…` to `rendered 1/1` and the right pane
**auto-reloads** to play the v1 clip.

## Refinement loop (where HTMLook earns its keep)

Pause the right pane, hear a word that lands a beat off-cadence. Use
`htmlook_cite` with a time range or a transcript word id, then ask
the LLM:

```text
The right-pane clip @ 0:11 — the word "moat" stutters in too fast.
Cite transcript words 8 to 14 and retime the kinetic stagger from
0.06 to 0.11 so "moat" lands on the beat. Same 20-s window.
```

The LLM re-edits, HF re-renders, the right pane reloads. **Same four
HTMLook moves as in hf-claude / hf-llama:** dual-pane MCP, cite,
apply_edit, auto-reload.

## TTS + alignment (optional polish)

If you want a pull-quote voiceover instead of the host's recorded
audio, add a Kokoro TTS pass and re-align with Whisper:

```bash
npx hyperframes tts pull_quote.txt -o assets/quote_tts.mp3
npx hyperframes transcribe assets/quote_tts.mp3 -o transcript.tts.json
npx hyperframes render --audio assets/quote_tts.mp3
```

The kinetic captions snap to the new timestamps automatically.

## Why HTMLook for podcast clips?

- The dual-pane keeps the **source transcript** and the **clip output**
  side by side — no swapping between Descript and a video editor.
- `htmlook_cite` produces an exact transcript word range that the LLM
  can read back, so retimes are deterministic instead of vibes.
- `bring your own LLM` — Claude, Llama, GPT, anything with the
  HTMLook MCP. The four moves are LLM-agnostic.

Run `creator-podcast`, `hf-claude`, and `hf-llama` side by side —
identical HTMLook moves, three different domains. **HTMLook is the
hub. The clip is the artifact.**
