# press-editor — HTMLook + LLM for editorial quote-citing by timestamp

A 15-second polished tear-sheet that demonstrates the **journalism / trade-press editor** workflow: keep an interview audio + word-level transcript on the left pane and the article draft `.md` on the right, then ask an LLM to cite a quote-range by timestamp, paraphrase or pull the verbatim quote, and apply the edit. The right pane reloads with the polished paragraph.

The fictional publication is **Workflow Magazine** — a print-flavoured editorial outlet whose Issue 47 cover story, *"The AI Moat Isn't the Model"*, is being filed.

## What you get

- `index.html` — the completed 15-s polished tear-sheet. Sepia paper background, deep ink, burgundy and olive editorial accents. Four scenes: publication header reveal, headline + byline kinetic typography, pull-quote serif slow reveal, filed-to-print colophon with issue stamp.
- `prompts.txt` — five English LLM prompts: one for the main "quote cite by timestamp" move, one for "paraphrase a quote", plus three follow-ups (verbatim pull, fact-check sweep, fix attribution).
- `brand.txt` — the Workflow Magazine palette + editorial copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a journalist or trade-press editor on a tight close. Your interview is a 22-minute mp3 with a Whisper word-level `transcript.json`. Your draft is a `.md` file. Without HTMLook you would scrub the audio in one app, copy quotes from another, and paste into your editor — losing the exact timestamp every time. With HTMLook:

1. Open the workspace. **Left pane = `interview.mp3` + `transcript.json`** (waveform with word-level highlights). **Right pane = `article.md`** (rendered draft). The sidebar lists the assignment, the source files, and any prior cite anchors.
2. Ask the LLM in the bottom terminal: *"Find the strongest quote about commoditised models between 12 and 16 minutes."* The LLM calls `htmlook_cite("left", "14:14-14:34")` and returns the verbatim quote with its time-range pinned.
3. Ask the LLM to **paraphrase or pull the verbatim quote** into the draft at a specific section. The LLM calls `htmlook_apply_edit` on `article.md`. The right pane reloads with the polished paragraph and the cite-anchor recorded inline.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Drop a real `interview.mp3` plus a Whisper-aligned `transcript.json` next to a working `article.md`, then attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama via Ollama, Gemini, GPT). Drop the `[1]` prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the audio + transcript on the left and the article markdown on the right.
2. Call `htmlook_cite("left", "14:14-14:34")` to anchor the spoken quote-range by timestamp.
3. Decide between a verbatim pull and a paraphrase, depending on the section's voice.
4. Call `htmlook_apply_edit` to insert the polished paragraph into `article.md` with the timestamp recorded inline as a cite anchor.
5. Hot-reload kicks in — the right pane re-renders the article and you scan the polished paragraph in print preview.

## Why this matters

Editors lose hours scrubbing audio for "the right quote" and then transcribing it with a different timestamp than the one they cited in their notes. HTMLook keeps the audio, the word-level transcript, and the live draft on one screen, and lets the LLM pin the exact range so the cite never drifts between revisions.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too — except the left pane is now an interview audio + transcript instead of a code diff, and the artifact is a polished article paragraph instead of a docs patch. **Same primitives, new craft.**
