# recipe-card — HTMLook + LLM + recipe layout (portrait 9:16)

A 15-second polished **portrait 9:16** recipe card teaser, generated
end-to-end through the same HTMLook workflow you use for landscape
personas. The artifact is a 1080×1920 single-page recipe card —
header, ingredients list, 4 numbered steps, footer wordmark.

## What you get

- `index.html` — the completed 15 s **portrait** teaser (header
  with tomato time pill, ingredient list reveal, 4 step icons
  stagger, "RecipeCards · 1인분" wordmark).
- `prompts.txt` — five English prompts to feed your LLM.
- `brand.txt` — the RecipeCards 2026 palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Try it

Open this folder as a workspace in **HTMLook Pro**, fire your LLM
of choice, paste the [1] prompt from `prompts.txt`, and watch the
card author itself top-to-bottom. The right pane preview is 9:16
letterboxed inside HTMLook's 16:9 layout.

## Why portrait?

- Mobile-first cooking — phones live on the kitchen counter.
- Instagram / Threads inline render 9:16 better than 16:9.
- Ingredients + steps fit one fullscreen scroll on a phone.

## Why HTMLook?

The same MCP that powers the landscape personas powers this — the
only difference is `data-width="1080" data-height="1920"` and the
right pane is letterboxed. **HTMLook is the workflow hub. Bring
your own format.**
