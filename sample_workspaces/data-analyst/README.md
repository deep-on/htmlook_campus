# data-analyst — HTMLook + LLM for iterative SQL analysis

A 15-second polished "insight card" that demonstrates the **working
analyst** workflow: keep `query.sql` open on the left pane and the
chart it produces on the right pane while asking an LLM to cite a
column, change an aggregation, and watch the chart redraw.

The fictional product is **Pulse Analytics** — a SaaS metrics
dashboard whose April board number is "MRR up 18% MoM, driven by the
enterprise tier."

## What you get

- `index.html` — the completed 15-s insight-card teaser. Dark navy
  background, electric cyan primary, lime annotations. Four scenes:
  hook insight number, bar chart fill + annotation, three supporting
  metrics, brand outro.
- `prompts.txt` — five English LLM prompts: cite a SQL column, add a
  tier breakdown, weight an average by ACV, annotate the chart, and
  narrate the insight.
- `brand.txt` — the Pulse Analytics palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a working analyst at a SaaS company. The board needs an
April readout. Without HTMLook this is the SQL tab in one window and
the chart preview in another, with constant context-switches. With
HTMLook:

1. Open the workspace. **Left pane = `query.sql`** (color-coded
   keywords + identifiers). **Right pane = the chart** (an inline
   responsive bar/line chart of a few hundred data points). The
   sidebar shows the saved queries and the current dataset.
2. Ask the LLM in the bottom terminal:
   *"Cite the `tier` column in the SELECT and add a per-tier
   breakdown."* The LLM cites the column, patches the query, and
   the right pane auto-reloads with the new chart.
3. Spot a row outlier. Ask the LLM to **switch to a weighted
   average by ACV**. Apply edit. The right pane redraws and the
   annotation moves with it.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real SQL
file at `query.sql` and a rendered chart at `chart.html`, then attach
the HTMLook MCP to your LLM of choice (Claude, Codex, Llama via
Ollama, Gemini, GPT, etc. — HTMLook is LLM-agnostic). Drop the `[1]`
prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the SQL (left) and the chart
   (right).
2. Call `htmlook_active_file` → identify which query is in focus.
3. Call `htmlook_cite("left", "L7-L12")` to anchor the SELECT
   clause it wants to change.
4. Call `htmlook_apply_edit` to patch the query.
5. Hot-reload kicks in — the right pane re-renders the chart from
   the new query and you visually confirm.

## Why this matters

SQL iteration is a tight feedback loop. A column rename, an extra
GROUP BY, a weighted average — each one wants to land in seconds,
not minutes. Putting the query and its chart on screen at the same
time, and letting the LLM cite a column or a row, collapses the loop
to a single keystroke.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs`, `hf-claude`
and `hf-llama` (dual-pane MCP, `cite`, `apply_edit`, auto-reload)
work here too — except the right pane is now a chart instead of a
docs file or a video, and the artifact is a patched query instead of
a docs patch or an mp4. **Same primitives, new craft.**
