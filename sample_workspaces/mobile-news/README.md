# mobile-news — HTMLook + LLM + 4-card deck (portrait 9:16)

A 15-second polished **portrait 9:16** news card deck teaser,
generated end-to-end through the same HTMLook workflow you use for
landscape personas. The artifact is a 1080×1920 4-card deck —
TLDR, key data, quote pull, source/handle.

## What you get

- `index.html` — the completed 15 s **portrait** teaser (header
  + issue pill, TLDR card, quote pull card, source card, "Issue
  47 · @workflowmag" wordmark).
- `prompts.txt` — five English prompts to feed your LLM.
- `brand.txt` — the WorkflowMag 2026 palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Try it

Open this folder as a workspace in **HTMLook Pro**, fire your LLM
of choice, paste the [1] prompt from `prompts.txt`, and watch all
four cards author themselves with one multi-target apply_edit. The
right pane preview is 9:16 letterboxed inside HTMLook's 16:9
layout.

## Why portrait?

- Threads / X / Substack inline render 9:16 better than 16:9.
- A 1500-word article doesn't fit a phone — but four cards do.
- The headline + TLDR fit one fullscreen on a phone, source on
  the next swipe.

## Why HTMLook?

The same MCP that powers the landscape personas powers this — the
only difference is `data-width="1080" data-height="1920"` and the
right pane is letterboxed. **HTMLook is the workflow hub. Bring
your own format.**
