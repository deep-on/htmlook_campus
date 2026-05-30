# teacher-quiz — HTMLook + LLM for chapter-to-quiz authoring

A 15-second polished "단원평가" teaser that demonstrates the
**middle-school English teacher** workflow: keep `chapter1.md` on the
left pane and `quiz.html` on the right pane while asking an LLM to
draft a unit-test paper from the chapter notes — multiple choice,
short answer, answer key, and a grading rubric — all on one printable
sheet.

The fictional school is **Seongsan Middle School**, Grade 2 English,
Unit 1 ("School Life"). The teaser preview shows the finished paper.

## What you get

- `index.html` — the completed 15-s "단원평가" teaser. Cream-paper
  background with school green and 칠판 ink. Four scenes: the test
  header (school + title + name boxes + 단원평가 stamp), 5 staggered
  multiple-choice items, 2 서술형 reveals with hand-drawn answer
  lines, and the answer-key + 채점 rubric card with the
  "단원평가 · 2026 1학기" watermark.
- `prompts.txt` — five English LLM prompts: one for "draft 5 MC + 2
  SA from the chapter", one for "tag difficulty + write rubric", plus
  three follow-ups.
- `brand.txt` — the seongsan-ms palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a middle-school English teacher writing the Unit 1 test the
night before printing day. Without HTMLook this is a chapter book on
your desk, a blank Word doc on screen, and a lot of typing the same
vocabulary three times. With HTMLook:

1. Open the workspace. **Left pane = `chapter1.md`** (vocabulary,
   grammar notes, example sentences). **Right pane = `quiz.html`**
   (empty test sheet). The sidebar shows the chapter source and the
   blank quiz output.
2. Ask the LLM in the bottom terminal: *"Read chapter1.md. Draft 5
   multiple choice and 2 short-answer items, with an answer key."*
   The LLM cites the vocab list and the grammar examples, then
   `apply_edit`s items 1-7 plus a separate answers file.
3. Pause. Ask the LLM to **refine the difficulty mix** (2 easy, 2
   medium, 1 hard) and **write a 3-level grading rubric**. Right pane
   reloads — difficulty tags appear next to each item, and an
   A / B / C rubric card lands at the bottom. Print.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Replace
`chapter1.md` with your own unit notes, attach the HTMLook MCP to
your LLM (Claude, Codex, Llama via Ollama, Gemini, GPT, etc.), and
drop the `[1]` prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. `htmlook_pane_pair` → see chapter notes (left) and the empty
   quiz (right).
2. `htmlook_active_file` → identify which file is in focus.
3. `htmlook_cite("left", "V1, G1, G2, E1")` to anchor the chapter
   sections that drive the items.
4. `htmlook_apply_edit` to insert the 7 items + answer key, and a
   second pass to add difficulty tags + the rubric.
5. Hot-reload kicks in — the right pane re-renders the patched quiz
   and you visually confirm before pressing print.

## Why this matters

Unit tests are the slowest part of teacher prep — vocabulary appears
three times, the answer key lives in a separate doc, and the grading
rubric is rebuilt every term. HTMLook puts the chapter and the test
on screen at the same time, so the LLM only writes from sources it
can cite.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs` (dual-pane MCP,
`cite`, `apply_edit`, auto-reload) work here too — except the right
pane is now a printable test sheet instead of a docs file, and the
artifact is a unit-test paper plus a rubric instead of a docs patch.
**Same primitives, new craft.**
