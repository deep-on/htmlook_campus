# corp-deck — HTMLook + LLM for section-to-slide deck authoring

A 15-second polished "Q3 review" deck teaser that demonstrates the
**quarterly presentation** workflow: keep the quarterly report on the
left pane and the slide deck on the right pane while asking an LLM to
turn one cited section of the report into one slide — with the
speaker notes appended in the same round trip.

The fictional company is **Apex Logistics Inc.** — a mid-market
logistics operator preparing the Q3 2026 CFO review.

## What you get

- `index.html` — the completed 15-s "Q3 review" deck teaser. Slate
  background with cobalt and emerald accents. Four scenes: title
  slide, KPI metric stagger, variance bar chart, "Next Quarter ·
  3 Actions" closing slide with company URL.
- `prompts.txt` — five English LLM prompts: section-to-slide,
  KPI extract, variance chart, speaker notes, next-quarter actions.
- `brand.txt` — the Apex Logistics palette + presentation
  guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a strategy manager preparing the CFO's Q3 deck. Without
HTMLook this is the report in one window, slides in another, speaker
notes in a third, and a lot of copy-paste-tidy. With HTMLook:

1. Open the workspace. **Left pane = `q3_report.md`** (sections:
   Executive Summary / KPIs / Variance / Risks / Next Quarter).
   **Right pane = `deck.html`** (a six-slide scaffold). The sidebar
   shows the deck slide list and `speaker_notes.md`.
2. Cite a section of the report in the bottom terminal:
   *"Take `## KPIs` and write slide 2 — title plus three bullets
   plus a chart placeholder. Append speaker notes for that slide."*
   The LLM cites the section, fills slide 2 in `deck.html`, and
   appends the matching paragraph to `speaker_notes.md` in the
   same call.
3. Repeat for each remaining section. Every cite triggers a
   multi-target `apply_edit` — slide HTML and speaker notes update
   together.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real
quarterly report at `q3_report.md` and a deck scaffold at
`deck.html`, then attach the HTMLook MCP to your LLM of choice
(Claude, Codex, Llama via Ollama, Gemini, GPT, etc.). Drop the
`[1]` prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the report (left) and the deck
   (right).
2. Call `htmlook_active_file` → identify which file is in focus.
3. Call `htmlook_cite("left", "q3_report.md#KPIs")` to anchor the
   cited section.
4. Call `htmlook_apply_edit` against `deck.html` AND
   `speaker_notes.md` in one round trip — slide markup goes to the
   deck, the matching prose goes to the notes file.
5. Hot-reload kicks in — the right pane re-renders the deck with
   the new slide and you visually confirm.

## Why this matters

Quarterly decks rot in the gap between the report and the slides.
Numbers drift, captions stale, speaker notes get re-written from
scratch the night before. HTMLook puts the source report and the
deck on screen together, and lets the LLM keep the two artefacts
in sync — one cite, one slide, one paragraph of notes, every time.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs` and
`product-prd` (dual-pane MCP, `cite`, `apply_edit`, auto-reload)
work here too — except the right pane is now a slide deck instead
of a wireframe, and the artefact is a slide plus speaker notes
instead of a docs patch. **Same primitives, new craft.**
