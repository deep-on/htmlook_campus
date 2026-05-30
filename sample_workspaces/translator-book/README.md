# translator-book — HTMLook + LLM for paragraph-by-paragraph book translation

A 15-second polished bilingual book page that demonstrates the
**book / technical-doc translator** workflow: keep the source PDF on
the left pane and the target-language draft on the right pane, while
asking an LLM to translate paragraph-by-paragraph using
`htmlook_cite` and to splice the translation back in via
`htmlook_apply_edit`. The right pane auto-reloads after every pass.

The fictional book is **"Hammers, Nails, and Other Lies"** by
E. R. Halloran, published by **Maren & Vale Press** — the chapter
shown is *Chapter 3 · The Workshop*.

## What you get

- `index.html` — the completed 15-s polished bilingual book page.
  Warm cream background, deep ink, burgundy chapter rule. Four
  scenes: chapter header settle, English column reveal, Korean
  column reveal in matched paragraph order, page-flip outro.
- `prompts.txt` — five English LLM prompts: paragraph 1, 2, 3
  passes, plus footnote pass and consistency sweep.
- `brand.txt` — the Maren & Vale Press palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are translating a book chapter from English into Korean. The
source PDF is fixed; the target draft is yours to write. Without
HTMLook this is a PDF reader, a Word document, a glossary, and a
lot of alt-tabbing. With HTMLook:

1. Open the workspace. **Left pane = source `chapter-03.pdf`**
   (the English original, scrollable). **Right pane = target
   `chapter-03.ko.md`** (your Korean draft, rendered). The
   sidebar shows your footnote glossary and the project's
   style sheet.
2. Ask the LLM in the bottom terminal:
   *"Translate paragraph 1 of chapter 3 into Korean. Use
   htmlook_cite to read the exact source paragraph; preserve the
   author's voice; reuse glossary terms."*
   The LLM cites the paragraph on the left, drafts the Korean
   version, and shows it inline.
3. Approve. The LLM calls `htmlook_apply_edit` on
   `chapter-03.ko.md`. The right pane reloads with the new
   paragraph slotted in, matching the source line by line.
4. **Iterate.** Move to paragraph 2. Repeat. Then paragraph 3.
   Then footnotes. Each pass is a small, reviewable edit, not a
   one-shot translation of the whole chapter.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real
PDF at `chapter-03.pdf` and a draft at `chapter-03.ko.md`, then
attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama
via Ollama, Gemini, GPT, etc.). Drop the `[1]` prompt from
`prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the source PDF (left) and the
   draft markdown (right).
2. Call `htmlook_active_file` → identify which paragraph is in
   focus on the left.
3. Call `htmlook_cite("left", "p.47, ¶1")` to anchor the source
   paragraph being translated.
4. Call `htmlook_apply_edit` on `chapter-03.ko.md` with the new
   Korean wording at the matched offset.
5. Hot-reload kicks in — the right pane re-renders the patched
   draft and you read the bilingual page side by side.

## Why this matters

A book translator's hardest move is staying *inside* the source
voice while writing in the target language. PDF readers and word
processors split that move across two windows. HTMLook puts the
source paragraph and the target paragraph on screen at the same
time, lets the LLM trace the exact source span being translated,
and reloads the printed result so you can read both columns at
once — every time you commit a paragraph.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and
`dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`, auto-reload)
work here too — except the right pane is now a Korean book draft
instead of a docs file, and the artifact is a printed bilingual
page instead of a video. **Same primitives, new craft.**
