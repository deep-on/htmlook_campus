# picture-book — HTMLook + LLM for verse drafting in the same view

A 15-second pastel "spread teaser" that demonstrates the **picture-book
author** workflow: keep the verse manuscript on the left pane and the
spread layout (펼침면) on the right pane while asking an LLM to tune
the Korean rhythm and tighten the right-page caption.

The fictional title is **달팽이의 학교** (*Snail School*) — a
working draft, page 4 spread.

## What you get

- `index.html` — the completed 15-s spread teaser. Ivory paper
  background with mint, pink, and ink accents. Four scenes: title +
  byline, three-line verse stagger, watercolor placeholder reveal,
  page-turn wordmark close.
- `prompts.txt` — five English LLM prompts: one for "tune the rhythm",
  one for "shorten the caption", plus three follow-ups (illustration
  brief, page-pacing, next-page hook).
- `brand.txt` — the 달팽이의 학교 palette + verse guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a Korean picture-book author drafting one spread at a time.
Without HTMLook this is a manuscript file in one window, a layout
mock-up in another, and a lot of alt-tabbing while you count
syllables. With HTMLook:

1. Open the workspace. **Left pane = `book.md`** (page 4 stanza, three
   verse lines). **Right pane = `spread.html`** (16:9 spread mockup —
   left half is the same verse rendered in the handwriting font, right
   half is a watercolor illustration placeholder with a small caption
   underneath). The sidebar shows the manuscript files.
2. Ask the LLM in the bottom terminal:
   *"Cite line 2 — propose a four-syllable tweak that keeps the
   meaning."*
   The LLM cites the line, returns a unified diff. apply_edit. The
   right pane reloads — the spread renders with the new line.
3. Pause on the right-page caption. Ask the LLM to **soften it by one
   syllable**. The right pane reloads. Caption now reads "갓 핀
   민들레꽃" instead of "갓 핀 민들레".

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real
manuscript at `book.md` and a layout mockup at `spread.html`, then
attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama
via Ollama, Gemini, GPT, etc.). Drop the `[1]` prompt from
`prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the manuscript (left) and the
   spread (right).
2. Call `htmlook_active_file` → identify page 4 in focus.
3. Call `htmlook_cite("left", "L2")` to anchor the four-syllable
   verse line.
4. Call `htmlook_apply_edit` to insert the tweak.
5. Hot-reload kicks in — the right pane re-renders the spread and
   you visually confirm the rhythm.

## Why this matters

Korean picture-book verse lives or dies on syllable rhythm, and
illustrated spreads live or die on the relationship between the
verse and the picture. Both halves rarely sit on screen together.
HTMLook puts the manuscript and the spread side by side, and lets
the LLM count syllables and trace caption tightness without
breaking the page-spread frame.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude`, `hf-llama`, and
`dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`, auto-reload)
work here too — except the right pane is now a 16:9 picture-book
spread instead of a video or a docs file, and the artifact is a
tighter stanza instead of an mp4. **Same primitives, new craft.**
