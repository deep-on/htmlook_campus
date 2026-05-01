# economy-analyst — HTMLook + LLM + chart libs (portrait macro briefs)

A 15-second polished **portrait 9:16** macro brief teaser, generated
end-to-end through the same HTMLook workflow you use for the
landscape personas. The artifact is a 1080×1920 single-page report
card stacked into four sections: hook number, small chart, three
take-aways, source/footer wordmark.

This is the **first portrait persona**. The workflow stays
landscape (HTMLook's dual pane is 16:9), but the artifact shipped on
the right pane is 9:16 — perfect for Substack, Threads, Instagram.

## What you get

- `index.html` — the completed 15 s **portrait** teaser ("Macro Brief #34", deep navy + gold, three-bullet reveal). Open it in HTMLook to see the full result. Root composition is `data-width="1080" data-height="1920"`.
- `prompts.txt` — five English prompts to feed your LLM (Claude / Llama / GPT — whichever you have wired through HTMLook MCP).
- `brand.txt` — the fictional Macro Brief 2026 palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Setup (one-time)

You need any LLM that speaks the HTMLook MCP. If you already wired
Claude or a local Llama for `hf-claude` / `hf-llama`, you're done —
this scenario uses the same MCP, just authoring a portrait
composition instead of landscape.

```bash
# Pick your LLM. Examples:
#   Anthropic API:   export ANTHROPIC_API_KEY=sk-ant-...
#   Local Llama:     ollama pull llama3.2 && ollama serve &
#   OpenAI / Codex:  set up your terminal of choice
```

## Try it

Open this folder as a workspace in **HTMLook Pro**. The sidebar
should show a HyperFrames banner with one composition. Then in the
bottom terminal, fire your LLM of choice and paste the [1] prompt
from `prompts.txt`:

```text
Draft this week's CPI brief. One hook number, one bar chart of the
last six prints, three take-away bullets, and a source link at the
footer. Portrait 1080×1920, navy+gold palette per brand.txt.
```

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the dual-pane state (left=`draft.md`, right=`portrait_report.html` empty 9:16 scaffold)
2. Call `htmlook_apply_edit` to drop in the hook number section first
3. Apply the chart section (bars + axis labels)
4. Apply the three bullets one-by-one
5. Apply the source/footer line last
6. Wait for `npx hyperframes preview` hot-reload to land each section
7. Run `npx hyperframes lint && npx hyperframes render` to ship the mp4

When the render lands, the right pane plays back the 9:16 teaser
**letterboxed** — HTMLook's preview pane is landscape, so the
portrait artifact sits centered with dark side bands. That's
intentional — readers who tap it on a phone see the artifact
fullscreen; you author it on your desktop.

## Refinement loop (this is where HTMLook earns its keep)

Pause the right pane. Reading the bullets, you realise the ranking
is wrong — the strongest take-away should come first, not last.
Cite the bullet block range with `htmlook_cite`, then ask the LLM:

```text
Reorder the three bullets — strongest first, weakest last. Same
copy, same source line. Cite the bullet range I just selected.
```

The LLM re-edits, HF re-renders, the right pane reloads. **Same
core HTMLook moves as in `hf-claude` / `hf-llama`:** dual-pane MCP,
cite, apply_edit, auto-reload. The only thing that changed is the
artifact's aspect ratio.

## Why portrait?

- Mobile-first readers see the brief fullscreen — no awkward
  letterbox on a phone, no zoom-and-pan.
- Threads / Instagram / Substack inline render 9:16 better than
  16:9.
- The hook number gets the entire top third — readers see the print
  before they read a word.

## Why HTMLook?

The same MCP that powers `hf-claude` and `hf-llama` powers this —
the only difference is `data-width="1080" data-height="1920"`. Run
all three side by side and you'll see HTMLook's dual-pane workflow
is **aspect-ratio-agnostic**. **HTMLook is the workflow hub. Bring
your own format.**
