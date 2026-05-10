# kids-science-mag — HTMLook + LLM (Wonder Lab Kids monthly page)

A 15-second polished **portrait 9:16** Wonder Lab Kids magazine page
teaser, generated end-to-end through the same HTMLook workflow you use
for every other persona.  The artifact is a 1080×1920 single-page
magazine card stacked into four sections: masthead with the cover
question, a yellow curiosity bubble, a 3-step experiment row, and an
answer + vocabulary glossary line.

This is the **second portrait persona** (after `economy-analyst`).
The HTMLook workflow stays landscape — the dual pane is 16:9 — but the
artifact shipped on the right pane is 9:16 portrait, perfect for a
school newsletter or a Substack Kids subscriber feed.

## What you get

- `index.html` — the completed 15 s **portrait** teaser (Wonder Lab
  Kids Issue #15, "왜 비누 거품은 둥글까?", four-scene reveal: cover
  → bubble → 3-step row → answer + glossary).  Open it in HTMLook to
  see the full result.  Root composition is `data-width="1080"
  data-height="1920"`.
- `prompts.txt` — five English prompts to feed your LLM (Claude /
  local Llama / GPT — whichever you have wired through HTMLook MCP).
- `brand.txt` — the Wonder Lab Kids palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Setup (one-time)

You need any LLM that speaks the HTMLook MCP.  If you already wired
Claude or a local Llama for `hf-claude` / `hf-llama`, you're done —
this scenario uses the same MCP, just authoring a magazine portrait
composition with a different palette.

```bash
# Pick your LLM. Examples:
#   Anthropic API:   export ANTHROPIC_API_KEY=sk-ant-...
#   Local Llama:     ollama pull llama3.2 && ollama serve &
#   OpenAI / Codex:  set up your terminal of choice
```

## Try it

Open this folder as a workspace in **HTMLook Pro**.  The sidebar
should show a HyperFrames banner with one composition.  Drop a short
adult-level science paragraph into a `science-paragraph.md` file in
this folder, then in the bottom terminal fire your LLM and paste the
[1] prompt from `prompts.txt`:

```text
Cite paragraph 1 of science-paragraph.md and rephrase it for a
9-year-old reader as a Wonder Lab Kids portrait page (1080×1920).
Masthead "Wonder Lab Kids · Issue #15" with the cover question "왜
비누 거품은 둥글까?", a yellow curiosity-bubble one-sentence hook,
a 3-step experiment row, and a vocabulary glossary chip for
"표면장력".
```

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the dual-pane state (left =
   `science-paragraph.md`, right = `wonder-lab-page.html` empty 9:16
   scaffold)
2. Call `htmlook_cite` to anchor the cited adult paragraph
3. Call `htmlook_apply_edit` to drop in the masthead + cover question
4. Apply the curiosity bubble (yellow card, one-sentence hook)
5. Apply the 3-step experiment row (orange step-number pills)
6. Apply the answer + glossary chip last
7. Wait for `npx hyperframes preview` hot-reload to land each section
8. Run `npx hyperframes lint && npx hyperframes render` to ship the mp4

When the render lands, the right pane plays back the 9:16 magazine
page **letterboxed** — HTMLook's preview pane is landscape, so the
portrait artifact sits centered with dark side bands.  That's
intentional — kids who tap the page on a phone see it fullscreen, you
author it on your desktop.

## Refinement loop (this is where HTMLook earns its keep)

Pause the right pane on the glossary chip.  Reading the "표면장력"
definition, you realise it's still too academic for a 9-year-old.
Cite the chip with `htmlook_cite`, then ask the LLM:

```text
The "표면장력" definition is still too academic.  Rewrite it as a
single sentence using the words "물 표면" and "끌어당겨서".  Keep
the chip layout, the cobalt term color, and the ink definition.
```

The LLM re-edits, HF re-renders, the right pane reloads.  **Same
core HTMLook moves as in `economy-analyst`:** dual-pane MCP, cite,
apply_edit, auto-reload.  The only thing that changed is the
artifact's audience and palette.

## Why portrait?

- Kids read fullscreen on a tablet or a parent's phone — no awkward
  letterbox, no zoom-and-pan.
- A school newsletter inlines 9:16 better than 16:9.
- The cover question gets the entire top third — readers see the
  hook before they read the answer.

## Why HTMLook?

The same MCP that powers every other persona unit powers this — the
only difference is the palette and the audience.  Run all the
portrait personas side by side and you'll see HTMLook's dual-pane
workflow is **audience-agnostic**.  **HTMLook is the workflow hub.
Bring your own LLM, your own palette, your own readers.**
