# finance-report — HTMLook + LLM for the cell-cite to narrative

A 15-second polished "CFO brief page" teaser that demonstrates the
**financial analyst** workflow: keep an open `.xlsx` model on the
left pane and the `report.html` exec-summary draft on the right pane
while asking an LLM to cite a cell, narrate the variance, and apply
the edit to the report.

The fictional company is **Atlas Manufacturing**. The document under
construction is the **Q3 2026 CFO Brief**.

## What you get

- `index.html` — the completed 15-s "CFO brief page" teaser.
  Corporate-navy background with gold highlights, alert-orange for
  negative variance, soft cream body. Four scenes: report title
  pulses on, three variance rows reveal one by one with arrows and
  narrative one-liners, footer sign-off rises, "CFO Brief"
  wordmark + URL dissolves in.
- `prompts.txt` — five English LLM prompts for the cell-cite
  workflow (cite a cell, narrate the variance, apply edit to the
  report, sweep cross-tab, draft a recommendation block).
- `brand.txt` — the Atlas Manufacturing palette + corporate-finance
  copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a financial analyst on a corporate finance team turning a
quarterly model into an exec summary the CFO will actually sign.
Without HTMLook this is Excel, a Word doc or HTML draft, and a lot
of switching back and forth to remember which cell drove which
sentence. With HTMLook:

1. Open the workspace. **Left pane = `q3_model.xlsx`** showing the
   variance tab (a faux table view: row labels + actual / plan /
   delta columns across multiple sub-tabs). **Right pane =
   `report.html`** — the exec summary draft. The sidebar shows the
   workbook tabs (Revenue, COGS, OpEx, EBITDA, Variance) and the
   report sections.
2. Ask the LLM in the bottom terminal:
   *"Cite EBITDA!B14 and narrate the variance vs plan."*
   The LLM calls `htmlook_cite("left", "EBITDA!B14")`, reads the
   cell value and its plan reference, and writes a one-sentence
   board-ready narrative ("Q3 EBITDA vs plan: -$2.1M, driven by
   higher input costs in the Castings line ...").
3. Pause on the narrative. Ask the LLM to **apply edit** to the
   report — insert the paragraph under the matching section heading
   in `report.html`. The right pane reloads with the new paragraph
   highlighted.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real
xlsx at `q3_model.xlsx` and an HTML draft at `report.html`, then
attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama
via Ollama, Gemini, GPT, etc.). Drop the `[1]` prompt from
`prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the model (left) and the report
   (right).
2. Call `htmlook_active_file` → identify the open tab and the
   active section.
3. Call `htmlook_cite("left", "EBITDA!B14")` to anchor the cell
   in the model.
4. Call `htmlook_apply_edit` to insert the narrative paragraph
   into `report.html` under the matching section.
5. Hot-reload kicks in — the right pane re-renders the patched
   report and you visually confirm.

## Why this matters

Corporate finance briefs ship every quarter, and the bottleneck is
not the model — it's turning forty cells into ten signed sentences
that a board can read. HTMLook puts the model and the draft on
screen at the same time, and lets the LLM anchor the cell that
produced the sentence at the moment of writing. Audit-ready, no
copy-paste, no "wait, where did that number come from?".

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and `dev-pr-docs`
(dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too —
except the left pane is now an `.xlsx` cell and the right pane is
an HTML draft, and the artifact is a board-ready brief page instead
of an mp4 or a docs patch. **Same primitives, new craft.**
