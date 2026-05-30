# research-notes — HTMLook + LLM for the academic section dive

A 15-second polished "research note page" teaser that demonstrates the
**academic researcher** workflow: keep an open paper PDF on the left
pane and a personal `notes.md` on the right pane while asking an LLM
to cite a paragraph, summarize the finding, and append a clean
bibliography entry.

The fictional notebook is **Apparatus Notes**. The paper under review
is Chen et al. 2026 — *"Sparse Cross-Modal Attention for Long-Context
Vision-Language Models"* (a NeurIPS-style ML paper).

## What you get

- `index.html` — the completed 15-s "research note page" teaser. Warm
  parchment background, deep slate body, citation purple for `[1][2][3]`
  markers, link cyan for DOIs. Four scenes: paper title fades up,
  three key-finding rows stagger in, bibliography slides in from
  below, "Apparatus Notes" wordmark dissolves over the page.
- `prompts.txt` — five English LLM prompts for the section dive
  (cite paragraph, summarize finding, append bibliography, suggest
  connecting reference, sweep next section).
- `brand.txt` — the Apparatus Notes palette + scholarly copy
  guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a working researcher (PhD student, postdoc, or industry
research engineer) reading a paper that you actually need to remember
and connect to your own bibliography. Without HTMLook this is a PDF
viewer, a markdown editor, a separate citation manager, and a lot of
copy-paste. With HTMLook:

1. Open the workspace. **Left pane = `paper.pdf`** scrolled to a
   section like Methods §3.2 or Results §4.1. **Right pane =
   `notes.md`** with your running extraction (key findings, citation
   keys, personal bibliography). The sidebar shows the paper's
   sections and your notes file tree.
2. Ask the LLM in the bottom terminal:
   *"Cite the methods paragraph that introduces sparse cross-modal
   attention and summarize it in one sentence."* The LLM calls
   `htmlook_cite("left", "p4 §3.2")`, reads the paragraph, and writes
   a one-sentence summary plus a citekey suggestion.
3. Pause on the summary. Ask the LLM to **apply edit** to the notes —
   append the finding under a `## Findings` heading and add a
   bibliography entry under `## Bibliography` with the DOI. The right
   pane reloads with the new lines highlighted.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real PDF
at `paper.pdf` and a notes file at `notes.md`, then attach the
HTMLook MCP to your LLM of choice (Claude, Codex, Llama via Ollama,
Gemini, GPT, etc.). Drop the `[1]` prompt from `prompts.txt` into
the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the paper (left) and the notes
   (right).
2. Call `htmlook_active_file` → identify which pane and what page
   the reader is on.
3. Call `htmlook_cite("left", "p4 §3.2 ¶2")` to anchor the methods
   paragraph in the paper.
4. Call `htmlook_apply_edit` to insert the finding row + bibliography
   entry into `notes.md`.
5. Hot-reload kicks in — the right pane re-renders the patched notes
   and you visually confirm.

## Why this matters

Researchers extract findings into private notes, but the link back to
the paragraph that produced the finding almost always rots. Two weeks
later you have a bullet point and no idea where it came from. HTMLook
keeps the paper and the notes on screen at the same time, and lets the
LLM anchor the cite at the moment of extraction — not as a
reconstruction afterward.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and `dev-pr-docs`
(dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too —
except the right pane is now `notes.md` instead of a video or doc
file, and the artifact is a published-looking research-note page
instead of an mp4 or a docs patch. **Same primitives, new craft.**
